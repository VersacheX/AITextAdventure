"""Rokhuld's Deep Core Dungeon Seed Configuration"""

from typing import Dict, Any

# Tile constants for dungeon rendering and builder decisions
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.04   # rocky collapses, unstable tunnels

FLOOR_HOSTILES = {
    1: [
        'stone_grub',
        'fault_bat',
        'cave_tremorling',
        'obsidian_sentry',
        'rubble_golem',
        'corrupt_miner',
        'core_salamander'
    ]
}

HOSTILE_SEEDS = [  # all level 8–10, ~10 hostiles total
    # Floor 1 - Deep Core (rock creatures, unstable beasts, corrupted miners)
    {
        'id': 'stone_grub',
        'name': 'Stone Grub',
        'hostile_type': 'creature',
        'min_spawn_level': 18,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 20,
        'common_drop': 'herb_minor',
        'rare_drop': None,
        'money_range': (2, 12),
        'basic_attack': 'gnaw',
        'strong_attack': 'burrow strike',
        'player_abilities': [],
        'base_str': 4,
        'base_dex': 3,
        'base_con': 4,
        'base_int': 1,
        'base_hp': 28,
        'base_ap': 3,
        'str_per_level': 1,
        'dex_per_level': 1,
        'con_per_level': 2,
        'int_per_level': 0,
        'resistances': ['earth'],
        'immunities': [],
        'weaknesses': ['water']
    },
    {
        'id': 'fault_bat',
        'name': 'Fault Bat',
        'hostile_type': 'creature',
        'min_spawn_level': 19,
        'role': 'hazard',
        'rarity': 'common',
        'base_xp': 36,
        'common_drop': 'stimulant_small',
        'rare_drop': 'stimulant_large',
        'money_range': (6, 30),
        'basic_attack': 'sonic screech',
        'strong_attack': 'faultline echo',
        'player_abilities': ['fire_earth_skill_lv2_volcanic_pike'],
        'base_str': 3,
        'base_dex': 6,
        'base_con': 3,
        'base_int': 2,
        'base_hp': 32,
        'base_ap': 4,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 0,
        'resistances': [],
        'immunities': ['sleep'],
        'weaknesses': ['ice']
    },
    {
        'id': 'cave_tremorling',
        'name': 'Cave Tremorling',
        'hostile_type': 'creature',
        'min_spawn_level': 20,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 60,
        'common_drop': 'herb_med',
        'rare_drop': 'herb_major',
        'money_range': (10, 50),
        'basic_attack': 'rumble stomp',
        'strong_attack': 'mini-quake',
        'player_abilities': ['earth_dark_technique_lv2_dark_impact'],
        'base_str': 5,
        'base_dex': 4,
        'base_con': 6,
        'base_int': 2,
        'base_hp': 70,
        'base_ap': 5,
        'str_per_level': 2,
        'dex_per_level': 1,
        'con_per_level': 2,
        'int_per_level': 0,
        'resistances': ['earth'],
        'immunities': [],
        'weaknesses': ['air']
    },
    {
        'id': 'obsidian_sentry',
        'name': 'Obsidian Sentry',
        'hostile_type': 'construct',
        'min_spawn_level': 20,
        'role': 'damage',
        'rarity': 'uncommon',
        'base_xp': 120,
        'common_drop': 'herb_med',
        'rare_drop': 'herb_major',
        'money_range': (20, 90),
        'basic_attack': 'shard slash',
        'strong_attack': 'obsidian burst',
        'player_abilities': ['earth_technique_lv1_armor_up', 'fire_earth_technique_lv2_blaze_hammer'],
        'base_str': 6,
        'base_dex': 3,
        'base_con': 10,
        'base_int': 1,
        'base_hp': 160,
        'base_ap': 6,
        'str_per_level': 2,
        'dex_per_level': 0,
        'con_per_level': 3,
        'int_per_level': 0,
        'resistances': ['earth'],
        'immunities': ['continuous_damage'],
        'weaknesses': ['water']
    },
    {
        'id': 'rubble_golem',
        'name': 'Rubble Golem',
        'hostile_type': 'construct',
        'min_spawn_level': 22,
        'role': 'damage',
        'rarity': 'rare',
        'base_xp': 200,
        'common_drop': 'herb_med',
        'rare_drop': 'tome_con',
        'money_range': (30, 120),
        'basic_attack': 'boulder fist',
        'strong_attack': 'collapse slam',
        'player_abilities': ['earth_earth_technique_lv2_terra_slam'],
        'base_str': 8,
        'base_dex': 2,
        'base_con': 12,
        'base_int': 1,
        'base_hp': 200,
        'base_ap': 5,
        'str_per_level': 2,
        'dex_per_level': 0,
        'con_per_level': 3,
        'int_per_level': 0,
        'resistances': ['earth'],
        'immunities': ['continuous_damage'],
        'weaknesses': ['air']
    },
    {
        'id': 'corrupt_miner',
        'name': 'Corrupt Miner',
        'hostile_type': 'undead',
        'min_spawn_level': 18,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 24,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (4, 16),
        'basic_attack': 'pickaxe rake',
        'strong_attack': 'collapse shriek',
        'player_abilities': [],
        'base_str': 5,
        'base_dex': 3,
        'base_con': 4,
        'base_int': 1,
        'base_hp': 30,
        'base_ap': 3,
        'str_per_level': 2,
        'dex_per_level': 1,
        'con_per_level': 1,
        'int_per_level': 0,
        'resistances': ['earth'],
        'immunities': ['continuous_damage'],
        'weaknesses': ['light']
    },
    {
        'id': 'core_salamander',
        'name': 'Core Salamander',
        'hostile_type': 'creature',
        'min_spawn_level': 24,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 300,
        'common_drop': 'herb_major',
        'rare_drop': 'tome_str_superrare',
        'money_range': (50, 200),
        'basic_attack': 'magma spit',
        'strong_attack': 'core flare',
        'player_abilities': ['fire_earth_magic_lv2_magma_javelin', 'fire_technique_lv1_scorch_slash'],
        'base_str': 6,
        'base_dex': 7,
        'base_con': 6,
        'base_int': 9,
        'base_hp': 380,
        'base_ap': 6,
        'str_per_level': 3,
        'dex_per_level': 2,
        'con_per_level': 2,
        'int_per_level': 0,
        'resistances': ['fire', 'earth'],
        'immunities': ['continuous_damage'],
        'weaknesses': ['water']
    }
]

