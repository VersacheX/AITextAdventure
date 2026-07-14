"""
Bloodspark Arena Gauntlet - Chapter 9 Dungeon Seed Configuration
A brutal arena where combat escalates with each encounter.
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "█"
IMPASSABLE_CHANCE = 0.08

# Hostiles
FLOOR_HOSTILES = {
    1: ['arena_gladiator', 'rage_hound', 'blood-forged_construct', 'champion_of_scalpel'],
}

HOSTILE_SEEDS = [
    {
        'id': 'arena_gladiator', 'name': 'Arena Gladiator', 'hostile_type': 'humanoid', 'min_spawn_level': 45, 'role': 'damage', 'rarity': 'common',
        'base_xp': 500, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (80, 160),
        'basic_attack': 'brutal slash', 'strong_attack': 'reckless charge', 'player_abilities': [],
        'base_str': 30, 'base_dex': 20, 'base_con': 25, 'base_int': 10, 'base_hp': 1400, 'base_ap': 55,
        'str_per_level': 4, 'dex_per_level': 2, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': [], 'immunities': [], 'weaknesses': ['ice']
    },
    {
        'id': 'rage_hound', 'name': 'Rage Hound', 'hostile_type': 'beast', 'min_spawn_level': 45, 'role': 'damage', 'rarity': 'uncommon',
        'base_xp': 550, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (90, 180),
        'basic_attack': 'frenzied bite', 'strong_attack': 'savage pounce', 'player_abilities': [],
        'base_str': 28, 'base_dex': 26, 'base_con': 22, 'base_int': 8, 'base_hp': 1300, 'base_ap': 60,
        'str_per_level': 3, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['fire'], 'immunities': [], 'weaknesses': ['water']
    },
    {
        'id': 'blood-forged_construct', 'name': 'Blood-Forged Construct', 'hostile_type': 'construct', 'min_spawn_level': 46, 'role': 'damage', 'rarity': 'rare',
        'base_xp': 650, 'common_drop': 'stimulant_full', 'rare_drop': 'tome_con_superrare', 'money_range': (120, 240),
        'basic_attack': 'iron cleave', 'strong_attack': 'sanguine eruption', 'player_abilities': [],
        'base_str': 35, 'base_dex': 15, 'base_con': 30, 'base_int': 5, 'base_hp': 2000, 'base_ap': 45,
        'str_per_level': 4, 'dex_per_level': 1, 'con_per_level': 4, 'int_per_level': 0,
        'resistances': ['physical', 'fire'], 'immunities': ['stun'], 'weaknesses': ['electric']
    },
    {
        'id': 'champion_of_scalpel', 'name': 'Champion of Scalpel', 'hostile_type': 'humanoid', 'min_spawn_level': 47, 'role': 'damage', 'rarity': 'superrare',
        'base_xp': 850, 'common_drop': 'panacea', 'rare_drop': 'tome_str_superrare', 'money_range': (200, 400),
        'basic_attack': 'precise strike', 'strong_attack': 'flurry of cuts', 'player_abilities': [],
        'base_str': 32, 'base_dex': 30, 'base_con': 26, 'base_int': 15, 'base_hp': 1800, 'base_ap': 70,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 2,
        'resistances': [], 'immunities': ['slow'], 'weaknesses': ['light']
    }
]

# Boss
DUNGEON_NPCS = [ {'id': 'scalpel','location': 'final_chamber'} ]
BOSS_MOB = {
    'id': 'glamour_scalpel_1',
    'name': 'Glamour and Scalpel',
    'hostiles': ['glamour_boss', 'scalpel_boss']
}

BOSS_HOSTILES = [
    {
        'id': 'glamour_boss', 'name': 'Glamour', 'hostile_type': 'aberration', 'min_spawn_level': 47, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 6000, 'common_drop': 'tome_int_superrare', 'rare_drop': 'unstable_relic', 'money_range': (800, 1500),
        'basic_attack': 'dazzling burst', 'strong_attack': 'overwhelming presence', 'player_abilities': ['radiant_lie', 'beauty_as_weapon', 'suffocating_allure'],
        'base_str': 20, 'base_dex': 30, 'base_con': 25, 'base_int': 38, 'base_hp': 15000, 'base_ap': 300,
        'str_per_level': 2, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 5,
        'resistances': ['light', 'air'], 'immunities': ['confuse', 'silence'], 'weaknesses': ['dark']
    },
    {
        'id': 'scalpel_boss', 'name': 'Scalpel', 'hostile_type': 'construct', 'min_spawn_level': 47, 'role': 'damage', 'rarity': 'notfound',
        'base_xp': 6000, 'common_drop': 'tome_int', 'rare_drop': 'tome_dex_superrare', 'money_range': (800, 1500),
        'basic_attack': 'anatomical strike', 'strong_attack': 'vivisection', 'player_abilities': ['cold_execution', 'perfect_cut', 'detached_slaughter'],
        'base_str': 32, 'base_dex': 40, 'base_con': 28, 'base_int': 20, 'base_hp': 18000, 'base_ap': 280,
        'str_per_level': 4, 'dex_per_level': 6, 'con_per_level': 3, 'int_per_level': 2,
        'resistances': ['ice', 'physical'], 'immunities': ['stun', 'petrify'], 'weaknesses': ['fire', 'electric']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'bloodspark_arena_gauntlet',
    'seed': abs(hash('bloodspark_arena_gauntlet')),
    'floor_count': 1,
    'room_size_min_max': (120, 200),
    'rooms_per_floor': 9,
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.05,
    'min_max_distance_between_rooms': (3, 7),
    'min_max_corridor_width': (3, 6),
    'display_name': "Bloodspark Arena",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': [{'id': 'glamour_scalpel_1', 'location': 'final_chamber'}],
    'items': [
        {'id': 'defibrillator', 'location': 'treasure_room'},
        {'id': 'stimulant_full', 'location': 'treasure_room'},
        {'id': 'tome_con_superrare', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 8,
}
