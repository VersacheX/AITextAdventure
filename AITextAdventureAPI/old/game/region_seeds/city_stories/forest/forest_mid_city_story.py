ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'emberwitch_thera',
		'name': 'Thera of the Emberlight',
		'description': (
			'A witch whose lantern glows with shifting orange runes.'
			' Thera studies flame‑born spirits and believes each spark carries a prophecy.'
			' Her laughter crackles like burning cedar.'
		)
	},
	{
		'npc_id': 'alchemist_mirlo',
		'name': 'Mirlo the Moonbrewer',
		'description': (
			'A wide‑eyed alchemist obsessed with lunar infusions and bubbling concoctions.'
			' Mirlo’s potions glow with soft moonlight, even underground.'
			' He often forgets whether he’s brewing medicine or mild chaos.'
		)
	},
    {
        'npc_id': 'glimmer_hermit_vael',
        'name': 'Vael the Glimmer‑Hermit',
        'description': (
            'A wandering mystic who reads moon‑embers drifting through the forest. '
            'Vael senses disturbances where flame and night intertwine.'
        )
    },
    {
        'npc_id': 'riftspark',
        'name': 'Riftspark',
        'description': (
            'A flickering ember‑spirit born from unstable flame‑magic within the Embergrove Rift.'
        )
    },
    {
        'npc_id': 'lunarcask_shade',
        'name': 'Lunarcask Shade',
        'description': (
            'A spectral figure formed from condensed moonlight and alchemical fumes.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'emberwitch_thera',
        'dialog_id': 'thera_intro',
        'dialog': [
            "The lantern’s sparks twist into warnings.",
            "Something is merging flame‑spirits with moonlight.",
            "If it completes the ritual, night itself will change."
        ]
    },

    {
        'npc_id': 'alchemist_mirlo',
        'dialog_id': 'mirlo_intro',
        'dialog': [
            "My moonbrews keep reacting to a strange pulse.",
            "It’s like the forest is brewing something of its own.",
            "Whatever it is… it’s unstable."
        ]
    },

    {
        'npc_id': 'glimmer_hermit_vael',
        'dialog_id': 'vael_intro',
        'dialog': [
            "Moon‑embers drift toward the Rift.",
            "A Crucible forms — half flame, half night.",
            "If it awakens fully, the forest’s cycle will break."
        ]
    },

    {
        'npc_id': 'riftspark',
        'dialog_id': 'riftspark_intro',
        'dialog': [
            "The Rift burns cold and glows hot.",
            "The Crucible feeds on contradictions.",
            "It waits deeper below."
        ]
    },

    {
        'npc_id': 'lunarcask_shade',
        'dialog_id': 'lunarcask_shade_intro',
        'dialog': [
            "The Depths churn with lunar residue.",
            "The Crucible stirs, shaping a new night.",
            "Only its core remains to be shattered."
        ]
    },

    {
        'npc_id': 'emberwitch_thera',
        'dialog_id': 'thera_closing',
        'dialog': [
            "The Crucible is extinguished.",
            "The lantern’s sparks settle — the futures calm.",
            "You’ve kept the forest’s night from fracturing."
        ]
    }

]


TASKS = [
	{
		'task_id': 'forest_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'emberwitch_thera',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'emberwitch_thera',
					'standing_text': [ 
						"The lantern shows small futures; stay and see what tonight whispers to you."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'alchemist_mirlo',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'alchemist_mirlo',
					'standing_text': [ 
						"I tinker with moonlight; tell me a tale and I’ll brew it into a memory."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_meet_thera'
                }
            }
		]		
	},

    # Task 1 — Meet Thera after initialization
    {
        'task_id': 'forest_mid_city_meet_thera',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'emberwitch_thera',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'emberwitch_thera',
                    'standing_text': [
                        "The lantern flickers strangely tonight.",
                        "Its sparks show futures that shouldn't exist."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'emberwitch_thera',
                    'dialog_id': 'thera_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_meet_mirlo'
                }
            }
        ]
    },

    # Task 2 — Meet Mirlo for the alchemical angle
    {
        'task_id': 'forest_mid_city_meet_mirlo',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'alchemist_mirlo',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'alchemist_mirlo',
                    'dialog_id': 'mirlo_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'alchemist_mirlo',
                    'standing_text': [
                        "My moonbrews are reacting to something in the forest.",
                        "The glow is… wrong. Pulsing. Like it's alive."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_find_vael'
                }
            }
        ]
    },

    # Task 3 — Find Vael the Glimmer‑Hermit in the open forest
    {
        'task_id': 'forest_mid_city_find_vael',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'glimmer_hermit_vael',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'glimmer_hermit_vael',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'glimmer_hermit_vael',
                    'standing_text': [
                        "Moon‑embers drift toward the Rift.",
                        "Something stirs where flame and night entwine."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'glimmer_hermit_vael',
                    'dialog_id': 'vael_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_embergrove_rift'
                }
            }
        ]
    },

    # Task 4 — Explore the Embergrove Rift (first dungeon)
    {
        'task_id': 'forest_mid_city_embergrove_rift',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'riftspark',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'embergrove_rift',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'riftspark',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'riftspark',
                    'dialog_id': 'riftspark_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_lunarcask_depths'
                }
            }
        ]
    },

    # Task 5 — Descend into the Lunarcask Depths (second dungeon)
    {
        'task_id': 'forest_mid_city_lunarcask_depths',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lunarcask_shade',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'lunarcask_depths',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'lunarcask_shade',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'lunarcask_shade',
                    'dialog_id': 'lunarcask_shade_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_twilit_crucible'
                }
            }
        ]
    },

    # Task 6 — Defeat the Twilit Crucible (boss dungeon)
    {
        'task_id': 'forest_mid_city_twilit_crucible',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'twilit_crucible_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_twilit_crucible',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'twilit_crucible_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'emberwitch_thera',
                    'dialog_id': 'thera_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'forest_mid_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
    'story_id': 'forest_mid_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}