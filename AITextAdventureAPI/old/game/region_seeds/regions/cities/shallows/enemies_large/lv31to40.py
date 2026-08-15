# Shallows Large City (Brineward Harbor) — hostile seeds levels 31–40.

RANDOM_HOSTILE_SEEDS = [
 {"id": "sea_witch_lg", "name": "Sea Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 500,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (100, 360),
  "basic_attack": "tide hex", "strong_attack": "deep sea curse",
  "player_abilities": ["water_magic_lv1_spray_shard", "water_dark_magic_lv2_abyssal_tide"],
  "base_str": 4, "base_dex": 12, "base_con": 6, "base_int": 22, "base_hp": 300, "base_ap": 20,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 5},
 {"id": "harbor_crime_lord", "name": "Harbor Crime Lord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 38, "rarity": "rare", "base_xp": 900,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (360, 1200),
  "basic_attack": "lord's blade", "strong_attack": "harbor decree",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 26, "base_dex": 14, "base_con": 24, "base_int": 8, "base_hp": 800, "base_ap": 12,
  "str_per_level": 5, "dex_per_level": 2, "con_per_level": 4, "int_per_level": 1},
]
