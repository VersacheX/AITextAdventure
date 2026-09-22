ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'elder_saphrin',
		'name': 'Saphrin the Hollow‑Keeper',
		'description': (
			'A serene elder who oversees the Exchange with ritualistic precision.'
			' Saphrin communes with the living wood, sensing emotional echoes in traded goods.'
			' Their presence is calming, like moss‑softened footsteps in ancient groves.'
		),
		"image": "npcs:elder_saphrin1",
		"psychology": {
			"mbti": "INFJ",
			"dominant": "Ni — Senses the deeper intention behind every trade before the terms are spoken.",
			"auxiliary": "Fe — Presides over the Exchange as an emotional anchor; their calm is a practiced, deliberate gift.",
			"tertiary": "Ti — Applies the forest's unwritten rules with quiet, precise interpretation.",
			"inferior": "Se — Rarely disturbed by physical urgency; slower to respond when crisis demands immediate action."
		},
		"enneagram": {
			"enneagram_type": "9w1",
			"core_fear": "Conflict fracturing the harmony of the Exchange and the living grove.",
			"core_desire": "A community in which every bargain is freely and honestly made.",
			"defense_mechanism": "Narcotization — Absorbs into the grove's rhythm to avoid confronting the rot within the pacts.",
			"stress_line": "Moves to Type 6 — Becomes anxious and over-cautious when the hollow's corruption accelerates.",
			"growth_line": "Moves to Type 3 — Takes decisive leadership when the Exchange genuinely depends on it.",
			"instinctual_variant": "so/sp — Community stewardship is the core expression of their identity."
		}
	},
	{
		'npc_id': 'twigwhisper_loryn',
		'name': 'Loryn Twigwhisper',
		'description': (
			'A nimble, sharp‑eyed negotiator who conducts deals from the high boughs.'
			' Loryn\'s voice carries like birdsong, disarming even the most guarded traders.'
			' They claim the forest itself enforces every bargain struck in the Den.'
		),
		"image": "npcs:twigwhisper_loryn1",
		"psychology": {
			"mbti": "ENTP",
			"dominant": "Ne — Reads negotiation as a game of shifting possibilities; always three counter-offers ahead.",
			"auxiliary": "Ti — Structures arguments internally with sharp logic, then delivers them as charming improvisation.",
			"tertiary": "Fe — Skilled at calibrating warmth and pressure to move traders toward agreement.",
			"inferior": "Si — Rarely honours precedent; every deal is fresh and the rules are flexible until they're not."
		},
		"enneagram": {
			"enneagram_type": "7w8",
			"core_fear": "Being locked into a bad deal with no exit clause.",
			"core_desire": "To be the sharpest, most celebrated deal-maker in the canopy.",
			"defense_mechanism": "Rationalization — Reframes lopsided bargains as 'creative arrangements' to avoid guilt.",
			"stress_line": "Moves to Type 1 — Becomes rigid and self-righteous when the forest punishes a broken pact.",
			"growth_line": "Moves to Type 5 — Develops genuine expertise in forest law when high stakes demand it.",
			"instinctual_variant": "so/sp — Reputation in the canopy network is the currency that matters most."
		}
	},
	{
		'npc_id': 'spore_seer_myrn',
		'name': 'Myrn the Spore‑Seer',
		'description': (
			'A wandering hermit who reads drifting spores like constellations. '
			'Myrn senses disturbances in the forest\'s emotional undergrowth.'
		),
		"image": "npcs:spore_seer_myrn1",
		"psychology": {
			"mbti": "INTP",
			"dominant": "Ti — Classifies spore-drift patterns into an elaborate internal taxonomy only he fully understands.",
			"auxiliary": "Ne — Leaps between pattern-connections, finding emotional meaning in microscopic variations.",
			"tertiary": "Si — Draws on decades of wandering observation; his memory is a living map of spore behaviour.",
			"inferior": "Fe — Struggles to communicate his readings in emotionally accessible terms; others often leave confused."
		},
		"enneagram": {
			"enneagram_type": "5w4",
			"core_fear": "Misreading the spores and sending someone into danger.",
			"core_desire": "To develop a complete, accurate understanding of the forest's emotional substrate.",
			"defense_mechanism": "Isolation — Retreats deeper into the undergrowth when his readings fail or go unheeded.",
			"stress_line": "Moves to Type 7 — Becomes scattered and restless when the spores stop making sense.",
			"growth_line": "Moves to Type 8 — Acts on his knowledge decisively when the forest is in genuine danger.",
			"instinctual_variant": "sp/sx — Self-sufficient wanderer who forms rare but deep bonds with those who take his readings seriously."
		}
	},
]

