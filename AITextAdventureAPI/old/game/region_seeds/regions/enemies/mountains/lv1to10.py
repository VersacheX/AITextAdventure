# LEVEL1-10 hostile regional seeds for mountains region (to be imported by higher-level modules).
# Export a list named SEEDS_LV1TO10
SEEDS_LV1TO10 = [
 {"id": "mountain_kiyi", "name": "Mountain Kiyi", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":8, "common_drop": "herb_minor", "money_range": (0,5),
 "basic_attack": "rocky bite", "strong_attack": "staggering chomp", "player_abilities": [], "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":9, "base_ap":1, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "scorch_scrub", "name": "Scorch Scrub", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":18, "common_drop": "herb_minor", "money_range": (1,6),
 "basic_attack": "rough jab", "strong_attack": "ember swing", "player_abilities": [], "base_str":2, "base_dex":2, "base_con":2, "base_int":1, "base_hp":16, "base_ap":2, "str_per_level":0, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "ember_wisp", "name": "Ember Wisp", "hostile_type": "spirit", "role": "damage", "min_spawn_level":1, "rarity": "rare", "base_xp":36, "common_drop": "herb_minor", "money_range": (0,6),
 "basic_attack": "faint ember", "strong_attack": "searing gust", "player_abilities": ["fire_magic_lv1_fireball"], "base_str":1, "base_dex":4, "base_con":1, "base_int":4, "base_hp":30, "base_ap":4, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 {"id": "crag_hare", "name": "Crag Hare", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6, "common_drop": "herb_minor", "money_range": (0,3),
 "basic_attack": "kick", "strong_attack": "spring strike", "player_abilities": [], "base_str":1, "base_dex":5, "base_con":1, "base_int":1, "base_hp":6, "base_ap":1, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 # Level2
 {"id": "trail_hunter", "name": "Trail Hunter", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":16, "common_drop": "herb_minor", "money_range": (1,8),
 "basic_attack": "stalking slash", "strong_attack": "vicious lunge", "player_abilities": [], "base_str":3, "base_dex":4, "base_con":2, "base_int":2, "base_hp":18, "base_ap":3, "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "ember_falcon", "name": "Ember Falcon", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12, "common_drop": "herb_minor", "money_range": (0,6),
 "basic_attack": "talon peck", "strong_attack": "flame dive", "player_abilities": [], "base_str":2, "base_dex":5, "base_con":2, "base_int":2, "base_hp":14, "base_ap":2, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "gear_marshal", "name": "Gear Marshal", "hostile_type": "construct", "role": "support", "min_spawn_level":2, "rarity": "uncommon", "base_xp":28, "common_drop": "stimulant_small", "money_range": (4,20),
 "basic_attack": "piston jab", "strong_attack": "hydraulic thump", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"], "base_str":4, "base_dex":2, "base_con":4, "base_int":1, "base_hp":28, "base_ap":4, "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "magma_monger", "name": "Magma Monger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":30, "common_drop": "herb_med", "money_range": (6,28),
 "basic_attack": "scorch slap", "strong_attack": "lava shove", "player_abilities": [], "base_str":4, "base_dex":3, "base_con":4, "base_int":2, "base_hp":36, "base_ap":4, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "ash_fox", "name": "Ash Fox", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":20, "common_drop": "herb_minor", "money_range": (2,14),
 "basic_attack": "nip", "strong_attack": "ember slash", "player_abilities": [], "base_str":3, "base_dex":5, "base_con":2, "base_int":2, "base_hp":22, "base_ap":3, "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "volcano_whistler", "name": "Volcano Whistler", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "uncommon", "base_xp":36, "common_drop": "stimulant_small", "money_range": (6,30),
 "basic_attack": "whistle jab", "strong_attack": "sonic clap", "player_abilities": ["ice_skill_lv1_ice_shuriken"], "base_str":3, "base_dex":4, "base_con":3, "base_int":3, "base_hp":34, "base_ap":4, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 # Level4
 {"id": "smoke_moth", "name": "Smoke Moth", "hostile_type": "creature", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":12, "common_drop": "herb_minor", "money_range": (1,6),
 "basic_attack": "dust nip", "strong_attack": "smoke cloud", "player_abilities": [], "base_str":1, "base_dex":6, "base_con":2, "base_int":1, "base_hp":32, "base_ap":2, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "ridge_looter", "name": "Ridge Looter", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":36, "common_drop": "herb_med", "money_range": (6,30),
 "basic_attack": "knife jab", "strong_attack": "gutting slash", "player_abilities": [], "base_str":4, "base_dex":4, "base_con":3, "base_int":2, "base_hp":36, "base_ap":4, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "pyre_crone", "name": "Pyre Crone", "hostile_type": "magic", "role": "hazard", "min_spawn_level":4, "rarity": "uncommon", "base_xp":56, "common_drop": "herb_med", "money_range": (10,44),
 "basic_attack": "ember touch", "strong_attack": "magma burst", "player_abilities": ["fire_magic_lv1_fireball", "fire_magic_lv1_fireball"], "base_str":2, "base_dex":3, "base_con":4, "base_int":10, "base_hp":44, "base_ap":6, "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 # Level5
 {"id": "cairn_sentinel", "name": "Cairn Sentinel", "hostile_type": "construct", "role": "support", "min_spawn_level":5, "rarity": "rare", "base_xp":80, "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (20,100),
 "basic_attack": "stone swipe", "strong_attack": "granite crush", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"], "base_str":6, "base_dex":3, "base_con":8, "base_int":2, "base_hp":100, "base_ap":6, "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # Level6
 {"id": "cold_sniper", "name": "Cold Sniper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "rare", "base_xp":140, "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (24,120),
 "basic_attack": "rifle snap", "strong_attack": "precision shot", "player_abilities": ["fire_earth_technique_lv2_blaze_hammer", "ice_skill_lv1_ice_shuriken"], "base_str":5, "base_dex":9, "base_con":5, "base_int":6, "base_hp":88, "base_ap":6, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # Level7
 {"id": "ash_berserker", "name": "Ash Berserker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "rare", "base_xp":180, "common_drop": "stimulant_large", "rare_drop": "cleaver", "money_range": (30,140),
 "basic_attack": "searing slash", "strong_attack": "rending maul", "player_abilities": ["fire_technique_lv3_berserker_tech"], "base_str":8, "base_dex":5, "base_con":8, "base_int":3, "base_hp":160, "base_ap":7, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "summit_spriggan", "name": "Summit Spriggan", "hostile_type": "creature", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":120, "common_drop": "herb_major", "money_range": (20,90),
 "basic_attack": "vine lash", "strong_attack": "root bind", "player_abilities": ["earth_earth_technique_lv2_terra_slam"], "base_str":6, "base_dex":4, "base_con":6, "base_int":3, "base_hp":140, "base_ap":6, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 {"id": "peak_keeper", "name": "Peak Keeper", "hostile_type": "undead", "role": "hazard", "min_spawn_level":8, "rarity": "rare", "base_xp":220, "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (30,140),
 "basic_attack": "bony swipe", "strong_attack": "necrotic thrust", "player_abilities": ["dark_dark_magic_lv2_umbra_storm"], "base_str":6, "base_dex":4, "base_con":8, "base_int":8, "base_hp":180, "base_ap":8, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":3},

 {"id": "storm_howler", "name": "Storm Howler", "hostile_type": "creature", "role": "damage", "min_spawn_level":9, "rarity": "rare", "base_xp":260, "common_drop": "stimulant_large", "rare_drop": "ointment", "money_range": (40,180),
 "basic_attack": "howling bite", "strong_attack": "tempest swipe", "player_abilities": [], "base_str":8, "base_dex":8, "base_con":6, "base_int":4, "base_hp":220, "base_ap":8, "str_per_level":3, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # Level10
 {"id": "pyre_witch", "name": "Pyre Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level":10, "rarity": "superrare", "base_xp":640, "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (50,220),
 "basic_attack": "ember finger", "strong_attack": "magma lance", "player_abilities": ["fire_magic_lv3_pyroclasm", "fire_magic_lv1_fireball"], "base_str":10, "base_dex":6, "base_con":12, "base_int":18, "base_hp":720, "base_ap":12, "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":4},

 {"id": "granite_pup", "name": "Granite Pup", "hostile_type": "creature", "role": "damage", "min_spawn_level":10, "rarity": "common", "base_xp":48, "common_drop": "herb_med", "rare_drop": None, "money_range": (6,28),
 "basic_attack": "stone nip", "strong_attack": "rock maul", "player_abilities": [], "base_str":6, "base_dex":3, "base_con":6, "base_int":1, "base_hp":80, "base_ap":4, "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},
]