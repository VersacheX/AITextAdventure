ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'warden_harrock',
		'name': 'Harrock the Cliff‑Warden',
		'description': (
			'A stoic guardian who ensures travelers survive the treacherous paths.'
			' Harrock\'s voice carries like distant thunder across the cliffs.'
			' He has an uncanny sense for impending rockslides.'
		)
	},
	{
		'npc_id': 'emberguide_ryla',
		'name': 'Ryla Emberguide',
		'description': (
			'A fire‑touched wanderer who teaches survival through controlled flame.'
			' Ryla\'s campfires burn with unnatural colors, shifting with her mood.'
			' She believes every ember remembers the mountain\'s ancient fury.'
		)
	},
	{
		'npc_id': 'avalanche_seer_korrin',
		'name': 'Korrin the Avalanche‑Seer',
		'description': (
			'A hermit who reads fall‑lines and predicts collapses. '
			'Korrin senses disturbances in the mountain\'s pressure and stone.'
		)
	},
	{
		'npc_id': 'fallshadow_echo',
		'name': 'Fallshadow Echo',
		'description': (
			'A spectral remnant of ancient rockslides, awakened by the Shatterpeak Core.'
		)
	},
	{
		'npc_id': 'emberwake_spirit',
		'name': 'Emberwake Spirit',
		'description': (
			'A fiery apparition formed from unstable heat deep within the Emberwake Cavern.'
		)
	}
]


NPC_DIALOG = [

	{
		'npc_id': 'warden_harrock',
		'dialog_id': 'harrock_intro',
		'dialog': [
			"The cliffs rumble without warning.",
			"Rockfalls strike where the paths were once safe.",
			"Something beneath the mountain shifts in its sleep."
		]
	},
	{
		'npc_id': 'emberguide_ryla',
		'dialog_id': 'ryla_intro',
		'dialog': [
			"My flames burn in colors I've never seen.",
			"The mountain's fury stirs in the embers.",
			"If it wakes fully, the cliffs will tear themselves apart."
		]
	},
	{
		'npc_id': 'avalanche_seer_korrin',
		'dialog_id': 'korrin_intro',
		'dialog': [
			"The fall‑lines tremble with warning.",
			"A Core awakens — pressure, flame, and stone given will.",
			"If it rises, the whole range will collapse."
		]
	},
	{
		'npc_id': 'fallshadow_echo',
		'dialog_id': 'fallshadow_echo_intro',
		'dialog': [
			"We are the echoes of old collapses.",
			"The Core calls the cliffs to fall again.",
			"It waits deeper in the Emberwake Cavern."
		]
	},
	{
		'npc_id': 'emberwake_spirit',
		'dialog_id': 'emberwake_spirit_intro',
		'dialog': [
			"The Cavern burns with ancient fury.",
			"The Core gathers strength.",
			"Only its heart remains to be stilled."
		]
	},
	{
		'npc_id': 'warden_harrock',
		'dialog_id': 'harrock_closing',
		'dialog': [
			"The cliffs quiet. The paths are safe again.",
			"You've stilled a force older than the mountain winds.",
			"Travelers will owe you their lives for generations."
		]
	},

]


TASKS = [
	{
		'task_id': 'mountains_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'warden_harrock',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'warden_harrock',
					'standing_text': [
						"The cliffs hum with memory—if you've a story of survival, I'll listen."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'emberguide_ryla',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'emberguide_ryla',
					'standing_text': [
						"Share a flame and a tale—our fires remember the names of brave travelers."
					]
				}
			},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_mid_city_regional_complete_gate' } }
		]
	},
	{
		'task_id': 'mountains_mid_city_regional_complete_gate',
		'type': 'complete_regional_quests',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_mid_city_type_c_find_korina' } },
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_mid_city_type_d_deliver_forge_core' } },
		]

	},
]


# ── Type C ── Korina Brightvein (extended character) ──────────────────────────
# Gated by is_chapter_gte: 17. Korina has been rallying demoralized survivors
# along the Gallows Rift passes. Harrock's word opens her trust — she won't
# follow anyone who doesn't have a local warden's confidence.

NPC_DIALOG += [

	{
		'npc_id': 'korina_brightvein',
		'dialog_id': 'korina_c_first_meet',
		'dialog': [
			"The Rift passes are full of people who've given up.",
			"I've been moving from camp to camp pulling them back.",
			"You carry yourselves differently.",
			"Like people who still believe something is worth fighting for.",
			"I need to hear a local warden say you're worth following before I sign on.",
			"Trust is the only currency that holds value up here."
		]
	},

	{
		'npc_id': 'warden_harrock',
		'dialog_id': 'harrock_c_vouch',
		'dialog': [
			"Korina kept three separate survivor camps from falling apart last season.",
			"She didn't use authority — she used belief.",
			"Tell her I said the Rift paths are safer when your party walks them.",
			"She'll know what that means."
		]
	},

	{
		'npc_id': 'korina_brightvein',
		'dialog_id': 'korina_c_joins',
		'dialog': [
			"Harrock says the Rift paths are safer when you walk them.",
			"He's never said that about anyone.",
			"Then I'm with you.",
			"Fair warning — I will push everyone on this team to be better.",
			"Including you.",
			"Especially you."
		]
	},

]

