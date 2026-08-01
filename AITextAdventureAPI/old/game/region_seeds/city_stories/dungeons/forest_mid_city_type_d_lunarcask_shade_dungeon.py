"""Forest Mid City — Lunarcask Shade Dungeon Seed (Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# forest_mid_city_type_d_lunarcask_shade_dungeon.py
# City: Cindercanopy Exchange (forest_mid, Ch.2)
# Chain: Type D — Mythic Accessory (Moonbriar Lantern)
# Player level at encounter: ~10
# Pattern: A — boss guards solidified moonlight in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#3a4858'
IMPASSABLE_COLOR = '#141820'
BORDER_TILE      = '·'
BORDER_COLOR     = '#2a3848'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'lunarcask_shade', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',        'location': 'treasure_room'},
    {'id': 'stimulant_small', 'location': 'treasure_room'},
    {'id': 'remedy_small',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['moonshade_crawler', 'bark_phantom', 'thornwood_stalker', 'cask_revenant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'moonshade_crawler',
        'name': 'Moonshade Crawler',
        'hostile_type': 'beast',
        'min_spawn_level': 8,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 58,
        'common_drop': 'herb_small',
        'rare_drop': None,
        'money_range': (12, 38),
        'basic_attack': 'slashes with moon-silvered claws',
        'strong_attack': 'moonshade rake',
        'player_abilities': [],
        'base_str': 5, 'base_dex': 6, 'base_con': 3, 'base_int': 1,
        'base_hp': 42, 'base_ap': 3,
        'str_per_level': 2, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 0,
        'resistances': ['dark'],
        'immunities': [],
        'weaknesses': ['light'],
    },
    {
        'id': 'bark_phantom',
        'name': 'Bark Phantom',
        'hostile_type': 'undead',
        'min_spawn_level': 9,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 82,
        'common_drop': 'remedy_small',
        'rare_drop': None,
        'money_range': (15, 50),
        'basic_attack': 'phases through bark to strike from unexpected angles',
        'strong_attack': 'bark phase',
        'player_abilities': [],
        'base_str': 3, 'base_dex': 7, 'base_con': 4, 'base_int': 3,
        'base_hp': 52, 'base_ap': 3,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 1,
        'resistances': ['dark'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'thornwood_stalker',
        'name': 'Thornwood Stalker',
        'hostile_type': 'beast',
        'min_spawn_level': 10,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 108,
        'common_drop': 'stimulant_small',
        'rare_drop': 'remedy_med',
        'money_range': (20, 65),
        'basic_attack': 'charges with thorn-covered limbs',
        'strong_attack': 'thornwood crash',
        'player_abilities': [],
        'base_str': 5, 'base_dex': 3, 'base_con': 9, 'base_int': 1,
        'base_hp': 82, 'base_ap': 3,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 3, 'int_per_level': 0,
        'resistances': ['earth', 'physical'],
        'immunities': ['slow'],
        'weaknesses': ['fire'],
    },
    {
        'id': 'cask_revenant',
        'name': 'Cask Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 10,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 145,
        'common_drop': 'herb_med',
        'rare_drop': 'remedy_med',
        'money_range': (28, 88),
        'basic_attack': 'channels moonfire into a searing strike',
        'strong_attack': 'moonfire surge',
        'player_abilities': [],
        'base_str': 6, 'base_dex': 8, 'base_con': 4, 'base_int': 7,
        'base_hp': 68, 'base_ap': 4,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 2,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep'],
        'weaknesses': ['light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'lunarcask_shade_boss',
    'name': 'Lunarcask Shade',
    'hostiles': ['lunarcask_shade_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'lunarcask_shade_1',
        'name': 'Lunarcask Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 11,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 2400,
        'common_drop': 'remedy_small',
        'rare_drop': 'remedy_med',
        'money_range': (65, 190),
        'basic_attack': 'drowns the hollow in hungry moonlight',
        'strong_attack': 'cask devour',
        'player_abilities': [],
        'base_str': 7, 'base_dex': 10, 'base_con': 7, 'base_int': 14,
        'base_hp': 2800, 'base_ap': 80,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 1, 'int_per_level': 2,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'fire'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'forest_mid_city_type_d_lunarcask_shade_dungeon',
    'display_name': 'The Lunarcask Hollow',
    'seed': abs(hash('forest_mid_city_type_d_lunarcask_shade_dungeon')),
    'floor_count': 1,
    'rooms_per_floor': 3,
    'room_size_min_max': (55, 95),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.06,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (2, 4),
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color': OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile': BORDER_TILE,
    'border_color': BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'visible_distance': 6,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}