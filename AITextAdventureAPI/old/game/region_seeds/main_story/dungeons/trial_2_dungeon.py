"""
Trial 2 Dungeon - Chapter 21 Dungeon Seed Configuration
System of Identity - Stigma, Rapture, and Scalpel
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "▒"
IMPASSABLE_TILE = "█"
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = "#8a6070"
IMPASSABLE_COLOR = "#200e14"
BORDER_TILE      = "·"
BORDER_COLOR     = "#5a3040"

# Hostiles
FLOOR_HOSTILES = {
    1: ['identity_judge', 'pressure_wraith', 'role_enforcer', 'classification_construct'],
}

HOSTILE_SEEDS = [
    {
        'id': 'identity_judge', 'name': 'Identity Judge', 'hostile_type': 'humanoid', 'min_spawn_level': 96, 'role': 'hazard', 'rarity': 'common',
        'base_xp': 8800, 'common_drop': 'defibrillator', 'rare_drop': None, 'money_range': (850, 1250),
        'basic_attack': 'defining label', 'strong_attack': 'identity erasure', 'player_abilities': [],
        'base_str': 42, 'base_dex': 38, 'base_con': 40, 'base_int': 52, 'base_hp': 42000, 'base_ap': 320,
        'str_per_level': 5, 'dex_per_level': 4, 'con_per_level': 4, 'int_per_level': 6,
        'resistances': ['dark', 'ice'], 'immunities': ['confuse'], 'weaknesses': ['light', 'fire']
    },
    {
        'id': 'pressure_wraith', 'name': 'Pressure Wraith', 'hostile_type': 'spirit', 'min_spawn_level': 97, 'role': 'damage', 'rarity': 'uncommon',
        'base_xp': 9200, 'common_drop': 'stimulant_full', 'rare_drop': 'apex_hunter_band', 'money_range': (900, 1350),
        'basic_attack': 'stress fracture', 'strong_attack': 'crushing expectation', 'player_abilities': [],
        'base_str': 48, 'base_dex': 50, 'base_con': 38, 'base_int': 42, 'base_hp': 40000, 'base_ap': 340,
        'str_per_level': 6, 'dex_per_level': 6, 'con_per_level': 4, 'int_per_level': 5,
        'resistances': ['air', 'dark'], 'immunities': ['sleep'], 'weaknesses': ['light', 'earth']
    },
    {
        'id': 'role_enforcer', 'name': 'Role Enforcer', 'hostile_type': 'construct', 'min_spawn_level': 98, 'role': 'tank', 'rarity': 'rare',
        'base_xp': 10500, 'common_drop': 'elixir_full_heal', 'rare_drop': 'tome_str_superrare', 'money_range': (950, 1550),
        'basic_attack': 'assigned purpose', 'strong_attack': 'role lock', 'player_abilities': [],
        'base_str': 55, 'base_dex': 40, 'base_con': 60, 'base_int': 38, 'base_hp': 48000, 'base_ap': 310,
        'str_per_level': 7, 'dex_per_level': 4, 'con_per_level': 7, 'int_per_level': 4,
        'resistances': ['physical', 'dark'], 'immunities': ['stun', 'confuse'], 'weaknesses': ['light']
    },
    {
        'id': 'classification_construct', 'name': 'Classification Construct', 'hostile_type': 'aberration', 'min_spawn_level': 99, 'role': 'hazard', 'rarity': 'superrare',
        'base_xp': 11500, 'common_drop': 'revive_kit', 'rare_drop': 'tome_int_superrare', 'money_range': (1050, 1650),
        'basic_attack': 'categorical strike', 'strong_attack': 'total filtration', 'player_abilities': ['dark_faith_lv1_shade_whisper'],
        'base_str': 45, 'base_dex': 52, 'base_con': 48, 'base_int': 58, 'base_hp': 46000, 'base_ap': 420,
        'str_per_level': 5, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 7,
        'resistances': ['dark', 'poison'], 'immunities': ['petrify', 'silence'], 'weaknesses': ['light', 'fire']
    }
]

# Boss
DUNGEON_NPCS = [
    {'id': 'stigma', 'location': 'final_chamber'}
]

BOSS_MOB = {
    'id': 'stigma_rapture_scalpel_1',
    'name': 'The Identity Breakers',
    'hostiles': ['stigma_trial', 'rapture_trial', 'scalpel_trial']
}

BOSS_HOSTILES = [
    {
        'id': 'stigma_trial', 'name': 'Stigma', 'hostile_type': 'void_entity', 'min_spawn_level': 99, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 110000, 'common_drop': 'tome_int_superrare', 'rare_drop': 'stigma_classification_lens', 'money_range': (5500, 11000),
        'basic_attack': 'defining judgment', 'strong_attack': 'identity collapse', 'player_abilities': ['void_refraction', 'the_darkness_consuming', 'you_can_be_me'],
        'base_str': 48, 'base_dex': 52, 'base_con': 55, 'base_int': 75, 'base_hp': 320000, 'base_ap': 650,
        'str_per_level': 5, 'dex_per_level': 6, 'con_per_level': 6, 'int_per_level': 9,
        'resistances': ['dark', 'ice'], 'immunities': ['confuse', 'sleep'], 'weaknesses': ['light']
    },
    {
        'id': 'rapture_trial', 'name': 'Rapture', 'hostile_type': 'void_entity', 'min_spawn_level': 99, 'role': 'damage', 'rarity': 'notfound',
        'base_xp': 110000, 'common_drop': 'tome_str_superrare', 'rare_drop': 'rapture_intensity_core', 'money_range': (5500, 11000),
        'basic_attack': 'euphoric rush', 'strong_attack': 'breaking point', 'player_abilities': ['adrenaline_surge', 'reckless_abandon', 'thrill_addiction'],
        'base_str': 65, 'base_dex': 60, 'base_con': 50, 'base_int': 45, 'base_hp': 340000, 'base_ap': 520,
        'str_per_level': 8, 'dex_per_level': 7, 'con_per_level': 5, 'int_per_level': 5,
        'resistances': ['fire', 'physical'], 'immunities': ['sleep', 'stun'], 'weaknesses': ['ice', 'light']
    },
    {
        'id': 'scalpel_trial', 'name': 'Scalpel', 'hostile_type': 'void_entity', 'min_spawn_level': 99, 'role': 'damage', 'rarity': 'notfound',
        'base_xp': 110000, 'common_drop': 'tome_dex_superrare', 'rare_drop': 'scalpel_precision_blade', 'money_range': (5500, 11000),
        'basic_attack': 'surgical cut', 'strong_attack': 'pressure test', 'player_abilities': ['cold_execution', 'perfect_cut', 'detached_slaughter'],
        'base_str': 52, 'base_dex': 70, 'base_con': 48, 'base_int': 55, 'base_hp': 300000, 'base_ap': 580,
        'str_per_level': 6, 'dex_per_level': 9, 'con_per_level': 5, 'int_per_level': 6,
        'resistances': ['ice', 'physical'], 'immunities': ['confuse', 'petrify'], 'weaknesses': ['fire', 'light']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'trial_2_dungeon',
    'seed': abs(hash('trial_2_dungeon')),
    'floor_count': 1,
    'room_size_min_max': (130, 210),
    'rooms_per_floor': 8,
    'max_neighbors_per_room': 3,
    'additional_connection_chance': 0.12,
    'min_max_distance_between_rooms': (3, 7),
    'min_max_corridor_width': (3, 6),
    'display_name': "The System of Identity",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color':  OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile':      BORDER_TILE,
    'border_color':     BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': DUNGEON_NPCS,
    'items': [
        {'id': 'elixir_full_heal', 'location': 'treasure_room'},
        {'id': 'defibrillator', 'location': 'treasure_room'},
        {'id': 'tome_ap_superrare', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 8,
}