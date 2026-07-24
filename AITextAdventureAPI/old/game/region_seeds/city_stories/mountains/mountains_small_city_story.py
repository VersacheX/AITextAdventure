ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'forgehand_belkan',
		'name': 'Belkan Forgehand',
		'description': (
			'A master smith who trains apprentices in the Fellowship\'s traditions.'
			' Belkan\'s hammer strikes ring with rhythmic precision.'
			' He believes metal reveals its true nature only under pressure.'
		)
	},
	{
		'npc_id': 'marshal_korla',
		'name': 'Korla Deepdelve',
		'description': (
			'A disciplined marshal who organizes expeditions into the mountain depths.'
			' Korla\'s armor is etched with maps of tunnels long since collapsed.'
			' She carries herself with the confidence of someone who has survived the dark.'
		)
	},
	{
		'npc_id': 'depth_seer_thalric',
		'name': 'Thalric the Depth‑Seer',
		'description': (
			'A tunnel mystic who reads fault‑echoes and senses disturbances in the deep stone.'
		)
	},
	{
		'npc_id': 'vorn_ashpike',
		'name': 'Vorn Ashpike',
		'description': (
			'A seasoned tunnel-runner who knows every mood and creak of the hollow.'
			' Stubborn as cold iron, but his instincts have kept the village standing.'
		)
	},
]


NPC_DIALOG = [

	{
		'npc_id': 'forgehand_belkan',
		'dialog_id': 'belkan_intro',
		'dialog': [
			"The forge cools too quickly.",
			"Heat drains into the stone like it's being stolen.",
			"Something below hungers for fire and metal."
		]
	},
	{
		'npc_id': 'marshal_korla',
		'dialog_id': 'korla_intro',
		'dialog': [
			"Tunnels collapse in deliberate patterns.",
			"Something shifts the stone with intent.",
			"If we don't act, the depths will swallow the village."
		]
	},
	{
		'npc_id': 'depth_seer_thalric',
		'dialog_id': 'thalric_intro',
		'dialog': [
			"The fault‑echoes tremble.",
			"A forge‑spirit stirs — the Ashen Anvil.",
			"If it rises, all metal will bend to its will."
		]
	},

]

NPC_DIALOG += [

	# ── Type E dialogs — Forge Dominion Shard ──────────────────────

	{
		'npc_id': 'forgehand_belkan',
		'dialog_id': 'belkan_e_resonance',
		'dialog': [
			"This shard hums with a resonance I've never felt in raw ore.",
			"The pattern etched into it — it matches marks we found on collapsed tunnel walls.",
			"Someone or something drove it deep into the stone. Deliberately."
		]
	},
	{
		'npc_id': 'depth_seer_thalric',
		'dialog_id': 'thalric_e_reading',
		'dialog': [
			"The shard is a dominion anchor.",
			"Whoever placed it claimed authority over the forge‑heat in this range.",
			"That claim must be dissolved before it spreads deeper."
		]
	},
	{
		'npc_id': 'marshal_korla',
		'dialog_id': 'korla_e_closing',
		'dialog': [
			"The resonance has quieted.",
			"Whatever hold that shard had on the tunnels — it's broken.",
			"The hollow can breathe again.",
			"Hold onto it. Something that strong doesn't stop being useful."
		]
	},

]

NPC_DIALOG += [

	# ── Type C dialogs — Lira Emberforge ───────────────────────────

	{
		'npc_id': 'vorn_ashpike',
		'dialog_id': 'vorn_c_lira_sighting',
		'dialog': [
			"Someone lit the secondary forge three nights ago.",
			"I didn't hire them. Belkan didn't either.",
			"The lock didn't stop them — and the work they left behind is nothing I've seen.",
			"Not hollow technique. Not foundry style.",
			"Go ask Belkan. He looked closer than I did."
		]
	},
	{
		'npc_id': 'forgehand_belkan',
		'dialog_id': 'belkan_c_lira_vouch',
		'dialog': [
			"She appeared without introduction and asked to use the secondary forge.",
			"I said no. She worked it anyway.",
			"Her welds are flawless — not trained, innate.",
			"The ore remembers her touch differently than anyone I've ever watched.",
			"I've asked around. No one in the hollow knows her name.",
			"She's still there. Go find out who she is."
		]
	},
	{
		'npc_id': 'lira_emberforge',
		'dialog_id': 'lira_c_first_meet',
		'dialog': [
			"The ore remembers everything that's been done to it.",
			"I read what others leave behind.",
			"Your party carries forge-heat that doesn't match any range I've worked.",
			"(sets down her hammer)",
			"That's interesting.",
			"Say what you came to say."
		]
	},
	{
		'npc_id': 'lira_emberforge',
		'dialog_id': 'lira_c_joins',
		'dialog': [
			"I've stayed here long enough to read everything this hollow holds.",
			"Whatever your party carries — I haven't read that yet.",
			"I'll come.",
			"Don't explain it. I'll understand it when I understand it."
		]
	},

]