NPC_DIALOG = [

	# ── Type A dialogs ──────────────────────────────────────────────
	{
		'npc_id': 'elder_saphrin',
		'dialog_id': 'saphrin_intro',
		'dialog': [
			"The Exchange falters. Promises rot at the edges.",
			"Something ancient stirs beneath the roots — a mind that binds all bargains.",
			"If it wakes fully, no oath will remain free."
		]
	},
	{
		'npc_id': 'twigwhisper_loryn',
		'dialog_id': 'loryn_intro',
		'dialog': [
			"The canopy rustles with warnings.",
			"Deals unravel, threads snap, and the forest tightens its grip.",
			"Whatever lies below wants every promise ever spoken."
		]
	},
	{
		'npc_id': 'spore_seer_myrn',
		'dialog_id': 'myrn_intro',
		'dialog': [
			"Spores drift toward the Hollows — drawn by a hungry root‑mind.",
			"The Heartwood Veil grows, weaving itself through every pact.",
			"If you descend, tread softly. It listens."
		]
	},
	{
		'npc_id': 'elder_saphrin',
		'dialog_id': 'saphrin_closing',
		'dialog': [
			"The Veil falls silent. The Exchange breathes again.",
			"You have freed our promises from its grasp.",
			"The forest will remember your name in its rings."
		]
	},

	# ── Type D dialogs ──────────────────────────────────────────────
	{
		'npc_id': 'elder_saphrin',
		'dialog_id': 'saphrin_veil_leaf',
		'dialog': [
			"A Veil Memory Leaf… I haven't seen one since the first Heartwood awakening.",
			"This fragment still hums with promises — it belongs to the Verdant Cradle.",
			"Seek Loryn. She knows the old ways of binding memory back to bark."
		]
	},
	{
		'npc_id': 'twigwhisper_loryn',
		'dialog_id': 'loryn_veil_ritual',
		'dialog': [
			"The leaf is real. The old promises are still alive inside it.",
			"There is a weapon sleeping in the deepest bark — the Canopy Sovereign.",
			"Bring the leaf to the Verdant Cradle. If it accepts you, the blade is yours."
		]
	},
	{
		'npc_id': 'twigwhisper_loryn',
		'dialog_id': 'loryn_veil_reward',
		'dialog': [
			"The Cradle released it. The Canopy Sovereign is yours.",
			"Carry it well — the forest remembers every oath sworn upon its edge."
		]
	},
	{
		'npc_id': 'elder_saphrin',
		'dialog_id': 'saphrin_a_ch18_memory_anchor',
		'dialog': [
			"A shifting map that won't hold still.",
			"(calm, deliberate) The Exchange has a shard of fixed memory — an echo so old the wood grew around it.",
			"It remembers a time before collapse was possible.",
			"That kind of certainty does not bend.",
			"(retrieves a small, smooth fragment of living wood from beneath the counter)",
			"Take it. If your cartographer places this against the map, the lines will have something to hold to.",
			"The forest trusts you with this. Do not waste it."
		]
	},
]

