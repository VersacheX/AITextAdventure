ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'archivist_fernhollow',
		'name': 'Fernhollow',
		'description': (
			'A gentle historian who records the forest\'s shifting lore.'
			' Fernhollow speaks to trees as though they are old friends.'
			' Their parchment always smells faintly of pine resin and rain.'
		)
	},
	{
		'npc_id': 'scout_lyss',
		'name': 'Lyss the Quiet Step',
		'description': (
			'A vigilant scout who hears disturbances long before they occur.'
			' Lyss meditates daily to attune her senses to the forest\'s whispers.'
			' She rarely raises her voice, yet commands instant attention.'
		)
	},
	{
		'npc_id': 'whisper_moth_selen',
		'name': 'Whisper‑Moth Selen',
		'description': (
			'A soft‑spoken wanderer who follows drifting moth‑spirits that carry the forest\'s memories.'
		)
	},
	{
		'npc_id': 'moth_echo',
		'name': 'Moth Echo',
		'description': (
			'A faint, fluttering apparition formed from forgotten stories and pale wing‑light.'
		)
	},
	{
		'npc_id': 'burrow_whisper',
		'name': 'Burrow Whisper',
		'description': (
			'A murmuring presence deep within the Echofern Burrows, shaped from lost recollections.'
		)
	}
]


NPC_DIALOG = [

	# ── Base city dialogs ───────────────────────────────────────────

	{
		'npc_id': 'archivist_fernhollow',
		'dialog_id': 'fernhollow_intro',
		'dialog': [
			"The forest forgets too much.",
			"Memories slip away like dew at dawn.",
			"Something steals our stories — gently, but relentlessly."
		]
	},
	{
		'npc_id': 'scout_lyss',
		'dialog_id': 'lyss_intro',
		'dialog': [
			"The quiet is wrong.",
			"Even the wind hesitates to speak.",
			"Whatever silences the forest moves softly."
		]
	},
	{
		'npc_id': 'whisper_moth_selen',
		'dialog_id': 'selen_intro',
		'dialog': [
			"The moths carry what the forest forgets.",
			"They drift toward a place where memories fade.",
			"Follow them, and you'll find the thief of whispers."
		]
	},
	{
		'npc_id': 'moth_echo',
		'dialog_id': 'moth_echo_intro',
		'dialog': [
			"We flutter with forgotten tales.",
			"The Silent Canopy drinks our voices.",
			"It waits deeper below."
		]
	},
	{
		'npc_id': 'burrow_whisper',
		'dialog_id': 'burrow_whisper_intro',
		'dialog': [
			"The Burrows tremble with stolen memories.",
			"The Canopy grows stronger with each silence.",
			"Only its heart remains to be severed."
		]
	},
	{
		'npc_id': 'archivist_fernhollow',
		'dialog_id': 'fernhollow_closing',
		'dialog': [
			"The forest breathes again.",
			"Its stories return like rain to thirsty soil.",
			"You've restored what was nearly lost."
		]
	},

]

NPC_DIALOG += [

	# ── Type E dialogs — Thornshade Root Graft ─────────────────────

	{
		'npc_id': 'archivist_fernhollow',
		'dialog_id': 'fernhollow_root_graft_discovery',
		'dialog': [
			"I've been cross-referencing old growth records and I found something unusual.",
			"There's an entry describing a graft — a living cutting taken from the oldest thorn-tree in the hamlet.",
			"The records say it was sealed in the Echofern Burrows for preservation.",
			"It was never retrieved. The tree it came from has been gone for two generations."
		]
	},
	{
		'npc_id': 'scout_lyss',
		'dialog_id': 'lyss_root_graft_context',
		'dialog': [
			"I've passed that section of the burrows. There's a sealed alcove — roots around the entrance, old growth.",
			"The Burrow Whisper guards that stretch of tunnel more fiercely than any other.",
			"It's not protecting the space. It's protecting something inside it."
		]
	},
	{
		'npc_id': 'burrow_whisper',
		'dialog_id': 'burrow_whisper_graft_guardian',
		'dialog': [
			"The Graft sleeps here.",
			"The forest asked us to keep it.",
			"You are not the forest."
		]
	},
	{
		'npc_id': 'archivist_fernhollow',
		'dialog_id': 'fernhollow_root_graft_received',
		'dialog': [
			"Still alive. After all this time, it's still alive.",
			"Selen's moths were holding its memory — they've been restless since you returned.",
			"She says it's looking for Boiling Bubble. The mycelium there will recognise it.",
			"This cutting carries the memory of a tree that no longer exists anywhere in Thornshade.",
			"The records say the original tree had roots that reached the forest at Boiling Bubble.",
			"Root grafts don't preserve — they transmit. This one has been trying for longer than I can date.",
			"Carry it. When the time comes, the mycelium will know you're there."
		]
	},

]

