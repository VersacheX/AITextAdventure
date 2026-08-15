# Snow Mid City (Hailward Hold) — hostile seeds levels 31–40.

RANDOM_HOSTILE_SEEDS = [
 {"id": "hold_sorcerer", "name": "Hold Sorcerer", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 34, "rarity": "uncommon", "base_xp": 520,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (100, 360),
  "basic_attack": "frost bolt", "strong_attack": "hailward curse",
  "player_abilities": ["ice_magic_lv1_frostbolt", "ice_water_magic_lv2_glacier_spike"],
  "base_str": 4, "base_dex": 8, "base_con": 6, "base_int": 20, "base_hp": 300, "base_ap": 18,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 5},
 {"id": "hold_frost_reaver", "name": "Hold Frost Reaver", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 38, "rarity": "rare", "base_xp": 760,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (280, 940),
  "basic_attack": "frost reaver blade", "strong_attack": "hailward decree",
  "player_abilities": [],
  "base_str": 24, "base_dex": 10, "base_con": 22, "base_int": 4, "base_hp": 680, "base_ap": 10,
  "str_per_level": 5, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 0},
]
