# Level11-20 hostile seeds for Boiling Bubble (mid-city witch district)
# Split out from constants_enemies_mid_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==11
 {"id": "grove_raider", "name": "Grove Raider", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (20,88),
 "basic_attack": "scrabbling swipe", "strong_attack": "bramble pummel", "player_abilities": None,
 "base_str":7, "base_dex":6, "base_con":6, "base_int":2, "base_hp":160, "base_ap":6,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "twilight_harrier", "name": "Twilight Harrier", "hostile_type": "creature", "role": "damage", "min_spawn_level":11, "rarity": "uncommon", "base_xp":140,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (24,96),
 "basic_attack": "grazing talon", "strong_attack": "dusken dive", "player_abilities": None,
 "base_str":8, "base_dex":8, "base_con":5, "base_int":3, "base_hp":150, "base_ap":7,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # min_spawn_level ==12
 {"id": "mire_picker", "name": "Mire Picker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":140,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (30,120),
 "basic_attack": "mud jab", "strong_attack": "sludge toss", "player_abilities": None,
 "base_str":6, "base_dex":4, "base_con":8, "base_int":2, "base_hp":180, "base_ap":6,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "woodland_wrecker", "name": "Woodland Wrecker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "rare", "base_xp":220,
 "common_drop": "herb_major", "rare_drop": "sawed_off", "money_range": (40,180),
 "basic_attack": "haymaker", "strong_attack": "wrecking ball", "player_abilities": ["earth_fire_technique_lv2_berserker_tech"],
 "base_str":10, "base_dex":3, "base_con":8, "base_int":1, "base_hp":140, "base_ap":6,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==13
 {"id": "root_forger", "name": "Root Forger", "hostile_type": "construct", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":160,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (32,128),
 "basic_attack": "sap slam", "strong_attack": "ironroot crush", "player_abilities": None,
 "base_str":9, "base_dex":2, "base_con":10, "base_int":2, "base_hp":200, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "clockwork_hunter", "name": "Clockwork Hunter", "hostile_type": "construct", "role": "damage", "min_spawn_level":13, "rarity": "uncommon", "base_xp":180,
 "common_drop": "stimulant_med", "rare_drop": None, "money_range": (34,140),
 "basic_attack": "gear bite", "strong_attack": "pressure maul", "player_abilities": None,
 "base_str":10, "base_dex":4, "base_con":9, "base_int":2, "base_hp":220, "base_ap":5,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==14
 {"id": "mist_whisper", "name": "Mist Whisper", "hostile_type": "fey", "role": "damage", "min_spawn_level":14, "rarity": "uncommon", "base_xp":200,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (36,160),
 "basic_attack": "murmer jab", "strong_attack": "shroud lash", "player_abilities": ["ice_skill_lv1_ice_shuriken"],
 "base_str":4, "base_dex":10, "base_con":3, "base_int":6, "base_hp":180, "base_ap":8,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":2},

 {"id": "dream_eater4", "name": "Dream Eater", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":14, "rarity": "rare", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,320),
 "basic_attack": "mind gnaw", "strong_attack": "maddening shriek", "player_abilities": ["lv2_hostile_ability_dark_air_skill_nightmare_wave"],
 "base_str":4, "base_dex":6, "base_con":6, "base_int":16, "base_hp":160, "base_ap":14,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":4},

 # min_spawn_level ==15
 {"id": "iron_bark", "name": "Iron Bark", "hostile_type": "creature", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":200,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (40,160),
 "basic_attack": "bark swipe", "strong_attack": "iron root slam", "player_abilities": None,
 "base_str":12, "base_dex":3, "base_con":12, "base_int":2, "base_hp":240, "base_ap":8,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "reclaimed_clockwork_colossus", "name": "Reclaimed Clockwork Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":15, "rarity": "rare", "base_xp":320,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (60,220),
 "basic_attack": "piston swing", "strong_attack": "hydraulic crush", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"],
 "base_str":16, "base_dex":2, "base_con":18, "base_int":1, "base_hp":320, "base_ap":3,
 "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 # min_spawn_level ==16
 {"id": "dryad_femme_fatale", "name": "Dryad Femme Fatale", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":16, "rarity": "superrare", "base_xp":520,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (120,480),
 "basic_attack": "elegant stab", "strong_attack": "fatal flourish", "player_abilities": ["lv2_hostile_ability_earth_light_tech_primal_disunion"],
 "base_str":9, "base_dex":11, "base_con":6, "base_int":8, "base_hp":200, "base_ap":12,
 "str_per_level":3, "dex_per_level":4, "con_per_level":2, "int_per_level":3},

 {"id": "root_shield", "name": "Root Shield", "hostile_type": "humanoid", "role": "support", "min_spawn_level":16, "rarity": "common", "base_xp":220,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (80,300),
 "basic_attack": "warding bash", "strong_attack": "bark guard", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"],
 "base_str":10, "base_dex":4, "base_con":10, "base_int":3, "base_hp":260, "base_ap":8,
 "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":1},

 # min_spawn_level ==17
 {"id": "briar_stalker", "name": "Briar Stalker", "hostile_type": "creature", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":240,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (90,360),
 "basic_attack": "lunge and slash", "strong_attack": "entangling pounce", "player_abilities": None,
 "base_str":11, "base_dex":9, "base_con":9, "base_int":4, "base_hp":300, "base_ap":9,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 {"id": "thorn_shade", "name": "Thorn Shade", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":17, "rarity": "uncommon", "base_xp":240,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (90,360),
 "basic_attack": "dark tendril", "strong_attack": "vanishing thorn", "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
 "base_str":8, "base_dex":10, "base_con":7, "base_int":6, "base_hp":240, "base_ap":9,
 "str_per_level":2, "dex_per_level":3, "con_per_level":2, "int_per_level":1},

 # min_spawn_level ==18
 {"id": "sprig_reaver", "name": "Sprig Reaver", "hostile_type": "creature", "role": "damage", "min_spawn_level":18, "rarity": "common", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (100,400),
 "basic_attack": "branch rend", "strong_attack": "sprig maul", "player_abilities": None,
 "base_str":12, "base_dex":8, "base_con":10, "base_int":4, "base_hp":340, "base_ap":10,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 {"id": "lumen_guard", "name": "Lumen Guard", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":18, "rarity": "uncommon", "base_xp":320,
 "common_drop": "stimulant_med", "rare_drop": None, "money_range": (110,420),
 "basic_attack": "gleam strike", "strong_attack": "luminary volley", "player_abilities": ["level_1_hostile_ability_light_faith_prism_burst"],
 "base_str":9, "base_dex":8, "base_con":9, "base_int":6, "base_hp":320, "base_ap":10,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 # min_spawn_level ==19
 {"id": "night_stag", "name": "Night Stag", "hostile_type": "creature", "role": "damage", "min_spawn_level":19, "rarity": "common", "base_xp":340,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (120,480),
 "basic_attack": "antler gore", "strong_attack": "phosphor stomp", "player_abilities": None,
 "base_str":13, "base_dex":9, "base_con":10, "base_int":5, "base_hp":360, "base_ap":11,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 {"id": "nocturne_revenant", "name": "Nocturne Revenant", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":19, "rarity": "rare", "base_xp":360,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (120,480),
 "basic_attack": "ethereal stomp", "strong_attack": "void collapse", "player_abilities": ["level_1_hostile_ability_night_whisper"],
 "base_str":10, "base_dex":10, "base_con":10, "base_int":8, "base_hp":380, "base_ap":12,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 # min_spawn_level ==20
 {"id": "elder_watch", "name": "Elder Watch", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":20, "rarity": "common", "base_xp":400,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (150,700),
 "basic_attack": "commanding strike", "strong_attack": "overseer barrage", "player_abilities": None,
 "base_str":12, "base_dex":8, "base_con":12, "base_int":6, "base_hp":420, "base_ap":12,
 "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 {"id": "dusk_warden", "name": "Dusk Warden", "hostile_type": "construct", "role": "support", "min_spawn_level":20, "rarity": "uncommon", "base_xp":420,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (150,700),
 "basic_attack": "twilight crush", "strong_attack": "dusken cataclysm", "player_abilities": ["air_earth_tech_lv5_reinforce_frame", "earth_fire_technique_lv2_berserker_tech"],
 "base_str":14, "base_dex":6, "base_con":14, "base_int":6, "base_hp":420, "base_ap":12,
 "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":2},
 ]
