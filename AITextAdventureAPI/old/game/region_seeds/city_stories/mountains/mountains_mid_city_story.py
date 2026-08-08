ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'warden_harrock',
		'name': 'Harrock the Cliff‑Warden',
		'description': (
			'A stoic guardian who ensures travelers survive the treacherous paths.'
			' Harrock\'s voice carries like distant thunder across the cliffs.'
			' He has an uncanny sense for impending rockslides.'
		),
		"image": "mountains_mid:warden_harrock1",
		"psychology": {
			"mbti": "ISTJ",
			"dominant": "Si — Has memorized the cliffs' every creak, shift, and warning sign through years of vigilant watch.",
			"auxiliary": "Te — Responds to rockfall threats with immediate, organized directives.",
			"tertiary": "Fi — Carries private grief for every traveler he could not warn in time.",
			"inferior": "Ne — Struggles when the rockslides stop following any pattern he recognizes."
		},
		"enneagram": {
			"enneagram_type": "6w5",
			"core_fear": "A traveler dying on a path he was supposed to be watching.",
			"core_desire": "To make every route through the cliffs as safe as stone and vigilance can make it.",
			"defense_mechanism": "Projection — Attributes every unusual rockfall to an identifiable external cause to maintain the illusion of control.",
			"stress_line": "Moves to Type 3 — Becomes performatively authoritative when the Shatterpeak Core shakes his competence.",
			"growth_line": "Moves to Type 9 — Accepts that some falls cannot be stopped, and guides others around them instead.",
			"instinctual_variant": "so/sp — Warden duty as the ultimate expression of community responsibility."
		}
	},
	{
		'npc_id': 'emberguide_ryla',
		'name': 'Ryla Emberguide',
		'description': (
			'A fire‑touched wanderer who teaches survival through controlled flame.'
			' Ryla\'s campfires burn with unnatural colors, shifting with her mood.'
			' She believes every ember remembers the mountain\'s ancient fury.'
		),
		"image": "mountains_mid:emberguide_ryla1",
		"psychology": {
			"mbti": "ENFP",
			"dominant": "Ne — Reads the mountain's anger through the language of flame; every color is a word.",
			"auxiliary": "Fi — Teaches through emotional resonance; her students survive because they feel the fire, not just obey it.",
			"tertiary": "Te — Applies structured fire-control techniques when lives are immediately at stake.",
			"inferior": "Si — The Emberwake's colours are new; her accumulated fire-memory doesn't have a name for what she's seeing."
		},
		"enneagram": {
			"enneagram_type": "4w3",
			"core_fear": "The mountain's fire turning on those she guided to trust it.",
			"core_desire": "For the ember to be a teacher, not a destroyer.",
			"defense_mechanism": "Introjection — Has absorbed the mountain's fury into her identity; she understands it because she has become it.",
			"stress_line": "Moves to Type 2 — Becomes desperate to be the one who saves everyone when the flame turns hostile.",
			"growth_line": "Moves to Type 1 — Channels her fire-touch into disciplined, principled teaching.",
			"instinctual_variant": "sx/sp — Intensity first; bonds forged in survival fire are the deepest she knows."
		}
	},
	{
		'npc_id': 'avalanche_seer_korrin',
		'name': 'Korrin the Avalanche‑Seer',
		'description': (
			'A hermit who reads fall‑lines and predicts collapses. '
			'Korrin senses disturbances in the mountain\'s pressure and stone.'
		),
		"image": "mountains_mid:avalanche_seer_korrin1",
		"psychology": {
			"mbti": "INTP",
			"dominant": "Ti — Reads fall-line geometry as a precise internal model; predictions are calculations, not intuitions.",
			"auxiliary": "Ne — Connects pressure-pattern variations across vast distances to identify the source of disturbance.",
			"tertiary": "Si — Decades of fall-lines memorized; the mountain's past collapses are the dataset he works from.",
			"inferior": "Fe — Cannot easily express urgency in terms others will respond to in time."
		},
		"enneagram": {
			"enneagram_type": "5w4",
			"core_fear": "An avalanche he predicted incorrectly — or failed to predict at all.",
			"core_desire": "A complete, accurate model of the mountain's collapse behaviour.",
			"defense_mechanism": "Isolation — Retreats into the peaks when his predictions are ignored.",
			"stress_line": "Moves to Type 7 — Becomes scattered and restless when the Shatterpeak Core defies every model.",
			"growth_line": "Moves to Type 8 — Leads the party decisively when the collapse is imminent and only he can read it.",
			"instinctual_variant": "sp/sx — Hermitic precision; bonds only with those willing to trust numbers over instinct."
		}
	},
	{
		'npc_id': 'fallshadow_echo',
		'name': 'Fallshadow Echo',
		'description': (
			'A spectral remnant of ancient rockslides, awakened by the Shatterpeak Core.'
		),
		"image": "mountains_mid:fallshadow_echo1",
		"psychology": {
			"mbti": "ISTP",
			"dominant": "Ti — Moves with the precise, inevitable logic of falling stone; every trajectory is calculated.",
			"auxiliary": "Se — Exists entirely in the kinetic present of descent and impact.",
			"tertiary": "Ni — Has a dim awareness of where it was heading before the original collapse.",
			"inferior": "Fe — No sense of who is in the path; obstruction is simply a variable in the fall."
		},
		"enneagram": {
			"enneagram_type": "8w9",
			"core_fear": "Being stopped — the fall arrested before completion.",
			"core_desire": "To complete the collapse the original rockslide began.",
			"defense_mechanism": "Denial — Cannot acknowledge that the original collapse already resolved; it loops in perpetual mid-fall.",
			"stress_line": "Moves to Type 5 — Becomes cold and methodical when obstacles repeatedly interrupt the trajectory.",
			"growth_line": "Moves to Type 2 — Dissipates peacefully when the Shatterpeak Core is resolved and the fall is finally over.",
			"instinctual_variant": "sp/so — The momentum of the old herd-collapse; it runs because stone once ran together."
		}
	},
	{
		'npc_id': 'emberwake_spirit',
		'name': 'Emberwake Spirit',
		'description': (
			'A fiery apparition formed from unstable heat deep within the Emberwake Cavern.'
		),
		"image": "mountains_mid:emberwake_spirit1",
		"psychology": {
			"mbti": "ENFP",
			"dominant": "Ne — Surges in every direction at once; its fire is possibility without constraint.",
			"auxiliary": "Fi — Burns with the raw, accumulated fury of every eruption the cavern has ever suppressed.",
			"tertiary": "Te — Channels heat into focused, devastating bursts when challenged.",
			"inferior": "Si — Has no memory of a time before the heat; cannot conceive of cooling."
		},
		"enneagram": {
			"enneagram_type": "7w8",
			"core_fear": "Cooling — the end of fire is the end of self.",
			"core_desire": "To burn without limit and wake every dormant forge in the mountain.",
			"defense_mechanism": "Rationalization — Destruction is simply heat finding its level.",
			"stress_line": "Moves to Type 1 — Becomes laser-focused and devastating when its expansion is blocked.",
			"growth_line": "Moves to Type 5 — Settles into a steady, sustainable heat when the Emberwake Core is resolved.",
			"instinctual_variant": "sx/sp — Pure intensity of flame; it exists most fully at the moment of ignition."
		}
	}
]


