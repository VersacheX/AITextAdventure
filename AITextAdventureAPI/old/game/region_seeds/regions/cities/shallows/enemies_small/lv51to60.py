# Shallows Small City (Tidekin Cove) — hostile seeds levels 51–60.

RANDOM_HOSTILE_SEEDS = [
 {"id": "cove_lich_sm", "name": "Cove Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 54, "rarity": "superrare", "base_xp": 5000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (1100, 3700),
  "basic_attack": "cove death bolt", "strong_attack": "tidekin lich storm",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 6, "base_dex": 10, "base_con": 8, "base_int": 48, "base_hp": 1800, "base_ap": 40,
  "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 10},
 {"id": "cove_sea_serpent", "name": "Cove Sea Serpent", "hostile_type": "creature", "role": "damage", "min_spawn_level": 58, "rarity": "rare", "base_xp": 3200,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (700, 2400),
  "basic_attack": "serpent bite", "strong_attack": "cove constrict",
  "player_abilities": ["water_magic_lv1_spray_shard"],
  "base_str": 46, "base_dex": 16, "base_con": 42, "base_int": 8, "base_hp": 3400, "base_ap": 12,
  "str_per_level": 9, "dex_per_level": 2, "con_per_level": 8, "int_per_level": 1},
]
