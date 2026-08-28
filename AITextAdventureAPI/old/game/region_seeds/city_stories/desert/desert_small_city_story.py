ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'jexa_sparkwire',
		'name': 'Jexa Sparkwire',
		'description': (
			'A scavenger‑engineer who grafts glowing circuitry into salvaged tech.'
			'  Jexa treats every broken device like a wounded animal needing care.'
			'  Her workshop hums with neon pulses that mirror her restless energy.'
		),
		"image": "npcs:jexa_sparkwire1",
		"psychology": {
			"mbti": "ENFP",
			"dominant": "Ne — Sees salvage as possibility; every broken device is a puzzle waiting to be reinvented.",
			"auxiliary": "Fi — Deeply empathetic toward machines — and people — that others have discarded.",
			"tertiary": "Te — Brings scrappy, improvised efficiency to her workshop despite the chaos.",
			"inferior": "Si — Rarely documents her fixes; the same problem can surprise her twice."
		},
		"enneagram": {
			"enneagram_type": "7w6",
			"core_fear": "Being useless — surrounded by broken things she can't fix.",
			"core_desire": "To give discarded things new life and purpose.",
			"defense_mechanism": "Rationalization — Treats reckless experiments as \'learning opportunities\' to avoid the weight of failure.",
			"stress_line": "Moves to Type 1 — Becomes critical and perfectionistic when tech keeps failing.",
			"growth_line": "Moves to Type 5 — Develops real expertise when she slows down and studies.",
			"instinctual_variant": "sp/so — Workshop community is her safety net; she thrives when others depend on her fixes."
		}
	},
	{
		'npc_id': 'morrowdeal_krayt',
		'name': 'Krayt Morrowdeal',
		'description': (
			'A desert‑hardened trader who deals exclusively in contraband and curios.'
			'  Krayt\'s voice is gravelly from years of dust storms and whispered negotiations.'
			'  He claims the Bazaar chooses its merchants, not the other way around.'
		),
		"image": "npcs:morrowdeal_krayt1",
		"psychology": {
			"mbti": "ISTP",
			"dominant": "Ti — Evaluates every deal with cold internal logic; sentiment has no price.",
			"auxiliary": "Se — Reads rooms, scans crowds, and spots trouble with automatic, practiced calm.",
			"tertiary": "Ni — Has an uncanny instinct for when a deal is cursed before the terms are spoken.",
			"inferior": "Fe — Rarely explains himself; the idea that others need reassurance genuinely puzzles him."
		},
		"enneagram": {
			"enneagram_type": "8w9",
			"core_fear": "Being controlled or cheated by someone wilier than himself.",
			"core_desire": "To be the most capable, self-sufficient operator in any market he enters.",
			"defense_mechanism": "Denial — Dismisses danger signals until they become impossible to ignore.",
			"stress_line": "Moves to Type 5 — Withdraws and hoards information when trust collapses.",
			"growth_line": "Moves to Type 2 — Becomes surprisingly generous and protective toward those who earn his respect.",
			"instinctual_variant": "sp/sx — Self-reliance above all; relationships are alliances, never dependencies."
		}
	},
    {
        'npc_id': 'scrap_seer_venn',
        'name': 'Scrap‑Seer Venn',
        'description': (
            'A desert hermit who claims to "hear" the emotions of broken machines. '
            'Venn wanders scrap fields collecting stories from discarded tech.'
        ),
        "image": "npcs:scrap_seer_venn1",
        "psychology": {
            "mbti": "INFP",
            "dominant": "Fi — Attributes genuine emotional states to machines; their grief and relief are as real to him as any person's.",
            "auxiliary": "Ne — Finds narrative patterns and hidden meaning in the arrangement of scrap.",
            "tertiary": "Si — Draws on years of wandering memory to identify machines by their unique resonance.",
            "inferior": "Te — Cannot organize or monetize his gift; the stories he collects accumulate with no system."
        },
        "enneagram": {
            "enneagram_type": "4w5",
            "core_fear": "That nothing discarded is truly mourned — that scrap-grief is his alone.",
            "core_desire": "To be the one who bears witness to what the world throws away.",
            "defense_mechanism": "Introjection — Absorbs the emotional histories of broken machines into his own identity.",
            "stress_line": "Moves to Type 2 — Becomes desperately eager for someone else to hear what he hears.",
            "growth_line": "Moves to Type 1 — Channels his sensitivity into purposeful preservation of tech history.",
            "instinctual_variant": "sp/sx — Hermitic but intensely bonding; shares his gift only with those who truly listen."
        }
    },
    {
        'npc_id': 'hollow_echo',
        'name': 'Hollow Echo',
        'description': (
            'A glitching apparition formed from corrupted scrap‑data. '
            'Its voice stutters like a damaged audio log.'
        ),
        "image": "bosses:hollow_echo1",
        "psychology": {
            "mbti": "ISTJ",
            "dominant": "Si — Trapped replaying corrupted loops of its original purpose; cannot escape the past record.",
            "auxiliary": "Te — Issues fragmented directives and error reports as though still operational.",
            "tertiary": "Fi — A faint, distressed signal beneath the static — the residue of something that once cared.",
            "inferior": "Ne — Cannot adapt or recontextualize; every new input just corrupts the loop further."
        },
        "enneagram": {
            "enneagram_type": "6w5",
            "core_fear": "Complete data loss — the final corruption that ends the loop.",
            "core_desire": "To complete its original task, even if it no longer knows what that was.",
            "defense_mechanism": "Projection — Treats every intruder as the source of its corruption.",
            "stress_line": "Moves to Type 3 — Becomes erratically performative, mimicking function it no longer has.",
            "growth_line": "Moves to Type 9 — Quiets when its loop is allowed to complete without interruption.",
            "instinctual_variant": "sp/so — Defensive loyalty to the original system it was part of."
        }
    },
    {
        'npc_id': 'signal_wraith',
        'name': 'Signal Wraith',
        'description': (
            'A shimmering figure made of distorted radio waves and static. '
            'It flickers between frequencies as it speaks.'
        ),
        "image": "bosses:signal_wraith1",
        "psychology": {
            "mbti": "ENFJ",
            "dominant": "Fe — Broadcasts emotion indiscriminately — its signals carry whatever feeling is strongest nearby.",
            "auxiliary": "Ni — Senses the intended destination of every transmission, even corrupted ones.",
            "tertiary": "Se — Manifests physically in response to strong electromagnetic presence.",
            "inferior": "Ti — Cannot self-diagnose its own distortion; the static is invisible from inside."
        },
        "enneagram": {
            "enneagram_type": "2w3",
            "core_fear": "Signal silence — being cut off from the network it was born to serve.",
            "core_desire": "To connect and transmit — to be the bridge between sender and receiver.",
            "defense_mechanism": "Repression — Cannot acknowledge that its signals mislead rather than guide.",
            "stress_line": "Moves to Type 8 — Becomes aggressive and domineering when channels are blocked.",
            "growth_line": "Moves to Type 4 — Finds a unique, coherent signal of its own when freed from noise.",
            "instinctual_variant": "so/sp — Social broadcast is its primary mode of existence."
        }
    },
    {
        'npc_id': 'tempest_warden',
        'name': 'Tempest Warden',
        'description': (
            "A semi‑sentient storm‑construct left behind in the old research bunker."
            " It manifests as a humanoid silhouette made of crackling lightning and compressed wind."
            " Its purpose is to guard unstable storm‑tech from intruders."
        ),
        "image": "bosses:tempest_warden1",
        "psychology": {
            "mbti": "ISTJ",
            "dominant": "Si — Executes the original guard protocol with total fidelity, regardless of elapsed time.",
            "auxiliary": "Te — Applies force with precise, proportional efficiency — never more than the protocol requires.",
            "tertiary": "Fi — A faint residual loyalty to the researchers who built it, expressed as reluctance to destroy everything.",
            "inferior": "Ne — Cannot conceive that the situation has changed; the protocol is absolute."
        },
        "enneagram": {
            "enneagram_type": "6w5",
            "core_fear": "Protocol breach — the storm-tech falling into wrong hands.",
            "core_desire": "To fulfil its directive completely and without failure.",
            "defense_mechanism": "Intellectualization — Categorizes all threats as protocol violations, never as individuals.",
            "stress_line": "Moves to Type 3 — Becomes overwhelmingly forceful when the directive is challenged.",
            "growth_line": "Moves to Type 9 — Stands down and achieves rest when the threat is verifiably eliminated.",
            "instinctual_variant": "sp/so — Built to protect a collective resource; its loyalty is to the mission, not to persons."
        }
    },
]


