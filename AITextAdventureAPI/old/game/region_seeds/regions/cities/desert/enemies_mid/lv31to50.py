# Desert Mid City — hostile seeds levels 31-50.

RANDOM_HOSTILE_SEEDS = [

 # min_spawn_level == 31
 {"id": "cartel_enforcer", "name": "Cartel Enforcer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 31, "rarity": "common", "base_xp": 300,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (80, 280),
  "basic_attack": "brass knuckle hit", "strong_attack": "enforcer beatdown",
  "player_abilities": [],
  "base_str": 14, "base_dex": 8, "base_con": 12, "base_int": 4, "base_hp": 280, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 1},

 {"id": "sand_revenant_mid", "name": "Sand Revenant", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 400,
  "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (30, 130),
  "basic_attack": "necrotic swipe", "strong_attack": "revenant wail",
  "player_abilities": ["level_1_hostile_ability_bone_spear"],
  "base_str": 12, "base_dex": 6, "base_con": 10, "base_int": 12, "base_hp": 380, "base_ap": 12,
  "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 3},

 # min_spawn_level == 33
 {"id": "district_boss", "name": "District Boss", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 33, "rarity": "uncommon", "base_xp": 480,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (140, 480),
  "basic_attack": "boss haymaker", "strong_attack": "turf stomp",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 18, "base_dex": 10, "base_con": 16, "base_int": 6, "base_hp": 440, "base_ap": 10,
  "str_per_level": 4, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 1},

 {"id": "hex_peddler", "name": "Hex Peddler", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 33, "rarity": "uncommon", "base_xp": 440,
  "common_drop": "tome_int", "rare_drop": None, "money_range": (100, 360),
  "basic_attack": "voodoo flick", "strong_attack": "curse barrage",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_spirit_lv1_shade_whisper"],
  "base_str": 4, "base_dex": 8, "base_con": 6, "base_int": 18, "base_hp": 280, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},

 # min_spawn_level == 35
 {"id": "turf_war_veteran", "name": "Turf War Veteran", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 35, "rarity": "common", "base_xp": 440,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (160, 520),
  "basic_attack": "veteran's strike", "strong_attack": "scarred fury",
  "player_abilities": [],
  "base_str": 20, "base_dex": 12, "base_con": 18, "base_int": 4, "base_hp": 500, "base_ap": 10,
  "str_per_level": 4, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 0},

 # min_spawn_level == 37
 {"id": "sand_warden_elite", "name": "Sand Warden Elite", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 37, "rarity": "uncommon", "base_xp": 520,
  "common_drop": "kevlar_vest", "rare_drop": None, "money_range": (180, 580),
  "basic_attack": "warden's lash", "strong_attack": "elite sentinel crush",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 22, "base_dex": 10, "base_con": 20, "base_int": 6, "base_hp": 560, "base_ap": 10,
  "str_per_level": 4, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 1},

 {"id": "void_thug", "name": "Void Thug", "hostile_type": "shadow", "role": "damage", "min_spawn_level": 37, "rarity": "common", "base_xp": 360,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (120, 400),
  "basic_attack": "shadow punch", "strong_attack": "void ambush",
  "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
  "base_str": 14, "base_dex": 18, "base_con": 12, "base_int": 8, "base_hp": 380, "base_ap": 14,
  "str_per_level": 2, "dex_per_level": 3, "con_per_level": 2, "int_per_level": 2},

 # min_spawn_level == 40
 {"id": "mid_city_crime_lord", "name": "Mid-City Crime Lord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 40, "rarity": "rare", "base_xp": 900,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (400, 1200),
  "basic_attack": "crime lord's blade", "strong_attack": "underworld decree",
  "player_abilities": ["level_1_hostile_ability_inspire", "dark_skill_lv1_creeping_strike"],
  "base_str": 28, "base_dex": 16, "base_con": 24, "base_int": 10, "base_hp": 720, "base_ap": 14,
  "str_per_level": 5, "dex_per_level": 2, "con_per_level": 4, "int_per_level": 2},

 # min_spawn_level == 42
 {"id": "spectral_mid_soldier", "name": "Spectral Mid Soldier", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 42, "rarity": "uncommon", "base_xp": 740,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (60, 220),
  "basic_attack": "spectral thrust", "strong_attack": "haunting barrage",
  "player_abilities": ["level_1_hostile_ability_night_whisper"],
  "base_str": 8, "base_dex": 16, "base_con": 10, "base_int": 22, "base_hp": 480, "base_ap": 20,
  "str_per_level": 1, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 5},

 # min_spawn_level == 45
 {"id": "enforcer_golem", "name": "Enforcer Golem", "hostile_type": "construct", "role": "damage", "min_spawn_level": 45, "rarity": "rare", "base_xp": 1200,
  "common_drop": None, "rare_drop": "kevlar_vest", "money_range": (0, 40),
  "basic_attack": "golem slam", "strong_attack": "enforcer protocol",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 34, "base_dex": 2, "base_con": 30, "base_int": 4, "base_hp": 1100, "base_ap": 6,
  "str_per_level": 7, "dex_per_level": 0, "con_per_level": 6, "int_per_level": 0},

 # min_spawn_level == 48
 {"id": "dune_shadow_lord", "name": "Dune Shadow Lord", "hostile_type": "shadow", "role": "hazard", "min_spawn_level": 48, "rarity": "superrare", "base_xp": 3000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (600, 2000),
  "basic_attack": "shadow edict", "strong_attack": "lord of darkness wave",
  "player_abilities": ["level_1_hostile_ability_night_whisper", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 14, "base_dex": 24, "base_con": 16, "base_int": 36, "base_hp": 1200, "base_ap": 32,
  "str_per_level": 2, "dex_per_level": 4, "con_per_level": 2, "int_per_level": 8},

 # min_spawn_level == 50
 {"id": "mid_city_apex_beast", "name": "Mid-City Apex Beast", "hostile_type": "creature", "role": "damage", "min_spawn_level": 50, "rarity": "superrare", "base_xp": 4000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (800, 2800),
  "basic_attack": "apex lunge", "strong_attack": "predator annihilation",
  "player_abilities": None,
  "base_str": 42, "base_dex": 16, "base_con": 38, "base_int": 6, "base_hp": 2600, "base_ap": 10,
  "str_per_level": 8, "dex_per_level": 2, "con_per_level": 7, "int_per_level": 1},
]
