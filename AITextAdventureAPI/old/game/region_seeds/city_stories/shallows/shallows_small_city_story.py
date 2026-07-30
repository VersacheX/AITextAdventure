ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'signalwatch_errol',
		'name': 'Errol Signalwatch',
		'description': (
			'A vigilant lookout who monitors the coastline for danger.'
			' Errol\'s signal flags move with flawless precision, even in storms.'
			' He claims he can read the sea\'s intentions like a book.'
		)
	},
	{
		'npc_id': 'runner_sylka',
		'name': 'Sylka the Cove‑Runner',
		'description': (
			'A swift courier who navigates hidden passages beneath the docks.'
			' Sylka\'s boots are always damp with seawater and secrets.'
			' She knows every smuggler\'s route but keeps her own path hidden.'
		)
	},
    {
        'npc_id': 'mist_seer_loryth',
        'name': 'Loryth the Mist‑Seer',
        'description': (
            'A fog‑reader who interprets drifting mist glyphs and senses drowned warnings.'
        )
    },
    {
        'npc_id': 'fogwhisper_echo',
        'name': 'Fogwhisper Echo',
        'description': (
            'A spectral remnant of lost coastal warnings swallowed by fog.'
        )
    },
    {
        'npc_id': 'coveveil_voice',
        'name': 'Coveveil Voice',
        'description': (
            'A whispering presence formed from hidden cove passages and drowned secrets.'
        )
    }
]


NPC_DIALOG = [

    {
        'npc_id': 'signalwatch_errol',
        'dialog_id': 'errol_intro',
        'dialog': [
            "The sea's signals blur.",
            "Flags read wrong even when the wind is steady.",
            "Something hides warnings beneath the fog."
        ]
    },

    {
        'npc_id': 'runner_sylka',
        'dialog_id': 'sylka_intro',
        'dialog': [
            "Hidden routes feel wrong.",
            "The fog watches back.",
            "If we don't act, the coves will swallow travelers whole."
        ]
    },

    {
        'npc_id': 'mist_seer_loryth',
        'dialog_id': 'loryth_intro',
        'dialog': [
            "The mist glyphs twist.",
            "A Silent Buoy rises — a spirit of drowned warnings.",
            "If it awakens, the coast will lose its voice."
        ]
    },

    {
        'npc_id': 'fogwhisper_echo',
        'dialog_id': 'fogwhisper_echo_intro',
        'dialog': [
            "We are the warnings the fog devoured.",
            "The Silent Buoy twists our signals.",
            "It waits deeper in the Coveveil Passage."
        ]
    },

    {
        'npc_id': 'coveveil_voice',
        'dialog_id': 'coveveil_voice_intro',
        'dialog': [
            "The Passage hums with stolen warnings.",
            "The Silent Buoy gathers strength.",
            "Only its heart remains to be dimmed."
        ]
    },

    {
        'npc_id': 'signalwatch_errol',
        'dialog_id': 'errol_closing',
        'dialog': [
            "The fog clears. The signals return.",
            "You've restored the coast's voice.",
            "The Shallows will remember your vigilance."
        ]
    },

	# ── Type C dialogs — Andrea Starveil ───────────────────────────
	{
		'npc_id': 'signalwatch_errol',
		'dialog_id': 'errol_c_andrea_sighting',
		'dialog': [
			"There's a performer who came in on the last tide.",
			"She's been doing something strange — lifting spirits in a city that has mandated celebration.",
			"Everyone here is supposed to be happy.",
			"She's the only one who actually seems to mean it.",
			"Sylka knows her. She ran the route she arrived on."
		]
	},
	{
		'npc_id': 'runner_sylka',
		'dialog_id': 'sylka_c_andrea_vouch',
		'dialog': [
			"Andrea Starveil.",
			"She paid me in a story instead of coin.",
			"Normally I'd refuse. But the story was worth it.",
			"She's the real thing — joy as an act of defiance in a place that weaponises it.",
			"Tell her Sylka says the hidden routes are clear.",
			"She'll know what that means."
		]
	},
	{
		'npc_id': 'andrea_starveil',
		'dialog_id': 'andrea_c_first_meet',
		'dialog': [
			"Sylka's phrase.",
			"She doesn't share that with people who aren't worth the route.",
			"I've been watching your crew move through this place.",
			"You're not performing survival — you're actually doing it.",
			"That's the most interesting thing I've seen in months.",
			"What's next?"
		]
	},
	{
		'npc_id': 'andrea_starveil',
		'dialog_id': 'andrea_c_joins',
		'dialog': [
			"Morale isn't a luxury.",
			"It's the difference between a party that breaks and one that doesn't.",
			"I keep people standing.",
			"Let me come."
		]
	},
]

