"""
Tempest Bunker - Chapter 5 Dungeon Seed Configuration
Abandoned pre-fracture storm research facility.
Theme: High-tech ruin with unstable energy, lightning hazards, and wind currents.
The Polar Amplifier is the main goal, guarded by the Tempest Warden boss.
"""

from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.14
OPEN_AREA_COLOR  = "#607080"
IMPASSABLE_COLOR = "#2a3040"
BORDER_TILE      = "·"
BORDER_COLOR     = "#485868"

# Hostiles per floor
FLOOR_HOSTILES = {
    1: ['storm_drone', 'arc_wraith', 'charged_slime', 'vent_crawler'],
    2: ['storm_drone', 'arc_wraith', 'tempest_automaton', 'vent_crawler'],
}

HOSTILE_SEEDS = [
    {
        'id': 'storm_drone',
        'name': 'Storm Drone',
        'hostile_type': 'construct',
        'min_spawn_level': 24,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 160,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (15, 30),
        'basic_attack': 'lightning burst',
        'strong_attack': 'overcharge beam',
        'player_abilities': ['electric_dark_tech_lv2_void_shocker'],
        'base_str': 8,
        'base_dex': 16,
        'base_con': 10,
        'base_int': 12,
        'base_hp': 340,
        'base_ap': 35,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 2,
        'resistances': ['electric'],
        'immunities': [],
        'weaknesses': ['earth']
    },
    {
        'id': 'arc_wraith',
        'name': 'Arc Wraith',
        'hostile_type': 'spirit',
        'min_spawn_level': 25,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 210,
        'common_drop': 'herb_med',
        'rare_drop': 'tome_int',
        'money_range': (20, 45),
        'basic_attack': 'plasma lash',
        'strong_attack': 'discharge scream',
        'player_abilities': ['electric_dark_magic_lv2_nocturne_shock'],
        'base_str': 6,
        'base_dex': 14,
        'base_con': 12,
        'base_int': 18,
        'base_hp': 380,
        'base_ap': 40,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 3,
        'resistances': ['electric', 'dark'],
        'immunities': ['continuous_damage'],
        'weaknesses': ['earth']
    },
    {
        'id': 'charged_slime',
        'name': 'Charged Slime',
        'hostile_type': 'ooze',
        'min_spawn_level': 24,
        'role': 'hazard',
        'rarity': 'common',
        'base_xp': 140,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (12, 28),
        'basic_attack': 'voltaic touch',
        'strong_attack': 'chain lightning',
        'player_abilities': ['electric_water_skill_lv2_corrosive_drip'],
        'base_str': 6,
        'base_dex': 10,
        'base_con': 16,
        'base_int': 8,
        'base_hp': 420,
        'base_ap': 25,
        'str_per_level': 1,
        'dex_per_level': 1,
        'con_per_level': 3,
        'int_per_level': 1,
        'resistances': ['electric'],
        'immunities': [],
        'weaknesses': ['ice']
    },
    {
        'id': 'vent_crawler',
        'name': 'Vent Crawler',
        'hostile_type': 'beast',
        'min_spawn_level': 25,
        'role': 'damage',
        'rarity': 'rare',
        'base_xp': 190,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (18, 38),
        'basic_attack': 'razor pincer',
        'strong_attack': 'vent ambush',
        'player_abilities': ['earth_dark_technique_lv2_rabid_bite'],
        'base_str': 14,
        'base_dex': 18,
        'base_con': 12,
        'base_int': 6,
        'base_hp': 360,
        'base_ap': 30,
        'str_per_level': 2,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 0,
        'resistances': ['physical'],
        'immunities': [],
        'weaknesses': ['fire']
    },
    {
        'id': 'tempest_automaton',
        'name': 'Tempest Automaton',
        'hostile_type': 'construct',
        'min_spawn_level': 26,
        'role': 'damage',
        'rarity': 'uncommon',
        'base_xp': 280,
        'common_drop': 'stimulant_med',
        'rare_drop': 'tome_con',
        'money_range': (35, 70),
        'basic_attack': 'storm hammer',
        'strong_attack': 'thunderclap',
        'player_abilities': ['electric_earth_tech_lv2_ion_leech'],
        'base_str': 20,
        'base_dex': 10,
        'base_con': 24,
        'base_int': 8,
        'base_hp': 850,
        'base_ap': 45,
        'str_per_level': 3,
        'dex_per_level': 1,
        'con_per_level': 3,
        'int_per_level': 1,
        'resistances': ['electric', 'earth'],
        'immunities': ['stun'],
        'weaknesses': ['ice']
    }
]

DUNGEON_NPCS = [
    {'id': 'tempest_warden', 'location': 'final_chamber'}
]

DUNGEON_ITEMS = [
    {'id': 'polar_amplifier', 'location': 'final_chamber'},
    {'id': 'stimulant_large', 'location': 'treasure_room'},
    {'id': 'arc_core', 'location': 'treasure_room'},
    {'id': 'storm_etched_plating', 'location': 'treasure_room'},
    {'id': 'tome_int', 'location': 'treasure_room'}
]

BOSS_MOB = {
    'id': 'tempest_warden_1',
    'name': 'Tempest Warden',
    'hostiles': ['tempest_warden_1', 'stormling', 'stormling']
}

BOSS_HOSTILES = [
    {
        'id': 'tempest_warden_1',
        'name': 'Tempest Warden',
        'hostile_type': 'storm_construct',
        'role': 'damage',
        'min_spawn_level': 28,
        'rarity': 'notfound',
        'base_xp': 4200,
        'common_drop': 'tome_con',
        'rare_drop': 'polar_amplifier',
        'money_range': (250, 550),
        'basic_attack': 'lightning lash',
        'strong_attack': 'cataclysmic storm',
        'player_abilities': ['electric_dark_magic_lv2_nocturne_shock', 'electric_earth_tech_lv2_seismic_rupture'],
        'base_str': 18,
        'base_dex': 22,
        'base_con': 20,
        'base_int': 16,
        'base_hp': 9200,
        'base_ap': 220,
        'str_per_level': 2,
        'dex_per_level': 3,
        'con_per_level': 3,
        'int_per_level': 2,
        'resistances': ['electric', 'air'],
        'immunities': ['stun', 'confuse'],
        'weaknesses': ['earth']
    },
    {
        'id': 'stormling',
        'name': 'Stormling',
        'hostile_type': 'elemental',
        'role': 'hazard',
        'min_spawn_level': 26,
        'rarity': 'uncommon',
        'base_xp': 180,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (15, 35),
        'basic_attack': 'spark burst',
        'strong_attack': 'chain lightning',
        'player_abilities': ['electric_water_skill_lv2_corrosive_drip'],
        'base_str': 8,
        'base_dex': 14,
        'base_con': 10,
        'base_int': 12,
        'base_hp': 320,
        'base_ap': 30,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 2,
        'resistances': ['electric'],
        'immunities': [],
        'weaknesses': ['ice']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'tempest_bunker_ch5',
    'seed': abs(hash('tempest_bunker_ch5')),
    'floor_count': 2,
    'room_size_min_max': (90, 160),
    'rooms_per_floor': 5,
    'max_neighbors_per_room': 3,
    'additional_connection_chance': 0.04,
    'min_max_distance_between_rooms': (2, 6),
    'min_max_corridor_width': (3, 6),
    'display_name': "Tempest Research Bunker",
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
    'visible_distance': 7,
}