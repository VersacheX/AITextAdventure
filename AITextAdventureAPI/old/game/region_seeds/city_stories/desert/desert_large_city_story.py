ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'kadeem',
		'name': 'Kadeem',
		'description': (
			'A wiry, quick-tongued merchant who runs a stall within The Black Market Guild. '
			'He moves rare and illicit goods through shadowed backrooms, always watching for opportunity.'
		)
	},
	{
		'npc_id': 'mara',
		'name': 'Mara',
		'description': (
			"A smooth, well-dressed broker who operates out of Broker's Hideout. "
			'She arranges favors, introductions, and discreet exchanges for the right price.'
		)
	},
    {
        'npc_id': 'rhyla',
        'name': 'Rhyla the Echo-Binder',
        'description': (
            'A desert mystic who can hear the "songs" of shifting dunes. '
            'She studies the Dune Choir and knows their ancient patterns.'
        )
    },
    {
        'npc_id': 'choir_echo',
        'name': 'Choir Echo',
        'description': (
            'A humanoid shape formed from vibrating sand. It speaks in layered voices, '
            'each one a memory of the desert.'
        )
    },
    {
        'npc_id': 'archive_voice',
        'name': 'Archive Voice',
        'description': (
            'A spectral librarian of the Sunken Archive, bound to drifting shelves of half-buried knowledge.'
        )
    }
]


# --- Base city standing dialog ---
NPC_DIALOG = [
	{
		'npc_id': 'kadeem',
		'dialog_id': 'kadeem_intro',
		'dialog': [
			"You look like someone who appreciates a good find.",
			"I can get you curious trinkets, weapons with a story, or information—for a fee, of course."
		]
	},
	{
		'npc_id': 'mara',
		'dialog_id': 'mara_intro',
		'dialog': [
			"Business moves fast in The Desert Metropolis. Know the right people and doors open.",
			"If you need a contact or a hush-hush job handled, I can broker the arrangement—provided you can pay."
		]
	},
    {
        'npc_id': 'rhyla',
        'dialog_id': 'rhyla_intro',
        'dialog': [
            "You feel it, don't you? The desert humming beneath your feet.",
            "Zaruun cracked something open. Now the Dune Choir stirs.",
            "If we don't silence them, the whole region will collapse into song and sand."
        ]
    },
    {
        'npc_id': 'choir_echo',
        'dialog_id': 'choir_echo_intro',
        'dialog': [
            "We are the Choir. We are the memory of sand.",
            "You walk on our bodies. You breathe our dust.",
            "You cannot silence what was here before you."
        ]
    },
    {
        'npc_id': 'archive_voice',
        'dialog_id': 'archive_voice_intro',
        'dialog': [
            "The Archive remembers every collapse.",
            "Zaruun was only the first crack. You are the second.",
            "The Glass Maw waits below."
        ]
    },
    {
        'npc_id': 'rhyla',
        'dialog_id': 'rhyla_closing',
        'dialog': [
            "It's done. The Choir falls quiet again.",
            "For now, the desert holds. But it never forgets.",
            "Travel well, wanderer. The sands will remember your steps."
        ]
    }

]

# --- Type E: Dune Cipher Stone ---
NPC_DIALOG += [


    {
        'npc_id': 'kadeem',
        'dialog_id': 'kadeem_cipher_tip',
        'dialog': [
            "A caravan crew dragged this in a few days back. Cracked stone, still warm, humming faintly.",
            "Buyers kept dropping it. Said it made their teeth ache.",
            "They reburied it far southwest — said the whole site looked sealed. Like a vault."
        ]
    },
    {
        'npc_id': 'rhyla',
        'dialog_id': 'rhyla_cipher_context',
        'dialog': [
            "A Cipher Vault. The old Choir used them to lock away resonant knowledge.",
            "The stone inside is not a weapon. It's a record — encoded in frequency, not language.",
            "The vault will be guarded. Speak to the Choir Echo you find there. It will not let you pass quietly."
        ]
    },
    {
        'npc_id': 'choir_echo',
        'dialog_id': 'choir_echo_vault_guardian',
        'dialog': [
            "You reach for what is not yours.",
            "The Cipher was sealed so the wrong hands would never hold it.",
            "You are the wrong hands."
        ]
    },
    {
        'npc_id': 'rhyla',
        'dialog_id': 'rhyla_cipher_received',
        'dialog': [
            "You brought it back whole. I didn't expect that.",
            "The resonance in this stone — it's older than the Choir. Older than any of these cities.",
            "Hold on to it. Someone, somewhere, will know what to do with it."
        ]
    },

]

