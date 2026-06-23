ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'sparkwire_Jexa',
		'name': 'Jexa Sparkwire',
		'description': (
			'A scavenger‑engineer who grafts glowing circuitry into salvaged tech.'
			'  Jexa treats every broken device like a wounded animal needing care.'
			'  Her workshop hums with neon pulses that mirror her restless energy.'
		)
	},
	{
		'npc_id': 'morrowdeal_krayt',
		'name': 'Krayt Morrowdeal',
		'description': (
			'A desert‑hardened trader who deals exclusively in contraband and curios.'
			'  Krayt’s voice is gravelly from years of dust storms and whispered negotiations.'
			'  He claims the Bazaar chooses its merchants, not the other way around.'
		)
	},
    {
        'npc_id': 'scrap_seer_venn',
        'name': 'Scrap‑Seer Venn',
        'description': (
            'A desert hermit who claims to “hear” the emotions of broken machines. '
            'Venn wanders scrap fields collecting stories from discarded tech.'
        )
    },
    {
        'npc_id': 'hollow_echo',
        'name': 'Hollow Echo',
        'description': (
            'A glitching apparition formed from corrupted scrap‑data. '
            'Its voice stutters like a damaged audio log.'
        )
    },
    {
        'npc_id': 'signal_wraith',
        'name': 'Signal Wraith',
        'description': (
            'A shimmering figure made of distorted radio waves and static. '
            'It flickers between frequencies as it speaks.'
        )
    }
]



NPC_DIALOG = [

    {
        'npc_id': 'sparkwire_Jexa',
        'dialog_id': 'Jexa_intro',
        'dialog': [
            "Something's wrong with the tech around here.",
            "Devices are waking up on their own — humming, twitching, overheating.",
            "Feels like a sick machine crying for help."
        ]
    },

    {
        'npc_id': 'morrowdeal_krayt',
        'dialog_id': 'krayt_intro',
        'dialog': [
            "A relic passed through the Bazaar last week.",
            "Looked harmless. Felt cursed.",
            "Now the whole district buzzes like a dying generator."
        ]
    },

    {
        'npc_id': 'scrap_seer_venn',
        'dialog_id': 'venn_intro',
        'dialog': [
            "You hear the static too. Good.",
            "The broken ones scream of a Heart beating too fast.",
            "Follow the noise. It will find you."
        ]
    },

    {
        'npc_id': 'hollow_echo',
        'dialog_id': 'hollow_echo_intro',
        'dialog': [
            "The Hollows remember every discarded thing.",
            "The Heart feeds on what you throw away.",
            "It grows stronger with every spark."
        ]
    },

    {
        'npc_id': 'signal_wraith',
        'dialog_id': 'signal_wraith_intro',
        'dialog': [
            "Your signal is clean. Rare.",
            "The Heart wants to rewrite you.",
            "Run, or burn bright."
        ]
    },

    {
        'npc_id': 'sparkwire_Jexa',
        'dialog_id': 'Jexa_closing',
        'dialog': [
            "You did it. The Heart’s gone quiet.",
            "Circuits are stable again — for now.",
            "If anything starts humming at night, bring it straight to me."
        ]
    }

]


TASKS = [
	{
		'task_id': 'desert_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'sparkwire_Jexa',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sparkwire_Jexa',
					'standing_text': [ 
						"I mend what others discard — sit and tell me how it broke."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'morrowdeal_krayt',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'morrowdeal_krayt',
					'standing_text': [ 
						"The Bazaar has stories for every ear — pull up a crate and share one."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_meet_Jexa'
                }
            }
		]		
	},

    # Task 1 — Meet Jexa after initialization
    {
        'task_id': 'desert_small_city_meet_Jexa',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'sparkwire_Jexa',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'sparkwire_Jexa',
                    'standing_text': [
                        "Circuits are acting strange lately. Like they're dreaming.",
                        "If your gear starts humming on its own, bring it to me."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'sparkwire_Jexa',
                    'dialog_id': 'Jexa_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_meet_krayt'
                }
            }
        ]
    },

    # Task 2 — Meet Krayt for the contraband angle
    {
        'task_id': 'desert_small_city_meet_krayt',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'morrowdeal_krayt',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'morrowdeal_krayt',
                    'dialog_id': 'krayt_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'morrowdeal_krayt',
                    'standing_text': [
                        "Someone brought a relic through the Bazaar last week.",
                        "Now half the tech in the district is glitching."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_find_venn'
                }
            }
        ]
    },

    # Task 3 — Find Scrap‑Seer Venn in the open desert
    {
        'task_id': 'desert_small_city_find_venn',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'scrap_seer_venn',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'scrap_seer_venn',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'scrap_seer_venn',
                    'standing_text': [
                        "Shhh. The broken ones are speaking.",
                        "Their pain points toward the Hollows."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'scrap_seer_venn',
                    'dialog_id': 'venn_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_scrap_hollows'
                }
            }
        ]
    },

    # Task 4 — Explore the Scrap Hollows (first dungeon)
    {
        'task_id': 'desert_small_city_scrap_hollows',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'hollow_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'scrap_hollows',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'hollow_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'hollow_echo',
                    'dialog_id': 'hollow_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_signal_wastes'
                }
            }
        ]
    },

    # Task 5 — Traverse the Signal Wastes (second dungeon)
    {
        'task_id': 'desert_small_city_signal_wastes',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'signal_wraith',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'signal_wastes',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'signal_wraith',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'signal_wraith',
                    'dialog_id': 'signal_wraith_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_overclocked_heart'
                }
            }
        ]
    },

    # Task 6 — Defeat the Overclocked Heart (boss dungeon)
    {
        'task_id': 'desert_small_city_overclocked_heart',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'overclocked_heart_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_overclocked_heart',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'overclocked_heart_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'sparkwire_Jexa',
                    'dialog_id': 'Jexa_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'desert_small_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
    'story_id': 'desert_small_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}