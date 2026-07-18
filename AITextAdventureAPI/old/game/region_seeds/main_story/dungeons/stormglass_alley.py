"""
Stormglass Alley - Chapter 5 Dungeon Seed Configuration
A narrow, crackling alley where reality thins, filled with static wraiths.
"""

from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "▒"
IMPASSABLE_TILE = "█"
IMPASSABLE_CHANCE = 0.05
OPEN_AREA_COLOR  = "#5a8aaa"
IMPASSABLE_COLOR = "#1a2a3a"
BORDER_TILE      = "·"
BORDER_COLOR     = "#3a6080"

# Hostiles
FLOOR_HOSTILES = {
    1: ['arc_rat', 'volt_gecko'],
}

HOSTILE_SEEDS = [
    {
        'id': 'arc_rat',
        'name': 'Arc Rat',
        'hostile_type': 'beast',
        'min_spawn_level': 24,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 150,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (15, 30),
        'basic_attack': 'volt bite',
        'strong_attack': 'rabid lunge',
        'player_abilities': [],
        'base_str': 10, 'base_dex': 15, 'base_con': 10, 'base_int': 5,
        'base_hp': 300, 'base_ap': 30,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 1,
        'resistances': ['electric'], 'immunities': [], 'weaknesses': ['earth']
    },
    {
        'id': 'volt_gecko',
        'name': 'Volt Gecko',
        'hostile_type': 'beast',
        'min_spawn_level': 24,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 170,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (20, 35),
        'basic_attack': 'static claw',
        'strong_attack': 'shocking gaze',
        'player_abilities': ['electric_tech_lv1_taze_charge'],
        'base_str': 9, 'base_dex': 17, 'base_con': 11, 'base_int': 12,
        'base_hp': 330, 'base_ap': 32,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 2,
        'resistances': ['electric'], 'immunities': [], 'weaknesses': ['earth']
    }
]

# This dungeon is for a specific combat encounter
DUNGEON_NPCS = [ {'id': 'static_wraith', 'location': 'final_chamber'} ]
BOSS_MOB = {
    'id': 'static_wraith_mob',
    'name': 'Static Wraiths',
    'hostiles': ['static_wraith', 'static_wraith', 'static_wraith']
}

BOSS_HOSTILES = [
    {
        'id': 'static_wraith',
        'name': 'Static Wraith',
        'hostile_type': 'spirit',
        'min_spawn_level': 25,
        'role': 'hazard',
        'rarity': 'rare',
        'base_xp': 180,
        'common_drop': 'stimulant_small',
        'rare_drop': 'stormglass_ember',
        'money_range': (20, 40),
        'basic_attack': 'static shock',
        'strong_attack': 'energy surge',
        'player_abilities': [],
        'base_str': 8, 'base_dex': 18, 'base_con': 10, 'base_int': 14,
        'base_hp': 350, 'base_ap': 30,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 2,
        'resistances': ['electric'], 'immunities': [], 'weaknesses': ['earth']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'stormglass_alley',
    'seed': abs(hash('stormglass_alley')),
    'floor_count': 1,
    'room_size_min_max': (40, 80),
    'rooms_per_floor': 8,
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.0,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (1, 2),
    'display_name': "Stormglass Alley",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color':  OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile':      BORDER_TILE,
    'border_color':     BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': [{'id': 'static_wraith_mob', 'location': 'final_chamber'}],
    'items': [
        {'id': 'stimulant_med', 'location': 'treasure_room'},
        {'id': 'tome_dex', 'location': 'treasure_room'}
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 5,
}