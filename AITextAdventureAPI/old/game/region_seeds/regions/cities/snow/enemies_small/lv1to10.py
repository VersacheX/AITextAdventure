# Level1-10 hostile seeds for Bleakwatch Outpost (small-city)
# Export a list named SEEDS_LV1TO10 used by constants_enemies_small_city.py
SEEDS_LV1TO10 = [
 {"id": "frost_scrapper", "name": "Frost Scrapper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "grimy slap", "strong_attack": "snowbank shove", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":2, "base_int":1, "base_hp":12, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "rusty_peddler", "name": "Rusty Peddler", "hostile_type": "humanoid", "role": "support", "min_spawn_level":1, "rarity": "common", "base_xp":10,
 "common_drop": "stimulant_small", "rare_drop": "tome_dex", "money_range": (1,10),
 "basic_attack": "pamphlet flick", "strong_attack": "jar heave", "player_abilities": ["level_1_hostile_ability_inspire"],
 "base_str":1, "base_dex":2, "base_con":2, "base_int":4, "base_hp":14, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "outpost_gull", "name": "Outpost Gull", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,3),
 "basic_attack": "peck at pockets", "strong_attack": "wing slap", "player_abilities": None,
 "base_str":1, "base_dex":4, "base_con":1, "base_int":1, "base_hp":8, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "salt_seller", "name": "Salt Seller", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":8,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "salty toss", "strong_attack": "sack smash", "player_abilities": None,
 "base_str":1, "base_dex":2, "base_con":2, "base_int":2, "base_hp":12, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 {"id": "slippery_tourist", "name": "Slippery Tourist", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "panicked flail", "strong_attack": "faceplant followed by groan", "player_abilities": None,
 "base_str":1, "base_dex":2, "base_con":1, "base_int":2, "base_hp":10, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 # Level1 additional rarity entries: uncommon and rare must exist at level1
 {"id": "outpost_skulker", "name": "Outpost Skulker", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":1, "rarity": "uncommon", "base_xp":20,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "slick snatch", "strong_attack": "shadow trip", "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
 "base_str":2, "base_dex":7, "base_con":2, "base_int":3, "base_hp":24, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 {"id": "rime_wisp", "name": "Rime Wisp", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":1, "rarity": "rare", "base_xp":80,
 "common_drop": "herb_minor", "rare_drop": "tome_int", "money_range": (6,36),
 "basic_attack": "whisper cold", "strong_attack": "spectral chill", "player_abilities": ["level_1_hostile_ability_night_whisper"],
 "base_str":1, "base_dex":5, "base_con":2, "base_int":8, "base_hp":44, "base_ap":6,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":2},

 # Level2
 {"id": "hutsman", "name": "Hutsman", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": "cloth_gloves", "money_range": (2,14),
 "basic_attack": "stump swing", "strong_attack": "bench toss", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":4, "base_int":1, "base_hp":26, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "locker_cutpurse", "name": "Locker Cutpurse", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "quick snatch", "strong_attack": "mitted stab", "player_abilities": None,
 "base_str":1, "base_dex":6, "base_con":1, "base_int":2, "base_hp":12, "base_ap":3,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "pack_hound", "name": "Pack Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "snap bite", "strong_attack": "pack maul", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":1, "base_hp":16, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "ice_gecko", "name": "Ice Gecko", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,10),
 "basic_attack": "fang nip", "strong_attack": "cold cling", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":2, "base_int":1, "base_hp":18, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "furrow_old", "name": "Furrow Old" , "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "gnarled shove", "strong_attack": "weathered swing", "player_abilities": None,
 "base_str":2, "base_dex":2, "base_con":2, "base_int":2, "base_hp":18, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "kelp_vendor", "name": "Kelp Vendor", "hostile_type": "humanoid", "role": "support", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "bundle whack", "strong_attack": "stinky toss", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":2, "base_hp":14, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 # Level3
 {"id": "ledger_lout", "name": "Ledger Lout", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":16,
 "common_drop": "herb_minor", "rare_drop": "tome_int", "money_range": (2,18),
 "basic_attack": "ledger slap", "strong_attack": "ink smear", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":6, "base_hp":20, "base_ap":3,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "rusty_peddler_sly", "name": "Rusty Peddler", "hostile_type": "humanoid", "role": "support", "min_spawn_level":3, "rarity": "common", "base_xp":18,
 "common_drop": "stimulant_small", "rare_drop": "tome_dex", "money_range": (2,18),
 "basic_attack": "slick sell", "strong_attack": "jar throw", "player_abilities": ["level_1_hostile_ability_inspire"],
 "base_str":1, "base_dex":4, "base_con":2, "base_int":5, "base_hp":24, "base_ap":3,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "snow_mime", "name": "Snow Mime)", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "common", "base_xp":14,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,8),
 "basic_attack": "invisible jab", "strong_attack": "imaginary choke", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":2, "base_int":4, "base_hp":16, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "frost_miner", "name": "Frost Miner", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":22,
 "common_drop": "herb_minor", "rare_drop": "machete", "money_range": (2,18),
 "basic_attack": "pick jab", "strong_attack": "vein smash", "player_abilities": None,
 "base_str":5, "base_dex":2, "base_con":4, "base_int":1, "base_hp":28, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "fishing_bonker", "name": "Fishing Bonker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": "magical_stick", "money_range": (2,12),
 "basic_attack": "net swing", "strong_attack": "bonk and tumble", "player_abilities": None,
 "base_str":3, "base_dex":3, "base_con":3, "base_int":1, "base_hp":20, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 # Level4
 {"id": "skipped_placeholder", "name": "Skipped Placeholder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,12),
 "basic_attack": "placeholder jab", "strong_attack": "placeholder slam", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":2, "base_int":4, "base_hp":22, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "shanty_chorus", "name": "Shanty Chorus", "hostile_type": "humanoid", "role": "support", "min_spawn_level":4, "rarity": "common", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,12),
 "basic_attack": "harmonic whoop", "strong_attack": "choral slam", "player_abilities": ["level_1_hostile_ability_inspire"],
 "base_str":1, "base_dex":3, "base_con":2, "base_int":6, "base_hp":22, "base_ap":3,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "sled_pounder", "name": "Sled Pounder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":44,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (6,30),
 "basic_attack": "sled bash", "strong_attack": "crushing roll", "player_abilities": None,
 "base_str":6, "base_dex":2, "base_con":6, "base_int":1, "base_hp":50, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "frozen_clown", "name": "Frozen Clown", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":4, "rarity": "uncommon", "base_xp":24,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (2,16),
 "basic_attack": "slapstick swipe", "strong_attack": "custard of ice", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":3, "base_int":5, "base_hp":26, "base_ap":3,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 {"id": "beacon_tender", "name": "Beacon Tender", "hostile_type": "humanoid", "role": "support", "min_spawn_level":4, "rarity": "uncommon", "base_xp":48,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (6,32),
 "basic_attack": "lamp swing", "strong_attack": "blinding sweep", "player_abilities": ["level_1_hostile_ability_light_faith_prism_burst"],
 "base_str":4, "base_dex":3, "base_con":5, "base_int":4, "base_hp":44, "base_ap":4,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":1},

 # Level5
 {"id": "watch_recruit", "name": "Watch Recruit", "hostile_type": "humanoid", "role": "support", "min_spawn_level":5, "rarity": "uncommon", "base_xp":60,
 "common_drop": "stimulant_small", "rare_drop": "cloth_gloves", "money_range": (8,30),
 "basic_attack": "spear jab", "strong_attack": "pike sweep", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":5, "base_dex":3, "base_con":5, "base_int":2, "base_hp":40, "base_ap":4,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # Level6
 {"id": "cache_smuggler", "name": "Cache Smuggler", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":6, "rarity": "uncommon", "base_xp":42,
 "common_drop": "stimulant_small", "rare_drop": "stimulant_large", "money_range": (10,60),
 "basic_attack": "slick jab", "strong_attack": "sealed parcel", "player_abilities": None,
 "base_str":3, "base_dex":5, "base_con":3, "base_int":3, "base_hp":30, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "drifting_hermit", "name": "Drifting Hermit", "hostile_type": "humanoid", "role": "support", "min_spawn_level":6, "rarity": "uncommon", "base_xp":56,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (4,30),
 "basic_attack": "cane jab", "strong_attack": "solitary howl", "player_abilities": None,
 "base_str":2, "base_dex":2, "base_con":4, "base_int":6, "base_hp":46, "base_ap":4,
 "str_per_level":0, "dex_per_level":0, "con_per_level":1, "int_per_level":1},

 {"id": "altar_believer", "name": "Altar Believer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":6, "rarity": "rare", "base_xp":120,
 "common_drop": "herb_major", "rare_drop": "short_sword", "money_range": (10,80),
 "basic_attack": "prayer lash", "strong_attack": "bone spear", "player_abilities": ["level_1_hostile_ability_arcane_blast"],
 "base_str":1, "base_dex":2, "base_con":3, "base_int":8, "base_hp":48, "base_ap":7,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 # Level7
 {"id": "drift_wolf_alpha", "name": "Drift Wolf", "hostile_type": "creature", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":88,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,44),
 "basic_attack": "maul", "strong_attack": "rending howl", "player_abilities": None,
 "base_str":7, "base_dex":6, "base_con":5, "base_int":2, "base_hp":90, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # Level8
 {"id": "watch_repair", "name": "Watch Repair", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":8, "rarity": "rare", "base_xp":120,
 "common_drop": "stimulant_small", "rare_drop": "tome_dex", "money_range": (18,90),
 "basic_attack": "wrench jab", "strong_attack": "coil burst", "player_abilities": ["level_1_hostile_ability_electric_tech_hack_overload", "level_1_hostile_ability_electric_tech_hack_overload"],
 "base_str":2, "base_dex":4, "base_con":4, "base_int":8, "base_hp":48, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "barnacle_shaman", "name": "Barnacle Shaman", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":9, "rarity": "rare", "base_xp":140,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (12,80),
 "basic_attack": "briny curse", "strong_attack": "barnacle burst", "player_abilities": ["level_1_hostile_ability_arcane_blast", "level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":2, "base_dex":3, "base_con":4, "base_int":10, "base_hp":80, "base_ap":8,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "ice_harpooner", "name": "Ice Harpooner", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":9, "rarity": "rare", "base_xp":150,
 "common_drop": "stimulant_med", "rare_drop": "revolver", "money_range": (28,120),
 "basic_attack": "harpoon jab", "strong_attack": "impaling throw", "player_abilities": None,
 "base_str":6, "base_dex":5, "base_con":6, "base_int":3, "base_hp":96, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "tundra_gnasher", "name": "Tundra Gnasher", "hostile_type": "creature", "role": "damage", "min_spawn_level":9, "rarity": "uncommon", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (8,60),
 "basic_attack": "jaw snap", "strong_attack": "bone crunch", "player_abilities": None,
 "base_str":6, "base_dex":4, "base_con":5, "base_int":2, "base_hp":110, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # Level10
 {"id": "watch_sergeant", "name": "Watch Sergeant", "hostile_type": "humanoid", "role": "support", "min_spawn_level":10, "rarity": "rare", "base_xp":160,
 "common_drop": "stimulant_med", "rare_drop": "kevlar_vest", "money_range": (22,110),
 "basic_attack": "veteran strike", "strong_attack": "crushing pike", "player_abilities": None,
 "base_str":8, "base_dex":3, "base_con":8, "base_int":3, "base_hp":120, "base_ap":5,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "fog_whisper", "name": "Fog Whisper", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":10, "rarity": "rare", "base_xp":180,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (20,100),
 "basic_attack": "murmured breeze", "strong_attack": "suffocating sigh", "player_abilities": ["level_1_hostile_ability_night_whisper"],
 "base_str":1, "base_dex":4, "base_con":2, "base_int":10, "base_hp":88, "base_ap":9,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 {"id": "bleak_lantern", "name": "Bleak Lantern", "hostile_type": "humanoid", "role": "support", "min_spawn_level":10, "rarity": "superrare", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,340),
 "basic_attack": "lantern swing", "strong_attack": "blinding flare", "player_abilities": ["level_1_hostile_ability_light_faith_prism_burst", "lv2_hostile_ability_dark_dark_faith_void_veil"],
 "base_str":8, "base_dex":5, "base_con":10, "base_int":9, "base_hp":240, "base_ap":10,
 "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":2},
]
