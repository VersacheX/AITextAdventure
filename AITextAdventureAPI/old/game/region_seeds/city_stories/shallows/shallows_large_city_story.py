ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'saltcaller_renlo',
		'name': 'Renlo Saltcaller',
		'description': (
			'A boisterous trader who smells perpetually of sea brine.'
			' Renlo’s booming laugh echoes across the market stalls.'
			' He claims to predict storms by tasting the air.'
		)
	},
	{
		'npc_id': 'vaultkeeper_syrin',
		'name': 'Syrin of the Harborlight',
		'description': (
			'A quiet curator who safeguards relics dredged from shipwrecks.'
			' Syrin’s lantern glows with a pale, underwater shimmer.'
			' She speaks as though every artifact carries a ghost.'
		)
	},
    {
        'npc_id': 'tide_seer_marenna',
        'name': 'Marenna the Tide‑Seer',
        'description': (
            'A wandering mystic who reads tide scars and hears drowned voices carried by the wind.'
        )
    },
    {
        'npc_id': 'stormtide_echo',
        'name': 'Stormtide Echo',
        'description': (
            'A spectral remnant of markets destroyed by ancient storms.'
        )
    },
    {
        'npc_id': 'undertow_voice',
        'name': 'Undertow Voice',
        'description': (
            'A murmuring presence formed from drowned memories deep within the Undertow Vault.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'saltcaller_renlo',
        'dialog_id': 'renlo_intro',
        'dialog': [
            "The air tastes wrong.",
            "Storms gather where the sky is clear.",
            "Something beneath the waves stirs the winds."
        ]
    },

    {
        'npc_id': 'vaultkeeper_syrin',
        'dialog_id': 'syrin_intro',
        'dialog': [
            "The relics glow brighter.",
            "They whisper of a Beacon drowned long ago.",
            "If it rises, the tides will follow."
        ]
    },

    {
        'npc_id': 'tide_seer_marenna',
        'dialog_id': 'marenna_intro',
        'dialog': [
            "The tide scars tremble.",
            "A Beacon stirs — a storm‑spirit born of shipwreck light.",
            "If it awakens, the sea will reclaim the coast."
        ]
    },

    {
        'npc_id': 'stormtide_echo',
        'dialog_id': 'stormtide_echo_intro',
        'dialog': [
            "We are the markets the storm devoured.",
            "The Beacon calls the tides to rise again.",
            "It waits deeper in the Undertow Vault."
        ]
    },

    {
        'npc_id': 'undertow_voice',
        'dialog_id': 'undertow_voice_intro',
        'dialog': [
            "The Vault churns with drowned memories.",
            "The Beacon gathers strength.",
            "Only its heart remains to be stilled."
        ]
    },

    {
        'npc_id': 'saltcaller_renlo',
        'dialog_id': 'renlo_closing',
        'dialog': [
            "The winds calm. The tides settle.",
            "You’ve stilled a storm older than the coast itself.",
            "The Shallows owe you their peace."
        ]
    }

]


TASKS = [
	{
		'task_id': 'shallows_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'saltcaller_renlo',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'saltcaller_renlo',
					'standing_text': [ 
						"Storms and stories—sit and taste the salt while I tell you of the last gale."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'vaultkeeper_syrin',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'vaultkeeper_syrin',
					'standing_text': [ 
						"Relics remember their voyages—if you listen, the sea will tell you its name."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_meet_renlo'
                }
            }
		]		
	},

    # Task 1 — Meet Renlo after initialization
    {
        'task_id': 'shallows_large_city_meet_renlo',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'saltcaller_renlo',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'saltcaller_renlo',
                    'standing_text': [
                        "The air tastes wrong today.",
                        "Storms gather where the sky is clear."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'saltcaller_renlo',
                    'dialog_id': 'renlo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_meet_syrin'
                }
            }
        ]
    },

    # Task 2 — Meet Syrin for the relic‑curator perspective
    {
        'task_id': 'shallows_large_city_meet_syrin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vaultkeeper_syrin',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'dialog_id': 'syrin_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'standing_text': [
                        "The relics glow brighter.",
                        "Something beneath the waves calls to them."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_find_marenna'
                }
            }
        ]
    },

    # Task 3 — Find Tide‑Seer Marenna in the open shallows
    {
        'task_id': 'shallows_large_city_find_marenna',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'tide_seer_marenna',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'tide_seer_marenna',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'tide_seer_marenna',
                    'standing_text': [
                        "The tide scars whisper.",
                        "A Beacon stirs beneath the drowned paths."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'tide_seer_marenna',
                    'dialog_id': 'marenna_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_stormtide_market_ruins'
                }
            }
        ]
    },

    # Task 4 — Explore the Stormtide Market Ruins (first dungeon)
    {
        'task_id': 'shallows_large_city_stormtide_market_ruins',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'stormtide_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'stormtide_market_ruins',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'stormtide_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'stormtide_echo',
                    'dialog_id': 'stormtide_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_undertow_vault'
                }
            }
        ]
    },

    # Task 5 — Descend into the Undertow Vault (second dungeon)
    {
        'task_id': 'shallows_large_city_undertow_vault',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'undertow_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'undertow_vault',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'undertow_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'undertow_voice',
                    'dialog_id': 'undertow_voice_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_drowned_beacon'
                }
            }
        ]
    },

    # Task 6 — Defeat the Drowned Beacon (boss dungeon)
    {
        'task_id': 'shallows_large_city_drowned_beacon',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'drowned_beacon_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_drowned_beacon',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'drowned_beacon_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'saltcaller_renlo',
                    'dialog_id': 'renlo_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'shallows_large_city'
                }
            }
        ]
    }

]



PRIMARY_STORY_SETTINGS = {
	'story_id': 'shallows_large_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}