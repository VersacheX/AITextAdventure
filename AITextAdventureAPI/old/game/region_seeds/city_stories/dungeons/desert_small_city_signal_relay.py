"""Desert Small City — Signal Relay Dungeon Seed (Type E + Type D shared)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# desert_small_city_signal_relay.py
# City: BioHazard Bazaar (desert_small, Ch.9)
# Chain: Type E (signal_wraith) + Type D (signal_wraith_2) — shared dungeon
# Player level at encounter: ~45
# Pattern: A — both wraith NPCs in final_chamber; story triggers each in turn
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#506050'
IMPASSABLE_COLOR = '#181e18'
BORDER_TILE      = '·'
BORDER_COLOR     = '#384838'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'signal_wraith',   'location': 'final_chamber'},
    {'id': 'signal_wraith_2', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['relay_husk', 'static_shade', 'frequency_revenant', 'void_signal'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'relay_husk',
        'name': 'Relay Husk',
        'hostile_type': 'construct',
        'min_spawn_level': 43,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 292,
        'common_drop': 'herb_large',
        'rare_drop': None,
        'money_range': (76, 240),
        'basic_attack': 'transmits a relay shock through contact',
        'strong_attack': 'relay discharge',
        'player_abilities': [],
        'base_str': 30, 'base_dex': 26, 'base_con': 24, 'base_int': 14,
        'base_hp': 580, 'base_ap': 11,
        'str_per_level': 3, 'dex_per_level': 2, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['electric', 'physical'],
        'immunities': ['stun'],
        'weaknesses': ['fire', 'water'],
    },
    {
        'id': 'static_shade',
        'name': 'Static Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 44,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 356,
        'common_drop': 'remedy_med',
        'rare_drop': 'herb_large',
        'money_range': (88, 282),
        'basic_attack': 'disrupts with a static-charged strike',
        'strong_attack': 'static burst',
        'player_abilities': [],
        'base_str': 18, 'base_dex': 32, 'base_con': 20, 'base_int': 20,
        'base_hp': 595, 'base_ap': 11,
        'str_per_level': 1, 'dex_per_level': 4, 'con_per_level': 2, 'int_per_level': 2,
        'resistances': ['electric', 'dark'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'water'],
    },
    {
        'id': 'frequency_revenant',
        'name': 'Frequency Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 45,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 452,
        'common_drop': 'stimulant_large',
        'rare_drop': 'remedy_large',
        'money_range': (108, 346),
        'basic_attack': 'resonates at a frequency that disrupts armor',
        'strong_attack': 'frequency shatter',
        'player_abilities': [],
        'base_str': 22, 'base_dex': 14, 'base_con': 38, 'base_int': 16,
        'base_hp': 780, 'base_ap': 11,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 5, 'int_per_level': 2,
        'resistances': ['electric', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['fire', 'water'],
    },
    {
        'id': 'void_signal',
        'name': 'Void Signal',
        'hostile_type': 'elemental',
        'min_spawn_level': 45,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 608,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (145, 464),
        'basic_attack': 'sends a void-infused broadcast through the relay network',
        'strong_attack': 'void broadcast',
        'player_abilities': [],
        'base_str': 28, 'base_dex': 32, 'base_con': 24, 'base_int': 28,
        'base_hp': 720, 'base_ap': 12,
        'str_per_level': 3, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark', 'electric'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'water'],
    },
]

BOSS_MOB: Dict = {
    'id': 'signal_wraith_boss',
    'name': 'The Signal Wraith',
    'hostiles': ['signal_wraith_combat'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'signal_wraith_combat',
        'name': 'The Signal Wraith',
        'hostile_type': 'elemental',
        'min_spawn_level': 46,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 9800,
        'common_drop': 'remedy_large',
        'rare_drop': 'remedy_large',
        'money_range': (245, 735),
        'basic_attack': 'floods the relay with every transaction ever recorded',
        'strong_attack': 'frequency devour',
        'player_abilities': [],
        'base_str': 36, 'base_dex': 40, 'base_con': 34, 'base_int': 40,
        'base_hp': 13000, 'base_ap': 210,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 4, 'int_per_level': 5,
        'resistances': ['electric', 'dark', 'physical'],
        'immunities': ['sleep', 'confuse', 'stun', 'slow'],
        'weaknesses': ['light', 'water'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'desert_small_city_signal_relay',
    'display_name': 'The Signal Relay',
    'seed': abs(hash('desert_small_city_signal_relay')),
    'floor_count': 1,
    'rooms_per_floor': 4,
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