# --- Character dialogs: main story chain ---
NPC_DIALOG += [

    # Meet Errol
    { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_small_meet_errol',    'dialog': [ "Flags reading wrong even when the wind is steady. Something is hiding warnings under the fog." ] },
    { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_small_meet_errol', 'dialog': [ "The sea's signals are blurring on purpose. That's never just weather." ] },
    { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_small_meet_errol',   'dialog': [ "Sylka will know the routes that feel wrong." ] },

    # Meet Sylka
    { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_small_meet_sylka', 'dialog': [ "Hidden routes feel wrong. The fog is watching back." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_meet_sylka', 'dialog': [ "If we don't act, the coves will swallow travelers whole. She's not exaggerating." ] },
    { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_small_meet_sylka', 'dialog': [ "Find Loryth. The mist glyphs will tell us what's rising." ] },

    # Find Loryth
    { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_small_find_loryth',    'dialog': [ "A Silent Buoy — spirit of drowned warnings. If it awakens, the coast loses its voice." ] },
    { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_small_find_loryth', 'dialog': [ "The mist glyphs are already twisting toward it. We move before it finishes rising." ] },
    { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_small_find_loryth',   'dialog': [ "Fogwhisper Inlet next." ] },

    # Fogwhisper Inlet
    { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_small_fogwhisper_inlet', 'dialog': [ "They are the warnings the fog devoured." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_fogwhisper_inlet', 'dialog': [ "The Silent Buoy is twisting their signals. It waits deeper in the Coveveil Passage." ] },
    { 'npc_id': 'lyren', 'dialog_id': 'lyren_shallows_small_fogwhisper_inlet', 'dialog': [ "Some warnings only know how to be swallowed. We take them back." ] },

    # Coveveil Passage
    { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_small_coveveil_passage', 'dialog': [ "The Passage is humming with stolen warnings." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_small_coveveil_passage',  'dialog': [ "The Silent Buoy is gathering strength. Only its heart remains." ] },
    { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_small_coveveil_passage', 'dialog': [ "Then we dim it." ] },

    # Silent Buoy
    { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_small_silent_buoy', 'dialog': [ "The fog clears. The signals return." ] },
    { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_small_silent_buoy', 'dialog': [ "You've restored the coast's voice. The Shallows will remember." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_small_silent_buoy',  'dialog': [ "Errol can read the flags again. That's enough." ] },

]

# --- Character dialogs: Type C (Andrea Starveil chain) ---
NPC_DIALOG += [

    # Type C – Find Andrea
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_c_find_andrea', 'dialog': [ "A performer lifting spirits in a city that has mandated celebration. She's the only one who actually means it." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_small_c_find_andrea',  'dialog': [ "Sylka ran the route she arrived on. She'll know everything." ] },
    { 'npc_id': 'nia',   'dialog_id': 'nia_shallows_small_c_find_andrea',   'dialog': [ "Joy as an act of defiance. That's rare." ] },

    # Type C – Consult Sylka
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_c_consult_sylka', 'dialog': [ "She paid in a story instead of coin. Sylka says the story was worth it." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_small_c_consult_sylka',  'dialog': [ "Tell her the hidden routes are clear. She'll know what that means." ] },
    { 'npc_id': 'nia',   'dialog_id': 'nia_shallows_small_c_consult_sylka',   'dialog': [ "The real thing — joy that isn't performed for the mandate." ] },

    # Type C – Earn Andrea
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_c_earn_andrea', 'dialog': [ "We're not performing survival — we're actually doing it. That's the most interesting thing she's seen in months." ] },
    { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_small_c_earn_andrea', 'dialog': [ "Morale isn't a luxury. It's the difference between a party that breaks and one that doesn't." ] },
    { 'npc_id': 'nia',   'dialog_id': 'nia_shallows_small_c_earn_andrea',   'dialog': [ "She keeps people standing. Let her come." ] },

]

# --- Character dialogs: Type D (Tidecaller's Edge chain) ---
NPC_DIALOG += [

    # Type D – Deliver Tidekin Seal
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_small_d_deliver_tidekin_seal',  'dialog': [ "The metal radiates dense and old — like the sea hardened it deliberately. Loryth reads the mist glyphs here." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_d_deliver_tidekin_seal', 'dialog': [ "If anything in this cove knows what that seal unlocks, she does." ] },
    { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_small_d_deliver_tidekin_seal', 'dialog': [ "Find her before the Passage notices." ] },

    # Type D – Consult Loryth
    { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_small_d_consult_loryth',    'dialog': [ "The Tidekin were the Cove's first wardens. They sealed their authority into objects like this when they passed on." ] },
    { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_small_d_consult_loryth', 'dialog': [ "The Coveveil Passage holds the resonance of their final ward. The seal is calling it forward." ] },
    { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_small_d_consult_loryth',   'dialog': [ "The Voice will not release the Tidekin metal willingly." ] },

    # Type D – Meet Coveveil Voice
    { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_small_d_meet_coveveil_voice', 'dialog': [ "It already decided we are not Tidekin." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_d_meet_coveveil_voice', 'dialog': [ "Every hidden route, every drowned warning, every smuggled secret — it holds them all." ] },
    { 'npc_id': 'lyren', 'dialog_id': 'lyren_shallows_small_d_meet_coveveil_voice', 'dialog': [ "Some voices only know how to keep what the first wardens left behind." ] },

    # Type D – Defeat Coveveil Voice
    { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_small_d_defeat_coveveil_voice', 'dialog': [ "Quiet. Take the Tidekin iron." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_small_d_defeat_coveveil_voice',  'dialog': [ "It doesn't rust, doesn't dull, and it knows where the current is before you do." ] },
    { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_small_d_defeat_coveveil_voice', 'dialog': [ "Every hidden route the Voice sealed has opened. The cove-runners can move freely again." ] },

]

# --- Character dialogs: Type B (Uul'thar chain) ---
NPC_DIALOG += [

    # B – Meet Uul'thar
    { 'npc_id': 'technique',  'dialog_id': 'chock_shallows_small_b_meet_uulthar',  'dialog': [ "The water remembers him. Let it show us where he is." ] },
    { 'npc_id': 'ripple', 'dialog_id': 'ripple_shallows_small_b_meet_uulthar', 'dialog': [ "I am not afraid of this water. I just need to keep reminding myself of that." ] },
    { 'npc_id': 'tech',   'dialog_id': 'kade_shallows_small_b_meet_uulthar',   'dialog': [ "He sees us as a point of failure. We reconfigure the argument." ] },

    # B – Defeat Uul'thar
    { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_small_b_defeat_uulthar', 'dialog': [ "Stay down. The tide doesn't need another system to correct." ] },
    { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_small_b_defeat_uulthar', 'dialog': [ "Some of us used to think the world was a system to be corrected. We learned to let the tide be what it is." ] },

]


TASKS = [
	{
		'task_id': 'shallows_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'signalwatch_errol',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'signalwatch_errol',
					'standing_text': [
						"The sea speaks in flags—watch with me and tell me what you spy."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'runner_sylka',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'runner_sylka',
					'standing_text': [
						"Hidden coves have stories—whisper one to me between the waves."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_small_city_meet_errol'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_small_city_type_c_find_andrea'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_small_city_type_d_deliver_tidekin_seal'
				}
			}
		]
	},

    # Task 1 — Meet Errol after initialization
    {
        'task_id': 'shallows_small_city_meet_errol',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'signalwatch_errol',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'signalwatch_errol',
                    'standing_text': [
                        "The sea's signals blur.",
                        "Flags read wrong even when the wind is steady."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'signalwatch_errol',
                    'dialog_id': 'errol_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_small_meet_errol'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_small_meet_errol' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_small_meet_errol'   } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_small_city_meet_sylka'
                }
            }
        ]
    },

    # Task 2 — Meet Sylka for the cove‑runner's perspective
    {
        'task_id': 'shallows_small_city_meet_sylka',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'runner_sylka',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'runner_sylka',
                    'dialog_id': 'sylka_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_small_meet_sylka' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_meet_sylka' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_small_meet_sylka' } },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'runner_sylka',
                    'standing_text': [
                        "Hidden routes feel wrong.",
                        "Something in the fog watches back."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_small_city_find_loryth'
                }
            }
        ]
    },

    # Task 3 — Find Mist‑Seer Loryth in the open shallows
    {
        'task_id': 'shallows_small_city_find_loryth',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'mist_seer_loryth',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'mist_seer_loryth',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'mist_seer_loryth',
                    'standing_text': [
                        "The mist glyphs twist.",
                        "A Silent Buoy rises beneath the fog."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'mist_seer_loryth',
                    'dialog_id': 'loryth_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_small_find_loryth'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_small_find_loryth' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_small_find_loryth'   } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_small_city_fogwhisper_inlet'
                }
            }
        ]
    },

    # Task 4 — Explore the Fogwhisper Inlet (first dungeon)
    {
        'task_id': 'shallows_small_city_fogwhisper_inlet',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'fogwhisper_echo',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'fogwhisper_inlet',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'fogwhisper_echo',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'fogwhisper_echo',
                    'dialog_id': 'fogwhisper_echo_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_small_fogwhisper_inlet' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_fogwhisper_inlet' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_shallows_small_fogwhisper_inlet' } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_small_city_coveveil_passage'
                }
            }
        ]
    },

    # Task 5 — Descend into the Coveveil Passage (second dungeon)
    {
        'task_id': 'shallows_small_city_coveveil_passage',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'coveveil_voice',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'coveveil_passage',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'coveveil_voice',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'coveveil_voice',
                    'dialog_id': 'coveveil_voice_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_small_coveveil_passage' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_small_coveveil_passage'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_small_coveveil_passage' } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_small_city_silent_buoy'
                }
            }
        ]
    },

    # Task 6 — Defeat the Silent Buoy (boss dungeon)
    {
        'task_id': 'shallows_small_city_silent_buoy',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'silent_buoy_1',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'the_silent_buoy',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'silent_buoy_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'signalwatch_errol',
                    'dialog_id': 'errol_closing'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_small_silent_buoy' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_small_silent_buoy' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_small_silent_buoy'  } },
            {
                'event_type': 'complete_region_quest',
                'params': {
                    'region_id': 'shallows_small_city'
                }
            }
        ]
    },

	# =========================================================
	# TYPE C — Andrea Starveil (extended character, slot 2)
	# Gated by is_chapter_gte: 15
	# Awarded by: shallows_small_city_initialize (conditional)
	# =========================================================

	{
		'task_id': 'shallows_small_city_type_c_find_andrea',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'signalwatch_errol',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'signalwatch_errol',
					'standing_text': [
						"Strange performer came in on the last tide.",
						"Joy that actually means something — in this city.",
						"Sylka knows her."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'signalwatch_errol',
					'dialog_id': 'errol_c_andrea_sighting'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_c_find_andrea' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_small_c_find_andrea'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_shallows_small_c_find_andrea'   } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_small_city_type_c_consult_sylka'
				}
			},
		]
	},
	{
		'task_id': 'shallows_small_city_type_c_consult_sylka',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'runner_sylka',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'runner_sylka',
					'standing_text': [
						"Errol sent you about the performer.",
						"I ran her route in. I can tell you everything."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'runner_sylka',
					'dialog_id': 'sylka_c_andrea_vouch'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_c_consult_sylka' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_small_c_consult_sylka'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_shallows_small_c_consult_sylka'   } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_small_city_type_c_earn_andrea'
				}
			},
		]
	},
	{
		'task_id': 'shallows_small_city_type_c_earn_andrea',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'andrea_starveil',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'andrea_starveil',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'andrea_starveil',
					'standing_text': [
						"The cove has its own rhythm if you listen past the mandate.",
						"Come find me when you're ready to hear it."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'andrea_starveil',
					'dialog_id': 'andrea_c_first_meet'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'andrea_starveil',
					'dialog_id': 'andrea_c_joins'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_c_earn_andrea' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_small_c_earn_andrea' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_shallows_small_c_earn_andrea'   } },
			{
				'event_type': 'hide_npc',
				'params': { 'npc_id': 'andrea_starveil' }
			},
			{
				'event_type': 'character_join',
				'params': { 'character_id': 'andrea_starveil' }
			},
		]
	},

]

