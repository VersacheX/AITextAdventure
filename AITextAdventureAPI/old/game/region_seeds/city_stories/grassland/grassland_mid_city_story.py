ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'scribe_althorin',
		'name': 'Althorin the Doctrine‑Scribe',
		'description': (
			'A devout scholar who preserves sacred texts with unwavering discipline.'
			' Althorin\'s quill never scratches—his writing flows like whispered prayer.'
			' He believes every doctrine has a hidden verse meant only for the worthy.'
		)
	},
	{
		'npc_id': 'oathwarden_seris',
		'name': 'Seris Oathwarden',
		'description': (
			'A solemn guardian who oversees the binding of vows and pacts.'
			' Seris speaks rarely, but every word carries ceremonial weight.'
			' Her presence alone compels honesty.'
		)
	},
	{
		'npc_id': 'verse_seeker_halven',
		'name': 'Halven the Verse‑Seeker',
		'description': (
			'A wandering scholar who hears fractured scripture carried on the wind. '
			'Halven follows broken verses to their source.'
		)
	},
	{
		'npc_id': 'lexicon_fragment',
		'name': 'Lexicon Fragment',
		'description': (
			'A living shard of doctrine, cracked by the False Verse\'s corruption.'
		)
	},
	{
		'npc_id': 'sanctum_voice',
		'name': 'Sanctum Voice',
		'description': (
			'A solemn echo within the Oathbreak Sanctum, formed from unraveling vows.'
		)
	}
]


NPC_DIALOG = [

	# ── Base city dialogs ───────────────────────────────────────────

	{
		'npc_id': 'scribe_althorin',
		'dialog_id': 'althorin_intro',
		'dialog': [
			"The doctrines shift in the night.",
			"Verses appear where none were written.",
			"A False Verse spreads — subtle, poisonous."
		]
	},
	{
		'npc_id': 'oathwarden_seris',
		'dialog_id': 'seris_intro',
		'dialog': [
			"Vows break without cause.",
			"Oaths unravel mid‑sentence.",
			"Something corrupts the very act of truth‑binding."
		]
	},
	{
		'npc_id': 'verse_seeker_halven',
		'dialog_id': 'halven_intro',
		'dialog': [
			"The wind carries fractured scripture.",
			"A Verse that was never meant to be spoken.",
			"If it completes itself, all doctrine will bend."
		]
	},
	{
		'npc_id': 'lexicon_fragment',
		'dialog_id': 'lexicon_fragment_intro',
		'dialog': [
			"We are the words that broke.",
			"The False Verse rewrites us.",
			"It waits deeper in the Sanctum."
		]
	},
	{
		'npc_id': 'sanctum_voice',
		'dialog_id': 'sanctum_voice_intro',
		'dialog': [
			"The Sanctum trembles with broken vows.",
			"The False Verse grows stronger.",
			"Only its heart remains to be silenced."
		]
	},
	{
		'npc_id': 'oathwarden_seris',
		'dialog_id': 'seris_closing',
		'dialog': [
			"The doctrines settle. The vows hold true again.",
			"You have restored the plains' sacred order.",
			"The grasslands remember your honesty."
		]
	},

]

NPC_DIALOG += [

	# ── Type C dialogs — Regent Sylvara ────────────────────────────

	{
		'npc_id': 'regent_sylvara',
		'dialog_id': 'sylvara_type_c_intro',
		'dialog': [
			"You found me. That means you were looking — or you were guided.",
			"Either way suggests competence.",
			"Highsteeple is a city built on doctrines it no longer believes in.",
			"I've been watching it unravel for some time. I'd like to stop it.",
			"Before I commit, speak to Seris. She has been observing your party since you arrived.",
			"Her assessment carries more weight than my instinct."
		]
	},
	{
		'npc_id': 'oathwarden_seris',
		'dialog_id': 'seris_c_sylvara_vouch',
		'dialog': [
			"Sylvara came to me before she spoke to you.",
			"She asked me to watch your party enter the city.",
			"What you did at the Sanctum told her what she needed to know.",
			"She doesn't use words like 'trust' — but she used it with me today.",
			"Go back to her. She's ready."
		]
	},
	{
		'npc_id': 'regent_sylvara',
		'dialog_id': 'sylvara_type_c_join',
		'dialog': [
			"The False Verse is not a monster. It's a failure of governance — someone let the wrong idea take root.",
			"That is exactly the kind of problem I was designed to solve.",
			"I'll come with you."
		]
	},

]

