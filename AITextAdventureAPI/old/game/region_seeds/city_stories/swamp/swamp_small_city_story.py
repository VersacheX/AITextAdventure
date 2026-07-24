ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'bogrunner_tavik',
		'name': 'Tavik Bogrunner',
		'description': (
			'A wiry trader who ferries goods through the swamp’s most treacherous channels.'
			' Tavik’s skiff is patched with mismatched planks and swamp‑etched runes.'
			' He claims the bog itself shows him safe paths when danger rises.'
		)
	},
	{
		'npc_id': 'rotwharf_madra',
		'name': 'Madra Rotwharf',
		'description': (
			'A hardened broker who deals in illicit wares dredged from the swamp’s depths.'
			' Madra’s voice is rough, as though she’s swallowed too much swamp fog.'
			' She knows every outlaw, fugitive, and mercenary who passes through Hollow’s shadows.'
		)
	},
    {
        'npc_id': 'channel_seer_draveth',
        'name': 'Draveth the Channel‑Seer',
        'description': (
            'A swamp navigator who reads current‑signs and senses when routes vanish beneath the mire.'
        )
    },
    {
        'npc_id': 'murkchannel_echo',
        'name': 'Murkchannel Echo',
        'description': (
            'A spectral remnant of forgotten channels twisted by the Swallowed Path.'
        )
    },
    {
        'npc_id': 'rotfen_voice',
        'name': 'Rotfen Voice',
        'description': (
            'A whispering presence formed from lost routes deep within the Hideaway.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'bogrunner_tavik',
        'dialog_id': 'tavik_intro',
        'dialog': [
            "The channels twist where they once ran straight.",
            "The swamp hides its own paths.",
            "Something swallows the routes we trust."
        ]
    },

    {
        'npc_id': 'rotwharf_madra',
        'dialog_id': 'madra_intro',
        'dialog': [
            "Shadows move wrong in Hollow.",
            "Smugglers vanish on routes they’ve walked for years.",
            "If we don’t act, the swamp will claim every traveler."
        ]
    },

    {
        'npc_id': 'channel_seer_draveth',
        'dialog_id': 'draveth_intro',
        'dialog': [
            "The current‑signs vanish.",
            "A Swallowed Path rises — a spirit of devoured routes.",
            "If it awakens fully, no one will find their way out."
        ]
    },

    {
        'npc_id': 'murkchannel_echo',
        'dialog_id': 'murkchannel_echo_intro',
        'dialog': [
            "We are the channels the swamp forgot.",
            "The Swallowed Path twists our flow.",
            "It waits deeper in the Rotfen Hideaway."
        ]
    },

    {
        'npc_id': 'rotfen_voice',
        'dialog_id': 'rotfen_voice_intro',
        'dialog': [
            "The Hideaway churns with lost routes.",
            "The Swallowed Path gathers strength.",
            "Only its heart remains to be severed."
        ]
    },

    {
        'npc_id': 'bogrunner_tavik',
        'dialog_id': 'tavik_closing',
        'dialog': [
            "The channels clear. The swamp breathes easier.",
            "You’ve restored the paths the mire tried to swallow.",
            "Travelers will owe you their lives."
        ]
    },

	# ── Type C dialogs — Ghost ──────────────────────────────────────
	{
		'npc_id': 'bogrunner_tavik',
		'dialog_id': 'tavik_c_ghost_sighting',
		'dialog': [
			"Someone moves through the night channels.",
			"No boat. No wake until they're already gone.",
			"Madra's clocked them twice near the Hideaway entrance.",
			"Whoever it is — they're not hiding from the swamp.",
			"They're hiding from us."
		]
	},
	{
		'npc_id': 'rotwharf_madra',
		'dialog_id': 'madra_c_ghost_vouch',
		'dialog': [
			"I've seen every kind of shadow pass through Hollow.",
			"Bounty hunters, deserters, couriers running black-market routes.",
			"This one's different.",
			"They move like the dark owes them a favour.",
			"I caught a name once. Ghost.",
			"They don't move for coin or cause.",
			"Find out what they're watching — that might earn you a word."
		]
	},
	{
		'npc_id': 'ghost',
		'dialog_id': 'ghost_c_first_meet',
		'dialog': [
			"You weren't followed.",
			"Good.",
			"I've been watching your party since the Riftlands.",
			"You operate quietly.",
			"That's worth something in Hollow.",
			"Say what you want."
		]
	},
	{
		'npc_id': 'ghost',
		'dialog_id': 'ghost_c_joins',
		'dialog': [
			"The swamp runs on favours and silence.",
			"You've earned both.",
			"I move when I decide. You point the direction.",
			"That's the arrangement."
		]
	},

	# ── Type A dialogs — Ch.7 Airship Tie-In ───────────────────────
	{
		'npc_id': 'bogrunner_tavik',
		'dialog_id': 'tavik_a_channel_check',
		'dialog': [
			"Something big is moving through the upper channels — airship-scale displacement.",
			"If Seth tries to lift off before the mire settles, the suction will collapse three routes.",
			"Get Draveth to read the current-signs.",
			"If he clears it, the swamp can handle the departure."
		]
	},
	{
		'npc_id': 'channel_seer_draveth',
		'dialog_id': 'draveth_a_clearance',
		'dialog': [
			"The channels are restless — they feel the engine pressure from the outpost.",
			"But the flow holds.",
			"Mire absorption rate is high enough to handle the displacement.",
			"Tell Madra the current-signs confirm it. She'll relay to Seth."
		]
	},
	{
		'npc_id': 'rotwharf_madra',
		'dialog_id': 'madra_a_network_clear',
		'dialog': [
			"Draveth's read is in.",
			"My network's gone quiet — no bounties filed, no interference flagged.",
			"Hollow's clear.",
			"Tell Seth he can lift off."
		]
	},

]
# ── Type D dialogs — Rotfen Dredge Blade ───────────────────────

