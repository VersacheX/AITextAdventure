# Swamp Large City (The Necropolis) — hostile seeds levels 31–40.

RANDOM_HOSTILE_SEEDS = [
 {"id": "necropolis_enforcer", "name": "Necropolis Enforcer", "hostile_type": "undead", "role": "damage", "min_spawn_level": 32, "rarity": "uncommon", "base_xp": 560,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (100, 360),
  "basic_attack": "bone slam", "strong_attack": "necrotic rush",
  "player_abilities": [],
  "base_str": 18, "base_dex": 6, "base_con": 16, "base_int": 4, "base_hp": 500, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 0, "con_per_level": 3, "int_per_level": 0},
 {"id": "necro_crime_lord", "name": "Necropolis Crime Lord", "hostile_type": "undead", "role": "damage", "min_spawn_level": 40, "rarity": "rare", "base_xp": 1100,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (400, 1400),
  "basic_attack": "lord's bone blade", "strong_attack": "necropolis decree",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 28, "base_dex": 10, "base_con": 26, "base_int": 10, "base_hp": 900, "base_ap": 10,
  "str_per_level": 5, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 2},
]
