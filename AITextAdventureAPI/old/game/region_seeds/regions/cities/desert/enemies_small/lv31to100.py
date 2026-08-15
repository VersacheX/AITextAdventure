# Desert Small City (BioHazard) — hostile seeds levels 31-100 (elite to apex).

RANDOM_HOSTILE_SEEDS = [

 # min_spawn_level == 31
 {"id": "rust_berserker", "name": "Rust Berserker", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 31, "rarity": "common", "base_xp": 320,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (80, 280),
  "basic_attack": "rusted cleave", "strong_attack": "berserker rush",
  "player_abilities": [],
  "base_str": 16, "base_dex": 8, "base_con": 14, "base_int": 2, "base_hp": 360, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},

 {"id": "toxic_specter", "name": "Toxic Specter", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 380,
  "common_drop": "ointment", "rare_drop": "herb_major", "money_range": (30, 120),
  "basic_attack": "toxic touch", "strong_attack": "poison mist",
  "player_abilities": ["level_1_hostile_ability_poison_dart", "level_1_hostile_ability_night_whisper"],
  "base_str": 4, "base_dex": 12, "base_con": 6, "base_int": 16, "base_hp": 280, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 4},

 # min_spawn_level == 34
 {"id": "chrome_hound", "name": "Chrome Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level": 34, "rarity": "uncommon", "base_xp": 440,
  "common_drop": None, "rare_drop": "stimulant_large", "money_range": (10, 60),
  "basic_attack": "chrome bite", "strong_attack": "pack lunge",
  "player_abilities": [],
  "base_str": 18, "base_dex": 14, "base_con": 16, "base_int": 4, "base_hp": 440, "base_ap": 10,
  "str_per_level": 4, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 0},

 # min_spawn_level == 37
 {"id": "wasteland_warlord", "name": "Wasteland Warlord", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 37, "rarity": "rare", "base_xp": 700,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (200, 700),
  "basic_attack": "warlord bash", "strong_attack": "wasteland conquest",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 24, "base_dex": 10, "base_con": 22, "base_int": 6, "base_hp": 680, "base_ap": 10,
  "str_per_level": 5, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 1},

 # min_spawn_level == 40
 {"id": "scrap_titan", "name": "Scrap Titan", "hostile_type": "construct", "role": "damage", "min_spawn_level": 40, "rarity": "superrare", "base_xp": 1800,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 50),
  "basic_attack": "titan crush", "strong_attack": "scrap apocalypse",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 32, "base_dex": 2, "base_con": 28, "base_int": 2, "base_hp": 1200, "base_ap": 6,
  "str_per_level": 6, "dex_per_level": 0, "con_per_level": 5, "int_per_level": 0},

 # min_spawn_level == 45
 {"id": "biohazard_lich", "name": "Biohazard Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 45, "rarity": "superrare", "base_xp": 3000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (400, 1400),
  "basic_attack": "toxic death bolt", "strong_attack": "biohazard death wave",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 8, "base_dex": 8, "base_con": 8, "base_int": 32, "base_hp": 800, "base_ap": 28,
  "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 7},

 # min_spawn_level == 50
 {"id": "irradiated_behemoth", "name": "Irradiated Behemoth", "hostile_type": "creature", "role": "damage", "min_spawn_level": 50, "rarity": "superrare", "base_xp": 4500,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (500, 1800),
  "basic_attack": "irradiated slam", "strong_attack": "behemoth quake",
  "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
  "base_str": 44, "base_dex": 6, "base_con": 40, "base_int": 4, "base_hp": 3000, "base_ap": 8,
  "str_per_level": 9, "dex_per_level": 1, "con_per_level": 8, "int_per_level": 0},

 # min_spawn_level == 60
 {"id": "void_machine_god", "name": "Void Machine God", "hostile_type": "construct", "role": "hazard", "min_spawn_level": 60, "rarity": "superrare", "base_xp": 8000,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (1200, 4000),
  "basic_attack": "machine hex", "strong_attack": "omnidestruction burst",
  "player_abilities": ["level_1_hostile_ability_electric_tech_hack_overload", "electric_electric_magic_lv2_chain_bolt"],
  "base_str": 54, "base_dex": 6, "base_con": 50, "base_int": 22, "base_hp": 7000, "base_ap": 14,
  "str_per_level": 11, "dex_per_level": 1, "con_per_level": 10, "int_per_level": 4},

 {"id": "wasteland_ironskin_brute", "name": "Wasteland Ironskin Brute", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 53, "rarity": "rare", "base_xp": 3500,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (700, 2400),
  "basic_attack": "ironskin bash", "strong_attack": "wasteland surge",
  "player_abilities": [],
  "base_str": 44, "base_dex": 8, "base_con": 40, "base_int": 4, "base_hp": 3200, "base_ap": 8,
  "str_per_level": 9, "dex_per_level": 1, "con_per_level": 8, "int_per_level": 0},

 {"id": "scrap_necromancer", "name": "Scrap Necromancer", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 62, "rarity": "rare", "base_xp": 5000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (800, 2800),
  "basic_attack": "death weld", "strong_attack": "undead parts barrage",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 10, "base_dex": 10, "base_con": 12, "base_int": 46, "base_hp": 2400, "base_ap": 40,
  "str_per_level": 1, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 10},

 {"id": "toxic_wasteland_titan", "name": "Toxic Wasteland Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 67, "rarity": "superrare", "base_xp": 11000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (3000, 10000),
  "basic_attack": "toxic titan slam", "strong_attack": "biohazard shockwave",
  "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
  "base_str": 64, "base_dex": 10, "base_con": 58, "base_int": 10, "base_hp": 11000, "base_ap": 10,
  "str_per_level": 13, "dex_per_level": 1, "con_per_level": 12, "int_per_level": 2},

 # min_spawn_level == 75
 {"id": "wasteland_god_beast", "name": "Wasteland God Beast", "hostile_type": "creature", "role": "damage", "min_spawn_level": 75, "rarity": "superrare", "base_xp": 18000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (5000, 17000),
  "basic_attack": "god beast maul", "strong_attack": "wasteland extinction",
  "player_abilities": None,
  "base_str": 90, "base_dex": 20, "base_con": 84, "base_int": 8, "base_hp": 22000, "base_ap": 12,
  "str_per_level": 18, "dex_per_level": 3, "con_per_level": 17, "int_per_level": 1},

 {"id": "irradiated_lich", "name": "Irradiated Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 78, "rarity": "superrare", "base_xp": 20000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (7000, 24000),
  "basic_attack": "irradiated death bolt", "strong_attack": "lich meltdown",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 12, "base_dex": 14, "base_con": 14, "base_int": 76, "base_hp": 10000, "base_ap": 62,
  "str_per_level": 2, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 16},

 # min_spawn_level == 82
 {"id": "rad_titan", "name": "Rad Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 82, "rarity": "superrare", "base_xp": 30000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (10000, 35000),
  "basic_attack": "radiation fist", "strong_attack": "nuclear pulse",
  "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
  "base_str": 100, "base_dex": 12, "base_con": 96, "base_int": 14, "base_hp": 36000, "base_ap": 14,
  "str_per_level": 20, "dex_per_level": 2, "con_per_level": 19, "int_per_level": 2},

 {"id": "apocalypse_scavenger", "name": "Apocalypse Scavenger", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 86, "rarity": "superrare", "base_xp": 38000,
  "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (12000, 40000),
  "basic_attack": "end-times slash", "strong_attack": "apocalypse harvest",
  "player_abilities": ["level_1_hostile_ability_inspire"],
  "base_str": 108, "base_dex": 24, "base_con": 102, "base_int": 16, "base_hp": 40000, "base_ap": 16,
  "str_per_level": 21, "dex_per_level": 4, "con_per_level": 20, "int_per_level": 3},

 # min_spawn_level == 100
 {"id": "biohazard_god", "name": "The Biohazard God", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 100, "rarity": "superrare", "base_xp": 90000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (30000, 100000),
  "basic_attack": "toxic mandate", "strong_attack": "biohazard apocalypse",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 24, "base_dex": 28, "base_con": 26, "base_int": 130, "base_hp": 70000, "base_ap": 110,
  "str_per_level": 4, "dex_per_level": 5, "con_per_level": 4, "int_per_level": 26},

 {"id": "biohazard_apex_titan", "name": "Biohazard Apex Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 94, "rarity": "superrare", "base_xp": 45000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (16000, 54000),
  "basic_attack": "apex rad slam", "strong_attack": "biohazard world collapse",
  "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
  "base_str": 114, "base_dex": 14, "base_con": 108, "base_int": 16, "base_hp": 66000, "base_ap": 14,
  "str_per_level": 23, "dex_per_level": 2, "con_per_level": 22, "int_per_level": 3},
]
