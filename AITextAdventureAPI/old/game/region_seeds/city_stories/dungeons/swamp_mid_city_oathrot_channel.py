"""Swamp Mid City — Oathrot Channel Dungeon Seed (Type B)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# swamp_mid_city_oathrot_channel.py
# City: Murkchannel (swamp_mid, Ch.20)
# Chain: Type B — Regional Boss / Void Gauntlet (Vex)
# Player level at encounter: ~100
# Pattern: B — player teleported to final_chamber; boss = oathrot_b1
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.13
OPEN_AREA_COLOR  = '#203018'
IMPASSABLE_COLOR = '#0a100a'
BORDER_TILE      = '·'
BORDER_COLOR     = '#182410'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'oathrot', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['sworn_rot', 'channel_shade', 'oath_sentinel', 'void_oath'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'sworn_rot',
        'name': 'Sworn Rot',
        'hostile_type': 'undead',
        'min_spawn_level': 98,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 724,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (196, 628),
        'basic_attack': 'strikes with the compacted rot of a broken oath',
        'strong_attack': 'oath strike',
        'player_abilities': [],
        'base_str': 72, 'base_dex': 62, 'base_con': 56, 'base_int': 30,
        'base_hp': 1400, 'base_ap': 20,
        'str_per_level': 7, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 2,
        'resistances': ['dark', 'earth', 'water'],
        'immunities': ['poison', 'sleep', 'slow'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'channel_shade',
        'name': 'Channel Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 99,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 882,
        'common_drop': 'stimulant_med',
        'rare_drop': 'herb_med',
        'money_range': (234, 750),
        'basic_attack': 'channels a drowned oath through the swamp into a draining pulse',
        'strong_attack': 'channel drain',
        'player_abilities': [],
        'base_str': 42, 'base_dex': 74, 'base_con': 44, 'base_int': 54,
        'base_hp': 1415, 'base_ap': 20,
        'str_per_level': 1, 'dex_per_level': 7, 'con_per_level': 3, 'int_per_level': 5,
        'resistances': ['dark', 'water'],
        'immunities': ['sleep', 'confuse', 'poison'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'oath_sentinel',
        'name': 'Oath Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 100,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 1120,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (292, 936),
        'basic_attack': 'guards the channel and strikes with the weight of every broken oath it holds',
        'strong_attack': 'oath press',
        'player_abilities': [],
        'base_str': 50, 'base_dex': 30, 'base_con': 92, 'base_int': 20,
        'base_hp': 1880, 'base_ap': 20,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 8, 'int_per_level': 2,
        'resistances': ['dark', 'earth', 'water', 'physical'],
        'immunities': ['stun', 'slow', 'poison', 'confuse'],
        'weaknesses': ['fire', 'electric'],
    },
    {
        'id': 'void_oath',
        'name': 'Void Oath',
        'hostile_type': 'elemental',
        'min_spawn_level': 100,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 1508,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (352, 1126),
        'basic_attack': 'drives void-corruption through every broken oath in the channel into a strike',
        'strong_attack': 'void oath surge',
        'player_abilities': [],
        'base_str': 64, 'base_dex': 68, 'base_con': 58, 'base_int': 66,
        'base_hp': 1780, 'base_ap': 22,
        'str_per_level': 6, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 6,
        'resistances': ['dark', 'earth', 'water'],
        'immunities': ['sleep', 'confuse', 'poison'],
        'weaknesses': ['fire', 'light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'oathrot_boss',
    'name': 'The Oathrot',
    'hostiles': ['oathrot_b1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'oathrot_b1',
        'name': 'The Oathrot',
        'hostile_type': 'elemental',
        'min_spawn_level': 102,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 62000,
        'common_drop': 'stimulant_med',
        'rare_drop': 'stimulant_med',
        'money_range': (1500, 4500),
        'basic_attack': 'drives every broken oath ever sworn in Murkchannel through the target in a single rotting tide',
        'strong_attack': 'channel of oaths',
        'player_abilities': [],
        'base_str': 80, 'base_dex': 76, 'base_con': 78, 'base_int': 86,
        'base_hp': 74000, 'base_ap': 940,
        'str_per_level': 8, 'dex_per_level': 7, 'con_per_level': 7, 'int_per_level': 8,
        'resistances': ['dark', 'earth', 'water', 'physical'],
        'immunities': ['sleep', 'confuse', 'fear', 'stun', 'slow', 'poison'],
        'weaknesses': ['fire', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'swamp_mid_city_oathrot_channel',
    'display_name': 'The Oathrot Channel',
    'seed': abs(hash('swamp_mid_city_oathrot_channel')),
    'floor_count': 1,
    'rooms_per_floor': 5,
    'room_size_min_max': (65, 120),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.08,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (3, 7),
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