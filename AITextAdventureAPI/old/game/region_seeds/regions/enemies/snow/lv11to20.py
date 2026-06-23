# LEVEL11-20 hostile regional seeds for snow region (to be imported by higher-level modules).
# Export a list named SEEDS_LV11TO20
SEEDS_LV11TO20 = [
 {"id": "icepick_bandit", "name": "Icepick Bandit", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":80, "common_drop": "stimulant_small", "rare_drop": None, "money_range": (8,40),
 "basic_attack": "dagger jab", "strong_attack": "ice slice", "player_abilities": [], "base_str":6, "base_dex":6, "base_con":4, "base_int":2, "base_hp":110, "base_ap":5, "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "waste_baron", "name": "Waste Baron", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "uncommon", "base_xp":160, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (40,160),
 "basic_attack": "wealthy swipe", "strong_attack": "opulent crush", "player_abilities": [], "base_str":8, "base_dex":5, "base_con":8, "base_int":8, "base_hp":220, "base_ap":10, "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "glacial_grazer", "name": "Glacial Grazer", "hostile_type": "creature", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":90, "common_drop": "herb_med", "rare_drop": None, "money_range": (10,56),
 "basic_attack": "horn gore", "strong_attack": "frost butt", "player_abilities": [], "base_str":8, "base_dex":4, "base_con":8, "base_int":2, "base_hp":140, "base_ap":6, "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "glacier_rigger", "name": "Glacier Rigger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "uncommon", "base_xp":140, "common_drop": "herb_med", "rare_drop": None, "money_range": (14,72),
 "basic_attack": "hook swipe", "strong_attack": "ice cleave", "player_abilities": [], "base_str":7, "base_dex":4, "base_con":7, "base_int":3, "base_hp":160, "base_ap":6, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "snowbinder_hound", "name": "Snowbinder Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":110, "common_drop": "herb_med", "rare_drop": None, "money_range": (12,64),
 "basic_attack": "lash bite", "strong_attack": "chill maul", "player_abilities": [], "base_str":7, "base_dex":8, "base_con":6, "base_int":2, "base_hp":130, "base_ap":6, "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "neon_fog_cultist", "name": "Neon Fog Cultist", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":13, "rarity": "superrare", "base_xp":180, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (20,100),
 "basic_attack": "cult brand", "strong_attack": "soul lash", "player_abilities": ["dark_magic_lv5_abyssal_shadow"], "base_str":6, "base_dex":5, "base_con":6, "base_int":12, "base_hp":200, "base_ap":12, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":3},

 {"id": "ice_drake_wyrmling", "name": "Ice Drake Wyrmling", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "rare", "base_xp":140, "common_drop": "herb_med", "rare_drop": None, "money_range": (16,80),
 "basic_attack": "bite", "strong_attack": "frost breath", "player_abilities": [], "base_str":9, "base_dex":6, "base_con":8, "base_int":4, "base_hp":180, "base_ap":6, "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 {"id": "polar_wraith", "name": "Polar Wraith", "hostile_type": "undead", "role": "hazard", "min_spawn_level":14, "rarity": "rare", "base_xp":420, "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (40,220),
 "basic_attack": "icy touch", "strong_attack": "wailing gale", "player_abilities": [], "base_str":6, "base_dex":6, "base_con":8, "base_int":10, "base_hp":260, "base_ap":10, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":3},

 {"id": "shiver_ruffian", "name": "Shiver Ruffian", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":160, "common_drop": "stimulant_small", "rare_drop": None, "money_range": (18,90),
 "basic_attack": "palm strike", "strong_attack": "frosty flurry", "player_abilities": [], "base_str":8, "base_dex":5, "base_con":6, "base_int":3, "base_hp":180, "base_ap":6, "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "pilfering_pelt", "name": "Pilfering Pelt", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":15, "rarity": "uncommon", "base_xp":150, "common_drop": "lockpick", "rare_drop": None, "money_range": (18,90),
 "basic_attack": "sneak stab", "strong_attack": "fisher's swipe", "player_abilities": [], "base_str":6, "base_dex":8, "base_con":6, "base_int":4, "base_hp":140, "base_ap":6, "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "frozen_ox", "name": "Frozen Ox", "hostile_type": "creature", "role": "damage", "min_spawn_level":16, "rarity": "common", "base_xp":200, "common_drop": "herb_major", "rare_drop": None, "money_range": (30,140),
 "basic_attack": "ram", "strong_attack": "frozen stomp", "player_abilities": [], "base_str":12, "base_dex":3, "base_con":12, "base_int":2, "base_hp":300, "base_ap":8, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "shardback_troll", "name": "Shardback Troll", "hostile_type": "creature", "role": "damage", "min_spawn_level":16, "rarity": "rare", "base_xp":580, "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (90,360),
 "basic_attack": "club swipe", "strong_attack": "spine rupture", "player_abilities": [], "base_str":14, "base_dex":3, "base_con":14, "base_int":2, "base_hp":420, "base_ap":8, "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "frost_harrier", "name": "Frost Harrier", "hostile_type": "creature", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":240, "common_drop": "herb_major", "rare_drop": None, "money_range": (40,180),
 "basic_attack": "talon slash", "strong_attack": "freezing dive", "player_abilities": [], "base_str":10, "base_dex":10, "base_con":8, "base_int":4, "base_hp":320, "base_ap":10, "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "north_station_guard", "name": "North Station Guard", "hostile_type": "humanoid", "role": "support", "min_spawn_level":17, "rarity": "uncommon", "base_xp":300, "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (60,240),
 "basic_attack": "guard strike", "strong_attack": "riot baton", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"], "base_str":10, "base_dex":6, "base_con":12, "base_int":6, "base_hp":560, "base_ap":10, "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":1},

 {"id": "ice_spiderling", "name": "Ice Spiderling", "hostile_type": "creature", "role": "hazard", "min_spawn_level":18, "rarity": "common", "base_xp":220, "common_drop": "herb_med", "rare_drop": None, "money_range": (36,160),
 "basic_attack": "venom nip", "strong_attack": "web bind", "player_abilities": [], "base_str":8, "base_dex":8, "base_con":6, "base_int":2, "base_hp":300, "base_ap":8, "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":0},

 {"id": "glacial_hulk", "name": "Glacial Hulk", "hostile_type": "creature", "role": "damage", "min_spawn_level":18, "rarity": "rare", "base_xp":420, "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (70,300),
 "basic_attack": "colossal slam", "strong_attack": "glacial maul", "player_abilities": [], "base_str":12, "base_dex":2, "base_con":12, "base_int":2, "base_hp":360, "base_ap":6, "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "snow_warg", "name": "Snow Warg", "hostile_type": "creature", "role": "damage", "min_spawn_level":19, "rarity": "common", "base_xp":300, "common_drop": "stimulant_large", "rare_drop": None, "money_range": (50,200),
 "basic_attack": "rending swipe", "strong_attack": "frost maul", "player_abilities": [], "base_str":12, "base_dex":8, "base_con":10, "base_int":3, "base_hp":420, "base_ap":10, "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":0},

 {"id": "frost_marshal", "name": "Frost Marshal", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":19, "rarity": "uncommon", "base_xp":360, "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (60,240),
 "basic_attack": "command jab", "strong_attack": "ordered volley", "player_abilities": [], "base_str":12, "base_dex":6, "base_con":12, "base_int":8, "base_hp":480, "base_ap":10, "str_per_level":4, "dex_per_level":1, "con_per_level":3, "int_per_level":2},

 {"id": "glacial_hatchling", "name": "Glacial Hatchling", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":20, "rarity": "rare", "base_xp":640, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (100,400),
 "basic_attack": "shadow nip", "strong_attack": "void bite", "player_abilities": ["earth_dark_skill_lv5_venom_trace"], "base_str":8, "base_dex":8, "base_con":8, "base_int":10, "base_hp":480, "base_ap":10, "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":3},

 {"id": "polar_paladin", "name": "Polar Paladin", "hostile_type": "celestial", "role": "support", "min_spawn_level":20, "rarity": "superrare", "base_xp":1000, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (160,640),
 "basic_attack": "radiant lance", "strong_attack": "celestial volley", "player_abilities": ["light_air_earth_water_faith_lv4_starfall"], "base_str":14, "base_dex":8, "base_con":12, "base_int":14, "base_hp":800, "base_ap":14, "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":3},
]