NPC_DIALOG += [

    {
        'npc_id': 'channel_seer_draveth',
        'dialog_id': 'draveth_d_vessel_read',
        'dialog': [
            "This vessel — the memory inside it is not from the Hollow.",
            "It carries an imprint of the Bayou's oldest channels.",
            "The Rotfen Voice will sense it the moment you cross the Hideaway threshold.",
            "It will interpret the vessel as a claim on its territory.",
            "That anger is what we need. It will surface — and you will be ready."
        ]
    },

    {
        'npc_id': 'rotfen_voice',
        'dialog_id': 'rotfen_voice_d_awakens',
        'dialog': [
            "That vessel does not belong in the Hollow.",
            "The Bayou's memory is a poison here.",
            "You carry it as a weapon against me.",
            "Then I will take it — and every route you ever knew."
        ]
    },

]

TASKS = [
	{
		'task_id': 'swamp_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'bogrunner_tavik',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'bogrunner_tavik',
					'standing_text': [
						"The channels whisper secrets—ride with me and tell what the swamp showed you."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'rotwharf_madra',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rotwharf_madra',
					'standing_text': [
						"Hollow's shadows remember faces—stay and tell me what brought you here."
					]
				}
			},
		],
		'task_complete_events': [
            { 'event_type': 'award_task', 'params': { 'task_id': 'swamp_small_city_type_a_ch7_find_pendant' }},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_regional_complete_gate'
				}
			},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'swamp_small_city_type_d_deliver_memory_vessel' }},
		]
	},
    {
        'task_id': 'swamp_small_city_regional_complete_gate',
        'type': 'complete_regional_quests',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_meet_tavik'
                }
            },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_type_c_find_ghost'
				}
			},
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_type_a_channel_check'
                }
            }
        ]

    },

    # Task 1 — Meet Tavik after initialization
    {
        'task_id': 'swamp_small_city_meet_tavik',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'bogrunner_tavik',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bogrunner_tavik',
                    'dialog_id': 'tavik_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'bogrunner_tavik',
                    'standing_text': [
                        "The channels twist where they once ran straight.",
                        "Something hides the safe paths."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_meet_madra'
                }
            }
        ]
    },

    # Task 2 — Meet Madra for the outlaw‑network perspective
    {
        'task_id': 'swamp_small_city_meet_madra',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rotwharf_madra',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rotwharf_madra',
                    'dialog_id': 'madra_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rotwharf_madra',
                    'standing_text': [
                        "Shadows move wrong in Hollow.",
                        "Someone — or something — is swallowing the routes smugglers rely on."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_find_draveth'
                }
            }
        ]
    },

    # Task 3 — Find Channel‑Seer Draveth in the open swamp
    {
        'task_id': 'swamp_small_city_find_draveth',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'channel_seer_draveth',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'channel_seer_draveth',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'channel_seer_draveth',
                    'standing_text': [
                        "The current‑signs vanish.",
                        "A Swallowed Path rises beneath the murk."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'channel_seer_draveth',
                    'dialog_id': 'draveth_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_murkchannel_run'
                }
            }
        ]
    },

    # Task 4 — Explore the Murkchannel Run (first dungeon)
    {
        'task_id': 'swamp_small_city_murkchannel_run',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'murkchannel_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'murkchannel_run',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'murkchannel_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'murkchannel_echo',
                    'dialog_id': 'murkchannel_echo_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_rotfen_hideaway'
                }
            }
        ]
    },

    # Task 5 — Descend into the Rotfen Hideaway (second dungeon)
    {
        'task_id': 'swamp_small_city_rotfen_hideaway',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rotfen_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'rotfen_hideaway',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'rotfen_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rotfen_voice',
                    'dialog_id': 'rotfen_voice_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_swallowed_path'
                }
            }
        ]
    },

    # Task 6 — Defeat the Swallowed Path (boss dungeon)
    {
        'task_id': 'swamp_small_city_swallowed_path',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'swallowed_path_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_swallowed_path',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'swallowed_path_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bogrunner_tavik',
                    'dialog_id': 'tavik_closing'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'swamp_small_city'
                }
            }
        ]
    },

    # ── Type D ── Rotfen Dredge Blade (mythic weapon) ─────────────────────────────
    # Gate: player holds bayou_memory_vessel from the Ch.20 Type E chain (retroactive).
    # Deliver to Diego → Draveth reads the vessel → defeat Rotfen Voice → mythic weapon.
    # No new NPCs — uses channel_seer_draveth, rotfen_voice, and diego (Ch.1 party anchor).

    {
        'task_id': 'swamp_small_city_type_d_deliver_memory_vessel',
        'type': 'deliver',
        'item_id': 'bayou_memory_vessel',
        'to_type': 'npc',
        'to_id': 'diego',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'diego',
                    'standing_text': [
                        "That vessel — the clay holds a forge-resonance I've never felt from a swamp relic.",
                        "There's metal inside the Hollow that only this thing can unlock.",
                        "Find Draveth. He reads the channels — he'll know where the resonance leads."
                    ]
                }
            },
		],
        'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_type_d_consult_draveth'
                }
            },
		]
    },

	# D-1 — Consult Draveth for the channel reading
	{
		'task_id': 'swamp_small_city_type_d_consult_draveth',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'channel_seer_draveth',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'channel_seer_draveth',
					'standing_text': [
						"The current-signs surged the moment that vessel crossed the Hollow's edge.",
						"The Bayou's memory doesn't belong here — and the Rotfen Voice knows it.",
						"Come quickly. The Hideaway won't stay open long."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'channel_seer_draveth',
					'dialog_id': 'draveth_d_vessel_read'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_type_d_meet_rotfen_voice'
				}
			},
		]
	},

	# D-2 — Meet the Rotfen Voice (boss intro)
	{
		'task_id': 'swamp_small_city_type_d_meet_rotfen_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rotfen_voice',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rotfen_voice',
					'standing_text': [
						"The mire thickens near the Hideaway entrance.",
						"Tavik says no one who entered last season ever surfaced.",
						"The vessel has agitated whatever lives in the deep rot."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rotfen_voice',
					'dialog_id': 'rotfen_voice_d_awakens'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_type_d_defeat_rotfen_voice'
				}
			},
		]
	},

	# D-3 — Defeat the Rotfen Voice; Diego forges the mythic weapon
	{
		'task_id': 'swamp_small_city_type_d_defeat_rotfen_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'rotfen_voice_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'rotfen_voice_1',
					'combat_type': 'boss_battle'
				}
			}
        ],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_swamp_small_rotfen_dredge_blade'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"The swamp-iron the Voice guarded — it's unlike any metal I've handled.",
						"I've worked it into the blade. It knows every route the swamp has ever swallowed.",
						"You won't get lost carrying this."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'channel_seer_draveth',
					'standing_text': [
						"The current-signs flow clean again.",
						"Every route the Voice devoured has returned.",
						"Tavik can run the channels safely now."
					]
				}
			},
		]
	},

]

