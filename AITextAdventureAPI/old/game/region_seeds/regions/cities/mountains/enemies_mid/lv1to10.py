# Level1-10 hostile seeds for Gallows Rift (mid-city)
# Export a list named SEEDS_LV1TO10 used by constants_enemies_mid_city.py
# Organized by min_spawn_level ascending and adjusted rarities for exact dispersity.
SEEDS_LV1TO10 = [
 # min_spawn_level =1 (ensure common, uncommon, rare present)
 {"id": "ridge_runt", "name": "Ridge Runt", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "scampers and nips", "strong_attack": "furious bite", "player_abilities": None,
 "base_str":1, "base_dex":4, "base_con":1, "base_int":1, "base_hp":9, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "bridge_hustler", "name": "Bridge Hustler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":12,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "quick palm", "strong_attack": "purse-swipe", "player_abilities": None,
 "base_str":1, "base_dex":6, "base_con":1, "base_int":2, "base_hp":10, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "dreg_drunk", "name": "Dreg Drunk", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "sloppy hook", "strong_attack": "broken bottle", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":2, "base_int":1, "base_hp":8, "base_ap":1,
 "str_per_level":0, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "hardy_brawler", "name": "Hardy Brawler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "rare", "base_xp":28,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "throws a haymaker", "strong_attack": "spinning strike", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":3, "base_int":1, "base_hp":20, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "pit_custodian", "name": "Pit Custodian", "hostile_type": "humanoid", "role": "support", "min_spawn_level":1, "rarity": "superrare", "base_xp":110,
 "common_drop": "stimulant_med", "rare_drop": "kevlar_vest", "money_range": (18,80),
 "basic_attack": "sweep with pole", "strong_attack": "stun-and-smash", "player_abilities": ["reinforce_frame"],
 "base_str":6, "base_dex":3, "base_con":6, "base_int":2, "base_hp":48, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 # min_spawn_level =2
 {"id": "rift_runt_pick", "name": "Pickpocket Apprentice", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":9,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "nervous jab", "strong_attack": "surprise snatch", "player_abilities": None,
 "base_str":1, "base_dex":5, "base_con":1, "base_int":2, "base_hp":9, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "rift_wolf", "name": "Rift Wolf", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "slashes with teeth", "strong_attack": "pouncing maul", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":1, "base_hp":12, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "rift_cutpurse", "name": "Rift Cutpurse", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":14,
 "common_drop": "lockpick", "rare_drop": "cloth_pants", "money_range": (2,12),
 "basic_attack": "quick slash", "strong_attack": "backstab flourish", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":2, "base_int":2, "base_hp":14, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 # min_spawn_level =3
 {"id": "pub_poet", "name": "Pub Poet", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "common", "base_xp":16,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,10),
 "basic_attack": "snide couplet", "strong_attack": "verse-lash", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":1, "base_int":5, "base_hp":12, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "gallows_brawler", "name": "Gallows Brawler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":30,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (3,16),
 "basic_attack": "club jab", "strong_attack": "spinning haymaker", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":3, "base_int":1, "base_hp":22, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 # min_spawn_level =4
 {"id": "copper_merchant", "name": "Copper Merchant", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":22,
 "common_drop": "herb_minor", "rare_drop": "cloth_pants", "money_range": (3,18),
 "basic_attack": "throws a pamphlet", "strong_attack": "coin barrage", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":4, "base_hp":18, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 # min_spawn_level =5
 {"id": "tarn_tinker", "name": "Tarn Tinker", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":5, "rarity": "uncommon", "base_xp":48,
 "common_drop": "lockpick", "rare_drop": "tome_dex", "money_range": (6,32),
 "basic_attack": "flings a spring", "strong_attack": "overclock jolt", "player_abilities": ["hack_overload"],
 "base_str":2, "base_dex":4, "base_con":3, "base_int":7, "base_hp":30, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "clumsy_tinker_apprentice", "name": "Cumsy Tinker Apprentice", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":5, "rarity": "uncommon", "base_xp":50,
 "common_drop": "lockpick", "rare_drop": "tome_int", "money_range": (10,40),
 "basic_attack": "sprays shrapnel", "strong_attack": "overclock stab", "player_abilities": ["hack_overload"],
 "base_str":2, "base_dex":5, "base_con":3, "base_int":7, "base_hp":32, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":2},

 # min_spawn_level =6
 {"id": "ledger_hound", "name": "Ledger Hound", "hostile_type": "humanoid", "role": "support", "min_spawn_level":6, "rarity": "uncommon", "base_xp":60,
 "common_drop": "stimulant_small", "rare_drop": "lockpick", "money_range": (8,34),
 "basic_attack": "barks a directive", "strong_attack": "ledger bash", "player_abilities": ["reinforce_frame"],
 "base_str":3, "base_dex":3, "base_con":4, "base_int":4, "base_hp":34, "base_ap":4,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":2},

 {"id": "cliff_viper", "name": "Cliff Viper", "hostile_type": "creature", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":48,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (4,30),
 "basic_attack": "venomous bite", "strong_attack": "constricting coil", "player_abilities": ["venom_trace"],
 "base_str":2, "base_dex":6, "base_con":3, "base_int":2, "base_hp":36, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "spire_cultist", "name": "Spire Cultist", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":6, "rarity": "rare", "base_xp":90,
 "common_drop": "herb_major", "rare_drop": "short_sword", "money_range": (10,64),
 "basic_attack": "casts a black mote", "strong_attack": "voiding spear", "player_abilities": ["arcane_blast"],
 "base_str":1, "base_dex":2, "base_con":3, "base_int":7, "base_hp":28, "base_ap":6,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 # min_spawn_level =8
 {"id": "rift_thief_lady", "name": "Lady Rogue", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "rare", "base_xp":110,
 "common_drop": "lockpick", "rare_drop": "pipe_wrench", "money_range": (20,80),
 "basic_attack": "stab", "strong_attack": "lethal dance", "player_abilities": ["precise_strike", "poison_dart"],
 "base_str":3, "base_dex":8, "base_con":3, "base_int":3, "base_hp":30, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # min_spawn_level =9 (superrare)
 {"id": "rift_wraith", "name": "Rift Wraith", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":9, "rarity": "superrare", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (6,44),
 "basic_attack": "ethereal lash", "strong_attack": "soulscream", "player_abilities": ["dark_magic_lv4_mind_shiver"],
 "base_str":1, "base_dex":4, "base_con":2, "base_int":9, "base_hp":44, "base_ap":9,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 # min_spawn_level =10
 {"id": "skew_ripper", "name": "Skew Ripper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":10, "rarity": "rare", "base_xp":140,
 "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (30,120),
 "basic_attack": "precise shot", "strong_attack": "aimed salvo", "player_abilities": ["quick_shot"],
 "base_str":2, "base_dex":7, "base_con":3, "base_int":3, "base_hp":36, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 {"id": "slag_acolyte", "name": "Slag Acolyte", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":10, "rarity": "rare", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (18,88),
 "basic_attack": "slag sputter", "strong_attack": "molten chain", "player_abilities": ["arcane_blast", "corrosive_spit"],
 "base_str":3, "base_dex":3, "base_con":6, "base_int":8, "base_hp":120, "base_ap":8,
 "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":2}
]