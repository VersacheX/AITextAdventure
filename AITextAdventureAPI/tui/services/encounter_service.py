"""
encounter_service: handles random encounter checks and boss fights.

Mirrors the console game's encounter flow:
  1. After each player action (movement, interaction), countdown the
     random_encounter_timer via `pg.countdown_random_encounter_timer()`.
  2. If the timer hits zero, generate a random encounter.
  3. If `pg.pending_fight_mob_id` is set, trigger a boss fight.

The console game calls these checks in `run_game_loop()` after `took_action`
is True. The TUI mirrors this by calling `check_and_handle_encounters()`
after every successful move or action in `OverworldScreen`.

Hostile generation delegates to `tui/services/combat_service.py`, which in
turn mirrors the hostile-generation half of the legacy
`old/game_screens/overworld_screen.py` functions
(`simulate_check_random_encounter()` / `handle_pending_boss_encounter()`).
Unlike those legacy versions, resolving combat itself no longer happens
here — `OverworldScreen` pushes the native `tui/screens/combat_screen.py`
and reacts to its result through a `push_screen` callback instead of
blocking on a returned bool.
"""
from __future__ import annotations

from typing import Any, List, Optional


def check_and_handle_encounters(pg: Any, active_area: Any) -> Optional[List[str]]:
    """Check for pending boss fights and random encounters.

    Returns a list of dialog messages to display if an encounter is triggered,
    or None if no encounter occurred. The caller is responsible for showing
    these messages and then transitioning to the combat screen.

    Mirrors the console game's sequence:
      1. Check for pending boss fight (`pg.pending_fight_mob_id`)
      2. Check for random encounter via `pg.countdown_random_encounter_timer()`

    Args:
        pg: PlayerGame instance
        active_area: The active region or city the player is in

    Returns:
        List of message strings if an encounter occurs, None otherwise.
    """
    messages: List[str] = []

    # Check for pending boss fight first (highest priority)
    if getattr(pg, "pending_fight_mob_id", None):
        messages.append("A powerful foe blocks your path!")
        messages.append("Prepare for battle!")
        # The actual combat initiation happens after messages are displayed
        return messages

    # Check if player is in a dungeon (dungeons handle their own encounters)
    dungeon = pg.get_dungeon_at_position()
    if dungeon:
        return None

    # Check if area is safe (safe areas don't have random encounters)
    try:
        if active_area and active_area.is_safe_area(pg):
            return None
    except (KeyError, AttributeError):
        pass  # tile not in area or no is_safe_area method → treat as unsafe

    # Check if phased or in aircraft (no encounters in these states)
    if getattr(pg, "phased", False) or getattr(pg, "inside_aircraft", False):
        return None

    # Countdown the encounter timer
    is_encounter = pg.countdown_random_encounter_timer()

    if is_encounter:
        messages.append("You sense danger approaching...")
        messages.append("An enemy appears!")
        return messages

    return None


def get_boss_encounter_hostiles(pg: Any) -> Optional[List[Any]]:
    """Generate hostiles for the pending boss encounter, if any.

    Delegates to `tui/services/combat_service.py`, which mirrors the
    hostile-resolution half of the legacy `handle_pending_boss_encounter()`.

    Returns None if there's no pending boss fight, or the boss id/hostile
    seeds couldn't be resolved — in the unresolved case,
    `pg.pending_fight_mob_id` is cleared here, matching the legacy fallback
    of treating an unknown boss id as a no-op rather than a soft-lock.
    """
    from tui.services.combat_service import generate_boss_encounter_hostiles  # noqa: PLC0415

    hostiles = generate_boss_encounter_hostiles(pg)
    if not hostiles:
        pg.pending_fight_mob_id = None
        return None
    return hostiles


def get_random_encounter_hostiles(pg: Any, active_area: Any) -> List[Any]:
    """Generate hostiles for a random overworld encounter.

    Delegates to `tui/services/combat_service.py`, which mirrors the
    hostile-generation half of the legacy `simulate_check_random_encounter()`.
    Returns an empty list if generation fails for any reason, so callers can
    treat that as "no encounter" rather than crashing the overworld loop.
    """
    from tui.services.combat_service import generate_random_encounter_hostiles  # noqa: PLC0415

    try:
        return generate_random_encounter_hostiles(pg, active_area)
    except Exception:
        return []