NPC_DIALOG += [

	# ── Type D dialogs — Dominion Edge (mythic weapon) ─────────────

	{
		'npc_id': 'forgehand_belkan',
		'dialog_id': 'belkan_d_shard_receipt',
		'dialog': [
			"The Dominion Hollow was guarding this for a reason.",
			"This shard — I've read its resonance pattern before.",
			"There is a blade in the deep fault-line that was forged when this was placed.",
			"They're linked. The shard is its key.",
			"Korla knows the descent path. Move — the resonance won't hold long."
		]
	},
	{
		'npc_id': 'marshal_korla',
		'dialog_id': 'korla_d_descent',
		'dialog': [
			"The shard resonates against every map I carry.",
			"The Dominion Edge has been below since before any tunnel I've charted.",
			"Thalric must perform the rite to wake it — but its guardian will answer first."
		]
	},
	{
		'npc_id': 'depth_seer_thalric',
		'dialog_id': 'thalric_d_rite',
		'dialog': [
			"The fault-echoes confirm it. The blade is real.",
			"The Dominion Hollow was its keeper. You've already broken it once.",
			"This time it guards the blade itself. It won't hold back."
		]
	},
	{
		'npc_id': 'forgehand_belkan',
		'dialog_id': 'belkan_d_reward',
		'dialog': [
			"The forge-heat steadied the moment you returned.",
			"The Dominion Edge chose you — I felt it from the anvil.",
			"Carry it with the weight it deserves."
		]
	},

]


TASKS = [
	{
		'task_id': 'mountains_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'forgehand_belkan',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'forgehand_belkan',
					'standing_text': [
						"The anvil sings; rest your feet and tell me where the road has taken you."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'marshal_korla',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'marshal_korla',
					'standing_text': [
						"I've walked dark tunnels for years — sit and share a watch, and I'll share what I've learned."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'vorn_ashpike',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'vorn_ashpike',
					'standing_text': [
						"The hollow keeps its own counsel.",
						"Most visitors don't stay long enough to hear it."
					]
				}
			},
		],
		'task_complete_events': [
			# Prompt Belkan toward the E chain immediately on city arrival
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'forgehand_belkan',
					'standing_text': [
						"Something embedded in the deep ore is pulling at the forge heat.",
						"I've seen nothing like it. Come — look at what we pulled from the wall."
					]
				}
			},
			# Prompt Vorn toward the C chain (Lira sighting)
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'vorn_ashpike',
					'standing_text': [
						"Someone lit the secondary forge last night.",
						"I didn't hire them. Neither did Belkan."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_e_investigate_resonance'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_c_find_vorn'
				},
				'condition': {
					'type': 'is_chapter_gte',
					'params': { 'chapter': 21 }
				}
			},
		]
	},
]

