ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'vigilant_karrek',
		'name': 'Karrek Windbreak',
		'description': (
			'A hardened watchman who stands guard through the fiercest storms.'
			' Karrek\'s cloak is patched with scraps from past expeditions.'
			' He claims the wind itself warns him of approaching danger.'
		)
	},
	{
		'npc_id': 'survivor_mira',
		'name': 'Mira Frostline',
		'description': (
			'A resourceful trader who deals in survival gear and hard‑earned wisdom.'
			' Mira\'s smile is rare but genuine, like sunlight on fresh snow.'
			' She has a story for every scar she carries.'
		)
	},
	{
		'npc_id': 'gale_seer_orlena',
		'name': 'Orlena the Gale‑Seer',
		'description': (
			'A wind-reader who interprets storm-patterns and senses disturbances in the frost.'
			' Orlena\'s breath fogs the air even on calm days.'
			' She says the cold carries the outpost\'s oldest warnings.'
		)
	},
	{
		'npc_id': 'stormhollow_voice',
		'name': 'Stormhollow Voice',
		'description': (
			'A roaring presence formed from hollow wind-channels and trapped battle-echoes.'
			' It guards the warden plate with the fury of every storm that ever buried the outpost.'
		)
	},
]


NPC_DIALOG = [

	# ── Intro dialogs ───────────────────────────────────────────────
	{
		'npc_id': 'vigilant_karrek',
		'dialog_id': 'karrek_intro',
		'dialog': [
			"The wind shifts in patterns I've never recorded.",
			"Something moves through the storm that shouldn't be there.",
			"Bleakwatch has survived worse — but not without knowing what's coming."
		]
	},
	{
		'npc_id': 'survivor_mira',
		'dialog_id': 'mira_intro',
		'dialog': [
			"Supply routes have gone quiet.",
			"The cold comes from the wrong direction.",
			"If the outpost loses its watch, the whole frontier falls dark."
		]
	},
	{
		'npc_id': 'gale_seer_orlena',
		'dialog_id': 'orlena_intro',
		'dialog': [
			"The storm-patterns fracture near the hollow.",
			"A Stormhollow Voice stirs — a spirit of trapped battle-wind.",
			"If it breaks free, no signal will carry across the snow line."
		]
	},
	{
		'npc_id': 'vigilant_karrek',
		'dialog_id': 'karrek_closing',
		'dialog': [
			"The wind reads clean again.",
			"Whatever drove those patterns — it's gone.",
			"Bleakwatch stands. That's all that matters."
		]
	},

]

NPC_DIALOG += [

	# ── Type C dialogs — Commander Drax ────────────────────────────
	{
		'npc_id': 'commander_drax',
		'dialog_id': 'drax_c_first_meet',
		'dialog': [
			"You're not garrison. You move like field-trained.",
			"I've been watching your party since you crossed the frost-line.",
			"Bleakwatch has a wall. What it doesn't have is people worth standing behind it.",
			"Prove you're worth my time and I'll consider the offer."
		]
	},
	{
		'npc_id': 'vigilant_karrek',
		'dialog_id': 'karrek_c_vouch',
		'dialog': [
			"Drax doesn't move for anyone. That's not stubbornness — it's policy.",
			"He's lost units before to commanders who moved too fast.",
			"Tell him I watched you on the storm-approach and you didn't flinch.",
			"Coming from me, that's the only credential that opens his door."
		]
	},
	{
		'npc_id': 'commander_drax',
		'dialog_id': 'drax_c_joins',
		'dialog': [
			"Karrek doesn't say that about anyone.",
			"He's watched soldiers break on that approach for twenty years.",
			"Fine. I'll move.",
			"But understand — I lead from the front.",
			"You position me at the rear and I walk."
		]
	},

]

