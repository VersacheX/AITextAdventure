"""Seth's Hideout Dungeon Seed Configuration"""

from typing import Dict, Any

# Tile constants for dungeon rendering and builder decisions
OPEN_AREA_TILE = "░" 
IMPASSABLE_TILE = "¤"      
#OPEN_AREA_TILE = "▞"

IMPASSABLE_CHANCE = 0.04   # roots shifting, blocking paths

#### SAVE FOR LATER... COOL TILE SET
# OPEN_AREA_TILE = "▞" # Disco
# IMPASSABLE_TILE = "◘" # Link block ... possible chest

FLOOR_HOSTILES = {
    1: ['cave_bat', 'cave_creeper', 'burrowback_tunneler', 'gloomfang_stalker'],
    2: ['tunnel_scavenger', 'glowcap_fungus', 'burrowback_tunneler', 'gloomfang_stalker'],
    3: ['tunnel_scavenger', 'glowcap_fungus', 'burrowback_tunneler', 'gloomfang_stalker'],
}

HOSTILE_SEEDS = [
    # Common 1 — Cave Bat
    {
        'id': 'cave_bat',
        'name': 'Cave Bat',
        'hostile_type': 'creature',
        'min_spawn_level': 1,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 6,
        'common_drop': 'stimulant_small',
        'rare_drop': None,
        'money_range': (1, 4),
        'basic_attack': 'wing slash',
        'strong_attack': 'sonic screech',
        'player_abilities': [],
        'base_str': 2,
        'base_dex': 4,
        'base_con': 2,
        'base_int': 1,
        'base_hp': 12,
        'base_ap': 2,
        'str_per_level': 1,
        'dex_per_level': 1,
        'con_per_level': 1,
        'int_per_level': 0,
        'resistances': [],
        'immunities': ['sleep'],
        'weaknesses': ['light']
    },

    # Common 2 — Tunnel Scavenger
    {
        'id': 'tunnel_scavenger',
        'name': 'Tunnel Scavenger',
        'hostile_type': 'creature',
        'min_spawn_level': 1,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 8,
        'common_drop': 'cloth_cap',
        'rare_drop': 'stimulant_med',
        'money_range': (2, 6),
        'basic_attack': 'gnaw',
        'strong_attack': 'rabid lunge',
        'player_abilities': [],
        'base_str': 3,
        'base_dex': 3,
        'base_con': 3,
        'base_int': 1,
        'base_hp': 16,
        'base_ap': 2,
        'str_per_level': 1,
        'dex_per_level': 1,
        'con_per_level': 1,
        'int_per_level': 0,
        'resistances': [],
        'immunities': [],
        'weaknesses': ['fire']
    },

    # Uncommon 1 — Glowcap Fungus
    {
        'id': 'glowcap_fungus',
        'name': 'Glowcap Fungus',
        'hostile_type': 'plant',
        'min_spawn_level': 4,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 14,
        'common_drop': 'herb_minor',
        'rare_drop': None,
        'money_range': (1, 5),
        'basic_attack': 'spore puff',
        'strong_attack': 'luminescent burst',
        'player_abilities': ['earth_skill_lv1_soporific_veil'],
        'base_str': 1,
        'base_dex': 1,
        'base_con': 5,
        'base_int': 2,
        'base_hp': 22,
        'base_ap': 3,
        'str_per_level': 0,
        'dex_per_level': 0,
        'con_per_level': 2,
        'int_per_level': 1,
        'resistances': ['earth'],
        'immunities': ['poison'],
        'weaknesses': ['fire']
    },

    # Uncommon 2 — Cave Creeper
    {
        'id': 'cave_creeper',
        'name': 'Cave Creeper',
        'hostile_type': 'creature',
        'min_spawn_level': 3,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 18,
        'common_drop': 'stimulant_small',
        'rare_drop': 'herb_minor',
        'money_range': (3, 8),
        'basic_attack': 'skitter strike',
        'strong_attack': 'web bind',
        'player_abilities': [],
        'base_str': 2,
        'base_dex': 5,
        'base_con': 3,
        'base_int': 1,
        'base_hp': 20,
        'base_ap': 3,
        'str_per_level': 1,
        'dex_per_level': 2,
        'con_per_level': 1,
        'int_per_level': 0,
        'resistances': [],
        'immunities': ['slow'],
        'weaknesses': ['fire']
    },

    # Rare — Burrowback Tunneler
    {
        'id': 'burrowback_tunneler',
        'name': 'Burrowback Tunneler',
        'hostile_type': 'creature',
        'min_spawn_level': 3,
        'role': 'damage',
        'rarity': 'rare',
        'base_xp': 30,
        'common_drop': 'herb_med',
        'rare_drop': 'tome_con',
        'money_range': (6, 14),
        'basic_attack': 'shell slam',
        'strong_attack': 'burrow charge',
        'player_abilities': [],
        'base_str': 4,
        'base_dex': 2,
        'base_con': 8,
        'base_int': 1,
        'base_hp': 40,
        'base_ap': 3,
        'str_per_level': 1,
        'dex_per_level': 0,
        'con_per_level': 3,
        'int_per_level': 0,
        'resistances': ['earth'],
        'immunities': [],
        'weaknesses': ['lightning']
    },

    # Superrare — Gloomfang Stalker
    {
        'id': 'gloomfang_stalker',
        'name': 'Gloomfang Stalker',
        'hostile_type': 'creature',
        'min_spawn_level': 4,
        'role': 'damage',
        'rarity': 'superrare',
        'base_xp': 60,
        'common_drop': 'stimulant_large',
        'rare_drop': 'tome_dex_superrare',
        'money_range': (10, 20),
        'basic_attack': 'shadow bite',
        'strong_attack': 'gloom pounce',
        'player_abilities': ['dark_skill_lv1_tranq_dart'],
        'base_str': 5,
        'base_dex': 9,
        'base_con': 4,
        'base_int': 2,
        'base_hp': 50,
        'base_ap': 4,
        'str_per_level': 1,
        'dex_per_level': 3,
        'con_per_level': 1,
        'int_per_level': 0,
        'resistances': ['dark'],
        'immunities': ['sleep'],
        'weaknesses': ['light']
    }
]