TASKS += [

	# C-1 — Find Korina Brightvein
	{
		'task_id': 'mountains_mid_city_type_c_find_korina',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'korina_brightvein',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'korina_brightvein',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'korina_brightvein',
					'standing_text': [
						"Another party on the Rift passes.",
						"I'm watching to see if you move like survivors or like tourists."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'korina_brightvein',
					'dialog_id': 'korina_c_first_meet'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_mid_city_type_c_consult_harrock'
				}
			},
		]
	},

	# C-2 — Get Harrock's word
	{
		'task_id': 'mountains_mid_city_type_c_consult_harrock',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'warden_harrock',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'warden_harrock',
					'dialog_id': 'harrock_c_vouch'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_mid_city_type_c_earn_korina'
				}
			},
		]
	},

	# C-3 — Return to Korina; she joins
	{
		'task_id': 'mountains_mid_city_type_c_earn_korina',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'korina_brightvein',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'korina_brightvein',
					'standing_text': [
						"Harrock sent you back.",
						"The Rift paths are safer when you walk them.",
						"That's all I needed to hear."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'korina_brightvein',
					'dialog_id': 'korina_c_joins'
				}
			},
			{
				'event_type': 'character_join',
				'params': {
					'character_id': 'korina_brightvein'
				}
			},
		]
	},

]


# ── Type D ── Shatterpeak Warplate (mythic armor) ─────────────────────────────
# Gate: player holds forge_echo_core from the Ch.4 Type E chain (mountains cross).
# Deliver to Brawn → Korrin reads the core → defeat Emberwake Spirit → mythic armor.
# No new NPCs — uses avalanche_seer_korrin, emberwake_spirit, and brawn (Ch.1 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'avalanche_seer_korrin',
		'dialog_id': 'korrin_d_core_read',
		'dialog': [
			"This Forge Echo Core — the pressure signature inside it is extraordinary.",
			"It matches the Emberwake Cavern's resonance almost exactly.",
			"The Emberwake Spirit has been drawing heat from Ryla's fires for years.",
			"It feeds on the same foundry frequency the Core carries.",
			"Present the Core at the Cavern entrance — the Spirit will surface.",
			"Silence it and the forge-pressure it guards crystallizes.",
			"Brawn can hammer forge-pressure crystal into armor that absorbs impact like mountain stone."
		]
	},

	{
		'npc_id': 'emberwake_spirit',
		'dialog_id': 'emberwake_spirit_d_awakens',
		'dialog': [
			"The Forge Echo Core reaches the Cavern.",
			"You carry Ironveil's foundry frequency into my domain.",
			"The pressure I have held since the first forge burned — it is mine.",
			"You will not leave with it."
		]
	},

]

TASKS += [

	# D-0 — Deliver forge_echo_core to Brawn (standalone deliver; unlocks D chain)
	{
		'task_id': 'mountains_mid_city_type_d_deliver_forge_core',
		'type': 'deliver',
		'item_id': 'forge_echo_core',
		'to_type': 'npc',
		'to_id': 'brawn',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'brawn',
					'standing_text': [
						"That core — the forge-pressure inside it is still active after all this time.",
						"Something in the Gallows Rift resonates with it.",
						"Find Korrin. He reads fall-lines and mountain pressure.",
						"He'll know exactly what this core is calling to."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_mid_city_type_d_consult_korrin'
				}
			},
		]
	},

	# D-1 — Consult Korrin for the pressure reading
	{
		'task_id': 'mountains_mid_city_type_d_consult_korrin',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'avalanche_seer_korrin',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'avalanche_seer_korrin',
					'standing_text': [
						"The fall-lines shifted the moment that core crossed the Rift.",
						"The Cavern has been waiting for that foundry frequency.",
						"Come quickly — the Emberwake Spirit is already stirring."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'avalanche_seer_korrin',
					'dialog_id': 'korrin_d_core_read'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_mid_city_type_d_meet_emberwake_spirit'
				}
			},
		]
	},

	# D-2 — Meet the Emberwake Spirit (boss intro)
	{
		'task_id': 'mountains_mid_city_type_d_meet_emberwake_spirit',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'emberwake_spirit',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'emberwake_spirit',
					'standing_text': [
						"Ryla's campfires have all burned down to cold ash.",
						"The Cavern entrance glows with a deep orange heat-pulse.",
						"The Forge Echo Core has called the Spirit forward."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'emberwake_spirit',
					'dialog_id': 'emberwake_spirit_d_awakens'
				}
			},
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'emberwake_spirit_1',
					'combat_type': 'boss_encounter'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_mid_city_type_d_defeat_emberwake_spirit'
				}
			},
		]
	},

	# D-3 — Defeat the Emberwake Spirit; Brawn forges the mythic armor
	{
		'task_id': 'mountains_mid_city_type_d_defeat_emberwake_spirit',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'emberwake_spirit_1',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_mountains_mid_shatterpeak_warplate'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'brawn',
					'standing_text': [
						"Forge-pressure crystal — it compresses under impact and rebounds harder.",
						"I've worked it into the warplate.",
						"The harder you're hit, the stronger it holds.",
						"This is the kind of armor the Rift deserves."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'avalanche_seer_korrin',
					'standing_text': [
						"The fall-lines are clear.",
						"The Cavern pressure has normalized.",
						"Ryla says her fires burn in the right colors again."
					]
				}
			},
		]
	},

]