# ── Type B ── Ripple / Uul'thar the Tide-Wakened (regional character quest) ───
# Gated by Ch.20 Void Gauntlet. Ripple feels Uul'thar's geometry re-forming
# in the Tidekin Cove shallows — the collapse of Oracle and Reliquary has
# released void-pressure that Uul'thar is absorbing. Creates dungeon in open area.
# No new NPCs — uses initiate_character_dialog on Ripple exclusively.

NPC_DIALOG += [

	{
		'npc_id': 'ripple',
		'dialog_id': 'ripple_b_tide_wrong',
		'dialog': [
			"The tide is wrong.",
			"Not the surface — deeper. The geometry of it.",
			"Uul'thar mapped every tide in these coves before we stopped him.",
			"The void's collapse released something. Pressure. A signal.",
			"He's been absorbing it.",
			"(very quietly) He doesn't surface on his own. Something called him.",
			"We have to go back down. Before he finishes reconstructing."
		]
	},
	{
		'npc_id': 'ripple',
		'dialog_id': 'ripple_b_entering_maw',
		'dialog': [
			"The water remembers him.",
			"Let it. Let it show us where he is.",
			"(steadying herself) I am not afraid of this water.",
			"I just need to keep reminding myself of that."
		]
	},
	{
		'npc_id': 'uulthar',
		'dialog_id': 'uulthar_b_risen',
		'dialog': [
			"The void gave me clarity.",
			"I understand the configuration now. Every tide. Every collapse. Every point of failure.",
			"You are a point of failure.",
			"I will reconfigure you."
		]
	},
	{
		'npc_id': 'ripple',
		'dialog_id': 'ripple_b_victory',
		'dialog': [
			"(long exhale) The tide is right again.",
			"Not the same as before — you can never step in the same tide twice.",
			"But right.",
			"He saw the world as a system to be corrected.",
			"(quietly) Some of us used to think that too.",
			"The difference is we learned to let the tide be what it is."
		]
	},

]

