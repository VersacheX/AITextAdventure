# LEVEL1-10 hostile regional seeds for grassland region (to be imported by higher-level modules).
# Export a list named SEEDS_LV1TO10
SEEDS_LV1TO10 = [
 {"id": "grassling", "name": "Grassling", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6, "common_drop": "herb_minor", "money_range": (0,4),
 "basic_attack": "nip", "strong_attack": "lashing reed", "player_abilities": [], "base_str":1, "base_dex":4, "base_con":1, "base_int":1, "base_hp":6, "base_ap":1, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "meadow_rat", "name": "Meadow Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":9, "common_drop": "herb_minor", "money_range": (0,5),
 "basic_attack": "fierce bite", "strong_attack": "savage bite", "player_abilities": [], "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":7, "base_ap":1, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "field_scrapper", "name": "Field Scrapper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":12, "common_drop": "herb_minor", "money_range": (1,6),
 "basic_attack": "dirty swipe", "strong_attack": "gutting jab", "player_abilities": [], "base_str":2, "base_dex":3, "base_con":2, "base_int":1, "base_hp":12, "base_ap":2, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "devil_raven", "name": "Devil Raven", "hostile_type": "spirit", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":12, "common_drop": "herb_minor", "money_range": (0,4),
 "basic_attack": "gust tap", "strong_attack": "whisper gust", "player_abilities": ["ice_skill_lv1_ice_shuriken"], "base_str":1, "base_dex":5, "base_con":1, "base_int":2, "base_hp":12, "base_ap":2, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "skylark", "name": "Skylark", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "rare", "base_xp":20, "common_drop": "herb_minor", "money_range": (0,3),
 "basic_attack": "peck", "strong_attack": "wind flap", "player_abilities": [], "base_str":1, "base_dex":7, "base_con":1, "base_int":1, "base_hp":22, "base_ap":2, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 # Level2
 {"id": "stalk_shade", "name": "Stalk Shade", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":2, "rarity": "common", "base_xp":14, "common_drop": "herb_minor", "money_range": (1,8),
 "basic_attack": "lurking swipe", "strong_attack": "shadow clamp", "player_abilities": ["dark_magic_lv1_shadow_tendril"], "base_str":2, "base_dex":4, "base_con":2, "base_int":2, "base_hp":16, "base_ap":3, "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "grass_vendor", "name": "Grass Vendor", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "uncommon", "base_xp":12, "common_drop": "stimulant_small", "money_range": (2,10),
 "basic_attack": "tray toss", "strong_attack": "stale crate", "player_abilities": [], "base_str":2, "base_dex":3, "base_con":2, "base_int":2, "base_hp":16, "base_ap":3, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 # Level3
 {"id": "prairie_hunter", "name": "Prairie Hunter", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":22, "common_drop": "herb_med", "money_range": (6,28),
 "basic_attack": "stalking slash", "strong_attack": "frenzied lunge", "player_abilities": [], "base_str":4, "base_dex":4, "base_con":3, "base_int":2, "base_hp":34, "base_ap":4, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "nettle_guardian", "name": "Nettle Guardian", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":18, "common_drop": "herb_minor", "money_range": (2,12),
 "basic_attack": "thorn jab", "strong_attack": "vicious bind", "player_abilities": [], "base_str":3, "base_dex":4, "base_con":3, "base_int":2, "base_hp":20, "base_ap":3, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "gale_rider", "name": "Gale Rider", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":36, "common_drop": "stimulant_small", "money_range": (6,30),
 "basic_attack": "gust strike", "strong_attack": "aerial clap", "player_abilities": ["air_skill_lv2_swift_tap"], "base_str":3, "base_dex":5, "base_con":3, "base_int":3, "base_hp":34, "base_ap":4, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # Level4
 {"id": "stonefolk", "name": "Stonefolk", "hostile_type": "construct", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":48, "common_drop": "herb_med", "money_range": (10,44),
 "basic_attack": "boulder bash", "strong_attack": "granite slam", "player_abilities": ["earth_earth_technique_lv2_terra_slam"], "base_str":4, "base_dex":2, "base_con":6, "base_int":2, "base_hp":44, "base_ap":5, "str_per_level":1, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "sun_scout", "name": "Sun Scout", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":48, "common_drop": "herb_med", "money_range": (6,30),
 "basic_attack": "knife jab", "strong_attack": "precision slash", "player_abilities": ["fire_earth_technique_lv2_blaze_hammer"], "base_str":4, "base_dex":5, "base_con":3, "base_int":3, "base_hp":44, "base_ap":4, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # Level5
 {"id": "thorn_shaman", "name": "Thorn Shaman", "hostile_type": "magic", "role": "support", "min_spawn_level":5, "rarity": "rare", "base_xp":90, "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (20,100),
 "basic_attack": "curse prickle", "strong_attack": "sap burst", "player_abilities": ["light_faith_lv2_prism_burst", "earth_earth_technique_lv2_terra_slam"], "base_str":3, "base_dex":3, "base_con":5, "base_int":10, "base_hp":92, "base_ap":6, "str_per_level":1, "dex_per_level":0, "con_per_level":2, "int_per_level":2},

 {"id": "wind_hound", "name": "Wind Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":62, "common_drop": "herb_med", "money_range": (12,56),
 "basic_attack": "rending bite", "strong_attack": "gust maul", "player_abilities": [], "base_str":6, "base_dex":6, "base_con":5, "base_int":2, "base_hp":64, "base_ap":6, "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # Level6
 {"id": "meadow_priest", "name": "Meadow Priest", "hostile_type": "faith", "role": "support", "min_spawn_level":6, "rarity": "rare", "base_xp":120, "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (20,100),
 "basic_attack": "blessed palm", "strong_attack": "lumen flare", "player_abilities": ["light_faith_lv2_prism_burst", "light_faith_lv1_glimmer"], "base_str":3, "base_dex":3, "base_con":6, "base_int":10, "base_hp":96, "base_ap":8, "str_per_level":1, "dex_per_level":0, "con_per_level":2, "int_per_level":2},

 {"id": "field_reaver", "name": "Field Reaver", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "rare", "base_xp":140, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (18,80),
 "basic_attack": "chrome slash", "strong_attack": "gutting rip", "player_abilities": ["fire_technique_lv4_berserker_tech"], "base_str":8, "base_dex":6, "base_con":6, "base_int":4, "base_hp":120, "base_ap":8, "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 # Level7
 {"id": "prairie_wraith", "name": "Prairie Wraith", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":7, "rarity": "rare", "base_xp":160, "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (25,120),
 "basic_attack": "soul chill", "strong_attack": "wailing gust", "player_abilities": ["dark_magic_lv2_night_whisper"], "base_str":2, "base_dex":4, "base_con":5, "base_int":10, "base_hp":120, "base_ap":8, "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":3},

 # Level8
 {"id": "fen_guardian", "name": "Fen Guardian", "hostile_type": "creature", "role": "damage", "min_spawn_level":8, "rarity": "rare", "base_xp":200, "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (30,140),
 "basic_attack": "root club", "strong_attack": "entangling slam", "player_abilities": [], "base_str":10, "base_dex":4, "base_con":10, "base_int":3, "base_hp":220, "base_ap":8, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 # Level9
 {"id": "black_grass_assassin", "name": "Black Grass Assassin", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":9, "rarity": "rare", "base_xp":240, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (40,180),
 "basic_attack": "silent plunge", "strong_attack": "venom plunge", "player_abilities": ["fire_dark_skill_lv2_embersmoke"], "base_str":7, "base_dex":11, "base_con":5, "base_int":5, "base_hp":180, "base_ap":9, "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # Level10
 {"id": "stone_colossus", "name": "Stone Colossus", "hostile_type": "construct", "role": "damage", "min_spawn_level":10, "rarity": "superrare", "base_xp":640, "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (50,220),
 "basic_attack": "massive slam", "strong_attack": "tremor crush", "player_abilities": ["earth_earth_technique_lv2_terra_slam"], "base_str":18, "base_dex":4, "base_con":18, "base_int":2, "base_hp":720, "base_ap":8, "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},
]