# Level11-20 hostile seeds for the Great Dune City
# Split out from constants_enemies_large_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==11
 {"id": "net_hag", "name": "Net Hag", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":11, "rarity": "common", "base_xp":132,
 "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (36,160),
 "basic_attack": "taps with a sand-scarab relay", "strong_attack": "sparking jolt", "player_abilities": ["hack_overload", "emp_burst"],
 "base_str":2, "base_dex":4, "base_con":2, "base_int":8, "base_hp":36, "base_ap":6, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "desert_serpent", "name": "Desert Serpent", "hostile_type": "creature", "role": "damage", "min_spawn_level":11, "rarity": "rare", "base_xp":300,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40,180),
 "basic_attack": "maw lash", "strong_attack": "constrict", "player_abilities": ["abyssal_storm"], "base_str":10, "base_dex":7, "base_con":9, "base_int":2, "base_hp":220, "base_ap":6, "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==12
 {"id": "dune_overlord", "name": "Dune Overlord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":12, "rarity": "rare", "base_xp":150,
 "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (30,140),
 "basic_attack": "crushes with a spiked dune-scepter", "strong_attack": "berserker sandburst", "player_abilities": ["berserker_tech", "earth_sunder"],
 "base_str":8, "base_dex":4, "base_con":7, "base_int":3, "base_hp":80, "base_ap":6, "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 {"id": "matron_hire", "name": "Hired Matron", "hostile_type": "humanoid", "role": "support", "min_spawn_level":12, "rarity": "common", "base_xp":168,
 "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (35,160),
 "basic_attack": "cane lash", "strong_attack": "crushing maternal blow", "player_abilities": None, "base_str":5, "base_dex":3, "base_con":8, "base_int":4, "base_hp":88, "base_ap":6, "str_per_level":2, "dex_per_level":0, "con_per_level":3, "int_per_level":1},

 {"id": "desert_mindflayer", "name": "Desert Mindflayer", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":12, "rarity": "superrare", "base_xp":420, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,240),
 "basic_attack": "psychic tendrils", "strong_attack": "psychic pulse", "player_abilities": ["dark_magic_lv5_abyssal_shadow"], "base_str":2, "base_dex":3, "base_con":3, "base_int":14, "base_hp":80, "base_ap":12, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":4},

 {"id": "lich_apprentice", "name": "Lich Apprentice", "hostile_type": "undead", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":320, "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (30,140),
 "basic_attack": "bone bolt", "strong_attack": "necrotic spear", "player_abilities": ["bone_spear"], "base_str":2, "base_dex":3, "base_con":4, "base_int":12, "base_hp":100, "base_ap":10, "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 # min_spawn_level ==13
 {"id": "harbinger_of_frost", "name": "Harbinger of Frost", "hostile_type": "elemental", "role": "damage", "min_spawn_level":13, "rarity": "uncommon", "base_xp":340, "common_drop": "stimulant_med", "rare_drop": "tome_int", "money_range": (30,140),
 "basic_attack": "ice shard", "strong_attack": "freezing blast", "player_abilities": ["frost_nova"], "base_str":6, "base_dex":5, "base_con":8, "base_int":7, "base_hp":180, "base_ap":9, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":2},

 {"id": "wreck_khan", "name": "Wreck Khan", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":13, "rarity": "uncommon", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": "sawed_off", "money_range": (30,160),
 "basic_attack": "haymaker of the dunes", "strong_attack": "wrecking maul", "player_abilities": [],
 "base_str":7, "base_dex":2, "base_con":6, "base_int":1, "base_hp":78, "base_ap":5, "str_per_level":3, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==14
 {"id": "glass_wrecker", "name": "Glass Wrecker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":14, "rarity": "uncommon", "base_xp":170,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (40,160),
 "basic_attack": "smashes with crystalline maul", "strong_attack": "cataclysmic shard slam", "player_abilities": None,
 "base_str":9, "base_dex":2, "base_con":8, "base_int":1, "base_hp":96, "base_ap":5, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "neon_siren", "name": "Neon Siren", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":14, "rarity": "uncommon", "base_xp":200,
 "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (44,200),
 "basic_attack": "glowing blade", "strong_attack": "stunning aria", "player_abilities": ["prism_burst"], "base_str":3, "base_dex":7, "base_con":3, "base_int":8, "base_hp":64, "base_ap":8, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":3},

 {"id": "clockwork_colossus", "name": "Clockwork Colossus", "hostile_type": "construct", "role": "support", "min_spawn_level":14, "rarity": "uncommon", "base_xp":320, "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (60,220),
 "basic_attack": "piston swing", "strong_attack": "hydraulic crush", "player_abilities": ["reinforce_frame"], "base_str":14, "base_dex":1, "base_con":18, "base_int":1, "base_hp":300, "base_ap":3, "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 # min_spawn_level ==15
 {"id": "black_dune_dealer", "name": "Black Dune Dealer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":15, "rarity": "common", "base_xp":210,
 "common_drop": "stimulant_large", "rare_drop": "stimulant_large", "money_range": (60,300),
 "basic_attack": "slick palm slap", "strong_attack": "contraband barrage", "player_abilities": ["primal_unison", "nether_cataclysm"],
 "base_str":3, "base_dex":4, "base_con":3, "base_int":7, "base_hp":52, "base_ap":6, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "rogue_mistress", "name": "Rogue Mistress", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":15, "rarity": "uncommon", "base_xp":240,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (60,260),
 "basic_attack": "shadow strike", "strong_attack": "deadly riposte", "player_abilities": ["poison_dart"], "base_str":6, "base_dex":10, "base_con":5, "base_int":7, "base_hp":100, "base_ap":9, "str_per_level":2, "dex_per_level":4, "con_per_level":1, "int_per_level":3},

 {"id": "dream_eater2", "name": "Dream Eater", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":15, "rarity": "common", "base_xp":480, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (60,280),
 "basic_attack": "mind gnaw", "strong_attack": "maddening shriek", "player_abilities": ["nightmare_wave"], "base_str":3, "base_dex":6, "base_con":5, "base_int":14, "base_hp":140, "base_ap":14, "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":4},

 # min_spawn_level ==16
 {"id": "mirage_stalker", "name": "Mirage Stalker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":16, "rarity": "rare", "base_xp":240,
 "common_drop": "lockpick", "rare_drop": "tome_int", "money_range": (50,220),
 "basic_attack": "silent sand-strike", "strong_attack": "illusory nightmare", "player_abilities": ["shadow_flicker", "nightmare_wave", "void_veil"], "base_str":5, "base_dex":9, "base_con":4, "base_int":6, "base_hp":70, "base_ap":8, "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":2},

 {"id": "revenant_queen", "name": "Revenant Queen", "hostile_type": "undead", "role": "hazard", "min_spawn_level":16, "rarity": "common", "base_xp":520, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (80,320),
 "basic_attack": "regal claws", "strong_attack": "necrotic burst", "player_abilities": ["void_veil"], "base_str":9, "base_dex":8, "base_con":10, "base_int":6, "base_hp":260, "base_ap":10, "str_per_level":4, "dex_per_level":3, "con_per_level":3, "int_per_level":2},

 # min_spawn_level ==17
 {"id": "baron_guard", "name": "Baron's Guard", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":260,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (70,320),
 "basic_attack": "polished strike", "strong_attack": "noble onslaught", "player_abilities": None,
 "base_str":7, "base_dex":5, "base_con":7, "base_int":4, "base_hp":150, "base_ap":8, "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 # min_spawn_level ==18
 {"id": "servo_sentinel", "name": "Servo Sentinel", "hostile_type": "humanoid", "role": "support", "min_spawn_level":18, "rarity": "rare", "base_xp":260,
 "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (80,340),
 "basic_attack": "servo jab", "strong_attack": "piston barrage", "player_abilities": ["reinforce_frame", "chain_reactor"], "base_str":6, "base_dex":5, "base_con":6, "base_int":4, "base_hp":120, "base_ap":8, "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 {"id": "mafia_madam", "name": "Mafia Madam", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":18, "rarity": "common", "base_xp":280,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (80,340),
 "basic_attack": "stiletto jab", "strong_attack": "brutal slash", "player_abilities": ["brutal_swing"], "base_str":8, "base_dex":6, "base_con":7, "base_int":6, "base_hp":150, "base_ap":8, "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":2},

 {"id": "celestial_watcher", "name": "Celestial Watcher", "hostile_type": "celestial", "role": "damage", "min_spawn_level":18, "rarity": "common", "base_xp":600, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (100,400),
 "basic_attack": "radiant talons", "strong_attack": "celestial shards", "player_abilities": ["stellar_fall"], "base_str":10, "base_dex":8, "base_con":12, "base_int":10, "base_hp":320, "base_ap":12, "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":3},

 # min_spawn_level ==20
 {"id": "dune_lieutenant", "name": "Dune Lieutenant", "hostile_type": "humanoid", "role": "support", "min_spawn_level":20, "rarity": "common", "base_xp":420,
 "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (150,700),
 "basic_attack": "ruthless sand-strikes", "strong_attack": "lieutenant's onslaught", "player_abilities": ["inspire", "berserker_tech"],
 "base_str":9, "base_dex":6, "base_con":9, "base_int":5, "base_hp":220, "base_ap":10, "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 {"id": "hyper_vixen", "name": "Hyper Vixen", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":20, "rarity": "common", "base_xp":480,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (180,800),
 "basic_attack": "elegant stab", "strong_attack": "fatal flourish", "player_abilities": ["primal_unison"], "base_str":9, "base_dex":11, "base_con":7, "base_int":9, "base_hp":240, "base_ap":12, "str_per_level":4, "dex_per_level":4, "con_per_level":2, "int_per_level":3},
]
