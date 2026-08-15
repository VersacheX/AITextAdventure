# Swamp Small City (Gnashwater Hollow) — hostile seeds levels 31–40.

RANDOM_HOSTILE_SEEDS = [
 {"id": "gnash_witch", "name": "Gnash Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 36, "rarity": "uncommon", "base_xp": 460,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 280),
  "basic_attack": "bog hex", "strong_attack": "gnashwater curse",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_faith_lv1_shade_whisper"],
  "base_str": 3, "base_dex": 8, "base_con": 5, "base_int": 18, "base_hp": 260, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},
 {"id": "gnash_enforcer", "name": "Gnash Enforcer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 32, "rarity": "uncommon", "base_xp": 380,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (80, 280),
  "basic_attack": "gnash iron bar", "strong_attack": "hollow beatdown",
  "player_abilities": [],
  "base_str": 18, "base_dex": 8, "base_con": 16, "base_int": 2, "base_hp": 480, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},
]
