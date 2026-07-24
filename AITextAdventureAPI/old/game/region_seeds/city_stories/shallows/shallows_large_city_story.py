ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'saltcaller_renlo',
		'name': 'Renlo Saltcaller',
		'description': (
			'A boisterous trader who smells perpetually of sea brine.'
			' Renlo\'s booming laugh echoes across the market stalls.'
			' He claims to predict storms by tasting the air.'
		)
	},
	{
		'npc_id': 'vaultkeeper_syrin',
		'name': 'Syrin of the Harborlight',
		'description': (
			'A quiet curator who safeguards relics dredged from shipwrecks.'
			' Syrin\'s lantern glows with a pale, underwater shimmer.'
			' She speaks as though every artifact carries a ghost.'
		)
	},
    {
        'npc_id': 'tide_seer_marenna',
        'name': 'Marenna the Tide‑Seer',
        'description': (
            'A wandering mystic who reads tide scars and hears drowned voices carried by the wind.'
        )
    },
    {
        'npc_id': 'stormtide_echo',
        'name': 'Stormtide Echo',
        'description': (
            'A spectral remnant of markets destroyed by ancient storms.'
        )
    },
    {
        'npc_id': 'undertow_voice',
        'name': 'Undertow Voice',
        'description': (
            'A murmuring presence formed from drowned memories deep within the Undertow Vault.'
        )
    }
]


NPC_DIALOG = [

    # --- Base city standing dialog ---

    {
        'npc_id': 'saltcaller_renlo',
        'dialog_id': 'renlo_intro',
        'dialog': [
            "The air tastes wrong.",
            "Storms gather where the sky is clear.",
            "Something beneath the waves stirs the winds."
        ]
    },
    {
        'npc_id': 'vaultkeeper_syrin',
        'dialog_id': 'syrin_intro',
        'dialog': [
            "The relics glow brighter.",
            "They whisper of a Beacon drowned long ago.",
            "If it rises, the tides will follow."
        ]
    },
    {
        'npc_id': 'tide_seer_marenna',
        'dialog_id': 'marenna_intro',
        'dialog': [
            "The tide scars tremble.",
            "A Beacon stirs — a storm‑spirit born of shipwreck light.",
            "If it awakens, the sea will reclaim the coast."
        ]
    },
    {
        'npc_id': 'stormtide_echo',
        'dialog_id': 'stormtide_echo_intro',
        'dialog': [
            "We are the markets the storm devoured.",
            "The Beacon calls the tides to rise again.",
            "It waits deeper in the Undertow Vault."
        ]
    },
    {
        'npc_id': 'undertow_voice',
        'dialog_id': 'undertow_voice_intro',
        'dialog': [
            "The Vault churns with drowned memories.",
            "The Beacon gathers strength.",
            "Only its heart remains to be stilled."
        ]
    },
    {
        'npc_id': 'saltcaller_renlo',
        'dialog_id': 'renlo_closing',
        'dialog': [
            "The winds calm. The tides settle.",
            "You've stilled a storm older than the coast itself.",
            "The Shallows owe you their peace."
        ]
    }

]

NPC_DIALOG += [

    # --- Type E: Brine Compass ---

    {
        'npc_id': 'vaultkeeper_syrin',
        'dialog_id': 'syrin_brine_compass_discovery',
        'dialog': [
            "There's a relic I can't account for — pulled from a wreck three seasons ago and never properly catalogued.",
            "It looks like a compass but it doesn't point north. It points somewhere beneath the harbor floor.",
            "The needle hasn't stopped moving since the tides began behaving strangely."
        ]
    },
    {
        'npc_id': 'tide_seer_marenna',
        'dialog_id': 'marenna_brine_compass_context',
        'dialog': [
            "A Brine Compass. The old navigators made them to chart routes through submerged fracture lines.",
            "The needle points to the nearest open fracture. Right now that fracture is very close.",
            "Whatever is down there guards the approaches. The Stormtide Echo will not let you pass unchallenged."
        ]
    },
    {
        'npc_id': 'stormtide_echo',
        'dialog_id': 'stormtide_echo_compass_guardian',
        'dialog': [
            "The Compass does not leave these waters.",
            "It was made here. It stays here.",
            "You are not a navigator. You are a thief."
        ]
    },
    {
        'npc_id': 'vaultkeeper_syrin',
        'dialog_id': 'syrin_brine_compass_received',
        'dialog': [
            "The needle's settled. It's pointing at you now.",
            "I think it's decided it belongs with whoever carries it next.",
            "I won't pretend to understand that. But I stopped arguing with relics years ago."
        ]
    },

]

