# Level11-20 hostile seeds for Tidekin Cove (small-city)
# Export a list named SEEDS_LV11TO20 used by constants_enemies_small_city.py
SEEDS_LV11TO20 = [
 {"id": "dockhand_apprentice", "name": "Dockhand Apprentice", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":80,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (6,36),
 "basic_attack": "crate shove", "strong_attack": "oar bash", "player_abilities": None,
 "base_str":3, "base_dex":3, "base_con":4, "base_int":1, "base_hp":72, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "harbor_brawler", "name": "Harbor Brawler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "uncommon", "base_xp":180,
 "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (24,120),
 "basic_attack": "shoulder charge", "strong_attack": "chain slam", "player_abilities": None,
 "base_str":7, "base_dex":3, "base_con":6, "base_int":2, "base_hp":88, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "slick_buoy", "name": "Slick Buoy", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":96,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (8,44),
 "basic_attack": "sabotage swipe", "strong_attack": "tripline kick", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":3, "base_int":2, "base_hp":80, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "grease_snare", "name": "Grease Snare", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":12, "rarity": "uncommon", "base_xp":180,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (24,120),
 "basic_attack": "greasy swipe", "strong_attack": "silent choke", "player_abilities": ["void_veil"],
 "base_str":3, "base_dex":8, "base_con":4, "base_int":6, "base_hp":92, "base_ap":7,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":2},

 {"id": "bay_scavenger", "name": "Bay Scavenger", "hostile_type": "creature", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (12,60),
 "basic_attack": "scavenge nip", "strong_attack": "bone rattle", "player_abilities": None,
 "base_str":4, "base_dex":5, "base_con":4, "base_int":1, "base_hp":110, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "tin_watchman", "name": "Tin Watchman", "hostile_type": "construct", "role": "support", "min_spawn_level":13, "rarity": "uncommon", "base_xp":220,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (40,180),
 "basic_attack": "piston jab", "strong_attack": "hydraulic crush", "player_abilities": ["reinforce_frame"],
 "base_str":10, "base_dex":2, "base_con":12, "base_int":2, "base_hp":200, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "scrap_crabber", "name": "Scrap Crabber", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "rare", "base_xp":260,
 "common_drop": "herb_major", "rare_drop": "frost_shins", "money_range": (30,140),
 "basic_attack": "rusty pincer", "strong_attack": "armor crush", "player_abilities": None,
 "base_str":6, "base_dex":4, "base_con":8, "base_int":1, "base_hp":160, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "rusted_skiff", "name": "Rusted Skiff", "hostile_type": "construct", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":180,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (12,60),
 "basic_attack": "oar jab", "strong_attack": "keel slam", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":6, "base_int":1, "base_hp":140, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "keeper_knell", "name": "Keeper Knell", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":16, "rarity": "superrare", "base_xp":480,
 "common_drop": "stimulant_large", "rare_drop": "gale_gauntlets", "money_range": (80,320),
 "basic_attack": "lantern bludgeon", "strong_attack": "blinding cataclysm", "player_abilities": ["prism_burst", "void_veil"],
 "base_str":8, "base_dex":5, "base_con":10, "base_int":8, "base_hp":260, "base_ap":10,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "harbor_shade", "name": "Harbor Shade", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":17, "rarity": "rare", "base_xp":320,
 "common_drop": "herb_major", "rare_drop": "stimulant_large", "money_range": (40,180),
 "basic_attack": "gloom swipe", "strong_attack": "ethereal maul", "player_abilities": ["shadow_flicker"],
 "base_str":4, "base_dex":7, "base_con":6, "base_int":6, "base_hp":200, "base_ap":7,
 "str_per_level":1, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "brine_warden", "name": "Brine Warden", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":18, "rarity": "rare", "base_xp":560,
 "common_drop": "stimulant_large", "rare_drop": "spectral_hauberk", "money_range": (100,420),
 "basic_attack": "soul-surge claw", "strong_attack": "abyssal command", "player_abilities": ["nightmare_wave", "abyssal_storm"],
 "base_str":10, "base_dex":6, "base_con":10, "base_int":10, "base_hp":360, "base_ap":12,
 "str_per_level":4, "dex_per_level":1, "con_per_level":3, "int_per_level":3},

 {"id": "sea_tramp", "name": "Sea Tramp", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":19, "rarity": "common", "base_xp":200,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (20,100),
 "basic_attack": "scrap swipe", "strong_attack": "tattered lunge", "player_abilities": None,
 "base_str":5, "base_dex":4, "base_con":6, "base_int":1, "base_hp":180, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},
]
