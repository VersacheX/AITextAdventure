#!/usr/bin/env python3
"""Interactive dungeon simulator for manual testing.

Usage: python old/run_dungeon_simulator.py
"""

import argparse
import random
#from typing import #List#, Tuple#, Optional#, Dict
from collections import deque

from game_screens.dungeon_screen import run_dungeon_screen
from combat_balancing_simulation.player_generator import generate_player
from game.constants import CHARACTER_CLASS_MAP
from game.objects.player_game import PlayerGame

from game.services.dungeon_builder_service import build_dungeon
from game.region_seeds.primary_stories.desert.zaruun_lair import DUNGEON_SETTINGS as ZARUUN_DUNGEON_SETTINGS
from game.region_seeds.primary_stories.forest.marrowroot_lair import DUNGEON_SETTINGS as MARROWROOT_DUNGEON_SETTINGS
from game.region_seeds.primary_stories.grassland.serene_lair import DUNGEON_SETTINGS as SERENE_DUNGEON_SETTINGS
from game.region_seeds.primary_stories.mountains.rokhuld_lair import DUNGEON_SETTINGS as ROKHULD_DUNGEON_SETTINGS
from game.region_seeds.primary_stories.shallows.uulthar_lair import DUNGEON_SETTINGS as UULTHAR_DUNGEON_SETTINGS
from game.region_seeds.primary_stories.snow.aeriola_lair import DUNGEON_SETTINGS as AERIOLA_DUNGEON_SETTINGS
from game.region_seeds.primary_stories.swamp.miregloom_lair import DUNGEON_SETTINGS as MIREGLOOM_DUNGEON_SETTINGS

DUNGEON_SETTINGS = [
    ROKHULD_DUNGEON_SETTINGS,
    ZARUUN_DUNGEON_SETTINGS,
    MARROWROOT_DUNGEON_SETTINGS,
    AERIOLA_DUNGEON_SETTINGS,
    SERENE_DUNGEON_SETTINGS,
    UULTHAR_DUNGEON_SETTINGS,
    MIREGLOOM_DUNGEON_SETTINGS
]


def generate_player_character(seed: int, level: int, class_key: str = None, player_game: PlayerGame= None):
    rng = random.Random(seed)
    if class_key is None:
        atypes = list(CHARACTER_CLASS_MAP.keys())
        atype = rng.choice(atypes)
    else:
        atype = class_key
    display_name = f"{CHARACTER_CLASS_MAP.get(atype, atype).strip()}"
    return generate_player(name=display_name, focus=atype, target_level=level, seed=seed, player_game=player_game)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, default=12345)
    parser.add_argument('--width', type=int, default=100)
    parser.add_argument('--height', type=int, default=60)
    parser.add_argument('--levels', type=int, default=3)
    parser.add_argument('--characters', type=int, default=5)
    parser.add_argument('--player-seed', type=int, default=86)
    parser.add_argument('--player-level', type=int, default=21)
    args = parser.parse_args()

    random_seed = random.SystemRandom().random() * args.seed
    rng = random.Random(random_seed)

    # place player at first passable tile on level0
    origin = (0,0,0)
    player_pos = origin

    # create player game with a single player
    pg = PlayerGame()
    for i in range(args.characters):
        player = generate_player_character(random_seed + i, args.player_level, player_game = pg)
        pg.add_character(player)
    
    dungeons = DUNGEON_SETTINGS

    #test override +++ refurbed dungeons with level 17-23 mob enemies and boss/subs lvl 23-30
    dungeons = [UULTHAR_DUNGEON_SETTINGS]    
    dungeon = build_dungeon(rng.choice(dungeons))


    run_dungeon_screen(dungeon, pg, player_pos)



if __name__ == '__main__':
    main()
