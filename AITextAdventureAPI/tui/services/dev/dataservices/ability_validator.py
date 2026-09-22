"""
Ability integrity validator.

Structural rules
----------------
A1  ABILITY_UNKNOWN_TYPE       ability_type not in recognised set
A2  ABILITY_UNKNOWN_EFFECT     effect not in recognised set
A3  ABILITY_DAMAGE_NO_POWER    effect=damage but base_power == 0
A4  ABILITY_HEAL_NO_POWER      effect=heal but base_power == 0
A5  ABILITY_STATUS_NO_KEYS     effect=status/cure but status_keys is empty
A6  ABILITY_NO_ELEMENTS        damage/status/heal ability has no elements  (warning)
A7  ABILITY_UNKNOWN_ELEMENT    an element in 'elements' is not in ELEMENTAL_CHAR_KEYS
A8  ABILITY_UNKNOWN_STATUS     a key in 'status_keys' is not in STATUS_EFFECTS
A9  ABILITY_STATUS_THIN        effect=status/cure but the summed status weight
                               is below the gently-scaling level floor
                               (6 + (level-1)*3)  (warning)
A10 ABILITY_TOO_FEW_ELEMENTS   an ability has fewer elements than its level
                               (level 4 requires at least 4 elements)

Status weighting
----------------
Statuses vary enormously in combat impact — a permanent ``petrify`` is worth
far more than an incremental ``intelligence_debuff``.  ``_status_weight`` maps
each status key to a relative weight so that both the total_value balance
score and the A9 thin-check reflect real power rather than a raw key count.
A single strong status can satisfy a level's expected weight, while weaker
stat buffs/debuffs must be stacked to reach the same target.

Balance rules  (warning — mirrors equipment TP balance check)
---------------
B1  ABILITY_BALANCE_WEAK       total_value < 65% of group average
B2  ABILITY_BALANCE_STRONG     total_value > 145% of group average
B3  ABILITY_AP_MISPRICED       value-per-AP efficiency falls outside the healthy
                               band (70%–140%) around the *per-effect* median
                               efficiency  (warning)
B4  ABILITY_STATUS_DENSITY     effect=status but < 50% of payload comes from the
                               statuses it applies (flat power dominates) (warning)
B5  ABILITY_SUPPORT_EFFICIENCY heal/revive/cure value-per-AP outside the band
                               around the combined support median  (warning)
B6  ABILITY_AOE_PREMIUM        AOE ability not costing more AP than single-target
                               peers, or vice versa  (warning)
B7  ABILITY_PROGRESSION_BREAK  a higher-level ability's payload falls below the
                               data-derived floor of the tiers below it  (error)

total_value formula
-------------------
    The combat value math lives in ``ability_value_calculator`` and folds
    together the level/element-scaled base power, the status weight, the real
    per-turn damage of damaging statuses (e.g. ``continuous_damage``), the AOE
    multiplier, and the AP cost::

        payload = (scaled_power + status_weight + status_damage) * aoe_mult
        tv      = payload - ap_cost
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List
import math

from tui.services.dev.dataservices.models import (
    AbilityNode,
    AbilityTypeNode,
    AbilityValidationError,
)
from tui.services.dev.dataservices.ability_value_calculator import (
    AOE_MULTIPLIER as _AOE_MULTIPLIER,
    ability_power_estimate,
    compute_ability_value,
    scaled_base_power,
    status_power_estimate,
    status_weight as _status_weight,
    status_weight_total as _status_weight_total,
    status_weight_total_scaled as _status_weight_total_scaled,
    total_value as _total_value,
)

_KNOWN_TYPES   = {"technique", "spirit", "magic", "tech", "skill"}
_KNOWN_EFFECTS = {"damage", "heal", "status", "revive", "cure"}

# Cure abilities accept special "meta" status keys that are *not* real
# STATUS_EFFECTS entries — they are consumed directly by
# ``PlayerAbility.apply()``'s EffectType.CURE branch:
#   * 'all'    -> target.cure_all_debuffs()
#   * 'debuff' -> target.cure_elemental_and_stat_debuffs()
# Any other key is treated as a concrete status id and must exist in
# STATUS_EFFECTS. These meta keys must be exempt from the A8 unknown-status
# check so a valid cure ability isn't flagged.
_CURE_META_STATUS_KEYS = {"all", "debuff"}

# A9 thin-check floor.  The intended design is *one primary status per ability*,
# so the floor scales gently rather than linearly: a single strong status (e.g.
# stun/petrify) satisfies most levels, while a lone weak stat buff/debuff is
# flagged as genuinely thin.  Peer-relative B1/B2 balance checks handle the rest.
#     target = _STATUS_WEIGHT_BASE + (level - 1) * _STATUS_WEIGHT_PER_LEVEL
_STATUS_WEIGHT_BASE      = 6.0
_STATUS_WEIGHT_PER_LEVEL = 3.0


def _status_weight_target(level: int) -> float:
    return _STATUS_WEIGHT_BASE + (max(level, 1) - 1) * _STATUS_WEIGHT_PER_LEVEL


# ── AP-cost mispricing check (B3) ─────────────────────────────────────────────
# AP cost is a *price*: it should be proportional to the combat payload the
# ability delivers.  Rather than a standard-deviation "outlier" check (which
# always flags the tails of any spread and can never report a clean dataset), we
# measure each ability's value-per-AP efficiency against the *median* efficiency
# of abilities *in the same effect category*.  Payload magnitudes differ wildly
# between categories (a lv5 damage ability delivers hundreds of points while a
# status ability delivers a handful), so a single global median would price all
# status abilities as overpriced and all damage abilities as underpriced.  A
# per-effect median self-calibrates to each category while the fixed multiplier
# band gives an absolute healthy range so a well-priced set produces zero
# warnings.
#     efficiency  = payload / ap_cost
#     flag when   efficiency < _AP_EFF_LOW  * median_efficiency[effect] (too dear)
#            or   efficiency > _AP_EFF_HIGH * median_efficiency[effect] (too cheap)
_AP_EFF_LOW  = 0.70
_AP_EFF_HIGH = 1.40

# Relative epsilon so an ability sitting *exactly* on a band edge (efficiency ==
# low_eff/high_eff) is treated as in-band rather than flagged by floating-point
# noise.  Without this, a value priced precisely at the boundary both trips the
# check and yields a "recommended AP" equal to its current AP (a contradiction).
_AP_EFF_EPS  = 1e-6

# ── Status-density check (B4) ─────────────────────────────────────────────────
# A status/cure ability's worth should come mostly from the *statuses it applies*,
# not from a large flat base_power riding along.  When the status weight + status
# damage is a small fraction of the total payload, the ability is really a damage
# stick wearing a status label — its status_keys are cosmetic.  Flag when the
# status contribution falls below this fraction of the payload.
_STATUS_DENSITY_MIN = 0.35

# ── Support-efficiency check (B5) ─────────────────────────────────────────────
# Heal/revive/cure abilities are priced together as one "support" category: each
# effect alone is sparse, but they share a payload scale and compete for the same
# AP budget.  Their value-per-AP must sit inside this band around the combined
# support median, independently of the per-effect B3 band.
_SUPPORT_EFFECTS   = frozenset({"heal", "revive", "cure"})
_SUPPORT_EFF_LOW   = 0.60
_SUPPORT_EFF_HIGH  = 1.60

# ── AOE-premium check (B6) ────────────────────────────────────────────────────
# AOE abilities deliver AOE_MULTIPLIER (1.5x) the payload of a single-target peer,
# so they must cost more AP.  This is a *sticker-price* sanity check on top of the
# payload-aware B3/B5 bands, so it uses a tolerance band rather than an exact
# boundary: an ability only trips it when its AP is *clearly* on the wrong side of
# the opposite bucket's median, not merely a point or two across.  A tie or a
# small overlap (e.g. a single-target carrying an extra status legitimately
# costing a little more) must not flag.
_AOE_PREMIUM_MIN_BUCKET = 2
_AOE_PREMIUM_TOL        = 1.25   # must be 25%+ across the median to flag

# ── Progression-break check (B7) ──────────────────────────────────────────────
# Power creep is derived from the data, not a fixed curve: each effect's expected
# floor at level N is the running maximum of the median payloads of all lower
# levels.  Using the running max (rather than level N-1 alone) prevents a locally
# weak tier from lowering the bar below an already-stronger earlier tier.  A
# higher-level ability delivering below this fraction of the floor is a genuine
# progression regression and is surfaced as an error.
_PROGRESSION_TOL = 0.90


def _err(code: str, message: str, severity: str = "error") -> AbilityValidationError:
    return AbilityValidationError(code=code, message=message, severity=severity)


def _median(values: List[float]) -> float:
    """Return the median of *values* (0.0 if empty)."""
    if not values:
        return 0.0
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2.0



def _flat_nodes(tree: List[AbilityTypeNode]) -> List[AbilityNode]:
    out: List[AbilityNode] = []
    for type_node in tree:
        for level_node in type_node.level_buckets:
            out.extend(level_node.abilities)
    return out


def validate_ability_tree(tree: List[AbilityTypeNode]) -> Dict[str, int]:
    """Validate every AbilityNode in *tree*, annotating .errors in-place.

    *const* should be the ``game.constants`` module.  When supplied, known
    elements are taken from ``const.ELEMENTAL_CHAR_KEYS`` and known statuses
    from ``const.STATUS_EFFECTS`` so the validator stays in sync with the
    game's authoritative data rather than a duplicated hardcoded set.

    Returns a summary dict::
        {"abilities_scanned": int, "invalid": int, "total_errors": int,
         "by_code": {code: count}}
    """
    from game import constants as const
    # Derive known sets from const when available; fall back to safe defaults
    known_elements: frozenset[str] = frozenset(
        str(k).lower() for k in (getattr(const, "ELEMENTAL_CHAR_KEYS", {}) or {}).keys()
    )
    known_statuses: frozenset[str] = frozenset(
        str(k).lower() for k in (getattr(const, "STATUS_EFFECTS", {}) or {}).keys()
    )

    all_nodes = _flat_nodes(tree)

    # Reset existing errors
    for node in all_nodes:
        node.errors.clear()

    by_code: Dict[str, int] = defaultdict(int)

    # ── Build balance groups ──────────────────────────────────────────────
    # Grouping is by (level, effect): abilities of the same level and effect are
    # compared against each other regardless of ability_type, so cross-type
    # outliers surface (B1/B2 total_value balance).
    tv_by_group: Dict[tuple, List[float]] = defaultdict(list)
    node_group:  Dict[str, tuple]         = {}

    # Collect value-per-AP efficiencies keyed by (effect, level) for the B3
    # mispricing median.  Payloads differ by orders of magnitude across effect
    # categories *and* grow steeply with level (damage roughly quadruples per
    # level), so pricing against a per-(effect, level) median gives an implicit
    # expected-payload curve: each ability is judged against a "typical" peer of
    # the same category and level rather than a flat global figure.
    efficiencies_by_key: Dict[tuple, List[float]] = defaultdict(list)

    # Extra buckets for the new balance checks:
    #   payloads_by_key       -> (effect, level) -> [payload]           (B7 curve)
    #   support_efficiencies  -> combined heal/revive/cure eff           (B5 band)
    #   appp_by_aoe           -> (effect, level, is_aoe) -> [ap/payload] (B6 premium)
    payloads_by_key:      Dict[tuple, List[float]] = defaultdict(list)
    support_efficiencies: List[float]              = []
    appp_by_aoe:          Dict[tuple, List[float]] = defaultdict(list)

    for node in all_nodes:
        seed   = node.record.extras.get("_seed") or {}
        level  = int(seed.get("level", 1) or 1)
        effect = str(seed.get("effect", "") or "").lower()
        gkey   = (level, effect)
        tv_by_group[gkey].append(_total_value(seed))
        node_group[node.ability_id] = gkey

        breakdown = compute_ability_value(seed)
        if breakdown.payload > 0:
            payloads_by_key[(effect, level)].append(breakdown.payload)
        if breakdown.ap_cost > 0 and breakdown.payload > 0:
            is_aoe = bool(seed.get("can_aoe", False))
            # AP *per unit payload*: a strong status raises both AP and payload,
            # so this price-per-value normalises status strength out of the AOE
            # comparison (a strong single-target status is no longer read as
            # "overpriced" just because its raw AP exceeds a weaker AOE peer's).
            appp_by_aoe[(effect, level, is_aoe)].append(breakdown.ap_cost / breakdown.payload)
            eff = breakdown.payload / breakdown.ap_cost
            efficiencies_by_key[(effect, level)].append(eff)
            if effect in _SUPPORT_EFFECTS:
                support_efficiencies.append(eff)

    # Only keep groups with more than one member AND a strictly positive
    # average.  A percentage ratio across a zero/negative baseline is
    # meaningless (e.g. "5.0 is only -214% of average -2.3"), so those groups
    # are skipped for balance checking entirely.
    group_avg: Dict[tuple, float] = {
        k: (sum(v) / len(v))
        for k, v in tv_by_group.items()
        if len(v) > 1 and (sum(v) / len(v)) > 0
    }

    # Median value-per-AP within each (effect, level) bucket.  This self-
    # calibrates to the category's typical payload at that level while resisting
    # extremes, so the B3 band flags genuine outliers rather than the structural
    # growth of payload with level or the gap between status and damage scales.
    # Buckets with too few members fall back to the effect-wide median so a lone
    # ability at some level is still priced against its category.
    _MIN_BUCKET = 3
    effect_efficiencies: Dict[str, List[float]] = defaultdict(list)
    for (effect, _level), effs in efficiencies_by_key.items():
        effect_efficiencies[effect].extend(effs)

    median_efficiency_by_key: Dict[tuple, float] = {}
    for key, effs in efficiencies_by_key.items():
        if effs:
            median_efficiency_by_key[key] = _median(effs)
    median_efficiency_by_effect: Dict[str, float] = {
        effect: _median(effs)
        for effect, effs in effect_efficiencies.items()
        if effs
    }

    # Median payload per (effect, level) — the raw material for the B7 curve.
    median_payload_by_key: Dict[tuple, float] = {
        key: _median(vals) for key, vals in payloads_by_key.items() if vals
    }

    # Per-effect progression floor: floor(effect, level) is the running maximum of
    # the median payloads of the every *lower* level with a populated bucket.  Judging
    # against the cumulative max (not just level-1) means a locally weak tier can never
    # pull the expected minimum below a stronger earlier tier.
    progression_floor: Dict[tuple, float] = {}
    levels_by_effect: Dict[str, List[int]] = defaultdict(list)
    for (effect, level) in median_payload_by_key:
        levels_by_effect[effect].append(level)
    for effect, levels in levels_by_effect.items():
        running_max = 0.0
        for level in sorted(set(levels)):
            if running_max > 0:
                progression_floor[(effect, level)] = running_max
            bucket = payloads_by_key.get((effect, level), [])
            if len(bucket) >= _MIN_BUCKET:
                running_max = max(running_max, median_payload_by_key[(effect, level)])

    # Combined support (heal/revive/cure) median value-per-AP for the B5 band.
    median_support_efficiency = _median(support_efficiencies) if support_efficiencies else 0.0

    # Median AP-per-payload by (effect, level, is_aoe) for the B6 AOE-premium
    # comparison.  Comparing price-per-value (not raw AP) means a legitimately
    # strong single-target status is not flagged merely for costing more AP than
    # a weaker AOE peer — only a genuine premium mismatch trips the check.
    median_appp_by_aoe: Dict[tuple, float] = {
        key: _median(vals) for key, vals in appp_by_aoe.items() if vals
    }

    # ── Per-node checks ───────────────────────────────────────────────────
    for node in all_nodes:
        seed        = node.record.extras.get("_seed") or {}
        atype       = str(seed.get("ability_type", "") or "").lower()
        effect      = str(seed.get("effect", "") or "").lower()
        base_power  = int(seed.get("base_power", 0) or 0)
        status_keys = seed.get("status_keys") or []
        elements    = seed.get("elements") or []

        # A1
        if atype not in _KNOWN_TYPES:
            node.errors.append(_err(
                "ABILITY_UNKNOWN_TYPE",
                f"ability_type '{atype}' is not a recognised type.",
            ))
            by_code["ABILITY_UNKNOWN_TYPE"] += 1

        # A2
        if effect not in _KNOWN_EFFECTS:
            node.errors.append(_err(
                "ABILITY_UNKNOWN_EFFECT",
                f"effect '{effect}' is not a recognised effect.",
            ))
            by_code["ABILITY_UNKNOWN_EFFECT"] += 1

        # A3
        if effect == "damage" and base_power == 0:
            node.errors.append(_err(
                "ABILITY_DAMAGE_NO_POWER",
                "Damage ability has base_power of 0.",
            ))
            by_code["ABILITY_DAMAGE_NO_POWER"] += 1

        # A4
        if effect == "heal" and base_power == 0:
            node.errors.append(_err(
                "ABILITY_HEAL_NO_POWER",
                "Heal ability has base_power of 0.",
            ))
            by_code["ABILITY_HEAL_NO_POWER"] += 1

        # A5
        if effect in ("status", "cure") and not status_keys:
            node.errors.append(_err(
                "ABILITY_STATUS_NO_KEYS",
                f"Effect '{effect}' ability has no status_keys.",
            ))
            by_code["ABILITY_STATUS_NO_KEYS"] += 1

        # A6
        if effect in ("damage", "status", "heal") and not elements:
            node.errors.append(_err(
                "ABILITY_NO_ELEMENTS",
                "Ability has no elements defined.",
                severity="warning",
            ))
            by_code["ABILITY_NO_ELEMENTS"] += 1

        # A7 — each unknown element is a separate error
        for elem in elements:
            if str(elem).lower() not in known_elements:
                node.errors.append(_err(
                    "ABILITY_UNKNOWN_ELEMENT",
                    f"Element '{elem}' is not in ELEMENTAL_CHAR_KEYS.",
                ))
                by_code["ABILITY_UNKNOWN_ELEMENT"] += 1

        # A10 — an ability must carry at least as many elements as its level.
        # Higher-level abilities are expected to span a broader elemental
        # profile; a lv4 ability with a single element is under-specified.
        if len(elements) < node.level:
            node.errors.append(_err(
                "ABILITY_TOO_FEW_ELEMENTS",
                f"Ability at level {node.level} has {len(elements)} element(s) "
                f"(expected ≥ {node.level}).",
            ))
            by_code["ABILITY_TOO_FEW_ELEMENTS"] += 1

        # A8 — each unknown status key is a separate error.
        # Cure abilities may use meta keys ('all'/'debuff') that are handled
        # directly by the CURE resolution branch rather than being real
        # STATUS_EFFECTS entries, so those are exempt.
        for sk in status_keys:
            sk_norm = str(sk).lower()
            if effect == "cure" and sk_norm in _CURE_META_STATUS_KEYS:
                continue
            if sk_norm not in known_statuses:
                node.errors.append(_err(
                    "ABILITY_UNKNOWN_STATUS",
                    f"status_key '{sk}' is not in STATUS_EFFECTS.",
                ))
                by_code["ABILITY_UNKNOWN_STATUS"] += 1

        # A9 — status/cure abilities should carry enough status weight for their
        # level.  A single strong status (e.g. petrify) can satisfy a level while
        # weaker stat buffs/debuffs must be stacked to reach the target.  The
        # ability's scaled power counts toward the weight, so a status ability
        # that also delivers heal/damage via base_power is credited for that
        # payload just as a heal/damage ability would be.  ``scaled_base_power``
        # already reflects the actual in-combat flat hit for status abilities
        # (halved, no level multiplier), so it is added at full value here.
        if effect in ("status", "cure") and status_keys:
            power_credit  = scaled_base_power(seed) * 2
            weight_total  = _status_weight_total_scaled(status_keys, node.level) + power_credit
            weight_target = _status_weight_target(node.level)
            if weight_total < weight_target:
                node.errors.append(_err(
                    "ABILITY_STATUS_THIN",
                    f"{effect.capitalize()} ability at level {node.level} has "
                    f"status weight {weight_total:.0f} from "
                    f"{len(status_keys)} key(s) + power "
                    f"(expected ≥ {weight_target:.0f}).",
                    severity="warning",
                ))
                by_code["ABILITY_STATUS_THIN"] += 1

        # B1 / B2
        gkey = node_group.get(node.ability_id)
        if gkey and gkey in group_avg:
            avg = group_avg[gkey]
            tv  = _total_value(seed)
            # Only compare when tv and avg share the same sign.  A percent-of-
            # average ratio across zero is meaningless (e.g. "-9.0 is only -206%
            # of average 4.4"), so abilities whose value straddle the group
            # average's sign are left for the A9 / B3 checks instead.
            if avg > 0 and tv > 0:
                ratio = tv / avg
                if ratio < 0.65:
                    node.errors.append(_err(
                        "ABILITY_BALANCE_WEAK",
                        f"Total value {tv:.1f} is only {ratio:.0%} of "
                        f"group average {avg:.1f} "
                        f"(lv={gkey[0]}, effect={gkey[1]}).",
                        severity="info",
                    ))
                    by_code["ABILITY_BALANCE_WEAK"] += 1
                elif ratio > 1.45:
                    node.errors.append(_err(
                        "ABILITY_BALANCE_STRONG",
                        f"Total value {tv:.1f} is {ratio:.0%} of "
                        f"group average {avg:.1f} "
                        f"(lv={gkey[0]}, effect={gkey[1]}).",
                        severity="notice",
                    ))
                    by_code["ABILITY_BALANCE_STRONG"] += 1

        # B3 — AP mispricing: value-per-AP efficiency outside the healthy band
        # around the *per-(effect, level)* median efficiency (an implicit
        # expected-payload curve).  Thin buckets fall back to the effect-wide
        # median.  Too-low efficiency means the ability is overpriced (dead
        # weight); too-high means underpriced (overpowered for its cost).
        node_level = int(seed.get("level", 1) or 1)
        bucket_effs = median_efficiency_by_key.get((effect, node_level))
        bucket_count = len(efficiencies_by_key.get((effect, node_level), []))
        if bucket_effs is not None and bucket_count >= _MIN_BUCKET:
            median_efficiency = bucket_effs
        else:
            median_efficiency = median_efficiency_by_effect.get(effect, 0.0)
        if median_efficiency > 0:
            ap_cost = float(seed.get("ap_cost", 0) or 0)
            breakdown = compute_ability_value(seed)
            if ap_cost > 0 and breakdown.payload > 0:
                efficiency = breakdown.payload / ap_cost
                ratio = efficiency / median_efficiency
                low_eff  = _AP_EFF_LOW  * median_efficiency
                high_eff = _AP_EFF_HIGH * median_efficiency
                rec_low_ap  = breakdown.payload / (_AP_EFF_HIGH * median_efficiency)
                rec_high_ap = breakdown.payload / (_AP_EFF_LOW  * median_efficiency)
                # Round the recommended AP band *inward* (up on the low end, down
                # on the high end) so the suggestion sits strictly inside the
                # healthy band and never echoes the flagged AP back to the user.
                rec_low_ap  = math.ceil(breakdown.payload / (_AP_EFF_HIGH * median_efficiency))
                rec_high_ap = math.floor(breakdown.payload / (_AP_EFF_LOW  * median_efficiency))
                if rec_high_ap < rec_low_ap:      # band collapsed by rounding
                    rec_high_ap = rec_low_ap
                if efficiency < low_eff * (1.0 - _AP_EFF_EPS):
                    node.errors.append(_err(
                        "ABILITY_AP_MISPRICED",
                        f"AP {ap_cost:.0f} buys {ratio:.2f}x the value-per-AP of a "
                        f"typical {effect} ability (overpriced; recommended AP "
                        f"{rec_low_ap:.0f}–{rec_high_ap:.0f}).",
                        severity="warning",
                    ))
                    by_code["ABILITY_AP_MISPRICED"] += 1
                elif efficiency > high_eff * (1.0 + _AP_EFF_EPS):
                    node.errors.append(_err(
                        "ABILITY_AP_MISPRICED",
                        f"AP {ap_cost:.0f} buys {ratio:.2f}x the value-per-AP of a "
                        f"typical {effect} ability (underpriced; recommended AP "
                        f"{rec_low_ap:.0f}–{rec_high_ap:.0f}).",
                        severity="warning",
                    ))
                    by_code["ABILITY_AP_MISPRICED"] += 1

        # B4 — STATUS_DENSITY: a status ability's worth should come mostly from
        # the statuses it applies, not from a large flat base_power riding along.
        # ``breakdown.status_weight`` + ``breakdown.status_damage`` is the status
        # contribution; the remainder of the payload is flat scaled power.  When
        # statuses supply less than half the payload the ability is really a
        # damage/heal stick wearing a status label (cosmetic status_keys).
        if effect in ("status", "cure") and status_keys:
            breakdown = compute_ability_value(seed)
            if breakdown.payload > 0:
                status_contrib  = breakdown.status_weight + breakdown.status_damage
                status_fraction = status_contrib / breakdown.payload
                if status_fraction < _STATUS_DENSITY_MIN:
                    node.errors.append(_err(
                        "ABILITY_STATUS_DENSITY",
                        f"{effect.capitalize()} ability at level {node.level} draws "
                        f"only {status_fraction:.0%} of its payload from statuses "
                        f"(rest is flat power; expected ≥ {_STATUS_DENSITY_MIN:.0%}).",
                        severity="warning",
                    ))
                    by_code["ABILITY_STATUS_DENSITY"] += 1

        # B5 — SUPPORT_EFFICIENCY: heal/revive/cure value-per-AP must sit inside a
        # band around the *combined* support median.  The recommended AP range is
        # the AP that would place this ability's payload back inside the band:
        #     ap ∈ [ payload / (HIGH*median) , payload / (LOW*median) ]
        # (higher AP → lower efficiency, so the band inverts into AP-space).
        if effect in _SUPPORT_EFFECTS and median_support_efficiency > 0:
            ap_cost   = float(seed.get("ap_cost", 0) or 0)
            breakdown = compute_ability_value(seed)
            if ap_cost > 0 and breakdown.payload > 0:
                support_eff   = breakdown.payload / ap_cost
                support_ratio = support_eff / median_support_efficiency
                rec_low_ap  = breakdown.payload / (_SUPPORT_EFF_HIGH * median_support_efficiency)
                rec_high_ap = breakdown.payload / (_SUPPORT_EFF_LOW  * median_support_efficiency)
                if support_ratio < _SUPPORT_EFF_LOW:
                    node.errors.append(_err(
                        "ABILITY_SUPPORT_EFFICIENCY",
                        f"Support value-per-AP is {support_ratio:.2f}x the support "
                        f"median (overpriced; recommended AP "
                        f"{rec_low_ap:.0f}–{rec_high_ap:.0f}).",
                        severity="warning",
                    ))
                    by_code["ABILITY_SUPPORT_EFFICIENCY"] += 1
                elif support_ratio > _SUPPORT_EFF_HIGH:
                    node.errors.append(_err(
                        "ABILITY_SUPPORT_EFFICIENCY",
                        f"Support value-per-AP is {support_ratio:.2f}x the support "
                        f"median (underpriced; recommended AP "
                        f"{rec_low_ap:.0f}–{rec_high_ap:.0f}).",
                        severity="warning",
                    ))
                    by_code["ABILITY_SUPPORT_EFFICIENCY"] += 1

        # B6 — AOE_PREMIUM (payload-aware): compare *AP-per-payload* between the
        # AOE and single-target buckets rather than raw AP, so a strong status
        # (which raises both AP and payload) does not read as mispriced.  Because
        # AOE payload already includes the _AOE_MULTIPLIER (1.5x), a fairly priced
        # AOE ability has a *lower* AP-per-payload than its single-target peers.
        #   * single-target with AP/payload clearly *below* the AOE median
        #     (cheaper per value than an AOE) => underpriced single-target.
        #   * single-target with AP/payload clearly *above* the AOE median is
        #     expected (single-target should cost more per value) and is NOT
        #     flagged here — B3 handles absolute mispricing.
        # A tolerance band keeps boundary ties quiet.
        node_level = int(seed.get("level", 1) or 1)
        ap_cost    = float(seed.get("ap_cost", 0) or 0)
        if ap_cost > 0:
            breakdown = compute_ability_value(seed)
            is_aoe    = bool(seed.get("can_aoe", False))
            st_appp   = appp_by_aoe.get((effect, node_level, False), [])
            aoe_appp  = appp_by_aoe.get((effect, node_level, True), [])
            if breakdown.payload > 0:
                node_appp = ap_cost / breakdown.payload
                if is_aoe and len(st_appp) >= _AOE_PREMIUM_MIN_BUCKET:
                    median_st = median_appp_by_aoe[(effect, node_level, False)]
                    # AOE underpriced if it costs *as much or more* per payload
                    # than single-target (it should cost clearly less).  Fix by
                    # lowering AP or raising power (payload) so AP-per-payload
                    # falls to at most the single-target median.
                    if median_st > 0 and node_appp >= median_st * _AOE_PREMIUM_TOL:
                        rec_ap = math.floor(breakdown.payload * median_st)
                        node.errors.append(_err(
                            "ABILITY_AOE_PREMIUM",
                            f"AOE ability costs {node_appp:.2f} AP per payload, at "
                            f"or above the single-target median {median_st:.2f} — "
                            f"AOE reach (x{_AOE_MULTIPLIER:g}) not reflected in "
                            f"cost.  Fix: decrease AP (≤ {rec_ap}) or increase "
                            f"power.",
                            severity="warning",
                        ))
                        by_code["ABILITY_AOE_PREMIUM"] += 1
                elif (not is_aoe) and len(aoe_appp) >= _AOE_PREMIUM_MIN_BUCKET:
                    median_aoe = median_appp_by_aoe[(effect, node_level, True)]
                    # Single-target underpriced if it costs *clearly less* per
                    # payload than an AOE ability (it should cost more per value).
                    # Fix by raising AP or lowering power (payload) so AP-per-
                    # payload rises to at least the AOE median.
                    if median_aoe > 0 and node_appp <= median_aoe / _AOE_PREMIUM_TOL:
                        rec_ap = math.ceil(breakdown.payload * median_aoe)
                        node.errors.append(_err(
                            "ABILITY_AOE_PREMIUM",
                            f"Single-target ability costs {node_appp:.2f} AP per "
                            f"payload, below the AOE median {median_aoe:.2f} — "
                            f"priced cheaper per value than an AOE peer.  Fix: "
                            f"increase AP (≥ {rec_ap}) or decrease power.",
                            severity="warning",
                        ))
                        by_code["ABILITY_AOE_PREMIUM"] += 1

        # B7 — PROGRESSION_BREAK (error): a higher-level ability must not deliver
        # less raw payload than the data-derived floor of the tiers below it.  The
        # floor is the running maximum of the median payloads of all lower levels
        # (built once in ``progression_floor``), so a locally weak tier can never
        # lower the bar beneath a stronger earlier tier.  Judged on raw payload —
        # B3's per-level normalized efficiency cannot see cross-level regressions.
        floor = progression_floor.get((effect, node_level))
        if floor and floor > 0:
            breakdown = compute_ability_value(seed)
            if breakdown.payload > 0 and breakdown.payload < _PROGRESSION_TOL * floor:
                node.errors.append(_err(
                    "ABILITY_PROGRESSION_BREAK",
                    f"Level {node_level} {effect} ability delivers payload "
                    f"{breakdown.payload:.0f}, below the level-progression floor "
                    f"{floor:.0f} set by lower tiers.",
                    severity="error",
                ))
                by_code["ABILITY_PROGRESSION_BREAK"] += 1


    invalid      = sum(1 for n in all_nodes if n.errors)
    total_errors = sum(len(n.errors) for n in all_nodes)

    return {
        "abilities_scanned": len(all_nodes),
        "invalid":           invalid,
        "total_errors":      total_errors,
        "by_code":           dict(by_code),
    }


def validate_abilities_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.ability_validator import validate_ability_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_ability_tree               # noqa: PLC0415

    tree    = get_ability_tree()
    summary = validate_ability_tree(tree)

    # Repopulate table so flagged rows render in colour
    rebuild_ability_tree_for_screen(screen)

    invalid      = summary.get("invalid", 0)
    total_errors = summary.get("total_errors", 0)

    if total_errors == 0:
        screen.notify("✓ Ability integrity OK — no issues found.", timeout=3.0)
    else:
        screen.notify(
            f"✗ {total_errors} issue(s) across {invalid} ability(s) — flagged in table.",
            severity="warning",
            timeout=5.0,
        )