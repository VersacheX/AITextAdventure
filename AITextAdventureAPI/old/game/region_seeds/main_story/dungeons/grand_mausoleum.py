"""
Grand Mausoleum - Chapter 13 Dungeon Seed Configuration
A vast necropolis where grief and self-loathing are given form.
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "█"
IMPASSABLE_CHANCE = 0.20
OPEN_AREA_COLOR  = "#6a7a8a"
IMPASSABLE_COLOR = "#2a3040"
BORDER_TILE      = "·"
BORDER_COLOR     = "#485868"

# Hostiles
FLOOR_HOSTILES = {
    1: ['grief_wraith', 'self-loathing_specter', 'memory_hoarder', 'tomb_guardian'],
}

HOSTILE_SEEDS = [
    {
        'id': 'grief_wraith', 'name': 'Grief Wraith', 'hostile_type': 'undead', 'min_spawn_level': 65, 'role': 'hazard', 'rarity': 'common',
        'base_xp': 800, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (150, 300),
        'basic_attack': 'sorrowful touch', 'strong_attack': 'weeping wail', 'player_abilities': ['dark_faith_lv1_shade_whisper'],
        'base_str': 30, 'base_dex': 35, 'base_con': 32, 'base_int': 40, 'base_hp': 2500, 'base_ap': 100,
        'str_per_level': 3, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 5,
        'resistances': ['dark', 'ice'], 'immunities': ['fear'], 'weaknesses': ['light', 'fire']
    },
    {
        'id': 'self-loathing_specter', 'name': 'Self-Loathing Specter', 'hostile_type': 'undead', 'min_spawn_level': 65, 'role': 'hazard', 'rarity': 'uncommon',
        'base_xp': 850, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (160, 320),
        'basic_attack': 'bitter strike', 'strong_attack': 'spiral of despair', 'player_abilities': ['dark_skill_lv1_creeping_strike'],
        'base_str': 38, 'base_dex': 32, 'base_con': 30, 'base_int': 35, 'base_hp': 2400, 'base_ap': 90,
        'str_per_level': 4, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark'], 'immunities': ['confuse'], 'weaknesses': ['light']
    },
    {
        'id': 'memory_hoarder', 'name': 'Memory Hoarder', 'hostile_type': 'aberration', 'min_spawn_level': 66, 'role': 'damage', 'rarity': 'rare',
        'base_xp': 1000, 'common_drop': 'panacea', 'rare_drop': 'tome_int_superrare', 'money_range': (200, 400),
        'basic_attack': 'stolen glance', 'strong_attack': 'unravel memory', 'player_abilities': [],
        'base_str': 30, 'base_dex': 30, 'base_con': 40, 'base_int': 45, 'base_hp': 3000, 'base_ap': 120,
        'str_per_level': 3, 'dex_per_level': 3, 'con_per_level': 4, 'int_per_level': 6,
        'resistances': ['ice'], 'immunities': ['sleep'], 'weaknesses': ['fire']
    },
    {
        'id': 'tomb_guardian', 'name': 'Tomb Guardian', 'hostile_type': 'construct', 'min_spawn_level': 67, 'role': 'damage', 'rarity': 'superrare',
        'base_xp': 1200, 'common_drop': 'stimulant_full', 'rare_drop': 'tome_con_superrare', 'money_range': (300, 600),
        'basic_attack': 'stone fist', 'strong_attack': 'necropolis quake', 'player_abilities': ['earth_technique_lv1_armor_up'],
        'base_str': 45, 'base_dex': 20, 'base_con': 45, 'base_int': 10, 'base_hp': 4000, 'base_ap': 80,
        'str_per_level': 6, 'dex_per_level': 2, 'con_per_level': 6, 'int_per_level': 1,
        'resistances': ['physical', 'earth'], 'immunities': ['stun', 'petrify'], 'weaknesses': ['electric']
    }
]

# Boss

DUNGEON_NPCS = [
    {'id': 'lament', 'location': 'final_chamber'}
]
BOSS_MOB = {
    'id': 'lament_garbage_1',
    'name': 'Lament and Garbage',
    'hostiles': ['lament_boss', 'garbage_boss']
}

BOSS_HOSTILES = [
    {
        'id': 'lament_boss', 'name': 'Lament', 'hostile_type': 'aberration', 'min_spawn_level': 67, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 15000, 'common_drop': 'tome_int_superrare', 'rare_drop': 'bracelet_of_void', 'money_range': (2000, 4000),
        'basic_attack': 'endless sorrow', 'strong_attack': 'grief wave', 'player_abilities': ['endless_tragedy', 'collapse_of_self', 'singularity_of_grief', 'weight_of_memory'],
        'base_str': 35, 'base_dex': 45, 'base_con': 40, 'base_int': 50, 'base_hp': 40000, 'base_ap': 600,
        'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 7,
        'resistances': ['dark', 'ice'], 'immunities': ['fear', 'sleep'], 'weaknesses': ['light', 'fire']
    },
    {
        'id': 'garbage_boss', 'name': 'Garbage', 'hostile_type': 'aberration', 'min_spawn_level': 67, 'role': 'damage', 'rarity': 'notfound',
        'base_xp': 15000, 'common_drop': 'tome_con_superrare', 'rare_drop': 'unstable_relic', 'money_range': (2000, 4000),
        'basic_attack': 'worthless strike', 'strong_attack': 'corrosive self-doubt', 'player_abilities': ['absolute_disgust', 'distortion_of_reality', 'the_epic_you_never_were', 'rot_of_potential'],
        'base_str': 48, 'base_dex': 40, 'base_con': 45, 'base_int': 30, 'base_hp': 45000, 'base_ap': 500,
        'str_per_level': 6, 'dex_per_level': 4, 'con_per_level': 5, 'int_per_level': 3,
        'resistances': ['dark', 'physical'], 'immunities': ['confuse', 'poison'], 'weaknesses': ['light']
 }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'grand_mausoleum',
    'seed': abs(hash('grand_mausoleum')),
    'floor_count': 3,
    'room_size_min_max': (200, 300),
    'rooms_per_floor': 5,
    'max_neighbors_per_room': 4,
    'additional_connection_chance': 0.2,
    'min_max_distance_between_rooms': (5, 10),
    'min_max_corridor_width': (5, 10),
    'display_name': "Grand Mausoleum",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color':  OPEN_AREA_COLOR,
	'impassable_color': IMPASSABLE_COLOR,
	'border_tile':      BORDER_TILE,
	'border_color':     BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': [{'id': 'lament_garbage_1', 'location': 'final_chamber'}],
    'items': [
        {'id': 'defibrillator', 'location': 'treasure_room'},
        {'id': 'panacea', 'location': 'treasure_room'},
        {'id': 'tome_hp_superrare', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 10,
}
