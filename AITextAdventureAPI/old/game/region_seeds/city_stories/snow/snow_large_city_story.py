ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'concordant_ivar',
		'name': 'Ivar the Concordant',
		'description': (
			'A stoic mediator who resolves disputes with icy calm.'
			'  Ivar\'s breath forms intricate frost patterns when he speaks.'
			'  He believes harmony is forged like ice—slowly, under pressure.'
		)
	},
	{
		'npc_id': 'artificer_lyndra',
		'name': 'Lyndra Frostlight',
		'description': (
			'A brilliant inventor who blends cold magic with delicate machinery.'
			'  Lyndra\'s creations glow with pale blue radiance.'
			'  She works tirelessly, claiming inspiration strikes like sudden snowfall.'
		)
	},
	{
		'npc_id': 'glacier_seer_thryna',
		'name': 'Thryna the Glacier‑Seer',
		'description': (
			'A mystic who reads ice harmonics and senses fractures before they form.'
		)
	}
]

NPC_DIALOG = [

	# ── Type A / intro dialogs ──────────────────────────────────────
	{
		'npc_id': 'concordant_ivar',
		'dialog_id': 'ivar_intro',
		'dialog': [
			"The frost patterns shift without cause.",
			"Harmony fractures beneath the ice.",
			"Something awakens in the deep cold."
		]
	},
	{
		'npc_id': 'artificer_lyndra',
		'dialog_id': 'lyndra_intro',
		'dialog': [
			"My machines hum out of tune.",
			"Cold magic splinters where it once flowed clean.",
			"If this continues, the city\'s frost‑engines will fail."
		]
	},
	{
		'npc_id': 'glacier_seer_thryna',
		'dialog_id': 'thryna_intro',
		'dialog': [
			"The ice harmonics tremble.",
			"A Fractured Chime rises — a spirit of broken harmony.",
			"If it awakens fully, the frost will turn against itself."
		]
	},
	{
		'npc_id': 'concordant_ivar',
		'dialog_id': 'ivar_closing',
		'dialog': [
			"The frost settles. Harmony returns.",
			"You\'ve stilled a discord older than the glacier itself.",
			"The Snowlands will remember your calm."
		]
	},

	# ── Type C dialogs — Lyric ──────────────────────────────────────
	{
		'npc_id': 'lyric',
		'dialog_id': 'lyric_intro',
		'dialog': [
			"You found me. Good. I wasn\'t sure I\'d put myself in a findable location.",
			"I\'ve been mapping the frost‑harmonic interference patterns.",
			"The maths are fascinating — everything here is breaking in a theoretically optimal way."
		]
	},
	{
		'npc_id': 'artificer_lyndra',
		'dialog_id': 'lyndra_lyric_consult',
		'dialog': [
			"Lyric? The theorist from the eastern cold-labs?",
			"If they say the pattern is solvable, it probably is.",
			"But you\'ll need to bring them proof before they\'ll commit. They don\'t trust observation alone."
		]
	},
	{
		'npc_id': 'lyric',
		'dialog_id': 'lyric_join',
		'dialog': [
			"You brought the data I asked for. And verified it independently.",
			"Thorough. Methodical. Rare.",
			"Fine. I\'ll come. Someone has to keep your conclusions honest."
		]
	},

	# ── Type D dialogs ──────────────────────────────────────────────
	{
		'npc_id': 'concordant_ivar',
		'dialog_id': 'ivar_armor_key',
		'dialog': [
			"An Armory Seal… this is from the Frostgate deep vaults.",
			"The old warplate locked inside hasn\'t been touched since the last glacier war.",
			"Speak to Lyndra — she knows the cold‑forging rites better than anyone."
		]
	},
	{
		'npc_id': 'artificer_lyndra',
		'dialog_id': 'lyndra_armor_ritual',
		'dialog': [
			"The Seal is authentic. The deep vault warplate is real.",
			"It\'s called the Frostgate Sovereign — forged from harmonized glacier-iron.",
			"Deliver the Seal to Thryna. She holds the unlocking rite."
		]
	},
	{
		'npc_id': 'glacier_seer_thryna',
		'dialog_id': 'thryna_armor_boss',
		'dialog': [
			"The Seal awakens the vault guardian.",
			"It will test whether you are worthy of the Sovereign.",
			"Survive, and the warplate is yours."
		]
	},
	{
		'npc_id': 'concordant_ivar',
		'dialog_id': 'ivar_armor_reward',
		'dialog': [
			"The guardian fell. The vault yields.",
			"The Frostgate Sovereign is yours — wear it as a promise.",
			"That armour has never known defeat. See that it still doesn\'t."
		]
	},
]