TASKS += [

	# =========================================================
	# TYPE E — Forge Dominion Shard
	# Artifact ID: forge_dominion_shard
	# Gates: mountains_small_city Type D (slot 3, this file — same city pair)
	# Awarded by: mountains_small_city_initialize
	# Chain: investigate with Belkan → consult Thalric → defeat Dominion Hollow
	# No create_dungeon — NPC-driven chain per Type E rules.
	# =========================================================

	# E-1 — Belkan shows the party the shard in the ore wall
	{
		'task_id': 'mountains_small_city_type_e_investigate_resonance',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'forgehand_belkan',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'forgehand_belkan',
					'dialog_id': 'belkan_e_resonance'
				}
			},
			# Spawn Thalric here so his standing text is ready before the meet task
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'depth_seer_thalric',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'depth_seer_thalric',
					'standing_text': [
						"The fault‑lines carry a foreign intent.",
						"Seek me on the ridge — I can read what was placed here."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_e_consult_thalric'
				}
			},
		]
	},

	# E-2 — Thalric identifies the shard as a dominion anchor
	{
		'task_id': 'mountains_small_city_type_e_consult_thalric',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'depth_seer_thalric',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'depth_seer_thalric',
					'dialog_id': 'thalric_e_reading'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_e_defeat_dominion_hollow'
				}
			},
		]
	},

	# E-3 — Defeat the Dominion Hollow; claim the artifact
	{
		'task_id': 'mountains_small_city_type_e_defeat_dominion_hollow',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'dominion_hollow_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'dominion_hollow_1',
					'combat_type': 'elite_encounter'
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'forge_dominion_shard'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'marshal_korla',
					'dialog_id': 'korla_e_closing'
				}
			},
			# Gate D chain — E artifact is the trigger for the same-city D slot
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'forgehand_belkan',
					'standing_text': [
						"That shard you're carrying — the forge-resonance has shifted.",
						"Something below recognises it.",
						"We should talk."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_d_deliver_shard'
				}
			},
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE C — Lira Emberforge (extended character, slot 2)
	# Gated by is_chapter_gte: 21
	# Awarded by: mountains_small_city_initialize (conditional)
	# Chain: Vorn spots Lira → Belkan vouches → meet Lira → Lira joins
	# Only new NPC beyond city seed: lira_emberforge (extended character).
	# Vorn Ashpike is used as the discovery lead — city NPC, no character_join.
	# =========================================================

	# C-1 — Vorn tips off the party about the mystery smith
	{
		'task_id': 'mountains_small_city_type_c_find_vorn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'vorn_ashpike',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vorn_ashpike',
					'dialog_id': 'vorn_c_lira_sighting'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'forgehand_belkan',
					'standing_text': [
						"Vorn sent you about the smith at the secondary forge.",
						"I've been watching her work. Come — I'll tell you what I know."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_c_consult_belkan'
				}
			},
		]
	},

	# C-2 — Belkan vouches and points the party toward Lira; Lira is placed
	{
		'task_id': 'mountains_small_city_type_c_consult_belkan',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'forgehand_belkan',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'forgehand_belkan',
					'dialog_id': 'belkan_c_lira_vouch'
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'lira_emberforge',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'lira_emberforge',
					'standing_text': [
						"The ore here remembers things I didn't put into it.",
						"Come find me when you want to understand why."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_c_earn_lira'
				}
			},
		]
	},

	# C-3 — Meet Lira; she joins the party
	{
		'task_id': 'mountains_small_city_type_c_earn_lira',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'lira_emberforge',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'lira_emberforge',
					'dialog_id': 'lira_c_first_meet'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'lira_emberforge',
					'dialog_id': 'lira_c_joins'
				}
			},
			{
				'event_type': 'hide_npc',
				'params': { 'npc_id': 'lira_emberforge' }
			},
			{
				'event_type': 'character_join',
				'params': { 'character_id': 'lira_emberforge' }
			},
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE D — Dominion Edge (mythic weapon, slot 3)
	# Gate: forge_dominion_shard — awarded by E chain's defeat task (same city)
	# Mythic reward: mythic_mountains_small_dominion_edge
	# Chain: deliver shard to Belkan → consult Korla → meet Thalric → defeat guardian
	# No new NPCs — Belkan, Korla, and Thalric are all city seed NPCs.
	# Thalric is already placed by the E chain when D becomes available.
	# =========================================================

	# D-1 — Deliver the Forge Dominion Shard to Belkan; he recognises the deeper resonance
	{
		'task_id': 'mountains_small_city_type_d_deliver_shard',
		'type': 'deliver',
		'item_id': 'forge_dominion_shard',
		'to_type': 'npc',
		'to_id': 'forgehand_belkan',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'forgehand_belkan',
					'standing_text': [
						"That shard you're carrying — the forge-resonance has shifted.",
						"Something below recognises it.",
						"We should talk."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'forgehand_belkan',
					'dialog_id': 'belkan_d_shard_receipt'
				}
			},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'forge_dominion_shard'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'marshal_korla',
					'standing_text': [
						"That shard hums against my maps.",
						"I know what it wants. Come — I'll show you the descent path."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_d_consult_korla'
				}
			},
		]
	},

	# D-2 — Korla maps the descent to the Dominion Edge
	{
		'task_id': 'mountains_small_city_type_d_consult_korla',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'marshal_korla',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'marshal_korla',
					'dialog_id': 'korla_d_descent'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'depth_seer_thalric',
					'standing_text': [
						"The fault-echoes confirm the blade's location.",
						"The guardian stirs already. I'll perform the rite — you face what answers."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_d_meet_thalric'
				}
			},
		]
	},

	# D-3 — Thalric performs the rite; the guardian responds
	{
		'task_id': 'mountains_small_city_type_d_meet_thalric',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'depth_seer_thalric',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'depth_seer_thalric',
					'dialog_id': 'thalric_d_rite'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_d_defeat_dominion_guardian'
				}
			},
		]
	},

	# D-4 — Defeat the Dominion Guardian; claim the Dominion Edge
	{
		'task_id': 'mountains_small_city_type_d_defeat_dominion_guardian',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'deep_dominion_guardian_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'deep_dominion_guardian_1',
					'combat_type': 'boss_battle'
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'forgehand_belkan',
					'dialog_id': 'belkan_d_reward'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_mountains_small_dominion_edge'
				}
			},
		]
	},

]


PRIMARY_STORY_SETTINGS = {
	'story_id': 'mountains_small_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}