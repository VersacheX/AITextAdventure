# Level11-20 hostile seeds for Crosswind Bazaar (large city)
# Split out from constants_enemies_large_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==10
 {"id": "fixer_shade", "name": "Fixer Shade", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":10, "rarity": "uncommon", "base_xp":130,
 "common_drop": "stimulant_large", "rare_drop": "handgun_basic", "money_range": (30,140),
 "basic_attack": "drops a smoke charge", "strong_attack": "hack-and-shock", "player_abilities": ["air_skill_lv1_smoke_bomb"],
 "base_str":2, "base_dex":5, "base_con":3, "base_int":9, "base_hp":36, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "void_weaver", "name": "Void Weaver", "hostile_type": "creature", "role": "damage", "min_spawn_level":10, "rarity": "common", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,44),
 "basic_attack": "fanged bite", "strong_attack": "venomous tear", "player_abilities": None,
 "base_str":3, "base_dex":8, "base_con":3, "base_int":2, "base_hp":44, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==11
 {"id": "abyss_serpent_mini", "name": "Abyss Serpent (mini)", "hostile_type": "creature", "role": "damage", "min_spawn_level":11, "rarity": "rare", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40,200),
 "basic_attack": "maw lash", "strong_attack": "constrict", "player_abilities": None,
 "base_str":10, "base_dex":7, "base_con":9, "base_int":2, "base_hp":220, "base_ap":6,
 "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":0},

 {"id": "elder_tendrils", "name": "Elder Tendrils", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":11, "rarity": "rare", "base_xp":200,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (20,100),
 "basic_attack": "tentacle whip", "strong_attack": "barbed crush", "player_abilities": None,
 "base_str":11, "base_dex":2, "base_con":9, "base_int":2, "base_hp":160, "base_ap":4,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

  # min_spawn_level ==12
 {"id": "lich_apprentice_quiet", "name": "Lich Apprentice (quietly smug)", "hostile_type": "undead", "role": "hazard", "min_spawn_level":12, "rarity": "uncommon", "base_xp":320,
 "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (30,140),
 "basic_attack": "bone bolt", "strong_attack": "necrotic spear", "player_abilities": ["dark_magic_lv4_mind_shiver"],
 "base_str":2, "base_dex":3, "base_con":4, "base_int":12, "base_hp":100, "base_ap":10,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "fixer_hacker_elite", "name": "Fixer Hacker Elite", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":12, "rarity": "uncommon", "base_xp":130,
 "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (40,160),
 "basic_attack": "cybernetic strike", "strong_attack": "system overload", "player_abilities": ["air_tech_lv4_gale_surge", "dark_magic_lv4_mind_shiver"],
 "base_str":3, "base_dex":5, "base_con":3, "base_int":10, "base_hp":40, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "matron_hired", "name": "Matron Hired", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (35,140),
 "basic_attack": "cane lash", "strong_attack": "crushing blow", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":7, "base_int":4, "base_hp":80, "base_ap":6,
 "str_per_level":2, "dex_per_level":0, "con_per_level":3, "int_per_level":1},

 # min_spawn_level ==13
 {"id": "harbinger_frost", "name": "Harbinger of Frost (mildly chilly)", "hostile_type": "elemental", "role": "hazard", "min_spawn_level":13, "rarity": "rare", "base_xp":340,
 "common_drop": "stimulant_med", "rare_drop": "tome_int", "money_range": (30,160),
 "basic_attack": "ice shard", "strong_attack": "freezing blast", "player_abilities": ["water_air_light_magic_lv4_frost_nova"],
 "base_str":6, "base_dex":4, "base_con":8, "base_int":6, "base_hp":180, "base_ap":9,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "harbinger_frost_2", "name": "Harbinger of Frost (aux)", "hostile_type": "elemental", "role": "hazard", "min_spawn_level":13, "rarity": "common", "base_xp":160,
 "common_drop": "stimulant_med", "rare_drop": None, "money_range": (30,160),
 "basic_attack": "ice nibble", "strong_attack": "chill pulse", "player_abilities": ["water_air_light_magic_lv4_frost_nova"],
 "base_str":4, "base_dex":4, "base_con":6, "base_int":6, "base_hp":140, "base_ap":8,
 "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "mind_merchant", "name": "Mind Merchant", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":13, "rarity": "common", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,320),
 "basic_attack": "psychic tendrils", "strong_attack": "mindful barrage", "player_abilities": ["dark_magic_lv4_mind_shiver"],
 "base_str":2, "base_dex":3, "base_con":3, "base_int":14, "base_hp":80, "base_ap":12,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":4},

 # min_spawn_level ==14
 {"id": "wrecker_hulker", "name": "Wrecker Hulker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":14, "rarity": "common", "base_xp":150,
 "common_drop": "herb_major", "rare_drop": "sawed_off", "money_range": (30,160),
 "basic_attack": "haymaker", "strong_attack": "wrecking ball slam", "player_abilities": None,
 "base_str":8, "base_dex":2, "base_con":6, "base_int":1, "base_hp":72, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "clockwork_giant", "name": "Clockwork Giant", "hostile_type": "construct", "role": "damage", "min_spawn_level":14, "rarity": "rare", "base_xp":320,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (60,260),
 "basic_attack": "piston swing", "strong_attack": "hydraulic crush", "player_abilities": ["air_earth_technique_lv4_whirlwind"],
 "base_str":14, "base_dex":1, "base_con":18, "base_int":1, "base_hp":300, "base_ap":3,
 "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "wrecker_hulker_2", "name": "Wrecker Hulker (bruiser)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":14, "rarity": "common", "base_xp":150,
 "common_drop": "herb_major", "rare_drop": None, "money_range": (30,160),
 "basic_attack": "haymaker", "strong_attack": "wrecking ball slam", "player_abilities": None,
 "base_str":7, "base_dex":2, "base_con":6, "base_int":1, "base_hp":70, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==15
 {"id": "dream_sipper", "name": "Dream Sipper", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":15, "rarity": "uncommon", "base_xp":480,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,300),
 "basic_attack": "mind gnaw", "strong_attack": "maddening shriek", "player_abilities": ["dark_magic_lv4_nightmare_echo"],
 "base_str":3, "base_dex":6, "base_con":5, "base_int":14, "base_hp":140, "base_ap":14,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":4},

 # min_spawn_level ==16
 {"id": "black_market_lady", "name": "Black Market Lady (sassy)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":16, "rarity": "common", "base_xp":200,
 "common_drop": "stimulant_large", "rare_drop": "stimulant_large", "money_range": (60,300),
 "basic_attack": "bitch slap", "strong_attack": "critical auctioneer shot", "player_abilities": ["fire_technique_lv4_berserker_tech"],
 "base_str":4, "base_dex":5, "base_con":4, "base_int":8, "base_hp":48, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 # min_spawn_level ==18
 {"id": "cybernet_watch", "name": "Cybernet Watch", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":18, "rarity": "common", "base_xp":260,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (80,340),
 "basic_attack": "precision strike", "strong_attack": "devastating barrage", "player_abilities": ["air_earth_techique_lv4_whirlwind"],
 "base_str":6, "base_dex":6, "base_con":6, "base_int":4, "base_hp":120, "base_ap":8,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 {"id": "celestial_watch", "name": "Celestial Watch", "hostile_type": "celestial", "role": "support", "min_spawn_level":18, "rarity": "common", "base_xp":600,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (100,420),
 "basic_attack": "radiant talons", "strong_attack": "celestial shards", "player_abilities": ["light_faith_lv4_hearthsong"],
 "base_str":10, "base_dex":8, "base_con":12, "base_int":10, "base_hp":320, "base_ap":12,
 "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":3},

 # min_spawn_level ==20
 {"id": "mob_exec", "name": "Mob Exec (wears too much eyeliner)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":20, "rarity": "superrare", "base_xp":420,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (150,700),
 "basic_attack": "ruthless backhand", "strong_attack": "mobster beatdown", "player_abilities": ["fire_technique_lv4_berserker_tech"],
 "base_str":9, "base_dex":6, "base_con":8, "base_int":6, "base_hp":200, "base_ap":10,
 "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 {"id": "praerie_femme_fatality", "name": "Praerie Femme Fatality", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":20, "rarity": "common", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (180,800),
 "basic_attack": "elegant stab", "strong_attack": "fatal flourish", "player_abilities": ["fire_technique_lv4_berserker_tech"],
 "base_str":8, "base_dex":10, "base_con":6, "base_int":8, "base_hp":220, "base_ap":12,
 "str_per_level":4, "dex_per_level":4, "con_per_level":2, "int_per_level":3},
]
