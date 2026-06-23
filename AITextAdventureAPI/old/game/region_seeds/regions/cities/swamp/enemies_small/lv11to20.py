# Level11-20 hostile seeds for small swamp city (Gnashwater Hollow)
# Export a list named SEEDS_LV11TO20 used by constants_enemies_small_city.py
SEEDS_LV11TO20 = [
 {"id": "bayou_scout", "name": "Bayou Scout", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":60,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (6,40),
 "basic_attack": "stabbing reed", "strong_attack": "sweeping harry", "player_abilities": None,
 "base_str":3, "base_dex":6, "base_con":3, "base_int":2, "base_hp":48, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "scrap_rigger", "name": "Scrap Rigger", "hostile_type": "humanoid", "role": "support", "min_spawn_level":11, "rarity": "uncommon", "base_xp":110,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (12,60),
 "basic_attack": "wrench jab", "strong_attack": "shard toss", "player_abilities": ["reinforce_frame"],
 "base_str":4, "base_dex":4, "base_con":4, "base_int":3, "base_hp":64, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 {"id": "net_whisperer", "name": "Net Whisperer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":11, "rarity": "rare", "base_xp":130,
 "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (36,160),
 "basic_attack": "taps with a data-squid", "strong_attack": "jolt of rusted circuitry", "player_abilities": ["hack_overload", "emp_burst"],
 "base_str":2, "base_dex":4, "base_con":2, "base_int":8, "base_hp":36, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "leek_stalker", "name": "Leek Stalker", "hostile_type": "creature", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":70,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,48),
 "basic_attack": "snap bite", "strong_attack": "coil and strike", "player_abilities": None,
 "base_str":4, "base_dex":5, "base_con":4, "base_int":2, "base_hp":60, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "sump_tinker", "name": "Sump Tinker", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":12, "rarity": "uncommon", "base_xp":120,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (14,72),
 "basic_attack": "pipe jab", "strong_attack": "oil slick", "player_abilities": ["emp_burst"],
 "base_str":3, "base_dex":5, "base_con":3, "base_int":6, "base_hp":48, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "young_lich_apprentice", "name": "Young Lich Apprentice", "hostile_type": "undead", "role": "hazard", "min_spawn_level":12, "rarity": "rare", "base_xp":320,
 "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (30,140), "basic_attack": "bone bolt", "strong_attack": "necrotic spear", "player_abilities": ["bone_spear"],
 "base_str":2, "base_dex":3, "base_con":4, "base_int":12, "base_hp":100, "base_ap":10,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "bog_runner", "name": "Bog Runner", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (10,56),
 "basic_attack": "slash and dash", "strong_attack": "spike trip", "player_abilities": None,
 "base_str":5, "base_dex":6, "base_con":4, "base_int":2, "base_hp":72, "base_ap":5,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "canal_huckster", "name": "Canal Huckster", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":13, "rarity": "uncommon", "base_xp":100,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (12,64),
 "basic_attack": "flailing bargain", "strong_attack": "smuggled strike", "player_abilities": None,
 "base_str":3, "base_dex":5, "base_con":3, "base_int":4, "base_hp":54, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "bog_elder_tendril", "name": "Bog Elder Tendril", "hostile_type": "eldritch", "role": "damage", "min_spawn_level":13, "rarity": "rare", "base_xp":200,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (18,100), "basic_attack": "whip of barbs", "strong_attack": "barbed crush", "player_abilities": None,
 "base_str":12, "base_dex":2, "base_con":10, "base_int":2, "base_hp":160, "base_ap":4,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "mudgill", "name": "Mudgill", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "common", "base_xp":100,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (14,70),
 "basic_attack": "gill snap", "strong_attack": "mire thrash", "player_abilities": None,
 "base_str":6, "base_dex":5, "base_con":6, "base_int":1, "base_hp":88, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "ratcatcher", "name": "Ratcatcher", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":14, "rarity": "uncommon", "base_xp":110,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (12,64),
 "basic_attack": "net jab", "strong_attack": "toxic bait", "player_abilities": ["venom_trace"],
 "base_str":3, "base_dex":6, "base_con":3, "base_int":4, "base_hp":60, "base_ap":6,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "perilous_snatcher", "name": "Perilous Snatcher", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":14, "rarity": "rare", "base_xp":92,
 "common_drop": "stimulant_med", "rare_drop": "herb_major", "money_range": (20,96),
 "basic_attack": "stabs with a crooked trinket", "strong_attack": "antique uppercut", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":2, "base_int":3, "base_hp":28, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "vile_marauder", "name": "Vile Marauder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":140,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (18,90), "basic_attack": "club swing", "strong_attack": "crab toss", "player_abilities": None,
 "base_str":6, "base_dex":3, "base_con":6, "base_int":2, "base_hp":180, "base_ap":5,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "net_slicer", "name": "Net Slicer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":15, "rarity": "uncommon", "base_xp":150,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (20,100), "basic_attack": "reap with net", "strong_attack": "entangling slash", "player_abilities": None,
 "base_str":5, "base_dex":6, "base_con":4, "base_int":3, "base_hp":84, "base_ap":6,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "mind_nibbler3", "name": "Mind Nibbler", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":15, "rarity": "rare", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,220), "basic_attack": "psychic tickle", "strong_attack": "brain buffet", "player_abilities": ["dark_magic_lv5_abyssal_shadow"],
 "base_str":2, "base_dex":3, "base_con":3, "base_int":14, "base_hp":80, "base_ap":12,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":4},

 {"id": "swamp_hunter", "name": "Swamp Hunter", "hostile_type": "creature", "role": "damage", "min_spawn_level":16, "rarity": "common", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (30,140), "basic_attack": "rending swipe", "strong_attack": "maul and drag", "player_abilities": None,
 "base_str":8, "base_dex":6, "base_con":8, "base_int":2, "base_hp":220, "base_ap":6, "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":0},

 {"id": "marsh_brute", "name": "Marsh Brute", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":180,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (36,160), "basic_attack": "bone-crusher", "strong_attack": "stomp of rot", "player_abilities": None,
 "base_str":10, "base_dex":3, "base_con":9, "base_int":1, "base_hp":240, "base_ap":5, "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "boardling_scout", "name": "Boardling Scout", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":18, "rarity": "common", "base_xp":200,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (40,180), "basic_attack": "board jab", "strong_attack": "plank volley", "player_abilities": None,
 "base_str":5, "base_dex":7, "base_con":5, "base_int":3, "base_hp":160, "base_ap":6, "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "mob_lieutenant", "name": "Hollow Lieutenant", "hostile_type": "humanoid", "role": "support", "min_spawn_level":20, "rarity": "superrare", "base_xp":400,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (150,600), "basic_attack": "ruthless cane strikes", "strong_attack": "legendary beatdown", "player_abilities": ["inspire", "berserker_tech"],
 "base_str":9, "base_dex":5, "base_con":8, "base_int":5, "base_hp":200, "base_ap":10, "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":2},
]
