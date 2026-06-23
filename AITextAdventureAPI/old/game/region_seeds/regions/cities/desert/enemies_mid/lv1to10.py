# Level1-10 hostile seeds for the Great Dune City (mid-tier)
# Split out from constants_enemies_mid_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==1
 {"id": "gloam_urchin", "name": "Gloam Urchin", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "tug at your cloak", "strong_attack": "shove and run", "player_abilities": None,
 "base_str":1, "base_dex":4, "base_con":1, "base_int":2, "base_hp":8, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "inkling_pickpocket", "name": "Inkling Pickpocket", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":10,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (0,8),
 "basic_attack": "paper cut", "strong_attack": "pocket pinch", "player_abilities": None,
 "base_str":1, "base_dex":6, "base_con":1, "base_int":2, "base_hp":12, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "stray_cutpurse", "name": "Stray Cutpurse", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "rare", "base_xp":20,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (0,10),
 "basic_attack": "quick snatch", "strong_attack": "gutting slash", "player_abilities": None,
 "base_str":2, "base_dex":7, "base_con":2, "base_int":3, "base_hp":16, "base_ap":3,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # min_spawn_level ==2
 {"id": "lantern_vendor", "name": "Lantern Vendor", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": "lockpick", "money_range": (1,10),
 "basic_attack": "brandish a broken lamp", "strong_attack": "swinging polearm", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":2, "base_hp":12, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "bookish_bumbler", "name": "Bookish Bumbler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "flap a tome", "strong_attack": "spill ink", "player_abilities": ["streamlet"],
 "base_str":1, "base_dex":2, "base_con":2, "base_int":5, "base_hp":12, "base_ap":3,
 "str_per_level":0, "dex_per_level":0, "con_per_level":0, "int_per_level":2},

 # min_spawn_level ==3
 {"id": "candle_jester", "name": "Candle Jester", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "uncommon", "base_xp":22,
 "common_drop": "stimulant_small", "rare_drop": "pipe_wrench", "money_range": (2,18),
 "basic_attack": "a mocking pratfall", "strong_attack": "exploding joke", "player_abilities": ["air_skill_lv1_smoke_bomb"],
 "base_str":2, "base_dex":6, "base_con":2, "base_int":4, "base_hp":14, "base_ap":3,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "cowl_thief", "name": "Cowl Thief", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "uncommon", "base_xp":30,
 "common_drop": "lockpick", "rare_drop": "dagger", "money_range": (3,20),
 "basic_attack": "snatch and slash", "strong_attack": "back-alley stab", "player_abilities": ["dark_magic_lv1_shadow_tendril"],
 "base_str":3, "base_dex":7, "base_con":2, "base_int":3, "base_hp":16, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "arcane_hound", "name": "Arcane Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": "stimulant_small", "money_range": (2,10),
 "basic_attack": "rips with arcane jaws", "strong_attack": "mana bite", "player_abilities": None,
 "base_str":3, "base_dex":5, "base_con":3, "base_int":2, "base_hp":18, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==4
 {"id": "ombre_brawler", "name": "Ombre Brawler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":36,
 "common_drop": "herb_med", "rare_drop": "cloth_gloves", "money_range": (6,28),
 "basic_attack": "haymaker from the dark", "strong_attack": "shadow slam", "player_abilities": ["fire_technique_lv4_berserker_tech"],
 "base_str":5, "base_dex":3, "base_con":4, "base_int":2, "base_hp":30, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "fixer_mike", "name": "Fixer Mike", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":4, "rarity": "common", "base_xp":40,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (8,32),
 "basic_attack": "spanner jab", "strong_attack": "glitched spark", "player_abilities": ["fire_water_tech_lv2_steam_grenade", "fire_air_tech_lv2_aero_flare"],
 "base_str":2, "base_dex":4, "base_con":2, "base_int":6, "base_hp":22, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 # min_spawn_level ==5
 {"id": "sigil_monger", "name": "Sigil Monger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":44,
 "common_drop": "stimulant_small", "rare_drop": "tome_dex", "money_range": (8,36),
 "basic_attack": "brandish a glowing sigil", "strong_attack": "arcane lash", "player_abilities": ["electric_fire_magic_lv2_arclance", "fire_magic_lv1_fireball"],
 "base_str":2, "base_dex":3, "base_con":2, "base_int":7, "base_hp":24, "base_ap":6,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 # min_spawn_level ==6
 {"id": "desert_neon_siren", "name": "Desert Neon Siren", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":6, "rarity": "rare", "base_xp":100,
 "common_drop": "stimulant_med", "rare_drop": "tome_int", "money_range": (20,90),
 "basic_attack": "glowing blade", "strong_attack": "stunning strike", "player_abilities": ["prism_burst"],
 "base_str":3, "base_dex":7, "base_con":3, "base_int":6, "base_hp":44, "base_ap":6,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":2},

 {"id": "shade_guard", "name": "Shade Guard", "hostile_type": "humanoid", "role": "support", "min_spawn_level":6, "rarity": "rare", "base_xp":90,
 "common_drop": "stimulant_med", "rare_drop": "kevlar_vest", "money_range": (20,80),
 "basic_attack": "guard's baton", "strong_attack": "stunning charge", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"],
 "base_str":5, "base_dex":4, "base_con":6, "base_int":3, "base_hp":48, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 # min_spawn_level ==8
 {"id": "banshee", "name": "Wailing Banshee", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":8, "rarity": "rare", "base_xp":140,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (6,44),
 "basic_attack": "piercing wail", "strong_attack": "banshee shriek", "player_abilities": ["night_whisper"],
 "base_str":1, "base_dex":4, "base_con":1, "base_int":9, "base_hp":30, "base_ap":8,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 # min_spawn_level ==9
 {"id": "void_spider", "name": "Void Spider", "hostile_type": "creature", "role": "hazard", "min_spawn_level":9, "rarity": "uncommon", "base_xp":100,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (4,40),
 "basic_attack": "fanged bite", "strong_attack": "venomous tear", "player_abilities": ["venom_trace"],
 "base_str":3, "base_dex":9, "base_con":4, "base_int":3, "base_hp":60, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==10
 {"id": "nightveil_raider", "name": "Nightveil Raider", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":10, "rarity": "superrare", "base_xp":420,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (80,320),
 "basic_attack": "raider's volley", "strong_attack": "assassin's hail", "player_abilities": ["shadow_flicker", "quick_shot"],
 "base_str":8, "base_dex":12, "base_con":6, "base_int":6, "base_hp":180, "base_ap":12,
 "str_per_level":3, "dex_per_level":3, "con_per_level":2, "int_per_level":2},
]