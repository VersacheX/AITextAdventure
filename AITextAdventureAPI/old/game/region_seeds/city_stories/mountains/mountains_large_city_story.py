ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'rustscribe_gorvak',
		'name': 'Gorvak Rustscribe',
		'description': (
			'A gruff archivist who catalogs the city\'s industrial relics.'
			' Gorvak\'s hands are permanently stained with iron dust.'
			' He treats every rusted gear like a sacred artifact.'
		)
	},
	{
		'npc_id': 'relaytech_sindra',
		'name': 'Sindra Coilrunner',
		'description': (
			'A quick‑thinking technician who maintains the volatile relay conduits.'
			' Sparks dance across Sindra\'s gloves as she works.'
			' She claims the machinery "talks back" when she listens closely.'
		)
	},
    {
        'npc_id': 'forge_seer_brannoc',
        'name': 'Brannoc the Forge‑Seer',
        'description': (
            'A hermit who listens to the mountain\'s internal machinery. '
            'Brannoc senses disturbances in the ancient forges beneath the peaks.'
        )
    },
    {
        'npc_id': 'gearghost',
        'name': 'Gearghost',
        'description': (
            'A spectral remnant of long‑dead machinery, animated by the Iron Resonance.'
        )
    },
    {
        'npc_id': 'conduit_echo',
        'name': 'Conduit Echo',
        'description': (
            'A volatile presence formed from unstable relay energy deep within the Conduit Maw.'
        )
    }
]


NPC_DIALOG = [

    # --- Base city standing dialog ---

    {
        'npc_id': 'rustscribe_gorvak',
        'dialog_id': 'gorvak_intro',
        'dialog': [
            "The relics hum louder than they should.",
            "Old gears turn without hands to guide them.",
            "Something deep below has awakened."
        ]
    },
    {
        'npc_id': 'relaytech_sindra',
        'dialog_id': 'sindra_intro',
        'dialog': [
            "The conduits spark in strange rhythms.",
            "It's like the mountain is trying to speak.",
            "Whatever's down there is messing with the relay grid."
        ]
    },
    {
        'npc_id': 'forge_seer_brannoc',
        'dialog_id': 'brannoc_intro',
        'dialog': [
            "The mountain's heart‑gears turn again.",
            "A Resonance stirs — metal remembering its purpose.",
            "If it grows stronger, the whole range will shake itself apart."
        ]
    },
    {
        'npc_id': 'gearghost',
        'dialog_id': 'gearghost_intro',
        'dialog': [
            "We are the gears that died turning.",
            "The Resonance calls us back to motion.",
            "It waits deeper in the Conduit Maw."
        ]
    },
    {
        'npc_id': 'conduit_echo',
        'dialog_id': 'conduit_echo_intro',
        'dialog': [
            "The Maw hums with unstable power.",
            "The Resonance grows louder.",
            "Only its core remains to be silenced."
        ]
    },
    {
        'npc_id': 'rustscribe_gorvak',
        'dialog_id': 'gorvak_closing',
        'dialog': [
            "The mountain quiets. The gears rest again.",
            "You've stilled a force older than any forge.",
            "The peaks owe you their peace."
        ]
    }

]

NPC_DIALOG += [

    # --- Type C: Spark Maddox ---

    {
        'npc_id': 'spark_maddox',
        'dialog_id': 'spark_type_c_intro',
        'dialog': [
            "Oh good, a person. I've been talking to the relay conduits for two days and they're terrible conversationalists.",
            "There's a resonance frequency coming out of the deep forge that should not be possible.",
            "Sindra thinks it's a malfunction. Gorvak thinks it's history. I think it's an invitation.",
            "I want in. Do you?"
        ]
    },
    {
        'npc_id': 'spark_maddox',
        'dialog_id': 'spark_type_c_sindra_check',
        'dialog': [
            "Sindra vouched for me? Ha! She told me yesterday I was a liability.",
            "She's right, technically. Doesn't mean she's wrong to let me try.",
            "The best discoveries always look like liabilities at first."
        ]
    },
    {
        'npc_id': 'spark_maddox',
        'dialog_id': 'spark_type_c_join',
        'dialog': [
            "Alright. Partnership. I invent things, you make sure they don't explode — or at least not at the wrong moment.",
            "This forge has secrets older than any catalog Gorvak has. I intend to find every single one.",
            "Let's go."
        ]
    },

]

