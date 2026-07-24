ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'elder_saphrin',
		'name': 'Saphrin the Hollow‑Keeper',
		'description': (
			'A serene elder who oversees the Exchange with ritualistic precision.'
			' Saphrin communes with the living wood, sensing emotional echoes in traded goods.'
			' Their presence is calming, like moss‑softened footsteps in ancient groves.'
		)
	},
	{
		'npc_id': 'twigwhisper_loryn',
		'name': 'Loryn Twigwhisper',
		'description': (
			'A nimble, sharp‑eyed negotiator who conducts deals from the high boughs.'
			' Loryn\'s voice carries like birdsong, disarming even the most guarded traders.'
			' They claim the forest itself enforces every bargain struck in the Den.'
		)
	},
	{
		'npc_id': 'spore_seer_myrn',
		'name': 'Myrn the Spore‑Seer',
		'description': (
			'A wandering hermit who reads drifting spores like constellations. '
			'Myrn senses disturbances in the forest\'s emotional undergrowth.'
		)
	},
]

NPC_DIALOG = [

	# ── Type A dialogs ──────────────────────────────────────────────
	{
		'npc_id': 'elder_saphrin',
		'dialog_id': 'saphrin_intro',
		'dialog': [
			"The Exchange falters. Promises rot at the edges.",
			"Something ancient stirs beneath the roots — a mind that binds all bargains.",
			"If it wakes fully, no oath will remain free."
		]
	},
	{
		'npc_id': 'twigwhisper_loryn',
		'dialog_id': 'loryn_intro',
		'dialog': [
			"The canopy rustles with warnings.",
			"Deals unravel, threads snap, and the forest tightens its grip.",
			"Whatever lies below wants every promise ever spoken."
		]
	},
	{
		'npc_id': 'spore_seer_myrn',
		'dialog_id': 'myrn_intro',
		'dialog': [
			"Spores drift toward the Hollows — drawn by a hungry root‑mind.",
			"The Heartwood Veil grows, weaving itself through every pact.",
			"If you descend, tread softly. It listens."
		]
	},
	{
		'npc_id': 'elder_saphrin',
		'dialog_id': 'saphrin_closing',
		'dialog': [
			"The Veil falls silent. The Exchange breathes again.",
			"You have freed our promises from its grasp.",
			"The forest will remember your name in its rings."
		]
	},

	# ── Type D dialogs ──────────────────────────────────────────────
	{
		'npc_id': 'elder_saphrin',
		'dialog_id': 'saphrin_veil_leaf',
		'dialog': [
			"A Veil Memory Leaf… I haven't seen one since the first Heartwood awakening.",
			"This fragment still hums with promises — it belongs to the Verdant Cradle.",
			"Seek Loryn. She knows the old ways of binding memory back to bark."
		]
	},
	{
		'npc_id': 'twigwhisper_loryn',
		'dialog_id': 'loryn_veil_ritual',
		'dialog': [
			"The leaf is real. The old promises are still alive inside it.",
			"There is a weapon sleeping in the deepest bark — the Canopy Sovereign.",
			"Bring the leaf to the Verdant Cradle. If it accepts you, the blade is yours."
		]
	},
	{
		'npc_id': 'twigwhisper_loryn',
		'dialog_id': 'loryn_veil_reward',
		'dialog': [
			"The Cradle released it. The Canopy Sovereign is yours.",
			"Carry it well — the forest remembers every oath sworn upon its edge."
		]
	},
	{
		'npc_id': 'elder_saphrin',
		'dialog_id': 'saphrin_a_ch18_memory_anchor',
		'dialog': [
			"A shifting map that won't hold still.",
			"(calm, deliberate) The Exchange has a shard of fixed memory — an echo so old the wood grew around it.",
			"It remembers a time before collapse was possible.",
			"That kind of certainty does not bend.",
			"(retrieves a small, smooth fragment of living wood from beneath the counter)",
			"Take it. If your cartographer places this against the map, the lines will have something to hold to.",
			"The forest trusts you with this. Do not waste it."
		]
	},
]

