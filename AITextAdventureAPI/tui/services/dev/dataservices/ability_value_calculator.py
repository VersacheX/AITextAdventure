"""
Ability value calculator.

Central home for the *combat-value* math used by the ability validator and the
dev UI detail panel.  Keeping this logic in one module (rather than inline in
the validator) makes the balance model easy to tune and reuse.

The model combines four signals into a single ``total_value`` figure:

    * ``base_power``            — raw declared power, scaled by level/elements
    * status weight            — relative combat worth of each applied status
    * status damage            — real per-turn damage from damaging statuses
                                 (e.g. ``continuous_damage``)
    * AP cost                  — subtracted, since a costly ability is worth
                                 less at parity payload

AOE abilities scale their payload by ``AOE_MULTIPLIER`` because they hit
multiple targets.

``compute_ability_value`` returns a :class:`AbilityValueBreakdown` so callers
(validator, detail panel) can present or reason about each component rather than
only the final number.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List

# ── Status weighting ──────────────────────────────────────────────────────────
# Relative combat value of each status key.  Hard-disables and permanent effects
# are worth far more than incremental stat buffs/debuffs.  Keys not listed here
# fall back to ``DEFAULT_STATUS_WEIGHT``.
STATUS_WEIGHTS: Dict[str, float] = {
    # ── Hard disables / permanent (very high value) ──
    "petrify":            22.0,
    "confuse":            17.0,
    "stun":               15.0,
    "sleep":              12.0,
    "silence":            15.0,    
    # ── Damage-over-time / persistent ──
    "continuous_damage":  6.0,
    # ── Heal-over-time (beneficial mirror of continuous_damage) ──
    "regen":              6.0,
    # ── Utility ──
    "scanned":             6.0,
    # ── Elemental buffs/debuffs (moderate) ──
    "elemental_attack_buff":  8.0,
    "elemental_defense_buff": 8.0,
    "elemental_debuff":       8.0,
    "attack_buff":            4.0,
    "attack_debuff":          4.0,
    "defense_buff":           4.0,
    "defense_debuff":         4.0,
    # ── Single-stat buffs/debuffs (low value) ──
    "strength_buff":       8.0,
    "strength_debuff":     6.0,
    "dexterity_buff":      8.0,
    "dexterity_debuff":    8.0,
    "intelligence_buff":   8.0,
    "intelligence_debuff": 6.0,
    "constitution_buff":   6.0,
    "constitution_debuff": 8.0,
}
DEFAULT_STATUS_WEIGHT = 8.0

# AOE payload multiplier.  An AOE ability hits multiple targets, so its
# base_power + status payload is scaled by this factor instead of a flat bonus.
AOE_MULTIPLIER = 1.5

# AP cost is discounted before being subtracted from the payload: an ability's
# AP cost only detracts ``AP_COST_WEIGHT`` of its face value from total_value
# (e.g. an 10 AP ability removes only 7.0 points).
AP_COST_WEIGHT = 1.00

# Status abilities that also carry ``base_power`` deal it as a *flat secondary
# hit* applied at half strength in combat (mirrors
# ``status_utils.LOW_DMG_STATUS_MOD``).  The value model uses the same factor so
# the previewed power matches what the ability actually deals, and — unlike pure
# damage abilities — no level multiplier is applied (level's contribution to a
# status ability already flows through the status mechanics themselves).
_STATUS_FLAT_POWER_MOD = 0.5

# ── Damage-over-time weighting ────────────────────────────────────────────────
# Damaging statuses (``continuous_damage``) are valued as *weight*, not as raw
# stacked per-turn × element damage.  The raw model compounded level and element
# count on top of an already level/element-scaled power, so a single lv5 DoT with
# several elements exploded into the thousands and dwarfed every other status.
# Instead a damaging status earns its base ``STATUS_WEIGHTS`` entry plus a modest,
# *capped* per-level bonus so higher-level DoT is worth a little more without
# distorting the whole status category.
DOT_WEIGHT_PER_LEVEL = 3.0
DOT_WEIGHT_CAP       = 30.0

# Final total_value precision.  Intermediate math retains full float precision;
# only the returned total_value is rounded to this many decimal places.
_TOTAL_VALUE_PRECISION = 3

# ── Status power preview ──────────────────────────────────────────────────────
# Only statuses that deal *actual damage* are previewed as a weight bonus.  Pure
# stat/defense debuffs (e.g. defense_debuff, elemental_debuff) amplify incoming
# damage but deal none themselves, and are already credited through the status
# weight — crediting them here too would double-count them.
#
# Damaging statuses use ``continuous_damage`` (constants_other.STATUS_EFFECTS).
# ``regen`` is the beneficial heal-over-time mirror and is valued the same way.
# Rather than projecting real per-turn damage/heal (which compounds level/element
# scaling), they contribute a small capped weight bonus via
# :func:`status_power_estimate` so DoT/HoT is valued without distorting the category.
_DAMAGING_STATUS_KEYS = {"continuous_damage", "regen"}


def status_weight(key: str) -> float:
    return STATUS_WEIGHTS.get(str(key).lower(), DEFAULT_STATUS_WEIGHT)


def status_weight_total(status_keys: List[Any]) -> float:
    return sum(status_weight(k) for k in (status_keys or []))


# ── Status level scaling ──────────────────────────────────────────────────────
# A status's real combat impact grows with the ability's level: in
# ``PlayerAbility._derive_status_effects`` the applied ``magnitude`` scales as
# ``level * magnitude_per_level`` and ``duration`` grows with level too, so a
# level-3 debuff lands with ~3x the magnitude of a level-1 one.  That magnitude
# then feeds *percentage* combat modifiers (mag * 0.25, mag * 0.10, ...) with
# floors, so the effective impact is sub-linear — crediting the weight at the
# full ``x level`` would badly over-value high-level statuses.  Instead the
# status weight earns a per-level percentage bonus that mirrors the established
# damage level convention (``1.0 + 0.20 * (level - 1)``): +20% per level above 1.
STATUS_WEIGHT_LEVEL_MOD = 0.20


def status_level_multiplier(level: int) -> float:
    """Return the level-scaling multiplier applied to raw status weight."""
    return 1.0 + STATUS_WEIGHT_LEVEL_MOD * max(0, int(level) - 1)


def status_weight_total_scaled(status_keys: List[Any], level: int) -> float:
    """Return status weight total scaled by the ability's level.

    Combines the raw :func:`status_weight_total` baseline with
    :func:`status_level_multiplier` so higher-level statuses are credited for the
    extra magnitude/duration they deliver without a runaway linear ``x level``.
    """
    return status_weight_total(status_keys) * status_level_multiplier(level)



def scaled_base_power(seed: dict) -> float:
    """Return ``base_power`` scaled for its effect type.

    For pure ``damage``/``heal``/``revive`` abilities, ``base_power`` *is* the
    whole payload, so it is scaled by level and element count to mirror
    ``PlayerAbility.compute_power()``.

    For ``status`` abilities, ``base_power`` is only a *flat secondary hit* that
    accompanies the status: in combat it is applied at half strength
    (``status_utils.LOW_DMG_STATUS_MOD``) and — crucially — level's real power
    contribution already flows through the status mechanics themselves
    (``_derive_status_effects`` scales magnitude, duration and per-turn
    damage/heal by ability level).  Multiplying the literal ``base_power`` by a
    level factor on top of that double-counts level, so a declared ``38`` reads
    as ``38`` whether the ability is level 1 or level 3.  Only the element
    multiplier (which does apply to the in-combat flat hit) is retained.
    """
    bp = float(seed.get("base_power", 0) or 0)
    level = int(seed.get("level", 1) or 1)
    n_elem = len(seed.get("elements") or [])
    elem_mult = 1.0 + 0.35 * n_elem

    effect = str(seed.get("effect", "") or "").lower()
    if effect == "status":
        # literal flat hit, halved in combat, no level multiplier
        return bp * _STATUS_FLAT_POWER_MOD * elem_mult

    level_mult = 1.0 + 0.20 * max(0, level - 1)
    elem_mult = 1.0 + 0.35 * n_elem
    return bp * level_mult * elem_mult


def status_power_estimate(seed: dict) -> float:
    """Estimate the combat *weight* contributed by damaging statuses.

    Damaging statuses (``continuous_damage``) previously projected their real
    per-turn damage (``level * scaled_power * 0.5 * elements``), which compounded
    level/element scaling on top of the already-scaled base power and produced
    values in the thousands for a single high-level multi-element DoT.  That one
    term dominated the entire status category and made every ordinary status
    ability read as balance-weak.

    To keep DoT meaningful but proportionate, it is now folded in as a *capped
    weight bonus*: a flat per-level increment on top of the status's base
    ``STATUS_WEIGHTS`` entry (which is already counted via
    :func:`status_weight_total`).  This preview therefore returns only the
    *bonus* weight, clamped to :data:`DOT_WEIGHT_CAP`.
    """
    status_keys = seed.get("status_keys") or []
    if not status_keys:
        return 0.0
    level = int(seed.get("level", 1) or 1)
    bonus = 0.0
    for key in status_keys:
        if str(key).lower() in _DAMAGING_STATUS_KEYS:
            bonus += min(DOT_WEIGHT_CAP, level * DOT_WEIGHT_PER_LEVEL)
    return bonus


def ability_power_estimate(seed: dict) -> int:
    """Return an integer combat-power figure combining scaled base power with
    any status-derived damage contribution.
    """
    return int(round(scaled_base_power(seed) + status_power_estimate(seed)))


@dataclass
class AbilityValueBreakdown:
    """Decomposed view of an ability's computed combat value."""
    scaled_power:    float
    status_weight:   float
    status_damage:   float
    ap_cost:         float
    aoe_multiplier:  float
    payload:         float   # (scaled_power + status_weight + status_damage) * aoe
    total_value:     float   # payload - ap_cost


