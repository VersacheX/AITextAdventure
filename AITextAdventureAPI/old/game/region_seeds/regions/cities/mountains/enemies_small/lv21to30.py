# Mountains Small City (Hollerforge Hollow) — hostile seeds levels 21–30.

RANDOM_HOSTILE_SEEDS = [
 {"id": "hollow_miner", "name": "Hollow Miner", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 220,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (50, 180),
  "basic_attack": "pickaxe strike", "strong_attack": "miner's fury",
  "player_abilities": [], "base_str": 14, "base_dex": 6, "base_con": 12, "base_int": 2, "base_hp": 300, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 0, "con_per_level": 3, "int_per_level": 0},
 {"id": "forge_shade_sm", "name": "Forge Shade", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 23, "rarity": "uncommon", "base_xp": 280,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (15, 60),
  "basic_attack": "ash touch", "strong_attack": "forge haunt",
  "player_abilities": ["level_1_hostile_ability_night_whisper"],
  "base_str": 3, "base_dex": 8, "base_con": 5, "base_int": 12, "base_hp": 220, "base_ap": 12,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 3},
 {"id": "hollow_forgemaster", "name": "Hollow Forgemaster", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 30, "rarity": "rare", "base_xp": 600,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (200, 700),
  "basic_attack": "forge hammer", "strong_attack": "master's decree",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 22, "base_dex": 8, "base_con": 20, "base_int": 6, "base_hp": 560, "base_ap": 10,
  "str_per_level": 4, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 1},
]
