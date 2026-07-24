ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'archivist_fernhollow',
		'name': 'Fernhollow',
		'description': (
			'A gentle historian who records the forest\'s shifting lore.'
			' Fernhollow speaks to trees as though they are old friends.'
			' Their parchment always smells faintly of pine resin and rain.'
		)
	},
	{
		'npc_id': 'scout_lyss',
		'name': 'Lyss the Quiet Step',
		'description': (
			'A vigilant scout who hears disturbances long before they occur.'
			' Lyss meditates daily to attune her senses to the forest\'s whispers.'
			' She rarely raises her voice, yet commands instant attention.'
		)
	},
    {
        'npc_id': 'whisper_moth_selen',
        'name': 'Whisper‑Moth Selen',
        'description': (
            'A soft‑spoken wanderer who follows drifting moth‑spirits that carry the forest\'s memories.'
        )
    },
    {
        'npc_id': 'moth_echo',
        'name': 'Moth Echo',
        'description': (
            'A faint, fluttering apparition formed from forgotten stories and pale wing‑light.'
        )
    },
    {
        'npc_id': 'burrow_whisper',
        'name': 'Burrow Whisper',
        'description': (
            'A murmuring presence deep within the Echofern Burrows, shaped from lost recollections.'
        )
    }
]


NPC_DIALOG = [

    # --- Base city standing dialog ---

    {
        'npc_id': 'archivist_fernhollow',
        'dialog_id': 'fernhollow_intro',
        'dialog': [
            "The forest forgets too much.",
            "Memories slip away like dew at dawn.",
            "Something steals our stories — gently, but relentlessly."
        ]
    },
    {
        'npc_id': 'scout_lyss',
        'dialog_id': 'lyss_intro',
        'dialog': [
            "The quiet is wrong.",
            "Even the wind hesitates to speak.",
            "Whatever silences the forest moves softly."
        ]
    },
    {
        'npc_id': 'whisper_moth_selen',
        'dialog_id': 'selen_intro',
        'dialog': [
            "The moths carry what the forest forgets.",
            "They drift toward a place where memories fade.",
            "Follow them, and you'll find the thief of whispers."
        ]
    },
    {
        'npc_id': 'moth_echo',
        'dialog_id': 'moth_echo_intro',
        'dialog': [
            "We flutter with forgotten tales.",
            "The Silent Canopy drinks our voices.",
            "It waits deeper below."
        ]
    },
    {
        'npc_id': 'burrow_whisper',
        'dialog_id': 'burrow_whisper_intro',
        'dialog': [
            "The Burrows tremble with stolen memories.",
            "The Canopy grows stronger with each silence.",
            "Only its heart remains to be severed."
        ]
    },
    {
        'npc_id': 'archivist_fernhollow',
        'dialog_id': 'fernhollow_closing',
        'dialog': [
            "The forest breathes again.",
            "Its stories return like rain to thirsty soil.",
            "You've restored what was nearly lost."
        ]
    }

]

NPC_DIALOG += [

    # --- Type E: Thornshade Root Graft ---

    {
        'npc_id': 'archivist_fernhollow',
        'dialog_id': 'fernhollow_root_graft_discovery',
        'dialog': [
            "I've been cross-referencing old growth records and I found something unusual.",
            "There's an entry describing a graft — a living cutting taken from the oldest thorn-tree in the hamlet.",
            "The records say it was sealed in the Echofern Burrows for preservation.",
            "It was never retrieved. The tree it came from has been gone for two generations."
        ]
    },
    {
        'npc_id': 'scout_lyss',
        'dialog_id': 'lyss_root_graft_context',
        'dialog': [
            "I've passed that section of the burrows. There's a sealed alcove — roots around the entrance, old growth.",
            "The Burrow Whisper guards that stretch of tunnel more fiercely than any other.",
            "It's not protecting the space. It's protecting something inside it."
        ]
    },
    {
        'npc_id': 'burrow_whisper',
        'dialog_id': 'burrow_whisper_graft_guardian',
        'dialog': [
            "The Graft sleeps here.",
            "The forest asked us to keep it.",
            "You are not the forest."
        ]
    },
    {
        'npc_id': 'archivist_fernhollow',
        'dialog_id': 'fernhollow_root_graft_received',
        'dialog': [
            "Still alive. After all this time, it's still alive.",
            "This cutting carries the memory of a tree that no longer exists.",
            "I can't explain why, but I believe it belongs somewhere far from here.",
            "The records say the original tree had roots that reached another region entirely.",
            "Carry it. When the time comes, you'll know where to plant it."
        ]
    },

]

