# Shallows Small City (Tidekin Cove) — hostile seeds levels 41–50.

RANDOM_HOSTILE_SEEDS = [
 {"id": "cove_bandit_lord", "name": "Cove Bandit Lord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 46, "rarity": "superrare", "base_xp": 2800,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (600, 2000),
  "basic_attack": "lord's blade", "strong_attack": "tidekin decree",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 36, "base_dex": 18, "base_con": 32, "base_int": 10, "base_hp": 2000, "base_ap": 12,
  "str_per_level": 7, "dex_per_level": 3, "con_per_level": 6, "int_per_level": 2},
 {"id": "cove_tide_horror", "name": "Cove Tide Horror", "hostile_type": "creature", "role": "damage", "min_spawn_level": 42, "rarity": "rare", "base_xp": 1100,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (200, 700),
  "basic_attack": "tide horror claw", "strong_attack": "cove surge",
  "player_abilities": ["water_magic_lv1_spray_shard"],
  "base_str": 32, "base_dex": 12, "base_con": 28, "base_int": 6, "base_hp": 1600, "base_ap": 10,
  "str_per_level": 6, "dex_per_level": 2, "con_per_level": 6, "int_per_level": 1},
]
