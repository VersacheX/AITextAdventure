# Swamp Mid City (Bayou Nocturne) — hostile seeds levels 61–70.

RANDOM_HOSTILE_SEEDS = [
 {"id": "bayou_lich", "name": "Bayou Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 62, "rarity": "superrare", "base_xp": 9000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (2000, 7000),
  "basic_attack": "bayou death bolt", "strong_attack": "lich bog storm",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 8, "base_dex": 10, "base_con": 10, "base_int": 57, "base_hp": 2600, "base_ap": 47,
  "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 12},
 {"id": "bayou_death_knight", "name": "Bayou Death Knight", "hostile_type": "undead", "role": "damage", "min_spawn_level": 66, "rarity": "superrare", "base_xp": 8500,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (2400, 8000),
  "basic_attack": "dark bog blade", "strong_attack": "bayou charge",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "level_1_hostile_ability_inspire"],
  "base_str": 62, "base_dex": 12, "base_con": 58, "base_int": 14, "base_hp": 12000, "base_ap": 14,
  "str_per_level": 12, "dex_per_level": 2, "con_per_level": 11, "int_per_level": 3},
]
