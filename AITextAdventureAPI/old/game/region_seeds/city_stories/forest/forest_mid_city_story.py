ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'emberwitch_thera',
		'name': 'Thera of the Emberlight',
		'description': (
			'A witch whose lantern glows with shifting orange runes.'
			' Thera studies flame‑born spirits and believes each spark carries a prophecy.'
			' Her laughter crackles like burning cedar.'
		)
	},
	{
		'npc_id': 'alchemist_mirlo',
		'name': 'Mirlo the Moonbrewer',
		'description': (
			'A wide-eyed alchemist obsessed with lunar infusions and bubbling concoctions.'
			' Mirlo\'s potions glow with soft moonlight, even underground.'
			' He often forgets whether he\'s brewing medicine or mild chaos.'
		),
		"psychology": {
			"mbti": "ENTP",
			"dominant": "Ne — Endlessly curious. Combines ingredients, theories, and side-effects with reckless, joyful creativity.",
			"auxiliary": "Ti — Reverse-engineers his own accidents with sharp internal logic. He understands why the chaos happened, even when he can't stop it.",
			"tertiary": "Fe — Genuinely delighted by other people's reactions to his brews. Social warmth drives his sharing instinct.",
			"inferior": "Si — Loses track of what he's already tried, repeating experiments and occasionally rediscovering the same disaster."
		},
		"enneagram": {
			"enneagram_type": "7w6",
			"core_fear": "Being deprived, bored, or trapped in limitation.",
			"core_desire": "To have a life full of stimulating discovery.",
			"defense_mechanism": "Rationalization — Frames dangerous experiments as necessary research, avoiding the weight of their potential consequences.",
			"stress_line": "Moves to Type 1 — Becomes rigid and perfectionistic when experiments spiral out of control.",
			"growth_line": "Moves to Type 5 — Develops genuine expertise and depth when he commits to studying a single phenomenon.",
			"instinctual_variant": "so/sp — Engages socially through his brews, securing his place in the community by being indispensable and entertaining."
		}
	},
    {
        'npc_id': 'glimmer_hermit_vael',
        'name': 'Vael the Glimmer-Hermit',
        'description': (
            'A wandering mystic who reads moon-embers drifting through the forest. '
            'Vael senses disturbances where flame and night intertwine.'
        ),
		"psychology": {
			"mbti": "INTJ",
			"dominant": "Ni — Reads the world through invisible patterns. Moon-embers tell him what others cannot perceive.",
			"auxiliary": "Te — Communicates observations with blunt, efficient precision. He doesn't waste words.",
			"tertiary": "Fi — Has strong private convictions about the forest's nature and his role within it.",
			"inferior": "Se — Rarely engages with the physical world directly. When forced to, he becomes briefly overwhelmed."
		},
		"enneagram": {
			"enneagram_type": "5w4",
			"core_fear": "Being useless or overwhelmed.",
			"core_desire": "To understand the world through observation.",
			"defense_mechanism": "Isolation — Withdraws into solitary study to maintain clarity and avoid emotional entanglement.",
			"stress_line": "Moves to Type 7 — Becomes restless and scattered when his patterns refuse to resolve.",
			"growth_line": "Moves to Type 8 — Applies his knowledge with decisive, protective action.",
			"instinctual_variant": "sp/sx — Hermitic and self-sufficient, engaging deeply only with phenomena he deems worthy of attention."
		}
    },
    {
        'npc_id': 'riftspark',
        'name': 'Riftspark',
        'description': (
            'A flickering ember‑spirit born from unstable flame‑magic within the Embergrove Rift.'
        )
    },
    {
        'npc_id': 'lunarcask_shade',
        'name': 'Lunarcask Shade',
        'description': (
            'A spectral figure formed from condensed moonlight and alchemical fumes.'
        )
    }
]


NPC_DIALOG = [

    # --- Base city standing dialog ---

    {
        'npc_id': 'emberwitch_thera',
        'dialog_id': 'thera_intro',
        'dialog': [
            "The lantern's sparks twist into warnings.",
            "Something is merging flame‑spirits with moonlight.",
            "If it completes the ritual, night itself will change."
        ]
    },
    {
        'npc_id': 'alchemist_mirlo',
        'dialog_id': 'mirlo_intro',
        'dialog': [
            "My moonbrews keep reacting to a strange pulse.",
            "It's like the forest is brewing something of its own.",
            "Whatever it is… it's unstable."
        ]
    },
    {
        'npc_id': 'glimmer_hermit_vael',
        'dialog_id': 'vael_intro',
        'dialog': [
            "Moon‑embers drift toward the Rift.",
            "A Crucible forms — half flame, half night.",
            "If it awakens fully, the forest's cycle will break."
        ]
    },
    {
        'npc_id': 'riftspark',
        'dialog_id': 'riftspark_intro',
        'dialog': [
            "The Rift burns cold and glows hot.",
            "The Crucible feeds on contradictions.",
            "It waits deeper below."
        ]
    },
    {
        'npc_id': 'lunarcask_shade',
        'dialog_id': 'lunarcask_shade_intro',
        'dialog': [
            "The Depths churn with lunar residue.",
            "The Crucible stirs, shaping a new night.",
            "Only its core remains to be shattered."
        ]
    },
    {
        'npc_id': 'emberwitch_thera',
        'dialog_id': 'thera_closing',
        'dialog': [
            "The Crucible is extinguished.",
            "The lantern's sparks settle — the futures calm.",
            "You've kept the forest's night from fracturing."
        ]
    }

]

