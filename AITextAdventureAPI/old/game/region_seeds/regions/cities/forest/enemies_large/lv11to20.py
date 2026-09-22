# Level11-20 hostile seeds for Aurelion Veil (forest city)
# Split out from constants_enemies_large_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==11
 {"id": "elder_tentacle", "name": "Elder Tendril", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":11, "rarity": "rare", "base_xp":260,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (30,140),
 "basic_attack": "slick lash", "strong_attack": "barbed crush", "player_abilities": ["lv2_hostile_ability_dark_electric_magic_abyssal_storm"],
 "base_str":12, "base_dex":2, "base_con":10, "base_int":2, "base_hp":160, "base_ap":6,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "moss_lurker", "name": "Moss Lurker", "hostile_type": "creature", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (18,72),
 "basic_attack": "mossy slap", "strong_attack": "spore burst", "player_abilities": None,
 "base_str":6, "base_dex":4, "base_con":6, "base_int":2, "base_hp":140, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==12
 {"id": "willow_witch", "name": "Willow Witch", "hostile_type": "humanoid", "role": "support", "min_spawn_level":12, "rarity": "rare", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (50,200),
 "basic_attack": "whisper charm", "strong_attack": "binding sorrow", "player_abilities": ["level_1_hostile_ability_night_whisper", "light_spirit_lv1_minor_heal"],
 "base_str":2, "base_dex":3, "base_con":5, "base_int":12, "base_hp":140, "base_ap":10,
 "str_per_level":0, "dex_per_level":1, "con_per_level":2, "int_per_level":3},

 {"id": "thorn_mender", "name": "Thorn Mender", "hostile_type": "humanoid", "role": "support", "min_spawn_level":12, "rarity": "common", "base_xp":140,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (22,96),
 "basic_attack": "prickly stitch", "strong_attack": "entangling weave", "player_abilities": ["water_spirit_lv1_mending_streams"],
 "base_str":4, "base_dex":4, "base_con":6, "base_int":4, "base_hp":160, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 # min_spawn_level ==13
 {"id": "root_golem", "name": "Root Golem", "hostile_type": "construct", "role": "support", "min_spawn_level":13, "rarity": "rare", "base_xp":340,
 "common_drop": "stimulant_med", "rare_drop": "kevlar_vest", "money_range": (40,180),
 "basic_attack": "piston club", "strong_attack": "root slam", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"],
 "base_str":14, "base_dex":1, "base_con":16, "base_int":1, "base_hp":260, "base_ap":5,
 "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "bramble_colt", "name": "Bramble Colt", "hostile_type": "creature", "role": "damage", "min_spawn_level":13, "rarity": "uncommon", "base_xp":160,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (24,110),
 "basic_attack": "thorn kick", "strong_attack": "bramble rush", "player_abilities": None,
 "base_str":6, "base_dex":8, "base_con":5, "base_int":2, "base_hp":140, "base_ap":6,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==14
 {"id": "dreamstalker", "name": "Dreamstalker", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":14, "rarity": "rare", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,320),
 "basic_attack": "suffocating lull", "strong_attack": "nightmare release", "player_abilities": ["lv2_hostile_ability_dark_air_skill_nightmare_wave", "dark_magic_lv5_abyssal_shadow"],
 "base_str":4, "base_dex":6, "base_con":6, "base_int":16, "base_hp":180, "base_ap":12,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":4},

 {"id": "mist_sprite", "name": "Mist Sprite", "hostile_type": "fey", "role": "hazard", "min_spawn_level":14, "rarity": "common", "base_xp":160,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (20,80),
 "basic_attack": "hiss and dash", "strong_attack": "shroud serenade", "player_abilities": ["ice_skill_lv1_ice_shuriken"],
 "base_str":2, "base_dex":10, "base_con":2, "base_int":6, "base_hp":120, "base_ap":6,
 "str_per_level":0, "dex_per_level":3, "con_per_level":0, "int_per_level":2},

 # min_spawn_level ==15
 {"id": "gear_ent", "name": "Gear Ent", "hostile_type": "construct", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":200,
 "common_drop": "cloth_gloves", "rare_drop": None, "money_range": (40,160),
 "basic_attack": "gear slam", "strong_attack": "magnetic crush", "player_abilities": None,
 "base_str":8, "base_dex":3, "base_con":8, "base_int":2, "base_hp":180, "base_ap":6,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "iron_talon", "name": "Iron Talon", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":15, "rarity": "uncommon", "base_xp":200,
 "common_drop": "stimulant_small", "rare_drop": "dagger", "money_range": (36,140),
 "basic_attack": "steel swipe", "strong_attack": "talon dive", "player_abilities": None,
 "base_str":7, "base_dex":6, "base_con":6, "base_int":3, "base_hp":200, "base_ap":7,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 # min_spawn_level ==16
 {"id": "vine_colossus", "name": "Vine Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":16, "rarity": "superrare", "base_xp":520,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (100,400),
 "basic_attack": "massive swipe", "strong_attack": "entangling crush", "player_abilities": ["earth_electric_lv2_technique_chain_reactor"],
 "base_str":18, "base_dex":2, "base_con":20, "base_int":2, "base_hp":420, "base_ap":6,
 "str_per_level":5, "dex_per_level":0, "con_per_level":4, "int_per_level":0},

 {"id": "root_sentinal", "name": "Root Sentinal", "hostile_type": "humanoid", "role": "support", "min_spawn_level":16, "rarity": "common", "base_xp":220,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (80,300),
 "basic_attack": "warding swipe", "strong_attack": "dune shield", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"],
 "base_str":9, "base_dex":6, "base_con":9, "base_int":3, "base_hp":220, "base_ap":8,
 "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":1},

 # min_spawn_level ==17
 {"id": "shadow_briar", "name": "Shadow Briar", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":17, "rarity": "uncommon", "base_xp":240,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (90,360),
 "basic_attack": "dark tendril", "strong_attack": "vanishing thorn", "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
 "base_str":8, "base_dex":10, "base_con":7, "base_int":6, "base_hp":240, "base_ap":9,
 "str_per_level":2, "dex_per_level":3, "con_per_level":2, "int_per_level":1},

 {"id": "baron_of_leaves", "name": "Baron of Leaves", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":220,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (90,360),
 "basic_attack": "polished strike", "strong_attack": "noble onslaught", "player_abilities": None,
 "base_str":10, "base_dex":6, "base_con":9, "base_int":4, "base_hp":240, "base_ap":9,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 # min_spawn_level ==18
 {"id": "starwarden", "name": "Starwarden", "hostile_type": "celestial", "role": "support", "min_spawn_level":18, "rarity": "uncommon", "base_xp":600,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (120,480),
 "basic_attack": "stellar talons", "strong_attack": "meteor flare", "player_abilities": ["light_light_spirit_lv2_seraphic_nova"],
 "base_str":12, "base_dex":8, "base_con":12, "base_int":10, "base_hp":360, "base_ap":12,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":3},

 {"id": "sky_bloom", "name": "Sky Bloom", "hostile_type": "fey", "role": "damage", "min_spawn_level":18, "rarity": "common", "base_xp":260,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (100,400),
 "basic_attack": "bloom lash", "strong_attack": "petal storm", "player_abilities": None,
 "base_str":6, "base_dex":8, "base_con":6, "base_int":4, "base_hp":300, "base_ap":8,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 # min_spawn_level ==19
 {"id": "hollow_stag", "name": "Hollow Stag", "hostile_type": "creature", "role": "damage", "min_spawn_level":19, "rarity": "common", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (120,480),
 "basic_attack": "antler gore", "strong_attack": "phosphor stomp", "player_abilities": None,
 "base_str":11, "base_dex":8, "base_con":9, "base_int":5, "base_hp":320, "base_ap":10,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 {"id": "night_warden", "name": "Night Warden", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":19, "rarity": "uncommon", "base_xp":260,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (80,320),
 "basic_attack": "ethereal swipe", "strong_attack": "void grasp", "player_abilities": ["level_1_hostile_ability_night_whisper"], "base_str":6, "base_dex":9, "base_con":6, "base_int":8, "base_hp":280, "base_ap":10,
 "str_per_level":2, "dex_per_level":3, "con_per_level":2, "int_per_level":2},

 # min_spawn_level ==20
 {"id": "elder_guard", "name": "Elder Guard", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":20, "rarity": "common", "base_xp":340,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (150,700),
 "basic_attack": "commanding strike", "strong_attack": "overseer barrage", "player_abilities": None,
 "base_str":10, "base_dex":8, "base_con":9, "base_int":5, "base_hp":320, "base_ap":10,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 {"id": "dusk_colossus", "name": "Dusk Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":20, "rarity": "uncommon", "base_xp":420,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (150,700),
 "basic_attack": "twilight crush", "strong_attack": "dusken cataclysm", "player_abilities": ["level_1_hostile_ability_reinforce_frame", "earth_fire_technique_lv2_berserker_tech"],
 "base_str":12, "base_dex":6, "base_con":12, "base_int":6, "base_hp":420, "base_ap":12,
 "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":2},
]
