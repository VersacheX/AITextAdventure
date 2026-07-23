ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'scribe_althorin',
		'name': 'Althorin the Doctrine‑Scribe',
		'description': (
			'A devout scholar who preserves sacred texts with unwavering discipline.'
			' Althorin\'s quill never scratches—his writing flows like whispered prayer.'
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
            'A living shard of doctrine, cracked by the False Verse\'s corruption.'
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

    # --- Base city standing dialog ---

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
            "You have restored the plains' sacred order.",
            "The grasslands remember your honesty."
        ]
    }

]

NPC_DIALOG += [

    # --- Type C: Regent Sylvara ---

    {
        'npc_id': 'regent_sylvara',
        'dialog_id': 'sylvara_type_c_intro',
        'dialog': [
            "You found me. That means you were looking — or you were guided.",
            "Either way suggests competence.",
            "Highsteeple is a city built on doctrines it no longer believes in.",
            "I've been watching it unravel for some time. I'd like to stop it. If you're willing."
        ]
    },
    {
        'npc_id': 'regent_sylvara',
        'dialog_id': 'sylvara_type_c_join',
        'dialog': [
            "The False Verse is not a monster. It's a failure of governance — someone let the wrong idea take root.",
            "That is exactly the kind of problem I was designed to solve.",
            "I'll come with you."
        ]
    },

]

NPC_DIALOG += [

    # --- Type E: Sanctum Seal Fragment ---

    {
        'npc_id': 'scribe_althorin',
        'dialog_id': 'althorin_seal_discovery',
        'dialog': [
            "I've been transcribing the Sanctum's founding texts.",
            "Every record references a foundation seal — the original binding that consecrated this place.",
            "It predates the False Verse by centuries. If it still exists, it's buried in the Sanctum's deepest chamber."
        ]
    },
    {
        'npc_id': 'verse_seeker_halven',
        'dialog_id': 'halven_seal_context',
        'dialog': [
            "The foundation seal is not a weapon and not a relic of worship.",
            "It is a compressed record — every oath ever sworn here, bound into stone.",
            "The False Verse cannot corrupt it. That is precisely why it buried the chamber."
        ]
    },
    {
        'npc_id': 'sanctum_voice',
        'dialog_id': 'sanctum_voice_seal_guardian',
        'dialog': [
            "The seal belongs to the Sanctum.",
            "What you call preservation, we call theft.",
            "Leave. Or we will remind you what broken vows feel like."
        ]
    },
    {
        'npc_id': 'scribe_althorin',
        'dialog_id': 'althorin_seal_received',
        'dialog': [
            "Extraordinary. This is the original mark — I can read every oath in the grain of the stone.",
            "It doesn't belong locked away down there. And it doesn't belong in my archive either.",
            "Carry it. Something will call for it eventually — oaths have a way of finding their purpose."
        ]
    },

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
						"Words weave history—share a memory and I'll add it to the ledger."
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
                    'task_id': 'grassland_mid_city_regional_complete_gate'
                }
            }
		]
	},
    {
        'task_id': 'grassland_mid_city_regional_complete_gate',
        'type': 'complete_regional_quests',
        'task_acquire_events': [],
        'task_complete_events': [
            # Type C — gated by chapter 3 being reached
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_type_c_find_sylvara'
                },
                'condition': {
                    'type': 'is_chapter_gte',
                    'params': { 'chapter': 3 }
                }
            },
            # Type E — no gate condition, artifact waits in inventory
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_type_e_investigate_seal'
                }
            }
        ]
    },

]

TASKS += [

    # =========================================================
    # TYPE C — Regent Sylvara
    # Extended Character: regent_sylvara
    # Final event: character_join
    # Awarded by: grassland_mid_city_regional_complete_gate (is_chapter_gte 3)
    # =========================================================

    {
        'task_id': 'grassland_mid_city_type_c_find_sylvara',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'regent_sylvara',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'regent_sylvara',
                    'location': 'region_city_other3'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'regent_sylvara',
                    'standing_text': [
                        "I've been watching this city for some time.",
                        "You're the first person who's looked like they could actually do something about it."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'regent_sylvara',
                    'dialog_id': 'sylvara_type_c_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_type_c_earn_sylvara'
                }
            }
        ]
    },

    {
        'task_id': 'grassland_mid_city_type_c_earn_sylvara',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'oathwarden_seris',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'oathwarden_seris',
                    'standing_text': [
                        "Sylvara sent you? Then you've already earned more trust than most.",
                        "She doesn't recommend people lightly."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'regent_sylvara',
                    'dialog_id': 'sylvara_type_c_join'
                }
            },
            {
                'event_type': 'character_join',
                'params': {
                    'npc_id': 'regent_sylvara'
                }
            }
        ]
    },

]

