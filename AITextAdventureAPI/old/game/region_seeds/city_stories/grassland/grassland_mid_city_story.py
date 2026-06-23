ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'scribe_althorin',
		'name': 'Althorin the Doctrine‑Scribe',
		'description': (
			'A devout scholar who preserves sacred texts with unwavering discipline.'
			' Althorin’s quill never scratches—his writing flows like whispered prayer.'
			' He believes every doctrine has a hidden verse meant only for the worthy.'
		)
	},
	{
		'npc_id': 'oathwarden_seris',
		'name': 'Seris Oathwarden',
		'description': (
			'A solemn guardian who oversees the binding of vows and pacts.'
			' Seris speaks rarely, but every word carries ceremonial weight.'
			' Her presence alone compels honesty.'
		)
	},
    {
        'npc_id': 'verse_seeker_halven',
        'name': 'Halven the Verse‑Seeker',
        'description': (
            'A wandering scholar who hears fractured scripture carried on the wind. '
            'Halven follows broken verses to their source.'
        )
    },
    {
        'npc_id': 'lexicon_fragment',
        'name': 'Lexicon Fragment',
        'description': (
            'A living shard of doctrine, cracked by the False Verse’s corruption.'
        )
    },
    {
        'npc_id': 'sanctum_voice',
        'name': 'Sanctum Voice',
        'description': (
            'A solemn echo within the Oathbreak Sanctum, formed from unraveling vows.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'scribe_althorin',
        'dialog_id': 'althorin_intro',
        'dialog': [
            "The doctrines shift in the night.",
            "Verses appear where none were written.",
            "A False Verse spreads — subtle, poisonous."
        ]
    },

    {
        'npc_id': 'oathwarden_seris',
        'dialog_id': 'seris_intro',
        'dialog': [
            "Vows break without cause.",
            "Oaths unravel mid‑sentence.",
            "Something corrupts the very act of truth‑binding."
        ]
    },

    {
        'npc_id': 'verse_seeker_halven',
        'dialog_id': 'halven_intro',
        'dialog': [
            "The wind carries fractured scripture.",
            "A Verse that was never meant to be spoken.",
            "If it completes itself, all doctrine will bend."
        ]
    },

    {
        'npc_id': 'lexicon_fragment',
        'dialog_id': 'lexicon_fragment_intro',
        'dialog': [
            "We are the words that broke.",
            "The False Verse rewrites us.",
            "It waits deeper in the Sanctum."
        ]
    },

    {
        'npc_id': 'sanctum_voice',
        'dialog_id': 'sanctum_voice_intro',
        'dialog': [
            "The Sanctum trembles with broken vows.",
            "The False Verse grows stronger.",
            "Only its heart remains to be silenced."
        ]
    },

    {
        'npc_id': 'oathwarden_seris',
        'dialog_id': 'seris_closing',
        'dialog': [
            "The doctrines settle. The vows hold true again.",
            "You have restored the plains’ sacred order.",
            "The grasslands remember your honesty."
        ]
    }

]


TASKS = [
	{
		'task_id': 'grassland_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'scribe_althorin',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scribe_althorin',
					'standing_text': [ 
						"Words weave history—share a memory and I’ll add it to the ledger."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'oathwarden_seris',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'oathwarden_seris',
					'standing_text': [ 
						"Pacts are spoken softly here—if your heart is true, speak and I will hear."
					]
				}
			}

		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_meet_althorin'
                }
            }
		]		
	},

    # Task 1 — Meet Althorin after initialization
    {
        'task_id': 'grassland_mid_city_meet_althorin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'scribe_althorin',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'scribe_althorin',
                    'standing_text': [
                        "The doctrines shift. Verses appear where none were written.",
                        "Something rewrites the sacred texts."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'scribe_althorin',
                    'dialog_id': 'althorin_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_meet_seris'
                }
            }
        ]
    },

    # Task 2 — Meet Seris for the oath‑binding perspective
    {
        'task_id': 'grassland_mid_city_meet_seris',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'oathwarden_seris',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'oathwarden_seris',
                    'dialog_id': 'seris_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'oathwarden_seris',
                    'standing_text': [
                        "Vows unravel. Promises break without cause.",
                        "Something corrupts the very act of oath‑making."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_find_halven'
                }
            }
        ]
    },

    # Task 3 — Find Verse‑Seeker Halven in the open plains
    {
        'task_id': 'grassland_mid_city_find_halven',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'verse_seeker_halven',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'verse_seeker_halven',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'verse_seeker_halven',
                    'standing_text': [
                        "The wind carries fractured scripture.",
                        "A False Verse spreads across the plains."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'verse_seeker_halven',
                    'dialog_id': 'halven_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_shattered_lexicon'
                }
            }
        ]
    },

    # Task 4 — Explore the Shattered Lexicon (first dungeon)
    {
        'task_id': 'grassland_mid_city_shattered_lexicon',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lexicon_fragment',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'shattered_lexicon',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'lexicon_fragment',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'lexicon_fragment',
                    'dialog_id': 'lexicon_fragment_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_oathbreak_sanctum'
                }
            }
        ]
    },

    # Task 5 — Descend into the Oathbreak Sanctum (second dungeon)
    {
        'task_id': 'grassland_mid_city_oathbreak_sanctum',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'sanctum_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'oathbreak_sanctum',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'sanctum_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'sanctum_voice',
                    'dialog_id': 'sanctum_voice_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_false_verse'
                }
            }
        ]
    },

    # Task 6 — Defeat the False Verse (boss dungeon)
    {
        'task_id': 'grassland_mid_city_false_verse',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'false_verse_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_false_verse',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'false_verse_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'oathwarden_seris',
                    'dialog_id': 'seris_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'grassland_mid_city'
                }
            }
        ]
    }

]



PRIMARY_STORY_SETTINGS = {
	'story_id': 'grassland_mid_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}