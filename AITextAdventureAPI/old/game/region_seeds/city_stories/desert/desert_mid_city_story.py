ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'velra_the_indexer',
		'name': 'Velra the Indexer',
		'description': (
			'A meticulous archivist who speaks in clipped, deliberate phrases.'
			' Velra claims the Vaults whisper to her, guiding her to lost records and forbidden histories.'
			' Her eyes flicker with bioluminescent ink, a side effect of decades spent cataloging arcane relics.'
		)
	},
	{
		'npc_id': 'shade_broker_kavren',
		'name': 'Kavren the Shade‑Broker',
		'description': (
			'A soft‑spoken information dealer who trades in secrets rather than coin.'
			' Kavren maintains a web of unseen contacts throughout Nightveil Spire.'
			' His presence is unsettlingly calm, as though he already knows the outcome of every conversation.'
		)
	},
	{
		'npc_id': 'archivist_warden_threx',
		'name': 'Archivist‑Warden Threx',
		'description': (
			'A half‑mechanical guardian built to maintain the Vaults. '
			'Threx\'s voice crackles with static and ancient protocol.'
		)
	},
	{
		'npc_id': 'vault_whisper',
		'name': 'Vault Whisper',
		'description': (
			'A disembodied voice formed from drifting script‑dust. '
			'It speaks in half‑sentences and broken memories.'
		)
	},
	{
		'npc_id': 'ink_specter',
		'name': 'Ink Specter',
		'description': (
			'A ghostly figure made of liquid ink, shifting between shapes as though searching for a lost identity.'
		)
	}
]


NPC_DIALOG = [
	{
		'npc_id': 'velra_the_indexer',
		'dialog_id': 'velra_intro',
		'dialog': [
			"Records vanish. Entire entries gone.",
			"The Vaults whisper of an intruder — a script that devours meaning.",
			"If you descend, do not trust what remembers you."
		]
	},
	{
		'npc_id': 'shade_broker_kavren',
		'dialog_id': 'kavren_intro',
		'dialog': [
			"People come to me to hide their secrets.",
			"But now secrets are hiding themselves.",
			"Someone is erasing identities from the inside out."
		]
	},
	{
		'npc_id': 'archivist_warden_threx',
		'dialog_id': 'threx_intro',
		'dialog': [
			"Designation: Threx. Archivist‑Warden.",
			"The Vaults breach. Containment failing.",
			"The Erasure feeds. You must descend."
		]
	},
	{
		'npc_id': 'vault_whisper',
		'dialog_id': 'vault_whisper_intro',
		'dialog': [
			"You hear us. Good.",
			"The script crawls. It eats names first.",
			"Yours tastes bright."
		]
	},
	{
		'npc_id': 'ink_specter',
		'dialog_id': 'ink_specter_intro',
		'dialog': [
			"Ink remembers what flesh forgets.",
			"The Erasure waits below, hungry for your outline.",
			"Turn back, or be rewritten."
		]
	},
	{
		'npc_id': 'velra_the_indexer',
		'dialog_id': 'velra_closing',
		'dialog': [
			"The Vaults quiet. The script retreats.",
			"You have preserved what remains of us.",
			"I will index your name myself — so it cannot be erased."
		]
	},
]


TASKS = [
	{
		'task_id': 'desert_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'velra_the_indexer',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'velra_the_indexer',
					'standing_text': [
						"Hello. The Vaults whisper; what do you seek?"
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'shade_broker_kavren',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'shade_broker_kavren',
					'standing_text': [
						"I know names and rumors. Tell me yours, and perhaps I can help."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task', 'params': { 'task_id': 'desert_mid_city_regional_complete_gate' }
			}
		]
	},
	{
		'task_id': 'desert_mid_city_regional_complete_gate',
		'type': 'complete_regional_quests',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'desert_mid_city_type_c_find_elyra' } },
			{ 'event_type': 'award_task', 'params': { 'task_id': 'desert_mid_city_type_d_deliver_ink_vial' } },
		]
	},
]


# ── Type C ── Elyra Dawnseer (extended character) ─────────────────────────────
# Gated by is_chapter_gte: 8. Elyra is drawn to Nightveil Spire by the
# Vault Whisper's resonance — she has been receiving fragmented visions of
# the city's erasure. Velra's recommendation earns her trust.

