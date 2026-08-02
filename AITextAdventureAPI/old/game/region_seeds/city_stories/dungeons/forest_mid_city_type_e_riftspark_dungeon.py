"""Forest Mid City — Riftspark Dungeon Seed (Type E)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# forest_mid_city_type_e_riftspark_dungeon.py
# City: Cindercanopy Exchange (forest_mid, Ch.2)
# Chain: Type E — Artifact (Mycelia Memory Spore)
# Player level at encounter: ~10
# Pattern: A — boss guards artifact in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#4a6830'
IMPASSABLE_COLOR = '#1e2e10'
BORDER_TILE      = '·'
BORDER_COLOR     = '#3a5020'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'riftspark', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',        'location': 'treasure_room'},
    {'id': 'ointment',    'location': 'treasure_room'},
    {'id': 'stimulant_small', 'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['root_creeper', 'spore_lurker', 'mycelium_crawler', 'rift_tendril'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'root_creeper',
        'name': 'Root Creeper',
        'hostile_type': 'beast',
        'min_spawn_level': 8,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 58,
        'common_drop': 'herb_minor',
        'rare_drop': None,
        'money_range': (12, 38),
        'basic_attack': 'lashes with a whip-like root',
        'strong_attack': 'root bind',
        'player_abilities': [],
        'base_str': 5, 'base_dex': 4, 'base_con': 4, 'base_int': 1,
        'base_hp': 45, 'base_ap': 3,
        'str_per_level': 2, 'dex_per_level': 1, 'con_per_level': 1, 'int_per_level': 0,
        'resistances': ['earth'],
        'immunities': [],
        'weaknesses': ['fire'],
    },
    {
        'id': 'spore_lurker',
        'name': 'Spore Lurker',
        'hostile_type': 'creature',
        'min_spawn_level': 9,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 82,
        'common_drop': 'ointment',
        'rare_drop': 'herb_med',
        'money_range': (15, 50),
        'basic_attack': 'releases a toxic spore burst',
        'strong_attack': 'spore cloud',
        'player_abilities': [],
        'base_str': 2, 'base_dex': 3, 'base_con': 6, 'base_int': 3,
        'base_hp': 55, 'base_ap': 3,
        'str_per_level': 0, 'dex_per_level': 1, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['earth'],
        'immunities': ['poison'],
        'weaknesses': ['fire'],
    },
    {
        'id': 'mycelium_crawler',
        'name': 'Mycelium Crawler',
        'hostile_type': 'beast',
        'min_spawn_level': 10,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 108,
        'common_drop': 'stimulant_small',
        'rare_drop': 'petrify_salve',
        'money_range': (20, 65),
        'basic_attack': 'crashes forward with dense fungal mass',
        'strong_attack': 'mycelia press',
        'player_abilities': [],
        'base_str': 4, 'base_dex': 2, 'base_con': 9, 'base_int': 1,
        'base_hp': 80, 'base_ap': 3,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 3, 'int_per_level': 0,
        'resistances': ['earth', 'poison'],
        'immunities': ['slow'],
        'weaknesses': ['fire'],
    },
    {
        'id': 'rift_tendril',
        'name': 'Rift Tendril',
        'hostile_type': 'elemental',
        'min_spawn_level': 10,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 145,
        'common_drop': 'herb_med',
        'rare_drop': 'petrify_salve',
        'money_range': (28, 88),
        'basic_attack': 'lashes with a crackling rift-infused tendril',
        'strong_attack': 'rift discharge',
        'player_abilities': [],
        'base_str': 5, 'base_dex': 8, 'base_con': 4, 'base_int': 6,
        'base_hp': 70, 'base_ap': 4,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 2,
        'resistances': ['dark'],
        'immunities': ['sleep'],
        'weaknesses': ['light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'riftspark_boss',
    'name': 'Riftspark',
    'hostiles': ['riftspark_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'riftspark_1',
        'name': 'Riftspark',
        'hostile_type': 'elemental',
        'min_spawn_level': 11,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 2200,
        'common_drop': 'ointment',
        'rare_drop': 'petrify_salve',
        'money_range': (65, 190),
        'basic_attack': 'erupts with crackling rift-energy across the hollow floor',
        'strong_attack': 'riftspark detonation',
        'player_abilities': [],
        'base_str': 8, 'base_dex': 12, 'base_con': 8, 'base_int': 14,
        'base_hp': 2800, 'base_ap': 80,
        'str_per_level': 1, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 2,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'fire'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'forest_mid_city_type_e_riftspark_dungeon',
    'display_name': 'The Mycelium Hollow',
    'seed': abs(hash('forest_mid_city_type_e_riftspark_dungeon')),
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
    'visible_distance': 7,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}