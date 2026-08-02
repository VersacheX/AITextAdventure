"""Desert Mid City — Ink Sanctum Dungeon Seed (Type D)"""

from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────────────────
# desert_mid_ink_sanctum.py
# City: The Vaults (desert_mid, Ch.8)
# Chain: Type D — Mythic Accessory (Veilscript Sigil)
# Player level at encounter: ~40
# Pattern: A — boss guards identity-ink in final_chamber
# ─────────────────────────────────────────────────────────────────────────────

OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.11
OPEN_AREA_COLOR  = '#282838'
IMPASSABLE_COLOR = '#0c0c14'
BORDER_TILE      = '·'
BORDER_COLOR     = '#1c1c28'

DUNGEON_NPCS: List[Dict] = [
    {'id': 'ink_specter', 'location': 'final_chamber'},
]

DUNGEON_ITEMS: List[Dict] = [
    {'id': 'herb_med',      'location': 'treasure_room'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'stimulant_med',    'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['script_shade', 'ink_crawler', 'vault_construct', 'identity_revenant'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'script_shade',
        'name': 'Script Shade',
        'hostile_type': 'undead',
        'min_spawn_level': 38,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 252,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (66, 210),
        'basic_attack': 'slashes with a script-hardened tendril',
        'strong_attack': 'inscription slash',
        'player_abilities': [],
        'base_str': 26, 'base_dex': 24, 'base_con': 20, 'base_int': 14,
        'base_hp': 480, 'base_ap': 10,
        'str_per_level': 3, 'dex_per_level': 2, 'con_per_level': 2, 'int_per_level': 1,
        'resistances': ['dark'],
        'immunities': ['sleep'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'ink_crawler',
        'name': 'Ink Crawler',
        'hostile_type': 'creature',
        'min_spawn_level': 39,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 308,
        'common_drop': 'petrify_salve',
        'rare_drop': 'herb_med',
        'money_range': (78, 248),
        'basic_attack': 'blots out vision with a spray of corrupted ink',
        'strong_attack': 'ink blind',
        'player_abilities': [],
        'base_str': 16, 'base_dex': 28, 'base_con': 18, 'base_int': 18,
        'base_hp': 490, 'base_ap': 10,
        'str_per_level': 1, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 2,
        'resistances': ['dark', 'physical'],
        'immunities': ['confuse'],
        'weaknesses': ['light', 'fire'],
    },
    {
        'id': 'vault_construct',
        'name': 'Vault Construct',
        'hostile_type': 'construct',
        'min_spawn_level': 40,
        'role': 'tank',
        'rarity': 'rare',
        'base_xp': 392,
        'common_drop': 'stimulant_large',
        'rare_drop': 'stimulant_med',
        'money_range': (96, 308),
        'basic_attack': 'pins targets beneath archival weight',
        'strong_attack': 'vault lock',
        'player_abilities': [],
        'base_str': 20, 'base_dex': 10, 'base_con': 34, 'base_int': 12,
        'base_hp': 680, 'base_ap': 10,
        'str_per_level': 1, 'dex_per_level': 0, 'con_per_level': 5, 'int_per_level': 1,
        'resistances': ['physical', 'dark'],
        'immunities': ['stun', 'slow'],
        'weaknesses': ['electric', 'fire'],
    },
    {
        'id': 'identity_revenant',
        'name': 'Identity Revenant',
        'hostile_type': 'undead',
        'min_spawn_level': 40,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 532,
        'common_drop': 'herb_med',
        'rare_drop': 'stimulant_med',
        'money_range': (128, 412),
        'basic_attack': "rewrites the target's defenses with stolen identity-ink",
        'strong_attack': 'identity rewrite',
        'player_abilities': [],
        'base_str': 26, 'base_dex': 28, 'base_con': 22, 'base_int': 24,
        'base_hp': 620, 'base_ap': 11,
        'str_per_level': 3, 'dex_per_level': 3, 'con_per_level': 2, 'int_per_level': 3,
        'resistances': ['dark', 'physical'],
        'immunities': ['sleep', 'confuse'],
        'weaknesses': ['light', 'fire'],
    },
]

BOSS_MOB: Dict = {
    'id': 'ink_specter_boss',
    'name': 'The Ink Specter',
    'hostiles': ['ink_specter_1'],
}

BOSS_HOSTILES: List[Dict] = [
    {
        'id': 'ink_specter_1',
        'name': 'The Ink Specter',
        'hostile_type': 'undead',
        'min_spawn_level': 41,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 8500,
        'common_drop': 'stimulant_med',
        'rare_drop': 'stimulant_med',
        'money_range': (210, 630),
        'basic_attack': 'floods the sanctum with identity-corroding ink',
        'strong_attack': 'veilscript erasure',
        'player_abilities': [],
        'base_str': 32, 'base_dex': 36, 'base_con': 30, 'base_int': 38,
        'base_hp': 11000, 'base_ap': 188,
        'str_per_level': 3, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 4,
        'resistances': ['dark', 'physical'],
        'immunities': ['sleep', 'confuse', 'stun'],
        'weaknesses': ['light', 'fire'],
    },
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'desert_mid_ink_sanctum',
    'display_name': 'The Inkwell Depths',
    'seed': abs(hash('desert_mid_ink_sanctum')),
    'floor_count': 1,
    'rooms_per_floor': 3,
    'room_size_min_max': (55, 100),
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