TASKS += [

	# B-0 — Void Gauntlet entry (self-completing gated task)
	{
		'task_id': 'shallows_small_city_b_void_gauntlet',
		'type': 'gated',
		'task_acquire_events': [
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'uulthars_tidal_maw', 'location': 'region_open_area' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_b_tide_wrong' }},
			{ 'event_type': 'complete_task', 'params': { 'task_id': 'shallows_small_city_b_void_gauntlet' }},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'shallows_small_city_b_meet_uulthar' }},
		]
	},

	# B-1 — Meet Uul'thar (boss intro)
	{
		'task_id': 'shallows_small_city_b_meet_uulthar',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'uulthar',
		'task_acquire_events': [
			{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'uulthars_tidal_maw', 'location': 'final_chamber' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_b_entering_maw' }},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'uulthar', 'dialog_id': 'uulthar_b_risen' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique',  'dialog_id': 'chock_shallows_small_b_meet_uulthar'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_shallows_small_b_meet_uulthar' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',   'dialog_id': 'kade_shallows_small_b_meet_uulthar'   } },
			{ 'event_type': 'award_task', 'params': { 'task_id': 'shallows_small_city_b_defeat_uulthar' }},
		]
	},

	# B-2 — Defeat Uul'thar
	{
		'task_id': 'shallows_small_city_b_defeat_uulthar',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'uulthar_b1',
		'task_acquire_events': [
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'uulthar_b1', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique',  'dialog_id': 'chock_shallows_small_b_defeat_uulthar'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_b_victory'                        } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',  'dialog_id': 'kaera_shallows_small_b_defeat_uulthar'  } },
			{ 'event_type': 'complete_regional_quest_2', 'params': { 'region_id': 'shallows' }},
		]
	},

]