NPC_DIALOG = [

	{
		'npc_id': 'warden_harrock',
		'dialog_id': 'harrock_intro',
		'dialog': [
			"The cliffs rumble without warning.",
			"Rockfalls strike where the paths were once safe.",
			"Something beneath the mountain shifts in its sleep."
		]
	},
	{
		'npc_id': 'emberguide_ryla',
		'dialog_id': 'ryla_intro',
		'dialog': [
			"My flames burn in colors I've never seen.",
			"The mountain's fury stirs in the embers.",
			"If it wakes fully, the cliffs will tear themselves apart."
		]
	},
	{
		'npc_id': 'avalanche_seer_korrin',
		'dialog_id': 'korrin_intro',
		'dialog': [
			"The fall‑lines tremble with warning.",
			"A Core awakens — pressure, flame, and stone given will.",
			"If it rises, the whole range will collapse."
		]
	},
	{
		'npc_id': 'fallshadow_echo',
		'dialog_id': 'fallshadow_echo_intro',
		'dialog': [
			"We are the echoes of old collapses.",
			"The Core calls the cliffs to fall again.",
			"It waits deeper in the Emberwake Cavern."
		]
	},
	{
		'npc_id': 'emberwake_spirit',
		'dialog_id': 'emberwake_spirit_intro',
		'dialog': [
			"The Cavern burns with ancient fury.",
			"The Core gathers strength.",
			"Only its heart remains to be stilled."
		]
	},
	{
		'npc_id': 'warden_harrock',
		'dialog_id': 'harrock_closing',
		'dialog': [
			"The cliffs quiet. The paths are safe again.",
			"You've stilled a force older than the mountain winds.",
			"Travelers will owe you their lives for generations."
		]
	},

]


