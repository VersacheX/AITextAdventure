# Desert shared hostiles - rarity-coverage fill, Lv 21-40.
#
# Reusable across all desert city sizes (large / mid / small) and the desert
# wilderness. Each seed is placed at exactly the level the validator suggested
# so a single seed clears each stacked REGION_HOSTILE_RARITY_GAP window.

RANDOM_HOSTILE_SEEDS = [

    # min_spawn_level == 21 (superrare window Lv 17-21)
    {"id": "veil_spire_apparition", "name": "Veil Spire Apparition", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 21, "rarity": "superrare", "base_xp": 480,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (70, 280),
     "basic_attack": "twilight murmur", "strong_attack": "obsidian unmaking",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "level_1_hostile_ability_poison_dart"],
     "base_str": 7, "base_dex": 8, "base_con": 7, "base_int": 15, "base_hp": 108, "base_ap": 10,
     "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 3},

    # min_spawn_level == 22 (superrare window Lv 18-22)
    {"id": "dune_oracle_wraith", "name": "Dune Oracle Wraith", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 22, "rarity": "superrare", "base_xp": 520,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 300),
     "basic_attack": "prophetic murmur", "strong_attack": "sand-veiled unmaking",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "level_1_hostile_ability_poison_dart"],
     "base_str": 8, "base_dex": 8, "base_con": 8, "base_int": 16, "base_hp": 110, "base_ap": 10,
     "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 3},

    # min_spawn_level == 23 (rare window Lv 19-23)
    {"id": "glass_fang_asp", "name": "Glass Fang Asp", "hostile_type": "creature", "role": "damage", "min_spawn_level": 23, "rarity": "rare", "base_xp": 360,
     "common_drop": "herb_med", "rare_drop": "herb_major", "money_range": (60, 260),
     "basic_attack": "crystalline bite", "strong_attack": "venom surge",
     "player_abilities": ["level_1_hostile_ability_poison_dart", "fire_magic_lv1_fireball"],
     "base_str": 11, "base_dex": 12, "base_con": 8, "base_int": 4, "base_hp": 100, "base_ap": 8,
     "str_per_level": 2, "dex_per_level": 3, "con_per_level": 1, "int_per_level": 0},

    # min_spawn_level == 25 (rare window Lv 21-25)
    {"id": "market_cutthroat", "name": "Market Cutthroat", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 25, "rarity": "rare", "base_xp": 420,
     "common_drop": "herb_med", "rare_drop": "herb_major", "money_range": (80, 320),
     "basic_attack": "twin dagger flurry", "strong_attack": "back-alley execution",
     "player_abilities": ["fire_technique_lv1_scorch_slash", "level_1_hostile_ability_poison_dart"],
     "base_str": 13, "base_dex": 14, "base_con": 10, "base_int": 4, "base_hp": 120, "base_ap": 8,
     "str_per_level": 2, "dex_per_level": 3, "con_per_level": 2, "int_per_level": 0},

    # min_spawn_level == 26 (superrare window Lv 22-26)
    {"id": "spire_shadow_priest", "name": "Spire Shadow Priest", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 26, "rarity": "superrare", "base_xp": 600,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (90, 360),
     "basic_attack": "grave-dust litany", "strong_attack": "veil of the dead",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "level_1_hostile_ability_bone_spear"],
     "base_str": 9, "base_dex": 8, "base_con": 10, "base_int": 17, "base_hp": 116, "base_ap": 11,
     "str_per_level": 1, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 3},

    # min_spawn_level == 27 (superrare window Lv 23-27)
    {"id": "sand_saint_effigy", "name": "Sand Saint Effigy", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 27, "rarity": "superrare", "base_xp": 640,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (100, 380),
     "basic_attack": "grave-dust curse", "strong_attack": "sepulchral edict",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "level_1_hostile_ability_bone_spear"],
     "base_str": 9, "base_dex": 8, "base_con": 10, "base_int": 18, "base_hp": 118, "base_ap": 11,
     "str_per_level": 1, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 3},

    # min_spawn_level == 28 (common window Lv 24-28)
    {"id": "backstreet_tough", "name": "Backstreet Tough", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 28, "rarity": "common", "base_xp": 200,
     "common_drop": "herb_med", "rare_drop": "stimulant_med", "money_range": (40, 170),
     "basic_attack": "cudgel swing", "strong_attack": "gutter haymaker",
     "player_abilities": [],
     "base_str": 12, "base_dex": 8, "base_con": 11, "base_int": 3, "base_hp": 130, "base_ap": 7,
     "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 0},

    # min_spawn_level == 31 (superrare window Lv 27-31)
    {"id": "obsidian_dread_warden", "name": "Obsidian Dread Warden", "hostile_type": "construct", "role": "damage", "min_spawn_level": 31, "rarity": "superrare", "base_xp": 720,
     "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 120),
     "basic_attack": "obsidian cleave", "strong_attack": "dread lockstep",
     "player_abilities": ["level_1_hostile_ability_reinforce_frame", "earth_earth_magic_lv2_quake_field", "fire_technique_lv1_scorch_slash"],
     "base_str": 22, "base_dex": 8, "base_con": 20, "base_int": 6, "base_hp": 170, "base_ap": 9,
     "str_per_level": 3, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},

    # min_spawn_level == 33 (common window Lv 29-33)
    {"id": "dust_lane_mugger", "name": "Dust Lane Mugger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 33, "rarity": "common", "base_xp": 280,
     "common_drop": "herb_med", "rare_drop": "stimulant_large", "money_range": (50, 200),
     "basic_attack": "shiv jab", "strong_attack": "cutpurse rush",
     "player_abilities": [],
     "base_str": 13, "base_dex": 9, "base_con": 11, "base_int": 4, "base_hp": 150, "base_ap": 7,
     "str_per_level": 2, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},

    # min_spawn_level == 35 (rare window Lv 31-35)
    {"id": "chrome_veil_assassin", "name": "Chrome Veil Assassin", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 35, "rarity": "rare", "base_xp": 520,
     "common_drop": "herb_med", "rare_drop": "herb_major", "money_range": (90, 340),
     "basic_attack": "monowire slash", "strong_attack": "silent takedown",
     "player_abilities": ["fire_technique_lv1_scorch_slash", "dark_dark_magic_lv2_umbra_storm"],
     "base_str": 15, "base_dex": 18, "base_con": 12, "base_int": 6, "base_hp": 180, "base_ap": 10,
     "str_per_level": 3, "dex_per_level": 4, "con_per_level": 2, "int_per_level": 0},

    # min_spawn_level == 36 (superrare window Lv 32-36)
    {"id": "twilight_spire_lich", "name": "Twilight Spire Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 36, "rarity": "superrare", "base_xp": 900,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (140, 520),
     "basic_attack": "twilight bolt", "strong_attack": "spire death knell",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 12, "base_dex": 14, "base_con": 14, "base_int": 30, "base_hp": 220, "base_ap": 16,
     "str_per_level": 2, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 5},
]
