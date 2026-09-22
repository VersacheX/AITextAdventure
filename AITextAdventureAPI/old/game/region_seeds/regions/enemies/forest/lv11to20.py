# LEVEL 1-10 hostile regional (to be imported by higher-level modules).

RANDOM_HOSTILE_SEEDS = []

# LEVEL11-20 hostile regional seeds for forest region (to be imported by higher-level modules).
# Export a list named SEEDS_LV11TO20
SEEDS_LV11TO20 = [
 {"id": "willow_guard", "name": "Willow Guard", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":72,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,44),
 "basic_attack": "sapling bash", "strong_attack": "bark shove", "player_abilities": None,
 "base_str":4, "base_dex":4, "base_con":4, "base_int":2, "base_hp":72, "base_ap":4, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "pond_tinker", "name": "Pond Tinker", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":11, "rarity": "uncommon", "base_xp":110,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (12,60),
 "basic_attack": "wrench jab", "strong_attack": "oil splash", "player_abilities": ["level_1_hostile_ability_electric_tech_hack_overload"],
 "base_str":3, "base_dex":5, "base_con":4, "base_int":5, "base_hp":84, "base_ap":5, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 {"id": "clockwork_beetle", "name": "Clockwork Beetle", "hostile_type": "construct", "role": "support", "min_spawn_level":11, "rarity": "uncommon", "base_xp":150,
 "common_drop": "stimulant_small", "rare_drop": "kevlar_vest", "money_range": (16,88),
 "basic_attack": "piston jab", "strong_attack": "hydraulic crush", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":8, "base_dex":3, "base_con":10, "base_int":1, "base_hp":140, "base_ap":5, "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "moon_tender", "name": "Moon Tender", "hostile_type": "spirit", "role": "support", "min_spawn_level":12, "rarity": "rare", "base_xp":260,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (22,120),
 "basic_attack": "moonbeam touch", "strong_attack": "lunar swell", "player_abilities": ["lv2_hostile_ability_air_water_spirit_gale_of_silence", "level_1_hostile_ability_fire_spirit_hearthsong"],
 "base_str":4, "base_dex":8, "base_con":6, "base_int":12, "base_hp":200, "base_ap":10, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":3},

 {"id": "nightmare_wolf", "name": "Nightmare Wolf", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":12, "rarity": "superrare", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (30,160),
 "basic_attack": "shadowy snap", "strong_attack": "nightmarish maul", "player_abilities": ["lv2_hostile_ability_dark_air_skill_nightmare_wave", "dark_magic_lv5_abyssal_shadow"],
 "base_str":8, "base_dex":10, "base_con":6, "base_int":10, "base_hp":220, "base_ap":12, "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":3},

 {"id": "mire_sorcerer", "name": "Mire Sorcerer", "hostile_type": "magic", "role": "hazard", "min_spawn_level":12, "rarity": "uncommon", "base_xp":230,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (22,120),
 "basic_attack": "splash bolt", "strong_attack": "bog cascade", "player_abilities": ["lv2_hostile_ability_water_electric_magic_maelstrom_burst", "level_1_hostile_ability_earth_magic_sap_bloom"],
 "base_str":4, "base_dex":6, "base_con":6, "base_int":12, "base_hp":180, "base_ap":10, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "canopy_scout", "name": "Canopy Scout", "hostile_type": "creature", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":92,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (10,56),
 "basic_attack": "swooping strike", "strong_attack": "reed jab", "player_abilities": None,
 "base_str":4, "base_dex":6, "base_con":4, "base_int":2, "base_hp":88, "base_ap":4, "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "ironwood_guard", "name": "Ironwood Guard", "hostile_type": "humanoid", "role": "support", "min_spawn_level":13, "rarity": "rare", "base_xp":320,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (30,160),
 "basic_attack": "bark strike", "strong_attack": "iron swipe", "player_abilities": ["level_1_hostile_ability_reinforce_frame", "earth_light_technique_lv2_stone_guard"],
 "base_str":10, "base_dex":4, "base_con":12, "base_int":3, "base_hp":260, "base_ap":6, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":1},

 {"id": "entangled_colossus", "name": "Entangled Colossus", "hostile_type": "creature", "role": "damage", "min_spawn_level":13, "rarity": "rare", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (30,180),
 "basic_attack": "grappling vines", "strong_attack": "root cataclysm", "player_abilities": ["earth_earth_technique_lv2_brutal_swing", "earth_light_technique_lv2_stone_guard"],
 "base_str":14, "base_dex":2, "base_con":14, "base_int":4, "base_hp":360, "base_ap":6, "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":1},

 {"id": "harvester_wyrm", "name": "Harvester Wyrm", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "superrare", "base_xp":420,
 "common_drop": "herb_major", "rare_drop": "sawed_off", "money_range": (40,220),
 "basic_attack": "rending bite", "strong_attack": "volcanic maw", "player_abilities": ["lv2_hostile_ability_water_electric_magic_maelstrom_burst"],
 "base_str":12, "base_dex":4, "base_con":12, "base_int":4, "base_hp":320, "base_ap":8, "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":1},

 {"id": "fen_colonist", "name": "Fen Colonist", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":14, "rarity": "uncommon", "base_xp":100,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (12,64),
 "basic_attack": "flailing bargain", "strong_attack": "smuggled strike", "player_abilities": None,
 "base_str":3, "base_dex":5, "base_con":3, "base_int":4, "base_hp":76, "base_ap":4, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "bog_colossus", "name": "Bog Colossus", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "common", "base_xp":140,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (18,90),
 "basic_attack": "club swing", "strong_attack": "bog toss", "player_abilities": None,
 "base_str":8, "base_dex":3, "base_con":8, "base_int":2, "base_hp":220, "base_ap":5, "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "hollow_knight", "name": "Hollow Knight", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":15, "rarity": "uncommon", "base_xp":320,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (50,260),
 "basic_attack": "hollow strike", "strong_attack": "void rend", "player_abilities": ["lv2_hostile_ability_dark_ice_skill_void_spike", "lv2_hostile_ability_dark_air_skill_nightmare_wave"],
 "base_str":12, "base_dex":9, "base_con":12, "base_int":12, "base_hp":420, "base_ap":12, "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":3},

 {"id": "bramble_gargant", "name": "Bramble Gargant", "hostile_type": "creature", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":180,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (36,160), "basic_attack": "thorn crush", "strong_attack": "bramble stomp", "player_abilities": None,
 "base_str":10, "base_dex":3, "base_con":10, "base_int":1, "base_hp":260, "base_ap":6, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "stalkwood_bear", "name": "Stalkwood Bear", "hostile_type": "creature", "role": "damage", "min_spawn_level":16, "rarity": "common", "base_xp":200,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (30,140), "basic_attack": "maul swipe", "strong_attack": "staggering maul", "player_abilities": None,
 "base_str":11, "base_dex":4, "base_con":12, "base_int":2, "base_hp":300, "base_ap":6, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "thorn_alpha", "name": "Thorn Alpha", "hostile_type": "creature", "role": "hazard", "min_spawn_level":16, "rarity": "uncommon", "base_xp":210,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (30,160), "basic_attack": "alpha bite", "strong_attack": "thorn roar", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":9, "base_dex":5, "base_con":9, "base_int":2, "base_hp":260, "base_ap":6, "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "root_lich", "name": "Root Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level":17, "rarity": "rare", "base_xp":420,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40,220), "basic_attack": "root bolt", "strong_attack": "necrotic rot", "player_abilities": ["level_1_hostile_ability_bone_spear", "level_1_hostile_ability_night_whisper"],
 "base_str":8, "base_dex":4, "base_con":10, "base_int":14, "base_hp":320, "base_ap":10, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":3},

 {"id": "moss_colossus", "name": "Moss Colossus", "hostile_type": "creature", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":240,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (40,180), "basic_attack": "moss slam", "strong_attack": "spore quake", "player_abilities": None,
 "base_str":12, "base_dex":3, "base_con":12, "base_int":2, "base_hp":380, "base_ap":8, "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "elder_ent", "name": "Elder Ent", "hostile_type": "creature", "role": "support", "min_spawn_level":18, "rarity": "common", "base_xp":260,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (48,220), "basic_attack": "ramming root", "strong_attack": "crushing root slam", "player_abilities": ["earth_light_technique_lv2_stone_guard"],
 "base_str":10, "base_dex":2, "base_con":12, "base_int":3, "base_hp":420, "base_ap":8, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":1},

 {"id": "forest_archdruid", "name": "Forest Archdruid", "hostile_type": "magic", "role": "support", "min_spawn_level":20, "rarity": "common", "base_xp":320,
 "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (60,280), "basic_attack": "thorn blast", "strong_attack": "ancient wrath", "player_abilities": ["lv2_hostile_ability_water_dark_magic_gloom_tide", "level_1_hostile_ability_earth_magic_sap_bloom"],
 "base_str":8, "base_dex":6, "base_con":8, "base_int":14, "base_hp":480, "base_ap":10, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":3},
]