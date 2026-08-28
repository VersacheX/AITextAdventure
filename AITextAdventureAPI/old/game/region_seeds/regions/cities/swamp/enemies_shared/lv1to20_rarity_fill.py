# Swamp shared rarity-fill band Lv 1-20.
# Uniform multiple-of-5 ladder per rarity (seed at N covers window starts N-4..N).
# Safe drops (no swamp city reports a gap): common Lv 15/20, uncommon Lv 5/10/15,
# rare Lv 15, superrare Lv 10/20.
RANDOM_HOSTILE_SEEDS = [
    # --- common ---
    {"id": "swamp_shared_bog_rat", "name": "Bog Rat", "hostile_type": "creature", "role": "damage", "min_spawn_level": 5, "rarity": "common", "base_xp": 40,
     "common_drop": "herb_minor", "rare_drop": None, "money_range": (5, 30),
     "basic_attack": "gnawing bite", "strong_attack": "scurrying swarm",
     "player_abilities": [],
     "base_str": 5, "base_dex": 6, "base_con": 5, "base_int": 2, "base_hp": 42, "base_ap": 5,
     "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 0},
    {"id": "swamp_shared_marsh_leech", "name": "Marsh Leech", "hostile_type": "creature", "role": "damage", "min_spawn_level": 10, "rarity": "common", "base_xp": 90,
     "common_drop": "herb_minor", "rare_drop": None, "money_range": (8, 44),
     "basic_attack": "latching bite", "strong_attack": "blood drain",
     "player_abilities": [],
     "base_str": 7, "base_dex": 9, "base_con": 6, "base_int": 3, "base_hp": 90, "base_ap": 7,
     "str_per_level": 1, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 0},

    # --- uncommon ---
    {"id": "swamp_shared_mire_stalker", "name": "Mire Stalker", "hostile_type": "creature", "role": "damage", "min_spawn_level": 20, "rarity": "uncommon", "base_xp": 300,
     "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (24, 110),
     "basic_attack": "raking claw", "strong_attack": "reed ambush",
     "player_abilities": ["level_1_hostile_ability_poison_dart"],
     "base_str": 14, "base_dex": 16, "base_con": 12, "base_int": 5, "base_hp": 200, "base_ap": 10,
     "str_per_level": 2, "dex_per_level": 3, "con_per_level": 2, "int_per_level": 0},

    # --- rare ---
    {"id": "swamp_shared_will_o_wisp", "name": "Will-o'-Wisp", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 5, "rarity": "rare", "base_xp": 75,
     "common_drop": "herb_minor", "rare_drop": "herb_med", "money_range": (10, 48),
     "basic_attack": "luring glow", "strong_attack": "marsh fire",
     "player_abilities": ["air_skill_lv1_smoke_bomb"],
     "base_str": 5, "base_dex": 8, "base_con": 5, "base_int": 7, "base_hp": 48, "base_ap": 7,
     "str_per_level": 1, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 1},
    {"id": "swamp_shared_fen_naga", "name": "Fen Naga", "hostile_type": "creature", "role": "hazard", "min_spawn_level": 10, "rarity": "rare", "base_xp": 150,
     "common_drop": "herb_med", "rare_drop": "stimulant_small", "money_range": (14, 66),
     "basic_attack": "venom spit", "strong_attack": "mire coil",
     "player_abilities": ["level_1_hostile_ability_poison_dart", "air_skill_lv1_smoke_bomb"],
     "base_str": 8, "base_dex": 11, "base_con": 8, "base_int": 10, "base_hp": 92, "base_ap": 8,
     "str_per_level": 1, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 2},
    {"id": "swamp_shared_bog_warden", "name": "Bog Warden", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 20, "rarity": "rare", "base_xp": 320,
     "common_drop": "tome_int", "rare_drop": "stimulant_small", "money_range": (28, 120),
     "basic_attack": "grave mire", "strong_attack": "sunken grasp",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "earth_magic_lv1_tremor"],
     "base_str": 14, "base_dex": 14, "base_con": 16, "base_int": 18, "base_hp": 210, "base_ap": 12,
     "str_per_level": 2, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 3},

    # --- superrare ---
    {"id": "swamp_shared_drowned_wraith", "name": "Drowned Wraith", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 5, "rarity": "superrare", "base_xp": 90,
     "common_drop": "herb_minor", "rare_drop": "stimulant_med", "money_range": (20, 90),
     "basic_attack": "cold whisper", "strong_attack": "drowning dread",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "air_skill_lv1_smoke_bomb", "level_1_hostile_ability_poison_dart"],
     "base_str": 5, "base_dex": 8, "base_con": 5, "base_int": 9, "base_hp": 52, "base_ap": 7,
     "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 1},
    {"id": "swamp_shared_hex_shade", "name": "Hex Shade", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 15, "rarity": "superrare", "base_xp": 300,
     "common_drop": "herb_med", "rare_drop": "stimulant_med", "money_range": (40, 160),
     "basic_attack": "voodoo murmur", "strong_attack": "swamp madness",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "air_skill_lv1_smoke_bomb"],
     "base_str": 10, "base_dex": 13, "base_con": 10, "base_int": 14, "base_hp": 160, "base_ap": 10,
     "str_per_level": 2, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 2},
]
