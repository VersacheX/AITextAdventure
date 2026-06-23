ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'rustscribe_gorvak',
		'name': 'Gorvak Rustscribe',
		'description': (
			'A gruff archivist who catalogs the city’s industrial relics.'
			' Gorvak’s hands are permanently stained with iron dust.'
			' He treats every rusted gear like a sacred artifact.'
		)
	},
	{
		'npc_id': 'relaytech_sindra',
		'name': 'Sindra Coilrunner',
		'description': (
			'A quick‑thinking technician who maintains the volatile relay conduits.'
			' Sparks dance across Sindra’s gloves as she works.'
			' She claims the machinery “talks back” when she listens closely.'
		)
	},
    {
        'npc_id': 'forge_seer_brannoc',
        'name': 'Brannoc the Forge‑Seer',
        'description': (
            'A hermit who listens to the mountain’s internal machinery. '
            'Brannoc senses disturbances in the ancient forges beneath the peaks.'
        )
    },
    {
        'npc_id': 'gearghost',
        'name': 'Gearghost',
        'description': (
            'A spectral remnant of long‑dead machinery, animated by the Iron Resonance.'
        )
    },
    {
        'npc_id': 'conduit_echo',
        'name': 'Conduit Echo',
        'description': (
            'A volatile presence formed from unstable relay energy deep within the Conduit Maw.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'rustscribe_gorvak',
        'dialog_id': 'gorvak_intro',
        'dialog': [
            "The relics hum louder than they should.",
            "Old gears turn without hands to guide them.",
            "Something deep below has awakened."
        ]
    },

    {
        'npc_id': 'relaytech_sindra',
        'dialog_id': 'sindra_intro',
        'dialog': [
            "The conduits spark in strange rhythms.",
            "It’s like the mountain is trying to speak.",
            "Whatever’s down there is messing with the relay grid."
        ]
    },

    {
        'npc_id': 'forge_seer_brannoc',
        'dialog_id': 'brannoc_intro',
        'dialog': [
            "The mountain’s heart‑gears turn again.",
            "A Resonance stirs — metal remembering its purpose.",
            "If it grows stronger, the whole range will shake itself apart."
        ]
    },

    {
        'npc_id': 'gearghost',
        'dialog_id': 'gearghost_intro',
        'dialog': [
            "We are the gears that died turning.",
            "The Resonance calls us back to motion.",
            "It waits deeper in the Conduit Maw."
        ]
    },

    {
        'npc_id': 'conduit_echo',
        'dialog_id': 'conduit_echo_intro',
        'dialog': [
            "The Maw hums with unstable power.",
            "The Resonance grows louder.",
            "Only its core remains to be silenced."
        ]
    },

    {
        'npc_id': 'rustscribe_gorvak',
        'dialog_id': 'gorvak_closing',
        'dialog': [
            "The mountain quiets. The gears rest again.",
            "You’ve stilled a force older than any forge.",
            "The peaks owe you their peace."
        ]
    }

]


TASKS = [
	{
		'task_id': 'mountains_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'rustscribe_gorvak',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rustscribe_gorvak',
					'standing_text': [ 
						"Old gears have songs—come, tell me what yours did before the rust."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'relaytech_sindra',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'relaytech_sindra',
					'standing_text': [ 
						"Sparks tell stories—share your curious misfires and I’ll laugh with you."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_meet_gorvak'
                }
            }
		]		
	},

    # Task 1 — Meet Gorvak after initialization
    {
        'task_id': 'mountains_large_city_meet_gorvak',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rustscribe_gorvak',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rustscribe_gorvak',
                    'standing_text': [
                        "The relics hum louder than usual.",
                        "Something deep below is waking the old gears."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rustscribe_gorvak',
                    'dialog_id': 'gorvak_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_meet_sindra'
                }
            }
        ]
    },

    # Task 2 — Meet Sindra for the conduit‑tech perspective
    {
        'task_id': 'mountains_large_city_meet_sindra',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'relaytech_sindra',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'relaytech_sindra',
                    'dialog_id': 'sindra_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'relaytech_sindra',
                    'standing_text': [
                        "The conduits spark in strange rhythms.",
                        "Feels like the mountain is trying to speak."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_find_brannoc'
                }
            }
        ]
    },

    # Task 3 — Find Forge‑Seer Brannoc in the open mountains
    {
        'task_id': 'mountains_large_city_find_brannoc',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'forge_seer_brannoc',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'forge_seer_brannoc',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'forge_seer_brannoc',
                    'standing_text': [
                        "The mountain groans. Its heart‑gears turn again.",
                        "A Resonance stirs in the deep forges."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'forge_seer_brannoc',
                    'dialog_id': 'brannoc_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_geargrave_pit'
                }
            }
        ]
    },

    # Task 4 — Explore the Geargrave Pit (first dungeon)
    {
        'task_id': 'mountains_large_city_geargrave_pit',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'gearghost',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'geargrave_pit',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'gearghost',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'gearghost',
                    'dialog_id': 'gearghost_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_conduit_maw'
                }
            }
        ]
    },

    # Task 5 — Descend into the Conduit Maw (second dungeon)
    {
        'task_id': 'mountains_large_city_conduit_maw',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'conduit_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'conduit_maw',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'conduit_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'conduit_echo',
                    'dialog_id': 'conduit_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_iron_resonance'
                }
            }
        ]
    },

    # Task 6 — Defeat the Iron Resonance (boss dungeon)
    {
        'task_id': 'mountains_large_city_iron_resonance',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'iron_resonance_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_iron_resonance',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'iron_resonance_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rustscribe_gorvak',
                    'dialog_id': 'gorvak_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'mountains_large_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
    'story_id': 'mountains_large_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}