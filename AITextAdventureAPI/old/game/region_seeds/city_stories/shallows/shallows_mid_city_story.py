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
        ),
        "psychology": {
            "mbti": "INFJ",
            "dominant": "Ni — Perceives hidden meaning in fractured signals, trusting intuition over the literal.",
            "auxiliary": "Fe — Reads the moods of sailors and townsfolk as easily as lantern codes, offering quiet reassurance.",
            "tertiary": "Ti — Cross-checks each pattern against internal logic before committing to a reading.",
            "inferior": "Se — Uneasy in the immediate chaos of storms, retreating into contemplation rather than action."
        },
        "enneagram": {
            "enneagram_type": "5w4",
            "core_fear": "Being overwhelmed by meaninglessness — signals that resolve to nothing.",
            "core_desire": "To understand the hidden order beneath the coast's noise.",
            "defense_mechanism": "Isolation — withdraws into study when patterns turn contradictory.",
            "stress_line": "Moves to Type 7 — scatters into frantic over-interpretation, chasing every flicker.",
            "growth_line": "Moves to Type 8 — acts decisively on his readings instead of endlessly deliberating.",
            "instinctual_variant": "sp/sx — Guards his solitude and energy, but bonds intensely with those who share his search."
        }
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

# --- Character dialogs: Type E (Tidekin Seal chain) ---
NPC_DIALOG += [

    # Type E – Investigate Seal
    { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_mid_e_investigate_seal',    'dialog': [ "Ceremonial, old Tidekin script around the rim. Merrik won't touch it — says it should go back where it came from." ] },
    { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_mid_e_investigate_seal', 'dialog': [ "The problem is nobody knows where that is. The undertunnel doesn't keep clear records." ] },
    { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_mid_e_investigate_seal',   'dialog': [ "Thalen will know the resonance." ] },

    # Type E – Consult Thalen
    { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_mid_e_consult_thalen',    'dialog': [ "Coastal clans used these to mark founding pacts. This one was separated from its cove during the storm that buried the undertunnel." ] },
    { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_mid_e_consult_thalen', 'dialog': [ "The Lanternfade Echo has been drawn to its resonance. It will try to claim it before we do." ] },
    { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_mid_e_consult_thalen',   'dialog': [ "Take it before the echo bonds completely." ] },

    # Type E – Confront Lanternfade Echo
    { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_mid_e_confront_lanternfade_echo', 'dialog': [ "It already decided the Seal is theirs." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_e_confront_lanternfade_echo', 'dialog': [ "'We answered. It is ours now.' Bold claim for something that just showed up." ] },
    { 'npc_id': 'lyren', 'dialog_id': 'lyren_shallows_mid_e_confront_lanternfade_echo', 'dialog': [ "Some echoes only know how to answer a call. They never ask who the call was meant for." ] },

    # Type E – Defeat Lanternfade Echo / Return to Vexa
    { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_mid_e_return_to_vexa', 'dialog': [ "It's dispersed. The Seal knows us now." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_e_return_to_vexa',  'dialog': [ "Merrik will say it should go to the courts. Don't. Something that old belongs somewhere specific." ] },
    { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_mid_e_return_to_vexa', 'dialog': [ "We'll figure out where." ] },

]

# --- Character dialogs: Type C (Dare chain) ---
NPC_DIALOG += [

    # Type C – Find Dare
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_c_find_dare', 'dialog': [ "A signal network nobody's touched in twenty years and routes that don't exist on any chart. She's already in." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_c_find_dare',  'dialog': [ "Vexa showed her the undertunnel maps. She's been waiting for someone who looks curious enough to follow." ] },
    { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_mid_c_find_dare', 'dialog': [ "We look curious enough." ] },

    # Type C – Consult Vexa
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_c_consult_vexa',  'dialog': [ "Reliable when it counts. Reckless the rest of the time. Vexa says we'd make a good pair." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_c_consult_vexa', 'dialog': [ "High praise from her. She doesn't say that about anyone." ] },
    { 'npc_id': 'bragg', 'dialog_id': 'bragg_shallows_mid_c_consult_vexa', 'dialog': [ "She's been scouting the coastline for a month. The undertunnel is the most interesting thing she's found." ] },

    # Type C – Earn Dare
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_c_earn_dare', 'dialog': [ "She moves fast and asks questions after. Fair warning." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_c_earn_dare',  'dialog': [ "If that's a problem, say so now. Otherwise we go find whatever's at the end of those routes." ] },
    { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_mid_c_earn_dare', 'dialog': [ "Not a problem. Let's move." ] },

]

# --- Character dialogs: Type D (Corsair's Depth Blade chain) ---
NPC_DIALOG += [

    # Type D – Deliver Corsair Fragment
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_d_deliver_corsair_fragment',  'dialog': [ "The metal has a tide-pull Diego's never felt in steel. Something in Blackwake Bay resonates with it." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_d_deliver_corsair_fragment', 'dialog': [ "Thalen reads the coastal signals. He'll know where this belongs." ] },
    { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_mid_d_deliver_corsair_fragment', 'dialog': [ "Find him." ] },

    # Type D – Consult Thalen
    { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_mid_d_consult_thalen',    'dialog': [ "The fragment carries the tide-frequency of Stormglass Alley. The Undertunnel Voice holds the matching resonance." ] },
    { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_mid_d_consult_thalen', 'dialog': [ "The corsair lineage sealed it there deliberately. Draw the Voice out with the fragment and the tide-steel solidifies." ] },
    { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_mid_d_consult_thalen',   'dialog': [ "Then we draw it out." ] },

    # Type D – Meet Undertunnel Voice
    { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_mid_d_meet_undertunnel_voice', 'dialog': [ "It's carrying every misdirected signal and every lost smuggler route." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_d_meet_undertunnel_voice', 'dialog': [ "'Take it from me if you can navigate the dark.' We can." ] },
    { 'npc_id': 'lyren', 'dialog_id': 'lyren_shallows_mid_d_meet_undertunnel_voice', 'dialog': [ "Some voices only know how to hold what the tunnels refused to return." ] },

    # Type D – Defeat Undertunnel Voice
    { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_mid_d_defeat_undertunnel_voice', 'dialog': [ "Quiet. Take the corsair-tide steel." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_d_defeat_undertunnel_voice',  'dialog': [ "A blade that knows every current and tunnel beneath the bay. Nothing will hold a line against this." ] },
    { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_mid_d_defeat_undertunnel_voice', 'dialog': [ "Every misdirected signal the Voice held has resolved. The tunnels are finally quiet." ] },

]

# --- Character dialogs: Type E post-chain (Seal path) ---
NPC_DIALOG += [

    # Type E – Consult Vexa (Seal path)
    { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_mid_e_consult_vexa',    'dialog': [ "Tidekin mark. A family in Tidekin Cove used it on sealed cargo that never arrived." ] },
    { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_mid_e_consult_vexa', 'dialog': [ "That wax has been waiting to close something ever since." ] },
    { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_mid_e_consult_vexa',   'dialog': [ "Collect it." ] },

    # Type E – Collect Seal
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_e_collect_seal',  'dialog': [ "Pressed into the wall near the entrance. Wax that hasn't aged. Cove marker Merrik doesn't recognise." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_e_collect_seal', 'dialog': [ "Vexa confirmed the crest. If it belongs to Tidekin Cove, it should go there." ] },
    { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_mid_e_collect_seal', 'dialog': [ "Take it through proper channels — whatever those are for us." ] },

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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'lanternrunner_vexa',
                    'dialog_id': 'vexa_tidekin_seal_discovery'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_mid_e_investigate_seal'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_mid_e_investigate_seal' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_mid_e_investigate_seal'   } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lanternrunner_vexa', 'standing_text': [ "Found something in the undertunnel last week — wedged behind a collapsed wall.", "Looks ceremonial. Old Tidekin script around the rim.", "Merrik won't touch it. Says it should go back to where it came from.", "The problem is nobody knows where that is." ] } },
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
                    'location': 'region_city_other2'
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
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_mid_e_consult_thalen'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_mid_e_consult_thalen' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_mid_e_consult_thalen'   } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'signal_seer_thalen', 'standing_text': [ "The Tidekin Seal. The coastal clans used it to mark founding pacts.", "This one was separated from its cove — probably during the storm that buried the undertunnel.", "The Lanternfade Echo has been drawn to its resonance. It will try to claim it.", "Take it before the echo bonds to it completely." ] } },
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
                    'location': None
                }
            },
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'shallows_mid_city_type_e_defeat_lanternfade_echo',
                    'location': 'region_open_area'
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
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_mid_e_confront_lanternfade_echo' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_e_confront_lanternfade_echo' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_shallows_mid_e_confront_lanternfade_echo' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lanternfade_echo', 'standing_text': [ "We are the signals that faded.", "The False Lantern twists our light.", "It waits deeper in the Undertunnel." ] } },
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
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'lanternfade_echo'
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'lanternrunner_vexa',
                    'dialog_id': 'vexa_tidekin_seal_received'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_mid_e_return_to_vexa' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_e_return_to_vexa'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_mid_e_return_to_vexa' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lanternrunner_vexa', 'standing_text': [ "You got it out clean. Merrik's going to say you should hand it over to the courts.", "Don't. Something that old belongs somewhere specific. You'll figure out where." ] } }
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
                    'location': 'region_bar'
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
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_c_find_dare' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_c_find_dare'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_mid_c_find_dare' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'dare', 'standing_text': [ "You hear that? That's the sound of a signal network nobody's touched in twenty years.", "Vexa showed me the undertunnel maps. There are routes in there that don't exist on any chart.", "I want in. I'm guessing you do too, or you wouldn't be standing here looking curious." ] } },
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'dare',
                    'dialog_id': 'dare_type_c_vexa_check'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_c_consult_vexa'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_c_consult_vexa' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_shallows_mid_c_consult_vexa' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lanternrunner_vexa', 'standing_text': [ "Vexa says you're reliable. High praise from her — she doesn't say that about anyone.", "I've been scouting this coastline for a month. The undertunnel is the most interesting thing I've found.", "You look like you know how to move through interesting places without dying." ] },
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
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'dare',
                    'dialog_id': 'dare_type_c_join'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_c_earn_dare' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_c_earn_dare'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_mid_c_earn_dare' } },
            {
                'event_type': 'character_join',
                'params': {
                    'character_id': 'dare'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'dare'
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

	{
		'npc_id': 'diego',
		'dialog_id': 'diego_d_fragment_received',
		'dialog': [
			"That fragment\u2026",
			"(turns the metal once, feeling the pull)",
			"Tide-pull I've never felt in steel. Not forge-heat. Not residual charge. Actual current, locked inside the grain.",
			"Something in Blackwake Bay is still answering it \u2014 every lantern on the waterfront just flickered the same direction.",
			"Thalen reads the coastal signals better than anyone still breathing. He'll know which drowned tunnel this belongs to.",
			"Take it to him before the Voice finishes noticing you're carrying it.",
			"And if the undertunnel starts humming while you're walking\u2026 keep moving."
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'diego',
					'dialog_id': 'diego_d_fragment_received'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_d_deliver_corsair_fragment'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_d_deliver_corsair_fragment' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_mid_d_deliver_corsair_fragment' } },
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'corsair_tide_fragment'
				}
			},
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'signal_seer_thalen',
					'dialog_id': 'thalen_d_fragment_read'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_mid_d_consult_thalen'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_mid_d_consult_thalen' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_mid_d_consult_thalen'   } },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'undertunnel_voice',
                    'location': None
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'undertunnel_voice',
                    'standing_text': [
                        "The corsair fragment opens the deep tunnel.",
                        "Every misdirected signal, every lost smuggler route — I carry them all.",
                        "You want the tide-steel the corsairs buried here.",
                        "Take it from me if you can navigate the dark."
                    ]
                }
            },
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'shallows_mid_city_type_d_defeat_undertunnel_voice',
                    'location': 'region_open_area'
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'undertunnel_voice',
					'dialog_id': 'undertunnel_voice_d_awakens'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_mid_d_meet_undertunnel_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_d_meet_undertunnel_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_shallows_mid_d_meet_undertunnel_voice' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'undertunnel_voice', 'standing_text': [ "The corsair fragment opens the deep tunnel.", "Every misdirected signal, every lost smuggler route — I carry them all.", "You want the tide-steel the corsairs buried here.", "Take it from me if you can navigate the dark." ] } },
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
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'undertunnel_voice'
                }
            },
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_shallows_mid_corsairs_depth_blade'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_mid_d_defeat_undertunnel_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_d_defeat_undertunnel_voice'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_mid_d_defeat_undertunnel_voice' } },
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
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lanternrunner_vexa', 'dialog_id': 'vexa_e_seal_context' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_mid_e_consult_vexa'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_mid_e_consult_vexa' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_mid_e_consult_vexa'   } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lanternrunner_vexa', 'standing_text': [
				"Merrik pulled something out of the tunnel evidence.",
				"A seal I recognise. Come — I'll tell you where it needs to go."
			]}},
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
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'tidejudge_merrik', 'dialog_id': 'merrik_e_tidekin_seal' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_mid_e_collect_seal'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_mid_e_collect_seal' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_mid_e_collect_seal' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'tidejudge_merrik', 'standing_text': [
				"Evidence logged. Case closed.",
				"The seal has no jurisdiction here.",
				"Come collect it."
			]}},
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