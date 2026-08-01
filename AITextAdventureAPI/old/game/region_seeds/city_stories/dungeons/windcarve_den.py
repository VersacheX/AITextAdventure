"""Grassland Large City — Windcarve Den Dungeon Seed (Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# windcarve_den.py
# City: The Noble Bazaar (grassland_large, Ch.10)
# Chain: Type D — Mythic Armor (Windcarver's Mantle)
# Player level at encounter: ~50
# Pattern: A — boss guards wind-crystal in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = '#708050'
IMPASSABLE_COLOR = '#242a18'
BORDER_TILE      = '·'
BORDER_COLOR     = '#506038'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'windcarve_spirit', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['plains_stalker', 'wind_wraith', 'migration_specter', 'windcarve_revenant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'plains_stalker',
        'name': 'Plains Stalker',
        'hostile_type': 'humanoid',
        'min_spawn_level': 48,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 334,
        'common_drop': 'herb_large',
        'rare_drop': None,
        'money_range': (88, 280),
        'basic_attack': 'drives a wind-hardened blade through the gap',
        'strong_attack': 'plains ambush',
        'player_abilities': [],
        'base_str': 34, 'base_dex': 30, 'base_con': 26, 'base_int': 10,
        'base_hp': 660, 'base_ap': 12,
        'str_per_level': 4, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 0,
        'resistances': ['physical'],
        'immunities': [],
        'weaknesses': ['electric', 'ice'],
    },
    {
        'id': 'wind_wraith',
        'name': 'Wind Wraith',
        'hostile_type': 'undead',
        'min_spawn_level': 49,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 408,
        'common_drop': 'remedy_large',
        'rare_drop': 'herb_large',
        'money_range': (108, 342),
        'basic_attack': 'cuts with a blade of compressed wind',
        'strong_attack': 'wind slash',
        'player_abilities': [],
        'base_str': 22, 'base_dex': 38, 'base_con': 22, 'base_int': 18,
        'base_hp': 670, 'base_ap': 12,
        'str_per_level': 1, 'dex_per_level': 4, 'con_per_level': 2, 'int_per_level': 2,
        'resistances': ['air', 'dark'],
        'immunities': ['slow', 'sleep'],
        'weaknesses': ['electric', 'ice'],
    },
    {
        'id': 'migration_specter',
        'name': 'Migration Specter',
        'hostile_type': 'undead',
        'min_spawn_level': 50,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 518,
        'common_drop': 'stimulant_large',
        'rare_drop': 'remedy_large',
        'money_range': (132, 420),
        'basic_attack': 'crashes forward on a phantom migration path',
        'strong_attack': 'route crash',
        'player_abilities': [],
        'base_str': 26, 'base_dex': 16, 'base_con': 42, 'base_int': 12,
        'base_hp': 880, 'base_ap': 12,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 5, 'int_per_level': 1,
        'resistances': ['physical', 'air'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['electric'],
    },
    {
        'id': 'windcarve_revenant',
        'name': 'Windcarve Revenant',
        'hostile_type': 'elemental',
        'min_spawn_level': 50,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 698,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (165, 530),
        'basic_attack': 'carves through armor on winds older than the first caravan',
        'strong_attack': 'windcarve surge',
        'player_abilities': [],
        'base_str': 32, 'base_dex': 36, 'base_con': 26, 'base_int': 24,
        'base_hp': 820, 'base_ap': 13,
        'str_per_level': 3, 'dex_per_level': 4, 'con_per_level': 2, 'int_per_level': 2,
        'resistances': ['air', 'dark'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['electric', 'ice'],
    },
]

BOSS_MOB: Dict = {
    'id': 'windcarve_spirit_boss',
    'name': 'The Windcarve Spirit',
    'hostiles': ['windcarve_spirit_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'windcarve_spirit_1',
        'name': 'The Windcarve Spirit',
        'hostile_type': 'elemental',
        'min_spawn_level': 51,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 11500,
        'common_drop': 'remedy_large',
        'rare_drop': 'remedy_large',
        'money_range': (280, 840),
        'basic_attack': 'fills the den with the oldest migration winds on the plains',
        'strong_attack': 'windcarve dominion',
        'player_abilities': [],
        'base_str': 40, 'base_dex': 46, 'base_con': 36, 'base_int': 38,
        'base_hp': 15500, 'base_ap': 230,
        'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 4,
        'resistances': ['air', 'dark', 'physical'],
        'immunities': ['sleep', 'slow', 'confuse', 'stun'],
        'weaknesses': ['electric', 'ice'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'windcarve_den',
    'display_name': 'The Windcarve Den',
    'seed': abs(hash('windcarve_den')),
    'floor_count': 1,
    'rooms_per_floor': 4,
    'room_size_min_max': (60, 110),
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
    'visible_distance': 8,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}