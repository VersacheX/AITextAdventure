ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'vigilant_karrek',
		'name': 'Karrek Windbreak',
		'description': (
			'A hardened watchman who stands guard through the fiercest storms.'
			' Karrek’s cloak is patched with scraps from past expeditions.'
			' He claims the wind itself warns him of approaching danger.'
		)
	},
	{
		'npc_id': 'survivor_mira',
		'name': 'Mira Frostline',
		'description': (
			'A resourceful trader who deals in survival gear and hard‑earned wisdom.'
			' Mira’s smile is rare but genuine, like sunlight on fresh snow.'
			' She has a story for every scar she carries.'
		)
	},
    {
        'npc_id': 'gale_seer_orlena',
        'name': 'Orlena the Gale‑Seer',
        'description': (
            'A wind‑reader who interprets storm glyphs drifting through the snow and senses stolen warnings.'
        )
    },
    {
        'npc_id': 'windscar_echo',
        'name': 'Windscar Echo',
        'description': (
            'A spectral remnant of wind‑borne warnings twisted by the Frozen Warning.'
        )
    },
    {
        'npc_id': 'stormhollow_voice',
        'name': 'Stormhollow Voice',
        'description': (
            'A whispering presence formed from stolen storm‑omens deep within the Crevasse.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'vigilant_karrek',
        'dialog_id': 'karrek_intro',
        'dialog': [
            "The wind’s warnings blur.",
            "Storm signs vanish before I can read them.",
            "Something hides danger beneath the snow."
        ]
    },

    {
        'npc_id': 'survivor_mira',
        'dialog_id': 'mira_intro',
        'dialog': [
            "The snow forgets too quickly.",
            "Stories storms should leave behind fade in moments.",
            "If we don’t act, travelers will walk blind into danger."
        ]
    },

    {
        'npc_id': 'gale_seer_orlena',
        'dialog_id': 'orlena_intro',
        'dialog': [
            "The storm glyphs twist.",
            "A Frozen Warning rises — a spirit of stolen omens.",
            "If it awakens fully, the wind will fall silent."
        ]
    },

    {
        'npc_id': 'windscar_echo',
        'dialog_id': 'windscar_echo_intro',
        'dialog': [
            "We are the warnings the wind once carried.",
            "The Frozen Warning twists our echoes.",
            "It waits deeper in the Stormhollow Crevasse."
        ]
    },

    {
        'npc_id': 'stormhollow_voice',
        'dialog_id': 'stormhollow_voice_intro',
        'dialog': [
            "The Crevasse hums with stolen wind.",
            "The Frozen Warning gathers strength.",
            "Only its heart remains to be stilled."
        ]
    },

    {
        'npc_id': 'vigilant_karrek',
        'dialog_id': 'karrek_closing',
        'dialog': [
            "The wind speaks clearly again.",
            "Storm signs return to the cliffs.",
            "You’ve restored the voice of the Snowlands."
        ]
    }

]


TASKS = [
	{
		'task_id': 'snow_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'vigilant_karrek',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'vigilant_karrek',
					'standing_text': [ 
						"The wind speaks of travelers—stand with me and tell what you've seen."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'survivor_mira',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'survivor_mira',
					'standing_text': [ 
						"Snow keeps memories; share one and I'll warm you with a story."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_small_city_regional_complete_gate'
                }
            }
		]		
	},
    {
        'task_id': 'snow_small_city_regional_complete_gate',
        'type': 'complete_regional_quests',
        'task_acquire_events': [],
        'task_complete_events': [            
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_small_city_meet_karrek'
                }
            }
        ]

    },

    # Task 1 — Meet Karrek after initialization
    {
        'task_id': 'snow_small_city_meet_karrek',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vigilant_karrek',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'vigilant_karrek',
                    'standing_text': [
                        "The wind’s warnings blur.",
                        "Storm signs vanish before I can read them."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vigilant_karrek',
                    'dialog_id': 'karrek_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_small_city_meet_mira'
                }
            }
        ]
    },

    # Task 2 — Meet Mira for the survival‑lore perspective
    {
        'task_id': 'snow_small_city_meet_mira',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'survivor_mira',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'survivor_mira',
                    'dialog_id': 'mira_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'survivor_mira',
                    'standing_text': [
                        "The snow keeps memories, but some fade too fast.",
                        "Something steals the stories storms should leave behind."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_small_city_find_orlena'
                }
            }
        ]
    },

    # Task 3 — Find Gale‑Seer Orlena in the open snowfields
    {
        'task_id': 'snow_small_city_find_orlena',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'gale_seer_orlena',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'gale_seer_orlena',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'gale_seer_orlena',
                    'standing_text': [
                        "The storm glyphs twist.",
                        "A Frozen Warning rises beneath the drifts."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'gale_seer_orlena',
                    'dialog_id': 'orlena_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_small_city_windscar_outpost'
                }
            }
        ]
    },

    # Task 4 — Explore the Windscar Outpost (first dungeon)
    {
        'task_id': 'snow_small_city_windscar_outpost',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'windscar_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'windscar_outpost',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'windscar_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'windscar_echo',
                    'dialog_id': 'windscar_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_small_city_stormhollow_crevasse'
                }
            }
        ]
    },

    # Task 5 — Descend into the Stormhollow Crevasse (second dungeon)
    {
        'task_id': 'snow_small_city_stormhollow_crevasse',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'stormhollow_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'stormhollow_crevasse',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'stormhollow_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'stormhollow_voice',
                    'dialog_id': 'stormhollow_voice_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_small_city_frozen_warning'
                }
            }
        ]
    },

    # Task 6 — Defeat the Frozen Warning (boss dungeon)
    {
        'task_id': 'snow_small_city_frozen_warning',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'frozen_warning_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_frozen_warning',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'frozen_warning_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vigilant_karrek',
                    'dialog_id': 'karrek_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'snow_small_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
    'story_id': 'snow_small_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}