def compute_ability_value(seed: dict) -> AbilityValueBreakdown:
    """Compute the full value breakdown for an ability seed.

    ``total_value`` folds together the real combat payload (level/element scaled
    base power + status weight + damaging-status damage), the AOE multiplier, and
    the AP cost so the validator's balance checks reflect true relative worth.
    """
    scaled_power = scaled_base_power(seed) / _STATUS_FLAT_POWER_MOD
    status_keys  = seed.get("status_keys") or []
    level        = int(seed.get("level", 1) or 1)
    sw           = status_weight_total_scaled(status_keys, level)
    sdmg         = status_power_estimate(seed)
    ap           = float(seed.get("ap_cost", 0) or 0)
    aoe          = AOE_MULTIPLIER if bool(seed.get("can_aoe", False)) else 1.0

    # Retain full precision through the intermediate calculation; only the final
    # total_value is rounded to _TOTAL_VALUE_PRECISION decimal places.
    payload = (scaled_power + sw + sdmg) * aoe
    total = payload - (ap * AP_COST_WEIGHT)
    return AbilityValueBreakdown(
        scaled_power   = scaled_power,
        status_weight  = sw,
        status_damage  = sdmg,
        ap_cost        = ap,
        aoe_multiplier = aoe,
        payload        = payload,
        total_value    = round(total, _TOTAL_VALUE_PRECISION),
    )


def total_value(seed: dict) -> float:
    """Convenience accessor for just the final combat value figure."""
    return compute_ability_value(seed).total_value
