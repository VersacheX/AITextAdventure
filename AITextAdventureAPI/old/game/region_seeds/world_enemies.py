"""
Global world hostile seeds.

WORLD_NPCS - These are hostiles not defined in any chapter or story document

WORLD_BOSS_MOBS - These are boss mobs not found as the main boss mob of any dungeon.  They are either secondary dungeon battles or overworld battles

WORLD_HOSTILES - These are hostiles not found in the main hostile set of any dungeon.  They are either secondary dungeon hostiles or overworld fixed battle hostiles.

OVERWORLD BOSS ENCOUNTERS
---------------------------------------------------------------------------
Some story chapters trigger boss_battle combat outside of any dungeon. These
fights occur directly in an overworld region or city location. Because there is
no dungeon seed file to house them, their boss_mob definition MUST live here in
WORLD_BOSS_MOBS, and their hostile definition(s) MUST live here in WORLD_HOSTILES.

Known overworld boss encounters (by chapter and mob id):

  Chapter 10 - festival_rioters_1 / festival_rioters_2 / festival_rioters_3
    Location : region_city_bar / city streets (overworld)
    Trigger  : main_story_ch10 defeat_rioters_1/2/3 tasks (begin_combat)
    Hostiles : manic_rioter, frenzied_rioter, festival_berserker
    Note     : Three escalating waves of manic citizens corrupted by
               Revelry and Rapture's influence. combat_type is 'combat'
      (not boss_battle). No create_npc or create_dungeon wraps
  these fights -- they break out directly in the city streets.
    Wave 1: three manic_rioters.
 Wave 2: one manic_rioter + two frenzied_rioters.
        Wave 3: one frenzied_rioter + one festival_berserker.

  Chapter 14 - stigma_boss_battle_1
    Location : region_city_bar (overworld)
    Trigger  : main_story_ch14_defeat_stigma task (begin_combat)
    Hostiles : stigma
    Note     : Stigma is placed with create_npc in the city bar. The fight
        is scripted, not dungeon-gated. The mob id used in the chapter
               is 'stigma_boss_battle_1' -- this is distinct from the generic
   'stigma_1' entry which is reserved for secondary encounters.

  Chapter 20 - oracle_reliquary_2
    Location : memory_museum dungeon (second battle, triggered mid-dungeon)
    Trigger  : main_story_ch20_defeat_oracle_and_reliquary_again task (begin_combat)
    Hostiles : oracle_boss_2, reliquary_boss_2
    Note     : The memory_museum dungeon only supports a single boss_mob entry.
         The second Oracle/Reliquary encounter is a story-triggered reset
      battle that occurs after the player delivers the memory tonic to
       Curator Lysa. Because it cannot live in the dungeon seed as a
               second boss_mob, it is defined here as a world mob instead.
       oracle_boss_2 and reliquary_boss_2 are the escalated Reset
               variants -- higher stats and an additional immunity each vs
        the round-1 versions in the dungeon file.
---------------------------------------------------------------------------"""

WORLD_NPCS = [
  {
    "npc_id": "the_void",
    "name": "Void",
    "description": "The horizon-sized absence at the end of all stories. Not darkness — the erasure of the concept of 'something.'",
    "theme_song": "Symphony of Destruction, Megadeth",
    "psychology": {
      "mbti": "ENTJ-shadow",
      "dominant": "Te — Executes annihilation with perfect, cosmic precision; every action is a terminal command.",
      "auxiliary": "Ni — Absolute inevitability; perceives only one valid future: total unmaking.",
      "tertiary": "Se — Rejects physicality; collapses matter into conceptual zero.",
      "inferior": "Fi — Values erasure as purity; rejects all bonds, meaning, and identity as contamination."
    }
  },
  {
    "npc_id": "dominion",
    "name": "Dominion",
    "description": "The architect of metaphysical imprisonment — the structure that ensures all things end as they must.",
    "theme_song": "The Becoming, Nine Inch Nails",
    "psychology": {
      "mbti": "INTJ-shadow",
      "dominant": "Ni — Sees all futures converging into a single, inescapable system.",
      "auxiliary": "Te — Imposes cosmic law; enforces annihilation as the only stable configuration.",
      "tertiary": "Fi — Rejects individuality; identity is a flaw to be excised.",
      "inferior": "Se — Material domination; reshapes matter into rigid, lifeless order."
    }
  }
]

