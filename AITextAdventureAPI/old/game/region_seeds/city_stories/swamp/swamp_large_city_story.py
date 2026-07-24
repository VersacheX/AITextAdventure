ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'bonechanter_velis',
		'name': 'Velis Bonechanter',
		'description': (
			'A ritualist who arranges skeletal remains into sacred patterns.'
			' Velis speaks in low, rhythmic tones that echo unnaturally.'
			' She believes bones remember every life they once carried.'
		)
	},
	{
		'npc_id': 'reliquarist_morwen',
		'name': 'Morwen the Veil‑Whisper',
		'description': (
			'A soft‑spoken curator who tends to relics said to house lingering spirits.'
			' Morwen\'s touch leaves faint trails of cold mist across metal and bone.'
			' She claims the reliquary murmurs warnings to those willing to listen.'
		)
	},
	{
		'npc_id': 'mire_seer_halveth',
		'name': 'Halveth the Mire‑Seer',
		'description': (
			'A swamp mystic who reads bone tides and senses when the dead shift in their rest.'
		)
	},
	{
		'npc_id': 'ossuary_whisper',
		'name': 'Ossuary Whisper',
		'description': (
			'A spectral remnant of drowned bones twisted by the Bone Drown.'
		)
	},
	{
		'npc_id': 'relicmire_voice',
		'name': 'Relicmire Voice',
		'description': (
			'A murmuring presence formed from drowned relics deep within the Sump.'
		)
	}
]


NPC_DIALOG = [

	{
		'npc_id': 'bonechanter_velis',
		'dialog_id': 'velis_intro',
		'dialog': [
			"The bones shift in their patterns.",
			"Their memories stir with unease.",
			"Something rises from the drowned past."
		]
	},
	{
		'npc_id': 'reliquarist_morwen',
		'dialog_id': 'morwen_intro',
		'dialog': [
			"The relics murmur warnings.",
			"Their spirits tremble as though something calls to them.",
			"If we ignore this, the swamp will choke on its own dead."
		]
	},
	{
		'npc_id': 'mire_seer_halveth',
		'dialog_id': 'halveth_intro',
		'dialog': [
			"The bone tides rise.",
			"A Bone Drown wakes — a spirit of drowned memory.",
			"If it awakens fully, the swamp will forget the living."
		]
	},
	{
		'npc_id': 'ossuary_whisper',
		'dialog_id': 'ossuary_whisper_intro',
		'dialog': [
			"We are the bones that sank too deep.",
			"The Bone Drown twists our rest.",
			"It waits deeper in the Relicmire Sump."
		]
	},
	{
		'npc_id': 'relicmire_voice',
		'dialog_id': 'relicmire_voice_intro',
		'dialog': [
			"The Sump churns with drowned relics.",
			"The Bone Drown gathers strength.",
			"Only its heart remains to be silenced."
		]
	},
	{
		'npc_id': 'bonechanter_velis',
		'dialog_id': 'velis_closing',
		'dialog': [
			"The bones settle. Their memories quiet.",
			"You've stilled a hunger older than the swamp itself.",
			"The mire will remember your tread."
		]
	},

]


TASKS = [
	{
		'task_id': 'swamp_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'bonechanter_velis',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'bonechanter_velis',
					'standing_text': [
						"Bones hum with stories—stay and let me arrange them into one."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'reliquarist_morwen',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'reliquarist_morwen',
					'standing_text': [
						"Relics whisper at night—come, and I will tell you what they grant and warn."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_large_city_regional_complete_gate'
				}
			},
		]
	},
	{
		'task_id': 'swamp_large_city_regional_complete_gate',
		'type': 'complete_regional_quests',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_large_city_type_c_find_anita'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_large_city_type_d_deliver_marrow_shard'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_large_city_b_void_gauntlet'
				}
			}
		]
	},
]


# ── Type C ── Anita (extended character) ──────────────────────────────────────
# Gated by is_chapter_gte: 13. Anita has come to the Necropolis cataloguing
# relic-spirit sightings. Morwen's verification earns her trust.

