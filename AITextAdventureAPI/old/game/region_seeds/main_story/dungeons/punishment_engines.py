"""
Punishment Engines - Chapter 17 Dungeon Seed Configuration
A dimension-spanning machine designed to enforce the logical impossibility of free will.
Its architecture generates contradictions. Every corridor leads to where you already are.
Boss: Paradox and Crux -- the twin Voidwalkers of contradiction and erasure.
"""
from typing import Dict, Any

OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.08
OPEN_AREA_COLOR  = "#3a7a7a"
IMPASSABLE_COLOR = "#101e1e"
BORDER_TILE      = "░"
BORDER_COLOR     = "#285858"

FLOOR_HOSTILES = {
	1: ['contradiction_drone', 'logic_enforcer', 'paradox_hound', 'impossibility_engine'],
}

HOSTILE_SEEDS = [
	{
		'id': 'contradiction_drone', 'name': 'Contradiction Drone', 'hostile_type': 'construct', 'min_spawn_level': 85, 'role': 'hazard', 'rarity': 'common',
		'base_xp': 1400, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (500, 1000),
		'basic_attack': 'false positive', 'strong_attack': 'logical inversion', 'player_abilities': [],
		'base_str': 38, 'base_dex': 42, 'base_con': 38, 'base_int': 50, 'base_hp': 3200, 'base_ap': 120,
		'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 6,
		'resistances': ['electric'], 'immunities': ['confuse'], 'weaknesses': ['dark']
	},
	{
		'id': 'logic_enforcer', 'name': 'Logic Enforcer', 'hostile_type': 'construct', 'min_spawn_level': 85, 'role': 'damage', 'rarity': 'uncommon',
		'base_xp': 1550, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (540, 1080),
		'basic_attack': 'axiom smash', 'strong_attack': 'determinism strike', 'player_abilities': ['earth_technique_lv1_armor_up'],
		'base_str': 50, 'base_dex': 38, 'base_con': 50, 'base_int': 30, 'base_hp': 4000, 'base_ap': 105,
		'str_per_level': 6, 'dex_per_level': 4, 'con_per_level': 6, 'int_per_level': 3,
		'resistances': ['physical', 'electric'], 'immunities': ['stun'], 'weaknesses': ['fire']
	},
	{
		'id': 'paradox_hound', 'name': 'Paradox Hound', 'hostile_type': 'beast', 'min_spawn_level': 86, 'role': 'damage', 'rarity': 'rare',
		'base_xp': 1900, 'common_drop': 'panacea', 'rare_drop': 'tome_dex_superrare', 'money_range': (660, 1320),
		'basic_attack': 'blink bite', 'strong_attack': 'recursive lunge', 'player_abilities': [],
		'base_str': 52, 'base_dex': 65, 'base_con': 42, 'base_int': 22, 'base_hp': 4200, 'base_ap': 115,
		'str_per_level': 6, 'dex_per_level': 8, 'con_per_level': 5, 'int_per_level': 2,
		'resistances': ['ice', 'dark'], 'immunities': ['fear'], 'weaknesses': ['light']
	},
	{
		'id': 'impossibility_engine', 'name': 'Impossibility Engine', 'hostile_type': 'construct', 'min_spawn_level': 87, 'role': 'hazard', 'rarity': 'superrare',
		'base_xp': 2500, 'common_drop': 'defibrillator', 'rare_drop': 'tome_int_superrare', 'money_range': (820, 1640),
		'basic_attack': 'null field', 'strong_attack': 'paradox cascade', 'player_abilities': ['dark_magic_lv1_shadow_tendril'],
		'base_str': 40, 'base_dex': 48, 'base_con': 45, 'base_int': 70, 'base_hp': 5500, 'base_ap': 180,
		'str_per_level': 5, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 9,
		'resistances': ['dark', 'ice', 'electric'], 'immunities': ['sleep', 'confuse'], 'weaknesses': ['fire', 'light']
	}
]

