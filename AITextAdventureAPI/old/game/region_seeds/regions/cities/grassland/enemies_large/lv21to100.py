# Grassland Large City — hostile seeds levels 21-100.

RANDOM_HOSTILE_SEEDS = [
 # min_spawn_level == 21
 {"id": "plains_champion", "name": "Plains Champion", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 280,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (60, 200),
  "basic_attack": "plains slash", "strong_attack": "champion charge",
  "player_abilities": [], "base_str": 12, "base_dex": 10, "base_con": 10, "base_int": 4, "base_hp": 320, "base_ap": 10,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},

 {"id": "grassland_revenant", "name": "Grassland Revenant", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 360,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "necrotic grasp", "strong_attack": "wail of the plains",
  "player_abilities": ["level_1_hostile_ability_bone_spear"],
  "base_str": 10, "base_dex": 8, "base_con": 8, "base_int": 12, "base_hp": 360, "base_ap": 12,
  "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 3},

 # min_spawn_level == 26
 {"id": "storm_caller", "name": "Storm Caller", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 26, "rarity": "uncommon", "base_xp": 440,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 300),
  "basic_attack": "storm bolt", "strong_attack": "tempest call",
  "player_abilities": ["electric_magic_lv1_fireball", "electric_fire_magic_lv2_arclance"],
  "base_str": 4, "base_dex": 10, "base_con": 6, "base_int": 20, "base_hp": 280, "base_ap": 18,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 5},

 # min_spawn_level == 30
 {"id": "thunder_warlord", "name": "Thunder Warlord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 30, "rarity": "rare", "base_xp": 900,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (300, 1000),
  "basic_attack": "thunder cleave", "strong_attack": "storm war cry",
  "player_abilities": ["level_1_hostile_ability_inspire", "electric_fire_magic_lv2_arclance"],
  "base_str": 24, "base_dex": 12, "base_con": 22, "base_int": 8, "base_hp": 700, "base_ap": 12,
  "str_per_level": 5, "dex_per_level": 2, "con_per_level": 4, "int_per_level": 1},

 # min_spawn_level == 38
 {"id": "tempest_colossus", "name": "Tempest Colossus", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 38, "rarity": "rare", "base_xp": 1200,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (100, 400),
  "basic_attack": "tempest slam", "strong_attack": "storm obliteration",
  "player_abilities": ["electric_electric_magic_lv2_chain_bolt"],
  "base_str": 30, "base_dex": 8, "base_con": 28, "base_int": 10, "base_hp": 1400, "base_ap": 12,
  "str_per_level": 6, "dex_per_level": 1, "con_per_level": 5, "int_per_level": 2},

 # min_spawn_level == 55
 {"id": "plains_lich", "name": "Plains Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 55, "rarity": "superrare", "base_xp": 6000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (1200, 4000),
  "basic_attack": "plains death bolt", "strong_attack": "lich plains storm",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 10, "base_dex": 12, "base_con": 12, "base_int": 52, "base_hp": 2000, "base_ap": 44,
  "str_per_level": 1, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 11},

 # min_spawn_level == 80
 {"id": "plains_god_avatar", "name": "Plains God Avatar", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 80, "rarity": "superrare", "base_xp": 28000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (8000, 26000),
  "basic_attack": "divine storm", "strong_attack": "plains god's wrath",
  "player_abilities": ["electric_electric_electric_magic_lv3_thunderstorm"],
  "base_str": 46, "base_dex": 28, "base_con": 46, "base_int": 110, "base_hp": 44000, "base_ap": 90,
  "str_per_level": 9, "dex_per_level": 5, "con_per_level": 9, "int_per_level": 22},

 # min_spawn_level == 100
 {"id": "grassland_world_god", "name": "The Grassland World God", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 120000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (50000, 160000),
  "basic_attack": "world storm decree", "strong_attack": "plains world end",
  "player_abilities": ["electric_electric_electric_magic_lv3_thunderstorm", "air_air_air_magic_lv3_storm_surge"],
  "base_str": 140, "base_dex": 32, "base_con": 132, "base_int": 36, "base_hp": 100000, "base_ap": 28,
  "str_per_level": 28, "dex_per_level": 6, "con_per_level": 26, "int_per_level": 7},
]
