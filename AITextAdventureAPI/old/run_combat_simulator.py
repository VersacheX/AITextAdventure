#!/usr/bin/env python3
"""Run a simple combat simulator loop for manual stepping and UI testing.

Usage: python old/run_combat_simulator.py
"""
import argparse
from itertools import count
import random
from typing import List, Dict, Any, Optional

from combat_balancing_simulation.player_generator import generate_player
from combat_balancing_simulation.run_hostile_generator import pick_hostiles_from_region
from combat_balancing_simulation.combat_simulator import (
 CombatSimulation
)
from combat_balancing_simulation.combat_simulator_screen import CombatScreen
from game.objects.random_hostile import RandomHostile#, _instantiate_from_seed as instantiateHostile
from game.objects.player_game import PlayerGame

from combat_balancing_simulation.hostile_seed_engine import instantiate_random_hostiles,generate_hostile_from_legacy_seed
from game.objects.utility_item import _instantiate_utility
import game.constants as const_items

#encoutner probability marks mob formation likelihood of being selected.
HOSTILE_MOB_FORMATIONS = [
    {
        'name': 'mega_boss_battle',
        'encounter_probability': 0.05,
        'superrare_count': 1,
        'uncommon_count': 2,
    },
    {
        'name': 'scout_squad',
        'encounter_probability': 0.25,
        'common_count': 5
    },
    {
        'name': 'raiding_party',
        'encounter_probability': 0.25,
        'uncommon_count': 2,
        'common_count': 2
    },
    {
        'name': 'bruiser_squad',
        'encounter_probability': 0.15,
        'rare_count': 1,
        'uncommon_count': 1,
        'common_count': 2
    },
    {
        'name': 'mob_squad',
        'encounter_probability': 0.15,
        'rare_count': 2,
        'uncommon_count': 2,
    },
    {
        'name':'delta_squad',
        'encounter_probability': 0.15,
        'rare_count': 3
    }
]

def get_beginning_items(player, pg: PlayerGame, max_heals: int = 5, max_ap: int = 2):
    """Return utility item seeds appropriate to player level (not instantiated)."""
    util_seeds = const_items.UTILITY_ITEM_SEEDS

    def best_candidates(prefix: str, count: int) -> List[dict]:
        cands = []
        for u in util_seeds:
            effect = u.get("effect") or ""
            min_lvl = int(u.get("min_spawn_level",1) or 1)
            if effect.startswith(prefix) and min_lvl <= player.level:
                cands.append(u)
            cands_sorted = sorted(cands, key=lambda x: int(x.get("min_spawn_level",1) or 1), reverse=True)
        # return the top candidate `count` times
        return cands_sorted[:1] * count if cands_sorted else []

    picks: List[dict] = []
    picks.extend(best_candidates("heal", max_heals))
    picks.extend(best_candidates("restore_ap", max_ap))

    pan = next((u for u in util_seeds if u.get("id") == "panacea" and int(u.get("min_spawn_level", 1) or 1) <= player.level), None)
    if pan:
        picks.extend([pan, pan])

    for p in picks:
        uobj = _instantiate_utility(p)
        pg.pick_up_item(uobj)
    return picks

def generate_random_mob(hostile_count, hostile_level, region_key = None):
    #select random homstile formation from HOSTILE_MOB_FORMATIONS... 
    # set the count to the total count of hostiles in that formation. 
    #def instantiate_random_hostiles(count: int, level: int, selected_region: str = None, superrare_count: int = 0, rare_count: int = 0, uncommon_count: int = 0, common_count: int = 0) -> List[RandomHostile]:
    superrare_count = 0
    rare_count = 0
    uncommon_count = 0
    common_count = 0
    
    random.seed(random.SystemRandom().randint(0,2**32 -1))

    random_mob_val = random.random()
    formation = None
    cumulative_probability = 0.0
    for f in HOSTILE_MOB_FORMATIONS:
        cumulative_probability += f['encounter_probability']
        if random_mob_val <= cumulative_probability:
            formation = f
            break

    if 'superrare_count' in formation:
        superrare_count = formation['superrare_count']
    if 'rare_count' in formation:
        rare_count = formation['rare_count']
    if 'uncommon_count' in formation:
        uncommon_count = formation['uncommon_count']
    if 'common_count' in formation:
        common_count = formation['common_count']

    total_count = superrare_count + rare_count + uncommon_count + common_count

    if total_count == 0:
        total_count = hostile_count
        
    hostiles = instantiate_random_hostiles(count=total_count, level=hostile_level, superrare_count=superrare_count, rare_count=rare_count, uncommon_count=uncommon_count, common_count=common_count, selected_region=region_key)
    # for hostile in hostiles:
    #     hostile.level_to(hostile_level)
    return hostiles

