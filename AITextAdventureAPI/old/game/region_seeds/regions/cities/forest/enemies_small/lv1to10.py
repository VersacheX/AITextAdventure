# Level1-10 hostile seeds for Thornshade Hamlet (small forest village)
# Split out from constants_enemies_small_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 {"id": "stump_rat", "name": "Stump Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "nips with drizzle-stained teeth", "strong_attack": "rabid gnaw", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":6, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "thatch_runner", "name": "Thatch Runner", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": "stimulant_small", "money_range": (1,6),
 "basic_attack": "snatch and dash", "strong_attack": "tripwire tumble", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":1, "base_int":2, "base_hp":10, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "twig_tot", "name": "Twig Tot", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "rare", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,8),
 "basic_attack": "poke with a splinter", "strong_attack": "tumble swarm", "player_abilities": None,
 "base_str":2, "base_dex":6, "base_con":2, "base_int":2, "base_hp":20, "base_ap":3,
 "str_per_level":0, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # min_spawn_level ==2
 {"id": "moss_barker", "name": "Moss Barker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (0,8),
 "basic_attack": "shout and splash", "strong_attack": "hot jug toss", "player_abilities": None,
 "base_str":2, "base_dex":2, "base_con":3, "base_int":1, "base_hp":12, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "stump_thug", "name": "Stump Thug", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "uncommon", "base_xp":22,
 "common_drop": "herb_med", "rare_drop": "cloth_gloves", "money_range": (4,18),
 "basic_attack": "club jab", "strong_attack": "root slam", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":3, "base_int":1, "base_hp":18, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==3
 {"id": "barkbard", "name": "Barkbard", "hostile_type": "humanoid", "role": "support", "min_spawn_level":3, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": "stimulant_small", "money_range": (1,10),
 "basic_attack": "singed lute slap", "strong_attack": "crescendo of thorns", "player_abilities": ["water_faith_lv1_mending_streams"],
 "base_str":1, "base_dex":5, "base_con":2, "base_int":5, "base_hp":14, "base_ap":3,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "leaf_hound", "name": "Leaf Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":16,
 "common_drop": "herb_minor", "rare_drop": "stimulant_small", "money_range": (2,12),
 "basic_attack": "snap bite", "strong_attack": "pouncing maul", "player_abilities": None,
 "base_str":4, "base_dex":5, "base_con":3, "base_int":1, "base_hp":22, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "nocturne_wisp", "name": "Nocturne Wisp", "hostile_type": "fey", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,8),
 "basic_attack": "sparkle jab", "strong_attack": "mirthful shock", "player_abilities": ["ice_skill_lv1_ice_shuriken"],
 "base_str":1, "base_dex":8, "base_con":1, "base_int":4, "base_hp":12, "base_ap":3,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # min_spawn_level ==4
 {"id": "sapling_swindler", "name": "Sapling Swindler", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":4, "rarity": "uncommon", "base_xp":36,
 "common_drop": "stimulant_small", "rare_drop": "dagger", "money_range": (6,28),
 "basic_attack": "fiddle with pockets", "strong_attack": "back-alley slice", "player_abilities": ["dark_magic_lv1_shadow_tendril"],
 "base_str":3, "base_dex":7, "base_con":2, "base_int":3, "base_hp":20, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "hollow_raider", "name": "Hollow Raider", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":60,
 "common_drop": "herb_med", "rare_drop": "leather_armor", "money_range": (10,40),
 "basic_attack": "axe swing", "strong_attack": "cleaving whirlwind", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":4, "base_int":1, "base_hp":30, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==5
 {"id": "nettlescribe", "name": "Nettle Scribe", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":44,
 "common_drop": "stimulant_small", "rare_drop": "tome_dex", "money_range": (8,36),
 "basic_attack": "inked scratch", "strong_attack": "parchment lash", "player_abilities": ["electric_fire_magic_lv2_arclance", "fire_magic_lv1_fireball"],
 "base_str":1, "base_dex":3, "base_con":2, "base_int":8, "base_hp":28, "base_ap":6,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 {"id": "sproutling", "name": "Sproutling", "hostile_type": "creature", "role": "damage", "min_spawn_level":5, "rarity": "common", "base_xp":40,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (4,18),
 "basic_attack": "needle poke", "strong_attack": "burst sprout", "player_abilities": None,
 "base_str":2, "base_dex":6, "base_con":3, "base_int":1, "base_hp":36, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==6
 {"id": "herbal_haglet", "name": "Herbal Haglet", "hostile_type": "humanoid", "role": "support", "min_spawn_level":6, "rarity": "rare", "base_xp":80,
 "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (12,60),
 "basic_attack": "sour pinch", "strong_attack": "potion lob", "player_abilities": ["light_faith_lv1_minor_heal"],
 "base_str":2, "base_dex":2, "base_con":5, "base_int":7, "base_hp":40, "base_ap":6,
 "str_per_level":0, "dex_per_level":0, "con_per_level":2, "int_per_level":2},

 {"id": "barnacle_bruiser", "name": "Barnacle Bruiser", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":70,
 "common_drop": "stimulant_small", "rare_drop": "cloth_cap", "money_range": (8,36),
 "basic_attack": "ramming shoulder", "strong_attack": "barnacle slam", "player_abilities": ["earth_fire_technique_lv2_berserker_tech"],
 "base_str":7, "base_dex":2, "base_con":5, "base_int":1, "base_hp":44, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==7
 {"id": "cottage_matron_small", "name": "Cottage Matron", "hostile_type": "humanoid", "role": "support", "min_spawn_level":7, "rarity": "uncommon", "base_xp":50,
 "common_drop": "herb_med", "rare_drop": "tome_con", "money_range": (6,30),
 "basic_attack": "rolling pin bash", "strong_attack": "boiling rebuke", "player_abilities": ["light_faith_lv1_minor_heal"],
 "base_str":3, "base_dex":2, "base_con":6, "base_int":4, "base_hp":56, "base_ap":5,
 "str_per_level":1, "dex_per_level":0, "con_per_level":2, "int_per_level":1},

 {"id": "cottage_matron_small_2", "name": "Cottage Matron", "hostile_type": "humanoid", "role": "support", "min_spawn_level":7, "rarity": "common", "base_xp":60,
 "common_drop": "herb_med", "rare_drop": "tome_con", "money_range": (6,30),
 "basic_attack": "rolling pin bash", "strong_attack": "boiling rebuke", "player_abilities": ["light_faith_lv1_minor_heal"],
 "base_str":4, "base_dex":3, "base_con":7, "base_int":4, "base_hp":66, "base_ap":6,
 "str_per_level":1, "dex_per_level":0, "con_per_level":2, "int_per_level":1},

 # min_spawn_level ==8
 {"id": "fen_phantom", "name": "Fen Phantom", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":8, "rarity": "rare", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": "tome_int", "money_range": (10,50),
 "basic_attack": "chill whisper", "strong_attack": "siphon moan", "player_abilities": ["level_1_hostile_ability_night_whisper", "level_1_hostile_ability_dark_magic_daze_whisper"],
 "base_str":1, "base_dex":4, "base_con":3, "base_int":10, "base_hp":60, "base_ap":8,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "hedge_lurker", "name": "Hedge Lurker", "hostile_type": "creature", "role": "damage", "min_spawn_level":8, "rarity": "common", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,36),
 "basic_attack": "mire bite", "strong_attack": "mudslide", "player_abilities": None,
 "base_str":5, "base_dex":4, "base_con":6, "base_int":2, "base_hp":120, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==9
 {"id": "ledger_guard", "name": "Ledger Guard", "hostile_type": "humanoid", "role": "support", "min_spawn_level":9, "rarity": "rare", "base_xp":120,
 "common_drop": "stimulant_small", "rare_drop": "stimulant_large", "money_range": (30,120),
 "basic_attack": "bitter prod", "strong_attack": "stunning ledger swing", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"],
 "base_str":5, "base_dex":4, "base_con":6, "base_int":3, "base_hp":80, "base_ap":6,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 {"id": "pond_rattler", "name": "Pond Rattler", "hostile_type": "creature", "role": "damage", "min_spawn_level":9, "rarity": "common", "base_xp":80,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (12,48),
 "basic_attack": "venom nip", "strong_attack": "coil snap", "player_abilities": None,
 "base_str":3, "base_dex":7, "base_con":4, "base_int":1, "base_hp":100, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==10
 {"id": "woodland_scout", "name": "Woodland Scout", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":10, "rarity": "common", "base_xp":140,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (20,88),
 "basic_attack": "swift jab", "strong_attack": "tracking barrage", "player_abilities": None,
 "base_str":6, "base_dex":8, "base_con":6, "base_int":3, "base_hp":160, "base_ap":6,
 "str_per_level":2, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "elder_herbalist", "name": "Elder Herbalist", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":10, "rarity": "superrare", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,320),
 "basic_attack": "potent pinch", "strong_attack": "vine of ages", "player_abilities": ["level_1_hostile_ability_light_faith_prism_burst"],
 "base_str":4, "base_dex":5, "base_con":10, "base_int":12, "base_hp":220, "base_ap":10,
 "str_per_level":1, "dex_per_level":1, "con_per_level":3, "int_per_level":4},
]
