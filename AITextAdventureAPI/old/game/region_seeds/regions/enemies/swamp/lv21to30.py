# LEVEL 21-30 hostile regional (swamp overworld).

SEEDS_LV21TO30 = [

 # min_spawn_level == 21
 {"id": "bog_marauder", "name": "Bog Marauder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 220,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (50, 180),
  "basic_attack": "bog cleave", "strong_attack": "swamp ambush",
  "player_abilities": [],
  "base_str": 12, "base_dex": 10, "base_con": 10, "base_int": 3, "base_hp": 300, "base_ap": 10,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 0},

 {"id": "swamp_shade", "name": "Swamp Shade", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 320,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "bog touch", "strong_attack": "mire wail",
  "player_abilities": ["level_1_hostile_ability_poison_dart"],
  "base_str": 4, "base_dex": 12, "base_con": 6, "base_int": 14, "base_hp": 270, "base_ap": 14,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 3},

 # min_spawn_level == 24
 {"id": "elder_bog_hunter", "name": "Elder Bog Hunter", "hostile_type": "creature", "role": "damage", "min_spawn_level": 24, "rarity": "uncommon", "base_xp": 380,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (10, 60),
  "basic_attack": "bog lunge", "strong_attack": "elder maul",
  "player_abilities": None,
  "base_str": 18, "base_dex": 12, "base_con": 16, "base_int": 2, "base_hp": 480, "base_ap": 10,
  "str_per_level": 4, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 0},

 # min_spawn_level == 27
 {"id": "swamp_witch", "name": "Swamp Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 27, "rarity": "uncommon", "base_xp": 420,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 280),
  "basic_attack": "blight hex", "strong_attack": "swamp curse",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "water_dark_magic_lv2_abyssal_tide"],
  "base_str": 4, "base_dex": 8, "base_con": 6, "base_int": 18, "base_hp": 260, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},

 # min_spawn_level == 30
 {"id": "elder_mire_brute", "name": "Elder Mire Brute", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 30, "rarity": "superrare", "base_xp": 1400,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (100, 400),
  "basic_attack": "mire crusher", "strong_attack": "rot stomp",
  "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
  "base_str": 26, "base_dex": 4, "base_con": 24, "base_int": 4, "base_hp": 900, "base_ap": 8,
  "str_per_level": 5, "dex_per_level": 0, "con_per_level": 5, "int_per_level": 0},
]