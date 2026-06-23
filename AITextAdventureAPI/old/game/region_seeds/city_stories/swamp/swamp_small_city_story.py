ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'bogrunner_tavik',
		'name': 'Tavik Bogrunner',
		'description': (
			'A wiry trader who ferries goods through the swamp’s most treacherous channels.'
			' Tavik’s skiff is patched with mismatched planks and swamp‑etched runes.'
			' He claims the bog itself shows him safe paths when danger rises.'
		)
	},
	{
		'npc_id': 'rotwharf_madra',
		'name': 'Madra Rotwharf',
		'description': (
			'A hardened broker who deals in illicit wares dredged from the swamp’s depths.'
			' Madra’s voice is rough, as though she’s swallowed too much swamp fog.'
			' She knows every outlaw, fugitive, and mercenary who passes through Hollow’s shadows.'
		)
	},
    {
        'npc_id': 'channel_seer_draveth',
        'name': 'Draveth the Channel‑Seer',
        'description': (
            'A swamp navigator who reads current‑signs and senses when routes vanish beneath the mire.'
        )
    },
    {
        'npc_id': 'murkchannel_echo',
        'name': 'Murkchannel Echo',
        'description': (
            'A spectral remnant of forgotten channels twisted by the Swallowed Path.'
        )
    },
    {
        'npc_id': 'rotfen_voice',
        'name': 'Rotfen Voice',
        'description': (
            'A whispering presence formed from lost routes deep within the Hideaway.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'bogrunner_tavik',
        'dialog_id': 'tavik_intro',
        'dialog': [
            "The channels twist where they once ran straight.",
            "The swamp hides its own paths.",
            "Something swallows the routes we trust."
        ]
    },

    {
        'npc_id': 'rotwharf_madra',
        'dialog_id': 'madra_intro',
        'dialog': [
            "Shadows move wrong in Hollow.",
            "Smugglers vanish on routes they’ve walked for years.",
            "If we don’t act, the swamp will claim every traveler."
        ]
    },

    {
        'npc_id': 'channel_seer_draveth',
        'dialog_id': 'draveth_intro',
        'dialog': [
            "The current‑signs vanish.",
            "A Swallowed Path rises — a spirit of devoured routes.",
            "If it awakens fully, no one will find their way out."
        ]
    },

    {
        'npc_id': 'murkchannel_echo',
        'dialog_id': 'murkchannel_echo_intro',
        'dialog': [
            "We are the channels the swamp forgot.",
            "The Swallowed Path twists our flow.",
            "It waits deeper in the Rotfen Hideaway."
        ]
    },

    {
        'npc_id': 'rotfen_voice',
        'dialog_id': 'rotfen_voice_intro',
        'dialog': [
            "The Hideaway churns with lost routes.",
            "The Swallowed Path gathers strength.",
            "Only its heart remains to be severed."
        ]
    },

    {
        'npc_id': 'bogrunner_tavik',
        'dialog_id': 'tavik_closing',
        'dialog': [
            "The channels clear. The swamp breathes easier.",
            "You’ve restored the paths the mire tried to swallow.",
            "Travelers will owe you their lives."
        ]
    }

]


TASKS = [
	{
		'task_id': 'swamp_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'bogrunner_tavik',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'bogrunner_tavik',
					'standing_text': [ 
						"The channels whisper secrets—ride with me and tell what the swamp showed you."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'rotwharf_madra',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rotwharf_madra',
					'standing_text': [ 
						"Hollow's shadows remember faces—stay and tell me what brought you here."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_meet_tavik'
                }
            }
		]		
	},

    # Task 1 — Meet Tavik after initialization
    {
        'task_id': 'swamp_small_city_meet_tavik',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'bogrunner_tavik',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bogrunner_tavik',
                    'dialog_id': 'tavik_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'bogrunner_tavik',
                    'standing_text': [
                        "The channels twist where they once ran straight.",
                        "Something hides the safe paths."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_meet_madra'
                }
            }
        ]
    },

    # Task 2 — Meet Madra for the outlaw‑network perspective
    {
        'task_id': 'swamp_small_city_meet_madra',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rotwharf_madra',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rotwharf_madra',
                    'dialog_id': 'madra_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rotwharf_madra',
                    'standing_text': [
                        "Shadows move wrong in Hollow.",
                        "Someone — or something — is swallowing the routes smugglers rely on."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_find_draveth'
                }
            }
        ]
    },

    # Task 3 — Find Channel‑Seer Draveth in the open swamp
    {
        'task_id': 'swamp_small_city_find_draveth',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'channel_seer_draveth',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'channel_seer_draveth',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'channel_seer_draveth',
                    'standing_text': [
                        "The current‑signs vanish.",
                        "A Swallowed Path rises beneath the murk."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'channel_seer_draveth',
                    'dialog_id': 'draveth_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_murkchannel_run'
                }
            }
        ]
    },

    # Task 4 — Explore the Murkchannel Run (first dungeon)
    {
        'task_id': 'swamp_small_city_murkchannel_run',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'murkchannel_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'murkchannel_run',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'murkchannel_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'murkchannel_echo',
                    'dialog_id': 'murkchannel_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_rotfen_hideaway'
                }
            }
        ]
    },

    # Task 5 — Descend into the Rotfen Hideaway (second dungeon)
    {
        'task_id': 'swamp_small_city_rotfen_hideaway',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rotfen_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'rotfen_hideaway',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'rotfen_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rotfen_voice',
                    'dialog_id': 'rotfen_voice_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_swallowed_path'
                }
            }
        ]
    },

    # Task 6 — Defeat the Swallowed Path (boss dungeon)
    {
        'task_id': 'swamp_small_city_swallowed_path',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'swallowed_path_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_swallowed_path',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'swallowed_path_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bogrunner_tavik',
                    'dialog_id': 'tavik_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'swamp_small_city'
                }
            }
        ]
    }

]



PRIMARY_STORY_SETTINGS = {
	'story_id': 'swamp_small_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}