"""
Trial 3 Dungeon - Chapter 21 Dungeon Seed Configuration
System of Sensation - Revelry, Lament, and Paradox
"""
from typing import Dict, Any

# Tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "█"
IMPASSABLE_CHANCE = 0.12
OPEN_AREA_COLOR  = "#7a4060"
IMPASSABLE_COLOR = "#1e0818"
BORDER_TILE      = "·"
BORDER_COLOR     = "#501028"

# Hostiles
FLOOR_HOSTILES = {
    1: ['euphoria_addict', 'silence_wraith', 'contradiction_beast', 'escalation_construct'],
}

HOSTILE_SEEDS = [
    {
        'id': 'euphoria_addict', 'name': 'Euphoria Addict', 'hostile_type': 'humanoid', 'min_spawn_level': 97, 'role': 'damage', 'rarity': 'common',
        'base_xp': 9000, 'common_drop': 'potion_hp_mega', 'rare_drop': None, 'money_range': (900, 1300),
        'basic_attack': 'frenzied assault', 'strong_attack': 'manic rush', 'player_abilities': [],
        'base_str': 52, 'base_dex': 48, 'base_con': 42, 'base_int': 35, 'base_hp': 43000, 'base_ap': 330,
        'str_per_level': 6, 'dex_per_level': 6, 'con_per_level': 5, 'int_per_level': 4,
        'resistances': ['fire'], 'immunities': ['fear'], 'weaknesses': ['ice', 'light']
    },
    {
        'id': 'silence_wraith', 'name': 'Silence Wraith', 'hostile_type': 'undead', 'min_spawn_level': 98, 'role': 'hazard', 'rarity': 'uncommon',
        'base_xp': 9500, 'common_drop': 'potion_ap_mega', 'rare_drop': 'tome_int_rare', 'money_range': (950, 1400),
        'basic_attack': 'hollow touch', 'strong_attack': 'aftermath despair', 'player_abilities': ['dark_faith_lv1_shade_whisper'],
        'base_str': 38, 'base_dex': 42, 'base_con': 40, 'base_int': 58, 'base_hp': 40000, 'base_ap': 380,
        'str_per_level': 4, 'dex_per_level': 5, 'con_per_level': 4, 'int_per_level': 7,
        'resistances': ['dark', 'ice'], 'immunities': ['sleep', 'silence'], 'weaknesses': ['light', 'fire']
    },
    {
        'id': 'contradiction_beast', 'name': 'Contradiction Beast', 'hostile_type': 'aberration', 'min_spawn_level': 99, 'role': 'hazard', 'rarity': 'rare',
        'base_xp': 11000, 'common_drop': 'elixir_full', 'rare_drop': 'tome_con_superrare', 'money_range': (1000, 1600),
        'basic_attack': 'paradoxical strike', 'strong_attack': 'logic collapse', 'player_abilities': [],
        'base_str': 50, 'base_dex': 50, 'base_con': 50, 'base_int': 50, 'base_hp': 50000, 'base_ap': 400,
        'str_per_level': 6, 'dex_per_level': 6, 'con_per_level': 6, 'int_per_level': 6,
        'resistances': ['dark', 'light'], 'immunities': ['confuse'], 'weaknesses': []
    },
    {
        'id': 'escalation_construct', 'name': 'Escalation Construct', 'hostile_type': 'construct', 'min_spawn_level': 100, 'role': 'damage', 'rarity': 'superrare',
        'base_xp': 12000, 'common_drop': 'phoenix_down', 'rare_drop': 'tome_dex_superrare', 'money_range': (1100, 1700),
        'basic_attack': 'intensity spike', 'strong_attack': 'unsustainable peak', 'player_abilities': [],
        'base_str': 62, 'base_dex': 58, 'base_con': 48, 'base_int': 40, 'base_hp': 52000, 'base_ap': 360,
        'str_per_level': 8, 'dex_per_level': 7, 'con_per_level': 5, 'int_per_level': 4,
        'resistances': ['fire', 'electric'], 'immunities': ['stun', 'fear'], 'weaknesses': ['ice', 'light']
    }
]

