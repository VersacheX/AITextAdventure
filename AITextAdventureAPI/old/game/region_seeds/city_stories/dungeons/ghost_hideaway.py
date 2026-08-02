"""Swamp Small City — Ghost Hideaway Dungeon Seed (Type C)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# ghost_hideaway.py
# City: Gnashwater Hollow (swamp_small, Ch.7)
# Chain: Type C — Extended Character (Ghost)
# Player level at encounter: ~35
# Pattern: A — exploration dungeon; Ghost waits in final_chamber, no boss fight
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.13
OPEN_AREA_COLOR  = '#2a3028'
IMPASSABLE_COLOR = '#0e100c'
BORDER_TILE      = '·'
BORDER_COLOR     = '#1e2418'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'ghost', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'petrify_salve',      'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['hollow_drifter', 'shadow_rot', 'swamp_specter', 'night_revenant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'hollow_drifter',
        'name': 'Hollow Drifter',
        'hostile_type': 'undead',
        'min_spawn_level': 32,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 210,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (55, 140),
        'basic_attack': 'strikes from behind with a waterlogged blade',
        'strong_attack': 'hollow ambush',
        'player_abilities': [],
        'base_str': 20, 'base_dex': 20, 'base_con': 14, 'base_int': 5,
        'base_hp': 370, 'base_ap': 9,
        'str_per_level': 2, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 0,
        'resistances': ['dark'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'shadow_rot',
        'name': 'Shadow Rot',
        'hostile_type': 'undead',
        'min_spawn_level': 33,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 248,
        'common_drop': 'ointment',
        'rare_drop': 'petrify_salve',
        'money_range': (62, 155),
        'basic_attack': 'seeps through the shadow to corrode on contact',
        'strong_attack': 'shadow drain',
        'player_abilities': [],
        'base_str': 12, 'base_dex': 18, 'base_con': 13, 'base_int': 10,
        'base_hp': 395, 'base_ap': 9,
        'str_per_level': 1, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['dark', 'earth'],
        'immunities': ['poison', 'sleep'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'swamp_specter',
        'name': 'Swamp Specter',
        'hostile_type': 'undead',
        'min_spawn_level': 34,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 298,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (80, 200),
        'basic_attack': 'phases through obstacles to strike directly',
        'strong_attack': 'spectral press',
        'player_abilities': [],
        'base_str': 15, 'base_dex': 12, 'base_con': 26, 'base_int': 8,
        'base_hp': 545, 'base_ap': 9,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 4, 'int_per_level': 1,
        'resistances': ['dark', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['light'],
    },
    {
        'id': 'night_revenant',
        'name': 'Night Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 35,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 375,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (110, 280),
        'basic_attack': 'channels the night channels into a focused void-strike',
        'strong_attack': 'nightchannel surge',
        'player_abilities': [],
        'base_str': 22, 'base_dex': 24, 'base_con': 16, 'base_int': 14,
        'base_hp': 490, 'base_ap': 10,
        'str_per_level': 3, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['dark'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'fire'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'ghost_hideaway',
    'display_name': 'The Night Hideaway',
    'seed': abs(hash('ghost_hideaway')),
    'floor_count': 1,
    'rooms_per_floor': 3,
    'room_size_min_max': (50, 95),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.07,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (2, 5),
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