NPC_DIALOG += [

    # --- Type E: Forge Echo Core ---

    {
        'npc_id': 'rustscribe_gorvak',
        'dialog_id': 'gorvak_echo_core_discovery',
        'dialog': [
            "I found a reference in the oldest catalog — predates the city's founding.",
            "The original forge architects built a resonance core into the mountain's deepest chamber.",
            "It was never meant to be extracted. They called it the Echo Core — the forge's memory made solid."
        ]
    },
    {
        'npc_id': 'forge_seer_brannoc',
        'dialog_id': 'brannoc_echo_core_context',
        'dialog': [
            "The Echo Core is not dangerous on its own.",
            "It absorbs the resonance of everything forged above it — centuries of metalwork compressed into one object.",
            "The Gearghost will be drawn to it. They always guard what the mountain values most."
        ]
    },
    {
        'npc_id': 'gearghost',
        'dialog_id': 'gearghost_echo_guardian',
        'dialog': [
            "The Core is the mountain's oldest memory.",
            "You would carry it away from here.",
            "We do not permit that."
        ]
    },
    {
        'npc_id': 'rustscribe_gorvak',
        'dialog_id': 'gorvak_echo_core_received',
        'dialog': [
            "You actually retrieved it intact.",
            "I can feel it humming — every alloy, every strike, every forge-fire since the mountain was first worked.",
            "This doesn't belong in an archive. It belongs with someone who'll use it.",
            "Keep it. Something out there will recognize what it is."
        ]
    },

]


TASKS = [
	{
		'task_id': 'mountains_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'rustscribe_gorvak',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rustscribe_gorvak',
					'standing_text': [
						"Old gears have songs—come, tell me what yours did before the rust."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'relaytech_sindra',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'relaytech_sindra',
					'standing_text': [
						"Sparks tell stories—share your curious misfires and I'll laugh with you."
					]
				}
			}
		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_regional_complete_gate'
                }
            }
		]
	},
    {
        'task_id': 'mountains_large_city_regional_complete_gate',
        'type': 'complete_regional_quests',
        'task_acquire_events': [],
        'task_complete_events': [
            # Type C — gated by chapter 4 being reached
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_type_c_find_spark'
                }
            },
            # Type E — no gate condition, artifact waits in inventory
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_type_e_investigate_echo'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_type_d_deliver_armor_key'
                }
            }
        ]
    },

]

TASKS += [

    # =========================================================
    # TYPE C — Spark Maddox
    # Extended Character: spark_maddox
    # Final event: character_join
    # Awarded by: mountains_large_city_regional_complete_gate (is_chapter_gte 4)
    # =========================================================

    {
        'task_id': 'mountains_large_city_type_c_find_spark',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'spark_maddox',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'spark_maddox',
                    'location': 'region_city_other3'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'spark_maddox',
                    'standing_text': [
                        "The conduits are doing something they have absolutely no business doing.",
                        "It's incredible. Also potentially catastrophic. Mostly incredible."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'spark_maddox',
                    'dialog_id': 'spark_type_c_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_type_c_consult_sindra'
                }
            }
        ]
    },

    {
        'task_id': 'mountains_large_city_type_c_consult_sindra',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'relaytech_sindra',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'relaytech_sindra',
                    'standing_text': [
                        "Spark? He's been poking at the deep conduits all week.",
                        "Honestly if anyone can figure out what's happening down there, it's him.",
                        "Just make sure he doesn't blow anything critical."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'spark_maddox',
                    'dialog_id': 'spark_type_c_sindra_check'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_type_c_earn_spark'
                }
            }
        ]
    },

    {
        'task_id': 'mountains_large_city_type_c_earn_spark',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'spark_maddox',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'spark_maddox',
                    'standing_text': [
                        "Sindra gave the nod? That's more than I expected.",
                        "Alright. Let's talk terms."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'spark_maddox',
                    'dialog_id': 'spark_type_c_join'
                }
            },
            {
                'event_type': 'character_join',
                'params': {
                    'character_id': 'spark_maddox'
                }
            }
        ]
    },

]

