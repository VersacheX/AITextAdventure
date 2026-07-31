# Level1-10 hostile seeds for BioHazard (small city)
# Split out from constants_enemies_small_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==1
 {"id": "scrap_rodent", "name": "Scrap Rodent", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "nips with rusty teeth", "strong_attack": "rabid gnaw", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":6, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0, "resistances": [], "immunities": [], "weaknesses": []},

 {"id": "scav_runner", "name": "Scav Runner", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": "lockpick", "money_range": (1,6),
 "basic_attack": "shove and snatch", "strong_attack": "garrote of wire", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":1, "base_int":2, "base_hp":10, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0, "resistances": [], "immunities": [], "weaknesses": []},

 {"id": "dirty_chav", "name": "Dirty Chav", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":1, "rarity": "rare", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": "dagger", "money_range": (3,18),
 "basic_attack": "punk shot", "strong_attack": "bitch slap", "player_abilities": ['air_skill_lv1_smoke_bomb'],
 "base_str":2, "base_dex":7, "base_con":2, "base_int":2, "base_hp":20, "base_ap":12,
 "str_per_level":1, "dex_per_level":3, "con_per_level":0, "int_per_level":1, "resistances": [], "immunities": ['sleep'], "weaknesses": ['ice']},

 # min_spawn_level ==2
 {"id": "jerky_barker", "name": "Jerky Barker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "rare", "base_xp":18,
 "common_drop": "jerkyshot", "rare_drop": None, "money_range": (0,8),
 "basic_attack": "yell and slap", "strong_attack": "spit-toss", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":1, "base_hp":20, "base_ap":2,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0, "resistances": [], "immunities": [], "weaknesses": []},

 {"id": "canteen_keeper", "name": "Canteen Keeper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":14,
 "common_drop": "water", "rare_drop": "herb_minor", "money_range": (0,10),
 "basic_attack": "spill hot brew", "strong_attack": "barstool bash", "player_abilities": None,
 "base_str":2, "base_dex":2, "base_con":3, "base_int":2, "base_hp":14, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0, "resistances": [], "immunities": [], "weaknesses": []},

 # min_spawn_level ==3
 {"id": "barrel_marauder", "name": "Barrel Marauder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,10),
 "basic_attack": "barrel toss", "strong_attack": "flame splatter", "player_abilities": None,
 "base_str":3, "base_dex":3, "base_con":3, "base_int":1, "base_hp":20, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0, "resistances": [], "immunities": [], "weaknesses": []},

 {"id": "junk_jester", "name": "Junk Jester", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "common", "base_xp":26,
 "common_drop": "herb_minor", "rare_drop": "dagger", "money_range": (2,18),
 "basic_attack": "mocking twirl", "strong_attack": "confetti trap", "player_abilities": ["air_skill_lv1_smoke_bomb"],
 "base_str":2, "base_dex":6, "base_con":2, "base_int":3, "base_hp":16, "base_ap":3,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":1, "resistances": [], "immunities": [], "weaknesses": []},

 # min_spawn_level ==4
 {"id": "gearhound", "name": "Gearhound", "hostile_type": "creature", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":70,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (6,28),
 "basic_attack": "bite with rusty gears", "strong_attack": "spinning maul", "player_abilities": None,
 "base_str":5, "base_dex":5, "base_con":4, "base_int":1, "base_hp":40, "base_ap":4,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0, "resistances": [], "immunities": [], "weaknesses": []},

 {"id": "radio_fix", "name": "Radio Fixer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":4, "rarity": "uncommon", "base_xp":44,
 "common_drop": "lockpick", "rare_drop": "stimulant_small", "money_range": (6,32),
 "basic_attack": "wrench jab", "strong_attack": "electro-spark", "player_abilities": ["fire_water_tech_lv2_steam_grenade", "fire_air_tech_lv2_aero_flare"],
 "base_str":2, "base_dex":4, "base_con":3, "base_int":6, "base_hp":24, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2, "resistances": [], "immunities": [], "weaknesses": []},

 # min_spawn_level ==5
 {"id": "trader_ricochet", "name": "Trader Ricochet", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "rare", "base_xp":90,
 "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (20,80),
 "basic_attack": "snap-shot", "strong_attack": "ricochet blast", "player_abilities": ["ice_skill_lv1_ice_shuriken"],
 "base_str":3, "base_dex":7, "base_con":3, "base_int":4, "base_hp":36, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1, "resistances": [], "immunities": [], "weaknesses": []},

 {"id": "night_raven", "name": "Night Raven", "hostile_type": "creature", "role": "hazard", "min_spawn_level":5, "rarity": "uncommon", "base_xp":40,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (6,30),
 "basic_attack": "peck and claw", "strong_attack": "venomous plunge", "player_abilities": ["earth_dark_skill_lv5_venom_trace"],
 "base_str":2, "base_dex":7, "base_con":3, "base_int":2, "base_hp":36, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":0, "resistances": [], "immunities": [], "weaknesses": []},

 # min_spawn_level ==6
 {"id": "muttering_matron", "name": "Muttering Matron", "hostile_type": "humanoid", "role": "support", "min_spawn_level":6, "rarity": "uncommon", "base_xp":58,
 "common_drop": "herb_med", "rare_drop": "tome_con", "money_range": (8,36),
 "basic_attack": "wagging finger", "strong_attack": "boiling rebuke", "player_abilities": ["water_faith_lv1_mending_streams"],
 "base_str":2, "base_dex":2, "base_con":5, "base_int":4, "base_hp":36, "base_ap":5,
 "str_per_level":1, "dex_per_level":0, "con_per_level":2, "int_per_level":1, "resistances": [], "immunities": [], "weaknesses": []},

 {"id": "scrap_siren", "name": "Scrap Siren", "hostile_type": "humanoid", "role": "support", "min_spawn_level":6, "rarity": "rare", "base_xp":120,
 "common_drop": "stimulant_med", "rare_drop": "tome_int", "money_range": (25,100),
 "basic_attack": "siren wail", "strong_attack": "distracting chorus", "player_abilities": ["light_faith_lv4_hearthsong", "light_fire_faith_lv3_dawn_heal"],
 "base_str":2, "base_dex":5, "base_con":3, "base_int":7, "base_hp":40, "base_ap":6,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":2, "resistances": [], "immunities": [], "weaknesses": []},

 # min_spawn_level ==7
 {"id": "junk_rigger", "name": "Junk Rigger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "common", "base_xp":110,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (18,88),
 "basic_attack": "shoddy lash", "strong_attack": "hook and swing", "player_abilities": None,
 "base_str":4, "base_dex":4, "base_con":4, "base_int":2, "base_hp":120, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "rust_clubber", "name": "Rust Clubber", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":30,
 "common_drop": "herb_med", "rare_drop": "pipe_wrench", "money_range": (4,24),
 "basic_attack": "club swing", "strong_attack": "overhead smash", "player_abilities": ["fire_technique_lv4_berserker_tech"],
 "base_str":6, "base_dex":2, "base_con":4, "base_int":1, "base_hp":28, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0, "resistances": ["fire"], "immunities": [], "weaknesses": []},

 # min_spawn_level ==8
 {"id": "vault_microthief", "name": "Vault Microthief", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":8, "rarity": "rare", "base_xp":160,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (40,160),
 "basic_attack": "silent pry", "strong_attack": "back-alley vanish", "player_abilities": ["dark_magic_lv1_shadow_tendril"],
 "base_str":3, "base_dex":9, "base_con":2, "base_int":6, "base_hp":48, "base_ap":8,
 "str_per_level":1, "dex_per_level":3, "con_per_level":0, "int_per_level":2, "resistances": [], "immunities": [], "weaknesses": []},

 {"id": "scrap_watcher", "name": "Scrap Watcher", "hostile_type": "creature", "role": "damage", "min_spawn_level":8, "rarity": "common", "base_xp":100,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (16,72),
 "basic_attack": "metal snap", "strong_attack": "gear pummel", "player_abilities": None,
 "base_str":5, "base_dex":6, "base_con":5, "base_int":1, "base_hp":120, "base_ap":5,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==9
 {"id": "mad_mechanic", "name": "Mad Mechanic", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":9, "rarity": "uncommon", "base_xp":180,
 "common_drop": "stimulant_large", "rare_drop": "energy_pistol", "money_range": (45,180),
 "basic_attack": "wrench flurry", "strong_attack": "overclocked blast", "player_abilities": ["fire_water_tech_lv2_steam_grenade", "air_fire_magic_lv4_chain_lightning"],
 "base_str":4, "base_dex":6, "base_con":4, "base_int":10, "base_hp":80, "base_ap":8,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":3, "resistances": [], "immunities": [], "weaknesses": []},

 {"id": "tinker_pup", "name": "Tinker Pup", "hostile_type": "creature", "role": "damage", "min_spawn_level":9, "rarity": "common", "base_xp":120,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (20,80),
 "basic_attack": "nips and whirrs", "strong_attack": "overclocked bite", "player_abilities": None,
 "base_str":4, "base_dex":6, "base_con":4, "base_int":2, "base_hp":140, "base_ap":6,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 # min_spawn_level ==10
 {"id": "peddler_phantom", "name": "Peddler Phantom", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":10, "rarity": "rare", "base_xp":200,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40,160),
 "basic_attack": "haunting pitch", "strong_attack": "phantom grasp", "player_abilities": ["dark_magic_lv2_night_whisper", "dark_magic_lv5_abyssal_shadow"],
 "base_str":1, "base_dex":4, "base_con":4, "base_int":12, "base_hp":80, "base_ap":10,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3, "resistances": [], "immunities": [], "weaknesses": []},

 {"id": "revenant_bard", "name": "Revenant Bard", "hostile_type": "spirit", "role": "support", "min_spawn_level":10, "rarity": "superrare", "base_xp":420,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,320),
 "basic_attack": "lamenting chord", "strong_attack": "shrieking reprise", "player_abilities": ["night_whisper", "streamlet"],
 "base_str":2, "base_dex":6, "base_con":4, "base_int":14, "base_hp":160, "base_ap":12,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":4},
]