NPC_DIALOG += [

    # --- Type F: Rift Observation Log ---

    {
        'npc_id': 'astra_wynn',
        'dialog_id': 'astra_wynn_brineward_arrival',
        'dialog': [
            "The rift near this harbor is the cleanest one I've seen since the Riftwaters crossing.",
            "No distortion, no echo interference. It's like someone prepared it.",
            "I've been logging observation posts like this one. There's a pattern I can't quite close."
        ]
    },
    {
        'npc_id': 'astra_wynn',
        'dialog_id': 'astra_wynn_log_request',
        'dialog': [
            "Syrin has a record of the harbor's tide anomalies going back decades.",
            "I need that data. The fracture timings she logged line up with two other sites I've marked.",
            "Ask her. She trusts vault-keepers more than riftcallers, for obvious reasons."
        ]
    },
    {
        'npc_id': 'vaultkeeper_syrin',
        'dialog_id': 'syrin_astra_data',
        'dialog': [
            "Astra Wynn wants the tide logs? She's been asking since the last storm season.",
            "Fine. But tell her the third anomaly was not a natural fracture event.",
            "Something moved through that rift deliberately. I logged the direction."
        ]
    },
    {
        'npc_id': 'astra_wynn',
        'dialog_id': 'astra_wynn_log_complete',
        'dialog': [
            "Deliberate movement. That matches what I saw at the northern post.",
            "I'm adding this harbor to the log. Two confirmed, one suspected — there's a third site further north.",
            "I'll find it eventually. Take this — it's a copy of everything I've compiled so far.",
            "If you reach that third site before I do, you'll know what to look for."
        ]
    },

]


TASKS = [
	{
		'task_id': 'shallows_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'saltcaller_renlo',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'saltcaller_renlo',
					'standing_text': [
						"Storms and stories—sit and taste the salt while I tell you of the last gale."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'vaultkeeper_syrin',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'vaultkeeper_syrin',
					'standing_text': [
						"Relics remember their voyages—if you listen, the sea will tell you its name."
					]
				}
			}
		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_regional_complete_gate'
                }
            }
		]
	},
    {
        'task_id': 'shallows_large_city_regional_complete_gate',
        'type': 'complete_regional_quests',
        'task_acquire_events': [],
        'task_complete_events': [
            # Type C — gated by chapter 11 being reached
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_type_c_find_dare'
                }
            },
            # Type E — no gate condition, artifact waits in inventory
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_type_e_investigate_compass'
                }
            },
            # Type F — Astra active from Ch.5
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_type_f_find_astra'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_type_d_deliver_brine_compass'
                }
            }
        ]
    },

]

