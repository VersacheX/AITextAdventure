"""
movement_service: TUI adapter over the legacy `old/services/player_movement_service`.

The legacy service contains all movement validation logic
(`get_allowed_moves`, `handle_movement_key`) and is the authoritative
source of truth for movement rules. This module:

  1. Resolves the correct `active_area` from the `PlayerGame` for the
     current position (child city when inside one, parent region otherwise)
     — matching what `old/console_game_gameloop.py` does at the top of
     every loop iteration.
  2. Wraps those calls in a clean interface so `OverworldScreen` never
     imports from `old/` directly.
  3. Exposes `ensure_tiles_around_sync()` for use in a background worker —
     `pg.ensure_tiles_around()` can be slow when generating a new region,
     so it must not block the Textual compositor thread.

Key → direction mapping
  w / up    → north
  s / down  → south
  a / left  → west
  d / right → east
"""
from __future__ import annotations

from typing import Any, Optional, Tuple

# Key → DIRECTIONAL_MAPPING key used by the legacy service
_KEY_TO_CMD: dict[str, str] = {
    "w": "w",
    "up": "w",
    "s": "s",
    "down": "s",
    "a": "a",
    "left": "a",
    "d": "d",
    "right": "d",
}


def _resolve_active_area(pg: Any) -> Optional[Any]:
    """Return the active area (child city or parent region) for the
    player's current position, exactly as the legacy game loop does.
    Returns None if the position is unknown (edge of world)."""
    try:
        _, active = pg.get_region_and_active_area_for_position()
        return active
    except Exception:
        return None


def try_move(key: str, pg: Any) -> Tuple[bool, str]:
    """Attempt to move the player one step in the direction bound to `key`.

    Returns (moved: bool, reason: str).  `reason` is empty on success and
    contains a short human-readable explanation on failure (for status bar
    display or debug toasts).

    This is the single entry point OverworldScreen calls on every movement
    key press.  It fully replicates the legacy game-loop movement path:
      1. Resolve the active area for the current position.
      2. Ask the legacy service for allowed moves.
      3. Delegate to the legacy service to apply the move.
    """
    from services.player_movement_service import get_allowed_moves, handle_movement_key  # noqa: PLC0415

    cmd = _KEY_TO_CMD.get(key)
    if not cmd:
        return False, f"unknown key '{key}'"

    active_area = _resolve_active_area(pg)
    if active_area is None:
        return False, "position is outside mapped world"

    allowed = get_allowed_moves(active_area, pg)
    if cmd not in allowed:
        return False, ""  # silently blocked (wall/impassable/building entrance)

    moved = handle_movement_key(cmd, active_area, allowed, 4, pg)
    return moved, "" if moved else "move was blocked"


def ensure_tiles_around_sync(pg: Any, check_rad: int = 4) -> None:
    """Synchronously ensure tiles within `check_rad` of the player exist.

    Call this from a `@work(thread=True)` worker — it may generate a new
    region (expensive) when the player approaches unexplored space.
    The underlying `pg.ensure_tiles_around()` is safe to call from a
    non-compositor thread because it only mutates `pg.world_tiles` and
    `pg.regions`, which are not Textual reactive attributes.
    """
    try:
        pg.ensure_tiles_around(check_rad=check_rad, max_attempts=1)
    except Exception:
        pass  # never crash the worker; the map will just show '?' tiles


def check_random_encounter(pg: Any, active_area: Any) -> bool:
    """Count down the encounter timer and return True if a random encounter
    should fire.  Mirrors the legacy game-loop check:

        if not dungeon and not active_city.is_safe_area(pg):
            is_combat = pg.countdown_random_encounter_timer()
    """
    try:
        dungeon = pg.get_dungeon_at_position()
        if dungeon:
            return False
        # is_safe_area raises KeyError if player is not in active_area.tiles
        try:
            if active_area.is_safe_area(pg):
                return False
        except (KeyError, AttributeError):
            pass  # tile not in area tiles dict → treat as unsafe
        return bool(pg.countdown_random_encounter_timer())
    except Exception:
        return False


def get_active_area(pg: Any) -> Optional[Any]:
    """Return the active area object for the player's current position."""
    return _resolve_active_area(pg)