TASKS = [
	{
		'task_id': 'mountains_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'warden_harrock',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'warden_harrock',
					'standing_text': [
						"The cliffs hum with memory—if you've a story of survival, I'll listen."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'emberguide_ryla',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'emberguide_ryla',
					'standing_text': [
						"Share a flame and a tale—our fires remember the names of brave travelers."
					]
				}
			},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_mid_city_regional_complete_gate' } }
		]
	},
	{
		'task_id': 'mountains_mid_city_regional_complete_gate',
		'type': 'complete_regional_quests',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_mid_city_type_c_find_korina' } },
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_mid_city_type_d_deliver_forge_core' } },
		]

	},
]


# ── Type C ── Korina Brightvein (extended character) ──────────────────────────
# Gated by is_chapter_gte: 17. Korina has been rallying demoralized survivors
# along the Gallows Rift passes. Harrock's word opens her trust — she won't
# follow anyone who doesn't have a local warden's confidence.

NPC_DIALOG += [

	{
		'npc_id': 'korina_brightvein',
		'dialog_id': 'korina_c_first_meet',
		'dialog': [
			"The Rift passes are full of people who've given up.",
			"I've been moving from camp to camp pulling them back.",
			"You carry yourselves differently.",
			"Like people who still believe something is worth fighting for.",
			"I need to hear a local warden say you're worth following before I sign on.",
			"Trust is the only currency that holds value up here."
		]
	},

	{
		'npc_id': 'warden_harrock',
		'dialog_id': 'harrock_c_vouch',
		'dialog': [
			"Korina kept three separate survivor camps from falling apart last season.",
			"She didn't use authority — she used belief.",
			"Tell her I said the Rift paths are safer when your party walks them.",
			"She'll know what that means."
		]
	},

	{
		'npc_id': 'korina_brightvein',
		'dialog_id': 'korina_c_joins',
		'dialog': [
			"Harrock says the Rift paths are safer when you walk them.",
			"He's never said that about anyone.",
			"Then I'm with you.",
			"Fair warning — I will push everyone on this team to be better.",
			"Including you.",
			"Especially you."
		]
	},

]

