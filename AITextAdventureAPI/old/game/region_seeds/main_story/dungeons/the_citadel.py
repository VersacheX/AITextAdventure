"""
The Citadel - Chapter 15 Dungeon Seed Configuration
The heart of Edict's control system, a sterile and oppressive fortress.
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "█"
IMPASSABLE_CHANCE = 0.05
OPEN_AREA_COLOR  = "#909090"
IMPASSABLE_COLOR = "#202020"
BORDER_TILE      = "·"
BORDER_COLOR     = "#606060"

# Hostiles
FLOOR_HOSTILES = {
    1: ['citadel_sentry', 'edict_enforcer', 'propaganda_drone', 'praetorian_guard'],
}

HOSTILE_SEEDS = [
    {
        'id': 'citadel_sentry', 'name': 'Citadel Sentry', 'hostile_type': 'construct', 'min_spawn_level': 75, 'role': 'damage', 'rarity': 'common',
        'base_xp': 1700, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (350, 700),
        'basic_attack': 'laser pulse', 'strong_attack': 'targeting sweep', 'player_abilities': [],
        'base_str': 50, 'base_dex': 50, 'base_con': 50, 'base_int': 30, 'base_hp': 5500, 'base_ap': 120,
        'str_per_level': 7, 'dex_per_level': 7, 'con_per_level': 7, 'int_per_level': 4,
        'resistances': ['electric'], 'immunities': [], 'weaknesses': ['earth']
    },
    {
        'id': 'edict_enforcer', 'name': 'Edict Enforcer', 'hostile_type': 'humanoid', 'min_spawn_level': 75, 'role': 'damage', 'rarity': 'uncommon',
        'base_xp': 1800, 'common_drop': 'herb_med', 'rare_drop': None, 'money_range': (400, 800),
        'basic_attack': 'compliance strike', 'strong_attack': 'judgment blow', 'player_abilities': [],
        'base_str': 55, 'base_dex': 45, 'base_con': 55, 'base_int': 25, 'base_hp': 6000, 'base_ap': 110,
        'str_per_level': 8, 'dex_per_level': 6, 'con_per_level': 8, 'int_per_level': 3,
        'resistances': ['physical'], 'immunities': ['confuse'], 'weaknesses': ['ice']
    },
    {
        'id': 'propaganda_drone', 'name': 'Propaganda Drone', 'hostile_type': 'construct', 'min_spawn_level': 76, 'role': 'hazard', 'rarity': 'rare',
        'base_xp': 2000, 'common_drop': 'panacea', 'rare_drop': 'tome_int_superrare', 'money_range': (500, 1000),
        'basic_attack': 'sonic disruption', 'strong_attack': 'loyalty broadcast', 'player_abilities': ['light_spirit_lv1_convert'],
        'base_str': 30, 'base_dex': 55, 'base_con': 45, 'base_int': 60, 'base_hp': 5000, 'base_ap': 150,
        'str_per_level': 4, 'dex_per_level': 8, 'con_per_level': 6, 'int_per_level': 9,
        'resistances': ['air', 'light'], 'immunities': ['sleep'], 'weaknesses': ['dark']
    },
    {
        'id': 'praetorian_guard', 'name': 'Praetorian Guard', 'hostile_type': 'construct', 'min_spawn_level': 77, 'role': 'damage', 'rarity': 'superrare',
        'base_xp': 2500, 'common_drop': 'defibrillator', 'rare_drop': 'tome_con_superrare', 'money_range': (600, 1200),
        'basic_attack': 'power cleave', 'strong_attack': 'annihilation protocol', 'player_abilities': [],
        'base_str': 70, 'base_dex': 40, 'base_con': 70, 'base_int': 20, 'base_hp': 9000, 'base_ap': 120,
        'str_per_level': 10, 'dex_per_level': 5, 'con_per_level': 10, 'int_per_level': 2,
        'resistances': ['physical', 'fire', 'ice', 'electric'], 'immunities': ['stun', 'petrify'], 'weaknesses': []
    }
]

# Boss
DUNGEON_NPCS = [
    {'id': 'edict', 'location': 'final_chamber'}
]
BOSS_MOB = {
    'id': 'pageant_edict_stigma_1',
    'name': 'Edict, Stigma, and Pageant',
    'hostiles': ['edict_boss', 'stigma_boss', 'pageant_boss_final']
}

BOSS_HOSTILES = [
    {
        'id': 'edict_boss', 'name': 'Edict', 'hostile_type': 'humanoid', 'min_spawn_level': 78, 'role': 'damage', 'rarity': 'notfound',
        'base_xp': 30000, 'common_drop': 'tome_con_superrare', 'rare_drop': 'undying_oath_ring', 'money_range': (5000, 10000),
        'basic_attack': 'system shock', 'strong_attack': 'defragment reality', 'player_abilities': ['ancient_rule', 'inescapable_edict', 'ritual_punishment', 'the_letter_of_the_law'],
        'base_str': 60, 'base_dex': 60, 'base_con': 70, 'base_int': 80, 'base_hp': 100000, 'base_ap': 1000,
        'str_per_level': 8, 'dex_per_level': 8, 'con_per_level': 9, 'int_per_level': 10,
        'resistances': ['physical', 'electric'], 'immunities': ['stun', 'confuse', 'petrify'], 'weaknesses': ['fire']
    },
    {
        'id': 'stigma_boss', 'name': 'Stigma', 'hostile_type': 'aberration', 'min_spawn_level': 78, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 30000, 'common_drop': 'tome_int_superrare', 'rare_drop': 'undying_oath_ring', 'money_range': (5000, 10000),
        'basic_attack': 'love bomb', 'strong_attack': 'unconditional acceptance', 'player_abilities': ['void_refraction', 'the_darkness_consuming', 'identity_collapse', 'you_can_be_me'],
        'base_str': 50, 'base_dex': 70, 'base_con': 60, 'base_int': 75, 'base_hp': 80000, 'base_ap': 1200,
        'str_per_level': 6, 'dex_per_level': 9, 'con_per_level': 7, 'int_per_level': 9,
        'resistances': ['light', 'air'], 'immunities': ['sleep'], 'weaknesses': ['dark']
    },
    {
        'id': 'pageant_boss_final', 'name': 'Pageant', 'hostile_type': 'spirit', 'min_spawn_level': 78, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 30000, 'common_drop': 'tome_dex_superrare', 'rare_drop': 'undying_oath_ring', 'money_range': (5000, 10000),
        'basic_attack': 'encore', 'strong_attack': 'curtain call', 'player_abilities': ['mask_of_expectation', 'crushing_reputation', 'curtain_call_offensive', 'obligation_chain'],
        'base_str': 45, 'base_dex': 80, 'base_con': 55, 'base_int': 65, 'base_hp': 75000, 'base_ap': 1100,
        'str_per_level': 5, 'dex_per_level': 10, 'con_per_level': 6, 'int_per_level': 8,
        'resistances': ['air'], 'immunities': ['confuse'], 'weaknesses': ['earth']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'the_citadel',
    'seed': abs(hash('the_citadel')),
    'floor_count': 1,
    'room_size_min_max': (150, 250),
    'rooms_per_floor': 10,
    'max_neighbors_per_room': 4,
    'additional_connection_chance': 0.1,
    'min_max_distance_between_rooms': (5, 10),
    'min_max_corridor_width': (4, 8),
    'display_name': "The Citadel",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color':  OPEN_AREA_COLOR,
	'impassable_color': IMPASSABLE_COLOR,
	'border_tile':      BORDER_TILE,
	'border_color':     BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': [{'id': 'pageant_edict_stigma_1', 'location': 'final_chamber'}],
    'items': [
        {'id': 'defibrillator', 'location': 'treasure_room'},
        {'id': 'panacea', 'location': 'treasure_room'},
        {'id': 'tome_hp_superrare', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 10,
}
