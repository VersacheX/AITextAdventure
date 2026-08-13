# Desert Overworld — hostile seeds levels 31-100 (elite through apex open-world threats).

SEEDS_LV31TO100 = [

 # min_spawn_level == 31
 {"id": "sand_herald", "name": "Sand Herald", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 460,
  "common_drop": "tome_int", "rare_drop": None, "money_range": (100, 360),
  "basic_attack": "herald declaration", "strong_attack": "war decree",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 14, "base_dex": 10, "base_con": 12, "base_int": 10, "base_hp": 400, "base_ap": 12,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 2},

 {"id": "rock_gargant", "name": "Rock Gargant", "hostile_type": "creature", "role": "damage", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 520,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (5, 40),
  "basic_attack": "boulder bash", "strong_attack": "rock avalanche",
  "player_abilities": None,
  "base_str": 22, "base_dex": 2, "base_con": 20, "base_int": 2, "base_hp": 600, "base_ap": 4,
  "str_per_level": 5, "dex_per_level": 0, "con_per_level": 4, "int_per_level": 0},

 # min_spawn_level == 35
 {"id": "tomb_keeper", "name": "Tomb Keeper", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 35, "rarity": "rare", "base_xp": 800,
  "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (80, 280),
  "basic_attack": "cursed touch", "strong_attack": "tomb sealing curse",
  "player_abilities": ["level_1_hostile_ability_bone_spear", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 12, "base_dex": 8, "base_con": 12, "base_int": 22, "base_hp": 580, "base_ap": 20,
  "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 5},

 # min_spawn_level == 38
 {"id": "sand_dragon_juvenile", "name": "Sand Dragon (Juvenile)", "hostile_type": "creature", "role": "damage", "min_spawn_level": 38, "rarity": "superrare", "base_xp": 2000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (300, 1000),
  "basic_attack": "claw swipe", "strong_attack": "fire breath",
  "player_abilities": ["fire_magic_lv1_fireball", "fire_fire_magic_lv2_inferno_spread"],
  "base_str": 28, "base_dex": 10, "base_con": 26, "base_int": 8, "base_hp": 1100, "base_ap": 10,
  "str_per_level": 6, "dex_per_level": 1, "con_per_level": 5, "int_per_level": 1},

 # min_spawn_level == 42
 {"id": "desert_archmage_elder", "name": "Desert Archmage Elder", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 42, "rarity": "superrare", "base_xp": 3500,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (500, 1800),
  "basic_attack": "elder arcane lance", "strong_attack": "grand meteor volley",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field", "earth_earth_earth_magic_lv3_earthshaker"],
  "base_str": 10, "base_dex": 10, "base_con": 12, "base_int": 36, "base_hp": 800, "base_ap": 32,
  "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 8},

 # min_spawn_level == 50
 {"id": "sand_leviathan", "name": "Sand Leviathan", "hostile_type": "creature", "role": "damage", "min_spawn_level": 50, "rarity": "superrare", "base_xp": 6000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1000, 3500),
  "basic_attack": "leviathan coil", "strong_attack": "sand burial",
  "player_abilities": None,
  "base_str": 50, "base_dex": 8, "base_con": 46, "base_int": 6, "base_hp": 4500, "base_ap": 10,
  "str_per_level": 10, "dex_per_level": 1, "con_per_level": 9, "int_per_level": 0},

 # min_spawn_level == 60
 {"id": "void_desert_beast", "name": "Void Desert Beast", "hostile_type": "eldritch", "role": "damage", "min_spawn_level": 60, "rarity": "superrare", "base_xp": 10000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (2000, 7000),
  "basic_attack": "void claw", "strong_attack": "desert void eruption",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm"],
  "base_str": 62, "base_dex": 12, "base_con": 58, "base_int": 16, "base_hp": 8000, "base_ap": 14,
  "str_per_level": 12, "dex_per_level": 2, "con_per_level": 11, "int_per_level": 3},

 {"id": "phantom_dune_rider", "name": "Phantom Dune Rider", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 63, "rarity": "rare", "base_xp": 7000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (1500, 5000),
  "basic_attack": "phantom strike", "strong_attack": "rider's curse",
  "player_abilities": ["level_1_hostile_ability_night_whisper", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 14, "base_dex": 22, "base_con": 16, "base_int": 52, "base_hp": 4000, "base_ap": 44,
  "str_per_level": 2, "dex_per_level": 4, "con_per_level": 2, "int_per_level": 11},

 # min_spawn_level == 75
 {"id": "elder_sand_dragon", "name": "Elder Sand Dragon", "hostile_type": "creature", "role": "damage", "min_spawn_level": 75, "rarity": "superrare", "base_xp": 22000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (6000, 20000),
  "basic_attack": "elder claw", "strong_attack": "cataclysmic inferno breath",
  "player_abilities": ["fire_magic_lv1_fireball", "fire_fire_magic_lv2_inferno_spread", "fire_fire_fire_magic_lv3_inferno_wave"],
  "base_str": 90, "base_dex": 18, "base_con": 84, "base_int": 16, "base_hp": 24000, "base_ap": 18,
  "str_per_level": 18, "dex_per_level": 3, "con_per_level": 17, "int_per_level": 3},

 {"id": "dune_god_herald", "name": "Dune God Herald", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 82, "rarity": "superrare", "base_xp": 28000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (9000, 30000),
  "basic_attack": "divine herald gale", "strong_attack": "god's prelude",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field"],
  "base_str": 50, "base_dex": 22, "base_con": 48, "base_int": 90, "base_hp": 20000, "base_ap": 74,
  "str_per_level": 10, "dex_per_level": 4, "con_per_level": 9, "int_per_level": 18},

 # min_spawn_level == 100
 {"id": "desert_world_god", "name": "Desert World God", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 120000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (50000, 150000),
  "basic_attack": "world decree", "strong_attack": "desert world ending",
  "player_abilities": ["earth_earth_earth_magic_lv3_earthshaker", "fire_fire_fire_magic_lv3_inferno_wave"],
  "base_str": 150, "base_dex": 24, "base_con": 142, "base_int": 28, "base_hp": 100000, "base_ap": 22,
  "str_per_level": 30, "dex_per_level": 5, "con_per_level": 28, "int_per_level": 5},
]
