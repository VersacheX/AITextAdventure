# LEVEL11-20 hostile regional seeds for mountains region (to be imported by higher-level modules).
# Export a list named SEEDS_LV11TO20
SEEDS_LV11TO20 = [
 {"id": "iron_pioneer", "name": "Iron Pioneer", "hostile_type": "humanoid", "role": "support", "min_spawn_level":11, "rarity": "uncommon", "base_xp":120, "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (20,100),
 "basic_attack": "foundry swing", "strong_attack": "anvil crush", "player_abilities": ["air_earth_tech_lv5_reinforce_frame"], "base_str":8, "base_dex":4, "base_con":8, "base_int":4, "base_hp":120, "base_ap":6, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":1},

 {"id": "forge_hound", "name": "Forge Hound", "hostile_type": "creature", "role": "damage", "min_spawn_level":11, "rarity": "common", "base_xp":72, "common_drop": "herb_med", "rare_drop": None, "money_range": (8,40),
 "basic_attack": "molten nip", "strong_attack": "ember maul", "player_abilities": [], "base_str":6, "base_dex":6, "base_con":6, "base_int":2, "base_hp":120, "base_ap":4, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":0},

 {"id": "magma_hydra", "name": "Magma Hydra", "hostile_type": "creature", "role": "damage", "min_spawn_level":12, "rarity": "superrare", "base_xp":480, "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40,200),
 "basic_attack": "multi-bite", "strong_attack": "lava barrage", "player_abilities": ["earth_dark_skill_lv5_venom_trace"], "base_str":12, "base_dex":10, "base_con":12, "base_int":8, "base_hp":520, "base_ap":10, "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":2},

 {"id": "peak_runner", "name": "Peak Runner", "hostile_type": "creature", "role": "damage", "min_spawn_level":12, "rarity": "common", "base_xp":90, "common_drop": "herb_med", "rare_drop": None, "money_range": (10,56),
 "basic_attack": "swooping claw", "strong_attack": "pierce dash", "player_abilities": [], "base_str":6, "base_dex":10, "base_con":6, "base_int":3, "base_hp":120, "base_ap":6, "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "summit_scout", "name": "Summit Scout", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":13, "rarity": "uncommon", "base_xp":110, "common_drop": "herb_med", "rare_drop": None, "money_range": (12,64),
 "basic_attack": "knife jab", "strong_attack": "ice toss", "player_abilities": [], "base_str":5, "base_dex":8, "base_con":6, "base_int":4, "base_hp":110, "base_ap":5, "str_per_level":2, "dex_per_level":2, "con_per_level":1, "int_per_level":1},

 {"id": "ridge_shaman", "name": "Ridge Shaman", "hostile_type": "magic", "role": "hazard", "min_spawn_level":13, "rarity": "uncommon", "base_xp":130, "common_drop": "herb_med", "rare_drop": "tome_int", "money_range": (14,72),
 "basic_attack": "cold touch", "strong_attack": "frost burst", "player_abilities": ["lv2_hostile_ability_ice_light_magic_frost_nova"], "base_str":4, "base_dex":5, "base_con":6, "base_int":10, "base_hp":120, "base_ap":8, "str_per_level":1, "dex_per_level":1, "con_per_level":1, "int_per_level":3},

 {"id": "alpine_poacher", "name": "Alpine Poacher", "hostile_type": "humanoid", "role": "damage", "min_spawn_level":13, "rarity": "uncommon", "base_xp":112, "common_drop": "stimulant_small", "rare_drop": None, "money_range": (12,64),
 "basic_attack": "snare jab", "strong_attack": "clubbed flank", "player_abilities": [], "base_str":6, "base_dex":6, "base_con":5, "base_int":3, "base_hp":108, "base_ap":5, "str_per_level":2, "dex_per_level":1, "con_per_level":1, "int_per_level":1},

 {"id": "peak_sentry", "name": "Peak Sentry", "hostile_type": "construct", "role": "damage", "min_spawn_level":14, "rarity": "common", "base_xp":140, "common_drop": "herb_med", "rare_drop": None, "money_range": (14,72),
 "basic_attack": "iron swipe", "strong_attack": "boulder crush", "player_abilities": [], "base_str":10, "base_dex":3, "base_con":10, "base_int":2, "base_hp":180, "base_ap":6, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "peak_warden", "name": "Peak Warden", "hostile_type": "celestial", "role": "hazard", "min_spawn_level":14, "rarity": "rare", "base_xp":420, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (40,200),
 "basic_attack": "radiant talons", "strong_attack": "celestial volley", "player_abilities": ["air_air_spirit_lv2_tempest_hymn"], "base_str":12, "base_dex":8, "base_con":12, "base_int":12, "base_hp":420, "base_ap":12, "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":3},

 {"id": "ember_colossus", "name": "Ember Colossus", "hostile_type": "creature", "role": "damage", "min_spawn_level":14, "rarity": "common", "base_xp":160, "common_drop": "herb_med", "rare_drop": None, "money_range": (16,80),
 "basic_attack": "magma club", "strong_attack": "lava heave", "player_abilities": [], "base_str":12, "base_dex":4, "base_con":12, "base_int":3, "base_hp":240, "base_ap":6, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":1},

 {"id": "nether_mole", "name": "Nether Mole", "hostile_type": "creature", "role": "damage", "min_spawn_level":15, "rarity": "uncommon", "base_xp":150, "common_drop": "herb_med", "rare_drop": None, "money_range": (18,90),
 "basic_attack": "tunnel bite", "strong_attack": "earth upheaval", "player_abilities": [], "base_str":8, "base_dex":4, "base_con":8, "base_int":2, "base_hp":200, "base_ap":6, "str_per_level":2, "dex_per_level":0, "con_per_level":2, "int_per_level":0},

 {"id": "lava_brute", "name": "Lava Brute", "hostile_type": "creature", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":180, "common_drop": "herb_major", "rare_drop": None, "money_range": (20,100),
 "basic_attack": "smash", "strong_attack": "molten slam", "player_abilities": [], "base_str":14, "base_dex":3, "base_con":12, "base_int":2, "base_hp":260, "base_ap":6, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "basalt_howler", "name": "Basalt Howler", "hostile_type": "creature", "role": "damage", "min_spawn_level":15, "rarity": "common", "base_xp":170, "common_drop": "herb_med", "rare_drop": None, "money_range": (18,90),
 "basic_attack": "piercing howl", "strong_attack": "rock maul", "player_abilities": [], "base_str":12, "base_dex":6, "base_con":10, "base_int":3, "base_hp":240, "base_ap":6, "str_per_level":3, "dex_per_level":2, "con_per_level":2, "int_per_level":1},

 {"id": "lava_gargant", "name": "Lava Gargant", "hostile_type": "creature", "role": "damage", "min_spawn_level":16, "rarity": "rare", "base_xp":820, "common_drop": "herb_major", "rare_drop": "kevlar_vest", "money_range": (80,360),
 "basic_attack": "colossal slam", "strong_attack": "magma monolith", "player_abilities": [], "base_str":18, "base_dex":4, "base_con":18, "base_int":4, "base_hp":1200, "base_ap":8, "str_per_level":5, "dex_per_level":0, "con_per_level":4, "int_per_level":1},

 {"id": "rock_lich", "name": "Rock Lich", "hostile_type": "undead", "role": "hazard", "min_spawn_level":16, "rarity": "rare", "base_xp":420, "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (40,220),
 "basic_attack": "stone bolt", "strong_attack": "necrotic quake", "player_abilities": ["dark_dark_magic_lv2_umbra_storm"], "base_str":10, "base_dex":4, "base_con":12, "base_int":14, "base_hp":380, "base_ap":10, "str_per_level":3, "dex_per_level":0, "con_per_level":3, "int_per_level":3},

 {"id": "granite_colossus", "name": "Granite Colossus", "hostile_type": "creature", "role": "damage", "min_spawn_level":17, "rarity": "common", "base_xp":240, "common_drop": "herb_major", "rare_drop": None, "money_range": (40,180),
 "basic_attack": "granite slam", "strong_attack": "granite quake", "player_abilities": [], "base_str":12, "base_dex":3, "base_con":12, "base_int":2, "base_hp":380, "base_ap":8, "str_per_level":4, "dex_per_level":0, "con_per_level":3, "int_per_level":0},

 {"id": "north_raven", "name": "North Raven", "hostile_type": "creature", "role": "hazard", "min_spawn_level":17, "rarity": "common", "base_xp":340, "common_drop": "stimulant_large", "rare_drop": "ointment", "money_range": (40,180),
 "basic_attack": "pierce cry", "strong_attack": "shadow beak", "player_abilities": ["dark_magic_lv1_shadow_tendril"], "base_str":8, "base_dex":12, "base_con":6, "base_int":6, "base_hp":340, "base_ap":10, "str_per_level":3, "dex_per_level":3, "con_per_level":1, "int_per_level":1},

 {"id": "summit_archmage", "name": "Summit Archmage", "hostile_type": "magic", "role": "hazard", "min_spawn_level":18, "rarity": "rare", "base_xp":1100, "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": (100,400),
 "basic_attack": "arcane flick", "strong_attack": "meteor shard", "player_abilities": ["electric_fire_magic_lv2_arclance"], "base_str":8, "base_dex":8, "base_con":10, "base_int":20, "base_hp":980, "base_ap":14, "str_per_level":2, "dex_per_level":1, "con_per_level":2, "int_per_level":4},

 {"id": "ash_revenant", "name": "Ash Revenant", "hostile_type": "undead", "role": "hazard", "min_spawn_level":18, "rarity": "common", "base_xp":360, "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (60,220),
 "basic_attack": "ichor swipe", "strong_attack": "necrotic gale", "player_abilities": ["dark_dark_magic_lv2_umbra_storm", "level_1_hostile_ability_night_whisper"], "base_str":12, "base_dex":8, "base_con":12, "base_int":12, "base_hp":520, "base_ap":12, "str_per_level":4, "dex_per_level":2, "con_per_level":3, "int_per_level":3},

 {"id": "storm_colossus", "name": "Storm Colossus", "hostile_type": "construct", "role": "hazard", "min_spawn_level":19, "rarity": "common", "base_xp":600, "common_drop": "stimulant_large", "rare_drop": "kevlar_vest", "money_range": (120,480),
 "basic_attack": "thunder stomp", "strong_attack": "tempest crush", "player_abilities": ["level_1_hostile_ability_electric_magic_chain_lightning"], "base_str":18, "base_dex":6, "base_con":18, "base_int":10, "base_hp":1400, "base_ap":14, "str_per_level":5, "dex_per_level":1, "con_per_level":4, "int_per_level":2},

 {"id": "auric_chalice", "name": "Auric Chalice", "hostile_type": "celestial", "role": "support", "min_spawn_level":20, "rarity": "uncommon", "base_xp":760, "common_drop": "stimulant_large", "rare_drop": "herb_major", "money_range": (140,560),
 "basic_attack": "luminous tap", "strong_attack": "solar cascade", "player_abilities": ["light_light_spirit_lv2_seraphic_nova", "level_1_hostile_ability_light_spirit_prism_burst"], "base_str":14, "base_dex":8, "base_con":14, "base_int":16, "base_hp":980, "base_ap":12, "str_per_level":3, "dex_per_level":2, "con_per_level":3, "int_per_level":3},
]