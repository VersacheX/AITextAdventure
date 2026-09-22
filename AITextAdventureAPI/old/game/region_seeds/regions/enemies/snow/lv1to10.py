# LEVEL1-10 hostile regional (to be imported by higher-level modules).

SEEDS_LV1TO10 = [
 {"id": "neon_drifter", "name": "Neon Drifter", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":12, "common_drop": "herb_minor", "money_range": (1,6),
 "basic_attack": "glancing jab", "strong_attack": "smashing blow", "player_abilities": [], "base_str":2, "base_dex":3, "base_con":2, "base_int":2, "base_hp":12, "base_ap":2, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "frost_rat", "name": "Frost Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":18, "common_drop": "herb_minor", "money_range": (0,4),
 "basic_attack": "tooth bite", "strong_attack": "bone crush", "player_abilities": [], "base_str":1, "base_dex":4, "base_con":1, "base_int":1, "base_hp":12, "base_ap":2, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "tundra_hound", "name": "Tundra Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "rare", "base_xp":30, "common_drop": "herb_minor", "money_range": (1,8),
 "basic_attack": "ripping maw", "strong_attack": "feral pounce", "player_abilities": [], "base_str":6, "base_dex":6, "base_con":4, "base_int":1, "base_hp":28, "base_ap":4, "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "cinder_pigeon", "name": "Cinder Pigeon", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6, "common_drop": "herb_minor", "money_range": (0,3),
 "basic_attack": "peck", "strong_attack": "flurry wing", "player_abilities": [], "base_str":1, "base_dex":5, "base_con":1, "base_int":1, "base_hp":6, "base_ap":1, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 # Level2
 {"id": "frozen_hobo", "name": "Frozen Hobo", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":18, "common_drop": "stimulant_small", "money_range": (1,10),
 "basic_attack": "dirty swipe", "strong_attack": "drunken slam", "player_abilities": [], "base_str":2, "base_dex":2, "base_con":3, "base_int":1, "base_hp":22, "base_ap":3, "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "ice_vendor", "name": "Ice Vendor", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":16, "common_drop": "herb_minor", "money_range": (2,12),
 "basic_attack": "tray toss", "strong_attack": "frozen crate", "player_abilities": [], "base_str":2, "base_dex":3, "base_con":2, "base_int":2, "base_hp":16, "base_ap":3, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "neon_sentry", "name": "Neon Sentry", "hostile_type": "construct", "role": "damage", "min_spawn_level":2, "rarity": "uncommon", "base_xp":28, "common_drop": "stimulant_small", "money_range": (4,20),
 "basic_attack": "metal swipe", "strong_attack": "spark burst", "player_abilities": ["fire_air_tech_lv2_aero_flare"], "base_str":4, "base_dex":2, "base_con":4, "base_int":1, "base_hp":28, "base_ap":4, "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "glass_fox", "name": "Glass Fox", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":20, "common_drop": "herb_minor", "money_range": (2,14),
 "basic_attack": "cunning bite", "strong_attack": "shard slash", "player_abilities": [], "base_str":3, "base_dex":5, "base_con":2, "base_int":2, "base_hp":22, "base_ap":3, "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # Level3
 {"id": "frost_patchman", "name": "Frost Patchman", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":30, "common_drop": "herb_med", "money_range": (6,28),
 "basic_attack": "striking fist", "strong_attack": "smashing blow", "player_abilities": [], "base_str":4, "base_dex":3, "base_con":4, "base_int":2, "base_hp":36, "base_ap":4, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "neon_riveter", "name": "Neon Riveter", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":42, "common_drop": "stimulant_small", "money_range": (8,36),
 "basic_attack": "riveting jab", "strong_attack": "steel uppercut", "player_abilities": [], "base_str":5, "base_dex":3, "base_con":5, "base_int":2, "base_hp":40, "base_ap":5, "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "frozen_vendor_drone", "name": "Frozen Vendor Drone", "hostile_type": "construct", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":46, "common_drop": "stimulant_med", "money_range": (10,44),
 "basic_attack": "servo jab", "strong_attack": "cold discharge", "player_abilities": ["lv2_hostile_ability_fire_water_tech_steam_grenade"], "base_str":4, "base_dex":3, "base_con":4, "base_int":3, "base_hp":44, "base_ap":5, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 {"id": "glow_moth", "name": "Glow Moth", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":22, "common_drop": "herb_minor", "money_range": (2,12),
 "basic_attack": "flit hit", "strong_attack": "luminous gust", "player_abilities": [], "base_str":1, "base_dex":6, "base_con":1, "base_int":3, "base_hp":18, "base_ap":3, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # Level4
 {"id": "ice_rigger", "name": "Ice Rigger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":70, "common_drop": "herb_med", "money_range": (14,60),
 "basic_attack": "hook swipe", "strong_attack": "deck cleave", "player_abilities": [], "base_str":6, "base_dex":4, "base_con":5, "base_int":2, "base_hp":68, "base_ap":6, "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "neon_jackal", "name": "Neon Jackal", "hostile_type": "creature", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":64, "common_drop": "herb_med", "money_range": (12,52),
 "basic_attack": "quick bite", "strong_attack": "rending leap", "player_abilities": [], "base_str":5, "base_dex":7, "base_con":4, "base_int":2, "base_hp":56, "base_ap":5, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "ice_gutter_punk", "name": "Ice Gutter Punk", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":36, "common_drop": "stimulant_small", "money_range": (6,30),
 "basic_attack": "chain jab", "strong_attack": "pipe smash", "player_abilities": [], "base_str":4, "base_dex":4, "base_con":3, "base_int":2, "base_hp":36, "base_ap":4, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # Level5
 {"id": "cold_case_investigator", "name": "Cold-case Investigator", "hostile_type": "humanoid", "role": "support", "min_spawn_level":5, "rarity": "rare", "base_xp":120, "common_drop": "stimulant_med", "rare_drop": "stimulant_small", "money_range": (20,100),
 "basic_attack": "interrogation jab", "strong_attack": "evidence slam", "player_abilities": ["light_spirit_lv5_ardent_inspire"], "base_str":6, "base_dex":5, "base_con":6, "base_int":6, "base_hp":92, "base_ap":6, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "spectral_trapper", "name": "Spectral Trapper", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":5, "rarity": "uncommon", "base_xp":100, "common_drop": "herb_med", "money_range": (8,48),
 "basic_attack": "ethereal snare", "strong_attack": "phantom crush", "player_abilities": ["level_1_hostile_ability_night_whisper"], "base_str":2, "base_dex":4, "base_con":3, "base_int":6, "base_hp":60, "base_ap":6, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 # Level6
 {"id": "iceberg_stalker", "name": "Iceberg Stalker", "hostile_type": "creature", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":150, "common_drop": "herb_major", "money_range": (20,90),
 "basic_attack": "great maul", "strong_attack": "ice crush", "player_abilities": [], "base_str":8, "base_dex":4, "base_con":8, "base_int":2, "base_hp":140, "base_ap":6, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "neon_barker", "name": "Neon Barker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":140, "common_drop": "stimulant_large", "money_range": (18,80),
 "basic_attack": "loud bark", "strong_attack": "blitz shout", "player_abilities": [], "base_str":5, "base_dex":6, "base_con":5, "base_int":3, "base_hp":120, "base_ap":7, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "frozen_enforcer", "name": "Frozen Enforcer", "hostile_type": "humanoid", "role": "support", "min_spawn_level":7, "rarity": "rare", "base_xp":200, "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (30,120),
 "basic_attack": "security strike", "strong_attack": "stun baton", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"], "base_str":9, "base_dex":5, "base_con":9, "base_int":4, "base_hp":180, "base_ap":7, "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 # Level8
 {"id": "snowblind_hunter", "name": "Snowblind Hunter", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "rare", "base_xp":240, "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (40,160),
 "basic_attack": "rifle snap", "strong_attack": "precision shot", "player_abilities": ["fire_earth_technique_lv2_blaze_hammer"], "base_str":6, "base_dex":9, "base_con":6, "base_int":7, "base_hp":160, "base_ap":8, "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":2},

 # Level9
 {"id": "black_ice_assassin", "name": "Black Ice Assassin", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":9, "rarity": "rare", "base_xp":280, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (50,200),
 "basic_attack": "silent stab", "strong_attack": "fatal plunge", "player_abilities": ["fire_dark_skill_lv2_embersmoke"], "base_str":7, "base_dex":10, "base_con":5, "base_int":6, "base_hp":180, "base_ap":9, "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":2},

 # Level10
 {"id": "ice_shaman", "name": "Ice Shaman", "hostile_type": "elemental", "role": "hazard", "min_spawn_level":10, "rarity": "superrare", "base_xp":640, "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (45,180),
 "basic_attack": "chill touch", "strong_attack": "glacial wave", "player_abilities": ["lv2_hostile_ability_ice_light_magic_frost_nova"], "base_str":8, "base_dex":6, "base_con":10, "base_int":14, "base_hp":720, "base_ap":12, "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":3},
]