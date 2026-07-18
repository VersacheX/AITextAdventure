"""Aeriola's Glacier Tomb Dungeon Seed Configuration"""

from typing import Dict, Any

# Tile constants for dungeon rendering and builder decisions
OPEN_AREA_TILE   = "░"
IMPASSABLE_TILE  = "¤"
IMPASSABLE_CHANCE = 0.03
OPEN_AREA_COLOR  = "#90b8d8"
IMPASSABLE_COLOR = "#1a3050"
BORDER_TILE      = "·"
BORDER_COLOR     = "#5a88a8"

FLOOR_HOSTILES = {
    1: ['frostling', 'ice_wolf', 'shiver_shade', 'glacier_spirit', 'frozen_stalker', 'snow_bandit', 'frostbound_bear']
}

HOSTILE_SEEDS = [  # all level 8–10, ~10 hostiles total
    # Floor 1 - Glacier Tomb (cold creatures, spirits, humanoids)
    {
        'id': 'frostling',
        'name': 'Frostling',
        'hostile_type': 'creature',
        'min_spawn_level': 18,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 20,
        'common_drop': 'herb_minor',
        'rare_drop': None,
        'money_range': (2, 12),
        'basic_attack': 'frost nip',
        'strong_attack': 'ice burst',
        'player_abilities': ['ice_magic_lv1_frostbolt'],
        'base_str': 2,
        'base_dex': 3,
        'base_con': 2,
        'base_int': 4,
        'base_hp': 24,
        'base_ap': 3,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 0,
        'resistances': ['ice'],
        'immunities': [],
        'weaknesses': ['fire']
    },
    {
        'id': 'ice_wolf',
        'name': 'Ice Wolf',
        'hostile_type': 'creature',
        'min_spawn_level': 19,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 36,
        'common_drop': 'stimulant_small',
        'rare_drop': 'stimulant_large',
        'money_range': (6, 30),
        'basic_attack': 'frost bite',
        'strong_attack': 'howling chill',
        'player_abilities': [],
        'base_str': 4,
        'base_dex': 6,
        'base_con': 4,
        'base_int': 2,
        'base_hp': 34,
        'base_ap': 4,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 0,
        'resistances': ['ice'],
        'immunities': [],
        'weaknesses': ['fire']
    },
    {
        'id': 'shiver_shade',
        'name': 'Shiver Shade',
        'hostile_type': 'spirit',
        'min_spawn_level': 20,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 60,
        'common_drop': 'herb_med',
        'rare_drop': 'herb_major',
        'money_range': (10, 50),
        'basic_attack': 'chill touch',
        'strong_attack': 'frozen scream',
        'player_abilities': ['ice_air_magic_lv2_chill_drift'],
        'base_str': 3,
        'base_dex': 5,
        'base_con': 5,
        'base_int': 6,
        'base_hp': 60,
        'base_ap': 4,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 2,
        'resistances': ['ice'],
        'immunities': ['continuous_damage'],
        'weaknesses': ['fire']
    },
    {
        'id': 'glacier_spirit',
        'name': 'Glacier Spirit',
        'hostile_type': 'spirit',
        'min_spawn_level': 20,
        'role': 'support',
        'rarity': 'uncommon',
        'base_xp': 120,
        'common_drop': 'herb_minor',
        'rare_drop': 'herb_major',
        'money_range': (20, 90),
        'basic_attack': 'frost pulse',
        'strong_attack': 'glacial bind',
        'player_abilities': ['ice_dark_magic_lv2_shadowfrost_bolt'],
        'base_str': 4,
        'base_dex': 4,
        'base_con': 6,
        'base_int': 6,
        'base_hp': 140,
        'base_ap': 6,
        'str_per_level': 1,
        'dex_per_level': 1,
        'con_per_level': 2,
        'int_per_level': 2,
        'resistances': ['ice'],
        'immunities': ['continuous_damage'],
        'weaknesses': ['fire']
    },
    {
        'id': 'frozen_stalker',
        'name': 'Frozen Stalker',
        'hostile_type': 'humanoid',
        'min_spawn_level': 22,
        'role': 'damage',
        'rarity': 'rare',
        'base_xp': 200,
        'common_drop': 'herb_minor',
        'rare_drop': 'herb_major',
        'money_range': (30, 120),
        'basic_attack': 'ice blade',
        'strong_attack': 'shatter strike',
        'player_abilities': ['ice_dark_skill_lv2_shadow_spike'],
        'base_str': 6,
        'base_dex': 7,
        'base_con': 6,
        'base_int': 3,
        'base_hp': 180,
        'base_ap': 5,
        'str_per_level': 2,
        'dex_per_level': 2,
        'con_per_level': 2,
        'int_per_level': 1,
        'resistances': ['ice'],
        'immunities': [],
        'weaknesses': ['fire']
    },
    {
        'id': 'snow_bandit',
        'name': 'Snow Bandit',
        'hostile_type': 'humanoid',
        'min_spawn_level': 18,
        'role': 'hazard',
        'rarity': 'common',
        'base_xp': 24,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (4, 16),
        'basic_attack': 'slash',
        'strong_attack': 'frosted strike',
        'player_abilities': [],
        'base_str': 4,
        'base_dex': 5,
        'base_con': 4,
        'base_int': 2,
        'base_hp': 28,
        'base_ap': 3,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 0,
        'resistances': [],
        'immunities': [],
        'weaknesses': ['fire']
    },
    {
        'id': 'frostbound_bear',
        'name': 'Frostbound Bear',
        'hostile_type': 'creature',
        'min_spawn_level': 24,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 300,
        'common_drop': 'herb_major',
        'rare_drop': 'tome_con_superrare',
        'money_range': (50, 200),
        'basic_attack': 'frozen maul',
        'strong_attack': 'avalanche slam',
        'player_abilities': ['ice_ice_technique_lv2_frost_smash'],
        'base_str': 10,
        'base_dex': 6,
        'base_con': 12,
        'base_int': 3,
        'base_hp': 420,
        'base_ap': 6,
        'str_per_level': 3,
        'dex_per_level': 1,
        'con_per_level': 3,
        'int_per_level': 0,
        'resistances': ['ice'],
        'immunities': ['ice'],
        'weaknesses': ['fire']
    }
]

