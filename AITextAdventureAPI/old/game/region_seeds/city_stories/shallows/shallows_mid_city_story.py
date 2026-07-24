ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'tidejudge_merrik',
		'name': 'Merrik Tidejudge',
		'description': (
			'A stern adjudicator who settles disputes among sailors and merchants.'
			' Merrik\'s gavel is carved from driftwood older than the town itself.'
			' He has a reputation for fairness, but never softness.'
		)
	},
	{
		'npc_id': 'lanternrunner_vexa',
		'name': 'Vexa Lanternrunner',
		'description': (
			'A cunning smuggler who uses coded lantern signals to move goods unseen.'
			' Vexa\'s grin is sharp, and her footsteps are softer than sea foam.'
			' She claims the Lanternhouse has secret tunnels even she hasn\'t found.'
		)
	},
    {
        'npc_id': 'signal_seer_thalen',
        'name': 'Thalen the Signal‑Seer',
        'description': (
            'A coastal mystic who reads broken lantern patterns drifting across the waves.'
        )
    },
    {
        'npc_id': 'lanternfade_echo',
        'name': 'Lanternfade Echo',
        'description': (
            'A spectral remnant of lost lantern signals swallowed by storms and fog.'
        )
    },
    {
        'npc_id': 'undertunnel_voice',
        'name': 'Undertunnel Voice',
        'description': (
            'A whispering presence formed from misdirected signals deep within the smuggler tunnels.'
        )
    }
]


NPC_DIALOG = [

    # --- Base city standing dialog ---

    {
        'npc_id': 'tidejudge_merrik',
        'dialog_id': 'merrik_intro',
        'dialog': [
            "Lantern codes contradict themselves.",
            "Signals flicker in patterns no sailor would send.",
            "Something disrupts the order of the coast."
        ]
    },
    {
        'npc_id': 'lanternrunner_vexa',
        'dialog_id': 'vexa_intro',
        'dialog': [
            "Routes flicker wrong.",
            "Someone's sending signals that lead nowhere — or worse.",
            "If we don't stop it, ships will vanish in calm waters."
        ]
    },
    {
        'npc_id': 'signal_seer_thalen',
        'dialog_id': 'thalen_intro',
        'dialog': [
            "The lantern patterns fracture.",
            "A False Lantern rises — a spirit of misdirection.",
            "If it awakens fully, the coast will lose its way."
        ]
    },
    {
        'npc_id': 'lanternfade_echo',
        'dialog_id': 'lanternfade_echo_intro',
        'dialog': [
            "We are the signals that faded.",
            "The False Lantern twists our light.",
            "It waits deeper in the Undertunnel."
        ]
    },
    {
        'npc_id': 'undertunnel_voice',
        'dialog_id': 'undertunnel_voice_intro',
        'dialog': [
            "The tunnels hum with stolen signals.",
            "The False Lantern gathers strength.",
            "Only its heart remains to be dimmed."
        ]
    },
    {
        'npc_id': 'tidejudge_merrik',
        'dialog_id': 'merrik_closing',
        'dialog': [
            "The signals steady. The coast finds its bearings again.",
            "You've restored truth to the lantern routes.",
            "The Shallows will remember your clarity."
        ]
    }

]

NPC_DIALOG += [

    # --- Type E: Tidekin Seal ---

    {
        'npc_id': 'lanternrunner_vexa',
        'dialog_id': 'vexa_tidekin_seal_discovery',
        'dialog': [
            "Found something in the undertunnel last week — wedged behind a collapsed wall.",
            "Looks ceremonial. Old Tidekin script around the rim.",
            "Merrik won't touch it. Says it should go back to where it came from.",
            "The problem is nobody knows where that is."
        ]
    },
    {
        'npc_id': 'signal_seer_thalen',
        'dialog_id': 'thalen_tidekin_seal_context',
        'dialog': [
            "The Tidekin Seal. The coastal clans used it to mark founding pacts.",
            "This one was separated from its cove — probably during the storm that buried the undertunnel.",
            "The Lanternfade Echo has been drawn to its resonance. It will try to claim it.",
            "Take it before the echo bonds to it completely."
        ]
    },
    {
        'npc_id': 'lanternfade_echo',
        'dialog_id': 'lanternfade_echo_seal_guardian',
        'dialog': [
            "The Seal called to us.",
            "We answered. It is ours now.",
            "You have no claim here."
        ]
    },
    {
        'npc_id': 'lanternrunner_vexa',
        'dialog_id': 'vexa_tidekin_seal_received',
        'dialog': [
            "You got it out clean.",
            "Merrik's going to say you should hand it over to the courts.",
            "Don't. Something that old belongs somewhere specific.",
            "You'll figure out where."
        ]
    },

]

