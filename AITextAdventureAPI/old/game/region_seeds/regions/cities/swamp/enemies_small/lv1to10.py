# Level1-10 hostile seeds for small swamp city (Gnashwater Hollow)
# Export a list named SEEDS_LV1TO10 used by constants_enemies_small_city.py
SEEDS_LV1TO10 = [
 # Level1: ensure common, uncommon and rare at level1
 {"id": "toss_vagrant", "name": "Tossed Vagrant", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "panicked shove", "strong_attack": "desperate flail", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":1, "base_int":1, "base_hp":6, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 {"id": "street_urchin", "name": "Street Urchin", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":14,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "quick jab", "strong_attack": "purse swipe", "player_abilities": None,
 "base_str":2, "base_dex":6, "base_con":1, "base_int":2, "base_hp":10, "base_ap":2,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "cursed_whisper", "name": "Cursed Whisper", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":1, "rarity": "rare", "base_xp":44,
 "common_drop": "herb_minor", "rare_drop": "tome_int", "money_range": (2,12),
 "basic_attack": "murmured chill", "strong_attack": "caustic wail", "player_abilities": ["shadow_lash"],
 "base_str":1, "base_dex":4, "base_con":1, "base_int":6, "base_hp":18, "base_ap":6,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 # Level2
 {"id": "marsh_leech", "name": "Marsh Leach", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "bite", "strong_attack": "sap", "player_abilities": None,
 "base_str":1, "base_dex":2, "base_con":1, "base_int":1, "base_hp":6, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "dock_dame", "name": "Dockside Dame", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "purse bash", "strong_attack": "heel-to-face", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":2, "base_hp":10, "base_ap":2,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "confused_courier_gal", "name": "Confused Courier Girl", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "uncommon", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "quick jab of a parcel", "strong_attack": "vicious elbow parcel flurry", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":2, "base_hp":10, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 # Level3
 {"id": "gutter_pincher", "name": "Gutter Pincher", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "common", "base_xp":8,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "nips with sticky fingers", "strong_attack": "snatch-and-dash", "player_abilities": None,
 "base_str":1, "base_dex":5, "base_con":1, "base_int":2, "base_hp":8, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "fang_pack", "name": "Fang Pack", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "bite in a coordinated swarm", "strong_attack": "pounce & maul", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":1, "base_hp":12, "base_ap":3,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "neon_drifter_swamp", "name": "Neon Drifter (The party in the Swamp)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,10),
 "basic_attack": "glinting kick", "strong_attack": "spinning neon barrage", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":2, "base_int":2, "base_hp":14, "base_ap":3, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # Level4
 {"id": "mire_hound", "name": "Mire Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "snaps with muddy jaws", "strong_attack": "venomous lunge", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":1, "base_hp":10, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "tunnel_mole3", "name": "Gutter Mole", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":4, "rarity": "uncommon", "base_xp":28,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (3,14),
 "basic_attack": "stabs with a broken fingernail", "strong_attack": "backstab from the drain", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":3, "base_hp":20, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 {"id": "skiff_runner", "name": "Skiff Runner", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":50,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (10,64),
 "basic_attack": "jab with a boat hook", "strong_attack": "crate toss", "player_abilities": None,
 "base_str":3, "base_dex":5, "base_con":2, "base_int":3, "base_hp":26, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # Level5
 {"id": "beggar_spoon", "name": "Beggar with a Spoon", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "common", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "pokes with a spoon", "strong_attack": "soup-stab", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":1, "base_int":2, "base_hp":9, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "ledger_fixer", "name": "Ledger Fixer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":5, "rarity": "rare", "base_xp":48,
 "common_drop": "lockpick", "rare_drop": "tome_dex", "money_range": (8,56),
 "basic_attack": "scribbles a lacerating note", "strong_attack": "pen-&-dagger", "player_abilities": ["hack_overload", "emp_burst"],
 "base_str":2, "base_dex":3, "base_con":2, "base_int":6, "base_hp":24, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 # Level6
 {"id": "bilge_bouncer", "name": "Bilge Bouncer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":56,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (6,30),
 "basic_attack": "throws patrons with a scowl", "strong_attack": "bottle opera", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":3, "base_int":2, "base_hp":30, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 {"id": "wailing_thing", "name": "Wailing Thing", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":6, "rarity": "rare", "base_xp":136,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (4,36),
 "basic_attack": "piercing cry", "strong_attack": "bog-shriek", "player_abilities": ["night_whisper"],
 "base_str":1, "base_dex":4, "base_con":1, "base_int":8, "base_hp":28, "base_ap":8,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 # Level7
 {"id": "smash_thug_mire", "name": "Club-Thug of the Mire", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "common", "base_xp":20,
 "common_drop": "herb_med", "rare_drop": "cloth_cap", "money_range": (6,24),
 "basic_attack": "club jab", "strong_attack": "club slam", "player_abilities": None,
 "base_str":3, "base_dex":2, "base_con":2, "base_int":1, "base_hp":14, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "spectral_hag2", "name": "Spectral Hag", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":7, "rarity": "uncommon", "base_xp":46,
 "common_drop": "herb_med", "rare_drop": "tome_con", "money_range": (6,34), "basic_attack": "withering curse", "strong_attack": "spectral claws", "player_abilities": ["shadow_lash"],
 "base_str":1, "base_dex":3, "base_con":2, "base_int":9, "base_hp":36, "base_ap":10,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 # Level8
 {"id": "plank_rogue", "name": "Plank Rogue", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":8, "rarity": "rare", "base_xp":110,
 "common_drop": "lockpick", "rare_drop": "pipe_wrench", "money_range": (18,80),
 "basic_attack": "silent plank-stab", "strong_attack": "lethal board dance", "player_abilities": ["precise_strike", "poison_dart"],
 "base_str":3, "base_dex":8, "base_con":3, "base_int":3, "base_hp":30, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # Level9
 {"id": "marsh_marksman", "name": "Marsh Marksman", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":9, "rarity": "rare", "base_xp":120,
 "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (24,100),
 "basic_attack": "precise marsh shot", "strong_attack": "headshot from reeds", "player_abilities": ["quick_shot"],
 "base_str":3, "base_dex":7, "base_con":3, "base_int":3, "base_hp":32, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # Level10 - superrare
 {"id": "dream_eater", "name": "Dream Eater", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":10, "rarity": "superrare", "base_xp":480,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,280), "basic_attack": "mind gnaw", "strong_attack": "maddening shriek", "player_abilities": ["nightmare_wave"],
 "base_str":3, "base_dex":6, "base_con":5, "base_int":14, "base_hp":140, "base_ap":14,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":4},
]