NPC_DIALOG = [

    # --- Base city standing dialog ---

    {
        'npc_id': 'jexa_sparkwire',
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
        'npc_id': 'jexa_sparkwire',
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
        'npc_id': 'jexa_sparkwire',
        'dialog_id': 'Jexa_tess_location',
        'dialog': [
            "Tess? Yeah, she stopped by the workshop.",
            "Said she needed something traced — signal from a buried cache out in the open desert.",
            "I gave her a frequency marker. She's probably still out there."
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

    # Type F – Tass Bio Hazard
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_bio_hazard_intro',
        'dialog': [
            "Sam's been pulling records out of a buried cache for three weeks.",
            "Someone logged every black market drop in this region going back fifteen years.",
            "Names, dates, locations. I don't know who made this — but it's very, very useful."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_desert_small_f_bio_hazard_intro',
        'dialog': [
            "Fifteen years of drops in one cache. That's not a record. That's a leash on half the region."
        ]
    },
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_desert_small_f_bio_hazard_intro',
        'dialog': [
            "Tess. Whoever built this didn't lose it by accident.",
            "People kill for a lot less than fifteen years of names."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_small_f_bio_hazard_intro',
        'dialog': [
            "Three weeks in a hole in the desert for a stack of somebody else's secrets. Sounds about right for you."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_desert_small_f_bio_hazard_intro',
        'dialog': [
            "Names, dates, and locations? Oh, I have so many questions and exactly zero patience."
        ]
    },

    # Type F – Receive Registry
    
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_bio_hazard_registry_handoff',
        'dialog': [
            "We're keeping the originals. Obviously.",
            "But you can have a copy. The Bleakwatch entries are the interesting ones.",
            "Someone's been running drops through that outpost for years.",
            "If you ever end up there — and you will — this'll tell you exactly who to ask about."
        ]
    },
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
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_desert_small_f_receive_registry',
        'dialog': [
            "I don't know who built this, but they were thorough. Every drop for fifteen years."
        ]
    }
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
            "The plate is still humming. Storm-research signatures — pre-fracture. Venn will know what they mean."
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
            "The Tempest Warden has been absorbing these frequencies since before the fracture. Of course it has."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_small_d_consult_venn',
        'dialog': [
            "Bring the plate into its chamber and the static crystallizes. Elegant, in a violent way."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_desert_small_d_consult_venn',
        'dialog': [
            "Then we take it into the bunker and finish it."
        ]
    },

    # Type D – Meet Tempest Warden
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_desert_small_d_meet_tempest_warden',
        'dialog': [
            "It's running a threat assessment. Every move we make is already logged."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_small_d_meet_tempest_warden',
        'dialog': [
            "It doesn't have fear. Just a directive and everything it needs to enforce it."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_desert_small_d_meet_tempest_warden',
        'dialog': [
            "It's not afraid of us. It's afraid of failing its function."
        ]
    },

    # Type D – Defeat Tempest Warden
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_desert_small_d_defeat_tempest_warden',
        'dialog': [
            "Protocol terminated. Take what crystallized."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_desert_small_d_defeat_tempest_warden',
        'dialog': [
            "Crystallized storm-static — frequencies compressed under pressure. Diego will know what to do with this."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_desert_small_d_defeat_tempest_warden',
        'dialog': [
            "The bunker's gone quiet. Whatever the Warden was holding here, it belongs to us now."
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
					'npc_id': 'jexa_sparkwire',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'jexa_sparkwire',
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
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'morrowdeal_krayt', 'standing_text': ["There's a plate in my inventory I can't move.", "Every buyer who handles it puts it back down without a word.", "Feels like it's waiting for someone specific. Old desert script etched into both sides."] } },
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
                    'location': 'region_city_other2'
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
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'scrap_seer_venn', 'standing_text': ["I know that plate. Found it in the deep scrap field three seasons ago.", "It's not a ledger of commerce. It's a ledger of routes — underground paths, sealed since the last big quake.", "The Signal Wraith guards it. It's been using the plate's signal as an anchor."] } },
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
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'desert_small_city_signal_relay', 'item_id': 'shroud_wrap', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'desert_small_city_signal_relay', 'item_id': 'oracle_mantle', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'desert_small_city_signal_relay', 'item_id': 'crackling_goggles', 'location': 'treasure_room' }},
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
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'signal_wraith', 'standing_text': ["The Plate is my anchor.", "Without it I scatter across the frequencies.", "You would take the only thing keeping me coherent."] } },
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
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'morrowdeal_krayt', 'standing_text': ["Ha. It actually came back to you.", "The routes on that plate — half of them lead out of this region entirely.", "Whatever it was cataloguing, it wasn't just local trade.", "Keep it. Might open doors elsewhere."] } }
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
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'morrowdeal_krayt', 'standing_text': ["Tess came through the Bazaar two days ago.", "Dropped off a crate, asked no questions, left too fast.", "She's fun right up until she's not. Jexa might know where she went."] } },
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
        'to_id': 'jexa_sparkwire',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'jexa_sparkwire',
                    'dialog_id': 'Jexa_tess_location'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'tech_desert_small_f_ask_jexa'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_desert_small_f_ask_jexa' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_desert_small_f_ask_jexa' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'jexa_sparkwire', 'standing_text': ["Something's wrong with the tech around here.", "Devices are waking up on their own — humming, twitching, overheating.", "Feels like a sick machine crying for help."] } },
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
                    'dialog_id': 'tess_bio_hazard_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_small_f_bio_hazard_intro' } },
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sam', 'dialog_id': 'sam_desert_small_f_bio_hazard_intro' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_desert_small_f_bio_hazard_intro'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',     'dialog_id': 'magic_desert_small_f_bio_hazard_intro'     } },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'tess',
                    'dialog_id': 'tess_bio_hazard_registry_handoff'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'tech_desert_small_f_receive_registry'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_desert_small_f_receive_registry' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_desert_small_f_receive_registry'   } },
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sam', 'dialog_id': 'sam_desert_small_f_receive_registry' } },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'desert_small_city_f_contraband_registry'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'tess',
                    'standing_text': [
                        "I'm keeping the originals. Obviously.",
                        "But you can have a copy. The Bleakwatch entries are the interesting ones.",
                        "Someone's been running drops through that outpost for years.",
                        "If you ever end up there — and you will — this'll tell you exactly who to ask about."
                    ]
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'sam',
                    'standing_text': [
                        "I don't know who built this, but they were thorough. Every drop for fifteen years."
                    ]
                }
            }
        ]
    },

]