def generate_random_dungeon_mob(hostile_count, hostile_level, hostile_seeds):
    #select random homstile formation from HOSTILE_MOB_FORMATIONS... 
    # set the count to the total count of hostiles in that formation. 
    #def instantiate_random_hostiles(count: int, level: int, selected_region: str = None, superrare_count: int = 0, rare_count: int = 0, uncommon_count: int = 0, common_count: int = 0) -> List[RandomHostile]:
    superrare_count = 0
    rare_count = 0
    uncommon_count = 0
    common_count = 0
    
    random.seed(random.SystemRandom().randint(0,2**32 -1))

    random_mob_val = random.random()
    formation = None
    cumulative_probability = 0.0
    for f in HOSTILE_MOB_FORMATIONS:
        cumulative_probability += f['encounter_probability']
        if random_mob_val <= cumulative_probability:
            formation = f
            break

    if 'superrare_count' in formation:
        superrare_count = formation['superrare_count']
    if 'rare_count' in formation:
        rare_count = formation['rare_count']
    if 'uncommon_count' in formation:
        uncommon_count = formation['uncommon_count']
    if 'common_count' in formation:
        common_count = formation['common_count']

    total_count = superrare_count + rare_count + uncommon_count + common_count

    if total_count == 0:
        total_count = hostile_count

    #select specific seeds based on rarity counts
    selected_seeds = []
    super_rares = [s for s in hostile_seeds if s['rarity'] == 'superrare']
    rares = [s for s in hostile_seeds if s['rarity'] == 'rare']
    uncommons = [s for s in hostile_seeds if s['rarity'] == 'uncommon']
    commons = [s for s in hostile_seeds if s['rarity'] == 'common']

    for _ in range(superrare_count):
        if super_rares:
            selected_seeds.append(random.choice(super_rares))
    for _ in range(rare_count): 
        if rares:
            selected_seeds.append(random.choice(rares))
    for _ in range(uncommon_count):
        if uncommons:
            selected_seeds.append(random.choice(uncommons))
    for _ in range(common_count):
        if commons:
            selected_seeds.append(random.choice(commons))

    hostiles = [] 
    for seed in selected_seeds:
        hostile = generate_hostile_from_legacy_seed(seed, hostile_level, retain_abilities = True)
        hostiles.append(hostile)

    # for hostile in hostiles:
    #     hostile.level_to(hostile_level)

    return hostiles




def generate_player_character(seed, level, class_key = None, player_game: PlayerGame = None):
    rng = random.Random(seed)

    if class_key is None:
        atypes = list(const_items.CHARACTER_CLASS_MAP.keys())
        atype = rng.choice(atypes)
    display_name = f"{const_items.CHARACTER_CLASS_MAP.get(atype, atype).strip()}"

    return generate_player(name=display_name, focus=atype, target_level=level, seed=seed, player_game=player_game)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=86)
    parser.add_argument("--players", type=int, default=5)
    parser.add_argument("--hostiles", type=int, default=3)
    parser.add_argument("--level", type=int, default=3)
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--frame-width", type=int, default=220, help='Frame width in characters for the combat screen')
    parser.add_argument("--frame-height", type=int, default=60, help='Frame height in rows for the combat screen')
    parser.add_argument("--player-width", type=int, default=50, help='Width reserved for each player box column') #<-- unnecessary use the actual objects
    parser.add_argument("--hostile-width", type=int, default=50, help='Width reserved for hostile box column') #<-- unnecessary use the actual objects
    args = parser.parse_args()

    rng = random.Random(args.seed)

    keep_going = True
    players_won = False
    while keep_going:
        if not players_won:
            player_game = PlayerGame()
            # create players via generator
            players = []
            #input (f"Generating {args.players} players at level {args.level}. Press Enter to continue...")
            seed= args.seed
            for i in range(args.players):
                p = generate_player_character(seed=seed, level=args.level, player_game = player_game)
                seed += 1

                players.append(p)

            for p in players:                
                get_beginning_items(p, player_game, max_heals=5, max_ap=2)
                player_game.add_character(p)

        hostiles = generate_random_mob(args.hostiles, args.level)

        #COMABT SIMULATION IS HANDED A PLAYER GAME  AND HOSTILE OBJECTS as defined in game.objects.player and game.objects.random_hostile
        sim = CombatSimulation(player_game, hostiles)

        # Use CombatScreen to render the UI and handle player input/menus
        screen = CombatScreen(width=args.frame_width, height=args.frame_height)
        # set optional per-side widths to control layout precisely
        screen.player_w = args.player_width
        screen.hostile_w = args.hostile_width
        players_won = screen.run(sim)
        while True:            
            print(f"Would you like to run another simulation? (y/n): ")
            response = input().strip().lower()
            if response == 'n':
                keep_going = False
                break
            elif response != 'y':
                print('Invalid response, please enter y or n.')
            else:
                break

if __name__ == '__main__':
 main()
