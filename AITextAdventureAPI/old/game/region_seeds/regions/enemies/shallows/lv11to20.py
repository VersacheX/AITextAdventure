# LEVEL 1-10 hostile regional (to be imported by higher-level modules).

RANDOM_HOSTILE_SEEDS = []

# LEVEL11-20 hostile regional seeds for shallows region (to be imported by higher-level modules).
# Export a list named SEEDS_LV11TO20
SEEDS_LV11TO20 = [
 {"id": "murkwalker_alpha", "name": "Murkwalker Alpha", "hostile_type": "creature", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":380, "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (60,260),
 "basic_attack": "alpha maul", "strong_attack": "rending charge", "player_abilities": [], "base_str":12, "base_dex":8, "base_con":12, "base_int":3, "base_hp":320, "base_ap":8, "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":0},

 {"id": "barnacle_scrapper", "name": "Barnacle Scrapper", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":90, "common_drop": "stimulant_small", "rare_drop": None, "money_range": (10,56),
 "basic_attack": "barnacle bash", "strong_attack": "rusted cleave", "player_abilities": [], "base_str":6, "base_dex":5, "base_con":6, "base_int":2, "base_hp":120, "base_ap":5, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "tide_howler", "name": "Tide Howler", "hostile_type": "creature", "role": "damage", "min_spawn_level":12, "rarity": "uncommon", "base_xp":140, "common_drop": "herb_med", "rare_drop": None, "money_range": (14,72),
 "basic_attack": "mournful bite", "strong_attack": "surf wail", "player_abilities": [], "base_str":8, "base_dex":6, "base_con":8, "base_int":3, "base_hp":160, "base_ap":6, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "plague_baron_shallows", "name": "Plague Baron", "hostile_type": "undead", "role": "hazard", "min_spawn_level":12, "rarity": "rare", "base_xp":460, "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (80,320),
 "basic_attack": "disease lash", "strong_attack": "virulent purge", "player_abilities": ["earth_dark_skill_lv5_venom_trace", "level_1_hostile_ability_dark_skill_corrosive_spit"], "base_str":9, "base_dex":6, "base_con":12, "base_int":8, "base_hp":420, "base_ap":10, "str_per_level":3, "dex_per_level":1, "con_per_level":3, "int_per_level":2},

 {"id": "tidal_chimera", "name": "Tidal Chimera", "hostile_type": "creature", "role": "damage", "min_spawn_level":13, "rarity": "rare", "base_xp":520, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (90,360),
 "basic_attack": "multi-bite", "strong_attack": "spine barrage", "player_abilities": ["lv2_hostile_ability_water_electric_magic_maelstrom_burst"], "base_str":14, "base_dex":10, "base_con":10, "base_int":6, "base_hp":480, "base_ap":10, "str_per_level":4, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "reef_colossus", "name": "Reef Colossus", "hostile_type": "construct", "role": "damage", "min_spawn_level":13, "rarity": "common", "base_xp":160, "common_drop": "herb_med", "rare_drop": None, "money_range": (16,80),
 "basic_attack": "coral club", "strong_attack": "reef crush", "player_abilities": [], "base_str":12, "base_dex":4, "base_con":12, "base_int":2, "base_hp":240, "base_ap":6, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "deep_tide_sage", "name": "Deep Tide Sage", "hostile_type": "magic", "role": "support", "min_spawn_level":14, "rarity": "rare", "base_xp":600, "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (100,400),
 "basic_attack": "current probe", "strong_attack": "mind rot", "player_abilities": ["lv2_hostile_ability_dark_ice_skill_void_spike", "light_faith_lv1_minor_heal"], "base_str":6, "base_dex":6, "base_con":8, "base_int":18, "base_hp":520, "base_ap":12, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":4},

 {"id": "brack_mauler", "name": "Brack Mauler", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":14, "rarity": "common", "base_xp":120, "common_drop": "herb_med", "rare_drop": None, "money_range": (12,64),
 "basic_attack": "maul", "strong_attack": "tide crush", "player_abilities": [], "base_str":8, "base_dex":4, "base_con":8, "base_int":2, "base_hp":160, "base_ap":6, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "pilfering_moccasin", "name": "Pilfering Moccasin", "hostile_type": "humanoid", "role": "hazard", "min_spawn_level":15, "rarity": "uncommon", "base_xp":150, "common_drop": "stimulant_small", "rare_drop": None, "money_range": (18,90),
 "basic_attack": "sneak stab", "strong_attack": "fisher's swipe", "player_abilities": [], "base_str":6, "base_dex":8, "base_con":6, "base_int":4, "base_hp":140, "base_ap":6, "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "tidal_fisher", "name": "Tidal Fisher", "hostile_type": "creature", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":140, "common_drop": "herb_med", "rare_drop": None, "money_range": (16,80),
 "basic_attack": "hook swipe", "strong_attack": "drag under", "player_abilities": [], "base_str":8, "base_dex":6, "base_con":8, "base_int":2, "base_hp":180, "base_ap":6, "str_per_level":3, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "maelstrom_serpent", "name": "Maelstrom Serpent", "hostile_type": "creature", "role": "damage", "min_spawn_level":15, "rarity": "uncommon", "base_xp":200, "common_drop": "stimulant_large", "rare_drop": None, "money_range": (20,100),
 "basic_attack": "coil strike", "strong_attack": "maelstrom fang", "player_abilities": [], "base_str":10, "base_dex":10, "base_con":8, "base_int":4, "base_hp":220, "base_ap":8, "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "brine_lord", "name": "Brine Lord", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level":16, "rarity": "rare", "base_xp":760, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (120,480),
 "basic_attack": "voided claw", "strong_attack": "abyssal lash", "player_abilities": ["dark_magic_lv5_abyssal_shadow", "lv2_hostile_ability_dark_water_tech_void_spatter"], "base_str":16, "base_dex":10, "base_con":14, "base_int":14, "base_hp":760, "base_ap":14, "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":3},

 {"id": "kelp_colossus", "name": "Kelp Colossus", "hostile_type": "creature", "role": "damage", "min_spawn_level":16, "rarity": "common", "base_xp":240, "common_drop": "herb_major", "rare_drop": None, "money_range": (40,180),
 "basic_attack": "kelp slam", "strong_attack": "tangle quake", "player_abilities": [], "base_str":12, "base_dex":3, "base_con":12, "base_int":2, "base_hp":380, "base_ap":8, "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "marsh_knight", "name": "Marsh Knight", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":17, "rarity": "uncommon", "base_xp":260, "common_drop": "herb_major", "rare_drop": None, "money_range": (48,220),
 "basic_attack": "plate slash", "strong_attack": "spear rout", "player_abilities": [], "base_str":12, "base_dex":4, "base_con":12, "base_int":4, "base_hp":420, "base_ap":10, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":1},

 {"id": "silt_guard", "name": "Silt Guard", "hostile_type": "construct", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":200, "common_drop": "herb_med", "rare_drop": None, "money_range": (40,180),
 "basic_attack": "plank bash", "strong_attack": "column crush", "player_abilities": [], "base_str":10, "base_dex":3, "base_con":10, "base_int":2, "base_hp":360, "base_ap":8, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "pilgrim_of_tide", "name": "Pilgrim of Tide", "hostile_type": "faith", "role": "support", "min_spawn_level":18, "rarity": "uncommon", "base_xp":300, "common_drop": "stimulant_large", "rare_drop": "tome_con", "money_range": (60,280),
 "basic_attack": "prayer strike", "strong_attack": "consecrate wave", "player_abilities": ["light_faith_lv5_ardent_inspire", "water_faith_lv1_mending_streams"], "base_str":10, "base_dex":8, "base_con":12, "base_int":16, "base_hp":380, "base_ap":10, "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":3},

 {"id": "skyscale_serpent", "name": "Skyscale Serpent", "hostile_type": "creature", "role": "hazard", "min_spawn_level":18, "rarity": "common", "base_xp":340, "common_drop": "stimulant_large", "rare_drop": None, "money_range": (40,180),
 "basic_attack": "coil strike", "strong_attack": "tempest fang", "player_abilities": ["lv2_hostile_ability_dark_ice_skill_void_spike"], "base_str":14, "base_dex":10, "base_con":14, "base_int":12, "base_hp":420, "base_ap":12, "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":3},

 {"id": "wave_reaver", "name": "Wave Reaver", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":19, "rarity": "uncommon", "base_xp":380, "common_drop": "herb_major", "rare_drop": None, "money_range": (60,260),
 "basic_attack": "sweeping slash", "strong_attack": "breaker lunge", "player_abilities": [], "base_str":12, "base_dex":8, "base_con":12, "base_int":4, "base_hp":420, "base_ap":10, "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":1},

 {"id": "tide_guardian", "name": "Tide Guardian", "hostile_type": "construct", "role": "damage", "min_spawn_level":19, "rarity": "common", "base_xp":420, "common_drop": "herb_major", "rare_drop": None, "money_range": (70,300),
 "basic_attack": "ocean swipe", "strong_attack": "anchor slam", "player_abilities": [], "base_str":14, "base_dex":6, "base_con":14, "base_int":6, "base_hp":480, "base_ap":12, "str_per_level":4, "dex_per_level":1, "con_per_level":3, "int_per_level":1},

 {"id": "maelstrom_colossus", "name": "Maelstrom Colossus", "hostile_type": "construct", "role": "hazard", "min_spawn_level":20, "rarity": "superrare", "base_xp":1100, "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (160,640),
 "basic_attack": "ocean slam", "strong_attack": "maelstrom crush", "player_abilities": ["lv2_hostile_ability_water_electric_magic_maelstrom_burst", "level_1_hostile_ability_electric_magic_chain_lightning"], "base_str":20, "base_dex":6, "base_con":20, "base_int":6, "base_hp":1400, "base_ap":12, "str_per_level":5, "dex_per_level":1, "con_per_level":4, "int_per_level":1},
]