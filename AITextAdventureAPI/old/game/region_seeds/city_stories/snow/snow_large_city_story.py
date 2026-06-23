ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'concordant_ivar',
		'name': 'Ivar the Concordant',
		'description': (
			'A stoic mediator who resolves disputes with icy calm.'
			'  Ivar’s breath forms intricate frost patterns when he speaks.'
			'  He believes harmony is forged like ice—slowly, under pressure.'
		)
	},
	{
		'npc_id': 'artificer_lyndra',
		'name': 'Lyndra Frostlight',
		'description': (
			'A brilliant inventor who blends cold magic with delicate machinery.'
			'  Lyndra’s creations glow with pale blue radiance.'
			'  She works tirelessly, claiming inspiration strikes like sudden snowfall.'
		)
	},
    {
        'npc_id': 'glacier_seer_thryna',
        'name': 'Thryna the Glacier‑Seer',
        'description': (
            'A mystic who reads ice harmonics and senses fractures before they form.'
        )
    },
    {
        'npc_id': 'frostline_echo',
        'name': 'Frostline Echo',
        'description': (
            'A spectral remnant of frozen harmonies twisted by the Fractured Chime.'
        )
    },
    {
        'npc_id': 'glacierpulse_voice',
        'name': 'Glacierpulse Voice',
        'description': (
            'A resonant presence formed from unstable frost deep within the Glacierpulse Chamber.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'concordant_ivar',
        'dialog_id': 'ivar_intro',
        'dialog': [
            "The frost patterns shift without cause.",
            "Harmony fractures beneath the ice.",
            "Something awakens in the deep cold."
        ]
    },

    {
        'npc_id': 'artificer_lyndra',
        'dialog_id': 'lyndra_intro',
        'dialog': [
            "My machines hum out of tune.",
            "Cold magic splinters where it once flowed clean.",
            "If this continues, the city’s frost‑engines will fail."
        ]
    },

    {
        'npc_id': 'glacier_seer_thryna',
        'dialog_id': 'thryna_intro',
        'dialog': [
            "The ice harmonics tremble.",
            "A Fractured Chime rises — a spirit of broken harmony.",
            "If it awakens fully, the frost will turn against itself."
        ]
    },

    {
        'npc_id': 'frostline_echo',
        'dialog_id': 'frostline_echo_intro',
        'dialog': [
            "We are the harmonies that froze wrong.",
            "The Chime twists our resonance.",
            "It waits deeper in the Glacierpulse Chamber."
        ]
    },

    {
        'npc_id': 'glacierpulse_voice',
        'dialog_id': 'glacierpulse_voice_intro',
        'dialog': [
            "The Chamber pulses with unstable frost.",
            "The Chime gathers strength.",
            "Only its heart remains to be stilled."
        ]
    },

    {
        'npc_id': 'concordant_ivar',
        'dialog_id': 'ivar_closing',
        'dialog': [
            "The frost settles. Harmony returns.",
            "You’ve stilled a discord older than the glacier itself.",
            "The Snowlands will remember your calm."
        ]
    }

]


TASKS = [
	{
		'task_id': 'snow_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'concordant_ivar',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'concordant_ivar',
					'standing_text': [ 
						"Calmness grows here—share a quarrel and I will help stitch it closed."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'artificer_lyndra',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'artificer_lyndra',
					'standing_text': [ 
						"My designs are born of frost—tell me a curious problem and I will sketch a solution."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_large_city_meet_ivar'
                }
            }
		]		
	},

    # Task 1 — Meet Ivar after initialization
    {
        'task_id': 'snow_large_city_meet_ivar',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'concordant_ivar',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'concordant_ivar',
                    'standing_text': [
                        "The frost patterns shift unpredictably.",
                        "Something disturbs the harmony beneath the ice."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'concordant_ivar',
                    'dialog_id': 'ivar_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_large_city_meet_lyndra'
                }
            }
        ]
    },

    # Task 2 — Meet Lyndra for the artificer’s perspective
    {
        'task_id': 'snow_large_city_meet_lyndra',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'artificer_lyndra',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'artificer_lyndra',
                    'dialog_id': 'lyndra_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'artificer_lyndra',
                    'standing_text': [
                        "My machines hum out of tune.",
                        "Cold magic fractures where it once flowed cleanly."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_large_city_find_thryna'
                }
            }
        ]
    },

    # Task 3 — Find Glacier‑Seer Thryna in the open snowfields
    {
        'task_id': 'snow_large_city_find_thryna',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'glacier_seer_thryna',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'glacier_seer_thryna',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'glacier_seer_thryna',
                    'standing_text': [
                        "The ice harmonics tremble.",
                        "A Fractured Chime awakens beneath the frostline."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'glacier_seer_thryna',
                    'dialog_id': 'thryna_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_large_city_frostline_conservatory'
                }
            }
        ]
    },

    # Task 4 — Explore the Frostline Conservatory (first dungeon)
    {
        'task_id': 'snow_large_city_frostline_conservatory',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'frostline_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'frostline_conservatory',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'frostline_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'frostline_echo',
                    'dialog_id': 'frostline_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_large_city_glacierpulse_chamber'
                }
            }
        ]
    },

    # Task 5 — Descend into the Glacierpulse Chamber (second dungeon)
    {
        'task_id': 'snow_large_city_glacierpulse_chamber',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'glacierpulse_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'glacierpulse_chamber',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'glacierpulse_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'glacierpulse_voice',
                    'dialog_id': 'glacierpulse_voice_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_large_city_fractured_chime'
                }
            }
        ]
    },

    # Task 6 — Defeat the Fractured Chime (boss dungeon)
    {
        'task_id': 'snow_large_city_fractured_chime',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'fractured_chime_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_fractured_chime',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'fractured_chime_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'concordant_ivar',
                    'dialog_id': 'ivar_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'snow_large_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
    'story_id': 'snow_large_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}