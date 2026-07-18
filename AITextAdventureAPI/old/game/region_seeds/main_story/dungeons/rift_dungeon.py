"""Rift Dungeon (Chapter 4) Seed Configuration

A two‑floor unstable rift beneath the city center. Spatial distortion,
temporal echoes, and void‑touched hostiles populate the shifting rooms.
Catalyst, a rift demon, anchors the instability at the deepest point.
"""

from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.18
OPEN_AREA_COLOR  = "#7a5a9e"
IMPASSABLE_COLOR = "#2e1a4a"
BORDER_TILE      = "░"
BORDER_COLOR     = "#5a3a7a"

############################################################
# HOSTILES PER FLOOR
############################################################

FLOOR_HOSTILES = {
    1: ['rift_shade', 'echo_stalker', 'phase_warp_beetle', 'unstable_fragment'],
    2: ['rift_horror', 'voidbound_sentinel', 'temporal_mite', 'echo_wraith'],
}

############################################################
# HOSTILE SEEDS
############################################################

HOSTILE_SEEDS = [

    # Floor 1 Hostiles
    {
        'id': 'rift_shade',
        'name': 'Rift Shade',
        'hostile_type': 'spirit',
        'min_spawn_level': 22,
        'role': 'hazard',
        'rarity': 'superrare',
        'base_xp': 200,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (18, 36),
        'basic_attack': 'shadow graze',
        'strong_attack': 'rift pulse',
        'player_abilities': ['dark_dark_magic_lv2_umbra_storm'],
        'base_str': 8,
        'base_dex': 14,
        'base_con': 10,
        'base_int': 18,
        'base_hp': 420,
        'base_ap': 40,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 3,
        'resistances': ['dark'],
        'immunities': ['continuous_damage'],
        'weaknesses': ['light']
    },

    {
        'id': 'echo_stalker',
        'name': 'Echo Stalker',
        'hostile_type': 'beast',
        'min_spawn_level': 22,
        'role': 'damage',
        'rarity': 'rare',
        'base_xp': 180,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (14, 32),
        'basic_attack': 'echo slash',
        'strong_attack': 'phase rend',
        'player_abilities': ['air_dark_skill_lv2_gale_of_doubt'],
        'base_str': 14,
        'base_dex': 16,
        'base_con': 12,
        'base_int': 6,
        'base_hp': 380,
        'base_ap': 32,
        'str_per_level': 2,
        'dex_per_level': 2,
        'con_per_level': 2,
        'int_per_level': 0,
        'resistances': ['physical'],
        'immunities': [],
        'weaknesses': ['ice']
    },

    {
        'id': 'phase_warp_beetle',
        'name': 'Phase‑Warp Beetle',
        'hostile_type': 'construct',
        'min_spawn_level': 23,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 260,
        'common_drop': 'stimulant_small',
        'rare_drop': 'tome_con',
        'money_range': (30, 60),
        'basic_attack': 'warp slam',
        'strong_attack': 'dimensional crush',
        'player_abilities': ['earth_earth_tech_lv2_seismic_rupture'],
        'base_str': 18,
        'base_dex': 6,
        'base_con': 22,
        'base_int': 4,
        'base_hp': 900,
        'base_ap': 40,
        'str_per_level': 3,
        'dex_per_level': 0,
        'con_per_level': 4,
        'int_per_level': 0,
        'resistances': ['earth', 'physical'],
        'immunities': ['stun'],
        'weaknesses': ['electric']
    },

    {
        'id': 'unstable_fragment',
        'name': 'Unstable Fragment',
        'hostile_type': 'elemental',
        'min_spawn_level': 21,
        'role': 'hazard',
        'rarity': 'common',
        'base_xp': 140,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (10, 20),
        'basic_attack': 'fracture burst',
        'strong_attack': 'volatile detonation',
        'player_abilities': ['electric_dark_tech_lv2_void_shocker'],
        'base_str': 10,
        'base_dex': 10,
        'base_con': 8,
        'base_int': 14,
        'base_hp': 300,
        'base_ap': 28,
        'str_per_level': 1,
        'dex_per_level': 1,
        'con_per_level': 1,
        'int_per_level': 2,
        'resistances': ['electric'],
        'immunities': [],
        'weaknesses': ['earth']
    },

    # Floor 2 Hostiles
    {
        'id': 'rift_horror',
        'name': 'Rift Horror',
        'hostile_type': 'aberration',
        'min_spawn_level': 25,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 300,
        'common_drop': 'stimulant_large',
        'rare_drop': 'tome_str',
        'money_range': (40, 80),
        'basic_attack': 'void lash',
        'strong_attack': 'horizon tear',
        'player_abilities': ['dark_dark_technique_lv2_void_crush'],
        'base_str': 20,
        'base_dex': 14,
        'base_con': 16,
        'base_int': 18,
        'base_hp': 600,
        'base_ap': 50,
        'str_per_level': 2,
        'dex_per_level': 2,
        'con_per_level': 2,
        'int_per_level': 2,
        'resistances': ['dark'],
        'immunities': ['confuse'],
        'weaknesses': ['light']
    },

    {
        'id': 'voidbound_sentinel',
        'name': 'Voidbound Sentinel',
        'hostile_type': 'construct',
        'min_spawn_level': 25,
        'role': 'support',
        'rarity': 'rare',
        'base_xp': 350,
        'common_drop': 'stimulant_small',
        'rare_drop': 'tome_con',
        'money_range': (50, 100),
        'basic_attack': 'null strike',
        'strong_attack': 'gravity crush',
        'player_abilities': ['earth_light_tech_lv2_impact_percussion'],
        'base_str': 22,
        'base_dex': 8,
        'base_con': 26,
        'base_int': 6,
        'base_hp': 1200,
        'base_ap': 60,
        'str_per_level': 3,
        'dex_per_level': 0,
        'con_per_level': 4,
        'int_per_level': 1,
        'resistances': ['earth', 'dark'],
        'immunities': ['stun'],
        'weaknesses': ['electric']
    },

    {
        'id': 'temporal_mite',
        'name': 'Temporal Mite',
        'hostile_type': 'insect',
        'min_spawn_level': 24,
        'role': 'hazard',
        'rarity': 'common',
        'base_xp': 160,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (12, 24),
        'basic_attack': 'time nibble',
        'strong_attack': 'chronal burst',
        'player_abilities': ['air_dark_magic_lv2_night_wind'],
        'base_str': 8,
        'base_dex': 18,
        'base_con': 8,
        'base_int': 12,
        'base_hp': 260,
        'base_ap': 30,
        'str_per_level': 1,
        'dex_per_level': 3,
        'con_per_level': 1,
        'int_per_level': 2,
        'resistances': ['air'],
        'immunities': [],
        'weaknesses': ['earth']
    },

    {
        'id': 'echo_wraith',
        'name': 'Echo Wraith',
        'hostile_type': 'spirit',
        'min_spawn_level': 24,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 200,
        'common_drop': 'ointment',
        'rare_drop': None,
        'money_range': (20, 40),
        'basic_attack': 'memory drain',
        'strong_attack': 'echo scream',
        'player_abilities': ['air_dark_tech_lv2_hush_now'],
        'base_str': 10,
        'base_dex': 14,
        'base_con': 10,
        'base_int': 20,
        'base_hp': 340,
        'base_ap': 36,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 3,
        'resistances': ['dark'],
        'immunities': [],
        'weaknesses': ['light']
    },
]

