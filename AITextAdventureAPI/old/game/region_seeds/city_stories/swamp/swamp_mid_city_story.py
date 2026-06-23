ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'bargaincaller_ress',
		'name': 'Ress the Mire‑Caller',
		'description': (
			'A shrewd dealmaker who trades in charms, curses, and swamp‑born oddities.'
			' Ress’s lantern glows with shifting green fire that reacts to lies.'
			' He insists every bargain struck in the Court binds both fate and fortune.'
		)
	},
	{
		'npc_id': 'lanternsworn_janrel',
		'name': 'Janrel of the Lantern‑Sworn',
		'description': (
			'A mystic who reads omens in the flicker of swamp‑light flames.'
			' Janrel’s lantern never extinguishes, even in heavy rain.'
			' She offers guidance to the lost, though her advice often sounds like prophecy.'
		)
	},
    {
        'npc_id': 'oath_reed_selka',
        'name': 'Selka the Oath‑Reed',
        'description': (
            'A swamp oath‑reader who interprets reed‑signs that shift when promises break.'
        )
    },
    {
        'npc_id': 'lanternbog_echo',
        'name': 'Lanternbog Echo',
        'description': (
            'A spectral remnant of drowned lantern‑light twisted by the Broken Pact.'
        )
    },
    {
        'npc_id': 'oathrot_voice',
        'name': 'Oathrot Voice',
        'description': (
            'A whispering presence formed from rotted vows deep within the Channel.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'bargaincaller_ress',
        'dialog_id': 'ress_intro',
        'dialog': [
            "The lantern-fire flares at every lie.",
            "Bargains twist in ways no mortal hand could shape.",
            "Something rewrites the Court’s fate‑threads."
        ]
    },

    {
        'npc_id': 'lanternsworn_janrel',
        'dialog_id': 'janrel_intro',
        'dialog': [
            "The lantern’s flame flickers in impossible patterns.",
            "Omen-light bends toward something hidden.",
            "If we ignore this, the swamp will lose its way."
        ]
    },

    {
        'npc_id': 'oath_reed_selka',
        'dialog_id': 'selka_intro',
        'dialog': [
            "The reeds whisper of broken promises.",
            "A Broken Pact rises — a spirit of violated bargains.",
            "If it awakens fully, no oath will hold in this mire."
        ]
    },

    {
        'npc_id': 'lanternbog_echo',
        'dialog_id': 'lanternbog_echo_intro',
        'dialog': [
            "We are the lanterns that drowned in lies.",
            "The Broken Pact twists our light.",
            "It waits deeper in the Oathrot Channel."
        ]
    },

    {
        'npc_id': 'oathrot_voice',
        'dialog_id': 'oathrot_voice_intro',
        'dialog': [
            "The Channel rots with broken vows.",
            "The Broken Pact gathers strength.",
            "Only its heart remains to be severed."
        ]
    },

    {
        'npc_id': 'bargaincaller_ress',
        'dialog_id': 'ress_closing',
        'dialog': [
            "The lantern-fire steadies.",
            "The Court’s bargains hold true again.",
            "You’ve restored fate to the swamp."
        ]
    }

]


TASKS = [
	{
		'task_id': 'swamp_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'bargaincaller_ress',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'bargaincaller_ress',
					'standing_text': [ 
						"Charms and curses have stories—tell me yours and I will listen."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'lanternsworn_janrel',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'lanternsworn_janrel',
					'standing_text': [ 
						"The lantern sees more than light—sit and speak, and I will share what it shows."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_mid_city_meet_ress'
                }
            }
		]		
	},

    # Task 1 — Meet Ress after initialization
    {
        'task_id': 'swamp_mid_city_meet_ress',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'bargaincaller_ress',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'bargaincaller_ress',
                    'standing_text': [
                        "The lantern-fire flares at every lie.",
                        "Something twists the bargains struck in this mire."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bargaincaller_ress',
                    'dialog_id': 'ress_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_mid_city_meet_janrel'
                }
            }
        ]
    },

    # Task 2 — Meet Janrel for the omen‑lantern perspective
    {
        'task_id': 'swamp_mid_city_meet_janrel',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lanternsworn_janrel',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'lanternsworn_janrel',
                    'dialog_id': 'janrel_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'lanternsworn_janrel',
                    'standing_text': [
                        "The lantern’s flame flickers in patterns I’ve never seen.",
                        "Omen-light bends as though something rewrites fate."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_mid_city_find_selka'
                }
            }
        ]
    },

    # Task 3 — Find Oath‑Reed Selka in the open swamp
    {
        'task_id': 'swamp_mid_city_find_selka',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'oath_reed_selka',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'oath_reed_selka',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'oath_reed_selka',
                    'standing_text': [
                        "The reeds whisper of broken promises.",
                        "A Broken Pact rises beneath the lanternbog."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'oath_reed_selka',
                    'dialog_id': 'selka_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_mid_city_lanternbog_crossing'
                }
            }
        ]
    },

    # Task 4 — Explore the Lanternbog Crossing (first dungeon)
    {
        'task_id': 'swamp_mid_city_lanternbog_crossing',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lanternbog_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'lanternbog_crossing',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'lanternbog_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'lanternbog_echo',
                    'dialog_id': 'lanternbog_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_mid_city_oathrot_channel'
                }
            }
        ]
    },

    # Task 5 — Descend into the Oathrot Channel (second dungeon)
    {
        'task_id': 'swamp_mid_city_oathrot_channel',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'oathrot_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'oathrot_channel',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'oathrot_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'oathrot_voice',
                    'dialog_id': 'oathrot_voice_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_mid_city_broken_pact'
                }
            }
        ]
    },

    # Task 6 — Defeat the Broken Pact (boss dungeon)
    {
        'task_id': 'swamp_mid_city_broken_pact',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'broken_pact_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_broken_pact',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'broken_pact_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bargaincaller_ress',
                    'dialog_id': 'ress_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'swamp_mid_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
    'story_id': 'swamp_mid_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}