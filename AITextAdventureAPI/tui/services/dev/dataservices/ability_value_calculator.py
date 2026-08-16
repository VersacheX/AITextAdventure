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
    "confuse":            22.0,
    "stun":               20.0,
    "sleep":              18.0,
    "silence":            15.0,    
    # ── Damage-over-time / persistent ──
    "continuous_damage":  11.0,
    # ── Utility ──
    "scanned":             9.0,
    # ── Elemental buffs/debuffs (moderate) ──
    "elemental_attack_buff":  8.0,
    "elemental_defense_buff": 8.0,
    "elemental_debuff":       8.0,
    "attack_buff":            5.0,
    "attack_debuff":          5.0,
    "defense_buff":           5.0,
    "defense_debuff":         5.0,
    # ── Single-stat buffs/debuffs (low value) ──
    "strength_buff":       8.0,
    "strength_debuff":     8.0,
    "dexterity_buff":      8.0,
    "dexterity_debuff":    8.0,
    "intelligence_buff":   8.0,
    "intelligence_debuff": 8.0,
    "constitution_buff":   8.0,
    "constitution_debuff": 8.0,
}
DEFAULT_STATUS_WEIGHT = 8.0

# AOE payload multiplier.  An AOE ability hits multiple targets, so its
# base_power + status payload is scaled by this factor instead of a flat bonus.
AOE_MULTIPLIER = 1.5

# ── Status power preview ──────────────────────────────────────────────────────
# Only statuses that deal *actual damage* are previewed as combat damage.  Pure
# stat/defense debuffs (e.g. defense_debuff, elemental_debuff) amplify incoming
# damage but deal none themselves, and are already credited through the status
# weight — crediting them here too would double-count them.
#
# ``continuous_damage`` template (constants_other.STATUS_EFFECTS):
#     magnitude_per_level = 0.5,  min_damage_per_turn = 1
# and ``_derive_status_effects`` computes, per applied status:
#     damage_per_turn = max(min_dpt, int(level * ability_power * magnitude_per_level))
#                       * max(1, element_count)
_DAMAGING_STATUS_KEYS = {"continuous_damage"}
_CONTINUOUS_DAMAGE_MAG_PER_LEVEL = 0.5
_CONTINUOUS_DAMAGE_MIN_PER_TURN = 1


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
    """Estimate the direct combat damage contributed by a status ability.

    Mirrors ``PlayerAbility._derive_status_effects`` for damaging statuses
    (``continuous_damage``) using the ability's own scaled power as the
    owner-independent ``ability_power``.  Non-damaging debuffs/buffs contribute
    nothing here — they are valued via :func:`status_weight_total` instead.
    """
    status_keys = seed.get("status_keys") or []
    if not status_keys:
        return 0.0
    level = int(seed.get("level", 1) or 1)
    n_elem = max(1, len(seed.get("elements") or []))
    ability_power = scaled_base_power(seed)
    total = 0.0
    for key in status_keys:
        if str(key).lower() in _DAMAGING_STATUS_KEYS:
            per_turn = max(
                _CONTINUOUS_DAMAGE_MIN_PER_TURN,
                int(level * ability_power * _CONTINUOUS_DAMAGE_MAG_PER_LEVEL),
            )
            total += per_turn * n_elem
    return total


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

    payload = (scaled_power + sw + sdmg) * aoe
    return AbilityValueBreakdown(
        scaled_power   = scaled_power,
        status_weight  = sw,
        status_damage  = sdmg,
        ap_cost        = ap,
        aoe_multiplier = aoe,
        payload        = payload,
        total_value    = payload - ap,
    )


def total_value(seed: dict) -> float:
    """Convenience accessor for just the final combat value figure."""
    return compute_ability_value(seed).total_value
