"""
Memory Museum - Chapter 20 Dungeon Seed Configuration
An impossibly vast archive where every wound, failure, and loss in history
is preserved under glass and kept pristine forever. The museum is never closed.
Nothing here is allowed to heal. Its halls are beautiful and absolutely suffocating.
Boss Round 1: Oracle and Reliquary (oracle_reliquary_1)
Boss Round 2: Oracle and Reliquary -- reality reset version (oracle_reliquary_2)
"""
from typing import Dict, Any

OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.08

FLOOR_HOSTILES = {
	1: ['preserved_horror', 'archival_specter', 'prophecy_shard', 'eternal_curator'],
}

HOSTILE_SEEDS = [
	{
		'id': 'preserved_horror', 'name': 'Preserved Horror', 'hostile_type': 'undead', 'min_spawn_level': 100, 'role': 'hazard', 'rarity': 'common',
		'base_xp': 1800, 'common_drop': 'herb_major', 'rare_drop': None, 'money_range': (600, 1200),
		'basic_attack': 'pristine pain', 'strong_attack': 'perfect preservation', 'player_abilities': ['dark_faith_lv1_shade_whisper'],
		'base_str': 38, 'base_dex': 45, 'base_con': 40, 'base_int': 65, 'base_hp': 3500, 'base_ap': 150,
		'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 8,
		'resistances': ['dark', 'ice'], 'immunities': ['fear', 'sleep'], 'weaknesses': ['light', 'fire']
	},
	{
		'id': 'archival_specter', 'name': 'Archival Specter', 'hostile_type': 'spirit', 'min_spawn_level': 100, 'role': 'damage', 'rarity': 'uncommon',
		'base_xp': 2000, 'common_drop': 'stimulant_large', 'rare_drop': None, 'money_range': (650, 1300),
		'basic_attack': 'recorded strike', 'strong_attack': 'historical wound', 'player_abilities': [],
		'base_str': 50, 'base_dex': 52, 'base_con': 45, 'base_int': 55, 'base_hp': 4200, 'base_ap': 140,
		'str_per_level': 6, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 7,
		'resistances': ['dark', 'physical'], 'immunities': ['confuse'], 'weaknesses': ['light']
	},
	{
		'id': 'prophecy_shard', 'name': 'Prophecy Shard', 'hostile_type': 'aberration', 'min_spawn_level': 101, 'role': 'hazard', 'rarity': 'rare',
		'base_xp': 2400, 'common_drop': 'panacea', 'rare_drop': 'tome_int_superrare', 'money_range': (800, 1600),
		'basic_attack': 'fated blow', 'strong_attack': 'inevitable collapse', 'player_abilities': ['dark_magic_lv1_shadow_tendril'],
		'base_str': 35, 'base_dex': 55, 'base_con': 38, 'base_int': 78, 'base_hp': 3800, 'base_ap': 180,
		'str_per_level': 4, 'dex_per_level': 7, 'con_per_level': 4, 'int_per_level': 10,
		'resistances': ['dark', 'electric', 'ice'], 'immunities': ['sleep', 'confuse'], 'weaknesses': ['light', 'fire']
	},
	{
		'id': 'eternal_curator', 'name': 'Eternal Curator', 'hostile_type': 'construct', 'min_spawn_level': 102, 'role': 'damage', 'rarity': 'superrare',
		'base_xp': 3200, 'common_drop': 'defibrillator', 'rare_drop': 'tome_con_superrare', 'money_range': (1000, 2000),
		'basic_attack': 'classification strike', 'strong_attack': 'final indexing', 'player_abilities': ['earth_technique_lv1_armor_up'],
		'base_str': 68, 'base_dex': 45, 'base_con': 72, 'base_int': 50, 'base_hp': 9000, 'base_ap': 140,
		'str_per_level': 8, 'dex_per_level': 5, 'con_per_level': 9, 'int_per_level': 6,
		'resistances': ['physical', 'dark', 'ice'], 'immunities': ['stun', 'petrify', 'fear'], 'weaknesses': ['fire']
	}
]

