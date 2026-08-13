# LEVEL 21-30 hostile regional (shallows overworld).

SEEDS_LV21TO30 = [

 # min_spawn_level == 21
 {"id": "reef_raider", "name": "Reef Raider", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 220,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (50, 180),
  "basic_attack": "coral blade", "strong_attack": "reef ambush",
  "player_abilities": [],
  "base_str": 12, "base_dex": 12, "base_con": 10, "base_int": 4, "base_hp": 300, "base_ap": 12,
  "str_per_level": 2, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},

 {"id": "water_shade", "name": "Water Shade", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 320,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "current grasp", "strong_attack": "water wail",
  "player_abilities": ["level_1_hostile_ability_streamlet"],
  "base_str": 4, "base_dex": 14, "base_con": 6, "base_int": 14, "base_hp": 260, "base_ap": 14,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 3},

 # min_spawn_level == 24
 {"id": "coral_golem", "name": "Coral Golem", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 24, "rarity": "uncommon", "base_xp": 380,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 20),
  "basic_attack": "coral slam", "strong_attack": "reef shatter",
  "player_abilities": ["water_magic_lv1_spray_shard"],
  "base_str": 18, "base_dex": 4, "base_con": 16, "base_int": 6, "base_hp": 460, "base_ap": 8,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 3, "int_per_level": 1},

 # min_spawn_level == 27
 {"id": "deep_sea_witch", "name": "Deep Sea Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 27, "rarity": "uncommon", "base_xp": 440,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 280),
  "basic_attack": "tide hex", "strong_attack": "deep current curse",
  "player_abilities": ["water_magic_lv1_spray_shard", "ice_water_magic_lv2_glacier_spike"],
  "base_str": 4, "base_dex": 10, "base_con": 6, "base_int": 18, "base_hp": 260, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},

 # min_spawn_level == 30
 {"id": "tidal_colossus", "name": "Tidal Colossus", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 30, "rarity": "superrare", "base_xp": 1500,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (100, 400),
  "basic_attack": "tidal slam", "strong_attack": "wave obliteration",
  "player_abilities": ["water_magic_lv1_spray_shard"],
  "base_str": 26, "base_dex": 8, "base_con": 24, "base_int": 6, "base_hp": 1000, "base_ap": 10,
  "str_per_level": 5, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 1},
]