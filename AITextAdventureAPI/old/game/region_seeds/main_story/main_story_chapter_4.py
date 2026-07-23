# ============================================================
# = CHAPTER4 : FRACTURE POINT
# ============================================================
#
# [ NEW CITY — DAWN / STRANGE STILLNESS ]
# -----------------------------------
# @ = player
# V = Velka (occult cartographer)
# D = Drin (street illusionist)
# K = Kirn (magic courier)
# M = Marlo Finch (arcane accountant)
# ? = Disturbance Source
#
# High level: triggers a fracture event that opens two regional dungeons,
# awards the player one Ancient Heirloom, and enables world systems.
# This module defines NPCs, dialogs, and sequenced tasks for that intro.

ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'catalyst',
		'name': 'Catalyst',
		'description': (
			'A destructive, reality-fracturing entity that accelerates collapse wherever it appears.'
			' Its form flickers like a glitch in existence, and its voice comes in broken, layered echoes.'
		),
        "psychology": {
            "mbti": "ENTJ",
            "dominant": "Te — Speaks in commands and inevitabilities. Its presence imposes structure through destruction, forcing reality into collapse.",
            "auxiliary": "Ni — Operates from a singular apocalyptic vision. It sees the end-state of worlds and moves toward it with absolute certainty.",
            "tertiary": "Se — Manifests physically with violent force, bending the environment and overwhelming sensory reality.",
            "inferior": "Fi — Displays distorted, alien echoes of judgment or righteousness, as if mimicking morality without understanding it."
        },
        "enneagram": {
          "enneagram_type": "8w9",
          "core_fear": "Being controlled or harmed by others (in this case, by existence itself).",
          "core_desire": "To be in control of its own destiny, which it defines as accelerating collapse.",
          "defense_mechanism": "Denial — Denies the value of existence, seeing only the 'truth' of its inevitable end. It is an agent of this denial.",
          "stress_line": "Moves to Type 5 — Withdraws into pure concept, becoming a glitch rather than a physical threat.",
          "growth_line": "Moves to Type 2 — (Hypothetically) Would use its power to protect and stabilize reality rather than destroy it.",
          "instinctual_variant": "sx/sp — An intense, focused force of destruction, driven by a singular relationship with the concept of collapse."
        },
        'image': 'bosses:catalyst1'
	},
	{
		'npc_id': 'velka',
		'name': 'Velka, Occult Cartographer',
		'description': (
			'An enigmatic mapmaker who charts tears in reality and reads the patterns hidden between lines.'
		),
        "psychology": {
            "mbti": "INTJ",
            "dominant": "Ni — Sees shifting patterns in maps, ley lines, and reality fractures. Interprets meaning where others see chaos.",
            "auxiliary": "Te — Communicates concisely, directing the player toward the next logical step in the investigation.",
            "tertiary": "Fi — Holds quiet personal convictions about the nature of reality and her duty to chart it.",
            "inferior": "Se — Overwhelmed by sudden distortions or sensory anomalies; prefers controlled environments."
        },
        "enneagram": {
          "enneagram_type": "5w4",
          "core_fear": "Being helpless, incapable, or overwhelmed by a world she cannot understand.",
          "core_desire": "To be capable and competent by understanding the world's hidden rules.",
          "defense_mechanism": "Isolation — Detaches from the chaos to observe and map it, finding safety in knowledge rather than participation.",
          "stress_line": "Moves to Type 7 — Becomes scattered and anxious when the patterns become too chaotic to map.",
          "growth_line": "Moves to Type 8 — Uses her knowledge to take decisive action and influence reality, not just chart it.",
          "instinctual_variant": "sp/sx — Hoards knowledge for her own security, engaging intensely with the mystery of the world's collapse."
        },
        'image': 'npcs:velka1'
	},
	{
		'npc_id': 'drin',
		'name': 'Drin the Illusionist',
		'description': (
			'A street performer who twists perception for coin — quick with a joke and quicker with a disappearing act.'
		),
        "psychology": {
            "mbti": "ENTP",
            "dominant": "Ne — Constantly plays with perception, possibilities, and tricks. His illusions are extensions of his imagination.",
            "auxiliary": "Ti — Analyzes how illusions work and why they’re malfunctioning. His humor hides a sharp, logical mind.",
            "tertiary": "Fe — Uses charm and theatrics to engage crowds or deflect fear.",
            "inferior": "Si — When illusions turn real, he panics; the loss of control triggers fixation on past failures."
        },
        "enneagram": {
          "enneagram_type": "7w6",
          "core_fear": "Being trapped in a reality he can't control or escape.",
          "core_desire": "To stay free and entertained, avoiding the scary, real parts of life.",
          "defense_mechanism": "Rationalization — Treats the world's collapse as just another illusion or a big joke to avoid his own terror.",
          "stress_line": "Moves to Type 1 — Becomes rigid and anxious when his tricks fail and reality becomes too real.",
          "growth_line": "Moves to Type 5 — Becomes more focused and begins to understand the real mechanics behind the 'illusions'.",
          "instinctual_variant": "so/sp — A social performer who uses his wit to entertain and secure his place, but is ultimately focused on his own escape."
        },
        'image': 'npcs:drin1'
	},
	{
		'npc_id': 'kirn',
		'name': 'Kirn, Magic Courier',
		'description': (
			'A courier who delivers arcane reports and knows every back alley in the city.'
		),
        "psychology": {
            "mbti": "ESFJ",
            "dominant": "Fe — Warm, expressive, and people‑focused. She tries to help even when scared.",
            "auxiliary": "Si — Relies on familiar routes and routines; reality warping terrifies her because it breaks her internal map.",
            "tertiary": "Ne — When stressed, she imagines bizarre possibilities or jumps to dramatic conclusions.",
            "inferior": "Ti — Overthinks or becomes rigid when forced to analyze magical anomalies."
        },
        "enneagram": {
          "enneagram_type": "6w7",
          "core_fear": "Being without support or guidance in a dangerous world.",
          "core_desire": "To have security and support.",
          "defense_mechanism": "Projection — Offloads her fear onto the 'dangerous' bracelet, seeking help from others to feel safe.",
          "stress_line": "Moves to Type 3 — Becomes frantic and image-focused, trying to appear competent while panicking internally.",
          "growth_line": "Moves to Type 9 — Becomes more trusting and calm, able to handle uncertainty without needing constant reassurance.",
          "instinctual_variant": "so/sp — Seeks security through her social network and by being a reliable, helpful member of the community."
        },
        'image': 'npcs:kirn1'
	},
	{
		'npc_id': 'marlo_finch',
		'name': 'Marlo Finch',
		'description': (
			'An arcane accountant who tracks fluctuations in world-stability like ledgers of misfortune.'
		),
        "psychology": {
            "mbti": "ISTJ",
            "dominant": "Si — Catalogs anomalies, tracks patterns, and maintains strict internal order. Treats reality like a ledger.",
            "auxiliary": "Te — Efficient, blunt, and procedural. He confiscates dangerous items without hesitation.",
            "tertiary": "Fi — Holds a quiet sense of duty and moral responsibility to protect the world from collapse.",
            "inferior": "Ne — Overwhelmed by unpredictable rifts or chaotic magic; becomes irritable or overly cautious."
        },
        "enneagram": {
          "enneagram_type": "1w9",
          "core_fear": "The world (and his ledger) being chaotic, wrong, or out of balance.",
          "core_desire": "To have order, integrity, and balance.",
          "defense_mechanism": "Reaction Formation — Channels his anxiety about the world's collapse into a rigid, methodical process of auditing and correcting anomalies.",
          "stress_line": "Moves to Type 4 — Becomes withdrawn and melancholic when faced with a reality too broken to audit.",
          "growth_line": "Moves to Type 7 — Becomes more flexible and able to appreciate the world beyond his ledgers.",
          "instinctual_variant": "sp/so — His self-preservation is tied to maintaining order in the world around him; a balanced ledger means a safe world."
        },
        'image': 'npcs:marlo_finch1'
	}
]

