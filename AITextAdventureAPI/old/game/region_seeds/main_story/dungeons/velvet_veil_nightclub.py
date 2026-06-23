"""
Velvet Veil Nightclub - Chapter 15 Dungeon Seed Configuration
A pulsing nightclub of forced ecstasy and performance, ruled by Pageant.
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "▒"
IMPASSABLE_TILE = "█"
IMPASSABLE_CHANCE = 0.1

# Hostiles
FLOOR_HOSTILES = {
    1: ['veil_bouncer', 'mirror_dancer', 'ecstasy_addict', 'elite_enforcer'],
}

HOSTILE_SEEDS = [
    {
        'id': 'veil_bouncer', 'name': 'Veil Bouncer', 'hostile_type': 'construct', 'min_spawn_level': 75, 'role': 'damage', 'rarity': 'common',
        'base_xp': 1500, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (300, 600),
        'basic_attack': 'heavy blow', 'strong_attack': 'crowd control', 'player_abilities': [],
        'base_str': 50, 'base_dex': 30, 'base_con': 50, 'base_int': 10, 'base_hp': 5000, 'base_ap': 100,
        'str_per_level': 7, 'dex_per_level': 3, 'con_per_level': 7, 'int_per_level': 1,
        'resistances': ['physical'], 'immunities': ['stun'], 'weaknesses': ['electric']
    },
    {
        'id': 'mirror_dancer', 'name': 'Mirror Dancer', 'hostile_type': 'spirit', 'min_spawn_level': 75, 'role': 'hazard', 'rarity': 'uncommon',
        'base_xp': 1600, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (350, 700),
        'basic_attack': 'shattered reflection', 'strong_attack': 'dazzling pirouette', 'player_abilities': ['light_faith_lv1_convert'],
        'base_str': 35, 'base_dex': 50, 'base_con': 35, 'base_int': 45, 'base_hp': 4500, 'base_ap': 120,
        'str_per_level': 4, 'dex_per_level': 7, 'con_per_level': 4, 'int_per_level': 6,
        'resistances': ['light', 'air'], 'immunities': ['confuse'], 'weaknesses': ['dark']
    },
    {
        'id': 'ecstasy_addict', 'name': 'Ecstasy Addict', 'hostile_type': 'humanoid', 'min_spawn_level': 76, 'role': 'damage', 'rarity': 'rare',
        'base_xp': 1800, 'common_drop': 'panacea', 'rare_drop': 'tome_dex_superrare', 'money_range': (400, 800),
        'basic_attack': 'frenzied strike', 'strong_attack': 'uncontrolled rage', 'player_abilities': [],
        'base_str': 48, 'base_dex': 45, 'base_con': 40, 'base_int': 15, 'base_hp': 4800, 'base_ap': 110,
        'str_per_level': 6, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 2,
        'resistances': [], 'immunities': ['fear'], 'weaknesses': ['ice']
    },
    {
        'id': 'elite_enforcer', 'name': 'Elite Enforcer', 'hostile_type': 'humanoid', 'min_spawn_level': 77, 'role': 'damage', 'rarity': 'superrare',
        'base_xp': 2200, 'common_drop': 'stimulant_full', 'rare_drop': 'tome_str_superrare', 'money_range': (500, 1000),
        'basic_attack': 'compliance baton', 'strong_attack': 'suppression field', 'player_abilities': [],
        'base_str': 55, 'base_dex': 40, 'base_con': 55, 'base_int': 25, 'base_hp': 6000, 'base_ap': 130,
        'str_per_level': 8, 'dex_per_level': 5, 'con_per_level': 8, 'int_per_level': 3,
        'resistances': ['physical'], 'immunities': ['stun', 'confuse'], 'weaknesses': ['electric']
    }
]

# Boss

DUNGEON_NPCS = [
    {'id': 'pageant', 'location': 'final_chamber'}
]
BOSS_MOB = {
    'id': 'pageant_boss_battle_1',
    'name': 'Pageant',
    'hostiles': ['pageant_boss']
}

BOSS_HOSTILES = [
    {
        'id': 'pageant_boss', 'name': 'Pageant', 'hostile_type': 'humanoid', 'min_spawn_level': 77, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 25000, 'common_drop': 'tome_dex_superrare', 'rare_drop': 'pageant_mask', 'money_range': (3000, 6000),
        'basic_attack': 'perfect smile', 'strong_attack': 'final performance', 'player_abilities': ['mask_of_expectation', 'crushing_reputation', 'obligation_chain'],
        'base_str': 40, 'base_dex': 60, 'base_con': 45, 'base_int': 55, 'base_hp': 60000, 'base_ap': 800,
        'str_per_level': 5, 'dex_per_level': 8, 'con_per_level': 5, 'int_per_level': 7,
        'resistances': ['light', 'air'], 'immunities': ['confuse', 'fear'], 'weaknesses': ['dark', 'earth']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'velvet_veil_nightclub',
    'seed': abs(hash('velvet_veil_nightclub')),
    'floor_count': 1,
    'room_size_min_max': (100, 200),
    'rooms_per_floor': 7,
    'max_neighbors_per_room': 3,
    'additional_connection_chance': 0.2,
    'min_max_distance_between_rooms': (3, 6),
    'min_max_corridor_width': (3, 5),
    'display_name': "The Velvet Veil",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': [{'id': 'pageant', 'location': 'final_chamber'}],
    'items': [
        {'id': 'defibrillator', 'location': 'treasure_room'},
        {'id': 'panacea', 'location': 'treasure_room'},
        {'id': 'tome_ap_superrare', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 8,
}
