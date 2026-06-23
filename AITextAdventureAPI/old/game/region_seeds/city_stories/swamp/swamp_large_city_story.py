ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'bonechanter_velis',
		'name': 'Velis Bonechanter',
		'description': (
			'A ritualist who arranges skeletal remains into sacred patterns.'
			' Velis speaks in low, rhythmic tones that echo unnaturally.'
			' She believes bones remember every life they once carried.'
		)
	},
	{
		'npc_id': 'reliquarist_morwen',
		'name': 'Morwen the Veil‑Whisper',
		'description': (
			'A soft‑spoken curator who tends to relics said to house lingering spirits.'
			' Morwen’s touch leaves faint trails of cold mist across metal and bone.'
			' She claims the reliquary murmurs warnings to those willing to listen.'
		)
	},
    {
        'npc_id': 'mire_seer_halveth',
        'name': 'Halveth the Mire‑Seer',
        'description': (
            'A swamp mystic who reads bone tides and senses when the dead shift in their rest.'
        )
    },
    {
        'npc_id': 'ossuary_whisper',
        'name': 'Ossuary Whisper',
        'description': (
            'A spectral remnant of drowned bones twisted by the Bone Drown.'
        )
    },
    {
        'npc_id': 'relicmire_voice',
        'name': 'Relicmire Voice',
        'description': (
            'A murmuring presence formed from drowned relics deep within the Sump.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'bonechanter_velis',
        'dialog_id': 'velis_intro',
        'dialog': [
            "The bones shift in their patterns.",
            "Their memories stir with unease.",
            "Something rises from the drowned past."
        ]
    },

    {
        'npc_id': 'reliquarist_morwen',
        'dialog_id': 'morwen_intro',
        'dialog': [
            "The relics murmur warnings.",
            "Their spirits tremble as though something calls to them.",
            "If we ignore this, the swamp will choke on its own dead."
        ]
    },

    {
        'npc_id': 'mire_seer_halveth',
        'dialog_id': 'halveth_intro',
        'dialog': [
            "The bone tides rise.",
            "A Bone Drown wakes — a spirit of drowned memory.",
            "If it awakens fully, the swamp will forget the living."
        ]
    },

    {
        'npc_id': 'ossuary_whisper',
        'dialog_id': 'ossuary_whisper_intro',
        'dialog': [
            "We are the bones that sank too deep.",
            "The Bone Drown twists our rest.",
            "It waits deeper in the Relicmire Sump."
        ]
    },

    {
        'npc_id': 'relicmire_voice',
        'dialog_id': 'relicmire_voice_intro',
        'dialog': [
            "The Sump churns with drowned relics.",
            "The Bone Drown gathers strength.",
            "Only its heart remains to be silenced."
        ]
    },

    {
        'npc_id': 'bonechanter_velis',
        'dialog_id': 'velis_closing',
        'dialog': [
            "The bones settle. Their memories quiet.",
            "You’ve stilled a hunger older than the swamp itself.",
            "The mire will remember your tread."
        ]
    }

]


TASKS = [
	{
		'task_id': 'swamp_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'bonechanter_velis',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'bonechanter_velis',
					'standing_text': [ 
						"Bones hum with stories—stay and let me arrange them into one." 
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'reliquarist_morwen',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'reliquarist_morwen',
					'standing_text': [ 
						"Relics whisper at night—come, and I will tell you what they grant and warn." 
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_large_city_meet_velis'
                }
            }
		]		
	},

    # Task 1 — Meet Velis after initialization
    {
        'task_id': 'swamp_large_city_meet_velis',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'bonechanter_velis',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'bonechanter_velis',
                    'standing_text': [
                        "The bones shift in their patterns.",
                        "Something stirs beneath the mire."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bonechanter_velis',
                    'dialog_id': 'velis_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_large_city_meet_morwen'
                }
            }
        ]
    },

    # Task 2 — Meet Morwen for the relic‑spirit perspective
    {
        'task_id': 'swamp_large_city_meet_morwen',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'reliquarist_morwen',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'reliquarist_morwen',
                    'dialog_id': 'morwen_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'reliquarist_morwen',
                    'standing_text': [
                        "The relics murmur louder.",
                        "Their warnings drip with dread."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_large_city_find_halveth'
                }
            }
        ]
    },

    # Task 3 — Find Mire‑Seer Halveth in the open swamp
    {
        'task_id': 'swamp_large_city_find_halveth',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'mire_seer_halveth',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'mire_seer_halveth',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'mire_seer_halveth',
                    'standing_text': [
                        "The bone tides rise.",
                        "A Bone Drown wakes beneath the muck."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'mire_seer_halveth',
                    'dialog_id': 'halveth_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_large_city_ossuary_slick'
                }
            }
        ]
    },

    # Task 4 — Explore the Ossuary Slick (first dungeon)
    {
        'task_id': 'swamp_large_city_ossuary_slick',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'ossuary_whisper',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'ossuary_slick',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'ossuary_whisper',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'ossuary_whisper',
                    'dialog_id': 'ossuary_whisper_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_large_city_relicmire_sump'
                }
            }
        ]
    },

    # Task 5 — Descend into the Relicmire Sump (second dungeon)
    {
        'task_id': 'swamp_large_city_relicmire_sump',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'relicmire_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'relicmire_sump',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'relicmire_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'relicmire_voice',
                    'dialog_id': 'relicmire_voice_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_large_city_bone_drown'
                }
            }
        ]
    },

    # Task 6 — Defeat the Bone Drown (boss dungeon)
    {
        'task_id': 'swamp_large_city_bone_drown',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'bone_drown_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_bone_drown',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'bone_drown_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bonechanter_velis',
                    'dialog_id': 'velis_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'swamp_large_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
    'story_id': 'swamp_large_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}