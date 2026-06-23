# Level1-10 hostile seeds for Boiling Bubble (mid-city witch district)
# Split out from constants_enemies_mid_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==1 (common, uncommon, rare)
 {"id": "pocket_imp", "name": "Pocket Imp", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":10,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "nasty nip", "strong_attack": "snatch and vanish", "player_abilities": None,
 "base_str":1, "base_dex":6, "base_con":1, "base_int":3, "base_hp":10, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "tea_barker", "name": "Tea Barker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":8,
 "common_drop": "water", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "yelled insult", "strong_attack": "hot splash", "player_abilities": None,
 "base_str":2, "base_dex":2, "base_con":2, "base_int":1, "base_hp":10, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "imp_chieftain", "name": "Imp Chieftain", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":1, "rarity": "rare", "base_xp":34,
 "common_drop": "lockpick", "rare_drop": "tome_dex", "money_range": (6,30),
 "basic_attack": "leader's bite", "strong_attack": "commanding shriek", "player_abilities": ["dark_magic_lv1_shadow_tendril"],
 "base_str":3, "base_dex":8, "base_con":4, "base_int":6, "base_hp":23, "base_ap":6,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":2},

 # min_spawn_level ==2
 {"id": "cauldron_clown", "name": "Cauldron Clown", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":2, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "slapstick swat", "strong_attack": "splash of sting", "player_abilities": ["air_skill_lv1_smoke_bomb"],
 "base_str":1, "base_dex":5, "base_con":2, "base_int":4, "base_hp":12, "base_ap":3,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "elven_court_jester", "name": "Court Jester of Leaves", "hostile_type": "humanoid", "role": "support", "min_spawn_level":2, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "slapstick bop", "strong_attack": "pratfall explosion", "player_abilities": ["water_faith_lv1_mending_streams"],
 "base_str":1, "base_dex":2, "base_con":2, "base_int":5, "base_hp":12, "base_ap":3,
 "str_per_level":0, "dex_per_level":0, "con_per_level":0, "int_per_level":2},

 # min_spawn_level ==3
 {"id": "hell_hound", "name": "Hell Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": "stimulant_small", "money_range": (2,10),
 "basic_attack": "shredding bite", "strong_attack": "thrashing teeth", "player_abilities": None,
 "base_str":3, "base_dex":5, "base_con":3, "base_int":2, "base_hp":18, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "slicktongue", "name": "Slicktongued Peddler", "hostile_type": "humanoid", "role": "support", "min_spawn_level":3, "rarity": "uncommon", "base_xp":30,
 "common_drop": "herb_med", "rare_drop": "pipe_wrench", "money_range": (3,24),
 "basic_attack": "peddler's shove", "strong_attack": "charm and pick", "player_abilities": ["water_faith_lv1_mending_streams"],
 "base_str":2, "base_dex":6, "base_con":2, "base_int":6, "base_hp":16, "base_ap":4,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":2},

 # min_spawn_level ==4
 {"id": "elven_scribbler", "name": "Elven Scribbler", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":4, "rarity": "rare", "base_xp":28,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (2,16),
 "basic_attack": "splatter paint", "strong_attack": "mock inking", "player_abilities": ["air_skill_lv1_smoke_bomb"],
 "base_str":2, "base_dex":7, "base_con":2, "base_int":4, "base_hp":18, "base_ap":4,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "kettle_brawler", "name": "Kettle Brawler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":30,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "lopsided haymaker", "strong_attack": "cauldron hook", "player_abilities": None,
 "base_str":6, "base_dex":3, "base_con":4, "base_int":1, "base_hp":22, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==5
 {"id": "rune_scribe", "name": "Rune Scribe", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "common", "base_xp":44,
 "common_drop": "stimulant_small", "rare_drop": "tome_dex", "money_range": (8,36),
 "basic_attack": "inked jab", "strong_attack": "rune lash", "player_abilities": ["electric_fire_magic_lv2_arclance", "fire_magic_lv1_fireball"],
 "base_str":1, "base_dex":3, "base_con":2, "base_int":8, "base_hp":28, "base_ap":6,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 {"id": "sprig_scout", "name": "Sprig Scout", "hostile_type": "creature", "role": "damage", "min_spawn_level":5, "rarity": "common", "base_xp":40,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (6,28),
 "basic_attack": "twig jab", "strong_attack": "rapid sprout", "player_abilities": None,
 "base_str":3, "base_dex":6, "base_con":3, "base_int":1, "base_hp":44, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==6
 {"id": "hexed_constable", "name": "Hexed Constable", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":6, "rarity": "rare", "base_xp":90,
 "common_drop": "stimulant_med", "rare_drop": "kevlar_vest", "money_range": (12,60),
 "basic_attack": "enchanted baton", "strong_attack": "overcharged reprimand", "player_abilities": ["air_skill_lv1_smoke_bomb", "fire_air_tech_lv2_aero_flare"],
 "base_str":4, "base_dex":4, "base_con":6, "base_int":3, "base_hp":44, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 {"id": "whisper_acolyte", "name": "Whisper Acolyte", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":6, "rarity": "rare", "base_xp":82,
 "common_drop": "herb_major", "rare_drop": "short_sword", "money_range": (18,70),
 "basic_attack": "murmured hex", "strong_attack": "drain whisper", "player_abilities": ["dark_magic_lv2_night_whisper", "dark_dark_magic_lv2_umbra_storm"],
 "base_str":1, "base_dex":2, "base_con":3, "base_int":8, "base_hp":28, "base_ap":7,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 # min_spawn_level ==7
 {"id": "cloak_roustabout", "name": "Cloak Roustabout", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":28,
 "common_drop": "herb_med", "rare_drop": "dagger", "money_range": (4,20),
 "basic_attack": "tumble and kick", "strong_attack": "trip and stab", "player_abilities": ["fire_earth_technique_lv2_blaze_hammer"],
 "base_str":3, "base_dex":6, "base_con":2, "base_int":3, "base_hp":18, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "fixer_ike", "name": "Fixer Ike", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":7, "rarity": "uncommon", "base_xp":40,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (8,32),
 "basic_attack": "spanner jab", "strong_attack": "glitched spark", "player_abilities": ["fire_water_tech_lv2_steam_grenade", "fire_air_tech_lv2_aero_flare"],
 "base_str":2, "base_dex":4, "base_con":2, "base_int":6, "base_hp":22, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 # min_spawn_level ==8
 {"id": "coven_fixer", "name": "Coven Fixer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":8, "rarity": "common", "base_xp":48,
 "common_drop": "lockpick", "rare_drop": "tome_dex", "money_range": (10,60),
 "basic_attack": "tinker's prod", "strong_attack": "rune short-circuit", "player_abilities": ["fire_water_tech_lv2_steam_grenade", "fire_air_tech_lv2_aero_flare"],
 "base_str":2, "base_dex":4, "base_con":3, "base_int":7, "base_hp":26, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "forest_siren", "name": "Forest Siren", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":8, "rarity": "common", "base_xp":100,
 "common_drop": "stimulant_med", "rare_drop": "tome_int", "money_range": (20,90),
 "basic_attack": "glowing blade", "strong_attack": "stunning strike", "player_abilities": ["light_faith_lv2_prism_burst"],
 "base_str":3, "base_dex":7, "base_con":3, "base_int":6, "base_hp":44, "base_ap":6,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":2},

 # min_spawn_level ==9
 {"id": "moss_smuggler", "name": "Moss Smuggler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":9, "rarity": "common", "base_xp":52,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (12,70),
 "basic_attack": "quick jab", "strong_attack": "mossy lariat", "player_abilities": None,
 "base_str":3, "base_dex":6, "base_con":2, "base_int":3, "base_hp":28, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "leaf_tender", "name": "Leaf Tender", "hostile_type": "creature", "role": "damage", "min_spawn_level":9, "rarity": "common", "base_xp":140,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (18,88),
 "basic_attack": "leaf slash", "strong_attack": "rooted slam", "player_abilities": None,
 "base_str":4, "base_dex":4, "base_con":6, "base_int":2, "base_hp":120, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==10
 {"id": "shadow_assassin", "name": "Shadow Assassin", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":10, "rarity": "rare", "base_xp":160,
 "common_drop": "lockpick", "rare_drop": "tome_int", "money_range": (40,160),
 "basic_attack": "silent strike", "strong_attack": "nightmare release", "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_air_light_magic_lv4_nightmare_wave"],
 "base_str":6, "base_dex":12, "base_con":4, "base_int":7, "base_hp":80, "base_ap":10,
 "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":2},

 {"id": "owl_sharpshooter", "name": "Owl Sharpshooter", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":10, "rarity": "superrare", "base_xp":420,
 "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (80,320),
 "basic_attack": "precise hoot-shot", "strong_attack": "sundering aim", "player_abilities": None,
 "base_str":2, "base_dex":8, "base_con":2, "base_int":5, "base_hp":60, "base_ap":8,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},
]
