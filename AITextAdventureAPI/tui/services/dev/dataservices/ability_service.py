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
    if base_power:
        lines.append(f"Power    : {base_power}")
    if elements:
        elem_str = "  ".join(_ELEMENT_CHARS.get(str(e).lower(), f"({e})") for e in elements)
        lines.append(f"Elements : {elem_str}")
    if status_keys:
        lines.append(f"Statuses : {', '.join(status_keys)}")
    lines.append(f"AOE      : {'Yes' if can_aoe else 'No'}")
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

    for type_id in _TYPE_ORDER:
        level_map  = by_type_level[type_id]
        level_nodes: List[AbilityLevelNode] = []
        for level in sorted(level_map.keys()):
            seeds = level_map[level]
            ability_nodes: List[AbilityNode] = []
            for seed in seeds:
                aid  = str(seed.get("id", "?"))
                name = str(seed.get("name", aid))
                record = DevRecord(
                    category="ability",
                    id=aid,
                    name=name,
                    subtitle=_ability_label(seed),
                    detail=_ability_detail(seed),
                    extras={
                        "level":        level,
                        "ability_type": type_id,
                        "effect":       str(seed.get("effect", "") or ""),
                        "ap_cost":      int(seed.get("ap_cost", 0) or 0),
                        "base_power":   int(seed.get("base_power", 0) or 0),
                        "can_aoe":      bool(seed.get("can_aoe", False)),
                        "status_keys":  list(seed.get("status_keys") or []),
                        "elements":     list(seed.get("elements") or []),
                        "_seed":        seed,   # kept for validator
                    },
                )
                ability_nodes.append(AbilityNode(
                    ability_id=aid,
                    label=name,
                    ability_type=type_id,
                    level=level,
                    record=record,
                ))
            level_nodes.append(AbilityLevelNode(
                level=level,
                label=f"Level {level}",
                abilities=ability_nodes,
            ))
        _ABILITY_TREE.append(AbilityTypeNode(
            type_id=type_id,
            label=_TYPE_LABELS[type_id],
            level_buckets=level_nodes,
        ))


def filter_ability_tree(
    tree: List[AbilityTypeNode],
    query: str = "",
) -> List[AbilityTypeNode]:
    """Return a pruned copy of *tree* matching *query* (case-insensitive)."""
    if not query:
        return tree
    q = query.strip().lower()
    result: List[AbilityTypeNode] = []
    for type_node in tree:
        type_matches = q in type_node.label.lower() or q in type_node.type_id.lower()
        filtered_levels: List[AbilityLevelNode] = []
        for level_node in type_node.level_buckets:
            level_matches = q in level_node.label.lower()
            if type_matches or level_matches:
                filtered_levels.append(level_node)
            else:
                abilities = [
                    a for a in level_node.abilities
                    if q in a.ability_id.lower()
                    or q in a.label.lower()
                    or q in a.record.detail.lower()
                ]
                if abilities:
                    filtered_levels.append(AbilityLevelNode(
                        level=level_node.level,
                        label=level_node.label,
                        abilities=abilities,
                    ))
        if filtered_levels:
            result.append(AbilityTypeNode(
                type_id=type_node.type_id,
                label=type_node.label,
                level_buckets=filtered_levels,
            ))
    return result