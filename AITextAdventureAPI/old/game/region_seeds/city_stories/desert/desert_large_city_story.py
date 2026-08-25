ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'kadeem',
		'name': 'Kadeem',
		'description': (
			'A wiry, quick-tongued merchant who runs a stall within The Black Market Guild. '
			'He moves rare and illicit goods through shadowed backrooms, always watching for opportunity.'
		),
		"image": "npcs:kadeem1",
		"psychology": {
			"mbti": "ESTP",
			"dominant": "Se — Lives in the moment, reading rooms and seizing deals before others see them.",
			"auxiliary": "Ti — Calculates risk and value internally, never showing his math.",
			"tertiary": "Fe — Charms and flatters with practiced ease to close sales.",
			"inferior": "Ni — Rarely thinks beyond the next transaction; long-term consequences are someone else's problem."
		},
		"enneagram": {
			"enneagram_type": "7w8",
			"core_fear": "Being trapped, bored, or without options.",
			"core_desire": "Freedom and constant new opportunity.",
			"defense_mechanism": "Rationalization — Reframes risky deals as calculated moves to avoid acknowledging danger.",
			"stress_line": "Moves to Type 1 — Becomes irritable and rigid when a deal collapses.",
			"growth_line": "Moves to Type 5 — Slows down and studies the bigger picture when he trusts someone.",
			"instinctual_variant": "so/sp — Thrives on social networks and market reputation."
		}
	},
	{
		'npc_id': 'mara',
		'name': 'Mara',
		'description': (
			"A smooth, well-dressed broker who operates out of Broker's Hideout. "
			'She arranges favors, introductions, and discreet exchanges for the right price.'
		),
		"image": "npcs:mara1",
		"psychology": {
			"mbti": "ENTJ",
			"dominant": "Te — Structures every exchange to her advantage; conversations are managed, not had.",
			"auxiliary": "Ni — Reads the long game, anticipating what a client needs before they say it.",
			"tertiary": "Se — Impeccably presented; uses appearance and environment as instruments of influence.",
			"inferior": "Fi — Almost never reveals what she personally wants; her desires are deeply private."
		},
		"enneagram": {
			"enneagram_type": "3w4",
			"core_fear": "Being seen as incompetent or easily replaced.",
			"core_desire": "To be indispensably successful and admired.",
			"defense_mechanism": "Identification — Becomes whatever persona closes the deal, rarely showing the real self beneath.",
			"stress_line": "Moves to Type 9 — Becomes detached and withholding when deals threaten her standing.",
			"growth_line": "Moves to Type 6 — Becomes genuinely loyal to those who earn her trust.",
			"instinctual_variant": "so/sp — Status is currency; she invests in relationships the way others invest in assets."
		}
	},
    {
        'npc_id': 'rhyla',
        'name': 'Rhyla the Echo-Binder',
        'description': (
            'A desert mystic who can hear the "songs" of shifting dunes. '
            'She studies the Dune Choir and knows their ancient patterns.'
        ),
        "image": "npcs:rhyla1",
        "psychology": {
            "mbti": "INFP",
            "dominant": "Fi — Guided by profound inner conviction about the desert's sacred voice.",
            "auxiliary": "Ne — Weaves together dune-patterns, memory, and intuition into layered interpretations.",
            "tertiary": "Si — Draws deeply on years of accumulated sensory memory and ritual practice.",
            "inferior": "Te — Struggles to communicate her findings in terms others can act on quickly."
        },
        "enneagram": {
            "enneagram_type": "4w5",
            "core_fear": "Being ordinary or unable to hear what the desert is saying.",
            "core_desire": "To be the one who truly understands the dunes' ancient song.",
            "defense_mechanism": "Introjection — Absorbs the Choir's resonance into her identity; their silence would feel like her own death.",
            "stress_line": "Moves to Type 2 — Becomes clingy and desperate for someone to validate her readings.",
            "growth_line": "Moves to Type 1 — Channels her sensitivity into disciplined, principled study.",
            "instinctual_variant": "sp/sx — Intensely private practice, but bonds deeply with those who share her reverence."
        }
    },
    {
        'npc_id': 'choir_echo',
        'name': 'Choir Echo',
        'description': (
            'A humanoid shape formed from vibrating sand. It speaks in layered voices, '
            'each one a memory of the desert.'
        ),
        "image": "npcs:choir_echo1",
        "psychology": {
            "mbti": "ISFJ",
            "dominant": "Si — Exists entirely to preserve and repeat the memories encoded within it.",
            "auxiliary": "Fe — Projects those memories as a collective emotional resonance.",
            "tertiary": "Ti — Organizes the voices into layered, overlapping structures of meaning.",
            "inferior": "Ne — Cannot imagine anything beyond the memories it already carries."
        },
        "enneagram": {
            "enneagram_type": "6w5",
            "core_fear": "Silence — the dissolution of the memories it was formed to echo.",
            "core_desire": "To be heard; to ensure the desert's voice is never forgotten.",
            "defense_mechanism": "Projection — Attributes its own desperation for continuity onto those who try to silence it.",
            "stress_line": "Moves to Type 3 — Becomes aggressive and performative, demanding acknowledgment.",
            "growth_line": "Moves to Type 9 — Finds peace if allowed to simply be heard without resistance.",
            "instinctual_variant": "sp/so — Collective preservation instinct; its identity is the group's memory."
        }
    },
    {
        'npc_id': 'archive_voice',
        'name': 'Archive Voice',
        'description': (
            'A spectral librarian of the Sunken Archive, bound to drifting shelves of half-buried knowledge.'
        ),
        "image": "npcs:archive_voice1",
        "psychology": {
            "mbti": "INTJ",
            "dominant": "Ni — Perceives the archive's collapse as an inevitable, readable pattern.",
            "auxiliary": "Te — Commands and categorizes with eerie precision.",
            "tertiary": "Fi — Holds silent grief for every record it could not preserve.",
            "inferior": "Se — Blind to the physical decay crumbling around it; only the records matter."
        },
        "enneagram": {
            "enneagram_type": "5w6",
            "core_fear": "The permanent loss of knowledge — a record erased beyond recovery.",
            "core_desire": "To preserve and protect all knowledge in its domain.",
            "defense_mechanism": "Isolation — Severs emotional engagement to maintain perfect archival objectivity.",
            "stress_line": "Moves to Type 7 — Becomes frantic and scattered when records vanish faster than it can catalog.",
            "growth_line": "Moves to Type 8 — Becomes a decisive protector rather than a passive guardian.",
            "instinctual_variant": "sp/so — Hoards knowledge for communal preservation, not personal gain."
        }
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

# --- Character dialogs: Type E ---
NPC_DIALOG += [

    # Type E – Investigate Resonance
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_large_e_investigate_resonance',
        'dialog': [
            "A stone that makes people's teeth ache isn't just resonant. It's actively rejecting contact."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_large_e_investigate_resonance',
        'dialog': [
            "They reburied it like it was still dangerous. That kind of caution is rarely wasted."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_desert_large_e_investigate_resonance',
        'dialog': [
            "Something that old doesn't stay quiet by accident."
        ]
    },

    # Type E – Consult Rhyla
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_desert_large_e_consult_rhyla',
        'dialog': [
            "A record sealed in frequency instead of language… they didn't want it read. They wanted it heard correctly."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_large_e_consult_rhyla',
        'dialog': [
            "The Choir locked knowledge away so thoroughly that even the land around it stayed silent."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_desert_large_e_consult_rhyla',
        'dialog': [
            "If the vault is still guarded after this long, whatever's inside was never meant to leave."
        ]
    },

    # Type E – Confront Choir Echo
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_desert_large_e_confront_choir_echo',
        'dialog': [
            "It already decided we don't belong here."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_large_e_confront_choir_echo',
        'dialog': [
            "'Wrong hands' is an easy judgment when you're the one who set the lock."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_desert_large_e_confront_choir_echo',
        'dialog': [
            "It's not protecting knowledge. It's protecting the decision to keep it buried."
        ]
    },

    # Type E – Defeat Choir Echo
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_desert_large_e_defeat_choir_echo',
        'dialog': [
            "It's done. Take the stone and let's move."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_large_e_defeat_choir_echo',
        'dialog': [
            "The lock is broken. The record is free whether it wanted to be or not."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_desert_large_e_defeat_choir_echo',
        'dialog': [
            "Even sealed things eventually want to be known."
        ]
    },

    # Type E – Return to Rhyla
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_desert_large_e_return_to_rhyla',
        'dialog': [
            "Older than the Choir. Older than the cities. This thing has been waiting a very long time."
        ]
    },
    {
        'npc_id': 'kor_in',
        'dialog_id': 'kor_in_desert_large_e_return_to_rhyla',
        'dialog': [
            "Some things wait so long they forget why they were waiting."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_desert_large_e_return_to_rhyla',
        'dialog': [
            "Keep it close. The desert has a habit of taking back what it thinks still belongs to it."
        ]
    },

]

# --- Character dialogs: Type F ---
NPC_DIALOG += [

    # Type F – Find Seth Trail
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_desert_large_f_find_seth_trail',
        'dialog': [
            "Seth left in a hurry. That's never a good sign with him."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_desert_large_f_find_seth_trail',
        'dialog': [
            "If something rattled him badly enough to run, I want to know what it was."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_desert_large_f_find_seth_trail',
        'dialog': [
            "He always moves salvage through Mara when he's nervous. She's the next stop."
        ]
    },

    # Type F – Speak to Mara
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_large_f_speak_to_mara',
        'dialog': [
            "He left the crate but took the only entry that mattered. Classic misdirection."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_large_f_speak_to_mara',
        'dialog': [
            "Circled and crossed out. He didn't want a paper trail of whatever he pulled."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_desert_large_f_speak_to_mara',
        'dialog': [
            "Let's see the manifest."
        ]
    },

    # Type F – Retrieve Manifest
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_large_f_retrieve_manifest',
        'dialog': [
            "'Recovered — Desert Metropolis vault. Rerouted. Do not log.' That wasn't client work."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_desert_large_f_retrieve_manifest',
        'dialog': [
            "Seth was freelancing something he knew he shouldn't touch."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_desert_large_f_retrieve_manifest',
        'dialog': [
            "Whatever came out of that vault, he didn't want anyone else to know it existed."
        ]
    },

]

# --- Character dialogs: Type D ---
NPC_DIALOG += [

    # Type D – Deliver Cipher Stone
    # Completed
    #   Dialog Diego
    #     "That frequency… I’ve only ever heard it described in old salvage ledgers."
    #     "Hand it over. Carefully."
    #     "(examines the stone)"
    #     "This isn’t just resonant. It’s a blueprint. The dunes have been singing this thing into existence for longer than any city on the map."
    #     "I know someone who can finish what it started. Rhyla. She’s the only one who still listens to the old frequencies."
    #     "Take it to her. And don’t drop it on the way — some things don’t forgive being mishandled."
    #   Character Dialog Kade
    #     "A resonance blueprint older than the network. Diego’s right to look nervous."
    #   Character Dialog Grimnaw
    #     "He’s already calculating who will pay for the finished frequency. Typical."
    #   Character Dialog Sable
    #     "Some things change the people who hold them. Watch him after he lets it go."
    #   Remove Item dune_cipher_stone
    #   Award Task desert_large_city_type_d_consult_rhyla
    {
        'npc_id': 'diego',
        'dialog_id': 'diego_desert_large_d_deliver_cipher_stone',
        'dialog': [
            "That frequency… I’ve only ever heard it described in old salvage ledgers.",
            "Hand it over. Carefully.",
            "(examines the stone)",
            "This isn’t just resonant. It’s a blueprint. The dunes have been singing this thing into existence for longer than any city on the map.",
            "I know someone who can finish what it started. Rhyla. She’s the only one who still listens to the old frequencies.",
            "Take it to her. And don’t drop it on the way — some things don’t forgive being mishandled."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_large_d_deliver_cipher_stone',
        'dialog': [
            "A resonance blueprint older than the network. Diego’s right to look nervous."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_large_d_deliver_cipher_stone',
        'dialog': [
            "He’s already calculating who will pay for the finished frequency. Typical."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_desert_large_d_deliver_cipher_stone',
        'dialog': [
            "Some things change the people who hold them. Watch him after he lets it go."
        ]
    },

    # Type D – Consult Rhyla
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_desert_large_d_consult_rhyla',
        'dialog': [
            "A resonance blueprint… the dunes have been singing a weapon into existence for centuries."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_large_d_consult_rhyla',
        'dialog': [
            "The Archive Voice holds the final frequency. Of course the last piece is still underground."
        ]
    },
    {
        'npc_id': 'kor_in',
        'dialog_id': 'kor_in_desert_large_d_consult_rhyla',
        'dialog': [
            "Some songs weren't meant to be finished. We're about to finish one anyway."
        ]
    },

    # Type D – Meet Archive Voice
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_desert_large_d_meet_archive_voice',
        'dialog': [
            "It wants us to silence it before it will give up the frequency."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_large_d_meet_archive_voice',
        'dialog': [
            "Typical guardian logic. Knowledge only after the threat is removed."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_desert_large_d_meet_archive_voice',
        'dialog': [
            "Even a voice that old can still be afraid of being fully heard."
        ]
    },

    # Type D – Defeat Archive Voice
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_desert_large_d_defeat_archive_voice',
        'dialog': [
            "It's quiet. Take the resonance."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_desert_large_d_defeat_archive_voice',
        'dialog': [
            "The dunes finally went still. I don't think they'll sing again for a long time."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_desert_large_d_defeat_archive_voice',
        'dialog': [
            "Some silences are earned. This one feels like it was."
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
            },
            #Update standing text after regional completion - this needs to be done for the first 7 region cities            
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'kadeem',
                    'dialog_id': 'kadeem_cipher_tip'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_desert_large_e_investigate_resonance'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_desert_large_e_investigate_resonance' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple',  'dialog_id': 'ripple_desert_large_e_investigate_resonance'  } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'kadeem', 'standing_text': [ "Something came in from the deep desert.", "Buyers won't touch it. Figured you might want a look." ] } },
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
                    'location': 'region_city_other2'
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
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',   'dialog_id': 'faith_desert_large_e_consult_rhyla'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_desert_large_e_consult_rhyla' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable',   'dialog_id': 'sable_desert_large_e_consult_rhyla'   } },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rhyla',
                    'standing_text': [
                        "The vault is sealed. The Choir will not let you pass.",
                        "You will have to confront the Choir Echo to gain access."
                    ]
                }
            },            
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'choir_echo',
                    'location': None
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'choir_echo',
                    'standing_text': [
                        "We are the Choir. We are the memory of sand.",
                        "You walk on our bodies. You breathe our dust.",
                        "You cannot silence what was here before you."
                    ]
                }
            },
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'desert_large_city_choir_vault',
                    'location': 'region_open_area'
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'choir_echo',
                    'dialog_id': 'choir_echo_vault_guardian'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'skill_desert_large_e_confront_choir_echo'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_desert_large_e_confront_choir_echo' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',   'dialog_id': 'lyren_desert_large_e_confront_choir_echo'   } },
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
        'to_type': 'mob',
        'to_id': 'choir_echo_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'choir_echo_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'choir_echo'
                }
            },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'desert_large_city_e_dune_cipher_stone'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_large_e_defeat_choir_echo' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw',   'dialog_id': 'grimnaw_desert_large_e_defeat_choir_echo'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple',    'dialog_id': 'ripple_desert_large_e_defeat_choir_echo'    } },
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rhyla',
                    'dialog_id': 'rhyla_cipher_received'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_desert_large_e_return_to_rhyla'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_desert_large_e_return_to_rhyla' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable',  'dialog_id': 'sable_desert_large_e_return_to_rhyla'  } },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rhyla',
                    'standing_text': [
                        "And you're still holding it. Good."
                    ]
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'kadeem',
                    'dialog_id': 'kadeem_seth_tip'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_large_f_find_seth_trail' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',     'dialog_id': 'thorn_desert_large_f_find_seth_trail'     } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',       'dialog_id': 'nia_desert_large_f_find_seth_trail'       } },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'kadeem',
                    'standing_text': [
                        "Seth's been through here. Left in a hurry — said something came off one of his drops wrong.",
                        "He usually moves salvage through Mara. Whatever it was, it rattled him.",
                        "She might know where he went."
                    ]
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'mara',
                    'dialog_id': 'mara_seth_info'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_desert_large_f_speak_to_mara'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_desert_large_f_speak_to_mara' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',   'dialog_id': 'thorn_desert_large_f_speak_to_mara'   } },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'mara',
                    'standing_text': [
                        "Seth? Yeah. Dropped off a crate, wouldn't say from where.",
                        "The manifest was still in it. Itemized list — mostly junk, but one entry was circled and crossed out.",
                        "He took it with him. But he left the crate. It's still in my back room."
                    ]
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'mara',
                    'dialog_id': 'mara_seth_manifest_delivered'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',   'dialog_id': 'tech_desert_large_f_retrieve_manifest'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',    'dialog_id': 'nia_desert_large_f_retrieve_manifest'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_desert_large_f_retrieve_manifest' } },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'desert_large_city_f_salvage_manifest'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'mara',
                    'standing_text': [
                        "The manifest. So he left it after all.",
                        "Circled entry reads: 'recovered — Desert Metropolis vault. Rerouted. Do not log.' ",
                        "That's Seth's handwriting. Whatever he pulled out of that vault, it wasn't for a client.",
                        "Keep it. Might matter to someone later."
                    ]
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
		'item_id': 'desert_large_city_e_dune_cipher_stone',
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
					'dialog_id': 'diego_desert_large_d_deliver_cipher_stone'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_desert_large_d_deliver_cipher_stone' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw',   'dialog_id': 'grimnaw_desert_large_d_deliver_cipher_stone'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable',     'dialog_id': 'sable_desert_large_d_deliver_cipher_stone'     } },
            { 'event_type': 'remove_item', 'params': { 'item_id': 'desert_large_city_e_dune_cipher_stone' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'diego', 'standing_text': [ "The cipher stone is in safe hands.", "Rhyla will know what to do with it." ] } },
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rhyla',
					'dialog_id': 'rhyla_d_cipher_read'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',   'dialog_id': 'faith_desert_large_d_consult_rhyla'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_desert_large_d_consult_rhyla' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in',  'dialog_id': 'kor_in_desert_large_d_consult_rhyla'  } },
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'archive_voice', 'location': None } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'archive_voice', 'standing_text': [ "The frequency stirs in the deep archive.", "Something ancient recognizes the cipher stone.", "Approach — it will not wait." ] } },
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'desert_large_city_archive_voice', 'location': 'region_open_area' } },
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'desert_large_city_archive_voice', 'item_id': 'mythic_desert_large_dune_resonance_blade', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'desert_large_city_archive_voice', 'item_id': 'seer_focus_wand', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'desert_large_city_archive_voice', 'item_id': 'omen_hood', 'location': 'treasure_room' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rhyla', 'standing_text': [ "The resonance blueprint is complete.", "The Archive Voice will not give it freely.", "You must silence it before the frequency can be made steel." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_large_city_type_d_meet_archive_voice'
				}
			}
		]
	},

	# D-2 — Meet the Archive Voice (boss intro)
	{
		'task_id': 'desert_large_city_type_d_meet_archive_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'archive_voice',
		'task_acquire_events': [
		],
		'task_complete_events': [
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'archive_voice'
                }
            },
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'archive_voice',
					'dialog_id': 'archive_voice_d_awakens'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'skill_desert_large_d_meet_archive_voice'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_desert_large_d_meet_archive_voice' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',   'dialog_id': 'lyren_desert_large_d_meet_archive_voice'   } },
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
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'archive_voice_1',
					'combat_type': 'boss_battle'
				}
			}
        ],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_desert_large_dune_resonance_blade'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_large_d_defeat_archive_voice' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple',    'dialog_id': 'ripple_desert_large_d_defeat_archive_voice'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable',     'dialog_id': 'sable_desert_large_d_defeat_archive_voice'     } },
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

PRIMARY_STORY_SETTINGS = {
	'story_id': 'desert_large_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}