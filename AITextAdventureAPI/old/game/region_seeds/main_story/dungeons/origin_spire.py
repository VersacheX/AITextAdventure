"""
Origin Spire - Chapter 16 Dungeon Seed Configuration
The site of the first fracture -- a place where logic itself is architecture,
and meaning has been structurally removed. The geometry is unstable and recursive.
Boss: Crux (Origin Form) -- a living paradox of void logic.
"""
from typing import Dict, Any

OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.12
OPEN_AREA_COLOR  = "#5a4a7a"
IMPASSABLE_COLOR = "#18101e"
BORDER_TILE      = "░"
BORDER_COLOR     = "#3a2a58"

FLOOR_HOSTILES = {
	1: ['logic_shard', 'void_tendril', 'meaning_wraith', 'fracture_sentinel'],
}

HOSTILE_SEEDS = [
	{
		'id': 'logic_shard', 'name': 'Logic Shard', 'hostile_type': 'construct', 'min_spawn_level': 80, 'role': 'damage', 'rarity': 'common',
		'base_xp': 1300, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (460, 920),
		'basic_attack': 'axiom strike', 'strong_attack': 'contradiction blast', 'player_abilities': [],
		'base_str': 42, 'base_dex': 38, 'base_con': 40, 'base_int': 42, 'base_hp': 3400, 'base_ap': 110,
		'str_per_level': 5, 'dex_per_level': 4, 'con_per_level': 5, 'int_per_level': 5,
		'resistances': ['electric'], 'immunities': ['confuse'], 'weaknesses': ['dark']
	},
	{
		'id': 'void_tendril', 'name': 'Void Tendril', 'hostile_type': 'aberration', 'min_spawn_level': 80, 'role': 'hazard', 'rarity': 'uncommon',
		'base_xp': 1450, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (510, 1020),
		'basic_attack': 'null grasp', 'strong_attack': 'purposeless pull', 'player_abilities': ['dark_spirit_lv1_shade_whisper'],
		'base_str': 35, 'base_dex': 45, 'base_con': 35, 'base_int': 52, 'base_hp': 3100, 'base_ap': 130,
		'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 7,
		'resistances': ['dark'], 'immunities': ['stun'], 'weaknesses': ['light']
	},
	{
		'id': 'meaning_wraith', 'name': 'Meaning Wraith', 'hostile_type': 'spirit', 'min_spawn_level': 81, 'role': 'hazard', 'rarity': 'rare',
		'base_xp': 1700, 'common_drop': 'panacea', 'rare_drop': 'tome_int_superrare', 'money_range': (620, 1240),
		'basic_attack': 'hollow touch', 'strong_attack': 'erasure wail', 'player_abilities': ['dark_magic_lv1_shadow_tendril'],
		'base_str': 28, 'base_dex': 48, 'base_con': 30, 'base_int': 65, 'base_hp': 2900, 'base_ap': 160,
		'str_per_level': 3, 'dex_per_level': 6, 'con_per_level': 3, 'int_per_level': 9,
		'resistances': ['dark', 'ice'], 'immunities': ['sleep'], 'weaknesses': ['light', 'fire']
	},
	{
		'id': 'fracture_sentinel', 'name': 'Fracture Sentinel', 'hostile_type': 'construct', 'min_spawn_level': 82, 'role': 'damage', 'rarity': 'superrare',
		'base_xp': 2200, 'common_drop': 'defibrillator', 'rare_drop': 'tome_con_superrare', 'money_range': (750, 1500),
		'basic_attack': 'reality cleave', 'strong_attack': 'structural collapse', 'player_abilities': [],
		'base_str': 58, 'base_dex': 38, 'base_con': 58, 'base_int': 30, 'base_hp': 6000, 'base_ap': 120,
		'str_per_level': 8, 'dex_per_level': 4, 'con_per_level': 8, 'int_per_level': 3,
		'resistances': ['physical', 'electric'], 'immunities': ['stun', 'petrify'], 'weaknesses': ['earth']
	}
]

DUNGEON_NPCS = [
	{'id': 'crux', 'location': 'final_chamber'}
]

BOSS_MOB = {
	'id': 'crux_origin_1',
	'name': 'Crux - Origin Form',
	'hostiles': ['crux_origin_1']
}

BOSS_HOSTILES = [
	{
		'id': 'crux_origin_1', 'name': 'Crux - Origin Form', 'hostile_type': 'aberration', 'min_spawn_level': 82, 'role': 'hazard', 'rarity': 'notfound',
		'base_xp': 40000, 'common_drop': 'tome_int_superrare', 'rare_drop': 'fracture_core', 'money_range': (6000, 12000),
		'basic_attack': 'paradox strike', 'strong_attack': 'void collapse',
		'player_abilities': ['impossibility_storm', 'debuff_the_wicked', 'glitch_cascade', 'static_erasure'],
		'base_str': 55, 'base_dex': 55, 'base_con': 60, 'base_int': 80, 'base_hp': 120000, 'base_ap': 1200,
		'str_per_level': 7, 'dex_per_level': 7, 'con_per_level': 8, 'int_per_level': 10,
		'resistances': ['dark', 'ice', 'electric'], 'immunities': ['confuse', 'sleep', 'stun'], 'weaknesses': ['light']
	}
]

DUNGEON_SETTINGS: Dict[str, Any] = {
	'dungeon_id': 'origin_spire',
	'seed': abs(hash('origin_spire')),
	'floor_count': 5,
	'room_size_min_max': (120, 200),
	'rooms_per_floor': 3,
	'max_neighbors_per_room': 2,
	'additional_connection_chance': 0.05,
	'min_max_distance_between_rooms': (3, 7),
	'min_max_corridor_width': (3, 6),
	'display_name': "Origin Spire",
	'open_area_tile': OPEN_AREA_TILE,
	'impassable_tile': IMPASSABLE_TILE,
	'open_area_color':  OPEN_AREA_COLOR,
	'impassable_color': IMPASSABLE_COLOR,
	'border_tile':      BORDER_TILE,
	'border_color':     BORDER_COLOR,
	'impassable_chance': IMPASSABLE_CHANCE,
	'floor_hostiles': FLOOR_HOSTILES,
	'hostile_seeds': HOSTILE_SEEDS,
	'npcs': [{'id': 'crux_origin_1', 'location': 'final_chamber'}],
	'items': [
		{'id': 'panacea', 'location': 'treasure_room'},
		{'id': 'defibrillator', 'location': 'treasure_room'},
		{'id': 'tome_hp_superrare', 'location': 'treasure_room'},
		{'id': 'stimulant_full', 'location': 'final_chamber'},
	],
	'boss_mob': BOSS_MOB,
	'boss_hostiles': BOSS_HOSTILES,
	'visible_distance': 8,
}