# ── Type A ── Ch.7 Chapter Tie-In (Lyren's Vale Pendant) ─────────────────────
# Awarded when Lyren is met in Ch.7. Tavik recovered the pendant from a
# sunken skiff in the channels — he's been waiting to hand it to someone
# who might know its owner. No new NPCs — Tavik is in the city seed.

NPC_DIALOG += [

    {
        'npc_id': 'bogrunner_tavik',
        'dialog_id': 'tavik_a_ch7_pendant',
        'dialog': [
            "Pulled this out of a sunken skiff three weeks ago.",
            "Silver pendant. Delicate work — not from around here.",
            "The skiff had a name burned into the hull: Vale.",
            "I've been asking around but nobody claimed it.",
            "(holds it out) You look like people who travel. Maybe you know someone."
        ]
    },

]

TASKS += [

    # A-1 — Meet Tavik to recover the Vale Pendant
    {
        'task_id': 'swamp_small_city_type_a_ch7_find_pendant',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'bogrunner_tavik',
        'task_acquire_events': [
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'bogrunner_tavik', 'standing_text': [
                "Found something in the channels that doesn't belong to anyone around here.",
                "Silver pendant. Someone out there's missing it."
            ]}},
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'bogrunner_tavik', 'dialog_id': 'tavik_a_ch7_pendant' }},
            { 'event_type': 'award_item', 'params': { 'item_id': 'vale_pendant' }},
        ]
    },

]

