ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'signalwatch_errol',
		'name': 'Errol Signalwatch',
		'description': (
			'A vigilant lookout who monitors the coastline for danger.'
			' Errol’s signal flags move with flawless precision, even in storms.'
			' He claims he can read the sea’s intentions like a book.'
		)
	},
	{
		'npc_id': 'runner_sylka',
		'name': 'Sylka the Cove‑Runner',
		'description': (
			'A swift courier who navigates hidden passages beneath the docks.'
			' Sylka’s boots are always damp with seawater and secrets.'
			' She knows every smuggler’s route but keeps her own path hidden.'
		)
	},
    {
        'npc_id': 'mist_seer_loryth',
        'name': 'Loryth the Mist‑Seer',
        'description': (
            'A fog‑reader who interprets drifting mist glyphs and senses drowned warnings.'
        )
    },
    {
        'npc_id': 'fogwhisper_echo',
        'name': 'Fogwhisper Echo',
        'description': (
            'A spectral remnant of lost coastal warnings swallowed by fog.'
        )
    },
    {
        'npc_id': 'coveveil_voice',
        'name': 'Coveveil Voice',
        'description': (
            'A whispering presence formed from hidden cove passages and drowned secrets.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'signalwatch_errol',
        'dialog_id': 'errol_intro',
        'dialog': [
            "The sea’s signals blur.",
            "Flags read wrong even when the wind is steady.",
            "Something hides warnings beneath the fog."
        ]
    },

    {
        'npc_id': 'runner_sylka',
        'dialog_id': 'sylka_intro',
        'dialog': [
            "Hidden routes feel wrong.",
            "The fog watches back.",
            "If we don’t act, the coves will swallow travelers whole."
        ]
    },

    {
        'npc_id': 'mist_seer_loryth',
        'dialog_id': 'loryth_intro',
        'dialog': [
            "The mist glyphs twist.",
            "A Silent Buoy rises — a spirit of drowned warnings.",
            "If it awakens, the coast will lose its voice."
        ]
    },

    {
        'npc_id': 'fogwhisper_echo',
        'dialog_id': 'fogwhisper_echo_intro',
        'dialog': [
            "We are the warnings the fog devoured.",
            "The Silent Buoy twists our signals.",
            "It waits deeper in the Coveveil Passage."
        ]
    },

    {
        'npc_id': 'coveveil_voice',
        'dialog_id': 'coveveil_voice_intro',
        'dialog': [
            "The Passage hums with stolen warnings.",
            "The Silent Buoy gathers strength.",
            "Only its heart remains to be dimmed."
        ]
    },

    {
        'npc_id': 'signalwatch_errol',
        'dialog_id': 'errol_closing',
        'dialog': [
            "The fog clears. The signals return.",
            "You’ve restored the coast’s voice.",
            "The Shallows will remember your vigilance."
        ]
    }

]


TASKS = [
	{
		'task_id': 'shallows_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'signalwatch_errol',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'signalwatch_errol',
					'standing_text': [ 
						"The sea speaks in flags—watch with me and tell me what you spy."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'runner_sylka',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'runner_sylka',
					'standing_text': [ 
						"Hidden coves have stories—whisper one to me between the waves."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_small_city_meet_errol'
                }
            }
		]		
	},

    # Task 1 — Meet Errol after initialization
    {
        'task_id': 'shallows_small_city_meet_errol',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'signalwatch_errol',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'signalwatch_errol',
                    'standing_text': [
                        "The sea’s signals blur.",
                        "Flags read wrong even when the wind is steady."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'signalwatch_errol',
                    'dialog_id': 'errol_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_small_city_meet_sylka'
                }
            }
        ]
    },

    # Task 2 — Meet Sylka for the cove‑runner’s perspective
    {
        'task_id': 'shallows_small_city_meet_sylka',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'runner_sylka',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'runner_sylka',
                    'dialog_id': 'sylka_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'runner_sylka',
                    'standing_text': [
                        "Hidden routes feel wrong.",
                        "Something in the fog watches back."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_small_city_find_loryth'
                }
            }
        ]
    },

    # Task 3 — Find Mist‑Seer Loryth in the open shallows
    {
        'task_id': 'shallows_small_city_find_loryth',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'mist_seer_loryth',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'mist_seer_loryth',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'mist_seer_loryth',
                    'standing_text': [
                        "The mist glyphs twist.",
                        "A Silent Buoy rises beneath the fog."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'mist_seer_loryth',
                    'dialog_id': 'loryth_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_small_city_fogwhisper_inlet'
                }
            }
        ]
    },

    # Task 4 — Explore the Fogwhisper Inlet (first dungeon)
    {
        'task_id': 'shallows_small_city_fogwhisper_inlet',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'fogwhisper_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'fogwhisper_inlet',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'fogwhisper_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'fogwhisper_echo',
                    'dialog_id': 'fogwhisper_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_small_city_coveveil_passage'
                }
            }
        ]
    },

    # Task 5 — Descend into the Coveveil Passage (second dungeon)
    {
        'task_id': 'shallows_small_city_coveveil_passage',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'coveveil_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'coveveil_passage',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'coveveil_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'coveveil_voice',
                    'dialog_id': 'coveveil_voice_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_small_city_silent_buoy'
                }
            }
        ]
    },

    # Task 6 — Defeat the Silent Buoy (boss dungeon)
    {
        'task_id': 'shallows_small_city_silent_buoy',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'silent_buoy_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_silent_buoy',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'silent_buoy_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'signalwatch_errol',
                    'dialog_id': 'errol_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'shallows_small_city'
                }
            }
        ]
    }

]



PRIMARY_STORY_SETTINGS = {
    'story_id': 'shallows_small_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}