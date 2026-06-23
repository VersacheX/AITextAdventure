# Level1-10 hostile seeds for the Great Dune City
# Split out from constants_enemies_large_city for maintainability

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level ==1
 {"id": "sand_rat", "name": "Sand Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "common", "base_xp":7,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,4),
 "basic_attack": "nips at toes", "strong_attack": "rabid chew", "player_abilities": None,
 "base_str":1, "base_dex":2, "base_con":1, "base_int":1, "base_hp":6, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "barfly", "name": "Barfly of the Mirage", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":1, "rarity": "uncommon", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "drunken hook", "strong_attack": "broken bottle", "player_abilities": [],
 "base_str":2, "base_dex":2, "base_con":3, "base_int":1, "base_hp":10, "base_ap":2,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "alley_cat", "name": "Alley Cat", "hostile_type": "creature", "role": "damage", "min_spawn_level":1, "rarity": "rare", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "claw maul", "strong_attack": "ferocious pounce", "player_abilities": None,
 "base_str":3, "base_dex":6, "base_con":2, "base_int":1, "base_hp":18, "base_ap":3,
 "str_per_level":1, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 # min_spawn_level ==2
 {"id": "spoon_beggar", "name": "Beggar with a Spoon (and a curse)", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":10,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,6),
 "basic_attack": "pokes with a rusty spoon", "strong_attack": "soup-stab", "player_abilities": [],
 "base_str":2, "base_dex":3, "base_con":1, "base_int":1, "base_hp":9, "base_ap":2,
 "str_per_level":1, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 {"id": "courier_girl", "name": "Courier Girl", "hostile_type": "humanoid", "role": "support", "min_spawn_level":2, "rarity": "common", "base_xp":12,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,6),
 "basic_attack": "parcel jab", "strong_attack": "vicious elbow flurry", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":2, "base_hp":12, "base_ap":2,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":0},

 {"id": "undercity_flea", "name": "Undercity Flea", "hostile_type": "creature", "role": "damage", "min_spawn_level":2, "rarity": "common", "base_xp":9,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (0,5),
 "basic_attack": "fierce bite", "strong_attack": "savage bite", "player_abilities": [],
 "base_str":1, "base_dex":3, "base_con":1, "base_int":1, "base_hp":7, "base_ap":1,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":0},

 # min_spawn_level ==3
 {"id": "dune_brawler", "name": "Dune Brawler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "uncommon", "base_xp":30,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,14),
 "basic_attack": "throws a grainy haymaker", "strong_attack": "dune slam", "player_abilities": None,
 "base_str":5, "base_dex":3, "base_con":4, "base_int":1, "base_hp":22, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":1, "int_per_level":0},

 {"id": "rumor_monger", "name": "Rumor Monger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":3, "rarity": "common", "base_xp":16,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (1,8),
 "basic_attack": "spiteful whisper", "strong_attack": "panic lash", "player_abilities": None,
 "base_str":1, "base_dex":3, "base_con":1, "base_int":4, "base_hp":12, "base_ap":2,
 "str_per_level":0, "dex_per_level":1, "con_per_level":0, "int_per_level":1},

 # min_spawn_level ==4
 {"id": "tunnel_viper", "name": "Tunnel Viper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "uncommon", "base_xp":34,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (3,18),
 "basic_attack": "stabs with a hollow reed", "strong_attack": "backstab from the dune", "player_abilities": None,
 "base_str":2, "base_dex":3, "base_con":2, "base_int":4, "base_hp":22, "base_ap":3,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 {"id": "neon_merchant", "name": "Neon Merchant", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":4, "rarity": "rare", "base_xp":18,
 "common_drop": "herb_minor", "rare_drop": None, "money_range": (2,10),
 "basic_attack": "glinting shove", "strong_attack": "spinning market kick", "player_abilities": None,
 "base_str":2, "base_dex":5, "base_con":2, "base_int":2, "base_hp":14, "base_ap":3,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # min_spawn_level ==5
 {"id": "vault_watcher", "name": "Vault Watcher", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "uncommon", "base_xp":48,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (10,44),
 "basic_attack": "bashes with a ledger-slate", "strong_attack": "stunning baton swing", "player_abilities": [],
 "base_str":4, "base_dex":2, "base_con":3, "base_int":3, "base_hp":28, "base_ap":3,
 "str_per_level":1, "dex_per_level":0, "con_per_level":1, "int_per_level":1},

 {"id": "sly_madam", "name": "Sly Madam", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":5, "rarity": "common", "base_xp":44,
 "common_drop": "lockpick", "rare_drop": None, "money_range": (6,28),
 "basic_attack": "feints and cons", "strong_attack": "outsmarting elbow", "player_abilities": None,
 "base_str":2, "base_dex":4, "base_con":2, "base_int":4, "base_hp":22, "base_ap":4,
 "str_per_level":0, "dex_per_level":2, "con_per_level":0, "int_per_level":1},

 # min_spawn_level ==6
 {"id": "salt_marshall", "name": "Salt Marshall", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":6, "rarity": "rare", "base_xp":88,
 "common_drop": "stimulant_med", "rare_drop": "kevlar_vest", "money_range": (15,56),
 "basic_attack": "fires a sand-laced shot", "strong_attack": "overcharged burst", "player_abilities": ["smoke_bomb", "emp_burst"],
 "base_str":4, "base_dex":5, "base_con":6, "base_int":3, "base_hp":40, "base_ap":5,
 "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 {"id": "market_bouncer", "name": "Market Bouncer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":60,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (6,30),
 "basic_attack": "heaves you off a stall", "strong_attack": "bottle-smash fanfare", "player_abilities": [],
 "base_str":4, "base_dex":3, "base_con":3, "base_int":2, "base_hp":30, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 {"id": "rival_barkeep", "name": "Rival Barkeep", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":6, "rarity": "uncommon", "base_xp":60,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (8,36),
 "basic_attack": "towel-slap", "strong_attack": "bottle-smash aria", "player_abilities": None,
 "base_str":4, "base_dex":3, "base_con":3, "base_int":2, "base_hp":32, "base_ap":4,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 # min_spawn_level ==7
 {"id": "oasis_smuggler", "name": "Oasis Smuggler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "common", "base_xp":54,
 "common_drop": "lockpick", "rare_drop": "stimulant_large", "money_range": (12,72),
 "basic_attack": "jab with a water-blade", "strong_attack": "poison spoil", "player_abilities": None,
 "base_str":3, "base_dex":6, "base_con":3, "base_int":3, "base_hp":28, "base_ap":4,
 "str_per_level":1, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "tough_grammy", "name": "Tough Grammy", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":7, "rarity": "uncommon", "base_xp":56,
 "common_drop": "herb_med", "rare_drop": None, "money_range": (6,36),
 "basic_attack": "needle jab", "strong_attack": "heavy pummel", "player_abilities": None,
 "base_str":4, "base_dex":2, "base_con":5, "base_int":2, "base_hp":48, "base_ap":3,
 "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 # min_spawn_level ==8
 {"id": "caravan_fixer", "name": "Caravan Fixer", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":8, "rarity": "common", "base_xp":56,
 "common_drop": "lockpick", "rare_drop": "tome_dex", "money_range": (10,64),
 "basic_attack": "shocks with a rusted relay", "strong_attack": "system spill", "player_abilities": ["hack_overload", "emp_burst"],
 "base_str":2, "base_dex":3, "base_con":2, "base_int":7, "base_hp":26, "base_ap":5,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "plank_marauder", "name": "Plank Marauder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":8, "rarity": "rare", "base_xp":112,
 "common_drop": "lockpick", "rare_drop": "pipe_wrench", "money_range": (18,88),
 "basic_attack": "silent sand-stab", "strong_attack": "lethal plank dance", "player_abilities": ["precise_strike", "poison_dart"],
 "base_str":3, "base_dex":8, "base_con":3, "base_int":3, "base_hp":32, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # min_spawn_level ==9
 {"id": "dune_hound", "name": "Dune Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":9, "rarity": "uncommon", "base_xp":72,
 "common_drop": "stimulant_small", "rare_drop": None, "money_range": (8,34),
 "basic_attack": "rips with sand-laced fangs", "strong_attack": "venomous lunge", "player_abilities": None,
 "base_str":6, "base_dex":6, "base_con":4, "base_int":1, "base_hp":42, "base_ap":4,
 "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":0},

 {"id": "marksman_drifter", "name": "Marksman Drifter", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":9, "rarity": "superrare", "base_xp":124,
 "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (24,110),
 "basic_attack": "precise drift-shot", "strong_attack": "headshot from afar", "player_abilities": ["quick_shot", "chain_lightning"],
 "base_str":3, "base_dex":7, "base_con":3, "base_int":3, "base_hp":34, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 # min_spawn_level ==10
 {"id": "resting_sand_sniper", "name": "Resting Sand Sniper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":10, "rarity": "rare", "base_xp":130,
 "common_drop": "stimulant_med", "rare_drop": "handgun_basic", "money_range": (28,110),
 "basic_attack": "takes a dry-lined shot", "strong_attack": "dune-arc salvo", "player_abilities": None,
 "base_str":2, "base_dex":8, "base_con":2, "base_int":3, "base_hp":30, "base_ap":6,
 "str_per_level":1, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 {"id": "wrench_madam", "name": "Wrench Madam", "hostile_type": "humanoid", "role": "support", "min_spawn_level":10, "rarity": "rare", "base_xp":132,
 "common_drop": "lockpick", "rare_drop": "tome_dex", "money_range": (30,140),
 "basic_attack": "wrench whap", "strong_attack": "hydraulic toss", "player_abilities": ["hack_overload", "reinforce_frame"],
 "base_str":3, "base_dex":4, "base_con":4, "base_int":7, "base_hp":44, "base_ap":6,
 "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":2}
]
