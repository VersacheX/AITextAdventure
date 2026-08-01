"""Shallows Mid City — Undertunnel Voice Dungeon Seed (Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# shallows_mid_city_type_d_defeat_undertunnel_voice.py
# City: The Lanternhouse (shallows_mid, Ch.11)
# Chain: Type D — Mythic Weapon (Corsair's Depth Blade)
# Player level at encounter: ~55
# Pattern: A — boss guards corsair-tide steel in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#283848'
IMPASSABLE_COLOR = '#0c1218'
BORDER_TILE      = '·'
BORDER_COLOR     = '#1c2c38'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'undertunnel_voice', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['tunnel_drifter', 'corsair_shade', 'route_revenant', 'void_current'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'tunnel_drifter',
        'name': 'Tunnel Drifter',
        'hostile_type': 'undead',
        'min_spawn_level': 53,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 382,
        'common_drop': 'herb_large',
        'rare_drop': None,
        'money_range': (106, 336),
        'basic_attack': 'follows misdirected signals to strike from the wrong direction',
        'strong_attack': 'misdirect',
        'player_abilities': [],
        'base_str': 36, 'base_dex': 32, 'base_con': 28, 'base_int': 14,
        'base_hp': 735, 'base_ap': 13,
        'str_per_level': 4, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'corsair_shade',
        'name': 'Corsair Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 54,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 466,
        'common_drop': 'remedy_large',
        'rare_drop': 'herb_large',
        'money_range': (128, 406),
        'basic_attack': 'cuts with a tide-cold blade left behind by drowned corsairs',
        'strong_attack': 'corsair cut',
        'player_abilities': [],
        'base_str': 24, 'base_dex': 40, 'base_con': 22, 'base_int': 22,
        'base_hp': 748, 'base_ap': 13,
        'str_per_level': 1, 'dex_per_level': 4, 'con_per_level': 2, 'int_per_level': 2,
        'resistances': ['dark', 'water'],
        'immunities': ['confuse', 'sleep'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'route_revenant',
        'name': 'Route Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 55,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 592,
        'common_drop': 'stimulant_large',
        'rare_drop': 'remedy_large',
        'money_range': (158, 502),
        'basic_attack': 'crashes through the tunnel with the weight of every lost route',
        'strong_attack': 'lost route slam',
        'player_abilities': [],
        'base_str': 26, 'base_dex': 16, 'base_con': 48, 'base_int': 12,
        'base_hp': 990, 'base_ap': 13,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 5, 'int_per_level': 1,
        'resistances': ['water', 'physical', 'dark'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'void_current',
        'name': 'Void Current',
        'hostile_type': 'elemental',
        'min_spawn_level': 55,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 798,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (188, 600),
        'basic_attack': 'channels a void-infused tide-current into a directed strike',
        'strong_attack': 'void tide surge',
        'player_abilities': [],
        'base_str': 32, 'base_dex': 38, 'base_con': 28, 'base_int': 34,
        'base_hp': 915, 'base_ap': 14,
        'str_per_level': 3, 'dex_per_level': 4, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'electric'],
    },
]

BOSS_MOB: Dict = {
    'id': 'undertunnel_voice_boss',
    'name': 'The Undertunnel Voice',
    'hostiles': ['undertunnel_voice_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'undertunnel_voice_1',
        'name': 'The Undertunnel Voice',
        'hostile_type': 'elemental',
        'min_spawn_level': 56,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 13500,
        'common_drop': 'remedy_large',
        'rare_drop': 'remedy_large',
        'money_range': (325, 975),
        'basic_attack': 'floods the tunnel with every misdirected signal and lost smuggler route',
        'strong_attack': 'corsair tide collapse',
        'player_abilities': [],
        'base_str': 44, 'base_dex': 46, 'base_con': 40, 'base_int': 42,
        'base_hp': 18500, 'base_ap': 265,
        'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 4,
        'resistances': ['dark', 'water', 'physical'],
        'immunities': ['sleep', 'confuse', 'slow', 'stun'],
        'weaknesses': ['light', 'electric'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'shallows_mid_city_type_d_defeat_undertunnel_voice',
    'display_name': 'The Deep Undertunnel',
    'seed': abs(hash('shallows_mid_city_type_d_defeat_undertunnel_voice')),
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
    'visible_distance': 7,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}