NPC_DIALOG = [
    {
        'npc_id': None,
        'dialog_id': 'narrator_intro_chapter_4',
        'dialog': [
            "Chapter 4 - Some things only become real the moment they break."
        ]
    },
    ###############################################
    # VELKA — Intro (Inn)
    ###############################################
    {
        'npc_id': 'velka',
        'dialog_id': 'velka_ch4_intro',
        'dialog': [
            "The maps are wrong. They’re shifting under my hands.",
            "Arcane lines are rewriting themselves — something is twisting the city’s shape.",
            "You should talk to Drin.  I heard him telling stories of his illusions becoming real.",
            "Normally I would just laugh at the though of a street illusion con artist suddenly being shocked by his illusions manifesting...",
            "...but if it’s true, then that’s a whole new level of weird.  You can find him in the bar."
        ]
    },

    ###############################################
    # Player reactions to Velka
    ###############################################
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch4_after_velka',
        'dialog': [
            "If the maps are fighting back, something’s provoking them.",
            "Let’s move. I want to see what’s bending reality."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch4_after_velka',
        'dialog': [
            "A disturbance like this… it feels alive.",
            "We should hurry. The city is calling for help."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch4_after_velka',
        'dialog': [
            "Great. Reality’s glitching again.",
            "Let’s go before the whole place desyncs."
        ]
    },

    ###############################################
    # DRIN — Illusion Distortion (Bar)
    ###############################################
    {
        'npc_id': 'drin',
        'dialog_id': 'drin_ch4_intro',
        'dialog': [
            "You feel that? The air’s got edges.",
            "My illusions are acting on their own, becoming real without my say‑so.",
            "It happened when Kirn showed up with that strange bracelet.",
            "I don’t know what it is, but it’s warping reality around her. She’s hanging out at the ₨, you should check it out."
        ]
    },

    ###############################################
    # KIRN — The Bracelet of Void (Shop Items)
    ###############################################
    {
        'npc_id': 'kirn',
        'dialog_id': 'kirn_ch4_intro',
        'dialog': [
            "Holy smokes you scared me for a second there.  You’re not from around here, are you?",
            "I’m Kirn. I deliver things.  I know every nook and cranny of this city, but I’ve been trying to steer clear of the open areas lately.",
            "I picked up a delivery route that shouldn’t exist — streets folding into each other.",
            "This bracelet… it warped reality around me. I’m not keeping it.",
            "I don’t know where it came from, but it’s been messing with the places I go.",
            "Here, take it. I'm not couriering this thing anymore."
        ]
    },

    ###############################################
    # FINAL CHARACTER — Inside the Rift - each character needs a dialog here as any of them could be the final_character
    ###############################################
    {
        'npc_id': 'technique',
        'dialog_id': 'final_character_ch4_intro',
        'dialog': [
            "You… I know your faces. Or I should.",
            "The rift dragged me in, but it didn’t take my strength, just my direction.",
            "If you’re here, then I’m not alone. I’ll fight with you."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'final_character_ch4_join',
        'dialog': [
            "I’m ready. Whatever’s tearing this place apart... We end it together."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'final_character_ch4_intro',
        'dialog': [
            "This rift… it’s pulling at something deep inside me.",
            "But I remember you. We fought together once, didn’t we?",
            "If we’re both trapped here, then we’ll need to rely on each other."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'final_character_ch4_join',
        'dialog': [
            "I can feel the rift’s pull, but I won’t let it consume me. Not while we stand together."
        ]
    },
    {
    'npc_id': 'skill',
        'dialog_id': 'final_character_ch4_intro',
        'dialog': [
            "One moment I was deep in meditation, the next I am here.",
            "The air itself feels… misaligned. Every instinct is telling me this place shouldn’t exist.",
            "But your presence steadies me. If the rift wants to test us, then I’ll meet it with precision."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'final_character_ch4_join',
        'dialog': [
            "My focus is clear now. Lead the way — I’ll strike where it counts."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'final_character_ch4_intro',
        'dialog': [
            "The rift’s energy is… familiar, yet wrong. It echoes spells I’ve never cast.",
            "I felt your signatures before I saw you — threads of fate pulling us back together.",
            "If this place bends the arcane, then we’ll bend it back."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'final_character_ch4_join',
        'dialog': [
            "Good. With our magic aligned, the rift won’t stand a chance."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'final_character_ch4_intro',
        'dialog': [
            "Okay, this is… not any dimension I’ve charted.",
            "My instruments fried the moment I crossed the threshold, but your signals cut through the static.",
            "If you’re here, then we can stabilize this together — or at least stop it from getting worse."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'final_character_ch4_join',
        'dialog': [
            "Systems online. Let’s crack this rift open and shut it down properly."
        ]
    },
    ###############################################
    # CATALYST — Rift Boss Intro
    ###############################################
    {
        'npc_id': 'catalyst',
        'dialog_id': 'catalyst_ch4_intro',
        'dialog': [
            "This fracture remembers what your world has forgotten.",
            "Order. Silence. Eternity.",
            "I am the Catalyst. The fracture’s herald and harbinger.",
            "You cannot stop the collapse, but you can beg for a swift end."
        ]
    },
    ##################### RIFT EVENT SECTION #####################
    ## Narrative of the world shaking and trembling.
    ## characters engage in conversation about the very earth shaking based on personalities
    ############################################################
    {
        'npc_id': None,
        'dialog_id': 'catalyst_defeated_world_shaking_event',
        'dialog': [
            "As Catalyst falls, the very ground trembles violently, sending dark shockwaves through the ground.",
            "The air fills with a deafening roar as reality itself seems to scream in agony.",            
            "The air darkens as a swirling maelstrom of energy erupts, sending you spiraling through space-void."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch4_after_rift',
        'dialog': [
            "The world is shaking! I can feel it in my bones!"
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch4_after_rift',
        'dialog': [ #spiritual kind
            "I can feel something different now.  The world HAS changed... It feels ... bigger!"
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch4_after_rift',
        'dialog': [
            "The energy that poured out when Catalyst fell... it's unlike anything I've ever felt.",
            "It's as if the very fabric of reality had been torn open, and came pouring out."
        ]
    },

    ###############################################
    # MARLO FINCH — Post‑Rift Confiscation
    ###############################################
    {
        'npc_id': 'marlo_finch',
        'dialog_id': 'marlo_finch_ch4_after_rift',
        'dialog': [
	        "Hey hold up a second there, I'm Marlo Finch.  Arcane Auditor to the Grand Council.",
	        "That bracelet you've been carrying...  That bracelet is a ledger of collapse, I’m going to need to audit it before it unravels reality.",
	        "After you took it from Kirn she told me what happened.  How you dissapeared into a rift, then not long after, the rift collapsed and shook the whole city.",
	        "Waters rose where there were none before.  The world is changed.  I need to take that bracelet off your hands and examine it before it causes any more damage.",
	        "This little thing has opened rifts in nearby wilds surrounding many cities.",
            "Kirn said he got it from Mira.",
            "Go back to Mira and find out what you can about it. There will be a reward if you manage to track it down."
        ]
    },
    {
        'npc_id': 'marlo_finch',
        'dialog_id': 'marlo_finch_ch4_after_rift_2',
        'dialog': [
            "This little thing has opened rifts in nearby wilds surrounding many cities.",
            "You should make a point of checking the µ of wilds surrounding cities.  There are local hero's up to the challenge of helping you out.  One of these rifts may help you find a way home.",
            "In any case, while you are here, I need you to help me find the Bracelet of Existence, the other half of this nasty thing.",
            "Go back to Mira and find out where the other bracelet went.  These things need to be put back together."
        ]
    },

    ###############################################
    # Mira — Outro
    ###############################################
    {
        'npc_id': 'mira',
        'dialog_id': 'mira_ch4_outro',
        'dialog': [
            "You say Marlo Finch confiscated the Bracelet of Void and is now looking for the Bracelet of Existence?",
            "I split that couplet in two... But you're gonna have to track the other one down yourself, I don't sell out my buyers.",
            "I haven't had it for days.  You should visit Kirn again, he might be able to dig up information on the courier that carried it."
        ]
    },

    ############################################################
    # Kess — After receiving Rift Dust
    ############################################################
    {
        'npc_id': 'kess_thornwrite',
        'dialog_id': 'kess_ch4_after_rift_dust',
        'dialog': [
            "Ooooh! Rift Dust! Now *this* is the good stuff.",
            "You can practically taste the dimensional instability… don’t actually taste it though.",
            "Give me a moment — I know exactly what to make with this.",
            "*He mixes, shakes, ignites, and grins far too wide.*",
            "Here! A Boreal Clasp. Stabilizes the body when reality gets wobbly."
        ]
    },

    ############################################################
    # Mira — After receiving Unstable Relic
    ############################################################
    {
        'npc_id': 'mira',
        'dialog_id': 'mira_ch4_after_unstable_relic',
        'dialog': [
            "Well now… this is a dangerous little treasure.",
            "Unstable, humming, and probably illegal in three different dimensions.",
            "Exactly my kind of artifact.",
            "Here — take this Mirethread Pendant.",
            "It’s woven from the same kind of energy. Should keep you from unraveling."
        ]
    }
]

TASKS = [

    ###############################################################
    # TASK 1 — MEET VELKA (Inn)
    ###############################################################
    {
        'task_id': 'main_story_ch4_meet_velka',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'velka',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'velka', 'location': 'region_city_inn' } },
			{
				'event_type': 'set_npc_met',
				'params': {
					'npc_id': 'velka'
				}
			},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'drin', 'location': 'region_city_bar' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'drin', 'standing_text': [
                        "Reality’s been acting weird lately.",
                        "I don’t know what’s going on, but it’s freaking me out."
                    ]
                }
            },
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'kirn', 'location': 'region_city_shopitems' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'kirn', 'standing_text': [
                        "I’ve been trying to avoid the open areas.  Something’s been warping reality around me.",
                        "I don’t know what it is, but it’s been messing with the places I go."
                    ]
                }
            },
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'marlo_finch', 'location': 'region_city_other1' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'marlo_finch', 'standing_text': [
                        "You look like you’ve been through a lot.  If you need help navigating the city, I’m your guy.",
                        "I keep track of all the weird happenings around here.  If something’s going on, I probably know about it."
                    ]
                }
            }
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'velka', 'dialog_id': 'velka_ch4_intro' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch4_after_velka' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch4_after_velka' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch4_after_velka' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'velka', 'standing_text': [
                "Drin felt the distortion first.",
                "Find him in the bar."
            ]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch4_meet_drin' } }
        ]
    },

    ###############################################################
    # TASK 2 — MEET DRIN (Bar)
    ###############################################################
    {
        'task_id': 'main_story_ch4_meet_drin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'drin',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'drin', 'dialog_id': 'drin_ch4_intro' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'drin', 'standing_text': [
                "Kirn’s carrying something dangerous.",
                "Find her in the shop."
            ]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch4_meet_kirn' } }
        ]
    },

    ###############################################################
    # TASK 3 — MEET KIRN (Shop Items)
    ###############################################################
    {
        'task_id': 'main_story_ch4_meet_kirn',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'kirn',
        'task_acquire_events': [],
        'task_complete_events': [

            # Kirn dialog
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'kirn', 'dialog_id': 'kirn_ch4_intro' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'kirn', 'standing_text': [
                        "I don’t know where this bracelet came from, but it’s been messing with the places I go.",
                        "Here, take it. I'm not couriering this thing anymore."
                    ]
                }
            },
            # Kirn gives bracelet
            { 'event_type': 'award_item', 'params': { 'item_id': 'bracelet_of_void', 'quantity': 1 } },

            # Rift triggers immediately
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'catalyst',
                    'location': None
                }
            },
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'final_character', 'location': None } },
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'rift_dungeon_ch4', 'location': 'region_city_open_area' } },
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'rift_dungeon_ch4', 'item_id': 'rift_dust', 'location': 'treasure_room'}},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'rift_dungeon_ch4', 'item_id': 'unstable_relic', 'location': 'treasure_room'}},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'rift_dungeon_ch4', 'item_id': 'phase_crystal', 'location': 'treasure_room'}},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'rift_dungeon_ch4', 'item_id': 'rift_core', 'location': 'treasure_room'}},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'rift_dungeon_ch4', 'item_id': 'mountains_large_city_armor_key', 'location': 'treasure_room'}},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'rift_dungeon_ch4', 'item_id': 'necropolis_marrow_shard', 'location': 'treasure_room'}},
            { 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'rift_dungeon_ch4', 'location': 'entrance' } },

            # Final Character appears inside rift
            { 'event_type': 'dungeon_add_npc', 'params': {
                'dungeon_id': 'rift_dungeon_ch4',
                'npc_id': 'final_character',
                'location': 'corridor'
            }},

            # Award next task
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch4_meet_final_character' } },
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch4_meet_catalyst' } }
        ]
    },

    ###############################################################
    # TASK 4 — MEET FINAL CHARACTER (Inside Rift)
    ###############################################################
    {
        'task_id': 'main_story_ch4_meet_final_character',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'final_character',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'final_character', 'dialog_id': 'final_character_ch4_intro' } },
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'final_character'} },
            { 'event_type': 'player_character_join', 'params': { 'dialog_id': 'final_character_ch4_join', 'is_final_character': True } }
        ]
    },

    ###############################################################
    # TASK 5 — MEET CATALYST (Dungeon Boss Intro)
    ###############################################################
    {
        'task_id': 'main_story_ch4_meet_catalyst',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'catalyst',
        'task_acquire_events': [

        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'catalyst', 'dialog_id': 'catalyst_ch4_intro' } },
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch4_defeat_catalyst' } }
        ]
    },

    ###############################################################
    # TASK 6 — DEFEAT CATALYST (Boss Fight)
    ###############################################################
    {
        'task_id': 'main_story_ch4_defeat_catalyst',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'catalyst_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'catalyst_1', 'combat_type': 'boss_battle' } }
        ],
        'task_complete_events': [                        
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'catalyst'} },
            { 'event_type': 'remove_player_from_dungeon', 'params': { 'dungeon_id': 'rift_dungeon_ch4' } },
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch4_meet_marlo_finch_after_rift' } },
            { 'event_type': 'complete_intro_story' },
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'catalyst_defeated_world_shaking_event' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch4_after_rift' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch4_after_rift' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch4_after_rift' } }
        ]
    },

    ###############################################################
    # TASK 7 — POST‑RIFT: MEET MARLO FINCH
    ###############################################################
    {
        'task_id': 'main_story_ch4_meet_marlo_finch_after_rift',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'marlo_finch',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch4_after_rift' } },
            { 'event_type': 'remove_item', 'params': { 'item_id': 'bracelet_of_void' } },
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch4_after_rift_2' } },
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch4_return_to_mira' } },

        ]
    },

    ###############################################################
    # TASK 8 — RETURN TO VELKA (Outro)
    ###############################################################
    {
        'task_id': 'main_story_ch4_return_to_mira',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'mira',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'mira', 'dialog_id': 'mira_ch4_outro' } },
            { 'event_type': 'award_task', 'params': { 'task_id': 'ch4_deliver_rift_dust_to_kess' } },
            { 'event_type': 'award_task', 'params': { 'task_id': 'ch4_deliver_unstable_relic_to_mira' } },
            { 'event_type': 'advance_chapter' }
        ]
    },
    ############################################################
    # CH4 SIDE DELIVERY — Deliver Rift Dust to Kess
    ############################################################
    {
        'task_id': 'ch4_deliver_rift_dust_to_kess',
        'type': 'deliver',
        'item_id': 'rift_dust',
        'to_type': 'npc',
        'to_id': 'kess_thornwrite',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'kess_thornwrite',
                    'dialog_id': 'kess_ch4_after_rift_dust'
                }
            },
            {
                'event_type': 'remove_item',
                'params': {
                    'item_id': 'rift_dust'
                }
            },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'boreal_clasp',
                    'quantity': 1
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'kess_thornwrite',
                    'standing_text': [
                        "If you find more rift‑touched materials, bring them my way.",
                        "Reality‑bending reagents are my specialty."
                    ]
                }
            }
        ]
    },

    ############################################################
    # CH4 SIDE DELIVERY — Deliver Unstable Relic to Mira
    ############################################################
    {
        'task_id': 'ch4_deliver_unstable_relic_to_mira',
        'type': 'deliver',
        'item_id': 'unstable_relic',
        'to_type': 'npc',
        'to_id': 'mira',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'mira',
                    'dialog_id': 'mira_ch4_after_unstable_relic'
                }
            },
            {
                'event_type': 'remove_item',
                'params': {
                    'item_id': 'unstable_relic'
                }
            },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'mirethread_pendant',
                    'quantity': 1
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'mira',
                    'standing_text': [
                        "If you come across more relics like that, don’t hesitate.",
                        "I always pay well for dangerous curios."
                    ]
                }
            }
        ]
    }

]

PRIMARY_STORY_SETTINGS = {
	'chapter_id': 'main_story_chapter_4',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}
