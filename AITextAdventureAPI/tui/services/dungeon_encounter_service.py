"""
dungeon_encounter_service: encounter detection and hostile generation for
the dungeon TUI screen.

Mirrors `old/game_screens/dungeon_screen.py`'s
`_simulate_check_random_encounter()` and the boss-mob path inside
`run_dungeon_screen()`, but stops short of running any blocking UI.

Hostile generation delegates to `generate_random_dungeon_mob()` from the
legacy `old/run_combat_simulator.py`. Combat UI is owned by the caller
(`DungeonScreen`) which pushes the native `tui/screens/combat_screen.py`
and reacts through a `push_screen` callback.
"""
from __future__ import annotations

import random
from typing import Any, List, Optional


def get_dungeon_setting(dungeon: Any) -> Optional[dict]:
    """Return the DUNGEON_SETTINGS entry for this dungeon, or None."""
    import game.constants as const  # noqa: PLC0415

    for ds in const.DUNGEON_SETTINGS:
        if ds.get("dungeon_id") == dungeon.id:
            return ds
    return None


def check_random_encounter(dungeon: Any, pg: Any, force: bool = False) -> bool:
    """Return True if a random dungeon encounter should fire.

    Mirrors the 8% roll used in
    `old/game_screens/dungeon_screen._check_for_random_mob_encounter()`.
    When `force` is True the result is always True (matches legacy
    `force_combat` flag triggered by the countdown timer).
    """
    rng = random.Random()
    return force or rng.random() < 0.08


def get_random_encounter_hostiles(dungeon: Any, pg: Any, force: bool = False) -> List[Any]:
    """Generate and return a random dungeon mob, or an empty list.

    Mirrors `old/game_screens/dungeon_screen._simulate_check_random_encounter()`.
    Returns [] if no encounter fires or if generation fails.
    """
    from run_combat_simulator import generate_random_dungeon_mob  # noqa: PLC0415

    if not check_random_encounter(dungeon, pg, force=force):
        return []

    try:
        ds = get_dungeon_setting(dungeon)
        hostile_seeds = ds.get("hostile_seeds", {}) if ds else {}
        max_level = pg.get_max_character_level()
        return generate_random_dungeon_mob(3, max_level, hostile_seeds)
    except Exception:
        return []


def get_boss_encounter_hostiles(dungeon: Any, pg: Any) -> List[Any]:
    """Generate hostiles for the pending boss encounter.

    Mirrors the `pg.pending_fight_mob_id` check in
    `old/game_screens/dungeon_screen.run_dungeon_screen()`.
    Returns [] if no boss is pending or if resolution fails.
    Clears `pg.pending_fight_mob_id` on failure so the game doesn't soft-lock.
    """
    mob_id = getattr(pg, "pending_fight_mob_id", None)
    if not mob_id:
        return []

    try:
        hostiles = dungeon.get_boss_mob(pg, mob_id)
        if hostiles:
            return hostiles
    except Exception:
        pass

    pg.pending_fight_mob_id = None
    return []