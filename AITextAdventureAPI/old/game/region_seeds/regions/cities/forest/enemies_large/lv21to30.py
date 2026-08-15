# Forest Large City (Aurelion Veil) � hostile seeds levels 21-30.
# Forest Large City (Aurelion Veil) — hostile seeds levels 21–30.

RANDOM_HOSTILE_SEEDS = [
 {"id": "thornwood_champion", "name": "Thornwood Champion", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 280,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (60, 200),
  "basic_attack": "thornwood slash", "strong_attack": "briar cleave",
  "player_abilities": [],
  "base_str": 12, "base_dex": 10, "base_con": 10, "base_int": 4, "base_hp": 320, "base_ap": 10,
  "str_per_level": 3, "dex_per_level": 2, "con_per_level": 2, "int_per_level": 0},
 {"id": "forest_revenant_lg", "name": "Forest Revenant", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 360,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "necrotic grasp", "strong_attack": "revenant wail",
  "player_abilities": ["level_1_hostile_ability_bone_spear"],
  "base_str": 10, "base_dex": 8, "base_con": 8, "base_int": 12, "base_hp": 360, "base_ap": 12,
  "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 3},
 {"id": "bark_golem_lg", "name": "Bark Golem", "hostile_type": "elemental", "role": "damage", "min_spawn_level": 24, "rarity": "uncommon", "base_xp": 380,
  "common_drop": None, "rare_drop": "herb_major", "money_range": (0, 20),
  "basic_attack": "bark slam", "strong_attack": "root crush",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 16, "base_dex": 2, "base_con": 14, "base_int": 4, "base_hp": 440, "base_ap": 6,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 3, "int_per_level": 0},
 {"id": "fey_warlock", "name": "Fey Warlock", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 27, "rarity": "uncommon", "base_xp": 420,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (80, 280),
  "basic_attack": "fey bolt", "strong_attack": "warlock hex",
  "player_abilities": ["air_magic_lv1_shredding_gust", "air_dark_magic_lv2_night_wind"],
  "base_str": 4, "base_dex": 10, "base_con": 6, "base_int": 18, "base_hp": 280, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},
]
