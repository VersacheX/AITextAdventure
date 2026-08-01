"""Snow Small City — Stormhollow Dungeon Seed (Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# stormhollow_voice_1.py
# City: Bleakwatch Outpost (snow_small, Ch.6)
# Chain: Type D — Mythic Armor (Bleakwatch Warden Plate)
# Player level at encounter: ~30
# Pattern: A — boss guards buried warden plate in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#607080'
IMPASSABLE_COLOR = '#1c2228'
BORDER_TILE      = '·'
BORDER_COLOR     = '#405060'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'stormhollow_voice', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',    'location': 'treasure_room'},
    {'id': 'stimulant_med', 'location': 'treasure_room'},
    {'id': 'remedy_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['frost_shade', 'blizzard_crawler', 'hollow_sentinel', 'battle_revenant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'frost_shade',
        'name': 'Frost Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 28,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 196,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (36, 112),
        'basic_attack': 'slashes with frost-hardened claws',
        'strong_attack': 'frost rake',
        'player_abilities': [],
        'base_str': 18, 'base_dex': 16, 'base_con': 14, 'base_int': 5,
        'base_hp': 320, 'base_ap': 8,
        'str_per_level': 3, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 0,
        'resistances': ['ice', 'dark'],
        'immunities': ['slow'],
        'weaknesses': ['fire', 'light'],
    },
    {
        'id': 'blizzard_crawler',
        'name': 'Blizzard Crawler',
        'hostile_type': 'beast',
        'min_spawn_level': 29,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 248,
        'common_drop': 'remedy_med',
        'rare_drop': 'herb_large',
        'money_range': (44, 140),
        'basic_attack': 'charges through the hollow trailing a blizzard',
        'strong_attack': 'blizzard surge',
        'player_abilities': [],
        'base_str': 14, 'base_dex': 18, 'base_con': 13, 'base_int': 4,
        'base_hp': 340, 'base_ap': 8,
        'str_per_level': 1, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 0,
        'resistances': ['ice'],
        'immunities': ['confuse'],
        'weaknesses': ['fire', 'electric'],
    },
    {
        'id': 'hollow_sentinel',
        'name': 'Hollow Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 30,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 318,
        'common_drop': 'stimulant_large',
        'rare_drop': 'remedy_large',
        'money_range': (56, 175),
        'basic_attack': 'stands fast and strikes with a heavy frost-plated gauntlet',
        'strong_attack': 'frost guard slam',
        'player_abilities': [],
        'base_str': 16, 'base_dex': 6, 'base_con': 26, 'base_int': 4,
        'base_hp': 480, 'base_ap': 8,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 5, 'int_per_level': 0,
        'resistances': ['ice', 'physical'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['fire', 'electric'],
    },
    {
        'id': 'battle_revenant',
        'name': 'Battle Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 30,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 432,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (76, 238),
        'basic_attack': 'embodies the battle-wind of every siege that buried this outpost',
        'strong_attack': 'siege memory',
        'player_abilities': [],
        'base_str': 20, 'base_dex': 20, 'base_con': 16, 'base_int': 12,
        'base_hp': 430, 'base_ap': 9,
        'str_per_level': 3, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['ice', 'dark'],
        'immunities': ['sleep', 'fear'],
        'weaknesses': ['light', 'fire'],
    },
]

BOSS_MOB: Dict = {
    'id': 'stormhollow_boss',
    'name': 'The Stormhollow Voice',
    'hostiles': ['stormhollow_voice_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'stormhollow_voice_1',
        'name': 'The Stormhollow Voice',
        'hostile_type': 'elemental',
        'min_spawn_level': 31,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 6500,
        'common_drop': 'remedy_large',
        'rare_drop': 'remedy_large',
        'money_range': (168, 490),
        'basic_attack': 'unleashes the accumulated battle-wind of every siege through the hollow',
        'strong_attack': 'siege storm',
        'player_abilities': [],
        'base_str': 24, 'base_dex': 26, 'base_con': 22, 'base_int': 20,
        'base_hp': 8500, 'base_ap': 158,
        'str_per_level': 3, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 2,
        'resistances': ['ice', 'dark', 'physical'],
        'immunities': ['sleep', 'slow', 'confuse', 'stun'],
        'weaknesses': ['fire', 'light'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'stormhollow_voice_1',
    'display_name': 'The Stormhollow',
    'seed': abs(hash('stormhollow_voice_1')),
    'floor_count': 1,
    'rooms_per_floor': 3,
    'room_size_min_max': (55, 100),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.07,
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