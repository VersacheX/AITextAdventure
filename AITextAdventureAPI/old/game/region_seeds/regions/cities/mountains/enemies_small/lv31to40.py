# Mountains Small City (Hollerforge Hollow) — hostile seeds levels 31–40.

RANDOM_HOSTILE_SEEDS = [
 {"id": "stone_construct_hollow", "name": "Stone Construct", "hostile_type": "construct", "role": "damage", "min_spawn_level": 38, "rarity": "uncommon", "base_xp": 700,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 30),
  "basic_attack": "stone fist", "strong_attack": "crush and grind",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 26, "base_dex": 2, "base_con": 24, "base_int": 4, "base_hp": 800, "base_ap": 6,
  "str_per_level": 5, "dex_per_level": 0, "con_per_level": 5, "int_per_level": 0},
 {"id": "hollow_sorcerer_sm", "name": "Hollow Sorcerer", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 33, "rarity": "uncommon", "base_xp": 480,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (90, 320),
  "basic_attack": "earth bolt", "strong_attack": "forge hex",
  "player_abilities": ["earth_magic_lv1_tremor"],
  "base_str": 3, "base_dex": 7, "base_con": 5, "base_int": 18, "base_hp": 280, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},
]