DUNGEON_NPCS = [ {'id': 'seth','location': 'final_chamber'} ]
DUNGEON_ITEMS = [ 
    {'id': 'herb_major', 'location': 'treasure_room'},
    {'id': 'taser', 'location': 'treasure_room'},
    {'id': 'leather_armor', 'location': 'treasure_room'},
    {'id': 'leather_bracers', 'location': 'treasure_room'},
    {'id': 'leather_chaps', 'location': 'treasure_room'}
]

BOSS_MOB = { 'id': 'seth_1',
             'name': 'Lone Wolf Seth',
             'hostiles': [
                'seth_1']
            }

BOSS_HOSTILES = [
    {
        "id": "seth_1", "name": "Lone Wolf Seth", "hostile_type": "rogue", "role": "damage",
        "min_spawn_level": 8, "rarity": "notfound", "base_xp": 1200,
        "common_drop": "herb_major", "rare_drop": "tome_dex", "money_range": (50,150),
        "basic_attack": "snap shot", "strong_attack": "renegade strike",
        "player_abilities": ['electric_skill_lv1_lightning_strike', 'dark_skill_lv1_tranq_dart'],
        "base_str": 8, "base_dex": 18, "base_con": 8, "base_int": 8,
        "base_hp": 2000, "base_ap": 80,
        "str_per_level": 1, "dex_per_level": 7, "con_per_level": 1, "int_per_level": 1,
        'resistances': [],
        'immunities': ['sleep', 'confuse', 'petrify'],
        'weaknesses': []
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    "dungeon_id": "seth_hideout",
    "seed": abs(hash("seth_hideout")),
    "floor_count": 3,
    "room_size_min_max": (81, 120),  # a 9x9 area is 81
    "rooms_per_floor": 3,
    "max_neighbors_per_room": 3,
    "additional_connection_chance": 0.0,
    "min_max_distance_between_rooms": (3,8),
    "min_max_corridor_width": (1,3),
    "display_name": "Seth's Hideout",
    "open_area_tile": OPEN_AREA_TILE,
    "impassable_tile": IMPASSABLE_TILE,
    "impassable_chance": IMPASSABLE_CHANCE,
    "floor_hostiles": FLOOR_HOSTILES,
    "hostile_seeds": HOSTILE_SEEDS,
    "npcs": DUNGEON_NPCS,
    "items": DUNGEON_ITEMS,
    "boss_mob": BOSS_MOB,
    "boss_hostiles": BOSS_HOSTILES,
    "visible_distance": 4
}
