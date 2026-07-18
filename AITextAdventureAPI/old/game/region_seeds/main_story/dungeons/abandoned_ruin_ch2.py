"""Abandoned Ruin (Chapter2) Dungeon Seed Configuration

Level ~10 dungeon used by Chapter2 fetch-ingredient task. Mirrors structure
from `seth_hideout.py` but tuned for higher-level threats and a demigorgon boss.
"""

from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.16
OPEN_AREA_COLOR  = "#7a7060"
IMPASSABLE_COLOR = "#3d3830"
BORDER_TILE      = "·"
BORDER_COLOR     = "#5a5248"

# Hostiles that may appear per floor
FLOOR_HOSTILES = {
    1: ['ruin_wight', 'acid_slime', 'ruin_sentinel', 'stone_scarab'],
}

HOSTILE_SEEDS = [
 {
 'id': 'ruin_wight',
 'name': 'Ruin Wight',
 'hostile_type': 'undead',
 'min_spawn_level':12,
 'role': 'damage',
 'rarity': 'superrare',
 'base_xp':80,
 'common_drop': 'herb_minor',
 'rare_drop': None,
 'money_range': (6,14),
 'basic_attack': 'infectious scratch',
 'strong_attack': 'toxic nerve',
 'player_abilities': ['ruin_wight_decay_touch', 'ruin_wight_soulsap'],
 'base_str':6,
 'base_dex':6,
 'base_con':8,
 'base_int':4,
 'base_hp':180,
 'base_ap':12,
 'str_per_level':1,
 'dex_per_level':1,
 'con_per_level':2,
 'int_per_level':1,
 'resistances': ['dark'],
 'immunities': ['continuous_damage'],
 'weaknesses': ['light']
 },

 {
 'id': 'acid_slime',
 'name': 'Acid Slime',
 'hostile_type': 'ooze',
 'min_spawn_level':11,
 'role': 'hazard',
 'rarity': 'rare',
 'base_xp':90,
 'common_drop': 'stimulant_small',
 'rare_drop': None,
 'money_range': (4,12),
 'basic_attack': 'corrosive touch',
 'strong_attack': 'acid spray',
 'player_abilities': ["acid_slime"],
 'base_str':4,
 'base_dex':3,
 'base_con':12,
 'base_int':1,
 'base_hp':220,
 'base_ap':6,
 'str_per_level':1,
 'dex_per_level':0,
 'con_per_level':3,
 'int_per_level':0,
 'resistances': ['continuous_damage'],
 'immunities': [],
 'weaknesses': ['ice']
 },

 {
 'id': 'ruin_sentinel',
 'name': 'Ruin Sentinel',
 'hostile_type': 'construct',
 'min_spawn_level':11,
 'role': 'damage',
 'rarity': 'uncommon',
 'base_xp':170,
 'common_drop': 'stimulant_small',
 'rare_drop': 'tome_con',
 'money_range': (12,28),
 'basic_attack': 'stalwart smash',
 'strong_attack': 'bone shatter',
 'player_abilities': ['ruin_sentinel_stone_smash', 'ruin_sentinel_earthshatter'],
 'base_str':10,
 'base_dex':2,
 'base_con':16,
 'base_int':2,
 'base_hp':450,
 'base_ap':10,
 'str_per_level':2,
 'dex_per_level':0,
 'con_per_level':4,
 'int_per_level':0,
 'resistances': ['earth'],
 'immunities': ['stun'],
 'weaknesses': ['electric']
 },

 {
 'id': 'stone_scarab',
 'name': 'Stone Scarab',
 'hostile_type': 'insect',
 'min_spawn_level':10,
 'role': 'damage',
 'rarity': 'common',
 'base_xp':85,
 'common_drop': 'nano_helmet',
 'rare_drop': 'tome_dex',
 'money_range': (5,16),
 'basic_attack': 'horn bash',
 'strong_attack': 'pincer attack',
 'player_abilities': ['stone_scarab_chitin_bite', 'stone_scarab_carapace_bash'],
 'base_str':7,
 'base_dex':8,
 'base_con':6,
 'base_int':1,
 'base_hp':200,
 'base_ap':8,
 'str_per_level':1,
 'dex_per_level':2,
 'con_per_level':1,
 'int_per_level':0,
 'resistances': [],
 'immunities': [],
 'weaknesses': ['fire']
 }
]

