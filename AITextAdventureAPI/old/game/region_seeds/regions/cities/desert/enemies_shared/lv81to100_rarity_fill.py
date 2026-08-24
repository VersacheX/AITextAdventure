# Desert shared hostiles - rarity-coverage fill, Lv 81-100.
#
# Reusable across all desert city sizes (large / mid / small) and the desert
# wilderness. Each seed is placed at exactly the level the validator suggested
# so a single seed clears each stacked REGION_HOSTILE_RARITY_GAP window.

RANDOM_HOSTILE_SEEDS = [

    # min_spawn_level == 81 (uncommon + rare windows Lv 77-81)
    {"id": "iron_caravan_captain", "name": "Iron Caravan Captain", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 81, "rarity": "uncommon", "base_xp": 7400,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (400, 1400),
     "basic_attack": "greatsword sweep", "strong_attack": "captain's onslaught",
     "player_abilities": ["fire_technique_lv1_scorch_slash"],
     "base_str": 62, "base_dex": 38, "base_con": 54, "base_int": 14, "base_hp": 1400, "base_ap": 18,
     "str_per_level": 8, "dex_per_level": 5, "con_per_level": 7, "int_per_level": 1},
    {"id": "sunforge_juggernaut", "name": "Sunforge Juggernaut", "hostile_type": "construct", "role": "damage", "min_spawn_level": 81, "rarity": "rare", "base_xp": 8600,
     "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 150),
     "basic_attack": "molten piston", "strong_attack": "solar overpressure",
     "player_abilities": ["level_1_hostile_ability_reinforce_frame", "fire_earth_magic_lv2_magma_javelin"],
     "base_str": 72, "base_dex": 24, "base_con": 66, "base_int": 14, "base_hp": 1900, "base_ap": 18,
     "str_per_level": 10, "dex_per_level": 3, "con_per_level": 9, "int_per_level": 1},

    # min_spawn_level == 82 (common window Lv 78-82)
    {"id": "boneglass_maw_beast", "name": "Boneglass Maw Beast", "hostile_type": "creature", "role": "damage", "min_spawn_level": 82, "rarity": "common", "base_xp": 7000,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (320, 1100),
     "basic_attack": "glass-fanged bite", "strong_attack": "shattering maul",
     "player_abilities": [],
     "base_str": 64, "base_dex": 40, "base_con": 56, "base_int": 12, "base_hp": 1500, "base_ap": 18,
     "str_per_level": 9, "dex_per_level": 5, "con_per_level": 8, "int_per_level": 0},

    # min_spawn_level == 86 (uncommon + rare windows Lv 82-86)
    {"id": "veil_cult_hierophant", "name": "Veil Cult Hierophant", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 86, "rarity": "uncommon", "base_xp": 9200,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (460, 1600),
     "basic_attack": "whispered hex", "strong_attack": "veil of unbeing",
     "player_abilities": ["dark_dark_magic_lv2_umbra_storm"],
     "base_str": 34, "base_dex": 38, "base_con": 44, "base_int": 60, "base_hp": 1600, "base_ap": 20,
     "str_per_level": 5, "dex_per_level": 5, "con_per_level": 6, "int_per_level": 9},
    {"id": "warglass_juggernaut", "name": "Warglass Juggernaut", "hostile_type": "construct", "role": "damage", "min_spawn_level": 86, "rarity": "rare", "base_xp": 10400,
     "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 160),
     "basic_attack": "war-piston slam", "strong_attack": "shatterfront charge",
     "player_abilities": ["level_1_hostile_ability_reinforce_frame", "earth_earth_magic_lv2_quake_field"],
     "base_str": 78, "base_dex": 30, "base_con": 70, "base_int": 14, "base_hp": 2100, "base_ap": 19,
     "str_per_level": 10, "dex_per_level": 4, "con_per_level": 9, "int_per_level": 1},

    # min_spawn_level == 87 (common window Lv 83-87)
    {"id": "grit_wall_enforcer", "name": "Grit Wall Enforcer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 87, "rarity": "common", "base_xp": 8800,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (400, 1400),
     "basic_attack": "riot maul", "strong_attack": "crushing wall press",
     "player_abilities": [],
     "base_str": 70, "base_dex": 36, "base_con": 62, "base_int": 12, "base_hp": 1800, "base_ap": 19,
     "str_per_level": 10, "dex_per_level": 5, "con_per_level": 8, "int_per_level": 0},

    # min_spawn_level == 88 (rare window Lv 84-88)
    {"id": "abyssal_dune_horror", "name": "Abyssal Dune Horror", "hostile_type": "eldritch", "role": "damage", "min_spawn_level": 88, "rarity": "rare", "base_xp": 11000,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (520, 1800),
     "basic_attack": "grasping tendril", "strong_attack": "engulfing collapse",
     "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 74, "base_dex": 46, "base_con": 68, "base_int": 26, "base_hp": 1950, "base_ap": 20,
     "str_per_level": 10, "dex_per_level": 6, "con_per_level": 9, "int_per_level": 3},

    # min_spawn_level == 89 (superrare window Lv 85-89)
    {"id": "eclipse_spire_god", "name": "Eclipse Spire God", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 89, "rarity": "superrare", "base_xp": 46000,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (12000, 40000),
     "basic_attack": "eclipse command", "strong_attack": "spire star-collapse",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 44, "base_dex": 54, "base_con": 58, "base_int": 100, "base_hp": 26000, "base_ap": 90,
     "str_per_level": 6, "dex_per_level": 7, "con_per_level": 8, "int_per_level": 20},

    # min_spawn_level == 91 (uncommon + rare windows Lv 87-91)
    {"id": "warglass_centurion", "name": "Warglass Centurion", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 91, "rarity": "uncommon", "base_xp": 13000,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (600, 2200),
     "basic_attack": "glaive cleave", "strong_attack": "phalanx breaker",
     "player_abilities": ["fire_technique_lv1_scorch_slash"],
     "base_str": 82, "base_dex": 52, "base_con": 74, "base_int": 18, "base_hp": 2000, "base_ap": 22,
     "str_per_level": 9, "dex_per_level": 6, "con_per_level": 8, "int_per_level": 1},
    {"id": "tomb_pharaoh_revenant", "name": "Tomb Pharaoh Revenant", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 91, "rarity": "rare", "base_xp": 15000,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (700, 2500),
     "basic_attack": "curse of dynasties", "strong_attack": "tomb-sealing edict",
     "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 40, "base_dex": 46, "base_con": 54, "base_int": 88, "base_hp": 2000, "base_ap": 24,
     "str_per_level": 5, "dex_per_level": 6, "con_per_level": 7, "int_per_level": 12},

    # min_spawn_level == 92 (common window Lv 88-92)
    {"id": "duneheart_ravager", "name": "Duneheart Ravager", "hostile_type": "creature", "role": "damage", "min_spawn_level": 92, "rarity": "common", "base_xp": 12500,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (500, 1900),
     "basic_attack": "rending gore", "strong_attack": "sandquake rampage",
     "player_abilities": [],
     "base_str": 84, "base_dex": 54, "base_con": 76, "base_int": 14, "base_hp": 2100, "base_ap": 21,
     "str_per_level": 10, "dex_per_level": 6, "con_per_level": 9, "int_per_level": 0},

    # min_spawn_level == 96 (uncommon + rare windows Lv 92-96)
    {"id": "stormglass_marauder", "name": "Stormglass Marauder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 96, "rarity": "uncommon", "base_xp": 17000,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (800, 2800),
     "basic_attack": "storm-etched slash", "strong_attack": "gale-driven rampage",
     "player_abilities": ["fire_technique_lv1_scorch_slash"],
     "base_str": 92, "base_dex": 60, "base_con": 84, "base_int": 20, "base_hp": 2400, "base_ap": 23,
     "str_per_level": 10, "dex_per_level": 7, "con_per_level": 9, "int_per_level": 1},
    {"id": "duneglass_wyrm", "name": "Duneglass Wyrm", "hostile_type": "creature", "role": "damage", "min_spawn_level": 96, "rarity": "rare", "base_xp": 19000,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (900, 3200),
     "basic_attack": "glass-scaled coil", "strong_attack": "shatter-fang devour",
     "player_abilities": ["level_1_hostile_ability_poison_dart", "fire_earth_magic_lv2_magma_javelin"],
     "base_str": 96, "base_dex": 62, "base_con": 88, "base_int": 18, "base_hp": 2600, "base_ap": 22,
     "str_per_level": 10, "dex_per_level": 7, "con_per_level": 9, "int_per_level": 1},

    # min_spawn_level == 97 (common window Lv 93-97)
    {"id": "sandstorm_ravager", "name": "Sandstorm Ravager", "hostile_type": "creature", "role": "damage", "min_spawn_level": 97, "rarity": "common", "base_xp": 16500,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (700, 2500),
     "basic_attack": "howling gore", "strong_attack": "cyclone rampage",
     "player_abilities": [],
     "base_str": 94, "base_dex": 58, "base_con": 86, "base_int": 16, "base_hp": 2500, "base_ap": 22,
     "str_per_level": 10, "dex_per_level": 7, "con_per_level": 9, "int_per_level": 0},

    # min_spawn_level == 98 (rare window Lv 94-98)
    {"id": "eclipse_dune_warlock", "name": "Eclipse Dune Warlock", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 98, "rarity": "rare", "base_xp": 20000,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (900, 3200),
     "basic_attack": "eclipse hex", "strong_attack": "collapsing star curse",
     "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 48, "base_dex": 56, "base_con": 62, "base_int": 96, "base_hp": 2300, "base_ap": 26,
     "str_per_level": 6, "dex_per_level": 7, "con_per_level": 8, "int_per_level": 13},

    # min_spawn_level == 99 (superrare window Lv 95-99)
    {"id": "dune_end_god", "name": "The Dune-End God", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 99, "rarity": "superrare", "base_xp": 110000,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (36000, 110000),
     "basic_attack": "world-ending gale", "strong_attack": "sands of finality",
     "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 132, "base_dex": 30, "base_con": 126, "base_int": 30, "base_hp": 84000, "base_ap": 24,
     "str_per_level": 26, "dex_per_level": 6, "con_per_level": 24, "int_per_level": 5},
]