DUNGEON_NPCS = [
	{'id': 'oracle_reliquary_1', 'location': 'final_chamber'}
]

BOSS_MOB = {
	'id': 'oracle_reliquary_1',
	'name': 'Oracle and Reliquary',
	'hostiles': ['oracle_boss_1', 'reliquary_boss_1']
}

BOSS_HOSTILES = [
	{
		'id': 'oracle_boss_1', 'name': 'Oracle', 'hostile_type': 'aberration', 'min_spawn_level': 102, 'role': 'hazard', 'rarity': 'notfound',
		'base_xp': 40000, 'common_drop': 'tome_int_superrare', 'rare_drop': 'prophecy_remnant', 'money_range': (10000, 20000),
		'basic_attack': 'written verdict', 'strong_attack': 'prophetic collapse', 'player_abilities': ['inescapable_prophecy', 'vision_of_ruin', 'fate_lock'],
		'base_str': 55, 'base_dex': 65, 'base_con': 58, 'base_int': 100, 'base_hp': 150000, 'base_ap': 1500,
		'str_per_level': 6, 'dex_per_level': 8, 'con_per_level': 7, 'int_per_level': 12,
		'resistances': ['dark', 'ice', 'electric'], 'immunities': ['fear', 'confuse', 'sleep'], 'weaknesses': ['light', 'fire']
	},
	{
		'id': 'reliquary_boss_1', 'name': 'Reliquary', 'hostile_type': 'aberration', 'min_spawn_level': 102, 'role': 'hazard', 'rarity': 'notfound',
		'base_xp': 40000, 'common_drop': 'tome_con_superrare', 'rare_drop': 'archive_shard', 'money_range': (10000, 20000),
		'basic_attack': 'preserved anguish', 'strong_attack': 'permanent collection', 'player_abilities': ['eternal_wound', 'memory_of_suffering', 'burden_of_the_lost'],
		'base_str': 58, 'base_dex': 55, 'base_con': 72, 'base_int': 85, 'base_hp': 160000, 'base_ap': 1300,
		'str_per_level': 7, 'dex_per_level': 6, 'con_per_level': 9, 'int_per_level': 10,
		'resistances': ['dark', 'physical', 'ice'], 'immunities': ['stun', 'petrify', 'confuse'], 'weaknesses': ['light', 'fire']
	}
]

DUNGEON_SETTINGS: Dict[str, Any] = {
	'dungeon_id': 'memory_museum',
	'seed': abs(hash('memory_museum')),
	'floor_count': 1,
	'room_size_min_max': (160, 260),
	'rooms_per_floor': 10,
	'max_neighbors_per_room': 4,
	'additional_connection_chance': 0.1,
	'min_max_distance_between_rooms': (5, 10),
	'min_max_corridor_width': (4, 8),
	'display_name': "Memory Museum",
	'open_area_tile': OPEN_AREA_TILE,
	'impassable_tile': IMPASSABLE_TILE,
	'impassable_chance': IMPASSABLE_CHANCE,
	'floor_hostiles': FLOOR_HOSTILES,
	'hostile_seeds': HOSTILE_SEEDS,
	'npcs': [{'id': 'oracle_reliquary_1', 'location': 'final_chamber'}],
	'items': [
		{'id': 'panacea', 'location': 'treasure_room'},
		{'id': 'panacea', 'location': 'treasure_room'},
		{'id': 'defibrillator', 'location': 'treasure_room'},
		{'id': 'defibrillator', 'location': 'treasure_room'},
		{'id': 'tome_hp_superrare', 'location': 'treasure_room'},
		{'id': 'stimulant_full', 'location': 'final_chamber'},
	],
	'boss_mob': BOSS_MOB,
	'boss_hostiles': BOSS_HOSTILES,
	'visible_distance': 10,
}
