"""
Theatre of Echoed Faces - Chapter 8 Dungeon Seed Configuration
A disorienting theatre where illusions and fractured attention are weapons.
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "▒"
IMPASSABLE_TILE = "▓"
IMPASSABLE_CHANCE = 0.15

# Hostiles
FLOOR_HOSTILES = {
    1: ['echoing_phantom', 'distortion_hound', 'glamour_weaver', 'attention_devourer'],
}

HOSTILE_SEEDS = [
    {
        'id': 'echoing_phantom', 'name': 'Echoing Phantom', 'hostile_type': 'spirit', 'min_spawn_level': 40, 'role': 'hazard', 'rarity': 'common',
        'base_xp': 400, 'common_drop': 'stimulant_med', 'rare_drop': None, 'money_range': (50, 100),
        'basic_attack': 'fading touch', 'strong_attack': 'dissonant scream', 'player_abilities': [],
        'base_str': 15, 'base_dex': 25, 'base_con': 18, 'base_int': 22, 'base_hp': 900, 'base_ap': 60,
        'str_per_level': 2, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['air', 'dark'], 'immunities': [], 'weaknesses': ['light']
    },
    {
        'id': 'distortion_hound', 'name': 'Distortion Hound', 'hostile_type': 'beast', 'min_spawn_level': 40, 'role': 'damage', 'rarity': 'uncommon',
        'base_xp': 450, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (60, 120),
        'basic_attack': 'phase bite', 'strong_attack': 'reality warp', 'player_abilities': [],
        'base_str': 24, 'base_dex': 22, 'base_con': 20, 'base_int': 10, 'base_hp': 1200, 'base_ap': 50,
        'str_per_level': 3, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['physical'], 'immunities': ['confuse'], 'weaknesses': ['electric']
    },
    {
        'id': 'glamour_weaver', 'name': 'Glamour Weaver', 'hostile_type': 'humanoid', 'min_spawn_level': 41, 'role': 'hazard', 'rarity': 'rare',
        'base_xp': 500, 'common_drop': 'stimulant_large', 'rare_drop': 'tome_int', 'money_range': (80, 150),
        'basic_attack': 'mesmerizing glance', 'strong_attack': 'shattering image', 'player_abilities': ['light_faith_lv1_convert'],
        'base_str': 18, 'base_dex': 24, 'base_con': 19, 'base_int': 28, 'base_hp': 1000, 'base_ap': 70,
        'str_per_level': 2, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 4,
        'resistances': ['light'], 'immunities': [], 'weaknesses': ['dark']
    },
    {
        'id': 'attention_devourer', 'name': 'Attention Devourer', 'hostile_type': 'aberration', 'min_spawn_level': 42, 'role': 'damage', 'rarity': 'superrare',
        'base_xp': 700, 'common_drop': 'panacea', 'rare_drop': 'tome_int_superrare', 'money_range': (150, 300),
        'basic_attack': 'focus drain', 'strong_attack': 'ego shatter', 'player_abilities': ['dark_faith_lv1_shade_whisper'],
        'base_str': 20, 'base_dex': 20, 'base_con': 25, 'base_int': 30, 'base_hp': 1500, 'base_ap': 80,
        'str_per_level': 2, 'dex_per_level': 2, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'ice'], 'immunities': ['silence'], 'weaknesses': ['fire']
    }
]

# Boss
DUNGEON_NPCS = [ {'id': 'glamour','location': 'final_chamber'} ]
BOSS_MOB = {
    'id': 'scalpel_projection_1',
    'name': 'Scalpel\'s Projection',
    'hostiles': ['scalpel_projection_1']
}

BOSS_HOSTILES = [
    {
        'id': 'scalpel_projection_1', 'name': 'Scalpel\'s Projection', 'hostile_type': 'construct', 'min_spawn_level': 42, 'role': 'damage', 'rarity': 'notfound',
        'base_xp': 5000, 'common_drop': 'tome_int', 'rare_drop': 'tome_dex_superrare', 'money_range': (500, 1000),
        'basic_attack': 'surgical strike', 'strong_attack': 'perfect cut', 'player_abilities': ['cold_execution', 'perfect_cut', 'detached_slaughter'],
        'base_str': 28, 'base_dex': 35, 'base_con': 24, 'base_int': 25, 'base_hp': 12000, 'base_ap': 250,
        'str_per_level': 3, 'dex_per_level': 5, 'con_per_level': 3, 'int_per_level': 3,
        'resistances': ['ice', 'physical'], 'immunities': ['stun', 'petrify'], 'weaknesses': ['fire', 'electric']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'theatre_of_echoed_faces',
    'seed': abs(hash('theatre_of_echoed_faces')),
    'floor_count': 1,
    'room_size_min_max': (100, 180),
    'rooms_per_floor': 8,
    'max_neighbors_per_room': 3,
    'additional_connection_chance': 0.1,
    'min_max_distance_between_rooms': (2, 6),
    'min_max_corridor_width': (2, 5),
    'display_name': "Theatre of Echoed Faces",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': [{'id': 'scalpel_projection_1', 'location': 'final_chamber'}],
    'items': [
        {'id': 'stimulant_full', 'location': 'treasure_room'},
        {'id': 'panacea', 'location': 'treasure_room'},
        {'id': 'tome_str_superrare', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 7,
}
