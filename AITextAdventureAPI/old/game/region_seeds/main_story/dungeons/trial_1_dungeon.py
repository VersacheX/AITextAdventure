"""
Trial 1 Dungeon - Chapter 21 Dungeon Seed Configuration
System of Compliance - Edict, Glamour, and Crux
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "▓"
IMPASSABLE_TILE = "█"
IMPASSABLE_CHANCE = 0.08

# Hostiles
FLOOR_HOSTILES = {
    1: ['compliance_drone', 'certainty_wraith', 'purpose_void', 'efficiency_construct'],
}

HOSTILE_SEEDS = [
    {
        'id': 'compliance_drone', 'name': 'Compliance Drone', 'hostile_type': 'construct', 'min_spawn_level': 95, 'role': 'tank', 'rarity': 'common',
        'base_xp': 8500, 'common_drop': 'potion_hp_mega', 'rare_drop': None, 'money_range': (800, 1200),
        'basic_attack': 'protocol enforcement', 'strong_attack': 'mandatory compliance', 'player_abilities': [],
        'base_str': 45, 'base_dex': 30, 'base_con': 55, 'base_int': 35, 'base_hp': 45000, 'base_ap': 300,
        'str_per_level': 5, 'dex_per_level': 3, 'con_per_level': 6, 'int_per_level': 4,
        'resistances': ['physical', 'dark'], 'immunities': ['confuse', 'fear'], 'weaknesses': ['light']
    },
    {
        'id': 'certainty_wraith', 'name': 'Certainty Wraith', 'hostile_type': 'undead', 'min_spawn_level': 96, 'role': 'damage', 'rarity': 'uncommon',
        'base_xp': 9000, 'common_drop': 'potion_ap_mega', 'rare_drop': 'tome_int_rare', 'money_range': (850, 1300),
        'basic_attack': 'false clarity', 'strong_attack': 'absolute conviction', 'player_abilities': [],
        'base_str': 38, 'base_dex': 42, 'base_con': 40, 'base_int': 50, 'base_hp': 38000, 'base_ap': 350,
        'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 6,
        'resistances': ['dark', 'ice'], 'immunities': ['confuse', 'sleep'], 'weaknesses': ['light', 'fire']
    },
    {
        'id': 'purpose_void', 'name': 'Purpose Void', 'hostile_type': 'aberration', 'min_spawn_level': 97, 'role': 'hazard', 'rarity': 'rare',
        'base_xp': 10000, 'common_drop': 'elixir_full', 'rare_drop': 'tome_con_superrare', 'money_range': (900, 1500),
        'basic_attack': 'meaningless motion', 'strong_attack': 'emptiness cascade', 'player_abilities': [],
        'base_str': 40, 'base_dex': 35, 'base_con': 45, 'base_int': 55, 'base_hp': 42000, 'base_ap': 400,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 5, 'int_per_level': 7,
        'resistances': ['dark', 'poison'], 'immunities': ['sleep', 'petrify'], 'weaknesses': ['light']
    },
    {
        'id': 'efficiency_construct', 'name': 'Efficiency Construct', 'hostile_type': 'construct', 'min_spawn_level': 98, 'role': 'damage', 'rarity': 'superrare',
        'base_xp': 11000, 'common_drop': 'phoenix_down', 'rare_drop': 'tome_str_superrare', 'money_range': (1000, 1600),
        'basic_attack': 'optimized strike', 'strong_attack': 'process termination', 'player_abilities': [],
        'base_str': 52, 'base_dex': 48, 'base_con': 50, 'base_int': 42, 'base_hp': 50000, 'base_ap': 350,
        'str_per_level': 6, 'dex_per_level': 5, 'con_per_level': 5, 'int_per_level': 5,
        'resistances': ['physical', 'electric'], 'immunities': ['stun', 'confuse'], 'weaknesses': ['light', 'fire']
    }
]

# Boss
DUNGEON_NPCS = [
    {'id': 'edict', 'location': 'final_chamber'}
]

BOSS_MOB = {
    'id': 'edict_glamour_crux_1',
    'name': 'The System Enforcers',
    'hostiles': ['edict_trial', 'glamour_trial', 'crux_trial']
}

BOSS_HOSTILES = [
    {
        'id': 'edict_trial', 'name': 'Edict', 'hostile_type': 'void_entity', 'min_spawn_level': 98, 'role': 'tank', 'rarity': 'notfound',
        'base_xp': 100000, 'common_drop': 'tome_con_superrare', 'rare_drop': 'edict_enforcement_seal', 'money_range': (5000, 10000),
        'basic_attack': 'lawful decree', 'strong_attack': 'absolute order', 'player_abilities': ['system_lockdown', 'rule_enforcement', 'procedural_inevitability'],
        'base_str': 55, 'base_dex': 35, 'base_con': 75, 'base_int': 60, 'base_hp': 350000, 'base_ap': 500,
        'str_per_level': 6, 'dex_per_level': 4, 'con_per_level': 8, 'int_per_level': 7,
        'resistances': ['physical', 'dark'], 'immunities': ['confuse', 'stun', 'fear', 'silence'], 'weaknesses': ['light']
    },
    {
        'id': 'glamour_trial', 'name': 'Glamour', 'hostile_type': 'void_entity', 'min_spawn_level': 98, 'role': 'support', 'rarity': 'notfound',
        'base_xp': 100000, 'common_drop': 'tome_int_superrare', 'rare_drop': 'glamour_illusion_veil', 'money_range': (5000, 10000),
        'basic_attack': 'false serenity', 'strong_attack': 'manufactured peace', 'player_abilities': ['certainty_field', 'doubt_erasure', 'calm_enforcement'],
        'base_str': 40, 'base_dex': 45, 'base_con': 50, 'base_int': 70, 'base_hp': 280000, 'base_ap': 600,
        'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 5, 'int_per_level': 9,
        'resistances': ['ice', 'dark'], 'immunities': ['confuse', 'fear', 'sleep'], 'weaknesses': ['light', 'fire']
    },
    {
        'id': 'crux_trial', 'name': 'Crux', 'hostile_type': 'void_entity', 'min_spawn_level': 98, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 100000, 'common_drop': 'tome_dex_superrare', 'rare_drop': 'crux_logic_core', 'money_range': (5000, 10000),
        'basic_attack': 'logic cascade', 'strong_attack': 'consistency override', 'player_abilities': ['contradiction_loop', 'simulated_truth', 'objective_elimination'],
        'base_str': 45, 'base_dex': 55, 'base_con': 55, 'base_int': 65, 'base_hp': 300000, 'base_ap': 550,
        'str_per_level': 5, 'dex_per_level': 6, 'con_per_level': 6, 'int_per_level': 8,
        'resistances': ['electric', 'dark'], 'immunities': ['confuse', 'petrify', 'sleep'], 'weaknesses': ['light']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'trial_1_dungeon',
    'seed': abs(hash('trial_1_dungeon')),
    'floor_count': 1,
    'room_size_min_max': (120, 200),
    'rooms_per_floor': 7,
    'max_neighbors_per_room': 3,
    'additional_connection_chance': 0.15,
    'min_max_distance_between_rooms': (3, 6),
    'min_max_corridor_width': (3, 5),
    'display_name': "The System of Compliance",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': DUNGEON_NPCS,
    'items': [
        {'id': 'elixir_full', 'location': 'treasure_room'},
        {'id': 'phoenix_down', 'location': 'treasure_room'},
        {'id': 'tome_hp_superrare', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 8,
}