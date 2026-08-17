# Level1-10 hostile seeds for Ironveil Foundry (large city)
# Split out from constants_enemies_large_city for maintainability
# Ordered by min_spawn_level asc and balanced rarities (minima enforced)

RANDOM_HOSTILE_SEEDS = [
 # level1
 {"id": "pickpocket", "name": "Pickpocket", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":10,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "quick hit", "strong_attack": "stab", "player_abilities": None,
 "base_str":1, "base_dex":5, "base_con":1, "base_int":2, "base_hp":10, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "coal_rat", "name": "Coal Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "nips at your boots", "strong_attack": "rabid bite", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":8, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "bandit", "name": "Bandit", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":1, "rarity": "uncommon", "base_xp":30,
 "common_drop": "stimulant_small", "rare_drop": "cloth_pants", "money_range": (3,12),
 "basic_attack": "slash", "strong_attack": "precise stab", "player_abilities": ["level_1_hostile_ability_smoke_screen"],
 "base_str":3, "base_dex":3, "base_con":2, "base_int":1, "base_hp":12, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "cultist", "name": "Cultist", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":1, "rarity": "rare", "base_xp":80,
 "common_drop": "herb_major", "rare_drop": "short_sword", "money_range": (30,80),
 "basic_attack": "casts a smoking bolt", "strong_attack": "drains with bone spear", "player_abilities": ["level_1_hostile_ability_arcane_blast", "level_1_hostile_ability_bone_spear"],
 "base_str":1, "base_dex":2, "base_con":2, "base_int":4, "base_hp":10, "base_ap":6,
 "str_per_level":0, "dex_per_level":1, "con_per_level":1, "int_per_level":2},

 {"id": "vagrant", "name": "Vagrant", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "clumsy shove", "strong_attack": "desperate lunge", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":1, "base_int":1, "base_hp":6, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 {"id": "drunk_barfly", "name": "The Drunken Barfly", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":6,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "drunken hook", "strong_attack": "broken bottle", "player_abilities": None,
 "base_str":1, "base_dex":1, "base_con":2, "base_int":1, "base_hp":6, "base_ap":1,
 "str_per_level":1, "dex_per_level":0, "con_per_level":0, "int_per_level":0},

 # level2
 {"id": "pickpocket_gangling", "name": "Gangling Pickpocket", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "clumsy swipe", "strong_attack": "pincer grab", "player_abilities": None,
 "base_str":1, "base_dex":4, "base_con":1, "base_int":2, "base_hp":10, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "forge_swash", "name": "Forge Swashbuckler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "slaps with a greasy wrench", "strong_attack": "overhand spanner", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":1, "base_hp":12, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "jackal", "name": "Pack Jackal", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "bites in a pack", "strong_attack": "venomous maul", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":1, "base_hp":10, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 # level3
 {"id": "tindermaid", "name": "Tindermaid", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "flinging ember", "strong_attack": "scalding jab", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":2, "base_hp":14, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 {"id": "rumor_hawker", "name": "Rumor Hawker", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":3, "rarity": "common", "base_xp":16,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,10),
 "basic_attack": "clamorous whisper", "strong_attack": "panic incite", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":1, "base_int":5, "base_hp":12, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "street_brawler", "name": "Street Brawler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":28,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,12),
 "basic_attack": "throws a haymaker", "strong_attack": "spinning strike", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":3, "base_int":1, "base_hp":20, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 # level4
 {"id": "brass_merchant", "name": "Brass Merchant", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "common", "base_xp":22,
 "common_drop": "herb_minor", "rare_drop": "cloth_pants", "money_range": (3,18),
 "basic_attack": "throws a pamphlet", "strong_attack": "coin barrage", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":4, "base_hp":18, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 {"id": "weldling", "name": "Weldling", "hostile_type": "humanoid", "role": "support", "min_spawn_level":4, "rarity": "uncommon", "base_xp":36,
 "common_drop": "stimulant_small", "rare_drop": "cloth_gloves", "money_range": (5,22),
 "basic_attack": "sparks a strike", "strong_attack": "molten swing", "player_abilities": ["level_1_hostile_ability_fire_faith_ember_shield"],
 "base_str":4, "base_dex":3, "base_con":4, "base_int":2, "base_hp":26, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 # level5
 {"id": "clocksmith_archie", "name": "Clocksmith Archie", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":46,
 "common_drop": "stimulant_small", "rare_drop": "tome_dex", "money_range": (6,30),
 "basic_attack": "tosses a tiny cog", "strong_attack": "tempered snare", "player_abilities": ["level_1_hostile_ability_air_magic_gale_surge"],
 "base_str":2, "base_dex":5, "base_con":3, "base_int":6, "base_hp":30, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":2},

 {"id": "tinker_apprentice", "name": "Tinker Apprentice", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":5, "rarity": "uncommon", "base_xp":50,
 "common_drop": "stimulant_small", "rare_drop": "tome_int", "money_range": (10,40),
 "basic_attack": "sprays shrapnel", "strong_attack": "overclock stab", "player_abilities": ["level_1_hostile_ability_electric_tech_hack_overload"],
 "base_str":2, "base_dex":5, "base_con":3, "base_int":7, "base_hp":32, "base_ap":5,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":2},

 {"id": "rivet_roper", "name": "Rivet Roper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "rare", "base_xp":52,
 "common_drop": "herb_med", "rare_drop": "tome_dex", "money_range": (8,30),
 "basic_attack": "lashes with rope", "strong_attack": "choking coil", "player_abilities": None,
 "base_str":3, "base_dex":4, "base_con":3, "base_int":2, "base_hp":28, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":0},

 # level7
 {"id": "anvil_comedian", "name": "Anvil Comedian", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":44,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (4,24),
 "basic_attack": "drops a pun-heavy anvil", "strong_attack": "comedic smash", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":4, "base_int":3, "base_hp":36, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":1},

 {"id": "cinder_widow", "name": "Cinder Widow", "hostile_type": "creature", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":90,
 "common_drop": "herb_med", "rare_drop": "ointment", "money_range": (4,36),
 "basic_attack": "webbing snap", "strong_attack": "ember bite", "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
 "base_str":2, "base_dex":8, "base_con":3, "base_int":3, "base_hp":42, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # level8
 {"id": "foundry_watch", "name": "Foundry Watch", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "rare", "base_xp":120,
 "common_drop": "stimulant_med", "rare_drop": "kevlar_vest", "money_range": (20,90),
 "basic_attack": "bashes with an iron rod", "strong_attack": "stunning baton smash", "player_abilities": None,
 "base_str":6, "base_dex":3, "base_con":6, "base_int":2, "base_hp":44, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 # level9
 {"id": "diamond_stalker", "name": "Diamond Stalker", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":9, "rarity": "uncommon", "base_xp":180,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (6,48),
 "basic_attack": "hard slap", "strong_attack": "diamond strike", "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
 "base_str":5, "base_dex":10, "base_con":4, "base_int":3, "base_hp":80, "base_ap":7,
 "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 {"id": "umbral_forgehound", "name": "Umbral Forgehound", "hostile_type": "shadow", "role": "hazard", "min_spawn_level":9, "rarity": "uncommon", "base_xp":160,
 "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (6,48),
 "basic_attack": "dark slash", "strong_attack": "vanishing strike", "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
 "base_str":5, "base_dex":9, "base_con":4, "base_int":4, "base_hp":80, "base_ap":7,
 "str_per_level":2, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # level10
 {"id": "wailing_bell_foundry", "name": "Wailing Bell", "hostile_type": "spirit", "role": "hazard", "min_spawn_level":10, "rarity": "rare", "base_xp":160,
 "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (6,44),
 "basic_attack": "piercing clang", "strong_attack": "banshee-forge shriek", "player_abilities": ["dark_magic_lv4_nightmare_echo"],
 "base_str":1, "base_dex":4, "base_con":2, "base_int":8, "base_hp":40, "base_ap":8,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":3},

 {"id": "foundry_champion", "name": "Foundry Champion", "hostile_type": "construct", "role": "support", "min_spawn_level":10, "rarity": "superrare", "base_xp":520,
 "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (100,420),
 "basic_attack": "forged hammer", "strong_attack": "colossal slam", "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
 "base_str":12, "base_dex":3, "base_con":14, "base_int":2, "base_hp":280, "base_ap":8,
 "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},
]
