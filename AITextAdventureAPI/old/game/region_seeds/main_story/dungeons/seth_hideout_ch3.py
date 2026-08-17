"""
Seth's Hideout - Chapter 3 Region Seed Data
Dungeon seed configuration for Seth's Hideout used in Chapter 3 of the main story.
 - This is a short dungeon with 3 rooms and hostiles at level 16. 1 superrare, 1 common, 1 rare and 1 uncommon.
 - No boss fight
 - npc is seth in the final room
 - loot panacea, stimulant_large, herb_major
"""

from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.12
OPEN_AREA_COLOR  = "#5a6b50"
IMPASSABLE_COLOR = "#2e3a28"
BORDER_TILE      = "·"
BORDER_COLOR     = "#445240"

# Hostiles that may appear per floor
# no humans. level 16 1 rare, superrare, uncommon, common. cave worthy.
FLOOR_HOSTILES = {
    1: ['rabid_bear', 'cave_spider', 'vampire_bat', 'growing_mold'],
}

HOSTILE_SEEDS = [
    {
        'id': 'rabid_bear',
        'name': 'Rabid Bear',
        'hostile_type': 'beast',
        'min_spawn_level':16,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp':150,
        'common_drop': 'herb_major',
        'rare_drop': None,
        'money_range': (15,25),
        'basic_attack': 'ferocious swipe',
        'strong_attack': 'raging maul',
        'player_abilities': ['earth_dark_technique_lv2_rabid_bite', 'dark_dark_technique_lv2_infectious_bite'],
        'base_str':14,
        'base_dex':10,
        'base_con':16,
        'base_int':4,
        'base_hp':400,
        'base_ap':20,
        'str_per_level':2,
        'dex_per_level':1,
        'con_per_level':2,
        'int_per_level':0,
        'resistances': ['physical'],
        'immunities': [],
        'weaknesses': ['fire']
    },
    {
        'id': 'cave_spider',
        'name': 'Cave Spider',
        'hostile_type': 'insect',
        'min_spawn_level':16,
        'role': 'hazard',
        'rarity': 'common',
        'base_xp':90,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (8,15),
        'basic_attack': 'venomous bite',
        'strong_attack': 'web entangle',
        'player_abilities': ['electric_water_skill_lv2_corrosive_splash_bomb'],
        'base_str':8,
        'base_dex':14,
        'base_con':10,
        'base_int':6,
        'base_hp':250,
        'base_ap':15,
        'str_per_level':1,
        'dex_per_level':2,
        'con_per_level':1,
        'int_per_level':1,
        'resistances': ['continuous_damage'],
        'immunities': [],
        'weaknesses': ['fire']
    },
    {
        'id': 'vampire_bat',
        'name': 'Vampire Bat',
        'hostile_type': 'beast',
        'min_spawn_level':16,
        'role': 'damage',
        'rarity': 'rare',
        'base_xp':110,
        'common_drop': 'herb_med',
        'rare_drop': None,
        'money_range': (10,18),
        'basic_attack': 'blood drain',
        'strong_attack': 'sonic screech',
        'player_abilities': ['electric_dark_magic_lv2_nocturne_shock', 'electric_earth_magic_lv2_ion_leech'],
        'base_str':10,
        'base_dex':16,
        'base_con':12,
        'base_int':8,
        'base_hp':300,
        'base_ap':18,
        'str_per_level':1,
        'dex_per_level':2,
        'con_per_level':1,
        'int_per_level':1,
        'resistances': ['dark'],
        'immunities': [],
        'weaknesses': ['light']
    },
    {
        'id': 'growing_mold',
        'name': 'Growing Mold',
        'hostile_type': 'fungi',
        'min_spawn_level':16,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp':100,
        'common_drop': 'ointment',
        'rare_drop': None,
        'money_range': (9,16),
        'basic_attack': 'spore burst',
        'strong_attack': 'toxic cloud',
        'player_abilities': ['ice_fire_skill_lv2_acid_slime_spray'],
        'base_str':6,
        'base_dex':8,
        'base_con':14,
        'base_int':10,
        'base_hp':280,
        'base_ap':16,
        'str_per_level':1,
        'dex_per_level':1,
        'con_per_level':2,
        'int_per_level':1,
        'resistances': ['poison'],
        'immunities': ['continuous_damage'],
        'weaknesses': ['fire']
    }
]

DUNGEON_NPCS = [ {'id': 'seth', 'location': 'final_chamber'} ]
DUNGEON_ITEMS = [ 
 {'id': 'stimulant_large', 'location': 'treasure_room'},
 {'id': 'panacea', 'location': 'final_chamber'},
 {'id': 'herb_major', 'location': 'treasure_room' },
 {'id': 'plasma_mitts', 'location': 'treasure_room' }
]

BOSS_MOB = {
}

BOSS_HOSTILES = [
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'seth_hideout_ch3',
    'seed': abs(hash('seth_hideout_ch3')),
    'floor_count':1,
    'room_size_min_max': (60,110),
    'rooms_per_floor':3,
    'max_neighbors_per_room':2,
    'additional_connection_chance':0.02,
    'min_max_distance_between_rooms': (1,3),
    'min_max_corridor_width': (3,7),
    'display_name': 'Seth\'s Hideout',
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
