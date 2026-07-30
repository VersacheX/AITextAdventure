ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'sparkwire_Jexa',
		'name': 'Jexa Sparkwire',
		'description': (
			'A scavenger‑engineer who grafts glowing circuitry into salvaged tech.'
			'  Jexa treats every broken device like a wounded animal needing care.'
			'  Her workshop hums with neon pulses that mirror her restless energy.'
		)
	},
	{
		'npc_id': 'morrowdeal_krayt',
		'name': 'Krayt Morrowdeal',
		'description': (
			'A desert‑hardened trader who deals exclusively in contraband and curios.'
			'  Krayt\'s voice is gravelly from years of dust storms and whispered negotiations.'
			'  He claims the Bazaar chooses its merchants, not the other way around.'
		)
	},
    {
        'npc_id': 'scrap_seer_venn',
        'name': 'Scrap‑Seer Venn',
        'description': (
            'A desert hermit who claims to "hear" the emotions of broken machines. '
            'Venn wanders scrap fields collecting stories from discarded tech.'
        )
    },
    {
        'npc_id': 'hollow_echo',
        'name': 'Hollow Echo',
        'description': (
            'A glitching apparition formed from corrupted scrap‑data. '
            'Its voice stutters like a damaged audio log.'
        )
    },
    {
        'npc_id': 'signal_wraith',
        'name': 'Signal Wraith',
        'description': (
            'A shimmering figure made of distorted radio waves and static. '
            'It flickers between frequencies as it speaks.'
        )
    },
    {
        'npc_id': 'signal_wraith_2',
        'name': 'Signal Wraith',
        'description': (
            'A shimmering figure made of distorted radio waves and static. '
            'It flickers between frequencies as it speaks.'
        )
    }
]


NPC_DIALOG = [

    # --- Base city standing dialog ---

    {
        'npc_id': 'sparkwire_Jexa',
        'dialog_id': 'Jexa_intro',
        'dialog': [
            "Something's wrong with the tech around here.",
            "Devices are waking up on their own — humming, twitching, overheating.",
            "Feels like a sick machine crying for help."
        ]
    },
    {
        'npc_id': 'morrowdeal_krayt',
        'dialog_id': 'krayt_intro',
        'dialog': [
            "A relic passed through the Bazaar last week.",
            "Looked harmless. Felt cursed.",
            "Now the whole district buzzes like a dying generator."
        ]
    },
    {
        'npc_id': 'scrap_seer_venn',
        'dialog_id': 'venn_intro',
        'dialog': [
            "You hear the static too. Good.",
            "The broken ones scream of a Heart beating too fast.",
            "Follow the noise. It will find you."
        ]
    },
    {
        'npc_id': 'hollow_echo',
        'dialog_id': 'hollow_echo_intro',
        'dialog': [
            "The Hollows remember every discarded thing.",
            "The Heart feeds on what you throw away.",
            "It grows stronger with every spark."
        ]
    },
    {
        'npc_id': 'signal_wraith',
        'dialog_id': 'signal_wraith_intro',
        'dialog': [
            "Your signal is clean. Rare.",
            "The Heart wants to rewrite you.",
            "Run, or burn bright."
        ]
    },
    {
        'npc_id': 'sparkwire_Jexa',
        'dialog_id': 'Jexa_closing',
        'dialog': [
            "You did it. The Heart's gone quiet.",
            "Circuits are stable again — for now.",
            "If anything starts humming at night, bring it straight to me."
        ]
    }

]

NPC_DIALOG += [

    # --- Type E: Eroded Ledger Plate ---

    {
        'npc_id': 'morrowdeal_krayt',
        'dialog_id': 'krayt_ledger_discovery',
        'dialog': [
            "There's a plate in my inventory I can't move.",
            "Every buyer who handles it puts it back down without a word.",
            "Feels like it's waiting for someone specific. Old desert script etched into both sides."
        ]
    },
    {
        'npc_id': 'scrap_seer_venn',
        'dialog_id': 'venn_ledger_context',
        'dialog': [
            "I know that plate. Found it in the deep scrap field three seasons ago.",
            "It's not a ledger of commerce. It's a ledger of routes — underground paths, sealed since the last big quake.",
            "The Signal Wraith guards it. It's been using the plate's signal as an anchor."
        ]
    },
    {
        'npc_id': 'signal_wraith',
        'dialog_id': 'signal_wraith_ledger_guardian',
        'dialog': [
            "The Plate is my anchor.",
            "Without it I scatter across the frequencies.",
            "You would take the only thing keeping me coherent."
        ]
    },
    {
        'npc_id': 'morrowdeal_krayt',
        'dialog_id': 'krayt_ledger_received',
        'dialog': [
            "Ha. It actually came back to you.",
            "The routes on that plate — half of them lead out of this region entirely.",
            "Whatever it was cataloguing, it wasn't just local trade.",
            "Keep it. Might open doors elsewhere."
        ]
    },

]