WORLD_BOSS_MOBS = [
    { 
        'id': 'the_void_1',
        'name': 'The Void',
        'hostiles': [
            'the_void'
        ]
    },
	# Ch14 - overworld fight in region_city_bar. Stigma is placed via create_npc,
	# not inside a dungeon. The chapter references this specific mob id.
    {
        'id': 'stigma_boss_battle_1',
        'name': 'Stigma',
        'hostiles': [
            'stigma'
        ]
	},
	# Ch10 - three escalating overworld rioter waves, triggered in city streets.
	# combat_type is 'combat', not 'boss_battle'.
	{
		'id': 'festival_rioters_1',
		'name': 'Festival Rioters',
		'hostiles': [
			'manic_rioter', 'manic_rioter', 'manic_rioter'
]
	},
	{
		'id': 'festival_rioters_2',
		'name': 'Festival Rioters - Wave 2',
		'hostiles': [
			'manic_rioter', 'frenzied_rioter', 'frenzied_rioter'
		]
	},
	{
		'id': 'festival_rioters_3',
		'name': 'Festival Rioters - Final Wave',
		'hostiles': [
			'frenzied_rioter', 'festival_berserker'
		]
	},
    {
	    'id': 'oracle_reliquary_2',
	    'name': 'Oracle and Reliquary - Reset',
	    'hostiles': ['oracle_boss_2', 'reliquary_boss_2']
    },
    { 
        'id': 'dominion_1',
        'name': 'Dominion - System Incarnate',
        'hostiles': ['dominion']
    }
]

