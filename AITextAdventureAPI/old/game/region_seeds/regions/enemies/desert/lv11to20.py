# LEVEL11-20 hostile regional (to be imported by higher-level modules).
# Seeds for desert region, levels11-20 — balanced dispersity and sorted by min_spawn_level.
SEEDS_LV11TO20 = [
 {"id": "sand_watch", "name": "Sand Watch", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":72,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,44),
 "basic_attack": "sandy jab", "strong_attack": "reeling shove", "player_abilities": None,
 "base_str":3, "base_dex":5, "base_con":3, "base_int":2, "base_hp":54, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "dune_pioneer", "name": "Dune Pioneer", "hostile_type": "humanoid", "role": "support", "min_spawn_level":11, "rarity": "uncommon", "base_xp":110,
 "common_drop": "stimulant_small", "rare_drop": "cloth_gloves", "money_range": (12,60),
 "basic_attack": "foundry swing", "strong_attack": "anvil crush", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":6, "base_dex":4, "base_con":6, "base_int":3, "base_hp":90, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "sand_slinger", "name": "Sand Slinger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":68,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (6,36),
 "basic_attack": "hook toss", "strong_attack": "barrel slam", "player_abilities": None,
 "base_str":4, "base_dex":4, "base_con":3, "base_int":2, "base_hp":64, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "sand_harrier", "name": "Sand Harrier", "hostile_type": "creature", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":78,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,48),
 "basic_attack": "lunge bite", "strong_attack": "mire pounce", "player_abilities": None,
 "base_str":4, "base_dex":6, "base_con":4, "base_int":2, "base_hp":72, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "sand_skiff", "name": "Sand Skiff", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":12, "rarity": "uncommon", "base_xp":120,
 "common_drop": "stimulant_small", "rare_drop": "stimulant_large", "money_range": (14,72),
 "basic_attack": "pipe jab", "strong_attack": "oil slick", "player_abilities": ["level_1_hostile_ability_electric_tech_hack_overload"],
 "base_str":4, "base_dex":5, "base_con":4, "base_int":5, "base_hp":80, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "sand_hydra", "name": "Sand Hydra", "hostile_type": "creature", "role": "damage", "min_spawn_level":12, "rarity": "rare", "base_xp":420,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (60,260),
 "basic_attack": "multi-bite", "strong_attack": "barbed barrage", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":12, "base_dex":10, "base_con":12, "base_int":8, "base_hp":520, "base_ap":10,
 "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 {"id": "cactus_stalker", "name": "Cactus Stalker", "hostile_type": "creature", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":92,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (10,56),
 "basic_attack": "snap bite", "strong_attack": "coil and strike", "player_abilities": None,
 "base_str":5, "base_dex":6, "base_con":4, "base_int":2, "base_hp":88, "base_ap":4,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "mire_huckster", "name": "Mire Huckster", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":13, "rarity": "uncommon", "base_xp":100,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (12,64),
 "basic_attack": "flailing bargain", "strong_attack": "smuggled strike", "player_abilities": None,
 "base_str":3, "base_dex":5, "base_con":3, "base_int":4, "base_hp":76, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "sand_elder_tendril", "name": "Sand Elder Tendril", "hostile_type": "eldritch", "role": "damage", "min_spawn_level":13, "rarity": "rare", "base_xp":200,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (18,100), "basic_attack": "whip of barbs", "strong_attack": "barbed crush", "player_abilities": None,
 "base_str":12, "base_dex":2, "base_con":10, "base_int":2, "base_hp":160, "base_ap":4,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "rotgill", "name": "Rotgill", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "common", "base_xp":100,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (14,70),
 "basic_attack": "gill snap", "strong_attack": "mire thrash", "player_abilities": None,
 "base_str":6, "base_dex":5, "base_con":6, "base_int":1, "base_hp":98, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "leechcatcher", "name": "Leechcatcher", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":14, "rarity": "common", "base_xp":110,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (12,64),
 "basic_attack": "net jab", "strong_attack": "toxic bait", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":3, "base_dex":6, "base_con":3, "base_int":4, "base_hp":84, "base_ap":6,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "baby_snatcher", "name": "Baby Snatcher", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":14, "rarity": "rare", "base_xp":92,
 "common_drop": "stimulant_med", "rare_drop": "herb_major", "money_range": (20,96),
 "basic_attack": "stabs with a crooked trinket", "strong_attack": "antique uppercut", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":2, "base_int":3, "base_hp":68, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "crab_dealer", "name": "Crab Dealer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":15, "rarity": "uncommon", "base_xp":140,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (18,90), "basic_attack": "pocket change", "strong_attack": "crab toss", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":6, "base_dex":3, "base_con":6, "base_int":2, "base_hp":180, "base_ap":5,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "open_net_slicer", "name": "Open Net Slicer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":15, "rarity": "uncommon", "base_xp":150,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (20,100), "basic_attack": "reap with net", "strong_attack": "entangling slash", "player_abilities": None,
 "base_str":5, "base_dex":6, "base_con":4, "base_int":3, "base_hp":84, "base_ap":6,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "mind_nibbler4", "name": "Mind Nibbler", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":15, "rarity": "rare", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,220), "basic_attack": "psychic tickle", "strong_attack": "brain buffet", "player_abilities": ["dark_magic_lv5_abyssal_shadow"],
 "base_str":2, "base_dex":3, "base_con":3, "base_int":14, "base_hp":80, "base_ap":12,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":4},

 {"id": "bog_hunter", "name": "Bog Hunter", "hostile_type": "creature", "role": "damage", "min_spawn_level":16, "rarity": "common", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (30,140), "basic_attack": "rending swipe", "strong_attack": "maul and drag", "player_abilities": None,
 "base_str":8, "base_dex":6, "base_con":8, "base_int":2, "base_hp":220, "base_ap":6, "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":0},

 {"id": "mire_brute", "name": "Mire Brute", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":180,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (36,160), "basic_attack": "bone-crusher", "strong_attack": "stomp of rot", "player_abilities": None,
 "base_str":10, "base_dex":3, "base_con":9, "base_int":1, "base_hp":240, "base_ap":5, "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "hopeless_boardling_scout", "name": "Hopeless Boardling Scout", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":18, "rarity": "uncommon", "base_xp":200,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (40,180), "basic_attack": "board jab", "strong_attack": "plank volley", "player_abilities": None,
 "base_str":5, "base_dex":7, "base_con":5, "base_int":3, "base_hp":160, "base_ap":6, "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "desert_archmage", "name": "Desert Archmage", "hostile_type": "magic", "role": "hazard", "min_spawn_level":19, "rarity": "superrare", "base_xp":1100, "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (160,640),
 "basic_attack": "arcane flick", "strong_attack": "meteor shard", "player_abilities": ["electric_fire_magic_lv2_arclance", "lv2_hostile_ability_earth_light_tech_primal_disunion"], "base_str":8, "base_dex":8, "base_con":10, "base_int":20, "base_hp":980, "base_ap":14, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":4},

 {"id": "bone_revenant", "name": "Bone Revenant", "hostile_type": "undead", "role": "hazard", "min_spawn_level":20, "rarity": "superrare", "base_xp":1280, "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (180,720),
 "basic_attack": "ichor swipe", "strong_attack": "necrotic gale", "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "level_1_hostile_ability_night_whisper"], "base_str":14, "base_dex":10, "base_con":14, "base_int":12, "base_hp":1400, "base_ap":12, "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":3},
]