NPC_DIALOG += [

    # --- Type E: Mycelia Memory Spore ---

    {
        'npc_id': 'alchemist_mirlo',
        'dialog_id': 'mirlo_spore_discovery',
        'dialog': [
            "Every moonbrew I've made this week glows green. Not the nice green — the wrong green.",
            "I traced the interference. There's a pulse coming from somewhere under the forest floor.",
            "Fungal, I think. Old. Like it's been waiting down there longer than this city has existed."
        ]
    },
    {
        'npc_id': 'glimmer_hermit_vael',
        'dialog_id': 'vael_spore_context',
        'dialog': [
            "A Mycelium Hollow. I've felt it — a node where the forest remembers through spore and root.",
            "What grows there is not dangerous. It simply... accumulates.",
            "One specimen at the core carries a century of absorbed memory. Retrieve it intact."
        ]
    },
    {
        'npc_id': 'riftspark',
        'dialog_id': 'riftspark_hollow_warning',
        'dialog': [
            "The Hollow breathes.",
            "Whatever feeds on memory down there does not welcome visitors.",
            "It will try to keep what it has."
        ]
    },
    {
        'npc_id': 'alchemist_mirlo',
        'dialog_id': 'mirlo_spore_received',
        'dialog': [
            "Oh — oh, this is extraordinary.",
            "The moonbrews have gone completely still. Like they recognise it.",
            "I don't know what it is, but it doesn't belong here. Keep it. Someone else will."
        ]
    },

]

NPC_DIALOG += [

    # --- Type C: Sera Flameweaver ---

    {
        'npc_id': 'sera_flameweaver',
        'dialog_id': 'sera_type_c_intro',
        'dialog': [
            "Oh! You actually stopped. Most people walk past.",
            "I've been watching the Rift from here for three days. The way it pulses — it's not random, it's emotional.",
            "Flame magic responds to feeling. Whatever is inside that Rift is feeling something enormous.",
            "I want to understand it. I think you do too."
        ]
    },
    {
        'npc_id': 'sera_flameweaver',
        'dialog_id': 'sera_type_c_thera_reaction',
        'dialog': [
            "Thera said that? She sees the sparks and calls them warnings.",
            "I see the sparks and call them invitations.",
            "We're both right. That's what makes this so interesting."
        ]
    },
    {
        'npc_id': 'sera_flameweaver',
        'dialog_id': 'sera_type_c_join',
        'dialog': [
            "You're not going to tell me to be careful, are you.",
            "Good. I've heard it. It never helps.",
            "I'll come with you. The fire in this forest has things to say and I intend to hear all of them."
        ]
    },

]


TASKS = [
	{
		'task_id': 'forest_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'emberwitch_thera',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'emberwitch_thera',
					'standing_text': [
						"The lantern shows small futures; stay and see what tonight whispers to you."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'alchemist_mirlo',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'alchemist_mirlo',
					'standing_text': [
						"I tinker with moonlight; tell me a tale and I'll brew it into a memory."
					]
				}
			}
		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_regional_complete_gate'
                }
            }
		]
	},
    {
        'task_id': 'forest_mid_city_regional_complete_gate',
        'type': 'complete_regional_quests',
        'task_acquire_events': [],
        'task_complete_events': [
            # Type E — no gate condition, artifact waits in inventory
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_type_e_investigate_pulse'
                }
            },
            # Type C — gated by chapter 2 being reached
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_type_c_find_sera'
                },
                'condition': {
                    'type': 'is_chapter_gte',
                    'params': { 'chapter': 2 }
                }
            }
        ]
    },

]

