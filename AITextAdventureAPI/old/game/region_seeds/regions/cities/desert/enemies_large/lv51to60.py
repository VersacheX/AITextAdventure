# Desert Large City — hostile seeds levels 51-60 (legendary threats).

RANDOM_HOSTILE_SEEDS = [

 # min_spawn_level == 51
 {"id": "fallen_sun_paladin", "name": "Fallen Sun Paladin", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 51, "rarity": "uncommon", "base_xp": 1400,
  "common_drop": "kevlar_vest", "rare_drop": "stimulant_large", "money_range": (280, 900),
  "basic_attack": "corrupted holy slash", "strong_attack": "judgment of the fallen",
  "player_abilities": ["light_technique_lv1_radiant_slash", "fire_light_magic_lv2_solar_spike"],
  "base_str": 32, "base_dex": 12, "base_con": 28, "base_int": 12, "base_hp": 1200, "base_ap": 14,
  "str_per_level": 6, "dex_per_level": 2, "con_per_level": 5, "int_per_level": 2},

 {"id": "elder_void_spider", "name": "Elder Void Spider", "hostile_type": "creature", "role": "hazard", "min_spawn_level": 51, "rarity": "rare", "base_xp": 1600,
  "common_drop": "ointment", "rare_drop": "herb_major", "money_range": (60, 250),
  "basic_attack": "elder fang", "strong_attack": "void web",
  "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 10, "base_dex": 32, "base_con": 12, "base_int": 22, "base_hp": 800, "base_ap": 28,
  "str_per_level": 1, "dex_per_level": 6, "con_per_level": 2, "int_per_level": 5},

 # min_spawn_level == 52
 {"id": "obsidian_giant", "name": "Obsidian Giant", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 52, "rarity": "rare", "base_xp": 2000,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 80),
  "basic_attack": "obsidian slam", "strong_attack": "volcanic eruption",
  "player_abilities": ["fire_magic_lv1_fireball", "fire_earth_magic_lv2_magma_javelin", "dark_earth_fire_technique_lv3_oblivion_burn_strike"],
  "base_str": 46, "base_dex": 4, "base_con": 42, "base_int": 6, "base_hp": 2800, "base_ap": 8,
  "str_per_level": 9, "dex_per_level": 0, "con_per_level": 8, "int_per_level": 1},

 # min_spawn_level == 53
 {"id": "abyssal_cultist_lord", "name": "Abyssal Cultist Lord", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 53, "rarity": "rare", "base_xp": 2200,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (400, 1400),
  "basic_attack": "ritual hex", "strong_attack": "abyssal summoning",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 8, "base_dex": 12, "base_con": 10, "base_int": 44, "base_hp": 900, "base_ap": 36,
  "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 10},

 # min_spawn_level == 54
 {"id": "gilded_dragon_cult", "name": "Gilded Dragon Cultist", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level": 54, "rarity": "uncommon", "base_xp": 1600,
  "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (320, 1000),
  "basic_attack": "cultist blade", "strong_attack": "dragon rite",
  "player_abilities": ["fire_magic_lv1_fireball", "fire_fire_magic_lv2_inferno_spread"],
  "base_str": 18, "base_dex": 14, "base_con": 18, "base_int": 30, "base_hp": 900, "base_ap": 26,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 7},

 # min_spawn_level == 55
 {"id": "dune_wraith_lord", "name": "Dune Wraith Lord", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 55, "rarity": "superrare", "base_xp": 5500,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (700, 2500),
  "basic_attack": "wraith rend", "strong_attack": "soul storm",
  "player_abilities": ["level_1_hostile_ability_night_whisper", "dark_dark_magic_lv2_umbra_storm", "dark_dark_dark_magic_lv3_shadow_blast"],
  "base_str": 14, "base_dex": 18, "base_con": 16, "base_int": 48, "base_hp": 2000, "base_ap": 40,
  "str_per_level": 2, "dex_per_level": 3, "con_per_level": 2, "int_per_level": 10},

 # min_spawn_level == 56
 {"id": "chrome_scorpion", "name": "Chrome Scorpion", "hostile_type": "construct", "role": "damage", "min_spawn_level": 56, "rarity": "uncommon", "base_xp": 1800,
  "common_drop": None, "rare_drop": "kevlar_vest", "money_range": (0, 60),
  "basic_attack": "chrome claw", "strong_attack": "bio-acid spray",
  "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
  "base_str": 36, "base_dex": 14, "base_con": 32, "base_int": 8, "base_hp": 2000, "base_ap": 10,
  "str_per_level": 7, "dex_per_level": 2, "con_per_level": 6, "int_per_level": 1},

 # min_spawn_level == 57
 {"id": "storm_sorcerer", "name": "Storm Sorcerer", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 57, "rarity": "rare", "base_xp": 2400,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (450, 1600),
  "basic_attack": "lightning finger", "strong_attack": "tempest nova",
  "player_abilities": ["electric_magic_lv1_fireball", "electric_electric_magic_lv2_chain_bolt", "electric_electric_electric_magic_lv3_thunderstorm"],
  "base_str": 8, "base_dex": 14, "base_con": 10, "base_int": 50, "base_hp": 1100, "base_ap": 42,
  "str_per_level": 1, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 11},

 # min_spawn_level == 58
 {"id": "sand_titan", "name": "Sand Titan", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 58, "rarity": "rare", "base_xp": 2800,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (200, 700),
  "basic_attack": "titan's grip", "strong_attack": "sandstorm barrage",
  "player_abilities": None,
  "base_str": 50, "base_dex": 6, "base_con": 46, "base_int": 4, "base_hp": 3800, "base_ap": 8,
  "str_per_level": 10, "dex_per_level": 1, "con_per_level": 9, "int_per_level": 0},

 # min_spawn_level == 59
 {"id": "mind_devourer", "name": "Mind Devourer", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 59, "rarity": "superrare", "base_xp": 6000,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (800, 2800),
  "basic_attack": "psychic lance", "strong_attack": "mind consume",
  "player_abilities": ["level_1_hostile_ability_dark_magic_daze_whisper", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 6, "base_dex": 18, "base_con": 10, "base_int": 54, "base_hp": 1800, "base_ap": 46,
  "str_per_level": 0, "dex_per_level": 3, "con_per_level": 1, "int_per_level": 12},

 # min_spawn_level == 60
 {"id": "desert_abomination", "name": "Desert Abomination", "hostile_type": "eldritch", "role": "damage", "min_spawn_level": 60, "rarity": "superrare", "base_xp": 8000,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (1000, 3500),
  "basic_attack": "crushing appendage", "strong_attack": "abomination wave",
  "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit", "dark_water_fire_magic_lv3_abyssal_flame"],
  "base_str": 56, "base_dex": 8, "base_con": 52, "base_int": 14, "base_hp": 5000, "base_ap": 12,
  "str_per_level": 11, "dex_per_level": 1, "con_per_level": 10, "int_per_level": 2},
]
