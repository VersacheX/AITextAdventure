# Desert shared hostiles - rarity-coverage fill, Lv 41-60.
#
# Reusable across all desert city sizes (large / mid / small) and the desert
# wilderness. Each seed is placed at exactly the level the validator suggested
# so a single seed clears each stacked REGION_HOSTILE_RARITY_GAP window.

RANDOM_HOSTILE_SEEDS = [

    # min_spawn_level == 41 (superrare window Lv 37-41)
    {"id": "sunspire_revenant_king", "name": "Sunspire Revenant King", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 41, "rarity": "superrare", "base_xp": 1400,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (200, 720),
     "basic_attack": "royal death curse", "strong_attack": "sunspire edict",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 16, "base_dex": 18, "base_con": 18, "base_int": 40, "base_hp": 320, "base_ap": 22,
     "str_per_level": 2, "dex_per_level": 3, "con_per_level": 3, "int_per_level": 6},

    # min_spawn_level == 42 (common window Lv 38-42)
    {"id": "scrap_yard_jackal", "name": "Scrap Yard Jackal", "hostile_type": "creature", "role": "damage", "min_spawn_level": 42, "rarity": "common", "base_xp": 620,
     "common_drop": "herb_med", "rare_drop": "stimulant_large", "money_range": (70, 260),
     "basic_attack": "snapping bite", "strong_attack": "pack takedown",
     "player_abilities": [],
     "base_str": 16, "base_dex": 14, "base_con": 14, "base_int": 5, "base_hp": 230, "base_ap": 9,
     "str_per_level": 3, "dex_per_level": 3, "con_per_level": 3, "int_per_level": 0},

    # min_spawn_level == 46 (superrare window Lv 42-46)
    {"id": "abyssal_mirage_horror", "name": "Abyssal Mirage Horror", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 46, "rarity": "superrare", "base_xp": 1800,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (260, 900),
     "basic_attack": "reality ripple", "strong_attack": "mirage collapse",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 20, "base_dex": 24, "base_con": 22, "base_int": 44, "base_hp": 360, "base_ap": 24,
     "str_per_level": 3, "dex_per_level": 4, "con_per_level": 3, "int_per_level": 7},

    # min_spawn_level == 47 (common + uncommon windows Lv 43-47)
    {"id": "canal_ward_brute", "name": "Canal Ward Brute", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 47, "rarity": "common", "base_xp": 720,
     "common_drop": "herb_med", "rare_drop": "herb_major", "money_range": (80, 300),
     "basic_attack": "pipe swing", "strong_attack": "wall slam",
     "player_abilities": [],
     "base_str": 20, "base_dex": 9, "base_con": 18, "base_int": 4, "base_hp": 320, "base_ap": 9,
     "str_per_level": 4, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},
    {"id": "oasis_toll_captain", "name": "Oasis Toll Captain", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 47, "rarity": "uncommon", "base_xp": 940,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (140, 520),
     "basic_attack": "saber cut", "strong_attack": "toll enforcement",
     "player_abilities": ["fire_technique_lv1_scorch_slash"],
     "base_str": 22, "base_dex": 16, "base_con": 20, "base_int": 8, "base_hp": 340, "base_ap": 11,
     "str_per_level": 4, "dex_per_level": 3, "con_per_level": 3, "int_per_level": 1},

    # min_spawn_level == 50 (rare window Lv 46-50)
    {"id": "brass_serpent_matron", "name": "Brass Serpent Matron", "hostile_type": "creature", "role": "damage", "min_spawn_level": 50, "rarity": "rare", "base_xp": 1300,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (200, 700),
     "basic_attack": "coiling strike", "strong_attack": "crushing constriction",
     "player_abilities": ["level_1_hostile_ability_poison_dart", "fire_earth_magic_lv2_magma_javelin"],
     "base_str": 30, "base_dex": 22, "base_con": 26, "base_int": 8, "base_hp": 420, "base_ap": 11,
     "str_per_level": 5, "dex_per_level": 3, "con_per_level": 4, "int_per_level": 0},

    # min_spawn_level == 52 (common window Lv 48-52)
    {"id": "quarry_scrapper", "name": "Quarry Scrapper", "hostile_type": "construct", "role": "damage", "min_spawn_level": 52, "rarity": "common", "base_xp": 1300,
     "common_drop": None, "rare_drop": "stimulant_large", "money_range": (0, 90),
     "basic_attack": "clamp strike", "strong_attack": "overload piston",
     "player_abilities": [],
     "base_str": 26, "base_dex": 12, "base_con": 22, "base_int": 5, "base_hp": 430, "base_ap": 11,
     "str_per_level": 4, "dex_per_level": 2, "con_per_level": 4, "int_per_level": 0},

    # min_spawn_level == 56 (uncommon + rare windows Lv 52-56)
    {"id": "dune_syndicate_lieutenant", "name": "Dune Syndicate Lieutenant", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 56, "rarity": "uncommon", "base_xp": 1500,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (180, 640),
     "basic_attack": "repeater burst", "strong_attack": "crossfire order",
     "player_abilities": ["fire_technique_lv1_scorch_slash"],
     "base_str": 28, "base_dex": 24, "base_con": 26, "base_int": 10, "base_hp": 520, "base_ap": 12,
     "str_per_level": 5, "dex_per_level": 4, "con_per_level": 4, "int_per_level": 1},
    {"id": "sandglass_djinn", "name": "Sandglass Djinn", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 56, "rarity": "rare", "base_xp": 2000,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (240, 820),
     "basic_attack": "scouring gust", "strong_attack": "hourglass vortex",
     "player_abilities": ["fire_earth_magic_lv2_magma_javelin", "dark_dark_magic_lv2_umbra_storm"],
     "base_str": 24, "base_dex": 28, "base_con": 26, "base_int": 34, "base_hp": 540, "base_ap": 15,
     "str_per_level": 4, "dex_per_level": 4, "con_per_level": 4, "int_per_level": 6},

    # min_spawn_level == 57 (common window Lv 53-57)
    {"id": "dune_raid_marauder", "name": "Dune Raid Marauder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 57, "rarity": "common", "base_xp": 1600,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (120, 420),
     "basic_attack": "scimitar slash", "strong_attack": "raider charge",
     "player_abilities": [],
     "base_str": 30, "base_dex": 16, "base_con": 26, "base_int": 6, "base_hp": 560, "base_ap": 12,
     "str_per_level": 5, "dex_per_level": 3, "con_per_level": 4, "int_per_level": 0},
]