# --- Character dialogs: Type C ---
NPC_DIALOG += [

    # Type C – Find Korina
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_mountains_mid_c_find_korina',
        'dialog': [
            "She's been pulling survivor camps back together with belief instead of authority. Rare skill up here."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_mountains_mid_c_find_korina',
        'dialog': [
            "Trust is the only currency that holds value on the Rift passes. She wants a local warden to vouch first."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_mountains_mid_c_find_korina',
        'dialog': [
            "Fair. Harrock's word carries weight on these cliffs."
        ]
    },

    # Type C – Consult Harrock
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_mountains_mid_c_consult_harrock',
        'dialog': [
            "She kept three separate camps from falling apart last season. She didn't use rank — she used belief."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_mid_c_consult_harrock',
        'dialog': [
            "Tell her the Rift paths are safer when we walk them. She'll know what that means."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_mountains_mid_c_consult_harrock',
        'dialog': [
            "Harrock doesn't say that about just anyone. That's the endorsement she needs."
        ]
    },

    # Type C – Earn Korina
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_mountains_mid_c_earn_korina',
        'dialog': [
            "He's never said that about anyone. She's in."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_mountains_mid_c_earn_korina',
        'dialog': [
            "Fair warning — she will push everyone on this team to be better. Including us."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_mountains_mid_c_earn_korina',
        'dialog': [
            "Especially us. Good. We could use the pressure."
        ]
    },

]

# --- Character dialogs: Type D ---
NPC_DIALOG += [

	# Type D – Deliver Forge Core
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_mountains_mid_d_deliver_forge_core',
		'dialog': [
			"The forge-pressure inside it is still active. Something in the Gallows Rift resonates with this exact frequency."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_mountains_mid_d_deliver_forge_core',
		'dialog': [
			"Korrin reads fall-lines and mountain pressure. He'll know what the core is calling to."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_mountains_mid_d_deliver_forge_core',
		'dialog': [
			"I already want to see what surfaces when we present it."
		]
	},

    # Type D – Consult Korrin
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_mid_d_consult_korrin',
        'dialog': [
            "The pressure signature matches the Emberwake Cavern almost exactly. The Spirit has been drawing heat from Ryla's fires for years."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grmnaw_mountains_mid_d_consult_korrin',
        'dialog': [
            "Present the Core and it will surface for the frequency it's been feeding on. Clean."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_mountains_mid_d_consult_korrin',
        'dialog': [
            "Silence it and the forge-pressure crystallizes. Brawn can work with that."
        ]
    },

    # Type D – Meet Emberwake Spirit
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_mountains_mid_d_meet_emberwake_spirit',
        'dialog': [
            "It already decided the pressure is its and we will not leave with it."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_mountains_mid_d_meet_emberwake_spirit',
        'dialog': [
            "Ironveil's foundry frequency walking into its domain. It's been waiting a long time for this."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_mountains_mid_d_meet_emberwake_spirit',
        'dialog': [
            "Some spirits only know how to hold what the mountain once burned. We take it back."
        ]
    },

    # Type D – Defeat Emberwake Spirit
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_mountains_mid_d_defeat_emberwake_spirit',
        'dialog': [
            "It's down. Take the forge-pressure crystal."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_mid_d_defeat_emberwake_spirit',
        'dialog': [
            "Armor that compresses under impact and rebounds harder. The harder you're hit, the stronger it holds."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_mountains_mid_d_defeat_emberwake_spirit',
        'dialog': [
            "The fall-lines are clear. Ryla's fires burn in the right colors again."
        ]
    },

]

# --- Character dialogs: Type B ---
NPC_DIALOG += [

    # B – Meet Rokhuld
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_mountains_mid_b_meet_rokhuld',
        'dialog': [
            "He's deeper than before. The void fed something in him."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_mountains_mid_b_meet_rokhuld',
        'dialog': [
            "Don't let him monologue. He gets worse the longer he talks."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_mountains_mid_b_meet_rokhuld',
        'dialog': [
            "He still thinks breaking the core is righteous. We end the argument today."
        ]
    },

	# B – Defeat Rokhuld
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_mountains_mid_b_defeat_rokhuld',
		'dialog': [
			"Stay down. The mountain doesn't need another crusade."
		]
	},
	{
		'npc_id': 'bragg',
		'dialog_id': 'bragg_mountains_mid_b_defeat_rokhuld',
		'dialog': [
			"We were both just afraid. The mountain's still standing. That's what matters."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_mountains_mid_b_defeat_rokhuld',
		'dialog': [
			"Some callings are just fear wearing a better name. This one is finished."
		]
	},

]

TASKS += [

	# C-1 — Find Korina Brightvein
	{
		'task_id': 'mountains_mid_city_type_c_find_korina',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'korina_brightvein',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'korina_brightvein',
					'location': 'region_city_other2'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'korina_brightvein',
					'dialog_id': 'korina_c_first_meet'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_mountains_mid_c_find_korina' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',     'dialog_id': 'faith_mountains_mid_c_find_korina'     } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg',     'dialog_id': 'bragg_mountains_mid_c_find_korina'     } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'korina_brightvein', 'standing_text': [ "Harrock sent you back.", "The Rift paths are safer when you walk them.", "That's all I needed to hear." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_mid_city_type_c_consult_harrock'
				}
			},
		]
	},

	# C-2 — Get Harrock's word
	{
		'task_id': 'mountains_mid_city_type_c_consult_harrock',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'warden_harrock',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'warden_harrock',
					'dialog_id': 'harrock_c_vouch'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_mountains_mid_c_consult_harrock' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'tech_mountains_mid_c_consult_harrock'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_mountains_mid_c_consult_harrock' } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_mid_city_type_c_earn_korina'
				}
			},
		]
	},

	# C-3 — Return to Korina; she joins
	{
		'task_id': 'mountains_mid_city_type_c_earn_korina',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'korina_brightvein',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'korina_brightvein',
					'dialog_id': 'korina_c_joins'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_mountains_mid_c_earn_korina' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',     'dialog_id': 'faith_mountains_mid_c_earn_korina'     } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg',     'dialog_id': 'bragg_mountains_mid_c_earn_korina'     } },
			{
				'event_type': 'character_join',
				'params': {
					'character_id': 'korina_brightvein'
				}
			},
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'korina_brightvein'
				}
			}
		]
	},

]


