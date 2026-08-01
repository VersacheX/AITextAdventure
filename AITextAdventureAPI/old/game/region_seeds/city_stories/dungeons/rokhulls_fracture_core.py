"""Mountains Mid City — Rokhuld's Fracture Core Dungeon Seed (Type B)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# rokhulls_fracture_core.py
# City: Gallows Rift (mountains_mid, Ch.17)
# Chain: Type B — Regional Boss / Void Gauntlet (Bragg)
# Player level at encounter: ~85
# Pattern: B — player teleported to final_chamber; boss = rokhuld_b1
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = '#585848'
IMPASSABLE_COLOR = '#1c1c18'
BORDER_TILE      = '·'
BORDER_COLOR     = '#404038'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'rokhuld', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['fracture_shard', 'drill_shade', 'core_sentinel', 'void_fracture'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'fracture_shard',
        'name': 'Fracture Shard',
        'hostile_type': 'elemental',
        'min_spawn_level': 83,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 610,
        'common_drop': 'herb_large',
        'rare_drop': None,
        'money_range': (165, 528),
        'basic_attack': 'drives a fracture-edged shard through the target',
        'strong_attack': 'fracture burst',
        'player_abilities': [],
        'base_str': 60, 'base_dex': 52, 'base_con': 44, 'base_int': 20,
        'base_hp': 1160, 'base_ap': 17,
        'str_per_level': 6, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['earth', 'physical'],
        'immunities': ['slow', 'stun'],
        'weaknesses': ['electric', 'light'],
    },
    {
        'id': 'drill_shade',
        'name': 'Drill Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 84,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 744,
        'common_drop': 'remedy_large',
        'rare_drop': 'herb_large',
        'money_range': (198, 634),
        'basic_attack': 'bores through defenses with a drill-pattern strike',
        'strong_attack': 'drill drain',
        'player_abilities': [],
        'base_str': 36, 'base_dex': 62, 'base_con': 36, 'base_int': 42,
        'base_hp': 1175, 'base_ap': 17,
        'str_per_level': 1, 'dex_per_level': 6, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'core_sentinel',
        'name': 'Core Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 85,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 944,
        'common_drop': 'stimulant_large',
        'rare_drop': 'remedy_large',
        'money_range': (248, 792),
        'basic_attack': 'holds the core passage and drives mountain-iron fists forward',
        'strong_attack': 'core press',
        'player_abilities': [],
        'base_str': 44, 'base_dex': 24, 'base_con': 76, 'base_int': 16,
        'base_hp': 1580, 'base_ap': 17,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 7, 'int_per_level': 1,
        'resistances': ['earth', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['electric', 'light'],
    },
    {
        'id': 'void_fracture',
        'name': 'Void Fracture',
        'hostile_type': 'elemental',
        'min_spawn_level': 85,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 1272,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (298, 952),
        'basic_attack': 'opens a void-fracture in the mountain and strikes through it',
        'strong_attack': 'void core collapse',
        'player_abilities': [],
        'base_str': 54, 'base_dex': 58, 'base_con': 46, 'base_int': 54,
        'base_hp': 1480, 'base_ap': 19,
        'str_per_level': 5, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 5,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['electric', 'light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'rokhuld_boss',
    'name': 'Rokhuld the Core-Breaker',
    'hostiles': ['rokhuld_b1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'rokhuld_b1',
        'name': 'Rokhuld the Core-Breaker',
        'hostile_type': 'humanoid',
        'min_spawn_level': 87,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 42000,
        'common_drop': 'remedy_large',
        'rare_drop': 'remedy_large',
        'money_range': (1020, 3060),
        'basic_attack': 'drives the fracture-drill through the mountain core in a directed collapse',
        'strong_attack': 'core breaking',
        'player_abilities': [],
        'base_str': 70, 'base_dex': 62, 'base_con': 66, 'base_int': 60,
        'base_hp': 52000, 'base_ap': 720,
        'str_per_level': 7, 'dex_per_level': 6, 'con_per_level': 6, 'int_per_level': 6,
        'resistances': ['earth', 'physical', 'dark'],
        'immunities': ['sleep', 'confuse', 'fear', 'stun', 'slow'],
        'weaknesses': ['electric', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'rokhulls_fracture_core',
    'display_name': "Rokhuld's Fracture Core",
    'seed': abs(hash('rokhulls_fracture_core')),
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