############################################################
# DUNGEON NPCS
############################################################

DUNGEON_NPCS = [
    {'id': 'catalyst', 'location': 'final_chamber'}
]

############################################################
# DUNGEON ITEMS
############################################################

DUNGEON_ITEMS = [
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'tome_int', 'location': 'treasure_room'},
    {'id': 'tome_dex', 'location': 'treasure_room'},
]

############################################################
# BOSS MOB
############################################################

BOSS_MOB = {
    'id': 'catalyst_1',
    'name': 'Catalyst',
    'hostiles': ['catalyst_1', 'riftling_malice', 'riftling_sorrow']
}

############################################################
# BOSS HOSTILES
############################################################

BOSS_HOSTILES = [

    {
        'id': 'catalyst_1',
        'name': 'Catalyst',
        'hostile_type': 'rift_demon',
        'role': 'damage',
        'min_spawn_level': 28,
        'rarity': 'notfound',
        'base_xp': 5000,
        'common_drop': 'tome_con',
        'rare_drop': 'tome_int',
        'money_range': (300, 700),
        'basic_attack': 'rift cleave',
        'strong_attack': 'cataclysmic inversion',
        'player_abilities': [
            'dark_dark_technique_lv2_void_crush',
            'light_dark_technique_lv2_twilight_cleave',
            'earth_dark_magic_lv2_sinkhole'
        ],
        'base_str': 24,
        'base_dex': 18,
        'base_con': 24,
        'base_int': 22,
        'base_hp': 10000,
        'base_ap': 240,
        'str_per_level': 3,
        'dex_per_level': 2,
        'con_per_level': 4,
        'int_per_level': 3,
        'resistances': ['dark', 'fire'],
        'immunities': ['confuse', 'stun', 'petrify'],
        'weaknesses': ['light']
    },

    {
        'id': 'riftling_malice',
        'name': 'Riftling of Malice',
        'hostile_type': 'fiend',
        'role': 'hazard',
        'min_spawn_level': 26,
        'rarity': 'uncommon',
        'base_xp': 200,
        'common_drop': 'herb_mid',
        'rare_drop': None,
        'money_range': (20, 40),
        'basic_attack': 'malice jab',
        'strong_attack': 'chaos bolt',
        'player_abilities': ['air_dark_magic_lv2_gloom_vortex'],
        'base_str': 10,
        'base_dex': 16,
        'base_con': 10,
        'base_int': 14,
        'base_hp': 360,
        'base_ap': 40,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 2,
        'resistances': ['fire'],
        'immunities': [],
        'weaknesses': ['water']
    },

    {
        'id': 'riftling_sorrow',
        'name': 'Riftling of Sorrow',
        'hostile_type': 'fiend',
        'role': 'hazard',
        'min_spawn_level': 26,
        'rarity': 'uncommon',
        'base_xp': 210,
        'common_drop': 'stimulant_mid',
        'rare_drop': None,
        'money_range': (22, 44),
        'basic_attack': 'sorrow claw',
        'strong_attack': 'void surge',
        'player_abilities': ['air_dark_skill_lv2_gale_of_doubt'],
        'base_str': 10,
        'base_dex': 18,
        'base_con': 10,
        'base_int': 14,
        'base_hp': 340,
        'base_ap': 40,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 2,
        'resistances': ['dark'],
        'immunities': [],
        'weaknesses': ['light']
    }
]

############################################################
# DUNGEON SETTINGS
############################################################

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'rift_dungeon_ch4',
    'seed': abs(hash('rift_dungeon_ch4')),
    'floor_count': 2,
    'room_size_min_max': (90, 150),
    'rooms_per_floor': 6,
    'max_neighbors_per_room': 3,
    'additional_connection_chance': 0.05,
    'min_max_distance_between_rooms': (2, 5),
    'min_max_corridor_width': (3, 7),
    'display_name': 'Rift Dungeon',
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color':  OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile':      BORDER_TILE,
    'border_color':     BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 8,
}
