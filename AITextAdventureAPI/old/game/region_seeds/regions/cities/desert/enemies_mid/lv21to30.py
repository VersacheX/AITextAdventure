# Level 21-30 hostile seeds for Nightveil Spire (mid city).

RANDOM_HOSTILE_SEEDS = [

 # min_spawn_level == 21
 {"id": "spire_enforcer", "name": "Spire Enforcer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 220,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (50, 180),
  "basic_attack": "spire baton", "strong_attack": "enforcer beatdown",
  "player_abilities": [],
  "base_str": 12, "base_dex": 8, "base_con": 10, "base_int": 4, "base_hp": 280, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 0},

 {"id": "obsidian_shade", "name": "Obsidian Shade", "hostile_type": "shadow", "role": "hazard", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 300,
  "common_drop": "herb_med", "rare_drop": None, "money_range": (20, 90),
  "basic_attack": "obsidian slash", "strong_attack": "void grasp",
  "player_abilities": ["level_1_hostile_ability_night_whisper"],
  "base_str": 6, "base_dex": 10, "base_con": 6, "base_int": 12, "base_hp": 300, "base_ap": 12,
  "str_per_level": 1, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 3},

 # min_spawn_level == 23
 {"id": "twilight_thug", "name": "Twilight Thug", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 23, "rarity": "common", "base_xp": 240,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (60, 220),
  "basic_attack": "twilight punch", "strong_attack": "night ambush",
  "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
  "base_str": 12, "base_dex": 14, "base_con": 10, "base_int": 4, "base_hp": 300, "base_ap": 10,
  "str_per_level": 2, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},

 # min_spawn_level == 26
 {"id": "arcane_street_witch", "name": "Arcane Street Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 26, "rarity": "uncommon", "base_xp": 360,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 300),
  "basic_attack": "arcane hex", "strong_attack": "spire curse",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_spirit_lv1_shade_whisper"],
  "base_str": 4, "base_dex": 8, "base_con": 6, "base_int": 16, "base_hp": 240, "base_ap": 14,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},

 # min_spawn_level == 28
 {"id": "spire_revenant", "name": "Spire Revenant", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 28, "rarity": "uncommon", "base_xp": 400,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (30, 120),
  "basic_attack": "necrotic claw", "strong_attack": "undead surge",
  "player_abilities": ["level_1_hostile_ability_bone_spear"],
  "base_str": 10, "base_dex": 6, "base_con": 8, "base_int": 10, "base_hp": 340, "base_ap": 10,
  "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 2},

 # min_spawn_level == 30
 {"id": "nightveil_boss", "name": "Nightveil Crime Boss", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 30, "rarity": "rare", "base_xp": 700,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (200, 800),
  "basic_attack": "boss slash", "strong_attack": "nightveil decree",
  "player_abilities": ["level_1_hostile_ability_inspire", "dark_skill_lv1_creeping_strike"],
  "base_str": 18, "base_dex": 12, "base_con": 16, "base_int": 8, "base_hp": 560, "base_ap": 12,
  "str_per_level": 4, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 1},
]