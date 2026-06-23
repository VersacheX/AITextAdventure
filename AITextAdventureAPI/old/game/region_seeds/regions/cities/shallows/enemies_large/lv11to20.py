# Level11-20 hostile seeds for Brineward Harbor (large-city)
# Export a list named SEEDS_LV11TO20 used by constants_enemies_large_city.py
SEEDS_LV11TO20 = [
 {"id": "abyssal_serpentling", "name": "Abyssal Serpentling", "hostile_type": "eldritch", "role": "damage", "min_spawn_level":11, "rarity": "uncommon", "base_xp":260,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (30,140),
 "basic_attack": "maw lash", "strong_attack": "shadow constrict", "player_abilities": ["abyssal_storm"],
 "base_str":8, "base_dex":6, "base_con":8, "base_int":3, "base_hp":180, "base_ap":6,
 "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":0},

 {"id": "hollow_savant_sea", "name": "Hollow Savant of the Sea", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":11, "rarity": "uncommon", "base_xp":220,
 "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (30,140),
 "basic_attack": "spent rune", "strong_attack": "mind latch", "player_abilities": ["nightmare_wave", "void_veil"],
 "base_str":2, "base_dex":3, "base_con":4, "base_int":12, "base_hp":110, "base_ap":9,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "pickled_smuggler", "name": "Pickled Smuggler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":140,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (20,100),
 "basic_attack": "rum-slick jab", "strong_attack": "gutting swing", "player_abilities": None,
 "base_str":5, "base_dex":4, "base_con":5, "base_int":2, "base_hp":120, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "night_oiler", "name": "Night Oiler", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":12, "rarity": "rare", "base_xp":220,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (30,140),
 "basic_attack": "grease swipe", "strong_attack": "silent choke", "player_abilities": ["void_veil"],
 "base_str":3, "base_dex":7, "base_con":4, "base_int":6, "base_hp":90, "base_ap":8,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":2},

 {"id": "rustwork_colossus", "name": "Rustwork Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":14, "rarity": "rare", "base_xp":320,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (60,240),
 "basic_attack": "piston slam", "strong_attack": "hydraulic crush", "player_abilities": ["reinforce_frame"],
 "base_str":14, "base_dex":1, "base_con":18, "base_int":1, "base_hp":300, "base_ap":4,
 "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "harbor_baron", "name": "Harbor Baron", "hostile_type": "humanoid", "role": "support", "min_spawn_level":14, "rarity": "uncommon", "base_xp":300,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (40,200),
 "basic_attack": "golden cane tap", "strong_attack": "commanding strike", "player_abilities": ["inspire"],
 "base_str":5, "base_dex":4, "base_con":6, "base_int":8, "base_hp":120, "base_ap":6,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "rustwork_guard", "name": "Rustwork Guard", "hostile_type": "construct", "role": "support", "min_spawn_level":15, "rarity": "uncommon", "base_xp":220,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (30,120),
 "basic_attack": "clank jab", "strong_attack": "servo bash", "player_abilities": ["reinforce_frame"],
 "base_str":10, "base_dex":3, "base_con":10, "base_int":2, "base_hp":220, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "brine_krakenling", "name": "Brine Krakenling", "hostile_type": "creature", "role": "hazard", "min_spawn_level":15, "rarity": "uncommon", "base_xp":340,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40,180),
 "basic_attack": "tentacle lash", "strong_attack": "ink blight", "player_abilities": ["void_veil"],
 "base_str":9, "base_dex":5, "base_con":9, "base_int":4, "base_hp":200, "base_ap":8,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 {"id": "rustwork_guard_senior", "name": "Rustwork Guard Senior", "hostile_type": "construct", "role": "support", "min_spawn_level":16, "rarity": "uncommon", "base_xp":340,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (60,240),
 "basic_attack": "servo crush", "strong_attack": "hydraulic stomp", "player_abilities": ["reinforce_frame"],
 "base_str":12, "base_dex":3, "base_con":14, "base_int":2, "base_hp":300, "base_ap":6,
 "str_per_level":4, "dex_per_level":1, "con_per_level":3, "int_per_level":0},

 {"id": "lighthouse_keeper", "name": "Lighthouse Keeper", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":16, "rarity": "superrare", "base_xp":520,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,340),
 "basic_attack": "lantern swing", "strong_attack": "blinding flare", "player_abilities": ["prism_burst", "void_veil"],
 "base_str":8, "base_dex":5, "base_con":10, "base_int":8, "base_hp":220, "base_ap":10,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "sea_wright", "name": "Sea Wright", "hostile_type": "humanoid", "role": "support", "min_spawn_level":19, "rarity": "common", "base_xp":480,
 "common_drop": "stimulant_large", "rare_drop": "cloth_gloves", "money_range": (60,260),
 "basic_attack": "forge hammer", "strong_attack": "reef shatter", "player_abilities": ["reinforce_frame"],
 "base_str":9, "base_dex":4, "base_con":12, "base_int":3, "base_hp":300, "base_ap":8,
 "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":1},

 {"id": "deep_harvester", "name": "Deep Harvester", "hostile_type": "creature", "role": "hazard", "min_spawn_level":20, "rarity": "common", "base_xp":560,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (100,420),
 "basic_attack": "harvesting bite", "strong_attack": "abyssal pull", "player_abilities": ["void_veil"],
 "base_str":10, "base_dex":5, "base_con":14, "base_int":6, "base_hp":360, "base_ap":10,
 "str_per_level":4, "dex_per_level":1, "con_per_level":3, "int_per_level":2},
]
