# Swamp Mid City (Bayou Nocturne) — hostile seeds levels 31–40.

RANDOM_HOSTILE_SEEDS = [
 {"id": "bayou_revenant", "name": "Bayou Revenant", "hostile_type": "undead", "role": "damage", "min_spawn_level": 33, "rarity": "common", "base_xp": 500,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (80, 280),
  "basic_attack": "necrotic claw", "strong_attack": "bog surge",
  "player_abilities": [],
  "base_str": 18, "base_dex": 8, "base_con": 16, "base_int": 4, "base_hp": 560, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},
 {"id": "bayou_crime_boss", "name": "Bayou Crime Boss", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 38, "rarity": "rare", "base_xp": 800,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (300, 1000),
  "basic_attack": "boss's blade", "strong_attack": "bayou dominion",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 24, "base_dex": 12, "base_con": 22, "base_int": 8, "base_hp": 720, "base_ap": 10,
  "str_per_level": 5, "dex_per_level": 2, "con_per_level": 4, "int_per_level": 1},
]