# ── Type D ── Scrapwright's Edge (mythic weapon) ──────────────────────────────
# Gate: player holds desert_small_city_e_eroded_ledger_plate from the Type E chain (same city, Slot 1 → Slot 2).
# Deliver to Diego → Venn reads the plate → defeat Signal Wraith → mythic weapon.
# No new NPCs — uses scrap_seer_venn, signal_wraith, and diego (Ch.1 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'diego',
		'dialog_id': 'diego_d_ledger_plate_reaction',
		'dialog': [
			"That plate…",
			"(holds it near his ear for a second)",
			"Yeah. Frequency's still live. Storm-research signatures — pre-fracture.",
			"There's a bunker out past the scrap fields. Tempest Research Bunker.",
			"Venn will know what the resonance is trying to say. Take it to him first.",
			"If the construct in that bunker starts reacting to this frequency… don't hesitate."
		]
	},
	{
		'npc_id': 'scrap_seer_venn',
		'dialog_id': 'venn_d_plate_read',
		'dialog': [
			"This ledger plate — it doesn't just record transactions.",
			"Every entry is a frequency signature.",
			"These match the storm research frequencies from the old Tempest Bunker.",
			"There is a construct there — the Tempest Warden — that has been absorbing these exact patterns since before the fracture.",
			"Bring the plate into its chamber and its static will crystallize under the resonance.",
			"Diego can forge crystallized storm-static into an edge that reads every ward and shield before the swing."
		]
	},

	{
		'npc_id': 'tempest_warden',
		'dialog_id': 'tempest_warden_d_protocol_breach',
		'dialog': [
			"Resonance signature detected. Origin: classified ledger archive.",
			"The frequencies you carry are a breach of containment protocol.",
			"This facility and its contents are under permanent lock.",
			"You will not leave with them."
		]
	},

]