# ── Type D ── Tidecaller's Edge (mythic weapon) ───────────────────────────────
# Gate: tidekin_seal from shallows_mid_city (Blackwake Bay, Ch.11) — retroactive.
# Deliver to Diego → Loryth reads the seal → defeat Coveveil Voice → mythic weapon.
# No new NPCs — uses mist_seer_loryth, coveveil_voice, and diego (Ch.1 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'mist_seer_loryth',
		'dialog_id': 'loryth_d_seal_read',
		'dialog': [
			"A Tidekin Seal. I have not seen one surface in this generation.",
			"The Tidekin were the Cove's first wardens — before signal flags, before runners.",
			"They sealed their authority into objects like this when they passed on.",
			"The Coveveil Passage holds the resonance of their final ward.",
			"The seal is calling it forward.",
			"The Voice will not release the Tidekin metal willingly.",
			"But Diego can forge Tidekin iron into something the sea itself cannot blunt."
		]
	},

	{
		'npc_id': 'coveveil_voice',
		'dialog_id': 'coveveil_voice_d_awakens',
		'dialog': [
			"The Tidekin Seal opens what was sealed at their passing.",
			"Every hidden route, every drowned warning, every smuggled secret — I hold them all.",
			"The metal at the Passage's heart was theirs.",
			"You are not Tidekin.",
			"You will not take what they left here."
		]
	},

]

