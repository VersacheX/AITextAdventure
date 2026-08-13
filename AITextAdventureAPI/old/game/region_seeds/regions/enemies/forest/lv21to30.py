# LEVEL 21-30 hostile regional (forest overworld).

SEEDS_LV21TO30 = [

 # min_spawn_level == 21
 {"id": "elder_wolf", "name": "Elder Wolf", "hostile_type": "creature", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 240,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (5, 30),
  "basic_attack": "alpha bite", "strong_attack": "pack howl lunge",
  "player_abilities": [],
  "base_str": 14, "base_dex": 14, "base_con": 12, "base_int": 4, "base_hp": 340, "base_ap": 12,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},

 {"id": "forest_shade", "name": "Forest Shade", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 340,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "shade touch", "strong_attack": "forest whisper curse",
  "player_abilities": ["level_1_hostile_ability_night_whisper"],
  "base_str": 4, "base_dex": 12, "base_con": 6, "base_int": 14, "base_hp": 280, "base_ap": 14,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 3},

 # min_spawn_level == 23
 {"id": "thorn_golem", "name": "Thorn Golem", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 23, "rarity": "uncommon", "base_xp": 380,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 20),
  "basic_attack": "thorn slam", "strong_attack": "briar entrapment",
  "player_abilities": ["earth_magic_lv1_tremor"],
  "base_str": 16, "base_dex": 4, "base_con": 14, "base_int": 6, "base_hp": 420, "base_ap": 8,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 3, "int_per_level": 1},

 # min_spawn_level == 25
 {"id": "wood_witch", "name": "Wood Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 25, "rarity": "uncommon", "base_xp": 420,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 300),
  "basic_attack": "hex volley", "strong_attack": "cursed root snare",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_water_magic_lv2_mudslide"],
  "base_str": 4, "base_dex": 8, "base_con": 6, "base_int": 18, "base_hp": 280, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},

 # min_spawn_level == 27
 {"id": "forest_troll", "name": "Forest Troll", "hostile_type": "creature", "role": "damage", "min_spawn_level": 27, "rarity": "common", "base_xp": 400,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (10, 60),
  "basic_attack": "club smash", "strong_attack": "troll regeneration slam",
  "player_abilities": None,
  "base_str": 20, "base_dex": 4, "base_con": 18, "base_int": 2, "base_hp": 560, "base_ap": 6,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 4, "int_per_level": 0},

 # min_spawn_level == 30
 {"id": "ancient_treant", "name": "Ancient Treant", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 30, "rarity": "superrare", "base_xp": 1600,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (50, 200),
  "basic_attack": "branch whip", "strong_attack": "ancient root crush",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field"],
  "base_str": 26, "base_dex": 2, "base_con": 24, "base_int": 8, "base_hp": 1000, "base_ap": 10,
  "str_per_level": 5, "dex_per_level": 0, "con_per_level": 5, "int_per_level": 1},
]