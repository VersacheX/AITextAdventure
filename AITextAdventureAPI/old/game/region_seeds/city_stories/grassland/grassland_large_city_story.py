ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'keeper_savran',
		'name': 'Savran Spicekeeper',
		'description': (
			'A charismatic curator of exotic beasts and rarities.'
			' Savran\'s cloak is stitched with feathers, scales, and fur from creatures he has tamed.'
			' His stories are as wild as the animals he tends.'
		)
	},
	{
		'npc_id': 'waymaster_delphi',
		'name': 'Delphi the Waymaster',
		'description': (
			'A seasoned caravan leader who has crossed every major trade route.'
			' Delphi\'s maps are etched into metal plates to survive harsh travel.'
			' She treats negotiation like a battlefield—calculated, decisive, and fair.'
		)
	},
	{
		'npc_id': 'trail_reader_vexa',
		'name': 'Vexa the Trail‑Reader',
		'description': (
			'A nomadic tracker who reads "wind scars" left by migrating beasts. '
			'Vexa senses disturbances in herd patterns long before they surface.'
		)
	},
	{
		'npc_id': 'hollow_runner',
		'name': 'Hollow Runner',
		'description': (
			'A swift, echoing apparition formed from the memory of stampedes.'
		)
	},
	{
		'npc_id': 'windcarve_spirit',
		'name': 'Windcarve Spirit',
		'description': (
			'A swirling presence shaped from carved tunnels and ancient wind currents.'
		)
	}
]


NPC_DIALOG = [

	{
		'npc_id': 'keeper_savran',
		'dialog_id': 'savran_intro',
		'dialog': [
			"The plains are uneasy. Even the docile beasts bare their teeth.",
			"Something ancient prowls the wind — a force that drives creatures wild.",
			"If we don't stop it, the grasslands will tear themselves apart."
		]
	},
	{
		'npc_id': 'waymaster_delphi',
		'dialog_id': 'delphi_intro',
		'dialog': [
			"Caravans vanish without a trace.",
			"The wind carries roars that don't belong to any living creature.",
			"Whatever's out there is disrupting every route I know."
		]
	},
	{
		'npc_id': 'trail_reader_vexa',
		'dialog_id': 'vexa_intro',
		'dialog': [
			"The wind scars tell a story of frenzy.",
			"Herds stampede in patterns no beast would choose.",
			"A Steppe‑Spirit wakes — hungry for motion, hungry for chaos."
		]
	},
	{
		'npc_id': 'hollow_runner',
		'dialog_id': 'hollow_runner_intro',
		'dialog': [
			"The Hollows echo with thunderous hooves.",
			"The Steppe's breath stirs the earth.",
			"It waits deeper within the wind‑carved tunnels."
		]
	},
	{
		'npc_id': 'windcarve_spirit',
		'dialog_id': 'windcarve_spirit_intro',
		'dialog': [
			"The Den howls with ancient fury.",
			"The Roaring Steppe gathers strength.",
			"Only its heart remains to be stilled."
		]
	},
	{
		'npc_id': 'keeper_savran',
		'dialog_id': 'savran_closing',
		'dialog': [
			"The plains calm. The beasts breathe easy again.",
			"You've tamed a force older than any creature I've known.",
			"The grasslands owe you their peace."
		]
	},

]


TASKS = [
	{
		'task_id': 'grassland_large_city_initialize',
		'type': 'complete_intro_story',	
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'keeper_savran',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'keeper_savran',
					'standing_text': [
						"I've seen beasts you'd never believe — sit and I'll tell you their names."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'waymaster_delphi',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'waymaster_delphi',
					'standing_text': [
						"Travelers bring tales — share one and I'll show you a path worth taking."
					]
				}
			},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_large_city_regional_complete_gate' }},
		]
	},
	{
		'task_id': 'grassland_large_city_regional_complete_gate',
		'type': 'complete_regional_quests',
		'task_acquire_events': [],
		'task_complete_events': [
			# C chain — gated by chapter 10 being reached
			# Place Voss and set her standing text so she is ready for the meet task
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'voss_caldera',
					'location': 'region_city_other3'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'voss_caldera',
					'standing_text': [
						"I don't have time for pleasantries.",
						"If you have something useful to offer, say it."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_large_city_type_c_find_voss'
				}
			},
			# D chain — trigger item (grassland_large_city_accessory_key) placed in
			# nobles_mansion_ch3 dungeon via dungeon_add_treasure in main_story_chapter_3.py.
			# Deliver task awarded here; it waits until the player recovers the key.
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"That key — the wind impressions on it are extraordinary.",
						"Someone mapped every grassland migration into this metal.",
						"Find Vexa. She reads wind scars better than anyone.",
						"She'll know what it opens."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_large_city_type_d_deliver_accessory_key'
				}
			},
		]
	},
]


