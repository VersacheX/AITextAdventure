ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'elder_saphrin',
		'name': 'Saphrin the Hollow‑Keeper',
		'description': (
			'A serene elder who oversees the Exchange with ritualistic precision.'
			' Saphrin communes with the living wood, sensing emotional echoes in traded goods.'
			' Their presence is calming, like moss‑softened footsteps in ancient groves.'
		)
	},
	{
		'npc_id': 'twigwhisper_loryn',
		'name': 'Loryn Twigwhisper',
		'description': (
			'A nimble, sharp‑eyed negotiator who conducts deals from the high boughs.'
			' Loryn’s voice carries like birdsong, disarming even the most guarded traders.'
			' They claim the forest itself enforces every bargain struck in the Den.'
		)
	},
    {
        'npc_id': 'spore_seer_myrn',
        'name': 'Myrn the Spore‑Seer',
        'description': (
            'A wandering hermit who reads drifting spores like constellations. '
            'Myrn senses disturbances in the forest’s emotional undergrowth.'
        )
    },
    {
        'npc_id': 'root_echo',
        'name': 'Root Echo',
        'description': (
            'A murmuring apparition formed from tangled roots and memory‑sap. '
            'It speaks in layered whispers of ancient oaths.'
        )
    },
    {
        'npc_id': 'vault_spirit',
        'name': 'Vault Spirit',
        'description': (
            'A guardian of the Sporevault, shaped from fungal light and old promises.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'elder_saphrin',
        'dialog_id': 'saphrin_intro',
        'dialog': [
            "The Exchange falters. Promises rot at the edges.",
            "Something ancient stirs beneath the roots — a mind that binds all bargains.",
            "If it wakes fully, no oath will remain free."
        ]
    },

    {
        'npc_id': 'twigwhisper_loryn',
        'dialog_id': 'loryn_intro',
        'dialog': [
            "The canopy rustles with warnings.",
            "Deals unravel, threads snap, and the forest tightens its grip.",
            "Whatever lies below wants every promise ever spoken."
        ]
    },

    {
        'npc_id': 'spore_seer_myrn',
        'dialog_id': 'myrn_intro',
        'dialog': [
            "Spores drift toward the Hollows — drawn by a hungry root‑mind.",
            "The Heartwood Veil grows, weaving itself through every pact.",
            "If you descend, tread softly. It listens."
        ]
    },

    {
        'npc_id': 'root_echo',
        'dialog_id': 'root_echo_intro',
        'dialog': [
            "We are the roots. We remember every oath.",
            "The Veil drinks promises like rain.",
            "Turn back, or be woven into its will."
        ]
    },

    {
        'npc_id': 'vault_spirit',
        'dialog_id': 'vault_spirit_intro',
        'dialog': [
            "The Sporevault keeps the forest’s oldest bargains.",
            "The Veil seeks to claim them all — past, present, future.",
            "Only its Heart remains to be severed."
        ]
    },

    {
        'npc_id': 'elder_saphrin',
        'dialog_id': 'saphrin_closing',
        'dialog': [
            "The Veil falls silent. The Exchange breathes again.",
            "You have freed our promises from its grasp.",
            "The forest will remember your name in its rings."
        ]
    }

]


TASKS = [
	{
		'task_id': 'forest_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'elder_saphrin',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'elder_saphrin',
					'standing_text': [ 
						"Sit awhile — the trees remember more stories than any traveler."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'standing_text': [ 
						"High branches hold gossip; lean close and I'll tell you what the leaves sang."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_large_city_meet_saphrin'
                }
            }
		]		
	},

    # Task 1 — Meet Saphrin after initialization
    {
        'task_id': 'forest_large_city_meet_saphrin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'elder_saphrin',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'elder_saphrin',
                    'standing_text': [
                        "The Exchange trembles. Something roots beneath our bargains.",
                        "Sit, traveler — the wood has warnings to whisper."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'elder_saphrin',
                    'dialog_id': 'saphrin_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_large_city_meet_loryn'
                }
            }
        ]
    },

    # Task 2 — Meet Loryn for the canopy‑side perspective
    {
        'task_id': 'forest_large_city_meet_loryn',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'twigwhisper_loryn',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'twigwhisper_loryn',
                    'dialog_id': 'loryn_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'twigwhisper_loryn',
                    'standing_text': [
                        "Deals are unraveling. Promises fray like old bark.",
                        "Something deep below is rewriting the rules."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_large_city_find_myrn'
                }
            }
        ]
    },

    # Task 3 — Find Myrn the Spore‑Seer in the open forest
    {
        'task_id': 'forest_large_city_find_myrn',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'spore_seer_myrn',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'spore_seer_myrn',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'spore_seer_myrn',
                    'standing_text': [
                        "Hush… the spores drift strangely today.",
                        "They fall toward the Hollows. Something wakes."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'spore_seer_myrn',
                    'dialog_id': 'myrn_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_large_city_hollow_roots'
                }
            }
        ]
    },

    # Task 4 — Explore the Hollow Roots (first dungeon)
    {
        'task_id': 'forest_large_city_hollow_roots',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'root_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'hollow_roots',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'root_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'root_echo',
                    'dialog_id': 'root_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_large_city_sporevault'
                }
            }
        ]
    },

    # Task 5 — Descend into the Sporevault (second dungeon)
    {
        'task_id': 'forest_large_city_sporevault',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vault_spirit',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'sporevault',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'vault_spirit',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vault_spirit',
                    'dialog_id': 'vault_spirit_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_large_city_heartwood_veil'
                }
            }
        ]
    },

    # Task 6 — Defeat the Heartwood Veil (boss dungeon)
    {
        'task_id': 'forest_large_city_heartwood_veil',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'heartwood_veil_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_heartwood_veil',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'heartwood_veil_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'elder_saphrin',
                    'dialog_id': 'saphrin_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'forest_large_city'
                }
            }
        ]
    }

]




PRIMARY_STORY_SETTINGS = {
    'story_id': 'forest_large_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}