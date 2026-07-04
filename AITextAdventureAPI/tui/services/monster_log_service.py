"""
monster_log_service: build RandomHostile instances for the Monster Log overlay.

Mirrors the `m` key handler in `old/game_screens/inventory_screen.py`: the
game only stores slain counts keyed by hostile id (`PlayerGame.enemies_slain`),
not full hostile objects, so the seed used to originally spawn each hostile
must be re-located (via `game.constants.HOSTILE_SEED_PATHS`) and re-instantiated
on demand purely for display purposes in the log.
"""
from __future__ import annotations

from typing import Any, Dict, List, Tuple


def build_slain_hostiles(player_game: Any) -> Tuple[List[Any], Dict[str, int]]:
    """Return (hostiles, slain_counts) for every hostile id in
    `player_game.enemies_slain`, re-instantiated from their original seed.

    Ids whose seed source can no longer be located (e.g. removed content)
    are silently skipped rather than raising, matching legacy behavior.
    """
    import game.constants as const
    from combat_balancing_simulation.hostile_seed_engine import generate_hostile_from_legacy_seed

    slain_map: Dict[str, int] = dict(getattr(player_game, "enemies_slain", {}) or {})
    hostiles: List[Any] = []
    for hid in list(slain_map.keys()):
        src_name = const.HOSTILE_SEED_PATHS.get(hid)
        if not src_name:
            continue
        src_list = getattr(const, src_name, None)
        if not src_list:
            continue
        choice = next((s for s in src_list if s.get("id") == hid), None)
        if not choice:
            continue
        try:
            rh = generate_hostile_from_legacy_seed(choice, choice.get("min_spawn_level"))
        except Exception:
            continue
        hostiles.append(rh)

    return hostiles, slain_map