NPC_DIALOG += [

	{
		'npc_id': 'elyra_dawnseer',
		'dialog_id': 'elyra_c_first_meet',
		'dialog': [
			"The visions brought me here.",
			"Fragments — ink dissolving, names going dark one by one.",
			"I have seen this city erased a hundred times in possible futures.",
			"I stay to understand why it keeps surviving."
		]
	},

	{
		'npc_id': 'velra_the_indexer',
		'dialog_id': 'velra_c_vouch',
		'dialog': [
			"Elyra appeared the morning the Vaults first whispered of the Erasure.",
			"I don't believe in coincidence — I believe in pattern.",
			"She reads the pattern the way I read the archive.",
			"If she trusts you, tell her I said the index has a new entry."
		]
	},

	{
		'npc_id': 'elyra_dawnseer',
		'dialog_id': 'elyra_c_joins',
		'dialog': [
			"Velra indexed you.",
			"That means you exist in a way the Erasure cannot touch.",
			"The futures I have seen that end well — you are in all of them.",
			"I will travel with you."
		]
	},

]

TASKS += [

	# C-1 — Find Elyra Dawnseer
	{
		'task_id': 'desert_mid_city_type_c_find_elyra',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'elyra_dawnseer',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'elyra_dawnseer',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'elyra_dawnseer',
					'standing_text': [
						"The visions led me here.",
						"I am still waiting to understand what they want me to do."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'elyra_dawnseer',
					'dialog_id': 'elyra_c_first_meet'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_mid_city_type_c_consult_velra'
				}
			},
		]
	},

	# C-2 — Get Velra's recommendation
	{
		'task_id': 'desert_mid_city_type_c_consult_velra',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'velra_the_indexer',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'velra_the_indexer',
					'dialog_id': 'velra_c_vouch'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_mid_city_type_c_earn_elyra'
				}
			},
		]
	},

	# C-3 — Return to Elyra; she joins
	{
		'task_id': 'desert_mid_city_type_c_earn_elyra',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'elyra_dawnseer',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'elyra_dawnseer',
					'standing_text': [
						"Velra sent you back.",
						"The index has a new entry.",
						"I know what that means."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'elyra_dawnseer',
					'dialog_id': 'elyra_c_joins'
				}
			},
			{
				'event_type': 'character_join',
				'params': {
					'character_id': 'elyra_dawnseer'
				}
			},
		]
	},

]


# ── Type D ── Veilscript Sigil (mythic accessory) ─────────────────────────────
# Gate: player holds ink_resonance_vial from theatre_of_echoed_faces (Ch.8 dungeon).
# Deliver to Mira → Threx decodes the vial → defeat Ink Specter → mythic accessory.
# No new NPCs — uses archivist_warden_threx, ink_specter, and mira (Ch.2 anchor).

NPC_DIALOG += [

	{
		'npc_id': 'archivist_warden_threx',
		'dialog_id': 'threx_d_vial_decode',
		'dialog': [
			"Ink Resonance Vial — designation: identity anchor.",
			"This compound was used to bind a living identity into script.",
			"The Ink Specter in the Inkwell Depths carries the matching frequency.",
			"Dissolve the Specter correctly and the vial's compound crystallizes.",
			"Mira can set crystallized identity-ink into an accessory unlike any other."
		]
	},

	{
		'npc_id': 'ink_specter',
		'dialog_id': 'ink_specter_d_awakens',
		'dialog': [
			"The vial calls to me.",
			"You carry what was taken from me.",
			"I will rewrite you before I let it go."
		]
	},

]

