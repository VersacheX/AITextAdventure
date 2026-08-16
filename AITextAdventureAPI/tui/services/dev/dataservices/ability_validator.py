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
                               (8 + (level-1)*3)  (warning)

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
                               band (70%–135%) around the global median
                               efficiency  (warning)
    Balance groups (B1/B2) are (level, effect): abilities are compared across
    ability_types so cross-type balance surfaces.  Groups with a single member
    are skipped (no meaningful average), as are groups whose average is not
    strictly positive.  B3 is *not* peer-grouped — it prices every ability's
    payload-per-AP against the median efficiency of the whole dataset, so a
    well-priced dataset produces zero warnings instead of always flagging tails.

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

from tui.services.dev.dataservices.models import (
    AbilityNode,
    AbilityTypeNode,
    AbilityValidationError,
)
from tui.services.dev.dataservices.ability_value_calculator import (
    AOE_MULTIPLIER as _AOE_MULTIPLIER,
    ability_power_estimate,
    compute_ability_value,
    status_power_estimate,
    status_weight as _status_weight,
    status_weight_total as _status_weight_total,
    total_value as _total_value,
)

_KNOWN_TYPES   = {"technique", "faith", "magic", "tech", "skill"}
_KNOWN_EFFECTS = {"damage", "heal", "status", "revive", "cure"}

# A9 thin-check floor.  The intended design is *one primary status per ability*,
# so the floor scales gently rather than linearly: a single strong status (e.g.
# stun/petrify) satisfies most levels, while a lone weak stat buff/debuff is
# flagged as genuinely thin.  Peer-relative B1/B2 balance checks handle the rest.
#     target = _STATUS_WEIGHT_BASE + (level - 1) * _STATUS_WEIGHT_PER_LEVEL
_STATUS_WEIGHT_BASE      = 8.0
_STATUS_WEIGHT_PER_LEVEL = 3.0


def _status_weight_target(level: int) -> float:
    return _STATUS_WEIGHT_BASE + (max(level, 1) - 1) * _STATUS_WEIGHT_PER_LEVEL


# ── AP-cost mispricing check (B3) ─────────────────────────────────────────────
# AP cost is a *price*: it should be proportional to the combat payload the
# ability delivers.  Rather than a standard-deviation "outlier" check (which
# always flags the tails of any spread and can never report a clean dataset), we
# measure each ability's value-per-AP efficiency against the *median* efficiency
# of all abilities.  The median self-calibrates to the real data yet is robust
# to extremes, while the fixed multiplier band gives an absolute healthy range
# so a well-priced dataset produces zero warnings.
#     efficiency  = payload / ap_cost
#     flag when   efficiency < _AP_EFF_LOW  * median_efficiency   (too expensive)
#            or   efficiency > _AP_EFF_HIGH * median_efficiency   (too cheap)
_AP_EFF_LOW  = 0.70
_AP_EFF_HIGH = 1.40


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

    # Collect value-per-AP efficiencies for the global B3 mispricing median.
    efficiencies: List[float] = []

    for node in all_nodes:
        seed   = node.record.extras.get("_seed") or {}
        level  = int(seed.get("level", 1) or 1)
        effect = str(seed.get("effect", "") or "").lower()
        gkey   = (level, effect)
        tv_by_group[gkey].append(_total_value(seed))
        node_group[node.ability_id] = gkey

        breakdown = compute_ability_value(seed)
        if breakdown.ap_cost > 0 and breakdown.payload > 0:
            efficiencies.append(breakdown.payload / breakdown.ap_cost)

    # Only keep groups with more than one member AND a strictly positive
    # average.  A percentage ratio against a zero/negative baseline is
    # meaningless (e.g. "5.0 is only -214% of average -2.3"), so those groups
    # are skipped for balance checking entirely.
    group_avg: Dict[tuple, float] = {
        k: (sum(v) / len(v))
        for k, v in tv_by_group.items()
        if len(v) > 1 and (sum(v) / len(v)) > 0
    }

    # Median value-per-AP across all priced abilities.  The median self-calibrates
    # to the real data while resisting extremes, so the B3 mispricing band is
    # anchored to a "typical" ability rather than to a spread that always has tails.
    median_efficiency = _median(efficiencies) if efficiencies else 0.0

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

        # A8 — each unknown status key is a separate error
        for sk in status_keys:
            if str(sk).lower() not in known_statuses:
                node.errors.append(_err(
                    "ABILITY_UNKNOWN_STATUS",
                    f"status_key '{sk}' is not in STATUS_EFFECTS.",
                ))
                by_code["ABILITY_UNKNOWN_STATUS"] += 1

        # A9 — status/cure abilities should carry enough status weight for their
        # level.  A single strong status (e.g. petrify) can satisfy a level while
        # weaker stat buffs/debuffs must be stacked to reach the target.
        if effect in ("status", "cure") and status_keys:
            weight_total  = _status_weight_total(status_keys)
            weight_target = _status_weight_target(node.level)
            if weight_total < weight_target:
                node.errors.append(_err(
                    "ABILITY_STATUS_THIN",
                    f"{effect.capitalize()} ability at level {node.level} has "
                    f"status weight {weight_total:.0f} from "
                    f"{len(status_keys)} key(s) "
                    f"(expected ≥ {weight_target:.0f}).",
                    severity="warning",
                ))
                by_code["ABILITY_STATUS_THIN"] += 1

        # B1 / B2
        gkey = node_group.get(node.ability_id)
        if gkey and gkey in group_avg:
            avg = group_avg[gkey]
            tv  = _total_value(seed)
            if avg != 0:
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
        # around the global median efficiency.  Too-low efficiency means the
        # ability is overpriced (dead weight); too-high means underpriced
        # (overpowered for its cost).
        if median_efficiency > 0:
            ap_cost = float(seed.get("ap_cost", 0) or 0)
            breakdown = compute_ability_value(seed)
            if ap_cost > 0 and breakdown.payload > 0:
                efficiency = breakdown.payload / ap_cost
                ratio = efficiency / median_efficiency
                low_eff  = _AP_EFF_LOW  * median_efficiency
                high_eff = _AP_EFF_HIGH * median_efficiency
                if efficiency < low_eff:
                    # overpriced: expected AP for a typical efficiency
                    expected_ap = breakdown.payload / median_efficiency
                    node.errors.append(_err(
                        "ABILITY_AP_MISPRICED",
                        f"AP {ap_cost:.0f} buys {ratio:.2f}x the value-per-AP of "
                        f"a typical ability (overpriced; expected AP ~= "
                        f"{expected_ap:.0f}).",
                        severity="warning",
                    ))
                    by_code["ABILITY_AP_MISPRICED"] += 1
                elif efficiency > high_eff:
                    expected_ap = breakdown.payload / median_efficiency
                    node.errors.append(_err(
                        "ABILITY_AP_MISPRICED",
                        f"AP {ap_cost:.0f} buys {ratio:.2f}x the value-per-AP of "
                        f"a typical ability (underpriced; expected AP ~= "
                        f"{expected_ap:.0f}).",
                        severity="warning",
                    ))
                    by_code["ABILITY_AP_MISPRICED"] += 1


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