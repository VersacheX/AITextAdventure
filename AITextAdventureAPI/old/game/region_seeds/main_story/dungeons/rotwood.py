"""
Rotwood - Chapter 19 Dungeon Seed Configuration
A rotting forest district of Aurelion Veil where living memory has been
replaced by looping false recollections. The deeper you go the less reliable
your own memories become. Contains forgotten_promises (Ch20 ingredient).
Boss: Twisted Darkwood -- the animate source of the false memory rot.
"""
from typing import Dict, Any

OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.18

FLOOR_HOSTILES = {
	1: ['false_memory_wisp', 'loop_shambler', 'rot_tendril', 'echo_guardian'],
}

HOSTILE_SEEDS = [
	{
		'id': 'false_memory_wisp', 'name': 'False Memory Wisp', 'hostile_type': 'spirit', 'min_spawn_level': 95, 'role': 'hazard', 'rarity': 'common',
		'base_xp': 1600, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (540, 1080),
		'basic_attack': 'distorted image', 'strong_attack': 'looping recall', 'player_abilities': ['dark_faith_lv1_shade_whisper'],
		'base_str': 30, 'base_dex': 48, 'base_con': 32, 'base_int': 65, 'base_hp': 3000, 'base_ap': 150,
		'str_per_level': 3, 'dex_per_level': 6, 'con_per_level': 3, 'int_per_level': 8,
		'resistances': ['dark', 'ice'], 'immunities': ['fear', 'sleep'], 'weaknesses': ['light', 'fire']
	},
	{
		'id': 'loop_shambler', 'name': 'Loop Shambler', 'hostile_type': 'undead', 'min_spawn_level': 95, 'role': 'damage', 'rarity': 'uncommon',
		'base_xp': 1750, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (580, 1160),
		'basic_attack': 'recursive strike', 'strong_attack': 'shambling repeat', 'player_abilities': [],
		'base_str': 52, 'base_dex': 35, 'base_con': 50, 'base_int': 22, 'base_hp': 4200, 'base_ap': 100,
		'str_per_level': 6, 'dex_per_level': 4, 'con_per_level': 6, 'int_per_level': 2,
		'resistances': ['dark', 'physical'], 'immunities': ['confuse'], 'weaknesses': ['light', 'fire']
	},
	{
		'id': 'rot_tendril', 'name': 'Rot Tendril', 'hostile_type': 'plant', 'min_spawn_level': 96, 'role': 'hazard', 'rarity': 'rare',
		'base_xp': 2100, 'common_drop': 'panacea', 'rare_drop': 'tome_int_superrare', 'money_range': (720, 1440),
		'basic_attack': 'rot lash', 'strong_attack': 'memory drain', 'player_abilities': ['dark_magic_lv1_shadow_tendril'],
		'base_str': 42, 'base_dex': 38, 'base_con': 55, 'base_int': 55, 'base_hp': 4500, 'base_ap': 135,
		'str_per_level': 5, 'dex_per_level': 4, 'con_per_level': 7, 'int_per_level': 7,
		'resistances': ['earth', 'dark'], 'immunities': ['poison'], 'weaknesses': ['fire', 'light']
	},
	{
		'id': 'echo_guardian', 'name': 'Echo Guardian', 'hostile_type': 'spirit', 'min_spawn_level': 97, 'role': 'damage', 'rarity': 'superrare',
		'base_xp': 2800, 'common_drop': 'defibrillator', 'rare_drop': 'tome_dex_superrare', 'money_range': (950, 1900),
		'basic_attack': 'phantom strike', 'strong_attack': 'echo collapse', 'player_abilities': ['dark_skill_lv1_creeping_strike'],
		'base_str': 58, 'base_dex': 68, 'base_con': 50, 'base_int': 48, 'base_hp': 6500, 'base_ap': 140,
		'str_per_level': 7, 'dex_per_level': 8, 'con_per_level': 6, 'int_per_level': 5,
		'resistances': ['dark', 'ice', 'physical'], 'immunities': ['stun', 'fear'], 'weaknesses': ['light']
	}
]

DUNGEON_NPCS = [
	{'id': 'twisted_darkwood', 'location': 'final_chamber'}
]

BOSS_MOB = {
	'id': 'twisted_darkwood_1',
	'name': 'Twisted Darkwood',
	'hostiles': ['twisted_darkwood_1']
}

BOSS_HOSTILES = [
	{
		'id': 'twisted_darkwood_1', 'name': 'Twisted Darkwood', 'hostile_type': 'plant', 'min_spawn_level': 97, 'role': 'hazard', 'rarity': 'notfound',
		'base_xp': 55000, 'common_drop': 'tome_int_superrare', 'rare_drop': 'rotwood_heartstone', 'money_range': (9000, 18000),
		'basic_attack': 'looping shame', 'strong_attack': 'false history', 'player_abilities': ['dark_faith_lv1_shade_whisper', 'dark_magic_lv1_shadow_tendril'],
		'base_str': 65, 'base_dex': 55, 'base_con': 80, 'base_int': 70, 'base_hp': 200000, 'base_ap': 1200,
		'str_per_level': 8, 'dex_per_level': 7, 'con_per_level': 10, 'int_per_level': 9,
		'resistances': ['dark', 'earth', 'physical'], 'immunities': ['poison', 'sleep', 'confuse'], 'weaknesses': ['fire', 'light']
	}
]

DUNGEON_SETTINGS: Dict[str, Any] = {
	'dungeon_id': 'rotwood',
	'seed': abs(hash('rotwood')),
	'floor_count': 1,
	'room_size_min_max': (120, 180),
	'rooms_per_floor': 8,
	'max_neighbors_per_room': 3,
	'additional_connection_chance': 0.1,
	'min_max_distance_between_rooms': (3, 7),
	'min_max_corridor_width': (3, 6),
	'display_name': "Rotwood",
	'open_area_tile': OPEN_AREA_TILE,
	'impassable_tile': IMPASSABLE_TILE,
	'impassable_chance': IMPASSABLE_CHANCE,
	'floor_hostiles': FLOOR_HOSTILES,
	'hostile_seeds': HOSTILE_SEEDS,
	'npcs': [{'id': 'twisted_darkwood_1', 'location': 'final_chamber'}],
	'items': [
		{'id': 'panacea', 'location': 'treasure_room'},
		{'id': 'panacea', 'location': 'treasure_room'},
		{'id': 'defibrillator', 'location': 'treasure_room'},
		{'id': 'tome_hp_superrare', 'location': 'treasure_room'},
		{'id': 'stimulant_full', 'location': 'final_chamber'},
	],
	'boss_mob': BOSS_MOB,
	'boss_hostiles': BOSS_HOSTILES,
	'visible_distance': 8,
}
