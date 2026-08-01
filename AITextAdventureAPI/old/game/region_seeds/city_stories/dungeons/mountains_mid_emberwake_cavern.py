"""Mountains Mid City — Emberwake Cavern Dungeon Seed (Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# mountains_mid_emberwake_cavern.py
# City: Gallows Rift (mountains_mid, Ch.17)
# Chain: Type D — Mythic Armor (Shatterpeak Warplate)
# Player level at encounter: ~85
# Pattern: A — boss guards forge-pressure crystal in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = '#684838'
IMPASSABLE_COLOR = '#221810'
BORDER_TILE      = '·'
BORDER_COLOR     = '#503828'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'emberwake_spirit', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'remedy_large',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['ember_remnant', 'cavern_shade', 'pressure_sentinel', 'void_ember'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'ember_remnant',
        'name': 'Ember Remnant',
        'hostile_type': 'construct',
        'min_spawn_level': 83,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 610,
        'common_drop': 'herb_large',
        'rare_drop': None,
        'money_range': (165, 528),
        'basic_attack': 'drives an ember-heated fist through plating',
        'strong_attack': 'ember slam',
        'player_abilities': [],
        'base_str': 62, 'base_dex': 48, 'base_con': 44, 'base_int': 18,
        'base_hp': 1155, 'base_ap': 17,
        'str_per_level': 6, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['fire', 'physical'],
        'immunities': ['burn', 'stun'],
        'weaknesses': ['water', 'electric'],
    },
    {
        'id': 'cavern_shade',
        'name': 'Cavern Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 84,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 744,
        'common_drop': 'remedy_large',
        'rare_drop': 'herb_large',
        'money_range': (198, 634),
        'basic_attack': 'channels the heat of the cavern into a draining pulse',
        'strong_attack': 'cavern drain',
        'player_abilities': [],
        'base_str': 34, 'base_dex': 62, 'base_con': 36, 'base_int': 42,
        'base_hp': 1170, 'base_ap': 17,
        'str_per_level': 1, 'dex_per_level': 6, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'fire'],
        'immunities': ['sleep', 'confuse', 'burn'],
        'weaknesses': ['water', 'light'],
    },
    {
        'id': 'pressure_sentinel',
        'name': 'Pressure Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 85,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 944,
        'common_drop': 'stimulant_large',
        'rare_drop': 'remedy_large',
        'money_range': (248, 792),
        'basic_attack': 'holds the cavern passage and strikes with forge-pressure force',
        'strong_attack': 'pressure crash',
        'player_abilities': [],
        'base_str': 42, 'base_dex': 24, 'base_con': 76, 'base_int': 16,
        'base_hp': 1575, 'base_ap': 17,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 7, 'int_per_level': 1,
        'resistances': ['fire', 'physical', 'earth'],
        'immunities': ['stun', 'slow', 'burn'],
        'weaknesses': ['water', 'electric'],
    },
    {
        'id': 'void_ember',
        'name': 'Void Ember',
        'hostile_type': 'elemental',
        'min_spawn_level': 85,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 1272,
        'common_drop': 'herb_large',
        'rare_drop': 'remedy_large',
        'money_range': (298, 952),
        'basic_attack': 'channels void-corruption through emberwake heat into a strike',
        'strong_attack': 'void ember surge',
        'player_abilities': [],
        'base_str': 54, 'base_dex': 56, 'base_con': 46, 'base_int': 54,
        'base_hp': 1475, 'base_ap': 19,
        'str_per_level': 5, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 5,
        'resistances': ['dark', 'fire'],
        'immunities': ['sleep', 'confuse', 'burn'],
        'weaknesses': ['water', 'light'],
    },
]

BOSS_MOB: Dict = {
    'id': 'emberwake_spirit_boss',
    'name': 'The Emberwake Spirit',
    'hostiles': ['emberwake_spirit_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'emberwake_spirit_1',
        'name': 'The Emberwake Spirit',
        'hostile_type': 'elemental',
        'min_spawn_level': 86,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 43000,
        'common_drop': 'remedy_large',
        'rare_drop': 'remedy_large',
        'money_range': (1040, 3120),
        'basic_attack': 'floods the cavern with the forge-pressure it has held since the first furnace burned here',
        'strong_attack': 'emberwake dominion',
        'player_abilities': [],
        'base_str': 68, 'base_dex': 62, 'base_con': 64, 'base_int': 64,
        'base_hp': 53000, 'base_ap': 725,
        'str_per_level': 7, 'dex_per_level': 6, 'con_per_level': 6, 'int_per_level': 6,
        'resistances': ['fire', 'earth', 'physical', 'dark'],
        'immunities': ['sleep', 'confuse', 'fear', 'stun', 'slow', 'burn'],
        'weaknesses': ['water', 'electric'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'mountains_mid_emberwake_cavern',
    'display_name': 'The Emberwake Cavern',
    'seed': abs(hash('mountains_mid_emberwake_cavern')),
    'floor_count': 1,
    'rooms_per_floor': 4,
    'room_size_min_max': (60, 110),
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