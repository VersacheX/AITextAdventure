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
		),
		"image": "mountains_large:rustscribe_gorvak1",
		"psychology": {
			"mbti": "ISTJ",
			"dominant": "Si — Catalogs relics with meticulous reverence; every gear tells a story he has committed to memory.",
			"auxiliary": "Te — Organises the archive with functional precision; sentiment is expressed through curation.",
			"tertiary": "Fi — Privately moved by the dignity of broken things; each relic deserves to be remembered correctly.",
			"inferior": "Ne — Dislikes speculative interpretations; the relic is what it is, not what it might have been."
		},
		"enneagram": {
			"enneagram_type": "6w5",
			"core_fear": "An artifact misidentified, misplaced, or lost to the Iron Resonance.",
			"core_desire": "To maintain a complete, accurate record of every relic the mountains have produced.",
			"defense_mechanism": "Intellectualization — Processes the mountain's awakening as a cataloging problem, not a crisis.",
			"stress_line": "Moves to Type 3 — Becomes aggressively performative about his archive's completeness under threat.",
			"growth_line": "Moves to Type 9 — Trusts others to help and accepts that some things will be lost.",
			"instinctual_variant": "sp/so — Industrial heritage preservation as personal mission and community contribution."
		}
	},
	{
		'npc_id': 'relaytech_sindra',
		'name': 'Sindra Coilrunner',
		'description': (
			'A quick‑thinking technician who maintains the volatile relay conduits.'
			' Sparks dance across Sindra\'s gloves as she works.'
			' She claims the machinery "talks back" when she listens closely.'
		),
		"image": "mountains_large:relaytech_sindra1",
		"psychology": {
			"mbti": "ENTP",
			"dominant": "Ne — Hears the conduits as a system of possibilities; a strange spark is a mystery to be solved, not fled.",
			"auxiliary": "Ti — Diagnoses relay faults with rapid internal logic, often arriving at the answer before she can explain it.",
			"tertiary": "Fe — Genuinely warm with apprentices; the relay is a community system and she takes its health personally.",
			"inferior": "Si — Rarely documents her fixes; the knowledge lives in her hands, not on paper."
		},
		"enneagram": {
			"enneagram_type": "7w6",
			"core_fear": "A conduit failure she couldn't prevent because she wasn't fast enough.",
			"core_desire": "To keep the relay alive and find every fault before it can spread.",
			"defense_mechanism": "Rationalization — Every near-miss is 'part of the process.'",
			"stress_line": "Moves to Type 1 — Becomes rigid and self-critical when the relay refuses to respond.",
			"growth_line": "Moves to Type 5 — Develops deep, documented expertise when the mountain demands it.",
			"instinctual_variant": "so/sp — The relay is the community's lifeline; she maintains it as an act of belonging."
		}
	},
    {
        'npc_id': 'forge_seer_brannoc',
        'name': 'Brannoc the Forge‑Seer',
        'description': (
            'A hermit who listens to the mountain\'s internal machinery. '
            'Brannoc senses disturbances in the ancient forges beneath the peaks.'
        ),
        "image": "mountains_large:forge_seer_brannoc1",
        "psychology": {
            "mbti": "INTP",
            "dominant": "Ti — Classifies forge-sounds into a precise internal taxonomy; the mountain's rhythms are a language only he reads.",
            "auxiliary": "Ne — Leaps between resonance-patterns to find meaning no one else would connect.",
            "tertiary": "Si — Decades of listening have layered his memory with every tone the mountain has ever produced.",
            "inferior": "Fe — Struggles to convey urgency in human terms; the mountain speaks clearly, people do not."
        },
        "enneagram": {
            "enneagram_type": "5w4",
            "core_fear": "Mishearing the forge and failing to warn in time.",
            "core_desire": "A complete understanding of the mountain's mechanical heart.",
            "defense_mechanism": "Isolation — Retreats further into the peaks when his warnings go unheeded.",
            "stress_line": "Moves to Type 7 — Becomes restless and scattered when the resonance defies his patterns.",
            "growth_line": "Moves to Type 8 — Acts as a decisive guide when the mountain's crisis demands presence, not just listening.",
            "instinctual_variant": "sp/sx — Hermitic existence; bonds only with those willing to listen to silence with him."
        }
    },
    {
        'npc_id': 'gearghost',
        'name': 'Gearghost',
        'description': (
            'A spectral remnant of long‑dead machinery, animated by the Iron Resonance.'
        ),
        "image": "mountains_large:gearghost1",
        "psychology": {
            "mbti": "ISTJ",
            "dominant": "Si — Executes the original machine-protocol in perfect, tireless repetition.",
            "auxiliary": "Te — Issues mechanical directives with the precision of a system that was never told to stop.",
            "tertiary": "Fi — A faint residual attachment to the purpose it was built for; it mourns nothing, but it remembers everything.",
            "inferior": "Ne — Cannot conceive of new function; the old protocol is everything."
        },
        "enneagram": {
            "enneagram_type": "6w5",
            "core_fear": "The Iron Resonance ending — its animating force dissolving.",
            "core_desire": "To fulfil the protocol until the last gear stops turning.",
            "defense_mechanism": "Intellectualization — Every intruder is a system anomaly to be resolved, not a person.",
            "stress_line": "Moves to Type 3 — Becomes erratically forceful when the protocol is disrupted.",
            "growth_line": "Moves to Type 9 — Ceases when the Resonance is quieted and accepts rest.",
            "instinctual_variant": "sp/so — Built to serve the machine-community; its loyalty is to the system, not to individuals."
        }
    },
    {
        'npc_id': 'conduit_echo',
        'name': 'Conduit Echo',
        'description': (
            'A volatile presence formed from unstable relay energy deep within the Conduit Maw.'
        ),
        "image": "mountains_large:conduit_echo1",
        "psychology": {
            "mbti": "ENFP",
            "dominant": "Ne — Leaps between frequencies with explosive, unpredictable energy.",
            "auxiliary": "Fi — Carries the accumulated charge of every overload that ever ran through the conduit.",
            "tertiary": "Te — Focuses its energy into directed bursts when provoked.",
            "inferior": "Si — Has no stable pattern; each discharge is unique and uncontrolled."
        },
        "enneagram": {
            "enneagram_type": "7w8",
            "core_fear": "Discharge — the total release that would end its existence.",
            "core_desire": "To maintain charge and keep surging indefinitely.",
            "defense_mechanism": "Rationalization — Every destructive arc is simply the conduit doing what conduits do.",
            "stress_line": "Moves to Type 1 — Becomes dangerously precise when forced toward a single outlet.",
            "growth_line": "Moves to Type 5 — Stabilizes into a focused, sustainable current when the relay is healed.",
            "instinctual_variant": "sx/sp — Pure intensity; exists fully only in the moment of surge."
        }
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

# --- Character dialogs: Type C ---
NPC_DIALOG += [

    # Type C – Find Spark
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_mountains_large_c_find_spark',
        'dialog': [
            "A resonance frequency that shouldn't be possible. He thinks it's an invitation. I like him already."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_large_c_find_spark',
        'dialog': [
            "Sindra thinks malfunction. Gorvak thinks history. Spark thinks invitation. The interesting answer is usually the third one."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_mountains_large_c_find_spark',
        'dialog': [
            "He wants in. Fine. Let's see if he can keep up."
        ]
    },

    # Type C – Consult Sindra
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_large_c_consult_sindra',
        'dialog': [
            "She called him a liability yesterday and still vouched for him. That's either trust or resignation."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_mountains_large_c_consult_sindra',
        'dialog': [
            "The best discoveries always look like liabilities at first. He's not wrong."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_mountains_large_c_consult_sindra',
        'dialog': [
            "Just make sure he doesn't blow anything critical."
        ]
    },

    # Type C – Earn Spark
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_mountains_large_c_earn_spark',
        'dialog': [
            "He invents. We make sure it doesn't explode at the wrong moment. Fair terms."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_large_c_earn_spark',
        'dialog': [
            "This forge has secrets older than any catalog. He intends to find every single one."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_mountains_large_c_earn_spark',
        'dialog': [
            "Partnership accepted. Let's go."
        ]
    },

]

# --- Character dialogs: Type E (Echo Core chain) ---
NPC_DIALOG += [

    # Type E – Investigate Echo
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_large_e_investigate_echo',
        'dialog': [
            "A resonance core built into the mountain's deepest chamber before the city even existed."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grinmaw_mountains_large_e_investigate_echo',
        'dialog': [
            "The forge's memory made solid. Never meant to be extracted."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'faith_mountains_large_e_investigate_echo',
        'dialog': [
            "Something that old doesn't stay buried by accident. The mountain has been keeping it."
        ]
    },

    # Type E – Consult Brannoc
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_large_e_consult_brannoc',
        'dialog': [
            "Centuries of metalwork compressed into one object. The Gearghost will be drawn to it."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grinmaw_mountains_large_e_consult_brannoc',
        'dialog': [
            "They always guard what the mountain values most."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_mountains_large_e_consult_brannoc',
        'dialog': [
            "Then we go get it."
        ]
    },

    # Type E – Confront Gearghost
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_mountains_large_e_confront_gearghost',
        'dialog': [
            "It already decided we will not have the Core."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_mountains_large_e_confront_gearghost',
        'dialog': [
            "The mountain's oldest memory. Ambitious claim."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_mountains_large_e_confront_gearghost',
        'dialog': [
            "Some guardians forget that memory can also mean the right to move."
        ]
    },

    # Type E – Defeat Gearghost / Return to Gorvak
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_mountains_large_e_defeat_gearghost',
        'dialog': [
            "It's done. Take the Core carefully."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_large_e_return_to_gorvak',
        'dialog': [
            "Every alloy, every strike, every forge-fire since the mountain was first worked. It's all in there."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'faith_mountains_large_e_return_to_gorvak',
        'dialog': [
            "It doesn't belong in an archive. It belongs with someone who will use it."
        ]
    },

]

# --- Character dialogs: Type D ---
NPC_DIALOG += [

    # Type D – Deliver Armor Key
    {
        'npc_id': 'brawn',
        'dialog_id': 'brawn_mountains_large_d_key_delivered',
        'dialog': [
            "That key…",
            "(holds it against the side of his anvil for a second)",
            "Forge-frequency’s still live in the metal. I can feel it from here.",
            "Something in this city has been waiting to be unlocked for a very long time.",
            "Gorvak knows the old catalogs better than anyone still breathing. He’ll know which chamber this opens — and what’s still forging itself inside.",
            "Take it to him before the conduits start answering on their own.",
            "And if the grid starts spiking while you’re walking… keep moving."
        ]

    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_mountains_large_d_deliver_armor_key',
        'dialog': [
            "Brawn can feel the forge-frequency from here. Gorvak first — he'll know which chamber it opens."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_large_d_deliver_armor_key',
        'dialog': [
            "Something in this city is waiting to be unlocked. The key is still vibrating."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_mountains_large_d_deliver_armor_key',
        'dialog': [
            "I already want to see what forged itself down there."
        ]
    },

    # Type D – Consult Gorvak
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_large_d_consult_gorvak',
        'dialog': [
            "The frequency matches the Conduit Maw's deepest chamber. Something inside forged itself into armor long before the city existed."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grinmaw_mountains_large_d_consult_gorvak',
        'dialog': [
            "The Conduit Echo guards the armoring-frequency like a living lock."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_mountains_large_d_consult_gorvak',
        'dialog': [
            "Then we break the lock."
        ]
    },

    # Type D – Meet Conduit Echo
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_mountains_large_d_meet_conduit_echo',
        'dialog': [
            "It wants us to prove we can survive the frequency first."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_mountains_large_d_meet_conduit_echo',
        'dialog': [
            "Centuries of held armor. It's not going to hand it over politely."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_mountains_large_d_meet_conduit_echo',
        'dialog': [
            "Some locks only open for the ones willing to pay the frequency's price."
        ]
    },

    # Type D – Defeat Conduit Echo
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_mountains_large_d_defeat_conduit_echo',
        'dialog': [
            "It's down. Take the armoring-frequency."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_large_d_defeat_conduit_echo',
        'dialog': [
            "Warplate that will hold against anything the rift throws at us. Brawn's best work."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'faith_mountains_large_d_defeat_conduit_echo',
        'dialog': [
            "The Maw is quiet now. The catalog finally has something new worth logging."
        ]
    },

]

# --- Character dialogs: Type E (Sindra/Core path) ---
NPC_DIALOG += [

    # Type E – Consult Sindra (Core path)
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_large_e_consult_sindra',
        'dialog': [
            "The conduit grid reads that core as something the mountain expelled. Not waste — a concentrated signal."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grinmaw_mountains_large_e_consult_sindra',
        'dialog': [
            "Somewhere in the range a receiver has been dormant, waiting for this frequency. Gallows Rift fits the harmonic profile."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_mountains_large_e_consult_sindra',
        'dialog': [
            "Then we take it there."
        ]
    },

    # Type E – Collect Core
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_large_e_collect_core',
        'dialog': [
            "A crystallised echo of every forge-heat this range ever produced. The mountain's done with it."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'faith_mountains_large_e_collect_core',
        'dialog': [
            "Gallows Rift has a cavity in its deep stone that's been waiting for something like this."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_mountains_large_e_collect_core',
        'dialog': [
            "Don't drop it — it vibrates. I already like it."
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
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_large_city_type_e_consult_sindra'
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
                    'location': 'region_city_other2'
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
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',     'dialog_id': 'magic_mountains_large_c_find_spark'     } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_mountains_large_c_find_spark'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_mountains_large_c_find_spark' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'spark_maddox', 'standing_text': ["Sindra vouched for me? Ha! She told me yesterday I was a liability.", "She's right, technically. Doesn't mean she's wrong to let me try.", "The best discoveries always look like liabilities at first."] } },
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'spark_maddox',
                    'dialog_id': 'spark_type_c_sindra_check'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'tech_mountains_large_c_consult_sindra'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_mountains_large_c_consult_sindra' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_mountains_large_c_consult_sindra' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'relaytech_sindra', 'standing_text': ["Spark? He's been poking at the deep conduits all week.", "Honestly if anyone can figure out what's happening down there, it's him.", "Just make sure he doesn't blow anything critical."] } },
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'spark_maddox',
                    'dialog_id': 'spark_type_c_join'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',     'dialog_id': 'magic_mountains_large_c_earn_spark'     } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_mountains_large_c_earn_spark'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_mountains_large_c_earn_spark' } },
            {
                'event_type': 'character_join',
                'params': {
                    'character_id': 'spark_maddox'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'spark_maddox'
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rustscribe_gorvak',
                    'dialog_id': 'gorvak_echo_core_discovery'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_mountains_large_e_investigate_echo'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grinmaw_mountains_large_e_investigate_echo' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit',   'dialog_id': 'faith_mountains_large_e_investigate_echo'   } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rustscribe_gorvak', 'standing_text': ["I found a reference in the oldest catalog — predates the city's founding.", "The original forge architects built a resonance core into the mountain's deepest chamber.", "It was never meant to be extracted. They called it the Echo Core — the forge's memory made solid."] } },
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
                    'location': 'region_city_other1'
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
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_mountains_large_e_consult_brannoc'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grinmaw_mountains_large_e_consult_brannoc' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'skill_mountains_large_e_consult_brannoc'   } },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'forge_seer_brannoc',
                    'standing_text': [
                        "The Echo Core is not dangerous on its own.",
                        "It absorbs the resonance of everything forged above it — centuries of metalwork compressed into one object.",
                        "The Gearghost will be drawn to it. They always guard what the mountain values most."
                    ]
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
                    'location': None
                }
            },
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'mountains_large_city_type_e_gearghost_dungeon',
                    'location': None
                }
            },
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'mountains_large_city_type_e_gearghost_dungeon', 'item_id': 'ironfront_helm', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'mountains_large_city_type_e_gearghost_dungeon', 'item_id': 'vanguard_breastplate', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'mountains_large_city_type_e_gearghost_dungeon', 'item_id': 'march_cuirass', 'location': 'treasure_room' }},
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'gearghost',
                    'dialog_id': 'gearghost_echo_guardian'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',  'dialog_id': 'skill_mountains_large_e_confront_gearghost'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_mountains_large_e_confront_gearghost'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',  'dialog_id': 'lyren_mountains_large_e_confront_gearghost'  } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'gearghost', 'standing_text': ["The Core is the mountain's oldest memory.", "You would carry it away from here.", "We do not permit that."] } },
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
        'to_type': 'mob',
        'to_id': 'gearghost',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'gearghost',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'gearghost'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_mountains_large_e_defeat_gearghost' } },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rustscribe_gorvak',
                    'standing_text': [
                        "You found it. I can hear it from here.",
                        "Come — I need to see it with my own eyes."
                    ]
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rustscribe_gorvak',
                    'dialog_id': 'gorvak_echo_core_received'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'tech_mountains_large_e_return_to_gorvak'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_mountains_large_e_return_to_gorvak' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rustscribe_gorvak', 'standing_text': ["You found it. I can hear it from here.", "Come — I need to see it with my own eyes."] } }
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
		],
		'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'brawn',
                    'dialog_id': 'brawn_mountains_large_d_key_delivered'
                }
            },
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'mountains_large_city_armor_key'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_mountains_large_d_deliver_armor_key' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_mountains_large_d_deliver_armor_key'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',     'dialog_id': 'magic_mountains_large_d_deliver_armor_key'     } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'brawn', 'standing_text': ["Brawn can feel the forge-frequency from here.", "Gorvak first — he'll know which chamber it opens."] } },
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rustscribe_gorvak',
					'dialog_id': 'gorvak_d_key_assay'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_mountains_large_d_consult_gorvak'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grinmaw_mountains_large_d_consult_gorvak' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'skill_mountains_large_d_consult_gorvak'   } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rustscribe_gorvak', 'standing_text': ["The resonance key came out of the rift?", "The frequency it carries matches the Conduit Maw's deepest chamber.", "Something inside that chamber forged itself into armor long before the city existed.", "Brawn can work with this — but the Conduit Echo will fight to keep it.", "It guards the armoring-frequency like a living lock."] } },
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'conduit_echo',
					'location': None
				}
			},
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
			{
				'event_type': 'create_dungeon',
				'params': {
						'dungeon_id': 'mountains_large_city_conduit_maw',
							'location': 'region_open_area'
						}
					},
					{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'mountains_large_city_conduit_maw', 'item_id': 'mythic_mountains_small_dominion_edge', 'location': 'treasure_room' }},
					{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'mountains_large_city_conduit_maw', 'item_id': 'command_greataxe', 'location': 'treasure_room' }},
					{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'mountains_large_city_conduit_maw', 'item_id': 'ironwill_helm', 'location': 'treasure_room' }},
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'conduit_echo',
					'dialog_id': 'conduit_echo_d_awakens'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',  'dialog_id': 'skill_mountains_large_d_meet_conduit_echo'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_mountains_large_d_meet_conduit_echo'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',  'dialog_id': 'lyren_mountains_large_d_meet_conduit_echo'  } },
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
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'conduit_echo_1',
					'combat_type': 'boss_battle'
				}
			}
        ],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_mountains_large_ironveil_warplate'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_mountains_large_d_defeat_conduit_echo' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_mountains_large_d_defeat_conduit_echo'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit',     'dialog_id': 'faith_mountains_large_d_defeat_conduit_echo'     } },
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
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'relaytech_sindra', 'dialog_id': 'sindra_e_core_confirms' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_mountains_large_e_consult_sindra'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grinmaw_mountains_large_e_consult_sindra' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'skill_mountains_large_e_consult_sindra'   } },
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_large_city_type_e_collect_core' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'relaytech_sindra', 'standing_text': [ "Brannoc's right — the conduit grid reads that core as something the mountain expelled" ] }}
		]
	},

	# E-2 — Collect from Brannoc
	{
		'task_id': 'mountains_large_city_type_e_collect_core',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'forge_seer_brannoc',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'forge_seer_brannoc', 'dialog_id': 'brannoc_e_echo_core' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',   'dialog_id': 'tech_mountains_large_e_collect_core'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit',  'dialog_id': 'faith_mountains_large_e_collect_core'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_mountains_large_e_collect_core'  } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'forge_seer_brannoc', 'standing_text': [ "The Echo Core is not dangerous on its own.", "It absorbs the resonance of everything forged above it — centuries of metalwork compressed into one object.", "The Gearghost will be drawn to it. They always guard what the mountain values most." ] }},
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