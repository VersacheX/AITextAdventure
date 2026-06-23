"""
Temporal Echoes - Chapter 16 Dungeon Seed Configuration
A shattered ruin suspended between fractured moments of time.
Contains the fracture_logs (story item) and is revisited in Chapter 20
for dream_essence ingredients.
No boss -- exploration and treasure dungeon.
"""
from typing import Dict, Any

OPEN_AREA_TILE = " "
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.15

FLOOR_HOSTILES = {
	1: ['void_echo', 'temporal_rift', 'memory_fragment', 'time_wraith'],
}

HOSTILE_SEEDS = [
	{
		'id': 'void_echo', 'name': 'Void Echo', 'hostile_type': 'aberration', 'min_spawn_level': 80, 'role': 'hazard', 'rarity': 'common',
		'base_xp': 1200, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (450, 900),
		'basic_attack': 'hollow resonance', 'strong_attack': 'emptiness wave', 'player_abilities': ['dark_faith_lv1_shade_whisper'],
		'base_str': 35, 'base_dex': 40, 'base_con': 35, 'base_int': 45, 'base_hp': 3000, 'base_ap': 110,
		'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 6,
		'resistances': ['dark'], 'immunities': ['fear'], 'weaknesses': ['light']
	},
	{
		'id': 'temporal_rift', 'name': 'Temporal Rift', 'hostile_type': 'aberration', 'min_spawn_level': 80, 'role': 'damage', 'rarity': 'uncommon',
		'base_xp': 1350, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (500, 1000),
		'basic_attack': 'time fracture', 'strong_attack': 'causality tear', 'player_abilities': [],
		'base_str': 40, 'base_dex': 35, 'base_con': 38, 'base_int': 50, 'base_hp': 3200, 'base_ap': 120,
		'str_per_level': 5, 'dex_per_level': 4, 'con_per_level': 4, 'int_per_level': 7,
		'resistances': ['ice', 'dark'], 'immunities': ['confuse'], 'weaknesses': ['fire']
	},
	{
		'id': 'memory_fragment', 'name': 'Memory Fragment', 'hostile_type': 'spirit', 'min_spawn_level': 81, 'role': 'hazard', 'rarity': 'rare',
		'base_xp': 1600, 'common_drop': 'panacea', 'rare_drop': 'tome_int_superrare', 'money_range': (600, 1200),
		'basic_attack': 'false recollection', 'strong_attack': 'recursive nightmare', 'player_abilities': ['dark_magic_lv1_shadow_tendril'],
		'base_str': 30, 'base_dex': 42, 'base_con': 32, 'base_int': 60, 'base_hp': 2800, 'base_ap': 150,
		'str_per_level': 3, 'dex_per_level': 5, 'con_per_level': 3, 'int_per_level': 8,
		'resistances': ['dark', 'ice'], 'immunities': ['sleep'], 'weaknesses': ['light', 'fire']
	},
	{
		'id': 'time_wraith', 'name': 'Time Wraith', 'hostile_type': 'undead', 'min_spawn_level': 82, 'role': 'damage', 'rarity': 'superrare',
		'base_xp': 2000, 'common_drop': 'defibrillator', 'rare_drop': 'tome_dex_superrare', 'money_range': (700, 1400),
		'basic_attack': 'chrono strike', 'strong_attack': 'temporal devour', 'player_abilities': ['dark_skill_lv1_creeping_strike'],
		'base_str': 50, 'base_dex': 55, 'base_con': 42, 'base_int': 45, 'base_hp': 5000, 'base_ap': 130,
		'str_per_level': 6, 'dex_per_level': 7, 'con_per_level': 5, 'int_per_level': 5,
		'resistances': ['dark', 'physical'], 'immunities': ['stun', 'petrify'], 'weaknesses': ['light']
	}
]

DUNGEON_NPCS = []
BOSS_MOB = None
BOSS_HOSTILES = []

DUNGEON_SETTINGS: Dict[str, Any] = {
	'dungeon_id': 'temporal_echoes',
	'seed': abs(hash('temporal_echoes')),
	'floor_count': 1,
	'room_size_min_max': (80, 140),
	'rooms_per_floor': 7,
	'max_neighbors_per_room': 2,
	'additional_connection_chance': 0.05,
	'min_max_distance_between_rooms': (2, 5),
	'min_max_corridor_width': (2, 5),
	'display_name': "Temporal Echoes",
	'open_area_tile': OPEN_AREA_TILE,
	'impassable_tile': IMPASSABLE_TILE,
	'impassable_chance': IMPASSABLE_CHANCE,
	'floor_hostiles': FLOOR_HOSTILES,
	'hostile_seeds': HOSTILE_SEEDS,
	'npcs': [],
	'items': [
		{'id': 'panacea', 'location': 'treasure_room'},
		{'id': 'panacea', 'location': 'treasure_room'},
		{'id': 'defibrillator', 'location': 'treasure_room'},
		{'id': 'tome_int_superrare', 'location': 'final_chamber'},
	],
	'boss_mob': BOSS_MOB,
	'boss_hostiles': BOSS_HOSTILES,
	'visible_distance': 7,
}
