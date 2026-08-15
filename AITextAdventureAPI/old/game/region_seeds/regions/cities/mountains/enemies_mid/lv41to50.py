# Mountains Mid City (Gallows Rift) — hostile seeds levels 41–50.

RANDOM_HOSTILE_SEEDS = [
 {"id": "rift_golem", "name": "Rift Golem", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 42, "rarity": "rare", "base_xp": 900,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 40),
  "basic_attack": "rift slam", "strong_attack": "cliff collapse",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 32, "base_dex": 2, "base_con": 28, "base_int": 6, "base_hp": 1100, "base_ap": 8,
  "str_per_level": 6, "dex_per_level": 0, "con_per_level": 5, "int_per_level": 1},
 {"id": "gallows_enforcer_elite", "name": "Gallows Elite Enforcer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 46, "rarity": "uncommon", "base_xp": 1100,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (300, 1000),
  "basic_attack": "elite rift slash", "strong_attack": "gallows decree",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 30, "base_dex": 12, "base_con": 28, "base_int": 6, "base_hp": 1400, "base_ap": 10,
  "str_per_level": 6, "dex_per_level": 2, "con_per_level": 5, "int_per_level": 1},
]
