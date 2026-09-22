"""
Trial 4 Dungeon - Chapter 21 Dungeon Seed Configuration
System of Perception - Pageant, Oracle, and Garbage
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "▒"
IMPASSABLE_TILE = "█"
IMPASSABLE_CHANCE = 0.14
OPEN_AREA_COLOR  = "#a09060"
IMPASSABLE_COLOR = "#282010"
BORDER_TILE      = "·"
BORDER_COLOR     = "#706040"

# Hostiles
FLOOR_HOSTILES = {
    1: ['performance_phantom', 'prophecy_sentinel', 'doubt_implanter', 'determinism_construct'],
}

HOSTILE_SEEDS = [
    {
        'id': 'performance_phantom', 'name': 'Performance Phantom', 'hostile_type': 'spirit', 'min_spawn_level': 98, 'role': 'hazard', 'rarity': 'common',
        'base_xp': 9500, 'common_drop': 'defibrillator', 'rare_drop': None, 'money_range': (950, 1350),
        'basic_attack': 'forced smile', 'strong_attack': 'crushing expectation', 'player_abilities': [],
        'base_str': 45, 'base_dex': 55, 'base_con': 48, 'base_int': 50, 'base_hp': 44000, 'base_ap': 350,
        'str_per_level': 5, 'dex_per_level': 7, 'con_per_level': 5, 'int_per_level': 6,
        'resistances': ['air', 'light'], 'immunities': ['confuse'], 'weaknesses': ['dark', 'earth']
    },
    {
        'id': 'prophecy_sentinel', 'name': 'Prophecy Sentinel', 'hostile_type': 'construct', 'min_spawn_level': 99, 'role': 'tank', 'rarity': 'uncommon',
        'base_xp': 10000, 'common_drop': 'stimulant_full', 'rare_drop': 'warlord_signet', 'money_range': (1000, 1450),
        'basic_attack': 'inevitable strike', 'strong_attack': 'fate lock', 'player_abilities': [],
        'base_str': 58, 'base_dex': 48, 'base_con': 65, 'base_int': 52, 'base_hp': 52000, 'base_ap': 340,
        'str_per_level': 7, 'dex_per_level': 5, 'con_per_level': 8, 'int_per_level': 6,
        'resistances': ['physical', 'dark'], 'immunities': ['stun', 'petrify'], 'weaknesses': ['light']
    },
    {
        'id': 'doubt_implanter', 'name': 'Doubt Implanter', 'hostile_type': 'aberration', 'min_spawn_level': 100, 'role': 'hazard', 'rarity': 'rare',
        'base_xp': 11500, 'common_drop': 'elixir_full_heal', 'rare_drop': 'tome_int_superrare', 'money_range': (1050, 1650),
        'basic_attack': 'intrusive thought', 'strong_attack': 'belief erosion', 'player_abilities': ['dark_spirit_lv1_shade_whisper'],
        'base_str': 40, 'base_dex': 50, 'base_con': 45, 'base_int': 70, 'base_hp': 42000, 'base_ap': 450,
        'str_per_level': 4, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 9,
        'resistances': ['dark', 'poison'], 'immunities': ['confuse', 'silence'], 'weaknesses': ['light', 'fire']
    },
    {
        'id': 'determinism_construct', 'name': 'Determinism Construct', 'hostile_type': 'construct', 'min_spawn_level': 101, 'role': 'damage', 'rarity': 'superrare',
        'base_xp': 12500, 'common_drop': 'revive_kit', 'rare_drop': 'tome_str_superrare', 'money_range': (1150, 1750),
        'basic_attack': 'predicted assault', 'strong_attack': 'scripted outcome', 'player_abilities': [],
        'base_str': 60, 'base_dex': 62, 'base_con': 55, 'base_int': 58, 'base_hp': 54000, 'base_ap': 380,
        'str_per_level': 7, 'dex_per_level': 8, 'con_per_level': 6, 'int_per_level': 7,
        'resistances': ['physical', 'electric'], 'immunities': ['stun', 'confuse'], 'weaknesses': ['light']
    }
]

# Boss
DUNGEON_NPCS = [
    {'id': 'pageant', 'location': 'final_chamber'}
]

BOSS_MOB = {
    'id': 'pageant_oracle_garbage_1',
    'name': 'The Determinism Enforcers',
    'hostiles': ['pageant_trial', 'oracle_trial', 'garbage_trial']
}

BOSS_HOSTILES = [
    {
        'id': 'pageant_trial', 'name': 'Pageant', 'hostile_type': 'void_entity', 'min_spawn_level': 101, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 130000, 'common_drop': 'tome_dex_superrare', 'rare_drop': 'pageant_performance_mask', 'money_range': (6500, 13000),
        'basic_attack': 'perfect composure', 'strong_attack': 'audience judgment', 'player_abilities': ['mask_of_expectation', 'crushing_reputation', 'obligation_chain'],
        'base_str': 50, 'base_dex': 70, 'base_con': 55, 'base_int': 62, 'base_hp': 340000, 'base_ap': 640,
        'str_per_level': 6, 'dex_per_level': 9, 'con_per_level': 6, 'int_per_level': 8,
        'resistances': ['air', 'light'], 'immunities': ['confuse', 'stun'], 'weaknesses': ['dark', 'earth']
    },
    {
        'id': 'oracle_trial', 'name': 'Oracle', 'hostile_type': 'void_entity', 'min_spawn_level': 101, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 130000, 'common_drop': 'tome_int_superrare', 'rare_drop': 'oracle_prophecy_tome', 'money_range': (6500, 13000),
        'basic_attack': 'immutable future', 'strong_attack': 'the only ending', 'player_abilities': ['inescapable_prophecy', 'vision_of_ruin', 'fate_lock'],
        'base_str': 48, 'base_dex': 52, 'base_con': 60, 'base_int': 80, 'base_hp': 320000, 'base_ap': 720,
        'str_per_level': 5, 'dex_per_level': 6, 'con_per_level': 7, 'int_per_level': 10,
        'resistances': ['dark', 'ice'], 'immunities': ['sleep', 'stun', 'petrify'], 'weaknesses': ['light', 'fire']
    },
    {
        'id': 'garbage_trial', 'name': 'Garbage', 'hostile_type': 'void_entity', 'min_spawn_level': 101, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 130000, 'common_drop': 'tome_con_superrare', 'rare_drop': 'garbage_doubt_seed', 'money_range': (6500, 13000),
        'basic_attack': 'whispered doubt', 'strong_attack': 'belief collapse', 'player_abilities': ['intrusive_truth', 'self_sabotage', 'unwanted_knowing'],
        'base_str': 45, 'base_dex': 55, 'base_con': 58, 'base_int': 75, 'base_hp': 330000, 'base_ap': 680,
        'str_per_level': 5, 'dex_per_level': 6, 'con_per_level': 7, 'int_per_level': 9,
        'resistances': ['dark', 'poison'], 'immunities': ['confuse', 'silence', 'stun'], 'weaknesses': ['light']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'trial_4_dungeon',
    'seed': abs(hash('trial_4_dungeon')),
    'floor_count': 1,
    'room_size_min_max': (150, 230),
    'rooms_per_floor': 10,
    'max_neighbors_per_room': 4,
    'additional_connection_chance': 0.20,
    'min_max_distance_between_rooms': (3, 7),
    'min_max_corridor_width': (4, 8),
    'display_name': "The System of Perception",
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
    'visible_distance': 9,
}