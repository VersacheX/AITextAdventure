# Level1-10 hostile seeds for Hollerforge Hollow (small-city)
# Export a list named SEEDS_LV1TO10 used by constants_enemies_small_city.py
SEEDS_LV1TO10 = [
 # min_spawn_level =1 (ensure common, uncommon, rare present)
 {"id": "hobnail_scrapper", "name": "Hobnail Scrapper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "shoves with a hobnail boot", "strong_attack": "stomping punt", "player_abilities": None,
 "base_str":2, "base_dex":2, "base_con":2, "base_int":1, "base_hp":10, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "roundhouse_rummy", "name": "Roundhouse Rummy (keeps singing)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "tipsy hook", "strong_attack": "broken mug", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":2, "base_int":1, "base_hp":8, "base_ap":1,
 "str_per_level":0, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "log_beggar", "name": "Log Beggar (dramatic)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "rare", "base_xp":7,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "pathetic shove", "strong_attack": "desperate lunge", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":1, "base_int":2, "base_hp":7, "base_ap":1,
 "str_per_level":0, "dex_per_level":0, "con_per_level":0, "int_per_level":1},

 {"id": "stone_marmot", "name": "Stone Marmot", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "nip", "strong_attack": "rock toss", "player_abilities": None,
 "base_str":1, "base_dex":2, "base_con":2, "base_int":1, "base_hp":8, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # min_spawn_level =2
 {"id": "stump_shyster", "name": "Stump Shyster", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (1,10),
 "basic_attack": "slick palm", "strong_attack": "underhand grab", "player_abilities": None,
 "base_str":1, "base_dex":6, "base_con":1, "base_int":3, "base_hp":12, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "hollow_peddler", "name": "Hollow Peddler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "pamphlet flick", "strong_attack": "coin barrage", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":4, "base_hp":16, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "moss_nicker", "name": "Moss Nicker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (1,10),
 "basic_attack": "snatch and run", "strong_attack": "cartwheel stab", "player_abilities": None,
 "base_str":1, "base_dex":6, "base_con":1, "base_int":2, "base_hp":12, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "moss_nicker_2", "name": "Moss Nicker (alt)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (1,10),
 "basic_attack": "snatch and run", "strong_attack": "cartwheel stab", "player_abilities": None,
 "base_str":1, "base_dex":6, "base_con":1, "base_int":2, "base_hp":12, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "holler_fox", "name": "Holler Fox", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "swift bite", "strong_attack": "pouncing maul", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":1, "base_int":2, "base_hp":10, "base_ap":3,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 # min_spawn_level =3
 {"id": "picktoe_lin", "name": "Picktoe Lineman", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":26,
 "common_drop": "herb_minor", "rare_drop": "cloth_gloves", "money_range": (3,18),
 "basic_attack": "gravel swing", "strong_attack": "pit-cleaver", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":4, "base_int":1, "base_hp":26, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "secondhand_sally", "name": "Secondhand Sally (loud)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,12),
 "basic_attack": "shill jab", "strong_attack": "price-slap", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":2, "base_int":4, "base_hp":14, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "pit_beetle", "name": "Pit Beetle", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "chitin snap", "strong_attack": "acidic burst", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":3, "base_int":1, "base_hp":14, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "trail_hound", "name": "Trail Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "tear and snap", "strong_attack": "pouncing maul", "player_abilities": None,
 "base_str":3, "base_dex":4, "base_con":3, "base_int":1, "base_hp":18, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # min_spawn_level =4
 {"id": "rift_raider", "name": "Rift Raider", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":36,
 "common_drop": "herb_med", "rare_drop": "leather_armor", "money_range": (10,60),
 "basic_attack": "axe swing", "strong_attack": "cleaving whirlwind", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":3, "base_int":1, "base_hp":18, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "taproom_tapster", "name": "Taproom Tapster", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":20,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "towel swipe", "strong_attack": "bottle smash", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":3, "base_int":2, "base_hp":20, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "taproom_tapster_2", "name": "Taproom Tapster (alt)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":20,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "towel swipe", "strong_attack": "bottle smash", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":3, "base_int":2, "base_hp":20, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "forge_hewer", "name": "Forge Hewer", "hostile_type": "humanoid", "role": "support", "min_spawn_level":4, "rarity": "uncommon", "base_xp":40,
 "common_drop": "stimulant_small", "rare_drop": "cloth_gloves", "money_range": (6,28),
 "basic_attack": "hack with chisel", "strong_attack": "overhand spike", "player_abilities": ["reinforce_frame"],
 "base_str":6, "base_dex":2, "base_con":5, "base_int":1, "base_hp":34, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "rift_raider_2", "name": "Rift Raider (alt)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":36,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (10,60),
 "basic_attack": "axe swing", "strong_attack": "cleaving whirlwind", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":3, "base_int":1, "base_hp":18, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 # min_spawn_level =5
 {"id": "hollow_tinker", "name": "Hollow Tinker", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":5, "rarity": "uncommon", "base_xp":50,
 "common_drop": "lockpick", "rare_drop": "tome_int", "money_range": (8,36),
 "basic_attack": "sprays shrapnel", "strong_attack": "overclock jab", "player_abilities": ["hack_overload"],
 "base_str":2, "base_dex":5, "base_con":3, "base_int":7, "base_hp":34, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":2},

 {"id": "mire_spider", "name": "Mire Spider", "hostile_type": "creature", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":40,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (3,24),
 "basic_attack": "web snap", "strong_attack": "venom maul", "player_abilities": ["venom_trace"],
 "base_str":2, "base_dex":6, "base_con":3, "base_int":2, "base_hp":34, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "axle_mason", "name": "Axle Mason", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":48,
 "common_drop": "herb_med", "rare_drop": "tome_dex", "money_range": (8,40),
 "basic_attack": "stone toss", "strong_attack": "mortar slam", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":5, "base_int":2, "base_hp":40, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "sly_cooperette", "name": "Sly Cooperette", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":5, "rarity": "uncommon", "base_xp":48,
 "common_drop": "lockpick", "rare_drop": "pipe_wrench", "money_range": (6,36),
 "basic_attack": "flick dagger", "strong_attack": "lethal twirl", "player_abilities": ["shadow_flicker"],
 "base_str":2, "base_dex":7, "base_con":2, "base_int":3, "base_hp":28, "base_ap":5,
 "str_per_level":1, "dex_per_level":3, "con_per_level":0, "int_per_level":1},

 # min_spawn_level =6
 {"id": "timber_watch", "name": "Timber Watch", "hostile_type": "humanoid", "role": "support", "min_spawn_level":6, "rarity": "rare", "base_xp":90,
 "common_drop": "stimulant_med", "rare_drop": "kevlar_vest", "money_range": (20,80),
 "basic_attack": "bark-and-bash", "strong_attack": "guarding crush", "player_abilities": ["reinforce_frame"],
 "base_str":5, "base_dex":3, "base_con":6, "base_int":2, "base_hp":48, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "stone_viper", "name": "Stone Viper", "hostile_type": "creature", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":48,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (4,30),
 "basic_attack": "venomous bite", "strong_attack": "constricting coil", "player_abilities": ["venom_trace"],
 "base_str":2, "base_dex":6, "base_con":3, "base_int":2, "base_hp":36, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "ledger_band", "name": "Ledger Bandit", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":6, "rarity": "uncommon", "base_xp":52,
 "common_drop": "lockpick", "rare_drop": "cloth_pants", "money_range": (6,30),
 "basic_attack": "slash-and-claim", "strong_attack": "purse rip", "player_abilities": ["smoke_bomb"],
 "base_str":3, "base_dex":4, "base_con":2, "base_int":2, "base_hp":26, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "ledger_louse", "name": "Ledger Louse", "hostile_type": "humanoid", "role": "support", "min_spawn_level":6, "rarity": "uncommon", "base_xp":60,
 "common_drop": "stimulant_small", "rare_drop": "lockpick", "money_range": (6,40),
 "basic_attack": "tally swipe", "strong_attack": "receipt pummel", "player_abilities": ["reinforce_frame"],
 "base_str":3, "base_dex":3, "base_con":4, "base_int":5, "base_hp":36, "base_ap":4,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":2},

 # min_spawn_level =7
 {"id": "anvil_humorist", "name": "Anvil Humorist", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":44,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (2,24),
 "basic_attack": "drops a pun anvil", "strong_attack": "groan-smash", "player_abilities": None,
 "base_str":3, "base_dex":2, "base_con":4, "base_int":5, "base_hp":36, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":2},

 {"id": "rivet_madame", "name": "Rivet Madame", "hostile_type": "humanoid", "role": "support", "min_spawn_level":7, "rarity": "uncommon", "base_xp":60,
 "common_drop": "herb_med", "rare_drop": "tome_dex", "money_range": (6,30),
 "basic_attack": "wrenching jab", "strong_attack": "precision wrench", "player_abilities": ["hack_overload", "reinforce_frame"],
 "base_str":3, "base_dex":4, "base_con":3, "base_int":6, "base_hp":38, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "snare_reaver", "name": "Snare Reaver", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":70,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (6,36),
 "basic_attack": "trip and slash", "strong_attack": "binding coil", "player_abilities": None,
 "base_str":4, "base_dex":5, "base_con":3, "base_int":2, "base_hp":44, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # min_spawn_level =8
 {"id": "granny_bruiser", "name": "Granny Bruiser", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "uncommon", "base_xp":62,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (6,36),
 "basic_attack": "needle jab", "strong_attack": "rocking chair maul", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":5, "base_int":3, "base_hp":56, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "guild_rigger", "name": "Guild Rigger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "rare", "base_xp":120,
 "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (30,120),
 "basic_attack": "snare punch", "strong_attack": "rope blast", "player_abilities": ["quick_shot"],
 "base_str":3, "base_dex":6, "base_con":4, "base_int":3, "base_hp":40, "base_ap":6,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "furnace_wail", "name": "Furnace Wail", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":8, "rarity": "rare", "base_xp":140,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (4,36),
 "basic_attack": "keening clang", "strong_attack": "soul flare", "player_abilities": ["night_whisper"],
 "base_str":1, "base_dex":4, "base_con":2, "base_int":9, "base_hp":36, "base_ap":8,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 # min_spawn_level =9
 {"id": "ironshade", "name": "Ironshade", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":9, "rarity": "uncommon", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": "lockpick", "money_range": (6,40),
 "basic_attack": "shade swipe", "strong_attack": "vanish maul", "player_abilities": ["shadow_flicker"],
 "base_str":4, "base_dex":7, "base_con":4, "base_int":3, "base_hp":66, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # min_spawn_level =10
 {"id": "slag_watcher", "name": "Slag Watcher", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":10, "rarity": "rare", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (18,88),
 "basic_attack": "slag sputter", "strong_attack": "molten lash", "player_abilities": ["arcane_blast", "corrosive_spit"],
 "base_str":3, "base_dex":3, "base_con":6, "base_int":8, "base_hp":120, "base_ap":8,
 "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "lesser_nightmare", "name": "Lesser Nightmare", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":10, "rarity": "superrare", "base_xp":320,
 "common_drop": "stimulant_small", "rare_drop": "herb_major", "money_range": (40,160),
 "basic_attack": "shiver touch", "strong_attack": "maddening howl", "player_abilities": ["nightmare_wave"],
 "base_str":3, "base_dex":4, "base_con":4, "base_int":10, "base_hp":140, "base_ap":10,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},
]
