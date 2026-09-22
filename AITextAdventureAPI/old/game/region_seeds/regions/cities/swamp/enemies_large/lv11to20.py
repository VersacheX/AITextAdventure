# Level11-20 hostile seeds for The Necropolis (large-city)
# Export a list named SEEDS_LV11TO20 used by constants_enemies_large_city.py
SEEDS_LV11TO20 = [
 # Level11
 {"id": "crypt_revenant", "name": "Crypt Revenant", "hostile_type": "undead", "role": "hazard", "min_spawn_level":11, "rarity": "rare", "base_xp":300,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (30,160),
 "basic_attack": "rotting swipe", "strong_attack": "necrotic burst", "player_abilities": ["lv2_hostile_ability_dark_dark_spirit_void_veil"],
 "base_str":8, "base_dex":4, "base_con":10, "base_int":5, "base_hp":260, "base_ap":8,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":1},

 {"id": "tomb_stigilist", "name": "Tomb Sigilist", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":11, "rarity": "rare", "base_xp":220,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (20,120),
 "basic_attack": "sigil tap", "strong_attack": "runic burst", "player_abilities": ["level_1_hostile_ability_arcane_blast", "level_1_hostile_ability_light_spirit_prism_burst"],
 "base_str":2, "base_dex":3, "base_con":4, "base_int":14, "base_hp":120, "base_ap":8,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":3},

 {"id": "dredge_skulker", "name": "Dredge Skulker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,44),
 "basic_attack": "slick swipe", "strong_attack": "bog tackle", "player_abilities": None,
 "base_str":3, "base_dex":5, "base_con":3, "base_int":2, "base_hp":120, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "silt_scrapper", "name": "Silt Scrapper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "uncommon", "base_xp":110,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (10,60),
 "basic_attack": "grime jab", "strong_attack": "silt uppercut", "player_abilities": None,
 "base_str":4, "base_dex":4, "base_con":4, "base_int":2, "base_hp":140, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # Level12
 {"id": "marrow_sentinel", "name": "Marrow Sentinel", "hostile_type": "undead", "role": "support", "min_spawn_level":12, "rarity": "rare", "base_xp":260,
 "common_drop": "stimulant_med", "rare_drop": "kevlar_vest", "money_range": (30,140),
 "basic_attack": "sentinel crush", "strong_attack": "marrow quake", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":8, "base_dex":3, "base_con":12, "base_int":4, "base_hp":260, "base_ap":6,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":1},

 {"id": "crypt_warden", "name": "Crypt Warden", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":12, "rarity": "rare", "base_xp":240,
 "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (30,150),
 "basic_attack": "lantern strike", "strong_attack": "grim pike", "player_abilities": ["level_1_hostile_ability_light_spirit_prism_burst"],
 "base_str":7, "base_dex":4, "base_con":8, "base_int":6, "base_hp":200, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "bog_lurker", "name": "Bog Lurker", "hostile_type": "creature", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":100,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (12,60),
 "basic_attack": "snap bite", "strong_attack": "mire maul", "player_abilities": None,
 "base_str":5, "base_dex":4, "base_con":5, "base_int":1, "base_hp":150, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "mire_marauder", "name": "Mire Marauder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "uncommon", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (14,70),
 "basic_attack": "club swing", "strong_attack": "silt toss", "player_abilities": None,
 "base_str":6, "base_dex":3, "base_con":6, "base_int":2, "base_hp":160, "base_ap":5,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # Level13
 {"id": "tide_specter", "name": "Tide Specter", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":13, "rarity": "rare", "base_xp":340,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (30,140),
 "basic_attack": "cold ripple", "strong_attack": "spectral tide", "player_abilities": ["lv2_hostile_ability_dark_dark_spirit_void_veil", "level_1_hostile_ability_night_whisper"],
 "base_str":2, "base_dex":5, "base_con":6, "base_int":9, "base_hp":200, "base_ap":9,
 "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "silt_sentinel", "name": "Silt Sentinel", "hostile_type": "humanoid", "role": "support", "min_spawn_level":13, "rarity": "uncommon", "base_xp":140,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (16,80),
 "basic_attack": "guard bash", "strong_attack": "mire sweep", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":6, "base_dex":3, "base_con":8, "base_int":3, "base_hp":180, "base_ap":6,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "fen_forager", "name": "Fen Forager", "hostile_type": "creature", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (12,64),
 "basic_attack": "peck", "strong_attack": "bog lunge", "player_abilities": None,
 "base_str":4, "base_dex":6, "base_con":4, "base_int":1, "base_hp":140, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # Level14
 {"id": "death_herald", "name": "Death Herald", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":14, "rarity": "rare", "base_xp":320,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (40,200),
 "basic_attack": "dirge note", "strong_attack": "pall of death", "player_abilities": ["level_1_hostile_ability_night_whisper", "lv2_hostile_ability_dark_dark_spirit_void_veil"],
 "base_str":3, "base_dex":4, "base_con":8, "base_int":14, "base_hp":220, "base_ap":10,
 "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":3},

 {"id": "sleet_haunter", "name": "Sleet Haunter", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":14, "rarity": "uncommon", "base_xp":180,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (18,96),
 "basic_attack": "frost moan", "strong_attack": "chill rift", "player_abilities": ["level_1_hostile_ability_night_whisper"],
 "base_str":2, "base_dex":5, "base_con":3, "base_int":8, "base_hp":160, "base_ap":7,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "marsh_warden", "name": "Marsh Warden", "hostile_type": "humanoid", "role": "support", "min_spawn_level":14, "rarity": "common", "base_xp":160,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (20,100),
 "basic_attack": "warden slash", "strong_attack": "bog command", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":6, "base_dex":4, "base_con":8, "base_int":3, "base_hp":200, "base_ap":6,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 # Level15
 {"id": "nasty_marrow_collector", "name": "Nasty Marrow Collector", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":15, "rarity": "rare", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (18,96),
 "basic_attack": "pick bone", "strong_attack": "marrow rip", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":4, "base_dex":3, "base_con":8, "base_int":6, "base_hp":140, "base_ap":6,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":1},

 {"id": "bone_colossus", "name": "Bone Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":15, "rarity": "rare", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (60,240),
 "basic_attack": "rib swing", "strong_attack": "colossal crush", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":14, "base_dex":1, "base_con":18, "base_int":1, "base_hp":400, "base_ap":4,
 "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "necropolis_marauder", "name": "Necropolis Marauder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":140,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (18,90),
 "basic_attack": "club swing", "strong_attack": "crab toss", "player_abilities": None,
 "base_str":6, "base_dex":3, "base_con":6, "base_int":2, "base_hp":180, "base_ap":5,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # Level16
 {"id": "iron_colossus", "name": "Iron Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":16, "rarity": "uncommon", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (60,240),
 "basic_attack": "iron slam", "strong_attack": "piston maul", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":14, "base_dex":2, "base_con":18, "base_int":2, "base_hp":420, "base_ap":5,
 "str_per_level":4, "dex_per_level":1, "con_per_level":3, "int_per_level":1},

 {"id": "mud_lich", "name": "Mud Lich", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":16, "rarity": "superrare", "base_xp":520,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,340),
 "basic_attack": "soul rot", "strong_attack": "abyssal mire", "player_abilities": ["lv2_hostile_ability_dark_electric_magic_abyssal_storm", "lv2_hostile_ability_dark_air_skill_nightmare_wave"],
 "base_str":6, "base_dex":4, "base_con":10, "base_int":14, "base_hp":360, "base_ap":12,
 "str_per_level":2, "dex_per_level":1, "con_per_level":3, "int_per_level":4},

 {"id": "mire_hopper", "name": "Mire Hopper", "hostile_type": "creature", "role": "damage", "min_spawn_level":16, "rarity": "common", "base_xp":200,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (40,180),
 "basic_attack": "leap bite", "strong_attack": "burrow slam", "player_abilities": None,
 "base_str":7, "base_dex":6, "base_con":8, "base_int":2, "base_hp":260, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 # Level17
 {"id": "grave_lurker", "name": "Grave Lurker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":17, "rarity": "uncommon", "base_xp":220,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (40,200),
 "basic_attack": "lurker slash", "strong_attack": "spine rift", "player_abilities": None,
 "base_str":8, "base_dex":4, "base_con":10, "base_int":3, "base_hp":280, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":0},

 {"id": "urban_mire_sentinel", "name": "Urban Mire Sentinel", "hostile_type": "humanoid", "role": "support", "min_spawn_level":17, "rarity": "uncommon", "base_xp":220,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (40,200),
 "basic_attack": "sentinel jab", "strong_attack": "mire slam", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":8, "base_dex":3, "base_con":10, "base_int":3, "base_hp":280, "base_ap":6,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 # Level18
 {"id": "necromancer_lord", "name": "Necromancer Lord", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":18, "rarity": "superrare", "base_xp":720,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (100,420),
 "basic_attack": "skeletal lash", "strong_attack": "dread invocation", "player_abilities": ["lv2_hostile_ability_dark_electric_magic_abyssal_storm", "lv2_hostile_ability_dark_dark_spirit_void_veil", "level_1_hostile_ability_light_spirit_prism_burst"],
 "base_str":6, "base_dex":6, "base_con":10, "base_int":16, "base_hp":420, "base_ap":14,
 "str_per_level":2, "dex_per_level":2, "con_per_level":3, "int_per_level":4},

 {"id": "bog_swimmer", "name": "Bog Swimmer", "hostile_type": "creature", "role": "damage", "min_spawn_level":18, "rarity": "common", "base_xp":240,
 "common_drop": "stimulant_med", "rare_drop": None, "money_range": (50,220),
 "basic_attack": "swipe bite", "strong_attack": "undermaul", "player_abilities": None,
 "base_str":9, "base_dex":5, "base_con":10, "base_int":2, "base_hp":300, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":0},

 # Level20
 {"id": "mort_queen", "name": "Mort Queen", "hostile_type": "undead", "role": "hazard", "min_spawn_level":20, "rarity": "superrare", "base_xp":900,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (180,700),
 "basic_attack": "regal claw", "strong_attack": "necrotic dominion", "player_abilities": ["lv2_hostile_ability_dark_air_skill_nightmare_wave", "lv2_hostile_ability_dark_dark_spirit_void_veil"],
 "base_str":10, "base_dex":8, "base_con":12, "base_int":14, "base_hp":600, "base_ap":16,
 "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":4},
]