NPC_DIALOG += [

    # --- Type F: Contraband Registry ---

    {
        'npc_id': 'morrowdeal_krayt',
        'dialog_id': 'krayt_tess_tip',
        'dialog': [
            "Tess came through the Bazaar two days ago.",
            "Dropped off a crate, asked no questions, left too fast.",
            "She's fun right up until she's not. Jexa might know where she went."
        ]
    },
    {
        'npc_id': 'sparkwire_Jexa',
        'dialog_id': 'Jexa_tess_location',
        'dialog': [
            "Tess? Yeah, she stopped by the workshop.",
            "Said she needed something traced — signal from a buried cache out in the open desert.",
            "I gave her a frequency marker. She's probably still out there."
        ]
    },
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_radpost_intro',
        'dialog': [
            "Oh good, someone who doesn't look like they work for a government.",
            "I've been pulling records out of a buried cache for three weeks.",
            "Someone logged every black market drop in this region going back fifteen years.",
            "Names, dates, locations. I don't know who made this — but it's very, very useful."
        ]
    },
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_radpost_registry_handoff',
        'dialog': [
            "I'm keeping the originals. Obviously.",
            "But you can have a copy. The Bleakwatch entries are the interesting ones.",
            "Someone's been running drops through that outpost for years.",
            "If you ever end up there — and you will — this'll tell you exactly who to ask about."
        ]
    },

]

