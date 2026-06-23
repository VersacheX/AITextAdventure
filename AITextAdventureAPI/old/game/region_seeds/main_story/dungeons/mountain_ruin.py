"""
Mountain Ruin - Chapter 17 Dungeon Seed Configuration
An ancient ruin half-buried in a mountain range where time has become non-linear.
The walls phase between states. The very structure exists in two timelines at once.
Boss: Displacer Gargantuan -- a creature that is simultaneously alive and already dead.
"""
from typing import Dict, Any

OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.1

FLOOR_HOSTILES = {
	1: ['phase_crawler', 'paradox_stalker', 'displaced_construct', 'ruin_colossus'],
}

HOSTILE_SEEDS = [
	{
		'id': 'phase_crawler', 'name': 'Phase Crawler', 'hostile_type': 'beast', 'min_spawn_level': 85, 'role': 'damage', 'rarity': 'common',
		'base_xp': 1400, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (480, 960),
		'basic_attack': 'phasing lunge', 'strong_attack': 'double strike', 'player_abilities': [],
		'base_str': 48, 'base_dex': 50, 'base_con': 42, 'base_int': 20, 'base_hp': 3600, 'base_ap': 100,
		'str_per_level': 6, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 2,
		'resistances': ['physical'], 'immunities': [], 'weaknesses': ['electric']
	},
	{
		'id': 'paradox_stalker', 'name': 'Paradox Stalker', 'hostile_type': 'aberration', 'min_spawn_level': 85, 'role': 'hazard', 'rarity': 'uncommon',
		'base_xp': 1550, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (530, 1060),
		'basic_attack': 'displacement field', 'strong_attack': 'temporal ambush', 'player_abilities': ['dark_skill_lv1_creeping_strike'],
		'base_str': 40, 'base_dex': 55, 'base_con': 38, 'base_int': 45, 'base_hp': 3400, 'base_ap': 125,
		'str_per_level': 5, 'dex_per_level': 7, 'con_per_level': 4, 'int_per_level': 5,
		'resistances': ['ice', 'dark'], 'immunities': ['confuse'], 'weaknesses': ['fire']
	},
	{
		'id': 'displaced_construct', 'name': 'Displaced Construct', 'hostile_type': 'construct', 'min_spawn_level': 86, 'role': 'damage', 'rarity': 'rare',
		'base_xp': 1800, 'common_drop': 'panacea', 'rare_drop': 'tome_str_superrare', 'money_range': (650, 1300),
		'basic_attack': 'ruin smash', 'strong_attack': 'blink charge', 'player_abilities': [],
		'base_str': 60, 'base_dex': 35, 'base_con': 55, 'base_int': 18, 'base_hp': 5000, 'base_ap': 100,
		'str_per_level': 8, 'dex_per_level': 4, 'con_per_level': 7, 'int_per_level': 2,
		'resistances': ['physical', 'earth'], 'immunities': ['stun'], 'weaknesses': ['electric']
	},
	{
		'id': 'ruin_colossus', 'name': 'Ruin Colossus', 'hostile_type': 'construct', 'min_spawn_level': 87, 'role': 'damage', 'rarity': 'superrare',
		'base_xp': 2400, 'common_drop': 'defibrillator', 'rare_drop': 'tome_con_superrare', 'money_range': (800, 1600),
		'basic_attack': 'boulder crush', 'strong_attack': 'seismic collapse', 'player_abilities': ['earth_technique_lv1_armor_up'],
		'base_str': 72, 'base_dex': 22, 'base_con': 72, 'base_int': 10, 'base_hp': 8000, 'base_ap': 110,
		'str_per_level': 10, 'dex_per_level': 2, 'con_per_level': 10, 'int_per_level': 1,
		'resistances': ['physical', 'earth', 'fire'], 'immunities': ['stun', 'petrify', 'knockback'], 'weaknesses': ['electric']
	}
]

DUNGEON_NPCS = [
	{'id': 'displacer_gargantuan', 'location': 'final_chamber'}
]

BOSS_MOB = {
	'id': 'displacer_gargantuan_1',
	'name': 'Displacer Gargantuan',
	'hostiles': ['displacer_gargantuan_1']
}

BOSS_HOSTILES = [
	{
		'id': 'displacer_gargantuan_1', 'name': 'Displacer Gargantuan', 'hostile_type': 'beast', 'min_spawn_level': 87, 'role': 'damage', 'rarity': 'notfound',
		'base_xp': 45000, 'common_drop': 'tome_str_superrare', 'rare_drop': 'echofoil_nullglass', 'money_range': (7000, 14000),
		'basic_attack': 'paradox lunge', 'strong_attack': 'both-states strike', 'player_abilities': [],
		'base_str': 80, 'base_dex': 60, 'base_con': 80, 'base_int': 20, 'base_hp': 150000, 'base_ap': 900,
		'str_per_level': 10, 'dex_per_level': 7, 'con_per_level': 10, 'int_per_level': 2,
		'resistances': ['physical', 'ice', 'dark'], 'immunities': ['confuse', 'sleep', 'petrify'], 'weaknesses': ['electric', 'light']
	}
]

DUNGEON_SETTINGS: Dict[str, Any] = {
	'dungeon_id': 'mountain_ruin',
	'seed': abs(hash('mountain_ruin')),
	'floor_count': 1,
	'room_size_min_max': (100, 160),
	'rooms_per_floor': 6,
	'max_neighbors_per_room': 2,
	'additional_connection_chance': 0.05,
	'min_max_distance_between_rooms': (2, 6),
	'min_max_corridor_width': (3, 6),
	'display_name': "Mountain Ruin",
	'open_area_tile': OPEN_AREA_TILE,
	'impassable_tile': IMPASSABLE_TILE,
	'impassable_chance': IMPASSABLE_CHANCE,
	'floor_hostiles': FLOOR_HOSTILES,
	'hostile_seeds': HOSTILE_SEEDS,
	'npcs': [{'id': 'displacer_gargantuan_1', 'location': 'final_chamber'}],
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