# final_chamber is a enum value that represents the furthest room from the start location in the dungeon
DUNGEON_NPCS = [ {'id': 'rokhuld','location': 'final_chamber'} ] #<- reference to npc which when interacted with triggers task event into boss fight
DUNGEON_ITEMS = [ {'id': 'herb_major', 'location': 'treasure_room'} ]

BOSS_MOB = { 'id': 'rokhuld_1',
             'name': 'Rokhuld the Core-Breaker',
             'hostiles': [
                'rokhuld_miner',
                'rokhuld_miner',
                'rokhuld_1']
            }

BOSS_HOSTILES = [
    {
        "id": "rokhuld_miner", "name": "Faultline Miner", "hostile_type": "melee", "role": "hazard",
        "min_spawn_level": 23, "rarity": "superrare", "base_xp": 480,
        "common_drop": "herb_major", "rare_drop": "tome_str", "money_range": (45,180),
        "basic_attack": "pickaxe swing", "strong_attack": "faultline crack",
        "player_abilities": ["fire_earth_technique_lv2_blaze_hammer", "earth_light_technique_lv2_rally_up"],
        "base_str": 12, "base_dex": 6, "base_con": 10, "base_int": 4,
        "base_hp": 1360, "base_ap": 10,
        "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 1
    },
    {
        "id": "rokhuld_1", "name": "Rokhuld the Core-Breaker", "hostile_type": "melee", "role": "boss",
        "min_spawn_level": 30, "rarity": "notfound", "base_xp": 1200,
        "common_drop": "herb_major", "rare_drop": "tome_str", "money_range": (100,300),
        "basic_attack": "core smash", "strong_attack": "seismic hammer",
        "player_abilities": ["fire_earth_technique_lv2_blaze_hammer", "fire_fire_technique_lv2_inferno_breach", 'dark_earth_fire_technique_lv3_oblivion_burn_strike'],
        "base_str": 18, "base_dex": 8, "base_con": 14, "base_int": 6,
        "base_hp": 2200, "base_ap": 12,
        "str_per_level": 3, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 1
    }
]

""" Dungeon generation logic

 1. create first room around 0,0
 2. use max_neighbors_per_room and additional_connection_chance to create new rooms and their connections
 3. place new rooms so they do not overlap with existing rooms
 4. make connections between rooms
 5. continue loop until rooms_per_floor is reached
 6. do a perimeter sweep to add naturalization avoiding overlap and creating unwanted connections
 7. place npcs
 8. place loot (get to this later)
"""
DUNGEON_SETTINGS: Dict[str, Any] = {
    "dungeon_id": "rokhuld_lair",
    "seed": abs(hash("rokhuld_lair")),
    "floor_count": 1,
    "room_size_min_max": (81, 120),  # a 9x9 area is 81
    "rooms_per_floor": 6,
    "max_neighbors_per_room": 2,
    "additional_connection_chance": 0.0,
    "min_max_distance_between_rooms": (5,12),
    "min_max_corridor_width": (3,6),
    "display_name": "Rokhuld's Deep Core",
    "open_area_tile": OPEN_AREA_TILE,
    "impassable_tile": IMPASSABLE_TILE,
    "impassable_chance": IMPASSABLE_CHANCE,
    "floor_hostiles": FLOOR_HOSTILES,
    "hostile_seeds": HOSTILE_SEEDS,
    "npcs": DUNGEON_NPCS,
	"items": DUNGEON_ITEMS,
    "boss_mob": BOSS_MOB,
    "boss_hostiles": BOSS_HOSTILES,
    "visible_distance": 5
}
