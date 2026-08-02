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
    {'id': 'herb_med',         'location': 'treasure_room'},
    {'id': 'stimulant_large',    'location': 'treasure_room'},
    {'id': 'petrify_salve',         'location': 'final_chamber'},
]

FLOOR_HOSTILES: Dict[int, List[str]] = {
    1: ['murk_drifter', 'rot_tendril', 'sludge_crawler', 'channel_wraith'],
}

HOSTILE_SEEDS: List[Dict] = [
    {
        'id': 'murk_drifter',
        'name': 'Murk Drifter',
        'hostile_type': 'humanoid',
        'role': 'damage',

        'min_spawn_level': 32,        
        'rarity': 'common',
        'base_xp': 210,

        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (55, 140),

        'basic_attack': 'slams with a waterlogged club',
        'strong_attack': 'dredging slam',
        'player_abilities': ['water_technique_lv1_slick_manuever', 'earth_technique_lv1_armor_up'],

        'base_str': 6, 'base_dex': 5, 'base_con': 5, 'base_int': 3,
        'base_hp': 200, 'base_ap': 54,
        'str_per_level': 5, 'dex_per_level': 3, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['water'],
        'immunities': [],
        'weaknesses': ['fire']
    },
    {
        'id': 'rot_tendril',
        'name': 'Rot Tendril',
        'hostile_type': 'beast',
        'min_spawn_level': 33,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 245,
        'common_drop': 'ointment',
        'rare_drop': 'petrify_salve',
        'money_range': (60, 155),
        'basic_attack': 'lashes with a rotting tendril',
        'strong_attack': 'constricting wrap',
        'player_abilities': ['poison_strike', 'ensnare'],

        'base_str': 5, 'base_dex': 6, 'base_con': 5, 'base_int': 2,
        'base_hp': 220, 'base_ap': 48,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 1,
        'resistances': ['continuous_damage'],
        'immunities': [],
        'weaknesses': ['fire']
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
        'rare_drop': 'plasma_carapace',
        'money_range': (80, 200),
        'basic_attack': 'crashes forward with its armored shell',
        'strong_attack': 'sludge crush',
        'player_abilities': ['earth_light_technique_lv2_stone_guard', 'earth_earth_technique_lv2_brutal_swing'],

        'base_str': 8, 'base_dex': 4, 'base_con': 8, 'base_int': 2,
        'base_hp': 300, 'base_ap': 60,
        'str_per_level': 5, 'dex_per_level': 2, 'con_per_level': 4, 'int_per_level': 1,
        'resistances': ['earth'],
        'immunities': ['stun'],
        'weaknesses': ['water']
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
        'rare_drop': 'greatsword',
        'money_range': (110, 280),
        'basic_attack': 'phases through and drains life',
        'strong_attack': 'channel devour',
        'player_abilities': ['lv2_hostile_ability_dark_electric_magic_abyssal_storm', 'air_dark_magic_lv2_gloom_vortex'],

        'base_str': 6, 'base_dex': 7, 'base_con': 5, 'base_int': 8,
        'base_hp': 250, 'base_ap': 70,
        'str_per_level': 4, 'dex_per_level': 4, 'con_per_level': 3, 'int_per_level': 5,
        'resistances': ['dark', 'electric'],
        'immunities': ['sleep', 'silence'],
        'weaknesses': ['light']
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