# Level1-10 hostile seeds for Bayou Nocturne (mid-city)
# Export a list named SEEDS_LV1TO10 used by constants_enemies_mid_city.py
SEEDS_LV1TO10 = [
 # Level1: include common, uncommon, rare
 {"id": "bayou_pick", "name": "Bayou Pick", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":1, "rarity": "common", "base_xp":8,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "nicks with a trinket", "strong_attack": "snatch-and-run", "player_abilities": None,
 "base_str":1, "base_dex":5, "base_con":1, "base_int":2, "base_hp":9, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "skulk_dog", "name": "Skulk Dog", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "lunges with grime teeth", "strong_attack": "dirty bite", "player_abilities": None,
 "base_str":2, "base_dex":2, "base_con":1, "base_int":1, "base_hp":8, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "tattered_vagrant", "name": "Tattered Vagrant", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "shoves with muffled hands", "strong_attack": "desperate lunge", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":1, "base_int":1, "base_hp":6, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 {"id": "last_call", "name": "Last Call", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6, "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "drunken swing", "strong_attack": "broken bottle surprise", "player_abilities": [],
 "base_str":1, "base_dex":1, "base_con":2, "base_int":1, "base_hp":6, "base_ap":1, "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 {"id": "marsh_scurrier", "name": "Marsh Scurrier", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6, "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4), "basic_attack": "nibble", "strong_attack": "scrab maul", "player_abilities": None, "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":8, "base_ap":1, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 # ensure at least one uncommon and one rare at level1
 {"id": "board_bandit", "name": "Boardwalk Bandit", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":1, "rarity": "uncommon", "base_xp":28,
 "common_drop": "stimulant_small", "rare_drop": "cloth_pants", "money_range": (3,14),
 "basic_attack": "slash with a plank", "strong_attack": "precise splinter stab", "player_abilities": [ "level_1_hostile_ability_smoke_screen" ],
 "base_str":3, "base_dex":3, "base_con":2, "base_int":1, "base_hp":14, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "slick_rogue", "name": "Slick Rogue", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":1, "rarity": "rare", "base_xp":48,
 "common_drop": "stimulant_small", "rare_drop": "pipe_wrench", "money_range": (10,44),
 "basic_attack": "backstab from the shadows", "strong_attack": "toxic flourish", "player_abilities": [ "level_1_hostile_ability_shadow_flicker", "level_1_hostile_ability_poison_dart" ],
 "base_str":2, "base_dex":5, "base_con":2, "base_int":2, "base_hp":12, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # Level2
 {"id": "angry_beggar_blade", "name": "Angry Beggar", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":8, "common_drop": "herb_minor", "money_range": (0,6),
 "basic_attack": "pokes with a spoon", "strong_attack": "stabby-goo", "player_abilities": [],
 "base_str":2, "base_dex":3, "base_con":1, "base_int":1, "base_hp":9, "base_ap":2, "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "undercity_rat", "name": "Undercity Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":9, "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "ferocious bite", "strong_attack": "savage bite", "player_abilities": [],
 "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":7, "base_ap":1, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "dame_of_streets", "name": "Dame of the Docks", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12, "common_drop": "herb_minor", "money_range": (1,8),
 "basic_attack": "heavy purse bash", "strong_attack": "heel of doom", "player_abilities": [],
 "base_str":2, "base_dex":4, "base_con":2, "base_int":2, "base_hp":10, "base_ap":2, "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "jackal_pack", "name": "Pack Jackal", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "bites in a pack", "strong_attack": "venomous maul", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":1, "base_hp":10, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "lost_courier_gal", "name": "Lost Courier Girl", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":10, "common_drop": "herb_minor", "money_range": (1,6),
 "basic_attack": "quick jab of a parcel", "strong_attack": "vicious elbow parcel flurry", "base_str":2, "base_dex":4, "base_con":2, "base_int":2, "base_hp":10, "base_ap":2, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "bog_wolf", "name": "Mire Wolf", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "uncommon", "base_xp":18,
 "common_drop": "herb_med", "rare_drop": "stimulant_med", "money_range": (4,16),
 "basic_attack": "slashes with muddy claws", "strong_attack": "pouncing maul", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":1, "base_hp":12, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "smash_thug_swamp", "name": "Thug of the Swamp", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":20,
 "common_drop": "herb_med", "rare_drop": "cloth_cap", "money_range": (6,24),
 "basic_attack": "club jab", "strong_attack": "club slam", "player_abilities": None,
 "base_str":3, "base_dex":2, "base_con":2, "base_int":1, "base_hp":14, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 # Level3
 {"id": "muck_brawler", "name": "Muck Brawler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":26,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "flails in the muck", "strong_attack": "mudslide slam", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":4, "base_int":1, "base_hp":22, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "tattooed_rascal", "name": "Tattooed Rascal", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":20, "common_drop": "herb_med", "money_range": (4,18),
 "basic_attack": "knuckle jab covered in ink", "strong_attack": "furious flurry of tiny tattoos", "player_abilities": [],
 "base_str":3, "base_dex":3, "base_con":2, "base_int":1, "base_hp":14, "base_ap":3, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "rumor_monger_bay", "name": "Rumor Monger", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "common", "base_xp":14, "common_drop": "herb_minor", "money_range": (1,8),
 "basic_attack": "spiteful gossip lash", "strong_attack": "panic-inducing rumor", "base_str":1, "base_dex":3, "base_con":1, "base_int":4, "base_hp":10, "base_ap":2, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "flitting_flapper", "name": "Flitting Flapper", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "uncommon", "base_xp":18, "common_drop": "herb_med", "money_range": (2,12),
 "basic_attack": "scratching vaudeville", "strong_attack": "deadly twirl", "player_abilities": [],
 "base_str":2, "base_dex":6, "base_con":2, "base_int":2, "base_hp":12, "base_ap":3, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "watch_dog", "name": "Boardwalk Watchdog", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":16,
 "common_drop": "stimulant_small", "rare_drop": "cloth_gloves", "money_range": (6,14),
 "basic_attack": "bites with righteous fury", "strong_attack": "savage maul", "player_abilities": None,
 "base_str":3, "base_dex":2, "base_con":3, "base_int":1, "base_hp":16, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "bog_wolf_02", "name": "Bog Pup", "hostile_type": "creature", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":20, "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,10), "basic_attack": "snap", "strong_attack": "pounce maul", "player_abilities": None, "base_str":2, "base_dex":4, "base_con":2, "base_int":1, "base_hp":14, "base_ap":3, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # Level4
 {"id": "watch_dog_02", "name": "Board Pup", "hostile_type": "creature", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":12, "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,10), "basic_attack": "snarl", "strong_attack": "pup maul", "player_abilities": None, "base_str":2, "base_dex":4, "base_con":2, "base_int":1, "base_hp":12, "base_ap":2, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "neon_street_dancer", "name": "Neon Street Dancer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":18, "common_drop": "herb_minor", "money_range": (2,10),
 "basic_attack": "dirty dance kick", "strong_attack": "spinning neon kick", "player_abilities": [],
 "base_str":2, "base_dex":5, "base_con":2, "base_int":2, "base_hp":14, "base_ap":3, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "sloop_raider", "name": "Sloop Raider", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":4, "rarity": "rare", "base_xp":64,
 "common_drop": "herb_major", "rare_drop": "leather_armor", "money_range": (18,60),
 "basic_attack": "axe-to-board swing", "strong_attack": "cleaving tide whirlwind", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":3, "base_int":1, "base_hp":18, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "tunnel_mole2", "name": "Gutter Mole", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":28,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (3,14),
 "basic_attack": "stabs with a broken fingernail", "strong_attack": "backstab from the drain", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":3, "base_hp":20, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 # Level5
 {"id": "sly_madam_bay", "name": "Sly Madam of the Bay", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":36, "common_drop": "stimulant_small", "money_range": (6,28),
 "basic_attack": "swift con move", "strong_attack": "outsmarting elbow", "player_abilities": [],
 "base_str":2, "base_dex":4, "base_con":2, "base_int":4, "base_hp":20, "base_ap":4, "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "swamp_cultist", "name": "Lily-Cultist", "hostile_type": "humanoid", "role": "support", "min_spawn_level":5, "rarity": "rare", "base_xp":78,
 "common_drop": "herb_major", "rare_drop": "short_sword", "money_range": (22,80),
 "basic_attack": "casts a bog bolt", "strong_attack": "bone-lotus spear", "player_abilities":[ "light_spirit_lv1_minor_heal", "level_1_hostile_ability_arcane_blast", "level_1_hostile_ability_bone_spear" ],
 "base_str":1, "base_dex":2, "base_con":2, "base_int":4, "base_hp":12, "base_ap":6, "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 # Level6
 {"id": "bouncer_gator", "name": "Gator Bouncer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":58, "common_drop": "stimulant_small", "money_range": (6,34),
 "basic_attack": "towel swipe (but with teeth)", "strong_attack": "bottle smash of doom", "player_abilities": [],
 "base_str":4, "base_dex":3, "base_con":3, "base_int":2, "base_hp":30, "base_ap":4, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 {"id": "neglected_banshee", "name": "Neglected Banshee of the Bog", "hostile_type": "spirit", "role": "support", "min_spawn_level":6, "rarity": "rare", "base_xp":136, "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (4,36),
 "basic_attack": "piercing wail", "strong_attack": "baneful shriek", "player_abilities": ["level_1_hostile_ability_night_whisper"], "base_str":1, "base_dex":4, "base_con":1, "base_int":8, "base_hp":28, "base_ap":8, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 # Level7
 {"id": "bay_void_spider", "name": "Bay Void Spider", "hostile_type": "creature", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":92, "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (2,30), "basic_attack": "fanged bite", "strong_attack": "venomous tear", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"], "base_str":2, "base_dex":8, "base_con":3, "base_int":2, "base_hp":40, "base_ap":6, "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":0},

 # Level8
 {"id": "spectral_hag_bay2", "name": "Spectral Hag", "hostile_type": "spirit", "role": "support", "min_spawn_level":8, "rarity": "uncommon", "base_xp":120, "common_drop": "herb_med", "rare_drop": "tome_con", "money_range": (8,44), "basic_attack": "withering curse", "strong_attack": "spectral claws", "player_abilities": ["level_1_hostile_ability_shadow_lash"], "base_str":1, "base_dex":3, "base_con":2, "base_int":9, "base_hp":36, "base_ap":10, "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 {"id": "antique_snatcher", "name": "Antique Snatcher", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "rare", "base_xp":92, "common_drop": "stimulant_med", "rare_drop": "herb_major", "money_range": (24,100), "basic_attack": "stab with a crooked spatula", "strong_attack": "crippling antiquity swing", "player_abilities": [], "base_str":2, "base_dex":5, "base_con":2, "base_int":3, "base_hp":28, "base_ap":5, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 # Level9
 {"id": "plague_stoker_bay", "name": "Plague Stoker", "hostile_type": "undead", "role": "damage", "min_spawn_level":9, "rarity": "uncommon", "base_xp":160, "common_drop": "ointment", "rare_drop": "stimulant_large", "money_range": (6,60), "basic_attack": "diseased swipe", "strong_attack": "virulent spray", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"], "base_str":4, "base_dex":3, "base_con":6, "base_int":6, "base_hp":120, "base_ap":6, "str_per_level":1, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 # Level10 (add one superrare here)
 {"id": "mind_nibbler2", "name": "Mind Nibbler", "hostile_type": "eldritch", "role": "damage", "min_spawn_level":10, "rarity": "superrare", "base_xp":420, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,220), "basic_attack": "psychic tickle", "strong_attack": "brain buffet", "player_abilities": ["dark_magic_lv5_abyssal_shadow"], "base_str":2, "base_dex":3, "base_con":3, "base_int":14, "base_hp":80, "base_ap":12, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":4},
]
