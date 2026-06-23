ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'curator_bramble',
		'name': 'Bramble the Curator',
		'description': (
			'A cheerful historian who preserves the village’s pastoral traditions.'
			'  Bramble’s satchel is filled with pressed flowers and old folk charms.'
			'  He treats every visitor like a long‑lost relative.'
		)
	},
	{
		'npc_id': 'librarian_sylfa',
		'name': 'Sylfa Meadowreader',
		'description': (
			'A soft‑spoken keeper of stories who reads by bioluminescent lanterns.'
			'  Sylfa believes books choose their readers, not the other way around.'
			'  Her calm demeanor soothes even the most road‑weary travelers.'
		)
	},
    {
        'npc_id': 'hearth_seer_marnel',
        'name': 'Marnel the Hearth‑Seer',
        'description': (
            'A wandering storyteller who senses when folk tales drift from their true paths.'
        )
    },
    {
        'npc_id': 'thicket_story',
        'name': 'Thicket Story',
        'description': (
            'A living tale grown wild within the Meadowtale Thicket.'
        )
    },
    {
        'npc_id': 'charmroot_voice',
        'name': 'Charmroot Voice',
        'description': (
            'A murmuring presence formed from corrupted folk charms deep in the Charmroot Den.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'curator_bramble',
        'dialog_id': 'bramble_intro',
        'dialog': [
            "The fields hum with strange tales.",
            "Folk charms twist into shapes I’ve never seen.",
            "Something meddles with our simplest stories."
        ]
    },

    {
        'npc_id': 'librarian_sylfa',
        'dialog_id': 'sylfa_intro',
        'dialog': [
            "Books whisper warnings.",
            "Stories shift when the meadow is uneasy.",
            "A Hollow spirit rewrites our gentlest lore."
        ]
    },

    {
        'npc_id': 'hearth_seer_marnel',
        'dialog_id': 'marnel_intro',
        'dialog': [
            "The meadow’s tales wander off their paths.",
            "A Folklore Hollow stirs beneath the roots.",
            "If it wakes fully, our traditions will turn against us."
        ]
    },

    {
        'npc_id': 'thicket_story',
        'dialog_id': 'thicket_story_intro',
        'dialog': [
            "We are the tales that grew wild.",
            "The Hollow twists us into danger.",
            "It waits deeper in the Charmroot Den."
        ]
    },

    {
        'npc_id': 'charmroot_voice',
        'dialog_id': 'charmroot_voice_intro',
        'dialog': [
            "The Den trembles with corrupted charms.",
            "The Hollow feeds on forgotten stories.",
            "Only its heart remains to be quieted."
        ]
    },

    {
        'npc_id': 'curator_bramble',
        'dialog_id': 'bramble_closing',
        'dialog': [
            "The fields breathe easy again.",
            "Our stories return to their gentle shapes.",
            "You’ve saved our traditions from being lost."
        ]
    }

]


TASKS = [
	{
		'task_id': 'grassland_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'curator_bramble',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'curator_bramble',
					'standing_text': [ 
						"Welcome! The fields have stories—sit and I'll tell you one."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'librarian_sylfa',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'librarian_sylfa',
					'standing_text': [ 
						"Books choose readers—perhaps one chose you. Care to listen?"
					]
				}
			}

		],
		'task_complete_events': [
		]		
	},

    # Task 1 — Meet Bramble after initialization
    {
        'task_id': 'grassland_small_city_meet_bramble',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'curator_bramble',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'curator_bramble',
                    'standing_text': [
                        "The fields whisper strange tales today.",
                        "Old charms twist into shapes I don’t recognize."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'curator_bramble',
                    'dialog_id': 'bramble_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_small_city_meet_sylfa'
                }
            }
        ]
    },

    # Task 2 — Meet Sylfa for the lorekeeper’s perspective
    {
        'task_id': 'grassland_small_city_meet_sylfa',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'librarian_sylfa',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'librarian_sylfa',
                    'dialog_id': 'sylfa_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'librarian_sylfa',
                    'standing_text': [
                        "Stories shift when the meadow is uneasy.",
                        "Something rewrites our gentlest tales."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_small_city_find_marnel'
                }
            }
        ]
    },

    # Task 3 — Find Hearth‑Seer Marnel in the open grasslands
    {
        'task_id': 'grassland_small_city_find_marnel',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'hearth_seer_marnel',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'hearth_seer_marnel',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'hearth_seer_marnel',
                    'standing_text': [
                        "The meadow’s tales wander off their paths.",
                        "A Hollow stirs beneath the folklore."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'hearth_seer_marnel',
                    'dialog_id': 'marnel_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_small_city_meadowtale_thicket'
                }
            }
        ]
    },

    # Task 4 — Explore the Meadowtale Thicket (first dungeon)
    {
        'task_id': 'grassland_small_city_meadowtale_thicket',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'thicket_story',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'meadowtale_thicket',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'thicket_story',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'thicket_story',
                    'dialog_id': 'thicket_story_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_small_city_charmroot_den'
                }
            }
        ]
    },

    # Task 5 — Descend into the Charmroot Den (second dungeon)
    {
        'task_id': 'grassland_small_city_charmroot_den',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'charmroot_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'charmroot_den',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'charmroot_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'charmroot_voice',
                    'dialog_id': 'charmroot_voice_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_small_city_folklore_hollow'
                }
            }
        ]
    },

    # Task 6 — Defeat the Folklore Hollow (boss dungeon)
    {
        'task_id': 'grassland_small_city_folklore_hollow',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'folklore_hollow_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_folklore_hollow',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'folklore_hollow_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'curator_bramble',
                    'dialog_id': 'bramble_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'grassland_small_city'
                }
            }
        ]
    }

]



PRIMARY_STORY_SETTINGS = {
    'story_id': 'grassland_small_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}