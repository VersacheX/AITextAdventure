# LEVEL1-10 hostile regional (to be imported by higher-level modules).
# Seeds for desert region, levels1-10 — balanced dispersity and sorted by min_spawn_level.
SEEDS_LV1TO10 = [
 {"id": "dune_rat", "name": "Dune Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":8, "common_drop": "herb_minor", "money_range": (0,5),
 "basic_attack": "fierce bite", "strong_attack": "savage bite", "player_abilities": [], "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":8, "base_ap":1, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "wild_sand_scrapper", "name": "Wild Sand Scrapper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":14, "common_drop": "herb_minor", "money_range": (1,6),
 "basic_attack": "rusty jab", "strong_attack": "sand swipe", "player_abilities": [], "base_str":2, "base_dex":3, "base_con":2, "base_int":1, "base_hp":12, "base_ap":2, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "mirage_waif", "name": "Mirage Waif", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":1, "rarity": "rare", "base_xp":40, "common_drop": "herb_minor", "rare_drop": "tome_int", "money_range": (2,12),
 "basic_attack": "ghostly touch", "strong_attack": "fading wail", "player_abilities": ["level_1_hostile_ability_night_whisper"], "base_str":1, "base_dex":4, "base_con":1, "base_int":6, "base_hp":18, "base_ap":6, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 # Level2
 {"id": "scorpionling", "name": "Scorpionling", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":14, "common_drop": "herb_minor", "money_range": (1,8),
 "basic_attack": "sting", "strong_attack": "venom lash", "player_abilities": [], "base_str":2, "base_dex":4, "base_con":2, "base_int":1, "base_hp":16, "base_ap":2, "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "dune_hustler", "name": "Dune Hustler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":16, "common_drop": "stimulant_small", "money_range": (2,10),
 "basic_attack": "dirty palm", "strong_attack": "sand toss", "player_abilities": [], "base_str":2, "base_dex":3, "base_con":2, "base_int":2, "base_hp":18, "base_ap":3, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "sand_skulk", "name": "Sand Skulk", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "uncommon", "base_xp":22, "common_drop": "herb_minor", "money_range": (2,12),
 "basic_attack": "low bite", "strong_attack": "sandy lunge", "player_abilities": None, "base_str":2, "base_dex":5, "base_con":2, "base_int":1, "base_hp":14, "base_ap":2, "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 # Level3
 {"id": "sand_snake", "name": "Sand Snake", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":20, "common_drop": "herb_minor", "money_range": (2,12),
 "basic_attack": "coil bite", "strong_attack": "burrowing crush", "player_abilities": [], "base_str":3, "base_dex":5, "base_con":3, "base_int":2, "base_hp":22, "base_ap":3, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "rock_lurker", "name": "Rock Lurker", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":18, "common_drop": "herb_minor", "money_range": (2,14),
 "basic_attack": "claw swipe", "strong_attack": "stone crush", "player_abilities": [], "base_str":3, "base_dex":3, "base_con":4, "base_int":1, "base_hp":20, "base_ap":2, "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "dust_thug", "name": "Dust Thug", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "uncommon", "base_xp":36, "common_drop": "stimulant_small", "money_range": (6,30),
 "basic_attack": "whistle jab", "strong_attack": "sonic clap", "player_abilities": ["ice_skill_lv1_ice_shuriken"], "base_str":3, "base_dex":4, "base_con":3, "base_int":3, "base_hp":34, "base_ap":4, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 # Level4
 {"id": "dune_bandit", "name": "Dune Bandit", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":36, "common_drop": "herb_med", "money_range": (6,30),
 "basic_attack": "knife jab", "strong_attack": "gutting slash", "player_abilities": [], "base_str":4, "base_dex":4, "base_con":3, "base_int":2, "base_hp":36, "base_ap":4, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "wind_skiff", "name": "Wind Skiff", "hostile_type": "creature", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":10, "common_drop": "herb_minor", "money_range": (0,4),
 "basic_attack": "peck", "strong_attack": "gusty flap", "player_abilities": [], "base_str":1, "base_dex":5, "base_con":1, "base_int":1, "base_hp":10, "base_ap":1, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "desert_pickpocket", "name": "Desert Pickpocket", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":4, "rarity": "uncommon", "base_xp":30, "common_drop": "stimulant_small", "money_range": (3,18),
 "basic_attack": "flick hand", "strong_attack": "distract-and-stab", "player_abilities": None, "base_str":2, "base_dex":6, "base_con":2, "base_int":3, "base_hp":28, "base_ap":3, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # Level5
 {"id": "sandstone_sentinel", "name": "Sandstone Sentinel", "hostile_type": "construct", "role": "support", "min_spawn_level":5, "rarity": "rare", "base_xp":80, "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (20,100),
 "basic_attack": "stone swipe", "strong_attack": "granite crush", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"], "base_str":6, "base_dex":3, "base_con":8, "base_int":2, "base_hp":100, "base_ap":6, "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # Level6
 {"id": "sand_sniper", "name": "Sand Sniper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "rare", "base_xp":140, "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (24,120),
 "basic_attack": "rifle snap", "strong_attack": "precision shot", "player_abilities": ["fire_earth_technique_lv2_blaze_hammer", "ice_skill_lv1_ice_shuriken"], "base_str":5, "base_dex":9, "base_con":5, "base_int":6, "base_hp":88, "base_ap":6, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # Level7
 {"id": "sand_berserker", "name": "Sand Berserker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "rare", "base_xp":180, "common_drop": "stimulant_large", "rare_drop": "cleaver", "money_range": (30,140),
 "basic_attack": "sand slash", "strong_attack": "rending maul", "player_abilities": ["air_electric_fire_technique_lv3_tempest_charge"], "base_str":8, "base_dex":5, "base_con":8, "base_int":3, "base_hp":160, "base_ap":7, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "oasis_dryad", "name": "Oasis Dryad", "hostile_type": "spirit", "role": "support", "min_spawn_level":7, "rarity": "uncommon", "base_xp":120, "common_drop": "herb_major", "money_range": (20,90),
 "basic_attack": "soothing touch", "strong_attack": "mirage bind", "player_abilities": ["water_faith_lv1_mending_streams"], "base_str":4, "base_dex":4, "base_con":6, "base_int":6, "base_hp":140, "base_ap":6, "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 # Level8
 {"id": "tomb_keeper", "name": "Tomb Keeper", "hostile_type": "undead", "role": "hazard", "min_spawn_level":8, "rarity": "rare", "base_xp":220, "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (30,140),
 "basic_attack": "bony swipe", "strong_attack": "necrotic thrust", "player_abilities": ["dark_dark_magic_lv2_umbra_storm"], "base_str":6, "base_dex":4, "base_con":8, "base_int":8, "base_hp":180, "base_ap":8, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":3},

 # Level9
 {"id": "sand_howler", "name": "Sand Howler", "hostile_type": "creature", "role": "damage", "min_spawn_level":9, "rarity": "common", "base_xp":90, "common_drop": "stimulant_large", "rare_drop": "ointment", "money_range": (40,180),
 "basic_attack": "howling bite", "strong_attack": "dune swipe", "player_abilities": [], "base_str":8, "base_dex":8, "base_con":6, "base_int":4, "base_hp":220, "base_ap":8, "str_per_level":3, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # Level10 - superrare
 {"id": "mirage_witch", "name": "Mirage Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level":10, "rarity": "superrare", "base_xp":480, "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (45,180),
 "basic_attack": "mirage touch", "strong_attack": "illusive burst", "player_abilities": ["electric_fire_magic_lv2_arclance", "dark_magic_lv1_shadow_tendril"], "base_str":6, "base_dex":6, "base_con":8, "base_int":14, "base_hp":320, "base_ap":10, "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":3},
]