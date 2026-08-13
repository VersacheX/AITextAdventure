# Shallows Overworld — hostile seeds levels 31-100.

SEEDS_LV31TO100 = [

 # min_spawn_level == 31
 {"id": "tide_commander", "name": "Tide Commander", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 500,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (120, 400),
  "basic_attack": "current strike", "strong_attack": "tide command",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 16, "base_dex": 14, "base_con": 14, "base_int": 6, "base_hp": 460, "base_ap": 12,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 1},

 {"id": "abyssal_eel", "name": "Abyssal Eel", "hostile_type": "creature", "role": "damage", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 480,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (10, 50),
  "basic_attack": "eel lunge", "strong_attack": "electric bite",
  "player_abilities": ["electric_magic_lv1_fireball"],
  "base_str": 16, "base_dex": 18, "base_con": 14, "base_int": 6, "base_hp": 440, "base_ap": 12,
  "str_per_level": 3, "dex_per_level": 3, "con_per_level": 2, "int_per_level": 1},

 # min_spawn_level == 38
 {"id": "sea_dragon", "name": "Sea Dragon", "hostile_type": "creature", "role": "damage", "min_spawn_level": 38, "rarity": "superrare", "base_xp": 2400,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (400, 1400),
  "basic_attack": "sea claw", "strong_attack": "tsunami breath",
  "player_abilities": ["water_magic_lv1_spray_shard", "water_water_magic_lv2_deluge_burst"],
  "base_str": 32, "base_dex": 16, "base_con": 30, "base_int": 10, "base_hp": 1600, "base_ap": 12,
  "str_per_level": 6, "dex_per_level": 2, "con_per_level": 6, "int_per_level": 2},

 # min_spawn_level == 50
 {"id": "ocean_leviathan", "name": "Ocean Leviathan", "hostile_type": "creature", "role": "damage", "min_spawn_level": 50, "rarity": "superrare", "base_xp": 7000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1500, 5000),
  "basic_attack": "ocean coil", "strong_attack": "deep water burial",
  "player_abilities": None,
  "base_str": 58, "base_dex": 12, "base_con": 54, "base_int": 6, "base_hp": 5500, "base_ap": 10,
  "str_per_level": 11, "dex_per_level": 2, "con_per_level": 10, "int_per_level": 0},

 # min_spawn_level == 65
 {"id": "tidal_titan", "name": "Tidal Titan", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 65, "rarity": "superrare", "base_xp": 13000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (3500, 12000),
  "basic_attack": "tidal fist", "strong_attack": "ocean obliteration",
  "player_abilities": ["water_magic_lv1_spray_shard", "water_water_magic_lv2_deluge_burst", "water_water_water_magic_lv3_tsunami_burst"],
  "base_str": 60, "base_dex": 14, "base_con": 56, "base_int": 22, "base_hp": 12000, "base_ap": 16,
  "str_per_level": 12, "dex_per_level": 2, "con_per_level": 11, "int_per_level": 4},

 # min_spawn_level == 100
 {"id": "ocean_world_god", "name": "Ocean World God", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 120000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (50000, 160000),
  "basic_attack": "world tide decree", "strong_attack": "end of the shallows age",
  "player_abilities": ["water_water_water_magic_lv3_tsunami_burst"],
  "base_str": 136, "base_dex": 28, "base_con": 130, "base_int": 30, "base_hp": 100000, "base_ap": 24,
  "str_per_level": 27, "dex_per_level": 5, "con_per_level": 26, "int_per_level": 6},

 # min_spawn_level == 51 (fills Lv51-60 gap)
 {"id": "shallows_sea_wyrm", "name": "Sea Wyrm", "hostile_type": "creature", "role": "damage", "min_spawn_level": 51, "rarity": "superrare", "base_xp": 7000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1500, 5000),
  "basic_attack": "tide bite", "strong_attack": "deep surge",
  "player_abilities": ["water_magic_lv1_spray_shard"],
  "base_str": 56, "base_dex": 16, "base_con": 52, "base_int": 8, "base_hp": 5500, "base_ap": 12,
  "str_per_level": 11, "dex_per_level": 3, "con_per_level": 10, "int_per_level": 1},

 {"id": "shallows_deep_golem", "name": "Deep Golem", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 57, "rarity": "superrare", "base_xp": 9000,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (500, 2000),
  "basic_attack": "coral fist", "strong_attack": "ocean crush",
  "player_abilities": ["water_water_magic_lv2_deluge_burst"],
  "base_str": 64, "base_dex": 4, "base_con": 60, "base_int": 8, "base_hp": 9000, "base_ap": 10,
  "str_per_level": 13, "dex_per_level": 0, "con_per_level": 12, "int_per_level": 1},

 # min_spawn_level == 71 (fills Lv71-80 gap)
 {"id": "shallows_elder_kraken", "name": "Elder Kraken", "hostile_type": "creature", "role": "damage", "min_spawn_level": 71, "rarity": "superrare", "base_xp": 20000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (6000, 20000),
  "basic_attack": "kraken slam", "strong_attack": "tentacle storm",
  "player_abilities": ["water_water_water_magic_lv3_tsunami_burst"],
  "base_str": 86, "base_dex": 14, "base_con": 80, "base_int": 12, "base_hp": 18000, "base_ap": 14,
  "str_per_level": 17, "dex_per_level": 2, "con_per_level": 16, "int_per_level": 2},

 {"id": "shallows_sea_titan", "name": "Sea Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 76, "rarity": "superrare", "base_xp": 24000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (8000, 27000),
  "basic_attack": "sea titan slam", "strong_attack": "ocean shatter",
  "player_abilities": ["water_water_water_magic_lv3_tsunami_burst"],
  "base_str": 96, "base_dex": 16, "base_con": 90, "base_int": 12, "base_hp": 24000, "base_ap": 14,
  "str_per_level": 19, "dex_per_level": 3, "con_per_level": 18, "int_per_level": 2},

 # min_spawn_level == 81 (fills Lv81-90 gap)
 {"id": "shallows_abyss_colossus", "name": "Abyss Colossus", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 81, "rarity": "superrare", "base_xp": 33000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (11000, 36000),
  "basic_attack": "abyss fist", "strong_attack": "void tide eruption",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "water_water_water_magic_lv3_tsunami_burst"],
  "base_str": 20, "base_dex": 24, "base_con": 20, "base_int": 114, "base_hp": 30000, "base_ap": 94,
  "str_per_level": 4, "dex_per_level": 5, "con_per_level": 4, "int_per_level": 23},

 {"id": "shallows_tide_titan_ow", "name": "Elder Tide Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 86, "rarity": "superrare", "base_xp": 42000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (15000, 50000),
  "basic_attack": "elder tide slam", "strong_attack": "shallows world shatter",
  "player_abilities": ["water_water_water_magic_lv3_tsunami_burst"],
  "base_str": 122, "base_dex": 20, "base_con": 116, "base_int": 18, "base_hp": 46000, "base_ap": 18,
  "str_per_level": 24, "dex_per_level": 4, "con_per_level": 23, "int_per_level": 3},
]
