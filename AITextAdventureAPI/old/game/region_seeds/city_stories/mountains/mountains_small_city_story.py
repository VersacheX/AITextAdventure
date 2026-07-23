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
			"The hollow can breathe again."
		]
	},

]

NPC_DIALOG += [

	# ── Type C dialogs — Vorn Ashpike ───────────────────────────────

	{
		'npc_id': 'vorn_ashpike',
		'dialog_id': 'vorn_c_first_meet',
		'dialog': [
			"I've seen too many outsiders come through looking for glory in the tunnels.",
			"I stay because the hollow needs someone who knows its moods.",
			"Give me one good reason to walk out of it with you."
		]
	},
	{
		'npc_id': 'forgehand_belkan',
		'dialog_id': 'belkan_c_vouch',
		'dialog': [
			"Vorn is stubborn as cold iron — but his instincts have kept this hollow standing.",
			"Tell him I sent you and that the resonance work is real.",
			"That's the only currency he'll accept."
		]
	},
	{
		'npc_id': 'vorn_ashpike',
		'dialog_id': 'vorn_c_joins',
		'dialog': [
			"Belkan doesn't vouch for fools.",
			"If the shard work is as serious as he says, you'll need someone who knows what lives in the deep.",
			"I'm in — but we do this right."
		]
	},

]

NPC_DIALOG += [

	# ── Type D dialogs — Dominion Edge ─────────────────────────────

	{
		'npc_id': 'forgehand_belkan',
		'dialog_id': 'belkan_d_weapon_key',
		'dialog': [
			"A Hollow Dominion Key… this was forged before the Fellowship existed.",
			"It doesn't open a lock. It opens a claim.",
			"There is a blade sleeping in the deep stone — the Dominion Edge.",
			"Speak to Korla. She knows the descent path."
		]
	},
	{
		'npc_id': 'marshal_korla',
		'dialog_id': 'korla_d_descent',
		'dialog': [
			"The key resonates with the deepest fault-line.",
			"The Dominion Edge has been down there since before any map I carry.",
			"Thalric must perform the rite to wake it — but the guardian will answer first."
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
			"The forge-heat steadied when you returned.",
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
						"I've walked dark tunnels for years—sit and share a watch, and I'll share what I've learned."
					]
				}
			},
		],
		'task_complete_events': [
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
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_c_find_lira'
				},
				'condition': {
					'type': 'is_chapter_gte',
					'params': { 'chapter': 21 }
				}
			}
		]
	},
]

TASKS += [

	# =========================================================
	# TYPE E — Forge Dominion Shard
	# Artifact ID: forge_dominion_shard
	# Gates: mountains_small_city Type D (slot 3, this file)
	# Awarded by: mountains_small_city_initialize
	# =========================================================

	{
		'task_id': 'mountains_small_city_type_e_investigate_resonance',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'forgehand_belkan',
		'task_acquire_events': [
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'forgehand_belkan',
					'dialog_id': 'belkan_e_resonance'
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
	{
		'task_id': 'mountains_small_city_type_e_consult_thalric',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'depth_seer_thalric',
		'task_acquire_events': [
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
		],
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
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE C — Vorn Ashpike (extended character)
	# Gated by is_chapter_gte: 21
	# Awarded by: mountains_small_city_initialize (conditional)
	# =========================================================

	{
		'task_id': 'mountains_small_city_type_c_find_vorn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'vorn_ashpike',
		'task_acquire_events': [
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
						"I keep to myself. The hollow gives me everything I need.",
						"Unless you've got a real reason to talk, move along."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vorn_ashpike',
					'dialog_id': 'vorn_c_first_meet'
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
					'dialog_id': 'belkan_c_vouch'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_c_earn_vorn'
				}
			},
		]
	},
	{
		'task_id': 'mountains_small_city_type_c_earn_vorn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'vorn_ashpike',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'vorn_ashpike',
					'standing_text': [
						"Belkan sent you back.",
						"That means something. Let's talk."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vorn_ashpike',
					'dialog_id': 'vorn_c_joins'
				}
			},
			{
				'event_type': 'add_extended_character',
				'params': {
					'character_id': 'vorn_ashpike'
				}
			},
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE D — Mythic Equipment Quest (slot 3)
	# Gate: mountains_small_city_weapon_key (from trial_1_dungeon, Ch.21)
	# Mythic reward: mythic_mountains_small_dominion_edge (weapon → Diego)
	# =========================================================

	{
		'task_id': 'mountains_small_city_type_d_deliver_weapon_key',
		'type': 'deliver',
		'item_id': 'mountains_small_city_weapon_key',
		'to_type': 'npc',
		'to_id': 'forgehand_belkan',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'forgehand_belkan',
					'dialog_id': 'belkan_d_weapon_key'
				}
			},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'mountains_small_city_weapon_key'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_d_consult_korla'
				}
			}
		]
	},
	{
		'task_id': 'mountains_small_city_type_d_consult_korla',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'marshal_korla',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'marshal_korla',
					'standing_text': [
						"That key hums against my maps.",
						"I know what it wants. Come — I'll show you the descent path."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'marshal_korla',
					'dialog_id': 'korla_d_descent'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_d_meet_dominion_guardian'
				}
			}
		]
	},
	{
		'task_id': 'mountains_small_city_type_d_meet_dominion_guardian',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'depth_seer_thalric',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'depth_seer_thalric',
					'standing_text': [
						"The fault-echoes confirm the blade's location.",
						"The guardian stirs already. I'll perform the rite — you face what answers."
					]
				}
			}
		],
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
			}
		]
	},
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
			}
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
			}
		]
	},

]


TASKS += [

	# =========================================================
	# TYPE C — Lira Emberforge (extended character, slot 2)
	# Gated by is_chapter_gte: 21
	# Awarded by: mountains_small_city_initialize (conditional)
	# =========================================================

	{
		'task_id': 'mountains_small_city_type_c_find_lira',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'forgehand_belkan',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'forgehand_belkan',
					'standing_text': [
						"There's a smith at the secondary forge I didn't hire.",
						"Her work is unlike anything I've seen.",
						"Korla checked her out. Come — I'll explain."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'forgehand_belkan',
					'dialog_id': 'belkan_c_lira_sighting'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_small_city_type_c_consult_korla'
				}
			},
		]
	},
	{
		'task_id': 'mountains_small_city_type_c_consult_korla',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'marshal_korla',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'marshal_korla',
					'standing_text': [
						"Belkan sent you about the smith.",
						"I've watched her work. I'll tell you what I know."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'marshal_korla',
					'dialog_id': 'korla_c_lira_vouch'
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
	{
		'task_id': 'mountains_small_city_type_c_earn_lira',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'lira_emberforge',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'lira_emberforge',
					'location': 'region_city_other1'
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
		],
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


PRIMARY_STORY_SETTINGS = {
	'story_id': 'mountains_small_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}