DUNGEON_NPCS = [
	{'id': 'paradox', 'location': 'final_chamber'}
]

BOSS_MOB = {
	'id': 'paradox_crux_1',
	'name': 'Paradox and Crux',
	'hostiles': ['paradox_boss', 'crux_boss']
}

BOSS_HOSTILES = [
	{
		'id': 'paradox_boss', 'name': 'Paradox', 'hostile_type': 'aberration', 'min_spawn_level': 87, 'role': 'hazard', 'rarity': 'notfound',
		'base_xp': 35000, 'common_drop': 'tome_int_superrare', 'rare_drop': 'sovereign_emblem', 'money_range': (7000, 14000),
		'basic_attack': 'reality fracture', 'strong_attack': 'existential collapse',
		'player_abilities': ['demonic_fury', 'infuriating_revelation', 'they_arent_who_you_are', 'paradox_touch'],
		'base_str': 55, 'base_dex': 60, 'base_con': 55, 'base_int': 90, 'base_hp': 110000, 'base_ap': 1300,
		'str_per_level': 7, 'dex_per_level': 7, 'con_per_level': 7, 'int_per_level': 11,
		'resistances': ['dark', 'electric', 'ice'], 'immunities': ['confuse', 'fear', 'sleep'], 'weaknesses': ['light']
	},
	{
		'id': 'crux_boss', 'name': 'Crux', 'hostile_type': 'aberration', 'min_spawn_level': 87, 'role': 'damage', 'rarity': 'notfound',
		'base_xp': 35000, 'common_drop': 'tome_con_superrare', 'rare_drop': 'sovereign_emblem', 'money_range': (7000, 14000),
		'basic_attack': 'logic erasure', 'strong_attack': 'structural collapse', 'player_abilities': ['impossibility_storm', 'debuff_the_wicked', 'structural_paradox', 'logic_collapse'],
		'base_str': 65, 'base_dex': 55, 'base_con': 65, 'base_int': 75, 'base_hp': 130000, 'base_ap': 1100,
		'str_per_level': 8, 'dex_per_level': 7, 'con_per_level': 8, 'int_per_level': 9,
		'resistances': ['dark', 'physical', 'ice'], 'immunities': ['stun', 'petrify', 'confuse'], 'weaknesses': ['light', 'fire']
	}
]

DUNGEON_SETTINGS: Dict[str, Any] = {
	'dungeon_id': 'punishment_engines',
	'seed': abs(hash('punishment_engines')),
	'floor_count': 1,
	'room_size_min_max': (130, 220),
	'rooms_per_floor': 8,
	'max_neighbors_per_room': 3,
	'additional_connection_chance': 0.1,
	'min_max_distance_between_rooms': (3, 8),
	'min_max_corridor_width': (3, 7),
	'display_name': "Punishment Engines",
	'open_area_tile': OPEN_AREA_TILE,
	'impassable_tile': IMPASSABLE_TILE,
	'open_area_color':  OPEN_AREA_COLOR,
	'impassable_color': IMPASSABLE_COLOR,
	'border_tile':      BORDER_TILE,
	'border_color':     BORDER_COLOR,
	'impassable_chance': IMPASSABLE_CHANCE,
	'floor_hostiles': FLOOR_HOSTILES,
	'hostile_seeds': HOSTILE_SEEDS,
	'npcs': [{'id': 'paradox_crux_1', 'location': 'final_chamber'}],
	'items': [
		{'id': 'panacea', 'location': 'treasure_room'},
		{'id': 'panacea', 'location': 'treasure_room'},
		{'id': 'defibrillator', 'location': 'treasure_room'},
		{'id': 'tome_hp_superrare', 'location': 'treasure_room'},
		{'id': 'stimulant_full', 'location': 'final_chamber'},
	],
	'boss_mob': BOSS_MOB,
	'boss_hostiles': BOSS_HOSTILES,
	'visible_distance': 9,
}
