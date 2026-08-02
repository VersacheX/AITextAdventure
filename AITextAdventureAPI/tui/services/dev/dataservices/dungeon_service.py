"""
Dungeon tree: builder, filter, and module-level cache.
get_dungeon_tree() lives in catalog.py to avoid circular imports.

Tree shape:  Group (Main Story / Primary Story / City & Regional) → Dungeon leaf
"""
from __future__ import annotations

from typing import Any, Dict, List

from tui.services.dev.dataservices.models import (
    DevRecord,
    DungeonGroupNode,
    DungeonNode,
)

# ── Module-level tree cache (mutated by catalog._load_all) ────────────────
_DUNGEON_TREE: List[DungeonGroupNode] = []

_GROUP_ORDER = ["main_story", "primary_story", "city_regional"]
_GROUP_LABELS: Dict[str, str] = {
    "main_story":     "Main Story",
    "primary_story":  "Primary Story",
    "city_regional":  "City & Regional",
}

# Primary story boss dungeon_id fragments (from primary_stories/ seeds)
_PRIMARY_STORY_FRAGMENTS = frozenset({
    "zaruun", "marrowroot", "serene_lair", "rokhuld", "uulthar",
    "aeriola", "miregloom",
})

# City/regional dungeon_id fragments — checked BEFORE primary story to
# prevent city dungeons sharing a boss name from being mis-classified.
_CITY_REGIONAL_FRAGMENTS = frozenset({
    "murkchannel", "rotfen", "swallowed_path",
    "swamp_mid_city", "miregloom_resurrection",
    "shallows_large_city", "shallows_mid_city", "shallows_small_city", "uulthars",
    "mountains_large_city", "mountains_mid_emberwake", "rokhulls_fracture",
    "desert_large_city", "desert_mid_ink", "desert_mid_city", "desert_small_city",
    "zaruuns_sanctum",
    "forest_large_city", "forest_mid_city", "forest_small_city", "marrowroots_deep",
    "grassland_large_city", "grassland_mid_city", "serenes_wind",
    "snow_large_city", "snow_mid_city", "aeriolass_frozen",
    "stormhollow",
    "ghost_hideaway",
    "windcarve_den",
    "charmroot_den",
    "relicmire_sump",
    "fogwhisper_inlet",
    "coveveil_passage",
})


def _classify_dungeon(dungeon_id: str) -> str:
    """Classify a dungeon_id into its source group.

    City/regional fragments are checked first so that city dungeons whose
    boss names also appear in _PRIMARY_STORY_FRAGMENTS (e.g. zaruun,
    miregloom, rokhuld) are not mis-classified as primary_story.
    """
    did_lower = dungeon_id.lower()
    for fragment in _CITY_REGIONAL_FRAGMENTS:
        if fragment in did_lower:
            return "city_regional"
    for fragment in _PRIMARY_STORY_FRAGMENTS:
        if fragment in did_lower:
            return "primary_story"
    return "main_story"


def _build_dungeon_tree(const: Any) -> None:
    """Rebuild _DUNGEON_TREE from const.DUNGEON_SETTINGS."""
    global _DUNGEON_TREE
    _DUNGEON_TREE.clear()

    by_group: Dict[str, List[DungeonNode]] = {g: [] for g in _GROUP_ORDER}

    for ds in getattr(const, "DUNGEON_SETTINGS", []) or []:
        if not isinstance(ds, dict):
            continue
        did   = str(ds.get("dungeon_id") or ds.get("id") or "")
        if not did:
            continue
        name  = str(ds.get("display_name", did))
        group = _classify_dungeon(did)

        floors   = ds.get("floor_count", 1)
        rooms    = ds.get("rooms_per_floor", "?")
        hostile_count = len(ds.get("hostile_seeds") or [])
        boss_count    = len(ds.get("boss_hostiles") or [])
        npc_count     = len(ds.get("npcs") or [])
        item_count    = len(ds.get("items") or [])

        subtitle = (
            f"{floors}F · {rooms}R  |  "
            f"{hostile_count} hostile{'s' if hostile_count != 1 else ''}  "
            f"{boss_count} boss  "
            f"{npc_count} NPC{'s' if npc_count != 1 else ''}  "
            f"{item_count} item{'s' if item_count != 1 else ''}"
        )

        record = DevRecord(
            category="dungeon",
            id=did,
            name=name,
            subtitle=subtitle,
            detail="",   # filled by detail panel from settings
            extras={
                "open_area_tile":   ds.get("open_area_tile",   "."),
                "impassable_tile":  ds.get("impassable_tile",  "#"),
                "border_tile":      ds.get("border_tile",      "*"),
                "open_area_color":  ds.get("open_area_color"),
                "impassable_color": ds.get("impassable_color"),
                "border_color":     ds.get("border_color"),
                "floors":           floors,
                "rooms":            rooms,
                "visible_distance": ds.get("visible_distance", 5),
            },
        )
        node = DungeonNode(
            dungeon_id=did,
            label=name,
            group_id=group,
            record=record,
            settings=ds,
        )
        by_group[group].append(node)

    for group_id in _GROUP_ORDER:
        nodes = sorted(by_group[group_id], key=lambda n: n.label)
        if not nodes:
            continue
        _DUNGEON_TREE.append(DungeonGroupNode(
            group_id=group_id,
            label=_GROUP_LABELS[group_id],
            dungeons=nodes,
        ))


def filter_dungeon_tree(
    tree: List[DungeonGroupNode],
    query: str = "",
) -> List[DungeonGroupNode]:
    """Return a filtered view of the dungeon tree matching query."""
    if not query:
        return tree
    q = query.lower()
    result: List[DungeonGroupNode] = []
    for group in tree:
        matched = [
            d for d in group.dungeons
            if q in d.dungeon_id.lower() or q in d.label.lower()
        ]
        if matched:
            result.append(DungeonGroupNode(
                group_id=group.group_id,
                label=group.label,
                dungeons=matched,
            ))
    return result