DUNGEON_NPCS = [ {'id': 'aeriola','location': 'final_chamber'} ]
DUNGEON_ITEMS = [ {'id': 'herb_major', 'location': 'treasure_room'} ]

BOSS_MOB = { 'id': 'aeriola_1',
             'name': 'Lady Aeriola Frostborn',
             'hostiles': [
                'aeriola_acolyte',
                'aeriola_acolyte',
                'aeriola_1']
            }

BOSS_HOSTILES = [
    {
        "id": "aeriola_acolyte", "name": "Aeriola Acolyte", "hostile_type": "magic", "role": "hazard",
        "min_spawn_level": 25, "rarity": "superrare", "base_xp": 480,
        "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (45,180),
        "basic_attack": "frost lash", "strong_attack": "stillness burst",
        "player_abilities": ["ice_air_magic_lv2_chill_drift", "ice_ice_magic_lv2_glacier_burst"],
        "base_str": 6, "base_dex": 6, "base_con": 8, "base_int": 14,
        "base_hp": 1500, "base_ap": 10,
        "str_per_level": 1, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 3
    },
    {
        "id": "aeriola_1", "name": "Lady Aeriola Frostborn", "hostile_type": "magic", "role": "boss",
        "min_spawn_level": 30, "rarity": "notfound", "base_xp": 1200,
        "common_drop": "herb_major", "rare_drop": "tome_int", "money_range": (100,300),
        "basic_attack": "frozen grasp", "strong_attack": "absolute zero",
        "player_abilities": ["ice_dark_magic_lv2_shadowfrost_bolt", "ice_water_magic_lv2_glacier_spike", 'ice_ice_ice_magic_lv3_frost_nova'],
        "base_str": 10, "base_dex": 8, "base_con": 12, "base_int": 16,
        "base_hp": 2200, "base_ap": 12,
        "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 3
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    "dungeon_id": "aeriola_lair",
    "seed": abs(hash("aeriola_lair")),
    "floor_count": 1,
    "room_size_min_max": (81, 120),  # a 9x9 area is 81
    "rooms_per_floor": 6,
    "max_neighbors_per_room": 3,
    "additional_connection_chance": 0.0,
    "min_max_distance_between_rooms": (8,12),
    "min_max_corridor_width": (3,4),
    "display_name": "Aeriola's Glacier Tomb",
    "open_area_tile": OPEN_AREA_TILE,
    "impassable_tile": IMPASSABLE_TILE,
    "open_area_color":  OPEN_AREA_COLOR,
	"impassable_color": IMPASSABLE_COLOR,
	"border_tile":      BORDER_TILE,
	"border_color":     BORDER_COLOR,
    "impassable_chance": IMPASSABLE_CHANCE,
    "floor_hostiles": FLOOR_HOSTILES,
    "hostile_seeds": HOSTILE_SEEDS,
    "npcs": DUNGEON_NPCS,
	"items": DUNGEON_ITEMS,
    "boss_mob": BOSS_MOB,
    "boss_hostiles": BOSS_HOSTILES,
    "visible_distance": 7
}