# Level21-30 hostile seeds for the Great Dune City
# Split out from constants_enemies_large_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==21
 {"id": "sand_pick", "name": "Sand-Pick", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":21, "rarity": "common", "base_xp":9,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "quick finger-prick", "strong_attack": "sandy snatch", "player_abilities": None,
 "base_str":1, "base_dex":6, "base_con":1, "base_int":2, "base_hp":10, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "drift_vagrant", "name": "Drift Vagrant", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":21, "rarity": "common", "base_xp":7,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "stumbles into you", "strong_attack": "desperate lunge", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":1, "base_int":1, "base_hp":6, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 # min_spawn_level ==22
 {"id": "sand_jackal", "name": "Sand Jackal", "hostile_type": "creature", "role": "damage", "min_spawn_level":22, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "bites in a pack", "strong_attack": "pouncing maul", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":1, "base_hp":12, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "dune_dame", "name": "Dune Dame", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":22, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "heavy purse bash", "strong_attack": "stiletto of heat", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":2, "base_hp":10, "base_ap":2,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # min_spawn_level ==23
 {"id": "tattooed_brigand", "name": "Tattooed Brigand", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":23, "rarity": "common", "base_xp":24,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (4,20),
 "basic_attack": "inked knuckle jab", "strong_attack": "furious flurry", "player_abilities": [],
 "base_str":3, "base_dex":3, "base_con":2, "base_int":1, "base_hp":16, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "sand_flapper", "name": "Sand Flapper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":23, "rarity": "common", "base_xp":20,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "feathered scratch", "strong_attack": "twirl of dunes", "player_abilities": [],
 "base_str":2, "base_dex":6, "base_con":2, "base_int":2, "base_hp":14, "base_ap":3,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # min_spawn_level ==24
 {"id": "sand_centurion", "name": "Sand Centurion", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":24, "rarity": "rare", "base_xp":200,
 "common_drop": "stimulant_med", "rare_drop": "kevlar_vest", "money_range": (30,140),
 "basic_attack": "centurion spear stab", "strong_attack": "sweeping dune strike", "player_abilities": None,
 "base_str":8, "base_dex":5, "base_con":8, "base_int":2, "base_hp":120, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "oasis_enforcer", "name": "Oasis Enforcer", "hostile_type": "humanoid", "role": "support", "min_spawn_level":24, "rarity": "common", "base_xp":120,
 "common_drop": "stimulant_small", "rare_drop": "cloth_gloves", "money_range": (12,60),
 "basic_attack": "water blade slash", "strong_attack": "drowning lunge", "player_abilities": ["air_light_faith_lv2_serene_breath"],
 "base_str":6, "base_dex":6, "base_con":6, "base_int":3, "base_hp":100, "base_ap":6,
 "str_per_level":2, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 # min_spawn_level ==25
 {"id": "scorpion_enforcer", "name": "Scorpion Enforcer", "hostile_type": "humanoid", "role": "support", "min_spawn_level":25, "rarity": "uncommon", "base_xp":64,
 "common_drop": "stimulant_small", "rare_drop": "cloth_gloves", "money_range": (8,32),
 "basic_attack": "stings with a poisoned hook", "strong_attack": "pincer crush", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":6, "base_dex":4, "base_con":5, "base_int":2, "base_hp":36, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "rusted_berserker", "name": "Rusted Berserker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":25, "rarity": "rare", "base_xp":220,
 "common_drop": "herb_major", "rare_drop": "sawed_off", "money_range": (40,180),
 "basic_attack": "rusted maul", "strong_attack": "feral overdrive", "player_abilities": ["earth_fire_technique_lv2_berserker_tech"],
 "base_str":10, "base_dex":3, "base_con":9, "base_int":1, "base_hp":160, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==26
 {"id": "desert_banshee", "name": "Desert Banshee", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":26, "rarity": "rare", "base_xp":140,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (5,40),
 "basic_attack": "piercing wail", "strong_attack": "baneful shriek", "player_abilities": ["level_1_hostile_ability_night_whisper"],
 "base_str":1, "base_dex":4, "base_con":1, "base_int":9, "base_hp":30, "base_ap":8,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 {"id": "sirene_mirage", "name": "Sirene of the Mirage", "hostile_type": "humanoid", "role": "support", "min_spawn_level":26, "rarity": "rare", "base_xp":76,
 "common_drop": "stimulant_small", "rare_drop": "tome_int", "money_range": (10,64),
 "basic_attack": "luring song", "strong_attack": "mesmeric mirage", "player_abilities": ["level_1_hostile_ability_fire_faith_hearthsong", "air_light_faith_lv2_serene_breath"],
 "base_str":2, "base_dex":6, "base_con":2, "base_int":6, "base_hp":26, "base_ap":5,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":3},

 # min_spawn_level ==27
 {"id": "maternal_guardian", "name": "Maternal Guardian", "hostile_type": "humanoid", "role": "support", "min_spawn_level":27, "rarity": "uncommon", "base_xp":64,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,40),
 "basic_attack": "bear-claw hug", "strong_attack": "crushing embrace", "player_abilities": None,
 "base_str":6, "base_dex":2, "base_con":6, "base_int":2, "base_hp":52, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":1},

 {"id": "techno_void_spider", "name": "Techno Void Spider", "hostile_type": "creature", "role": "hazard", "min_spawn_level":27, "rarity": "uncommon", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (2,30),
 "basic_attack": "fanged bite", "strong_attack": "venomous tear", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit", "level_1_hostile_ability_shadow_lash"],
 "base_str":2, "base_dex":8, "base_con":3, "base_int":10, "base_hp":40, "base_ap":12,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":4},

 # min_spawn_level ==28
 {"id": "treasure_snatcher", "name": "Treasure Snatcher", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":28, "rarity": "common", "base_xp":96,
 "common_drop": "stimulant_med", "rare_drop": "herb_major", "money_range": (24,110),
 "basic_attack": "stabs with a jeweled trinket", "strong_attack": "antique uppercut", "player_abilities": [],
 "base_str":2, "base_dex":5, "base_con":2, "base_int":4, "base_hp":30, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "spectral_hag", "name": "Spectral Hag", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":28, "rarity": "uncommon", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": "tome_con", "money_range": (8,44),
 "basic_attack": "withering curse", "strong_attack": "spectral claws", "player_abilities": ["level_1_hostile_ability_shadow_lash"],
 "base_str":1, "base_dex":3, "base_con":2, "base_int":9, "base_hp":36, "base_ap":10,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 # min_spawn_level ==29
 {"id": "elder_sand_tentacle", "name": "Elder Sand Tentacle", "hostile_type": "eldritch", "role": "damage", "min_spawn_level":29, "rarity": "superrare", "base_xp":200,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (20,100),
 "basic_attack": "tentacle whip", "strong_attack": "barbed crush", "player_abilities": None,
 "base_str":12, "base_dex":2, "base_con":10, "base_int":2, "base_hp":160, "base_ap":4,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "umbral_stalker", "name": "Umbral Stalker", "hostile_type": "shadow", "role": "damage", "min_spawn_level":29, "rarity": "uncommon", "base_xp":180,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (6,48),
 "basic_attack": "dark slash", "strong_attack": "vanishing strike", "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
 "base_str":5, "base_dex":10, "base_con":4, "base_int":3, "base_hp":80, "base_ap":7,
 "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # min_spawn_level ==30
 {"id": "wraith_knight", "name": "Wraith Knight", "hostile_type": "undead", "role": "hazard", "min_spawn_level":30, "rarity": "rare", "base_xp":260,
 "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (25,120),
 "basic_attack": "spectral blade", "strong_attack": "ghostly cleave", "player_abilities": None,
 "base_str":8, "base_dex":6, "base_con":6, "base_int":3, "base_hp":120, "base_ap":8,
 "str_per_level":2, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "plague_stoker", "name": "Plague Stoker", "hostile_type": "undead", "role": "hazard", "min_spawn_level":30, "rarity": "uncommon", "base_xp":160,
 "common_drop": "ointment", "rare_drop": "stimulant_large", "money_range": (5,60),
 "basic_attack": "diseased smite", "strong_attack": "virulent spray", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":4, "base_dex":3, "base_con":6, "base_int":6, "base_hp":120, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":2},
]
