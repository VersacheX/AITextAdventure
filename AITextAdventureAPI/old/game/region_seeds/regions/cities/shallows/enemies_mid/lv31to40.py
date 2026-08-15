# Shallows Mid City (Blackwake Bay) — hostile seeds levels 31–40.

RANDOM_HOSTILE_SEEDS = [
 {"id": "blackwake_lord", "name": "Blackwake Pirate Lord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 36, "rarity": "rare", "base_xp": 760,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (280, 900),
  "basic_attack": "captain's blade", "strong_attack": "pirate lord decree",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 24, "base_dex": 14, "base_con": 22, "base_int": 8, "base_hp": 700, "base_ap": 12,
  "str_per_level": 4, "dex_per_level": 2, "con_per_level": 4, "int_per_level": 1},
 {"id": "bay_tide_sorcerer", "name": "Bay Tide Sorcerer", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 33, "rarity": "uncommon", "base_xp": 480,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (100, 340),
  "basic_attack": "tide bolt", "strong_attack": "bay hex",
  "player_abilities": ["water_magic_lv1_spray_shard"],
  "base_str": 3, "base_dex": 12, "base_con": 5, "base_int": 20, "base_hp": 280, "base_ap": 18,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 4},
]