TASKS = [

	# ── Intro scaffold ───────────────────────────────────────────────
	{
		'task_id': 'snow_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'concordant_ivar',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'concordant_ivar',
					'standing_text': [
						"Calmness grows here — share a quarrel and I will help stitch it closed."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'artificer_lyndra',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'artificer_lyndra',
					'standing_text': [
						"My designs are born of frost — tell me a curious problem and I will sketch a solution."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_large_city_meet_ivar'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_large_city_type_c_find_lyric'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_large_city_type_d_deliver_armor_key'
				}
			}
		]
	},
	{
		'task_id': 'snow_large_city_meet_ivar',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'concordant_ivar',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'concordant_ivar',
					'standing_text': [
						"The frost patterns shift unpredictably.",
						"Something disturbs the harmony beneath the ice."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'concordant_ivar',
					'dialog_id': 'ivar_intro'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_large_city_meet_lyndra'
				}
			}
		]
	},
	{
		'task_id': 'snow_large_city_meet_lyndra',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'artificer_lyndra',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'artificer_lyndra',
					'dialog_id': 'lyndra_intro'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'artificer_lyndra',
					'standing_text': [
						"My machines hum out of tune.",
						"Cold magic fractures where it once flowed cleanly."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_large_city_find_thryna'
				}
			}
		]
	},
	{
		'task_id': 'snow_large_city_find_thryna',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'glacier_seer_thryna',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'glacier_seer_thryna',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'glacier_seer_thryna',
					'standing_text': [
						"The ice harmonics tremble.",
						"A Fractured Chime awakens beneath the frostline."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'glacier_seer_thryna',
					'dialog_id': 'thryna_intro'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'concordant_ivar',
					'dialog_id': 'ivar_closing'
				}
			},
			{
				'event_type': 'complete_regional_quests',
				'params': {
					'region_id': 'snow_large_city'
				}
			}
		]
	},

	# ── Type C — Lyric (extended character, slot 1) ───────────────────
	{
		'task_id': 'snow_large_city_type_c_find_lyric',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'lyric',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'lyric',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'lyric',
					'standing_text': [
						"The interference pattern has seventeen variables.",
						"I've collapsed it to three. Come back when you've verified the fourth."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'lyric',
					'dialog_id': 'lyric_intro'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_large_city_type_c_consult_lyndra'
				}
			},
		]
	},
	{
		'task_id': 'snow_large_city_type_c_consult_lyndra',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'artificer_lyndra',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'artificer_lyndra',
					'dialog_id': 'lyndra_lyric_consult'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_large_city_type_c_earn_lyric'
				}
			},
		]
	},
	{
		'task_id': 'snow_large_city_type_c_earn_lyric',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'lyric',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'lyric',
					'standing_text': [
						"You've spoken to Lyndra? Good.",
						"Then you understand what I need. Come and tell me what you found."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'lyric',
					'dialog_id': 'lyric_join'
				}
			},
			{
				'event_type': 'hide_npc',
				'params': { 'npc_id': 'lyric' }
			},
			{
				'event_type': 'character_join',
				'params': { 'character_id': 'lyric' }
			},
		]
	},

	# ── Type D — Mythic Equipment Quest (slot 2) ─────────────────────
	# Gate: snow_large_city_armor_key (from seraphine_glade, Ch.19)
	# Mythic reward: mythic_snow_large_frostgate_sovereign (armor → Brawn)
	{
		'task_id': 'snow_large_city_type_d_deliver_armor_key',
		'type': 'deliver',
		'item_id': 'snow_large_city_armor_key',
		'to_type': 'npc',
		'to_id': 'concordant_ivar',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'concordant_ivar',
					'dialog_id': 'ivar_armor_key'
				}
			},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'snow_large_city_armor_key'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_large_city_type_d_consult_lyndra'
				}
			}
		]
	},
	{
		'task_id': 'snow_large_city_type_d_consult_lyndra',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'artificer_lyndra',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'artificer_lyndra',
					'standing_text': [
						"That seal — it hums with deep vault resonance.",
						"I know what it opens. Come, I\'ll explain the rites."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'artificer_lyndra',
					'dialog_id': 'lyndra_armor_ritual'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_large_city_type_d_meet_vault_guardian'
				}
			}
		]
	},
	{
		'task_id': 'snow_large_city_type_d_meet_vault_guardian',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'glacier_seer_thryna',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'glacier_seer_thryna',
					'standing_text': [
						"The vault stirs. The rite must be spoken before the guardian emerges.",
						"Are you ready?"
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'glacier_seer_thryna',
					'dialog_id': 'thryna_armor_boss'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_large_city_type_d_defeat_vault_guardian'
				}
			}
		]
	},
	{
		'task_id': 'snow_large_city_type_d_defeat_vault_guardian',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'frostgate_vault_guardian_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'frostgate_vault_guardian_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'concordant_ivar',
					'dialog_id': 'ivar_armor_reward'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_snow_large_frostgate_sovereign'
				}
			}
		]
	},

]