NPC_DIALOG += [

    # --- Type C: Dare ---

    {
        'npc_id': 'dare',
        'dialog_id': 'dare_type_c_intro',
        'dialog': [
            "You hear that?",
            "That's the sound of a signal network nobody's touched in twenty years.",
            "Vexa showed me the undertunnel maps. There are routes in there that don't exist on any chart.",
            "I want in. I'm guessing you do too, or you wouldn't be standing here looking curious."
        ]
    },
    {
        'npc_id': 'dare',
        'dialog_id': 'dare_type_c_vexa_check',
        'dialog': [
            "Vexa says you're reliable. High praise from her — she doesn't say that about anyone.",
            "I've been scouting this coastline for a month. The undertunnel is the most interesting thing I've found.",
            "You look like you know how to move through interesting places without dying."
        ]
    },
    {
        'npc_id': 'dare',
        'dialog_id': 'dare_type_c_join',
        'dialog': [
            "Alright. I'm in.",
            "Fair warning — I move fast and I ask questions after.",
            "If that's a problem, say so now. Otherwise, let's go find whatever's at the end of those routes."
        ]
    },

]


TASKS = [
	{
		'task_id': 'shallows_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'tidejudge_merrik',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'tidejudge_merrik',
					'standing_text': [
						"Disputes find their calm here—if you have a grievance, speak plainly."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'lanternrunner_vexa',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'lanternrunner_vexa',
					'standing_text': [
						"Lanterns hide more than light—share a secret and I might share a route."
					]
				}
			}
		],
		'task_complete_events': [
            # Type E — no gate condition, artifact waits in inventory
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_type_e_investigate_seal'
                }
            },
            # Type C — gated by chapter 11 being reached
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_type_c_find_dare'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_type_d_deliver_corsair_fragment'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_type_e_consult_vexa'
                }
            }
		]
	},

]