NPC_DIALOG += [

	# ── Type C dialogs — Talia Softheart ───────────────────────────

	{
		'npc_id': 'talia_softheart',
		'dialog_id': 'talia_type_c_intro',
		'dialog': [
			"You look like you've been carrying a lot.",
			"I don't mean your pack.",
			"I've been tending to the hamlet's wounded for three months — there are more than there should be.",
			"The forest's distress is reaching people. I could use someone to help me reach back."
		]
	},
	{
		'npc_id': 'talia_softheart',
		'dialog_id': 'talia_type_c_lyss_check',
		'dialog': [
			"Lyss told you about me? That's — actually that means a lot.",
			"She doesn't say kind things about people unless she means them.",
			"I've been hoping for someone to travel with who actually listens."
		]
	},
	{
		'npc_id': 'talia_softheart',
		'dialog_id': 'talia_type_c_join',
		'dialog': [
			"I'll come with you.",
			"I can't heal the forest from here — I need to go where the wounds are.",
			"Just... tell me when people are hurting. I'm not always good at waiting to be asked."
		]
	},

]

NPC_DIALOG += [

	# ── Type D dialogs — Echofern Blade (mythic weapon) ────────────

	{
		'npc_id': 'whisper_moth_selen',
		'dialog_id': 'selen_d_spore_read',
		'dialog': [
			"This spore carries the Boiling Bubble's oldest memory-network.",
			"The mycelia encoded every story the forest wanted preserved.",
			"The Burrow Whisper feeds on exactly this kind of stored memory.",
			"It has been draining Thornshade's recollections through the root network for years.",
			"Present the spore at the Burrow entrance — the Whisper will surface for it.",
			"Silence it and the memory-metal it guards crystallizes.",
			"Diego can forge memory-crystal into a blade that never forgets a path it has walked."
		]
	},
	{
		'npc_id': 'burrow_whisper',
		'dialog_id': 'burrow_whisper_d_awakens',
		'dialog': [
			"The mycelia spore reaches the Burrows.",
			"You carry the network's oldest memory into my domain.",
			"I have been hungry for this frequency for a very long time.",
			"You will not leave with it."
		]
	},

]