TASKS += [

	# =========================================================
	# TYPE C — Ghost (extended character, slot 2)
	# Gated by is_chapter_gte: 7
	# Awarded by: swamp_small_city_regional_complete_gate (conditional)
	# Chain: tavik reports sighting → madra vouches → meet Ghost → Ghost joins
	# Ghost is the reward — not a guide. No new NPCs beyond Ghost.
	# =========================================================

	# C-1 — Tavik reports the mysterious figure in the night channels
	{
		'task_id': 'swamp_small_city_type_c_find_ghost',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'bogrunner_tavik',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'bogrunner_tavik',
					'standing_text': [
						"Someone moves through the night channels without a boat.",
						"No wake. No sound until they're already gone.",
						"You should hear this from me directly."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'bogrunner_tavik',
					'dialog_id': 'tavik_c_ghost_sighting'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_type_c_madra_vouch'
				}
			},
		]
	},

	# C-2 — Madra gives the name and the lead
	{
		'task_id': 'swamp_small_city_type_c_madra_vouch',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rotwharf_madra',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rotwharf_madra',
					'standing_text': [
						"Tavik sent you. Good — I've clocked this shadow twice near the Hideaway entrance.",
						"I've got a name. Come ask."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rotwharf_madra',
					'dialog_id': 'madra_c_ghost_vouch'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_type_c_meet_ghost'
				}
			},
		]
	},

	# C-3 — Meet Ghost; Ghost joins the party
	{
		'task_id': 'swamp_small_city_type_c_meet_ghost',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'ghost',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'ghost',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'ghost',
					'standing_text': [
						"A figure stands perfectly still in the shadow of the Hideaway entrance.",
						"They watched you arrive without moving."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'ghost',
					'dialog_id': 'ghost_c_first_meet'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'ghost',
					'dialog_id': 'ghost_c_joins'
				}
			},
			{
				'event_type': 'character_join',
				'params': {
					'character_id': 'ghost'
				}
			},
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE A — Ch.7 Airship Channel Clearance
	# Seth cannot lift off safely until the swamp channels are read.
	# Awarded by: swamp_small_city_regional_complete_gate
	# Chain: read current-signs with Draveth → relay clearance to Madra
	# No new NPCs — Draveth and Madra are both in the city seed.
	# advance_chapter is handled by the pendant chain (swamp_small_city_type_a_ch7_find_pendant)
	# =========================================================

	# A-1 — Find Draveth for the channel reading
	{
		'task_id': 'swamp_small_city_type_a_channel_check',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'channel_seer_draveth',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'channel_seer_draveth',
					'standing_text': [
						"Engine pressure from the outpost disturbs the current-signs.",
						"I need to read the flow before anything large lifts off.",
						"Come quickly."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'bogrunner_tavik',
					'standing_text': [
						"Something big is moving through the upper channels — airship-scale displacement.",
						"Get Draveth to read the current-signs before Seth tries to lift off."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'channel_seer_draveth',
					'dialog_id': 'draveth_a_clearance'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_type_a_relay_to_madra'
				}
			},
		]
	},

	# A-2 — Relay Draveth's clearance to Madra; she signals Seth
	{
		'task_id': 'swamp_small_city_type_a_relay_to_madra',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rotwharf_madra',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rotwharf_madra',
					'standing_text': [
						"Draveth's read is the last thing I need.",
						"My network's already gone quiet.",
						"Bring me his word and I'll clear Seth for departure."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rotwharf_madra',
					'dialog_id': 'madra_a_network_clear'
				}
			},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
	'story_id': 'swamp_small_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}