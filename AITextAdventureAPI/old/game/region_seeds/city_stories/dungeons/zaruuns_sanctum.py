"""Desert Mid City — Zaruun's Sanctum Dungeon Seed (Type B)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# zaruuns_sanctum.py
# City: The Vaults (desert_mid, Ch.8)
# Chain: Type B — Regional Boss / Void Gauntlet (Sable)
# Player level at encounter: ~40
# Pattern: B — player teleported to final_chamber; boss = zaruun_b1
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = '#6a5030'
IMPASSABLE_COLOR = '#221808'
BORDER_TILE      = '·'
BORDER_COLOR     = '#4a3820'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'zaruun', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['void_sand', 'dune_wraith', 'desert_revenant', 'void_drifter'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'void_sand',
        'name': 'Void Sand',
        'hostile_type': 'elemental',
        'min_spawn_level': 38,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 252,
        'common_drop': 'herb_large',
        'rare_drop': None,
        'money_range': (66, 210),
        'basic_attack': 'scours with void-infused sand',
        'strong_attack': 'void scour',
        'player_abilities': [],
        'base_str': 24, 'base_dex': 22, 'base_con': 18, 'base_int': 16,
        'base_hp': 475, 'base_ap': 10,
        'str_per_level': 3, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 2,
        'resistances': ['earth', 'dark'],
        'immunities': ['slow'],
        'weaknesses': ['water', 'light'],
    },
    {
        'id': 'dune_wraith',
        'name': 'Dune Wraith',
        'hostile_type': 'undead',
        'min_spawn_level': 39,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 308,
        'common_drop': 'remedy_med',
        'rare_drop': 'herb_large',
        'money_range': (78, 248),
        'basic_attack': 'rises from the dune to strike from below',
        'strong_attack': 'dune surge',
        'player_abilities': [],
        'base_str': 16, 'base_dex': 26, 'base_con': 16, 'base_int': 16,
        'base_hp': 488, 'base_ap': 10,
        'str_per_level': 1, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 2,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'water'],
    },
    {
        'id': 'desert_revenant',
        'name': 'Desert Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 40,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 392,
        'common_drop': 'stimulant_large',
        'rare_drop': 'remedy_large',
        'money_range': (96, 308),
        'basic_attack': 'charges with the hardened weight of the desert',
        'strong_attack': 'desert press',
        'player_abilities': [],
        'base_str': 20, 'base_dex': 10, 'base_con': 34, 'base_int': 10,
        'base_hp': 675, 'base_ap': 10,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 5, 'int_per_level': 1,
        'resistances': ['earth', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['water', 'electric'],
    },
    {
        'id': 'void_drifter',
        'name': 'Void Drifter',
        'hostile_type': 'elemental',
        'min_spawn_level': 40,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 532,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (128, 412),
        'basic_attack': 'phases between void and sand to strike at the weakest point',
        'strong_attack': 'void phase',
        'player_abilities': [],
        'base_str': 26, 'base_dex': 28, 'base_con': 20, 'base_int': 24,
        'base_hp': 610, 'base_ap': 11,
        'str_per_level': 3, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'water'],
    },
]

BOSS_MOB: Dict = {
    'id': 'zaruun_boss',
    'name': 'Zaruun the Void-Warlock',
    'hostiles': ['zaruun_b1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'zaruun_b1',
        'name': 'Zaruun the Void-Warlock',
        'hostile_type': 'humanoid',
        'min_spawn_level': 42,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 18000,
        'common_drop': 'remedy_large',
        'rare_drop': 'remedy_large',
        'money_range': (440, 1320),
        'basic_attack': "channels the desert's void into a directed beam",
        'strong_attack': 'void emptying',
        'player_abilities': [],
        'base_str': 35, 'base_dex': 38, 'base_con': 32, 'base_int': 42,
        'base_hp': 22000, 'base_ap': 380,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 4, 'int_per_level': 5,
        'resistances': ['dark', 'earth', 'physical'],
        'immunities': ['sleep', 'confuse', 'fear', 'stun'],
        'weaknesses': ['light', 'water'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'zaruuns_sanctum',
    'display_name': "Zaruun's Sanctum",
    'seed': abs(hash('zaruuns_sanctum')),
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
    'visible_distance': 8,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}