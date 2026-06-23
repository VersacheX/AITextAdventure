# Level1-10 hostile seeds for Aurelion Veil (forest city)
# Split out from constants_enemies_large_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==1
 {"id": "rootling", "name": "Rootling", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "gnawing root", "strong_attack": "tangled lash", "player_abilities": None,
 "base_str":1, "base_dex":2, "base_con":2, "base_int":1, "base_hp":8, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "glowgnat", "name": "Glowgnat Swarm", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "bites in swarms", "strong_attack": "blinding cloud", "player_abilities": None,
 "base_str":1, "base_dex":5, "base_con":1, "base_int":1, "base_hp":10, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "moss_wight", "name": "Moss Wight", "hostile_type": "fey", "role": "hazard", "min_spawn_level":1, "rarity": "rare", "base_xp":22,
 "common_drop": "herb_minor", "rare_drop": "tome_dex", "money_range": (0,10),
 "basic_attack": "moldy grasp", "strong_attack": "decaying touch", "player_abilities": ["dark_magic_lv1_shadow_tendril"],
 "base_str":2, "base_dex":3, "base_con":3, "base_int":5, "base_hp":18, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 # min_spawn_level ==2
 {"id": "mosspiper", "name": "Mosspiper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": "lockpick", "money_range": (1,8),
 "basic_attack": "flute jab", "strong_attack": "harmonized stomp", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":1, "base_int":3, "base_hp":12, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "glimmer_sprite", "name": "Glimmer Sprite", "hostile_type": "fey", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,8),
 "basic_attack": "prickling light", "strong_attack": "tickle storm", "player_abilities": ["ice_skill_lv1_ice_shuriken"],
 "base_str":1, "base_dex":8, "base_con":1, "base_int":4, "base_hp":12, "base_ap":3,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # min_spawn_level ==3
 {"id": "silvertongue", "name": "Silvertongue Peddler", "hostile_type": "humanoid", "role": "support", "min_spawn_level":3, "rarity": "uncommon", "base_xp":30,
 "common_drop": "herb_med", "rare_drop": "pipe_wrench", "money_range": (3,24),
 "basic_attack": "peddler's shove", "strong_attack": "charm and pick", "player_abilities": ["water_faith_lv1_mending_streams"],
 "base_str":2, "base_dex":6, "base_con":2, "base_int":6, "base_hp":16, "base_ap":4,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":2},

 {"id": "royal_court_jester", "name": "Royal Court Jester", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "uncommon", "base_xp":28,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (2,16),
 "basic_attack": "slapstick bop", "strong_attack": "pratfall explosion", "player_abilities": ["air_skill_lv1_smoke_bomb"],
 "base_str":2, "base_dex":7, "base_con":2, "base_int":4, "base_hp":18, "base_ap":4,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # min_spawn_level ==4
 {"id": "bramble_bandit", "name": "Bramble Bandit", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":4, "rarity": "uncommon", "base_xp":36,
 "common_drop": "lockpick", "rare_drop": "dagger", "money_range": (6,30),
 "basic_attack": "prickly slash", "strong_attack": "ambush lunge", "player_abilities": ["dark_magic_lv1_shadow_tendril"],
 "base_str":4, "base_dex":8, "base_con":3, "base_int":2, "base_hp":28, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "death_hound", "name": "Death Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":50,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (6,28),
 "basic_attack": "death snap", "strong_attack": "death maul", "player_abilities": None,
 "base_str":5, "base_dex":6, "base_con":4, "base_int":2, "base_hp":44, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==5
 {"id": "thistle_mage", "name": "Thistle Mage", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "rare", "base_xp":100,
 "common_drop": "stimulant_med", "rare_drop": "tome_int", "money_range": (18,80),
 "basic_attack": "thistle bolt", "strong_attack": "arcane blossom", "player_abilities": ["electric_fire_magic_lv2_arclance", "fire_magic_lv1_fireball"],
 "base_str":1, "base_dex":3, "base_con":3, "base_int":10, "base_hp":36, "base_ap":8,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "sapling_scout", "name": "Sapling Scout", "hostile_type": "creature", "role": "damage", "min_spawn_level":5, "rarity": "common", "base_xp":40,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (6,28),
 "basic_attack": "twig jab", "strong_attack": "rapid sprout", "player_abilities": None,
 "base_str":3, "base_dex":6, "base_con":3, "base_int":1, "base_hp":44, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==6
 {"id": "fey_trickster", "name": "Fey Trickster", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":6, "rarity": "uncommon", "base_xp":80,
 "common_drop": "herb_med", "rare_drop": "tome_dex", "money_range": (12,48),
 "basic_attack": "practical joke", "strong_attack": "confounding riddle", "player_abilities": ["dark_magic_lv1_shadow_tendril", "air_skill_lv1_smoke_bomb"],
 "base_str":2, "base_dex":9, "base_con":2, "base_int":8, "base_hp":44, "base_ap":7,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":2},

 {"id": "branch_imp", "name": "Branch Imp", "hostile_type": "fey", "role": "damage", "min_spawn_level":6, "rarity": "common", "base_xp":44,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,36),
 "basic_attack": "needle swipe", "strong_attack": "entangling snare", "player_abilities": None,
 "base_str":2, "base_dex":6, "base_con":3, "base_int":2, "base_hp":48, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==7
 {"id": "sigil_harvester", "name": "Sigil Harvester", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":7, "rarity": "rare", "base_xp":140,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (30,120),
 "basic_attack": "rune lunge", "strong_attack": "sigil burst", "player_abilities": ["light_faith_lv2_prism_burst", "fire_magic_lv1_fireball"],
 "base_str":2, "base_dex":4, "base_con":4, "base_int":12, "base_hp":60, "base_ap":10,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":4},

 {"id": "leaf_guardian", "name": "Leaf Guardian", "hostile_type": "creature", "role": "damage", "min_spawn_level":7, "rarity": "common", "base_xp":110,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (18,88),
 "basic_attack": "leaf slash", "strong_attack": "rooted slam", "player_abilities": None,
 "base_str":4, "base_dex":4, "base_con":6, "base_int":2, "base_hp":120, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==8
 {"id": "scrub_howler", "name": "Scrub Howler", "hostile_type": "creature", "role": "damage", "min_spawn_level":8, "rarity": "common", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (16,72),
 "basic_attack": "howling bite", "strong_attack": "echoing maul", "player_abilities": None,
 "base_str":6, "base_dex":6, "base_con":6, "base_int":2, "base_hp":140, "base_ap":6,
 "str_per_level":2, "dex_per_level":2, "con_per_level":2, "int_per_level":0},

 {"id": "thornling", "name": "Thornling", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "common", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (12,48),
 "basic_attack": "prickly jab", "strong_attack": "thorn volley", "player_abilities": None,
 "base_str":3, "base_dex":5, "base_con":4, "base_int":1, "base_hp":100, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==9
 {"id": "twig_golem", "name": "Twig Golem", "hostile_type": "construct", "role": "damage", "min_spawn_level":9, "rarity": "common", "base_xp":150,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (20,80),
 "basic_attack": "wooden slam", "strong_attack": "timber crush", "player_abilities": None,
 "base_str":7, "base_dex":3, "base_con":8, "base_int":1, "base_hp":180, "base_ap":6,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "bough_wolf_lv9", "name": "Bough Wolf", "hostile_type": "creature", "role": "damage", "min_spawn_level":9, "rarity": "uncommon", "base_xp":30,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (4,16),
 "basic_attack": "claw pounce", "strong_attack": "rending maul", "player_abilities": None,
 "base_str":5, "base_dex":6, "base_con":4, "base_int":2, "base_hp":40, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},
 
 {"id": "bough_wolf", "name": "Bough Wolf", "hostile_type": "creature", "role": "damage", "min_spawn_level":9, "rarity": "uncommon", "base_xp":30,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (4,16),
 "basic_attack": "claw pounce", "strong_attack": "rending maul", "player_abilities": None,
 "base_str":5, "base_dex":6, "base_con":4, "base_int":2, "base_hp":40, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==10
 {"id": "palais_sentinal", "name": "Palais Sentinal", "hostile_type": "humanoid", "role": "support", "min_spawn_level":10, "rarity": "rare", "base_xp":220,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (40,160),
 "basic_attack": "bough strike", "strong_attack": "vine snare", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"],
 "base_str":8, "base_dex":4, "base_con":10, "base_int":3, "base_hp":120, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":0},

 {"id": "ancient_ent", "name": "Ancient Ent", "hostile_type": "construct", "role": "support", "min_spawn_level":10, "rarity": "superrare", "base_xp":520,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (120,480),
 "basic_attack": "rooted slam", "strong_attack": "forest's wrath", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"],
 "base_str":16, "base_dex":2, "base_con":18, "base_int":4, "base_hp":420, "base_ap":12,
 "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":1},
]