# ── Type C ── Voss Caldera (extended character, slot 1) ───────────────────────
# Voss arrives at the Bazaar on business but
# recognises the party's capability. Delphi's endorsement earns her trust.
# Voss is placed and given initial standing text in regional_complete_gate.

NPC_DIALOG += [

	{
		'npc_id': 'voss_caldera',
		'dialog_id': 'voss_c_first_meet',
		'dialog': [
			"I'm here on business, not sentiment.",
			"The Bazaar's route network is collapsing and nobody in charge seems to care.",
			"I've been watching your party.",
			"You solve problems efficiently. That's rare.",
			"But I don't travel with strangers. Impress someone I trust first."
		]
	},
	{
		'npc_id': 'waymaster_delphi',
		'dialog_id': 'delphi_c_vouch',
		'dialog': [
			"Voss Caldera — she doesn't endorse anyone lightly.",
			"But she asked about you. That means something.",
			"Tell her I said the routes are safer since you arrived.",
			"That's the only currency she respects."
		]
	},
	{
		'npc_id': 'voss_caldera',
		'dialog_id': 'voss_c_joins',
		'dialog': [
			"Delphi called the routes safer.",
			"She doesn't exaggerate. Ever.",
			"Fine. I'm in.",
			"But I set the terms when we negotiate — understood?"
		]
	},

]