NPC_DIALOG += [

	{
		'npc_id': 'anita',
		'dialog_id': 'anita_c_first_meet',
		'dialog': [
			"I've catalogued forty-seven relic-spirit manifestations this season alone.",
			"The Necropolis is the most information-dense location I've ever worked.",
			"Everything here remembers — the bones, the relics, the mire itself.",
			"I don't leave a place like this until I understand it completely."
		]
	},

	{
		'npc_id': 'reliquarist_morwen',
		'dialog_id': 'morwen_c_vouch',
		'dialog': [
			"Anita catalogued the reliquary's entire spirit-manifest index in a single sitting.",
			"She noticed patterns I've spent twenty years missing.",
			"Tell her I said the relics recognize her methodology.",
			"She'll understand the weight of that."
		]
	},

	{
		'npc_id': 'anita',
		'dialog_id': 'anita_c_joins',
		'dialog': [
			"The relics recognize my methodology.",
			"Morwen doesn't say things like that without precision.",
			"My archive travels with me.",
			"If you encounter things out there that need cataloguing — and you will — I can be useful.",
			"I'm coming."
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE C — Anita (extended character, slot 2)
	# Gated by is_chapter_gte: 13
	# Awarded by: swamp_large_city_regional_complete_gate (conditional)
	# =========================================================

	{
		'task_id': 'swamp_large_city_type_c_find_anita',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'anita',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'anita',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'anita',
					'standing_text': [
						"Every bone here carries data.",
						"I intend to record all of it before I leave.",
						"Which may be never."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'anita',
					'dialog_id': 'anita_c_first_meet'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_large_city_type_c_consult_morwen'
				}
			},
		]
	},
	{
		'task_id': 'swamp_large_city_type_c_consult_morwen',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'reliquarist_morwen',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'reliquarist_morwen',
					'dialog_id': 'morwen_c_vouch'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_large_city_type_c_earn_anita'
				}
			},
		]
	},
	{
		'task_id': 'swamp_large_city_type_c_earn_anita',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'anita',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'anita',
					'standing_text': [
						"Morwen sent you back.",
						"The relics recognize my methodology.",
						"Very well."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'anita',
					'dialog_id': 'anita_c_joins'
				}
			},
			{
				'event_type': 'hide_npc',
				'params': { 'npc_id': 'anita' }
			},
			{
				'event_type': 'character_join',
				'params': { 'character_id': 'anita' }
			},
		]
	},

]


# ── Type D ── Bonedrown Reliquary (mythic weapon) ─────────────────────────────
# Gate: player holds necropolis_marrow_shard from rift_dungeon_ch4 (Ch.4).
# Deliver to Diego → Halveth reads the shard → defeat Relicmire Voice → mythic weapon.
# No new NPCs — uses mire_seer_halveth, relicmire_voice, and diego (Ch.1 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'mire_seer_halveth',
		'dialog_id': 'halveth_d_shard_read',
		'dialog': [
			"This marrow shard — it came through a rift?",
			"The bone-tide resonance on it is unlike anything native to this swamp.",
			"But the Relicmire Voice recognizes it.",
			"It has been waiting for this exact frequency since the Sump formed.",
			"Draw it out with the shard and the drowned metal it guards will surface.",
			"Diego can forge drowned Necropolis metal into a weapon that remembers every kill."
		]
	},

	{
		'npc_id': 'relicmire_voice',
		'dialog_id': 'relicmire_voice_d_awakens',
		'dialog': [
			"The marrow shard reaches the Sump.",
			"You carry rift-bone into the domain of the drowned.",
			"The metal you want has been mine for centuries.",
			"Come and take it — if the mire lets you leave."
		]
	},

]

TASKS += [

	# D-0 — Deliver necropolis_marrow_shard to Diego (standalone deliver; unlocks D chain)
	{
		'task_id': 'swamp_large_city_type_d_deliver_marrow_shard',
		'type': 'deliver',
		'item_id': 'necropolis_marrow_shard',
		'to_type': 'npc',
		'to_id': 'diego',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"That shard — the marrow inside it hasn't decayed despite the rift exposure.",
						"Something in the Necropolis is preserving it.",
						"Find Halveth. He reads bone tides — he'll know what this is connected to."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'mire_seer_halveth',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_large_city_type_d_consult_halveth'
				}
			},
		]
	},

	# D-1 — Consult Halveth for the bone-tide reading
	{
		'task_id': 'swamp_large_city_type_d_consult_halveth',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'mire_seer_halveth',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mire_seer_halveth',
					'standing_text': [
						"The bone tides surged the moment that shard crossed the mire's edge.",
						"The Sump has been waiting for it.",
						"Come quickly — the Relicmire Voice is already stirring."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'mire_seer_halveth',
					'dialog_id': 'halveth_d_shard_read'
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'relicmire_voice',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_large_city_type_d_meet_relicmire_voice'
				}
			},
		]
	},

	# D-2 — Meet the Relicmire Voice (boss intro)
	{
		'task_id': 'swamp_large_city_type_d_meet_relicmire_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'relicmire_voice',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'relicmire_voice',
					'standing_text': [
						"The Sump churns violently near the deep entrance.",
						"Velis says the bone patterns have all pointed inward since dawn.",
						"The marrow shard has called the Voice to the surface."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'relicmire_voice',
					'dialog_id': 'relicmire_voice_d_awakens'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_large_city_type_d_defeat_relicmire_voice'
				}
			},
		]
	},

	# D-3 — Defeat the Relicmire Voice; Diego forges the mythic weapon
	{
		'task_id': 'swamp_large_city_type_d_defeat_relicmire_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'relicmire_voice_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'relicmire_voice_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_swamp_large_bonedrown_reliquary'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"Drowned Necropolis metal — dense, cold, and impossibly sharp.",
						"I've worked it into the blade.",
						"It remembers every wound it's ever dealt.",
						"And it intends to add yours to the collection."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mire_seer_halveth',
					'standing_text': [
						"The bone tides have settled.",
						"The Sump is quiet for the first time in years.",
						"Morwen says the relics stopped murmuring warnings."
					]
				}
			},
		]
	},

]