NPC_DIALOG += [

    # --- Type C: Talia Softheart ---

    {
        'npc_id': 'talia_softheart',
        'dialog_id': 'talia_type_c_intro',
        'dialog': [
            "You look like you've been carrying a lot.",
            "I don't mean your pack.",
            "I've been tending to the hamlet's wounded for three months — there are more than there should be.",
            "The forest's distress is reaching people. I could use someone to help me reach back."
        ]
    },
    {
        'npc_id': 'talia_softheart',
        'dialog_id': 'talia_type_c_lyss_check',
        'dialog': [
            "Lyss told you about me? That's — actually that means a lot.",
            "She doesn't say kind things about people unless she means them.",
            "I've been hoping for someone to travel with who actually listens."
        ]
    },
    {
        'npc_id': 'talia_softheart',
        'dialog_id': 'talia_type_c_join',
        'dialog': [
            "I'll come with you.",
            "I can't heal the forest from here — I need to go where the wounds are.",
            "Just... tell me when people are hurting. I'm not always good at waiting to be asked."
        ]
    },

]


TASKS = [
	{
		'task_id': 'forest_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'archivist_fernhollow',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'archivist_fernhollow',
					'standing_text': [
						"Come read the old leaves with me; they hum of distant summers."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'scout_lyss',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scout_lyss',
					'standing_text': [
						"Quiet roads are a blessing—if you've tales, I'll listen between steps."
					]
				}
			}
		],
		'task_complete_events': [
            # Type E — no gate condition, artifact waits in inventory
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_type_e_investigate_graft'
                }
            },
            # Type C — gated by chapter 16 being reached
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_type_c_find_talia'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_type_d_deliver_memory_spore'
                }
            }
		]
	},

]

TASKS += [

    # =========================================================
    # TYPE E — Thornshade Root Graft
    # Artifact ID: forest_small_city_e_thornshade_root_graft
    # Gates: forest_mid_city (Boiling Bubble, Ch.2) Type D (Slot 3) — retroactive
    # Awarded by: forest_small_city_initialize
    # =========================================================

    {
        'task_id': 'forest_small_city_type_e_investigate_graft',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'archivist_fernhollow',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'archivist_fernhollow',
                    'standing_text': [
                        "I found something in the old growth records that doesn't add up.",
                        "A preservation entry for a graft that was never retrieved."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'archivist_fernhollow',
                    'dialog_id': 'fernhollow_root_graft_discovery'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_type_e_consult_lyss'
                }
            }
        ]
    },

    {
        'task_id': 'forest_small_city_type_e_consult_lyss',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'scout_lyss',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'scout_lyss',
                    'standing_text': [
                        "I know the alcove Fernhollow means.",
                        "The Burrow Whisper circles it more than anywhere else in the tunnels."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'scout_lyss',
                    'dialog_id': 'lyss_root_graft_context'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_type_e_confront_burrow_whisper'
                }
            }
        ]
    },

    {
        'task_id': 'forest_small_city_type_e_confront_burrow_whisper',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'burrow_whisper',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'burrow_whisper',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'burrow_whisper',
                    'standing_text': [
                        "The Graft sleeps here.",
                        "It is not yours to take."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'burrow_whisper',
                    'dialog_id': 'burrow_whisper_graft_guardian'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_type_e_defeat_burrow_whisper'
                }
            }
        ]
    },

    {
        'task_id': 'forest_small_city_type_e_defeat_burrow_whisper',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'burrow_whisper',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'burrow_whisper_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'forest_small_city_e_thornshade_root_graft'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_type_e_return_to_fernhollow'
                }
            }
        ]
    },

    {
        'task_id': 'forest_small_city_type_e_return_to_fernhollow',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'archivist_fernhollow',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'archivist_fernhollow',
                    'standing_text': [
                        "You retrieved it. And it's still alive.",
                        "Come — I need to see it."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'archivist_fernhollow',
                    'dialog_id': 'fernhollow_root_graft_received'
                }
            }
        ]
    },

]

