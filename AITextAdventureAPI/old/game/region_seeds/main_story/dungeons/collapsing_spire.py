"""
Collapsing Spire - Chapter 18 Dungeon Seed Configuration
A city-district tower undergoing methodical, geometrically precise self-destruction.
Its floors schedule their own collapse. Every room knows when it will fall.
Boss: Cataclysm -- a titan of living ordered collapse who sees existence as inefficiency.
"""
from typing import Dict, Any

OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = "#888078"
IMPASSABLE_COLOR = "#282420"
BORDER_TILE      = "·"
BORDER_COLOR     = "#585048"

FLOOR_HOSTILES = {
	1: ['order_fragment', 'efficiency_drone', 'scheduled_ruin', 'protocol_titan'],
}

HOSTILE_SEEDS = [
	{
		'id': 'order_fragment', 'name': 'Order Fragment', 'hostile_type': 'construct', 'min_spawn_level': 90, 'role': 'damage', 'rarity': 'common',
		'base_xp': 1500, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (520, 1040),
		'basic_attack': 'systematic strike', 'strong_attack': 'protocol cleave', 'player_abilities': [],
		'base_str': 48, 'base_dex': 40, 'base_con': 48, 'base_int': 35, 'base_hp': 3800, 'base_ap': 110,
		'str_per_level': 6, 'dex_per_level': 5, 'con_per_level': 6, 'int_per_level': 4,
		'resistances': ['physical', 'electric'], 'immunities': ['confuse'], 'weaknesses': ['fire']
	},
	{
		'id': 'efficiency_drone', 'name': 'Efficiency Drone', 'hostile_type': 'construct', 'min_spawn_level': 90, 'role': 'hazard', 'rarity': 'uncommon',
		'base_xp': 1650, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (560, 1120),
		'basic_attack': 'audit pulse', 'strong_attack': 'waste elimination', 'player_abilities': ['light_spirit_lv1_convert'],
		'base_str': 35, 'base_dex': 52, 'base_con': 40, 'base_int': 58, 'base_hp': 3400, 'base_ap': 140,
		'str_per_level': 4, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 7,
		'resistances': ['electric', 'air'], 'immunities': ['sleep'], 'weaknesses': ['dark']
	},
	{
		'id': 'scheduled_ruin', 'name': 'Scheduled Ruin', 'hostile_type': 'aberration', 'min_spawn_level': 91, 'role': 'damage', 'rarity': 'rare',
		'base_xp': 2000, 'common_drop': 'panacea', 'rare_drop': 'tome_con_superrare', 'money_range': (700, 1400),
		'basic_attack': 'collapse strike', 'strong_attack': 'decommission wave', 'player_abilities': [],
		'base_str': 62, 'base_dex': 38, 'base_con': 60, 'base_int': 25, 'base_hp': 5500, 'base_ap': 105,
		'str_per_level': 8, 'dex_per_level': 4, 'con_per_level': 8, 'int_per_level': 3,
		'resistances': ['physical', 'earth'], 'immunities': ['stun'], 'weaknesses': ['electric']
	},
	{
		'id': 'protocol_titan', 'name': 'Protocol Titan', 'hostile_type': 'construct', 'min_spawn_level': 92, 'role': 'damage', 'rarity': 'superrare',
		'base_xp': 2700, 'common_drop': 'defibrillator', 'rare_drop': 'tome_str_superrare', 'money_range': (900, 1800),
		'basic_attack': 'mandatory destruction', 'strong_attack': 'final verdict', 'player_abilities': ['earth_technique_lv1_armor_up'],
		'base_str': 78, 'base_dex': 28, 'base_con': 75, 'base_int': 18, 'base_hp': 9000, 'base_ap': 115,
		'str_per_level': 10, 'dex_per_level': 3, 'con_per_level': 10, 'int_per_level': 2,
		'resistances': ['physical', 'fire', 'electric', 'earth'], 'immunities': ['stun', 'petrify'], 'weaknesses': []
	}
]

DUNGEON_NPCS = [
	{'id': 'cataclysm', 'location': 'final_chamber'}
]

BOSS_MOB = {
	'id': 'cataclysm_1',
	'name': 'Cataclysm',
	'hostiles': ['cataclysm_1']
}

BOSS_HOSTILES = [
	{
		'id': 'cataclysm_1', 'name': 'Cataclysm', 'hostile_type': 'construct', 'min_spawn_level': 92, 'role': 'damage', 'rarity': 'notfound',
		'base_xp': 50000, 'common_drop': 'tome_con_superrare', 'rare_drop': 'defibrillator', 'money_range': (8000, 16000),
		'basic_attack': 'inevitable strike', 'strong_attack': 'scheduled annihilation',
		'player_abilities': ['absolute_destruction', 'calamity', 'eternal_nerve', 'scheduled_obliteration'],
		'base_str': 85, 'base_dex': 40, 'base_con': 90, 'base_int': 60, 'base_hp': 180000, 'base_ap': 1000,
		'str_per_level': 11, 'dex_per_level': 5, 'con_per_level': 11, 'int_per_level': 7,
		'resistances': ['physical', 'fire', 'electric', 'earth', 'ice'], 'immunities': ['stun', 'petrify', 'confuse', 'sleep'], 'weaknesses': ['dark']
	}
]

DUNGEON_SETTINGS: Dict[str, Any] = {
	'dungeon_id': 'collapsing_spire',
	'seed': abs(hash('collapsing_spire')),
	'floor_count': 4,
	'room_size_min_max': (150, 250),
	'rooms_per_floor': 3,
	'max_neighbors_per_room': 3,
	'additional_connection_chance': 0.08,
	'min_max_distance_between_rooms': (4, 9),
	'min_max_corridor_width': (4, 8),
	'display_name': "Collapsing Spire",
	'open_area_tile': OPEN_AREA_TILE,
	'impassable_tile': IMPASSABLE_TILE,
	'open_area_color':  OPEN_AREA_COLOR,
	'impassable_color': IMPASSABLE_COLOR,
	'border_tile':      BORDER_TILE,
	'border_color':     BORDER_COLOR,
	'impassable_chance': IMPASSABLE_CHANCE,
	'floor_hostiles': FLOOR_HOSTILES,
	'hostile_seeds': HOSTILE_SEEDS,
	'npcs': [{'id': 'cataclysm_1', 'location': 'final_chamber'}],
	'items': [
		{'id': 'panacea', 'location': 'treasure_room'},
		{'id': 'panacea', 'location': 'treasure_room'},
		{'id': 'defibrillator', 'location': 'treasure_room'},
		{'id': 'tome_hp_superrare', 'location': 'treasure_room'},
		{'id': 'stimulant_full', 'location': 'final_chamber'},
	],
	'boss_mob': BOSS_MOB,
	'boss_hostiles': BOSS_HOSTILES,
	'visible_distance': 10,
}
