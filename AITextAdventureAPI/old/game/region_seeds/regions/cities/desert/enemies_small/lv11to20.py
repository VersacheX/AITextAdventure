# Level11-20 hostile seeds for BioHazard (small city)
# Split out from constants_enemies_small_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==11
 {"id": "scrap_raider", "name": "Scrap Raider", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":80,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (10,48),
 "basic_attack": "shard jab", "strong_attack": "gutting bash", "player_abilities": None,
 "base_str":5, "base_dex":5, "base_con":4, "base_int":2, "base_hp":88, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "pawn_stalker", "name": "Pawn Stalker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "uncommon", "base_xp":96,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (12,56),
 "basic_attack": "shadow nibble", "strong_attack": "bleeding rip", "player_abilities": [],
 "base_str":4, "base_dex":7, "base_con":4, "base_int":3, "base_hp":96, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==12
 {"id": "wasteland_wrecker", "name": "Wasteland Wrecker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "rare", "base_xp":220,
 "common_drop": "stimulant_large", "rare_drop": "sawed_off", "money_range": (50,200),
 "basic_attack": "ram and smash", "strong_attack": "cataclysmic swing", "player_abilities": ["fire_technique_lv4_berserker_tech"],
 "base_str":10, "base_dex":2, "base_con":8, "base_int":1, "base_hp":140, "base_ap":6,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0, "resistances": [], "immunities": [], "weaknesses": []},

 {"id": "sand_scrapper", "name": "Sand Scrapper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (20,88),
 "basic_attack": "scrape and shove", "strong_attack": "dune sweep", "player_abilities": None,
 "base_str":6, "base_dex":4, "base_con":5, "base_int":2, "base_hp":120, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==13
 {"id": "dune_enforcer", "name": "Dune Enforcer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":140,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (22,96),
 "basic_attack": "sandy cleave", "strong_attack": "mauling charge", "player_abilities": None,
 "base_str":7, "base_dex":4, "base_con":6, "base_int":2, "base_hp":140, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "scrap_shaman", "name": "Scrap Shaman", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":13, "rarity": "uncommon", "base_xp":150,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (30,140),
 "basic_attack": "rattle and curse", "strong_attack": "metallic hex", "player_abilities": ["dark_magic_lv2_night_whisper", "fire_magic_lv1_fireball"],
 "base_str":1, "base_dex":3, "base_con":3, "base_int":10, "base_hp":60, "base_ap":8,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 # min_spawn_level ==14
 {"id": "elite_mad_mechanic", "name": "Elite Mad Mechanic", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":14, "rarity": "rare", "base_xp":180,
 "common_drop": "stimulant_large", "rare_drop": "energy_pistol", "money_range": (45,180),
 "basic_attack": "wrench flurry", "strong_attack": "overclocked blast", "player_abilities": ["fire_water_tech_lv2_steam_grenade", "air_fire_magic_lv4_chain_lightning"],
 "base_str":4, "base_dex":6, "base_con":4, "base_int":10, "base_hp":80, "base_ap":8,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":3},

 {"id": "silt_runner", "name": "Silt Runner", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "uncommon", "base_xp":130,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (24,110),
 "basic_attack": "slashing bite", "strong_attack": "spine lunge", "player_abilities": None,
 "base_str":6, "base_dex":7, "base_con":5, "base_int":1, "base_hp":140, "base_ap":5,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==15
 {"id": "gear_goliath", "name": "Gear Goliath", "hostile_type": "creature", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":180,
 "common_drop": "cloth_gloves", "rare_drop": None, "money_range": (40,160),
 "basic_attack": "gear crush", "strong_attack": "spinning maul", "player_abilities": None,
 "base_str":8, "base_dex":4, "base_con":8, "base_int":2, "base_hp":180, "base_ap":6,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "vault_guardian", "name": "Vault Guardian", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":15, "rarity": "uncommon", "base_xp":160,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (30,120),
 "basic_attack": "silent pry", "strong_attack": "vault slam", "player_abilities": ["dark_magic_lv1_shadow_tendril"],
 "base_str":5, "base_dex":6, "base_con":6, "base_int":4, "base_hp":160, "base_ap":7,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # min_spawn_level ==16
 {"id": "scrap_colossus", "name": "Scrap Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":16, "rarity": "superrare", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (120,480),
 "basic_attack": "piston slam", "strong_attack": "mag-throw", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"],
 "base_str":16, "base_dex":2, "base_con":18, "base_int":1, "base_hp":320, "base_ap":4,
 "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "iron_wrangler", "name": "Iron Wrangler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":16, "rarity": "common", "base_xp":200,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (80,300),
 "basic_attack": "welding swipe", "strong_attack": "cauterize crush", "player_abilities": None,
 "base_str":9, "base_dex":4, "base_con":9, "base_int":2, "base_hp":200, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==17
 {"id": "barrow_keeper", "name": "Barrow Keeper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":220,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (90,360),
 "basic_attack": "polished strike", "strong_attack": "noble onslaught", "player_abilities": None,
 "base_str":10, "base_dex":6, "base_con":9, "base_int":4, "base_hp":240, "base_ap":9,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 {"id": "shadow_knitter", "name": "Shadow Knitter", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":17, "rarity": "uncommon", "base_xp":200,
 "common_drop": "herb_med", "rare_drop": "lockpick", "money_range": (60,240),
 "basic_attack": "dark slash", "strong_attack": "vanishing strike", "player_abilities": ["shadow_flicker"],
 "base_str":7, "base_dex":12, "base_con":6, "base_int":5, "base_hp":220, "base_ap":8,
 "str_per_level":2, "dex_per_level":3, "con_per_level":2, "int_per_level":1},

 # min_spawn_level ==18
 {"id": "bone_crusher_small", "name": "Bone Crusher", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":18, "rarity": "common", "base_xp":260,
 "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (100,400),
 "basic_attack": "crushing blow", "strong_attack": "bone shatter", "player_abilities": None,
 "base_str":12, "base_dex":4, "base_con":10, "base_int":2, "base_hp":300, "base_ap":8,
 "str_per_level":4, "dex_per_level":1, "con_per_level":3, "int_per_level":0},

 {"id": "shade_sentry", "name": "Shade Sentry", "hostile_type": "humanoid", "role": "support", "min_spawn_level":18, "rarity": "rare", "base_xp":280,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (110,420),
 "basic_attack": "guard charge", "strong_attack": "stunning volley", "player_abilities": ["reinforce_frame"],
 "base_str":8, "base_dex":6, "base_con":10, "base_int":4, "base_hp":260, "base_ap":10,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 # min_spawn_level ==19
 {"id": "sand_overseer_small", "name": "Sand Overseer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":19, "rarity": "common", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (120,480),
 "basic_attack": "commanding strike", "strong_attack": "overseer barrage", "player_abilities": None,
 "base_str":10, "base_dex":8, "base_con":9, "base_int":5, "base_hp":320, "base_ap":10,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 {"id": "sand_phantom_small", "name": "Sand Phantom", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":19, "rarity": "uncommon", "base_xp":260,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (80,320),
 "basic_attack": "ethereal swipe", "strong_attack": "void grasp", "player_abilities": ["night_whisper"],
 "base_str":6, "base_dex":9, "base_con":6, "base_int":8, "base_hp":280, "base_ap":10,
 "str_per_level":2, "dex_per_level":3, "con_per_level":2, "int_per_level":2},

 # min_spawn_level ==20
 {"id": "dune_champion_small", "name": "Dune Champion", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":20, "rarity": "common", "base_xp":340,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (150,700),
 "basic_attack": "champion's cleave", "strong_attack": "earthshatter", "player_abilities": None,
 "base_str":12, "base_dex":8, "base_con":12, "base_int":6, "base_hp":380, "base_ap":12,
 "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 {"id": "dune_lieutenant_small", "name": "Dune Lieutenant", "hostile_type": "humanoid", "role": "support", "min_spawn_level":20, "rarity": "rare", "base_xp":420,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (150,700),
 "basic_attack": "ruthless sand-strikes", "strong_attack": "lieutenant's onslaught", "player_abilities": ["inspire", "berserker_tech"],
 "base_str":9, "base_dex":6, "base_con":9, "base_int":5, "base_hp":220, "base_ap":10,
 "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":2},
]
