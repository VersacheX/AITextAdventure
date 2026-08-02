"""Shallows Mid City — Lanternfade Echo Dungeon Seed (Type E)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# shallows_mid_city_type_e_defeat_lanternfade_echo.py
# City: The Lanternhouse (shallows_mid, Ch.11)
# Chain: Type E — Artifact (Tidekin Seal)
# Player level at encounter: ~55
# Pattern: A — boss guards seal in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#304858'
IMPASSABLE_COLOR = '#0e181e'
BORDER_TILE      = '·'
BORDER_COLOR     = '#203848'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'lanternfade_echo', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['fade_drifter', 'signal_shade', 'lantern_revenant', 'void_lantern'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'fade_drifter',
        'name': 'Fade Drifter',
        'hostile_type': 'undead',
        'min_spawn_level': 53,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 382,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (106, 336),
        'basic_attack': 'strikes while fading in and out of the signal',
        'strong_attack': 'fade strike',
        'player_abilities': [],
        'base_str': 36, 'base_dex': 34, 'base_con': 28, 'base_int': 14,
        'base_hp': 740, 'base_ap': 13,
        'str_per_level': 4, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'signal_shade',
        'name': 'Signal Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 54,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 466,
        'common_drop': 'stimulant_med',
        'rare_drop': 'herb_med',
        'money_range': (128, 406),
        'basic_attack': 'sends a false signal that leads into a strike',
        'strong_attack': 'false signal',
        'player_abilities': [],
        'base_str': 22, 'base_dex': 40, 'base_con': 24, 'base_int': 26,
        'base_hp': 755, 'base_ap': 13,
        'str_per_level': 1, 'dex_per_level': 4, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark'],
        'immunities': ['confuse', 'sleep'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'lantern_revenant',
        'name': 'Lantern Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 55,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 592,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (158, 502),
        'basic_attack': 'dims the lantern and crashes into the gap',
        'strong_attack': 'lantern crush',
        'player_abilities': [],
        'base_str': 28, 'base_dex': 16, 'base_con': 46, 'base_int': 14,
        'base_hp': 980, 'base_ap': 13,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 5, 'int_per_level': 1,
        'resistances': ['dark', 'water', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'void_lantern',
        'name': 'Void Lantern',
        'hostile_type': 'elemental',
        'min_spawn_level': 55,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 798,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (188, 600),
        'basic_attack': 'burns with a void-infused lantern beam',
        'strong_attack': 'void beacon',
        'player_abilities': [],
        'base_str': 34, 'base_dex': 38, 'base_con': 28, 'base_int': 32,
        'base_hp': 920, 'base_ap': 14,
        'str_per_level': 3, 'dex_per_level': 4, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'electric'],
    },
]

BOSS_MOB: Dict = {
    'id': 'lanternfade_echo_boss',
    'name': 'The Lanternfade Echo',
    'hostiles': ['lanternfade_echo_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'lanternfade_echo_1',
        'name': 'The Lanternfade Echo',
        'hostile_type': 'elemental',
        'min_spawn_level': 56,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 13000,
        'common_drop': 'stimulant_med',
        'rare_drop': 'stimulant_med',
        'money_range': (320, 960),
        'basic_attack': 'drowns the undertunnel in false lantern signals',
        'strong_attack': 'lanternfade collapse',
        'player_abilities': [],
        'base_str': 42, 'base_dex': 46, 'base_con': 38, 'base_int': 44,
        'base_hp': 18000, 'base_ap': 260,
        'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 5,
        'resistances': ['dark', 'water', 'physical'],
        'immunities': ['sleep', 'confuse', 'slow', 'stun'],
        'weaknesses': ['light', 'electric'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'shallows_mid_city_type_e_defeat_lanternfade_echo',
    'display_name': 'The Undertunnel',
    'seed': abs(hash('shallows_mid_city_type_e_defeat_lanternfade_echo')),
    'floor_count': 1,
    'rooms_per_floor': 3,
    'room_size_min_max': (55, 100),
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