# --- Character dialogs: Type E ---
NPC_DIALOG += [

    # Type E – Investigate Graft
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_forest_small_e_investigate_graft',
        'dialog': [
            "A living cutting sealed for preservation and never retrieved. The original tree has been gone for two generations."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_forest_small_e_investigate_graft',
        'dialog': [
            "Root grafts don't just preserve — they transmit. This one has been trying to reach something for longer than the records can date."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_forest_small_e_investigate_graft',
        'dialog': [
            "The tree it came from is gone, but the cutting is still alive. That's not accident. That's intention."
        ]
    },

    # Type E – Consult Lyss
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_forest_small_e_consult_lyss',
        'dialog': [
            "The Burrow Whisper guards that stretch more fiercely than any other. It's protecting something inside."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_forest_small_e_consult_lyss',
        'dialog': [
            "Sealed alcove, old growth roots around the entrance. The forest asked something to keep watch."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_forest_small_e_consult_lyss',
        'dialog': [
            "It's not protecting the space. It's protecting the graft."
        ]
    },

    # Type E – Confront Burrow Whisper
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_forest_small_e_confront_burrow_whisper',
        'dialog': [
            "It already decided we are not the forest."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_forest_small_e_confront_burrow_whisper',
        'dialog': [
            "'The forest asked us to keep it.' Convenient when you're the one who decided what the forest wanted."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_forest_small_e_confront_burrow_whisper',
        'dialog': [
            "Some keepers forget that the thing they're guarding might still want to leave."
        ]
    },

    # Type E – Defeat Burrow Whisper
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_forest_small_e_defeat_burrow_whisper',
        'dialog': [
            "It's done. Take the graft carefully — it's still alive."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_forest_small_e_defeat_burrow_whisper',
        'dialog': [
            "A cutting that carries the memory of a tree that no longer exists anywhere in Thornshade."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_forest_small_e_defeat_burrow_whisper',
        'dialog': [
            "Fernhollow will want to see it before it decides where it needs to go."
        ]
    },

    # Type E – Return to Fernhollow
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_forest_small_e_return_to_fernhollow',
        'dialog': [
            "Still alive after all this time. The moths have been holding its memory."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_forest_small_e_return_to_fernhollow',
        'dialog': [
            "Root grafts transmit. This one has been trying to reach Boiling Bubble's mycelium for longer than we can measure."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_forest_small_e_return_to_fernhollow',
        'dialog': [
            "When the time comes, the network will know you're there. Carry it until then."
        ]
    },

]

# --- Character dialogs: Type C ---
NPC_DIALOG += [

    # Type C – Find Talia
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_forest_small_c_find_talia',
        'dialog': [
            "She's been tending more wounded than there should be. The forest's distress is reaching people."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_forest_small_c_find_talia',
        'dialog': [
            "She could use someone who actually listens when the wounds start talking."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_forest_small_c_find_talia',
        'dialog': [
            "The hamlet is carrying more than it can hold. She's right to look outward."
        ]
    },

    # Type C – Consult Lyss (Talia path)
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_forest_small_c_consult_lyss',
        'dialog': [
            "Lyss doesn't say kind things about people unless she means them. That matters."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_forest_small_c_consult_lyss',
        'dialog': [
            "She's been hoping for someone who actually listens. Rare request."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_forest_small_c_consult_lyss',
        'dialog': [
            "Some people wait a long time for the right traveling company."
        ]
    },

    # Type C – Earn Talia
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_forest_small_c_earn_talia',
        'dialog': [
            "She can't heal the forest from here. She needs to go where the wounds are."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_forest_small_c_earn_talia',
        'dialog': [
            "Just tell her when people are hurting. She's not always good at waiting to be asked."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_forest_small_c_earn_talia',
        'dialog': [
            "Useful. Welcome."
        ]
    },

]

# --- Character dialogs: Type D ---
NPC_DIALOG += [

    # Type D – Deliver Memory Spore
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_forest_small_d_deliver_memory_spore',
        'dialog': [
            "The memory-network residue is still active. Something in this hamlet resonates with it."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_forest_small_d_deliver_memory_spore',
        'dialog': [
            "Selen follows moth-spirits that carry forest memories. She'll know where this frequency leads."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_forest_small_d_deliver_memory_spore',
        'dialog': [
            "The spore is already speaking to every memory the forest has ever lost."
        ]
    },

    # Type D – Consult Selen
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_forest_small_d_consult_selen',
        'dialog': [
            "The Burrow Whisper has been draining Thornshade's recollections through the root network for years."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grmnaw_forest_small_d_consult_selen',
        'dialog': [
            "Present the spore and it will surface for the frequency it's been hungry for. Clean trap."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_forest_small_d_consult_selen',
        'dialog': [
            "Silence it and the memory-metal crystallizes. A blade that never forgets a path it has walked."
        ]
    },

    # Type D – Meet Burrow Whisper (Spore path)
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_forest_small_d_meet_burrow_whisper',
        'dialog': [
            "It's been hungry for this frequency for a very long time."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_forest_small_d_meet_burrow_whisper',
        'dialog': [
            "'You will not leave with it.' We'll see."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_forest_small_d_meet_burrow_whisper',
        'dialog': [
            "It's not defending territory. It's defending the last meal it still understands."
        ]
    },

    # Type D – Defeat Burrow Whisper (Spore path)
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_forest_small_d_defeat_burrow_whisper',
        'dialog': [
            "Quiet. Take the memory-crystal."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_forest_small_d_defeat_burrow_whisper',
        'dialog': [
            "A blade that remembers every path it has ever walked. You'll never lose your way carrying this."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_forest_small_d_defeat_burrow_whisper',
        'dialog': [
            "Every memory the Whisper drained has returned to the root network. The archive filled itself back in."
        ]
    },

]


TASKS = [
	{
		'task_id': 'forest_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'archivist_fernhollow',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'archivist_fernhollow',
					'standing_text': [
						"Come read the old leaves with me; they hum of distant summers."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'scout_lyss',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scout_lyss',
					'standing_text': [
						"Quiet roads are a blessing — if you've tales, I'll listen between steps."
					]
				}
			},
		],
		'task_complete_events': [
			# Prompt Fernhollow toward the E chain immediately on city arrival
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'archivist_fernhollow',
					'standing_text': [
						"I found something in the old growth records that doesn't add up.",
						"A preservation entry for a graft that was never retrieved."
					]
				}
			},
			# Place Talia so she is ready when the C chain meet task fires
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'talia_softheart',
					'location': 'region_city_other3'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'talia_softheart',
					'standing_text': [
						"The hamlet's wounded keep coming.",
						"The forest's distress reaches people in ways I'm only starting to understand."
					]
				}
			},
			# E chain — no gate; artifact waits in inventory
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_e_investigate_graft'
				}
			},
			# C chain
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_c_find_talia'
				}
			},
			# D chain — deliver task waits until player holds forest_mid_city_e_mycelia_memory_spore
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"That spore — the memory-network residue is still active inside it.",
						"Something in Thornshade Hamlet resonates with it.",
						"Find Selen. She follows moth-spirits that carry forest memories.",
						"She'll know where this frequency leads."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_d_deliver_memory_spore'
				}
			},
		]
	},
]

