# LEVEL 1-10 hostile regional (to be imported by higher-level modules).

RANDOM_HOSTILE_SEEDS = []

# LEVEL1-10 hostile regional seeds for forest region (to be imported by higher-level modules).
# Export a list named SEEDS_LV1TO10
SEEDS_LV1TO10 = [
 {"id": "bracken_hopper", "name": "Bracken Hopper", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":18, "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "spring kick", "strong_attack": "pounce", "player_abilities": [], "base_str":1, "base_dex":3, "base_con":2, "base_int":1, "base_hp":16, "base_ap":2, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "forest_pickpocket", "name": "Forest Pickpocket", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":1, "rarity": "uncommon", "base_xp":24, "common_drop": "stimulant_small", "rare_drop": None, "money_range": (0,8),
 "basic_attack": "flick hand", "strong_attack": "distract-and-stab", "player_abilities": None, "base_str":2, "base_dex":6, "base_con":2, "base_int":3, "base_hp":28, "base_ap":3, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "weeping_wisp", "name": "Weeping Wisp", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":1, "rarity": "rare", "base_xp":46, "common_drop": "herb_minor", "rare_drop": "tome_int", "money_range": (2,12),
 "basic_attack": "mournful touch", "strong_attack": "wailing grasp", "player_abilities": ["level_1_hostile_ability_night_whisper"], "base_str":1, "base_dex":4, "base_con":1, "base_int":6, "base_hp":20, "base_ap":6, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 {"id": "mossling", "name": "Mossling", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":24, "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "moss pelt", "strong_attack": "clinging tendrils", "player_abilities": [], "base_str":1, "base_dex":3, "base_con":2, "base_int":1, "base_hp":30, "base_ap":2, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "sapling_swarm", "name": "Sapling Swarm", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":22, "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "sap pelt", "strong_attack": "swarm overwhelm", "player_abilities": [], "base_str":1, "base_dex":5, "base_con":2, "base_int":1, "base_hp":36, "base_ap":2, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "murder_of_raven", "name": "Murder of Raven", "hostile_type": "creature", "role": "hazard", "min_spawn_level":3, "rarity": "common", "base_xp":36, "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "peck barrage", "strong_attack": "raven maul", "player_abilities": ["ice_skill_lv1_ice_shuriken"], "base_str":2, "base_dex":8, "base_con":2, "base_int":2, "base_hp":44, "base_ap":3, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "ember_fawn", "name": "Ember Fawn", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":30, "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "ember nudge", "strong_attack": "scorch stomp", "player_abilities": ["fire_magic_lv1_fireball"], "base_str":2, "base_dex":6, "base_con":3, "base_int":3, "base_hp":46, "base_ap":3, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "sylph_sprite", "name": "Sylph Sprite", "hostile_type": "spirit", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":28, "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "gust tap", "strong_attack": "whirl dart", "player_abilities": ["ice_skill_lv1_ice_shuriken", "air_light_skill_lv2_dawn_cut"], "base_str":1, "base_dex":9, "base_con":2, "base_int":3, "base_hp":36, "base_ap":4, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "roamer_boar", "name": "Roamer Boar", "hostile_type": "creature", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":44, "common_drop": "herb_minor", "rare_drop": "machete", "money_range": (4,18),
 "basic_attack": "tusk gore", "strong_attack": "charging tusk", "player_abilities": [], "base_str":6, "base_dex":4, "base_con":6, "base_int":1, "base_hp":70, "base_ap":3, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "spectral_crow", "name": "Spectral Crow", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":4, "rarity": "common", "base_xp":40, "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "ethereal peck", "strong_attack": "spirit dive", "player_abilities": ["level_1_hostile_ability_dark_magic_daze_whisper"], "base_str":1, "base_dex":7, "base_con":2, "base_int":4, "base_hp":46, "base_ap":3, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "gnarlroot", "name": "Gnarlroot", "hostile_type": "creature", "role": "hazard", "min_spawn_level":5, "rarity": "common", "base_xp":40, "common_drop": "herb_minor", "rare_drop": "cloth_gloves", "money_range": (2,12),
 "basic_attack": "root slap", "strong_attack": "entangling grasp", "player_abilities": ["earth_earth_technique_lv2_terra_slam"], "base_str":4, "base_dex":2, "base_con":6, "base_int":1, "base_hp":48, "base_ap":2, "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "spriggan", "name": "Spriggan", "hostile_type": "creature", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":90, "common_drop": "herb_med", "rare_drop": "short_sword", "money_range": (6,36),
 "basic_attack": "branch jab", "strong_attack": "whiplash", "player_abilities": ["ice_skill_lv1_ice_shuriken"], "base_str":5, "base_dex":7, "base_con":5, "base_int":2, "base_hp":86, "base_ap":4, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "glade_serpent", "name": "Glade Serpent", "hostile_type": "creature", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":95, "common_drop": "herb_med", "rare_drop": "dagger", "money_range": (6,40),
 "basic_attack": "coil bite", "strong_attack": "venom strike", "player_abilities": ["fire_dark_skill_lv2_embersmoke"], "base_str":5, "base_dex":9, "base_con":5, "base_int":3, "base_hp":100, "base_ap":5, "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":0},

 {"id": "crag_howler", "name": "Crag Howler", "hostile_type": "creature", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":84, "common_drop": "herb_med", "rare_drop": "revolver", "money_range": (8,44),
 "basic_attack": "piercing howl", "strong_attack": "sonic maul", "player_abilities": ["ice_skill_lv1_ice_shuriken"], "base_str":6, "base_dex":7, "base_con":5, "base_int":3, "base_hp":96, "base_ap":4, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "bog_tremor", "name": "Bog Tremor", "hostile_type": "creature", "role": "hazard", "min_spawn_level":6, "rarity": "uncommon", "base_xp":98, "common_drop": "herb_med", "rare_drop": "pipe_wrench", "money_range": (8,44),
 "basic_attack": "mud stomp", "strong_attack": "earthquake heave", "player_abilities": ["air_electric_fire_technique_lv3_tempest_charge"], "base_str":9, "base_dex":2, "base_con":10, "base_int":2, "base_hp":160, "base_ap":4, "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "fen_hag", "name": "Fen Hag", "hostile_type": "spirit", "role": "support", "min_spawn_level":8, "rarity": "uncommon", "base_xp":130, "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (6,36),
 "basic_attack": "needle growth", "strong_attack": "spore burst", "player_abilities": ["level_1_hostile_ability_earth_magic_sap_bloom"], "base_str":2, "base_dex":4, "base_con":5, "base_int":7, "base_hp":92, "base_ap":6, "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "marsh_witch", "name": "Marsh Witch", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":9, "rarity": "rare", "base_xp":180, "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (14,80),
 "basic_attack": "hexed jab", "strong_attack": "mire hex", "player_abilities": ["level_1_hostile_ability_night_whisper", "level_1_hostile_ability_fire_faith_hearthsong"], "base_str":3, "base_dex":5, "base_con":4, "base_int":11, "base_hp":120, "base_ap":8, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "crystal_serpent", "name": "Crystal Serpent", "hostile_type": "creature", "role": "hazard", "min_spawn_level":9, "rarity": "rare", "base_xp":190, "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (18,90),
 "basic_attack": "maw lash", "strong_attack": "glacial constrict", "player_abilities": ["lv2_hostile_ability_water_electric_magic_maelstrom_burst"], "base_str":6, "base_dex":8, "base_con":6, "base_int":4, "base_hp":160, "base_ap":7, "str_per_level":2, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "echolisk", "name": "Echolisk", "hostile_type": "creature", "role": "damage", "min_spawn_level":9, "rarity": "rare", "base_xp":170, "common_drop": "stimulant_med", "rare_drop": "rapier", "money_range": (12,80),
 "basic_attack": "sonic bite", "strong_attack": "echoshred", "player_abilities": ["lv2_hostile_ability_fire_water_tech_steam_grenade", "ice_skill_lv1_ice_shuriken"], "base_str":7, "base_dex":8, "base_con":7, "base_int":5, "base_hp":150, "base_ap":6, "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "willow_wight", "name": "Willow Wight", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":10, "rarity": "superrare", "base_xp":420, "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (18,100),
 "basic_attack": "sorrow touch", "strong_attack": "weeping gale", "player_abilities": ["lv2_hostile_ability_water_dark_magic_gloom_tide", "level_1_hostile_ability_fire_faith_hearthsong"], "base_str":4, "base_dex":6, "base_con":8, "base_int":12, "base_hp":260, "base_ap":12, "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":3},

 {"id": "lichen_gargoyle", "name": "Lichen Gargoyle", "hostile_type": "construct", "role": "support", "min_spawn_level":10, "rarity": "superrare", "base_xp":480, "common_drop": "stimulant_med", "rare_drop": "reinforced_helmet", "money_range": (18,100),
 "basic_attack": "stone peck", "strong_attack": "crushing wing", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"], "base_str":12, "base_dex":3, "base_con":14, "base_int":1, "base_hp":320, "base_ap":10, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},
]