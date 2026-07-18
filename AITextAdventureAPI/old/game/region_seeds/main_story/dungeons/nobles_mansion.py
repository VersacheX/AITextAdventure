"""
Noble's Mansion - Chapter3 Dungeon Seed Configuration
This dungeon is created for Seth's side quest. A smaller mansion with a guardian boss
and several rooms. Contains the ingredients required by Kess: `scribe_mint` (final_chamber)
and `scarred_thyme` (treasure_room).
"""

from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.08
OPEN_AREA_COLOR  = "#b8904a"
IMPASSABLE_COLOR = "#5a3d20"
BORDER_TILE      = "·"
BORDER_COLOR     = "#8a6830"

# Hostiles that may appear per floor
FLOOR_HOSTILES = {
1: ['mansion_wraith', 'scarred_hound', 'steward_golem', 'mansion_specter'],
}

HOSTILE_SEEDS = [
 {
 'id': 'mansion_wraith',
 'name': 'Mansion Wraith',
 'hostile_type': 'undead',
 'min_spawn_level':17,
 'role': 'hazard',
 'rarity': 'rare',
 'base_xp':180,
 'common_drop': 'herb_med',
 'rare_drop': None,
 'money_range': (20,40),
 'basic_attack': 'phantasmal touch',
 'strong_attack': 'soul lash',
 'player_abilities': ['dark_dark_magic_lv2_umbra_storm', 'air_dark_tech_lv2_hush_now'],
 'base_str':8,
 'base_dex':12,
 'base_con':10,
 'base_int':14,
 'base_hp':420,
 'base_ap':40,
 'str_per_level':1,
 'dex_per_level':1,
 'con_per_level':2,
 'int_per_level':2,
 'resistances': ['dark'],
 'immunities': ['continuous_damage'],
 'weaknesses': ['light']
 },
 {
 'id': 'scarred_hound',
 'name': 'Scarred Hound',
 'hostile_type': 'beast',
 'min_spawn_level':17,
 'role': 'damage',
 'rarity': 'common',
 'base_xp':120,
 'common_drop': 'stimulant_small',
 'rare_drop': None,
 'money_range': (10,24),
 'basic_attack': 'maw snap',
 'strong_attack': 'scarred pounce',
 'player_abilities': ['fire_earth_tech_lv2_forge_pulse', 'earth_earth_technique_lv2_terra_slam'],
 'base_str':12,
 'base_dex':14,
 'base_con':12,
 'base_int':6,
 'base_hp':360,
 'base_ap':26,
 'str_per_level':2,
 'dex_per_level':2,
 'con_per_level':2,
 'int_per_level':0,
 'resistances': ['physical'],
 'immunities': [],
 'weaknesses': ['ice']
 },
 {
 'id': 'steward_golem',
 'name': 'Steward Golem',
 'hostile_type': 'construct',
 'min_spawn_level':18,
 'role': 'damage',
 'rarity': 'uncommon',
 'base_xp':220,
 'common_drop': 'stimulant_small',
 'rare_drop': 'tome_con',
 'money_range': (30,60),
 'basic_attack': 'iron bash',
 'strong_attack': 'earthshatter',
 'player_abilities': ['earth_earth_tech_lv2_seismic_rupture', 'earth_light_tech_lv2_impact_percussion'],
 'base_str':16,
 'base_dex':6,
 'base_con':20,
 'base_int':4,
 'base_hp':800,
 'base_ap':36,
 'str_per_level':3,
 'dex_per_level':0,
 'con_per_level':4,
 'int_per_level':0,
 'resistances': ['earth', 'physical'],
 'immunities': ['stun'],
 'weaknesses': ['electric']
 },
 {
 'id': 'mansion_specter',
 'name': 'Mansion Specter',
 'hostile_type': 'spirit',
 'min_spawn_level':15,
 'role': 'hazard',
 'rarity': 'uncommon',
 'base_xp':150,
 'common_drop': 'ointment',
 'rare_drop': None,
 'money_range': (12,28),
 'basic_attack': 'soul whisper',
 'strong_attack': 'etheric scream',
 'player_abilities': ['air_dark_magic_lv2_night_wind', 'electric_dark_tech_lv2_void_shocker'],
 'base_str':6,
 'base_dex':14,
 'base_con':10,
 'base_int':16,
 'base_hp':360,
 'base_ap':34,
 'str_per_level':1,
 'dex_per_level':2,
 'con_per_level':1,
 'int_per_level':3,
 'resistances': ['dark'],
 'immunities': [],
 'weaknesses': ['light']
 }
]

# place seth at the entrance as requested
DUNGEON_NPCS = [
    {'id': 'seth', 'location': 'entrance'},
    {'id': 'relic_guardian', 'location': 'final_chamber'}
]

DUNGEON_ITEMS = [
 {'id': 'stimulant_large', 'location': 'treasure_room'} 
]

# boss mob definition used by main story task flow
BOSS_MOB = {
 'id': 'relic_guardian_1',
 'name': 'Relic Guardian',
 'hostiles': ['relic_guardian_1']
}

BOSS_HOSTILES = [
 {
 'id': 'relic_guardian_1',
 'name': 'Relic Guardian',
 'hostile_type': 'spirit_construct',
 'role': 'damage',
 'min_spawn_level':20,
 'rarity': 'notfound',
 'base_xp':2500,
 'common_drop': 'tome_int',
 'rare_drop': 'scribe_mint',
 'money_range': (150,400),
 'basic_attack': 'relic slam',
 'strong_attack': 'cataclysmic rupture',
 'player_abilities': ['earth_dark_magic_lv2_sinkhole', 'dark_dark_technique_lv2_void_crush', 'light_light_faith_lv2_seraphic_nova'],
 'base_str':20,
 'base_dex':10,
 'base_con':22,
 'base_int':18,
 'base_hp':6000,
 'base_ap':180,
 'str_per_level':3,
 'dex_per_level':1,
 'con_per_level':4,
 'int_per_level':2,
 'resistances': ['earth', 'dark'],
 'immunities': ['petrify', 'confuse'],
 'weaknesses': ['light']
 }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'nobles_mansion_ch3',
    'seed': abs(hash('nobles_mansion_ch3')),
    'floor_count':1,
    'room_size_min_max': (80,140),
    'rooms_per_floor':5,
    'max_neighbors_per_room':3,
    'additional_connection_chance':0.03,
    'min_max_distance_between_rooms': (1,4),
    'min_max_corridor_width': (3,7),
    'display_name': "Noble's Mansion",
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
    'visible_distance':8,
}
