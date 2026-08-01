"""Grassland Mid City — Sanctum Vault Dungeon Seed (Type E)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# grassland_mid_city_sanctum_vault.py
# City: Highsteeple (grassland_mid, Ch.3)
# Chain: Type E — Artifact (Sanctum Seal Fragment)
# Player level at encounter: ~15
# Pattern: A — boss guards seal in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = '#7a7040'
IMPASSABLE_COLOR = '#2e2a18'
BORDER_TILE      = '·'
BORDER_COLOR     = '#585030'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'sanctum_voice', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',     'location': 'treasure_room'},
    {'id': 'remedy_small', 'location': 'treasure_room'},
    {'id': 'remedy_med',   'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['doctrine_guard', 'vow_shade', 'false_verse_echo', 'sanctum_revenant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'doctrine_guard',
        'name': 'Doctrine Guard',
        'hostile_type': 'humanoid',
        'min_spawn_level': 13,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 95,
        'common_drop': 'herb_small',
        'rare_drop': None,
        'money_range': (18, 55),
        'basic_attack': 'strikes with a doctrine-branded weapon',
        'strong_attack': 'doctrine slash',
        'player_abilities': [],
        'base_str': 8, 'base_dex': 6, 'base_con': 7, 'base_int': 4,
        'base_hp': 110, 'base_ap': 5,
        'str_per_level': 2, 'dex_per_level': 1, 'con_per_level': 2, 'int_per_level': 0,
        'resistances': [],
        'immunities': [],
        'weaknesses': ['dark'],
    },
    {
        'id': 'vow_shade',
        'name': 'Vow Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 14,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 122,
        'common_drop': 'remedy_small',
        'rare_drop': 'herb_med',
        'money_range': (22, 68),
        'basic_attack': 'lashes with a chain of broken vows',
        'strong_attack': 'oath break',
        'player_abilities': [],
        'base_str': 5, 'base_dex': 7, 'base_con': 5, 'base_int': 6,
        'base_hp': 130, 'base_ap': 5,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 1,
        'resistances': ['dark'],
        'immunities': ['sleep'],
        'weaknesses': ['light'],
    },
    {
        'id': 'false_verse_echo',
        'name': 'False Verse Echo',
        'hostile_type': 'undead',
        'min_spawn_level': 15,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 158,
        'common_drop': 'stimulant_med',
        'rare_drop': 'remedy_med',
        'money_range': (28, 88),
        'basic_attack': 'slams with the weight of a corrupted doctrine',
        'strong_attack': 'false verse crush',
        'player_abilities': [],
        'base_str': 7, 'base_dex': 3, 'base_con': 12, 'base_int': 5,
        'base_hp': 180, 'base_ap': 5,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 4, 'int_per_level': 1,
        'resistances': ['physical'],
        'immunities': ['stun'],
        'weaknesses': ['light'],
    },
    {
        'id': 'sanctum_revenant',
        'name': 'Sanctum Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 15,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 212,
        'common_drop': 'herb_med',
        'rare_drop': 'remedy_med',
        'money_range': (40, 128),
        'basic_attack': 'channels broken oaths into a directed strike',
        'strong_attack': 'sanctum rupture',
        'player_abilities': [],
        'base_str': 9, 'base_dex': 10, 'base_con': 7, 'base_int': 8,
        'base_hp': 160, 'base_ap': 6,
        'str_per_level': 2, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 1,
        'resistances': ['dark'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'sanctum_voice_boss',
    'name': 'The Sanctum Voice',
    'hostiles': ['sanctum_voice_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'sanctum_voice_1',
        'name': 'The Sanctum Voice',
        'hostile_type': 'undead',
        'min_spawn_level': 16,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 3200,
        'common_drop': 'remedy_med',
        'rare_drop': 'remedy_med',
        'money_range': (100, 280),
        'basic_attack': 'fills the chamber with the crushing weight of broken vows',
        'strong_attack': 'voice of the false verse',
        'player_abilities': [],
        'base_str': 12, 'base_dex': 14, 'base_con': 12, 'base_int': 18,
        'base_hp': 4200, 'base_ap': 100,
        'str_per_level': 2, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark', 'physical'],
        'immunities': ['sleep', 'confuse', 'stun'],
        'weaknesses': ['light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'grassland_mid_city_sanctum_vault',
    'display_name': 'The Sanctum Vault',
    'seed': abs(hash('grassland_mid_city_sanctum_vault')),
    'floor_count': 1,
    'rooms_per_floor': 3,
    'room_size_min_max': (55, 100),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.06,
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