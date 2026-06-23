ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'runeforger_bjorn',
		'name': 'Bjorn Runeforger',
		'description': (
			'A muscular craftsman who carves runes into weapons and armor.'
			' Bjorn’s forge burns with unnatural blue flame.'
			' He insists each rune must be sung into existence.'
		)
	},
	{
		'npc_id': 'speaker_yrsa',
		'name': 'Yrsa Icebound',
		'description': (
			'A mystic who communes with ancestral spirits through ritual chants.'
			' Yrsa’s voice resonates like wind across frozen cliffs.'
			' She carries the weight of countless whispered histories.'
		)
	},
    {
        'npc_id': 'chant_seer_haldrin',
        'name': 'Haldrin the Chant‑Seer',
        'description': (
            'A mystic who hears rune echoes trapped in the ice and senses when chants fracture.'
        )
    },
    {
        'npc_id': 'rimechant_echo',
        'name': 'Rimechant Echo',
        'description': (
            'A spectral remnant of frozen chants twisted by the Shattered Rune.'
        )
    },
    {
        'npc_id': 'blueforge_spirit',
        'name': 'Blueforge Spirit',
        'description': (
            'A molten‑blue apparition formed from unstable flame deep within the Blueforge Depths.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'runeforger_bjorn',
        'dialog_id': 'bjorn_intro',
        'dialog': [
            "The runes resist the flame.",
            "Their meanings twist beneath the ice.",
            "Something breaks their song."
        ]
    },

    {
        'npc_id': 'speaker_yrsa',
        'dialog_id': 'yrsa_intro',
        'dialog': [
            "The chants echo wrong.",
            "Ancestral voices strain to reach us.",
            "A force blocks their path."
        ]
    },

    {
        'npc_id': 'chant_seer_haldrin',
        'dialog_id': 'haldrin_intro',
        'dialog': [
            "The rune echoes fracture.",
            "A Shattered Rune rises — a spirit of broken chants.",
            "If it awakens fully, the ancestors will fall silent."
        ]
    },

    {
        'npc_id': 'rimechant_echo',
        'dialog_id': 'rimechant_echo_intro',
        'dialog': [
            "We are the chants that froze wrong.",
            "The Shattered Rune twists our echoes.",
            "It waits deeper in the Blueforge Depths."
        ]
    },

    {
        'npc_id': 'blueforge_spirit',
        'dialog_id': 'blueforge_spirit_intro',
        'dialog': [
            "The Depths burn with unstable blue flame.",
            "The Shattered Rune gathers strength.",
            "Only its heart remains to be stilled."
        ]
    },

    {
        'npc_id': 'runeforger_bjorn',
        'dialog_id': 'bjorn_closing',
        'dialog': [
            "The runes sing true again.",
            "The forge burns steady.",
            "You’ve restored the voice of the ancestors."
        ]
    }

]


TASKS = [
	{
		'task_id': 'snow_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'runeforger_bjorn',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'runeforger_bjorn',
					'standing_text': [ 
						"Runes remember deeds—sit by the forge and tell me one of yours."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'speaker_yrsa',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'speaker_yrsa',
					'standing_text': [ 
						"Ancestral winds carry many tales—speak softly and the cliffs will answer."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_meet_bjorn'
                }
            }
		]		
	},

    # Task 1 — Meet Bjorn after initialization
    {
        'task_id': 'snow_mid_city_meet_bjorn',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'runeforger_bjorn',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'runeforger_bjorn',
                    'standing_text': [
                        "The runes resist the flame.",
                        "Something twists their meaning beneath the ice."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'runeforger_bjorn',
                    'dialog_id': 'bjorn_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_meet_yrsa'
                }
            }
        ]
    },

    # Task 2 — Meet Yrsa for the ancestral‑chant perspective
    {
        'task_id': 'snow_mid_city_meet_yrsa',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'speaker_yrsa',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'speaker_yrsa',
                    'dialog_id': 'yrsa_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'speaker_yrsa',
                    'standing_text': [
                        "The chants echo wrong.",
                        "Ancestral voices strain as though something blocks them."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_find_haldrin'
                }
            }
        ]
    },

    # Task 3 — Find Chant‑Seer Haldrin in the open snowfields
    {
        'task_id': 'snow_mid_city_find_haldrin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'chant_seer_haldrin',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'chant_seer_haldrin',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'chant_seer_haldrin',
                    'standing_text': [
                        "The rune echoes fracture.",
                        "A Shattered Rune stirs beneath the frost."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'chant_seer_haldrin',
                    'dialog_id': 'haldrin_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_rimechant_hall'
                }
            }
        ]
    },

    # Task 4 — Explore the Rimechant Hall (first dungeon)
    {
        'task_id': 'snow_mid_city_rimechant_hall',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rimechant_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'rimechant_hall',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'rimechant_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rimechant_echo',
                    'dialog_id': 'rimechant_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_blueforge_depths'
                }
            }
        ]
    },

    # Task 5 — Descend into the Blueforge Depths (second dungeon)
    {
        'task_id': 'snow_mid_city_blueforge_depths',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'blueforge_spirit',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'blueforge_depths',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'blueforge_spirit',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'blueforge_spirit',
                    'dialog_id': 'blueforge_spirit_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_shattered_rune'
                }
            }
        ]
    },

    # Task 6 — Defeat the Shattered Rune (boss dungeon)
    {
        'task_id': 'snow_mid_city_shattered_rune',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'shattered_rune_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_shattered_rune',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'shattered_rune_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'runeforger_bjorn',
                    'dialog_id': 'bjorn_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'snow_mid_city'
                }
            }
        ]
    }

]



PRIMARY_STORY_SETTINGS = {
	'story_id': 'snow_mid_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}