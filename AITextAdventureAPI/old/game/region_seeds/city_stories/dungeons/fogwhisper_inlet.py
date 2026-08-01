"""Shallows Small City — Fogwhisper Inlet Dungeon Seed (Type A)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# fogwhisper_inlet.py
# City: Tidekin Cove (shallows_small, Ch.14)
# Chain: Type A slot 1 — meet fogwhisper_echo
# Player level at encounter: ~70
# Pattern: A — exploration; fogwhisper_echo waits in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#304858'
IMPASSABLE_COLOR = '#0e181e'
BORDER_TILE      = '·'
BORDER_COLOR     = '#203848'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'fogwhisper_echo', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['fog_drifter', 'inlet_shade', 'cove_sentinel', 'void_fog'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'fog_drifter',
        'name': 'Fog Drifter',
        'hostile_type': 'undead',
        'min_spawn_level': 68,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 496,
        'common_drop': 'herb_large',
        'rare_drop': None,
        'money_range': (134, 428),
        'basic_attack': 'drifts through the fog and strikes from an unseen angle',
        'strong_attack': 'fog ambush',
        'player_abilities': [],
        'base_str': 48, 'base_dex': 44, 'base_con': 36, 'base_int': 16,
        'base_hp': 955, 'base_ap': 15,
        'str_per_level': 5, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'inlet_shade',
        'name': 'Inlet Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 69,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 604,
        'common_drop': 'remedy_large',
        'rare_drop': 'herb_large',
        'money_range': (162, 516),
        'basic_attack': 'sends a devoured warning as a concussive strike',
        'strong_attack': 'warning drain',
        'player_abilities': [],
        'base_str': 30, 'base_dex': 52, 'base_con': 30, 'base_int': 34,
        'base_hp': 968, 'base_ap': 15,
        'str_per_level': 1, 'dex_per_level': 5, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark', 'water'],
        'immunities': ['confuse', 'sleep'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'cove_sentinel',
        'name': 'Cove Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 70,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 768,
        'common_drop': 'stimulant_large',
        'rare_drop': 'remedy_large',
        'money_range': (202, 646),
        'basic_attack': 'holds the inlet passage and strikes with tide-pressure force',
        'strong_attack': 'inlet crush',
        'player_abilities': [],
        'base_str': 34, 'base_dex': 20, 'base_con': 62, 'base_int': 14,
        'base_hp': 1275, 'base_ap': 15,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 6, 'int_per_level': 1,
        'resistances': ['water', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['electric', 'light'],
    },
    {
        'id': 'void_fog',
        'name': 'Void Fog',
        'hostile_type': 'elemental',
        'min_spawn_level': 70,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 1034,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (242, 774),
        'basic_attack': 'condenses void-infused fog into a focused strike',
        'strong_attack': 'void fog collapse',
        'player_abilities': [],
        'base_str': 44, 'base_dex': 48, 'base_con': 36, 'base_int': 42,
        'base_hp': 1195, 'base_ap': 17,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'electric'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'fogwhisper_inlet',
    'display_name': 'Fogwhisper Inlet',
    'seed': abs(hash('fogwhisper_inlet')),
    'floor_count': 1,
    'rooms_per_floor': 3,
    'room_size_min_max': (55, 105),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.08,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (3, 6),
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color': OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile': BORDER_TILE,
    'border_color': BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'visible_distance': 6,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': None,
    'boss_hostiles': [],
}