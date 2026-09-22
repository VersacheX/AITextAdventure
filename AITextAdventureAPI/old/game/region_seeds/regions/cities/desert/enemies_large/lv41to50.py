# Desert Large City — hostile seeds levels 41-50 (apex city threats and legendary desert horrors).

RANDOM_HOSTILE_SEEDS = [

 # min_spawn_level == 41
 {"id": "iron_templar", "name": "Iron Templar", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 41, "rarity": "uncommon", "base_xp": 700,
  "common_drop": "kevlar_vest", "rare_drop": "stimulant_large", "money_range": (160, 520),
  "basic_attack": "iron cross", "strong_attack": "templar siege",
  "player_abilities": ["level_1_hostile_ability_inspire", "light_technique_lv1_radiant_slash"],
  "base_str": 26, "base_dex": 8, "base_con": 24, "base_int": 6, "base_hp": 740, "base_ap": 10,
  "str_per_level": 5, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 1},

 {"id": "mirage_specter", "name": "Mirage Specter", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 41, "rarity": "uncommon", "base_xp": 760,
  "common_drop": "tome_int", "rare_drop": None, "money_range": (30, 130),
  "basic_attack": "spectre touch", "strong_attack": "mind fracture",
  "player_abilities": ["level_1_hostile_ability_dark_magic_daze_whisper", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 4, "base_dex": 14, "base_con": 6, "base_int": 28, "base_hp": 440, "base_ap": 22,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 7},

 # min_spawn_level == 42
 {"id": "dune_behemoth", "name": "Dune Behemoth", "hostile_type": "creature", "role": "damage", "min_spawn_level": 42, "rarity": "rare", "base_xp": 1200,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (60, 220),
  "basic_attack": "ground pound", "strong_attack": "cataclysmic charge",
  "player_abilities": None,
  "base_str": 32, "base_dex": 4, "base_con": 30, "base_int": 2, "base_hp": 1400, "base_ap": 6,
  "str_per_level": 7, "dex_per_level": 0, "con_per_level": 6, "int_per_level": 0},

 {"id": "sand_sorcerer_prime", "name": "Sand Sorcerer Prime", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 42, "rarity": "rare", "base_xp": 1100,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (200, 680),
  "basic_attack": "arcane surge", "strong_attack": "sandstorm nova",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field", "earth_earth_earth_magic_lv3_earthshaker"],
  "base_str": 6, "base_dex": 8, "base_con": 8, "base_int": 32, "base_hp": 500, "base_ap": 26,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 8},

 # min_spawn_level == 43
 {"id": "gilded_assassin_lord", "name": "Gilded Assassin Lord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 43, "rarity": "uncommon", "base_xp": 900,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (240, 800),
  "basic_attack": "precision stab", "strong_attack": "whirlwind of daggers",
  "player_abilities": ["level_1_hostile_ability_shadow_flicker", "ice_dark_skill_lv2_shadow_spike"],
  "base_str": 16, "base_dex": 30, "base_con": 14, "base_int": 10, "base_hp": 580, "base_ap": 22,
  "str_per_level": 2, "dex_per_level": 6, "con_per_level": 2, "int_per_level": 2},

 {"id": "elder_scorpion", "name": "Elder Scorpion", "hostile_type": "creature", "role": "damage", "min_spawn_level": 43, "rarity": "uncommon", "base_xp": 800,
  "common_drop": "ointment", "rare_drop": "herb_major", "money_range": (20, 90),
  "basic_attack": "pincer crush", "strong_attack": "elder sting",
  "player_abilities": ["level_1_hostile_ability_poison_dart"],
  "base_str": 24, "base_dex": 10, "base_con": 22, "base_int": 4, "base_hp": 900, "base_ap": 8,
  "str_per_level": 5, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 0},

 # min_spawn_level == 44
 {"id": "shadow_herald", "name": "Shadow Herald", "hostile_type": "shadow", "role": "hazard", "min_spawn_level": 44, "rarity": "rare", "base_xp": 1300,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (100, 380),
  "basic_attack": "herald's curse", "strong_attack": "void proclamation",
  "player_abilities": ["level_1_hostile_ability_night_whisper", "dark_electric_water_magic_lv3_night_tide"],
  "base_str": 8, "base_dex": 18, "base_con": 10, "base_int": 30, "base_hp": 560, "base_ap": 24,
  "str_per_level": 1, "dex_per_level": 3, "con_per_level": 2, "int_per_level": 6},

 {"id": "dune_siege_engine", "name": "Dune Siege Engine", "hostile_type": "construct", "role": "damage", "min_spawn_level": 44, "rarity": "uncommon", "base_xp": 880,
  "common_drop": None, "rare_drop": "kevlar_vest", "money_range": (0, 30),
  "basic_attack": "battering ram", "strong_attack": "ballista volley",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 30, "base_dex": 2, "base_con": 28, "base_int": 2, "base_hp": 1100, "base_ap": 4,
  "str_per_level": 6, "dex_per_level": 0, "con_per_level": 5, "int_per_level": 0},

 # min_spawn_level == 45
 {"id": "pharaoh_revenant", "name": "Pharaoh Revenant", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 45, "rarity": "superrare", "base_xp": 3200,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (400, 1200),
  "basic_attack": "scepter smite", "strong_attack": "royal death curse",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 20, "base_dex": 12, "base_con": 20, "base_int": 36, "base_hp": 1400, "base_ap": 28,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 8},

 # min_spawn_level == 46
 {"id": "volcanic_dust_wyrm", "name": "Volcanic Dust Wyrm", "hostile_type": "creature", "role": "damage", "min_spawn_level": 46, "rarity": "rare", "base_xp": 1600,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (100, 400),
  "basic_attack": "burrowing slam", "strong_attack": "eruption surge",
  "player_abilities": ["fire_magic_lv1_fireball", "fire_earth_magic_lv2_magma_javelin"],
  "base_str": 30, "base_dex": 8, "base_con": 28, "base_int": 6, "base_hp": 1600, "base_ap": 10,
  "str_per_level": 6, "dex_per_level": 1, "con_per_level": 5, "int_per_level": 1},

 {"id": "neon_shade", "name": "Neon Shade", "hostile_type": "shadow", "role": "damage", "min_spawn_level": 46, "rarity": "uncommon", "base_xp": 960,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (180, 580),
  "basic_attack": "neon slash", "strong_attack": "photon blitz",
  "player_abilities": ["level_1_hostile_ability_shadow_flicker", "electric_dark_skill_lv2_nightward_dart"],
  "base_str": 18, "base_dex": 26, "base_con": 14, "base_int": 14, "base_hp": 620, "base_ap": 20,
  "str_per_level": 3, "dex_per_level": 5, "con_per_level": 2, "int_per_level": 3},

 # min_spawn_level == 47
 {"id": "golden_cult_zealot", "name": "Golden Cult Zealot", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level": 47, "rarity": "uncommon", "base_xp": 1000,
  "common_drop": "tome_int", "rare_drop": "stimulant_large", "money_range": (160, 520),
  "basic_attack": "blessed strike", "strong_attack": "golden wrath",
  "player_abilities": ["light_spirit_lv1_convert", "fire_light_magic_lv2_solar_spike"],
  "base_str": 14, "base_dex": 10, "base_con": 16, "base_int": 26, "base_hp": 680, "base_ap": 22,
  "str_per_level": 2, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 6},

 # min_spawn_level == 48
 {"id": "dune_titan_sentinel", "name": "Dune Titan Sentinel", "hostile_type": "construct", "role": "damage", "min_spawn_level": 48, "rarity": "rare", "base_xp": 1800,
  "common_drop": None, "rare_drop": "kevlar_vest", "money_range": (0, 60),
  "basic_attack": "titan punch", "strong_attack": "seismic stomp",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame", "earth_magic_lv1_tremor"],
  "base_str": 36, "base_dex": 2, "base_con": 34, "base_int": 4, "base_hp": 2000, "base_ap": 8,
  "str_per_level": 7, "dex_per_level": 0, "con_per_level": 6, "int_per_level": 0},

 # min_spawn_level == 49
 {"id": "void_drifter", "name": "Void Drifter", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 49, "rarity": "rare", "base_xp": 1900,
  "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (200, 700),
  "basic_attack": "psychic barb", "strong_attack": "reality fracture",
  "player_abilities": ["level_1_hostile_ability_arcane_blast", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 6, "base_dex": 16, "base_con": 8, "base_int": 38, "base_hp": 700, "base_ap": 30,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 8},

 # min_spawn_level == 50
 {"id": "ancient_desert_colossus", "name": "Ancient Desert Colossus", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 50, "rarity": "superrare", "base_xp": 5000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (600, 2000),
  "basic_attack": "fist of the dune", "strong_attack": "colossal sandstorm",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field", "earth_earth_earth_magic_lv3_earthshaker"],
  "base_str": 44, "base_dex": 6, "base_con": 40, "base_int": 10, "base_hp": 3500, "base_ap": 10,
  "str_per_level": 9, "dex_per_level": 1, "con_per_level": 8, "int_per_level": 1},
]
