ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'forgehand_belkan',
		'name': 'Belkan Forgehand',
		'description': (
			'A master smith who trains apprentices in the Fellowship’s traditions.'
			' Belkan’s hammer strikes ring with rhythmic precision.'
			' He believes metal reveals its true nature only under pressure.'
		)
	},
	{
		'npc_id': 'marshal_korla',
		'name': 'Korla Deepdelve',
		'description': (
			'A disciplined marshal who organizes expeditions into the mountain depths.'
			' Korla’s armor is etched with maps of tunnels long since collapsed.'
			' She carries herself with the confidence of someone who has survived the dark.'
		)
	},
    {
        'npc_id': 'depth_seer_thalric',
        'name': 'Thalric the Depth‑Seer',
        'description': (
            'A tunnel mystic who reads fault‑echoes and senses disturbances in the deep stone.'
        )
    },
    {
        'npc_id': 'forgefall_echo',
        'name': 'Forgefall Echo',
        'description': (
            'A spectral remnant of abandoned forges, awakened by the Ashen Anvil.'
        )
    },
    {
        'npc_id': 'deepcoil_spirit',
        'name': 'Deepcoil Spirit',
        'description': (
            'A molten apparition formed from stolen forge‑heat deep within the Foundry.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'forgehand_belkan',
        'dialog_id': 'belkan_intro',
        'dialog': [
            "The forge cools too quickly.",
            "Heat drains into the stone like it’s being stolen.",
            "Something below hungers for fire and metal."
        ]
    },

    {
        'npc_id': 'marshal_korla',
        'dialog_id': 'korla_intro',
        'dialog': [
            "Tunnels collapse in deliberate patterns.",
            "Something shifts the stone with intent.",
            "If we don’t act, the depths will swallow the village."
        ]
    },

    {
        'npc_id': 'depth_seer_thalric',
        'dialog_id': 'thalric_intro',
        'dialog': [
            "The fault‑echoes tremble.",
            "A forge‑spirit stirs — the Ashen Anvil.",
            "If it rises, all metal will bend to its will."
        ]
    },

    {
        'npc_id': 'forgefall_echo',
        'dialog_id': 'forgefall_echo_intro',
        'dialog': [
            "We are the forges that fell silent.",
            "The Anvil calls us back to flame.",
            "It waits deeper in the Foundry."
        ]
    },

    {
        'npc_id': 'deepcoil_spirit',
        'dialog_id': 'deepcoil_spirit_intro',
        'dialog': [
            "The Foundry coils with stolen heat.",
            "The Anvil gathers strength.",
            "Only its heart remains to be shattered."
        ]
    },

    {
        'npc_id': 'forgehand_belkan',
        'dialog_id': 'belkan_closing',
        'dialog': [
            "The forges breathe again.",
            "The metal sings true once more.",
            "You’ve saved our craft — and our future."
        ]
    }

]


TASKS = [
	{
		'task_id': 'mountains_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'forgehand_belkan',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'forgehand_belkan',
					'standing_text': [ 
						"The anvil sings; rest your feet and tell me where the road has taken you."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'marshal_korla',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'marshal_korla',
					'standing_text': [ 
						"I’ve walked dark tunnels for years—sit and share a watch, and I’ll share what I’ve learned."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_small_city_meet_belkan'
                }
            }
		]		
	},

    # Task 1 — Meet Belkan after initialization
    {
        'task_id': 'mountains_small_city_meet_belkan',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'forgehand_belkan',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'forgehand_belkan',
                    'standing_text': [
                        "The metal cools too quickly these days.",
                        "Something deep below steals the forge’s heat."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'forgehand_belkan',
                    'dialog_id': 'belkan_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_small_city_meet_korla'
                }
            }
        ]
    },

    # Task 2 — Meet Korla for the expedition perspective
    {
        'task_id': 'mountains_small_city_meet_korla',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'marshal_korla',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'marshal_korla',
                    'dialog_id': 'korla_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'marshal_korla',
                    'standing_text': [
                        "Tunnels collapse in patterns I’ve never seen.",
                        "Something shifts the stone on purpose."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_small_city_find_thalric'
                }
            }
        ]
    },

    # Task 3 — Find Depth‑Seer Thalric in the open mountains
    {
        'task_id': 'mountains_small_city_find_thalric',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'depth_seer_thalric',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'depth_seer_thalric',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'depth_seer_thalric',
                    'standing_text': [
                        "The fault‑echoes tremble.",
                        "A forge‑spirit stirs beneath the Ashen halls."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'depth_seer_thalric',
                    'dialog_id': 'thalric_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_small_city_forgefall_tunnels'
                }
            }
        ]
    },

    # Task 4 — Explore the Forgefall Tunnels (first dungeon)
    {
        'task_id': 'mountains_small_city_forgefall_tunnels',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'forgefall_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'forgefall_tunnels',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'forgefall_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'forgefall_echo',
                    'dialog_id': 'forgefall_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_small_city_deepcoil_foundry'
                }
            }
        ]
    },

    # Task 5 — Descend into the Deepcoil Foundry (second dungeon)
    {
        'task_id': 'mountains_small_city_deepcoil_foundry',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'deepcoil_spirit',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'deepcoil_foundry',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'deepcoil_spirit',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'deepcoil_spirit',
                    'dialog_id': 'deepcoil_spirit_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_small_city_ashen_anvil'
                }
            }
        ]
    },

    # Task 6 — Defeat the Ashen Anvil (boss dungeon)
    {
        'task_id': 'mountains_small_city_ashen_anvil',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'ashen_anvil_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_ashen_anvil',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'ashen_anvil_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'forgehand_belkan',
                    'dialog_id': 'belkan_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'mountains_small_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
    'story_id': 'mountains_small_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}