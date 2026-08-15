# LEVEL 21-30 hostile regional (desert overworld).

SEEDS_LV21TO30 = [

 # min_spawn_level == 21
 {"id": "sand_colossus", "name": "Sand Colossus", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 400,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (10, 60),
  "basic_attack": "colossal slam", "strong_attack": "sand deluge",
  "player_abilities": ["earth_magic_lv1_tremor"],
  "base_str": 16, "base_dex": 2, "base_con": 14, "base_int": 4, "base_hp": 440, "base_ap": 6,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 3, "int_per_level": 0},

 {"id": "dune_pioneer", "name": "Dune Pioneer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 240,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (60, 200),
  "basic_attack": "pioneer strike", "strong_attack": "frontier charge",
  "player_abilities": [],
  "base_str": 12, "base_dex": 10, "base_con": 10, "base_int": 4, "base_hp": 320, "base_ap": 10,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},

 # min_spawn_level == 23
 {"id": "sand_raven", "name": "Sand Raven", "hostile_type": "creature", "role": "damage", "min_spawn_level": 23, "rarity": "common", "base_xp": 260,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (5, 30),
  "basic_attack": "talon rake", "strong_attack": "dive bomb",
  "player_abilities": [],
  "base_str": 10, "base_dex": 16, "base_con": 8, "base_int": 4, "base_hp": 280, "base_ap": 12,
  "str_per_level": 2, "dex_per_level": 3, "con_per_level": 1, "int_per_level": 0},

 {"id": "mirage_witch", "name": "Mirage Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 23, "rarity": "uncommon", "base_xp": 400,
  "common_drop": "tome_int", "rare_drop": None, "money_range": (80, 300),
  "basic_attack": "illusion bolt", "strong_attack": "desert mirage hex",
  "player_abilities": ["level_1_hostile_ability_dark_magic_daze_whisper", "earth_water_magic_lv2_mudslide"],
  "base_str": 4, "base_dex": 8, "base_con": 6, "base_int": 16, "base_hp": 260, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},

 # min_spawn_level == 25
 {"id": "dune_warden", "name": "Dune Warden", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 25, "rarity": "uncommon", "base_xp": 380,
  "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (120, 400),
  "basic_attack": "warden's spear", "strong_attack": "guardian sweep",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 16, "base_dex": 10, "base_con": 14, "base_int": 6, "base_hp": 420, "base_ap": 10,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 1},

 # min_spawn_level == 27
 {"id": "sand_howler", "name": "Sand Howler", "hostile_type": "creature", "role": "damage", "min_spawn_level": 27, "rarity": "uncommon", "base_xp": 380,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (10, 50),
  "basic_attack": "sand howl lunge", "strong_attack": "pack fury",
  "player_abilities": [],
  "base_str": 14, "base_dex": 16, "base_con": 12, "base_int": 4, "base_hp": 380, "base_ap": 12,
  "str_per_level": 3, "dex_per_level": 3, "con_per_level": 2, "int_per_level": 0},

 # min_spawn_level == 29
 {"id": "auric_stela", "name": "Auric Stela", "hostile_type": "construct", "role": "hazard", "min_spawn_level": 29, "rarity": "rare", "base_xp": 700,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 30),
  "basic_attack": "cursed beam", "strong_attack": "auric curse wave",
  "player_abilities": ["light_magic_lv1_luminous_spike", "fire_light_magic_lv2_solar_spike"],
  "base_str": 8, "base_dex": 6, "base_con": 10, "base_int": 20, "base_hp": 500, "base_ap": 18,
  "str_per_level": 1, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 5},

 # min_spawn_level == 30
 {"id": "dune_emperor", "name": "Dune Emperor", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 30, "rarity": "superrare", "base_xp": 1400,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (300, 1000),
  "basic_attack": "emperor's decree", "strong_attack": "imperial devastation",
  "player_abilities": ["level_1_hostile_ability_inspire", "fire_technique_lv1_scorch_slash"],
  "base_str": 22, "base_dex": 12, "base_con": 20, "base_int": 8, "base_hp": 800, "base_ap": 12,
  "str_per_level": 5, "dex_per_level": 2, "con_per_level": 4, "int_per_level": 1},
]