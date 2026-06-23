ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'warden_harrock',
		'name': 'Harrock the Cliff‑Warden',
		'description': (
			'A stoic guardian who ensures travelers survive the treacherous paths.'
			' Harrock’s voice carries like distant thunder across the cliffs.'
			' He has an uncanny sense for impending rockslides.'
		)
	},
	{
		'npc_id': 'emberguide_ryla',
		'name': 'Ryla Emberguide',
		'description': (
			'A fire‑touched wanderer who teaches survival through controlled flame.'
			' Ryla’s campfires burn with unnatural colors, shifting with her mood.'
			' She believes every ember remembers the mountain’s ancient fury.'
		)
	},
    {
        'npc_id': 'avalanche_seer_korrin',
        'name': 'Korrin the Avalanche‑Seer',
        'description': (
            'A hermit who reads fall‑lines and predicts collapses. '
            'Korrin senses disturbances in the mountain’s pressure and stone.'
        )
    },
    {
        'npc_id': 'fallshadow_echo',
        'name': 'Fallshadow Echo',
        'description': (
            'A spectral remnant of ancient rockslides, awakened by the Shatterpeak Core.'
        )
    },
    {
        'npc_id': 'emberwake_spirit',
        'name': 'Emberwake Spirit',
        'description': (
            'A fiery apparition formed from unstable heat deep within the Emberwake Cavern.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'warden_harrock',
        'dialog_id': 'harrock_intro',
        'dialog': [
            "The cliffs rumble without warning.",
            "Rockfalls strike where the paths were once safe.",
            "Something beneath the mountain shifts in its sleep."
        ]
    },

    {
        'npc_id': 'emberguide_ryla',
        'dialog_id': 'ryla_intro',
        'dialog': [
            "My flames burn in colors I’ve never seen.",
            "The mountain’s fury stirs in the embers.",
            "If it wakes fully, the cliffs will tear themselves apart."
        ]
    },

    {
        'npc_id': 'avalanche_seer_korrin',
        'dialog_id': 'korrin_intro',
        'dialog': [
            "The fall‑lines tremble with warning.",
            "A Core awakens — pressure, flame, and stone given will.",
            "If it rises, the whole range will collapse."
        ]
    },

    {
        'npc_id': 'fallshadow_echo',
        'dialog_id': 'fallshadow_echo_intro',
        'dialog': [
            "We are the echoes of old collapses.",
            "The Core calls the cliffs to fall again.",
            "It waits deeper in the Emberwake Cavern."
        ]
    },

    {
        'npc_id': 'emberwake_spirit',
        'dialog_id': 'emberwake_spirit_intro',
        'dialog': [
            "The Cavern burns with ancient fury.",
            "The Core gathers strength.",
            "Only its heart remains to be stilled."
        ]
    },

    {
        'npc_id': 'warden_harrock',
        'dialog_id': 'harrock_closing',
        'dialog': [
            "The cliffs quiet. The paths are safe again.",
            "You’ve stilled a force older than the mountain winds.",
            "Travelers will owe you their lives for generations."
        ]
    }

]


TASKS = [
	{
		'task_id': 'mountains_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'warden_harrock',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'warden_harrock',
					'standing_text': [ 
						"The cliffs hum with memory—if you’ve a story of survival, I’ll listen."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'emberguide_ryla',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'emberguide_ryla',
					'standing_text': [ 
						"Share a flame and a tale—our fires remember the names of brave travelers."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_mid_city_meet_harrock'
                }
            }
		]		
	},

    # Task 1 — Meet Harrock after initialization
    {
        'task_id': 'mountains_mid_city_meet_harrock',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'warden_harrock',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'warden_harrock',
                    'standing_text': [
                        "The cliffs rumble more each day.",
                        "Rockfalls strike without warning — something shifts beneath us."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'warden_harrock',
                    'dialog_id': 'harrock_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_mid_city_meet_ryla'
                }
            }
        ]
    },

    # Task 2 — Meet Ryla for the ember‑ritual perspective
    {
        'task_id': 'mountains_mid_city_meet_ryla',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'emberguide_ryla',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'emberguide_ryla',
                    'dialog_id': 'ryla_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'emberguide_ryla',
                    'standing_text': [
                        "My flames burn in strange colors.",
                        "The mountain’s fury stirs — I can feel it in the embers."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_mid_city_find_korrin'
                }
            }
        ]
    },

    # Task 3 — Find Avalanche‑Seer Korrin in the open mountains
    {
        'task_id': 'mountains_mid_city_find_korrin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'avalanche_seer_korrin',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'avalanche_seer_korrin',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'avalanche_seer_korrin',
                    'standing_text': [
                        "The fall‑lines tremble.",
                        "A Core awakens beneath the Shatterpeak."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'avalanche_seer_korrin',
                    'dialog_id': 'korrin_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_mid_city_fallshadow_crevasse'
                }
            }
        ]
    },

    # Task 4 — Explore the Fallshadow Crevasse (first dungeon)
    {
        'task_id': 'mountains_mid_city_fallshadow_crevasse',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'fallshadow_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'fallshadow_crevasse',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'fallshadow_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'fallshadow_echo',
                    'dialog_id': 'fallshadow_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_mid_city_emberwake_cavern'
                }
            }
        ]
    },

    # Task 5 — Descend into the Emberwake Cavern (second dungeon)
    {
        'task_id': 'mountains_mid_city_emberwake_cavern',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'emberwake_spirit',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'emberwake_cavern',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'emberwake_spirit',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'emberwake_spirit',
                    'dialog_id': 'emberwake_spirit_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_mid_city_shatterpeak_core'
                }
            }
        ]
    },

    # Task 6 — Defeat the Shatterpeak Core (boss dungeon)
    {
        'task_id': 'mountains_mid_city_shatterpeak_core',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'shatterpeak_core_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_shatterpeak_core',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'shatterpeak_core_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'warden_harrock',
                    'dialog_id': 'harrock_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'mountains_mid_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
    'story_id': 'mountains_mid_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}