# Level11-20 hostile seeds for Brineward Harbor (mid-city)
# Export a list named SEEDS_LV11TO20 used by constants_enemies_mid_city.py
SEEDS_LV11TO20 = [
 {"id": "harbor_bully", "name": "Harbor Bully", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "uncommon", "base_xp":160,
 "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (30,140),
 "basic_attack": "shoulder bash", "strong_attack": "chain swing", "player_abilities": None,
 "base_str":7, "base_dex":3, "base_con":6, "base_int":2, "base_hp":88, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "salt_vicar", "name": "Salt Vicar", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":11, "rarity": "rare", "base_xp":200,
 "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (18,96),
 "basic_attack": "blight chant", "strong_attack": "corrosive blessing", "player_abilities": ["corrosive_spit", "arcane_blast"],
 "base_str":3, "base_dex":3, "base_con":6, "base_int":9, "base_hp":120, "base_ap":8,
 "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "night_sneak", "name": "Night Sneak", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":13, "rarity": "uncommon", "base_xp":220,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (30,140),
 "basic_attack": "grease strike", "strong_attack": "silent garrote", "player_abilities": ["void_veil"],
 "base_str":3, "base_dex":8, "base_con":4, "base_int":5, "base_hp":92, "base_ap":8,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":2},

 {"id": "abyssal_cuttle", "name": "Abyssal Cuttle", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":14, "rarity": "rare", "base_xp":300,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (40,180),
 "basic_attack": "ink lash", "strong_attack": "mind-bleak pulse", "player_abilities": ["abyssal_storm"],
 "base_str":6, "base_dex":6, "base_con":8, "base_int":8, "base_hp":200, "base_ap":8,
 "str_per_level":2, "dex_per_level":2, "con_per_level":2, "int_per_level":3},

 {"id": "dock_automat", "name": "Dock Automat", "hostile_type": "construct", "role": "support", "min_spawn_level":15, "rarity": "uncommon", "base_xp":340,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (60,260),
 "basic_attack": "piston strike", "strong_attack": "hydraulic crush", "player_abilities": ["reinforce_frame"],
 "base_str":12, "base_dex":2, "base_con":14, "base_int":2, "base_hp":260, "base_ap":6,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "kraken_whelp", "name": "Kraken Whelp", "hostile_type": "creature", "role": "damage", "min_spawn_level":16, "rarity": "rare", "base_xp":340,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (50,220),
 "basic_attack": "tentacle slap", "strong_attack": "ink burst", "player_abilities": ["void_veil"],
 "base_str":8, "base_dex":5, "base_con":9, "base_int":4, "base_hp":220, "base_ap":8,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 {"id": "harbor_lich", "name": "Harbor Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level":17, "rarity": "superrare", "base_xp":520,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,340),
 "basic_attack": "skeletal lash", "strong_attack": "necrotic tide", "player_abilities": ["void_veil", "nightmare_wave"],
 "base_str":6, "base_dex":4, "base_con":10, "base_int":14, "base_hp":320, "base_ap":10,
 "str_per_level":2, "dex_per_level":1, "con_per_level":3, "int_per_level":4},

 {"id": "captain_tide", "name": "Captain Tidefinger", "hostile_type": "humanoid", "role": "support", "min_spawn_level":18, "rarity": "rare", "base_xp":600,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (100,420),
 "basic_attack": "cutlass rip", "strong_attack": "abyssal command", "player_abilities": ["abyssal_storm", "prism_burst"],
 "base_str":9, "base_dex":7, "base_con":9, "base_int":8, "base_hp":360, "base_ap":10,
 "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":2},
]
