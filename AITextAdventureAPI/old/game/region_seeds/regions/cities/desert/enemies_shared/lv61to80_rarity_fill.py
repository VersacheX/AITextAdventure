# Desert shared hostiles - rarity-coverage fill, Lv 61-80.
#
# Reusable across all desert city sizes (large / mid / small) and the desert
# wilderness. Each seed is placed at exactly the level the validator suggested
# so a single seed clears each stacked REGION_HOSTILE_RARITY_GAP window.

RANDOM_HOSTILE_SEEDS = [

    # min_spawn_level == 61 (uncommon + common windows Lv 57-61)
    {"id": "brass_syndicate_gunner", "name": "Brass Syndicate Gunner", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 61, "rarity": "uncommon", "base_xp": 2800,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (200, 700),
     "basic_attack": "repeater volley", "strong_attack": "suppressing barrage",
     "player_abilities": ["fire_technique_lv1_scorch_slash"],
     "base_str": 32, "base_dex": 28, "base_con": 28, "base_int": 10, "base_hp": 640, "base_ap": 13,
     "str_per_level": 5, "dex_per_level": 5, "con_per_level": 4, "int_per_level": 1},
    {"id": "gutter_sand_stalker", "name": "Gutter Sand Stalker", "hostile_type": "creature", "role": "damage", "min_spawn_level": 61, "rarity": "common", "base_xp": 2400,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (150, 520),
     "basic_attack": "raking claw", "strong_attack": "ambush pounce",
     "player_abilities": [],
     "base_str": 34, "base_dex": 26, "base_con": 30, "base_int": 8, "base_hp": 680, "base_ap": 13,
     "str_per_level": 6, "dex_per_level": 4, "con_per_level": 5, "int_per_level": 0},

    # min_spawn_level == 62 (common window Lv 58-62)
    {"id": "rustpit_scavenger", "name": "Rustpit Scavenger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 62, "rarity": "common", "base_xp": 3000,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (170, 560),
     "basic_attack": "rebar swing", "strong_attack": "scrap avalanche",
     "player_abilities": [],
     "base_str": 38, "base_dex": 24, "base_con": 32, "base_int": 8, "base_hp": 760, "base_ap": 13,
     "str_per_level": 6, "dex_per_level": 4, "con_per_level": 5, "int_per_level": 0},

    # min_spawn_level == 66 (uncommon + rare windows Lv 62-66)
    {"id": "chrome_cult_zealot", "name": "Chrome Cult Zealot", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level": 66, "rarity": "uncommon", "base_xp": 3200,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (220, 760),
     "basic_attack": "ritual sear", "strong_attack": "chrome benediction",
     "player_abilities": ["dark_dark_magic_lv2_umbra_storm"],
     "base_str": 22, "base_dex": 22, "base_con": 26, "base_int": 34, "base_hp": 700, "base_ap": 15,
     "str_per_level": 3, "dex_per_level": 3, "con_per_level": 4, "int_per_level": 6},
    {"id": "mirage_reaver", "name": "Mirage Reaver", "hostile_type": "eldritch", "role": "damage", "min_spawn_level": 66, "rarity": "rare", "base_xp": 3800,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (300, 1000),
     "basic_attack": "phantom cleave", "strong_attack": "heat-mirage rend",
     "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 40, "base_dex": 30, "base_con": 34, "base_int": 18, "base_hp": 820, "base_ap": 14,
     "str_per_level": 7, "dex_per_level": 5, "con_per_level": 6, "int_per_level": 2},

    # min_spawn_level == 67 (common window Lv 63-67)
    {"id": "duneback_pack_beast", "name": "Duneback Pack Beast", "hostile_type": "creature", "role": "damage", "min_spawn_level": 67, "rarity": "common", "base_xp": 3000,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (200, 720),
     "basic_attack": "goring charge", "strong_attack": "trampling stampede",
     "player_abilities": [],
     "base_str": 44, "base_dex": 26, "base_con": 40, "base_int": 8, "base_hp": 900, "base_ap": 14,
     "str_per_level": 7, "dex_per_level": 4, "con_per_level": 6, "int_per_level": 0},

    # min_spawn_level == 71 (uncommon + rare windows Lv 67-71)
    {"id": "salt_reaver_captain", "name": "Salt Reaver Captain", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 71, "rarity": "uncommon", "base_xp": 4400,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (260, 900),
     "basic_attack": "cutlass arc", "strong_attack": "boarding rush",
     "player_abilities": ["fire_technique_lv1_scorch_slash"],
     "base_str": 44, "base_dex": 30, "base_con": 38, "base_int": 12, "base_hp": 900, "base_ap": 15,
     "str_per_level": 6, "dex_per_level": 4, "con_per_level": 5, "int_per_level": 1},
    {"id": "obsidian_tomb_warden", "name": "Obsidian Tomb Warden", "hostile_type": "construct", "role": "damage", "min_spawn_level": 71, "rarity": "rare", "base_xp": 5000,
     "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 120),
     "basic_attack": "obsidian smash", "strong_attack": "warden lockdown",
     "player_abilities": ["level_1_hostile_ability_reinforce_frame", "earth_earth_magic_lv2_quake_field"],
     "base_str": 52, "base_dex": 18, "base_con": 48, "base_int": 10, "base_hp": 1100, "base_ap": 15,
     "str_per_level": 8, "dex_per_level": 2, "con_per_level": 7, "int_per_level": 1},

    # min_spawn_level == 72 (common window Lv 68-72)
    {"id": "dune_colossus_hound", "name": "Dune Colossus Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level": 72, "rarity": "common", "base_xp": 4200,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (200, 720),
     "basic_attack": "crushing jaws", "strong_attack": "avalanche pounce",
     "player_abilities": [],
     "base_str": 46, "base_dex": 28, "base_con": 42, "base_int": 8, "base_hp": 960, "base_ap": 15,
     "str_per_level": 7, "dex_per_level": 4, "con_per_level": 6, "int_per_level": 0},

    # min_spawn_level == 76 (uncommon + rare windows Lv 72-76)
    {"id": "ashglass_conjurer", "name": "Ashglass Conjurer", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 76, "rarity": "uncommon", "base_xp": 5600,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (320, 1100),
     "basic_attack": "ember lash", "strong_attack": "glassing firestorm",
     "player_abilities": ["fire_earth_magic_lv2_magma_javelin"],
     "base_str": 30, "base_dex": 30, "base_con": 36, "base_int": 44, "base_hp": 1080, "base_ap": 17,
     "str_per_level": 4, "dex_per_level": 4, "con_per_level": 5, "int_per_level": 7},
    {"id": "revenant_dune_rider", "name": "Revenant Dune Rider", "hostile_type": "undead", "role": "damage", "min_spawn_level": 76, "rarity": "rare", "base_xp": 6200,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (360, 1200),
     "basic_attack": "spectral lance", "strong_attack": "grave-charge trample",
     "player_abilities": ["level_1_hostile_ability_bone_spear", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 56, "base_dex": 34, "base_con": 50, "base_int": 20, "base_hp": 1320, "base_ap": 17,
     "str_per_level": 8, "dex_per_level": 5, "con_per_level": 7, "int_per_level": 2},

    # min_spawn_level == 77 (common window Lv 73-77)
    {"id": "scourwind_bruiser", "name": "Scourwind Bruiser", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 77, "rarity": "common", "base_xp": 5200,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (240, 840),
     "basic_attack": "hammer blow", "strong_attack": "grinding overhead",
     "player_abilities": [],
     "base_str": 54, "base_dex": 26, "base_con": 48, "base_int": 10, "base_hp": 1240, "base_ap": 16,
     "str_per_level": 8, "dex_per_level": 3, "con_per_level": 7, "int_per_level": 0},

    # min_spawn_level == 78 (rare window Lv 74-78)
    {"id": "abyssal_sand_horror", "name": "Abyssal Sand Horror", "hostile_type": "eldritch", "role": "damage", "min_spawn_level": 78, "rarity": "rare", "base_xp": 6600,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (400, 1400),
     "basic_attack": "grasping tendril", "strong_attack": "engulfing collapse",
     "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 58, "base_dex": 40, "base_con": 52, "base_int": 24, "base_hp": 1420, "base_ap": 18,
     "str_per_level": 8, "dex_per_level": 5, "con_per_level": 7, "int_per_level": 3},
]