# ── Type B ── Grimnaw / Miregloom (regional character quest) ──────────────────
# Gated by Ch.20 Void Gauntlet. Grimnaw detects that a shard of Miregloom's
# soul-rot survived — absorbed into the Necropolis bone-strata, still
# accelerating the world's decay. Creates dungeon in open area.
# No new NPCs — uses initiate_character_dialog on Grimnaw exclusively.

NPC_DIALOG += [

	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_b_miregloom_stirs',
		'dialog': [
			"Heheheh. Thought I smelled him.",
			"Miregloom. Not the whole thing — just a splinter. A philosophy with ambition.",
			"He convinced himself the swamp was the world's first grave.",
			"A splinter of that conviction doesn't just dissolve. It burrows.",
			"(tapping a device against his palm, eyes bright) It's been burrowing into the Necropolis for months.",
			"The bones here have been humming in a frequency I recognize.",
			"Let me translate: they are very, very unhappy.",
			"We go down. We correct this. I find the experience professionally satisfying."
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_b_entering_pit',
		'dialog': [
			"The rot down here is structured. Intentional.",
			"He's been growing a new architecture out of the dead.",
			"(quietly, almost to himself) He really did love decay.",
			"Shame it was pointed in entirely the wrong direction."
		]
	},
	{
		'npc_id': 'miregloom',
		'dialog_id': 'miregloom_b_risen',
		'dialog': [
			"The rot remembers even when the body forgets.",
			"I am what the swamp always intended — the world's first and final grave.",
			"You cannot fight decay. You can only delay it.",
			"And you have delayed long enough."
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_b_victory',
		'dialog': [
			"There. Done. The frequency is gone.",
			"(clicking a device off, dropping it in a pocket) He was never going to win.",
			"Decay is not a destination. It is a process.",
			"And processes can be interrupted.",
			"(small, satisfied laugh) I enjoy interrupting things."
		]
	},

]

TASKS += [

	# B-0 — Void Gauntlet entry (self-completing gated task)
	{
		'task_id': 'swamp_large_city_b_void_gauntlet',
		'type': 'gated',
		'task_acquire_events': [
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'miregloom_resurrection_pit', 'location': 'region_open_area' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_b_miregloom_stirs' }},
			{ 'event_type': 'complete_task', 'params': { 'task_id': 'swamp_large_city_b_void_gauntlet' }},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'swamp_large_city_b_meet_miregloom' }},
		]
	},

	# B-1 — Meet Miregloom (boss intro)
	{
		'task_id': 'swamp_large_city_b_meet_miregloom',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'miregloom',
		'task_acquire_events': [
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'miregloom', 'location': None }},
			{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'miregloom_resurrection_pit', 'location': 'final_chamber' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_b_entering_pit' }},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'miregloom', 'dialog_id': 'miregloom_b_risen' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'swamp_large_city_b_defeat_miregloom' }},
		]
	},

	# B-2 — Defeat Miregloom
	{
		'task_id': 'swamp_large_city_b_defeat_miregloom',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'miregloom_b1',
		'task_acquire_events': [
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'miregloom_b1', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_b_victory' }},
			{ 'event_type': 'complete_regional_quest_2', 'params': { 'region_id': 'swamp' }},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
	'story_id': 'swamp_large_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}