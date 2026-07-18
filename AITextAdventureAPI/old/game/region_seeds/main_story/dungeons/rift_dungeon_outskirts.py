"""
Rift Dungeon Outskirts - Chapter 5 Dungeon Seed Configuration
The chaotic space where the player lands after Astra Wynn's Riftcall.
"""

from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "▒"
IMPASSABLE_TILE = "█"
IMPASSABLE_CHANCE = 0.05
OPEN_AREA_COLOR  = "#6a4a8a"
IMPASSABLE_COLOR = "#28183a"
BORDER_TILE      = "·"
BORDER_COLOR     = "#4a3060"

# Hostiles for this area
FLOOR_HOSTILES = {
    1: ['outskirts_rift_shade', 'outskirts_echo_stalker', 'outskirts_unstable_fragment'],
}

HOSTILE_SEEDS = [
    {
        'id': 'outskirts_rift_shade',
        'name': 'Rift Shade',
        'hostile_type': 'spirit',
        'min_spawn_level': 25,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 200,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (18, 36),
        'basic_attack': 'shadow graze',
        'strong_attack': 'rift pulse',
        'player_abilities': ['dark_dark_magic_lv2_umbra_storm'],
        'base_str': 8, 'base_dex': 14, 'base_con': 10, 'base_int': 18,
        'base_hp': 420, 'base_ap': 40,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 3,
        'resistances': ['dark'], 'immunities': ['continuous_damage'], 'weaknesses': ['light']
    },
    {
        'id': 'outskirts_echo_stalker',
        'name': 'Echo Stalker',
        'hostile_type': 'beast',
        'min_spawn_level': 25,
        'role': 'damage',
        'rarity': 'rare',
        'base_xp': 180,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (14, 32),
        'basic_attack': 'echo slash',
        'strong_attack': 'phase rend',
        'player_abilities': ['air_dark_skill_lv2_gale_of_doubt'],
        'base_str': 14, 'base_dex': 16, 'base_con': 12, 'base_int': 6,
        'base_hp': 380, 'base_ap': 32,
        'str_per_level': 2, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 0,
        'resistances': ['physical'], 'immunities': [], 'weaknesses': ['ice']
    },
    {
        'id': 'outskirts_unstable_fragment',
        'name': 'Unstable Fragment',
        'hostile_type': 'elemental',
        'min_spawn_level': 25,
        'role': 'hazard',
        'rarity': 'common',
        'base_xp': 140,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (10, 20),
        'basic_attack': 'fracture burst',
        'strong_attack': 'volatile detonation',
        'player_abilities': ['electric_dark_tech_lv2_void_shocker'],
        'base_str': 10, 'base_dex': 10, 'base_con': 8, 'base_int': 14,
        'base_hp': 300, 'base_ap': 28,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 1, 'int_per_level': 2,
        'resistances': ['electric'], 'immunities': [], 'weaknesses': ['earth']
    }
]

# No boss in this area, it's a landing zone.
BOSS_MOB = {}
BOSS_HOSTILES = []

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'rift_dungeon_outskirts',
    'seed': abs(hash('rift_dungeon_outskirts')),
    'floor_count': 1,
    'room_size_min_max': (100, 150),
    'rooms_per_floor': 6, # Only one "room" or area to land in
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.0,
    'min_max_distance_between_rooms': (0, 0),
    'min_max_corridor_width': (1, 1),
    'display_name': "Rift Dungeon Outskirts",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color':  OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile':      BORDER_TILE,
    'border_color':     BORDER_COLOR,
    'impassable_chance': 0.25, # More chaotic than the main dungeon
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': [],
    'items': [
        {'id': 'stimulant_large', 'location': 'treasure_room'},
        {'id': 'tome_dex', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 7,
}
