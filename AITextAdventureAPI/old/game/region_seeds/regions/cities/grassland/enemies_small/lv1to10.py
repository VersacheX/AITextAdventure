# Level1-10 hostile seeds for Quantford Hollow (small city)
# Split out from constants_enemies_small_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # level1
 {"id": "stump_thief", "name": "Stump Thief", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "rare", "base_xp":8,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,5),
 "basic_attack": "fumbles a grab", "strong_attack": "bold pluck", "player_abilities": None,
 "base_str":1, "base_dex":5, "base_con":1, "base_int":2, "base_hp":9, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "old_vagrant", "name": "Old Vagrant", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "clumsy shove", "strong_attack": "desperate lunge", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":1, "base_int":1, "base_hp":6, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 {"id": "fern_rat", "name": "Fern Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "nips at you", "strong_attack": "rabid bite", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":7, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 # level2
 {"id": "barn_brawler", "name": "Barn Brawler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":20,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,10),
 "basic_attack": "swings a pitchfork", "strong_attack": "haystack smash", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":3, "base_int":1, "base_hp":18, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "market_bandit", "name": "Market Bandit", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":14,
 "common_drop": "stimulant_small", "rare_drop": "cloth_pants", "money_range": (2,12),
 "basic_attack": "snatches a purse", "strong_attack": "precise stab", "player_abilities": None,
 "base_str":3, "base_dex":4, "base_con":2, "base_int":1, "base_hp":12, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "beggar_blade", "name": "Beggar with a Blade", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "punch", "strong_attack": "stab", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":1, "base_int":1, "base_hp":9, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "pond_wolf", "name": "Pond Wolf", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "snaps at ankles", "strong_attack": "pouncing maul", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":1, "base_hp":10, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # level3

 {"id": "thatch_rogue", "name": "Thatch Rogue", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":30,
 "common_drop": "herb_med", "rare_drop": "pipe_wrench", "money_range": (4,20),
 "basic_attack": "quick slash", "strong_attack": "backstab flourish", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":2, "base_int":2, "base_hp":16, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "hedge_thug", "name": "Hedge Thug", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":24,
 "common_drop": "herb_med", "rare_drop": "cloth_pants", "money_range": (4,18),
 "basic_attack": "deez knuckles", "strong_attack": "furious flurry", "player_abilities": None,
 "base_str":3, "base_dex":3, "base_con":2, "base_int":1, "base_hp":14, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # level4
 {"id": "loft_watch", "name": "Loft Watch", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":36,
 "common_drop": "stimulant_small", "rare_drop": "cloth_gloves", "money_range": (6,24),
 "basic_attack": "raises a cudgel", "strong_attack": "crushing whack", "player_abilities": None,
 "base_str":5, "base_dex":2, "base_con":5, "base_int":1, "base_hp":28, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "mole_troublemaker", "name": "Mole Troublemaker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":28,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (3,16),
 "basic_attack": "stabs from below", "strong_attack": "subterranean lunge", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":3, "base_hp":20, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 # level5

 {"id": "cottage_matron", "name": "Cottage Matron", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":40,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (6,28),
 "basic_attack": "heaves a skillet", "strong_attack": "pan slam", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":4, "base_int":2, "base_hp":26, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "pawn_guard", "name": "Pawnshop Guard", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":45,
 "common_drop": "stimulant_small", "rare_drop": "stimulant_large", "money_range": (10,40),
 "basic_attack": "bashes with a baton", "strong_attack": "stunning strike", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":3, "base_int":2, "base_hp":26, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":1},

 {"id": "sly_country_madam", "name": "Sly Country Madam", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":40,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (6,28),
 "basic_attack": "swift move", "strong_attack": "outsmart", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":4, "base_hp":20, "base_ap":4,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # level6
 {"id": "peasant_fixit", "name": "Peasant Fixit", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":48,
 "common_drop": "stimulant_small", "rare_drop": "tome_dex", "money_range": (8,40),
 "basic_attack": "taps your gear with a wrench", "strong_attack": "sparked lurch", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":6, "base_hp":26, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "ledger_guard_praerie", "name": "Ledger Guard of the Praerie", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":46,
 "common_drop": "stimulant_small", "rare_drop": "stimulant_large", "money_range": (8,36),
 "basic_attack": "bashes with a ledger", "strong_attack": "stunning baton", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":4, "base_int":2, "base_hp":30, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":1},

 {"id": "disgruntled_bartender", "name": "Disgruntled Bartender", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":58,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (8,36),
 "basic_attack": "towel swipe", "strong_attack": "bottle smash", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":3, "base_int":2, "base_hp":30, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 # level7
 {"id": "lady_cutpurse_small", "name": "Lady Cutpurse", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "rare", "base_xp":100,
 "common_drop": "stimulant_small", "rare_drop": "dagger", "money_range": (15,70),
 "basic_attack": "swift stab", "strong_attack": "lethal twirl", "player_abilities": ["level_1_hostile_ability_air_skill_gale_dash"],
 "base_str":3, "base_dex":8, "base_con":3, "base_int":3, "base_hp":34, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 {"id": "meadaow_void_spider", "name": "Meadow Void Spider", "hostile_type": "creature", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (2,30),
 "basic_attack": "fanged bite", "strong_attack": "venomous tear", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":2, "base_dex":8, "base_con":3, "base_int":2, "base_hp":40, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":0},

 {"id": "tough_country_granny", "name": "Tough Country Granny", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":54,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (6,30),
 "basic_attack": "needle jab", "strong_attack": "heavy pummel", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":5, "base_int":2, "base_hp":44, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # level8
 {"id": "curio_fox", "name": "Curio Fox", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "rare", "base_xp":88,
 "common_drop": "stimulant_med", "rare_drop": "herb_major", "money_range": (20,100),
 "basic_attack": "pries at wares", "strong_attack": "crippling pry-stab", "player_abilities": None,
 "base_str":2, "base_dex":6, "base_con":2, "base_int":4, "base_hp":30, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "antique_thief", "name": "Antique Thief", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "rare", "base_xp":90,
 "common_drop": "stimulant_med", "rare_drop": "herb_major", "money_range": (25,100),
 "basic_attack": "stab", "strong_attack": "crippling blow", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":2, "base_int":3, "base_hp":28, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "lady_rogue", "name": "Lady Rogue", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "rare", "base_xp":110,
 "common_drop": "stimulant_small", "rare_drop": "pipe_wrench", "money_range": (20,80),
 "basic_attack": "stab", "strong_attack": "lethal dance", "player_abilities": ["fire_earth_technique_lv2_blaze_hammer"],
 "base_str":3, "base_dex":8, "base_con":3, "base_int":3, "base_hp":30, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # level9
 {"id": "praerie_cyber_hound", "name": "Prarie Cyber Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":9, "rarity": "uncommon", "base_xp":70,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (8,30),
 "basic_attack": "rips with fangs", "strong_attack": "venomous lunge", "player_abilities": None,
 "base_str":6, "base_dex":6, "base_con":4, "base_int":1, "base_hp":40, "base_ap":4,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "trigger_happy_gun_slinger_gal", "name": "Trigger Happy Gunslinger Gal", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":9, "rarity": "rare", "base_xp":120,
 "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (25,100),
 "basic_attack": "precise shot", "strong_attack": "headshot", "player_abilities": ["ice_skill_lv1_ice_shuriken"],
 "base_str":3, "base_dex":7, "base_con":3, "base_int":3, "base_hp":32, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # level10
 {"id": "forlorn_fixer_tinker", "name": "Forlorn Fixer Tinker", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":10, "rarity": "rare", "base_xp":120,
 "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (30,140),
 "basic_attack": "throws a gadget", "strong_attack": "sparking overload", "player_abilities": ["level_1_hostile_ability_air_magic_gale_surge", "dark_magic_lv4_mind_shiver"],
 "base_str":2, "base_dex":4, "base_con":3, "base_int":9, "base_hp":36, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "madam_ratchet", "name": "Madam Ratchet", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":10, "rarity": "rare", "base_xp":130,
 "common_drop": "stimulant_small", "rare_drop": "tome_dex", "money_range": (30,120),
 "basic_attack": "precision strikes", "strong_attack": "wrenching attack", "player_abilities": ["lv2_hostile_ability_fire_water_tech_steam_grenade"],
 "base_str":3, "base_dex":4, "base_con":3, "base_int":6, "base_hp":40, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "praerie_wraith_knight", "name": "Praerie Wraith Knight", "hostile_type": "undead", "role": "hazard", "min_spawn_level":10, "rarity": "rare", "base_xp":260,
 "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (25,120),
 "basic_attack": "spectral blade", "strong_attack": "ghostly cleave", "player_abilities": None,
 "base_str":8, "base_dex":6, "base_con":6, "base_int":3, "base_hp":120, "base_ap":8,
 "str_per_level":2, "dex_per_level":2, "con_per_level":2, "int_per_level":1},
]