# ── Type D ── Shatterpeak Warplate (mythic armor) ─────────────────────────────
# Gate: player holds mountains_large_city_e_forge_echo_core from the Ch.4 Type E chain (mountains cross).
# Deliver to Brawn → Korrin reads the core → defeat Emberwake Spirit → mythic armor.
# No new NPCs — uses avalanche_seer_korrin, emberwake_spirit, and brawn (Ch.1 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'brawn',
		'dialog_id': 'brawn_d_forge_core_reaction',
		'dialog': [
			"Forge-pressure still active inside this thing…",
			"(turns the core carefully in both hands)",
			"I can feel the foundry frequency humming against the plate. Whatever made this was never meant to leave the mountain.",
			"Korrin reads fall-lines and pressure better than anyone on these cliffs. He'll know exactly what this core is calling to.",
			"Take it to him before the resonance starts pulling something up on its own.",
			"And if the ground starts answering… step carefully."
		]
	},
	{
		'npc_id': 'avalanche_seer_korrin',
		'dialog_id': 'korrin_d_core_read',
		'dialog': [
			"This Forge Echo Core — the pressure signature inside it is extraordinary.",
			"It matches the Emberwake Cavern's resonance almost exactly.",
			"The Emberwake Spirit has been drawing heat from Ryla's fires for years.",
			"It feeds on the same foundry frequency the Core carries.",
			"Present the Core at the Cavern entrance — the Spirit will surface.",
			"Silence it and the forge-pressure it guards crystallizes.",
			"Brawn can hammer forge-pressure crystal into armor that absorbs impact like mountain stone."
		]
	},

	{
		'npc_id': 'emberwake_spirit',
		'dialog_id': 'emberwake_spirit_d_awakens',
		'dialog': [
			"The Forge Echo Core reaches the Cavern.",
			"You carry Ironveil's foundry frequency into my domain.",
			"The pressure I have held since the first forge burned — it is mine.",
			"You will not leave with it."
		]
	},

]

