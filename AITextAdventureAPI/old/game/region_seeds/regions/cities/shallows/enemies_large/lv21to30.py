# Shallows Large City (Brineward Harbor) — hostile seeds levels 21–30.

RANDOM_HOSTILE_SEEDS = [
 {"id": "harbor_thug", "name": "Harbor Thug", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 240,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (50, 180),
  "basic_attack": "dock punch", "strong_attack": "harbor ambush",
  "player_abilities": [], "base_str": 12, "base_dex": 10, "base_con": 10, "base_int": 3, "base_hp": 300, "base_ap": 10,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 0},
 {"id": "brine_shade", "name": "Brine Shade", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 22, "rarity": "uncommon", "base_xp": 320,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "brine touch", "strong_attack": "harbor wail",
  "player_abilities": ["level_1_hostile_ability_streamlet"],
  "base_str": 4, "base_dex": 14, "base_con": 6, "base_int": 14, "base_hp": 260, "base_ap": 14,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 3},
 {"id": "brineward_pirate", "name": "Brineward Pirate", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 26, "rarity": "common", "base_xp": 320,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (100, 340),
  "basic_attack": "cutlass slash", "strong_attack": "pirate's raid",
  "player_abilities": [], "base_str": 14, "base_dex": 14, "base_con": 12, "base_int": 4, "base_hp": 360, "base_ap": 12,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},
]
