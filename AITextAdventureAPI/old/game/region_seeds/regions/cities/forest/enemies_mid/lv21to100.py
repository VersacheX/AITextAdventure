# Forest Mid City — hostile seeds levels 21-100.

RANDOM_HOSTILE_SEEDS = [

 # min_spawn_level == 21
 {"id": "guild_enforcer_forest", "name": "Guild Enforcer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 260,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (60, 200),
  "basic_attack": "guild punch", "strong_attack": "enforcer rush",
  "player_abilities": [],
  "base_str": 12, "base_dex": 8, "base_con": 10, "base_int": 4, "base_hp": 300, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 0},

 {"id": "forest_shade_mid", "name": "Forest Shade", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 320,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "shade touch", "strong_attack": "forest whisper",
  "player_abilities": ["level_1_hostile_ability_night_whisper"],
  "base_str": 4, "base_dex": 12, "base_con": 6, "base_int": 14, "base_hp": 280, "base_ap": 14,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 3},

 # min_spawn_level == 25
 {"id": "thorn_berserker", "name": "Thorn Berserker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 25, "rarity": "common", "base_xp": 340,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (80, 280),
  "basic_attack": "thorn bash", "strong_attack": "briar fury",
  "player_abilities": [],
  "base_str": 16, "base_dex": 8, "base_con": 14, "base_int": 3, "base_hp": 380, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},

 # min_spawn_level == 30
 {"id": "canopy_crime_lord", "name": "Canopy Crime Lord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 30, "rarity": "rare", "base_xp": 800,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (300, 1000),
  "basic_attack": "lord's blade", "strong_attack": "canopy decree",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 22, "base_dex": 14, "base_con": 20, "base_int": 8, "base_hp": 620, "base_ap": 12,
  "str_per_level": 4, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 1},

 # min_spawn_level == 38
 {"id": "elder_bark_golem", "name": "Elder Bark Golem", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 38, "rarity": "rare", "base_xp": 1000,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 40),
  "basic_attack": "elder bark fist", "strong_attack": "canopy stomp",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame", "earth_magic_lv1_tremor"],
  "base_str": 30, "base_dex": 2, "base_con": 28, "base_int": 6, "base_hp": 1000, "base_ap": 8,
  "str_per_level": 6, "dex_per_level": 0, "con_per_level": 5, "int_per_level": 1},

 # min_spawn_level == 50
 {"id": "twilight_beast", "name": "Twilight Beast", "hostile_type": "creature", "role": "damage", "min_spawn_level": 50, "rarity": "superrare", "base_xp": 4500,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (800, 2800),
  "basic_attack": "twilight lunge", "strong_attack": "dusk maul",
  "player_abilities": ["dark_magic_lv1_shadow_tendril"],
  "base_str": 44, "base_dex": 18, "base_con": 40, "base_int": 8, "base_hp": 3200, "base_ap": 12,
  "str_per_level": 9, "dex_per_level": 3, "con_per_level": 8, "int_per_level": 1},

 # min_spawn_level == 75
 {"id": "forest_god_avatar", "name": "Forest God Avatar", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 75, "rarity": "superrare", "base_xp": 20000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (6000, 20000),
  "basic_attack": "divine root", "strong_attack": "forest god's wrath",
  "player_abilities": ["earth_earth_earth_magic_lv3_earthshaker"],
  "base_str": 44, "base_dex": 24, "base_con": 44, "base_int": 100, "base_hp": 40000, "base_ap": 80,
  "str_per_level": 8, "dex_per_level": 4, "con_per_level": 8, "int_per_level": 20},

 # min_spawn_level == 100
 {"id": "canopy_world_god", "name": "The Canopy World God", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 100000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40000, 130000),
  "basic_attack": "canopy decree", "strong_attack": "forest world end",
  "player_abilities": ["earth_earth_earth_magic_lv3_earthshaker", "air_air_air_magic_lv3_storm_surge"],
  "base_str": 28, "base_dex": 36, "base_con": 28, "base_int": 150, "base_hp": 80000, "base_ap": 120,
  "str_per_level": 5, "dex_per_level": 7, "con_per_level": 5, "int_per_level": 30},
]
