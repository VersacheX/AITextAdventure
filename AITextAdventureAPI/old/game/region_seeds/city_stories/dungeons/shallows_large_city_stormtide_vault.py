"""Shallows Large City — Stormtide Vault Dungeon Seed (Type E)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# shallows_large_city_stormtide_vault.py
# City: Blackwake Harbor (shallows_large, Ch.5)
# Chain: Type E — Artifact (Brine Compass)
# Player level at encounter: ~25
# Pattern: A — boss guards compass in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = '#305870'
IMPASSABLE_COLOR = '#101e28'
BORDER_TILE      = '·'
BORDER_COLOR     = '#204058'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'stormtide_echo', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_med', 'location': 'treasure_room'},
    {'id': 'petrify_salve',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['tide_crawler', 'drowned_spirit', 'reef_stalker', 'storm_revenant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'tide_crawler',
        'name': 'Tide Crawler',
        'hostile_type': 'beast',
        'min_spawn_level': 23,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 168,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (28, 88),
        'basic_attack': 'claws with tide-sharpened talons',
        'strong_attack': 'tide rake',
        'player_abilities': [],
        'base_str': 16, 'base_dex': 14, 'base_con': 13, 'base_int': 3,
        'base_hp': 280, 'base_ap': 7,
        'str_per_level': 3, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 0,
        'resistances': ['water'],
        'immunities': [],
        'weaknesses': ['electric', 'light'],
    },
    {
        'id': 'drowned_spirit',
        'name': 'Drowned Spirit',
        'hostile_type': 'undead',
        'min_spawn_level': 24,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 210,
        'common_drop': 'petrify_salve',
        'rare_drop': 'herb_med',
        'money_range': (34, 108),
        'basic_attack': 'drags with waterlogged hands',
        'strong_attack': 'drowning pull',
        'player_abilities': [],
        'base_str': 10, 'base_dex': 12, 'base_con': 10, 'base_int': 8,
        'base_hp': 295, 'base_ap': 7,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'reef_stalker',
        'name': 'Reef Stalker',
        'hostile_type': 'beast',
        'min_spawn_level': 25,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 272,
        'common_drop': 'stimulant_med',
        'rare_drop': 'petrify_salve',
        'money_range': (44, 138),
        'basic_attack': 'slams with a reef-encrusted carapace',
        'strong_attack': 'reef crash',
        'player_abilities': [],
        'base_str': 14, 'base_dex': 8, 'base_con': 22, 'base_int': 3,
        'base_hp': 400, 'base_ap': 7,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 4, 'int_per_level': 0,
        'resistances': ['physical', 'water'],
        'immunities': ['stun'],
        'weaknesses': ['electric'],
    },
    {
        'id': 'storm_revenant',
        'name': 'Storm Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 25,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 368,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (62, 196),
        'basic_attack': 'unleashes a concentrated bolt of stormtide energy',
        'strong_attack': 'stormtide burst',
        'player_abilities': [],
        'base_str': 15, 'base_dex': 18, 'base_con': 13, 'base_int': 14,
        'base_hp': 360, 'base_ap': 8,
        'str_per_level': 2, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 2,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'electric'],
    },
]

BOSS_MOB: Dict = {
    'id': 'stormtide_echo_boss',
    'name': 'The Stormtide Echo',
    'hostiles': ['stormtide_echo_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'stormtide_echo_1',
        'name': 'The Stormtide Echo',
        'hostile_type': 'elemental',
        'min_spawn_level': 26,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 5500,
        'common_drop': 'petrify_salve',
        'rare_drop': 'stimulant_med',
        'money_range': (150, 430),
        'basic_attack': 'floods the vault with compressed tide-energy',
        'strong_attack': 'stormtide collapse',
        'player_abilities': [],
        'base_str': 20, 'base_dex': 24, 'base_con': 20, 'base_int': 22,
        'base_hp': 7200, 'base_ap': 145,
        'str_per_level': 2, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['water', 'dark', 'physical'],
        'immunities': ['sleep', 'confuse', 'slow'],
        'weaknesses': ['light', 'electric'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'shallows_large_city_stormtide_vault',
    'display_name': 'The Stormtide Vault',
    'seed': abs(hash('shallows_large_city_stormtide_vault')),
    'floor_count': 1,
    'rooms_per_floor': 3,
    'room_size_min_max': (55, 100),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.07,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (3, 6),
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color': OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile': BORDER_TILE,
    'border_color': BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'visible_distance': 8,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}