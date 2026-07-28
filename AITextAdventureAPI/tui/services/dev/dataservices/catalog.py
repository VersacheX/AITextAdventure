"""
Central catalog: CATEGORIES, caches, preload, get_records, and tree getters.
"""
from __future__ import annotations

from typing import Any, Dict, List, Tuple

from tui.services.dev.dataservices.models import (
    AbilityTypeNode,
    DevRecord,
    DialogueActNode,
    DungeonGroupNode,
    HostileRarityNode,
    NpcGroupNode,
    TimelineGroupNode,
)
from tui.services.dev.dataservices.dialogue_service import (
    _DIALOG_INDEX,
    _DIALOG_TREE,
    _NAME_BY_ID,
    _build_dialogue_tree,
)
from tui.services.dev.dataservices.timeline_service import (
    _TIMELINE_TREE,
    _build_timeline_tree,
)
from tui.services.dev.dataservices.npc_service import (
    _NPC_TREE,
    _build_npc_tree,
)
from tui.services.dev.dataservices.ability_service import (
    _ABILITY_TREE,
    _build_ability_tree,
)
from tui.services.dev.dataservices.hostile_service import (
    _HOSTILE_TREE,
    _build_hostile_tree,
)
from tui.services.dev.dataservices.dungeon_service import (
    _DUNGEON_TREE,
    _build_dungeon_tree,
)
from tui.services.dev.dataservices.record_builders import (
    _build_characters,
    _build_cities,
    _build_dungeons,
    _build_equipment,
    _build_accessories,
    _build_items,
    _build_special_items,
)

CATEGORIES: Tuple[str, ...] = (
    "character",
    "timeline",
    "item",
    "special_item",
    "equipment",
    "dungeon",
    "city",
    "npc",
    "character_dialog",
    "ability",
    "hostile",
    "simulation",
)

CATEGORY_LABELS: Dict[str, str] = {
    "character":        "Characters",
    "timeline":         "Timeline",
    "item":             "Items",
    "special_item":     "Special Items",
    "equipment":        "Equipment",
    "dungeon":          "Dungeons",
    "city":             "Cities",
    "npc":              "NPCs",
    "character_dialog": "Dialogue",
    "ability":          "Abilities",
    "hostile":          "Hostiles",
    "simulation":       "Simulation",
}

_CACHE: Dict[str, List[DevRecord]] = {}


def preload() -> None:
    """Eagerly build and cache every category.  Call once from a background worker."""
    if _CACHE:
        return
    _load_all()


def get_records(category: str) -> List[DevRecord]:
    """Return every DevRecord for category, building on first use."""
    if not _CACHE:
        _load_all()
    return _CACHE.get(category, [])


def search_records(category: str, query: str) -> List[DevRecord]:
    """Return records in category matching query (case-insensitive)."""
    return [r for r in get_records(category) if r.matches(query)]


def filter_equipment_records(type_query: str = "", slot_query: str = "") -> List[DevRecord]:
    """Filter equipment records by type (weapon/armor/accessory) and armor slot."""
    preload()
    all_equipment = _CACHE.get("equipment", [])
    if not type_query and not slot_query:
        return all_equipment
    type_lower = type_query.lower()
    slot_lower = slot_query.lower()
    filtered = []
    for record in all_equipment:
        tl = record.extras.get("type_label", "").lower()
        if type_lower:
            if type_lower == "weapon" and not tl.startswith("weapon"):
                continue
            if type_lower == "armor" and not tl.startswith("armor"):
                continue
            if type_lower == "accessory" and tl != "accessory":
                continue
        if slot_lower:
            if not tl.startswith("armor"):
                continue
            if slot_lower not in tl:
                continue
        filtered.append(record)
    return filtered


def get_dialogue_tree() -> List[DialogueActNode]:
    """Return the cached Act → Chapter → Task → stage → line tree."""
    if not _CACHE:
        _load_all()
    return _DIALOG_TREE


def get_timeline_tree() -> List[TimelineGroupNode]:
    """Return the cached group → bucket → task tree."""
    if not _CACHE:
        _load_all()
    return _TIMELINE_TREE


def get_npc_tree() -> List[NpcGroupNode]:
    """Return the cached group → NPC tree."""
    if not _CACHE:
        _load_all()
    return _NPC_TREE


def get_ability_tree() -> List[AbilityTypeNode]:
    if not _CACHE:
        _load_all()
    return _ABILITY_TREE


def get_hostile_tree() -> List[HostileRarityNode]:
    """Return the cached Rarity → Level bucket → Hostile tree."""
    if not _CACHE:
        _load_all()
    return _HOSTILE_TREE


def get_dungeon_tree() -> List[DungeonGroupNode]:
    """Return the cached Group → Dungeon tree."""
    if not _CACHE:
        _load_all()
    return _DUNGEON_TREE


def get_dialog_index() -> Dict[Tuple[Any, Any], List[str]]:
    if not _CACHE:
        _load_all()
    return _DIALOG_INDEX


def get_npc_names() -> Dict[str, str]:
    """Return the npc_id → display name map built from NPCS + PLAYER_NPCS."""
    if not _CACHE:
        _load_all()
    return _NAME_BY_ID


def _load_all() -> None:
    """Build and cache records for every category from game.constants."""
    import game.constants as const

    _CACHE["character"]        = _build_characters(const)
    _CACHE["timeline"]         = []  # tree category; use get_timeline_tree()
    _CACHE["item"]             = _build_items(const)
    _CACHE["special_item"]     = _build_special_items(const)
    _CACHE["equipment"]        = _build_equipment(const) + _build_accessories(const)
    _CACHE["dungeon"]          = _build_dungeons(const)
    _CACHE["city"]             = _build_cities(const)
    _CACHE["npc"]              = []
    _CACHE["character_dialog"] = []
    _CACHE["ability"]          = []   # tree category; use get_ability_tree()
    _CACHE["hostile"]          = []   # tree category; use get_hostile_tree()
    _CACHE["simulation"]       = []

    _DIALOG_TREE.clear()
    _DIALOG_TREE.extend(_build_dialogue_tree(const))

    _TIMELINE_TREE.clear()
    _TIMELINE_TREE.extend(_build_timeline_tree(const))

    _NPC_TREE.clear()
    _NPC_TREE.extend(_build_npc_tree(const))

    _build_ability_tree(const)

    _build_hostile_tree(const)

    _build_dungeon_tree(const)