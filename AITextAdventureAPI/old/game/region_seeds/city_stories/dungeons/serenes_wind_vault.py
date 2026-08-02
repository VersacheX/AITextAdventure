"""Grassland Large City — Serene's Wind Vault Dungeon Seed (Type B)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# serenes_wind_vault.py
# City: The Noble Bazaar (grassland_large, Ch.10)
# Chain: Type B — Regional Boss / Void Gauntlet (Nia)
# Player level at encounter: ~50
# Pattern: B — player teleported to final_chamber; boss = serene_b1
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.09
OPEN_AREA_COLOR  = '#788858'
IMPASSABLE_COLOR = '#262e1c'
BORDER_TILE      = '·'
BORDER_COLOR     = '#566640'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'serene', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['echo_stalker', 'archived_whisper', 'vault_sentinel', 'void_echo'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'echo_stalker',
        'name': 'Echo Stalker',
        'hostile_type': 'undead',
        'min_spawn_level': 48,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 334,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (88, 280),
        'basic_attack': 'replays a stolen word as a concussive force',
        'strong_attack': 'echo replay',
        'player_abilities': [],
        'base_str': 32, 'base_dex': 32, 'base_con': 24, 'base_int': 16,
        'base_hp': 648, 'base_ap': 12,
        'str_per_level': 3, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['dark', 'air'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'electric'],
    },
    {
        'id': 'archived_whisper',
        'name': 'Archived Whisper',
        'hostile_type': 'undead',
        'min_spawn_level': 49,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 408,
        'common_drop': 'stimulant_med',
        'rare_drop': 'herb_med',
        'money_range': (108, 342),
        'basic_attack': 'speaks a stolen pattern into a disorienting strike',
        'strong_attack': 'pattern disrupt',
        'player_abilities': [],
        'base_str': 20, 'base_dex': 36, 'base_con': 22, 'base_int': 24,
        'base_hp': 660, 'base_ap': 12,
        'str_per_level': 1, 'dex_per_level': 4, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark'],
        'immunities': ['confuse', 'sleep'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'vault_sentinel',
        'name': 'Vault Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 50,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 518,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (132, 420),
        'basic_attack': 'walls off movement with the weight of archived voices',
        'strong_attack': 'archive crush',
        'player_abilities': [],
        'base_str': 24, 'base_dex': 14, 'base_con': 44, 'base_int': 14,
        'base_hp': 890, 'base_ap': 12,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 5, 'int_per_level': 1,
        'resistances': ['physical', 'dark'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['electric', 'light'],
    },
    {
        'id': 'void_echo',
        'name': 'Void Echo',
        'hostile_type': 'elemental',
        'min_spawn_level': 50,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 698,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (165, 530),
        'basic_attack': 'broadcasts a void-infused echo that bypasses shields',
        'strong_attack': 'void broadcast',
        'player_abilities': [],
        'base_str': 30, 'base_dex': 36, 'base_con': 26, 'base_int': 30,
        'base_hp': 810, 'base_ap': 13,
        'str_per_level': 3, 'dex_per_level': 4, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark', 'air'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'electric'],
    },
]

BOSS_MOB: Dict = {
    'id': 'serene_boss',
    'name': 'Serene the Whisper-Thief',
    'hostiles': ['serene_b1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'serene_b1',
        'name': 'Serene the Whisper-Thief',
        'hostile_type': 'humanoid',
        'min_spawn_level': 52,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 22000,
        'common_drop': 'stimulant_med',
        'rare_drop': 'stimulant_med',
        'money_range': (540, 1620),
        'basic_attack': "turns the player's own words into a weapon",
        'strong_attack': 'whisper theft',
        'player_abilities': [],
        'base_str': 38, 'base_dex': 48, 'base_con': 34, 'base_int': 46,
        'base_hp': 26000, 'base_ap': 420,
        'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 5,
        'resistances': ['dark', 'air', 'physical'],
        'immunities': ['sleep', 'confuse', 'fear', 'stun'],
        'weaknesses': ['light', 'electric'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'serenes_wind_vault',
    'display_name': "Serene's Wind Vault",
    'seed': abs(hash('serenes_wind_vault')),
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