# Shallows Small City (Tidekin Cove) — hostile seeds levels 21–30.

RANDOM_HOSTILE_SEEDS = [
 {"id": "cove_thief", "name": "Cove Thief", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 200,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (40, 150),
  "basic_attack": "cove shiv", "strong_attack": "tidal ambush",
  "player_abilities": [], "base_str": 10, "base_dex": 12, "base_con": 8, "base_int": 3, "base_hp": 240, "base_ap": 10,
  "str_per_level": 2, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},
 {"id": "tidekin_shade", "name": "Tidekin Shade", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 23, "rarity": "uncommon", "base_xp": 280,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (15, 60),
  "basic_attack": "tide touch", "strong_attack": "cove wail",
  "player_abilities": ["level_1_hostile_ability_streamlet"],
  "base_str": 3, "base_dex": 12, "base_con": 5, "base_int": 12, "base_hp": 220, "base_ap": 12,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 3},
 {"id": "cove_raider", "name": "Cove Raider", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 28, "rarity": "common", "base_xp": 300,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (80, 280),
  "basic_attack": "raider slash", "strong_attack": "cove fury",
  "player_abilities": [], "base_str": 14, "base_dex": 12, "base_con": 12, "base_int": 2, "base_hp": 340, "base_ap": 10,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},
]
