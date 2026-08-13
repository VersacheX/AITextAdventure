# LEVEL 21-30 hostile regional (mountains overworld).

SEEDS_LV21TO30 = [

 # min_spawn_level == 21
 {"id": "peak_raider", "name": "Peak Raider", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 230,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (60, 200),
  "basic_attack": "axe swing", "strong_attack": "avalanche charge",
  "player_abilities": [],
  "base_str": 14, "base_dex": 8, "base_con": 12, "base_int": 3, "base_hp": 320, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 0},

 {"id": "stone_wraith", "name": "Stone Wraith", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 320,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "stone chill", "strong_attack": "mountain haunt",
  "player_abilities": ["level_1_hostile_ability_night_whisper"],
  "base_str": 4, "base_dex": 10, "base_con": 6, "base_int": 14, "base_hp": 280, "base_ap": 14,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 3},

 # min_spawn_level == 24
 {"id": "mountain_giant", "name": "Mountain Giant", "hostile_type": "creature", "role": "damage", "min_spawn_level": 24, "rarity": "uncommon", "base_xp": 440,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (10, 50),
  "basic_attack": "giant fist", "strong_attack": "boulder toss",
  "player_abilities": None,
  "base_str": 22, "base_dex": 2, "base_con": 20, "base_int": 2, "base_hp": 620, "base_ap": 4,
  "str_per_level": 5, "dex_per_level": 0, "con_per_level": 4, "int_per_level": 0},

 # min_spawn_level == 27
 {"id": "frost_drake", "name": "Frost Drake", "hostile_type": "creature", "role": "damage", "min_spawn_level": 27, "rarity": "rare", "base_xp": 700,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (100, 360),
  "basic_attack": "frost claw", "strong_attack": "ice breath",
  "player_abilities": ["ice_magic_lv1_frostbolt", "ice_water_magic_lv2_glacier_spike"],
  "base_str": 20, "base_dex": 10, "base_con": 18, "base_int": 8, "base_hp": 600, "base_ap": 10,
  "str_per_level": 4, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 2},

 # min_spawn_level == 30
 {"id": "peak_titan", "name": "Peak Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 30, "rarity": "superrare", "base_xp": 1600,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (150, 500),
  "basic_attack": "titan fist", "strong_attack": "peak sunder",
  "player_abilities": ["earth_magic_lv1_tremor"],
  "base_str": 28, "base_dex": 4, "base_con": 26, "base_int": 4, "base_hp": 1100, "base_ap": 8,
  "str_per_level": 6, "dex_per_level": 0, "con_per_level": 5, "int_per_level": 0},
]