TASKS += [

    # =========================================================
    # TYPE E — Sanctum Seal Fragment
    # Artifact ID: grassland_mid_city_e_sanctum_seal_fragment
    # Gates: grassland_large_city (Crosswind Bazaar, Ch.10) Type D (Slot 2)
    # Awarded by: grassland_mid_city_regional_complete_gate
    # =========================================================

    {
        'task_id': 'grassland_mid_city_type_e_investigate_seal',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'scribe_althorin',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'scribe_althorin',
                    'standing_text': [
                        "I've been tracing the Sanctum's oldest texts.",
                        "There is a foundation seal referenced in every founding document — but I cannot find the stone itself."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'scribe_althorin',
                    'dialog_id': 'althorin_seal_discovery'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_type_e_consult_halven'
                }
            }
        ]
    },

    {
        'task_id': 'grassland_mid_city_type_e_consult_halven',
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
                        "A foundation seal? Yes — I've traced references to it in three separate doctrine winds.",
                        "The False Verse buried it deliberately. That alone tells you it matters."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'verse_seeker_halven',
                    'dialog_id': 'halven_seal_context'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_type_e_confront_sanctum_voice'
                }
            }
        ]
    },

    {
        'task_id': 'grassland_mid_city_type_e_confront_sanctum_voice',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'sanctum_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'sanctum_voice',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'sanctum_voice',
                    'standing_text': [
                        "The chamber is sealed for a reason.",
                        "Turn back."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'sanctum_voice',
                    'dialog_id': 'sanctum_voice_seal_guardian'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_type_e_defeat_sanctum_voice'
                }
            }
        ]
    },

    {
        'task_id': 'grassland_mid_city_type_e_defeat_sanctum_voice',
        'type': 'defeat',
        'to_type': 'npc',
        'to_id': 'sanctum_voice',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'give_item',
                'params': {
                    'item_id': 'grassland_mid_city_e_sanctum_seal_fragment'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_mid_city_type_e_return_to_althorin'
                }
            }
        ]
    },

    {
        'task_id': 'grassland_mid_city_type_e_return_to_althorin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'scribe_althorin',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'scribe_althorin',
                    'standing_text': [
                        "You found it. I can feel the oaths radiating from it from here.",
                        "Come — let me read what it says."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'scribe_althorin',
                    'dialog_id': 'althorin_seal_received'
                }
            }
        ]
    },

]


# ── Type D ── Oathbreaker's Sigil (mythic accessory) ─────────────────────────
# Gate: player holds sanctum_seal_fragment from the Type E chain.
# Deliver to Mira → Althorin deciphers the seal → defeat Sanctum Voice → mythic accessory.
# No new NPCs — uses scribe_althorin, sanctum_voice, and mira (Ch.2 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'scribe_althorin',
		'dialog_id': 'althorin_d_seal_read',
		'dialog': [
			"This fragment holds the original Oathbreaker's imprint.",
			"The Sanctum Voice — the echo we thought destroyed — it was bound inside this seal.",
			"Releasing it correctly will shatter the bond and crystallize the residue.",
			"Crystallized oath-residue is what Mira has been searching for.",
			"But first the Voice must be drawn out and silenced properly."
		]
	},

	{
		'npc_id': 'sanctum_voice',
		'dialog_id': 'sanctum_voice_d_awakens',
		'dialog': [
			"The seal opens.",
			"Every broken vow flows back to me.",
			"I will finish what the doctrine started."
		]
	},

]