TASKS += [

    # =========================================================
    # TYPE C — Talia Softheart
    # Extended Character: talia_softheart
    # Final event: character_join
    # Awarded by: forest_small_city_initialize (is_chapter_gte 16)
    # =========================================================

    {
        'task_id': 'forest_small_city_type_c_find_talia',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'talia_softheart',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'talia_softheart',
                    'location': 'region_city_other3'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'talia_softheart',
                    'standing_text': [
                        "The hamlet's wounded keep coming.",
                        "The forest's distress reaches people in ways I'm only starting to understand."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'talia_softheart',
                    'dialog_id': 'talia_type_c_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_type_c_consult_lyss'
                }
            }
        ]
    },

    {
        'task_id': 'forest_small_city_type_c_consult_lyss',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'scout_lyss',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'scout_lyss',
                    'standing_text': [
                        "Talia asked me about you.",
                        "I told her what I know. She's worth your time."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'talia_softheart',
                    'dialog_id': 'talia_type_c_lyss_check'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_small_city_type_c_earn_talia'
                }
            }
        ]
    },

    {
        'task_id': 'forest_small_city_type_c_earn_talia',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'talia_softheart',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'talia_softheart',
                    'standing_text': [
                        "I've made my decision.",
                        "The forest needs more than this hamlet can give right now."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'talia_softheart',
                    'dialog_id': 'talia_type_c_join'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': { 'npc_id': 'talia_softheart' }
            },
            {
                'event_type': 'character_join',
                'params': { 'character_id': 'talia_softheart' }
            },
        ]
    },

]

NPC_DIALOG += [

	{
		'npc_id': 'whisper_moth_selen',
		'dialog_id': 'selen_d_spore_read',
		'dialog': [
			"This spore carries the Boiling Bubble's oldest memory-network.",
			"The mycelia encoded every story the forest wanted preserved.",
			"The Burrow Whisper feeds on exactly this kind of stored memory.",
			"It has been draining Thornshade's recollections through the root network for years.",
			"Present the spore at the Burrow entrance — the Whisper will surface for it.",
			"Silence it and the memory-metal it guards crystallizes.",
			"Diego can forge memory-crystal into a blade that never forgets a path it has walked."
		]
	},

	{
		'npc_id': 'burrow_whisper',
		'dialog_id': 'burrow_whisper_d_awakens',
		'dialog': [
			"The mycelia spore reaches the Burrows.",
			"You carry the network's oldest memory into my domain.",
			"I have been hungry for this frequency for a very long time.",
			"You will not leave with it."
		]
	},

]

