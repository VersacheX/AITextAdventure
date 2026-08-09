"""Shallows Small City — Uul'thar's Tidal Maw Dungeon Seed (Type B)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# uulthars_tidal_maw.py
# City: Tidekin Cove (shallows_small, Ch.14)
# Chain: Type B — Regional Boss / Void Gauntlet (Ripple)
# Player level at encounter: ~70
# Pattern: B — player teleported to final_chamber; boss = uulthar_b1
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#205868'
IMPASSABLE_COLOR = '#081c22'
BORDER_TILE      = '·'
BORDER_COLOR     = '#184858'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'uulthar', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['tide_construct', 'cove_wraith', 'tidal_sentinel', 'void_tide'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'tide_construct',
        'name': 'Tide Construct',
        'hostile_type': 'construct',
        'min_spawn_level': 68,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 496,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (134, 428),
        'basic_attack': 'slams with a tide-hardened appendage',
        'strong_attack': 'tidal slam',
        'player_abilities': [],
        'base_str': 48, 'base_dex': 40, 'base_con': 36, 'base_int': 16,
        'base_hp': 960, 'base_ap': 15,
        'str_per_level': 5, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['water', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['electric', 'light'],
    },
    {
        'id': 'cove_wraith',
        'name': 'Cove Wraith',
        'hostile_type': 'undead',
        'min_spawn_level': 69,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 604,
        'common_drop': 'stimulant_med',
        'rare_drop': 'herb_med',
        'money_range': (162, 516),
        'basic_attack': 'drags with cove-cold hands that disrupt the tide geometry',
        'strong_attack': 'geometry drain',
        'player_abilities': [],
        'base_str': 28, 'base_dex': 50, 'base_con': 30, 'base_int': 36,
        'base_hp': 975, 'base_ap': 15,
        'str_per_level': 1, 'dex_per_level': 5, 'con_per_level': 2, 'int_per_level': 4,
        'resistances': ['dark', 'water'],
        'immunities': ['confuse', 'sleep'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'tidal_sentinel',
        'name': 'Tidal Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 70,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 768,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (202, 646),
        'basic_attack': 'holds position and strikes with a tide-pressure pulse',
        'strong_attack': 'pressure crash',
        'player_abilities': [],
        'base_str': 34, 'base_dex': 20, 'base_con': 60, 'base_int': 14,
        'base_hp': 1280, 'base_ap': 15,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 6, 'int_per_level': 1,
        'resistances': ['water', 'physical'],
        'immunities': ['stun', 'slow', 'confuse'],
        'weaknesses': ['electric', 'light'],
    },
    {
        'id': 'void_tide',
        'name': 'Void Tide',
        'hostile_type': 'elemental',
        'min_spawn_level': 70,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 1034,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (242, 774),
        'basic_attack': 'sends a void-infused tidal wave that rewrites local geometry',
        'strong_attack': 'void configuration',
        'player_abilities': [],
        'base_str': 44, 'base_dex': 46, 'base_con': 36, 'base_int': 42,
        'base_hp': 1200, 'base_ap': 17,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'electric'],
    },
]

BOSS_MOB: Dict = {
    'id': 'uulthar_boss',
    'name': "Uul'thar the Tide-Wakened",
    'hostiles': ['uulthar_b1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'uulthar_b1',
        'name': "Uul'thar the Tide-Wakened",
        'hostile_type': 'humanoid',
        'min_spawn_level': 72,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 32000,
        'common_drop': 'stimulant_med',
        'rare_drop': 'stimulant_med',
        'money_range': (780, 2340),
        'basic_attack': 'reconfigures the tidal geometry of the maw into a directed collapse',
        'strong_attack': 'tide reconfiguration',
        'player_abilities': [],
        'base_str': 56, 'base_dex': 54, 'base_con': 52, 'base_int': 60,
        'base_hp': 38000, 'base_ap': 560,
        'str_per_level': 5, 'dex_per_level': 5, 'con_per_level': 5, 'int_per_level': 6,
        'resistances': ['water', 'dark', 'physical'],
        'immunities': ['sleep', 'confuse', 'stun', 'slow'],
        'weaknesses': ['electric', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'uulthars_tidal_maw',
    'display_name': "Uul'thar's Tidal Maw",
    'seed': abs(hash('uulthars_tidal_maw')),
    'floor_count': 1,
    'rooms_per_floor': 5,
    'room_size_min_max': (60, 115),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.08,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (3, 7),
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color': OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile': BORDER_TILE,
    'border_color': BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'visible_distance': 7,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}