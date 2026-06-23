ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'tidejudge_merrik',
		'name': 'Merrik Tidejudge',
		'description': (
			'A stern adjudicator who settles disputes among sailors and merchants.'
			' Merrik’s gavel is carved from driftwood older than the town itself.'
			' He has a reputation for fairness, but never softness.'
		)
	},
	{
		'npc_id': 'lanternrunner_vexa',
		'name': 'Vexa Lanternrunner',
		'description': (
			'A cunning smuggler who uses coded lantern signals to move goods unseen.'
			' Vexa’s grin is sharp, and her footsteps are softer than sea foam.'
			' She claims the Lanternhouse has secret tunnels even she hasn’t found.'
		)
	},
    {
        'npc_id': 'signal_seer_thalen',
        'name': 'Thalen the Signal‑Seer',
        'description': (
            'A coastal mystic who reads broken lantern patterns drifting across the waves.'
        )
    },
    {
        'npc_id': 'lanternfade_echo',
        'name': 'Lanternfade Echo',
        'description': (
            'A spectral remnant of lost lantern signals swallowed by storms and fog.'
        )
    },
    {
        'npc_id': 'undertunnel_voice',
        'name': 'Undertunnel Voice',
        'description': (
            'A whispering presence formed from misdirected signals deep within the smuggler tunnels.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'tidejudge_merrik',
        'dialog_id': 'merrik_intro',
        'dialog': [
            "Lantern codes contradict themselves.",
            "Signals flicker in patterns no sailor would send.",
            "Something disrupts the order of the coast."
        ]
    },

    {
        'npc_id': 'lanternrunner_vexa',
        'dialog_id': 'vexa_intro',
        'dialog': [
            "Routes flicker wrong.",
            "Someone’s sending signals that lead nowhere — or worse.",
            "If we don’t stop it, ships will vanish in calm waters."
        ]
    },

    {
        'npc_id': 'signal_seer_thalen',
        'dialog_id': 'thalen_intro',
        'dialog': [
            "The lantern patterns fracture.",
            "A False Lantern rises — a spirit of misdirection.",
            "If it awakens fully, the coast will lose its way."
        ]
    },

    {
        'npc_id': 'lanternfade_echo',
        'dialog_id': 'lanternfade_echo_intro',
        'dialog': [
            "We are the signals that faded.",
            "The False Lantern twists our light.",
            "It waits deeper in the Undertunnel."
        ]
    },

    {
        'npc_id': 'undertunnel_voice',
        'dialog_id': 'undertunnel_voice_intro',
        'dialog': [
            "The tunnels hum with stolen signals.",
            "The False Lantern gathers strength.",
            "Only its heart remains to be dimmed."
        ]
    },

    {
        'npc_id': 'tidejudge_merrik',
        'dialog_id': 'merrik_closing',
        'dialog': [
            "The signals steady. The coast finds its bearings again.",
            "You’ve restored truth to the lantern routes.",
            "The Shallows will remember your clarity."
        ]
    }

]


TASKS = [
	{
		'task_id': 'shallows_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'tidejudge_merrik',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'tidejudge_merrik',
					'standing_text': [ 
						"Disputes find their calm here—if you have a grievance, speak plainly."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'lanternrunner_vexa',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'lanternrunner_vexa',
					'standing_text': [ 
						"Lanterns hide more than light—share a secret and I might share a route."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_meet_merrik'
                }
            }
		]		
	},

    # Task 1 — Meet Merrik after initialization
    {
        'task_id': 'shallows_mid_city_meet_merrik',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'tidejudge_merrik',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'tidejudge_merrik',
                    'standing_text': [
                        "Signals conflict. Lantern codes contradict themselves.",
                        "Something disrupts the order of the coast."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'tidejudge_merrik',
                    'dialog_id': 'merrik_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_meet_vexa'
                }
            }
        ]
    },

    # Task 2 — Meet Vexa for the smuggler’s perspective
    {
        'task_id': 'shallows_mid_city_meet_vexa',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lanternrunner_vexa',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'lanternrunner_vexa',
                    'dialog_id': 'vexa_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'lanternrunner_vexa',
                    'standing_text': [
                        "Lantern routes flicker wrong.",
                        "Someone — or something — is sending false signals."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_find_thalen'
                }
            }
        ]
    },

    # Task 3 — Find Signal‑Seer Thalen in the open shallows
    {
        'task_id': 'shallows_mid_city_find_thalen',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'signal_seer_thalen',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'signal_seer_thalen',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'signal_seer_thalen',
                    'standing_text': [
                        "Lantern patterns fracture.",
                        "A False Lantern rises beneath the waves."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'signal_seer_thalen',
                    'dialog_id': 'thalen_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_lanternfade_passage'
                }
            }
        ]
    },

    # Task 4 — Explore the Lanternfade Passage (first dungeon)
    {
        'task_id': 'shallows_mid_city_lanternfade_passage',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lanternfade_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'lanternfade_passage',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'lanternfade_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'lanternfade_echo',
                    'dialog_id': 'lanternfade_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_smugglers_undertunnel'
                }
            }
        ]
    },

    # Task 5 — Descend into the Smugglers’ Undertunnel (second dungeon)
    {
        'task_id': 'shallows_mid_city_smugglers_undertunnel',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'undertunnel_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'smugglers_undertunnel',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'undertunnel_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'undertunnel_voice',
                    'dialog_id': 'undertunnel_voice_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_false_lantern'
                }
            }
        ]
    },

    # Task 6 — Defeat the False Lantern (boss dungeon)
    {
        'task_id': 'shallows_mid_city_false_lantern',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'false_lantern_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_false_lantern',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'false_lantern_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'tidejudge_merrik',
                    'dialog_id': 'merrik_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'shallows_mid_city'
                }
            }
        ]
    }

]



PRIMARY_STORY_SETTINGS = {
	'story_id': 'shallows_mid_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}