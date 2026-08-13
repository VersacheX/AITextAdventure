# Desert Mid City — hostile seeds levels 51-100 (high-tier to apex).

RANDOM_HOSTILE_SEEDS = [

 # min_spawn_level == 51
 {"id": "black_iron_sentinel", "name": "Black Iron Sentinel", "hostile_type": "construct", "role": "damage", "min_spawn_level": 51, "rarity": "uncommon", "base_xp": 1400,
  "common_drop": None, "rare_drop": "kevlar_vest", "money_range": (0, 50),
  "basic_attack": "iron slam", "strong_attack": "sentinel overdrive",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 40, "base_dex": 4, "base_con": 36, "base_int": 4, "base_hp": 2200, "base_ap": 8,
  "str_per_level": 8, "dex_per_level": 0, "con_per_level": 7, "int_per_level": 0},

 {"id": "sand_cult_archon", "name": "Sand Cult Archon", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 51, "rarity": "rare", "base_xp": 1800,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (500, 1600),
  "basic_attack": "archon curse", "strong_attack": "cult ceremony blast",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 8, "base_dex": 10, "base_con": 10, "base_int": 42, "base_hp": 800, "base_ap": 36,
  "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 9},

 # min_spawn_level == 55
 {"id": "city_revenant_lord", "name": "City Revenant Lord", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 55, "rarity": "superrare", "base_xp": 5000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (1000, 3500),
  "basic_attack": "lord's death call", "strong_attack": "revenant dominion",
  "player_abilities": ["level_1_hostile_ability_bone_spear", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 20, "base_dex": 14, "base_con": 20, "base_int": 50, "base_hp": 2600, "base_ap": 42,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 11},

 # min_spawn_level == 60
 {"id": "warlord_of_spires", "name": "Warlord of Spires", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 60, "rarity": "superrare", "base_xp": 7000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (2000, 7000),
  "basic_attack": "spire charge", "strong_attack": "warlord devastation",
  "player_abilities": ["level_1_hostile_ability_inspire", "fire_fire_magic_lv2_inferno_spread"],
  "base_str": 52, "base_dex": 18, "base_con": 48, "base_int": 12, "base_hp": 6000, "base_ap": 14,
  "str_per_level": 10, "dex_per_level": 3, "con_per_level": 9, "int_per_level": 2},

 # min_spawn_level == 65
 {"id": "nocturne_shadow_titan", "name": "Nocturne Shadow Titan", "hostile_type": "shadow", "role": "hazard", "min_spawn_level": 65, "rarity": "superrare", "base_xp": 9000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (2500, 9000),
  "basic_attack": "nocturne crush", "strong_attack": "shadow titan wave",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 20, "base_dex": 30, "base_con": 22, "base_int": 60, "base_hp": 4000, "base_ap": 50,
  "str_per_level": 3, "dex_per_level": 5, "con_per_level": 3, "int_per_level": 13},

 # min_spawn_level == 70
 {"id": "elder_city_drake", "name": "Elder City Drake", "hostile_type": "creature", "role": "damage", "min_spawn_level": 70, "rarity": "superrare", "base_xp": 13000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (4000, 13000),
  "basic_attack": "elder claw", "strong_attack": "city-quake breath",
  "player_abilities": ["fire_magic_lv1_fireball", "fire_fire_magic_lv2_inferno_spread"],
  "base_str": 70, "base_dex": 18, "base_con": 64, "base_int": 12, "base_hp": 12000, "base_ap": 16,
  "str_per_level": 14, "dex_per_level": 3, "con_per_level": 12, "int_per_level": 2},

 # min_spawn_level == 80
 {"id": "void_city_leviathan", "name": "Void City Leviathan", "hostile_type": "eldritch", "role": "damage", "min_spawn_level": 80, "rarity": "superrare", "base_xp": 22000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (8000, 26000),
  "basic_attack": "leviathan grind", "strong_attack": "city devourer",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_water_fire_magic_lv3_abyssal_flame"],
  "base_str": 86, "base_dex": 16, "base_con": 80, "base_int": 22, "base_hp": 22000, "base_ap": 18,
  "str_per_level": 17, "dex_per_level": 2, "con_per_level": 16, "int_per_level": 4},

 # min_spawn_level == 90
 {"id": "spire_god_avatar", "name": "Spire God Avatar", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 90, "rarity": "superrare", "base_xp": 50000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (18000, 60000),
  "basic_attack": "divine decree", "strong_attack": "spire collapse",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field", "earth_earth_earth_magic_lv3_earthshaker"],
  "base_str": 38, "base_dex": 26, "base_con": 38, "base_int": 110, "base_hp": 40000, "base_ap": 90,
  "str_per_level": 7, "dex_per_level": 5, "con_per_level": 7, "int_per_level": 22},

 # min_spawn_level == 100
 {"id": "nightveil_god", "name": "The Nightveil God", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 100000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40000, 130000),
  "basic_attack": "void edict", "strong_attack": "nightveil annihilation",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 26, "base_dex": 36, "base_con": 28, "base_int": 150, "base_hp": 80000, "base_ap": 120,
  "str_per_level": 4, "dex_per_level": 7, "con_per_level": 4, "int_per_level": 30},
]
