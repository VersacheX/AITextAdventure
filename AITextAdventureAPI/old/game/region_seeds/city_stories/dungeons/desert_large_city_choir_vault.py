"""Desert Large City — Choir Vault Dungeon Seed (Type E)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# desert_large_city_choir_vault.py
# City: Desert Metropolis (desert_large, Ch.1)
# Chain: Type E — Artifact (Dune Cipher Stone)
# Player level at encounter: ~5
# Pattern: A — boss guards artifact in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.12
OPEN_AREA_COLOR  = '#8a7858'
IMPASSABLE_COLOR = '#302818'
BORDER_TILE      = '·'
BORDER_COLOR     = '#5a4830'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'choir_echo', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_small',      'location': 'treasure_room'},
    {'id': 'remedy_small',    'location': 'treasure_room'},
    {'id': 'stimulant_small', 'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['sand_wanderer', 'buried_shade', 'dune_construct', 'echo_revenant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'sand_wanderer',
        'name': 'Sand Wanderer',
        'hostile_type': 'humanoid',
        'min_spawn_level': 3,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 28,
        'common_drop': 'herb_small',
        'rare_drop': None,
        'money_range': (5, 18),
        'basic_attack': 'swings with a sand-worn blade',
        'strong_attack': 'dust strike',
        'player_abilities': [],
        'base_str': 3, 'base_dex': 3, 'base_con': 2, 'base_int': 1,
        'base_hp': 18, 'base_ap': 2,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 1, 'int_per_level': 0,
        'resistances': ['earth'],
        'immunities': [],
        'weaknesses': ['water'],
    },
    {
        'id': 'buried_shade',
        'name': 'Buried Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 4,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 42,
        'common_drop': 'remedy_small',
        'rare_drop': None,
        'money_range': (8, 24),
        'basic_attack': 'claws from below with desiccated hands',
        'strong_attack': 'burial drag',
        'player_abilities': [],
        'base_str': 2, 'base_dex': 4, 'base_con': 3, 'base_int': 2,
        'base_hp': 24, 'base_ap': 2,
        'str_per_level': 0, 'dex_per_level': 1, 'con_per_level': 1, 'int_per_level': 1,
        'resistances': ['dark'],
        'immunities': ['sleep'],
        'weaknesses': ['light'],
    },
    {
        'id': 'dune_construct',
        'name': 'Dune Construct',
        'hostile_type': 'construct',
        'min_spawn_level': 5,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 62,
        'common_drop': 'stimulant_small',
        'rare_drop': 'herb_med',
        'money_range': (12, 35),
        'basic_attack': 'slams with a compressed-sand fist',
        'strong_attack': 'dune press',
        'player_abilities': [],
        'base_str': 4, 'base_dex': 2, 'base_con': 7, 'base_int': 1,
        'base_hp': 38, 'base_ap': 3,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 3, 'int_per_level': 0,
        'resistances': ['earth', 'physical'],
        'immunities': ['stun'],
        'weaknesses': ['water'],
    },
    {
        'id': 'echo_revenant',
        'name': 'Echo Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 5,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 82,
        'common_drop': 'remedy_small',
        'rare_drop': 'herb_med',
        'money_range': (18, 52),
        'basic_attack': 'strikes with a resonant frequency blast',
        'strong_attack': 'choir echo burst',
        'player_abilities': [],
        'base_str': 5, 'base_dex': 6, 'base_con': 4, 'base_int': 4,
        'base_hp': 48, 'base_ap': 3,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 1, 'int_per_level': 1,
        'resistances': ['dark'],
        'immunities': ['sleep'],
        'weaknesses': ['light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'choir_echo_boss',
    'name': 'The Choir Echo',
    'hostiles': ['choir_echo_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'choir_echo_1',
        'name': 'The Choir Echo',
        'hostile_type': 'elemental',
        'min_spawn_level': 6,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 320,
        'common_drop': 'remedy_small',
        'rare_drop': 'herb_med',
        'money_range': (40, 120),
        'basic_attack': 'releases a resonance wave that fills the vault',
        'strong_attack': 'choir silence',
        'player_abilities': [],
        'base_str': 6, 'base_dex': 8, 'base_con': 6, 'base_int': 10,
        'base_hp': 1400, 'base_ap': 60,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 1, 'int_per_level': 2,
        'resistances': ['dark'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'desert_large_city_choir_vault',
    'display_name': 'The Choir Vault',
    'seed': abs(hash('desert_large_city_choir_vault')),
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