# Level11-20 hostile seeds for Ironveil Foundry (large city)
# Rebalanced for rarity dispersity and ordered by min_spawn_level

RANDOM_HOSTILE_SEEDS = [
 # level11
 {"id": "rumor_spreader", "name": "Rumor Spreader", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":11, "rarity": "common", "base_xp":60,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (4,18),
 "basic_attack": "clamorous whisper", "strong_attack": "panic incite", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":2, "base_int":5, "base_hp":30, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "broker_braggart", "name": "Broker Braggart", "hostile_type": "humanoid", "role": "support", "min_spawn_level":11, "rarity": "uncommon", "base_xp":110,
 "common_drop": "stimulant_med", "rare_drop": "cloth_pants", "money_range": (10,60),
 "basic_attack": "throws a ledger", "strong_attack": "accounting strike", "player_abilities": ["reinforce_frame"],
 "base_str":3, "base_dex":3, "base_con":4, "base_int":6, "base_hp":46, "base_ap":5,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":2},

 # level12
 {"id": "coal_rat_large", "name": "Coal Rat (grown)", "hostile_type": "creature", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":64,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "nips at your boots", "strong_attack": "rabid bite", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":3, "base_int":1, "base_hp":34, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "fixer", "name": "The Fixer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":12, "rarity": "uncommon", "base_xp":120,
 "common_drop": "lockpick", "rare_drop": "tome_dex", "money_range": (12,72),
 "basic_attack": "hacking charge", "strong_attack": "system overload", "player_abilities": ["fire_water_tech_lv2_steam_grenade"],
 "base_str":2, "base_dex":4, "base_con":3, "base_int":7, "base_hp":44, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 # level13
 {"id": "wrecker_small", "name": "Wrecker (farmhand)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":70,
 "common_drop": "herb_major", "rare_drop": "sawed_off", "money_range": (10,70),
 "basic_attack": "haymaker", "strong_attack": "wrecking slam", "player_abilities": None,
 "base_str":6, "base_dex":2, "base_con":5, "base_int":1, "base_hp":70, "base_ap":5,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "dream_moth_small", "name": "Dream Moth", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":13, "rarity": "uncommon", "base_xp":140,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (20,120),
 "basic_attack": "maddening flutter", "strong_attack": "dream stab", "player_abilities": ["dark_magic_lv4_nightmare_echo"],
 "base_str":3, "base_dex":6, "base_con":4, "base_int":14, "base_hp":80, "base_ap":8,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":3},

 # level14
 {"id": "clockwork_mill", "name": "Clockwork Mill-guard", "hostile_type": "construct", "role": "support", "min_spawn_level":14, "rarity": "common", "base_xp":88,
 "common_drop": "stimulant_small", "rare_drop": "kevlar_vest", "money_range": (20,100),
 "basic_attack": "cog swing", "strong_attack": "hydraulic crush", "player_abilities": ["air_earth_technique_lv4_whirlwind"],
 "base_str":6, "base_dex":2, "base_con":8, "base_int":1, "base_hp":96, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "steam_collosus", "name": "Steam Collosus", "hostile_type": "construct", "role": "damage", "min_spawn_level":14, "rarity": "uncommon", "base_xp":140,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (40,180),
 "basic_attack": "piston slam", "strong_attack": "hydraulic stomp", "player_abilities": ["air_earth_technique_lv4_whirlwind"],
 "base_str":10, "base_dex":2, "base_con":12, "base_int":1, "base_hp":160, "base_ap":4,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # level15
 {"id": "black_market_dealer", "name": "Black Market Dealer", "hostile_type": "humanoid", "role": "support", "min_spawn_level":15, "rarity": "common", "base_xp":96,
 "common_drop": "stimulant_large", "rare_drop": "stimulant_large", "money_range": (40,180),
 "basic_attack": "slick trade", "strong_attack": "underhand strike", "player_abilities": ["primal_unison"],
 "base_str":3, "base_dex":4, "base_con":3, "base_int":6, "base_hp":56, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "dream_eater5", "name": "Dream Eater", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":15, "rarity": "uncommon", "base_xp":220,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (50,220),
 "basic_attack": "mind gnaw", "strong_attack": "maddening shriek", "player_abilities": ["nightmare_wave"],
 "base_str":3, "base_dex":6, "base_con":5, "base_int":14, "base_hp":120, "base_ap":10,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":3},

 # level16
 {"id": "rivet_fiend", "name": "Rivet Fiend", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":16, "rarity": "common", "base_xp":104,
 "common_drop": "herb_major", "rare_drop": "sawed_off", "money_range": (30,140),
 "basic_attack": "crashes with pipe", "strong_attack": "wrecking chain", "player_abilities": None,
 "base_str":6, "base_dex":3, "base_con":8, "base_int":1, "base_hp":110, "base_ap":5,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "fixer_hacker", "name": "Fixer Hacker", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":16, "rarity": "uncommon", "base_xp":160,
 "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (40,160),
 "basic_attack": "cybernetic punch", "strong_attack": "powerful jolt", "player_abilities": ["fire_water_tech_lv2_steam_grenade", "emp_burst"],
 "base_str":3, "base_dex":4, "base_con":3, "base_int":10, "base_hp":80, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 # level17
 {"id": "slag_golem", "name": "Slag Golem", "hostile_type": "construct", "role": "damage", "min_spawn_level":17, "rarity": "rare", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (60,240),
 "basic_attack": "slag swipe", "strong_attack": "vulcan crush", "player_abilities": None,
 "base_str":10, "base_dex":3, "base_con":10, "base_int":2, "base_hp":220, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "baroness_guard", "name": "Baroness' Guard", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":140,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (50,200),
 "basic_attack": "elegance", "strong_attack": "nobility", "player_abilities": None,
 "base_str":6, "base_dex":4, "base_con":6, "base_int":3, "base_hp":140, "base_ap":6,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 # level18
 {"id": "magma_serpent", "name": "Magma Serpent", "hostile_type": "creature", "role": "damage", "min_spawn_level":18, "rarity": "rare", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (60,260),
 "basic_attack": "scalding snap", "strong_attack": "molten constrict", "player_abilities": ["abyssal_storm"],
 "base_str":9, "base_dex":6, "base_con":8, "base_int":3, "base_hp":180, "base_ap":6,
 "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "cybernet_guard", "name": "Cybernet Guard", "hostile_type": "humanoid", "role": "support", "min_spawn_level":18, "rarity": "common", "base_xp":120,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (40,160),
 "basic_attack": "cybernetic precision", "strong_attack": "devastating barrage", "player_abilities": ["air_earth_technique_lv4_whirlwind"],
 "base_str":5, "base_dex":4, "base_con":6, "base_int":3, "base_hp":120, "base_ap":6,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 # level19
 {"id": "steam_colossus_guard", "name": "Steam Colossus Guard", "hostile_type": "construct", "role": "support", "min_spawn_level":19, "rarity": "rare", "base_xp":320,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (80,320),
 "basic_attack": "piston slam", "strong_attack": "hydraulic stomp", "player_abilities": ["reinforce_frame"],
 "base_str":14, "base_dex":2, "base_con":16, "base_int":1, "base_hp":260, "base_ap":4,
 "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 # level20 (rare + superrare)
 {"id": "sunder_priest", "name": "Sunder Priest", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":20, "rarity": "rare", "base_xp":600,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (120,420),
 "basic_attack": "searing invocation", "strong_attack": "forge purge", "player_abilities": ["void_veil", "nightmare_wave"],
 "base_str":6, "base_dex":5, "base_con":8, "base_int":12, "base_hp":300, "base_ap":10,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":4},

 {"id": "iron_warden", "name": "Iron Warden", "hostile_type": "construct", "role": "support", "min_spawn_level":20, "rarity": "superrare", "base_xp":720,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (160,640),
 "basic_attack": "forged strike", "strong_attack": "anvil crash", "player_abilities": ["reinforce_frame", "berserker_tech"],
 "base_str":16, "base_dex":4, "base_con":18, "base_int":4, "base_hp":360, "base_ap":10,
 "str_per_level":4, "dex_per_level":1, "con_per_level":3, "int_per_level":1},
]
