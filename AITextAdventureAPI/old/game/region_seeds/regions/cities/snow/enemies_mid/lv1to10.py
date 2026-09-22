# Level1-10 hostile seeds for Hailward Hold (mid-city)
# Export a list named SEEDS_LV1TO10 used by constants_enemies_mid_city.py
SEEDS_LV1TO10 = [
 {"id": "furrow_scraper", "name": "Furrow Scraper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "shabby slap", "strong_attack": "barnacle shove", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":2, "base_int":1, "base_hp":12, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "smoked_peddler", "name": "Smoked Peddler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":10,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "pamphlet flick", "strong_attack": "stale coin toss", "player_abilities": None,
 "base_str":1, "base_dex":2, "base_con":2, "base_int":3, "base_hp":14, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "hanger_gull", "name": "Hanger Gull", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "peck", "strong_attack": "wing jab", "player_abilities": None,
 "base_str":1, "base_dex":4, "base_con":1, "base_int":1, "base_hp":8, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 # Ensure level1 includes an uncommon and a rare seed
 {"id": "hold_initiate", "name": "Hold Initiate", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":18,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "rookie jab", "strong_attack": "training shove", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":2, "base_hp":18, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "rime_echo", "name": "Rime Echo", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":1, "rarity": "rare", "base_xp":45,
 "common_drop": "herb_minor", "rare_drop": "tome_int", "money_range": (4,18),
 "basic_attack": "cold murmur", "strong_attack": "echoing chill", "player_abilities": ["level_1_hostile_ability_night_whisper"],
 "base_str":1, "base_dex":4, "base_con":2, "base_int":6, "base_hp":20, "base_ap":5,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 # Level2
 {"id": "longhouse_brawler", "name": "Longhouse Brawler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":22,
 "common_drop": "herb_minor", "rare_drop": "cloth_gloves", "money_range": (2,14),
 "basic_attack": "stout jab", "strong_attack": "bench slam", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":4, "base_int":1, "base_hp":26, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "fur_lurker", "name": "Fur Lurker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,10),
 "basic_attack": "quick snatch", "strong_attack": "mitted stab", "player_abilities": None,
 "base_str":1, "base_dex":6, "base_con":1, "base_int":2, "base_hp":12, "base_ap":3,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "fjord_gardener", "name": "Fjord Gardener", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,10),
 "basic_attack": "shovel thwack", "strong_attack": "frost rake", "player_abilities": None,
 "base_str":3, "base_dex":2, "base_con":3, "base_int":1, "base_hp":16, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "barrow_thug", "name": "Barrow Thug", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":16,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "clubbed fist", "strong_attack": "grit slam", "player_abilities": None,
 "base_str":3, "base_dex":2, "base_con":3, "base_int":1, "base_hp":18, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "salted_haggle", "name": "Salted Haggle", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "sharp retort", "strong_attack": "purse swipe", "player_abilities": None,
 "base_str":1, "base_dex":4, "base_con":2, "base_int":3, "base_hp":12, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 # Level3
 {"id": "tally_clerk", "name": "Tally Clerk", "hostile_type": "humanoid", "role": "support", "min_spawn_level":3, "rarity": "common", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": "tome_int", "money_range": (2,20),
 "basic_attack": "ledger slap", "strong_attack": "ink lash", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":6, "base_hp":22, "base_ap":3,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "ice_bowler", "name": "Ice Bowler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":20,
 "common_drop": "herb_minor", "rare_drop": "cloth_gloves", "money_range": (2,12),
 "basic_attack": "ball swing", "strong_attack": "lane smash", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":4, "base_int":1, "base_hp":22, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "rune_apprentice", "name": "Rune Apprentice", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "common", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": "tome_int", "money_range": (2,18),
 "basic_attack": "scribble bolt", "strong_attack": "ink eruption", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":2, "base_int":6, "base_hp":20, "base_ap":3,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 # Level4
 {"id": "skald_singer", "name": "Skald Singer", "hostile_type": "humanoid", "role": "support", "min_spawn_level":4, "rarity": "common", "base_xp":24,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (3,22),
 "basic_attack": "shrill verse", "strong_attack": "inspirational lash", "player_abilities": ["level_1_hostile_ability_inspire"],
 "base_str":2, "base_dex":4, "base_con":2, "base_int":6, "base_hp":24, "base_ap":3,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "rune_smasher", "name": "Rune Smasher", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":48,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (6,28),
 "basic_attack": "stone club", "strong_attack": "rune-crack", "player_abilities": None,
 "base_str":6, "base_dex":2, "base_con":6, "base_int":1, "base_hp":48, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # Level5
 {"id": "gear_gull", "name": "Gear Gull", "hostile_type": "construct", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":40,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (2,20),
 "basic_attack": "metal peck", "strong_attack": "screech arc", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":3, "base_int":1, "base_hp":30, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "keel_guard", "name": "Keel Guard", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":48,
 "common_drop": "stimulant_small", "rare_drop": "cloth_gloves", "money_range": (6,28),
 "basic_attack": "dock swing", "strong_attack": "bilge smash", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":5, "base_int":1, "base_hp":44, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "shard_knife", "name": "Shard Knife", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":5, "rarity": "uncommon", "base_xp":56,
 "common_drop": "stimulant_small", "rare_drop": "pipe_wrench", "money_range": (8,44),
 "basic_attack": "frost nick", "strong_attack": "shard flourish", "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
 "base_str":2, "base_dex":8, "base_con":2, "base_int":3, "base_hp":32, "base_ap":5,
 "str_per_level":1, "dex_per_level":3, "con_per_level":0, "int_per_level":1},

 {"id": "fur_loving_courier_girl", "name": "Fur Loving Courier Girl", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "common", "base_xp":20,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "package throw", "strong_attack": "sled bash", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":3, "base_int":2, "base_hp":22, "base_ap":3,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # Level6
 {"id": "rift_scavenger", "name": "Rift Scavenger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":60,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (8,36),
 "basic_attack": "scavenge swipe", "strong_attack": "crude lunge", "player_abilities": None,
 "base_str":4, "base_dex":4, "base_con":4, "base_int":2, "base_hp":56, "base_ap":3,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "keel_guard_old", "name": "Keel Guard", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":50,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (6,30),
 "basic_attack": "rusty dock swing", "strong_attack": "bilge slam", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":5, "base_int":1, "base_hp":46, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # Level8
 {"id": "rime_eel", "name": "Rime Eel", "hostile_type": "creature", "role": "damage", "min_spawn_level":8, "rarity": "uncommon", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (6,44),
 "basic_attack": "zap bite", "strong_attack": "coil snap", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":3, "base_dex":6, "base_con":4, "base_int":3, "base_hp":46, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "vault_scrivener", "name": "Vault Scrivener", "hostile_type": "humanoid", "role": "support", "min_spawn_level":8, "rarity": "rare", "base_xp":92,
 "common_drop": "stimulant_med", "rare_drop": "stimulant_small", "money_range": (10,64),
 "basic_attack": "stamp strike", "strong_attack": "ledger crush", "player_abilities": ["level_1_hostile_ability_inspire"],
 "base_str":3, "base_dex":3, "base_con":3, "base_int":8, "base_hp":60, "base_ap":5,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":2},

 # Level9
 {"id": "alley_wraith", "name": "Alley Wraith", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":9, "rarity": "uncommon", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (6,36),
 "basic_attack": "ink swipe", "strong_attack": "vanishing strike", "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
 "base_str":4, "base_dex":8, "base_con":3, "base_int":3, "base_hp":60, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 {"id": "northern_banshee", "name": "Northern Banshee", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":9, "rarity": "rare", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (10,60),
 "basic_attack": "moan of cold", "strong_attack": "soul freeze", "player_abilities": ["level_1_hostile_ability_night_whisper"],
 "base_str":1, "base_dex":4, "base_con":2, "base_int":11, "base_hp":64, "base_ap":9,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 # Level10
 {"id": "hold_watch", "name": "Hold Watch", "hostile_type": "humanoid", "role": "support", "min_spawn_level":10, "rarity": "rare", "base_xp":160,
 "common_drop": "stimulant_med", "rare_drop": "kevlar_vest", "money_range": (20,100),
 "basic_attack": "spear jab", "strong_attack": "pike sweep", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":6, "base_dex":3, "base_con":6, "base_int":3, "base_hp":72, "base_ap":5,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":1},

 {"id": "frostwork_sentinel", "name": "Frostwork Sentinel", "hostile_type": "construct", "role": "support", "min_spawn_level":10, "rarity": "uncommon", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": "kevlar_vest", "money_range": (12,64),
 "basic_attack": "jointed swipe", "strong_attack": "servo crush", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":6, "base_dex":3, "base_con":8, "base_int":2, "base_hp":140, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # Superrare to satisfy parity (placed at level10)
 {"id": "runekeeper_wardling", "name": "Runekeeper Wardling", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":10, "rarity": "superrare", "base_xp":380,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,260),
 "basic_attack": "warding lash", "strong_attack": "arcane cataclysm", "player_abilities": ["level_1_hostile_ability_light_spirit_prism_burst"],
 "base_str":6, "base_dex":4, "base_con":8, "base_int":10, "base_hp":220, "base_ap":8,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":3},
]
