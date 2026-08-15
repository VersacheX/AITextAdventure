# Forest Overworld — hostile seeds levels 31-100.

SEEDS_LV31TO100 = [

 # min_spawn_level == 31
 {"id": "dire_bear", "name": "Dire Bear", "hostile_type": "creature", "role": "damage", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 520,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (10, 50),
  "basic_attack": "dire claw", "strong_attack": "bear rampage",
  "player_abilities": None,
  "base_str": 22, "base_dex": 6, "base_con": 20, "base_int": 2, "base_hp": 640, "base_ap": 6,
  "str_per_level": 5, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 0},

 {"id": "nightmare_dryad", "name": "Nightmare Dryad", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 500,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (40, 160),
  "basic_attack": "nightmare touch", "strong_attack": "dream entangle",
  "player_abilities": ["level_1_hostile_ability_earth_magic_sap_bloom", "air_dark_magic_lv2_night_wind"],
  "base_str": 6, "base_dex": 14, "base_con": 8, "base_int": 22, "base_hp": 360, "base_ap": 20,
  "str_per_level": 1, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 5},

 # min_spawn_level == 35
 {"id": "elder_treant_lord", "name": "Elder Treant Lord", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 35, "rarity": "rare", "base_xp": 1000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (30, 120),
  "basic_attack": "lord's branch", "strong_attack": "forest earthquake",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field"],
  "base_str": 28, "base_dex": 2, "base_con": 26, "base_int": 10, "base_hp": 1200, "base_ap": 12,
  "str_per_level": 6, "dex_per_level": 0, "con_per_level": 5, "int_per_level": 2},

 # min_spawn_level == 40
 {"id": "forest_dragon", "name": "Forest Dragon", "hostile_type": "creature", "role": "damage", "min_spawn_level": 40, "rarity": "superrare", "base_xp": 2800,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (400, 1400),
  "basic_attack": "claw sweep", "strong_attack": "acid breath",
  "player_abilities": ["water_magic_lv1_spray_shard", "earth_water_magic_lv2_mudslide"],
  "base_str": 34, "base_dex": 12, "base_con": 30, "base_int": 10, "base_hp": 1600, "base_ap": 12,
  "str_per_level": 7, "dex_per_level": 2, "con_per_level": 6, "int_per_level": 2},

 # min_spawn_level == 50
 {"id": "forest_leviathan", "name": "Forest Leviathan", "hostile_type": "creature", "role": "damage", "min_spawn_level": 50, "rarity": "superrare", "base_xp": 6000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1200, 4000),
  "basic_attack": "forest coil", "strong_attack": "canopy crush",
  "player_abilities": None,
  "base_str": 52, "base_dex": 8, "base_con": 48, "base_int": 6, "base_hp": 4800, "base_ap": 10,
  "str_per_level": 10, "dex_per_level": 1, "con_per_level": 9, "int_per_level": 0},

 # min_spawn_level == 60
 {"id": "void_forest_horror", "name": "Void Forest Horror", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 60, "rarity": "superrare", "base_xp": 10000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (2000, 7000),
  "basic_attack": "eldritch vine", "strong_attack": "forest of nightmares",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_air_earth_magic_lv3_shadow_quake"],
  "base_str": 18, "base_dex": 22, "base_con": 20, "base_int": 50, "base_hp": 5500, "base_ap": 44,
  "str_per_level": 3, "dex_per_level": 4, "con_per_level": 3, "int_per_level": 11},

 # min_spawn_level == 80
 {"id": "elder_forest_god", "name": "Elder Forest God", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 80, "rarity": "superrare", "base_xp": 28000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (8000, 27000),
  "basic_attack": "nature's decree", "strong_attack": "world tree collapse",
  "player_abilities": ["earth_earth_earth_magic_lv3_earthshaker", "water_water_water_magic_lv3_tsunami_burst"],
  "base_str": 44, "base_dex": 20, "base_con": 42, "base_int": 90, "base_hp": 32000, "base_ap": 74,
  "str_per_level": 8, "dex_per_level": 4, "con_per_level": 8, "int_per_level": 18},

 # min_spawn_level == 100
 {"id": "world_tree_spirit", "name": "World Tree Spirit", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 120000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (50000, 160000),
  "basic_attack": "world root strike", "strong_attack": "end of the canopy age",
  "player_abilities": ["earth_earth_earth_magic_lv3_earthshaker"],
  "base_str": 120, "base_dex": 26, "base_con": 114, "base_int": 36, "base_hp": 100000, "base_ap": 28,
  "str_per_level": 24, "dex_per_level": 5, "con_per_level": 22, "int_per_level": 7},

 # min_spawn_level == 61 (fills Lv61-70 gap)
 {"id": "forest_elder_dire_wolf", "name": "Elder Dire Wolf", "hostile_type": "creature", "role": "damage", "min_spawn_level": 61, "rarity": "superrare", "base_xp": 10000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (2000, 7000),
  "basic_attack": "dire maw", "strong_attack": "pack alpha howl",
  "player_abilities": None,
  "base_str": 64, "base_dex": 22, "base_con": 60, "base_int": 8, "base_hp": 9000, "base_ap": 12,
  "str_per_level": 13, "dex_per_level": 4, "con_per_level": 12, "int_per_level": 1},

 {"id": "forest_ancient_treant", "name": "Ancient Treant", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 65, "rarity": "superrare", "base_xp": 13000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (3000, 10000),
  "basic_attack": "branch slam", "strong_attack": "rootquake",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field"],
  "base_str": 70, "base_dex": 6, "base_con": 68, "base_int": 12, "base_hp": 12000, "base_ap": 14,
  "str_per_level": 14, "dex_per_level": 1, "con_per_level": 13, "int_per_level": 2},

 # min_spawn_level == 81 (fills Lv81-90 gap)
 {"id": "forest_shadow_colossus", "name": "Shadow Colossus", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 81, "rarity": "superrare", "base_xp": 32000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (10000, 34000),
  "basic_attack": "shadow fist", "strong_attack": "void eruption",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 20, "base_dex": 20, "base_con": 20, "base_int": 110, "base_hp": 28000, "base_ap": 90,
  "str_per_level": 4, "dex_per_level": 4, "con_per_level": 4, "int_per_level": 22},

 {"id": "forest_nature_titan", "name": "Nature Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 86, "rarity": "superrare", "base_xp": 40000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (14000, 46000),
  "basic_attack": "nature titan slam", "strong_attack": "forest world shatter",
  "player_abilities": ["earth_earth_earth_magic_lv3_earthshaker"],
  "base_str": 116, "base_dex": 20, "base_con": 110, "base_int": 20, "base_hp": 44000, "base_ap": 18,
  "str_per_level": 23, "dex_per_level": 4, "con_per_level": 22, "int_per_level": 4},
]