# --- Type F: Seth's Salvage Manifest ---
NPC_DIALOG += [


    {
        'npc_id': 'kadeem',
        'dialog_id': 'kadeem_seth_tip',
        'dialog': [
            "Seth's been through here. Left in a hurry — said something came off one of his drops wrong.",
            "He usually moves salvage through Mara. Whatever it was, it rattled him.",
            "She might know where he went."
        ]
    },
    {
        'npc_id': 'mara',
        'dialog_id': 'mara_seth_info',
        'dialog': [
            "Seth? Yeah. Dropped off a crate, wouldn't say from where.",
            "The manifest was still in it. Itemized list — mostly junk, but one entry was circled and crossed out.",
            "He took it with him. But he left the crate. It's still in my back room."
        ]
    },
    {
        'npc_id': 'mara',
        'dialog_id': 'mara_seth_manifest_delivered',
        'dialog': [
            "The manifest. So he left it after all.",
            "Circled entry reads: 'recovered — Desert Metropolis vault. Rerouted. Do not log.' ",
            "That's Seth's handwriting. Whatever he pulled out of that vault, it wasn't for a client.",
            "Keep it. Might matter to someone later."
        ]
    },

]

# --- Base city standing tasks ---
TASKS = [
	{
		'task_id': 'desert_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'kadeem',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'kadeem',
					'standing_text': [
						"Care to browse?"
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'mara',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mara',
					'standing_text': [
						"Looking for something particular, or just lost in the heat?"
					]
				}
			}
		],
		'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_regional_complete_gate'
                }
            }
		]
	},
    {
        'task_id': 'desert_large_city_regional_complete_gate',
        'type': 'complete_regional_quests',
        'task_acquire_events': [],
        'task_complete_events': [
            # Type D — not gated by anything, player must find the cipher stone and deliver it. standing task
            { 'event_type': 'award_task', 'params': { 'task_id': 'desert_large_city_type_d_deliver_cipher_stone' } },
            # Type C — standing task
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_type_c_find_elyra'
                }
            },
            # Type E — no gate condition, artifact waits in inventory
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_type_e_investigate_resonance'
                }
            },
            # Type F — no extra gate, Seth is active from Ch.1
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_type_f_find_seth_trail'
                }
            }
        ]
    },

]

# =========================================================
# TYPE E — Dune Cipher Stone
# Artifact ID: desert_large_city_e_dune_cipher_stone
# Gates: desert_large_city Type D (Slot 2)
# Awarded by: desert_large_city_regional_complete_gate
# =========================================================
TASKS += [
    {
        'task_id': 'desert_large_city_type_e_investigate_resonance',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'kadeem',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'kadeem',
                    'standing_text': [
                        "Something came in from the deep desert.",
                        "Buyers won't touch it. Figured you might want a look."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'kadeem',
                    'dialog_id': 'kadeem_cipher_tip'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_type_e_consult_rhyla'
                }
            }
        ]
    },

    {
        'task_id': 'desert_large_city_type_e_consult_rhyla',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rhyla',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'rhyla',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rhyla',
                    'standing_text': [
                        "A Cipher Vault. I haven't heard that name in years.",
                        "Tell me what Kadeem described."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rhyla',
                    'dialog_id': 'rhyla_cipher_context'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_type_e_confront_choir_echo'
                }
            }
        ]
    },

    {
        'task_id': 'desert_large_city_type_e_confront_choir_echo',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'choir_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'choir_echo',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'choir_echo',
                    'standing_text': [
                        "This place is sealed.",
                        "Leave."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'choir_echo',
                    'dialog_id': 'choir_echo_vault_guardian'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_type_e_defeat_choir_echo'
                }
            }
        ]
    },

    {
        'task_id': 'desert_large_city_type_e_defeat_choir_echo',
        'type': 'defeat',
        'to_type': 'npc',
        'to_id': 'choir_echo',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'desert_large_city_e_dune_cipher_stone'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_type_e_return_to_rhyla'
                }
            }
        ]
    },

    {
        'task_id': 'desert_large_city_type_e_return_to_rhyla',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rhyla',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rhyla',
                    'standing_text': [
                        "You made it back.",
                        "And you're still holding it. Good."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rhyla',
                    'dialog_id': 'rhyla_cipher_received'
                }
            }
        ]
    },

]