TASKS += [

    # =========================================================
    # TYPE E — Brine Compass
    # Artifact ID: shallows_large_city_e_brine_compass
    # Gates: shallows_large_city Type D (Slot 2) — same city
    # Awarded by: shallows_large_city_regional_complete_gate
    # =========================================================

    {
        'task_id': 'shallows_large_city_type_e_investigate_compass',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vaultkeeper_syrin',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'standing_text': [
                        "There's a relic in the vault I can't explain.",
                        "The needle moves on its own. It's been pointing toward the harbor floor for weeks."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'dialog_id': 'syrin_brine_compass_discovery'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_type_e_consult_marenna'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_large_city_type_e_consult_marenna',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'tide_seer_marenna',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'tide_seer_marenna',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'tide_seer_marenna',
                    'standing_text': [
                        "A Brine Compass. I haven't heard of one surfacing in years.",
                        "The fracture it's pointing to — I know that place."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'tide_seer_marenna',
                    'dialog_id': 'marenna_brine_compass_context'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_type_e_confront_stormtide_echo'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_large_city_type_e_confront_stormtide_echo',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'stormtide_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'stormtide_echo',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'stormtide_echo',
                    'standing_text': [
                        "The Compass does not leave these waters.",
                        "Turn back."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'stormtide_echo',
                    'dialog_id': 'stormtide_echo_compass_guardian'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_type_e_defeat_stormtide_echo'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_large_city_type_e_defeat_stormtide_echo',
        'type': 'defeat',
        'to_type': 'npc',
        'to_id': 'stormtide_echo',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'stormtide_echo',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'shallows_large_city_e_brine_compass'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_type_e_return_to_syrin'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_large_city_type_e_return_to_syrin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vaultkeeper_syrin',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'standing_text': [
                        "The needle stopped moving the moment you stepped back in.",
                        "I think it knows you have it."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'dialog_id': 'syrin_brine_compass_received'
                }
            }
        ]
    },

]

TASKS += [

    # =========================================================
    # TYPE F — Rift Observation Log
    # Faction Item ID: shallows_large_city_f_rift_observation_log
    # Recurring NPC: astra_wynn (Ch.5, Ch.19)
    # Gates: snow_large_city (Frostgate Spire, Ch.19) Type D (Slot 2)
    # Awarded by: shallows_large_city_regional_complete_gate (is_chapter_gte 5)
    # =========================================================

    {
        'task_id': 'shallows_large_city_type_f_find_astra',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'astra_wynn',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'astra_wynn',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'astra_wynn',
                    'standing_text': [
                        "The rift here is unusually clean.",
                        "I've been watching it for two days. Something about it doesn't add up."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'astra_wynn',
                    'dialog_id': 'astra_wynn_brineward_arrival'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_type_f_get_syrin_data'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_large_city_type_f_get_syrin_data',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'astra_wynn',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'astra_wynn',
                    'standing_text': [
                        "Syrin keeps the tide anomaly records.",
                        "I need them. Go ask her — she'll respond better coming from you."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'astra_wynn',
                    'dialog_id': 'astra_wynn_log_request'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_type_f_speak_to_syrin'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_large_city_type_f_speak_to_syrin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vaultkeeper_syrin',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'standing_text': [
                        "Astra Wynn sent you? I've been expecting this.",
                        "I have what she needs."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'dialog_id': 'syrin_astra_data'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_large_city_type_f_deliver_to_astra'
                }
            }
        ]
    },

    {
        'task_id': 'shallows_large_city_type_f_deliver_to_astra',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'astra_wynn',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'astra_wynn',
                    'standing_text': [
                        "You got it. What did she say?"
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'astra_wynn',
                    'dialog_id': 'astra_wynn_log_complete'
                }
            },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'shallows_large_city_f_rift_observation_log'
                }
            }
        ]
    },

]

# ── Type D ── Tidecleaver (mythic weapon) ─────────────────────────────────────
# Gate: player holds brine_compass from the Type E chain (same city, Slot 1 → Slot 2).
# Deliver to Diego → Marenna reads the compass → defeat Undertow Voice → mythic weapon.
# No new NPCs — uses tide_seer_marenna, undertow_voice, and diego (Ch.1 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'tide_seer_marenna',
		'dialog_id': 'marenna_d_compass_read',
		'dialog': [
			"This compass doesn't point to any shore I know.",
			"It reads the Undertow Vault — the drowned chamber beneath the harbor.",
			"A Voice lives there, made from every navigator who never surfaced.",
			"The compass is the key that unlocks its attention.",
			"Silence the Voice and the brine will crystallize into a blade unlike any other."
		]
	},

	{
		'npc_id': 'undertow_voice',
		'dialog_id': 'undertow_voice_d_awakens',
		'dialog': [
			"The compass calls me upward.",
			"Every drowned sailor's last bearing — I carry them all.",
			"You want what the tide guards.",
			"Take it from me if you can."
		]
	},

]

