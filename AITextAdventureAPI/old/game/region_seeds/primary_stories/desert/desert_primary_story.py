# #DESERT
# local characters:
#  Sable - Sand witch that sells miracles (magic)
# local bad-guys:
#  ZARUUN THE SAND-SUNDERER
#   A towering warlock wrapped in cracked sandstone armor.
#   He believes the desert must “return to emptiness” and is actively collapsing dunes, oases, and ruins into sinkholes.

#   Why he opposes Sable:  
#    He thinks Sable’s “miracles” interfere with the desert’s “true destiny” — dissolution.

#   Void Hint:  
#    He claims he can hear the world thinning beneath the sand.

# dialog and story:

# Sable & Zaruun
# Protagonist Intro (Sable → Player)
# “Well now… you look like someone who can handle a little sandstorm of trouble.
# Zaruun’s been cracking the desert open again — sinkholes, screaming dunes, the whole mess.”

# “He thinks the desert wants to return to emptiness.
# I think he’s an idiot with an ego.”

# “Go knock some sense into him before he hollows the whole region.”

# CREATE: DUNGEON

# Antagonist Intro (Zaruun → Player)
# “So the witch sends another fool.
# The desert is thinning — can’t you feel it?
# I merely help it shed its last illusions.”

# “Turn back, or be swallowed with the rest.”

# Antagonist Defeat (Zaruun → Player)
# “You delay the desert’s truth…
# but the void waits beneath every grain.”

# Protagonist Closing (Sable → Player)
# “Well done, traveler.
# Zaruun’s gone, and the desert can breathe again — for now.”

# “You’ve got grit. I like that.
# I’ll tag along. Someone needs to keep you alive.”

# Reward: Sable joins the cause.

ATTAINABLE_PLAYER_CHARACTERS = [
    #{'id': 'sable', 'name': 'Sable'}
	{ 
        ## total power points = 15 + 15* 29  = 465
        ## total stat points = 10 + 6*29 = 184
        'id': 'sable', 
        'name': 'Sable',
        'arm_armor': 'sandcall_bracers',
        'head_armor': 'mirage_crown',
        'body_armor': 'duneweave_mantle',
        'leg_armor': 'oasis_walker_greaves',
        'equipped_weapon': 'sandglass_staff',
        'max_hp': 891, # 20 + 20 * 29 = 600            + 365
        'current_hp': 891,
        'max_ap': 400, # 5 + 5 * 29 = 150              + 100
        'current_ap': 400,
        'unused_ability_slots': 0,
        'unused_stat_points': 0,
        'unused_power_points': 0,
        'strength': 38,
        'dexterity': 38,        
        'intelligence': 224,                            # + 184
        'constitution': 38,
        'level': 30,
        'abilities': ['earth_earth_earth_magic_lv3_earthshaker', 'air_earth_electric_magic_lv3_gale_shock', 
                      'earth_air_magic_lv2_sandstream', 'earth_light_magic_lv2_prism_shard', 'earth_earth_magic_lv2_quake_field',
                      'earth_magic_lv1_tremor', 'light_magic_lv1_luminous_spike'

        ]

    }
]

#DUNGEONS = ['zaruun_lair']

NPCS = [
	{
		'npc_id': 'sable',
		'name': 'Sable',
		'description': (
			'A desert witch who sells miracles to travelers, though she no longer believes in them herself.'
			' She once failed to save a caravan swallowed by a sand-sink during the first Fracture wave,'
			' and she still hears their voices beneath the dunes. Despite her charisma and insight,'
			' she carries a quiet grief that shapes every choice she makes.'
		),
		"theme_song": "Salt — Daughter",
		"psychology": {
			"mbti": "ENFJ",
			"dominant": "Fe — Reads people instantly and speaks with charismatic authority, guiding others with emotional precision.",
			"auxiliary": "Ni — Senses deeper patterns in the desert’s shifting nature and the Void’s influence beneath it.",
			"tertiary": "Se — Acts decisively in the moment, using her magic with flair and confidence.",
			"inferior": "Ti — Under stress, becomes sharply critical, dissecting others’ logic with biting precision."
		},
        "enneagram": {
          "enneagram_type": "2w3",
          "core_fear": "Being unwanted or unworthy of love.",
          "core_desire": "To be loved and needed.",
          "defense_mechanism": "Repression — Helps others to prove her own worth and atone for her past failure, while repressing her own deep grief and needs.",
          "stress_line": "Moves to Type 8 — Becomes controlling and aggressive when her help is rejected or her past failure is triggered.",
          "growth_line": "Moves to Type 4 — Learns to confront her own grief and find her identity outside of her service to others.",
          "instinctual_variant": "so/sx — Socially charismatic and focused on the needs of the group, but forms intense, emotionally charged connections."
        }
	},
	{
		'npc_id': 'zaruun',
		'name': 'Zaruun',
		'description': (
			'Zaruun the Sand-Sunderer, a towering warlock wrapped in cracked sandstone armor.'
			' He believes the desert must "return to emptiness" and is actively collapsing dunes, oases, and ruins into sinkholes.'
		),
		"psychology": {
			"mbti": "INTJ",
			"dominant": "Ni — Interprets the desert’s decay as destiny. He sees a singular future: dissolution, emptiness, and the stripping away of illusion.",
			"auxiliary": "Te — Executes his vision with ruthless efficiency, collapsing structures and reshaping the land to match his ideology.",
			"tertiary": "Fi — Holds a deeply personal, almost spiritual conviction about the desert’s ‘true nature.’ His morality is internal and unshakeable.",
			"inferior": "Se — When destabilized, he becomes overwhelmed by sensory chaos, lashing out with destructive bursts of magic."
		},
        "enneagram": {
          "enneagram_type": "1w9",
          "core_fear": "Being corrupt, evil, or imbalanced.",
          "core_desire": "To be good and have integrity, to restore the 'pure' state of the desert.",
          "defense_mechanism": "Reaction Formation — Channels his fear of chaos and illusion into a rigid, destructive crusade for 'emptiness' and 'purity'.",
          "stress_line": "Moves to Type 4 — Becomes withdrawn and melancholic, lost in his own bleak philosophy when his vision is challenged.",
          "growth_line": "Moves to Type 7 — Learns to see the beauty and value in the world as it is, not just his idealized version of it.",
          "instinctual_variant": "sp/so — A self-contained reformer, focused on 'purifying' his environment according to his rigid ideals."
        }
	}
]