# =========================================================
# TYPE F — Seth's Salvage Manifest
# Faction Item ID: desert_large_city_f_salvage_manifest
# Recurring NPC: seth (Ch.1–Ch.13)
# Gates: grassland_mid_city (Highsteeple Crossing, Ch.3) Type D (Slot 2)
# Awarded by: desert_large_city_regional_complete_gate
# =========================================================

TASKS += [
    {
        'task_id': 'desert_large_city_type_f_find_seth_trail',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'kadeem',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'kadeem',
                    'standing_text': [
                        "Seth blew through here and left in a hurry.",
                        "Left something with Mara. Ask her about it."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'kadeem',
                    'dialog_id': 'kadeem_seth_tip'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_type_f_speak_to_mara'
                }
            }
        ]
    },

    {
        'task_id': 'desert_large_city_type_f_speak_to_mara',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'mara',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'mara',
                    'standing_text': [
                        "Seth? Yes, he was here.",
                        "Left something in my back room. Not sure what to make of it."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'mara',
                    'dialog_id': 'mara_seth_info'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_type_f_retrieve_manifest'
                }
            }
        ]
    },

    {
        'task_id': 'desert_large_city_type_f_retrieve_manifest',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'mara',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'mara',
                    'standing_text': [
                        "The crate is in the back. The manifest is still inside.",
                        "Take it — I want no part of whatever Seth was moving."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'mara',
                    'dialog_id': 'mara_seth_manifest_delivered'
                }
            },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'desert_large_city_f_salvage_manifest'
                }
            }
        ]
    },

]

# ── Type D ── Dune Resonance Blade (mythic weapon) ───────────────────────────
# Gate: player holds dune_cipher_stone from the Type E chain.
# Deliver to Diego → Rhyla reads the cipher → defeat Archive Voice → mythic weapon.
# No new NPCs — uses kadeem, rhyla, archive_voice, and diego (Ch.1 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'rhyla',
		'dialog_id': 'rhyla_d_cipher_read',
		'dialog': [
			"This stone doesn't just record sound — it holds a resonance blueprint.",
			"The dunes have been singing a weapon into existence for centuries.",
			"The Archive Voice below the market carries the final frequency.",
			"Bring it out of silence and the blade will answer."
		]
	},

	{
		'npc_id': 'archive_voice',
		'dialog_id': 'archive_voice_d_awakens',
		'dialog': [
			"The cipher reaches me.",
			"You want the frequency made steel.",
			"Silence me first — then the resonance is yours."
		]
	},

]

TASKS += [

	# D-0 — Deliver dune_cipher_stone to Diego (standalone deliver; unlocks D chain)
	{
		'task_id': 'desert_large_city_type_d_deliver_cipher_stone',
		'type': 'deliver',
		'item_id': 'dune_cipher_stone',
		'to_type': 'npc',
		'to_id': 'diego',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"That stone hums at a frequency I've only heard in legends.",
						"Let me see it — if it's what I think it is, this changes everything."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'diego',
					'dialog_id': 'diego_intro'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_large_city_type_d_consult_rhyla'
				}
			},
		]
	},

	# D-1 — Consult Rhyla for the resonance reading
	{
		'task_id': 'desert_large_city_type_d_consult_rhyla',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rhyla',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rhyla',
					'standing_text': [
						"Diego sent you with the cipher stone.",
						"I can hear what it wants to become.",
						"Come close — the dunes are already answering."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rhyla',
					'dialog_id': 'rhyla_d_cipher_read'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_large_city_type_d_meet_archive_voice'
				}
			},
		]
	},

	# D-2 — Meet the Archive Voice (boss intro)
	{
		'task_id': 'desert_large_city_type_d_meet_archive_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'archive_voice',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'archive_voice',
					'standing_text': [
						"The frequency stirs in the deep archive.",
						"Something ancient recognizes the cipher stone.",
						"Approach — it will not wait."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'archive_voice',
					'dialog_id': 'archive_voice_d_awakens'
				}
			},
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'archive_voice_1',
					'combat_type': 'boss_encounter'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_large_city_type_d_defeat_archive_voice'
				}
			},
		]
	},

	# D-3 — Defeat the Archive Voice; award mythic weapon
	{
		'task_id': 'desert_large_city_type_d_defeat_archive_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'archive_voice_1',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_desert_large_dune_resonance_blade'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rhyla',
					'standing_text': [
						"The resonance blade is yours now.",
						"The dunes finally went quiet.",
						"I don't think they'll sing again for a long time."
					]
				}
			},
		]
	},

]