# ── Type B ── Kor-in / Lady Aeriola (regional character quest) ────────────────
# Gated by Ch.20 Void Gauntlet. Kor-in senses Aeriola's time-stopping residue
# crystallizing inside the Frostgate Spire glacier — the void's collapse
# released frozen moments she left behind, and they are beginning to stack.
# Creates dungeon in open area.
# No new NPCs — uses initiate_character_dialog on Kor-in exclusively.

NPC_DIALOG += [

	{
		'npc_id': 'kor_in',
		'dialog_id': 'kor_in_b_frost_wrong',
		'dialog': [
			"The frost is wrong.",
			"Not broken. Held.",
			"Aeriola's spell — when it released, it didn't disappear.",
			"The cold stored it. Frosted moments. Dozens of them.",
			"They've been stacking inside the glacier since she fell.",
			"The void's collapse released enough pressure to start thawing them.",
			"(very quiet, very precise) If they thaw all at once, they collapse into a single frozen point.",
			"I know what that does to the people caught inside it.",
			"I will not let it happen again."
		]
	},
	{
		'npc_id': 'kor_in',
		'dialog_id': 'kor_in_b_entering_sanctum',
		'dialog': [
			"She will have reformed around the stored moments.",
			"She believes time is hers to stop.",
			"(hand on weapon, still) She is wrong. Time is not stopped by will.",
			"It is stopped by grief. And grief does not last forever."
		]
	},
	{
		'npc_id': 'aeriola',
		'dialog_id': 'aeriola_b_risen',
		'dialog': [
			"You cannot reach me here.",
			"I stopped time in this place before. I stopped it perfectly.",
			"The void returned what your violence took from me.",
			"Every frozen moment I ever made — I carry them all now.",
			"Stand still. I will add yours to the collection."
		]
	},
	{
		'npc_id': 'kor_in',
		'dialog_id': 'kor_in_b_victory',
		'dialog': [
			"(stands in the thawed chamber, ice melting around him)",
			"She thought stopping time was mercy.",
			"(long silence)",
			"Maybe she believed that.",
			"It doesn't matter what she believed.",
			"What matters is that the frost is moving again.",
			"(quietly) Things that move can change.",
			"Things that stop — they just wait to be found."
		]
	},

]

TASKS += [

	# B-0 — Void Gauntlet entry (self-completing gated task)
	{
		'task_id': 'snow_large_city_b_void_gauntlet',
		'type': 'gated',
		'task_acquire_events': [
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'aeriolass_frozen_sanctum', 'location': 'region_open_area' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_b_frost_wrong' }},
			{ 'event_type': 'complete_task', 'params': { 'task_id': 'snow_large_city_b_void_gauntlet' }},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'snow_large_city_b_meet_aeriola' }},
		]
	},

	# B-1 — Meet Aeriola (boss intro)
	{
		'task_id': 'snow_large_city_b_meet_aeriola',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'aeriola',
		'task_acquire_events': [
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'aeriola', 'location': None }},
			{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'aeriolass_frozen_sanctum', 'location': 'final_chamber' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_b_entering_sanctum' }},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'aeriola', 'dialog_id': 'aeriola_b_risen' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'snow_large_city_b_defeat_aeriola' }},
		]
	},

	# B-2 — Defeat Aeriola
	{
		'task_id': 'snow_large_city_b_defeat_aeriola',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'aeriola_b1',
		'task_acquire_events': [
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'aeriola_b1', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_b_victory' }},
			{ 'event_type': 'complete_regional_quest_2', 'params': { 'region_id': 'snow' }},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
	'story_id': 'snow_large_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}