NPC_DIALOG += [

	# ── Type D dialogs — Bleakwatch Warden Plate ───────────────────
	{
		'npc_id': 'vigilant_karrek',
		'dialog_id': 'karrek_d_registry',
		'dialog': [
			"A contraband registry from Tess\'s network — these log black-market warden equipment.",
			"The outpost\'s original warden plate disappeared during the second siege.",
			"This entry traces the last known location to the Stormhollow.",
			"Brawn will know what to make of it — that plate\'s design is old-order military."
		]
	},
	{
		'npc_id': 'gale_seer_orlena',
		'dialog_id': 'orlena_d_storm_read',
		'dialog': [
			"Brawn\'s right — the storm-patterns around the hollow carry the warden frequency.",
			"The plate has been down there since the siege.",
			"The Stormhollow Voice absorbed the battle-wind that buried it.",
			"Force it out and the plate surfaces with the storm it was trapped in.",
			"Be ready — it won\'t surrender the warden\'s armour quietly."
		]
	},
	{
		'npc_id': 'stormhollow_voice',
		'dialog_id': 'stormhollow_voice_awakens',
		'dialog': [
			"The warden\'s plate is mine.",
			"Every storm that buried this outpost feeds me.",
			"I am the battle-wind that never stopped.",
			"You will not strip the hollow of its armour."
		]
	},
	{
		'npc_id': 'vigilant_karrek',
		'dialog_id': 'karrek_d_reward',
		'dialog': [
			"The storm broke clean when you came back.",
			"That plate — it hasn\'t breathed open air since the second siege.",
			"Brawn says it\'s the finest warden-grade steel he\'s handled.",
			"The outpost\'s warden returns to the wall. Fitting."
		]
	},

]


