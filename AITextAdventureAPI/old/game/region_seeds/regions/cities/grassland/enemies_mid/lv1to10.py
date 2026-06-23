# Level1-10 hostile seeds for Highsteeple Crossing (mid city)
# Split out from constants_enemies_mid_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 {"id": "coin_mumbler", "name": "Coin Mumbler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":8,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "mumbles and swipes", "strong_attack": "bold snatch", "player_abilities": None,
 "base_str":1, "base_dex":5, "base_con":1, "base_int":2, "base_hp":9, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "shifty_apprentice", "name": "Shifty Apprentice", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":9,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "light jab", "strong_attack": "sudden vanish", "player_abilities": None,
 "base_str":1, "base_dex":5, "base_con":1, "base_int":2, "base_hp":9, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "homeless_lyric", "name": "Homeless Lyric (loud)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "sloppy shove", "strong_attack": "lamenting wail", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":1, "base_int":2, "base_hp":6, "base_ap":1,
 "str_per_level":0, "dex_per_level":0, "con_per_level":0, "int_per_level":1},

 {"id": "taproom_fly", "name": "Taproom Fly", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "drunken hook", "strong_attack": "broken bottle", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":2, "base_int":1, "base_hp":6, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 {"id": "alley_feral", "name": "Alley Feral", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "rare", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "claw maul", "strong_attack": "ferocious pounce", "player_abilities": None,
 "base_str":1, "base_dex":4, "base_con":1, "base_int":1, "base_hp":8, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 # level2
 {"id": "shadow_mouser", "name": "Shadow Mouser", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "paws at you", "strong_attack": "pouncing ambush", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":2, "base_int":1, "base_hp":12, "base_ap":3,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "beggar_cutpurse", "name": "Beggar Cutpurse", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "poke with a spoon", "strong_attack": "knife behind a coin cup", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":1, "base_int":1, "base_hp":10, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "civic_dame", "name": "Civic Dame", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "heavy purse", "strong_attack": "deadly heel", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":3, "base_hp":12, "base_ap":2,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "sewer_scrap", "name": "Sewer Scrap", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":9,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "fierce bite", "strong_attack": "savage bite", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":7, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 # level3
 {"id": "rumor_monger_mid", "name": "Rumor Monger", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "spiteful word", "strong_attack": "panic lash", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":1, "base_int":4, "base_hp":12, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "pewter_brawler", "name": "Pewter Brawler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":26,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,14),
 "basic_attack": "swings a pewter mug", "strong_attack": "staggering haymaker", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":4, "base_int":1, "base_hp":22, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "inked_row", "name": "Inked Row (tattoo show-off)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":24,
 "common_drop": "herb_med", "rare_drop": "cloth_pants", "money_range": (4,18),
 "basic_attack": "deez knuckles", "strong_attack": "furious flurry", "player_abilities": None,
 "base_str":3, "base_dex":3, "base_con":2, "base_int":1, "base_hp":14, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "rat_warren_king", "name": "Rat Warren King", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":28,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,16),
 "basic_attack": "bites fiercely", "strong_attack": "swarming gnaw", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":3, "base_int":1, "base_hp":18, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # level4
 {"id": "sacred_hound", "name": "Sacred Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":14,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "snaps with righteous teeth", "strong_attack": "charging maul", "player_abilities": None,
 "base_str":4, "base_dex":5, "base_con":4, "base_int":1, "base_hp":20, "base_ap":3,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "mole_apothecary", "name": "Mole Apothecary", "hostile_type": "humanoid", "role": "support", "min_spawn_level":4, "rarity": "uncommon", "base_xp":30,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (3,18),
 "basic_attack": "stabs with a small scalpel", "strong_attack": "tunnel lunge", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":4, "base_hp":24, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 {"id": "rogue_minstrel", "name": "Rogue Minstrel (off-key)", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":4, "rarity": "uncommon", "base_xp":36,
 "common_drop": "herb_med", "rare_drop": "pipe_wrench", "money_range": (5,22),
 "basic_attack": "launches a sour verse", "strong_attack": "emotional strike", "player_abilities": ["dark_magic_lv4_nightmare_echo"],
 "base_str":2, "base_dex":6, "base_con":2, "base_int":4, "base_hp":22, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "vesper_dancer", "name": "Vesper Dancer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":22,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "graceful kick", "strong_attack": "spinning flourish", "player_abilities": None,
 "base_str":2, "base_dex":6, "base_con":2, "base_int":2, "base_hp":14, "base_ap":3,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # level5
 {"id": "alderman_ruffians", "name": "Alderman Ruffians", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":44,
 "common_drop": "herb_med", "rare_drop": "cloth_gloves", "money_range": (10,45),
 "basic_attack": "throws a ledger", "strong_attack": "coordinated shove", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":4, "base_int":2, "base_hp":38, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 # level6
 {"id": "canon_enforcer", "name": "Canon Enforcer", "hostile_type": "humanoid", "role": "support", "min_spawn_level":6, "rarity": "rare", "base_xp":80,
 "common_drop": "stimulant_small", "rare_drop": "cloth_gloves", "money_range": (10,50),
 "basic_attack": "bashes with a ceremonial staff", "strong_attack": "crushing consecration", "player_abilities": ["fire_earth_technique_lv3_embershield"],
 "base_str":6, "base_dex":3, "base_con":6, "base_int":2, "base_hp":36, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "raider_crossbow", "name": "Raider Crossbowman", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "rare", "base_xp":68,
 "common_drop": "herb_major", "rare_drop": "machete", "money_range": (18,70),
 "basic_attack": "axes with gusto", "strong_attack": "whirling cleave", "player_abilities": None,
 "base_str":5, "base_dex":4, "base_con":4, "base_int":1, "base_hp":36, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "doorwatch", "name": "Doorwatch (inn bouncer)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":62,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (6,30),
 "basic_attack": "shoulder ram", "strong_attack": "haymaker swing", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":5, "base_int":1, "base_hp":34, "base_ap":3,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "wailing_bell", "name": "Wailing Bell", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":6, "rarity": "rare", "base_xp":140,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (5,40),
 "basic_attack": "piercing wail", "strong_attack": "banshee shriek", "player_abilities": ["dark_magic_lv4_nightmare_echo"],
 "base_str":1, "base_dex":4, "base_con":1, "base_int":8, "base_hp":28, "base_ap":8,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 # level7
 {"id": "altar_fixit", "name": "Altar Fixit (greasy smile)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":48,
 "common_drop": "lockpick", "rare_drop": "tome_dex", "money_range": (8,40),
 "basic_attack": "fiddles with a brazier", "strong_attack": "electrostatic lurch", "player_abilities": ["air_tech_lv4_gale_surge"] if False else None,
 "base_str":2, "base_dex":4, "base_con":3, "base_int":6, "base_hp":28, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "smuggler_chorister", "name": "Smuggler Chorister", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":50,
 "common_drop": "lockpick", "rare_drop": "stimulant_med", "money_range": (12,60),
 "basic_attack": "brandishes a wrapped relic", "strong_attack": "poisoned dart", "player_abilities": None,
 "base_str":3, "base_dex":5, "base_con":2, "base_int":3, "base_hp":30, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "void_moth", "name": "Void Moth", "hostile_type": "creature", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":88,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (2,30),
 "basic_attack": "scales of shadow", "strong_attack": "venomous gust", "player_abilities": None,
 "base_str":2, "base_dex":8, "base_con":3, "base_int":2, "base_hp":40, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":0},

 {"id": "siren_of_halls", "name": "Siren of Halls", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":7, "rarity": "rare", "base_xp":72,
 "common_drop": "stimulant_small", "rare_drop": "tome_int", "money_range": (12,60),
 "basic_attack": "siren song", "strong_attack": "mesmerize", "player_abilities": ["light_faith_lv4_hearthsong", "dark_magic_lv4_nightmare_echo"],
 "base_str":2, "base_dex":5, "base_con":2, "base_int":7, "base_hp":30, "base_ap":6,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":3},

 # level8
 {"id": "curio_snatcher", "name": "Curio Snatcher", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "rare", "base_xp":92,
 "common_drop": "stimulant_med", "rare_drop": "herb_major", "money_range": (25,120),
 "basic_attack": "pries with a hooked pick", "strong_attack": "crippling pry-stab", "player_abilities": None,
 "base_str":2, "base_dex":6, "base_con":2, "base_int":4, "base_hp":32, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "spectral_midwife", "name": "Spectral Midwife", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":8, "rarity": "uncommon", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": "tome_con", "money_range": (8,44),
 "basic_attack": "withering curse", "strong_attack": "spectral claws", "player_abilities": ["dark_magic_lv4_mind_shiver"],
 "base_str":1, "base_dex":3, "base_con":2, "base_int":9, "base_hp":36, "base_ap":10,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 # level9
 {"id": "jester_sermon", "name": "Jester of Sermon", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":9, "rarity": "rare", "base_xp":98,
 "common_drop": "stimulant_small", "rare_drop": "dagger", "money_range": (10,60),
 "basic_attack": "juggling knives", "strong_attack": "banana peel ambush", "player_abilities": ["air_skill_lv4_gale_dash"],
 "base_str":3, "base_dex":8, "base_con":3, "base_int":5, "base_hp":34, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 {"id": "vault_warden", "name": "Vault Warden", "hostile_type": "humanoid", "role": "support", "min_spawn_level":9, "rarity": "uncommon", "base_xp":48,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (12,50),
 "basic_attack": "bashes with a ledger", "strong_attack": "stunning baton strike", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":4, "base_int":3, "base_hp":30, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":1},

 {"id": "elder_root", "name": "Elder Root", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":9, "rarity": "rare", "base_xp":200,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (20,100),
 "basic_attack": "root whip", "strong_attack": "barbed crush", "player_abilities": None,
 "base_str":12, "base_dex":2, "base_con":10, "base_int":2, "base_hp":160, "base_ap":4,
 "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "umbral_courser", "name": "Umbral Courser", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":9, "rarity": "uncommon", "base_xp":180,
 "common_drop": "herb_med", "rare_drop": "lockpick", "money_range": (6,48),
 "basic_attack": "dark slash", "strong_attack": "vanishing strike", "player_abilities": ["dark_magic_lv4_mind_shiver"],
 "base_str":5, "base_dex":10, "base_con":4, "base_int":3, "base_hp":80, "base_ap":7,
 "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # level10
 {"id": "steeple_sniper", "name": "Steeple Sniper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":10, "rarity": "rare", "base_xp":120,
 "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (30,100),
 "basic_attack": "takes a patient shot", "strong_attack": "aimed salvo", "player_abilities": ["air_skill_lv1_smoke_bomb"],
 "base_str":2, "base_dex":7, "base_con":2, "base_int":3, "base_hp":30, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 {"id": "wraith_chalice", "name": "Wraith Chalice", "hostile_type": "undead", "role": "hazard", "min_spawn_level":10, "rarity": "superrare", "base_xp":260,
 "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (25,120),
 "basic_attack": "spectral blade", "strong_attack": "ghostly cleave", "player_abilities": None,
 "base_str":8, "base_dex":6, "base_con":6, "base_int":3, "base_hp":120, "base_ap":8,
 "str_per_level":2, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "plague_baker_mid", "name": "Plague Baker", "hostile_type": "undead", "role": "hazard", "min_spawn_level":10, "rarity": "uncommon", "base_xp":160,
 "common_drop": "ointment", "rare_drop": "stimulant_large", "money_range": (5,60),
 "basic_attack": "diseased smite", "strong_attack": "virulent spray", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":6, "base_int":5, "base_hp":120, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":1},
]
