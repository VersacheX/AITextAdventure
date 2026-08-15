# Swamp Large City (The Necropolis) — hostile seeds levels 21–30.

RANDOM_HOSTILE_SEEDS = [
 {"id": "necropolis_cultist", "name": "Necropolis Cultist", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level": 21, "rarity": "common", "base_xp": 260,
  "common_drop": "tome_int", "rare_drop": None, "money_range": (50, 180),
  "basic_attack": "ritual blade", "strong_attack": "death rite",
  "player_abilities": ["dark_faith_lv1_shade_whisper"],
  "base_str": 8, "base_dex": 8, "base_con": 8, "base_int": 14, "base_hp": 280, "base_ap": 14,
  "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 3},
 {"id": "swamp_revenant_lg", "name": "Swamp Revenant", "hostile_type": "undead", "role": "damage", "min_spawn_level": 22, "rarity": "common", "base_xp": 260,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "necrotic claw", "strong_attack": "bog surge",
  "player_abilities": [],
  "base_str": 14, "base_dex": 6, "base_con": 12, "base_int": 4, "base_hp": 340, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 0, "con_per_level": 2, "int_per_level": 0},
 {"id": "necro_witch_lg", "name": "Necro Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 27, "rarity": "uncommon", "base_xp": 440,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (90, 320),
  "basic_attack": "dark hex", "strong_attack": "necropolis curse",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_faith_lv1_shade_whisper"],
  "base_str": 4, "base_dex": 8, "base_con": 6, "base_int": 20, "base_hp": 300, "base_ap": 18,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},
]
