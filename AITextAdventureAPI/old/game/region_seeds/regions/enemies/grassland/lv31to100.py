# Grassland Overworld — hostile seeds levels 31-100.

SEEDS_LV31TO100 = [

 # min_spawn_level == 31
 {"id": "warlord_of_the_plains", "name": "Warlord of the Plains", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 520,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (120, 400),
  "basic_attack": "plains war cry", "strong_attack": "warlord charge",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 18, "base_dex": 10, "base_con": 16, "base_int": 4, "base_hp": 480, "base_ap": 10,
  "str_per_level": 4, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},

 {"id": "storm_spirit", "name": "Storm Spirit", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 480,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (10, 50),
  "basic_attack": "lightning touch", "strong_attack": "storm burst",
  "player_abilities": ["electric_magic_lv1_fireball", "electric_electric_magic_lv2_chain_bolt"],
  "base_str": 8, "base_dex": 16, "base_con": 8, "base_int": 20, "base_hp": 360, "base_ap": 18,
  "str_per_level": 1, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 5},

 # min_spawn_level == 38
 {"id": "tempest_dragon", "name": "Tempest Dragon", "hostile_type": "creature", "role": "damage", "min_spawn_level": 38, "rarity": "superrare", "base_xp": 2200,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (400, 1400),
  "basic_attack": "tempest claw", "strong_attack": "lightning breath",
  "player_abilities": ["electric_magic_lv1_fireball", "electric_fire_magic_lv2_arclance"],
  "base_str": 30, "base_dex": 14, "base_con": 28, "base_int": 10, "base_hp": 1400, "base_ap": 12,
  "str_per_level": 6, "dex_per_level": 2, "con_per_level": 5, "int_per_level": 2},

 # min_spawn_level == 50
 {"id": "prairie_leviathan", "name": "Prairie Leviathan", "hostile_type": "creature", "role": "damage", "min_spawn_level": 50, "rarity": "superrare", "base_xp": 6000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1200, 4000),
  "basic_attack": "prairie coil", "strong_attack": "land burial",
  "player_abilities": None,
  "base_str": 52, "base_dex": 8, "base_con": 48, "base_int": 4, "base_hp": 4800, "base_ap": 8,
  "str_per_level": 10, "dex_per_level": 1, "con_per_level": 9, "int_per_level": 0},

 # min_spawn_level == 65
 {"id": "storm_titan", "name": "Storm Titan", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 65, "rarity": "superrare", "base_xp": 11000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (3000, 10000),
  "basic_attack": "titan lightning fist", "strong_attack": "thunderstorm annihilation",
  "player_abilities": ["electric_electric_magic_lv2_chain_bolt", "electric_electric_electric_magic_lv3_thunderstorm"],
  "base_str": 36, "base_dex": 24, "base_con": 34, "base_int": 60, "base_hp": 9000, "base_ap": 50,
  "str_per_level": 7, "dex_per_level": 4, "con_per_level": 6, "int_per_level": 12},

 # min_spawn_level == 100
 {"id": "plains_world_god", "name": "Plains World God", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 120000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (50000, 160000),
  "basic_attack": "world storm decree", "strong_attack": "end of the plains age",
  "player_abilities": ["electric_electric_electric_magic_lv3_thunderstorm", "air_air_air_magic_lv3_storm_surge"],
  "base_str": 130, "base_dex": 30, "base_con": 124, "base_int": 36, "base_hp": 100000, "base_ap": 26,
  "str_per_level": 26, "dex_per_level": 6, "con_per_level": 24, "int_per_level": 7},

 # min_spawn_level == 51 (fills Lv51-60 gap)
 {"id": "plains_thunderbird", "name": "Plains Thunderbird", "hostile_type": "creature", "role": "damage", "min_spawn_level": 51, "rarity": "superrare", "base_xp": 6500,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1400, 4800),
  "basic_attack": "thunder talon", "strong_attack": "storm dive",
  "player_abilities": ["electric_magic_lv1_fireball", "electric_electric_magic_lv2_chain_bolt"],
  "base_str": 54, "base_dex": 28, "base_con": 50, "base_int": 14, "base_hp": 5000, "base_ap": 16,
  "str_per_level": 11, "dex_per_level": 5, "con_per_level": 10, "int_per_level": 3},

 {"id": "plains_earth_golem_lg", "name": "Plains Earth Golem", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 56, "rarity": "superrare", "base_xp": 8500,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (500, 1800),
  "basic_attack": "earth fist", "strong_attack": "seismic slam",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field"],
  "base_str": 62, "base_dex": 4, "base_con": 58, "base_int": 8, "base_hp": 8000, "base_ap": 10,
  "str_per_level": 12, "dex_per_level": 0, "con_per_level": 11, "int_per_level": 1},

 # min_spawn_level == 71 (fills Lv71-80 gap)
 {"id": "plains_elder_basilisk", "name": "Elder Basilisk", "hostile_type": "creature", "role": "hazard", "min_spawn_level": 71, "rarity": "superrare", "base_xp": 18000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (5000, 17000),
  "basic_attack": "basilisk gaze", "strong_attack": "petrify stare",
  "player_abilities": ["level_1_hostile_ability_petrify_gaze"],
  "base_str": 70, "base_dex": 16, "base_con": 66, "base_int": 18, "base_hp": 14000, "base_ap": 18,
  "str_per_level": 14, "dex_per_level": 3, "con_per_level": 13, "int_per_level": 3},

 {"id": "plains_wind_titan", "name": "Plains Wind Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 76, "rarity": "superrare", "base_xp": 22000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (7000, 23000),
  "basic_attack": "wind titan slam", "strong_attack": "storm shatter",
  "player_abilities": ["electric_electric_electric_magic_lv3_thunderstorm"],
  "base_str": 90, "base_dex": 22, "base_con": 84, "base_int": 14, "base_hp": 22000, "base_ap": 16,
  "str_per_level": 18, "dex_per_level": 4, "con_per_level": 17, "int_per_level": 2},

 # min_spawn_level == 81 (fills Lv81-90 gap)
 {"id": "plains_shadow_colossus", "name": "Grassland Shadow Colossus", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 81, "rarity": "superrare", "base_xp": 32000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (10000, 34000),
  "basic_attack": "shadow fist", "strong_attack": "void eruption",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 22, "base_dex": 22, "base_con": 22, "base_int": 112, "base_hp": 28000, "base_ap": 92,
  "str_per_level": 4, "dex_per_level": 4, "con_per_level": 4, "int_per_level": 22},

 {"id": "plains_storm_titan", "name": "Savanna Storm Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 86, "rarity": "superrare", "base_xp": 40000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (14000, 46000),
  "basic_attack": "storm titan slam", "strong_attack": "plains world shatter",
  "player_abilities": ["electric_electric_electric_magic_lv3_thunderstorm"],
  "base_str": 118, "base_dex": 26, "base_con": 112, "base_int": 22, "base_hp": 44000, "base_ap": 20,
  "str_per_level": 23, "dex_per_level": 5, "con_per_level": 22, "int_per_level": 4},
]
