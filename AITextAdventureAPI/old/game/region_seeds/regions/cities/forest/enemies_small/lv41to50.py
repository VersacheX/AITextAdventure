# Forest Small City (Thornshade Hamlet) — hostile seeds Lv 41–50.

RANDOM_HOSTILE_SEEDS = [
 {"id": "forest_bandit_lord", "name": "Forest Bandit Lord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 45, "rarity": "superrare", "base_xp": 2500,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (500, 1800),
  "basic_attack": "lord's slash", "strong_attack": "bandit decree",
  "player_abilities": ["level_1_hostile_ability_inspire", "dark_skill_lv1_creeping_strike"],
  "base_str": 34, "base_dex": 18, "base_con": 30, "base_int": 10, "base_hp": 1600, "base_ap": 14,
  "str_per_level": 7, "dex_per_level": 3, "con_per_level": 6, "int_per_level": 2},
 {"id": "hollow_beast_small", "name": "Hollow Beast", "hostile_type": "creature", "role": "damage", "min_spawn_level": 41, "rarity": "common", "base_xp": 820,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (100, 400),
  "basic_attack": "hollow maw", "strong_attack": "void lunge",
  "player_abilities": [],
  "base_str": 22, "base_dex": 20, "base_con": 20, "base_int": 5, "base_hp": 980, "base_ap": 9,
  "str_per_level": 4, "dex_per_level": 4, "con_per_level": 4, "int_per_level": 0},
 {"id": "corrupted_dryad_small", "name": "Corrupted Dryad", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 44, "rarity": "uncommon", "base_xp": 1100,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (150, 520),
  "basic_attack": "blight tendril", "strong_attack": "corruption bloom",
  "player_abilities": ["lv2_hostile_ability_earth_air_faith_thornbind"],
  "base_str": 14, "base_dex": 20, "base_con": 16, "base_int": 26, "base_hp": 1140, "base_ap": 12,
  "str_per_level": 2, "dex_per_level": 3, "con_per_level": 2, "int_per_level": 5},
]
