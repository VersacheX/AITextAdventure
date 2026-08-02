"""Forest Small City — Burrow Alcove 2 Dungeon Seed (Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# forest_small_city_burrow_alcove_2.py
# City: Thornshade Hamlet (forest_small, Ch.16)
# Chain: Type D — Mythic Weapon (Echofern Blade)
# Player level at encounter: ~80
# Pattern: A — boss guards memory-crystal in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.12
OPEN_AREA_COLOR  = '#304020'
IMPASSABLE_COLOR = '#0e1608'
BORDER_TILE      = '·'
BORDER_COLOR     = '#223012'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'burrow_whisper_2', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['memory_creep', 'echofern_shade', 'deep_burrow_sentinel', 'void_memory'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'memory_creep',
        'name': 'Memory Creep',
        'hostile_type': 'beast',
        'min_spawn_level': 78,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 572,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (154, 492),
        'basic_attack': 'strikes with limbs heavy with absorbed forest memory',
        'strong_attack': 'memory slam',
        'player_abilities': [],
        'base_str': 54, 'base_dex': 48, 'base_con': 42, 'base_int': 18,
        'base_hp': 1095, 'base_ap': 16,
        'str_per_level': 5, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['earth', 'dark'],
        'immunities': ['slow'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'echofern_shade',
        'name': 'Echofern Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 79,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 698,
        'common_drop': 'stimulant_med',
        'rare_drop': 'herb_med',
        'money_range': (186, 594),
        'basic_attack': 'releases a pulse of drained forest memory as a concussive wave',
        'strong_attack': 'echofern drain',
        'player_abilities': [],
        'base_str': 32, 'base_dex': 58, 'base_con': 36, 'base_int': 40,
        'base_hp': 1110, 'base_ap': 16,
        'str_per_level': 1, 'dex_per_level': 5, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'deep_burrow_sentinel',
        'name': 'Deep Burrow Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 80,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 888,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (232, 742),
        'basic_attack': 'blocks the burrow passage and drives memory-dense fists forward',
        'strong_attack': 'deep burrow press',
        'player_abilities': [],
        'base_str': 38, 'base_dex': 22, 'base_con': 70, 'base_int': 14,
        'base_hp': 1490, 'base_ap': 16,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 6, 'int_per_level': 1,
        'resistances': ['earth', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['fire', 'electric'],
    },
    {
        'id': 'void_memory',
        'name': 'Void Memory',
        'hostile_type': 'elemental',
        'min_spawn_level': 80,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 1196,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (278, 888),
        'basic_attack': 'weaponizes drained forest memories into a void-charged strike',
        'strong_attack': 'void recollection',
        'player_abilities': [],
        'base_str': 50, 'base_dex': 54, 'base_con': 42, 'base_int': 50,
        'base_hp': 1375, 'base_ap': 18,
        'str_per_level': 5, 'dex_per_level': 5, 'con_per_level': 3, 'int_per_level': 5,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['fire', 'light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'burrow_whisper_2_boss',
    'name': 'The Burrow Whisper',
    'hostiles': ['burrow_whisper_2'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'burrow_whisper_2',
        'name': 'The Burrow Whisper',
        'hostile_type': 'elemental',
        'min_spawn_level': 81,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 39000,
        'common_drop': 'stimulant_med',
        'rare_drop': 'stimulant_med',
        'money_range': (940, 2820),
        'basic_attack': 'floods the deep burrow with every memory it has drained from the root network',
        'strong_attack': 'memory network collapse',
        'player_abilities': [],
        'base_str': 64, 'base_dex': 64, 'base_con': 58, 'base_int': 68,
        'base_hp': 47000, 'base_ap': 645,
        'str_per_level': 6, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 7,
        'resistances': ['dark', 'earth', 'physical'],
        'immunities': ['sleep', 'confuse', 'fear', 'stun', 'slow'],
        'weaknesses': ['fire', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'forest_small_city_burrow_alcove_2',
    'display_name': 'The Deep Echofern Burrow',
    'seed': abs(hash('forest_small_city_burrow_alcove_2')),
    'floor_count': 1,
    'rooms_per_floor': 4,
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