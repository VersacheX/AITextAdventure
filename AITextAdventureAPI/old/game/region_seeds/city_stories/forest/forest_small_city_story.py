ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'archivist_fernhollow',
		'name': 'Fernhollow',
		'description': (
			'A gentle historian who records the forest’s shifting lore.'
			' Fernhollow speaks to trees as though they are old friends.'
			' Their parchment always smells faintly of pine resin and rain.'
		)
	},
	{
		'npc_id': 'scout_lyss',
		'name': 'Lyss the Quiet Step',
		'description': (
			'A vigilant scout who hears disturbances long before they occur.'
			' Lyss meditates daily to attune her senses to the forest’s whispers.'
			' She rarely raises her voice, yet commands instant attention.'
		)
	},
    {
        'npc_id': 'whisper_moth_selen',
        'name': 'Whisper‑Moth Selen',
        'description': (
            'A soft‑spoken wanderer who follows drifting moth‑spirits that carry the forest’s memories.'
        )
    },
    {
        'npc_id': 'moth_echo',
        'name': 'Moth Echo',
        'description': (
            'A faint, fluttering apparition formed from forgotten stories and pale wing‑light.'
        )
    },
    {
        'npc_id': 'burrow_whisper',
        'name': 'Burrow Whisper',
        'description': (
            'A murmuring presence deep within the Echofern Burrows, shaped from lost recollections.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'archivist_fernhollow',
        'dialog_id': 'fernhollow_intro',
        'dialog': [
            "The forest forgets too much.",
            "Memories slip away like dew at dawn.",
            "Something steals our stories — gently, but relentlessly."
        ]
    },

    {
        'npc_id': 'scout_lyss',
        'dialog_id': 'lyss_intro',
        'dialog': [
            "The quiet is wrong.",
            "Even the wind hesitates to speak.",
            "Whatever silences the forest moves softly."
        ]
    },

    {
        'npc_id': 'whisper_moth_selen',
        'dialog_id': 'selen_intro',
        'dialog': [
            "The moths carry what the forest forgets.",
            "They drift toward a place where memories fade.",
            "Follow them, and you’ll find the thief of whispers."
        ]
    },

    {
        'npc_id': 'moth_echo',
        'dialog_id': 'moth_echo_intro',
        'dialog': [
            "We flutter with forgotten tales.",
            "The Silent Canopy drinks our voices.",
            "It waits deeper below."
        ]
    },

    {
        'npc_id': 'burrow_whisper',
        'dialog_id': 'burrow_whisper_intro',
        'dialog': [
            "The Burrows tremble with stolen memories.",
            "The Canopy grows stronger with each silence.",
            "Only its heart remains to be severed."
        ]
    },

    {
        'npc_id': 'archivist_fernhollow',
        'dialog_id': 'fernhollow_closing',
        'dialog': [
            "The forest breathes again.",
            "Its stories return like rain to thirsty soil.",
            "You’ve restored what was nearly lost."
        ]
    }

]


TASKS = [
	{
		'task_id': 'forest_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'archivist_fernhollow',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'archivist_fernhollow',
					'standing_text': [ 
						"Come read the old leaves with me; they hum of distant summers."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'scout_lyss',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scout_lyss',
					'standing_text': [ 
						"Quiet roads are a blessing—if you’ve tales, I’ll listen between steps."
					]
				}
			}

		],
		'task_complete_events': [
            { 'event_type': 'award_task', 'params': { 'task_id': 'forest_small_city_meet_fernhollow' } }
		]		
	},

    # Task 1 — Meet Fernhollow after initialization
    {
        'task_id': 'forest_small_city_meet_fernhollow',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'archivist_fernhollow',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'archivist_fernhollow',
                    'standing_text': [
                        "The leaves forget their stories too quickly.",
                        "Something steals the forest’s memories."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'archivist_fernhollow',
                    'dialog_id': 'fernhollow_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_meet_lyss'
                }
            }
        ]
    },

    # Task 2 — Meet Lyss for the scout’s perspective
    {
        'task_id': 'forest_small_city_meet_lyss',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'scout_lyss',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'scout_lyss',
                    'dialog_id': 'lyss_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'scout_lyss',
                    'standing_text': [
                        "The forest is too quiet.",
                        "Even the birds hesitate to speak."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_find_selen'
                }
            }
        ]
    },

    # Task 3 — Find Whisper‑Moth Selen in the open forest
    {
        'task_id': 'forest_small_city_find_selen',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'whisper_moth_selen',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'whisper_moth_selen',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'whisper_moth_selen',
                    'standing_text': [
                        "The moths drift toward the Passage.",
                        "They carry memories the forest has lost."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'whisper_moth_selen',
                    'dialog_id': 'selen_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_mothglade_passage'
                }
            }
        ]
    },

    # Task 4 — Explore the Mothglade Passage (first dungeon)
    {
        'task_id': 'forest_small_city_mothglade_passage',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'moth_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'mothglade_passage',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'moth_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'moth_echo',
                    'dialog_id': 'moth_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_echofern_burrows'
                }
            }
        ]
    },

    # Task 5 — Descend into the Echofern Burrows (second dungeon)
    {
        'task_id': 'forest_small_city_echofern_burrows',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'burrow_whisper',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'echofern_burrows',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'burrow_whisper',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'burrow_whisper',
                    'dialog_id': 'burrow_whisper_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_silent_canopy'
                }
            }
        ]
    },

    # Task 6 — Defeat the Silent Canopy (boss dungeon)
    {
        'task_id': 'forest_small_city_silent_canopy',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'silent_canopy_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_silent_canopy',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'silent_canopy_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'archivist_fernhollow',
                    'dialog_id': 'fernhollow_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'forest_small_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
    'story_id': 'forest_small_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}