TASKS += [

	# =========================================================
	# TYPE E — Thornshade Root Graft
	# Artifact ID: forest_small_city_e_thornshade_root_graft
	# Gates: forest_mid_city (Boiling Bubble, Ch.2) Type D — retroactive
	# Awarded by: forest_small_city_initialize
	# Chain: investigate with Fernhollow → consult Lyss → confront Burrow Whisper
	#        → defeat → return to Fernhollow
	# No create_dungeon — NPC-driven per Type E rules.
	# =========================================================

	# E-1 — Fernhollow traces the graft in the old growth records
	{
		'task_id': 'forest_small_city_type_e_investigate_graft',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'archivist_fernhollow',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'archivist_fernhollow',
					'dialog_id': 'fernhollow_root_graft_discovery'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',   'dialog_id': 'tech_forest_small_e_investigate_graft'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',  'dialog_id': 'faith_forest_small_e_investigate_graft'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_forest_small_e_investigate_graft' } },
			# Prime Lyss's standing text before the party goes to her
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scout_lyss',
					'standing_text': [
						"I know the alcove Fernhollow means.",
						"The Burrow Whisper circles it more than anywhere else in the tunnels."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_e_consult_lyss'
				}
			},
		]
	},

	# E-2 — Lyss confirms the Burrow Whisper is guarding the alcove; Whisper is placed
	{
		'task_id': 'forest_small_city_type_e_consult_lyss',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'scout_lyss',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'scout_lyss',
					'dialog_id': 'lyss_root_graft_context'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_forest_small_e_consult_lyss' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_forest_small_e_consult_lyss' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'tech_forest_small_e_consult_lyss'  } },
			{
				'event_type': 'create_dungeon',
				'params': {
					'dungeon_id': 'forest_small_city_burrow_alcove',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'burrow_whisper',
					'location': None
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'burrow_whisper',
					'standing_text': [
						"The Graft sleeps here.",
						"It is not yours to take."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_e_confront_burrow_whisper'
				}
			},
		]
	},

	# E-3 — Confront the Burrow Whisper guarding the sealed alcove
	{
		'task_id': 'forest_small_city_type_e_confront_burrow_whisper',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'burrow_whisper',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'burrow_whisper',
					'dialog_id': 'burrow_whisper_graft_guardian'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',  'dialog_id': 'skill_forest_small_e_confront_burrow_whisper'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_forest_small_e_confront_burrow_whisper'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',  'dialog_id': 'lyren_forest_small_e_confront_burrow_whisper'  } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_e_defeat_burrow_whisper'
				}
			},
		]
	},

	# E-4 — Defeat the Burrow Whisper; claim the artifact
	{
		'task_id': 'forest_small_city_type_e_defeat_burrow_whisper',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'burrow_whisper_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'burrow_whisper_1',
					'combat_type': 'boss_battle'
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'forest_small_city_e_thornshade_root_graft'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_forest_small_e_defeat_burrow_whisper' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',     'dialog_id': 'faith_forest_small_e_defeat_burrow_whisper'     } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_forest_small_e_defeat_burrow_whisper'      } },
			# Set Fernhollow's standing text for the return step
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'archivist_fernhollow',
					'standing_text': [
						"You retrieved it. And it's still alive.",
						"Come — I need to see it."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_e_return_to_fernhollow'
				}
			},
		]
	},

	# E-5 — Return to Fernhollow; he reads the graft and sends the player to carry it
	{
		'task_id': 'forest_small_city_type_e_return_to_fernhollow',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'archivist_fernhollow',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'archivist_fernhollow',
					'dialog_id': 'fernhollow_root_graft_received'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',  'dialog_id': 'faith_forest_small_e_return_to_fernhollow'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',   'dialog_id': 'tech_forest_small_e_return_to_fernhollow'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_forest_small_e_return_to_fernhollow' } },
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE C — Talia Softheart (extended character, slot 2)
	# Awarded by: forest_small_city_initialize
	# Chain: find Talia → Lyss vouches → return to Talia → Talia joins
	# Talia placed in initialize complete events.
	# =========================================================

	# C-1 — Talia introduces herself and asks Lyss to speak for the party
	{
		'task_id': 'forest_small_city_type_c_find_talia',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'talia_softheart',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'talia_softheart',
					'dialog_id': 'talia_type_c_intro'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_forest_small_c_find_talia' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_forest_small_c_find_talia'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_forest_small_c_find_talia' } },
			# Prime Lyss's standing text for the C vouch step
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'scout_lyss',
					'standing_text': [
						"Talia asked me about you.",
						"I told her what I know. She's worth your time."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_c_consult_lyss'
				}
			},
		]
	},

	# C-2 — Lyss vouches; Talia's dialog response fires; Talia updated for C-3
	{
		'task_id': 'forest_small_city_type_c_consult_lyss',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'scout_lyss',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'talia_softheart',
					'dialog_id': 'talia_type_c_lyss_check'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',  'dialog_id': 'faith_forest_small_c_consult_lyss'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_forest_small_c_consult_lyss'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',    'dialog_id': 'nia_forest_small_c_consult_lyss'    } },
			# Update Talia's standing text so she signals she is ready
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'talia_softheart',
					'standing_text': [
						"I've made my decision.",
						"The forest needs more than this hamlet can give right now."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_c_earn_talia'
				}
			},
		]
	},

	# C-3 — Return to Talia; she joins the party
	{
		'task_id': 'forest_small_city_type_c_earn_talia',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'talia_softheart',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'talia_softheart',
					'dialog_id': 'talia_type_c_join'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',  'dialog_id': 'faith_forest_small_c_earn_talia'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',    'dialog_id': 'nia_forest_small_c_earn_talia'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',  'dialog_id': 'skill_forest_small_c_earn_talia'  } },
			{
				'event_type': 'hide_npc',
				'params': { 'npc_id': 'talia_softheart' }
			},
			{
				'event_type': 'character_join',
				'params': { 'character_id': 'talia_softheart' }
			},
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE D — Echofern Blade (mythic weapon, slot 3)
	# Gate: forest_mid_city_e_mycelia_memory_spore (from Boiling Bubble E chain — retroactive)
	# Mythic reward: mythic_forest_small_echofern_blade
	# Deliver to Diego → Selen reads the spore → defeat Burrow Whisper → mythic weapon
	# No new NPCs — uses whisper_moth_selen and burrow_whisper (both city seed NPCs).
	# Diego's standing text set in initialize complete events alongside D award_task.
	# Selen placed in D deliver complete events; burrow_whisper already placed by E chain.
	# =========================================================

	# D-0 — Deliver spore to Diego; he directs the party to Selen
	{
		'task_id': 'forest_small_city_type_d_deliver_memory_spore',
		'type': 'deliver',
		'item_id': 'forest_mid_city_e_mycelia_memory_spore',
		'to_type': 'npc',
		'to_id': 'diego',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'forest_mid_city_e_mycelia_memory_spore'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',   'dialog_id': 'tech_forest_small_d_deliver_memory_spore'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_forest_small_d_deliver_memory_spore'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',  'dialog_id': 'faith_forest_small_d_deliver_memory_spore'  } },
			# Place Selen and set her standing text for the consult step
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'whisper_moth_selen',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'whisper_moth_selen',
					'standing_text': [
						"The moth-spirits clustered around you the moment you entered the hamlet.",
						"That spore you carry — it speaks to every memory the forest has ever lost.",
						"Come quickly. The Burrow already stirs."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_d_consult_selen'
				}
			},
		]
	},

	# D-1 — Selen reads the spore's resonance and identifies the Burrow Whisper's hunger
	{
		'task_id': 'forest_small_city_type_d_consult_selen',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'whisper_moth_selen',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'whisper_moth_selen',
					'dialog_id': 'selen_d_spore_read'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_forest_small_d_consult_selen'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grmnaw_forest_small_d_consult_selen' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',   'dialog_id': 'faith_forest_small_d_consult_selen'   } },
			# Set Burrow Whisper's standing text for the D meet step
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'burrow_whisper',
					'standing_text': [
						"A low resonance bleeds from the Echofern Burrow entrance.",
						"Fernhollow says the archive parchments have gone blank since dawn.",
						"Lyss says the forest has gone completely silent.",
						"The spore has drawn the Whisper forward."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_d_meet_burrow_whisper'
				}
			},
		]
	},

	# D-2 — Meet the Burrow Whisper; it surfaces drawn by the spore's frequency
	{
		'task_id': 'forest_small_city_type_d_meet_burrow_whisper',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'burrow_whisper',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'burrow_whisper',
					'dialog_id': 'burrow_whisper_d_awakens'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',  'dialog_id': 'skill_forest_small_d_meet_burrow_whisper'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_forest_small_d_meet_burrow_whisper'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',  'dialog_id': 'lyren_forest_small_d_meet_burrow_whisper'  } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_small_city_type_d_defeat_burrow_whisper'
				}
			},
		]
	},

	# D-3 — Defeat the Burrow Whisper; Diego forges the mythic weapon
	{
		'task_id': 'forest_small_city_type_d_defeat_burrow_whisper',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'burrow_whisper_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'burrow_whisper_1',
					'combat_type': 'boss_battle'
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_forest_small_echofern_blade'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_forest_small_d_defeat_burrow_whisper' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_forest_small_d_defeat_burrow_whisper'      } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',     'dialog_id': 'faith_forest_small_d_defeat_burrow_whisper'     } },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"Memory-crystal — it forges like hardened thought.",
						"I've worked it into the blade.",
						"It remembers every path it has ever walked.",
						"You'll never lose your way carrying this."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'whisper_moth_selen',
					'standing_text': [
						"The moth-spirits are calm again.",
						"Every memory the Whisper drained has returned to the root network.",
						"Fernhollow says the archive parchments filled back in on their own."
					]
				}
			},
		]
	},

]


PRIMARY_STORY_SETTINGS = {
	'story_id': 'forest_small_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}