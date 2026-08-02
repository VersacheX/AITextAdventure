# Level11-20 hostile seeds for the Great Dune City (mid-tier)
# Split out from constants_enemies_mid_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==11
 {"id": "sand_weaver", "name": "Sand Weaver", "hostile_type": "creature", "role": "hazard", "min_spawn_level":11, "rarity": "common", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (12,48),
 "basic_attack": "webbed strike", "strong_attack": "tangling lash", "player_abilities": None,
 "base_str":4, "base_dex":6, "base_con":3, "base_int":2, "base_hp":80, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "gutter_monger", "name": "Gutter Monger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "uncommon", "base_xp":110,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (10,50),
 "basic_attack": "slime palm", "strong_attack": "gut punch", "player_abilities": [],
 "base_str":5, "base_dex":5, "base_con":4, "base_int":2, "base_hp":92, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==12
 {"id": "mid_city_wrecker", "name": "Mid-city Wrecker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "rare", "base_xp":220,
 "common_drop": "herb_major", "rare_drop": "sawed_off", "money_range": (40,180),
 "basic_attack": "haymaker", "strong_attack": "wrecking ball", "player_abilities": ["earth_fire_technique_lv2_berserker_tech"],
 "base_str":10, "base_dex":3, "base_con":8, "base_int":1, "base_hp":140, "base_ap":6,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "ruffian_lieutenant", "name": "Ruffian Lieutenant", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":130,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (20,88),
 "basic_attack": "short spear jab", "strong_attack": "brutish sweep", "player_abilities": None,
 "base_str":6, "base_dex":4, "base_con":5, "base_int":2, "base_hp":120, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==13
 {"id": "dune_marauder", "name": "Dune Marauder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":140,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (22,96),
 "basic_attack": "sandy cleave", "strong_attack": "mauling charge", "player_abilities": None,
 "base_str":7, "base_dex":4, "base_con":6, "base_int":2, "base_hp":140, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "dust_scholar", "name": "Dust Scholar", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":13, "rarity": "uncommon", "base_xp":150,
 "common_drop": "herb_med", "rare_drop": "tome_dex", "money_range": (18,80),
 "basic_attack": "scribbled jabs", "strong_attack": "arcane flare", "player_abilities": ["level_1_hostile_ability_streamlet"],
 "base_str":3, "base_dex":5, "base_con":3, "base_int":9, "base_hp":110, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 # min_spawn_level ==14
 {"id": "dream_eater3", "name": "Dream Eater", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":14, "rarity": "rare", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,320),
 "basic_attack": "mind gnaw", "strong_attack": "maddening shriek", "player_abilities": ["lv2_hostile_ability_dark_air_skill_nightmare_wave"],
 "base_str":4, "base_dex":6, "base_con":6, "base_int":14, "base_hp":160, "base_ap":14,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":4},

 {"id": "mid_city_silt_runner", "name": "Mid-city Silt Runner", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "uncommon", "base_xp":130,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (24,110),
 "basic_attack": "slashing bite", "strong_attack": "spine lunge", "player_abilities": None,
 "base_str":6, "base_dex":7, "base_con":5, "base_int":1, "base_hp":140, "base_ap":5,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==15
 {"id": "decrepit_colossus", "name": "Decrepit Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":15, "rarity": "rare", "base_xp":320,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (60,220),
 "basic_attack": "piston swing", "strong_attack": "hydraulic crush", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":16, "base_dex":2, "base_con":18, "base_int":1, "base_hp":320, "base_ap":4,
 "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "iron_watchman", "name": "Iron Watchman", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":180,
 "common_drop": "cloth_gloves", "rare_drop": None, "money_range": (40,160),
 "basic_attack": "guard swipe", "strong_attack": "bracing stomp", "player_abilities": None,
 "base_str":8, "base_dex":3, "base_con":8, "base_int":2, "base_hp":180, "base_ap":6,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==16
 {"id": "femme_fatale", "name": "Femme Fatale", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":16, "rarity": "superrare", "base_xp":380,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (120,480),
 "basic_attack": "elegant stab", "strong_attack": "fatal flourish", "player_abilities": ["lv2_hostile_ability_earth_light_tech_primal_disunion"],
 "base_str":9, "base_dex":11, "base_con":6, "base_int":8, "base_hp":200, "base_ap":12,
 "str_per_level":3, "dex_per_level":4, "con_per_level":2, "int_per_level":3},

 {"id": "sand_warden", "name": "Sand Warden", "hostile_type": "humanoid", "role": "support", "min_spawn_level":16, "rarity": "common", "base_xp":200,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (80,300),
 "basic_attack": "warding sweep", "strong_attack": "dune shield", "player_abilities": None,
 "base_str":9, "base_dex":6, "base_con":9, "base_int":3, "base_hp":220, "base_ap":8,
 "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":1},

 # min_spawn_level ==17
 {"id": "baron_sentinel", "name": "Baron Sentinel", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":220,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (90,360),
 "basic_attack": "polished strike", "strong_attack": "noble onslaught", "player_abilities": None,
 "base_str":10, "base_dex":6, "base_con":9, "base_int":4, "base_hp":240, "base_ap":9,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 {"id": "veil_reaver", "name": "Veil Reaver", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":17, "rarity": "uncommon", "base_xp":200,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (60,240),
 "basic_attack": "dark slash", "strong_attack": "vanishing strike", "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
 "base_str":7, "base_dex":12, "base_con":6, "base_int":5, "base_hp":220, "base_ap":8,
 "str_per_level":2, "dex_per_level":3, "con_per_level":2, "int_per_level":1},

 # min_spawn_level ==18
 {"id": "bone_crusher", "name": "Bone Crusher", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":18, "rarity": "common", "base_xp":260,
 "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (100,400),
 "basic_attack": "crushing blow", "strong_attack": "bone shatter", "player_abilities": None,
 "base_str":12, "base_dex":4, "base_con":10, "base_int":2, "base_hp":300, "base_ap":8,
 "str_per_level":4, "dex_per_level":1, "con_per_level":3, "int_per_level":0},

 {"id": "shade_garrison", "name": "Shade Garrison", "hostile_type": "humanoid", "role": "support", "min_spawn_level":18, "rarity": "rare", "base_xp":280,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (110,420),
 "basic_attack": "guard charge", "strong_attack": "stunning volley", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":8, "base_dex":6, "base_con":10, "base_int":4, "base_hp":260, "base_ap":10,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 # min_spawn_level ==19
 {"id": "sand_overseer", "name": "Sand Overseer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":19, "rarity": "common", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (120,480),
 "basic_attack": "commanding strike", "strong_attack": "overseer barrage", "player_abilities": None,
 "base_str":10, "base_dex":8, "base_con":9, "base_int":5, "base_hp":320, "base_ap":10,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 {"id": "sand_phantom", "name": "Sand Phantom", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":19, "rarity": "uncommon", "base_xp":260,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (80,320),
 "basic_attack": "ethereal swipe", "strong_attack": "void grasp", "player_abilities": ["level_1_hostile_ability_night_whisper"],
 "base_str":6, "base_dex":9, "base_con":6, "base_int":8, "base_hp":280, "base_ap":10,
 "str_per_level":2, "dex_per_level":3, "con_per_level":2, "int_per_level":2},

 # min_spawn_level ==20
 {"id": "dune_champion", "name": "Dune Champion", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":20, "rarity": "common", "base_xp":340,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (150,700),
 "basic_attack": "champion's cleave", "strong_attack": "earthshatter", "player_abilities": None,
 "base_str":12, "base_dex":8, "base_con":12, "base_int":6, "base_hp":380, "base_ap":12,
 "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 {"id": "deserter_dune_lieutenant", "name": "Deserter Dune Lieutenant", "hostile_type": "humanoid", "role": "support", "min_spawn_level":20, "rarity": "rare", "base_xp":420,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (150,700),
 "basic_attack": "ruthless sand-strikes", "strong_attack": "lieutenant's onslaught", "player_abilities": ["level_1_hostile_ability_inspire", "earth_fire_technique_lv2_berserker_tech"],
 "base_str":9, "base_dex":6, "base_con":9, "base_int":5, "base_hp":220, "base_ap":10,
 "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":2},
]
