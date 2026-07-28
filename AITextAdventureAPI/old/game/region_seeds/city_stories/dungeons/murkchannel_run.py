from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# murkchannel_run.py
# City: Gnashwater Hollow (swamp_small, Ch.7)
# Chain: Type A — Slot 1 (meet murkchannel_echo inside)
# Player level at encounter: ~35
# Pattern: Exploration dungeon — no boss, random hostiles only.
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE = '░'
IMPASSABLE_TILE = '¤'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'murkchannel_echo', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_large',         'location': 'treasure_room'},
    {'id': 'stimulant_large',    'location': 'treasure_room'},
    {'id': 'remedy_med',         'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['murk_drifter', 'rot_tendril', 'sludge_crawler', 'channel_wraith'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'murk_drifter',
        'name': 'Murk Drifter',
        'hostile_type': 'humanoid',
        'min_spawn_level': 32,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 210,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (55, 140),
        'basic_attack': 'slams with a waterlogged club',
        'strong_attack': 'dredging slam',
        'player_abilities': ['heavy_strike', 'taunt'],
    },
    {
        'id': 'rot_tendril',
        'name': 'Rot Tendril',
        'hostile_type': 'beast',
        'min_spawn_level': 33,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 245,
        'common_drop': 'remedy_small',
        'rare_drop': 'remedy_med',
        'money_range': (60, 155),
        'basic_attack': 'lashes with a rotting tendril',
        'strong_attack': 'constricting wrap',
        'player_abilities': ['poison_strike', 'ensnare'],
    },
    {
        'id': 'sludge_crawler',
        'name': 'Sludge Crawler',
        'hostile_type': 'creature',
        'min_spawn_level': 34,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 295,
        'common_drop': 'stimulant_med',
        'rare_drop': 'armor_shard',
        'money_range': (80, 200),
        'basic_attack': 'crashes forward with its armored shell',
        'strong_attack': 'sludge crush',
        'player_abilities': ['fortify', 'ground_slam'],
    },
    {
        'id': 'channel_wraith',
        'name': 'Channel Wraith',
        'hostile_type': 'undead',
        'min_spawn_level': 35,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 370,
        'common_drop': 'tome_int',
        'rare_drop': 'rift_shard',
        'money_range': (110, 280),
        'basic_attack': 'phases through and drains life',
        'strong_attack': 'channel devour',
        'player_abilities': ['void_strike', 'life_drain'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'murkchannel_run',
    'display_name': "The Murkchannel Run",
    'seed': abs(hash('murkchannel_run')),
    'floor_count': 1,
    'rooms_per_floor': 4,
    'room_size_min_max': (55, 100),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.08,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (2, 5),
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'impassable_chance': 0.10,
    'visible_distance': 7,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': None,
    'boss_hostiles': [],
}