# Level11-20 hostile seeds for Gallows Rift (mid-city)
# Export a list named SEEDS_LV11TO20 used by constants_enemies_mid_city.py
# Organized by min_spawn_level ascending and adjusted rarities for dispersity.
SEEDS_LV11TO20 = [
 # min_spawn_level =11
 {"id": "slate_golem", "name": "Slate Golem", "hostile_type": "construct", "role": "damage", "min_spawn_level":11, "rarity": "rare", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40,180),
 "basic_attack": "slag swipe", "strong_attack": "vulcan crush", "player_abilities": None,
 "base_str":10, "base_dex":3, "base_con":10, "base_int":2, "base_hp":220, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "abyssal_serpent", "name": "Abyssal Serpent", "hostile_type": "creature", "role": "damage", "min_spawn_level":11, "rarity": "uncommon", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40,180),
 "basic_attack": "maw lash", "strong_attack": "constrict", "player_abilities": ["abyssal_storm"],
 "base_str":10, "base_dex":7, "base_con":9, "base_int":2, "base_hp":220, "base_ap":6,
 "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":0},

 {"id": "scrap_rat", "name": "Scrap Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":30,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,10),
 "basic_attack": "scratches", "strong_attack": "rabid bite", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":1, "base_hp":28, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "alder_sentry", "name": "Alder Sentry", "hostile_type": "humanoid", "role": "support", "min_spawn_level":11, "rarity": "common", "base_xp":34,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (4,14),
 "basic_attack": "sweep", "strong_attack": "guard strike", "player_abilities": None,
 "base_str":3, "base_dex":3, "base_con":3, "base_int":1, "base_hp":32, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 # min_spawn_level =12
 {"id": "party_rivet_fiend", "name": "Party Rivet Fiend", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "uncommon", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": "sawed_off", "money_range": (30,160),
 "basic_attack": "crashes with pipe", "strong_attack": "wrecking chain", "player_abilities": ["berserker_tech"],
 "base_str":8, "base_dex":2, "base_con":8, "base_int":1, "base_hp":100, "base_ap":6,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "mindflayer", "name": "Mindflayer", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":12, "rarity": "superrare", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,220),
 "basic_attack": "psychic tendrils", "strong_attack": "psychic pulse", "player_abilities": ["dark_magic_lv5_abyssal_shadow"],
 "base_str":2, "base_dex":3, "base_con":3, "base_int":14, "base_hp":80, "base_ap":12,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":4},

 {"id": "wandering_lich_apprentice", "name": "Wandering Lich Apprentice", "hostile_type": "undead", "role": "hazard", "min_spawn_level":12, "rarity": "rare", "base_xp":320,
 "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (30,140),
 "basic_attack": "bone bolt", "strong_attack": "necrotic spear", "player_abilities": ["bone_spear"],
 "base_str":2, "base_dex":3, "base_con":4, "base_int":12, "base_hp":100, "base_ap":10,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "stone_imperial", "name": "Stone Imperial", "hostile_type": "construct", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":60,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,28),
 "basic_attack": "punch", "strong_attack": "seismic stomp", "player_abilities": None,
 "base_str":6, "base_dex":1, "base_con":6, "base_int":1, "base_hp":80, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # min_spawn_level =13
 {"id": "highland_wrecker", "name": "Highland Wrecker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":13, "rarity": "uncommon", "base_xp":150,
 "common_drop": "herb_major", "rare_drop": "sawed_off", "money_range": (30,160),
 "basic_attack": "haymaker", "strong_attack": "wrecking ball", "player_abilities": None,
 "base_str":7, "base_dex":2, "base_con":5, "base_int":1, "base_hp":70, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "magma_serpent2", "name": "Magma Serpent", "hostile_type": "creature", "role": "damage", "min_spawn_level":13, "rarity": "uncommon", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (30,140),
 "basic_attack": "scalding snap", "strong_attack": "molten constrict", "player_abilities": ["abyssal_storm"],
 "base_str":9, "base_dex":6, "base_con":8, "base_int":3, "base_hp":180, "base_ap":6,
 "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "charred_hound", "name": "Charred Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":70,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (6,30),
 "basic_attack": "flame snap", "strong_attack": "ember maul", "player_abilities": None,
 "base_str":5, "base_dex":6, "base_con":4, "base_int":1, "base_hp":60, "base_ap":4,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # min_spawn_level =14
 {"id": "enforcer_heavy", "name": "Heavy Enforcer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":14, "rarity": "uncommon", "base_xp":160,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (40,140),
 "basic_attack": "smashes with a maul", "strong_attack": "cataclysmic slam", "player_abilities": None,
 "base_str":9, "base_dex":2, "base_con":7, "base_int":1, "base_hp":90, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "steamwork_colossus", "name": "Steamwork Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":14, "rarity": "rare", "base_xp":320,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (60,220),
 "basic_attack": "piston swing", "strong_attack": "hydraulic crush", "player_abilities": ["reinforce_frame"],
 "base_str":14, "base_dex":1, "base_con":18, "base_int":1, "base_hp":300, "base_ap":3,
 "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "iron_scout", "name": "Iron Scout", "hostile_type": "construct", "role": "damage", "min_spawn_level":14, "rarity": "common", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (10,36),
 "basic_attack": "clank jab", "strong_attack": "servo slash", "player_abilities": None,
 "base_str":6, "base_dex":3, "base_con":6, "base_int":1, "base_hp":88, "base_ap":3,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 # min_spawn_level =15
 {"id": "dream_eater6", "name": "Dream Eater", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":15, "rarity": "uncommon", "base_xp":480,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,280),
 "basic_attack": "mind gnaw", "strong_attack": "maddening shriek", "player_abilities": ["nightmare_wave"],
 "base_str":3, "base_dex":6, "base_con":5, "base_int":14, "base_hp":140, "base_ap":14,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":4},

 {"id": "dream_smoke", "name": "Dream Smoke", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":15, "rarity": "common", "base_xp":480,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,280),
 "basic_attack": "mind-scent wisp", "strong_attack": "maddening swirl", "player_abilities": ["nightmare_wave"],
 "base_str":2, "base_dex":6, "base_con":4, "base_int":14, "base_hp":140, "base_ap":12,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":4},

 {"id": "dream_eater_prime", "name": "Dream Eater Prime", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":15, "rarity": "common", "base_xp":480,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,280),
 "basic_attack": "mind gnaw", "strong_attack": "maddening shriek", "player_abilities": ["nightmare_wave"],
 "base_str":4, "base_dex":6, "base_con":6, "base_int":16, "base_hp":180, "base_ap":16,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":4},

 {"id": "underground_market_dealer", "name": "Underground Market Dealer", "hostile_type": "humanoid", "role": "support", "min_spawn_level":15, "rarity": "rare", "base_xp":200,
 "common_drop": "stimulant_large", "rare_drop": "stimulant_large", "money_range": (60,260),
 "basic_attack": "slick trade", "strong_attack": "underhand strike", "player_abilities": ["primal_unison"],
 "base_str":3, "base_dex":4, "base_con":3, "base_int":6, "base_hp":48, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 # min_spawn_level =16
 {"id": "forge_colossus", "name": "Forge Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":16, "rarity": "common", "base_xp":520,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,340),
 "basic_attack": "anvil swing", "strong_attack": "seismic crush", "player_abilities": ["reinforce_frame"],
 "base_str":14, "base_dex":2, "base_con":16, "base_int":2, "base_hp":320, "base_ap":6,
 "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":1},

 {"id": "ravine_stalker", "name": "Ravine Stalker", "hostile_type": "creature", "role": "damage", "min_spawn_level":16, "rarity": "uncommon", "base_xp":240,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (20,90),
 "basic_attack": "lunge and slash", "strong_attack": "ferocious maul", "player_abilities": ["venom_trace"],
 "base_str":8, "base_dex":6, "base_con":7, "base_int":2, "base_hp":160, "base_ap":6,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 # min_spawn_level =17
 {"id": "bridge_reaver", "name": "Bridge Reaver", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":17, "rarity": "uncommon", "base_xp":280,
 "common_drop": "lockpick", "rare_drop": "cloth_gloves", "money_range": (30,120),
 "basic_attack": "slashes with cleaver", "strong_attack": "bridge smash", "player_abilities": ["berserker_tech"],
 "base_str":9, "base_dex":4, "base_con":8, "base_int":1, "base_hp":200, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "cliff_phantom", "name": "Cliff Phantom", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":17, "rarity": "rare", "base_xp":360,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (25,140),
 "basic_attack": "ethereal swipe", "strong_attack": "voiding shriek", "player_abilities": ["night_whisper"],
 "base_str":2, "base_dex":6, "base_con":4, "base_int":12, "base_hp":220, "base_ap":8,
 "str_per_level":0, "dex_per_level":2, "con_per_level":1, "int_per_level":3},

 # min_spawn_level =18
 {"id": "pit_lieutenant", "name": "Pit Lieutenant", "hostile_type": "humanoid", "role": "support", "min_spawn_level":18, "rarity": "rare", "base_xp":600,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (100,420),
 "basic_attack": "ruthless barrage", "strong_attack": "commanding roar", "player_abilities": ["berserker_tech", "inspire"],
 "base_str":10, "base_dex":6, "base_con":10, "base_int":6, "base_hp":360, "base_ap":10,
 "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 # min_spawn_level =19
 {"id": "mountain_reaver", "name": "Mountain Reaver", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":19, "rarity": "uncommon", "base_xp":380,
 "common_drop": "stimulant_large", "rare_drop": None, "money_range": (50,200),
 "basic_attack": "rending strike", "strong_attack": "colossal maul", "player_abilities": ["berserker_tech"],
 "base_str":11, "base_dex":5, "base_con":10, "base_int":2, "base_hp":260, "base_ap":7,
 "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":0},

 {"id": "vein_colossus", "name": "Vein Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":19, "rarity": "rare", "base_xp":500,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,320),
 "basic_attack": "mace crush", "strong_attack": "seismic rupture", "player_abilities": ["reinforce_frame"],
 "base_str":14, "base_dex":2, "base_con":14, "base_int":1, "base_hp":360, "base_ap":6,
 "str_per_level":4, "dex_per_level":0, "con_per_level":4, "int_per_level":0},

 # min_spawn_level =20
 {"id": "rift_archer", "name": "Rift Archer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":20, "rarity": "uncommon", "base_xp":420,
 "common_drop": "lockpick", "rare_drop": "handgun_basic", "money_range": (60,240),
 "basic_attack": "precise shot", "strong_attack": "piercing volley", "player_abilities": ["quick_shot"],
 "base_str":3, "base_dex":10, "base_con":5, "base_int":3, "base_hp":220, "base_ap":7,
 "str_per_level":1, "dex_per_level":3, "con_per_level":2, "int_per_level":1},

 {"id": "mountain_overlord", "name": "Mountain Overlord", "hostile_type": "humanoid", "role": "support", "min_spawn_level":20, "rarity": "rare", "base_xp":650,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (120,480),
 "basic_attack": "ruthless barrage", "strong_attack": "overlord's cleave", "player_abilities": ["inspire", "berserker_tech"],
 "base_str":12, "base_dex":6, "base_con":12, "base_int":6, "base_hp":420, "base_ap":10,
 "str_per_level":4, "dex_per_level":2, "con_per_level":4, "int_per_level":2},
]
