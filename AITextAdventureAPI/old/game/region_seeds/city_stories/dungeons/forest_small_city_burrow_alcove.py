"""Forest Small City — Burrow Alcove Dungeon Seed (Type E)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# forest_small_city_burrow_alcove.py
# City: Thornshade Hamlet (forest_small, Ch.16)
# Chain: Type E — Artifact (Thornshade Root Graft)
# Player level at encounter: ~80
# Pattern: A — boss guards root graft in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.12
OPEN_AREA_COLOR  = '#384828'
IMPASSABLE_COLOR = '#101808'
BORDER_TILE      = '·'
BORDER_COLOR     = '#283818'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'burrow_whisper', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['burrow_creep', 'root_shade', 'alcove_sentinel', 'void_burrow'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'burrow_creep',
        'name': 'Burrow Creep',
        'hostile_type': 'beast',
        'min_spawn_level': 78,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 572,
        'common_drop': 'herb_large',
        'rare_drop': None,
        'money_range': (154, 492),
        'basic_attack': 'lunges from a burrow entrance with hardened root-claws',
        'strong_attack': 'burrow lunge',
        'player_abilities': [],
        'base_str': 56, 'base_dex': 48, 'base_con': 40, 'base_int': 14,
        'base_hp': 1100, 'base_ap': 16,
        'str_per_level': 5, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['earth', 'physical'],
        'immunities': ['slow'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'root_shade',
        'name': 'Root Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 79,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 698,
        'common_drop': 'remedy_large',
        'rare_drop': 'herb_large',
        'money_range': (186, 594),
        'basic_attack': 'lashes with a tendril of memory-laden root',
        'strong_attack': 'memory drain',
        'player_abilities': [],
        'base_str': 34, 'base_dex': 58, 'base_con': 36, 'base_int': 38,
        'base_hp': 1115, 'base_ap': 16,
        'str_per_level': 1, 'dex_per_level': 5, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'alcove_sentinel',
        'name': 'Alcove Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 80,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 888,
        'common_drop': 'stimulant_large',
        'rare_drop': 'remedy_large',
        'money_range': (232, 742),
        'basic_attack': 'stands firm and drives root-reinforced fists into the target',
        'strong_attack': 'alcove press',
        'player_abilities': [],
        'base_str': 40, 'base_dex': 22, 'base_con': 68, 'base_int': 14,
        'base_hp': 1480, 'base_ap': 16,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 6, 'int_per_level': 1,
        'resistances': ['earth', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['fire', 'electric'],
    },
    {
        'id': 'void_burrow',
        'name': 'Void Burrow',
        'hostile_type': 'elemental',
        'min_spawn_level': 80,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 1196,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (278, 888),
        'basic_attack': 'opens a void-infused burrow beneath the target and strikes upward',
        'strong_attack': 'void burrow collapse',
        'player_abilities': [],
        'base_str': 52, 'base_dex': 54, 'base_con': 42, 'base_int': 48,
        'base_hp': 1380, 'base_ap': 18,
        'str_per_level': 5, 'dex_per_level': 5, 'con_per_level': 3, 'int_per_level': 5,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['fire', 'light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'burrow_whisper_boss',
    'name': 'The Burrow Whisper',
    'hostiles': ['burrow_whisper_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'burrow_whisper_1',
        'name': 'The Burrow Whisper',
        'hostile_type': 'elemental',
        'min_spawn_level': 81,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 38000,
        'common_drop': 'remedy_large',
        'rare_drop': 'remedy_large',
        'money_range': (920, 2760),
        'basic_attack': 'fills every burrow in the alcove with the forest\'s demand to keep what it holds',
        'strong_attack': 'burrow whisper collapse',
        'player_abilities': [],
        'base_str': 64, 'base_dex': 62, 'base_con': 58, 'base_int': 66,
        'base_hp': 46000, 'base_ap': 640,
        'str_per_level': 6, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 6,
        'resistances': ['dark', 'earth', 'physical'],
        'immunities': ['sleep', 'confuse', 'fear', 'stun', 'slow'],
        'weaknesses': ['fire', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'forest_small_city_burrow_alcove',
    'display_name': 'The Echofern Burrows',
    'seed': abs(hash('forest_small_city_burrow_alcove')),
    'floor_count': 1,
    'rooms_per_floor': 3,
    'room_size_min_max': (55, 105),
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