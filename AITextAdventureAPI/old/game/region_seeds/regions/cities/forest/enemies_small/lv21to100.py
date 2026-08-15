# Forest Small City — hostile seeds levels 21-100.

RANDOM_HOSTILE_SEEDS = [

 # min_spawn_level == 21
 {"id": "root_thief", "name": "Root Thief", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 220,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (40, 160),
  "basic_attack": "root shiv", "strong_attack": "bramble ambush",
  "player_abilities": [],
  "base_str": 10, "base_dex": 12, "base_con": 8, "base_int": 3, "base_hp": 260, "base_ap": 10,
  "str_per_level": 2, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},

 # min_spawn_level == 24
 {"id": "thorn_wraith", "name": "Thorn Wraith", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 24, "rarity": "uncommon", "base_xp": 320,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "thorn touch", "strong_attack": "briar wail",
  "player_abilities": ["level_1_hostile_ability_night_whisper"],
  "base_str": 4, "base_dex": 10, "base_con": 6, "base_int": 12, "base_hp": 240, "base_ap": 12,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 3},

 # min_spawn_level == 28
 {"id": "forest_berserker", "name": "Forest Berserker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 28, "rarity": "common", "base_xp": 340,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (80, 280),
  "basic_attack": "berserk slash", "strong_attack": "forest fury",
  "player_abilities": [],
  "base_str": 16, "base_dex": 8, "base_con": 14, "base_int": 2, "base_hp": 380, "base_ap": 8,
  "str_per_level": 4, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},

 # min_spawn_level == 35
 {"id": "moss_golem", "name": "Moss Golem", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 35, "rarity": "uncommon", "base_xp": 500,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 30),
  "basic_attack": "moss slam", "strong_attack": "spore burst",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 20, "base_dex": 2, "base_con": 18, "base_int": 4, "base_hp": 560, "base_ap": 6,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 4, "int_per_level": 0},

 # min_spawn_level == 45
 {"id": "forest_bandit_lord", "name": "Forest Bandit Lord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 45, "rarity": "superrare", "base_xp": 2500,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (500, 1800),
  "basic_attack": "lord's slash", "strong_attack": "bandit decree",
  "player_abilities": ["level_1_hostile_ability_inspire", "dark_skill_lv1_creeping_strike"],
  "base_str": 34, "base_dex": 18, "base_con": 30, "base_int": 10, "base_hp": 1600, "base_ap": 14,
  "str_per_level": 7, "dex_per_level": 3, "con_per_level": 6, "int_per_level": 2},

 # min_spawn_level == 51
 {"id": "blight_runner_small", "name": "Blight Runner", "hostile_type": "creature", "role": "damage", "min_spawn_level": 51, "rarity": "common", "base_xp": 1300,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (280, 850),
  "basic_attack": "infected lunge", "strong_attack": "blight sprint",
  "player_abilities": ["lv2_hostile_ability_dark_ice_skill_void_spike"],
  "base_str": 28, "base_dex": 30, "base_con": 24, "base_int": 8, "base_hp": 1300, "base_ap": 11,
  "str_per_level": 5, "dex_per_level": 5, "con_per_level": 4, "int_per_level": 1},

 {"id": "shade_ravager_small", "name": "Shade Ravager", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 56, "rarity": "uncommon", "base_xp": 1800,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (180, 640),
  "basic_attack": "shadow gouge", "strong_attack": "darkwood dirge",
  "player_abilities": ["lv2_hostile_ability_dark_air_skill_nightmare_wave"],
  "base_str": 12, "base_dex": 30, "base_con": 16, "base_int": 28, "base_hp": 1440, "base_ap": 13,
  "str_per_level": 2, "dex_per_level": 5, "con_per_level": 2, "int_per_level": 4},

 # min_spawn_level == 71
 {"id": "grovekeeper_revenant", "name": "Grovekeeper Revenant", "hostile_type": "undead", "role": "support", "min_spawn_level": 71, "rarity": "rare", "base_xp": 8500,
  "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (2000, 7000),
  "basic_attack": "revenant grasp", "strong_attack": "grove restoration curse",
  "player_abilities": ["seizing_the_moment", "predator_rush"],
  "base_str": 20, "base_dex": 50, "base_con": 28, "base_int": 58, "base_hp": 5600, "base_ap": 18,
  "str_per_level": 3, "dex_per_level": 7, "con_per_level": 4, "int_per_level": 8},

 {"id": "arcane_warden_small", "name": "Arcane Warden", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level": 76, "rarity": "uncommon", "base_xp": 10000,
  "common_drop": "tome_int", "rare_drop": None, "money_range": (2500, 8000),
  "basic_attack": "runic lash", "strong_attack": "ward burst",
  "player_abilities": ["wild_possibility"],
  "base_str": 16, "base_dex": 44, "base_con": 20, "base_int": 62, "base_hp": 4800, "base_ap": 18,
  "str_per_level": 2, "dex_per_level": 6, "con_per_level": 3, "int_per_level": 9},

 # min_spawn_level == 81
 {"id": "void_forest_stalker", "name": "Void Forest Stalker", "hostile_type": "eldritch", "role": "damage", "min_spawn_level": 81, "rarity": "rare", "base_xp": 13000,
  "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (4000, 13000),
  "basic_attack": "void tendril strike", "strong_attack": "forest annihilation",
  "player_abilities": ["rot_of_potential", "detached_slaughter"],
  "base_str": 78, "base_dex": 54, "base_con": 72, "base_int": 36, "base_hp": 6500, "base_ap": 20,
  "str_per_level": 9, "dex_per_level": 7, "con_per_level": 9, "int_per_level": 5},

 # min_spawn_level == 70
 {"id": "elder_vine_titan", "name": "Elder Vine Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 70, "rarity": "superrare", "base_xp": 14000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (4000, 14000),
  "basic_attack": "vine titan crush", "strong_attack": "canopy annihilation",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field"],
  "base_str": 80, "base_dex": 10, "base_con": 76, "base_int": 12, "base_hp": 18000, "base_ap": 14,
  "str_per_level": 16, "dex_per_level": 1, "con_per_level": 15, "int_per_level": 2},

 # min_spawn_level == 100
 {"id": "small_forest_god", "name": "The Small Forest God", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 90000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (30000, 100000),
  "basic_attack": "root mandate", "strong_attack": "forest apocalypse",
  "player_abilities": ["earth_earth_earth_magic_lv3_earthshaker"],
  "base_str": 24, "base_dex": 28, "base_con": 26, "base_int": 130, "base_hp": 70000, "base_ap": 110,
  "str_per_level": 5, "dex_per_level": 5, "con_per_level": 5, "int_per_level": 26},
]
