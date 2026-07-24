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
						"I've seen beasts you'd never believe—sit and I'll tell you their names."
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
						"Travelers bring tales—share one and I'll show you a path worth taking."
					]
				}
			},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_large_city_regional_complete_gate' }}
		]
	},
	{
		'task_id': 'grassland_large_city_regional_complete_gate',
		'type': 'complete_regional_quests',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_large_city_type_c_find_voss' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_large_city_type_d_deliver_accessory_key' }},
		]
	},
]


# ── Type C ── Voss Caldera (extended character) ───────────────────────────────
# Gated by is_chapter_gte: 10. Voss arrives at the Bazaar on business but
# recognises the party's capability. Delphi's endorsement earns her trust.

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

TASKS += [

	# C-1 — Find Voss Caldera
	{
		'task_id': 'grassland_large_city_type_c_find_voss',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'voss_caldera',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'voss_caldera',
					'location': 'region_city_other1'
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'voss_caldera',
					'dialog_id': 'voss_c_first_meet'
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

	# C-2 — Get Delphi's endorsement
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
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_large_city_type_c_earn_voss'
				}
			},
		]
	},

	# C-3 — Return to Voss; she joins
	{
		'task_id': 'grassland_large_city_type_c_earn_voss',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'voss_caldera',
		'task_acquire_events': [
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'voss_caldera',
					'dialog_id': 'voss_c_joins'
				}
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


# ── Type D ── Windcarver's Mantle (mythic accessory) ──────────────────────────
# Gate: player holds grassland_large_city_accessory_key from nobles_mansion (Ch.3 dungeon).
# Standalone deliver to Mira → Vexa reads the key → defeat Windcarve Spirit → mythic accessory.
# No new NPCs — uses trail_reader_vexa, windcarve_spirit, and mira (Ch.2 party anchor).

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

	# D-0 — Deliver grassland_large_city_accessory_key to Mira (standalone deliver; unlocks D chain)
	{
		'task_id': 'grassland_large_city_type_d_deliver_accessory_key',
		'type': 'deliver',
		'item_id': 'grassland_large_city_accessory_key',
		'to_type': 'npc',
		'to_id': 'mira',
		'task_acquire_events': [
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
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_large_city_type_d_consult_vexa'
				}
			},
		]
	},

	# D-1 — Consult Vexa for the wind-route reading
	{
		'task_id': 'grassland_large_city_type_d_consult_vexa',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'trail_reader_vexa',
		'task_acquire_events': [
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'trail_reader_vexa',
					'dialog_id': 'vexa_d_key_read'
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

	# D-2 — Meet the Windcarve Spirit (boss intro)
	{
		'task_id': 'grassland_large_city_type_d_meet_windcarve_spirit',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'windcarve_spirit',
		'task_acquire_events': [
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'windcarve_spirit',
					'dialog_id': 'windcarve_spirit_d_awakens'
				}
			},
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'windcarve_spirit_1',
					'combat_type': 'boss_encounter'
				}
			},
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
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_grassland_large_windcarvers_mantle'
				}
			},
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
# Gated by Ch.20 Void Gauntlet. Nia hears Serene's signal threading through
# the Crosswind Bazaar's updrafts — the Whisper-Thief is collecting echoes
# from the party's own past. Creates dungeon in open area.
# No new NPCs — uses initiate_character_dialog on Nia exclusively.

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

	# B-0 — Void Gauntlet entry (self-completing gated task)
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
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'serene', 'location': None }},
			{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'serenes_wind_vault', 'location': 'final_chamber' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_b_entering_vault' }},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'serene', 'dialog_id': 'serene_b_risen' }},
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'serene_b1', 'combat_type': 'boss_battle' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_large_city_b_defeat_serene' }},
		]
	},

	# B-2 — Defeat Serene
	{
		'task_id': 'grassland_large_city_b_defeat_serene',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'serene_b1',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_b_victory' }},
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