# Level11-20 hostile seeds for Bayou Nocturne (mid-city)
# Export a list named SEEDS_LV11TO20 used by constants_enemies_mid_city.py
# Reworked to better reflect the shadowed canals, voodoo mystics, and smuggler gangs of Bayou Nocturne.
SEEDS_LV11TO20 = [
 # Level11
 {"id": "scavenger_net", "name": "Scavenger Net", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":75,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (10,56),
 "basic_attack": "scrap jab", "strong_attack": "rusty swipe", "player_abilities": None,
 "base_str":4, "base_dex":4, "base_con":4, "base_int":1, "base_hp":110, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "fixer_hacker_bay", "name": "Bay Net-Whisperer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":11, "rarity": "uncommon", "base_xp":130,
 "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (40,160),
 "basic_attack": "cybernetic tch", "strong_attack": "powerful jolt", "player_abilities": ["hack_overload", "emp_burst"],
 "base_str":2, "base_dex":4, "base_con":2, "base_int":8, "base_hp":36, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 # Level12
 {"id": "marsh_scav", "name": "Marsh Scavenger", "hostile_type": "creature", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":95,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (14,64),
 "basic_attack": "bite", "strong_attack": "mud swipe", "player_abilities": None,
 "base_str":5, "base_dex":5, "base_con":5, "base_int":1, "base_hp":140, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "mire_hunter", "name": "Mire Hunter", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "uncommon", "base_xp":110,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (18,90),
 "basic_attack": "pike jab", "strong_attack": "net entangle", "player_abilities": None,
 "base_str":6, "base_dex":4, "base_con":6, "base_int":2, "base_hp":160, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 # Level13
 {"id": "board_petty", "name": "Board Petty", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":85,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (12,60),
 "basic_attack": "shank", "strong_attack": "gut twist", "player_abilities": None,
 "base_str":4, "base_dex":5, "base_con":4, "base_int":1, "base_hp":130, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "lich_apprentice_bay", "name": "Dirty Lich Apprentice", "hostile_type": "undead", "role": "hazard", "min_spawn_level":13, "rarity": "rare", "base_xp":320,
 "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (30,140),
 "basic_attack": "bone bolt", "strong_attack": "necrotic spear", "player_abilities": ["bone_spear"],
 "base_str":2, "base_dex":3, "base_con":4, "base_int":12, "base_hp":100, "base_ap":10,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 # Level14
 {"id": "tide_runt", "name": "Tide Runt", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "common", "base_xp":100,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (16,76),
 "basic_attack": "snap", "strong_attack": "tail whip", "player_abilities": None,
 "base_str":4, "base_dex":6, "base_con":4, "base_int":1, "base_hp":140, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "rustling_harrier", "name": "Rustling Harrier", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "uncommon", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (20,88),
 "basic_attack": "claw flurry", "strong_attack": "mire pounce", "player_abilities": None,
 "base_str":6, "base_dex":8, "base_con":6, "base_int":2, "base_hp":160, "base_ap":6,
 "str_per_level":2, "dex_per_level":3, "con_per_level":2, "int_per_level":0},

 # Level15
 {"id": "bilge_marauder", "name": "Bilge Marauder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":140,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (18,90),
 "basic_attack": "club swing", "strong_attack": "crab toss", "player_abilities": None,
 "base_str":6, "base_dex":3, "base_con":6, "base_int":2, "base_hp":180, "base_ap":5,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "nether_hound", "name": "Nether Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":15, "rarity": "uncommon", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (36,140),
 "basic_attack": "lash bite", "strong_attack": "void maul", "player_abilities": None,
 "base_str":7, "base_dex":6, "base_con":8, "base_int":2, "base_hp":200, "base_ap":6,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":0},

 # Level16
 {"id": "bog_wrecker", "name": "Bog Wrecker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":16, "rarity": "rare", "base_xp":152,
 "common_drop": "stimulant_large", "rare_drop": "reinforced_plate", "money_range": (36,140),
 "basic_attack": "mauls with a clubbed stump", "strong_attack": "cataclysmic swamp slam", "player_abilities": None,
 "base_str":9, "base_dex":2, "base_con":7, "base_int":1, "base_hp":92, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "wrecker_johnson_02", "name": "Wrecker Johnson Jr.", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":16, "rarity": "common", "base_xp":80,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (12,60),
 "basic_attack": "haymaker practice", "strong_attack": "mini wrecking ball", "player_abilities": None,
 "base_str":5, "base_dex":2, "base_con":4, "base_int":1, "base_hp":90, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 # Level17
 {"id": "harbinger_woe", "name": "Harbinger of Woe", "hostile_type": "elemental", "role": "hazard", "min_spawn_level":17, "rarity": "rare", "base_xp":340,
 "common_drop": "stimulant_med", "rare_drop": "tome_int", "money_range": (30,140),
 "basic_attack": "ice shard throw", "strong_attack": "freezing blast", "player_abilities": ["frost_nova"],
 "base_str":6, "base_dex":5, "base_con":8, "base_int":7, "base_hp":180, "base_ap":9,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "pier_ruffian", "name": "Pier Ruffian", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (20,100),
 "basic_attack": "piercing jab", "strong_attack": "crab pummel", "player_abilities": None,
 "base_str":6, "base_dex":3, "base_con":5, "base_int":1, "base_hp":140, "base_ap":5,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # Level18
 {"id": "dark_watchman", "name": "Dark Watchman", "hostile_type": "humanoid", "role": "support", "min_spawn_level":18, "rarity": "uncommon", "base_xp":260,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (80,320),
 "basic_attack": "cybernetic precision jab", "strong_attack": "devastating barrage of servo-fists", "player_abilities": ["reinforce_frame", "chain_reactor"],
 "base_str":6, "base_dex":5, "base_con":6, "base_int":4, "base_hp":120, "base_ap":8,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 {"id": "enducated_antique_snatcher", "name": "Educated Antique Snatcher", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":18, "rarity": "rare", "base_xp":92,
 "common_drop": "stimulant_med", "rare_drop": "herb_major", "money_range": (24,100),
 "basic_attack": "stab with a crooked spatula", "strong_attack": "crippling antiquity swing", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":2, "base_int":3, "base_hp":28, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # Level19
 {"id": "black_market_crook", "name": "Black Market Cat", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":19, "rarity": "common", "base_xp":200,
 "common_drop": "stimulant_large", "rare_drop": "stimulant_large", "money_range": (60,260),
 "basic_attack": "slap with a velvet paw", "strong_attack": "critical contraband shot", "player_abilities": ["primal_unison", "nether_cataclysm"],
 "base_str":3, "base_dex":4, "base_con":3, "base_int":6, "base_hp":48, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "rogue_mistress_bay", "name": "Rogue Mistress", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":19, "rarity": "uncommon", "base_xp":220,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (60,240),
 "basic_attack": "shadowed riposte", "strong_attack": "deadly silk rip", "player_abilities": ["poison_dart"],
 "base_str":5, "base_dex":9, "base_con":4, "base_int":6, "base_hp":90, "base_ap":9,
 "str_per_level":2, "dex_per_level":4, "con_per_level":1, "int_per_level":3},

 # Level20 - boss-tier
 {"id": "mob_lieutenant_bay", "name": "Bay Lieutenant", "hostile_type": "humanoid", "role": "support", "min_spawn_level":20, "rarity": "superrare", "base_xp":400,
 "common_drop": "herb_major", "rare_drop": "nano_suit", "money_range": (150,600),
 "basic_attack": "ruthless cane strikes", "strong_attack": "mobster beatdown of legend", "player_abilities": ["inspire", "berserker_tech"],
 "base_str":9, "base_dex":5, "base_con":8, "base_int":5, "base_hp":200, "base_ap":10,
 "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":2},
]
