# Mountains Large City (Ironveil Foundry) — hostile seeds levels 31–40.

RANDOM_HOSTILE_SEEDS = [
 {"id": "foundry_crime_lord", "name": "Foundry Crime Lord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 36, "rarity": "rare", "base_xp": 800,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (300, 1000),
  "basic_attack": "lord's hammer", "strong_attack": "iron decree",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 26, "base_dex": 10, "base_con": 24, "base_int": 8, "base_hp": 720, "base_ap": 10,
  "str_per_level": 5, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 1},
 {"id": "iron_sorcerer_lg", "name": "Iron Sorcerer", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 33, "rarity": "uncommon", "base_xp": 540,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (120, 400),
  "basic_attack": "iron bolt", "strong_attack": "foundry hex",
  "player_abilities": ["earth_magic_lv1_tremor", "fire_earth_magic_lv2_magma_javelin"],
  "base_str": 4, "base_dex": 8, "base_con": 6, "base_int": 22, "base_hp": 330, "base_ap": 20,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 5},
]
