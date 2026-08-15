# Grassland Large City (Crosswind Bazaar) — hostile seeds Lv 51–60.

RANDOM_HOSTILE_SEEDS = [
 {"id": "plains_lich", "name": "Plains Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 55, "rarity": "superrare", "base_xp": 6000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (1200, 4000),
  "basic_attack": "plains death bolt", "strong_attack": "lich plains storm",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 10, "base_dex": 12, "base_con": 12, "base_int": 52, "base_hp": 2000, "base_ap": 44,
  "str_per_level": 1, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 11},
 {"id": "storm_rider_elite", "name": "Storm Rider Elite", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 51, "rarity": "common", "base_xp": 1400,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (300, 1000),
  "basic_attack": "storm lance", "strong_attack": "rider charge",
  "player_abilities": ["lv2_hostile_ability_water_electric_magic_maelstrom_burst"],
  "base_str": 32, "base_dex": 30, "base_con": 28, "base_int": 10, "base_hp": 1520, "base_ap": 12,
  "str_per_level": 5, "dex_per_level": 5, "con_per_level": 4, "int_per_level": 1},
 {"id": "bazaar_shaman", "name": "Bazaar Shaman", "hostile_type": "humanoid", "role": "support", "min_spawn_level": 57, "rarity": "uncommon", "base_xp": 2000,
  "common_drop": "tome_int", "rare_drop": "tome_con", "money_range": (400, 1400),
  "basic_attack": "spirit hex", "strong_attack": "market blessing",
  "player_abilities": ["lv2_hostile_ability_dark_light_faith_calm_bleat"],
  "base_str": 8, "base_dex": 18, "base_con": 14, "base_int": 36, "base_hp": 1400, "base_ap": 16,
  "str_per_level": 1, "dex_per_level": 3, "con_per_level": 2, "int_per_level": 6},
]
