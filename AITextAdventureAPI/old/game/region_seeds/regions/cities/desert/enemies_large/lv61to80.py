# Desert Large City — hostile seeds levels 61-80 (elder-tier threats).

RANDOM_HOSTILE_SEEDS = [

 # min_spawn_level == 61
 {"id": "dune_elder_serpent", "name": "Dune Elder Serpent", "hostile_type": "creature", "role": "damage", "min_spawn_level": 61, "rarity": "rare", "base_xp": 3000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (300, 1000),
  "basic_attack": "venomous strike", "strong_attack": "constricting death",
  "player_abilities": ["level_1_hostile_ability_poison_dart", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 42, "base_dex": 16, "base_con": 38, "base_int": 8, "base_hp": 4200, "base_ap": 12,
  "str_per_level": 8, "dex_per_level": 2, "con_per_level": 7, "int_per_level": 1},

 # min_spawn_level == 62
 {"id": "spectral_pharaoh", "name": "Spectral Pharaoh", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 62, "rarity": "superrare", "base_xp": 8000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (1200, 4000),
  "basic_attack": "pharaonic curse", "strong_attack": "edict of death",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 22, "base_dex": 20, "base_con": 22, "base_int": 60, "base_hp": 3000, "base_ap": 50,
  "str_per_level": 3, "dex_per_level": 3, "con_per_level": 3, "int_per_level": 12},

 # min_spawn_level == 63
 {"id": "gilded_war_machine", "name": "Gilded War Machine", "hostile_type": "construct", "role": "damage", "min_spawn_level": 63, "rarity": "rare", "base_xp": 3600,
  "common_drop": None, "rare_drop": "kevlar_vest", "money_range": (0, 80),
  "basic_attack": "cannon volley", "strong_attack": "siege protocol",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 52, "base_dex": 4, "base_con": 48, "base_int": 6, "base_hp": 5500, "base_ap": 8,
  "str_per_level": 10, "dex_per_level": 0, "con_per_level": 9, "int_per_level": 1},

 # min_spawn_level == 65
 {"id": "void_leviathan", "name": "Void Leviathan", "hostile_type": "eldritch", "role": "damage", "min_spawn_level": 65, "rarity": "superrare", "base_xp": 10000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1500, 5000),
  "basic_attack": "void maw", "strong_attack": "leviathan crush",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_water_fire_magic_lv3_abyssal_flame"],
  "base_str": 60, "base_dex": 10, "base_con": 56, "base_int": 18, "base_hp": 7000, "base_ap": 14,
  "str_per_level": 12, "dex_per_level": 1, "con_per_level": 11, "int_per_level": 3},

 # min_spawn_level == 67
 {"id": "desert_god_avatar", "name": "Desert God Avatar", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 67, "rarity": "superrare", "base_xp": 12000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (2000, 7000),
  "basic_attack": "divine sandstorm", "strong_attack": "wrath of the dune god",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field", "earth_earth_earth_magic_lv3_earthshaker"],
  "base_str": 40, "base_dex": 22, "base_con": 40, "base_int": 64, "base_hp": 6000, "base_ap": 52,
  "str_per_level": 7, "dex_per_level": 4, "con_per_level": 7, "int_per_level": 13},

 # min_spawn_level == 70
 {"id": "death_colossus", "name": "Death Colossus", "hostile_type": "undead", "role": "damage", "min_spawn_level": 70, "rarity": "superrare", "base_xp": 15000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (3000, 10000),
  "basic_attack": "death march", "strong_attack": "colossus annihilation",
  "player_abilities": ["level_1_hostile_ability_bone_spear", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 70, "base_dex": 12, "base_con": 64, "base_int": 20, "base_hp": 10000, "base_ap": 16,
  "str_per_level": 14, "dex_per_level": 2, "con_per_level": 12, "int_per_level": 3},

 # min_spawn_level == 73
 {"id": "elder_desert_lich", "name": "Elder Desert Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 73, "rarity": "superrare", "base_xp": 18000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (4000, 14000),
  "basic_attack": "elder death bolt", "strong_attack": "lich apocalypse",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 12, "base_dex": 18, "base_con": 14, "base_int": 78, "base_hp": 5500, "base_ap": 64,
  "str_per_level": 1, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 16},

 # min_spawn_level == 76
 {"id": "gilded_golem_prime", "name": "Gilded Golem Prime", "hostile_type": "construct", "role": "damage", "min_spawn_level": 76, "rarity": "superrare", "base_xp": 20000,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 100),
  "basic_attack": "prime fist", "strong_attack": "golem supernova",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame", "earth_magic_lv1_tremor"],
  "base_str": 80, "base_dex": 6, "base_con": 76, "base_int": 10, "base_hp": 14000, "base_ap": 12,
  "str_per_level": 16, "dex_per_level": 1, "con_per_level": 15, "int_per_level": 1},

 # min_spawn_level == 80
 {"id": "abyssal_dune_titan", "name": "Abyssal Dune Titan", "hostile_type": "eldritch", "role": "damage", "min_spawn_level": 80, "rarity": "superrare", "base_xp": 28000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (6000, 20000),
  "basic_attack": "titan void claw", "strong_attack": "abyssal apocalypse",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 88, "base_dex": 14, "base_con": 82, "base_int": 24, "base_hp": 20000, "base_ap": 18,
  "str_per_level": 18, "dex_per_level": 2, "con_per_level": 16, "int_per_level": 4},
]
