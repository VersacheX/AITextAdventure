"""
Edict's Prison - Chapter 14 Dungeon Seed Configuration
A black site for correcting those who are 'too real' for Edict's stage.
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "█"
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = "#787878"
IMPASSABLE_COLOR = "#1c1c1c"
BORDER_TILE      = "·"
BORDER_COLOR     = "#484848"

# Hostiles
FLOOR_HOSTILES = {
    1: ['compliance_officer', 're-education_drone', 'memory_scrubber', 'warden_enforcer'],
}

HOSTILE_SEEDS = [
    {
        'id': 'compliance_officer', 'name': 'Compliance Officer', 'hostile_type': 'humanoid', 'min_spawn_level': 70, 'role': 'damage', 'rarity': 'common',
        'base_xp': 1300, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (250, 500),
        'basic_attack': 'baton strike', 'strong_attack': 'suppression burst', 'player_abilities': [],
        'base_str': 45, 'base_dex': 40, 'base_con': 45, 'base_int': 20, 'base_hp': 4000, 'base_ap': 90,
        'str_per_level': 6, 'dex_per_level': 5, 'con_per_level': 6, 'int_per_level': 2,
        'resistances': ['physical'], 'immunities': [], 'weaknesses': ['electric']
    },
    {
        'id': 're-education_drone', 'name': 'Re-Education Drone', 'hostile_type': 'construct', 'min_spawn_level': 70, 'role': 'hazard', 'rarity': 'uncommon',
        'base_xp': 1400, 'common_drop': 'herb_med', 'rare_drop': None, 'money_range': (280, 560),
        'basic_attack': 'psionic pulse', 'strong_attack': 'conformity beam', 'player_abilities': ['light_faith_lv1_convert'],
        'base_str': 25, 'base_dex': 45, 'base_con': 40, 'base_int': 50, 'base_hp': 3800, 'base_ap': 110,
        'str_per_level': 3, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 7,
        'resistances': ['light'], 'immunities': ['confuse'], 'weaknesses': ['dark']
    },
    {
        'id': 'memory_scrubber', 'name': 'Memory Scrubber', 'hostile_type': 'aberration', 'min_spawn_level': 71, 'role': 'hazard', 'rarity': 'rare',
        'base_xp': 1600, 'common_drop': 'panacea', 'rare_drop': 'tome_int_superrare', 'money_range': (350, 700),
        'basic_attack': 'erase thought', 'strong_attack': 'identity wipe', 'player_abilities': ['dark_faith_lv1_shade_whisper'],
        'base_str': 30, 'base_dex': 40, 'base_con': 38, 'base_int': 55, 'base_hp': 3500, 'base_ap': 130,
        'str_per_level': 3, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 8,
        'resistances': ['dark', 'ice'], 'immunities': ['sleep', 'stun'], 'weaknesses': ['fire']
    },
    {
        'id': 'warden_enforcer', 'name': 'Warden Enforcer', 'hostile_type': 'construct', 'min_spawn_level': 72, 'role': 'damage', 'rarity': 'superrare',
        'base_xp': 2000, 'common_drop': 'stimulant_full', 'rare_drop': 'tome_con_superrare', 'money_range': (450, 900),
        'basic_attack': 'crushing blow', 'strong_attack': 'containment field', 'player_abilities': [],
        'base_str': 60, 'base_dex': 30, 'base_con': 60, 'base_int': 10, 'base_hp': 7000, 'base_ap': 100,
        'str_per_level': 8, 'dex_per_level': 3, 'con_per_level': 8, 'int_per_level': 1,
        'resistances': ['physical', 'electric'], 'immunities': ['stun', 'petrify'], 'weaknesses': ['water']
    }
]

# Boss
DUNGEON_NPCS = [
    {'id': 'prison_warden', 'location': 'final_chamber'}
]
BOSS_MOB = {
    'id': 'prison_warden_boss_battle',
    'name': 'Prison Warden',
    'hostiles': ['prison_warden_boss']
}

BOSS_HOSTILES = [
    {
        'id': 'prison_warden_boss', 'name': 'Prison Warden', 'hostile_type': 'construct', 'min_spawn_level': 72, 'role': 'damage', 'rarity': 'notfound',
        'base_xp': 20000, 'common_drop': 'tome_con_superrare', 'rare_drop': 'standard_warblade', 'money_range': (2500, 5000),
        'basic_attack': 'judgement strike', 'strong_attack': 'protocol omega', 'player_abilities': ['earth_technique_lv1_armor_up'],
        'base_str': 65, 'base_dex': 35, 'base_con': 65, 'base_int': 30, 'base_hp': 80000, 'base_ap': 400,
        'str_per_level': 9, 'dex_per_level': 4, 'con_per_level': 9, 'int_per_level': 3,
        'resistances': ['physical', 'electric', 'ice'], 'immunities': ['stun', 'petrify', 'confuse'], 'weaknesses': ['fire']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'edicts_prison',
    'seed': abs(hash('edicts_prison')),
    'floor_count': 2,
    'room_size_min_max': (80, 150),
    'rooms_per_floor': 5,
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.0,
    'min_max_distance_between_rooms': (4, 8),
    'min_max_corridor_width': (2, 4),
    'display_name': "Edict's Correctional Facility",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color':  OPEN_AREA_COLOR,
	'impassable_color': IMPASSABLE_COLOR,
	'border_tile':      BORDER_TILE,
	'border_color':     BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': [{'id': 'prison_warden', 'location': 'final_chamber'}],
    'items': [
        {'id': 'defibrillator', 'location': 'treasure_room'},
        {'id': 'panacea', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 7,
}