NPC_DIALOG = [
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_intro',
		'dialog': [
			"Well now… you look like someone who can handle a little sandstorm of trouble.",
			"Zaruun’s been cracking the desert open again — sinkholes, screaming dunes, the whole mess.",
			"He thinks the desert wants to return to emptiness. I think he’s an idiot with an ego.",
			"Go knock some sense into him before he hollows the whole region."
		]
	},
	{
		'npc_id': 'zaruun',
		'dialog_id': 'zaruun_intro',
		'dialog': [
			"So the witch sends another fool.",
			"The desert is thinning — can’t you feel it? I merely help it shed its last illusions.",
			"Turn back, or be swallowed with the rest."
		]
	},
	{
		'npc_id': 'zaruun',
		'dialog_id': 'zaruun_defeat',
		'dialog': [
			"You delay the desert’s truth… but the void waits beneath every grain."
		]
	},
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_closing',
		'dialog': [
			"Well done, traveler. Zaruun’s gone, and the desert can breathe again — for now.",
			"You’ve got grit. I like that. I’ll tag along. Someone needs to keep you alive."
		]
	}
]

TASKS = [
	{
		'task_id': 'desert_primary_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'sable',
					'location': 'region_bar'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sable',
					'standing_text': [ 
						"How's it going?  I'm Sable, the friendliest sand witch around.  I'm out here selling miracles to need.",
						"Maybe one day you'll need one of my miracles too.",
						"Maybe I'll need one from you."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_primary_meet_sable'
				}
			}
		]		
	},
	# Task 1: meet Sable at region bar coordinates
	{		
		'task_id': 'desert_primary_meet_sable',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'sable',
		'item_id': 'dune_sundial',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sable',
					'standing_text': [
						"Zaruun is out there, cracking open the desert. I need the Dune Sundial to hone in on him.",
						"He's been causing sinkholes all over the desert. Please find the Sundial."
					]
				}
			}
		],
		'task_complete_events': [ #< = after meeting
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'sable',
					'dialog_id': 'sable_intro'
				}
			},
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'sable',
                    'standing_text': [
						"Zaruun is still out there, cracking open the desert. Go stop him.",
						"I've heard he’s holed up somewhere in the desert nearby. Be careful."
                    ]
                }
            },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_primary_defeat_zaruun'
				}
			}
		]
	},
	# Task 2: meet Zaruun the Sand-Sunderer in a dungeon
	{
		'task_id': 'desert_primary_defeat_zaruun',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'zaruun',
		'task_acquire_events': [
			{
				'event_type': 'create_dungeon', # <-  creating dungeon with zaruun as boss - speak to him to complete task
				'params': {
					'dungeon_id': 'zaruun_lair',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'zaruun',
					'location': None
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'zaruun',
					'dialog_id': 'zaruun_intro'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'defeat_zaruun'
				}
			}
		],
	},
	# Task 3: defeat Zaruun the Sand-Sunderer
	{
		'task_id': 'defeat_zaruun',
        'type': 'defeat',
        'to_type': 'mob',
		'to_id': 'zaruun_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat', # <- begin combat with zaruun as boss defeating him completes event
				'params': {
					'boss_mob_id': 'zaruun_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'zaruun',
					'dialog_id': 'zaruun_defeat'
				}
			},
			{ 'event_type': 'hide_npc', 'params': { 'npc_id': 'zaruun' }},
			{
				'event_type': 'complete_region_quest',
				'params': {
					'region_id': 'desert',
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_primary_report_to_sable'
				}
			}
		]
	},
	# Task 4: report back to Sable at region bar
	{
		'task_id': 'desert_primary_report_to_sable',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'sable',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'sable',
					'dialog_id': 'sable_closing'
				}
			},
			#remove npc sable location (so she's not on the map)
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'sable'
				}
			},
			{
				'event_type': 'character_join',
				'params': {
					'character_id': 'sable'
				}
			}
		]
	}

    
]



PRIMARY_STORY_SETTINGS = {
    'story_id': 'desert_primary_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
    }