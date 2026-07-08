"""
location_actions: detect all available actions at the player's current
tile and return them as a structured list.

Mirrors the action-detection block from `old/console_game_gameloop.py`.
Sublocation actions store the tile coordinates at detection time so
LocationOverlay can pass the exact position to `loot_sublocation` even
if the player has moved since the overlay was shown.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List


@dataclass
class LocationAction:
    """A single available action at the player's current tile."""

    id: str
    label: str
    kind: str   # npc | shop | sublocation | floor_up | floor_down | travel | aircraft_enter | aircraft_land
    data: Any = None


def get_location_actions(pg: Any, active_area: Any) -> List[LocationAction]:
    """Return all available actions at the player's current position."""
    actions: List[LocationAction] = []
    if pg is None or active_area is None:
        return actions

    # ── NPC interaction ───────────────────────────────────────────────────
    try:
        can_interact, npc_name, npc_id = pg._can_npc_interact_at_player_location()
        if can_interact and npc_name:
            actions.append(LocationAction(
                id=f"npc_{npc_id}",
                label=f"Talk to {npc_name}",
                kind="npc",
                data={"npc_id": npc_id, "npc_name": npc_name},
            ))
    except Exception:
        pass

    # ── Shop ─────────────────────────────────────────────────────────────
    try:
        can_shop, business_def = active_area._is_location_shop_first_floor(pg)
        if can_shop and business_def:
            shop_name = business_def.get("display_name", "Shop")
            actions.append(LocationAction(
                id="shop",
                label=f"Shop at {shop_name}",
                kind="shop",
                data={"business_def": business_def},
            ))
    except Exception:
        pass

    # ── Sublocations ──────────────────────────────────────────────────────
    # (x, y, z) are stored in data so loot_sublocation can find the right
    # subloc even if the player moves before confirming the loot dialog.
    try:
        sublocs = active_area.get_sublocation_at((pg.x, pg.y, pg.z)) or []
        for sl in sublocs:
            name = sl.get("name", "Unknown")
            mode = sl.get("mode", "searchable")
            prompt = sl.get("prompt") or f"Examine the {name}"
            has_loot = (
                sl.get("loot") is not None
                or int(sl.get("money", 0) or 0) > 0
            )
            if mode == "searchable":
                label = f"Search: {name}"
            else:
                label = prompt
            actions.append(LocationAction(
                id=f"subloc_{name}",
                label=label,
                kind="sublocation",
                data={
                    "subloc": sl,
                    "name": name,
                    "has_loot": has_loot,
                    "x": pg.x,
                    "y": pg.y,
                    "z": pg.z,
                },
            ))
    except Exception:
        pass

    # ── Floor up / down ───────────────────────────────────────────────────
    try:
        from services.player_movement_service import get_floor_options
        can_up, can_down = get_floor_options(active_area, pg)
        if can_up:
            actions.append(LocationAction(id="floor_up", label="Go up a floor", kind="floor_up"))
        if can_down:
            actions.append(LocationAction(id="floor_down", label="Go down a floor", kind="floor_down"))
    except Exception:
        pass

    # ── Fast travel (Hyperway) ────────────────────────────────────────────
    try:
        if active_area._can_travel_from_player_location(pg):
            actions.append(LocationAction(id="travel", label="Fast Travel (Hyperway)", kind="travel"))
    except Exception:
        pass

    # ── Aircraft ─────────────────────────────────────────────────────────
    try:
        at_aircraft = getattr(pg, "aircraft_location", None) == (pg.x, pg.y)
        inside_aircraft = getattr(pg, "inside_aircraft", False)
        if at_aircraft and not inside_aircraft:
            actions.append(LocationAction(id="aircraft_enter", label="Enter aircraft", kind="aircraft_enter"))
        if inside_aircraft:
            actions.append(LocationAction(id="aircraft_land", label="Land aircraft", kind="aircraft_land"))
    except Exception:
        pass

    return actions