# =========================================================
# TYPE C — Elyra Dawnseer (extended character, slot 2)
# Gated by is_chapter_gte: 8
# Awarded by: desert_large_city_regional_complete_gate (conditional)
# =========================================================
NPC_DIALOG += [

    # ── Type C dialogs — Elyra Dawnseer ────────────────────────────
    {
        'npc_id': 'kadeem',
        'dialog_id': 'kadeem_c_elyra_rumour',
        'dialog': [
            "There's a woman who passes through the Spire every few weeks.",
            "Doesn't buy. Doesn't sell.",
            "She just watches — like she already knows how every deal in this market ends.",
            "Mara knows her name. She knows everyone's name."
        ]
    },
    {
        'npc_id': 'mara',
        'dialog_id': 'mara_c_elyra_vouch',
        'dialog': [
            "Elyra Dawnseer.",
            "She's been circling the Spire for weeks.",
            "The visions she describes — they're not prophecy. They're pattern recognition pushed past the edge of language.",
            "She watches your party because she's already seen what happens if you fail.",
            "Tell her Mara said the cards are in your favour.",
            "That's the only phrase that opens her door."
        ]
    },
    {
        'npc_id': 'elyra_dawnseer',
        'dialog_id': 'elyra_c_first_meet',
        'dialog': [
            "Mara's phrase.",
            "I've been waiting to hear it from someone who means it.",
            "The Glamour and the Scalpel — you've felt both by now.",
            "The city shows you what it wants you to see.",
            "I see what it hides.",
            "You need that. And I need somewhere to stand when the next vision breaks."
        ]
    },
    {
        'npc_id': 'elyra_dawnseer',
        'dialog_id': 'elyra_c_joins',
        'dialog': [
            "Every future I've seen with you in it is uncertain.",
            "That's the first honest thing I've encountered in years.",
            "I'll come."
        ]
    },

]

TASKS += [
    {
        'task_id': 'desert_large_city_type_c_find_elyra',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'kadeem',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'kadeem',
                    'standing_text': [
                        "Strange woman's been watching the market again.",
                        "Mara knows her. She knows everyone."
                    ]
                }
            },
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'kadeem',
                    'dialog_id': 'kadeem_c_elyra_rumour'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_type_c_consult_mara'
                }
            },
        ]
    },
    {
        'task_id': 'desert_large_city_type_c_consult_mara',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'mara',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'mara',
                    'standing_text': [
                        "Kadeem sent you about the woman in the Spire.",
                        "I know exactly who you mean."
                    ]
                }
            },
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'mara',
                    'dialog_id': 'mara_c_elyra_vouch'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_large_city_type_c_earn_elyra'
                }
            },
        ]
    },
    {
        'task_id': 'desert_large_city_type_c_earn_elyra',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'elyra_dawnseer',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'elyra_dawnseer',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'elyra_dawnseer',
                    'standing_text': [
                        "The Spire changes what people see.",
                        "Come when you're ready to hear what it hides."
                    ]
                }
            },
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'elyra_dawnseer',
                    'dialog_id': 'elyra_c_first_meet'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'elyra_dawnseer',
                    'dialog_id': 'elyra_c_joins'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': { 'npc_id': 'elyra_dawnseer' }
            },
            {
                'event_type': 'character_join',
                'params': { 'character_id': 'elyra_dawnseer' }
            },
        ]
    },

]

# ── Type E ── Dune Cipher Stone → gates Desert Large Type D ───────────────────
# Rhyla the Echo-Binder holds a stone carved with resonance patterns she
# recovered from the Dune Choir's dispersal site. No new NPCs. No dungeon.

NPC_DIALOG += [

	{
		'npc_id': 'rhyla',
		'dialog_id': 'rhyla_e_cipher_stone',
		'dialog': [
			"After the Choir fell silent, I swept the dispersal site.",
			"The sand had pressed this into the surface — a stone carved with resonance patterns.",
			"It stores the frequency of the Choir's final note.",
			"I don't know what it unlocks. But it hums when held near old desert architecture.",
			"Take it. Something out there will know what to do with it."
		]
	},

]

TASKS += [

	# E-1 — Meet Rhyla to receive the Dune Cipher Stone
	{
		'task_id': 'desert_large_city_type_e_meet_rhyla',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rhyla',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rhyla', 'standing_text': [
				"The dispersal site left something behind.",
				"A carved stone that hums with old resonance.",
				"Come find me when you're ready for it."
			]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rhyla', 'dialog_id': 'rhyla_e_cipher_stone' }},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'desert_large_city_e_dune_cipher_stone' }},
		]
	},

]


PRIMARY_STORY_SETTINGS = {
	'story_id': 'desert_large_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}