"""Desert Large City — Archive Voice Dungeon Seed"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# desert_large_city_archive_voice.py
# City: Desert Metropolis (desert_large, Ch.1)
# Chain: Type D — Mythic Weapon (Dune Resonance Blade)
# Player level at encounter: ~5
# Pattern: A — boss guards resonance frequency in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.12
OPEN_AREA_COLOR  = '#8a7050'
IMPASSABLE_COLOR = '#3a2e1e'
BORDER_TILE      = '·'
BORDER_COLOR     = '#5a4030'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'archive_voice', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_minor',      'location': 'treasure_room'},
    {'id': 'stimulant_small', 'location': 'treasure_room'},
    {'id': 'ointment',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['script_remnant', 'archive_shade', 'frequency_construct', 'vault_revenant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'script_remnant',
        'name': 'Script Remnant',
        'hostile_type': 'undead',
        'min_spawn_level': 3,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 28,
        'common_drop': 'herb_minor',
        'rare_drop': None,
        'money_range': (5, 18),
        'basic_attack': 'strikes with a sharpened fragment of ancient script',
        'strong_attack': 'inscription slash',
        'player_abilities': [],
        'base_str': 3, 'base_dex': 3, 'base_con': 2, 'base_int': 2,
        'base_hp': 18, 'base_ap': 2,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 1, 'int_per_level': 0,
        'resistances': [],
        'immunities': [],
        'weaknesses': ['fire'],
    },
    {
        'id': 'archive_shade',
        'name': 'Archive Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 4,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 42,
        'common_drop': 'ointment',
        'rare_drop': None,
        'money_range': (8, 24),
        'basic_attack': 'lashes with a tendril of recorded memory',
        'strong_attack': 'archive drain',
        'player_abilities': [],
        'base_str': 2, 'base_dex': 4, 'base_con': 3, 'base_int': 4,
        'base_hp': 24, 'base_ap': 3,
        'str_per_level': 0, 'dex_per_level': 1, 'con_per_level': 1, 'int_per_level': 2,
        'resistances': ['dark'],
        'immunities': ['sleep'],
        'weaknesses': ['light'],
    },
    {
        'id': 'frequency_construct',
        'name': 'Frequency Construct',
        'hostile_type': 'construct',
        'min_spawn_level': 5,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 62,
        'common_drop': 'stimulant_small',
        'rare_drop': 'herb_med',
        'money_range': (12, 35),
        'basic_attack': 'pulses with resonant force',
        'strong_attack': 'frequency overload',
        'player_abilities': [],
        'base_str': 4, 'base_dex': 2, 'base_con': 7, 'base_int': 3,
        'base_hp': 40, 'base_ap': 3,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 3, 'int_per_level': 0,
        'resistances': ['electric'],
        'immunities': ['stun'],
        'weaknesses': ['fire'],
    },
    {
        'id': 'vault_revenant',
        'name': 'Vault Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 5,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 82,
        'common_drop': 'ointment',
        'rare_drop': 'herb_med',
        'money_range': (18, 52),
        'basic_attack': 'channels the vault\'s stored frequency into a focused strike',
        'strong_attack': 'resonance burst',
        'player_abilities': [],
        'base_str': 5, 'base_dex': 7, 'base_con': 4, 'base_int': 5,
        'base_hp': 52, 'base_ap': 4,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 1,
        'resistances': ['dark'],
        'immunities': ['sleep'],
        'weaknesses': ['light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'archive_voice_boss',
    'name': 'The Archive Voice',
    'hostiles': ['archive_voice_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'archive_voice_1',
        'name': 'The Archive Voice',
        'hostile_type': 'elemental',
        'min_spawn_level': 6,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 1400,
        'common_drop': 'ointment',
        'rare_drop': 'herb_med',
        'money_range': (50, 140),
        'basic_attack': 'unleashes a wave of compressed resonance',
        'strong_attack': 'archive silence',
        'player_abilities': [],
        'base_str': 6, 'base_dex': 8, 'base_con': 6, 'base_int': 12,
        'base_hp': 1500, 'base_ap': 65,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 1, 'int_per_level': 2,
        'resistances': ['dark', 'electric'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'desert_large_city_archive_voice',
    'display_name': 'The Archive Voice',
    'seed': abs(hash('desert_large_city_archive_voice')),
    'floor_count': 1,
    'rooms_per_floor': 3,
    'room_size_min_max': (50, 90),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.05,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (2, 4),
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color': OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile': BORDER_TILE,
    'border_color': BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'visible_distance': 7,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}