"""Swamp Large City — Relicmire Sump Dungeon Seed (Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# relicmire_sump.py
# City: The Necropolis (swamp_large, Ch.13)
# Chain: Type D — Mythic Weapon (Bonedrown Reliquary)
# Player level at encounter: ~65
# Pattern: A — boss guards drowned Necropolis metal in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.13
OPEN_AREA_COLOR  = '#253020'
IMPASSABLE_COLOR = '#0a0e08'
BORDER_TILE      = '·'
BORDER_COLOR     = '#1a2416'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'relicmire_voice', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['sump_crawler', 'relic_shade', 'marrow_sentinel', 'void_drowned'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'sump_crawler',
        'name': 'Sump Crawler',
        'hostile_type': 'beast',
        'min_spawn_level': 63,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 458,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (124, 396),
        'basic_attack': 'drags through the sump to strike with bone-encrusted claws',
        'strong_attack': 'sump lunge',
        'player_abilities': [],
        'base_str': 46, 'base_dex': 38, 'base_con': 34, 'base_int': 14,
        'base_hp': 875, 'base_ap': 14,
        'str_per_level': 5, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['water', 'earth'],
        'immunities': ['slow', 'poison'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'relic_shade',
        'name': 'Relic Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 64,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 558,
        'common_drop': 'stimulant_med',
        'rare_drop': 'herb_med',
        'money_range': (150, 478),
        'basic_attack': 'channels the memory of a drowned relic into a draining strike',
        'strong_attack': 'relic drain',
        'player_abilities': [],
        'base_str': 28, 'base_dex': 46, 'base_con': 28, 'base_int': 34,
        'base_hp': 890, 'base_ap': 14,
        'str_per_level': 1, 'dex_per_level': 5, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep', 'confuse', 'poison'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'marrow_sentinel',
        'name': 'Marrow Sentinel',
        'hostile_type': 'undead',
        'min_spawn_level': 65,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 710,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (188, 600),
        'basic_attack': 'drives a column of fused bone and sump-iron into the target',
        'strong_attack': 'marrow press',
        'player_abilities': [],
        'base_str': 34, 'base_dex': 18, 'base_con': 58, 'base_int': 12,
        'base_hp': 1185, 'base_ap': 14,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 6, 'int_per_level': 1,
        'resistances': ['physical', 'dark', 'water'],
        'immunities': ['stun', 'slow', 'poison'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'void_drowned',
        'name': 'Void Drowned',
        'hostile_type': 'elemental',
        'min_spawn_level': 65,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 956,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (224, 716),
        'basic_attack': 'forces void-corruption through drowned relic-metal into a strike',
        'strong_attack': 'void submersion',
        'player_abilities': [],
        'base_str': 42, 'base_dex': 44, 'base_con': 34, 'base_int': 40,
        'base_hp': 1105, 'base_ap': 16,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep', 'confuse', 'poison'],
        'weaknesses': ['light', 'fire'],
    },
]

BOSS_MOB: Dict = {
    'id': 'relicmire_voice_boss',
    'name': 'The Relicmire Voice',
    'hostiles': ['relicmire_voice_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'relicmire_voice_1',
        'name': 'The Relicmire Voice',
        'hostile_type': 'elemental',
        'min_spawn_level': 66,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 28500,
        'common_drop': 'stimulant_med',
        'rare_drop': 'stimulant_med',
        'money_range': (695, 2085),
        'basic_attack': 'surges the sump upward and drives centuries of drowned metal through the target',
        'strong_attack': 'relicmire submersion',
        'player_abilities': [],
        'base_str': 54, 'base_dex': 50, 'base_con': 50, 'base_int': 56,
        'base_hp': 35000, 'base_ap': 525,
        'str_per_level': 5, 'dex_per_level': 5, 'con_per_level': 5, 'int_per_level': 6,
        'resistances': ['dark', 'water', 'earth', 'physical'],
        'immunities': ['sleep', 'confuse', 'poison', 'fear', 'stun', 'slow'],
        'weaknesses': ['fire', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'relicmire_sump',
    'display_name': 'The Relicmire Sump',
    'seed': abs(hash('relicmire_sump')),
    'floor_count': 1,
    'rooms_per_floor': 4,
    'room_size_min_max': (55, 110),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.08,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (3, 6),
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