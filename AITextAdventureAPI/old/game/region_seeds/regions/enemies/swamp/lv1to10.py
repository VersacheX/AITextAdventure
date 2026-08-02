# LEVEL 1-10 hostile regional (to be imported by higher-level modules).

RANDOM_HOSTILE_SEEDS = []

# LEVEL1-10 hostile regional seeds for swamp region (to be imported by higher-level modules).
# Export a list named SEEDS_LV1TO10
SEEDS_LV1TO10 = [
 {"id": "murkling", "name": "Murkling", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6, "common_drop": "herb_minor", "money_range": (0,4),
 "basic_attack": "mire nip", "strong_attack": "mud snap", "player_abilities": [],
 "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":6, "base_ap":1, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "swamp_rat", "name": "Swamp Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":10, "common_drop": "herb_minor", "money_range": (0,5),
 "basic_attack": "fierce bite", "strong_attack": "savage bite", "player_abilities": [],
 "base_str":2, "base_dex":4, "base_con":2, "base_int":1, "base_hp":12, "base_ap":1, "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "slick_trapper", "name": "Slick Trapper", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":1, "rarity": "rare", "base_xp":24, "common_drop": "herb_minor", "money_range": (1,8),
 "basic_attack": "snare jab", "strong_attack": "entangle pull", "player_abilities": [],
 "base_str":4, "base_dex":4, "base_con":4, "base_int":3, "base_hp":20, "base_ap":3, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "neon_frog", "name": "Neon Frog", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6, "common_drop": "herb_minor", "money_range": (0,3),
 "basic_attack": "tongue slap", "strong_attack": "acid spit", "player_abilities": [],
 "base_str":1, "base_dex":5, "base_con":1, "base_int":1, "base_hp":6, "base_ap":1, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 # Level2
 {"id": "bayou_hobo", "name": "Bayou Hobo", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":14, "common_drop": "stimulant_small", "money_range": (1,8),
 "basic_attack": "grimy swipe", "strong_attack": "barrel smash", "player_abilities": [],
 "base_str":2, "base_dex":2, "base_con":3, "base_int":1, "base_hp":18, "base_ap":3, "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "mire_gargoyle", "name": "Mire Gargoyle", "hostile_type": "construct", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":16, "common_drop": "herb_minor", "money_range": (2,10),
 "basic_attack": "stone beak", "strong_attack": "crushing wing", "player_abilities": [],
 "base_str":3, "base_dex":2, "base_con":4, "base_int":1, "base_hp":24, "base_ap":2, "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "fog_stalker", "name": "Fog Stalker", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":2, "rarity": "uncommon", "base_xp":22, "common_drop": "herb_med", "money_range": (4,18),
 "basic_attack": "dark slash", "strong_attack": "vanishing strike", "player_abilities": ["dark_magic_lv1_shadow_tendril"],
 "base_str":3, "base_dex":5, "base_con":2, "base_int":3, "base_hp":26, "base_ap":4, "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # Level3
 {"id": "swamp_scrapper", "name": "Swamp Scrapper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":26, "common_drop": "herb_med", "money_range": (6,24),
 "basic_attack": "striking fist", "strong_attack": "smashing blow", "player_abilities": [],
 "base_str":4, "base_dex":3, "base_con":4, "base_int":2, "base_hp":32, "base_ap":4, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "rot_walker", "name": "Rot Walker", "hostile_type": "undead", "role": "hazard", "min_spawn_level":3, "rarity": "common", "base_xp":28, "common_drop": "herb_med", "money_range": (4,22),
 "basic_attack": "putrid punch", "strong_attack": "decay slam", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":3, "base_dex":2, "base_con":5, "base_int":1, "base_hp":36, "base_ap":4, "str_per_level":1, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "bog_slither", "name": "Bog Slither", "hostile_type": "creature", "role": "hazard", "min_spawn_level":3, "rarity": "common", "base_xp":18, "common_drop": "herb_minor", "money_range": (2,12),
 "basic_attack": "venom nip", "strong_attack": "constrict", "player_abilities": [],
 "base_str":2, "base_dex":5, "base_con":2, "base_int":2, "base_hp":20, "base_ap":3, "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 # Level4
 {"id": "neon_wader", "name": "Neon Wader", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":40, "common_drop": "stimulant_small", "money_range": (8,36),
 "basic_attack": "tire iron", "strong_attack": "neck snap", "player_abilities": ["ice_skill_lv1_ice_shuriken"],
 "base_str":5, "base_dex":4, "base_con":5, "base_int":2, "base_hp":44, "base_ap":5, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "silt_mage", "name": "Silt Mage", "hostile_type": "magic", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":48, "common_drop": "herb_med", "money_range": (10,44),
 "basic_attack": "mire spark", "strong_attack": "silt burst", "player_abilities": ["electric_fire_magic_lv2_arclance"],
 "base_str":2, "base_dex":3, "base_con":3, "base_int":10, "base_hp":36, "base_ap":6, "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "swamp_gutter_punk", "role": "damage", "name": "Swamp Gutter Punk", "hostile_type": "humanoid", "min_spawn_level":4, "rarity": "common", "base_xp":36, "common_drop": "stimulant_small", "money_range": (6,30),
 "basic_attack": "chain jab", "strong_attack": "pipe smash", "player_abilities": [], "base_str":4, "base_dex":4, "base_con":3, "base_int":2, "base_hp":36, "base_ap":4, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # Level5
 {"id": "dire_hound", "name": "Dire Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":62, "common_drop": "herb_med", "money_range": (12,56),
 "basic_attack": "rending bite", "strong_attack": "frenzied maul", "player_abilities": [],
 "base_str":6, "base_dex":6, "base_con":5, "base_int":2, "base_hp":64, "base_ap":6, "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "fenling", "name": "Fenling", "hostile_type": "creature", "role": "damage", "min_spawn_level":5, "rarity": "common", "base_xp":48, "common_drop": "herb_minor", "money_range": (10,44),
 "basic_attack": "snarl", "strong_attack": "bog stomp", "player_abilities": [], "base_str":5, "base_dex":5, "base_con":4, "base_int":2, "base_hp":80, "base_ap":5, "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # Level6
 {"id": "swamp_priest", "name": "Swamp Priest", "hostile_type": "faith", "role": "support", "min_spawn_level":6, "rarity": "rare", "base_xp":120, "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (20,100),
 "basic_attack": "blighted palm", "strong_attack": "curse flare", "player_abilities": ["light_light_air_faith_lv3_major_heal", "air_faith_lv1_zephyr_bless"],
 "base_str":3, "base_dex":3, "base_con":6, "base_int":10, "base_hp":96, "base_ap":8, "str_per_level":1, "dex_per_level":0, "con_per_level":2, "int_per_level":2},

 {"id": "neon_reaver", "name": "Neon Reaver", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "rare", "base_xp":140, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (18,80),
 "basic_attack": "chrome slash", "strong_attack": "gutting rip", "player_abilities": ["air_electric_fire_technique_lv3_tempest_charge"],
 "base_str":8, "base_dex":6, "base_con":6, "base_int":4, "base_hp":120, "base_ap":8, "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 # Level7
 {"id": "bog_wraith", "name": "Bog Wraith", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":7, "rarity": "rare", "base_xp":160, "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (25,120),
 "basic_attack": "soul chill", "strong_attack": "wailing gust", "player_abilities": ["level_1_hostile_ability_night_whisper"],
 "base_str":2, "base_dex":4, "base_con":5, "base_int":10, "base_hp":120, "base_ap":8, "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":3},

 # Level8
 {"id": "bog_predator", "name": "Bog Predator", "hostile_type": "creature", "role": "damage", "min_spawn_level":8, "rarity": "uncommon", "base_xp":200, "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (30,140),
 "basic_attack": "root club", "strong_attack": "entangling slam", "player_abilities": [],
 "base_str":10, "base_dex":4, "base_con":10, "base_int":3, "base_hp":220, "base_ap":8, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 # Level9
 {"id": "black_mire_assassin", "name": "Black Mire Assassin", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":9, "rarity": "uncommon", "base_xp":240, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (40,180),
 "basic_attack": "silent plunge", "strong_attack": "toxic plunge", "player_abilities": ["fire_dark_skill_lv2_embersmoke"],
 "base_str":7, "base_dex":11, "base_con":5, "base_int":5, "base_hp":180, "base_ap":9, "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # Level10
 {"id": "muck_colossus", "name": "Muck Colossus", "hostile_type": "construct", "role": "damage", "min_spawn_level":10, "rarity": "superrare", "base_xp":640, "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (50,220),
 "basic_attack": "massive slam", "strong_attack": "tremor crush", "player_abilities": [],
 "base_str":14, "base_dex":2, "base_con":14, "base_int":2, "base_hp":720, "base_ap":10, "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},
]