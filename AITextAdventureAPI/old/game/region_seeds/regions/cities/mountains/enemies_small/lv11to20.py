# Level11-20 hostile seeds for Hollerforge Hollow (small-city)
# Export a list named SEEDS_LV11TO20 used by constants_enemies_small_city.py
# Organized by min_spawn_level ascending and adjusted rarities for dispersity.
SEEDS_LV11TO20 = [
 {"id": "hollow_savant", "name": "Hollow Savant", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":11, "rarity": "rare", "base_xp":220,
 "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (30,140),
 "basic_attack": "spent rune", "strong_attack": "mind latch", "player_abilities": ["lv2_hostile_ability_dark_air_skill_nightmare_wave", "lv2_hostile_ability_dark_dark_faith_void_veil"],
 "base_str":2, "base_dex":3, "base_con":4, "base_int":12, "base_hp":110, "base_ap":9,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "ore_scrapper", "name": "Ore Scrapper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":48,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,36),
 "basic_attack": "gravel jab", "strong_attack": "pick smash", "player_abilities": None,
 "base_str":5, "base_dex":2, "base_con":5, "base_int":1, "base_hp":80, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "marauder_matriarch", "name": "Marauder Matriarch", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "rare", "base_xp":180,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40,160),
 "basic_attack": "maw of the clan", "strong_attack": "wrathful onslaught", "player_abilities": ["earth_fire_technique_lv2_berserker_tech"],
 "base_str":7, "base_dex":4, "base_con":6, "base_int":3, "base_hp":90, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 {"id": "pickaxe_ganger", "name": "Pickaxe Ganger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "uncommon", "base_xp":80,
 "common_drop": "herb_med", "rare_drop": "cloth_gloves", "money_range": (12,48),
 "basic_attack": "side swing", "strong_attack": "pit cleave", "player_abilities": None,
 "base_str":6, "base_dex":3, "base_con":6, "base_int":1, "base_hp":120, "base_ap":5,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "ridge_hulker", "name": "Ridge Hulker", "hostile_type": "creature", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (10,44),
 "basic_attack": "tackle", "strong_attack": "rock maul", "player_abilities": None,
 "base_str":7, "base_dex":3, "base_con":6, "base_int":1, "base_hp":140, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "ember_drake", "name": "Ember Drake", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "uncommon", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40,180),
 "basic_attack": "scalding snap", "strong_attack": "molten breath", "player_abilities": ["lv2_hostile_ability_dark_electric_magic_abyssal_storm"],
 "base_str":9, "base_dex":6, "base_con":8, "base_int":4, "base_hp":200, "base_ap":6,
 "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "slag_rodent", "name": "Slag Rodent", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "common", "base_xp":40,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (6,28),
 "basic_attack": "nibble", "strong_attack": "acidic bite", "player_abilities": None,
 "base_str":3, "base_dex":4, "base_con":3, "base_int":1, "base_hp":60, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "hollow_colossus", "name": "Hollow Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":15, "rarity": "rare", "base_xp":340,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (60,260),
 "basic_attack": "piston slam", "strong_attack": "hydraulic stomp", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":12, "base_dex":2, "base_con":14, "base_int":2, "base_hp":260, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "dream_stag", "name": "Dream Stag", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":16, "rarity": "superrare", "base_xp":480,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,320),
 "basic_attack": "antler gouge", "strong_attack": "maddening charge", "player_abilities": ["lv2_hostile_ability_dark_air_skill_nightmare_wave"],
 "base_str":8, "base_dex":8, "base_con":8, "base_int":10, "base_hp":260, "base_ap":12,
 "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":3},

 {"id": "forge_warden", "name": "Forge Warden", "hostile_type": "construct", "role": "support", "min_spawn_level":17, "rarity": "uncommon", "base_xp":520,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,340),
 "basic_attack": "anvil strike", "strong_attack": "seismic core", "player_abilities": ["level_1_hostile_ability_reinforce_frame", "earth_electric_lv2_technique_chain_reactor"],
 "base_str":14, "base_dex":3, "base_con":16, "base_int":4, "base_hp":360, "base_ap":8,
 "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":1},

 {"id": "timber_wyrm", "name": "Timber Wyrm", "hostile_type": "eldritch", "role": "damage", "min_spawn_level":18, "rarity": "uncommon", "base_xp":600,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (120,480),
 "basic_attack": "timber lash", "strong_attack": "rooted cataclysm", "player_abilities": ["earth_fire_technique_lv2_berserker_tech", "level_1_hostile_ability_inspire"],
 "base_str":12, "base_dex":6, "base_con":14, "base_int":8, "base_hp":400, "base_ap":12,
 "str_per_level":4, "dex_per_level":1, "con_per_level":3, "int_per_level":2},

 {"id": "vein_warden", "name": "Vein Warden", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":19, "rarity": "uncommon", "base_xp":420,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (60,260),
 "basic_attack": "sunder", "strong_attack": "vein rupture", "player_abilities": None,
 "base_str":9, "base_dex":4, "base_con":10, "base_int":2, "base_hp":240, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":0},

 {"id": "deep_miner", "name": "Deep Miner", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":20, "rarity": "common", "base_xp":460,
 "common_drop": "stimulant_large", "rare_drop": "cloth_gloves", "money_range": (80,300),
 "basic_attack": "shovel bash", "strong_attack": "quarry charge", "player_abilities": None,
 "base_str":8, "base_dex":3, "base_con":12, "base_int":2, "base_hp":260, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},
]
