"""Snow Large City — Aeriola's Frozen Sanctum Dungeon Seed (Type B)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# aeriolass_frozen_sanctum.py
# City: Snowfall Spire (snow_large, Ch.19)
# Chain: Type B — Regional Boss / Void Gauntlet (Kor-in)
# Player level at encounter: ~95
# Pattern: B — player teleported to final_chamber; boss = aeriola_b1
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = '#5878a8'
IMPASSABLE_COLOR = '#1c2838'
BORDER_TILE      = '·'
BORDER_COLOR     = '#406090'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'aeriola', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['frozen_moment', 'glacial_shade', 'time_sentinel', 'void_frost'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'frozen_moment',
        'name': 'Frozen Moment',
        'hostile_type': 'elemental',
        'min_spawn_level': 93,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 686,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (186, 596),
        'basic_attack': 'weaponizes a stopped moment into a concussive strike',
        'strong_attack': 'moment collapse',
        'player_abilities': [],
        'base_str': 68, 'base_dex': 58, 'base_con': 52, 'base_int': 28,
        'base_hp': 1320, 'base_ap': 19,
        'str_per_level': 6, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 2,
        'resistances': ['ice', 'dark'],
        'immunities': ['slow', 'confuse'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'glacial_shade',
        'name': 'Glacial Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 94,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 836,
        'common_drop': 'stimulant_med',
        'rare_drop': 'herb_med',
        'money_range': (222, 710),
        'basic_attack': 'channels a stored frozen moment into a draining pulse',
        'strong_attack': 'glacial drain',
        'player_abilities': [],
        'base_str': 40, 'base_dex': 70, 'base_con': 42, 'base_int': 50,
        'base_hp': 1335, 'base_ap': 19,
        'str_per_level': 1, 'dex_per_level': 6, 'con_per_level': 3, 'int_per_level': 5,
        'resistances': ['ice', 'dark'],
        'immunities': ['sleep', 'confuse', 'slow'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'time_sentinel',
        'name': 'Time Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 95,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 1060,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (278, 890),
        'basic_attack': 'holds the sanctum passage and strikes with frozen-time density',
        'strong_attack': 'time press',
        'player_abilities': [],
        'base_str': 48, 'base_dex': 28, 'base_con': 86, 'base_int': 18,
        'base_hp': 1780, 'base_ap': 19,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 7, 'int_per_level': 2,
        'resistances': ['ice', 'physical'],
        'immunities': ['stun', 'slow', 'confuse'],
        'weaknesses': ['fire', 'electric'],
    },
    {
        'id': 'void_frost',
        'name': 'Void Frost',
        'hostile_type': 'elemental',
        'min_spawn_level': 95,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 1428,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (334, 1070),
        'basic_attack': 'drives void-corruption through frozen collected moments into a strike',
        'strong_attack': 'void freeze surge',
        'player_abilities': [],
        'base_str': 60, 'base_dex': 64, 'base_con': 54, 'base_int': 62,
        'base_hp': 1680, 'base_ap': 21,
        'str_per_level': 5, 'dex_per_level': 6, 'con_per_level': 4, 'int_per_level': 6,
        'resistances': ['ice', 'dark'],
        'immunities': ['sleep', 'confuse', 'slow'],
        'weaknesses': ['fire', 'light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'aeriola_boss',
    'name': 'Lady Aeriola Frostborn',
    'hostiles': ['aeriola_b1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'aeriola_b1',
        'name': 'Lady Aeriola Frostborn',
        'hostile_type': 'humanoid',
        'min_spawn_level': 97,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 55000,
        'common_drop': 'stimulant_med',
        'rare_drop': 'stimulant_med',
        'money_range': (1330, 3990),
        'basic_attack': 'releases every frozen moment she has collected into a single directed collapse',
        'strong_attack': 'temporal collection',
        'player_abilities': [],
        'base_str': 76, 'base_dex': 72, 'base_con': 72, 'base_int': 80,
        'base_hp': 66000, 'base_ap': 860,
        'str_per_level': 7, 'dex_per_level': 7, 'con_per_level': 7, 'int_per_level': 8,
        'resistances': ['ice', 'dark', 'physical'],
        'immunities': ['sleep', 'confuse', 'stun', 'slow'],
        'weaknesses': ['fire', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'aeriolass_frozen_sanctum',
    'display_name': "Aeriola's Frozen Sanctum",
    'seed': abs(hash('aeriolass_frozen_sanctum')),
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
    'visible_distance': 8,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}