# Swamp Mid City (Bayou Nocturne) — hostile seeds levels 21–30.

RANDOM_HOSTILE_SEEDS = [
 {"id": "bayou_thug", "name": "Bayou Thug", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 230,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (50, 180),
  "basic_attack": "swamp knife", "strong_attack": "bayou ambush",
  "player_abilities": [], "base_str": 12, "base_dex": 10, "base_con": 10, "base_int": 3, "base_hp": 280, "base_ap": 10,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 0},
 {"id": "bayou_shade", "name": "Bayou Shade", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 22, "rarity": "uncommon", "base_xp": 300,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (15, 60),
  "basic_attack": "bog touch", "strong_attack": "bayou wail",
  "player_abilities": ["dark_spirit_lv1_shade_whisper"],
  "base_str": 4, "base_dex": 10, "base_con": 6, "base_int": 12, "base_hp": 240, "base_ap": 12,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 3},
 {"id": "bayou_witch_mid", "name": "Bayou Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 27, "rarity": "uncommon", "base_xp": 400,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 280),
  "basic_attack": "voodoo hex", "strong_attack": "bayou curse",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_spirit_lv1_shade_whisper"],
  "base_str": 4, "base_dex": 8, "base_con": 6, "base_int": 18, "base_hp": 260, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},
]
