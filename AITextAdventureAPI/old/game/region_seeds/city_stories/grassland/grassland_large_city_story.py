ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'keeper_savran',
		'name': 'Savran Spicekeeper',
		'description': (
			'A charismatic curator of exotic beasts and rarities.'
			' Savran’s cloak is stitched with feathers, scales, and fur from creatures he has tamed.'
			' His stories are as wild as the animals he tends.'
		)
	},
	{
		'npc_id': 'waymaster_delphi',
		'name': 'Delphi the Waymaster',
		'description': (
			'A seasoned caravan leader who has crossed every major trade route.'
			' Delphi’s maps are etched into metal plates to survive harsh travel.'
			' She treats negotiation like a battlefield—calculated, decisive, and fair.'
		)
	},
    {
        'npc_id': 'trail_reader_vexa',
        'name': 'Vexa the Trail‑Reader',
        'description': (
            'A nomadic tracker who reads “wind scars” left by migrating beasts. '
            'Vexa senses disturbances in herd patterns long before they surface.'
        )
    },
    {
        'npc_id': 'hollow_runner',
        'name': 'Hollow Runner',
        'description': (
            'A swift, echoing apparition formed from the memory of stampedes.'
        )
    },
    {
        'npc_id': 'windcarve_spirit',
        'name': 'Windcarve Spirit',
        'description': (
            'A swirling presence shaped from carved tunnels and ancient wind currents.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'keeper_savran',
        'dialog_id': 'savran_intro',
        'dialog': [
            "The plains are uneasy. Even the docile beasts bare their teeth.",
            "Something ancient prowls the wind — a force that drives creatures wild.",
            "If we don’t stop it, the grasslands will tear themselves apart."
        ]
    },

    {
        'npc_id': 'waymaster_delphi',
        'dialog_id': 'delphi_intro',
        'dialog': [
            "Caravans vanish without a trace.",
            "The wind carries roars that don’t belong to any living creature.",
            "Whatever’s out there is disrupting every route I know."
        ]
    },

    {
        'npc_id': 'trail_reader_vexa',
        'dialog_id': 'vexa_intro',
        'dialog': [
            "The wind scars tell a story of frenzy.",
            "Herds stampede in patterns no beast would choose.",
            "A Steppe‑Spirit wakes — hungry for motion, hungry for chaos."
        ]
    },

    {
        'npc_id': 'hollow_runner',
        'dialog_id': 'hollow_runner_intro',
        'dialog': [
            "The Hollows echo with thunderous hooves.",
            "The Steppe’s breath stirs the earth.",
            "It waits deeper within the wind‑carved tunnels."
        ]
    },

    {
        'npc_id': 'windcarve_spirit',
        'dialog_id': 'windcarve_spirit_intro',
        'dialog': [
            "The Den howls with ancient fury.",
            "The Roaring Steppe gathers strength.",
            "Only its heart remains to be stilled."
        ]
    },

    {
        'npc_id': 'keeper_savran',
        'dialog_id': 'savran_closing',
        'dialog': [
            "The plains calm. The beasts breathe easy again.",
            "You’ve tamed a force older than any creature I’ve known.",
            "The grasslands owe you their peace."
        ]
    }

]


TASKS = [
	{
		'task_id': 'grassland_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'keeper_savran',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'keeper_savran',
					'standing_text': [ 
						"I’ve seen beasts you’d never believe—sit and I’ll tell you their names."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'waymaster_delphi',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'waymaster_delphi',
					'standing_text': [ 
						"Travelers bring tales—share one and I’ll show you a path worth taking."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_large_city_meet_savran'
                }
            }
		]		
	},

    # Task 1 — Meet Savran after initialization
    {
        'task_id': 'grassland_large_city_meet_savran',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'keeper_savran',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'keeper_savran',
                    'standing_text': [
                        "The beasts are restless. Even the gentle ones snarl at shadows.",
                        "Something stirs across the plains."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'keeper_savran',
                    'dialog_id': 'savran_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_large_city_meet_delphi'
                }
            }
        ]
    },

    # Task 2 — Meet Delphi for the caravan perspective
    {
        'task_id': 'grassland_large_city_meet_delphi',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'waymaster_delphi',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'waymaster_delphi',
                    'dialog_id': 'delphi_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'waymaster_delphi',
                    'standing_text': [
                        "Trade routes are collapsing. Caravans vanish without a trace.",
                        "Whatever’s causing this moves with the wind."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_large_city_find_vexa'
                }
            }
        ]
    },

    # Task 3 — Find Trail‑Reader Vexa in the open grasslands
    {
        'task_id': 'grassland_large_city_find_vexa',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'trail_reader_vexa',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'trail_reader_vexa',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'trail_reader_vexa',
                    'standing_text': [
                        "The wind carries claw‑marks today.",
                        "Something drives the herds into madness."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'trail_reader_vexa',
                    'dialog_id': 'vexa_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_large_city_stampede_hollows'
                }
            }
        ]
    },

    # Task 4 — Explore the Stampede Hollows (first dungeon)
    {
        'task_id': 'grassland_large_city_stampede_hollows',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'hollow_runner',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'stampede_hollows',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'hollow_runner',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'hollow_runner',
                    'dialog_id': 'hollow_runner_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_large_city_windcarve_den'
                }
            }
        ]
    },

    # Task 5 — Descend into the Windcarve Den (second dungeon)
    {
        'task_id': 'grassland_large_city_windcarve_den',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'windcarve_spirit',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'windcarve_den',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'windcarve_spirit',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'windcarve_spirit',
                    'dialog_id': 'windcarve_spirit_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_large_city_roaring_steppe'
                }
            }
        ]
    },

    # Task 6 — Defeat the Roaring Steppe (boss dungeon)
    {
        'task_id': 'grassland_large_city_roaring_steppe',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'roaring_steppe_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_roaring_steppe',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'roaring_steppe_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'keeper_savran',
                    'dialog_id': 'savran_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'grassland_large_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
    'story_id': 'grassland_large_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}