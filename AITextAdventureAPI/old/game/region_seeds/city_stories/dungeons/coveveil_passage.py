"""Shallows Small City — Coveveil Passage Dungeon Seed (Type A / Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# coveveil_passage.py
# City: Tidekin Cove (shallows_small, Ch.14)
# Chain: Type A slot 2 (coveveil_voice meet) + Type D (coveveil_voice_1 defeat)
# Player level at encounter: ~70
# Pattern: A — both voice NPCs in final_chamber; story triggers each in turn
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#284058'
IMPASSABLE_COLOR = '#0c1820'
BORDER_TILE      = '·'
BORDER_COLOR     = '#1c3048'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'coveveil_voice',   'location': 'final_chamber'},
    {'id': 'coveveil_voice_1', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['passage_drifter', 'veil_shade', 'tidekin_sentinel', 'void_veil'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'passage_drifter',
        'name': 'Passage Drifter',
        'hostile_type': 'undead',
        'min_spawn_level': 68,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 496,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (134, 428),
        'basic_attack': 'follows a hidden route to strike from behind',
        'strong_attack': 'passage ambush',
        'player_abilities': [],
        'base_str': 46, 'base_dex': 46, 'base_con': 36, 'base_int': 16,
        'base_hp': 950, 'base_ap': 15,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'veil_shade',
        'name': 'Veil Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 69,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 604,
        'common_drop': 'stimulant_med',
        'rare_drop': 'herb_med',
        'money_range': (162, 516),
        'basic_attack': 'sends a stolen warning through the veil as a disorienting strike',
        'strong_attack': 'veil drain',
        'player_abilities': [],
        'base_str': 28, 'base_dex': 52, 'base_con': 30, 'base_int': 36,
        'base_hp': 965, 'base_ap': 15,
        'str_per_level': 1, 'dex_per_level': 5, 'con_per_level': 2, 'int_per_level': 4,
        'resistances': ['dark', 'water'],
        'immunities': ['confuse', 'sleep'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'tidekin_sentinel',
        'name': 'Tidekin Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 70,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 768,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (202, 646),
        'basic_attack': 'guards the passage and strikes with Tidekin-iron force',
        'strong_attack': 'tidekin press',
        'player_abilities': [],
        'base_str': 34, 'base_dex': 20, 'base_con': 62, 'base_int': 14,
        'base_hp': 1280, 'base_ap': 15,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 6, 'int_per_level': 1,
        'resistances': ['water', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['electric', 'light'],
    },
    {
        'id': 'void_veil',
        'name': 'Void Veil',
        'hostile_type': 'elemental',
        'min_spawn_level': 70,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 1034,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (242, 774),
        'basic_attack': 'tears the passage veil open and strikes through the gap',
        'strong_attack': 'void passage collapse',
        'player_abilities': [],
        'base_str': 44, 'base_dex': 48, 'base_con': 36, 'base_int': 44,
        'base_hp': 1190, 'base_ap': 17,
        'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'electric'],
    },
]

BOSS_MOB: Dict = {
    'id': 'coveveil_voice_boss',
    'name': 'The Coveveil Voice',
    'hostiles': ['coveveil_voice_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'coveveil_voice_1',
        'name': 'The Coveveil Voice',
        'hostile_type': 'elemental',
        'min_spawn_level': 71,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 33000,
        'common_drop': 'stimulant_med',
        'rare_drop': 'stimulant_med',
        'money_range': (800, 2400),
        'basic_attack': 'floods the passage with every hidden route and drowned warning it has held since the first wardens passed on',
        'strong_attack': 'coveveil dominion',
        'player_abilities': [],
        'base_str': 56, 'base_dex': 56, 'base_con': 52, 'base_int': 60,
        'base_hp': 39000, 'base_ap': 570,
        'str_per_level': 5, 'dex_per_level': 5, 'con_per_level': 5, 'int_per_level': 6,
        'resistances': ['dark', 'water', 'physical'],
        'immunities': ['sleep', 'confuse', 'stun', 'slow'],
        'weaknesses': ['electric', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'coveveil_passage',
    'display_name': 'The Coveveil Passage',
    'seed': abs(hash('coveveil_passage')),
    'floor_count': 1,
    'rooms_per_floor': 4,
    'room_size_min_max': (55, 110),
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
    'visible_distance': 7,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}