ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'kadeem',
		'name': 'Kadeem',
		'description': (
			'A wiry, quick-tongued merchant who runs a stall within The Black Market Guild. '
			'He moves rare and illicit goods through shadowed backrooms, always watching for opportunity.'
		)
	},
	{
		'npc_id': 'mara',
		'name': 'Mara',
		'description': (
			"A smooth, well-dressed broker who operates out of Broker's Hideout. "
			'She arranges favors, introductions, and discreet exchanges for the right price.'
		)
	},
    {
        'npc_id': 'rhyla',
        'name': 'Rhyla the Echo-Binder',
        'description': (
            'A desert mystic who can hear the “songs” of shifting dunes. '
            'She studies the Dune Choir and knows their ancient patterns.'
        )
    }
]

NPCS += [
    {
        'npc_id': 'choir_echo',
        'name': 'Choir Echo',
        'description': (
            'A humanoid shape formed from vibrating sand. It speaks in layered voices, '
            'each one a memory of the desert.'
        )
    },
    {
        'npc_id': 'archive_voice',
        'name': 'Archive Voice',
        'description': (
            'A spectral librarian of the Sunken Archive, bound to drifting shelves of half-buried knowledge.'
        )
    }
]


NPC_DIALOG = [
	{
		'npc_id': 'kadeem',
		'dialog_id': 'kadeem_intro',
		'dialog': [
			"You look like someone who appreciates a good find.",
			"I can get you curious trinkets, weapons with a story, or information—for a fee, of course."
		]
	},
	{
		'npc_id': 'mara',
		'dialog_id': 'mara_intro',
		'dialog': [
			"Business moves fast in The Desert Metropolis. Know the right people and doors open.",
			"If you need a contact or a hush-hush job handled, I can broker the arrangement—provided you can pay."
		]
	}
]
NPC_DIALOG += [

    {
        'npc_id': 'rhyla',
        'dialog_id': 'rhyla_intro',
        'dialog': [
            "You feel it, don't you? The desert humming beneath your feet.",
            "Zaruun cracked something open. Now the Dune Choir stirs.",
            "If we don't silence them, the whole region will collapse into song and sand."
        ]
    },

    {
        'npc_id': 'choir_echo',
        'dialog_id': 'choir_echo_intro',
        'dialog': [
            "We are the Choir. We are the memory of sand.",
            "You walk on our bodies. You breathe our dust.",
            "You cannot silence what was here before you."
        ]
    },

    {
        'npc_id': 'archive_voice',
        'dialog_id': 'archive_voice_intro',
        'dialog': [
            "The Archive remembers every collapse.",
            "Zaruun was only the first crack. You are the second.",
            "The Glass Maw waits below."
        ]
    },

    {
        'npc_id': 'rhyla',
        'dialog_id': 'rhyla_closing',
        'dialog': [
            "It's done. The Choir falls quiet again.",
            "For now, the desert holds. But it never forgets.",
            "Travel well, wanderer. The sands will remember your steps."
        ]
    }

]


TASKS = [
	{
		'task_id': 'desert_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'kadeem',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'kadeem',
					'standing_text': [ 
						"Care to browse?"
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'mara',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mara',
					'standing_text': [ 
						"Looking for something particular, or just lost in the heat?"
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_meet_kadeem'
                }
            }
		]		
	},

    # Task 1 — Speak to Kadeem after city initialization
    {
        'task_id': 'desert_large_city_meet_kadeem',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'kadeem',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'kadeem',
                    'standing_text': [
                        "Strange shipments have been coming in from the deep desert.",
                        "Sand that hums. Stones that whisper. Something's stirring out there."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'kadeem',
                    'dialog_id': 'kadeem_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_meet_mara'
                }
            }
        ]
    },

    # Task 2 — Speak to Mara for the first real hook
    {
        'task_id': 'desert_large_city_meet_mara',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'mara',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'mara',
                    'dialog_id': 'mara_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'mara',
                    'standing_text': [
                        "If you're looking for trouble, the desert has plenty.",
                        "A new faction is moving out there—something old, something loud."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_find_rhyla'
                }
            }
        ]
    },

    # Task 3 — Find Rhyla the Echo-Binder in the open desert
    {
        'task_id': 'desert_large_city_find_rhyla',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rhyla',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'rhyla',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rhyla',
                    'standing_text': [
                        "The desert is singing again.",
                        "And not the kind of song you want to hear."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rhyla',
                    'dialog_id': 'rhyla_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_choir_outpost'
                }
            }
        ]
    },

    # Task 4 — Investigate the first Dune Choir outpost (dungeon)
    {
        'task_id': 'desert_large_city_choir_outpost',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'choir_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'choir_outpost',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'choir_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'choir_echo',
                    'dialog_id': 'choir_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_sunken_archive'
                }
            }
        ]
    },

    # Task 5 — Explore the Sunken Archive (second dungeon)
    {
        'task_id': 'desert_large_city_sunken_archive',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'archive_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'sunken_archive',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'archive_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'archive_voice',
                    'dialog_id': 'archive_voice_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_glass_maw'
                }
            }
        ]
    },

    # Task 6 — Defeat the Glass Maw (boss dungeon)
    {
        'task_id': 'desert_large_city_glass_maw',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'glass_maw_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'glass_maw',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'glass_maw_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rhyla',
                    'dialog_id': 'rhyla_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'desert_large'
                }
            }
        ]
    }

]



PRIMARY_STORY_SETTINGS = {
	'story_id': 'desert_large_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}