TASKS += [

    # =========================================================
    # TYPE E — Forge Echo Core
    # Artifact ID: mountains_large_city_e_forge_echo_core
    # Gates: mountains_mid_city (Gallows Rift, Ch.17) Type D (Slot 2)
    # Awarded by: mountains_large_city_regional_complete_gate
    # =========================================================

    {
        'task_id': 'mountains_large_city_type_e_investigate_echo',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rustscribe_gorvak',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rustscribe_gorvak',
                    'standing_text': [
                        "I've been cross-referencing the oldest catalogs.",
                        "There's something in the founding records that none of the newer archivists have documented."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rustscribe_gorvak',
                    'dialog_id': 'gorvak_echo_core_discovery'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_type_e_consult_brannoc'
                }
            }
        ]
    },

    {
        'task_id': 'mountains_large_city_type_e_consult_brannoc',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'forge_seer_brannoc',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'forge_seer_brannoc',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'forge_seer_brannoc',
                    'standing_text': [
                        "The mountain's memory stirs.",
                        "I have felt the Echo Core pulse twice this season."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'forge_seer_brannoc',
                    'dialog_id': 'brannoc_echo_core_context'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_type_e_confront_gearghost'
                }
            }
        ]
    },

    {
        'task_id': 'mountains_large_city_type_e_confront_gearghost',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'gearghost',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'gearghost',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'gearghost',
                    'standing_text': [
                        "You come for the Core.",
                        "You will not have it."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'gearghost',
                    'dialog_id': 'gearghost_echo_guardian'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_type_e_defeat_gearghost'
                }
            }
        ]
    },

    {
        'task_id': 'mountains_large_city_type_e_defeat_gearghost',
        'type': 'defeat',
        'to_type': 'npc',
        'to_id': 'gearghost',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'mountains_large_city_e_forge_echo_core'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_type_e_return_to_gorvak'
                }
            }
        ]
    },

    {
        'task_id': 'mountains_large_city_type_e_return_to_gorvak',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rustscribe_gorvak',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rustscribe_gorvak',
                    'standing_text': [
                        "You found it. I can hear it from here.",
                        "Come — I need to see it with my own eyes."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rustscribe_gorvak',
                    'dialog_id': 'gorvak_echo_core_received'
                }
            }
        ]
    },

]

NPC_DIALOG += [

	{
		'npc_id': 'rustscribe_gorvak',
		'dialog_id': 'gorvak_d_key_assay',
		'dialog': [
			"This resonance key — it came out of the rift?",
			"The frequency it carries matches the Conduit Maw's deepest chamber.",
			"Something inside that chamber forged itself into armor long before the city existed.",
			"Brawn can work with this — but the Conduit Echo will fight to keep it.",
			"It guards the armoring-frequency like a living lock."
		]
	},

	{
		'npc_id': 'conduit_echo',
		'dialog_id': 'conduit_echo_d_awakens',
		'dialog': [
			"The resonance key hums.",
			"You want what the Maw has held for centuries.",
			"Prove you can survive the frequency first."
		]
	},

]

