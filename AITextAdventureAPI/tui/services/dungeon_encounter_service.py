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
            from game.dev_diagnostics import dev_log  # noqa: PLC0415
            names = ', '.join(getattr(h, 'name', '?') for h in hostiles)
            dev_log(
                f'boss fight starting for {mob_id} with {len(hostiles)} '
                f'hostile(s): {names}',
                source='dungeon_encounter_service',
            )
            return hostiles
    except Exception as exc:  # noqa: BLE001
        # Surface the failure to the dev-only diagnostic channel instead of
        # silently clearing the pending fight (which looks like the boss fight
        # just never happened). Never touches the player's info-dialog queue.
        import traceback  # noqa: PLC0415
        from game.dev_diagnostics import dev_log  # noqa: PLC0415
        dev_log(
            f'get_boss_mob({mob_id}) raised: {exc}\n{traceback.format_exc()}',
            source='dungeon_encounter_service',
        )

    # Reaching here means get_boss_mob returned falsy (None/[]) or raised. The
    # per-step reasons were already emitted inside get_boss_mob; add one more so
    # the clear-and-skip is visible rather than silent.
    from game.dev_diagnostics import dev_log  # noqa: PLC0415
    dev_log(
        f'No boss hostiles resolved for pending fight {mob_id}; '
        'clearing pending fight (no combat will start).',
        source='dungeon_encounter_service',
    )

    pg.pending_fight_mob_id = None
    return []