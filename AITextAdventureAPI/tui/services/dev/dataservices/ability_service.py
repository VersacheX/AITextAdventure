"""
Ability tree: builder, filter, and module-level cache.
get_ability_tree() lives in catalog.py to avoid circular imports.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List

from tui.services.dev.dataservices.models import (
    AbilityLevelNode,
    AbilityNode,
    AbilityTypeNode,
    DevRecord,
)

# ── Module-level tree cache (mutated by catalog._load_all) ────────────────
_ABILITY_TREE: List[AbilityTypeNode] = []

_TYPE_ORDER = ["technique", "faith", "magic", "tech", "skill"]
_TYPE_LABELS: Dict[str, str] = {
    "technique": "Technique",
    "faith":     "Faith",
    "magic":     "Magic",
    "tech":      "Tech",
    "skill":     "Skill",
}
_EFFECT_LABELS: Dict[str, str] = {
    "damage": "Damage",
    "heal":   "Heal",
    "status": "Status",
    "revive": "Revive",
    "cure":   "Cure",
}
_ELEMENT_CHARS: Dict[str, str] = {
    "dark": "(D)", "light": "(L)", "earth": "(Ë)", "fire": "(F)",
    "water": "(W)", "air": "(A)", "ice": "(I)", "electric": "(É)",
}


def _flat_ability_nodes(tree: List[AbilityTypeNode]) -> List[AbilityNode]:
    """Return every AbilityNode from *tree* as a flat list."""
    out: List[AbilityNode] = []
    for type_node in tree:
        for level_node in type_node.level_buckets:
            out.extend(level_node.abilities)
    return out


def _ability_label(seed: dict) -> str:
    name    = str(seed.get("name", seed.get("id", "?")))
    level   = int(seed.get("level", 1) or 1)
    atype   = str(seed.get("ability_type", "") or "")
    effect  = str(seed.get("effect", "") or "")
    elements = seed.get("elements") or []
    elem_str = "".join(_ELEMENT_CHARS.get(str(e).lower(), "") for e in elements)
    type_abbr   = _TYPE_LABELS.get(atype, atype[:4].title())
    effect_abbr = _EFFECT_LABELS.get(effect, effect[:4].title())
    return f"{name}  [dim]Lv.{level}  {type_abbr}  {effect_abbr}  {elem_str}[/dim]"


def _ability_detail(seed: dict) -> str:
    lines: list[str] = []
    desc        = str(seed.get("description", "") or "")
    atype       = str(seed.get("ability_type", "") or "")
    level       = int(seed.get("level", 1) or 1)
    elements    = seed.get("elements") or []
    base_power  = seed.get("base_power", 0)
    ap_cost     = seed.get("ap_cost", 0)
    effect      = str(seed.get("effect", "") or "")
    status_keys = seed.get("status_keys") or []
    can_aoe     = seed.get("can_aoe", False)

    if desc:
        lines.append(desc)
        lines.append("")

    lines.append(f"Type     : {_TYPE_LABELS.get(atype, atype.title())}")
    lines.append(f"Level    : {level}")
    lines.append(f"Effect   : {_EFFECT_LABELS.get(effect, effect.title())}")
    lines.append(f"AP Cost  : {ap_cost}")
    lines.append(f"Power    : {base_power}")
    # Status abilities usually declare base_power 0 yet several apply damaging
    # statuses (e.g. continuous_damage).  Surface the DoT weight bonus separately
    # so the panel reflects real combat value without overriding base_power.
    if effect == "status" and status_keys:
        from tui.services.dev.dataservices.ability_value_calculator import (
            status_power_estimate,
        )
        est = status_power_estimate(seed)
        if est:
            lines.append(f"DoT Bonus: +{est:.1f} (weight)")
    if elements:
        elem_str = "  ".join(_ELEMENT_CHARS.get(str(e).lower(), f"({e})") for e in elements)
        lines.append(f"Elements : {elem_str}")
    if status_keys:
        lines.append(f"Statuses : {', '.join(status_keys)}")
    lines.append(f"AOE      : {'Yes' if can_aoe else 'No'}")

    # ── Calculated value breakout ─────────────────────────────────────────
    # Show the same combat-value components the validator uses for its balance
    # and AP-outlier notices, so the numbers behind a WARN/NOTICE are visible.
    # NOTE: this string is rich-escaped by the detail panel, so it must stay
    # plain text (no [dim]/markup tags — they would render literally).
    from tui.services.dev.dataservices.ability_value_calculator import (
        compute_ability_value,
    )
    v = compute_ability_value(seed)
    lines.append("")
    lines.append("-- Calculated Value --")
    lines.append(f"Scaled Power : {v.scaled_power:.1f}")
    if v.status_weight:
        lines.append(f"Status Weight: {v.status_weight:.1f}")
    if v.status_damage:
        lines.append(f"DoT Bonus    : {v.status_damage:.1f} (weight)")
    if v.aoe_multiplier != 1.0:
        lines.append(f"AOE x{v.aoe_multiplier:g}    : {v.payload:.1f} (payload)")
    from tui.services.dev.dataservices.ability_value_calculator import AP_COST_WEIGHT
    lines.append(f"AP Cost      : -{v.ap_cost * AP_COST_WEIGHT:.3f} ({v.ap_cost:.0f} x{AP_COST_WEIGHT:g})")
    lines.append(f"Total Value  : {v.total_value:.3f}")
    if v.ap_cost > 0 and v.payload > 0:
        lines.append(f"Value/AP     : {v.payload / v.ap_cost:.2f} (payload per AP)")
    return "\n".join(lines)


def _build_ability_tree(const: Any) -> None:
    """Rebuild _ABILITY_TREE from const.PLAYER_ABILITY_SEEDS."""
    global _ABILITY_TREE
    _ABILITY_TREE.clear()

    # Group seeds by (type, level)
    by_type_level: Dict[str, Dict[int, List[dict]]] = {
        t: defaultdict(list) for t in _TYPE_ORDER
    }
    other: Dict[int, List[dict]] = defaultdict(list)

    for seed in getattr(const, "PLAYER_ABILITY_SEEDS", []) or []:
        if not isinstance(seed, dict):
            continue
        atype = str(seed.get("ability_type", "") or "").lower()
        level = int(seed.get("level", 1) or 1)
        if atype in by_type_level:
            by_type_level[atype][level].append(seed)
        else:
            other[level].append(seed)

    for atype in _TYPE_ORDER:
        level_map = by_type_level[atype]
        if not level_map:
            continue
        buckets: List[AbilityLevelNode] = []
        for level in sorted(level_map.keys()):
            seeds = level_map[level]
            abilities: List[AbilityNode] = []
            for seed in seeds:
                ability_id = str(seed.get("id", ""))
                name       = str(seed.get("name", ability_id))
                label      = _ability_label(seed)
                record     = DevRecord(
                    category="ability",
                    id=ability_id,
                    name=name,
                    subtitle=f"Lv.{level} {_TYPE_LABELS.get(atype, atype)}",
                    detail=_ability_detail(seed),
                    extras={"_seed": seed},
                )
                abilities.append(AbilityNode(
                    ability_id=ability_id,
                    label=name,
                    ability_type=atype,
                    level=level,
                    record=record,
                ))
            buckets.append(AbilityLevelNode(
                level=level,
                label=f"Level {level}",
                abilities=abilities,
            ))
        _ABILITY_TREE.append(AbilityTypeNode(
            type_id=atype,
            label=_TYPE_LABELS.get(atype, atype.title()),
            level_buckets=buckets,
        ))

    # Any ability types not in _TYPE_ORDER
    if other:
        buckets = []
        for level in sorted(other.keys()):
            seeds = other[level]
            abilities = []
            for seed in seeds:
                ability_id = str(seed.get("id", ""))
                name       = str(seed.get("name", ability_id))
                label      = _ability_label(seed)
                record     = DevRecord(
                    category="ability",
                    id=ability_id,
                    name=name,
                    subtitle=f"Lv.{level} Other",
                    detail=_ability_detail(seed),
                    extras={"_seed": seed},
                )
                abilities.append(AbilityNode(
                    ability_id=ability_id,
                    label=name,
                    ability_type=str(seed.get("ability_type", "") or ""),
                    level=level,
                    record=record,
                ))
            buckets.append(AbilityLevelNode(level=level, label=f"Level {level}", abilities=abilities))
        _ABILITY_TREE.append(AbilityTypeNode(type_id="other", label="Other", level_buckets=buckets))


def filter_ability_tree(
    tree: List[AbilityTypeNode],
    query: str = "",
) -> List[AbilityTypeNode]:
    """Return a filtered copy of *tree* matching *query* against ability id/name."""
    if not query:
        return tree
    q = query.lower()
    result: List[AbilityTypeNode] = []
    for type_node in tree:
        matching_buckets: List[AbilityLevelNode] = []
        for level_node in type_node.level_buckets:
            matching = [
                a for a in level_node.abilities
                if q in a.ability_id.lower() or q in a.label.lower()
            ]
            if matching:
                matching_buckets.append(AbilityLevelNode(
                    level=level_node.level,
                    label=level_node.label,
                    abilities=matching,
                ))
        if matching_buckets:
            result.append(AbilityTypeNode(
                type_id=type_node.type_id,
                label=type_node.label,
                level_buckets=matching_buckets,
            ))
    return result