TASKS += [

    # =========================================================
    # TYPE E — Mycelia Memory Spore
    # Artifact ID: forest_mid_city_e_mycelia_memory_spore
    # Gates: forest_small_city (Thornshade Hamlet, Ch.16) Type D (Slot 3)
    # Awarded by: forest_mid_city_regional_complete_gate
    # =========================================================

    {
        'task_id': 'forest_mid_city_type_e_investigate_pulse',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'alchemist_mirlo',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'alchemist_mirlo',
                    'standing_text': [
                        "Something underground is interfering with all my brews.",
                        "It's not the Rift — it's older. Deeper."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'alchemist_mirlo',
                    'dialog_id': 'mirlo_spore_discovery'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_type_e_consult_vael'
                }
            }
        ]
    },

    {
        'task_id': 'forest_mid_city_type_e_consult_vael',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'glimmer_hermit_vael',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'glimmer_hermit_vael',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'glimmer_hermit_vael',
                    'standing_text': [
                        "I felt it too. Something below the roots has been awake for a long time.",
                        "Not hostile. But it does not give up what it holds easily."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'glimmer_hermit_vael',
                    'dialog_id': 'vael_spore_context'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_type_e_confront_riftspark'
                }
            }
        ]
    },

    {
        'task_id': 'forest_mid_city_type_e_confront_riftspark',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'riftspark',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'riftspark',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'riftspark',
                    'standing_text': [
                        "The Hollow breathes.",
                        "You should not be here."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'riftspark',
                    'dialog_id': 'riftspark_hollow_warning'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_type_e_defeat_riftspark'
                }
            }
        ]
    },

    {
        'task_id': 'forest_mid_city_type_e_defeat_riftspark',
        'type': 'defeat',
        'to_type': 'npc',
        'to_id': 'riftspark',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'give_item',
                'params': {
                    'item_id': 'forest_mid_city_e_mycelia_memory_spore'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_type_e_return_to_mirlo'
                }
            }
        ]
    },

    {
        'task_id': 'forest_mid_city_type_e_return_to_mirlo',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'alchemist_mirlo',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'alchemist_mirlo',
                    'standing_text': [
                        "You're back! And the pulse stopped — did you find something?"
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'alchemist_mirlo',
                    'dialog_id': 'mirlo_spore_received'
                }
            }
        ]
    },

]

TASKS += [

    # =========================================================
    # TYPE C — Sera Flameweaver
    # Extended Character: sera_flameweaver
    # Final event: character_join
    # Awarded by: forest_mid_city_regional_complete_gate (is_chapter_gte 2)
    # =========================================================

    {
        'task_id': 'forest_mid_city_type_c_find_sera',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'sera_flameweaver',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'sera_flameweaver',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'sera_flameweaver',
                    'standing_text': [
                        "The Rift pulses like a heartbeat.",
                        "I've been trying to figure out whose."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'sera_flameweaver',
                    'dialog_id': 'sera_type_c_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_type_c_consult_thera'
                }
            }
        ]
    },

    {
        'task_id': 'forest_mid_city_type_c_consult_thera',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'emberwitch_thera',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'emberwitch_thera',
                    'standing_text': [
                        "A fire mage watching the Rift? That's either very wise or very reckless.",
                        "Bring her to me. I want to read her lantern."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'sera_flameweaver',
                    'dialog_id': 'sera_type_c_thera_reaction'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_mid_city_type_c_earn_sera'
                }
            }
        ]
    },

    {
        'task_id': 'forest_mid_city_type_c_earn_sera',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'sera_flameweaver',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'sera_flameweaver',
                    'standing_text': [
                        "I've made my decision.",
                        "Thera sees warnings. I see invitations. You're the only one who seems curious about both."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'sera_flameweaver',
                    'dialog_id': 'sera_type_c_join'
                }
            },
            {
                'event_type': 'character_join',
                'params': {
                    'npc_id': 'sera_flameweaver'
                }
            }
        ]
    },

]

# ── Type D ── Moonbriar Lantern (mythic accessory) ───────────────────────────
# Gate: player holds thornshade_root_graft from the Ch.16 Type E chain.
# Deliver to Mira → Thera reads the graft → defeat Lunarcask Shade → mythic accessory.
# No new NPCs — uses emberwitch_thera, lunarcask_shade, and mira (Ch.2 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'emberwitch_thera',
		'dialog_id': 'thera_d_graft_read',
		'dialog': [
			"This root graft carries moonfire residue — Thornshade's oldest grove memories.",
			"The Lunarcask Shade has been feeding on exactly this frequency.",
			"If we can draw it out with the graft's resonance, its moonlight solidifies.",
			"Solidified moonlight — Mira can bind that into something extraordinary."
		]
	},

	{
		'npc_id': 'lunarcask_shade',
		'dialog_id': 'lunarcask_shade_d_awakens',
		'dialog': [
			"The root-song reaches me.",
			"You bring the grove's memory here.",
			"I will take it — and everything else."
		]
	},

]