TASKS += [

    # =========================================================
    # TYPE E — Tidekin Seal
    # Artifact ID: shallows_mid_city_e_tidekin_seal
    # Gates: shallows_small_city (Tidekin Cove, Ch.14) Type D (Slot 2)
    # Awarded by: shallows_mid_city_initialize
    # =========================================================

    {
        'task_id': 'shallows_mid_city_type_e_investigate_seal',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lanternrunner_vexa',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'lanternrunner_vexa',
                    'standing_text': [
                        "I pulled something out of the undertunnel that I can't place.",
                        "Old script, ceremonial looking. Merrik won't go near it."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'lanternrunner_vexa',
                    'dialog_id': 'vexa_tidekin_seal_discovery'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_type_e_consult_thalen'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_mid_city_type_e_consult_thalen',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'signal_seer_thalen',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'signal_seer_thalen',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'signal_seer_thalen',
                    'standing_text': [
                        "The Seal's resonance has been drifting for weeks.",
                        "The Lanternfade Echo is circling it. We need to act before it bonds."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'signal_seer_thalen',
                    'dialog_id': 'thalen_tidekin_seal_context'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_type_e_confront_lanternfade_echo'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_mid_city_type_e_confront_lanternfade_echo',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lanternfade_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'lanternfade_echo',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'lanternfade_echo',
                    'standing_text': [
                        "The Seal is ours.",
                        "Leave."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'lanternfade_echo',
                    'dialog_id': 'lanternfade_echo_seal_guardian'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_type_e_defeat_lanternfade_echo'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_mid_city_type_e_defeat_lanternfade_echo',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'lanternfade_echo',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'lanternfade_echo',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'shallows_mid_city_e_tidekin_seal'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_type_e_return_to_vexa'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_mid_city_type_e_return_to_vexa',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lanternrunner_vexa',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'lanternrunner_vexa',
                    'standing_text': [
                        "The echo dispersed the moment you stepped back in.",
                        "Whatever you're holding — it knows you now."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'lanternrunner_vexa',
                    'dialog_id': 'vexa_tidekin_seal_received'
                }
            }
        ]
    },

]

TASKS += [

    # =========================================================
    # TYPE C — Dare
    # Extended Character: dare
    # Final event: character_join
    # Awarded by: shallows_mid_city_initialize (is_chapter_gte 11)
    # =========================================================

    {
        'task_id': 'shallows_mid_city_type_c_find_dare',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'dare',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'dare',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'dare',
                    'standing_text': [
                        "You hear that frequency coming from the undertunnel?",
                        "Twenty years dormant and now it's singing. I want to know why."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'dare',
                    'dialog_id': 'dare_type_c_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_type_c_consult_vexa'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_mid_city_type_c_consult_vexa',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lanternrunner_vexa',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'lanternrunner_vexa',
                    'standing_text': [
                        "Dare? Yeah I know her.",
                        "Reliable when it counts. Reckless the rest of the time.",
                        "You'd make a good pair, honestly."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'dare',
                    'dialog_id': 'dare_type_c_vexa_check'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_mid_city_type_c_earn_dare'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_mid_city_type_c_earn_dare',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'dare',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'dare',
                    'standing_text': [
                        "Vexa vouched for you.",
                        "That's enough for me."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'dare',
                    'dialog_id': 'dare_type_c_join'
                }
            },
            {
                'event_type': 'character_join',
                'params': {
                    'character_id': 'dare'
                }
            }
        ]
    },

]

# ── Type D ── Corsair's Depth Blade (mythic weapon) ───────────────────────────
# Gate: player holds corsair_tide_fragment from stormglass_alley (Ch.5 dungeon).
# Deliver to Diego → Thalen reads the fragment → defeat Undertunnel Voice → mythic weapon.
# No new NPCs — uses signal_seer_thalen, undertunnel_voice, and diego (Ch.1 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'signal_seer_thalen',
		'dialog_id': 'thalen_d_fragment_read',
		'dialog': [
			"This fragment carries the tide-frequency of Stormglass Alley.",
			"Those static wraiths were guarding something far older than any storm.",
			"The Undertunnel Voice beneath the smuggler network holds the matching resonance.",
			"The corsair lineage that built these tunnels sealed it there deliberately.",
			"Draw the Voice out with the fragment — it will surface.",
			"Silence it and the corsair-tide metal solidifies.",
			"Diego can forge corsair-tide steel into a blade that cuts through any current."
		]
	},

	{
		'npc_id': 'undertunnel_voice',
		'dialog_id': 'undertunnel_voice_d_awakens',
		'dialog': [
			"The corsair fragment opens the deep tunnel.",
			"Every misdirected signal, every lost smuggler route — I carry them all.",
			"You want the tide-steel the corsairs buried here.",
			"Take it from me if you can navigate the dark."
		]
	},

]

