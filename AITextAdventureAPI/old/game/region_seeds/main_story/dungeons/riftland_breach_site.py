"""
Riftland Breach Site - Chapter 6 Dungeon Seed Configuration
The site of a reality breach where a Riftspawn Aberrant has emerged.
"""

from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.30
OPEN_AREA_COLOR  = "#4a7a5a"
IMPASSABLE_COLOR = "#1a3a28"
BORDER_TILE      = "·"
BORDER_COLOR     = "#3a5a48"

# Hostiles
FLOOR_HOSTILES = {
    1: ['breach_crawler', 'reality_splinter'],
}

HOSTILE_SEEDS = [
    {
        'id': 'breach_crawler',
        'name': 'Breach Crawler',
        'hostile_type': 'beast',
        'min_spawn_level': 26,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 220,
        'common_drop': 'stimulant_med',
        'rare_drop': None,
        'money_range': (25, 50),
        'basic_attack': 'pincer snap',
        'strong_attack': 'phase lunge',
        'player_abilities': [],
        'base_str': 15, 'base_dex': 19, 'base_con': 14, 'base_int': 5,
        'base_hp': 450, 'base_ap': 35,
        'str_per_level': 2, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 0,
        'resistances': ['physical'], 'immunities': [], 'weaknesses': ['ice']
    },
    {
        'id': 'reality_splinter',
        'name': 'Reality Splinter',
        'hostile_type': 'elemental',
        'min_spawn_level': 25,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 250,
        'common_drop': 'herb_med',
        'rare_drop': 'tome_int',
        'money_range': (30, 60),
        'basic_attack': 'fracture shard',
        'strong_attack': 'unraveling burst',
        'player_abilities': ['electric_dark_tech_lv2_void_shocker'],
        'base_str': 9, 'base_dex': 15, 'base_con': 12, 'base_int': 21,
        'base_hp': 400, 'base_ap': 45,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 3,
        'resistances': ['dark'], 'immunities': [], 'weaknesses': ['light']
    }
]

# The aberrant is the boss of this "dungeon"
DUNGEON_NPCS = [ {'id': 'riftspawn_aberrant', 'location': 'final_chamber'} ]
BOSS_MOB = {
    'id': 'riftspawn_aberrant_1',
    'name': 'Riftspawn Aberrant',
    'hostiles': ['riftspawn_aberrant_1']
}

BOSS_HOSTILES = [
    {
        'id': 'riftspawn_aberrant_1',
        'name': 'Riftspawn Aberrant',
        'hostile_type': 'aberration',
        'min_spawn_level': 27,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 3500,
        'common_drop': 'tome_dex',
        'rare_drop': 'riftland_stabilizer_core',
        'money_range': (200, 450),
        'basic_attack': 'reality slash',
        'strong_attack': 'dimensional shriek',
        'player_abilities': ['dark_dark_technique_lv2_void_crush', 'air_dark_magic_lv2_gloom_vortex'],
        'base_str': 16, 'base_dex': 24, 'base_con': 18, 'base_int': 20,
        'base_hp': 8500, 'base_ap': 200,
        'str_per_level': 2, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark', 'air'], 'immunities': ['confuse'], 'weaknesses': ['light', 'earth']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'riftland_breach_site',
    'seed': abs(hash('riftland_breach_site')),
    'floor_count': 1,
    'room_size_min_max': (120, 200),
    'rooms_per_floor': 2, # A single, large breach area
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.0,
    'min_max_distance_between_rooms': (0, 0),
    'min_max_corridor_width': (1, 1),
    'display_name': "Riftland Breach Site",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color':  OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile':      BORDER_TILE,
    'border_color':     BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': [{'id': 'riftspawn_aberrant', 'location': 'final_chamber'}],
    'items': [
        {'id': 'stimulant_large', 'location': 'treasure_room'},
        {'id': 'panacea', 'location': 'treasure_room'}
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 8,
}