DUNGEON_NPCS = [ {'id': 'the_demigorgon', 'location': 'final_chamber'} ]
DUNGEON_ITEMS = [ 
 {'id': 'stimulant_large', 'location': 'treasure_room'},
 {'id': 'exoshell_armor', 'location': 'treasure_room'},
 {'id': 'exoshell_gauntlets', 'location': 'treasure_room'},
 {'id': 'exoshell_legs', 'location': 'treasure_room'},
 {'id': 'katana', 'location': 'treasure_room'}
]

BOSS_MOB = {
 'id': 'demigorgon_1',
 'name': 'Demigorgon',
 'hostiles': [
    'demigorgon_1',
    'imp_mischief',
    'imp_malice']
}

BOSS_HOSTILES = [
    {
        'id': 'demigorgon_1',
        'name': 'The Demigorgon',
        'hostile_type': 'otherworld',
        'role': 'damage',
        'min_spawn_level':15,
        'rarity': 'notfound',
        'base_xp':4000,
        'common_drop': 'tome_int',
        'rare_drop': 'tome_con',
        'money_range': (200,500),
        'basic_attack': 'rending claw',
        'strong_attack': 'void maelstrom',
        'player_abilities': ['dark_dark_technique_lv2_void_crush', 'light_dark_technique_lv2_twilight_cleave'],
        'base_str':18,
        'base_dex':14,
        'base_con':18,
        'base_int':14,
        'base_hp':8000,
        'base_ap':200,
        'str_per_level':2,
        'dex_per_level':2,
        'con_per_level':3,
        'int_per_level':2,
        'resistances': ['dark', 'fire'],
        'immunities': ['confuse', 'stun', 'petrify'],
        'weaknesses': ['light']
    },
    {
        'id': 'imp_mischief',
        'name': 'Imp of Mischief',
        'hostile_type': 'fiend',
        'role': 'hazard',
        'min_spawn_level':13,
        'rarity': 'uncommon',
        'base_xp':150,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (10,30),
        'basic_attack': 'fiendish jab',
        'strong_attack': 'chaos bolt',
        'player_abilities': ['air_dark_magic_lv2_gloom_vortex'],
        'base_str':5,
        'base_dex':12,
        'base_con':6,
        'base_int':10,
        'base_hp':300,
        'base_ap':30,
        'str_per_level':1,
        'dex_per_level':2,
        'con_per_level':1,
        'int_per_level':2,
        'resistances': ['fire'],
        'immunities': [],
        'weaknesses': ['water']
    },
    {
        'id': 'imp_malice',
        'name': 'Imp of Malice',
        'hostile_type': 'fiend',
        'role': 'hazard',
        'min_spawn_level':13,
        'rarity': 'uncommon',
        'base_xp':160,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (12,32),
        'basic_attack': 'shadow claw',
        'strong_attack': 'dark surge',
        'player_abilities': ['air_dark_skill_lv2_gale_of_doubt'],
        'base_str':6,
        'base_dex':14,
        'base_con':5,
        'base_int':10,
        'base_hp':280,
        'base_ap':30,
        'str_per_level':1,
        'dex_per_level':2,
        'con_per_level':1,
        'int_per_level':2,
        'resistances': ['dark'],
        'immunities': [],
        'weaknesses': ['light']
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'abandoned_ruin_ch2',
    'seed': abs(hash('abandoned_ruin_ch2')),
    'floor_count':1,
    'room_size_min_max': (100,160),
    'rooms_per_floor':7,
    'max_neighbors_per_room':4,
    'additional_connection_chance':0.02,
    'min_max_distance_between_rooms': (2,5),
    'min_max_corridor_width': (3,7),
    'display_name': 'Abandoned Ruin',
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
