"""
Trial 5 Dungeon - Chapter 21 Dungeon Seed Configuration
System of Memory - Cataclysm and Reliquary
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "▓"
IMPASSABLE_TILE = "█"
IMPASSABLE_CHANCE = 0.16
OPEN_AREA_COLOR  = "#7a3838"
IMPASSABLE_COLOR = "#1e0808"
BORDER_TILE      = "·"
BORDER_COLOR     = "#501818"

# Hostiles
FLOOR_HOSTILES = {
    1: ['failure_archive', 'memory_construct', 'pattern_enforcer', 'recursive_horror'],
}

HOSTILE_SEEDS = [
    {
        'id': 'failure_archive', 'name': 'Failure Archive', 'hostile_type': 'undead', 'min_spawn_level': 99, 'role': 'hazard', 'rarity': 'common',
        'base_xp': 10000, 'common_drop': 'defibrillator', 'rare_drop': None, 'money_range': (1000, 1400),
        'basic_attack': 'past mistake', 'strong_attack': 'recorded collapse', 'player_abilities': [],
        'base_str': 48, 'base_dex': 50, 'base_con': 52, 'base_int': 58, 'base_hp': 46000, 'base_ap': 360,
        'str_per_level': 6, 'dex_per_level': 6, 'con_per_level': 6, 'int_per_level': 7,
        'resistances': ['dark', 'ice'], 'immunities': ['sleep', 'petrify'], 'weaknesses': ['light', 'fire']
    },
    {
        'id': 'memory_construct', 'name': 'Memory Construct', 'hostile_type': 'construct', 'min_spawn_level': 100, 'role': 'tank', 'rarity': 'uncommon',
        'base_xp': 10500, 'common_drop': 'stimulant_full', 'rare_drop': 'tome_con_rare', 'money_range': (1050, 1500),
        'basic_attack': 'preserved pain', 'strong_attack': 'eternal wound', 'player_abilities': [],
        'base_str': 55, 'base_dex': 48, 'base_con': 70, 'base_int': 55, 'base_hp': 56000, 'base_ap': 350,
        'str_per_level': 7, 'dex_per_level': 5, 'con_per_level': 9, 'int_per_level': 6,
        'resistances': ['physical', 'dark'], 'immunities': ['stun', 'confuse'], 'weaknesses': ['light']
    },
    {
        'id': 'pattern_enforcer', 'name': 'Pattern Enforcer', 'hostile_type': 'aberration', 'min_spawn_level': 101, 'role': 'damage', 'rarity': 'rare',
        'base_xp': 12000, 'common_drop': 'elixir_full_heal', 'rare_drop': 'tome_str_superrare', 'money_range': (1100, 1700),
        'basic_attack': 'repetition strike', 'strong_attack': 'pattern lock', 'player_abilities': [],
        'base_str': 65, 'base_dex': 60, 'base_con': 58, 'base_int': 52, 'base_hp': 52000, 'base_ap': 370,
        'str_per_level': 8, 'dex_per_level': 7, 'con_per_level': 7, 'int_per_level': 6,
        'resistances': ['physical', 'dark'], 'immunities': ['stun'], 'weaknesses': ['light', 'fire']
    },
    {
        'id': 'recursive_horror', 'name': 'Recursive Horror', 'hostile_type': 'aberration', 'min_spawn_level': 102, 'role': 'hazard', 'rarity': 'superrare',
        'base_xp': 13000, 'common_drop': 'revive_kit', 'rare_drop': 'tome_int_superrare', 'money_range': (1200, 1800),
        'basic_attack': 'feedback loop', 'strong_attack': 'recursive collapse', 'player_abilities': ['dark_faith_lv1_shade_whisper'],
        'base_str': 52, 'base_dex': 55, 'base_con': 60, 'base_int': 72, 'base_hp': 54000, 'base_ap': 460,
        'str_per_level': 6, 'dex_per_level': 6, 'con_per_level': 7, 'int_per_level': 9,
        'resistances': ['dark', 'poison', 'ice'], 'immunities': ['confuse', 'petrify', 'silence'], 'weaknesses': ['light', 'fire']
    }
]

# Boss
DUNGEON_NPCS = [
    {'id': 'cataclysm', 'location': 'final_chamber'}
]

BOSS_MOB = {
    'id': 'cataclysm_reliquary_1',
    'name': 'The Memory Refiners',
    'hostiles': ['cataclysm_trial', 'reliquary_trial']
}

BOSS_HOSTILES = [
    {
        'id': 'cataclysm_trial', 'name': 'Cataclysm', 'hostile_type': 'void_entity', 'min_spawn_level': 102, 'role': 'damage', 'rarity': 'notfound',
        'base_xp': 140000, 'common_drop': 'tome_str_superrare', 'rare_drop': 'cataclysm_refinement_core', 'money_range': (7000, 14000),
        'basic_attack': 'optimized failure', 'strong_attack': 'efficient collapse', 'player_abilities': ['systematic_destruction', 'refinement_loop', 'inevitable_failure'],
        'base_str': 70, 'base_dex': 62, 'base_con': 68, 'base_int': 65, 'base_hp': 380000, 'base_ap': 600,
        'str_per_level': 9, 'dex_per_level': 8, 'con_per_level': 9, 'int_per_level': 8,
        'resistances': ['physical', 'dark', 'fire'], 'immunities': ['stun', 'petrify', 'fear'], 'weaknesses': ['light']
    },
    {
        'id': 'reliquary_trial', 'name': 'Reliquary', 'hostile_type': 'void_entity', 'min_spawn_level': 102, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 140000, 'common_drop': 'tome_con_superrare', 'rare_drop': 'reliquary_preservation_shard', 'money_range': (7000, 14000),
        'basic_attack': 'archived trauma', 'strong_attack': 'structural memory', 'player_abilities': ['eternal_wound', 'memory_of_suffering', 'burden_of_the_lost'],
        'base_str': 55, 'base_dex': 58, 'base_con': 75, 'base_int': 78, 'base_hp': 400000, 'base_ap': 680,
        'str_per_level': 6, 'dex_per_level': 7, 'con_per_level': 9, 'int_per_level': 10,
        'resistances': ['dark', 'ice', 'physical'], 'immunities': ['sleep', 'petrify', 'confuse'], 'weaknesses': ['light', 'fire']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'trial_5_dungeon',
    'seed': abs(hash('trial_5_dungeon')),
    'floor_count': 1,
    'room_size_min_max': (160, 240),
    'rooms_per_floor': 11,
    'max_neighbors_per_room': 4,
    'additional_connection_chance': 0.22,
    'min_max_distance_between_rooms': (4, 8),
    'min_max_corridor_width': (5, 9),
    'display_name': "The System of Memory",
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
        {'id': 'revive_kit', 'location': 'treasure_room'},
        {'id': 'tome_hp_superrare', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 10,
}