# Boss
DUNGEON_NPCS = [
    {'id': 'revelry', 'location': 'final_chamber'}
]

BOSS_MOB = {
    'id': 'revelry_lament_paradox_1',
    'name': 'The Sensation Cycle',
    'hostiles': ['revelry_trial', 'lament_trial', 'paradox_trial']
}

BOSS_HOSTILES = [
    {
        'id': 'revelry_trial', 'name': 'Revelry', 'hostile_type': 'void_entity', 'min_spawn_level': 100, 'role': 'damage', 'rarity': 'notfound',
        'base_xp': 120000, 'common_drop': 'tome_dex_superrare', 'rare_drop': 'revelry_euphoria_crystal', 'money_range': (6000, 12000),
        'basic_attack': 'intoxicating rush', 'strong_attack': 'crescendo', 'player_abilities': ['euphoric_cascade', 'sensory_overload', 'the_rush'],
        'base_str': 58, 'base_dex': 68, 'base_con': 52, 'base_int': 48, 'base_hp': 330000, 'base_ap': 600,
        'str_per_level': 7, 'dex_per_level': 9, 'con_per_level': 6, 'int_per_level': 5,
        'resistances': ['fire', 'air'], 'immunities': ['fear', 'sleep', 'confuse'], 'weaknesses': ['ice', 'light']
    },
    {
        'id': 'lament_trial', 'name': 'Lament', 'hostile_type': 'void_entity', 'min_spawn_level': 100, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 120000, 'common_drop': 'tome_int_superrare', 'rare_drop': 'lament_sorrow_shroud', 'money_range': (6000, 12000),
        'basic_attack': 'melancholic drain', 'strong_attack': 'the quiet after', 'player_abilities': ['crushing_despair', 'hollow_silence', 'the_emptiness'],
        'base_str': 42, 'base_dex': 45, 'base_con': 55, 'base_int': 72, 'base_hp': 310000, 'base_ap': 680,
        'str_per_level': 5, 'dex_per_level': 5, 'con_per_level': 6, 'int_per_level': 9,
        'resistances': ['dark', 'ice'], 'immunities': ['sleep', 'silence', 'petrify'], 'weaknesses': ['light', 'fire']
    },
    {
        'id': 'paradox_trial', 'name': 'Paradox', 'hostile_type': 'void_entity', 'min_spawn_level': 100, 'role': 'hazard', 'rarity': 'notfound',
        'base_xp': 120000, 'common_drop': 'tome_str_superrare', 'rare_drop': 'paradox_duality_orb', 'money_range': (6000, 12000),
        'basic_attack': 'contradictory force', 'strong_attack': 'both and neither', 'player_abilities': ['contradiction_loop', 'impossible_truth', 'paradox_embrace'],
        'base_str': 55, 'base_dex': 55, 'base_con': 60, 'base_int': 60, 'base_hp': 340000, 'base_ap': 620,
        'str_per_level': 6, 'dex_per_level': 6, 'con_per_level': 7, 'int_per_level': 7,
        'resistances': ['dark', 'light', 'physical'], 'immunities': ['confuse', 'stun'], 'weaknesses': []
    }
]

DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'trial_3_dungeon',
    'seed': abs(hash('trial_3_dungeon')),
    'floor_count': 1,
    'room_size_min_max': (140, 220),
    'rooms_per_floor': 9,
    'max_neighbors_per_room': 4,
    'additional_connection_chance': 0.18,
    'min_max_distance_between_rooms': (2, 6),
    'min_max_corridor_width': (4, 7),
    'display_name': "The System of Sensation",
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color':  OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile':      BORDER_TILE,
    'border_color':     BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'npcs': DUNGEON_NPCS,
    'items': [
        {'id': 'elixir_full', 'location': 'treasure_room'},
        {'id': 'phoenix_down', 'location': 'treasure_room'},
        {'id': 'tome_hp_superrare', 'location': 'treasure_room'},
    ],
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
    'visible_distance': 9,
}