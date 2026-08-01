"""Mountains Large City — Conduit Maw Dungeon Seed (Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# mountains_large_city_conduit_maw.py
# City: Ironveil (mountains_large, Ch.4)
# Chain: Type D — Mythic Armor (Ironveil Warplate)
# Player level at encounter: ~20
# Pattern: A — boss guards armoring-frequency in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = '#505868'
IMPASSABLE_COLOR = '#181c22'
BORDER_TILE      = '·'
BORDER_COLOR     = '#384048'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'conduit_echo', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_med', 'location': 'treasure_room'},
    {'id': 'remedy_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['relay_stalker', 'maw_creep', 'iron_revenant', 'conduit_specter'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'relay_stalker',
        'name': 'Relay Stalker',
        'hostile_type': 'construct',
        'min_spawn_level': 18,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 130,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (22, 72),
        'basic_attack': 'strikes along the relay conduits',
        'strong_attack': 'relay shock',
        'player_abilities': [],
        'base_str': 13, 'base_dex': 8, 'base_con': 11, 'base_int': 4,
        'base_hp': 195, 'base_ap': 6,
        'str_per_level': 3, 'dex_per_level': 1, 'con_per_level': 2, 'int_per_level': 0,
        'resistances': ['electric'],
        'immunities': [],
        'weaknesses': ['fire'],
    },
    {
        'id': 'maw_creep',
        'name': 'Maw Creep',
        'hostile_type': 'beast',
        'min_spawn_level': 19,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 162,
        'common_drop': 'remedy_small',
        'rare_drop': 'herb_med',
        'money_range': (28, 88),
        'basic_attack': 'scuttles forward and bites through plate',
        'strong_attack': 'conduit bite',
        'player_abilities': [],
        'base_str': 9, 'base_dex': 13, 'base_con': 8, 'base_int': 3,
        'base_hp': 170, 'base_ap': 6,
        'str_per_level': 1, 'dex_per_level': 3, 'con_per_level': 1, 'int_per_level': 0,
        'resistances': [],
        'immunities': ['slow'],
        'weaknesses': ['electric', 'light'],
    },
    {
        'id': 'iron_revenant',
        'name': 'Iron Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 20,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 212,
        'common_drop': 'stimulant_med',
        'rare_drop': 'remedy_med',
        'money_range': (36, 115),
        'basic_attack': 'charges with centuries of forge-hardened momentum',
        'strong_attack': 'iron crush',
        'player_abilities': [],
        'base_str': 11, 'base_dex': 5, 'base_con': 18, 'base_int': 4,
        'base_hp': 275, 'base_ap': 6,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 4, 'int_per_level': 0,
        'resistances': ['physical', 'fire'],
        'immunities': ['stun'],
        'weaknesses': ['electric'],
    },
    {
        'id': 'conduit_specter',
        'name': 'Conduit Specter',
        'hostile_type': 'elemental',
        'min_spawn_level': 20,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 288,
        'common_drop': 'herb_med',
        'rare_drop': 'remedy_med',
        'money_range': (52, 162),
        'basic_attack': 'fires a concentrated conduit discharge',
        'strong_attack': 'frequency collapse',
        'player_abilities': [],
        'base_str': 10, 'base_dex': 15, 'base_con': 9, 'base_int': 12,
        'base_hp': 235, 'base_ap': 7,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 2,
        'resistances': ['electric', 'dark'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'fire'],
    },
]

BOSS_MOB: Dict = {
    'id': 'conduit_echo_boss',
    'name': 'The Conduit Echo',
    'hostiles': ['conduit_echo_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'conduit_echo_1',
        'name': 'The Conduit Echo',
        'hostile_type': 'elemental',
        'min_spawn_level': 21,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 4400,
        'common_drop': 'remedy_med',
        'rare_drop': 'remedy_med',
        'money_range': (120, 350),
        'basic_attack': 'surges through the conduit network in a full-frequency discharge',
        'strong_attack': 'maw resonance',
        'player_abilities': [],
        'base_str': 16, 'base_dex': 18, 'base_con': 16, 'base_int': 20,
        'base_hp': 5800, 'base_ap': 125,
        'str_per_level': 2, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['electric', 'physical', 'dark'],
        'immunities': ['stun', 'sleep', 'confuse'],
        'weaknesses': ['light', 'fire'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'mountains_large_city_conduit_maw',
    'display_name': 'The Conduit Maw',
    'seed': abs(hash('mountains_large_city_conduit_maw')),
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