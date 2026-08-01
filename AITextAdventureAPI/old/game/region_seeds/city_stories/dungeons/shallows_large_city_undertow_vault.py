"""Shallows Large City — Undertow Vault Dungeon Seed (Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# shallows_large_city_undertow_vault.py
# City: Blackwake Harbor (shallows_large, Ch.5)
# Chain: Type D — Mythic Weapon (Tidecleaver)
# Player level at encounter: ~25
# Pattern: A — boss guards drowned steel in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = '#205060'
IMPASSABLE_COLOR = '#0a1820'
BORDER_TILE      = '·'
BORDER_COLOR     = '#183848'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'undertow_voice', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',    'location': 'treasure_room'},
    {'id': 'stimulant_med', 'location': 'treasure_room'},
    {'id': 'remedy_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['vault_drifter', 'brine_shade', 'undertow_stalker', 'harbor_revenant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'vault_drifter',
        'name': 'Vault Drifter',
        'hostile_type': 'undead',
        'min_spawn_level': 23,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 168,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (28, 88),
        'basic_attack': 'drifts forward and strikes with tide-cold hands',
        'strong_attack': 'vault drag',
        'player_abilities': [],
        'base_str': 14, 'base_dex': 15, 'base_con': 12, 'base_int': 5,
        'base_hp': 270, 'base_ap': 7,
        'str_per_level': 2, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 0,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'brine_shade',
        'name': 'Brine Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 24,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 210,
        'common_drop': 'remedy_med',
        'rare_drop': 'herb_med',
        'money_range': (34, 108),
        'basic_attack': 'corrodes armor with brine-saturated strikes',
        'strong_attack': 'brine corrode',
        'player_abilities': [],
        'base_str': 8, 'base_dex': 14, 'base_con': 10, 'base_int': 10,
        'base_hp': 285, 'base_ap': 7,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['water', 'dark'],
        'immunities': ['poison'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'undertow_stalker',
        'name': 'Undertow Stalker',
        'hostile_type': 'beast',
        'min_spawn_level': 25,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 272,
        'common_drop': 'stimulant_med',
        'rare_drop': 'remedy_med',
        'money_range': (44, 138),
        'basic_attack': 'crashes with the force of a pulling undertow',
        'strong_attack': 'undertow slam',
        'player_abilities': [],
        'base_str': 13, 'base_dex': 8, 'base_con': 22, 'base_int': 3,
        'base_hp': 405, 'base_ap': 7,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 4, 'int_per_level': 0,
        'resistances': ['water', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['electric'],
    },
    {
        'id': 'harbor_revenant',
        'name': 'Harbor Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 25,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 368,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (62, 196),
        'basic_attack': 'strikes with the last bearings of every drowned navigator',
        'strong_attack': "navigator's curse",
        'player_abilities': [],
        'base_str': 16, 'base_dex': 18, 'base_con': 13, 'base_int': 12,
        'base_hp': 355, 'base_ap': 8,
        'str_per_level': 2, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'electric'],
    },
]

BOSS_MOB: Dict = {
    'id': 'undertow_voice_boss',
    'name': 'The Undertow Voice',
    'hostiles': ['undertow_voice_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'undertow_voice_1',
        'name': 'The Undertow Voice',
        'hostile_type': 'elemental',
        'min_spawn_level': 26,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 5800,
        'common_drop': 'remedy_med',
        'rare_drop': 'remedy_large',
        'money_range': (155, 445),
        'basic_attack': 'pulls the chamber into a concentrated undertow surge',
        'strong_attack': "drowned navigator's tide",
        'player_abilities': [],
        'base_str': 18, 'base_dex': 22, 'base_con': 20, 'base_int': 24,
        'base_hp': 7500, 'base_ap': 148,
        'str_per_level': 2, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['water', 'dark', 'physical'],
        'immunities': ['sleep', 'confuse', 'slow', 'stun'],
        'weaknesses': ['light', 'electric'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'shallows_large_city_undertow_vault',
    'display_name': 'The Undertow Vault',
    'seed': abs(hash('shallows_large_city_undertow_vault')),
    'floor_count': 1,
    'rooms_per_floor': 4,
    'room_size_min_max': (60, 110),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.07,
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