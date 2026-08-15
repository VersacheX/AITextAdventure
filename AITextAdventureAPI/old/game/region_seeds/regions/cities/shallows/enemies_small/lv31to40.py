# Shallows Small City (Tidekin Cove) — hostile seeds levels 31–40.

RANDOM_HOSTILE_SEEDS = [
 {"id": "cove_sea_witch", "name": "Cove Sea Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 36, "rarity": "uncommon", "base_xp": 500,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 300),
  "basic_attack": "cove hex", "strong_attack": "tidal curse",
  "player_abilities": ["water_magic_lv1_spray_shard", "ice_water_magic_lv2_glacier_spike"],
  "base_str": 3, "base_dex": 10, "base_con": 5, "base_int": 20, "base_hp": 280, "base_ap": 18,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},
 {"id": "cove_buccaneer_lord", "name": "Cove Buccaneer Lord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 33, "rarity": "rare", "base_xp": 640,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (200, 680),
  "basic_attack": "cove cutlass", "strong_attack": "tidekin decree",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 22, "base_dex": 14, "base_con": 20, "base_int": 6, "base_hp": 600, "base_ap": 12,
  "str_per_level": 4, "dex_per_level": 2, "con_per_level": 4, "int_per_level": 1},
]
