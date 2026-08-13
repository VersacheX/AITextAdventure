# LEVEL 21-30 hostile regional (snow overworld).

SEEDS_LV21TO30 = [

 # min_spawn_level == 21
 {"id": "tundra_berserker", "name": "Tundra Berserker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 230,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (50, 180),
  "basic_attack": "frost axe", "strong_attack": "blizzard rage",
  "player_abilities": [],
  "base_str": 14, "base_dex": 8, "base_con": 12, "base_int": 3, "base_hp": 320, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 0},

 {"id": "ice_shade", "name": "Ice Shade", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 320,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "frost touch", "strong_attack": "blizzard wail",
  "player_abilities": ["ice_magic_lv1_frostbolt"],
  "base_str": 4, "base_dex": 10, "base_con": 6, "base_int": 14, "base_hp": 280, "base_ap": 14,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 3},

 # min_spawn_level == 24
 {"id": "frost_titan", "name": "Frost Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 24, "rarity": "uncommon", "base_xp": 420,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (10, 50),
  "basic_attack": "frost fist", "strong_attack": "glacier stomp",
  "player_abilities": ["ice_magic_lv1_frostbolt"],
  "base_str": 20, "base_dex": 4, "base_con": 18, "base_int": 4, "base_hp": 560, "base_ap": 6,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 4, "int_per_level": 0},

 # min_spawn_level == 27
 {"id": "blizzard_witch", "name": "Blizzard Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 27, "rarity": "uncommon", "base_xp": 440,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 280),
  "basic_attack": "frost hex", "strong_attack": "blizzard curse",
  "player_abilities": ["ice_magic_lv1_frostbolt", "ice_water_magic_lv2_glacier_spike"],
  "base_str": 4, "base_dex": 8, "base_con": 6, "base_int": 18, "base_hp": 260, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},

 # min_spawn_level == 30
 {"id": "glacier_colossus", "name": "Glacier Colossus", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 30, "rarity": "superrare", "base_xp": 1500,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (100, 400),
  "basic_attack": "glacier slam", "strong_attack": "ice age wave",
  "player_abilities": ["ice_magic_lv1_frostbolt", "ice_ice_magic_lv2_glacier_burst"],
  "base_str": 26, "base_dex": 4, "base_con": 24, "base_int": 6, "base_hp": 1100, "base_ap": 8,
  "str_per_level": 5, "dex_per_level": 0, "con_per_level": 5, "int_per_level": 1},
]