TASKS += [

	# D-0 — Deliver thornshade_root_graft to Mira (standalone deliver; unlocks D chain)
	{
		'task_id': 'forest_mid_city_type_d_deliver_root_graft',
		'type': 'deliver',
		'item_id': 'thornshade_root_graft',
		'to_type': 'npc',
		'to_id': 'mira',
		'gate': {
			'has_item': 'thornshade_root_graft'
		},
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"That graft — I've been looking for something like this for years.",
						"The grove residue on it is unlike anything from a recent harvest.",
						"Show Thera first. She'll know exactly what we can do with it."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_mid_city_type_d_consult_thera'
				}
			},
		]
	},

	# D-1 — Consult Thera for the moonfire reading
	{
		'task_id': 'forest_mid_city_type_d_consult_thera',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'emberwitch_thera',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'emberwitch_thera',
					'standing_text': [
						"I felt the moonfire shift the moment you entered the grove.",
						"That root you carry — it called to the Lunarcask Shade.",
						"Come. We need to speak before it finds you first."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'emberwitch_thera',
					'dialog_id': 'thera_d_graft_read'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_mid_city_type_d_meet_lunarcask_shade'
				}
			},
		]
	},

	# D-2 — Meet the Lunarcask Shade (boss intro)
	{
		'task_id': 'forest_mid_city_type_d_meet_lunarcask_shade',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'lunarcask_shade',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'lunarcask_shade',
					'standing_text': [
						"A cold shimmer drifts at the grove's edge.",
						"The moonlight here feels wrong — too heavy, too hungry.",
						"Something has been waiting here for the root graft's return."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'lunarcask_shade',
					'dialog_id': 'lunarcask_shade_d_awakens'
				}
			},
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'lunarcask_shade_1',
					'combat_type': 'boss_encounter'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_mid_city_type_d_defeat_lunarcask_shade'
				}
			},
		]
	},

	# D-3 — Defeat the Lunarcask Shade; Mira crafts the mythic accessory
	{
		'task_id': 'forest_mid_city_type_d_defeat_lunarcask_shade',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'lunarcask_shade_1',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_forest_mid_moonbriar_lantern'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"The solidified moonlight is perfect.",
						"I've bound it into the lantern — it will guide you through any darkness.",
						"Even the kind that has no light to reflect."
					]
				}
			},
		]
	},

]
# ── Type E ── Mycelia Memory Spore → gates Forest Mid Type D (Thornshade) ─────
# Mirlo the Moonbrewer accidentally cultured a spore during one of his lunar
# infusions — it carries compressed forest memory. No new NPCs. No dungeon.

NPC_DIALOG += [

	{
		'npc_id': 'alchemist_mirlo',
		'dialog_id': 'mirlo_e_memory_spore',
		'dialog': [
			"Oh! You're here about the spore.",
			"I didn't mean to grow it — I was trying to infuse moonlight into a standard restorative.",
			"The mycelia absorbed the brew instead and... compressed something. A memory. A big one.",
			"(holds up a faintly glowing vial)",
			"The Glimmer-Hermit says it's from the forest's first winter. Whatever that means.",
			"I can't use it. My notes say it wants somewhere older. Take it before it decides to bloom."
		]
	},
	{
		'npc_id': 'glimmer_hermit_vael',
		'dialog_id': 'vael_e_spore_context',
		'dialog': [
			"That spore holds a memory older than the city.",
			"The mycelium network preserves what trees forget.",
			"Thornshade's roots have been reaching for something like this for years.",
			"It will find its way there eventually. Better carried than drifting."
		]
	},

]

TASKS += [

	# E-1 — Consult Vael about the spore
	{
		'task_id': 'forest_mid_city_type_e_meet_vael',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'glimmer_hermit_vael',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'glimmer_hermit_vael', 'standing_text': [
				"Mirlo's latest accident has produced something worth examining.",
				"Come. I'll tell you what the moon-embers say about it."
			]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glimmer_hermit_vael', 'dialog_id': 'vael_e_spore_context' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'forest_mid_city_type_e_collect_spore' }},
		]
	},

	# E-2 — Collect from Mirlo
	{
		'task_id': 'forest_mid_city_type_e_collect_spore',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'alchemist_mirlo',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'alchemist_mirlo', 'standing_text': [
				"It's been glowing brighter since this morning.",
				"I really think it wants to leave."
			]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'alchemist_mirlo', 'dialog_id': 'mirlo_e_memory_spore' }},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'forest_mid_city_e_mycelia_memory_spore' }},
		]
	},

]


PRIMARY_STORY_SETTINGS = {
    'story_id': 'forest_mid_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}