TASKS += [

	# D-0 — Deliver ink_resonance_vial to Mira (standalone deliver; unlocks D chain)
	{
		'task_id': 'desert_mid_city_type_d_deliver_ink_vial',
		'type': 'deliver',
		'item_id': 'ink_resonance_vial',
		'to_type': 'npc',
		'to_id': 'mira',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"That vial — the ink inside moves on its own.",
						"It's looking for something to write itself into.",
						"Take it to Threx before it finds a host."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_mid_city_type_d_consult_threx'
				}
			},
		]
	},

	# D-1 — Consult Threx for the vial decode
	{
		'task_id': 'desert_mid_city_type_d_consult_threx',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'archivist_warden_threx',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'archivist_warden_threx',
					'standing_text': [
						"Ink Resonance Vial detected.",
						"Provenance: Theatre of Echoed Faces.",
						"Protocol: decode before compound destabilizes.",
						"Bring it to me immediately."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'archivist_warden_threx',
					'dialog_id': 'threx_d_vial_decode'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_mid_city_type_d_meet_ink_specter'
				}
			},
		]
	},

	# D-2 — Meet the Ink Specter (boss intro)
	{
		'task_id': 'desert_mid_city_type_d_meet_ink_specter',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'ink_specter',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'ink_specter',
					'standing_text': [
						"The Inkwell Depths stir.",
						"Kavren says a shifting presence has been seen near the lower archive entrance.",
						"The vial has drawn the Specter forward."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'ink_specter',
					'dialog_id': 'ink_specter_d_awakens'
				}
			},
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'ink_specter_1',
					'combat_type': 'boss_encounter'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_mid_city_type_d_defeat_ink_specter'
				}
			},
		]
	},

	# D-3 — Defeat the Ink Specter; Mira crafts the mythic accessory
	{
		'task_id': 'desert_mid_city_type_d_defeat_ink_specter',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'ink_specter_1',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_desert_mid_veilscript_sigil'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"The crystallized identity-ink set perfectly.",
						"I've bound it into the sigil — whoever wears it cannot be erased.",
						"Not by magic, not by time, not by the Vaults."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'velra_the_indexer',
					'standing_text': [
						"The Inkwell Depths are quiet.",
						"I've re-indexed every entry the Specter corrupted.",
						"The archive is whole again."
					]
				}
			},
		]
	},

]


# ── Type B ── Sable / Zaruun the Sand-Sunderer (regional character quest) ─────
# Gated by Ch.20 Void Gauntlet. Sable senses Zaruun's dissolution-hunger
# leaking back through the sand. Creates dungeon in open area.
# No new NPCs — uses initiate_character_dialog on Sable exclusively.

NPC_DIALOG += [

	{
		'npc_id': 'sable',
		'dialog_id': 'sable_b_shadow_returns',
		'dialog': [
			"The sand is lying again.",
			"Not the small lies — the deep ones. The kind Zaruun used to leave behind him.",
			"He's not gone. Something of him soaked into the dunes when we broke him.",
			"It's been waiting for the right silence to climb back out.",
			"The desert told me. It always does, if you know what to listen for.",
			"We go back in. We finish what the desert started."
		]
	},
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_b_entering_sanctum',
		'dialog': [
			"I know this sand.",
			"He's not the same shape he was. The void remade him.",
			"Stay close. The dunes here are his memory — and they remember us."
		]
	},
	{
		'npc_id': 'zaruun',
		'dialog_id': 'zaruun_b_risen',
		'dialog': [
			"You cannot undo what the void has already emptied.",
			"I am the desert's will now. Not a man. Not a warlock.",
			"The sand opened for me. And it will swallow you before it closes."
		]
	},
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_b_victory',
		'dialog': [
			"The sand is quiet again. Really quiet.",
			"Not the silence before something breaks — the other kind.",
			"The kind that means it's over.",
			"(long pause) I spent years thinking the desert had no mercy in it.",
			"Turns out it was just waiting for us to earn some."
		]
	},

]

TASKS += [

	# B-0 — Void Gauntlet entry (self-completing gated task)
	{
		'task_id': 'desert_mid_city_b_void_gauntlet',
		'type': 'gated',
		'task_acquire_events': [
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'zaruuns_sanctum', 'location': 'region_open_area' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_b_shadow_returns' }},
			{ 'event_type': 'complete_task', 'params': { 'task_id': 'desert_mid_city_b_void_gauntlet' }},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'desert_mid_city_b_meet_zaruun' }},
		]
	},

	# B-1 — Meet Zaruun (boss intro)
	{
		'task_id': 'desert_mid_city_b_meet_zaruun',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'zaruun',
		'task_acquire_events': [
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'zaruun', 'location': None }},
			{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'zaruuns_sanctum', 'location': 'final_chamber' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_b_entering_sanctum' }},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'zaruun', 'dialog_id': 'zaruun_b_risen' }},
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'zaruun_b1', 'combat_type': 'boss_battle' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'desert_mid_city_b_defeat_zaruun' }},
		]
	},

	# B-2 — Defeat Zaruun
	{
		'task_id': 'desert_mid_city_b_defeat_zaruun',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'zaruun_b1',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_b_victory' }},
			{ 'event_type': 'complete_regional_quest_2', 'params': { 'region_id': 'desert' }},
		]
	},

]


PRIMARY_STORY_SETTINGS = {
	'story_id': 'desert_mid_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}