NPC_DIALOG += [

	# ── Type E dialogs — Sanctum Seal Fragment ─────────────────────

	{
		'npc_id': 'scribe_althorin',
		'dialog_id': 'althorin_seal_discovery',
		'dialog': [
			"I've been transcribing the Sanctum's founding texts.",
			"Every record references a foundation seal — the original binding that consecrated this place.",
			"It predates the False Verse by centuries. If it still exists, it's buried in the Sanctum's deepest chamber."
		]
	},
	{
		'npc_id': 'verse_seeker_halven',
		'dialog_id': 'halven_seal_context',
		'dialog': [
			"The foundation seal is not a weapon and not a relic of worship.",
			"It is a compressed record — every oath ever sworn here, bound into stone.",
			"The False Verse cannot corrupt it. That is precisely why it buried the chamber."
		]
	},
	{
		'npc_id': 'sanctum_voice',
		'dialog_id': 'sanctum_voice_seal_guardian',
		'dialog': [
			"The seal belongs to the Sanctum.",
			"What you call preservation, we call theft.",
			"Leave. Or we will remind you what broken vows feel like."
		]
	},
	{
		'npc_id': 'scribe_althorin',
		'dialog_id': 'althorin_seal_received',
		'dialog': [
			"Extraordinary. This is the original mark — I can read every oath in the grain of the stone.",
			"It doesn't belong locked away down there. And it doesn't belong in my archive either.",
			"Carry it. Something will call for it eventually — oaths have a way of finding their purpose."
		]
	},

]

NPC_DIALOG += [

	# ── Type D dialogs — Oathbreaker's Sigil (mythic accessory) ────

	{
		'npc_id': 'scribe_althorin',
		'dialog_id': 'althorin_d_seal_read',
		'dialog': [
			"This fragment holds the original Oathbreaker's imprint.",
			"The Sanctum Voice — the echo we thought destroyed — it was bound inside this seal.",
			"Releasing it correctly will shatter the bond and crystallize the residue.",
			"Crystallized oath-residue is what Mira has been searching for.",
			"But first the Voice must be drawn out and silenced properly."
		]
	},
	{
		'npc_id': 'sanctum_voice',
		'dialog_id': 'sanctum_voice_d_awakens',
		'dialog': [
			"The seal opens.",
			"Every broken vow flows back to me.",
			"I will finish what the doctrine started."
		]
	},

]


TASKS = [
	{
		'task_id': 'grassland_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'scribe_althorin',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scribe_althorin',
					'standing_text': [
						"Words weave history — share a memory and I'll add it to the ledger."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'oathwarden_seris',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'oathwarden_seris',
					'standing_text': [
						"Pacts are spoken softly here — if your heart is true, speak and I will hear."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_regional_complete_gate'
				}
			},
		]
	},
	{
		'task_id': 'grassland_mid_city_regional_complete_gate',
		'type': 'complete_regional_quests',
		'task_acquire_events': [],
		'task_complete_events': [
			# E chain — no gate; artifact waits in inventory
			# Prompt Althorin toward the seal investigation
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scribe_althorin',
					'standing_text': [
						"I've been tracing the Sanctum's oldest texts.",
						"There is a foundation seal referenced in every founding document — but I cannot find the stone itself."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_e_investigate_seal'
				}
			},
			# C chain — gated by chapter 3 being reached
			# Place Sylvara and set her standing text so she is ready for the meet task
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'regent_sylvara',
					'location': 'region_city_other3'
				},
				'condition': {
					'type': 'is_chapter_gte',
					'params': { 'chapter': 3 }
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'regent_sylvara',
					'standing_text': [
						"I've been watching this city for some time.",
						"You're the first person who's looked like they could actually do something about it."
					]
				},
				'condition': {
					'type': 'is_chapter_gte',
					'params': { 'chapter': 3 }
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_c_find_sylvara'
				},
				'condition': {
					'type': 'is_chapter_gte',
					'params': { 'chapter': 3 }
				}
			},
		]
	},
]