TASKS += [

	# D-0 — Deliver tidekin_seal to Diego (standalone deliver; unlocks D chain)
	{
		'task_id': 'shallows_small_city_type_d_deliver_tidekin_seal',
		'type': 'deliver',
		'item_id': 'shallows_mid_city_e_tidekin_seal',
		'to_type': 'npc',
		'to_id': 'diego',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"That seal — the metal it radiates is unlike anything I've handled.",
						"Old. Dense. Like the sea hardened it deliberately.",
						"Find Loryth. She reads the mist glyphs here.",
						"If anything in this cove knows what that seal unlocks, she does."
					]
				}
			},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_small_d_deliver_tidekin_seal'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_d_deliver_tidekin_seal' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_small_d_deliver_tidekin_seal' } },
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'shallows_mid_city_e_tidekin_seal'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_small_city_type_d_consult_loryth'
				}
			},
		]
	},

	# D-1 — Consult Loryth for the seal reading
	{
		'task_id': 'shallows_small_city_type_d_consult_loryth',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'mist_seer_loryth',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mist_seer_loryth',
					'standing_text': [
						"The mist glyphs changed the moment you arrived.",
						"They are spelling a name I have not read in years.",
						"Tidekin. Come — before the Passage notices what you carry."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'mist_seer_loryth',
					'dialog_id': 'loryth_d_seal_read'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_shallows_small_d_consult_loryth'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_shallows_small_d_consult_loryth' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_shallows_small_d_consult_loryth'   } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_small_city_type_d_meet_coveveil_voice'
				}
			},
		]
	},

	# D-2 — Meet the Coveveil Voice (boss intro)
	{
		'task_id': 'shallows_small_city_type_d_meet_coveveil_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'coveveil_voice',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'coveveil_voice',
					'standing_text': [
						"The Coveveil Passage hums with a resonance deeper than fog.",
						"Sylka says the hidden routes have all gone cold — even the ones she runs blindfolded.",
						"The Tidekin Seal has drawn the Voice to the surface."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'coveveil_voice',
					'dialog_id': 'coveveil_voice_d_awakens'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_shallows_small_d_meet_coveveil_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_shallows_small_d_meet_coveveil_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_shallows_small_d_meet_coveveil_voice' } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_small_city_type_d_defeat_coveveil_voice'
				}
			},
		]
	},

	# D-3 — Defeat the Coveveil Voice; Diego forges the mythic weapon
	{
		'task_id': 'shallows_small_city_type_d_defeat_coveveil_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'coveveil_voice_1',
		'task_acquire_events':[
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'coveveil_voice_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_shallows_small_tidecaller_edge'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_shallows_small_d_defeat_coveveil_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_shallows_small_d_defeat_coveveil_voice'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_shallows_small_d_defeat_coveveil_voice' } },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"Tidekin iron — it doesn't rust, doesn't dull, and it knows where the current is before you do.",
						"I've worked it into the blade.",
						"The sea forged this metal once. I just finished the job."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mist_seer_loryth',
					'standing_text': [
						"The mist glyphs read clearly again.",
						"Every hidden route the Voice sealed has opened.",
						"Sylka says the cove-runners can move freely."
					]
				}
			},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
    'story_id': 'shallows_small_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}