# --- Character dialogs: Type E ---
NPC_DIALOG += [

    # Type E – Investigate Ledger
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_small_e_investigate_ledger',
        'dialog': [
            "A plate every buyer refuses to keep. That's not bad merchandise — that's a warning."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_small_e_investigate_ledger',
        'dialog': [
            "Old desert script on both sides and no one will hold it. It's waiting for a specific frequency."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_desert_small_e_investigate_ledger',
        'dialog': [
            "I already want to know what it's cataloguing."
        ]
    },

    # Type E – Consult Venn
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_small_e_consult_venn',
        'dialog': [
            "A ledger of sealed underground routes, not commerce. That changes the value completely."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_small_e_consult_venn',
        'dialog': [
            "The Signal Wraith has been using it as an anchor. Of course it has."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_desert_small_e_consult_venn',
        'dialog': [
            "Then we take the anchor away from it."
        ]
    },

    # Type E – Confront Signal Wraith
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_desert_small_e_confront_signal_wraith',
        'dialog': [
            "It's treating the plate like the only thing keeping it coherent."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_desert_small_e_confront_signal_wraith',
        'dialog': [
            "Without the plate it scatters across the frequencies. That's either tragic or extremely useful."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_desert_small_e_confront_signal_wraith',
        'dialog': [
            "It's not guarding a ledger. It's guarding the last shape it can still hold."
        ]
    },

    # Type E – Defeat Signal Wraith
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_desert_small_e_defeat_signal_wraith',
        'dialog': [
            "It's done. Take the plate."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_small_e_defeat_signal_wraith',
        'dialog': [
            "Routes that lead out of the region entirely. This wasn't local bookkeeping."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_small_e_defeat_signal_wraith',
        'dialog': [
            "The signal is quiet. The ledger is free to be read by someone who actually wants the information."
        ]
    },

    # Type E – Return to Krayt
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_desert_small_e_return_to_krayt',
        'dialog': [
            "It came back to us. Funny how that works."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_small_e_return_to_krayt',
        'dialog': [
            "Half these routes leave the region. Whatever it was tracking, it wasn't just trade."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_desert_small_e_return_to_krayt',
        'dialog': [
            "Keep it. Doors open for people who know the old paths."
        ]
    },

]

# --- Character dialogs: Type F ---
NPC_DIALOG += [

    # Type F – Find Tess Trail
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_desert_small_f_find_tess_trail',
        'dialog': [
            "Tess blew through here and left too fast. Classic."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_desert_small_f_find_tess_trail',
        'dialog': [
            "She only moves that quickly when the information is better than the company."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_desert_small_f_find_tess_trail',
        'dialog': [
            "Jexa's the next stop. Tess always needs something traced."
        ]
    },

    # Type F – Ask Jexa
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_small_f_ask_jexa',
        'dialog': [
            "A frequency marker pointed at a buried cache. She's still out there."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_desert_small_f_ask_jexa',
        'dialog': [
            "Tess and a buried cache of black-market records. I already like this errand."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_desert_small_f_ask_jexa',
        'dialog': [
            "Let's go find her before someone else does."
        ]
    },

    # Type F – Find Tess
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_desert_small_f_find_tess',
        'dialog': [
            "Three weeks pulling records out of a buried cache. She's committed, I'll give her that."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_small_f_find_tess',
        'dialog': [
            "Fifteen years of black-market drops. Names, dates, locations. That's not a hobby — that's leverage."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_desert_small_f_find_tess',
        'dialog': [
            "Someone logged every quiet transaction in the region. Tess found the only copy that matters."
        ]
    },

    # Type F – Receive Registry
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_small_f_receive_registry',
        'dialog': [
            "Bleakwatch entries. Of course that's the section that matters."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_desert_small_f_receive_registry',
        'dialog': [
            "She's keeping the originals. Smart. The copy is still dangerous enough."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_desert_small_f_receive_registry',
        'dialog': [
            "If we ever end up in Bleakwatch, we'll know exactly who to ask."
        ]
    },

]

# --- Character dialogs: Type D ---
NPC_DIALOG += [

    # Type D – Deliver Ledger Plate
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_desert_small_d_deliver_ledger_plate',
        'dialog': [
            "Diego again. At least he can hear the frequency on this one."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_small_d_deliver_ledger_plate',
        'dialog': [
            "The plate is still humming. Venn will know what it's trying to say."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_small_d_deliver_ledger_plate',
        'dialog': [
            "Resonance left behind by whatever was recorded. That's never just data."
        ]
    },

    # Type D – Consult Venn
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_small_d_consult_venn',
        'dialog': [
            "Every entry is a frequency signature. The Wraith has been feeding on them since the Radpost was built."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_small_d_consult_venn',
        'dialog': [
            "Draw it out with the plate's own resonance and the static crystallizes. Elegant, in a violent way."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_desert_small_d_consult_venn',
        'dialog': [
            "Then we call it and finish it."
        ]
    },

    # Type D – Meet Signal Wraith (2)
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_desert_small_d_meet_signal_wraith',
        'dialog': [
            "It's been listening to every transaction since the post was built."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_desert_small_d_meet_signal_wraith',
        'dialog': [
            "'I will drown you in static first.' At least it's honest about its methods."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_desert_small_d_meet_signal_wraith',
        'dialog': [
            "It's not defending territory. It's defending the only conversation it still understands."
        ]
    },

    # Type D – Defeat Signal Wraith (2)
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_desert_small_d_defeat_signal_wraith',
        'dialog': [
            "Quiet. Take the crystallized static."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_small_d_defeat_signal_wraith',
        'dialog': [
            "A blade that reads every ward and shield before the swing. That's a dangerous edge."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_small_d_defeat_signal_wraith',
        'dialog': [
            "The machines stopped screaming. The broadcast is finally over."
        ]
    },

]


TASKS = [
	{
		'task_id': 'desert_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'sparkwire_Jexa',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sparkwire_Jexa',
					'standing_text': [
						"I mend what others discard — sit and tell me how it broke."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'morrowdeal_krayt',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'morrowdeal_krayt',
					'standing_text': [
						"The Bazaar has stories for every ear — pull up a crate and share one."
					]
				}
			}
		],
		'task_complete_events': [
            # Type E — no gate condition, artifact waits in inventory
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_type_e_investigate_ledger'
                }
            },
            # Type F — Tess active from Ch.2
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_type_f_find_tess_trail'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_type_d_deliver_ledger_plate'
                }
            }
		]
	},

]
# E
TASKS += [

    # =========================================================
    # TYPE E — Eroded Ledger Plate
    # Artifact ID: desert_small_city_e_eroded_ledger_plate
    # Gates: desert_small_city Type D (Slot 2) — same city
    # Awarded by: desert_small_city_initialize
    # =========================================================

    {
        'task_id': 'desert_small_city_type_e_investigate_ledger',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'morrowdeal_krayt',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'morrowdeal_krayt',
                    'standing_text': [
                        "There's a plate in my stock I can't sell.",
                        "Every buyer picks it up and puts it right back down."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'morrowdeal_krayt',
                    'dialog_id': 'krayt_ledger_discovery'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_desert_small_e_investigate_ledger'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_desert_small_e_investigate_ledger' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',   'dialog_id': 'magic_desert_small_e_investigate_ledger'   } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_type_e_consult_venn'
                }
            }
        ]
    },

    {
        'task_id': 'desert_small_city_type_e_consult_venn',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'scrap_seer_venn',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'scrap_seer_venn',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'scrap_seer_venn',
                    'standing_text': [
                        "Krayt's plate. I remember when it surfaced.",
                        "The Signal Wraith latched onto it immediately."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'scrap_seer_venn',
                    'dialog_id': 'venn_ledger_context'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_desert_small_e_consult_venn'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_desert_small_e_consult_venn' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'skill_desert_small_e_consult_venn'   } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_type_e_confront_signal_wraith'
                }
            }
        ]
    },

    {
        'task_id': 'desert_small_city_type_e_confront_signal_wraith',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'signal_wraith',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'signal_wraith',
                    'location': None
                }
            },
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'desert_small_city_signal_relay',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'signal_wraith',
                    'standing_text': [
                        "You want the Plate.",
                        "I cannot let you have it."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'signal_wraith',
                    'dialog_id': 'signal_wraith_ledger_guardian'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',  'dialog_id': 'skill_desert_small_e_confront_signal_wraith'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_desert_small_e_confront_signal_wraith'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',  'dialog_id': 'lyren_desert_small_e_confront_signal_wraith'  } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_type_e_defeat_signal_wraith'
                }
            }
        ]
    },

    {
        'task_id': 'desert_small_city_type_e_defeat_signal_wraith',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'signal_wraith',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'signal_wraith',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'desert_small_city_e_eroded_ledger_plate'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_small_e_defeat_signal_wraith' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_desert_small_e_defeat_signal_wraith'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw',   'dialog_id': 'grimnaw_desert_small_e_defeat_signal_wraith'   } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_type_e_return_to_krayt'
                }
            }
        ]
    },

    {
        'task_id': 'desert_small_city_type_e_return_to_krayt',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'morrowdeal_krayt',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'morrowdeal_krayt',
                    'standing_text': [
                        "The static in the district dropped the moment you came back.",
                        "Whatever you did out there — it worked."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'morrowdeal_krayt',
                    'dialog_id': 'krayt_ledger_received'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_small_e_return_to_krayt' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_desert_small_e_return_to_krayt'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',       'dialog_id': 'nia_desert_small_e_return_to_krayt'       } },
        ]
    },

]
# F
TASKS += [

    # =========================================================
    # TYPE F — Contraband Registry
    # Faction Item ID: desert_small_city_f_contraband_registry
    # Recurring NPC: tess (Ch.2+)
    # Gates: snow_small_city (Bleakwatch Outpost, Ch.6) Type D (Slot 3)
    # Awarded by: desert_small_city_initialize (is_chapter_gte 2)
    # =========================================================

    {
        'task_id': 'desert_small_city_type_f_find_tess_trail',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'morrowdeal_krayt',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'morrowdeal_krayt',
                    'standing_text': [
                        "Tess blew through here two days ago.",
                        "Dropped something off and left before I could ask questions."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'morrowdeal_krayt',
                    'dialog_id': 'krayt_tess_tip'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_small_f_find_tess_trail' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',     'dialog_id': 'magic_desert_small_f_find_tess_trail'     } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',     'dialog_id': 'thorn_desert_small_f_find_tess_trail'     } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_type_f_ask_jexa'
                }
            }
        ]
    },

    {
        'task_id': 'desert_small_city_type_f_ask_jexa',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'sparkwire_Jexa',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'sparkwire_Jexa',
                    'standing_text': [
                        "Tess? Oh she was here.",
                        "Needed a tracer. Pointed it at something buried outside the city limits."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'sparkwire_Jexa',
                    'dialog_id': 'Jexa_tess_location'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'tech_desert_small_f_ask_jexa'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_desert_small_f_ask_jexa' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_desert_small_f_ask_jexa' } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_type_f_find_tess'
                }
            }
        ]
    },

    {
        'task_id': 'desert_small_city_type_f_find_tess',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'tess',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'tess',
                    'dialog_id': 'tess_radpost_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_small_f_find_tess' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_desert_small_f_find_tess'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',     'dialog_id': 'magic_desert_small_f_find_tess'     } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'desert_small_city_type_f_receive_registry'
                }
            }
        ]
    },

    {
        'task_id': 'desert_small_city_type_f_receive_registry',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'tess',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'tess',
                    'standing_text': [
                        "Still here? Good.",
                        "I made you a copy. The Bleakwatch section is the one you'll want."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'tess',
                    'dialog_id': 'tess_radpost_registry_handoff'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'tech_desert_small_f_receive_registry'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_desert_small_f_receive_registry' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_desert_small_f_receive_registry'   } },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'desert_small_city_f_contraband_registry'
                }
            }
        ]
    },

]


