"""Mountains Large City — Gearghost Dungeon Seed (Type E)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# mountains_large_city_type_e_gearghost_dungeon.py
# City: Ironveil (mountains_large, Ch.4)
# Chain: Type E — Artifact (Forge Echo Core)
# Player level at encounter: ~20
# Pattern: A — boss guards Echo Core in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = '#606060'
IMPASSABLE_COLOR = '#202020'
BORDER_TILE      = '·'
BORDER_COLOR     = '#404040'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'gearghost', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_med', 'location': 'treasure_room'},
    {'id': 'petrify_salve',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['forge_remnant', 'iron_shardling', 'conduit_crawler', 'gear_revenant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'forge_remnant',
        'name': 'Forge Remnant',
        'hostile_type': 'construct',
        'min_spawn_level': 18,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 130,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (22, 72),
        'basic_attack': 'swings with a slag-encrusted fist',
        'strong_attack': 'forge slam',
        'player_abilities': [],
        'base_str': 14, 'base_dex': 6, 'base_con': 12, 'base_int': 3,
        'base_hp': 200, 'base_ap': 6,
        'str_per_level': 3, 'dex_per_level': 1, 'con_per_level': 3, 'int_per_level': 0,
        'resistances': ['fire', 'physical'],
        'immunities': ['burn'],
        'weaknesses': ['electric'],
    },
    {
        'id': 'iron_shardling',
        'name': 'Iron Shardling',
        'hostile_type': 'elemental',
        'min_spawn_level': 19,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 162,
        'common_drop': 'ointment',
        'rare_drop': 'herb_med',
        'money_range': (28, 88),
        'basic_attack': 'scatters razor-edged metal shards',
        'strong_attack': 'shard burst',
        'player_abilities': [],
        'base_str': 8, 'base_dex': 14, 'base_con': 8, 'base_int': 6,
        'base_hp': 175, 'base_ap': 6,
        'str_per_level': 1, 'dex_per_level': 3, 'con_per_level': 1, 'int_per_level': 1,
        'resistances': ['physical'],
        'immunities': ['slow'],
        'weaknesses': ['electric', 'fire'],
    },
    {
        'id': 'conduit_crawler',
        'name': 'Conduit Crawler',
        'hostile_type': 'construct',
        'min_spawn_level': 20,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 212,
        'common_drop': 'stimulant_med',
        'rare_drop': 'petrify_salve',
        'money_range': (36, 115),
        'basic_attack': 'crashes forward along the relay conduits',
        'strong_attack': 'conduit surge',
        'player_abilities': [],
        'base_str': 10, 'base_dex': 5, 'base_con': 18, 'base_int': 4,
        'base_hp': 280, 'base_ap': 6,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 4, 'int_per_level': 0,
        'resistances': ['electric', 'physical'],
        'immunities': ['stun'],
        'weaknesses': ['fire'],
    },
    {
        'id': 'gear_revenant',
        'name': 'Gear Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 20,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 288,
        'common_drop': 'herb_med',
        'rare_drop': 'petrify_salve',
        'money_range': (52, 162),
        'basic_attack': 'strikes charged by centuries of forge-frequency',
        'strong_attack': 'resonance discharge',
        'player_abilities': [],
        'base_str': 12, 'base_dex': 14, 'base_con': 10, 'base_int': 10,
        'base_hp': 240, 'base_ap': 7,
        'str_per_level': 2, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['dark', 'physical'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'electric'],
    },
]

BOSS_MOB: Dict = {
    'id': 'gearghost_boss',
    'name': 'The Gearghost',
    'hostiles': ['gearghost_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'gearghost_1',
        'name': 'The Gearghost',
        'hostile_type': 'undead',
        'min_spawn_level': 21,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 4200,
        'common_drop': 'petrify_salve',
        'rare_drop': 'petrify_salve',
        'money_range': (120, 350),
        'basic_attack': 'phases through the forge walls to strike from every direction',
        'strong_attack': 'gearghost rupture',
        'player_abilities': [],
        'base_str': 18, 'base_dex': 20, 'base_con': 16, 'base_int': 18,
        'base_hp': 5500, 'base_ap': 120,
        'str_per_level': 2, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 2,
        'resistances': ['dark', 'physical', 'fire'],
        'immunities': ['sleep', 'stun', 'burn'],
        'weaknesses': ['light', 'electric'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'mountains_large_city_type_e_gearghost_dungeon',
    'display_name': 'The Deep Forge',
    'seed': abs(hash('mountains_large_city_type_e_gearghost_dungeon')),
    'floor_count': 1,
    'rooms_per_floor': 3,
    'room_size_min_max': (55, 100),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.07,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (3, 5),
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