# --- Character dialogs: Type A ---
NPC_DIALOG += [

    # Type A – Meet Saphrin
    {
        'npc_id': 'spirit',
        'dialog_id': 'spirit_forest_large_a_meet_saphrin',
        'dialog': [
            "Promises rotting at the edges… something is rewriting the weight of every oath."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_forest_large_a_meet_saphrin',
        'dialog': [
            "A mind that binds all bargains. The forest is trying to warn us before it finishes waking."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_forest_large_a_meet_saphrin',
        'dialog': [
            "If it wakes fully, no deal in this place stays free. We move before that happens."
        ]
    },

    # Type A – Meet Loryn
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_forest_large_a_meet_loryn',
        'dialog': [
            "The canopy is restless. Deals are fraying for a reason."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_forest_large_a_meet_loryn',
        'dialog': [
            "Whatever's below wants every promise ever spoken. That's an ambitious appetite."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_forest_large_a_meet_loryn',
        'dialog': [
            "The forest is tightening its grip. We need to find the source before it finishes."
        ]
    },

    # Type A – Find Myrn
    {
        'npc_id': 'spirit',
        'dialog_id': 'spirit_forest_large_a_find_myrn',
        'dialog': [
            "Spores drifting toward the Hollows… the root-mind is already calling."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_forest_large_a_find_myrn',
        'dialog': [
            "The Heartwood Veil is weaving itself through every pact. Tread carefully."
        ]
    },
    {
        'npc_id': 'kor_in',
        'dialog_id': 'kor_in_forest_large_a_find_myrn',
        'dialog': [
            "Some hungers don't stop at the body. This one wants the meaning of the words we speak."
        ]
    },

]

# --- Character dialogs: Type D ---
NPC_DIALOG += [

    # Type D – Deliver Veil Leaf
    {
        'npc_id': 'spirit',
        'dialog_id': 'spirit_forest_large_d_deliver_veil_leaf',
        'dialog': [
            "A leaf that still hums with old promises. The forest hasn't forgotten them."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_forest_large_d_deliver_veil_leaf',
        'dialog': [
            "Memory bound into bark. I can feel it wanting to go home."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_forest_large_d_deliver_veil_leaf',
        'dialog': [
            "Loryn will know how to return it properly. She always does."
        ]
    },

    # Type D – Consult Loryn
    {
        'npc_id': 'spirit',
        'dialog_id': 'spirit_forest_large_d_consult_loryn',
        'dialog': [
            "The old promises are still alive inside the leaf."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_forest_large_d_consult_loryn',
        'dialog': [
            "A weapon sleeping in the deepest bark — the Canopy Sovereign. Of course it is."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_forest_large_d_consult_loryn',
        'dialog': [
            "If the Verdant Cradle accepts the leaf, the blade is ours. We go carefully."
        ]
    },

    # Type D – Meet / Defeat Verdant Cradle
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_forest_large_d_meet_verdant_cradle',
        'dialog': [
            "The Cradle released it. Take the blade."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'spirit_forest_large_d_meet_verdant_cradle',
        'dialog': [
            "The forest remembers every oath sworn on that edge. Carry it carefully."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_forest_large_d_meet_verdant_cradle',
        'dialog': [
            "Some weapons are grown, not forged. This one knows the weight of promises."
        ]
    },

]

# --- Character dialogs: Type A Ch18 ---
NPC_DIALOG += [

    # Type A – Ch18 Find Anchor
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_forest_large_a_ch18_find_anchor',
        'dialog': [
            "A shard of fixed memory from before collapse was possible. That's rare certainty."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'spirit_forest_large_a_ch18_find_anchor',
        'dialog': [
            "The wood grew around it to keep it safe. The forest trusts us with this."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_forest_large_a_ch18_find_anchor',
        'dialog': [
            "Something unmoored needs an anchor. This one does not bend."
        ]
    },

]

# --- Character dialogs: Type B ---
NPC_DIALOG += [

    # B – Meet Marrowroot
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_forest_large_b_meet_marrowroot',
        'dialog': [
            "He's still in the wood. The intention didn't burn out with him."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_forest_large_b_meet_marrowroot',
        'dialog': [
            "Quiet. He hears through the roots. He already knows we're here."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_forest_large_b_meet_marrowroot',
        'dialog': [
            "The void fed what was left of his purpose. Now it's reaching for the canopy again."
        ]
    },

    # B – Defeat Marrowroot
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_forest_large_b_defeat_marrowroot',
		'dialog': [
			"Stay down. The forest doesn't need another savior."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_forest_large_b_defeat_marrowroot',
		'dialog': [
			"The forest isn't his to save. It just needs to be left alone. We did that."
		]
	},

]

TASKS = [

	# ── Type A — Chapter Tie‑In (slot 1) ────────────────────────────
	{
		'task_id': 'forest_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'elder_saphrin',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'elder_saphrin',
					'standing_text': [
						"Sit awhile — the trees remember more stories than any traveler."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'standing_text': [
						"High branches hold gossip; lean close and I'll tell you what the leaves sang."
					]
				}
			},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'forest_large_city_type_a_ch18_find_anchor' }},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_large_city_type_a_meet_saphrin'
				}
			},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'forest_large_city_type_d_deliver_veil_leaf' }}
		]
	},
	{
		'task_id': 'forest_large_city_type_a_meet_saphrin',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'elder_saphrin',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'elder_saphrin',
					'dialog_id': 'saphrin_intro'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit',  'dialog_id': 'spirit_forest_large_a_meet_saphrin'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_forest_large_a_meet_saphrin' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',  'dialog_id': 'thorn_forest_large_a_meet_saphrin'  } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'elder_saphrin', 'standing_text': [ "The Exchange trembles. Something roots beneath our bargains.", "Sit, traveler — the wood has warnings to whisper." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_large_city_type_a_meet_loryn'
				}
			}
		]
	},
	{
		'task_id': 'forest_large_city_type_a_meet_loryn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'twigwhisper_loryn',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'dialog_id': 'loryn_intro'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',  'dialog_id': 'skill_forest_large_a_meet_loryn'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_forest_large_a_meet_loryn'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',  'dialog_id': 'thorn_forest_large_a_meet_loryn'  } },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'standing_text': [
						"Deals are unraveling. Promises fray like old bark.",
						"Something deep below is rewriting the rules."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_large_city_type_a_find_myrn'
				}
			}
		]
	},
	{
		'task_id': 'forest_large_city_type_a_find_myrn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'spore_seer_myrn',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'spore_seer_myrn',
					'location': 'region_city_other1'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'spore_seer_myrn',
					'dialog_id': 'myrn_intro'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit',  'dialog_id': 'spirit_forest_large_a_find_myrn'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_forest_large_a_find_myrn' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_forest_large_a_find_myrn' } },
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'elder_saphrin',
					'dialog_id': 'saphrin_closing'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'spore_seer_myrn',
					'standing_text': [
						"The forest is quiet again. The root-mind sleeps, and the Exchange breathes.",
						"Thank you for keeping its promises free."
					]
				}
			}
		]
	},

	# ── Type D — Mythic Equipment Quest (slot 2) ─────────────────────
	# Gate: veil_memory_leaf (from abandoned_ruin_ch2, Ch.2)
	# Mythic reward: mythic_forest_large_canopy_sovereign (weapon → Diego)
	{
		'task_id': 'forest_large_city_type_d_deliver_veil_leaf',
		'type': 'deliver',
		'item_id': 'veil_memory_leaf',
		'to_type': 'npc',
		'to_id': 'elder_saphrin',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'elder_saphrin',
					'dialog_id': 'saphrin_veil_leaf'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit',  'dialog_id': 'spirit_forest_large_d_deliver_veil_leaf'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_forest_large_d_deliver_veil_leaf'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',  'dialog_id': 'thorn_forest_large_d_deliver_veil_leaf'  } },
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'veil_memory_leaf'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'elder_saphrin',
					'standing_text': [
						"The leaf is real. The old promises are still alive inside it.",
						"Seek Loryn. She knows the old ways of binding memory back to bark."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_large_city_type_d_consult_loryn'
				}
			}
		]
	},
	{
		'task_id': 'forest_large_city_type_d_consult_loryn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'twigwhisper_loryn',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'dialog_id': 'loryn_veil_ritual'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit',  'dialog_id': 'spirit_forest_large_d_consult_loryn'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',   'dialog_id': 'tech_forest_large_d_consult_loryn'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',  'dialog_id': 'thorn_forest_large_d_consult_loryn'  } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'twigwhisper_loryn', 'standing_text': [ "The Cradle waits. If it accepts the leaf, the Canopy Sovereign is yours." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_large_city_type_d_meet_verdant_cradle'
				}
			}
		]
	},
	{
		'task_id': 'forest_large_city_type_d_meet_verdant_cradle',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'verdant_cradle_guardian_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'verdant_cradle_guardian_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'dialog_id': 'loryn_veil_reward'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_forest_large_d_meet_verdant_cradle' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit',     'dialog_id': 'spirit_forest_large_d_meet_verdant_cradle'     } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',     'dialog_id': 'thorn_forest_large_d_meet_verdant_cradle'     } },
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_forest_large_canopy_sovereign'
				}
			}
		]
	},

	# A-1 — Meet Saphrin to receive the living memory anchor
	{
		'task_id': 'forest_large_city_type_a_ch18_find_anchor',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'elder_saphrin',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'elder_saphrin', 'dialog_id': 'saphrin_a_ch18_memory_anchor' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',   'dialog_id': 'tech_forest_large_a_ch18_find_anchor'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit',  'dialog_id': 'spirit_forest_large_a_ch18_find_anchor'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_forest_large_a_ch18_find_anchor' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'elder_saphrin', 'standing_text': [ "The forest trusts you with this. Do not waste it." ] } },
			{ 'event_type': 'award_item', 'params': { 'item_id': 'living_memory_anchor' }},
		]
	},

]

