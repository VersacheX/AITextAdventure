# Forest Large City (Aurelion Veil) — hostile seeds levels 21-100.

RANDOM_HOSTILE_SEEDS = [

 # min_spawn_level == 21
 {"id": "thornwood_champion", "name": "Thornwood Champion", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 280,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (60, 200),
  "basic_attack": "thornwood slash", "strong_attack": "briar cleave",
  "player_abilities": [],
  "base_str": 12, "base_dex": 10, "base_con": 10, "base_int": 4, "base_hp": 320, "base_ap": 10,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},

 {"id": "forest_revenant_lg", "name": "Forest Revenant", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 360,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "necrotic grasp", "strong_attack": "revenant wail",
  "player_abilities": ["level_1_hostile_ability_bone_spear"],
  "base_str": 10, "base_dex": 8, "base_con": 8, "base_int": 12, "base_hp": 360, "base_ap": 12,
  "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 3},

 # min_spawn_level == 24
 {"id": "bark_golem_lg", "name": "Bark Golem", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 24, "rarity": "uncommon", "base_xp": 380,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 20),
  "basic_attack": "bark slam", "strong_attack": "root crush",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 16, "base_dex": 2, "base_con": 14, "base_int": 4, "base_hp": 440, "base_ap": 6,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 3, "int_per_level": 0},

 # min_spawn_level == 27
 {"id": "fey_warlock", "name": "Fey Warlock", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 27, "rarity": "uncommon", "base_xp": 420,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 280),
  "basic_attack": "fey bolt", "strong_attack": "warlock hex",
  "player_abilities": ["air_magic_lv1_shredding_gust", "air_dark_magic_lv2_night_wind"],
  "base_str": 4, "base_dex": 10, "base_con": 6, "base_int": 18, "base_hp": 280, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},

 # min_spawn_level == 30
 {"id": "dusk_archon", "name": "Dusk Archon", "hostile_type": "shadow", "role": "hazard", "min_spawn_level": 30, "rarity": "superrare", "base_xp": 1400,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (200, 700),
  "basic_attack": "dusk decree", "strong_attack": "archon's veil",
  "player_abilities": ["level_1_hostile_ability_night_whisper", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 10, "base_dex": 14, "base_con": 10, "base_int": 22, "base_hp": 600, "base_ap": 20,
  "str_per_level": 1, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 5},

 # min_spawn_level == 33
 {"id": "forest_warlord", "name": "Forest Warlord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 33, "rarity": "uncommon", "base_xp": 500,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (140, 480),
  "basic_attack": "warlord cleave", "strong_attack": "forest siege",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 20, "base_dex": 10, "base_con": 18, "base_int": 6, "base_hp": 520, "base_ap": 10,
  "str_per_level": 4, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 1},

 {"id": "twilight_sorcerer", "name": "Twilight Sorcerer", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 33, "rarity": "uncommon", "base_xp": 520,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (100, 360),
  "basic_attack": "twilight bolt", "strong_attack": "dusk nova",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "air_dark_magic_lv2_night_wind"],
  "base_str": 4, "base_dex": 10, "base_con": 6, "base_int": 22, "base_hp": 320, "base_ap": 20,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 5},

 # min_spawn_level == 38
 {"id": "ancient_treant_lord", "name": "Ancient Treant Lord", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 38, "rarity": "rare", "base_xp": 1000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (60, 220),
  "basic_attack": "ancient branch", "strong_attack": "forest earthquake",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field"],
  "base_str": 28, "base_dex": 2, "base_con": 26, "base_int": 10, "base_hp": 1200, "base_ap": 12,
  "str_per_level": 6, "dex_per_level": 0, "con_per_level": 5, "int_per_level": 2},

 # min_spawn_level == 45
 {"id": "forest_lich", "name": "Forest Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 45, "rarity": "superrare", "base_xp": 3200,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (400, 1400),
  "basic_attack": "death bolt", "strong_attack": "lich forest wail",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 8, "base_dex": 10, "base_con": 10, "base_int": 34, "base_hp": 800, "base_ap": 28,
  "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 8},

 # min_spawn_level == 55
 {"id": "forest_dragon_elder", "name": "Elder Forest Dragon", "hostile_type": "creature", "role": "damage", "min_spawn_level": 55, "rarity": "superrare", "base_xp": 6000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1200, 4000),
  "basic_attack": "elder claw", "strong_attack": "canopy breath",
  "player_abilities": ["air_magic_lv1_shredding_gust", "air_air_magic_lv2_tempest_note"],
  "base_str": 54, "base_dex": 16, "base_con": 50, "base_int": 12, "base_hp": 6000, "base_ap": 14,
  "str_per_level": 10, "dex_per_level": 2, "con_per_level": 9, "int_per_level": 2},

 # min_spawn_level == 70
 {"id": "dusk_titan", "name": "Dusk Titan", "hostile_type": "shadow", "role": "hazard", "min_spawn_level": 70, "rarity": "superrare", "base_xp": 14000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (4000, 14000),
  "basic_attack": "titan's veil", "strong_attack": "dusk obliteration",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 22, "base_dex": 28, "base_con": 24, "base_int": 72, "base_hp": 14000, "base_ap": 60,
  "str_per_level": 3, "dex_per_level": 5, "con_per_level": 4, "int_per_level": 15},

 # min_spawn_level == 100
 {"id": "world_tree_lord", "name": "World Tree Lord", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 120000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (50000, 160000),
  "basic_attack": "world root wrath", "strong_attack": "canopy apocalypse",
  "player_abilities": ["earth_earth_earth_magic_lv3_earthshaker", "air_air_air_magic_lv3_storm_surge"],
  "base_str": 130, "base_dex": 28, "base_con": 124, "base_int": 38, "base_hp": 100000, "base_ap": 30,
  "str_per_level": 26, "dex_per_level": 5, "con_per_level": 24, "int_per_level": 7},

 # Lv71-80 band
 {"id": "aurelion_bough_titan", "name": "Bough Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 73, "rarity": "superrare", "base_xp": 18000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (5000, 18000),
  "basic_attack": "bough slam", "strong_attack": "canopy shatter",
  "player_abilities": ["earth_earth_earth_magic_lv3_earthshaker"],
  "base_str": 82, "base_dex": 12, "base_con": 76, "base_int": 14, "base_hp": 18000, "base_ap": 14,
  "str_per_level": 16, "dex_per_level": 2, "con_per_level": 15, "int_per_level": 2},

 {"id": "aurelion_grove_lich", "name": "Ancient Grove Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 77, "rarity": "superrare", "base_xp": 22000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (7000, 24000),
  "basic_attack": "grove death bolt", "strong_attack": "lich canopy storm",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 10, "base_dex": 14, "base_con": 12, "base_int": 76, "base_hp": 10000, "base_ap": 62,
  "str_per_level": 2, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 15},

 # Lv81-90 band
 {"id": "aurelion_grove_god", "name": "Grove God Warrior", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 82, "rarity": "superrare", "base_xp": 30000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (10000, 34000),
  "basic_attack": "god root strike", "strong_attack": "grove apocalypse",
  "player_abilities": ["earth_earth_earth_magic_lv3_earthshaker"],
  "base_str": 102, "base_dex": 18, "base_con": 96, "base_int": 16, "base_hp": 36000, "base_ap": 16,
  "str_per_level": 20, "dex_per_level": 3, "con_per_level": 19, "int_per_level": 3},

 {"id": "aurelion_void_colossus", "name": "Aurelion Shadow Colossus", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 88, "rarity": "superrare", "base_xp": 38000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (13000, 44000),
  "basic_attack": "void fist", "strong_attack": "void forest eruption",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 24, "base_dex": 24, "base_con": 24, "base_int": 118, "base_hp": 40000, "base_ap": 98,
  "str_per_level": 5, "dex_per_level": 5, "con_per_level": 5, "int_per_level": 24},
]
