"""Grassland Small City — Charmroot Den Dungeon Seed (Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# charmroot_den.py
# City: Wildhollow (grassland_small, Ch.12)
# Chain: Type D — Mythic Accessory (Folklore Hollow Talisman)
# Player level at encounter: ~60
# Pattern: A — boss guards crystallized grief in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#607040'
IMPASSABLE_COLOR = '#202410'
BORDER_TILE      = '·'
BORDER_COLOR     = '#485830'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'charmroot_voice', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['charm_drifter', 'grief_shade', 'hollow_stalker', 'folk_revenant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'charm_drifter',
        'name': 'Charm Drifter',
        'hostile_type': 'undead',
        'min_spawn_level': 58,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 420,
        'common_drop': 'herb_large',
        'rare_drop': None,
        'money_range': (115, 365),
        'basic_attack': 'strikes with the weight of an unfinished folk charm',
        'strong_attack': 'charm drain',
        'player_abilities': [],
        'base_str': 40, 'base_dex': 36, 'base_con': 30, 'base_int': 16,
        'base_hp': 810, 'base_ap': 14,
        'str_per_level': 4, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['earth', 'dark'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'grief_shade',
        'name': 'Grief Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 59,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 512,
        'common_drop': 'remedy_large',
        'rare_drop': 'herb_large',
        'money_range': (138, 440),
        'basic_attack': 'lashes with a tendril of unresolved grief',
        'strong_attack': 'grief bind',
        'player_abilities': [],
        'base_str': 24, 'base_dex': 42, 'base_con': 26, 'base_int': 28,
        'base_hp': 825, 'base_ap': 14,
        'str_per_level': 1, 'dex_per_level': 4, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark'],
        'immunities': ['confuse', 'sleep'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'hollow_stalker',
        'name': 'Hollow Stalker',
        'hostile_type': 'beast',
        'min_spawn_level': 60,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 650,
        'common_drop': 'stimulant_large',
        'rare_drop': 'remedy_large',
        'money_range': (172, 548),
        'basic_attack': 'crashes through the den with hollow-hardened bulk',
        'strong_attack': 'hollow crash',
        'player_abilities': [],
        'base_str': 30, 'base_dex': 18, 'base_con': 50, 'base_int': 12,
        'base_hp': 1080, 'base_ap': 14,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 5, 'int_per_level': 1,
        'resistances': ['earth', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['fire', 'electric'],
    },
    {
        'id': 'folk_revenant',
        'name': 'Folk Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 60,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 876,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (205, 655),
        'basic_attack': 'channels every unfinished story in the hollow into a strike',
        'strong_attack': 'unfinished tale',
        'player_abilities': [],
        'base_str': 38, 'base_dex': 40, 'base_con': 30, 'base_int': 36,
        'base_hp': 1010, 'base_ap': 15,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 3,
        'resistances': ['dark', 'earth'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'fire'],
    },
]

BOSS_MOB: Dict = {
    'id': 'charmroot_voice_boss',
    'name': 'The Charmroot Voice',
    'hostiles': ['charmroot_voice_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'charmroot_voice_1',
        'name': 'The Charmroot Voice',
        'hostile_type': 'elemental',
        'min_spawn_level': 61,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 15500,
        'common_drop': 'remedy_large',
        'rare_drop': 'remedy_large',
        'money_range': (380, 1140),
        'basic_attack': 'floods the den with every unresolved story the hollow has ever held',
        'strong_attack': "charmroot's ending",
        'player_abilities': [],
        'base_str': 48, 'base_dex': 50, 'base_con': 44, 'base_int': 50,
        'base_hp': 21000, 'base_ap': 295,
        'str_per_level': 5, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 5,
        'resistances': ['dark', 'earth', 'physical'],
        'immunities': ['sleep', 'confuse', 'slow', 'stun'],
        'weaknesses': ['light', 'fire'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'charmroot_den',
    'display_name': 'The Charmroot Den',
    'seed': abs(hash('charmroot_den')),
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