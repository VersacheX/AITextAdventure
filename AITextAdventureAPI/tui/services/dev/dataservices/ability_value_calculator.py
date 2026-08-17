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
    "petrify":            30.0,
    "confuse":            17.0,
    "stun":               15.0,
    "sleep":              12.0,
    "silence":            15.0,    
    # ── Damage-over-time / persistent ──
    "continuous_damage":  6.0,
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
# Rather than projecting real per-turn damage (which compounds level/element
# scaling), they contribute a small capped weight bonus via
# :func:`status_power_estimate` so DoT is valued without distorting the category.
_DAMAGING_STATUS_KEYS = {"continuous_damage"}


def status_weight(key: str) -> float:
    return STATUS_WEIGHTS.get(str(key).lower(), DEFAULT_STATUS_WEIGHT)


def status_weight_total(status_keys: List[Any]) -> float:
    return sum(status_weight(k) for k in (status_keys or []))


def scaled_base_power(seed: dict) -> float:
    """Return base_power scaled by level and element count, mirroring
    ``PlayerAbility.compute_power()``.
    """
    bp = float(seed.get("base_power", 0) or 0)
    level = int(seed.get("level", 1) or 1)
    n_elem = len(seed.get("elements") or [])
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
    scaled_power = scaled_base_power(seed)
    status_keys  = seed.get("status_keys") or []
    sw           = status_weight_total(status_keys)
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
