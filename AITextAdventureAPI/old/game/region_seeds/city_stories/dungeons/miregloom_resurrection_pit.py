"""Swamp Large City — Miregloom Resurrection Pit Dungeon Seed (Type B)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# miregloom_resurrection_pit.py
# City: The Necropolis (swamp_large, Ch.13)
# Chain: Type B — Regional Boss / Void Gauntlet (Grimnaw)
# Player level at encounter: ~65
# Pattern: B — player teleported to final_chamber; boss = miregloom_b1
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.12
OPEN_AREA_COLOR  = '#2a3820'
IMPASSABLE_COLOR = '#0c1008'
BORDER_TILE      = '·'
BORDER_COLOR     = '#1c2818'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'miregloom', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['rot_shard', 'necropolis_shade', 'bone_sentinel', 'void_marrow'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'rot_shard',
        'name': 'Rot Shard',
        'hostile_type': 'undead',
        'min_spawn_level': 63,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 458,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (124, 396),
        'basic_attack': 'splinters off and drives a rot-soaked shard into its target',
        'strong_attack': 'shard burst',
        'player_abilities': [],
        'base_str': 44, 'base_dex': 38, 'base_con': 32, 'base_int': 16,
        'base_hp': 880, 'base_ap': 14,
        'str_per_level': 5, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['dark', 'earth'],
        'immunities': ['poison', 'sleep'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'necropolis_shade',
        'name': 'Necropolis Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 64,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 558,
        'common_drop': 'stimulant_med',
        'rare_drop': 'herb_med',
        'money_range': (150, 478),
        'basic_attack': 'drains the target through layers of accumulated rot',
        'strong_attack': 'necropolis drain',
        'player_abilities': [],
        'base_str': 26, 'base_dex': 46, 'base_con': 28, 'base_int': 32,
        'base_hp': 895, 'base_ap': 14,
        'str_per_level': 1, 'dex_per_level': 5, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark'],
        'immunities': ['confuse', 'poison', 'sleep'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'bone_sentinel',
        'name': 'Bone Sentinel',
        'hostile_type': 'undead',
        'min_spawn_level': 65,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 710,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (188, 600),
        'basic_attack': 'slams with a column of fused bone',
        'strong_attack': 'bone collapse',
        'player_abilities': [],
        'base_str': 32, 'base_dex': 18, 'base_con': 56, 'base_int': 12,
        'base_hp': 1180, 'base_ap': 14,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 6, 'int_per_level': 1,
        'resistances': ['physical', 'dark', 'earth'],
        'immunities': ['stun', 'slow', 'poison'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'void_marrow',
        'name': 'Void Marrow',
        'hostile_type': 'elemental',
        'min_spawn_level': 65,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 956,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (224, 716),
        'basic_attack': 'forces void-corruption through exposed bone into a strike',
        'strong_attack': 'marrow void surge',
        'player_abilities': [],
        'base_str': 40, 'base_dex': 42, 'base_con': 34, 'base_int': 38,
        'base_hp': 1100, 'base_ap': 16,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse', 'poison'],
        'weaknesses': ['light', 'fire'],
    },
]

BOSS_MOB: Dict = {
    'id': 'miregloom_boss',
    'name': 'Lich-King Miregloom',
    'hostiles': ['miregloom_b1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'miregloom_b1',
        'name': 'Lich-King Miregloom',
        'hostile_type': 'undead',
        'min_spawn_level': 66,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 28000,
        'common_drop': 'stimulant_med',
        'rare_drop': 'stimulant_med',
        'money_range': (680, 2040),
        'basic_attack': 'channels the rot of every grave in the Necropolis into a directed strike',
        'strong_attack': 'grave architecture',
        'player_abilities': [],
        'base_str': 52, 'base_dex': 50, 'base_con': 48, 'base_int': 58,
        'base_hp': 34000, 'base_ap': 520,
        'str_per_level': 5, 'dex_per_level': 5, 'con_per_level': 5, 'int_per_level': 6,
        'resistances': ['dark', 'earth', 'physical'],
        'immunities': ['sleep', 'confuse', 'poison', 'stun', 'slow'],
        'weaknesses': ['fire', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'miregloom_resurrection_pit',
    'display_name': 'The Resurrection Pit',
    'seed': abs(hash('miregloom_resurrection_pit')),
    'floor_count': 1,
    'rooms_per_floor': 5,
    'room_size_min_max': (60, 115),
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