TASKS += [

	# =========================================================
	# TYPE C — Regent Sylvara (extended character, slot 1)
	# Gated by is_chapter_gte: 3
	# Awarded by: grassland_mid_city_regional_complete_gate (conditional)
	# Chain: find Sylvara → Seris vouches → return to Sylvara → Sylvara joins
	# Sylvara is placed in regional_complete_gate complete events.
	# =========================================================

	# C-1 — Sylvara introduces herself and asks for Seris's assessment
	{
		'task_id': 'grassland_mid_city_type_c_find_sylvara',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'regent_sylvara',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'regent_sylvara',
					'dialog_id': 'sylvara_type_c_intro'
				}
			},
			# Prime Seris's standing text before the party goes to her
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'oathwarden_seris',
					'standing_text': [
						"Sylvara sent you to me.",
						"I've been watching your party since you arrived. Come speak."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_c_earn_sylvara'
				}
			},
		]
	},

	# C-2 — Seris gives her assessment and points the party back to Sylvara
	{
		'task_id': 'grassland_mid_city_type_c_earn_sylvara',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'oathwarden_seris',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'oathwarden_seris',
					'dialog_id': 'seris_c_sylvara_vouch'
				}
			},
			# Update Sylvara's standing text so she signals she is ready
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'regent_sylvara',
					'standing_text': [
						"Seris has given her word.",
						"I'm ready to speak plainly now."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_c_join_sylvara'
				}
			},
		]
	},

	# C-3 — Return to Sylvara; she joins the party
	{
		'task_id': 'grassland_mid_city_type_c_join_sylvara',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'regent_sylvara',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'regent_sylvara',
					'dialog_id': 'sylvara_type_c_join'
				}
			},
			{
				'event_type': 'hide_npc',
				'params': { 'npc_id': 'regent_sylvara' }
			},
			{
				'event_type': 'character_join',
				'params': {
					'character_id': 'regent_sylvara'
				}
			},
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE E — Sanctum Seal Fragment
	# Artifact ID: grassland_mid_city_e_sanctum_seal_fragment
	# Gates: grassland_large_city (Crosswind Bazaar, Ch.10) Type D (Slot 2)
	# Awarded by: grassland_mid_city_regional_complete_gate
	# Chain: investigate with Althorin → consult Halven → confront Voice → defeat → return to Althorin
	# No create_dungeon — NPC-driven per Type E rules.
	# Halven and sanctum_voice placed by preceding task complete events.
	# =========================================================

	# E-1 — Althorin traces the foundation seal in the records
	{
		'task_id': 'grassland_mid_city_type_e_investigate_seal',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'scribe_althorin',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'scribe_althorin',
					'dialog_id': 'althorin_seal_discovery'
				}
			},
			# Place Halven and set his standing text before the next meet task
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'verse_seeker_halven',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'verse_seeker_halven',
					'standing_text': [
						"A foundation seal? Yes — I've traced references to it in three separate doctrine winds.",
						"The False Verse buried it deliberately. That alone tells you it matters."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_e_consult_halven'
				}
			},
		]
	},

	# E-2 — Halven provides context on the seal's nature
	{
		'task_id': 'grassland_mid_city_type_e_consult_halven',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'verse_seeker_halven',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'verse_seeker_halven',
					'dialog_id': 'halven_seal_context'
				}
			},
			# Place the Sanctum Voice and set its standing text before the confront task
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'sanctum_voice',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sanctum_voice',
					'standing_text': [
						"The chamber is sealed for a reason.",
						"Turn back."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_e_confront_sanctum_voice'
				}
			},
		]
	},

	# E-3 — Confront the Sanctum Voice guarding the sealed chamber
	{
		'task_id': 'grassland_mid_city_type_e_confront_sanctum_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'sanctum_voice',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'sanctum_voice',
					'dialog_id': 'sanctum_voice_seal_guardian'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_e_defeat_sanctum_voice'
				}
			},
		]
	},

	# E-4 — Defeat the Sanctum Voice; claim the artifact
	{
		'task_id': 'grassland_mid_city_type_e_defeat_sanctum_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'sanctum_voice_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'sanctum_voice_1',
					'combat_type': 'boss_battle'
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'grassland_mid_city_e_sanctum_seal_fragment'
				}
			},
			# Set Althorin's standing text for the return step
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scribe_althorin',
					'standing_text': [
						"You found it. I can feel the oaths radiating from it from here.",
						"Come — let me read what it says."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_e_return_to_althorin'
				}
			},
			# D chain is gated by this E artifact — award deliver task immediately
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"An Oathbreak seal fragment — do you understand what this means?",
						"I've seen shards like this in theory texts but never held one.",
						"Take it to Althorin first.",
						"He'll know how to read the imprint before we do anything irreversible."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_d_deliver_seal_fragment'
				}
			},
		]
	},

	# E-5 — Return to Althorin; he reads the seal and releases the player to carry it
	{
		'task_id': 'grassland_mid_city_type_e_return_to_althorin',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'scribe_althorin',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'scribe_althorin',
					'dialog_id': 'althorin_seal_received'
				}
			},
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE D — Oathbreaker's Sigil (mythic accessory, slot 3)
	# Gate: grassland_mid_city_e_sanctum_seal_fragment (from E chain above)
	# Mythic reward: mythic_grassland_mid_oathbreakers_sigil
	# Deliver to Mira → Althorin reads the imprint → defeat Sanctum Voice → mythic accessory
	# No new NPCs — uses scribe_althorin, sanctum_voice, and mira (Ch.2 party anchor).
	# Sanctum Voice already placed by the E chain; Althorin standing text set by D deliver complete.
	# =========================================================

	# D-0 — Deliver seal fragment to Mira; she directs the party to Althorin
	{
		'task_id': 'grassland_mid_city_type_d_deliver_seal_fragment',
		'type': 'deliver',
		'item_id': 'grassland_mid_city_e_sanctum_seal_fragment',
		'to_type': 'npc',
		'to_id': 'mira',
		'task_acquire_events': [],
		'task_complete_events': [
			# Set Althorin's standing text for the consult step
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scribe_althorin',
					'standing_text': [
						"I felt the seal's presence the moment it entered the city.",
						"The doctrine-scripts have been trembling since dawn.",
						"Bring it here — I have been waiting to read this imprint my entire career."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_d_consult_althorin'
				}
			},
		]
	},

	# D-1 — Althorin reads the imprint and identifies the Voice inside
	{
		'task_id': 'grassland_mid_city_type_d_consult_althorin',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'scribe_althorin',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'scribe_althorin',
					'dialog_id': 'althorin_d_seal_read'
				}
			},
			# Set sanctum_voice standing text before the meet task
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sanctum_voice',
					'standing_text': [
						"The air in the sanctum thickens — every spoken word feels wrong.",
						"The Voice stirs where broken oaths accumulate.",
						"The seal fragment has called it forward."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_d_meet_sanctum_voice'
				}
			},
		]
	},

	# D-2 — Meet the Sanctum Voice; it awakens from the broken seal
	{
		'task_id': 'grassland_mid_city_type_d_meet_sanctum_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'sanctum_voice',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'sanctum_voice',
					'dialog_id': 'sanctum_voice_d_awakens'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_mid_city_type_d_defeat_sanctum_voice'
				}
			},
		]
	},

	# D-3 — Defeat the Sanctum Voice; Mira crystallizes the residue into the sigil
	{
		'task_id': 'grassland_mid_city_type_d_defeat_sanctum_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'sanctum_voice_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'sanctum_voice_1',
					'combat_type': 'boss_battle'
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_grassland_mid_oathbreakers_sigil'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"The crystallized oath-residue is perfect.",
						"I've set it into the sigil — it will hold any vow you make absolutely.",
						"Even the ones you make with yourself."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scribe_althorin',
					'standing_text': [
						"The doctrine-scripts have gone still.",
						"For the first time in months, the verses read correctly.",
						"Whatever you did in that sanctum — it worked."
					]
				}
			},
		]
	},

]


PRIMARY_STORY_SETTINGS = {
	'story_id': 'grassland_mid_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}