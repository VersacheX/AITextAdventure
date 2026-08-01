"""Snow Mid City — Rimechant Hall Dungeon Seed (Type E)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# snow_mid_city_rimechant_hall.py
# City: Hailward Hold (snow_mid, Ch.15)
# Chain: Type E — Artifact (Pageant Decree Shard)
# Player level at encounter: ~75
# Pattern: A — boss guards decree shard in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#586878'
IMPASSABLE_COLOR = '#1c2228'
BORDER_TILE      = '·'
BORDER_COLOR     = '#3c5060'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'rimechant_echo', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['chant_drifter', 'decree_shade', 'hall_sentinel', 'void_chant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'chant_drifter',
        'name': 'Chant Drifter',
        'hostile_type': 'undead',
        'min_spawn_level': 73,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 534,
        'common_drop': 'herb_large',
        'rare_drop': None,
        'money_range': (144, 460),
        'basic_attack': 'strikes with the resonant force of a half-remembered chant',
        'strong_attack': 'chant strike',
        'player_abilities': [],
        'base_str': 52, 'base_dex': 46, 'base_con': 38, 'base_int': 18,
        'base_hp': 1020, 'base_ap': 15,
        'str_per_level': 5, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['ice', 'dark'],
        'immunities': ['sleep', 'slow'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'decree_shade',
        'name': 'Decree Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 74,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 652,
        'common_drop': 'remedy_large',
        'rare_drop': 'herb_large',
        'money_range': (174, 556),
        'basic_attack': 'lashes with the chain of an unanswered formal decree',
        'strong_attack': 'decree bind',
        'player_abilities': [],
        'base_str': 32, 'base_dex': 56, 'base_con': 32, 'base_int': 38,
        'base_hp': 1035, 'base_ap': 15,
        'str_per_level': 1, 'dex_per_level': 5, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'ice'],
        'immunities': ['confuse', 'sleep'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'hall_sentinel',
        'name': 'Hall Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 75,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 828,
        'common_drop': 'stimulant_large',
        'rare_drop': 'remedy_large',
        'money_range': (218, 696),
        'basic_attack': 'stands in the hall passage and drives ice-plated fists forward',
        'strong_attack': 'hall press',
        'player_abilities': [],
        'base_str': 38, 'base_dex': 22, 'base_con': 66, 'base_int': 14,
        'base_hp': 1380, 'base_ap': 15,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 6, 'int_per_level': 1,
        'resistances': ['ice', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['fire', 'electric'],
    },
    {
        'id': 'void_chant',
        'name': 'Void Chant',
        'hostile_type': 'elemental',
        'min_spawn_level': 75,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 1114,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (260, 832),
        'basic_attack': 'weaponizes a void-infused ancestral chant into a directed strike',
        'strong_attack': 'void decree',
        'player_abilities': [],
        'base_str': 48, 'base_dex': 52, 'base_con': 40, 'base_int': 48,
        'base_hp': 1290, 'base_ap': 17,
        'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 3, 'int_per_level': 5,
        'resistances': ['dark', 'ice'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['fire', 'light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'rimechant_echo_boss',
    'name': 'The Rimechant Echo',
    'hostiles': ['rimechant_echo_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'rimechant_echo_1',
        'name': 'The Rimechant Echo',
        'hostile_type': 'elemental',
        'min_spawn_level': 76,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 35000,
        'common_drop': 'remedy_large',
        'rare_drop': 'remedy_large',
        'money_range': (855, 2565),
        'basic_attack': 'fills the hall with the resonance of every decree it has absorbed since the Shard was lost',
        'strong_attack': 'rimechant collapse',
        'player_abilities': [],
        'base_str': 60, 'base_dex': 58, 'base_con': 54, 'base_int': 64,
        'base_hp': 42000, 'base_ap': 600,
        'str_per_level': 6, 'dex_per_level': 5, 'con_per_level': 5, 'int_per_level': 6,
        'resistances': ['dark', 'ice', 'physical'],
        'immunities': ['sleep', 'confuse', 'fear', 'stun', 'slow'],
        'weaknesses': ['fire', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'snow_mid_city_rimechant_hall',
    'display_name': 'The Rimechant Hall',
    'seed': abs(hash('snow_mid_city_rimechant_hall')),
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
    'visible_distance': 7,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}