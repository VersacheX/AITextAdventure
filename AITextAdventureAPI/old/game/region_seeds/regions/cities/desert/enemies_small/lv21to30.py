# Desert Small City (BioHazard) — hostile seeds levels 21-30.

RANDOM_HOSTILE_SEEDS = [

 # min_spawn_level == 21
 {"id": "wasteland_wrecker_elite", "name": "Wasteland Wrecker Elite", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 21, "rarity": "common", "base_xp": 220,
  "common_drop": "stimulant_large", "rare_drop": None, "money_range": (40, 160),
  "basic_attack": "scrap maul", "strong_attack": "wasteland rampage",
  "player_abilities": [],
  "base_str": 12, "base_dex": 6, "base_con": 10, "base_int": 3, "base_hp": 260, "base_ap": 8,
  "str_per_level": 3, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 0},

 {"id": "scrap_revenant", "name": "Scrap Revenant", "hostile_type": "undead", "role": "hazard", "min_spawn_level": 21, "rarity": "uncommon", "base_xp": 300,
  "common_drop": "herb_major", "rare_drop": None, "money_range": (20, 80),
  "basic_attack": "rusted claws", "strong_attack": "undead surge",
  "player_abilities": ["level_1_hostile_ability_bone_spear"],
  "base_str": 10, "base_dex": 6, "base_con": 8, "base_int": 8, "base_hp": 300, "base_ap": 10,
  "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 2},

 # min_spawn_level == 23
 {"id": "junk_golem", "name": "Junk Golem", "hostile_type": "construct", "role": "damage", "min_spawn_level": 23, "rarity": "uncommon", "base_xp": 340,
  "common_drop": None, "rare_drop": "kevlar_vest", "money_range": (0, 20),
  "basic_attack": "scrap fist", "strong_attack": "debris crush",
  "player_abilities": ["level_1_hostile_ability_reinforce_frame"],
  "base_str": 16, "base_dex": 2, "base_con": 14, "base_int": 2, "base_hp": 360, "base_ap": 4,
  "str_per_level": 4, "dex_per_level": 0, "con_per_level": 3, "int_per_level": 0},

 # min_spawn_level == 25
 {"id": "mad_mechanic_prime", "name": "Mad Mechanic Prime", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level": 25, "rarity": "uncommon", "base_xp": 360,
  "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (80, 300),
  "basic_attack": "wrench strike", "strong_attack": "overloaded gadget burst",
  "player_abilities": ["level_1_hostile_ability_electric_tech_hack_overload"],
  "base_str": 8, "base_dex": 10, "base_con": 8, "base_int": 14, "base_hp": 280, "base_ap": 14,
  "str_per_level": 1, "dex_per_level": 2, "con_per_level": 1, "int_per_level": 3},

 # min_spawn_level == 27
 {"id": "scrap_shaman_elder", "name": "Scrap Shaman Elder", "hostile_type": "magic", "role": "hazard", "min_spawn_level": 27, "rarity": "rare", "base_xp": 480,
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (60, 240),
  "basic_attack": "hex bolt", "strong_attack": "junk curse",
  "player_abilities": ["dark_magic_lv1_shadow_tendril", "dark_dark_magic_lv2_umbra_storm"],
  "base_str": 4, "base_dex": 6, "base_con": 6, "base_int": 18, "base_hp": 240, "base_ap": 16,
  "str_per_level": 0, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 4},

 # min_spawn_level == 30
 {"id": "biohazard_colossus", "name": "Biohazard Colossus", "hostile_type": "creature", "role": "damage", "min_spawn_level": 30, "rarity": "superrare", "base_xp": 1200,
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (100, 400),
  "basic_attack": "toxic slam", "strong_attack": "biohazard pulse",
  "player_abilities": ["level_1_hostile_ability_dark_skill_corrosive_spit"],
  "base_str": 22, "base_dex": 6, "base_con": 20, "base_int": 4, "base_hp": 700, "base_ap": 8,
  "str_per_level": 5, "dex_per_level": 1, "con_per_level": 4, "int_per_level": 0},
]