TASKS += [

	# D-0 — Deliver mountains_large_city_e_forge_echo_core to Brawn (standalone deliver; unlocks D chain)
	{
		'task_id': 'mountains_mid_city_type_d_deliver_forge_core',
		'type': 'deliver',
		'item_id': 'mountains_large_city_e_forge_echo_core',
		'to_type': 'npc',
		'to_id': 'brawn',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'brawn', 'dialog_id': 'brawn_d_forge_core_reaction' }},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'mountains_large_city_e_forge_echo_core'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_mountains_mid_d_deliver_forge_core'      } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_mountains_mid_d_deliver_forge_core' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',     'dialog_id': 'magic_mountains_mid_d_deliver_forge_core'     } },
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'avalanche_seer_korrin',
					'location': 'region_city_bar'
				}
			},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'avalanche_seer_korrin', 'standing_text': [ "The Forge Echo Core carries a resonance that matches the Emberwake Cavern almost exactly.", "Present it at the Cavern entrance and the Emberwake Spirit will surface.", "Silence it and the forge-pressure crystallizes. Brawn can work with that." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_mid_city_type_d_consult_korrin'
				}
			},
		]
	},

	# D-1 — Consult Korrin for the pressure reading
	{
		'task_id': 'mountains_mid_city_type_d_consult_korrin',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'avalanche_seer_korrin',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'avalanche_seer_korrin',
					'dialog_id': 'korrin_d_core_read'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_mountains_mid_d_consult_korrin'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grmnaw_mountains_mid_d_consult_korrin' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'skill_mountains_mid_d_consult_korrin'   } },
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'emberwake_spirit',
					'location': None
				}
			},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'avalanche_seer_korrin', 'standing_text': [ "The Emberwake Spirit has been drawing heat from Ryla's fires for years.", "Present the Forge Echo Core at the Cavern entrance and it will surface.", "Silence it and the forge-pressure crystallizes. Brawn can work with that." ] } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'emberwake_spirit', 'standing_text': [ "The Cavern burns with ancient fury.", "The Core gathers strength.", "Only its heart remains to be stilled." ] } },
			{
				'event_type': 'create_dungeon',
				'params': {
					'dungeon_id': 'mountains_mid_emberwake_cavern',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_mid_city_type_d_meet_emberwake_spirit'
				}
			},
		]
	},

	# D-2 — Meet the Emberwake Spirit (boss intro)
	{
		'task_id': 'mountains_mid_city_type_d_meet_emberwake_spirit',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'emberwake_spirit',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'emberwake_spirit'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'emberwake_spirit',
					'dialog_id': 'emberwake_spirit_d_awakens'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',  'dialog_id': 'skill_mountains_mid_d_meet_emberwake_spirit'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_mountains_mid_d_meet_emberwake_spirit'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',  'dialog_id': 'lyren_mountains_mid_d_meet_emberwake_spirit'  } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_mid_city_type_d_defeat_emberwake_spirit'
				}
			}
		]
	},

	# D-3 — Defeat the Emberwake Spirit; Brawn forges the mythic armor
	{
		'task_id': 'mountains_mid_city_type_d_defeat_emberwake_spirit',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'emberwake_spirit_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'emberwake_spirit_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_mountains_mid_shatterpeak_warplate'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_mountains_mid_d_defeat_emberwake_spirit' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_mountains_mid_d_defeat_emberwake_spirit'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',     'dialog_id': 'faith_mountains_mid_d_defeat_emberwake_spirit'     } },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'brawn',
					'standing_text': [
						"Forge-pressure crystal — it compresses under impact and rebounds harder.",
						"I've worked it into the warplate.",
						"The harder you're hit, the stronger it holds.",
						"This is the kind of armor the Rift deserves."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'avalanche_seer_korrin',
					'standing_text': [
						"The fall-lines are clear.",
						"The Cavern pressure has normalized.",
						"Ryla says her fires burn in the right colors again."
					]
				}
			},
		]
	},

]

# ── Type B ── Bragg / Rokhuld the Core-Breaker (regional character quest) ─────
# Gated by Ch.20 Void Gauntlet. Bragg feels the fracture-frequency returning —
# Rokhuld's obsession with the mountain's 'true ending' survived as a resonance
# pattern inside the Gallows Rift stone. Creates dungeon in open area.
# No new NPCs — uses initiate_character_dialog on Bragg exclusively.