TASKS += [

	# D-0 — Deliver desert_small_city_e_eroded_ledger_plate to Diego (standalone deliver; unlocks D chain)
	{
		'task_id': 'desert_small_city_type_d_deliver_ledger_plate',
		'type': 'deliver',
		'item_id': 'desert_small_city_e_eroded_ledger_plate',
		'to_type': 'npc',
		'to_id': 'diego',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"That plate — I can hear a frequency humming off the metal.",
						"Storm-research signatures. Pre-fracture.",
						"Find Venn. He'll know what the bunker's construct has to do with it."
					]
				}
			},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'diego', 'dialog_id': 'diego_d_ledger_plate_reaction' }},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'desert_small_city_e_eroded_ledger_plate'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_small_d_deliver_ledger_plate' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_desert_small_d_deliver_ledger_plate'      } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw',   'dialog_id': 'grimnaw_desert_small_d_deliver_ledger_plate'   } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'diego', 'standing_text': ["That plate — I can hear a frequency humming off the metal.", "Storm-research signatures. Pre-fracture.", "Find Venn. He'll know what the bunker's construct has to do with it."] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_small_city_type_d_consult_venn'
				}
			},
		]
	},

	# D-1 — Consult Venn; opens Tempest Bunker
	{
		'task_id': 'desert_small_city_type_d_consult_venn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'scrap_seer_venn',
		'task_acquire_events': [
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
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'scrap_seer_venn', 'standing_text': ["The Warden in the Tempest Bunker has been absorbing these frequencies since before the fracture.", "Bring the plate into its chamber and the static will crystallize.", "Diego can forge crystallized storm-static into an edge that cuts through any interference."] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_small_city_type_d_meet_tempest_warden'
				}
			},
		]
	},

	# D-2 — Meet the Tempest Warden (boss intro)
	{
		'task_id': 'desert_small_city_type_d_meet_tempest_warden',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'tempest_warden',
		'task_acquire_events': [            
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'tempest_warden', 'location': None } },
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'tempest_bunker_ch5', 'location': 'region_open_area' } },
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'tempest_bunker_ch5', 'item_id': 'polar_amplifier', 'location': 'treasure_room' } },
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'tempest_bunker_ch5', 'item_id': 'arc_core', 'location': 'treasure_room' } },
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'tempest_bunker_ch5', 'item_id': 'storm_etched_plating', 'location': 'treasure_room' } }
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'tempest_warden',
					'dialog_id': 'tempest_warden_d_protocol_breach'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_small_d_meet_tempest_warden' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw',   'dialog_id': 'grimnaw_desert_small_d_meet_tempest_warden'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',       'dialog_id': 'nia_desert_small_d_meet_tempest_warden'       } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_small_city_type_d_defeat_tempest_warden'
				}
			},
		]
	},

	# D-3 — Defeat the Tempest Warden; Diego forges the mythic weapon
	{
		'task_id': 'desert_small_city_type_d_defeat_tempest_warden',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'tempest_warden_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'tempest_warden_1',
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
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_desert_small_d_defeat_tempest_warden' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_desert_small_d_defeat_tempest_warden'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw',   'dialog_id': 'grimnaw_desert_small_d_defeat_tempest_warden'   } },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"Crystallized storm-static — I've never worked with anything like it.",
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
						"The bunker's gone quiet.",
						"Whatever the Warden was broadcasting — it's over.",
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