# ── Type B ── Bragg / Rokhuld the Core-Breaker (regional character quest) ─────
# Gated by Ch.20 Void Gauntlet. Bragg feels the fracture-frequency returning —
# Rokhuld's obsession with the mountain's 'true ending' survived as a resonance
# pattern inside the Gallows Rift stone. Creates dungeon in open area.
# No new NPCs — uses initiate_character_dialog on Bragg exclusively.

NPC_DIALOG += [

	{
		'npc_id': 'bragg',
		'dialog_id': 'bragg_b_fracture_echo',
		'dialog': [
			"That sound.",
			"I know that sound. I've heard it in every nightmare since the explosion.",
			"That is a micro-fracture forming. Deep. Real deep.",
			"Rokhuld — or whatever's left of him — is drilling again.",
			"(jaw tight) He convinced himself breaking the core was righteous. Sacred duty.",
			"He was wrong then. He's still wrong now.",
			"I built golems to hold this mountain together. He built a crusade to tear it apart.",
			"We end it. Today."
		]
	},
	{
		'npc_id': 'bragg',
		'dialog_id': 'bragg_b_entering_core',
		'dialog': [
			"He'll be deeper than before. The void fed something in him.",
			"Don't let him monologue. He gets worse the longer he talks.",
			"(quietly) I know because I used to do the same thing."
		]
	},
	{
		'npc_id': 'rokhuld',
		'dialog_id': 'rokhuld_b_risen',
		'dialog': [
			"The void showed me the truth of my mission.",
			"The mountain's core contains the world's final breath.",
			"I will reach it. I will release it. This is righteous.",
			"You cannot stop what is already written in the stone."
		]
	},
	{
		'npc_id': 'bragg',
		'dialog_id': 'bragg_b_victory',
		'dialog': [
			"(sitting down against the wall, hands shaking slightly)",
			"I spent years thinking the explosion was punishment. For something I did wrong.",
			"He spent years thinking it was a calling. For something he had to do right.",
			"We were both just afraid.",
			"(stands up, steadier now) The mountain's still standing.",
			"That's what matters."
		]
	},

]

TASKS += [

	# B-0 — Void Gauntlet entry (self-completing gated task)
	{
		'task_id': 'mountains_mid_city_b_void_gauntlet',
		'type': 'gated',
		'task_acquire_events': [
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'rokhulls_fracture_core', 'location': 'region_open_area' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_b_fracture_echo' }},
			{ 'event_type': 'complete_task', 'params': { 'task_id': 'mountains_mid_city_b_void_gauntlet' }},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_mid_city_b_meet_rokhuld' }},
		]
	},

	# B-1 — Meet Rokhuld (boss intro)
	{
		'task_id': 'mountains_mid_city_b_meet_rokhuld',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rokhuld',
		'task_acquire_events': [
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'rokhuld', 'location': None }},
			{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'rokhulls_fracture_core', 'location': 'final_chamber' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_b_entering_core' }},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rokhuld', 'dialog_id': 'rokhuld_b_risen' }},
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'rokhuld_b1', 'combat_type': 'boss_battle' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_mid_city_b_defeat_rokhuld' }},
		]
	},

	# B-2 — Defeat Rokhuld
	{
		'task_id': 'mountains_mid_city_b_defeat_rokhuld',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'rokhuld_b1',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_b_victory' }},
			{ 'event_type': 'complete_regional_quest_2', 'params': { 'region_id': 'mountains' }},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
	'story_id': 'mountains_mid_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}