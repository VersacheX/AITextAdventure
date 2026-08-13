# Mountains Overworld — hostile seeds levels 31-100.

SEEDS_LV31TO100 = [

 # min_spawn_level == 31
 {"id": "peak_warlord", "name": "Peak Warlord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 540,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (120, 420),
  "basic_attack": "peak war cry", "strong_attack": "mountain charge",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 20, "base_dex": 8, "base_con": 18, "base_int": 4, "base_hp": 500, "base_ap": 8,
  "str_per_level": 4, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 0},

 {"id": "avalanche_elemental", "name": "Avalanche Elemental", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 500,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 30),
  "basic_attack": "rock slide", "strong_attack": "avalanche wave",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field"],
  "base_str": 22, "base_dex": 4, "base_con": 20, "base_int": 6, "base_hp": 580, "base_ap": 8,
  "str_per_level": 5, "dex_per_level": 0, "con_per_level": 4, "int_per_level": 1},

 # min_spawn_level == 38
 {"id": "frost_wyvern", "name": "Frost Wyvern", "hostile_type": "creature", "role": "damage", "min_spawn_level": 38, "rarity": "superrare", "base_xp": 2400,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (400, 1400),
  "basic_attack": "frost claw swipe", "strong_attack": "ice storm breath",
  "player_abilities": ["ice_magic_lv1_frostbolt", "ice_ice_magic_lv2_glacier_burst"],
  "base_str": 32, "base_dex": 14, "base_con": 30, "base_int": 10, "base_hp": 1600, "base_ap": 12,
  "str_per_level": 6, "dex_per_level": 2, "con_per_level": 6, "int_per_level": 2},

 # min_spawn_level == 50
 {"id": "mountain_leviathan", "name": "Mountain Leviathan", "hostile_type": "creature", "role": "damage", "min_spawn_level": 50, "rarity": "superrare", "base_xp": 6500,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1200, 4200),
  "basic_attack": "mountain coil", "strong_attack": "peak burial",
  "player_abilities": None,
  "base_str": 56, "base_dex": 8, "base_con": 52, "base_int": 4, "base_hp": 5000, "base_ap": 8,
  "str_per_level": 11, "dex_per_level": 1, "con_per_level": 10, "int_per_level": 0},

 # min_spawn_level == 65
 {"id": "glacier_titan", "name": "Glacier Titan", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 65, "rarity": "superrare", "base_xp": 12000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (3000, 10000),
  "basic_attack": "glacier fist", "strong_attack": "ice age collapse",
  "player_abilities": ["ice_magic_lv1_frostbolt", "ice_ice_magic_lv2_glacier_burst", "ice_ice_ice_magic_lv3_hailstorm"],
  "base_str": 60, "base_dex": 10, "base_con": 56, "base_int": 20, "base_hp": 12000, "base_ap": 14,
  "str_per_level": 12, "dex_per_level": 1, "con_per_level": 11, "int_per_level": 4},

 # min_spawn_level == 100
 {"id": "mountain_world_god", "name": "Mountain World God", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 120000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (50000, 160000),
  "basic_attack": "world peak decree", "strong_attack": "end of the mountain age",
  "player_abilities": ["earth_earth_earth_magic_lv3_earthshaker", "ice_ice_ice_magic_lv3_hailstorm"],
  "base_str": 140, "base_dex": 22, "base_con": 132, "base_int": 28, "base_hp": 100000, "base_ap": 22,
  "str_per_level": 28, "dex_per_level": 4, "con_per_level": 26, "int_per_level": 5},

 # min_spawn_level == 51 (fills Lv51-60 gap)
 {"id": "mountain_rock_wyrm", "name": "Rock Wyrm", "hostile_type": "creature", "role": "damage", "min_spawn_level": 51, "rarity": "superrare", "base_xp": 7000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1500, 5000),
  "basic_attack": "rock bite", "strong_attack": "stone crush",
  "player_abilities": ["earth_magic_lv1_tremor"],
  "base_str": 58, "base_dex": 10, "base_con": 54, "base_int": 8, "base_hp": 6000, "base_ap": 10,
  "str_per_level": 12, "dex_per_level": 1, "con_per_level": 11, "int_per_level": 1},

 {"id": "mountain_ice_colossus", "name": "Ice Colossus", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 56, "rarity": "superrare", "base_xp": 9000,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (500, 2000),
  "basic_attack": "glacier fist", "strong_attack": "absolute freeze",
  "player_abilities": ["ice_ice_magic_lv2_glacier_burst"],
  "base_str": 64, "base_dex": 4, "base_con": 60, "base_int": 10, "base_hp": 9000, "base_ap": 12,
  "str_per_level": 13, "dex_per_level": 0, "con_per_level": 12, "int_per_level": 2},

 # min_spawn_level == 71 (fills Lv71-80 gap)
 {"id": "mountain_elder_golem", "name": "Elder Mountain Golem", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 71, "rarity": "superrare", "base_xp": 19000,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (5000, 17000),
  "basic_attack": "elder slam", "strong_attack": "mountain collapse",
  "player_abilities": ["earth_earth_magic_lv2_quake_field", "level_1_hostile_ability_reinforce_frame"],
  "base_str": 84, "base_dex": 6, "base_con": 78, "base_int": 10, "base_hp": 18000, "base_ap": 12,
  "str_per_level": 17, "dex_per_level": 1, "con_per_level": 16, "int_per_level": 2},

 {"id": "mountain_frost_dragon", "name": "Mountain Frost Dragon", "hostile_type": "creature", "role": "damage", "min_spawn_level": 76, "rarity": "superrare", "base_xp": 23000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (7500, 25000),
  "basic_attack": "frost fang", "strong_attack": "blizzard breath",
  "player_abilities": ["ice_ice_ice_magic_lv3_hailstorm"],
  "base_str": 94, "base_dex": 16, "base_con": 88, "base_int": 14, "base_hp": 22000, "base_ap": 16,
  "str_per_level": 19, "dex_per_level": 3, "con_per_level": 18, "int_per_level": 2},

 # min_spawn_level == 81 (fills Lv81-90 gap)
 {"id": "mountain_shadow_colossus", "name": "Mountain Shadow Colossus", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 81, "rarity": "superrare", "base_xp": 33000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (11000, 36000),
  "basic_attack": "shadow fist", "strong_attack": "void mountain eruption",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 22, "base_dex": 20, "base_con": 22, "base_int": 114, "base_hp": 30000, "base_ap": 94,
  "str_per_level": 4, "dex_per_level": 4, "con_per_level": 4, "int_per_level": 23},

 {"id": "mountain_peak_titan", "name": "Peak Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 86, "rarity": "superrare", "base_xp": 42000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (15000, 50000),
  "basic_attack": "peak titan slam", "strong_attack": "mountain world shatter",
  "player_abilities": ["earth_earth_earth_magic_lv3_earthshaker"],
  "base_str": 120, "base_dex": 18, "base_con": 114, "base_int": 20, "base_hp": 46000, "base_ap": 20,
  "str_per_level": 24, "dex_per_level": 3, "con_per_level": 23, "int_per_level": 4},
]
