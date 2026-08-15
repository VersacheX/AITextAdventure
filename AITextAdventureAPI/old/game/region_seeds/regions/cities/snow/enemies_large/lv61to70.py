# Snow Large City (Frostgate Spire) — hostile seeds levels 61–70.

RANDOM_HOSTILE_SEEDS = [
 {"id": "frost_lich_lg", "name": "Frost Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 65, "rarity": "superrare", "base_xp": 11000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (3000, 10000),
  "basic_attack": "frost death bolt", "strong_attack": "lich ice storm",
  "player_abilities": ["ice_magic_lv1_frostbolt", "ice_ice_magic_lv2_glacier_burst", "ice_ice_ice_magic_lv3_hailstorm"],
  "base_str": 8, "base_dex": 12, "base_con": 10, "base_int": 62, "base_hp": 3600, "base_ap": 52,
  "str_per_level": 1, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 13},
 {"id": "spire_ice_colossus", "name": "Spire Ice Colossus", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 62, "rarity": "superrare", "base_xp": 9000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (2500, 8500),
  "basic_attack": "ice colossus slam", "strong_attack": "spire avalanche",
  "player_abilities": ["ice_ice_magic_lv2_glacier_burst"],
  "base_str": 68, "base_dex": 8, "base_con": 64, "base_int": 10, "base_hp": 12000, "base_ap": 12,
  "str_per_level": 14, "dex_per_level": 1, "con_per_level": 13, "int_per_level": 2},
]