# ── Type B ── Thorn / Elder Marrowroot (regional character quest) ──────────────
# Gated by Ch.20 Void Gauntlet. Thorn senses Marrowroot's corruption seeping
# back into the Aurelion Veil canopy — the root-mind's promise to 'save' the
# forest didn't die, it went dormant and the void's collapse woke it.
# Creates dungeon in open area.
# No new NPCs — uses initiate_character_dialog on Thorn exclusively.

NPC_DIALOG += [

	{
		'npc_id': 'thorn',
		'dialog_id': 'thorn_b_roots_move',
		'dialog': [
			"Roots are moving wrong.",
			"Not growing. Reaching.",
			"Marrowroot fused with the tree to save the forest. That intention didn't burn out with him.",
			"It's in the wood. Patient.",
			"The void's collapse — all that pressure releasing — it found the intention and fed it.",
			"Now it's reaching toward the canopy again.",
			"(terse) We go in. We burn it out. It doesn't get to do this twice."
		]
	},
	{
		'npc_id': 'thorn',
		'dialog_id': 'thorn_b_entering_grove',
		'dialog': [
			"Quiet. Don't touch the roots.",
			"He hears through them.",
			"(stops, listens) He already knows we're here."
		]
	},
	{
		'npc_id': 'marrowroot',
		'dialog_id': 'marrowroot_b_risen',
		'dialog': [
			"You cut me from the tree. But the tree remembers me.",
			"The void showed me the edge approaching. The forest must transform or be consumed.",
			"I am the transformation.",
			"You are the resistance. And resistance is what I was made to overcome."
		]
	},
	{
		'npc_id': 'marrowroot',
		'dialog_id': 'marrowroot_b_defeated',
		'dialog': [
			"(roots cracking, voice already half-wood)",
			"You cut me from the tree once…",
			"The intention did not die with the body. It only waited.",
			"Seven places where the world already tried to empty itself.",
			"Seven remnants the void found useful.",
			"You close them… and still the reaching continues.",
			"(almost gentle)",
			"When the last root is burned… you will see.",
			"I was never trying to save the forest from the edge.",
			"I was trying to make it ready for what comes after the edge arrives."
		]
	},
	{
		'npc_id': 'thorn',
		'dialog_id': 'thorn_b_victory',
		'dialog': [
			"(stands in the cleared grove, breathing hard)",
			"He believed what he was doing was good.",
			"That's the part that makes it hard.",
			"(looking at the trees) But the forest isn't his to save. It's not mine either.",
			"It just needs to be left alone.",
			"(quietly) We did that. We left it alone."
		]
	},

]

