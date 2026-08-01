"""Snow Mid City — Blueforge Depths Dungeon Seed (Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# snow_mid_city_blueforge_depths.py
# City: Hailward Hold (snow_mid, Ch.15)
# Chain: Type D — Mythic Armor (Blueforge Warplate)
# Player level at encounter: ~75
# Pattern: A — boss guards blue-forge crystal in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#304868'
IMPASSABLE_COLOR = '#0e1822'
BORDER_TILE      = '·'
BORDER_COLOR     = '#203858'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'blueforge_spirit', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['blueforge_remnant', 'rune_shade', 'depths_sentinel', 'void_forge'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'blueforge_remnant',
        'name': 'Blueforge Remnant',
        'hostile_type': 'construct',
        'min_spawn_level': 73,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 534,
        'common_drop': 'herb_large',
        'rare_drop': None,
        'money_range': (144, 460),
        'basic_attack': 'drives a blue-flame-heated fist through the target',
        'strong_attack': 'blueforge slam',
        'player_abilities': [],
        'base_str': 54, 'base_dex': 44, 'base_con': 40, 'base_int': 16,
        'base_hp': 1015, 'base_ap': 15,
        'str_per_level': 5, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['fire', 'ice', 'physical'],
        'immunities': ['burn', 'stun'],
        'weaknesses': ['electric', 'light'],
    },
    {
        'id': 'rune_shade',
        'name': 'Rune Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 74,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 652,
        'common_drop': 'remedy_large',
        'rare_drop': 'herb_large',
        'money_range': (174, 556),
        'basic_attack': 'channels an ancient rune-frequency into a draining pulse',
        'strong_attack': 'rune drain',
        'player_abilities': [],
        'base_str': 30, 'base_dex': 56, 'base_con': 32, 'base_int': 40,
        'base_hp': 1030, 'base_ap': 15,
        'str_per_level': 1, 'dex_per_level': 5, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'ice'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'depths_sentinel',
        'name': 'Depths Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 75,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 828,
        'common_drop': 'stimulant_large',
        'rare_drop': 'remedy_large',
        'money_range': (218, 696),
        'basic_attack': 'blocks the depths passage and strikes with blue-iron force',
        'strong_attack': 'depths press',
        'player_abilities': [],
        'base_str': 38, 'base_dex': 22, 'base_con': 66, 'base_int': 14,
        'base_hp': 1385, 'base_ap': 15,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 6, 'int_per_level': 1,
        'resistances': ['ice', 'physical', 'fire'],
        'immunities': ['stun', 'slow', 'burn'],
        'weaknesses': ['electric'],
    },
    {
        'id': 'void_forge',
        'name': 'Void Forge',
        'hostile_type': 'elemental',
        'min_spawn_level': 75,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 1114,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (260, 832),
        'basic_attack': 'channels void-corruption through the blue-forge flame into a strike',
        'strong_attack': 'void forge burst',
        'player_abilities': [],
        'base_str': 48, 'base_dex': 50, 'base_con': 42, 'base_int': 48,
        'base_hp': 1285, 'base_ap': 17,
        'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 3, 'int_per_level': 5,
        'resistances': ['dark', 'fire', 'ice'],
        'immunities': ['sleep', 'confuse', 'burn'],
        'weaknesses': ['electric', 'light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'blueforge_spirit_boss',
    'name': 'The Blueforge Spirit',
    'hostiles': ['blueforge_spirit_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'blueforge_spirit_1',
        'name': 'The Blueforge Spirit',
        'hostile_type': 'elemental',
        'min_spawn_level': 76,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 36000,
        'common_drop': 'remedy_large',
        'rare_drop': 'remedy_large',
        'money_range': (875, 2625),
        'basic_attack': 'floods the depths with the rune-frequency it has fed on since the first forge burned here',
        'strong_attack': 'blueforge dominion',
        'player_abilities': [],
        'base_str': 60, 'base_dex': 58, 'base_con': 56, 'base_int': 64,
        'base_hp': 43000, 'base_ap': 610,
        'str_per_level': 6, 'dex_per_level': 5, 'con_per_level': 5, 'int_per_level': 7,
        'resistances': ['dark', 'fire', 'ice', 'physical'],
        'immunities': ['sleep', 'confuse', 'fear', 'stun', 'slow', 'burn'],
        'weaknesses': ['electric', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'snow_mid_city_blueforge_depths',
    'display_name': 'The Blueforge Depths',
    'seed': abs(hash('snow_mid_city_blueforge_depths')),
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