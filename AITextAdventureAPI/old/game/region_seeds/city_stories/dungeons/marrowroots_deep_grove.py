"""Forest Large City — Marrowroot's Deep Grove Dungeon Seed (Type B)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# marrowroots_deep_grove.py
# City: Verdant Exchange (forest_large, Ch.18)
# Chain: Type B — Regional Boss / Void Gauntlet (Thorn)
# Player level at encounter: ~90
# Pattern: B — player teleported to final_chamber; boss = marrowroot_b1
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.12
OPEN_AREA_COLOR  = '#284018'
IMPASSABLE_COLOR = '#0c1608'
BORDER_TILE      = '·'
BORDER_COLOR     = '#1e3010'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'marrowroot', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['reaching_root', 'grove_shade', 'bark_sentinel', 'void_growth'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'reaching_root',
        'name': 'Reaching Root',
        'hostile_type': 'elemental',
        'min_spawn_level': 88,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 648,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (176, 562),
        'basic_attack': 'drives a void-hardened root through the target from below',
        'strong_attack': 'root surge',
        'player_abilities': [],
        'base_str': 66, 'base_dex': 54, 'base_con': 48, 'base_int': 22,
        'base_hp': 1240, 'base_ap': 18,
        'str_per_level': 6, 'dex_per_level': 4, 'con_per_level': 4, 'int_per_level': 1,
        'resistances': ['earth', 'dark'],
        'immunities': ['slow', 'poison'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'grove_shade',
        'name': 'Grove Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 89,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 790,
        'common_drop': 'stimulant_med',
        'rare_drop': 'herb_med',
        'money_range': (210, 672),
        'basic_attack': 'channels the grove\'s intent into a draining strike',
        'strong_attack': 'grove drain',
        'player_abilities': [],
        'base_str': 38, 'base_dex': 66, 'base_con': 40, 'base_int': 46,
        'base_hp': 1255, 'base_ap': 18,
        'str_per_level': 1, 'dex_per_level': 6, 'con_per_level': 3, 'int_per_level': 5,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse', 'poison'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'bark_sentinel',
        'name': 'Bark Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 90,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 1002,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (264, 844),
        'basic_attack': 'holds the grove passage and drives bark-reinforced mass forward',
        'strong_attack': 'bark press',
        'player_abilities': [],
        'base_str': 46, 'base_dex': 26, 'base_con': 82, 'base_int': 16,
        'base_hp': 1680, 'base_ap': 18,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 7, 'int_per_level': 1,
        'resistances': ['earth', 'physical'],
        'immunities': ['stun', 'slow', 'poison'],
        'weaknesses': ['fire', 'electric'],
    },
    {
        'id': 'void_growth',
        'name': 'Void Growth',
        'hostile_type': 'elemental',
        'min_spawn_level': 90,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 1350,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (316, 1012),
        'basic_attack': 'channels void-corruption through the grove\'s root network into a strike',
        'strong_attack': 'void grove surge',
        'player_abilities': [],
        'base_str': 58, 'base_dex': 60, 'base_con': 50, 'base_int': 58,
        'base_hp': 1580, 'base_ap': 20,
        'str_per_level': 5, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 5,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse', 'poison'],
        'weaknesses': ['fire', 'light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'marrowroot_boss',
    'name': 'Elder Marrowroot',
    'hostiles': ['marrowroot_b1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'marrowroot_b1',
        'name': 'Elder Marrowroot',
        'hostile_type': 'elemental',
        'min_spawn_level': 92,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 48000,
        'common_drop': 'stimulant_med',
        'rare_drop': 'stimulant_med',
        'money_range': (1160, 3480),
        'basic_attack': 'drives the root network of the entire grove through the target in a single intention',
        'strong_attack': 'grove transformation',
        'player_abilities': [],
        'base_str': 74, 'base_dex': 66, 'base_con': 70, 'base_int': 70,
        'base_hp': 58000, 'base_ap': 780,
        'str_per_level': 7, 'dex_per_level': 6, 'con_per_level': 7, 'int_per_level': 7,
        'resistances': ['earth', 'dark', 'physical'],
        'immunities': ['sleep', 'confuse', 'fear', 'stun', 'slow', 'poison'],
        'weaknesses': ['fire', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'marrowroots_deep_grove',
    'display_name': "Marrowroot's Deep Grove",
    'seed': abs(hash('marrowroots_deep_grove')),
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