TASKS = [

	# ── Intro scaffold ───────────────────────────────────────────────
	{
		'task_id': 'snow_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'vigilant_karrek',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'vigilant_karrek',
					'standing_text': [
						"The wind warns before anything else does — learn to listen."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'survivor_mira',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'survivor_mira',
					'standing_text': [
						"Survival gear, hard-won wisdom — I trade in both."
					]
				}
			},
		],
		'task_complete_events': [			
            { 'event_type': 'award_task', 'params': { 'task_id': 'snow_small_city_type_a_ch6_meet_karrek' }},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_meet_karrek'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_c_find_drax'
				},
				'condition': {
					'type': 'is_chapter_gte',
					'params': { 'chapter': 6 }
				}
			}
		]
	},
	{
		'task_id': 'snow_small_city_meet_karrek',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'vigilant_karrek',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'vigilant_karrek',
					'standing_text': [
						"The wind patterns are wrong.",
						"Something moves through the storm that doesn't belong."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vigilant_karrek',
					'dialog_id': 'karrek_intro'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_meet_survivor_mira'
				}
			}
		]
	},
	{
		'task_id': 'snow_small_city_meet_survivor_mira',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'survivor_mira',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'survivor_mira',
					'dialog_id': 'mira_intro'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_find_orlena'
				}
			}
		]
	},
	{
		'task_id': 'snow_small_city_find_orlena',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'gale_seer_orlena',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'gale_seer_orlena',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'gale_seer_orlena',
					'standing_text': [
						"The storm-patterns fracture near the hollow.",
						"A Stormhollow Voice stirs — listen and you'll hear it."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'gale_seer_orlena',
					'dialog_id': 'orlena_intro'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vigilant_karrek',
					'dialog_id': 'karrek_closing'
				}
			},
			{
				'event_type': 'complete_regional_quests',
				'params': {
					'region_id': 'snow_small_city'
				}
			}
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE C — Commander Drax (extended character, slot 2)
	# Gated by is_chapter_gte: 6
	# Awarded by: snow_small_city_initialize (conditional)
	# =========================================================

	{
		'task_id': 'snow_small_city_type_c_find_drax',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'commander_drax',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'commander_drax',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'commander_drax',
					'standing_text': [
						"You're not garrison.",
						"State your purpose or get off my wall."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'commander_drax',
					'dialog_id': 'drax_c_first_meet'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_c_consult_karrek'
				}
			},
		]
	},
	{
		'task_id': 'snow_small_city_type_c_consult_karrek',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'vigilant_karrek',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'vigilant_karrek',
					'standing_text': [
						"Drax sent you to me, didn't he.",
						"He does that. Means he's already half-decided."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vigilant_karrek',
					'dialog_id': 'karrek_c_vouch'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_c_earn_drax'
				}
			},
		]
	},
	{
		'task_id': 'snow_small_city_type_c_earn_drax',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'commander_drax',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'commander_drax',
					'standing_text': [
						"Karrek spoke for you.",
						"I don't ignore that. Come back and we'll talk terms."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'commander_drax',
					'dialog_id': 'drax_c_joins'
				}
			},
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'commander_drax'
				}
			},
			{
				'event_type': 'character_join',
				'params': {
					'character_id': 'commander_drax'
				}
			},
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE D — Mythic Equipment Quest (slot 3)
	# Gate: desert_small_city_f_contraband_registry (Tess F chain, Ch.9)
	# Deliver to: Brawn (armor)
	# Mythic reward: mythic_snow_small_bleakwatch_warden_plate
	# =========================================================

	{
		'task_id': 'snow_small_city_type_d_deliver_contraband_registry',
		'type': 'deliver',
		'item_id': 'desert_small_city_f_contraband_registry',
		'to_type': 'npc',
		'to_id': 'brawn',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'desert_small_city_f_contraband_registry'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vigilant_karrek',
					'dialog_id': 'karrek_d_registry'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_d_consult_orlena'
				}
			}
		]
	},
	{
		'task_id': 'snow_small_city_type_d_consult_orlena',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'gale_seer_orlena',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'gale_seer_orlena',
					'standing_text': [
						"The storm-patterns near the hollow shifted again.",
						"Something old and armoured is down there.",
						"Come — I need to show you what the gale is reading."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'gale_seer_orlena',
					'dialog_id': 'orlena_d_storm_read'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_d_meet_stormhollow_voice'
				}
			}
		]
	},
	{
		'task_id': 'snow_small_city_type_d_meet_stormhollow_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'stormhollow_voice',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'stormhollow_voice',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'stormhollow_voice',
					'standing_text': [
						"The hollow howls with a voice that isn't the wind.",
						"Orlena says this is it — the storm that never broke."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'stormhollow_voice',
					'dialog_id': 'stormhollow_voice_awakens'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_d_defeat_stormhollow_voice'
				}
			}
		]
	},
	{
		'task_id': 'snow_small_city_type_d_defeat_stormhollow_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'stormhollow_voice_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'stormhollow_voice_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vigilant_karrek',
					'dialog_id': 'karrek_d_reward'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_snow_small_bleakwatch_warden_plate'
				}
			}
		]
	},

]
# ── Type A ── Ch.6 Chapter Tie-In (Karrek storm report) ───────────────────────
# Awarded by Ch.6 Seth after his resistance reveal. Player must speak to Karrek
# at the storm post and collect his breach-approach reading before Seth will
# hand over his contact (Rhett). No new NPCs — Karrek is in the city seed.

NPC_DIALOG += [

    {
        'npc_id': 'vigilant_karrek',
        'dialog_id': 'karrek_a_ch6_storm_report',
        'dialog': [
            "Seth sent you? Good timing.",
            "I've been logging storm-pattern fractures near the hollow for three days.",
            "The wind doesn't lie — something moved through that breach site that wasn't weather.",
            "Take this reading. Seth will know what it means.",
            "(pressing a sealed wind-chart into your hands)",
            "Tell him: the hollow is listening. Whatever crawled out — it knows we're watching too."
        ]
    },

]

TASKS += [

    # A-1 — Meet Karrek for the storm report (completes the gate)
    {
        'task_id': 'snow_small_city_type_a_ch6_meet_karrek',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vigilant_karrek',
        'task_acquire_events': [
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'vigilant_karrek', 'standing_text': [
                "The wind carries bad omens from the hollow.",
                "Seth's people should know what I've recorded."
            ]}}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vigilant_karrek', 'dialog_id': 'karrek_a_ch6_storm_report' }},
        ]
    },

]
PRIMARY_STORY_SETTINGS = {
	'story_id': 'snow_small_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}