# ── Type D ── Scrapwright's Edge (mythic weapon) ──────────────────────────────
# Gate: player holds eroded_ledger_plate from the Type E chain (same city, Slot 1 → Slot 2).
# Deliver to Diego → Venn reads the plate → defeat Signal Wraith → mythic weapon.
# No new NPCs — uses scrap_seer_venn, signal_wraith, and diego (Ch.1 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'scrap_seer_venn',
		'dialog_id': 'venn_d_plate_read',
		'dialog': [
			"This ledger plate — it doesn't just record transactions.",
			"Every entry is a frequency signature.",
			"The Signal Wraith has been feeding on those exact frequencies since the Radpost was built.",
			"Draw it out with the plate's resonance and its static will crystallize.",
			"Diego can forge crystallized signal-static into an edge that cuts through interference.",
			"Any shield, any armor, any ward — this blade reads the frequency and bypasses it."
		]
	},

	{
		'npc_id': 'signal_wraith_2',
		'dialog_id': 'signal_wraith_d_awakens',
		'dialog': [
			"The ledger plate opens my frequency.",
			"Every transaction ever recorded here — I have been listening.",
			"You want to silence me.",
			"I will drown you in static first."
		]
	},

]

TASKS += [

	# D-0 — Deliver eroded_ledger_plate to Diego (standalone deliver; unlocks D chain)
	{
		'task_id': 'desert_small_city_type_d_deliver_ledger_plate',
		'type': 'deliver',
		'item_id': 'eroded_ledger_plate',
		'to_type': 'npc',
		'to_id': 'diego',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"That plate — I can hear a frequency humming off the metal.",
						"Whatever was recorded on it left a resonance behind.",
						"Find Venn. He speaks machine. He'll know what it's trying to say."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'eroded_ledger_plate'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_small_d_deliver_ledger_plate' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_desert_small_d_deliver_ledger_plate'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw',   'dialog_id': 'grimnaw_desert_small_d_deliver_ledger_plate'   } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_small_city_type_d_consult_venn'
				}
			},
		]
	},

	# D-1 — Consult Venn for the plate reading
	{
		'task_id': 'desert_small_city_type_d_consult_venn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'scrap_seer_venn',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scrap_seer_venn',
					'standing_text': [
						"The scrap field went quiet when you walked in.",
						"Every broken machine is listening.",
						"That plate you carry — it's speaking to all of them.",
						"Come here. Quickly."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'scrap_seer_venn',
					'dialog_id': 'venn_d_plate_read'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_desert_small_d_consult_venn'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_desert_small_d_consult_venn' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'skill_desert_small_d_consult_venn'   } },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'signal_wraith_2',
                    'location': 'region_open_area'
                }
            },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_small_city_type_d_meet_signal_wraith'
				}
			},
		]
	},

	# D-2 — Meet the Signal Wraith (boss intro)
	{
		'task_id': 'desert_small_city_type_d_meet_signal_wraith',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'signal_wraith_2',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'signal_wraith_2',
					'standing_text': [
						"Static bleeds across every device in the Bazaar.",
						"Jexa says her circuits are screaming — something is broadcasting on all channels.",
						"The ledger plate has called the Wraith forward."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'signal_wraith_2',
					'dialog_id': 'signal_wraith_d_awakens'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',  'dialog_id': 'skill_desert_small_d_meet_signal_wraith'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_desert_small_d_meet_signal_wraith'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',  'dialog_id': 'lyren_desert_small_d_meet_signal_wraith'  } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_small_city_type_d_defeat_signal_wraith'
				}
			},
		]
	},

	# D-3 — Defeat the Signal Wraith; Diego forges the mythic weapon
	{
		'task_id': 'desert_small_city_type_d_defeat_signal_wraith',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'signal_wraith_2',
		'task_acquire_events': [            
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'signal_wraith_2',
					'combat_type': 'boss_battle'
				}
			}
        ],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_desert_small_scrapwrights_edge'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_small_d_defeat_signal_wraith' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_desert_small_d_defeat_signal_wraith'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw',   'dialog_id': 'grimnaw_desert_small_d_defeat_signal_wraith'   } },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"Crystallized signal-static — I've never worked with anything like it.",
						"I've hammered it into the blade.",
						"It reads every ward and shield before you swing.",
						"Nothing will hold against this."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scrap_seer_venn',
					'standing_text': [
						"The machines are quiet again.",
						"Whatever the Wraith was broadcasting — it's gone.",
						"Jexa says her circuits finally stopped screaming."
					]
				}
			},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
    'story_id': 'desert_small_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}