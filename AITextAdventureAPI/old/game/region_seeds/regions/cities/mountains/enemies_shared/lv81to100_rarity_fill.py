# Mountains shared hostiles - rarity-coverage fill, Lv 81-100.
#
# EFFICIENT fill: seeds placed at the union of gap anchors from the mountain
# small/mid/large reports for this band, collapsed so each seed's coverage
# window (anchors N-4..N) satisfies as many flagged anchors as possible:
#   common    -> Lv 81, 86, 91, 96
#   uncommon  -> Lv 81, 86, 91, 96
#   rare      -> Lv 82, 87, 92, 97   (also covers large's 85/90/95/100 windows)
#   superrare -> Lv 82, 92, 98       (collapsed: 82 covers 78/82, 92 covers 89/91/92, 98 covers 97/98)
#
# Ability ids reused from loaded band files (known-valid vs PLAYER_ABILITY_SEEDS).
# Theme: apex forge-gods, world-titans, void-touched summit horrors.

RANDOM_HOSTILE_SEEDS = [

    # ?? common ?????????????????????????????????????????????????????????????
    {"id": "mountain_shared_warpeak_marauder", "name": "Warpeak Marauder", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 81, "rarity": "common", "base_xp": 6600,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (300, 1050),
     "basic_attack": "greataxe cleave", "strong_attack": "summit onslaught",
     "player_abilities": [],
     "base_str": 66, "base_dex": 30, "base_con": 58, "base_int": 10, "base_hp": 1500, "base_ap": 18,
     "str_per_level": 10, "dex_per_level": 3, "con_per_level": 7, "int_per_level": 0},
    {"id": "mountain_shared_granite_behemoth", "name": "Granite Behemoth", "hostile_type": "creature", "role": "damage", "min_spawn_level": 86, "rarity": "common", "base_xp": 8000,
     "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 130),
     "basic_attack": "granite smash", "strong_attack": "mountain quake",
     "player_abilities": [],
     "base_str": 74, "base_dex": 24, "base_con": 66, "base_int": 8, "base_hp": 1750, "base_ap": 18,
     "str_per_level": 11, "dex_per_level": 2, "con_per_level": 8, "int_per_level": 0},
    {"id": "mountain_shared_ironsummit_champion", "name": "Ironsummit Champion", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 91, "rarity": "common", "base_xp": 10000,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (400, 1400),
     "basic_attack": "champion maul", "strong_attack": "peakbreaker execution",
     "player_abilities": [],
     "base_str": 82, "base_dex": 34, "base_con": 72, "base_int": 10, "base_hp": 2100, "base_ap": 19,
     "str_per_level": 12, "dex_per_level": 4, "con_per_level": 9, "int_per_level": 0},
    {"id": "mountain_shared_titan_yeti", "name": "Titan Yeti", "hostile_type": "creature", "role": "damage", "min_spawn_level": 96, "rarity": "common", "base_xp": 13000,
     "common_drop": "herb_major", "rare_drop": None, "money_range": (0, 150),
     "basic_attack": "colossal swipe", "strong_attack": "glacier avalanche",
     "player_abilities": [],
     "base_str": 90, "base_dex": 30, "base_con": 82, "base_int": 10, "base_hp": 2500, "base_ap": 20,
     "str_per_level": 13, "dex_per_level": 3, "con_per_level": 11, "int_per_level": 0},

    # ?? uncommon ???????????????????????????????????????????????????????????
    {"id": "mountain_shared_skyfang_wyvern", "name": "Skyfang Wyvern", "hostile_type": "creature", "role": "damage", "min_spawn_level": 81, "rarity": "uncommon", "base_xp": 7200,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (360, 1250),
     "basic_attack": "skyfang rake", "strong_attack": "apex divebomb",
     "player_abilities": ["air_skill_lv1_smoke_bomb"],
     "base_str": 66, "base_dex": 54, "base_con": 56, "base_int": 14, "base_hp": 1550, "base_ap": 19,
     "str_per_level": 10, "dex_per_level": 6, "con_per_level": 7, "int_per_level": 1},
    {"id": "mountain_shared_magmaforge_warlord", "name": "Magmaforge Warlord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 86, "rarity": "uncommon", "base_xp": 8800,
     "common_drop": "herb_major", "rare_drop": "tome_str", "money_range": (420, 1450),
     "basic_attack": "molten cleave", "strong_attack": "forgefire devastation",
     "player_abilities": ["fire_technique_lv1_scorch_slash", "earth_magic_lv1_tremor"],
     "base_str": 76, "base_dex": 36, "base_con": 66, "base_int": 16, "base_hp": 1800, "base_ap": 19,
     "str_per_level": 11, "dex_per_level": 4, "con_per_level": 8, "int_per_level": 1},
    {"id": "mountain_shared_permafrost_alpha", "name": "Permafrost Alpha", "hostile_type": "creature", "role": "damage", "min_spawn_level": 91, "rarity": "uncommon", "base_xp": 11000,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (480, 1650),
     "basic_attack": "permafrost bite", "strong_attack": "blizzard takedown",
     "player_abilities": ["level_1_hostile_ability_poison_dart"],
     "base_str": 82, "base_dex": 52, "base_con": 72, "base_int": 14, "base_hp": 2100, "base_ap": 20,
     "str_per_level": 12, "dex_per_level": 6, "con_per_level": 8, "int_per_level": 0},
    {"id": "mountain_shared_tempest_hierophant", "name": "Tempest Hierophant", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level": 96, "rarity": "uncommon", "base_xp": 14000,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (540, 1850),
     "basic_attack": "storm sigil", "strong_attack": "tempest litany",
     "player_abilities": ["air_skill_lv1_smoke_bomb", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 46, "base_dex": 52, "base_con": 60, "base_int": 84, "base_hp": 2200, "base_ap": 24,
     "str_per_level": 6, "dex_per_level": 6, "con_per_level": 8, "int_per_level": 13},

    # ?? rare ???????????????????????????????????????????????????????????????
    {"id": "mountain_shared_worldforge_golem", "name": "Worldforge Golem", "hostile_type": "construct", "role": "hazard", "min_spawn_level": 82, "rarity": "rare", "base_xp": 8000,
     "common_drop": None, "rare_drop": "tome_con", "money_range": (0, 200),
     "basic_attack": "worldforge fist", "strong_attack": "cataclysmic stomp",
     "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field"],
     "base_str": 78, "base_dex": 22, "base_con": 80, "base_int": 14, "base_hp": 2000, "base_ap": 18,
     "str_per_level": 11, "dex_per_level": 2, "con_per_level": 10, "int_per_level": 1},
    {"id": "mountain_shared_infernal_wyrm", "name": "Infernal Wyrm", "hostile_type": "creature", "role": "damage", "min_spawn_level": 87, "rarity": "rare", "base_xp": 9600,
     "common_drop": "herb_major", "rare_drop": "tome_str", "money_range": (500, 1700),
     "basic_attack": "infernal breath", "strong_attack": "molten coil devastation",
     "player_abilities": ["fire_technique_lv1_scorch_slash", "earth_earth_magic_lv2_quake_field"],
     "base_str": 78, "base_dex": 44, "base_con": 68, "base_int": 28, "base_hp": 2000, "base_ap": 22,
     "str_per_level": 11, "dex_per_level": 5, "con_per_level": 8, "int_per_level": 2},
    {"id": "mountain_shared_summit_archlich", "name": "Summit Archlich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 92, "rarity": "rare", "base_xp": 12000,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (620, 2100),
     "basic_attack": "soul blizzard", "strong_attack": "peak-eternal requiem",
     "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 48, "base_dex": 46, "base_con": 58, "base_int": 82, "base_hp": 2100, "base_ap": 24,
     "str_per_level": 6, "dex_per_level": 5, "con_per_level": 7, "int_per_level": 13},
    {"id": "mountain_shared_stormcrown_archon", "name": "Stormcrown Archon", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 97, "rarity": "rare", "base_xp": 16000,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (760, 2600),
     "basic_attack": "crown arc", "strong_attack": "apex chain tempest",
     "player_abilities": ["air_skill_lv1_smoke_bomb", "dark_dark_dark_magic_lv3_shadow_blast", "earth_earth_magic_lv2_quake_field"],
     "base_str": 56, "base_dex": 54, "base_con": 66, "base_int": 90, "base_hp": 2300, "base_ap": 26,
     "str_per_level": 7, "dex_per_level": 6, "con_per_level": 8, "int_per_level": 14},

    # ?? superrare ??????????????????????????????????????????????????????????
    {"id": "mountain_shared_worldpeak_god", "name": "Worldpeak God", "hostile_type": "eldritch", "role": "damage", "min_spawn_level": 82, "rarity": "superrare", "base_xp": 40000,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (10000, 34000),
     "basic_attack": "worldpeak wrath", "strong_attack": "mountain-end cataclysm",
     "player_abilities": ["earth_earth_magic_lv2_quake_field", "dark_dark_dark_magic_lv3_shadow_blast", "dark_dark_magic_lv2_umbra_storm"],
     "base_str": 80, "base_dex": 46, "base_con": 72, "base_int": 60, "base_hp": 24000, "base_ap": 70,
     "str_per_level": 14, "dex_per_level": 6, "con_per_level": 12, "int_per_level": 10},
    {"id": "mountain_shared_the_deep_hunger", "name": "The Deep Hunger", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 92, "rarity": "superrare", "base_xp": 54000,
     "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (14000, 46000),
     "basic_attack": "devouring dark", "strong_attack": "unmaking of the deep",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 88, "base_dex": 54, "base_con": 80, "base_int": 76, "base_hp": 30000, "base_ap": 82,
     "str_per_level": 16, "dex_per_level": 7, "con_per_level": 14, "int_per_level": 12},
    {"id": "mountain_shared_the_summit_eternal", "name": "The Summit Eternal", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 98, "rarity": "superrare", "base_xp": 68000,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (18000, 60000),
     "basic_attack": "eternal gale", "strong_attack": "the peak ascends",
     "player_abilities": ["air_skill_lv1_smoke_bomb", "earth_earth_magic_lv2_quake_field", "dark_dark_dark_magic_lv3_shadow_blast"],
     "base_str": 100, "base_dex": 60, "base_con": 90, "base_int": 80, "base_hp": 34000, "base_ap": 90,
     "str_per_level": 18, "dex_per_level": 8, "con_per_level": 15, "int_per_level": 13},
]
