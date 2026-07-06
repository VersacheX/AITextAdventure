"""
combat_service: TUI adapter over the legacy `old/combat_balancing_simulation/combat_simulator`.

`CombatSimulation` (old/combat_balancing_simulation/combat_simulator.py) is
pure simulation logic — no I/O, no blocking input, no terminal rendering —
so it is reused as-is. This module only adds:

  1. Hostile-generation helpers that mirror
     `old/game_screens/overworld_screen.py`'s `simulate_check_random_encounter()`
     and `handle_pending_boss_encounter()`, but stop short of running the
     legacy blocking `CombatScreen` — hostile generation is a pure
     computation, while the actual turn-by-turn UI is owned by
     `tui/screens/combat_screen.py`.
  2. Thin, explicitly-named wrappers around `CombatSimulation` methods so the
     Textual screen never has to know legacy action-dict shapes or reach
     into underscore-prefixed "private" helpers on game objects directly.
  3. `generate_test_party()` / `generate_test_hostiles()` — self-contained
     helpers for the combat simulator dev runner (`run_combat_sim.py`) that
     build a fully-equipped party and a random hostile mob from scratch,
     isolating all `old/` imports so callers stay clean.

None of the functions here block on input or print to the terminal.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


def build_simulation(pg: Any, hostiles: List[Any]) -> Any:
    """Construct a CombatSimulation from a PlayerGame and a hostile list."""
    from combat_balancing_simulation.combat_simulator import CombatSimulation  # noqa: PLC0415

    return CombatSimulation(pg, hostiles)


# ── dev-runner helpers ───────────────────────────────────────────────────────

def generate_test_party(seed: int, num_players: int, level: int) -> Any:
    """Build a fresh PlayerGame with a fully-equipped test party.

    Mirrors the setup portion of `old/run_combat_simulator.py`'s `main()`:
    creates `num_players` characters at `level` using `generate_player_character()`
    and hands each of them starter heal/AP potions via `get_beginning_items()`.
    All `old/` imports are localised here so `run_combat_sim.py` stays clean.

    Returns the populated `PlayerGame` instance.
    """
    from game.objects.player_game import PlayerGame  # noqa: PLC0415
    from run_combat_simulator import (  # noqa: PLC0415
        generate_player_character,
        get_beginning_items,
    )

    pg = PlayerGame()
    current_seed = seed
    for _ in range(num_players):
        player = generate_player_character(seed=current_seed, level=level, player_game=pg)
        current_seed += 1
        get_beginning_items(player, pg, max_heals=5, max_ap=2)
        pg.add_character(player)
    return pg


def generate_test_hostiles(level: int, num_hostiles: int, region_key: Optional[str] = None) -> List[Any]:
    """Generate a random hostile mob for the dev runner.

    Wraps `generate_random_mob()` from `old/run_combat_simulator.py`, passing
    through the optional `region_key` so callers can pin a specific region's
    hostile seed table or leave it as `None` to pick at random.
    """
    from run_combat_simulator import generate_random_mob  # noqa: PLC0415

    return generate_random_mob(num_hostiles, level, region_key)


# ── hostile generation (mirrors old/game_screens/overworld_screen.py) ────────

def generate_random_encounter_hostiles(pg: Any, active_area: Any) -> List[Any]:
    """Generate hostiles for a random overworld encounter.

    Mirrors the hostile-generation half of
    `simulate_check_random_encounter()` without running the legacy blocking
    `CombatScreen`.
    """
    from services.player_movement_service import check_for_random_mob_encounter  # noqa: PLC0415

    _, region = pg.get_region_and_active_area_for_position((pg.x, pg.y))
    parent_region_name = region.get_parent_region_name(pg)
    region_name = region.city_name if not region.isRegion() else region.region_name

    if not parent_region_name:
        region_key = f"{region_name.upper()}_RANDOM_HOSTILE_SEEDS"
    else:
        region_key = f"{parent_region_name.upper()}_{region.city_name.upper()}_RANDOM_HOSTILE_SEEDS"

    return check_for_random_mob_encounter(pg, region_key, force_combat=True)


def generate_boss_encounter_hostiles(pg: Any) -> Optional[List[Any]]:
    """Generate hostiles for a pending boss encounter.

    Mirrors the hostile-generation half of `handle_pending_boss_encounter()`.
    Returns None if the mob id can't be resolved — the caller should treat
    that as an auto-win and clear `pg.pending_fight_mob_id`, matching the
    legacy fallback behavior.
    """
    import game.constants as const  # noqa: PLC0415
    from combat_balancing_simulation.hostile_seed_engine import generate_hostile_from_legacy_seed  # noqa: PLC0415

    mob_id = pg.pending_fight_mob_id
    if not mob_id:
        return None

    boss_setting = next((b for b in const.WORLD_BOSS_MOBS if b.get("id") == mob_id), None)
    if not boss_setting:
        return None

    hostiles = []
    for hostile_id in boss_setting.get("hostiles", []):
        src_name = const.HOSTILE_SEED_PATHS.get(hostile_id)
        seed = None
        if src_name:
            src_list = getattr(const, src_name, None)
            if src_list:
                seed = next((s for s in src_list if s.get("id") == hostile_id), None)
        if seed is None:
            continue
        hostiles.append(
            generate_hostile_from_legacy_seed(seed, pg.get_max_character_level(), retain_abilities=True)
        )

    return hostiles


# ── simulation state queries ──────────────────────────────────────────────────

def check_combat_over(sim: Any) -> Optional[bool]:
    """Return True if players won, False if players lost, None if ongoing.

    Mirrors `CombatScreen.run()`'s loop condition in the legacy blocking UI:
    a loss takes priority over a simultaneous double-knockout.
    """
    players_alive = sim.is_player_annhilation()
    hostiles_alive = sim.is_hostile_annhilation()
    if players_alive and hostiles_alive:
        return None
    return players_alive


def get_next_ready_unit(sim: Any) -> Optional[Any]:
    """Return the next unit whose action timer has elapsed, or None."""
    return sim.next_active_unit()


def is_unit_player(unit: Any) -> bool:
    return bool(unit._is_player())


def get_blocking_status_result(unit: Any) -> Optional[Dict[str, Any]]:
    """Return the blocking-status dict for `unit`, or None if it can act."""
    import game.status_utils as status_utils  # noqa: PLC0415

    return status_utils.get_blocking_status(unit.entity)


def is_confused(unit: Any) -> bool:
    statuses = unit.entity.statuses or []
    return "confuse" in [s.get("id") for s in statuses]


def is_silenced(unit: Any) -> bool:
    statuses = unit.entity.statuses or []
    return "silence" in [s.get("id") for s in statuses]


def is_beneficial_ability(ability: Any) -> bool:
    return bool(ability._is_beneficial_ability())


def is_beneficial_item(item: Any) -> bool:
    return bool(item._is_beneficial_item())


def get_targets(sim: Any, unit: Any, *, want_enemies: bool) -> List[Any]:
    """Return alive units on the requested side relative to `unit`.

    `want_enemies=True` returns the opposing side (e.g. hostiles when `unit`
    is a player); `want_enemies=False` returns `unit`'s own side (allies).
    """
    is_player = is_unit_player(unit)
    result: List[Any] = []
    for u in sim.units:
        if not u.is_alive():
            continue
        same_side = is_unit_player(u) == is_player
        if want_enemies and not same_side:
            result.append(u)
        elif not want_enemies and same_side:
            result.append(u)
    return result


# ── turn actions (thin wrappers over CombatSimulation.perform_unit_action) ───

def perform_auto_skip(sim: Any, unit: Any, status_result: Dict[str, Any]) -> Dict[str, Any]:
    return sim.perform_unit_action(unit, {"type": "auto_skip", "reason": status_result})


def perform_confused_action(sim: Any, unit: Any) -> Dict[str, Any]:
    return sim.perform_unit_action(unit, {"type": "confused"})


def perform_hostile_auto_action(sim: Any, unit: Any) -> Dict[str, Any]:
    return sim.perform_unit_action(unit, {"type": "auto"})


def perform_player_attack(sim: Any, unit: Any, targets: List[Any]) -> Dict[str, Any]:
    return sim.perform_unit_action(unit, {"type": "attack", "targets": targets})


def perform_player_ability(sim: Any, unit: Any, ability: Any, targets: List[Any]) -> Dict[str, Any]:
    return sim.perform_unit_action(unit, {"type": "ability", "ability": ability, "targets": targets})


def perform_player_item(sim: Any, unit: Any, item_index: int, targets: List[Any]) -> Dict[str, Any]:
    return sim.perform_unit_action(unit, {"type": "item", "item": item_index, "targets": targets})


def perform_player_escape(sim: Any, unit: Any) -> Dict[str, Any]:
    """Forward a flee attempt to the engine.

    `CombatSimulation.perform_unit_action()` doesn't implement an 'escape'
    action yet (see the "need to add escape action later" TODO in
    `combat_simulator.py`) — it currently just reports "Unknown action." and
    ends the turn, identical to the legacy 'r' key in
    `combat_simulator_screen.py`. This wrapper exists so the TUI doesn't need
    changes once the engine grows real flee logic.
    """
    return sim.perform_unit_action(unit, {"type": "escape"})


def distribute_rewards(sim: Any) -> List[str]:
    return sim.distribute_rewards()