# Mountains shared hostiles - rarity-coverage fill, Lv 1-20.
#
# EFFICIENT fill (not a blanket every-rarity-every-5-levels roster). Seeds are
# placed ONLY at the marks the mountain small/mid/large validator reports flag
# as gaps. A seed at level N satisfies any sliding window containing N, so each
# reported gap is snapped to the nearest <=5 mark within range. Low levels are
# largely covered by each city's own base seeds, so this band is sparse.
#
# Reports covered (this band):
#   common     -> Lv 5, 15   (gaps at Lv 9, 19)
#   uncommon   -> Lv 20      (gap at Lv 21)
#   rare       -> Lv 15, 20  (gaps at Lv 15, 20)
#   superrare  -> Lv 5, 15, 20 (gaps at Lv 5, 15, 21)
#
# Ability ids reused from loaded band files (known-valid vs PLAYER_ABILITY_SEEDS).
# Theme: mine vermin, forge sprites, cave stalkers, rockslide horrors.

RANDOM_HOSTILE_SEEDS = [

    # ?? Lv 5 ???????????????????????????????????????????????????????????????
    {"id": "mountain_shared_mine_rat", "name": "Mine Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level": 5, "rarity": "common", "base_xp": 40,
     "common_drop": "herb_minor", "rare_drop": None, "money_range": (5, 30),
     "basic_attack": "gnawing bite", "strong_attack": "scurrying swarm",
     "player_abilities": [],
     "base_str": 5, "base_dex": 6, "base_con": 5, "base_int": 2, "base_hp": 42, "base_ap": 5,
     "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 0},
    {"id": "mountain_shared_slag_wisp", "name": "Slag Wisp", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 5, "rarity": "superrare", "base_xp": 90,
     "common_drop": "herb_minor", "rare_drop": "stimulant_med", "money_range": (20, 90),
     "basic_attack": "ember flicker", "strong_attack": "choking smog",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "air_skill_lv1_smoke_bomb", "level_1_hostile_ability_poison_dart"],
     "base_str": 5, "base_dex": 8, "base_con": 5, "base_int": 9, "base_hp": 52, "base_ap": 7,
     "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 1},

    # ?? Lv 15 ??????????????????????????????????????????????????????????????
    {"id": "mountain_shared_tunnel_creeper", "name": "Tunnel Creeper", "hostile_type": "creature", "role": "damage", "min_spawn_level": 15, "rarity": "common", "base_xp": 140,
     "common_drop": "herb_minor", "rare_drop": "herb_med", "money_range": (14, 70),
     "basic_attack": "raking claw", "strong_attack": "burrow lunge",
     "player_abilities": [],
     "base_str": 9, "base_dex": 10, "base_con": 8, "base_int": 3, "base_hp": 120, "base_ap": 8,
     "str_per_level": 2, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 0},
    {"id": "mountain_shared_rockseam_lurker", "name": "Rockseam Lurker", "hostile_type": "creature", "role": "hazard", "min_spawn_level": 15, "rarity": "rare", "base_xp": 210,
     "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (24, 100),
     "basic_attack": "ambush snap", "strong_attack": "cavern collapse",
     "player_abilities": ["earth_magic_lv1_tremor", "level_1_hostile_ability_poison_dart"],
     "base_str": 11, "base_dex": 12, "base_con": 10, "base_int": 6, "base_hp": 150, "base_ap": 9,
     "str_per_level": 2, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 1},
    {"id": "mountain_shared_deepshaft_phantom", "name": "Deepshaft Phantom", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 15, "rarity": "superrare", "base_xp": 300,
     "common_drop": "herb_med", "rare_drop": "stimulant_med", "money_range": (40, 160),
     "basic_attack": "gloom whisper", "strong_attack": "shaft-black dread",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "air_skill_lv1_smoke_bomb"],
     "base_str": 10, "base_dex": 13, "base_con": 10, "base_int": 14, "base_hp": 160, "base_ap": 10,
     "str_per_level": 2, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 2},

    # ?? Lv 20 ??????????????????????????????????????????????????????????????
    {"id": "mountain_shared_scree_prowler", "name": "Scree Prowler", "hostile_type": "creature", "role": "damage", "min_spawn_level": 20, "rarity": "uncommon", "base_xp": 300,
     "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (30, 130),
     "basic_attack": "pouncing rake", "strong_attack": "cliffside takedown",
     "player_abilities": ["fire_technique_lv1_scorch_slash"],
     "base_str": 14, "base_dex": 15, "base_con": 12, "base_int": 5, "base_hp": 200, "base_ap": 10,
     "str_per_level": 2, "dex_per_level": 3, "con_per_level": 2, "int_per_level": 0},
    {"id": "mountain_shared_ore_golemling", "name": "Ore Golemling", "hostile_type": "construct", "role": "hazard", "min_spawn_level": 20, "rarity": "rare", "base_xp": 380,
     "common_drop": None, "rare_drop": "tome_str", "money_range": (0, 60),
     "basic_attack": "stone fist", "strong_attack": "quarry slam",
     "player_abilities": ["earth_magic_lv1_tremor"],
     "base_str": 18, "base_dex": 8, "base_con": 18, "base_int": 3, "base_hp": 240, "base_ap": 9,
     "str_per_level": 3, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},
    {"id": "mountain_shared_gloomvein_horror", "name": "Gloomvein Horror", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 20, "rarity": "superrare", "base_xp": 520,
     "common_drop": "herb_med", "rare_drop": "stimulant_med", "money_range": (60, 220),
     "basic_attack": "vein rupture", "strong_attack": "deep-earth madness",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "air_skill_lv1_smoke_bomb", "level_1_hostile_ability_poison_dart"],
     "base_str": 16, "base_dex": 16, "base_con": 16, "base_int": 18, "base_hp": 260, "base_ap": 12,
     "str_per_level": 3, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 2},
]