TASKS += [

	# D-0 — Deliver brine_compass to Diego (standalone deliver; unlocks D chain)
	{
		'task_id': 'shallows_large_city_type_d_deliver_brine_compass',
		'type': 'deliver',
		'item_id': 'brine_compass',
		'to_type': 'npc',
		'to_id': 'diego',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"That compass — the needle points somewhere that shouldn't exist.",
						"I've never seen brine-forged metal hold a direction like that.",
						"Find Marenna. She'll know what the tide carved into it."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_large_city_type_d_consult_marenna'
				}
			},
		]
	},

	# D-1 — Consult Marenna for the tide reading
	{
		'task_id': 'shallows_large_city_type_d_consult_marenna',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'tide_seer_marenna',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'tide_seer_marenna',
					'standing_text': [
						"The tide scars shifted when you arrived.",
						"That compass is pulling at every drowned memory in this harbor.",
						"Come quickly — I can read it before the Vault notices."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'tide_seer_marenna',
					'dialog_id': 'marenna_d_compass_read'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_large_city_type_d_meet_undertow_voice'
				}
			},
		]
	},

	# D-2 — Meet the Undertow Voice (boss intro)
	{
		'task_id': 'shallows_large_city_type_d_meet_undertow_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'undertow_voice',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'undertow_voice',
					'standing_text': [
						"The harbor water darkens around the vault entrance.",
						"A low murmur rises — dozens of voices overlapping into one.",
						"The compass has drawn it to the surface."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'undertow_voice',
					'dialog_id': 'undertow_voice_d_awakens'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_large_city_type_d_defeat_undertow_voice'
				}
			},
		]
	},

	# D-3 — Defeat the Undertow Voice; Diego forges the mythic weapon
	{
		'task_id': 'shallows_large_city_type_d_defeat_undertow_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'undertow_voice_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'undertow_voice_1',
					'combat_type': 'boss_battle'
				}
			}
        ],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_shallows_large_tidecleaver'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"The brine crystallized perfectly once the Voice was silenced.",
						"I've worked it into the blade — it cuts clean through anything the tide would carry.",
						"This weapon knows where it's going before you do."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'tide_seer_marenna',
					'standing_text': [
						"The tide scars have gone quiet.",
						"The Vault is empty now.",
						"Whatever bearings those sailors carried — they can rest."
					]
				}
			},
		]
	},

]

# ── Type E ── Brine Compass → gates Shallows Large Type D ─────────────────────
# Syrin the Vaultkeeper recovered a compass from the Undertow Vault that
# aligns to storm-spirit traces rather than magnetic north. No new NPCs. No dungeon.

NPC_DIALOG += [

	{
		'npc_id': 'vaultkeeper_syrin',
		'dialog_id': 'syrin_e_brine_compass',
		'dialog': [
			"After the Undertow cleared, I found this at the base of the vault.",
			"A compass — but it doesn't point north.",
			"(watching the needle drift)",
			"It points toward storm-spirit traces. Things that have moved through salt water and void both.",
			"I've catalogued it. I've dated it. I still don't know what it opens.",
			"But it's too specific to be decorative.",
			"Take it. The sea will tell you where it belongs."
		]
	},

]

TASKS += [

	# E-1 — Meet Syrin to receive the Brine Compass
	{
		'task_id': 'shallows_large_city_type_e_meet_syrin',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'vaultkeeper_syrin',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'vaultkeeper_syrin', 'standing_text': [
				"Something came up from the vault floor after the Beacon fell.",
				"A compass. Not for navigation — for something else.",
				"Come see it."
			]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vaultkeeper_syrin', 'dialog_id': 'syrin_e_brine_compass' }},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'shallows_large_city_e_brine_compass' }},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
	'story_id': 'shallows_large_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}