TASKS = [

	# ── Type A — Chapter Tie‑In (slot 1) ────────────────────────────
	{
		'task_id': 'forest_large_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'elder_saphrin',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'elder_saphrin',
					'standing_text': [
						"Sit awhile — the trees remember more stories than any traveler."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'standing_text': [
						"High branches hold gossip; lean close and I'll tell you what the leaves sang."
					]
				}
			},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'forest_large_city_type_a_ch18_find_anchor' }},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_large_city_type_a_meet_saphrin'
				}
			},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'forest_large_city_type_d_deliver_veil_leaf' }}
		]
	},
	{
		'task_id': 'forest_large_city_type_a_meet_saphrin',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'elder_saphrin',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'elder_saphrin',
					'standing_text': [
						"The Exchange trembles. Something roots beneath our bargains.",
						"Sit, traveler — the wood has warnings to whisper."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'elder_saphrin',
					'dialog_id': 'saphrin_intro'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_large_city_type_a_meet_loryn'
				}
			}
		]
	},
	{
		'task_id': 'forest_large_city_type_a_meet_loryn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'twigwhisper_loryn',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'dialog_id': 'loryn_intro'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'standing_text': [
						"Deals are unraveling. Promises fray like old bark.",
						"Something deep below is rewriting the rules."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_large_city_type_a_find_myrn'
				}
			}
		]
	},
	{
		'task_id': 'forest_large_city_type_a_find_myrn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'spore_seer_myrn',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'spore_seer_myrn',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'spore_seer_myrn',
					'standing_text': [
						"Hush… the spores drift strangely today.",
						"They fall toward the Hollows. Something wakes."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'spore_seer_myrn',
					'dialog_id': 'myrn_intro'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'elder_saphrin',
					'dialog_id': 'saphrin_closing'
				}
			},
			{
				'event_type': 'complete_regional_quests',
				'params': {
					'region_id': 'forest_large_city'
				}
			}
		]
	},

	# ── Type D — Mythic Equipment Quest (slot 2) ─────────────────────
	# Gate: veil_memory_leaf (from abandoned_ruin_ch2, Ch.2)
	# Mythic reward: mythic_forest_large_canopy_sovereign (weapon → Diego)
	{
		'task_id': 'forest_large_city_type_d_deliver_veil_leaf',
		'type': 'deliver',
		'item_id': 'veil_memory_leaf',
		'to_type': 'npc',
		'to_id': 'elder_saphrin',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'elder_saphrin',
					'dialog_id': 'saphrin_veil_leaf'
				}
			},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'veil_memory_leaf'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_large_city_type_d_consult_loryn'
				}
			}
		]
	},
	{
		'task_id': 'forest_large_city_type_d_consult_loryn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'twigwhisper_loryn',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'standing_text': [
						"There is something in the air today… old bark, old promises.",
						"Come closer — I think I know what that leaf wants from you."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'dialog_id': 'loryn_veil_ritual'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_large_city_type_d_meet_verdant_cradle'
				}
			}
		]
	},
	{
		'task_id': 'forest_large_city_type_d_meet_verdant_cradle',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'verdant_cradle_guardian_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'verdant_cradle_guardian_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'twigwhisper_loryn',
					'dialog_id': 'loryn_veil_reward'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_forest_large_canopy_sovereign'
				}
			}
		]
	},

	# A-1 — Meet Saphrin to receive the living memory anchor
	{
		'task_id': 'forest_large_city_type_a_ch18_find_anchor',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'elder_saphrin',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'elder_saphrin', 'standing_text': [
				"Something in the city feels unmoored.",
				"The Exchange holds a fixed memory that may help.",
				"Come speak with me."
			]}},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'elder_saphrin', 'dialog_id': 'saphrin_a_ch18_memory_anchor' }},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'living_memory_anchor' }},
		]
	},

]

# ── Type B ── Thorn / Elder Marrowroot (regional character quest) ──────────────
# Gated by Ch.20 Void Gauntlet. Thorn senses Marrowroot's corruption seeping
# back into the Aurelion Veil canopy — the root-mind's promise to 'save' the
# forest didn't die, it went dormant and the void's collapse woke it.
# Creates dungeon in open area.
# No new NPCs — uses initiate_character_dialog on Thorn exclusively.

NPC_DIALOG += [

	{
		'npc_id': 'thorn',
		'dialog_id': 'thorn_b_roots_move',
		'dialog': [
			"Roots are moving wrong.",
			"Not growing. Reaching.",
			"Marrowroot fused with the tree to save the forest. That intention didn't burn out with him.",
			"It's in the wood. Patient.",
			"The void's collapse — all that pressure releasing — it found the intention and fed it.",
			"Now it's reaching toward the canopy again.",
			"(terse) We go in. We burn it out. It doesn't get to do this twice."
		]
	},
	{
		'npc_id': 'thorn',
		'dialog_id': 'thorn_b_entering_grove',
		'dialog': [
			"Quiet. Don't touch the roots.",
			"He hears through them.",
			"(stops, listens) He already knows we're here."
		]
	},
	{
		'npc_id': 'marrowroot',
		'dialog_id': 'marrowroot_b_risen',
		'dialog': [
			"You cut me from the tree. But the tree remembers me.",
			"The void showed me the edge approaching. The forest must transform or be consumed.",
			"I am the transformation.",
			"You are the resistance. And resistance is what I was made to overcome."
		]
	},
	{
		'npc_id': 'thorn',
		'dialog_id': 'thorn_b_victory',
		'dialog': [
			"(stands in the cleared grove, breathing hard)",
			"He believed what he was doing was good.",
			"That's the part that makes it hard.",
			"(looking at the trees) But the forest isn't his to save. It's not mine either.",
			"It just needs to be left alone.",
			"(quietly) We did that. We left it alone."
		]
	},

]

TASKS += [

	# B-0 — Void Gauntlet entry (self-completing gated task)
	{
		'task_id': 'forest_large_city_b_void_gauntlet',
		'type': 'gated',
		'task_acquire_events': [
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'marrowroots_deep_grove', 'location': 'region_open_area' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_b_roots_move' }},
			{ 'event_type': 'complete_task', 'params': { 'task_id': 'forest_large_city_b_void_gauntlet' }},
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'forest_large_city_b_meet_marrowroot' }},
		]
	},

	# B-1 — Meet Marrowroot (boss intro)
	{
		'task_id': 'forest_large_city_b_meet_marrowroot',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'marrowroot',
		'task_acquire_events': [
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'marrowroot', 'location': None }},
			{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'marrowroots_deep_grove', 'location': 'final_chamber' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_b_entering_grove' }},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marrowroot', 'dialog_id': 'marrowroot_b_risen' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'forest_large_city_b_defeat_marrowroot' }},
		]
	},

	# B-2 — Defeat Marrowroot
	{
		'task_id': 'forest_large_city_b_defeat_marrowroot',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'marrowroot_b1',
		'task_acquire_events': [			
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'marrowroot_b1', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_b_victory' }},
			{ 'event_type': 'complete_regional_quest_2', 'params': { 'region_id': 'forest' }},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
	'story_id': 'forest_large_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}