TASKS += [

	# D-0 — Deliver mycelia_memory_spore to Diego (standalone deliver; unlocks D chain)
	{
		'task_id': 'forest_small_city_type_d_deliver_memory_spore',
		'type': 'deliver',
		'item_id': 'mycelia_memory_spore',
		'to_type': 'npc',
		'to_id': 'diego',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"That spore — the memory-network residue is still active inside it.",
						"Something in Thornshade Hamlet resonates with it.",
						"Find Selen. She follows moth-spirits that carry forest memories.",
						"She'll know where this frequency leads."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_d_consult_selen'
				}
			},
		]
	},

	# D-1 — Consult Selen for the spore reading
	{
		'task_id': 'forest_small_city_type_d_consult_selen',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'whisper_moth_selen',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'whisper_moth_selen',
					'standing_text': [
						"The moth-spirits clustered around you the moment you entered the hamlet.",
						"That spore you carry — it speaks to every memory the forest has ever lost.",
						"Come quickly. The Burrow already stirs."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'whisper_moth_selen',
					'dialog_id': 'selen_d_spore_read'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_d_meet_burrow_whisper'
				}
			},
		]
	},

	# D-2 — Meet the Burrow Whisper (boss intro)
	{
		'task_id': 'forest_small_city_type_d_meet_burrow_whisper',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'burrow_whisper',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'burrow_whisper',
					'standing_text': [
						"A low resonance bleeds from the Echofern Burrow entrance.",
						"Fernhollow says the archive parchments have gone blank since dawn.",
						"Lyss says the forest has gone completely silent.",
						"The spore has drawn the Whisper forward."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'burrow_whisper',
					'dialog_id': 'burrow_whisper_d_awakens'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_d_defeat_burrow_whisper'
				}
			},
		]
	},

	# D-3 — Defeat the Burrow Whisper; Diego forges the mythic weapon
	{
		'task_id': 'forest_small_city_type_d_defeat_burrow_whisper',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'burrow_whisper_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'burrow_whisper_1',
					'combat_type': 'boss_battle'
				}
			}
        ],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_forest_small_echofern_blade'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"Memory-crystal — it forges like hardened thought.",
						"I've worked it into the blade.",
						"It remembers every path it has ever walked.",
						"You'll never lose your way carrying this."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'whisper_moth_selen',
					'standing_text': [
						"The moth-spirits are calm again.",
						"Every memory the Whisper drained has returned to the root network.",
						"Fernhollow says the archive parchments filled back in on their own."
					]
				}
			},
		]
	},

]
# ── Type E ── Thornshade Root Graft → gates Forest Mid Type D (Boiling Bubble) ─
# Whisper-Moth Selen recovered a root graft from the Echofern Burrows — a
# cutting from the oldest thornshade tree preserved in the moth-memory network.
# No new NPCs. No dungeon.

NPC_DIALOG += [

	{
		'npc_id': 'whisper_moth_selen',
		'dialog_id': 'selen_e_root_graft',
		'dialog': [
			"The moths led me to this after the Burrows cleared.",
			"A root graft — thornshade, very old.",
			"(turning it in her hands)",
			"The memory in it is from before Thornshade Hamlet existed.",
			"It's looking for Boiling Bubble. The mycelium there will recognise it.",
			"Fernhollow says it's not a relic — it's a message that hasn't been delivered yet.",
			"Carry it gently."
		]
	},
	{
		'npc_id': 'archivist_fernhollow',
		'dialog_id': 'fernhollow_e_graft_context',
		'dialog': [
			"The graft is alive.",
			"Root grafts don't preserve — they transmit.",
			"This one has been trying to reach the forest at Boiling Bubble for longer than I can date.",
			"The moths held it in memory because nothing else could.",
			"Now it has a carrier. That's you."
		]
	},

]

TASKS += [

	# E-1 — Consult Fernhollow about the graft
	{
		'task_id': 'forest_small_city_type_e_consult_fernhollow',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'archivist_fernhollow',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'archivist_fernhollow', 'standing_text': [
				"Selen found something in the Burrows after the clearing.",
				"A root graft. Living. Old.",
				"Come — I'll tell you what it means."
			]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'archivist_fernhollow', 'dialog_id': 'fernhollow_e_graft_context' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'forest_small_city_type_e_collect_graft' }},
		]
	},

	# E-2 — Collect from Selen
	{
		'task_id': 'forest_small_city_type_e_collect_graft',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'whisper_moth_selen',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'whisper_moth_selen', 'standing_text': [
				"The moths are restless with it.",
				"They've held this memory long enough.",
				"Take it before it starts to bloom."
			]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'whisper_moth_selen', 'dialog_id': 'selen_e_root_graft' }},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'forest_small_city_e_thornshade_root_graft' }},
		]
	},

]


PRIMARY_STORY_SETTINGS = {
    'story_id': 'forest_small_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}