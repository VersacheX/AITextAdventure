"""Swamp Small City — Rotfen Hideaway Dungeon Seed (Type A / Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# rotfen_hideaway.py
# City: Gnashwater Hollow (swamp_small, Ch.7)
# Chain: Type A slot 2 (rotfen_voice meet) + Type D (rotfen_voice_1 defeat)
# Player level at encounter: ~35
# Pattern: A — both voice NPCs placed in final_chamber; story triggers each
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.12
OPEN_AREA_COLOR  = '#3a4820'
IMPASSABLE_COLOR = '#121808'
BORDER_TILE      = '·'
BORDER_COLOR     = '#283510'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'rotfen_voice',   'location': 'final_chamber'},
    {'id': 'rotfen_voice_1', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'petrify_salve',      'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['bog_lurker', 'rot_walker', 'mire_creep', 'void_rot'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'bog_lurker',
        'name': 'Bog Lurker',
        'hostile_type': 'beast',
        'min_spawn_level': 32,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 210,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (55, 140),
        'basic_attack': 'lunges from the bog with a foul-smelling strike',
        'strong_attack': 'bog lunge',
        'player_abilities': [],
        'base_str': 22, 'base_dex': 18, 'base_con': 16, 'base_int': 3,
        'base_hp': 380, 'base_ap': 9,
        'str_per_level': 3, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 0,
        'resistances': ['water', 'earth'],
        'immunities': ['slow'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'rot_walker',
        'name': 'Rot Walker',
        'hostile_type': 'undead',
        'min_spawn_level': 33,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 248,
        'common_drop': 'ointment',
        'rare_drop': 'petrify_salve',
        'money_range': (62, 155),
        'basic_attack': 'strikes with a rot-drenched limb',
        'strong_attack': 'rot drain',
        'player_abilities': [],
        'base_str': 14, 'base_dex': 16, 'base_con': 14, 'base_int': 8,
        'base_hp': 400, 'base_ap': 9,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['dark', 'earth'],
        'immunities': ['poison', 'sleep'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'mire_creep',
        'name': 'Mire Creep',
        'hostile_type': 'beast',
        'min_spawn_level': 34,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 298,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (80, 200),
        'basic_attack': 'envelops and squeezes with swamp-hardened bulk',
        'strong_attack': 'mire crush',
        'player_abilities': [],
        'base_str': 18, 'base_dex': 8, 'base_con': 28, 'base_int': 3,
        'base_hp': 560, 'base_ap': 9,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 5, 'int_per_level': 0,
        'resistances': ['earth', 'water', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['fire'],
    },
    {
        'id': 'void_rot',
        'name': 'Void Rot',
        'hostile_type': 'elemental',
        'min_spawn_level': 35,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 375,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (110, 280),
        'basic_attack': 'channels void-corruption through the rot into a strike',
        'strong_attack': 'void rot surge',
        'player_abilities': [],
        'base_str': 20, 'base_dex': 22, 'base_con': 17, 'base_int': 16,
        'base_hp': 500, 'base_ap': 10,
        'str_per_level': 2, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 2,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'fire'],
    },
]

BOSS_MOB: Dict = {
    'id': 'rotfen_voice_boss',
    'name': 'The Rotfen Voice',
    'hostiles': ['rotfen_voice_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'rotfen_voice_1',
        'name': 'The Rotfen Voice',
        'hostile_type': 'elemental',
        'min_spawn_level': 36,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 7200,
        'common_drop': 'stimulant_med',
        'rare_drop': 'stimulant_med',
        'money_range': (185, 550),
        'basic_attack': 'floods the hideaway with churning lost routes',
        'strong_attack': 'swallowed path',
        'player_abilities': [],
        'base_str': 26, 'base_dex': 28, 'base_con': 24, 'base_int': 22,
        'base_hp': 9200, 'base_ap': 168,
        'str_per_level': 3, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 2,
        'resistances': ['dark', 'earth', 'water'],
        'immunities': ['poison', 'sleep', 'slow', 'confuse'],
        'weaknesses': ['light', 'fire'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'rotfen_hideaway',
    'display_name': 'The Rotfen Hideaway',
    'seed': abs(hash('rotfen_hideaway')),
    'floor_count': 1,
    'rooms_per_floor': 4,
    'room_size_min_max': (55, 100),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.08,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (2, 5),
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