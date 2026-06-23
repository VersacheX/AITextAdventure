#!/usr/bin/env python3
"""Quick test harness to build a5-player PlayerGame and hand it to the InventoryScreen.

This uses helper functions in `run_combat_simulator.py` to construct players
and beginning inventory, then renders the inventory screen once for inspection.

Run from the repository root or from the `old` directory so imports resolve.
"""
import os
import sys
import time

from game.objects.weapon import Weapon
from game.objects.armor import Armor
from typing import List
import random
from game.objects.weapon import _instantiate_weapon
from game.objects.armor import _instantiate_armor
import game.constants as const

# Make sure the 'old' directory is on sys.path so local imports resolve when run from repo root
THIS_DIR = os.path.dirname(__file__) or '.'
if THIS_DIR not in sys.path:
    sys.path.insert(0, THIS_DIR)

from run_combat_simulator import generate_player_character, get_beginning_items
from game.objects.player_game import PlayerGame
from game_screens.inventory_screen import InventoryScreen


def build_test_player_game(player_count: int = 5, starting_level: int = 3, seed_start: int = 1000) -> PlayerGame:
    pg = PlayerGame()
    seed = int(seed_start or 1000)
    for i in range(player_count):
        p = generate_player_character(seed=seed + i, level=starting_level, player_game=pg)

        pg.add_character(p)
        #pg.characters.append(p)

        get_beginning_items(p, pg, max_heals=3, max_ap=1)

    return pg


def add_equipment_to_game(pg: PlayerGame) -> None:
    """For each player in `pg.characters`, pick a weapon and one armor piece
    appropriate to the player's level and add them to the shared PlayerGame
    inventory. Uses seed data in `game.constants_items` and the internal
    instantiation helpers to create runtime `Weapon`/`Armor` objects.
    """
    # flatten armor seeds into (slot, seed) pairs for easy filtering
    armor_pairs = []
    for slot, seeds in (const.ARMOR_SEEDS or {}).items():
        for s in seeds:
            armor_pairs.append((slot, s))

    weapon_seeds = list(const.WEAPON_SEEDS or [])

    rng = random.Random(12345)

    for p in list(pg.characters):
        lvl = p.level

        # pick weapon seed appropriate to level: consider all candidates with min_spawn_level <= lvl
        # but sample with weights proportional to min_spawn_level so higher-tier items are more likely
        w_cands = [s for s in weapon_seeds if int(s.get('min_spawn_level',1) or 1) <= lvl]
        if not w_cands:
            w_cands = weapon_seeds
        if w_cands:
            weights = [int(s.get('min_spawn_level',1) or 1) for s in w_cands]
            # rng.choices returns a list
            w_seed = rng.choices(w_cands, weights=weights, k=1)[0]
            wobj = _instantiate_weapon(w_seed)
            pg.pick_up_item(wobj)

        # For each armor slot (head/body/arms/legs), pick the top2 seeds
        # whose min_spawn_level is <= player level (prefer higher min_spawn_level).
        for slot_name in const.ARMOR_TYPES.keys():
            # collect seeds for this slot
            slot_seeds = [s for (sl, s) in armor_pairs if sl == slot_name]
            if not slot_seeds:
                continue
            # eligible seeds for player's level
            eligible = [s for s in slot_seeds if int(s.get('min_spawn_level', 1) or 1) <= lvl]
            # if none eligible at this level, fall back to all seeds for the slot
            if not eligible:
                eligible = slot_seeds
            # sample up to two unique seeds using weights based on min_spawn_level
            weights = [int(s.get('min_spawn_level',1) or 1) for s in eligible]
            # pick up to2 unique seeds
            picks = []
            pool = list(eligible)
            pool_weights = list(weights)
            for _ in range(min(2, len(pool))):
                sel = rng.choices(pool, weights=pool_weights, k=1)[0]
                picks.append(sel)
                # remove selected from pool
                idx = pool.index(sel)
                pool.pop(idx)
                pool_weights.pop(idx)
            for a_seed in picks:
                aobj = _instantiate_armor(a_seed, slot_name)
                pg.pick_up_item(aobj)

def gain_levels_for_characters(pg, levels_to_gain: int) -> None:
    """Gain `levels_to_gain` levels for each character in `pg`."""
    for p in pg.characters:
        for _ in range(levels_to_gain):
            final_xp = p.get_required_experience_to_level()
            levels_gained = p.gain_experience(final_xp)
			# record
            if levels_gained:
                if levels_gained > 0:
                    for (lg) in range(levels_gained):
                        p.check_level_up_awards()
                        #print (f"Level {p.level}:  {p.unused_ability_slots} ability points, {p.unused_stat_points} stat points, {p.unused_power_points} power points for {p.name}")


def main() -> None:
    print("Building test PlayerGame inventory screen with 9 characters...")
    pg = build_test_player_game(player_count=9, starting_level=3, seed_start=2000)
    add_equipment_to_game(pg)
    gain_levels_for_characters(pg, levels_to_gain=6)

    # add a few monsters to the monster log for testing purposes
    pg.enemies_slain["bayou_hobo"] = 5
    pg.enemies_slain["slick_trapper"] = 3
    pg.enemies_slain["swamp_rat"] = 2
    #for p in pg.characters:
        # display power points, stat points and ability points
        #print (f"{p.unused_ability_slots} ability points, {p.unused_stat_points} stat points, {p.unused_power_points} power points for {p.name}")
    #input ("Press Enter to continue to render inventory screen...")


    screen = InventoryScreen()
    #RUN THE TEST
    screen.run(pg)

    print("Rendered inventory screen for inspection. Sleeping2s before exit.")
    time.sleep(2)


if __name__ == '__main__':
    main()
