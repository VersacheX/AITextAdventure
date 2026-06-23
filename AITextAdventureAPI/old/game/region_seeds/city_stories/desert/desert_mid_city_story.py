ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'velra_the_indexer',
		'name': 'Velra the Indexer',
		'description': (
			'A meticulous archivist who speaks in clipped, deliberate phrases.'
			' Velra claims the Vaults whisper to her, guiding her to lost records and forbidden histories.'
			' Her eyes flicker with bioluminescent ink, a side effect of decades spent cataloging arcane relics.'
		)
	},
	{
		'npc_id': 'shade_broker_kavren',
		'name': 'Kavren the Shade‑Broker',
		'description': (
			'A soft‑spoken information dealer who trades in secrets rather than coin.'
			' Kavren maintains a web of unseen contacts throughout Nightveil Spire.'
			' His presence is unsettlingly calm, as though he already knows the outcome of every conversation.'
		)
	},
    {
        'npc_id': 'archivist_warden_threx',
        'name': 'Archivist‑Warden Threx',
        'description': (
            'A half‑mechanical guardian built to maintain the Vaults. '
            'Threx’s voice crackles with static and ancient protocol.'
        )
    },
    {
        'npc_id': 'vault_whisper',
        'name': 'Vault Whisper',
        'description': (
            'A disembodied voice formed from drifting script‑dust. '
            'It speaks in half‑sentences and broken memories.'
        )
    },
    {
        'npc_id': 'ink_specter',
        'name': 'Ink Specter',
        'description': (
            'A ghostly figure made of liquid ink, shifting between shapes as though searching for a lost identity.'
        )
    }
]


NPC_DIALOG = [
    {
        'npc_id': 'velra_the_indexer',
        'dialog_id': 'velra_intro',
        'dialog': [
            "Records vanish. Entire entries gone.",
            "The Vaults whisper of an intruder — a script that devours meaning.",
            "If you descend, do not trust what remembers you."
        ]
    },

    {
        'npc_id': 'shade_broker_kavren',
        'dialog_id': 'kavren_intro',
        'dialog': [
            "People come to me to hide their secrets.",
            "But now secrets are hiding themselves.",
            "Someone is erasing identities from the inside out."
        ]
    },

    {
        'npc_id': 'archivist_warden_threx',
        'dialog_id': 'threx_intro',
        'dialog': [
            "Designation: Threx. Archivist‑Warden.",
            "The Vaults breach. Containment failing.",
            "The Erasure feeds. You must descend."
        ]
    },

    {
        'npc_id': 'vault_whisper',
        'dialog_id': 'vault_whisper_intro',
        'dialog': [
            "You hear us. Good.",
            "The script crawls. It eats names first.",
            "Yours tastes bright."
        ]
    },

    {
        'npc_id': 'ink_specter',
        'dialog_id': 'ink_specter_intro',
        'dialog': [
            "Ink remembers what flesh forgets.",
            "The Erasure waits below, hungry for your outline.",
            "Turn back, or be rewritten."
        ]
    },

    {
        'npc_id': 'velra_the_indexer',
        'dialog_id': 'velra_closing',
        'dialog': [
            "The Vaults quiet. The script retreats.",
            "You have preserved what remains of us.",
            "I will index your name myself — so it cannot be erased."
        ]
    }

]


TASKS = [
	{
		'task_id': 'desert_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'velra_the_indexer',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'velra_the_indexer',
					'standing_text': [ 
						"Hello. The Vaults whisper; what do you seek?"
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'shade_broker_kavren',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'shade_broker_kavren',
					'standing_text': [ 
						"I know names and rumors. Tell me yours, and perhaps I can help."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_mid_city_meet_velra'
                }
            }
		]		
	},

    # Task 1 — Meet Velra after initialization
    {
        'task_id': 'desert_mid_city_meet_velra',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'velra_the_indexer',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'velra_the_indexer',
                    'standing_text': [
                        "The Vaults shift again. Something is rewriting the catalog.",
                        "If you hear whispers, do not answer them."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'velra_the_indexer',
                    'dialog_id': 'velra_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_mid_city_meet_kavren'
                }
            }
        ]
    },

    # Task 2 — Meet Kavren for the shadow‑side of the mystery
    {
        'task_id': 'desert_mid_city_meet_kavren',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'shade_broker_kavren',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'shade_broker_kavren',
                    'dialog_id': 'kavren_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'shade_broker_kavren',
                    'standing_text': [
                        "Names are disappearing from my ledgers.",
                        "Someone — or something — is erasing people."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_mid_city_find_threx'
                }
            }
        ]
    },

    # Task 3 — Find Archivist‑Warden Threx in the open desert
    {
        'task_id': 'desert_mid_city_find_threx',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'archivist_warden_threx',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'archivist_warden_threx',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'archivist_warden_threx',
                    'standing_text': [
                        "The Vaults breach. Protocols failing.",
                        "Identity integrity compromised."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'archivist_warden_threx',
                    'dialog_id': 'threx_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_mid_city_lower_vaults'
                }
            }
        ]
    },

    # Task 4 — Explore the Lower Vaults (first dungeon)
    {
        'task_id': 'desert_mid_city_lower_vaults',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vault_whisper',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'lower_vaults',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'vault_whisper',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vault_whisper',
                    'dialog_id': 'vault_whisper_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_mid_city_inkwell_depths'
                }
            }
        ]
    },

    # Task 5 — Descend into the Inkwell Depths (second dungeon)
    {
        'task_id': 'desert_mid_city_inkwell_depths',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'ink_specter',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'inkwell_depths',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'ink_specter',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'ink_specter',
                    'dialog_id': 'ink_specter_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_mid_city_erasure_chamber'
                }
            }
        ]
    },

    # Task 6 — Defeat The Erasure (boss dungeon)
    {
        'task_id': 'desert_mid_city_erasure_chamber',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'erasure_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_erasure_chamber',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'erasure_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'velra_the_indexer',
                    'dialog_id': 'velra_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'desert_mid_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
	'story_id': 'desert_mid_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}