# --- Character dialogs: Type C ---
NPC_DIALOG += [

    # Type C – Find Voss
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_grassland_large_c_find_voss',
        'dialog': [
            "She's watching the route network collapse and nobody in charge seems to care. Fair."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_grassland_large_c_find_voss',
        'dialog': [
            "She doesn't travel with strangers. Impress someone she trusts first. Efficient filter."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_grassland_large_c_find_voss',
        'dialog': [
            "Business, not sentiment. I can work with that."
        ]
    },

    # Type C – Consult Delphi
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_grassland_large_c_consult_delphi',
        'dialog': [
            "Delphi doesn't waste words. If she says the routes are safer, that's the only currency Voss respects."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_grassland_large_c_consult_delphi',
        'dialog': [
            "Confirmation from someone she already trusts. Clean."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_grassland_large_c_consult_delphi',
        'dialog': [
            "Some people only move when the right person speaks for you."
        ]
    },

    # Type C – Earn Voss
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_grassland_large_c_earn_voss',
        'dialog': [
            "She's in. And she sets the terms when we negotiate. Understood."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_grassland_large_c_earn_voss',
        'dialog': [
            "Delphi called the routes safer. She doesn't exaggerate. That was enough."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_grassland_large_c_earn_voss',
        'dialog': [
            "Good. Let's get to work."
        ]
    },

]

# --- Character dialogs: Type D ---
NPC_DIALOG += [

    # Type D – Deliver Accessory Key
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_grassland_large_d_deliver_accessory_key',
        'dialog': [
            "Wind impressions mapped into metal. Someone catalogued every grassland migration into this key."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_grassland_large_d_deliver_accessory_key',
        'dialog': [
            "Vexa reads wind scars better than anyone. She'll know what it opens."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_grassland_large_d_deliver_accessory_key',
        'dialog': [
            "The wind already shifted when we crossed the plains. Something is listening."
        ]
    },

    # Type D – Consult Vexa
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_grassland_large_d_consult_vexa',
        'dialog': [
            "The noble's lineage mapped every migration across the grasslands. The Windcarve Spirit hoards the oldest of those routes."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grmnaw_grassland_large_d_consult_vexa',
        'dialog': [
            "Unlock the chamber and the routes crystallize. Mira can set wind-crystal into something that reads the air."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_grassland_large_d_consult_vexa',
        'dialog': [
            "You'll feel ambushes before they form. That's worth the risk."
        ]
    },

    # Type D – Meet Windcarve Spirit
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_grassland_large_d_meet_windcarve_spirit',
        'dialog': [
            "It already decided we won't leave with the routes."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_grassland_large_d_meet_windcarve_spirit',
        'dialog': [
            "Guarded since the first caravan crossed these plains. Ambitious tenure."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_grassland_large_d_meet_windcarve_spirit',
        'dialog': [
            "It's not protecting paths. It's protecting the right to decide who gets to walk them."
        ]
    },

    # Type D – Defeat Windcarve Spirit
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_grassland_large_d_defeat_windcarve_spirit',
        'dialog': [
            "It's down. Take the wind-crystal."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_grassland_large_d_defeat_windcarve_spirit',
        'dialog': [
            "A mantle that reads the air around you. You'll sense what's coming before it arrives."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_grassland_large_d_defeat_windcarve_spirit',
        'dialog': [
            "Every migration route the Spirit hoarded has returned to the plains. The caravans can move freely again."
        ]
    },

]

# --- Character dialogs: Type B ---
NPC_DIALOG += [

    # B – Meet Serene
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_grassland_large_b_meet_serene',
        'dialog': [
            "She predicted we'd come. Of course she did."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_grassland_large_b_meet_serene',
        'dialog': [
            "Don't let her voice get inside your head — she'll use your own words against you."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_grassland_large_b_meet_serene',
        'dialog': [
            "She's catalogued every pattern we carry. She thinks that means she owns the next move."
        ]
    },

    # B – Defeat Serene
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_grassland_large_b_defeat_serene',
        'dialog': [
            "Stay down. The future doesn't belong to you."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_grassland_large_b_defeat_serene',
        'dialog': [
            "The wind sounds like itself again. Not recorded. Not archived. Just the wind."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_grassland_large_b_defeat_serene',
        'dialog': [
            "You can't steal something that won't hold still. She never understood that."
        ]
    },

]

TASKS += [

	# =========================================================
	# TYPE C — Voss Caldera (extended character, slot 1)
	# Awarded by: grassland_large_city_regional_complete_gate (conditional)
	# Chain: find Voss → Delphi vouches → return to Voss → Voss joins
	# Voss placed in regional_complete_gate complete events.
	# =========================================================

	# C-1 — Voss introduces herself and directs the party to Delphi
	{
		'task_id': 'grassland_large_city_type_c_find_voss',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'voss_caldera',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'voss_caldera',
					'dialog_id': 'voss_c_first_meet'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_grassland_large_c_find_voss' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_grassland_large_c_find_voss'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg',     'dialog_id': 'bragg_grassland_large_c_find_voss'     } },
			# Prime Delphi's standing text before the party goes to her
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'waymaster_delphi',
					'standing_text': [
						"Voss sent you? Then she's already decided — she just wants confirmation.",
						"I'll give it."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_large_city_type_c_consult_delphi'
				}
			},
		]
	},

	# C-2 — Delphi vouches and points the party back to Voss
	{
		'task_id': 'grassland_large_city_type_c_consult_delphi',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'waymaster_delphi',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'waymaster_delphi',
					'dialog_id': 'delphi_c_vouch'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'tech_grassland_large_c_consult_delphi'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_grassland_large_c_consult_delphi' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_grassland_large_c_consult_delphi'   } },
			# Update Voss's standing text so she signals she is ready
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'voss_caldera',
					'standing_text': [
						"Delphi spoke for you.",
						"She doesn't waste words. Neither will I.",
						"Let's get to work."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_large_city_type_c_earn_voss'
				}
			},
		]
	},

	# C-3 — Return to Voss; she joins the party
	{
		'task_id': 'grassland_large_city_type_c_earn_voss',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'voss_caldera',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'voss_caldera',
					'dialog_id': 'voss_c_joins'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_grassland_large_c_earn_voss' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_grassland_large_c_earn_voss'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg',     'dialog_id': 'bragg_grassland_large_c_earn_voss'     } },
			{
				'event_type': 'hide_npc',
				'params': { 'npc_id': 'voss_caldera' }
			},
			{
				'event_type': 'character_join',
				'params': {
					'character_id': 'voss_caldera'
				}
			},
		]
	},

]


# ── Type D ── Windcarver's Mantle (mythic accessory, slot 2) ──────────────────
# Gate: grassland_large_city_accessory_key placed in nobles_mansion_ch3 (Ch.3 dungeon).
# Deliver to Mira → Vexa reads the key → defeat Windcarve Spirit → mythic accessory.
# No new NPCs — trail_reader_vexa and windcarve_spirit are both in the city NPCS list.
# Mira's standing text and the deliver award_task fire from regional_complete_gate.
# Vexa placed in deliver complete events; windcarve_spirit placed in consult_vexa complete events.

NPC_DIALOG += [

	{
		'npc_id': 'trail_reader_vexa',
		'dialog_id': 'vexa_d_key_read',
		'dialog': [
			"This key carries wind-route impressions from somewhere far to the south.",
			"The noble's estate — their lineage mapped every migration across the grasslands.",
			"The Windcarve Spirit hoards the oldest of those routes.",
			"Unlock its chamber with this key and the routes crystallize into something tangible.",
			"Mira can set wind-crystal into an accessory that reads the air around you.",
			"You'll feel ambushes before they form."
		]
	},
	{
		'npc_id': 'windcarve_spirit',
		'dialog_id': 'windcarve_spirit_d_awakens',
		'dialog': [
			"The estate key opens my den.",
			"You carry the migration routes I have guarded since the first caravan crossed these plains.",
			"You will not leave with them."
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE D — Windcarver's Mantle (mythic accessory, slot 2)
	# Gate: grassland_large_city_accessory_key (nobles_mansion_ch3, Ch.3)
	# Mythic reward: mythic_grassland_large_windcarvers_mantle
	# Awarded by: grassland_large_city_regional_complete_gate (deliver task waits for item)
	# =========================================================

	# D-0 — Deliver key to Mira; she directs the party to Vexa
	{
		'task_id': 'grassland_large_city_type_d_deliver_accessory_key',
		'type': 'deliver',
		'item_id': 'grassland_large_city_accessory_key',
		'to_type': 'npc',
		'to_id': 'mira',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'grassland_large_city_accessory_key'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'tech_grassland_large_d_deliver_accessory_key'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_grassland_large_d_deliver_accessory_key' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_grassland_large_d_deliver_accessory_key'   } },
			# Place Vexa and set her standing text for the consult step
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'trail_reader_vexa',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'trail_reader_vexa',
					'standing_text': [
						"The wind scars shifted the moment you crossed the plains.",
						"That key you carry — it speaks to every migration I've ever tracked.",
						"Come. The Windcarve Den is stirring."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_large_city_type_d_consult_vexa'
				}
			},
		]
	},

	# D-1 — Vexa reads the wind-route impressions on the key
	{
		'task_id': 'grassland_large_city_type_d_consult_vexa',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'trail_reader_vexa',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'trail_reader_vexa',
					'dialog_id': 'vexa_d_key_read'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_grassland_large_d_consult_vexa'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grmnaw_grassland_large_d_consult_vexa' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',     'dialog_id': 'nia_grassland_large_d_consult_vexa'     } },
			# Place the Windcarve Spirit and set standing text for the meet step
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'windcarve_spirit',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'windcarve_spirit',
					'standing_text': [
						"A deep roar rises from the Windcarve tunnels.",
						"Savran says the beasts refuse to graze near the entrance.",
						"The estate key has awakened whatever sleeps inside."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_large_city_type_d_meet_windcarve_spirit'
				}
			},
		]
	},

	# D-2 — Meet the Windcarve Spirit; it reveals what it guards
	{
		'task_id': 'grassland_large_city_type_d_meet_windcarve_spirit',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'windcarve_spirit',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'windcarve_spirit',
					'dialog_id': 'windcarve_spirit_d_awakens'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',  'dialog_id': 'skill_grassland_large_d_meet_windcarve_spirit'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_grassland_large_d_meet_windcarve_spirit'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',  'dialog_id': 'lyren_grassland_large_d_meet_windcarve_spirit'  } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_large_city_type_d_defeat_windcarve_spirit'
				}
			},
		]
	},

	# D-3 — Defeat the Windcarve Spirit; Mira crafts the mythic accessory
	{
		'task_id': 'grassland_large_city_type_d_defeat_windcarve_spirit',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'windcarve_spirit_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'windcarve_spirit_1',
					'combat_type': 'boss_battle'
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_grassland_large_windcarvers_mantle'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_grassland_large_d_defeat_windcarve_spirit' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_grassland_large_d_defeat_windcarve_spirit'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',       'dialog_id': 'nia_grassland_large_d_defeat_windcarve_spirit'       } },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"Wind-crystal — I've heard of it but never worked with it.",
						"I've set it into the mantle.",
						"It reads the air around you.",
						"You'll sense what's coming before it arrives."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'trail_reader_vexa',
					'standing_text': [
						"The wind scars are clean again.",
						"Every migration route the Spirit hoarded has returned to the plains.",
						"Delphi's caravans can move freely."
					]
				}
			},
		]
	},

]


