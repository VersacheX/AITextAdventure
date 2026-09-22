# Level1-10 hostile seeds for The Necropolis (large-city)
# Export a list named SEEDS_LV1TO10 used by constants_enemies_large_city.py
SEEDS_LV1TO10 = [
 # Level1: ensure common, uncommon, rare present
 {"id": "mire_tosser", "name": "Mire Tosser", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "mud flick", "strong_attack": "splash shove", "player_abilities": None,
 "base_str":1, "base_dex":2, "base_con":2, "base_int":1, "base_hp":12, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "grave_hawker", "name": "Grave Hawker", "hostile_type": "humanoid", "role": "support", "min_spawn_level":1, "rarity": "common", "base_xp":12,
 "common_drop": "stimulant_small", "rare_drop": "tome_dex", "money_range": (1,12),
 "basic_attack": "rusty patter", "strong_attack": "jar heave", "player_abilities": ["level_1_hostile_ability_inspire"],
 "base_str":1, "base_dex":3, "base_con":2, "base_int":4, "base_hp":16, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "sock_rat", "name": "Sock Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "nibble", "strong_attack": "rabid bite", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":8, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "skeleton_minion_01", "name": "Ragged Skeleton", "hostile_type": "undead", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "clattering swipe", "strong_attack": "fragile cleave", "player_abilities": None,
 "base_str":2, "base_dex":2, "base_con":1, "base_int":1, "base_hp":10, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 {"id": "cryptling_01", "name": "Cryptling", "hostile_type": "undead", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6, "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4), "basic_attack": "scratch", "strong_attack": "bite", "player_abilities": None, "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":8, "base_ap":1, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "carrion_bat_01", "name": "Carrion Bat", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "bite", "strong_attack": "swoop maul", "player_abilities": None,
 "base_str":1, "base_dex":6, "base_con":1, "base_int":1, "base_hp":8, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 # Level1: uncommon + rare required
 {"id": "shade_picker", "name": "Shade Picker", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":1, "rarity": "uncommon", "base_xp":20,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "slick snatch", "strong_attack": "shadow trip", "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
 "base_str":2, "base_dex":7, "base_con":2, "base_int":3, "base_hp":24, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "mourning_wisp", "name": "Mourning Wisp", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":1, "rarity": "rare", "base_xp":80,
 "common_drop": "herb_minor", "rare_drop": "tome_int", "money_range": (6,36),
 "basic_attack": "whisper cold", "strong_attack": "spectral chill", "player_abilities": ["level_1_hostile_ability_night_whisper"],
 "base_str":1, "base_dex":5, "base_con":2, "base_int":8, "base_hp":44, "base_ap":6,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 # Level2
 {"id": "cryptling_02", "name": "Cryptling Whelp", "hostile_type": "undead", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":8, "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6), "basic_attack": "nibble", "strong_attack": "fang rut", "player_abilities": None, "base_str":2, "base_dex":4, "base_con":1, "base_int":1, "base_hp":10, "base_ap":1, "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "coffin_cutpurse", "name": "Coffin Cutpurse", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":2, "rarity": "common", "base_xp":14,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,10),
 "basic_attack": "pilfer jab", "strong_attack": "dagger flourish", "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
 "base_str":1, "base_dex":6, "base_con":1, "base_int":2, "base_hp":14, "base_ap":3,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "putrid_zombie_01", "name": "Putrid Zombie", "hostile_type": "undead", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,8),
 "basic_attack": "sluggish swipe", "strong_attack": "rotting crush", "player_abilities": None,
 "base_str":3, "base_dex":1, "base_con":4, "base_int":1, "base_hp":30, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "undertaker_apprentice", "name": "Undertaker Apprentice", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,10),
 "basic_attack": "shovel jab", "strong_attack": "earth heave", "player_abilities": None,
 "base_str":2, "base_dex":2, "base_con":3, "base_int":2, "base_hp":18, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "skeleton_minion_02", "name": "Bone Scrapper", "hostile_type": "undead", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "rib jab", "strong_attack": "spine snap", "player_abilities": None,
 "base_str":3, "base_dex":2, "base_con":2, "base_int":1, "base_hp":12, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 {"id": "skeleton_minion_03", "name": "Skitter Bone", "hostile_type": "undead", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "skewer", "strong_attack": "calcium crush", "player_abilities": None,
 "base_str":3, "base_dex":3, "base_con":2, "base_int":1, "base_hp":14, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "corpse_moth", "name": "Corpse Moth", "hostile_type": "creature", "role": "hazard", "min_spawn_level":2, "rarity": "common", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "dust flutter", "strong_attack": "powder choke", "player_abilities": None,
 "base_str":1, "base_dex":4, "base_con":2, "base_int":2, "base_hp":16, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 # Level3
 {"id": "skeleton_archer_01", "name": "Bone Archer", "hostile_type": "undead", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":20,
 "common_drop": "herb_minor", "rare_drop": "pipe_wrench", "money_range": (2,12),
 "basic_attack": "bone shot", "strong_attack": "barbed volley", "player_abilities": None,
 "base_str":2, "base_dex":6, "base_con":2, "base_int":1, "base_hp":18, "base_ap":3,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "grave_digger_01", "name": "Grave Digger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":22,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "digger swing", "strong_attack": "tomb toss", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":4, "base_int":2, "base_hp":40, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "talon_merchant", "name": "Talon Merchant", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": "tome_int", "money_range": (2,20),
 "basic_attack": "invoice slap", "strong_attack": "ink lash", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":6, "base_hp":22, "base_ap":3,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "ghoul_runner_01", "name": "Ghoul Runner", "hostile_type": "undead", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":22,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,12),
 "basic_attack": "frenzied bite", "strong_attack": "gut tear", "player_abilities": None,
 "base_str":4, "base_dex":6, "base_con":3, "base_int":1, "base_hp":28, "base_ap":3,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "sock_rat_02", "name": "Sock Rat Young", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "nibble", "strong_attack": "scrab maul", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":1, "base_int":1, "base_hp":10, "base_ap":1,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 # Level4
 {"id": "tomb_wight_01", "name": "Tomb Wight", "hostile_type": "undead", "role": "hazard", "min_spawn_level":4, "rarity": "uncommon", "base_xp":44,
 "common_drop": "herb_med", "rare_drop": "tome_int", "money_range": (6,44),
 "basic_attack": "pale grasp", "strong_attack": "life sap", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":4, "base_dex":3, "base_con":6, "base_int":4, "base_hp":60, "base_ap":5,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":1},

 {"id": "putrid_zombie_02", "name": "Corpse Drudge", "hostile_type": "undead", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":34,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (2,18),
 "basic_attack": "stumble bash", "strong_attack": "foul pummel", "player_abilities": None,
 "base_str":4, "base_dex":1, "base_con":6, "base_int":1, "base_hp":56, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "sepulcher_hound_01", "name": "Sepulcher Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":24,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,16),
 "basic_attack": "snarl bite", "strong_attack": "burrow maul", "player_abilities": None,
 "base_str":4, "base_dex":5, "base_con":3, "base_int":1, "base_hp":36, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # Level5
 {"id": "skeleton_archer_02", "name": "Crossbone Marksman", "hostile_type": "undead", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":36,
 "common_drop": "herb_med", "rare_drop": "handgun_basic", "money_range": (6,36),
 "basic_attack": "pierce shot", "strong_attack": "deadeye volley", "player_abilities": ["level_1_hostile_ability_air_skill_quick_shot"],
 "base_str":3, "base_dex":7, "base_con":3, "base_int":2, "base_hp":30, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "rot_brigand", "name": "Rot Brigand", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":46,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (4,28),
 "basic_attack": "slime swipe", "strong_attack": "pustule burst", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":5, "base_int":2, "base_hp":64, "base_ap":4,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "moss_jester", "name": "Moss Jester", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":5, "rarity": "uncommon", "base_xp":36,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (2,20),
 "basic_attack": "slapstick flail", "strong_attack": "custard of rot", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":3, "base_int":5, "base_hp":36, "base_ap":3,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 # Level6
 {"id": "grave_digger_02", "name": "Dusk Digger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":56,
 "common_drop": "herb_med", "rare_drop": "short_sword", "money_range": (6,30),
 "basic_attack": "shovel cleave", "strong_attack": "pitfall slam", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":6, "base_int":2, "base_hp":80, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "moss_spider", "name": "Moss Spider", "hostile_type": "creature", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (4,36),
 "basic_attack": "bite", "strong_attack": "web entangle", "player_abilities": None,
 "base_str":2, "base_dex":6, "base_con":3, "base_int":2, "base_hp":56, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "funeral_pallbearer", "name": "Funeral Pallbearer", "hostile_type": "humanoid", "role": "support", "min_spawn_level":6, "rarity": "uncommon", "base_xp":60,
 "common_drop": "herb_med", "rare_drop": "cloth_gloves", "money_range": (6,30),
 "basic_attack": "pall swing", "strong_attack": "coffin crash", "player_abilities": None,
 "base_str":6, "base_dex":2, "base_con":6, "base_int":2, "base_hp":80, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # Level7
 {"id": "sepulcher_hound_02", "name": "Ghast Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":72,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (6,40),
 "basic_attack": "spectral snap", "strong_attack": "ethereal maul", "player_abilities": None,
 "base_str":6, "base_dex":6, "base_con":5, "base_int":2, "base_hp":90, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "tomb_stalker_01", "name": "Tomb Stalker", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":7, "rarity": "uncommon", "base_xp":78, "common_drop": "stimulant_small", "rare_drop": "pipe_wrench", "money_range": (8,44), "basic_attack": "silent cut", "strong_attack": "rear rip", "player_abilities": ["level_1_hostile_ability_shadow_flicker"], "base_str":4, "base_dex":8, "base_con":3, "base_int":4, "base_hp":88, "base_ap":6, "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 {"id": "sexton_mad", "name": "Sexton Mad", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":40,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (4,24),
 "basic_attack": "mad hiss", "strong_attack": "bell smash", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":3, "base_int":5, "base_hp":44, "base_ap":3,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 # Level8
 {"id": "bone_tinker", "name": "Bone Tinker", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":8, "rarity": "rare", "base_xp":120,
 "common_drop": "stimulant_small", "rare_drop": "tome_dex", "money_range": (18,90),
 "basic_attack": "wrench snap", "strong_attack": "spine clamp", "player_abilities": ["level_1_hostile_ability_electric_tech_hack_overload", "level_1_hostile_ability_electric_tech_hack_overload"],
 "base_str":2, "base_dex":4, "base_con":5, "base_int":9, "base_hp":64, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 # Level9
 {"id": "bog_wyrm", "name": "Bog Wyrm", "hostile_type": "creature", "role": "damage", "min_spawn_level":9, "rarity": "rare", "base_xp":220,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (30,160),
 "basic_attack": "toxic bite", "strong_attack": "constricting coil", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":9, "base_dex":5, "base_con":8, "base_int":3, "base_hp":220, "base_ap":6,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "ossuary_priest_01", "name": "Ossuary Priest", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":9, "rarity": "rare", "base_xp":180,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (18,96),
 "basic_attack": "bone incant", "strong_attack": "curse of marrow", "player_abilities": ["level_1_hostile_ability_arcane_blast", "level_1_hostile_ability_night_whisper"],
 "base_str":2, "base_dex":3, "base_con":6, "base_int":12, "base_hp":140, "base_ap":8,
 "str_per_level":1, "dex_per_level":0, "con_per_level":2, "int_per_level":3},

 {"id": "marrow_collector", "name": "Marrow Collector", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":9, "rarity": "rare", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (18,96),
 "basic_attack": "pick bone", "strong_attack": "marrow rip", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":4, "base_dex":3, "base_con":8, "base_int":6, "base_hp":140, "base_ap":6,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":1},

 {"id": "grate_sentry", "name": "Grate Sentry", "hostile_type": "construct", "min_spawn_level":9, "rarity": "uncommon", "base_xp":88,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (6,44), "role": "damage",
 "basic_attack": "sprocket jab", "strong_attack": "steam burst", "player_abilities": None,
 "base_str":4, "base_dex":5, "base_con":4, "base_int":2, "base_hp":88, "base_ap":3,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # Level10
 {"id": "tomb_stalker_02", "name": "Sepulchre Shade", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":10, "rarity": "rare", "base_xp":200, "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (20,100), "basic_attack": "ink swipe", "strong_attack": "vanishing cleave", "player_abilities": ["level_1_hostile_ability_shadow_flicker", "lv2_hostile_ability_dark_dark_spirit_void_veil"], "base_str":5, "base_dex":9, "base_con":4, "base_int":6, "base_hp":140, "base_ap":8, "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":2},

 {"id": "vault_keeper", "name": "Vault Keeper", "hostile_type": "humanoid", "role": "support", "min_spawn_level":10, "rarity": "rare", "base_xp":180,
 "common_drop": "stimulant_med", "rare_drop": "stimulant_large", "money_range": (20,120),
 "basic_attack": "staff bash", "strong_attack": "seal slam", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":5, "base_dex":3, "base_con":6, "base_int":4, "base_hp":120, "base_ap":5,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":1},

 {"id": "ossuary_lantern", "name": "Ossuary Lantern", "hostile_type": "undead", "role": "hazard", "min_spawn_level":10, "rarity": "superrare", "base_xp":520,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,340),
 "basic_attack": "lantern swing", "strong_attack": "blinding flare", "player_abilities": ["level_1_hostile_ability_light_spirit_prism_burst", "lv2_hostile_ability_dark_dark_spirit_void_veil"],
 "base_str":8, "base_dex":5, "base_con":10, "base_int":9, "base_hp":240, "base_ap":10,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":2},
]
