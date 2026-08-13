# Snow Overworld — hostile seeds levels 31-100.

SEEDS_LV31TO100 = [

 # min_spawn_level == 31
 {"id": "frost_warlord", "name": "Frost Warlord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 540,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (120, 420),
  "basic_attack": "ice axe", "strong_attack": "blizzard war cry",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 20, "base_dex": 8, "base_con": 18, "base_int": 4, "base_hp": 520, "base_ap": 8,
  "str_per_level": 4, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 0},

 {"id": "permafrost_elemental", "name": "Permafrost Elemental", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 520,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 30),
  "basic_attack": "frost slam", "strong_attack": "permafrost wave",
  "player_abilities": ["ice_magic_lv1_frostbolt", "ice_ice_magic_lv2_glacier_burst"],
  "base_str": 22, "base_dex": 4, "base_con": 20, "base_int": 8, "base_hp": 580, "base_ap": 10,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 4, "int_per_level": 2},

 # min_spawn_level == 38
 {"id": "ice_dragon_elder", "name": "Ice Dragon (Elder)", "hostile_type": "creature", "role": "damage", "min_spawn_level": 38, "rarity": "superrare", "base_xp": 2600,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (400, 1400),
  "basic_attack": "elder ice claw", "strong_attack": "absolute zero breath",
  "player_abilities": ["ice_magic_lv1_frostbolt", "ice_ice_magic_lv2_glacier_burst"],
  "base_str": 34, "base_dex": 12, "base_con": 32, "base_int": 10, "base_hp": 1800, "base_ap": 12,
  "str_per_level": 7, "dex_per_level": 1, "con_per_level": 6, "int_per_level": 2},

 # min_spawn_level == 50
 {"id": "blizzard_leviathan", "name": "Blizzard Leviathan", "hostile_type": "creature", "role": "damage", "min_spawn_level": 50, "rarity": "superrare", "base_xp": 7000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1200, 4200),
  "basic_attack": "blizzard coil", "strong_attack": "frost burial",
  "player_abilities": ["ice_magic_lv1_frostbolt"],
  "base_str": 58, "base_dex": 8, "base_con": 54, "base_int": 6, "base_hp": 5200, "base_ap": 8,
  "str_per_level": 11, "dex_per_level": 1, "con_per_level": 10, "int_per_level": 1},

 # min_spawn_level == 65
 {"id": "hailstorm_titan", "name": "Hailstorm Titan", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 65, "rarity": "superrare", "base_xp": 13000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (3500, 12000),
  "basic_attack": "hailstorm fist", "strong_attack": "ice age obliteration",
  "player_abilities": ["ice_magic_lv1_frostbolt", "ice_ice_magic_lv2_glacier_burst", "ice_ice_ice_magic_lv3_hailstorm"],
  "base_str": 62, "base_dex": 10, "base_con": 58, "base_int": 20, "base_hp": 12500, "base_ap": 14,
  "str_per_level": 12, "dex_per_level": 1, "con_per_level": 11, "int_per_level": 4},

 # min_spawn_level == 100
 {"id": "frost_world_god", "name": "Frost World God", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 120000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (50000, 160000),
  "basic_attack": "world frost decree", "strong_attack": "end of the snow age",
  "player_abilities": ["ice_ice_ice_magic_lv3_hailstorm"],
  "base_str": 142, "base_dex": 22, "base_con": 134, "base_int": 28, "base_hp": 100000, "base_ap": 22,
  "str_per_level": 28, "dex_per_level": 4, "con_per_level": 26, "int_per_level": 5},

 # min_spawn_level == 51 (fills Lv51-60 gap)
 {"id": "snow_frost_wyrm", "name": "Frost Wyrm", "hostile_type": "creature", "role": "damage", "min_spawn_level": 51, "rarity": "superrare", "base_xp": 7000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1500, 5000),
  "basic_attack": "frost bite", "strong_attack": "blizzard surge",
  "player_abilities": ["ice_magic_lv1_frostbolt"],
  "base_str": 58, "base_dex": 12, "base_con": 54, "base_int": 8, "base_hp": 5800, "base_ap": 10,
  "str_per_level": 12, "dex_per_level": 2, "con_per_level": 11, "int_per_level": 1},

 {"id": "snow_permafrost_golem", "name": "Permafrost Golem", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 57, "rarity": "superrare", "base_xp": 9000,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (500, 2000),
  "basic_attack": "ice fist", "strong_attack": "freeze shatter",
  "player_abilities": ["ice_ice_magic_lv2_glacier_burst"],
  "base_str": 64, "base_dex": 4, "base_con": 60, "base_int": 8, "base_hp": 9000, "base_ap": 10,
  "str_per_level": 13, "dex_per_level": 0, "con_per_level": 12, "int_per_level": 1},

 # min_spawn_level == 71 (fills Lv71-80 gap)
 {"id": "snow_elder_ice_dragon", "name": "Elder Ice Dragon", "hostile_type": "creature", "role": "damage", "min_spawn_level": 71, "rarity": "superrare", "base_xp": 20000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (6000, 20000),
  "basic_attack": "elder frost fang", "strong_attack": "absolute zero breath",
  "player_abilities": ["ice_ice_ice_magic_lv3_hailstorm"],
  "base_str": 88, "base_dex": 14, "base_con": 82, "base_int": 12, "base_hp": 18000, "base_ap": 14,
  "str_per_level": 18, "dex_per_level": 2, "con_per_level": 17, "int_per_level": 2},

 {"id": "snow_glacier_titan", "name": "Glacier Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 76, "rarity": "superrare", "base_xp": 24000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (8000, 27000),
  "basic_attack": "glacier titan slam", "strong_attack": "tundra annihilation",
  "player_abilities": ["ice_ice_ice_magic_lv3_hailstorm"],
  "base_str": 96, "base_dex": 12, "base_con": 92, "base_int": 12, "base_hp": 24000, "base_ap": 14,
  "str_per_level": 19, "dex_per_level": 2, "con_per_level": 18, "int_per_level": 2},

 # min_spawn_level == 81 (fills Lv81-90 gap)
 {"id": "snow_void_colossus", "name": "Snow Void Colossus", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 81, "rarity": "superrare", "base_xp": 33000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (11000, 36000),
  "basic_attack": "void fist", "strong_attack": "frozen void eruption",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "ice_ice_ice_magic_lv3_hailstorm"],
  "base_str": 22, "base_dex": 18, "base_con": 22, "base_int": 114, "base_hp": 30000, "base_ap": 94,
  "str_per_level": 4, "dex_per_level": 3, "con_per_level": 4, "int_per_level": 23},

 {"id": "snow_permafrost_titan", "name": "Permafrost Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 86, "rarity": "superrare", "base_xp": 42000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (15000, 50000),
  "basic_attack": "permafrost titan slam", "strong_attack": "snow world shatter",
  "player_abilities": ["ice_ice_ice_magic_lv3_hailstorm"],
  "base_str": 120, "base_dex": 16, "base_con": 116, "base_int": 18, "base_hp": 46000, "base_ap": 18,
  "str_per_level": 24, "dex_per_level": 3, "con_per_level": 23, "int_per_level": 3},
]
