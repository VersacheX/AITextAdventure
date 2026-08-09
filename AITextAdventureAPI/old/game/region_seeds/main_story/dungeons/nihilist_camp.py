"""
Nihilist Camp - Chapter 12 Dungeon Seed Configuration
A small, bleak camp where despair is the only creed.
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.05
OPEN_AREA_COLOR  = "#4a4a4a"
IMPASSABLE_COLOR = "#1e1e1e"
BORDER_TILE      = "·"
BORDER_COLOR     = "#383838"

# Hostiles
FLOOR_HOSTILES = {
    1: ['despair_cultist', 'hollow_zealot'],
}

HOSTILE_SEEDS = [
    {
        'id': 'despair_cultist', 'name': 'Despair Cultist', 'hostile_type': 'humanoid', 'min_spawn_level': 60, 'role': 'hazard', 'rarity': 'common',
        'base_xp': 700, 'common_drop': 'stimulant_med', 'rare_drop': None, 'money_range': (120, 240),
        'basic_attack': 'empty gaze', 'strong_attack': 'draining touch', 'player_abilities': ['dark_faith_lv1_shade_whisper'],
        'base_str': 30, 'base_dex': 30, 'base_con': 30, 'base_int': 30, 'base_hp': 2000, 'base_ap': 80,
        'str_per_level': 3, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 3,
        'resistances': ['dark'], 'immunities': ['stun'], 'weaknesses': ['light']
    },
    {
        'id': 'hollow_zealot', 'name': 'Hollow Zealot', 'hostile_type': 'humanoid', 'min_spawn_level': 60, 'role': 'damage', 'rarity': 'uncommon',
        'base_xp': 750, 'common_drop': 'herb_med', 'rare_drop': None, 'money_range': (140, 280),
        'basic_attack': 'void strike', 'strong_attack': 'nothingness wave', 'player_abilities': ['dark_magic_lv1_shadow_tendril'],
        'base_str': 35, 'base_dex': 25, 'base_con': 32, 'base_int': 20, 'base_hp': 2200, 'base_ap': 70,
        'str_per_level': 4, 'dex_per_level': 3, 'con_per_level': 4, 'int_per_level': 2,
        'resistances': ['dark'], 'immunities': ['confuse'], 'weaknesses': ['light']
    }
]

# Boss
DUNGEON_NPCS = [
    {'id': 'nihilist_leader', 'location': 'final_chamber'}
]
BOSS_MOB = {
    'id': 'nihilist_leader_1',
    'name': 'Nihilist Leader',
    'hostiles': ['nihilist_leader_1', 'anarchist', 'anarchist']
}

BOSS_HOSTILES = [
    {
        'id': 'nihilist_leader_1', 'name': 'Nihilist Leader', 'hostile_type': 'humanoid', 'min_spawn_level': 62, 'role': 'damage', 'rarity': 'notfound',
        'base_xp': 10000, 'common_drop': 'tome_con_superrare', 'rare_drop': 'bracelet_of_void', 'money_range': (1500, 3000),
        'basic_attack': 'final word', 'strong_attack': 'entropic cascade', 'player_abilities': ['dark_dark_technique_lv2_void_crush'],
        'base_str': 38, 'base_dex': 38, 'base_con': 35, 'base_int': 40, 'base_hp': 30000, 'base_ap': 500,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 4, 'int_per_level': 5,
        'resistances': ['dark', 'ice'], 'immunities': ['sleep', 'confuse'], 'weaknesses': ['light']
    },
    {
        'id': 'anarchist', 'name': 'Anarchist', 'hostile_type': 'humanoid', 'min_spawn_level': 55, 'role': 'damage', 'rarity': 'uncommon',
        'base_xp': 8000, 'common_drop': 'herb_med', 'rare_drop': None, 'money_range': (1400, 2800),
        'basic_attack': 'chaotic strike', 'strong_attack': 'anarchy wave', 'player_abilities': ['dark_magic_lv1_shadow_tendril'],
        'base_str': 35, 'base_dex': 25, 'base_con': 32, 'base_int': 20, 'base_hp': 2200, 'base_ap': 70,
        'str_per_level': 4, 'dex_per_level': 3, 'con_per_level': 4, 'int_per_level': 2,
        'resistances': ['dark'], 'immunities': ['confuse'], 'weaknesses': ['light']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'nihilist_camp',
    'seed': abs(hash('nihilist_camp')),
    'floor_count': 1,
    'room_size_min_max': (80, 120),
    'rooms_per_floor': 6,
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.0,
    'min_max_distance_between_rooms': (1, 4),
    'min_max_corridor_width': (2, 4),
    'display_name': "Nihilist Camp",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color':  OPEN_AREA_COLOR,
	'impassable_color': IMPASSABLE_COLOR,
	'border_tile':      BORDER_TILE,
	'border_color':     BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': [{'id': 'nihilist_leader', 'location': 'final_chamber'}],
    'items': [
        {'id': 'panacea', 'location': 'treasure_room'},
        {'id': 'elixir_full_heal', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 6,
}