TASKS += [

	# B-0 — Void Gauntlet entry (self-completing gated task)
	{
		'task_id': 'forest_large_city_b_void_gauntlet',
		'type': 'gated',
		'task_acquire_events': [
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'marrowroots_deep_grove', 'location': 'region_open_area' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'marrowroots_deep_grove', 'item_id': 'earrings_of_insight', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'marrowroots_deep_grove', 'item_id': 'hurricane_blade', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'marrowroots_deep_grove', 'item_id': 'archivists_hood', 'location': 'treasure_room' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_b_roots_move' }},
			{ 'event_type': 'complete_task', 'params': { 'task_id': 'forest_large_city_b_void_gauntlet' }},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'forest_large_city_b_meet_marrowroot' }},
		]
	},

	# B-1 — Meet Marrowroot (boss intro)
	{
		'task_id': 'forest_large_city_b_meet_marrowroot',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'marrowroot',
		'task_acquire_events': [
			{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'marrowroots_deep_grove', 'location': 'final_chamber' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_b_entering_grove' }},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marrowroot', 'dialog_id': 'marrowroot_b_risen' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_forest_large_b_meet_marrowroot' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',     'dialog_id': 'thorn_forest_large_b_meet_marrowroot'     } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_forest_large_b_meet_marrowroot'      } },
			{ 'event_type': 'award_task', 'params': { 'task_id': 'forest_large_city_b_defeat_marrowroot' }},
		]
	},

	# B-2 — Defeat Marrowroot
	{
		'task_id': 'forest_large_city_b_defeat_marrowroot',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'marrowroot_b1',
		'task_acquire_events': [			
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'marrowroot_b1', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog',          'params': { 'npc_id': 'marrowroot', 'dialog_id': 'marrowroot_b_defeated'                         }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',      'dialog_id': 'thorn_b_victory'                               }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_forest_large_b_defeat_marrowroot' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit',     'dialog_id': 'spirit_forest_large_b_defeat_marrowroot'     } },
			{ 'event_type': 'complete_regional_quest_2', 'params': { 'region_id': 'forest' }},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
	'story_id': 'forest_large_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}