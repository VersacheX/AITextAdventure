# Desert Large City — hostile seeds levels 31-40 (Great Dune City elite tier).
# Threats scale into hardened veterans, occult warlords, and apex desert beasts.

RANDOM_HOSTILE_SEEDS = [

 # min_spawn_level == 31
 {"id": "dune_warlord", "name": "Dune Warlord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 320,
  "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (60, 220),
  "basic_attack": "war-hammer blow", "strong_attack": "sand-storm cleave",
  "player_abilities": ["level_1_hostile_ability_inspire", "fire_technique_lv1_scorch_slash"],
  "base_str": 14, "base_dex": 5, "base_con": 12, "base_int": 4, "base_hp": 280, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 1},

 {"id": "sand_banshee", "name": "Sand Banshee", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 380,
  "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (20, 100),
  "basic_attack": "wailing screech", "strong_attack": "soul-rend wail",
  "player_abilities": ["level_1_hostile_ability_night_whisper", "dark_magic_lv1_shadow_tendril"],
  "base_str": 3, "base_dex": 10, "base_con": 5, "base_int": 16, "base_hp": 200, "base_ap": 14,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 4},

 # min_spawn_level == 32
 {"id": "scorpion_titan", "name": "Scorpion Titan", "hostile_type": "creature", "role": "damage", "min_spawn_level": 32, "rarity": "rare", "base_xp": 520,
  "common_drop": "ointment", "rare_drop": "stimulant_large", "money_range": (10, 60),
  "basic_attack": "crushing claw", "strong_attack": "venomous tail slam",
  "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
  "base_str": 18, "base_dex": 4, "base_con": 16, "base_int": 2, "base_hp": 420, "base_ap": 6,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 3, "int_per_level": 0},

 {"id": "mirage_assassin", "name": "Mirage Assassin", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 32, "rarity": "uncommon", "base_xp": 400,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (80, 280),
  "basic_attack": "phantom blade", "strong_attack": "illusory decapitation",
  "player_abilities": ["level_1_hostile_ability_shadow_flicker", "dark_skill_lv1_creeping_strike"],
  "base_str": 10, "base_dex": 18, "base_con": 8, "base_int": 6, "base_hp": 260, "base_ap": 14,
  "str_per_level": 2, "dex_per_level": 4, "con_per_level": 1, "int_per_level": 1},

 # min_spawn_level == 33
 {"id": "tomb_revenant", "name": "Tomb Revenant", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 33, "rarity": "rare", "base_xp": 600,
  "common_drop": "herb_major", "rare_drop": "tome_con", "money_range": (30, 130),
  "basic_attack": "necrotic fist", "strong_attack": "death grasp",
  "player_abilities": ["level_1_hostile_ability_bone_spear", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 16, "base_dex": 6, "base_con": 14, "base_int": 8, "base_hp": 500, "base_ap": 10,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 2},

 {"id": "brass_golem", "name": "Brass Golem", "hostile_type": "construct", "role": "damage", "min_spawn_level": 33, "rarity": "uncommon", "base_xp": 460,
  "common_drop": None, "rare_drop": "kevlar_vest", "money_range": (0, 40),
  "basic_attack": "brass fist", "strong_attack": "steam-powered stomp",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 20, "base_dex": 2, "base_con": 18, "base_int": 2, "base_hp": 560, "base_ap": 4,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 4, "int_per_level": 0},

 # min_spawn_level == 34
 {"id": "glass_hydra", "name": "Glass Hydra", "hostile_type": "creature", "role": "damage", "min_spawn_level": 34, "rarity": "superrare", "base_xp": 1400,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (50, 200),
  "basic_attack": "multi-head bite", "strong_attack": "venom torrent",
  "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit", "fire_magic_lv1_fireball"],
  "base_str": 22, "base_dex": 6, "base_con": 20, "base_int": 4, "base_hp": 800, "base_ap": 8,
  "str_per_level": 5, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 0},

 {"id": "cursed_dune_priest", "name": "Cursed Dune Priest", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 34, "rarity": "rare", "base_xp": 700,
  "common_drop": "tome_int", "rare_drop": "stimulant_large", "money_range": (60, 240),
  "basic_attack": "hex bolt", "strong_attack": "blasphemous rite",
  "player_abilities": ["dark_faith_lv1_shade_whisper", "earth_water_magic_lv2_mudslide"],
  "base_str": 5, "base_dex": 6, "base_con": 7, "base_int": 20, "base_hp": 300, "base_ap": 18,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 5},

 # min_spawn_level == 35
 {"id": "dune_colossus_brute", "name": "Dune Colossus Brute", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 35, "rarity": "uncommon", "base_xp": 560,
  "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (100, 360),
  "basic_attack": "boulder toss", "strong_attack": "colossus smash",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 24, "base_dex": 3, "base_con": 22, "base_int": 2, "base_hp": 640, "base_ap": 6,
  "str_per_level": 5, "dex_per_level": 0, "con_per_level": 4, "int_per_level": 0},

 {"id": "obsidian_witch", "name": "Obsidian Witch", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 35, "rarity": "rare", "base_xp": 820,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 300),
  "basic_attack": "dark hex", "strong_attack": "obsidian curse",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_fire_ice_magic_lv3_flame_wraith"],
  "base_str": 4, "base_dex": 8, "base_con": 6, "base_int": 24, "base_hp": 340, "base_ap": 20,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 6},

 # min_spawn_level == 36
 {"id": "gilded_enforcer", "name": "Gilded Enforcer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 36, "rarity": "common", "base_xp": 480,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (120, 400),
  "basic_attack": "pommel strike", "strong_attack": "gilded smash",
  "player_abilities": [],
  "base_str": 18, "base_dex": 8, "base_con": 16, "base_int": 4, "base_hp": 480, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 1},

 {"id": "sand_elemental", "name": "Sand Elemental", "hostile_type": "elemental", "role": "hazard", "min_spawn_level": 36, "rarity": "uncommon", "base_xp": 580,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (0, 20),
  "basic_attack": "sand blast", "strong_attack": "abrasive storm",
  "player_abilities": ["earth_magic_lv1_tremor", "earth_earth_magic_lv2_quake_field"],
  "base_str": 12, "base_dex": 10, "base_con": 14, "base_int": 10, "base_hp": 440, "base_ap": 12,
  "str_per_level": 2, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 2},

 # min_spawn_level == 37
 {"id": "fallen_dune_knight", "name": "Fallen Dune Knight", "hostile_type": "undead", "role": "damage", "min_spawn_level": 37, "rarity": "uncommon", "base_xp": 640,
  "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (60, 200),
  "basic_attack": "spectral lance", "strong_attack": "death charge",
  "player_abilities": ["level_1_hostile_ability_bone_spear"],
  "base_str": 20, "base_dex": 8, "base_con": 18, "base_int": 6, "base_hp": 560, "base_ap": 10,
  "str_per_level": 4, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 1},

 {"id": "black_market_viper", "name": "Black Market Viper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 37, "rarity": "common", "base_xp": 420,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (140, 480),
  "basic_attack": "shiv strike", "strong_attack": "poisoned ambush",
  "player_abilities": ["level_1_hostile_ability_poison_dart", "dark_skill_lv1_creeping_strike"],
  "base_str": 12, "base_dex": 20, "base_con": 10, "base_int": 8, "base_hp": 360, "base_ap": 14,
  "str_per_level": 2, "dex_per_level": 4, "con_per_level": 2, "int_per_level": 1},

 # min_spawn_level == 38
 {"id": "solar_golem", "name": "Solar Golem", "hostile_type": "construct", "role": "damage", "min_spawn_level": 38, "rarity": "rare", "base_xp": 900,
  "common_drop": None, "rare_drop": "tome_int", "money_range": (0, 50),
  "basic_attack": "solar punch", "strong_attack": "radiant beam",
  "player_abilities": ["light_magic_lv1_luminous_spike", "fire_light_magic_lv2_solar_spike"],
  "base_str": 22, "base_dex": 4, "base_con": 20, "base_int": 12, "base_hp": 700, "base_ap": 14,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 4, "int_per_level": 3},

 {"id": "void_jackal", "name": "Void Jackal", "hostile_type": "creature", "role": "damage", "min_spawn_level": 38, "rarity": "uncommon", "base_xp": 520,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 90),
  "basic_attack": "void bite", "strong_attack": "phase lunge",
  "player_abilities": ["level_1_hostile_ability_shadow_flicker"],
  "base_str": 14, "base_dex": 22, "base_con": 12, "base_int": 8, "base_hp": 400, "base_ap": 16,
  "str_per_level": 2, "dex_per_level": 4, "con_per_level": 2, "int_per_level": 2},

 # min_spawn_level == 39
 {"id": "dune_lich", "name": "Dune Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 39, "rarity": "superrare", "base_xp": 2200,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (200, 700),
  "basic_attack": "death bolt", "strong_attack": "lich wail",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 8, "base_dex": 10, "base_con": 10, "base_int": 30, "base_hp": 600, "base_ap": 24,
  "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 7},

 # min_spawn_level == 40
 {"id": "desert_dragon_whelp", "name": "Desert Dragon Whelp", "hostile_type": "creature", "role": "damage", "min_spawn_level": 40, "rarity": "superrare", "base_xp": 2800,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (250, 900),
  "basic_attack": "claw rake", "strong_attack": "flame breath",
  "player_abilities": ["fire_magic_lv1_fireball", "fire_fire_magic_lv2_inferno_spread"],
  "base_str": 28, "base_dex": 12, "base_con": 26, "base_int": 10, "base_hp": 1200, "base_ap": 12,
  "str_per_level": 6, "dex_per_level": 2, "con_per_level": 5, "int_per_level": 2},
]
