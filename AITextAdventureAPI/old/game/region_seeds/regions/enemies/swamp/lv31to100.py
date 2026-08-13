# Swamp Overworld — hostile seeds levels 31-100.

SEEDS_LV31TO100 = [

 # min_spawn_level == 31
 {"id": "bog_warlord", "name": "Bog Warlord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 520,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (120, 400),
  "basic_attack": "bog axe", "strong_attack": "swamp war cry",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 18, "base_dex": 10, "base_con": 16, "base_int": 4, "base_hp": 480, "base_ap": 10,
  "str_per_level": 4, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},

 {"id": "plague_elemental", "name": "Plague Elemental", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 500,
  "common_drop": "ointment", "rare_drop": "herb_major", "money_range": (10, 50),
  "basic_attack": "plague touch", "strong_attack": "blight wave",
  "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit", "water_dark_magic_lv2_abyssal_tide"],
  "base_str": 10, "base_dex": 10, "base_con": 12, "base_int": 16, "base_hp": 400, "base_ap": 16,
  "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 3},

 # min_spawn_level == 38
 {"id": "bog_dragon", "name": "Bog Dragon", "hostile_type": "creature", "role": "damage", "min_spawn_level": 38, "rarity": "superrare", "base_xp": 2400,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (400, 1400),
  "basic_attack": "bog claw", "strong_attack": "poison breath",
  "player_abilities": ["level_1_hostile_ability_poison_dart", "water_dark_magic_lv2_abyssal_tide"],
  "base_str": 32, "base_dex": 14, "base_con": 30, "base_int": 10, "base_hp": 1600, "base_ap": 12,
  "str_per_level": 6, "dex_per_level": 2, "con_per_level": 6, "int_per_level": 2},

 # min_spawn_level == 50
 {"id": "swamp_leviathan", "name": "Swamp Leviathan", "hostile_type": "creature", "role": "damage", "min_spawn_level": 50, "rarity": "superrare", "base_xp": 6500,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1200, 4200),
  "basic_attack": "swamp coil", "strong_attack": "bog burial",
  "player_abilities": ["level_1_hostile_ability_poison_dart"],
  "base_str": 54, "base_dex": 10, "base_con": 50, "base_int": 6, "base_hp": 5000, "base_ap": 10,
  "str_per_level": 10, "dex_per_level": 1, "con_per_level": 9, "int_per_level": 0},

 # min_spawn_level == 65
 {"id": "blight_titan", "name": "Blight Titan", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 65, "rarity": "superrare", "base_xp": 12000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (3000, 10000),
  "basic_attack": "blight fist", "strong_attack": "plague world obliteration",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_electric_water_magic_lv3_night_tide"],
  "base_str": 42, "base_dex": 18, "base_con": 40, "base_int": 50, "base_hp": 10000, "base_ap": 44,
  "str_per_level": 8, "dex_per_level": 3, "con_per_level": 8, "int_per_level": 10},

 # min_spawn_level == 100
 {"id": "swamp_world_god", "name": "Swamp World God", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 120000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (50000, 160000),
  "basic_attack": "world blight decree", "strong_attack": "end of the swamp age",
  "player_abilities": ["dark_electric_water_magic_lv3_night_tide", "water_water_water_magic_lv3_tsunami_burst"],
  "base_str": 132, "base_dex": 26, "base_con": 126, "base_int": 34, "base_hp": 100000, "base_ap": 26,
  "str_per_level": 26, "dex_per_level": 5, "con_per_level": 25, "int_per_level": 7},

 # min_spawn_level == 51 (fills Lv51-60 gap)
 {"id": "swamp_elder_bog_wyrm", "name": "Elder Bog Wyrm", "hostile_type": "creature", "role": "damage", "min_spawn_level": 51, "rarity": "superrare", "base_xp": 7000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1500, 5000),
  "basic_attack": "bog bite", "strong_attack": "mire surge",
  "player_abilities": None,
  "base_str": 56, "base_dex": 14, "base_con": 52, "base_int": 8, "base_hp": 5500, "base_ap": 10,
  "str_per_level": 11, "dex_per_level": 2, "con_per_level": 10, "int_per_level": 1},

 {"id": "swamp_necrotic_colossus", "name": "Necrotic Colossus", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 57, "rarity": "superrare", "base_xp": 9000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (1000, 3500),
  "basic_attack": "necrotic slam", "strong_attack": "death shatter",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 62, "base_dex": 8, "base_con": 58, "base_int": 22, "base_hp": 7000, "base_ap": 20,
  "str_per_level": 12, "dex_per_level": 1, "con_per_level": 11, "int_per_level": 4},

 # min_spawn_level == 71 (fills Lv71-80 gap)
 {"id": "swamp_elder_lich", "name": "Elder Swamp Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 71, "rarity": "superrare", "base_xp": 20000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (6000, 20000),
  "basic_attack": "elder death bolt", "strong_attack": "lich swamp storm",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 12, "base_dex": 14, "base_con": 14, "base_int": 82, "base_hp": 14000, "base_ap": 68,
  "str_per_level": 2, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 16},

 {"id": "swamp_bog_titan_ow", "name": "Bog Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 76, "rarity": "superrare", "base_xp": 24000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (8000, 27000),
  "basic_attack": "bog titan slam", "strong_attack": "swamp shatter",
  "player_abilities": None,
  "base_str": 96, "base_dex": 12, "base_con": 90, "base_int": 10, "base_hp": 24000, "base_ap": 12,
  "str_per_level": 19, "dex_per_level": 2, "con_per_level": 18, "int_per_level": 2},

 # min_spawn_level == 81 (fills Lv81-90 gap)
 {"id": "swamp_void_colossus", "name": "Swamp Void Colossus", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 81, "rarity": "superrare", "base_xp": 33000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (11000, 36000),
  "basic_attack": "void fist", "strong_attack": "void swamp eruption",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 22, "base_dex": 18, "base_con": 22, "base_int": 116, "base_hp": 30000, "base_ap": 96,
  "str_per_level": 4, "dex_per_level": 3, "con_per_level": 4, "int_per_level": 23},

 {"id": "swamp_blight_titan", "name": "Blight Titan", "hostile_type": "undead", "role": "damage", "min_spawn_level": 86, "rarity": "superrare", "base_xp": 42000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (15000, 50000),
  "basic_attack": "blight titan slam", "strong_attack": "swamp world shatter",
  "player_abilities": ["dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 120, "base_dex": 16, "base_con": 114, "base_int": 24, "base_hp": 46000, "base_ap": 22,
  "str_per_level": 24, "dex_per_level": 3, "con_per_level": 23, "int_per_level": 4},
]
