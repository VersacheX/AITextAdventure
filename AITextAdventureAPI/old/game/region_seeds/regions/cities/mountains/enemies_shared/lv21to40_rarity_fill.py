# Mountains shared hostiles - rarity-coverage fill, Lv 21-40.
#
# EFFICIENT fill: seeds placed only at the union of gap marks the mountain
# small/mid/large reports flag, collapsed so each seed covers as many flagged
# 5-level windows as possible. Placements this band:
#   common    -> Lv 26, 31, 36
#   uncommon  -> Lv 27, 32, 38
#   rare      -> Lv 25, 30, 35, 40
#   superrare -> Lv 25, 30, 35, 40
#
# Ability ids reused from loaded band files (known-valid vs PLAYER_ABILITY_SEEDS).

RANDOM_HOSTILE_SEEDS = [

    # ?? common ?????????????????????????????????????????????????????????????
    {"id": "mountain_shared_pit_gnawer", "name": "Pit Gnawer", "hostile_type": "creature", "role": "damage", "min_spawn_level": 26, "rarity": "common", "base_xp": 460,
     "common_drop": "herb_med", "rare_drop": None, "money_range": (24, 110),
     "basic_attack": "gnashing bite", "strong_attack": "burrow charge",
     "player_abilities": [],
     "base_str": 18, "base_dex": 16, "base_con": 15, "base_int": 4, "base_hp": 280, "base_ap": 11,
     "str_per_level": 3, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},
    {"id": "mountain_shared_shaft_brigand", "name": "Shaft Brigand", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 31, "rarity": "common", "base_xp": 560,
     "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (36, 150),
     "basic_attack": "pick swing", "strong_attack": "ambush cleave",
     "player_abilities": [],
     "base_str": 22, "base_dex": 18, "base_con": 18, "base_int": 6, "base_hp": 340, "base_ap": 12,
     "str_per_level": 3, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 0},
    {"id": "mountain_shared_cragback_boar", "name": "Cragback Boar", "hostile_type": "creature", "role": "damage", "min_spawn_level": 36, "rarity": "common", "base_xp": 680,
     "common_drop": "herb_med", "rare_drop": None, "money_range": (40, 170),
     "basic_attack": "tusk gore", "strong_attack": "downhill barrel",
     "player_abilities": [],
     "base_str": 26, "base_dex": 18, "base_con": 22, "base_int": 5, "base_hp": 400, "base_ap": 12,
     "str_per_level": 4, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 0},

    # ?? uncommon ???????????????????????????????????????????????????????????
    {"id": "mountain_shared_ledge_stalker", "name": "Ledge Stalker", "hostile_type": "creature", "role": "damage", "min_spawn_level": 27, "rarity": "uncommon", "base_xp": 520,
     "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (34, 150),
     "basic_attack": "raking pounce", "strong_attack": "cliff takedown",
     "player_abilities": ["fire_technique_lv1_scorch_slash"],
     "base_str": 20, "base_dex": 22, "base_con": 17, "base_int": 6, "base_hp": 310, "base_ap": 12,
     "str_per_level": 3, "dex_per_level": 3, "con_per_level": 2, "int_per_level": 0},
    {"id": "mountain_shared_forge_zealot", "name": "Forge Zealot", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 32, "rarity": "uncommon", "base_xp": 640,
     "common_drop": "herb_med", "rare_drop": "tome_str", "money_range": (44, 180),
     "basic_attack": "hammer blow", "strong_attack": "molten smite",
     "player_abilities": ["fire_technique_lv1_scorch_slash", "earth_magic_lv1_tremor"],
     "base_str": 24, "base_dex": 18, "base_con": 20, "base_int": 8, "base_hp": 380, "base_ap": 13,
     "str_per_level": 3, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 1},
    {"id": "mountain_shared_scarp_raptor", "name": "Scarp Raptor", "hostile_type": "creature", "role": "damage", "min_spawn_level": 38, "rarity": "uncommon", "base_xp": 780,
     "common_drop": "herb_med", "rare_drop": "stimulant_med", "money_range": (52, 210),
     "basic_attack": "diving talon", "strong_attack": "screech dive",
     "player_abilities": ["air_skill_lv1_smoke_bomb"],
     "base_str": 26, "base_dex": 28, "base_con": 20, "base_int": 7, "base_hp": 420, "base_ap": 14,
     "str_per_level": 4, "dex_per_level": 4, "con_per_level": 2, "int_per_level": 0},

    # ?? rare ???????????????????????????????????????????????????????????????
    {"id": "mountain_shared_quarry_golem", "name": "Quarry Golem", "hostile_type": "construct", "role": "hazard", "min_spawn_level": 25, "rarity": "rare", "base_xp": 520,
     "common_drop": None, "rare_drop": "tome_con", "money_range": (0, 80),
     "basic_attack": "granite fist", "strong_attack": "rockfall slam",
     "player_abilities": ["earth_magic_lv1_tremor"],
     "base_str": 24, "base_dex": 10, "base_con": 26, "base_int": 4, "base_hp": 360, "base_ap": 11,
     "str_per_level": 4, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 0},
    {"id": "mountain_shared_embervein_shaman", "name": "Embervein Shaman", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level": 30, "rarity": "rare", "base_xp": 640,
     "common_drop": "tome_int", "rare_drop": "stimulant_med", "money_range": (48, 200),
     "basic_attack": "cinder hex", "strong_attack": "magma surge",
     "player_abilities": ["fire_technique_lv1_scorch_slash", "dark_magic_lv1_shadow_tendril"],
     "base_str": 16, "base_dex": 18, "base_con": 18, "base_int": 28, "base_hp": 360, "base_ap": 15,
     "str_per_level": 2, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 5},
    {"id": "mountain_shared_stonewrath_ogre", "name": "Stonewrath Ogre", "hostile_type": "creature", "role": "damage", "min_spawn_level": 35, "rarity": "rare", "base_xp": 820,
     "common_drop": "herb_med", "rare_drop": "tome_str", "money_range": (60, 240),
     "basic_attack": "boulder smash", "strong_attack": "avalanche swing",
     "player_abilities": ["earth_magic_lv1_tremor"],
     "base_str": 32, "base_dex": 14, "base_con": 28, "base_int": 5, "base_hp": 500, "base_ap": 13,
     "str_per_level": 5, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 0},
    {"id": "mountain_shared_gloom_warden", "name": "Gloom Warden", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 40, "rarity": "rare", "base_xp": 980,
     "common_drop": "tome_int", "rare_drop": "stimulant_med", "money_range": (70, 280),
     "basic_attack": "grave chill", "strong_attack": "cave-in curse",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "earth_magic_lv1_tremor"],
     "base_str": 24, "base_dex": 20, "base_con": 26, "base_int": 30, "base_hp": 520, "base_ap": 16,
     "str_per_level": 3, "dex_per_level": 2, "con_per_level": 4, "int_per_level": 5},

    # ?? superrare ??????????????????????????????????????????????????????????
    {"id": "mountain_shared_magma_revenant", "name": "Magma Revenant", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 25, "rarity": "superrare", "base_xp": 900,
     "common_drop": "herb_med", "rare_drop": "stimulant_med", "money_range": (120, 420),
     "basic_attack": "molten grasp", "strong_attack": "eruption wail",
     "player_abilities": ["fire_technique_lv1_scorch_slash", "dark_magic_lv1_shadow_tendril", "earth_magic_lv1_tremor"],
     "base_str": 24, "base_dex": 20, "base_con": 24, "base_int": 26, "base_hp": 440, "base_ap": 16,
     "str_per_level": 4, "dex_per_level": 2, "con_per_level": 4, "int_per_level": 3},
    {"id": "mountain_shared_deepdark_terror", "name": "Deepdark Terror", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 30, "rarity": "superrare", "base_xp": 1100,
     "common_drop": "tome_int", "rare_drop": "stimulant_med", "money_range": (150, 520),
     "basic_attack": "abyssal whisper", "strong_attack": "sanity fracture",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "air_skill_lv1_smoke_bomb"],
     "base_str": 22, "base_dex": 24, "base_con": 24, "base_int": 32, "base_hp": 480, "base_ap": 18,
     "str_per_level": 3, "dex_per_level": 3, "con_per_level": 4, "int_per_level": 5},
    {"id": "mountain_shared_riftborn_horror", "name": "Riftborn Horror", "hostile_type": "eldritch", "role": "damage", "min_spawn_level": 35, "rarity": "superrare", "base_xp": 1400,
     "common_drop": "herb_med", "rare_drop": "stimulant_med", "money_range": (200, 700),
     "basic_attack": "rift lash", "strong_attack": "void collapse",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "earth_magic_lv1_tremor", "air_skill_lv1_smoke_bomb"],
     "base_str": 30, "base_dex": 26, "base_con": 28, "base_int": 30, "base_hp": 560, "base_ap": 19,
     "str_per_level": 5, "dex_per_level": 3, "con_per_level": 4, "int_per_level": 4},
    {"id": "mountain_shared_obsidian_wraith", "name": "Obsidian Wraith", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 40, "rarity": "superrare", "base_xp": 1750,
     "common_drop": "tome_int", "rare_drop": "stimulant_med", "money_range": (260, 880),
     "basic_attack": "glass shard flay", "strong_attack": "shattering scream",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "air_skill_lv1_smoke_bomb"],
     "base_str": 32, "base_dex": 30, "base_con": 30, "base_int": 34, "base_hp": 640, "base_ap": 20,
     "str_per_level": 5, "dex_per_level": 3, "con_per_level": 4, "int_per_level": 5},
]