# ── Type B ── Nia / Serene the Whisper-Thief (regional character quest) ───────
# Gated by Ch.20 Void Gauntlet. Awarded externally from main_story_chapter_20.py
# when the Void Gauntlet event fires — not from this file's regional gate.
# grassland_large_city_b_void_gauntlet will show TASK_UNREACHABLE until Ch.20 is updated.

NPC_DIALOG += [

	{
		'npc_id': 'nia',
		'dialog_id': 'nia_b_echo_resonance',
		'dialog': [
			"Okay. Okay, this is interesting.",
			"The wind here? It's full of us. Our voices. Things we said months ago.",
			"Serene's been harvesting echoes from every city we've passed through.",
			"She's building something — a map of who we are so she can predict us.",
			"(grinning, but the grin doesn't reach her eyes) Not on my watch.",
			"I know her patterns. I grew up in them.",
			"We find her vault. We take it apart. We make sure she never gets the wind back."
		]
	},
	{
		'npc_id': 'nia',
		'dialog_id': 'nia_b_entering_vault',
		'dialog': [
			"There. The echoes are louder in here.",
			"Don't let her voice get inside your head — she'll use your own words against you.",
			"I've had years of practice ignoring her. You'll be fine. Probably."
		]
	},
	{
		'npc_id': 'serene',
		'dialog_id': 'serene_b_risen',
		'dialog': [
			"You came exactly when I predicted.",
			"I have catalogued every pattern you carry.",
			"Every word. Every choice. I know what you will say next.",
			"I know because I stole it from the wind you breathed.",
			"You cannot surprise what already owns your future."
		]
	},
	{
		'npc_id': 'nia',
		'dialog_id': 'nia_b_victory',
		'dialog': [
			"The wind sounds like itself again.",
			"Not recorded. Not archived. Just... the wind.",
			"(quietly) She always said she owned the future.",
			"But she never understood that the future moves.",
			"You can't steal something that won't hold still.",
			"(takes a breath) I think I finally believe that."
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE B — Nia / Serene the Whisper-Thief (regional character quest, slot 3)
	# Gated by Ch.20 Void Gauntlet — awarded from main_story_chapter_20.py externally.
	# grassland_large_city_b_void_gauntlet is the entry task; TASK_UNREACHABLE is expected
	# until Ch.20 is updated to award it.
	# =========================================================

	# B-0 — Void Gauntlet entry (awarded by Ch.20 externally)
	{
		'task_id': 'grassland_large_city_b_void_gauntlet',
		'type': 'gated',
		'task_acquire_events': [
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'serenes_wind_vault', 'location': 'region_open_area' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_b_echo_resonance' }},
			{ 'event_type': 'complete_task', 'params': { 'task_id': 'grassland_large_city_b_void_gauntlet' }},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_large_city_b_meet_serene' }},
		]
	},

	# B-1 — Meet Serene (boss intro)
	{
		'task_id': 'grassland_large_city_b_meet_serene',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'serene',
		'task_acquire_events': [
			{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'serenes_wind_vault', 'location': 'final_chamber' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_b_entering_vault' }},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'serene', 'dialog_id': 'serene_b_risen' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_grassland_large_b_meet_serene' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',       'dialog_id': 'nia_grassland_large_b_meet_serene'       } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_grassland_large_b_meet_serene'      } },
			{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_large_city_b_defeat_serene' }},
		]
	},

	# B-2 — Defeat Serene
	{
		'task_id': 'grassland_large_city_b_defeat_serene',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'serene_b1',
		'task_acquire_events': [
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'serene_b1', 'combat_type': 'boss_battle' }},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_b_victory' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_grassland_large_b_defeat_serene' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',       'dialog_id': 'nia_grassland_large_b_defeat_serene'       } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',     'dialog_id': 'faith_grassland_large_b_defeat_serene'     } },
			{ 'event_type': 'complete_regional_quest_2', 'params': { 'region_id': 'grassland' }},
		]
	},

]


PRIMARY_STORY_SETTINGS = {
	'story_id': 'grassland_large_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}