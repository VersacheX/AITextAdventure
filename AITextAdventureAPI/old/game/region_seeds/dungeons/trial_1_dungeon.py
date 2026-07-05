"""
Trial 1 Dungeon - System of Compliance
========================================
Chapter 21 - First Voidwalker Trial

This dungeon represents Edict, Glamour, and Crux's trial of systemic control.
The environment is a maze of contradictory rules and false certainty where
people stop struggling not because they found truth, but because doubt was removed.

Boss: Edict, Glamour, and Crux (triple boss fight)
Theme: Order without purpose, compliance without meaning
"""

SETTINGS = {
    'dungeon_id': 'trial_1_dungeon',
    'name': 'The System of Compliance',
    'description': (
        'A sterile maze of endless corridors marked with contradictory signs. '
        'The walls pulse with a cold, mechanical rhythm. Citizens wander aimlessly, '
        'following paths without knowing why, their faces blank and peaceful. '
        'Overhead, a voice drones: "Efficiency achieved. Consistency maintained."'
    ),
    'region': 'void_realm',
    'min_level': 95,
    'max_level': 100,
    'boss_mob': {
        'id': 'edict_glamour_crux_1',
        'name': 'The System Enforcers',
        'hostiles': ['edict', 'glamour', 'crux']
    },
    'hostiles': [
        'compliance_drone',
        'certainty_wraith',
        'purpose_void',
        'efficiency_construct'
    ],
    'common_loot': [
        'potion_hp_mega',
        'potion_ap_mega',
        'elixir_full',
        'phoenix_down'
    ],
    'rare_loot': [
        'tome_str_superrare',
        'tome_dex_superrare',
        'tome_int_superrare',
        'tome_con_superrare',
        'void_resistant_armor',
        'system_breaker_weapon'
    ],
    'treasure': [
        'elixir_full',
        'tome_str_rare',
        'void_shard_fragment'
    ]
}