WORLD_HOSTILES = [
    {
        'id': 'the_void',
        'name': 'Void',
        'hostile_type': 'void_entity',
        'min_spawn_level': 100,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 50000,
        'common_drop': None,
        'rare_drop': None,
        'money_range': (1000, 5000),
        'basic_attack': 'void grasp',
        'strong_attack': 'void eruption',
        'player_abilities': ['eternal_void', 'absolution', 'unfinity'],
        'base_str': 50,
        'base_dex': 30,
        'base_con': 50,
        'base_int': 70,
        'base_hp': 2000000,
        'base_ap': 500,
        'str_per_level': 5,
        'dex_per_level': 3,
        'con_per_level': 5,
        'int_per_level': 7,
        'resistances': ['dark'],
        'immunities': ['confuse', 'stun', 'petrify', 'silence', 'sleep'],
        'weaknesses': ['light']
    },
    {
        'id': 'dominion',
        'name': 'Dominion',
        'hostile_type': 'void_entity',
        'min_spawn_level': 95,
        'role': 'tank',
        'rarity': 'notfound',
        'base_xp': 80000,
        'common_drop': None,
        'rare_drop': None,
        'money_range': (2000, 8000),
        'basic_attack': 'lawful strike',
        'strong_attack': 'inescapable decree',
        'player_abilities': ['inevitability_matrix', 'inescapable_fate', 'void_lattice'],
        'base_str': 60,
        'base_dex': 30,
        'base_con': 80,
        'base_int': 90,
        'base_hp': 1200000,
        'base_ap': 450,
        'str_per_level': 6,
        'dex_per_level': 3,
        'con_per_level': 8,
        'int_per_level': 8,
        'resistances': ['dark'],
        'immunities': ['confuse', 'stun', 'petrify', 'silence', 'sleep'],
        'weaknesses': ['light']
    },
    {
        'id': 'stigma',
        'name': 'Stigma',
        'hostile_type': 'void_entity',
        'min_spawn_level': 70,
        'role': 'support',
        'rarity': 'notfound',
        'base_xp': 60000,
        'common_drop': None,
        'rare_drop': None,
        'money_range': (1500, 7500),
        'basic_attack': 'supportive touch',
        'strong_attack': 'void embrace',
        'player_abilities': ['void_refraction', 'the_darkness_consuming', 'you_can_be_me'],
        'base_str': 40,
        'base_dex': 30,
        'base_con': 40,
        'base_int': 60,
        'base_hp': 250000,
        'base_ap': 400,
        'str_per_level': 4,
        'dex_per_level': 3,
        'con_per_level': 4,
        'int_per_level': 6,
        'resistances': ['dark'],
        'immunities': ['confuse', 'stun', 'petrify', 'silence', 'sleep'],
        'weaknesses': ['light']
    },
	# -------------------------------------------------------------------
	# Chapter 10 overworld rioters — manic citizens corrupted by Revelry
	# and Rapture. Appear in three escalating waves on the city streets.
	# -------------------------------------------------------------------
	{
		'id': 'manic_rioter',
		'name': 'Manic Rioter',
		'hostile_type': 'humanoid',
		'min_spawn_level': 50,
		'role': 'damage',
		'rarity': 'notfound',
		'base_xp': 800,
		'common_drop': None,
		'rare_drop': None,
		'money_range': (50, 150),
		'basic_attack': 'frenzied strike',
		'strong_attack': 'mob surge',
		'player_abilities': [],
		'base_str': 28,
		'base_dex': 22,
		'base_con': 25,
		'base_int': 10,
		'base_hp': 8000,
		'base_ap': 80,
		'str_per_level': 3,
		'dex_per_level': 2,
		'con_per_level': 2,
		'int_per_level': 1,
		'resistances': [],
		'immunities': ['fear', 'confuse'],
		'weaknesses': ['ice']
	},
	{
		'id': 'frenzied_rioter',
		'name': 'Frenzied Rioter',
		'hostile_type': 'humanoid',
		'min_spawn_level': 52,
		'role': 'damage',
		'rarity': 'notfound',
		'base_xp': 1200,
		'common_drop': None,
		'rare_drop': None,
		'money_range': (80, 200),
		'basic_attack': 'wild assault',
		'strong_attack': 'euphoric rampage',
		'player_abilities': [],
		'base_str': 35,
		'base_dex': 30,
		'base_con': 30,
		'base_int': 8,
		'base_hp': 12000,
		'base_ap': 90,
		'str_per_level': 4,
		'dex_per_level': 3,
		'con_per_level': 3,
		'int_per_level': 1,
		'resistances': ['fire'],
		'immunities': ['fear', 'confuse', 'sleep'],
		'weaknesses': ['ice']
	},
	{
		'id': 'festival_berserker',
		'name': 'Festival Berserker',
		'hostile_type': 'humanoid',
		'min_spawn_level': 54,
		'role': 'damage',
		'rarity': 'notfound',
		'base_xp': 2000,
		'common_drop': None,
		'rare_drop': None,
		'money_range': (120, 300),
		'basic_attack': 'adrenaline slam',
		'strong_attack': 'crash wave',
		'player_abilities': [],
		'base_str': 48,
		'base_dex': 35,
		'base_con': 40,
		'base_int': 6,
		'base_hp': 20000,
		'base_ap': 100,
		'str_per_level': 5,
		'dex_per_level': 4,
		'con_per_level': 4,
		'int_per_level': 1,
		'resistances': ['fire', 'physical'],
		'immunities': ['fear', 'confuse', 'sleep', 'stun'],
		'weaknesses': ['ice', 'dark']
	},
	{
		'id': 'oracle_boss_2', 'name': 'Oracle - Reset', 'hostile_type': 'aberration', 'min_spawn_level': 103, 'role': 'hazard', 'rarity': 'notfound',
		'base_xp': 50000, 'common_drop': 'tome_int_superrare', 'rare_drop': 'shattered_prophecy', 'money_range': (12000, 24000),
		'basic_attack': 'immutable future', 'strong_attack': 'the only ending', 'player_abilities': ['inescapable_prophecy', 'vision_of_ruin', 'fate_lock'],
		'base_str': 60, 'base_dex': 70, 'base_con': 62, 'base_int': 110, 'base_hp': 180000, 'base_ap': 1800,
		'str_per_level': 7, 'dex_per_level': 9, 'con_per_level': 8, 'int_per_level': 14,
		'resistances': ['dark', 'ice', 'electric', 'air'], 'immunities': ['fear', 'confuse', 'sleep', 'stun'], 'weaknesses': ['light']
	},
	{
		'id': 'reliquary_boss_2', 'name': 'Reliquary - Reset', 'hostile_type': 'aberration', 'min_spawn_level': 103, 'role': 'damage', 'rarity': 'notfound',
		'base_xp': 50000, 'common_drop': 'tome_con_superrare', 'rare_drop': 'final_archive', 'money_range': (12000, 24000),
		'basic_attack': 'the past always returns', 'strong_attack': 'inescapable record', 'player_abilities': ['eternal_wound', 'memory_of_suffering', 'burden_of_the_lost'],
		'base_str': 65, 'base_dex': 60, 'base_con': 80, 'base_int': 92, 'base_hp': 200000, 'base_ap': 1600,
		'str_per_level': 8, 'dex_per_level': 7, 'con_per_level': 10, 'int_per_level': 11,
		'resistances': ['dark', 'physical', 'ice', 'earth'], 'immunities': ['stun', 'petrify', 'confuse', 'fear'], 'weaknesses': ['light', 'fire']
	}
]