TASKS += [

	# D-0 — Deliver sanctum_seal_fragment to Mira (standalone deliver; unlocks D chain)
	{
		'task_id': 'grassland_mid_city_type_d_deliver_seal_fragment',
		'type': 'deliver',
		'item_id': 'sanctum_seal_fragment',
		'to_type': 'npc',
		'to_id': 'mira',
		'gate': {
			'has_item': 'sanctum_seal_fragment'
		},
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"An Oathbreak seal fragment — do you understand what this means?",
						"I've seen shards like this in theory texts but never held one.",
						"Take it to Althorin first.",
						"He'll know how to read the imprint before we do anything irreversible."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_d_consult_althorin'
				}
			},
		]
	},

	# D-1 — Consult Althorin for the seal reading
	{
		'task_id': 'grassland_mid_city_type_d_consult_althorin',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'scribe_althorin',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scribe_althorin',
					'standing_text': [
						"I felt the seal's presence the moment it entered the city.",
						"The doctrine-scripts have been trembling since dawn.",
						"Bring it here — I have been waiting to read this imprint my entire career."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'scribe_althorin',
					'dialog_id': 'althorin_d_seal_read'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_d_meet_sanctum_voice'
				}
			},
		]
	},

	# D-2 — Meet the Sanctum Voice (boss intro)
	{
		'task_id': 'grassland_mid_city_type_d_meet_sanctum_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'sanctum_voice',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sanctum_voice',
					'standing_text': [
						"The air in the sanctum thickens — every spoken word feels wrong.",
						"The Voice stirs where broken oaths accumulate.",
						"The seal fragment has called it forward."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'sanctum_voice',
					'dialog_id': 'sanctum_voice_d_awakens'
				}
			},
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'sanctum_voice_1',
					'combat_type': 'boss_encounter'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_d_defeat_sanctum_voice'
				}
			},
		]
	},

	# D-3 — Defeat the Sanctum Voice; Mira crafts the mythic accessory
	{
		'task_id': 'grassland_mid_city_type_d_defeat_sanctum_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'sanctum_voice_1',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_grassland_mid_oathbreakers_sigil'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"The crystallized oath-residue is perfect.",
						"I've set it into the sigil — it will hold any vow you make absolutely.",
						"Even the ones you make with yourself."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scribe_althorin',
					'standing_text': [
						"The doctrine-scripts have gone still.",
						"For the first time in months, the verses read correctly.",
						"Whatever you did in that sanctum — it worked."
					]
				}
			},
		]
	},

]
# ── Type E ── Sanctum Seal Fragment → gates Grassland Large Type D ────────────
# Halven the Verse-Seeker recovered a cracked seal from the Oathbreak Sanctum
# during the False Verse hunt. No new NPCs. No dungeon.

NPC_DIALOG += [

	{
		'npc_id': 'verse_seeker_halven',
		'dialog_id': 'halven_e_seal_fragment',
		'dialog': [
			"I found this wedged in the Sanctum's foundation after the False Verse collapsed.",
			"A seal fragment — half a binding mark, still warm from whatever oath it once closed.",
			"Althorin says it's older than the Sanctum itself.",
			"He can't identify the original pact. Neither can I.",
			"But I know it belongs somewhere in the grasslands — somewhere larger.",
			"Take it. Keep it dry. It hates water."
		]
	},
	{
		'npc_id': 'scribe_althorin',
		'dialog_id': 'althorin_e_seal_provenance',
		'dialog': [
			"The script on that fragment predates our Sanctum by at least three centuries.",
			"It is a seal — not a key, not a weapon.",
			"Whatever it once closed, it can close again.",
			"I would keep it, but the verse-patterns tell me it must travel."
		]
	},

]

TASKS += [

	# E-1 — Consult Althorin about the fragment
	{
		'task_id': 'grassland_mid_city_type_e_consult_althorin',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'scribe_althorin',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'scribe_althorin', 'standing_text': [
				"A seal fragment from the Sanctum's foundation.",
				"Ancient. Pre-doctrine. Come read it with me."
			]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scribe_althorin', 'dialog_id': 'althorin_e_seal_provenance' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_mid_city_type_e_collect_fragment' }},
		]
	},

	# E-2 — Collect from Halven
	{
		'task_id': 'grassland_mid_city_type_e_collect_fragment',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'verse_seeker_halven',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'verse_seeker_halven', 'standing_text': [
				"I've been holding the fragment since the Sanctum cleared.",
				"Althorin says it has to move. Come take it."
			]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'verse_seeker_halven', 'dialog_id': 'halven_e_seal_fragment' }},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'grassland_mid_city_e_sanctum_seal_fragment' }},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
	'story_id': 'grassland_mid_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}