HOSTILES = [
    {
        'id': 'compliance_drone',
        'name': 'Compliance Drone',
        'hostile_type': 'construct',
        'min_spawn_level': 95,
        'role': 'tank',
        'rarity': 'uncommon',
        'base_xp': 8500,
        'common_drop': 'potion_hp_mega',
        'rare_drop': 'void_shard_fragment',
        'money_range': (800, 1200),
        'basic_attack': 'protocol enforcement',
        'strong_attack': 'mandatory compliance',
        'player_abilities': [],
        'base_str': 45,
        'base_dex': 30,
        'base_con': 55,
        'base_int': 35,
        'base_hp': 45000,
        'base_ap': 300,
        'str_per_level': 5,
        'dex_per_level': 3,
        'con_per_level': 6,
        'int_per_level': 4,
        'resistances': ['physical', 'dark'],
        'immunities': ['confuse', 'fear'],
        'weaknesses': ['light']
    },
    {
        'id': 'certainty_wraith',
        'name': 'Certainty Wraith',
        'hostile_type': 'undead',
        'min_spawn_level': 96,
        'role': 'damage',
        'rarity': 'uncommon',
        'base_xp': 9000,
        'common_drop': 'potion_ap_mega',
        'rare_drop': 'tome_int_rare',
        'money_range': (850, 1300),
        'basic_attack': 'false clarity',
        'strong_attack': 'absolute conviction',
        'player_abilities': [],
        'base_str': 38,
        'base_dex': 42,
        'base_con': 40,
        'base_int': 50,
        'base_hp': 38000,
        'base_ap': 350,
        'str_per_level': 4,
        'dex_per_level': 5,
        'con_per_level': 4,
        'int_per_level': 6,
        'resistances': ['dark', 'ice'],
        'immunities': ['confuse', 'sleep'],
        'weaknesses': ['light', 'fire']
    },
    {
        'id': 'purpose_void',
        'name': 'Purpose Void',
        'hostile_type': 'aberration',
        'min_spawn_level': 97,
        'role': 'hazard',
        'rarity': 'rare',
        'base_xp': 10000,
        'common_drop': 'elixir_full',
        'rare_drop': 'tome_con_superrare',
        'money_range': (900, 1500),
        'basic_attack': 'meaningless motion',
        'strong_attack': 'emptiness cascade',
        'player_abilities': [],
        'base_str': 40,
        'base_dex': 35,
        'base_con': 45,
        'base_int': 55,
        'base_hp': 42000,
        'base_ap': 400,
        'str_per_level': 4,
        'dex_per_level': 4,
        'con_per_level': 5,
        'int_per_level': 7,
        'resistances': ['dark', 'poison'],
        'immunities': ['sleep', 'petrify'],
        'weaknesses': ['light']
    },
    {
        'id': 'efficiency_construct',
        'name': 'Efficiency Construct',
        'hostile_type': 'construct',
        'min_spawn_level': 98,
        'role': 'damage',
        'rarity': 'rare',
        'base_xp': 11000,
        'common_drop': 'phoenix_down',
        'rare_drop': 'system_breaker_weapon',
        'money_range': (1000, 1600),
        'basic_attack': 'optimized strike',
        'strong_attack': 'process termination',
        'player_abilities': [],
        'base_str': 52,
        'base_dex': 48,
        'base_con': 50,
        'base_int': 42,
        'base_hp': 50000,
        'base_ap': 350,
        'str_per_level': 6,
        'dex_per_level': 5,
        'con_per_level': 5,
        'int_per_level': 5,
        'resistances': ['physical', 'electric'],
        'immunities': ['stun', 'confuse'],
        'weaknesses': ['light', 'fire']
    },
    {
        'id': 'edict',
        'name': 'Edict',
        'hostile_type': 'void_entity',
        'min_spawn_level': 98,
        'role': 'tank',
        'rarity': 'notfound',
        'base_xp': 100000,
        'common_drop': 'tome_con_superrare',
        'rare_drop': 'edict_enforcement_seal',
        'money_range': (5000, 10000),
        'basic_attack': 'lawful decree',
        'strong_attack': 'absolute order',
        'player_abilities': ['system_lockdown', 'rule_enforcement', 'procedural_inevitability'],
        'base_str': 55,
        'base_dex': 35,
        'base_con': 75,
        'base_int': 60,
        'base_hp': 350000,
        'base_ap': 500,
        'str_per_level': 6,
        'dex_per_level': 4,
        'con_per_level': 8,
        'int_per_level': 7,
        'resistances': ['physical', 'dark'],
        'immunities': ['confuse', 'stun', 'fear', 'silence'],
        'weaknesses': ['light']
    },
    {
        'id': 'glamour',
        'name': 'Glamour',
        'hostile_type': 'void_entity',
        'min_spawn_level': 98,
        'role': 'support',
        'rarity': 'notfound',
        'base_xp': 100000,
        'common_drop': 'tome_int_superrare',
        'rare_drop': 'glamour_illusion_veil',
        'money_range': (5000, 10000),
        'basic_attack': 'false serenity',
        'strong_attack': 'manufactured peace',
        'player_abilities': ['certainty_field', 'doubt_erasure', 'calm_enforcement'],
        'base_str': 40,
        'base_dex': 45,
        'base_con': 50,
        'base_int': 70,
        'base_hp': 280000,
        'base_ap': 600,
        'str_per_level': 4,
        'dex_per_level': 5,
        'con_per_level': 5,
        'int_per_level': 9,
        'resistances': ['ice', 'dark'],
        'immunities': ['confuse', 'fear', 'sleep'],
        'weaknesses': ['light', 'fire']
    },
    {
        'id': 'crux',
        'name': 'Crux',
        'hostile_type': 'void_entity',
        'min_spawn_level': 98,
        'role': 'hazard',
        'rarity': 'notfound',
        'base_xp': 100000,
        'common_drop': 'tome_dex_superrare',
        'rare_drop': 'crux_logic_core',
        'money_range': (5000, 10000),
        'basic_attack': 'logic cascade',
        'strong_attack': 'consistency override',
        'player_abilities': ['contradiction_loop', 'simulated_truth', 'objective_elimination'],
        'base_str': 45,
        'base_dex': 55,
        'base_con': 55,
        'base_int': 65,
        'base_hp': 300000,
        'base_ap': 550,
        'str_per_level': 5,
        'dex_per_level': 6,
        'con_per_level': 6,
        'int_per_level': 8,
        'resistances': ['electric', 'dark'],
        'immunities': ['confuse', 'petrify', 'sleep'],
        'weaknesses': ['light']
    }
]

PRIMARY_DUNGEON_SETTINGS = {
    'settings': SETTINGS,
    'hostiles': HOSTILES
}