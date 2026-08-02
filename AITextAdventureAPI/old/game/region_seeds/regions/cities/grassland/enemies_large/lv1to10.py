# Level1-10 hostile seeds for Crosswind Bazaar (large city)
# Split out from constants_enemies_large_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==1
 {"id": "coin_finger", "name": "Coin-Finger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":8,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "snatches at your pouch", "strong_attack": "panicked grab", "player_abilities": None,
 "base_str":1, "base_dex":6, "base_con":1, "base_int":2, "base_hp":8, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "tent_swashbuckler", "name": "Tent Swashbuckler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":14,
 "common_drop": "pipe_wrench", "rare_drop": "dagger", "money_range": (3,12),
 "basic_attack": "flourishes a blade", "strong_attack": "overhead lunge", "player_abilities": None,
 "base_str":3, "base_dex":4, "base_con":2, "base_int":1, "base_hp":12, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "pickpocket_apprentice", "name": "Pickpocket Apprentice", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":9,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,5),
 "basic_attack": "light jab", "strong_attack": "sudden vanish", "player_abilities": None,
 "base_str":1, "base_dex":5, "base_con":1, "base_int":2, "base_hp":8, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "vagrant_old", "name": "Vagrant", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "sloppy shove", "strong_attack": "lamenting wail", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":1, "base_int":2, "base_hp":6, "base_ap":1,
 "str_per_level":0, "dex_per_level":0, "con_per_level":0, "int_per_level":1},

 {"id": "barfly_drunkard", "name": "Barfly Drunkard", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "drunken hook", "strong_attack": "bottle smash", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":2, "base_int":1, "base_hp":6, "base_ap":1,
 "str_per_level":0, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "antique_pick", "name": "Antique Pick", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "rare", "base_xp":90,
 "common_drop": "stimulant_med", "rare_drop": "herb_major", "money_range": (25,120),
 "basic_attack": "pries at you with a hook", "strong_attack": "precise pry-stab", "player_abilities": None,
 "base_str":2, "base_dex":6, "base_con":2, "base_int":3, "base_hp":30, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # min_spawn_level ==2
 {"id": "shadow_cat", "name": "Shadow Cat", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "slashes with claws", "strong_attack": "pouncing ambush", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":2, "base_int":1, "base_hp":12, "base_ap":3,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "undercity_roach", "name": "Undercity Roach", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":9,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "fierce bite", "strong_attack": "savage swarm", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":7, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "beggar_swash", "name": "Beggar with a Blade", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "poke with a spoon", "strong_attack": "knife behind a coin cup", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":1, "base_int":1, "base_hp":9, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 # min_spawn_level ==3
 {"id": "bazaarkeeper", "name": "Bazaarkeeper Babushka", "hostile_type": "humanoid", "role": "support", "min_spawn_level":3, "rarity": "uncommon", "base_xp":30,
 "common_drop": "herb_med", "rare_drop": "tome_dex", "money_range": (6,30),
 "basic_attack": "hurls a basket", "strong_attack": "ceramic bust", "player_abilities": ["air_light_faith_lv2_serene_breath"],
 "base_str":2, "base_dex":3, "base_con":4, "base_int":5, "base_hp":22, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "rat_king", "name": "Rat King", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":26,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,14),
 "basic_attack": "bites fiercely", "strong_attack": "swarming gnaw", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":1, "base_hp":16, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "tattooed_rowdy", "name": "Tattooed Rowdy", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":24,
 "common_drop": "herb_med", "rare_drop": "cloth_pants", "money_range": (4,16),
 "basic_attack": "deez knuckles", "strong_attack": "furious flurry", "player_abilities": None,
 "base_str":3, "base_dex":4, "base_con":2, "base_int":1, "base_hp":14, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "streetwise_fox", "name": "Streetwise Fox", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "heavy purse-twist", "strong_attack": "deadly heel", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":2, "base_hp":10, "base_ap":2,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # min_spawn_level ==4
 {"id": "cyber_hound_pup", "name": "Cyber-Hound Pup", "hostile_type": "creature", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":12,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (2,10),
 "basic_attack": "nips playfully", "strong_attack": "charging maul", "player_abilities": None,
 "base_str":4, "base_dex":5, "base_con":3, "base_int":1, "base_hp":18, "base_ap":3,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "mole_trader", "name": "Mole Trader", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":28,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (3,16),
 "basic_attack": "stabs with a cramped dagger", "strong_attack": "tunnel lunge", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":3, "base_hp":20, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 {"id": "rogue_poet", "name": "Rogue Poet", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":4, "rarity": "uncommon", "base_xp":36,
 "common_drop": "herb_med", "rare_drop": "pipe_wrench", "money_range": (5,22),
 "basic_attack": "throws a scathing couplet", "strong_attack": "emotional strike", "player_abilities": ["dark_magic_lv4_mind_shiver"],
 "base_str":2, "base_dex":6, "base_con":2, "base_int":4, "base_hp":20, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "flapper_dancer", "name": "Flapper Dancer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":20,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (2,14),
 "basic_attack": "scratching claws", "strong_attack": "spinning kick", "player_abilities": None,
 "base_str":2, "base_dex":6, "base_con":2, "base_int":2, "base_hp":12, "base_ap":3,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # min_spawn_level ==5
 {"id": "ganger_rabble", "name": "Ganger Rabble", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":40,
 "common_drop": "herb_med", "rare_drop": "cloth_gloves", "money_range": (10,45),
 "basic_attack": "throws a pipe", "strong_attack": "coordinated surge", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":4, "base_int":1, "base_hp":36, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==6
 {"id": "caravan_giant", "name": "Caravan Giant", "hostile_type": "creature", "role": "damage", "min_spawn_level":6, "rarity": "rare", "base_xp":140,
 "common_drop": "stimulant_med", "rare_drop": "leather_armor", "money_range": (20,90),
 "basic_attack": "clubs with a crate", "strong_attack": "stampede charge", "player_abilities": None,
 "base_str":8, "base_dex":2, "base_con":8, "base_int":1, "base_hp":80, "base_ap":3,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "raider_windman", "name": "Raider Windman", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "rare", "base_xp":70,
 "common_drop": "herb_major", "rare_drop": "machete", "money_range": (18,60),
 "basic_attack": "axes with gusto", "strong_attack": "whirling cleave", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":4, "base_int":1, "base_hp":34, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "bouncer_bram", "name": "Bouncer Bram", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":60,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (6,28),
 "basic_attack": "shoulder ram", "strong_attack": "haymaker swing", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":5, "base_int":1, "base_hp":32, "base_ap":3,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==7
 {"id": "smiling_fixit", "name": "Smiling Fixit", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":50,
 "common_drop": "stimulant_small", "rare_drop": "tome_int", "money_range": (8,40),
 "basic_attack": "taps your pocket with a wrench", "strong_attack": "electro jolt", "player_abilities": ["level_1_hostile_ability_air_magic_gale_surge"] if False else None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":6, "base_hp":26, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "smuggler_herald", "name": "Smuggler Herald", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":48,
 "common_drop": "stimulant_small", "rare_drop": "stimulant_med", "money_range": (10,50),
 "basic_attack": "brandishes a sealed crate", "strong_attack": "poisoned dart", "player_abilities": None,
 "base_str":3, "base_dex":5, "base_con":2, "base_int":3, "base_hp":28, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "siren_muse", "name": "Siren Muse", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":7, "rarity": "rare", "base_xp":72,
 "common_drop": "stimulant_small", "rare_drop": "tome_int", "money_range": (12,60),
 "basic_attack": "siren song", "strong_attack": "mesmerize", "player_abilities": ["air_light_faith_lv2_serene_breath", "dark_magic_lv4_nightmare_echo"],
 "base_str":2, "base_dex":5, "base_con":2, "base_int":7, "base_hp":28, "base_ap":6,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":3},

 # min_spawn_level ==8
 {"id": "pawn_watch", "name": "Pawnwatcher", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "uncommon", "base_xp":46,
 "common_drop": "stimulant_small", "rare_drop": "stimulant_large", "money_range": (10,48),
 "basic_attack": "bashes with a ledger", "strong_attack": "stunning baton strike", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":4, "base_int":2, "base_hp":28, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":1},

 {"id": "court_jester", "name": "Court Jester", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "rare", "base_xp":95,
 "common_drop": "stimulant_small", "rare_drop": "dagger", "money_range": (12,70),
 "basic_attack": "juggling knives", "strong_attack": "banana peel ambush", "player_abilities": ["level_1_hostile_ability_air_skill_gale_dash"],
 "base_str":3, "base_dex":8, "base_con":3, "base_int":4, "base_hp":30, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # min_spawn_level ==9
 {"id": "wind_sniper", "name": "Wind Sniper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":9, "rarity": "rare", "base_xp":120,
 "common_drop": "handgun_basic", "rare_drop": None, "money_range": (30,120),
 "basic_attack": "takes a careful shot", "strong_attack": "rapid volley", "player_abilities": ["air_skill_lv1_smoke_bomb"],
 "base_str":2, "base_dex":8, "base_con":2, "base_int":3, "base_hp":28, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 {"id": "lady_cutpurse", "name": "Lady Cutpurse", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":9, "rarity": "rare", "base_xp":110,
 "common_drop": "stimulant_small", "rare_drop": "pipe_wrench", "money_range": (18,80),
 "basic_attack": "stab", "strong_attack": "lethal dance", "player_abilities": ["air_skill_lv1_smoke_bomb"],
 "base_str":3, "base_dex":8, "base_con":3, "base_int":3, "base_hp":30, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},
 
 {"id": "umbral_racer", "name": "Umbral Racer", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":9, "rarity": "uncommon", "base_xp":180,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (6,48),
 "basic_attack": "dark slash", "strong_attack": "vanishing strike", "player_abilities": ["dark_magic_lv4_mind_shiver"],
 "base_str":5, "base_dex":10, "base_con":4, "base_int":3, "base_hp":80, "base_ap":7,
 "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # min_spawn_level ==10
 {"id": "plague_baker", "name": "Plague Baker", "hostile_type": "undead", "role": "hazard", "min_spawn_level":10, "rarity": "uncommon", "base_xp":160,
 "common_drop": "ointment", "rare_drop": "stimulant_large", "money_range": (5,60),
 "basic_attack": "diseased smite", "strong_attack": "virulent spray", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":6, "base_int":5, "base_hp":120, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 {"id": "wraith_watchman", "name": "Wraith Watchman", "hostile_type": "undead", "role": "hazard", "min_spawn_level":10, "rarity": "rare", "base_xp":260,
 "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (25,120),
 "basic_attack": "spectral blade", "strong_attack": "ghostly cleave", "player_abilities": None,
 "base_str":8, "base_dex":6, "base_con":6, "base_int":3, "base_hp":120, "base_ap":8,
 "str_per_level":2, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "enforcer_brute", "name": "Enforcer Brute", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":10, "rarity": "rare", "base_xp":160,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (45,160),
 "basic_attack": "cleaves with a baton", "strong_attack": "earthshaker slam", "player_abilities": None,
 "base_str":9, "base_dex":2, "base_con":7, "base_int":1, "base_hp":92, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "gunslinger_maiden", "name": "Gunslinger Maiden", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":10, "rarity": "superrare", "base_xp":420,
 "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (25,120),
 "basic_attack": "quick shot", "strong_attack": "headshot", "player_abilities": ["level_1_hostile_ability_air_skill_gale_dash"],
 "base_str":3, "base_dex":7, "base_con":3, "base_int":3, "base_hp":32, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},
]
