# Mountains Mid City (Gallows Rift) — hostile seeds levels 21–30.

RANDOM_HOSTILE_SEEDS = [
 {"id": "rift_raider", "name": "Rift Raider", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 240,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (50, 180),
  "basic_attack": "rift slash", "strong_attack": "cliff ambush",
  "player_abilities": [], "base_str": 12, "base_dex": 10, "base_con": 10, "base_int": 3, "base_hp": 300, "base_ap": 10,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 0},
 {"id": "gallows_shade", "name": "Gallows Shade", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 22, "rarity": "uncommon", "base_xp": 300,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "gallows touch", "strong_attack": "rift wail",
  "player_abilities": ["level_1_hostile_ability_night_whisper"],
  "base_str": 4, "base_dex": 10, "base_con": 6, "base_int": 12, "base_hp": 260, "base_ap": 12,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 3},
 {"id": "cliff_berserker", "name": "Cliff Berserker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 27, "rarity": "common", "base_xp": 340,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (100, 340),
  "basic_attack": "cliff rush", "strong_attack": "avalanche fury",
  "player_abilities": [], "base_str": 16, "base_dex": 8, "base_con": 14, "base_int": 2, "base_hp": 380, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},
]