TASKS += [

	# D-0 — Deliver mountains_large_city_armor_key to Brawn (standalone deliver; unlocks D chain)
	{
		'task_id': 'mountains_large_city_type_d_deliver_armor_key',
		'type': 'deliver',
		'item_id': 'mountains_large_city_armor_key',
		'to_type': 'npc',
		'to_id': 'brawn',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'brawn',
					'standing_text': [
						"That key — I can feel the forge-frequency vibrating off it from here.",
						"Something in this city is waiting to be unlocked.",
						"Show Gorvak first. He'll know which chamber it belongs to."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_large_city_type_d_consult_gorvak'
				}
			},
		]
	},

	# D-1 — Consult Gorvak for the resonance assay
	{
		'task_id': 'mountains_large_city_type_d_consult_gorvak',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rustscribe_gorvak',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rustscribe_gorvak',
					'standing_text': [
						"The relics catalog trembled when you walked in.",
						"Whatever you're carrying has a resonance signature I've logged before — in theory only.",
						"Let me see it."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rustscribe_gorvak',
					'dialog_id': 'gorvak_d_key_assay'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_large_city_type_d_meet_conduit_echo'
				}
			},
		]
	},

	# D-2 — Meet the Conduit Echo (boss intro)
	{
		'task_id': 'mountains_large_city_type_d_meet_conduit_echo',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'conduit_echo',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'conduit_echo',
					'standing_text': [
						"The relay conduits deep in the Maw crackle with sudden violence.",
						"The resonance key has called the Echo forward.",
						"Sindra says the grid is spiking — whatever is down there is aware."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'conduit_echo',
					'dialog_id': 'conduit_echo_d_awakens'
				}
			},
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'conduit_echo_1',
					'combat_type': 'boss_encounter'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_large_city_type_d_defeat_conduit_echo'
				}
			},
		]
	},

	# D-3 — Defeat the Conduit Echo; Brawn forges the mythic armor
	{
		'task_id': 'mountains_large_city_type_d_defeat_conduit_echo',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'conduit_echo_1',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_mountains_large_ironveil_warplate'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'brawn',
					'standing_text': [
						"The Conduit Maw's armoring-frequency is finally free.",
						"I've worked it into the warplate — it'll hold against anything the rift throws at you.",
						"This is the best work I've ever done."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rustscribe_gorvak',
					'standing_text': [
						"I've updated the relics catalog.",
						"First time in twenty years I've had something new worth logging.",
						"The Maw is quiet now."
					]
				}
			},
		]
	},

]

# ── Type E ── Forge Echo Core → gates Mountains Mid Type D (Gallows Rift) ─────
# Brannoc the Forge-Seer extracted a resonance core from the Conduit Maw
# after the Iron Resonance was defeated. No new NPCs. No dungeon.

NPC_DIALOG += [

	{
		'npc_id': 'forge_seer_brannoc',
		'dialog_id': 'brannoc_e_echo_core',
		'dialog': [
			"When the Iron Resonance collapsed, it left a core.",
			"A crystallised echo of every forge-heat this range ever produced.",
			"It doesn't belong here — this mountain's done with it.",
			"Gallows Rift has a cavity in its deep stone that's been waiting for something like this.",
			"I've felt it for years. Now I know what fills it.",
			"Take the core there. Don't drop it — it vibrates."
		]
	},
	{
		'npc_id': 'relaytech_sindra',
		'dialog_id': 'sindra_e_core_confirms',
		'dialog': [
			"Brannoc's right — the conduit grid reads that core as something the mountain expelled.",
			"It's not waste. It's a concentrated signal.",
			"Somewhere in the range, there's a receiver that's been dormant waiting for this frequency.",
			"Gallows Rift fits the harmonic profile."
		]
	},

]

TASKS += [

	# E-1 — Consult Sindra about the core
	{
		'task_id': 'mountains_large_city_type_e_consult_sindra',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'relaytech_sindra',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'relaytech_sindra', 'standing_text': [
				"The Resonance left something behind in the Maw.",
				"Brannoc pulled it out. I've been trying to read its frequency.",
				"Come look at it with me."
			]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'relaytech_sindra', 'dialog_id': 'sindra_e_core_confirms' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_large_city_type_e_collect_core' }},
		]
	},

	# E-2 — Collect from Brannoc
	{
		'task_id': 'mountains_large_city_type_e_collect_core',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'forge_seer_brannoc',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'forge_seer_brannoc', 'standing_text': [
				"The core is ready.",
				"The mountain's told me all it can.",
				"Gallows Rift is waiting."
			]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'forge_seer_brannoc', 'dialog_id': 'brannoc_e_echo_core' }},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'mountains_large_city_e_forge_echo_core' }},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
    'story_id': 'mountains_large_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}