TASKS += [

	# D-0 — Deliver corsair_tide_fragment to Diego (standalone deliver; unlocks D chain)
	{
		'task_id': 'shallows_mid_city_type_d_deliver_corsair_fragment',
		'type': 'deliver',
		'item_id': 'corsair_tide_fragment',
		'to_type': 'npc',
		'to_id': 'diego',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"That fragment — the metal has a tide-pull I've never felt in steel.",
						"Something in Blackwake Bay resonates with it.",
						"Find Thalen. He reads the coastal signals — he'll know where this belongs."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_mid_city_type_d_consult_thalen'
				}
			},
		]
	},

	# D-1 — Consult Thalen for the fragment reading
	{
		'task_id': 'shallows_mid_city_type_d_consult_thalen',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'signal_seer_thalen',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'signal_seer_thalen',
					'standing_text': [
						"The lantern patterns shifted when you arrived.",
						"Something in what you carry is broadcasting on the corsair frequency.",
						"Come quickly — the tunnels are already answering."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'signal_seer_thalen',
					'dialog_id': 'thalen_d_fragment_read'
				}
			},
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'undertunnel_voice',
                    'location': 'region_open_area'
                }
            },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_mid_city_type_d_meet_undertunnel_voice'
				}
			},
		]
	},

	# D-2 — Meet the Undertunnel Voice (boss intro)
	{
		'task_id': 'shallows_mid_city_type_d_meet_undertunnel_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'undertunnel_voice',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'undertunnel_voice',
					'standing_text': [
						"Vexa says the smuggler tunnels are humming on their own.",
						"Merrik closed the lower entrance — too many signals bleeding up from below.",
						"The corsair fragment has woken whatever the old lineage sealed down there."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'undertunnel_voice',
					'dialog_id': 'undertunnel_voice_d_awakens'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_mid_city_type_d_defeat_undertunnel_voice'
				}
			},
		]
	},

	# D-3 — Defeat the Undertunnel Voice; Diego forges the mythic weapon
	{
		'task_id': 'shallows_mid_city_type_d_defeat_undertunnel_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'undertunnel_voice_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'undertunnel_voice_1',
					'combat_type': 'boss_battle'
				}
			}
        ],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_shallows_mid_corsairs_depth_blade'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"Corsair-tide steel — it forges like nothing I've ever handled.",
						"The blade knows every current and tunnel beneath the bay.",
						"Nothing will hold a line against this."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'signal_seer_thalen',
					'standing_text': [
						"The lantern patterns are clear again.",
						"Every misdirected signal the Voice held has resolved.",
						"Vexa says the tunnels are finally quiet."
					]
				}
			},
		]
	},

]
# ── Type E ── Tidekin Seal → gates Shallows Small Type D (Tidekin Cove) ───────
# Merrik Tidejudge found a pressed wax seal among evidence recovered from
# the False Lantern's tunnel. No new NPCs. No dungeon.

NPC_DIALOG += [

	{
		'npc_id': 'tidejudge_merrik',
		'dialog_id': 'merrik_e_tidekin_seal',
		'dialog': [
			"When we recovered evidence from the tunnel, this was pressed into the wall near the entrance.",
			"A seal — wax, but it hasn't aged. The impression is of a cove marker I don't recognise.",
			"Vexa says it's a Tidekin mark. Old coastal family crest.",
			"I catalogued it as evidence but no case requires it.",
			"If it belongs to Tidekin Cove, it should go there.",
			"Take it through proper channels. Whatever those are, in your situation."
		]
	},
	{
		'npc_id': 'lanternrunner_vexa',
		'dialog_id': 'vexa_e_seal_context',
		'dialog': [
			"Tidekin mark. I know that crest.",
			"There's a family in Tidekin Cove who used it on sealed cargo.",
			"Whatever was sealed — it never arrived.",
			"That wax has been waiting to close something ever since."
		]
	},

]

TASKS += [

	# E-1 — Consult Vexa about the seal
	{
		'task_id': 'shallows_mid_city_type_e_consult_vexa',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'lanternrunner_vexa',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lanternrunner_vexa', 'standing_text': [
				"Merrik pulled something out of the tunnel evidence.",
				"A seal I recognise. Come — I'll tell you where it needs to go."
			]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lanternrunner_vexa', 'dialog_id': 'vexa_e_seal_context' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'shallows_mid_city_type_e_collect_seal' }},
		]
	},

	# E-2 — Collect from Merrik
	{
		'task_id': 'shallows_mid_city_type_e_collect_seal',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'tidejudge_merrik',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'tidejudge_merrik', 'standing_text': [
				"Evidence logged. Case closed.",
				"The seal has no jurisdiction here.",
				"Come collect it."
			]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'tidejudge_merrik', 'dialog_id': 'merrik_e_tidekin_seal' }},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'shallows_mid_city_e_tidekin_seal' }},
		]
	},

]


PRIMARY_STORY_SETTINGS = {
	'story_id': 'shallows_mid_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}