NPC_DIALOG += [

	{
		'npc_id': 'bragg',
		'dialog_id': 'bragg_b_fracture_echo',
		'dialog': [
			"That sound.",
			"I know that sound. I've heard it in every nightmare since the explosion.",
			"That is a micro-fracture forming. Deep. Real deep.",
			"Rokhuld — or whatever's left of him — is drilling again.",
			"(jaw tight) He convinced himself breaking the core was righteous. Sacred duty.",
			"He was wrong then. He's still wrong now.",
			"I built golems to hold this mountain together. He built a crusade to tear it apart.",
			"We end it. Today."
		]
	},
	{
		'npc_id': 'bragg',
		'dialog_id': 'bragg_b_entering_core',
		'dialog': [
			"He'll be deeper than before. The void fed something in him.",
			"Don't let him monologue. He gets worse the longer he talks.",
			"(quietly) I know because I used to do the same thing."
		]
	},
	{
		'npc_id': 'rokhuld',
		'dialog_id': 'rokhuld_b_risen',
		'dialog': [
			"The void showed me the truth of my mission.",
			"The mountain's core contains the world's final breath.",
			"I will reach it. I will release it. This is righteous.",
			"You cannot stop what is already written in the stone."
		]
	},
	{
		'npc_id': 'rokhuld',
		'dialog_id': 'rokhuld_b_defeated',
		'dialog': [
			"(hammer cracking, voice already half-stone)",
			"You stop the drill…",
			"The mission does not stop with me.",
			"Seven places where the world already tried to empty itself.",
			"Seven fractures the void found useful.",
			"You seal them… and still the pressure builds.",
			"(almost calm)",
			"When the last core is broken… you will understand.",
			"I was never trying to end the mountain.",
			"I was trying to let the world finish the breath it started holding the day the first fracture opened."
		]
	},
	{
		'npc_id': 'bragg',
		'dialog_id': 'bragg_b_victory',
		'dialog': [
			"(sitting down against the wall, hands shaking slightly)",
			"I spent years thinking the explosion was punishment. For something I did wrong.",
			"He spent years thinking it was a calling. For something he had to do right.",
			"We were both just afraid.",
			"(stands up, steadier now) The mountain's still standing.",
			"That's what matters."
		]
	},

]

TASKS += [

	# B-0 — Void Gauntlet entry (self-completing gated task)
	{
		'task_id': 'mountains_mid_city_b_void_gauntlet',
		'type': 'gated',
		'task_acquire_events': [
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'rokhulls_fracture_core', 'location': 'region_open_area' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_b_fracture_echo' }},
			{ 'event_type': 'complete_task', 'params': { 'task_id': 'mountains_mid_city_b_void_gauntlet' }},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_mid_city_b_meet_rokhuld' }},
		]
	},

	# B-1 — Meet Rokhuld (boss intro)
	{
		'task_id': 'mountains_mid_city_b_meet_rokhuld',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rokhuld',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rokhuld', 'dialog_id': 'rokhuld_b_risen' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_mountains_mid_b_meet_rokhuld' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg',     'dialog_id': 'bragg_mountains_mid_b_meet_rokhuld'     } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_mountains_mid_b_meet_rokhuld'      } },
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_mid_city_b_defeat_rokhuld' }},
		]
	},

	# B-2 — Defeat Rokhuld
	{
		'task_id': 'mountains_mid_city_b_defeat_rokhuld',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'rokhuld_b1',
		'task_acquire_events': [
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'rokhuld_b1', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog',           'params': { 'npc_id': 'rokhuld',    'dialog_id': 'rokhuld_b_defeated'                            }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg',      'dialog_id': 'bragg_b_victory'                               }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_mountains_mid_b_defeat_rokhuld' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',     'dialog_id': 'faith_mountains_mid_b_defeat_rokhuld'     } },
			{ 'event_type': 'complete_regional_quest_2', 'params': { 'region_id': 'mountains' }},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
	'story_id': 'mountains_mid_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}