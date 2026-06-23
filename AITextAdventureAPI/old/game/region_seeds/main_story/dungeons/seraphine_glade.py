"""
Seraphine Glade - Chapter 19 Dungeon Seed Configuration
A small, impossibly warm clearing in the rotwood held in stasis by Seraphine's
unbroken song. The harmony makes it beautiful and deeply unsettling. It exists
just outside normal time -- nothing decays here, nothing changes.
Contains two harmony_echo items needed for Seraphine's arc.
No boss -- short exploration and treasure dungeon.
"""
from typing import Dict, Any

OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.06

FLOOR_HOSTILES = {
	1: ['hollow_harmony', 'stasis_wisp', 'preserved_wraith', 'perfect_echo'],
}

HOSTILE_SEEDS = [
	{
		'id': 'hollow_harmony', 'name': 'Hollow Harmony', 'hostile_type': 'spirit', 'min_spawn_level': 95, 'role': 'hazard', 'rarity': 'common',
		'base_xp': 1600, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (540, 1080),
		'basic_attack': 'empty melody', 'strong_attack': 'false comfort', 'player_abilities': ['light_faith_lv1_convert'],
		'base_str': 28, 'base_dex': 50, 'base_con': 30, 'base_int': 68, 'base_hp': 2800, 'base_ap': 160,
		'str_per_level': 3, 'dex_per_level': 6, 'con_per_level': 3, 'int_per_level': 8,
		'resistances': ['light', 'air'], 'immunities': ['sleep'], 'weaknesses': ['dark']
	},
	{
		'id': 'stasis_wisp', 'name': 'Stasis Wisp', 'hostile_type': 'spirit', 'min_spawn_level': 95, 'role': 'hazard', 'rarity': 'uncommon',
		'base_xp': 1750, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (580, 1160),
		'basic_attack': 'freeze moment', 'strong_attack': 'permanent now', 'player_abilities': [],
		'base_str': 25, 'base_dex': 55, 'base_con': 28, 'base_int': 72, 'base_hp': 2600, 'base_ap': 170,
		'str_per_level': 3, 'dex_per_level': 7, 'con_per_level': 3, 'int_per_level': 9,
		'resistances': ['light', 'ice'], 'immunities': ['confuse', 'fear'], 'weaknesses': ['fire']
	},
	{
		'id': 'preserved_wraith', 'name': 'Preserved Wraith', 'hostile_type': 'undead', 'min_spawn_level': 96, 'role': 'damage', 'rarity': 'rare',
		'base_xp': 2100, 'common_drop': 'panacea', 'rare_drop': 'tome_int_superrare', 'money_range': (720, 1440),
		'basic_attack': 'pristine strike', 'strong_attack': 'unchanging pain', 'player_abilities': ['dark_magic_lv1_shadow_tendril'],
		'base_str': 45, 'base_dex': 50, 'base_con': 40, 'base_int': 58, 'base_hp': 4000, 'base_ap': 145,
		'str_per_level': 5, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 7,
		'resistances': ['light', 'dark'], 'immunities': ['sleep'], 'weaknesses': ['fire']
	},
	{
		'id': 'perfect_echo', 'name': 'Perfect Echo', 'hostile_type': 'aberration', 'min_spawn_level': 97, 'role': 'hazard', 'rarity': 'superrare',
		'base_xp': 2800, 'common_drop': 'defibrillator', 'rare_drop': 'tome_dex_superrare', 'money_range': (950, 1900),
		'basic_attack': 'mirror strike', 'strong_attack': 'infinite refrain', 'player_abilities': ['light_faith_lv1_convert'],
		'base_str': 42, 'base_dex': 65, 'base_con': 42, 'base_int': 65, 'base_hp': 5000, 'base_ap': 180,
		'str_per_level': 5, 'dex_per_level': 8, 'con_per_level': 5, 'int_per_level': 8,
		'resistances': ['light', 'air', 'ice'], 'immunities': ['fear', 'confuse'], 'weaknesses': ['dark', 'fire']
	}
]

DUNGEON_NPCS = []
BOSS_MOB = None
BOSS_HOSTILES = []

DUNGEON_SETTINGS: Dict[str, Any] = {
	'dungeon_id': 'seraphine_glade',
	'seed': abs(hash('seraphine_glade')),
	'floor_count': 1,
	'room_size_min_max': (60, 100),
	'rooms_per_floor': 6,
	'max_neighbors_per_room': 2,
	'additional_connection_chance': 0.0,
	'min_max_distance_between_rooms': (1, 4),
	'min_max_corridor_width': (2, 4),
	'display_name': "Seraphine's Glade",
	'open_area_tile': OPEN_AREA_TILE,
	'impassable_tile': IMPASSABLE_TILE,
	'impassable_chance': IMPASSABLE_CHANCE,
	'floor_hostiles': FLOOR_HOSTILES,
	'hostile_seeds': HOSTILE_SEEDS,
	'npcs': [],
	'items': [
		{'id': 'panacea', 'location': 'treasure_room'},
		{'id': 'defibrillator', 'location': 'treasure_room'},
		{'id': 'tome_int_superrare', 'location': 'final_chamber'},
	],
	'boss_mob': BOSS_MOB,
	'boss_hostiles': BOSS_HOSTILES,
	'visible_distance': 6,
}
