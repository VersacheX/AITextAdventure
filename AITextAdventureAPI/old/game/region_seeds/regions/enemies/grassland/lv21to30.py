# LEVEL 21-30 hostile regional (grassland overworld).

SEEDS_LV21TO30 = [

 # min_spawn_level == 21
 {"id": "plains_marauder", "name": "Plains Marauder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 220,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (50, 180),
  "basic_attack": "plains cleave", "strong_attack": "marauder rush",
  "player_abilities": [],
  "base_str": 12, "base_dex": 10, "base_con": 10, "base_int": 3, "base_hp": 300, "base_ap": 10,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},

 {"id": "grassland_wraith", "name": "Grassland Wraith", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 320,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "wraith grasp", "strong_attack": "plains wail",
  "player_abilities": ["level_1_hostile_ability_night_whisper"],
  "base_str": 4, "base_dex": 12, "base_con": 6, "base_int": 14, "base_hp": 280, "base_ap": 14,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 3},

 # min_spawn_level == 24
 {"id": "thunderhorn", "name": "Thunderhorn", "hostile_type": "creature", "role": "damage", "min_spawn_level": 24, "rarity": "uncommon", "base_xp": 380,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (10, 50),
  "basic_attack": "horn charge", "strong_attack": "thunderous stampede",
  "player_abilities": ["electric_magic_lv1_fireball"],
  "base_str": 18, "base_dex": 8, "base_con": 16, "base_int": 4, "base_hp": 480, "base_ap": 8,
  "str_per_level": 4, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},

 # min_spawn_level == 27
 {"id": "plains_shaman", "name": "Plains Shaman", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 27, "rarity": "uncommon", "base_xp": 420,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 300),
  "basic_attack": "shaman hex", "strong_attack": "storm call",
  "player_abilities": ["air_magic_lv1_shredding_gust", "electric_fire_magic_lv2_arclance"],
  "base_str": 4, "base_dex": 8, "base_con": 6, "base_int": 18, "base_hp": 260, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},

 # min_spawn_level == 30
 {"id": "plains_colossus", "name": "Plains Colossus", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 30, "rarity": "superrare", "base_xp": 1400,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (100, 400),
  "basic_attack": "colossal stomp", "strong_attack": "plains quake",
  "player_abilities": ["earth_magic_lv1_tremor"],
  "base_str": 24, "base_dex": 4, "base_con": 22, "base_int": 4, "base_hp": 900, "base_ap": 8,
  "str_per_level": 5, "dex_per_level": 0, "con_per_level": 4, "int_per_level": 0},
]