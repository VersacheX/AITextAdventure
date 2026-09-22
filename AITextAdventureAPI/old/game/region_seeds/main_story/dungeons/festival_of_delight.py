"""
Festival of Delight - Chapter 11 Dungeon Seed Configuration
A chaotic festival ground where emotions are weaponized.
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "▓"
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = "#9a6040"
IMPASSABLE_COLOR = "#3a2010"
BORDER_TILE      = "·"
BORDER_COLOR     = "#6a4020"

# Hostiles
FLOOR_HOSTILES = {
    1: ['manic_reveler', 'joyful_zealot', 'frenzied_brute', 'ecstatic_elemental'],
}

HOSTILE_SEEDS = [
    {
        'id': 'manic_reveler', 'name': 'Manic Reveler', 'hostile_type': 'humanoid', 'min_spawn_level': 55, 'role': 'hazard', 'rarity': 'common',
        'base_xp': 600, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (100, 200),
        'basic_attack': 'wild swing', 'strong_attack': 'frenzied dance', 'player_abilities': [],
        'base_str': 35, 'base_dex': 30, 'base_con': 28, 'base_int': 10, 'base_hp': 1800, 'base_ap': 70,
        'str_per_level': 4, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': [], 'immunities': ['confuse'], 'weaknesses': ['ice']
    },
    {
        'id': 'joyful_zealot', 'name': 'Joyful Zealot', 'hostile_type': 'humanoid', 'min_spawn_level': 55, 'role': 'hazard', 'rarity': 'uncommon',
        'base_xp': 650, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (120, 240),
        'basic_attack': 'ecstatic strike', 'strong_attack': 'blinding joy', 'player_abilities': ['light_spirit_lv1_convert'],
        'base_str': 30, 'base_dex': 28, 'base_con': 26, 'base_int': 25, 'base_hp': 1700, 'base_ap': 80,
        'str_per_level': 3, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 3,
        'resistances': ['light'], 'immunities': [], 'weaknesses': ['dark']
    },
    {
        'id': 'frenzied_brute', 'name': 'Frenzied Brute', 'hostile_type': 'humanoid', 'min_spawn_level': 56, 'role': 'damage', 'rarity': 'rare',
        'base_xp': 800, 'common_drop': 'stimulant_full', 'rare_drop': 'tome_str_superrare', 'money_range': (150, 300),
        'basic_attack': 'heavy slam', 'strong_attack': 'unstoppable charge', 'player_abilities': [],
        'base_str': 40, 'base_dex': 20, 'base_con': 35, 'base_int': 5, 'base_hp': 2500, 'base_ap': 60,
        'str_per_level': 5, 'dex_per_level': 2, 'con_per_level': 4, 'int_per_level': 0,
        'resistances': ['physical'], 'immunities': ['stun'], 'weaknesses': ['electric']
    },
    {
        'id': 'ecstatic_elemental', 'name': 'Ecstatic Elemental', 'hostile_type': 'elemental', 'min_spawn_level': 57, 'role': 'damage', 'rarity': 'superrare',
        'base_xp': 1000, 'common_drop': 'panacea', 'rare_drop': 'tome_int_superrare', 'money_range': (250, 500),
        'basic_attack': 'searing light', 'strong_attack': 'rapturous explosion', 'player_abilities': ['fire_magic_lv1_fireball'],
        'base_str': 20, 'base_dex': 30, 'base_con': 28, 'base_int': 40, 'base_hp': 2200, 'base_ap': 100,
        'str_per_level': 2, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 5,
        'resistances': ['fire', 'light'], 'immunities': [], 'weaknesses': ['water', 'dark']
    }
]

# Boss
DUNGEON_NPCS = [
    {'id': 'revelry', 'location': 'final_chamber'}
]
BOSS_MOB = {
    'id': 'rapture_revelry_1',
    'name': 'Rapture and Revelry',
    'hostiles': ['rapture_boss', 'revelry_boss']
}

BOSS_HOSTILES = [
    {
        'id': 'rapture_boss', 'name': 'Rapture', 'hostile_type': 'aberration', 'min_spawn_level': 57, 'role': 'damage', 'rarity': 'notfound',
        'base_xp': 8000, 'common_drop': 'tome_int', 'rare_drop': 'tome_str_superrare', 'money_range': (1000, 2000),
        'basic_attack': 'painful truth', 'strong_attack': 'agony spike', 'player_abilities': ['blood_spectacle', 'thrill_of_ruin', 'seizing_the_moment', 'predator_rush'],
        'base_str': 40, 'base_dex': 35, 'base_con': 30, 'base_int': 25, 'base_hp': 25000, 'base_ap': 350,
        'str_per_level': 5, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 3,
        'resistances': ['dark', 'physical'], 'immunities': ['stun'], 'weaknesses': ['light']
    },
    {
        'id': 'revelry_boss', 'name': 'Revelry', 'hostile_type': 'aberration', 'min_spawn_level': 57, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 8000, 'common_drop': 'tome_dex_superrare', 'rare_drop': 'unstable_relic', 'money_range': (1000, 2000),
        'basic_attack': 'manic burst', 'strong_attack': 'endless party', 'player_abilities': ['manic_freedom', 'collapse_of_joy', 'wild_possibility', 'entropic_spiral'],
        'base_str': 30, 'base_dex': 40, 'base_con': 25, 'base_int': 35, 'base_hp': 22000, 'base_ap': 400,
        'str_per_level': 3, 'dex_per_level': 5, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['air', 'light'], 'immunities': ['confuse', 'sleep'], 'weaknesses': ['earth']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'festival_of_delight',
    'seed': abs(hash('festival_of_delight')),
    'floor_count': 1,
    'room_size_min_max': (150, 250),
    'rooms_per_floor': 9,
    'max_neighbors_per_room': 3,
    'additional_connection_chance': 0.15,
    'min_max_distance_between_rooms': (4, 8),
    'min_max_corridor_width': (4, 8),
    'display_name': "Festival of Delight",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color':  OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile':      BORDER_TILE,
    'border_color':     BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': [{'id': 'rapture_revelry_1', 'location': 'final_chamber'}],
    'items': [
        {'id': 'revive_kit', 'location': 'treasure_room'},
        {'id': 'panacea', 'location': 'treasure_room'},
        {'id': 'tome_int_superrare', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 9,
}
