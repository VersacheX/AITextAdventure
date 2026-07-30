ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'curator_bramble',
		'name': 'Bramble the Curator',
		'description': (
			'A cheerful historian who preserves the village\'s pastoral traditions.'
			'  Bramble\'s satchel is filled with pressed flowers and old folk charms.'
			'  He treats every visitor like a long‑lost relative.'
		)
	},
	{
		'npc_id': 'librarian_sylfa',
		'name': 'Sylfa Meadowreader',
		'description': (
			'A soft‑spoken keeper of stories who reads by bioluminescent lanterns.'
			'  Sylfa believes books choose their readers, not the other way around.'
			'  Her calm demeanor soothes even the most road‑weary travelers.'
		)
	},
	{
		'npc_id': 'hearth_seer_marnel',
		'name': 'Marnel the Hearth‑Seer',
		'description': (
			'A wandering storyteller who senses when folk tales drift from their true paths.'
		)
	},
	{
		'npc_id': 'thicket_story',
		'name': 'Thicket Story',
		'description': (
			'A living tale grown wild within the Meadowtale Thicket.'
		)
	},
	{
		'npc_id': 'charmroot_voice',
		'name': 'Charmroot Voice',
		'description': (
			'A murmuring presence formed from corrupted folk charms deep in the Charmroot Den.'
		)
	}
]


NPC_DIALOG = [

	{
		'npc_id': 'curator_bramble',
		'dialog_id': 'bramble_intro',
		'dialog': [
			"The fields hum with strange tales.",
			"Folk charms twist into shapes I've never seen.",
			"Something meddles with our simplest stories."
		]
	},
	{
		'npc_id': 'librarian_sylfa',
		'dialog_id': 'sylfa_intro',
		'dialog': [
			"Books whisper warnings.",
			"Stories shift when the meadow is uneasy.",
			"A Hollow spirit rewrites our gentlest lore."
		]
	},
	{
		'npc_id': 'hearth_seer_marnel',
		'dialog_id': 'marnel_intro',
		'dialog': [
			"The meadow's tales wander off their paths.",
			"A Folklore Hollow stirs beneath the roots.",
			"If it wakes fully, our traditions will turn against us."
		]
	},
	{
		'npc_id': 'thicket_story',
		'dialog_id': 'thicket_story_intro',
		'dialog': [
			"We are the tales that grew wild.",
			"The Hollow twists us into danger.",
			"It waits deeper in the Charmroot Den."
		]
	},
	{
		'npc_id': 'charmroot_voice',
		'dialog_id': 'charmroot_voice_intro',
		'dialog': [
			"The Den trembles with corrupted charms.",
			"The Hollow feeds on forgotten stories.",
			"Only its heart remains to be quieted."
		]
	},
	{
		'npc_id': 'curator_bramble',
		'dialog_id': 'bramble_closing',
		'dialog': [
			"The fields breathe easy again.",
			"Our stories return to their gentle shapes.",
			"You've saved our traditions from being lost."
		]
	},

]


TASKS = [
	{
		'task_id': 'grassland_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'curator_bramble',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'curator_bramble',
					'standing_text': [
						"Welcome! The fields have stories—sit and I'll tell you one."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'librarian_sylfa',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'librarian_sylfa',
					'standing_text': [
						"Books choose readers—perhaps one chose you. Care to listen?"
					]
				}
			},
		],
		'task_complete_events': [
            { 'event_type': 'award_task', 'params': { 'task_id': 'grassland_small_city_type_a_ch12_find_keepsake' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_small_city_type_c_find_rynn' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_small_city_type_d_deliver_grief_token' }},
		]
	},
]


# ── Type C ── Rynn (extended character) ───────────────────────────────────────
# Gated by is_chapter_gte: 12. Rynn has come to Quantford Hollow after
# hearing that folk-charm wounds resist normal treatment. Sylfa's trust
# opens him up to the party.

NPC_DIALOG += [

	{
		'npc_id': 'rynn',
		'dialog_id': 'rynn_c_first_meet',
		'dialog': [
			"These folk-charm wounds don't close the way they should.",
			"I've treated a dozen people this week alone.",
			"Whatever is corrupting the hollow's traditions — it bleeds into the body too.",
			"I can't leave until I understand it."
		]
	},

	{
		'npc_id': 'librarian_sylfa',
		'dialog_id': 'sylfa_c_vouch',
		'dialog': [
			"Rynn arrived three days ago and hasn't rested since.",
			"He remembers every patient by name.",
			"That kind of care is rare.",
			"Tell him I said the books trust him.",
			"He'll understand what that means."
		]
	},

	{
		'npc_id': 'rynn',
		'dialog_id': 'rynn_c_joins',
		'dialog': [
			"Sylfa said the books trust you.",
			"She doesn't say that lightly.",
			"I've done what I can here.",
			"If the corruption spreads further out there, you'll need a medic who remembers.",
			"I'm coming with you."
		]
	},

]

# --- Character dialogs: Type C ---
NPC_DIALOG += [

    # Type C – Find Rynn
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_grassland_small_c_find_rynn',
        'dialog': [
            "Folk-charm wounds that won't close the way they should. The corruption is bleeding into the body."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_grassland_small_c_find_rynn',
        'dialog': [
            "He's treated a dozen people this week and still won't leave until he understands it. That kind of care is rare."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_grassland_small_c_find_rynn',
        'dialog': [
            "Whatever is wrong with the hollow's traditions is reaching the people who live by them."
        ]
    },

    # Type C – Consult Sylfa
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_grassland_small_c_consult_sylfa',
        'dialog': [
            "He remembers every patient by name. Sylfa noticed."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_grassland_small_c_consult_sylfa',
        'dialog': [
            "'The books trust him.' That's not a small endorsement from a librarian."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_grassland_small_c_consult_sylfa',
        'dialog': [
            "Tell him that. He'll understand what it means."
        ]
    },

    # Type C – Earn Rynn
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_grassland_small_c_earn_rynn',
        'dialog': [
            "Sylfa doesn't say that lightly. It settled it for him."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_grassland_small_c_earn_rynn',
        'dialog': [
            "If the corruption spreads further out there, we'll need a medic who remembers."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_grassland_small_c_earn_rynn',
        'dialog': [
            "He's coming. Good."
        ]
    },

]

# --- Character dialogs: Type D ---
NPC_DIALOG += [

    # Type D – Deliver Grief Token
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_grassland_small_d_deliver_grief_token',
        'dialog': [
            "A grief token from a noble's estate. The charm residue hasn't faded after all these years."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_grassland_small_d_deliver_grief_token',
        'dialog': [
            "These are extraordinarily rare. Marnel reads folk tales better than anyone — she'll know which story it belongs to."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_grassland_small_d_deliver_grief_token',
        'dialog': [
            "An unfinished story that still carries weight. Of course Mira wants a closer look."
        ]
    },

    # Type D – Consult Marnel
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_grassland_small_d_consult_marnel',
        'dialog': [
            "It carries the echo of a story that was never finished. The lineage held onto it for generations."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_grassland_small_d_consult_marnel',
        'dialog': [
            "The Charmroot Voice feeds on exactly this kind of unresolved tale. Draw it out and the grief crystallizes."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grmnaw_grassland_small_d_consult_marnel',
        'dialog': [
            "Mira can set crystallized grief into a talisman that carries the weight without breaking the wearer."
        ]
    },

    # Type D – Meet Charmroot Voice
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_grassland_small_d_meet_charmroot_voice',
        'dialog': [
            "It already decided it will write the ending — and ours."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_grassland_small_d_meet_charmroot_voice',
        'dialog': [
            "An unfinished story walking into its den. Bold move on our part."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_grassland_small_d_meet_charmroot_voice',
        'dialog': [
            "Some voices only know how to finish what was left open. We don't let this one choose the ending."
        ]
    },

    # Type D – Defeat Charmroot Voice
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_grassland_small_d_defeat_charmroot_voice',
        'dialog': [
            "It's done. Take the crystallized grief carefully."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_grassland_small_d_defeat_charmroot_voice',
        'dialog': [
            "A talisman that carries the weight of every unfinished story — and somehow that makes it stronger."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_grassland_small_d_defeat_charmroot_voice',
        'dialog': [
            "Every story the Voice corrupted has resolved itself. The folk charms glow properly again."
        ]
    },

]

# --- Character dialogs: Type A ---
NPC_DIALOG += [

    # Type A – Ch12 Find Keepsake
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_grassland_small_a_ch12_find_keepsake',
        'dialog': [
            "Pressed with real care. The petals kept their colour perfectly."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_grassland_small_a_ch12_find_keepsake',
        'dialog': [
            "Someone left this waiting for the right person to claim it."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_grassland_small_a_ch12_find_keepsake',
        'dialog': [
            "Bramble held it in the archive until the right hands showed up. Take it where it needs to go."
        ]
    },

]


TASKS += [

	# C-1 — Find Rynn
	{
		'task_id': 'grassland_small_city_type_c_find_rynn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rynn',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'rynn',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rynn',
					'standing_text': [
						"The folk-charm wounds are unlike anything I've treated before.",
						"Something is very wrong with the hollow's traditions."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rynn',
					'dialog_id': 'rynn_c_first_meet'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_grassland_small_c_find_rynn' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_grassland_small_c_find_rynn'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_grassland_small_c_find_rynn' } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_small_city_type_c_consult_sylfa'
				}
			},
		]
	},

	# C-2 — Get Sylfa's endorsement
	{
		'task_id': 'grassland_small_city_type_c_consult_sylfa',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'librarian_sylfa',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'librarian_sylfa',
					'dialog_id': 'sylfa_c_vouch'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_grassland_small_c_consult_sylfa' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'tech_grassland_small_c_consult_sylfa'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_grassland_small_c_consult_sylfa'   } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_small_city_type_c_earn_rynn'
				}
			},
		]
	},

	# C-3 — Return to Rynn; he joins
	{
		'task_id': 'grassland_small_city_type_c_earn_rynn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rynn',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rynn',
					'standing_text': [
						"Sylfa sent you back.",
						"The books trust you.",
						"That settles it."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rynn',
					'dialog_id': 'rynn_c_joins'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_grassland_small_c_earn_rynn' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_grassland_small_c_earn_rynn'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_grassland_small_c_earn_rynn' } },
			{
				'event_type': 'character_join',
				'params': {
					'character_id': 'rynn'
				}
			},
		]
	},

]


# ── Type D ── Folklore Hollow Talisman (mythic accessory) ─────────────────────
# Gate: player holds hollow_grief_token from nobles_mansion (Ch.3 dungeon).
# Deliver to Mira → Marnel reads the token → defeat Charmroot Voice → mythic accessory.
# No new NPCs — uses hearth_seer_marnel, charmroot_voice, and mira (Ch.2 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'hearth_seer_marnel',
		'dialog_id': 'marnel_d_token_read',
		'dialog': [
			"This grief token — it carries the echo of a story that was never finished.",
			"The noble's lineage held onto it for generations.",
			"The Charmroot Voice feeds on exactly this kind of unresolved tale.",
			"Draw it out with the token's resonance and the Voice will surface.",
			"Silence it properly and the grief crystallizes into something pure.",
			"Mira can set crystallized grief into a talisman that carries its weight without breaking you."
		]
	},

	{
		'npc_id': 'charmroot_voice',
		'dialog_id': 'charmroot_voice_d_awakens',
		'dialog': [
			"The grief token opens the Den.",
			"You carry an unfinished story into my domain.",
			"I will write its ending — and yours."
		]
	},

]

TASKS += [

	# D-0 — Deliver hollow_grief_token to Mira (standalone deliver; unlocks D chain)
	{
		'task_id': 'grassland_small_city_type_d_deliver_grief_token',
		'type': 'deliver',
		'item_id': 'hollow_grief_token',
		'to_type': 'npc',
		'to_id': 'mira',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"A grief token from a noble's estate — these are extraordinarily rare.",
						"The charm residue on it hasn't faded after all these years.",
						"Find Marnel. She reads folk tales better than anyone.",
						"She'll know what story this belongs to."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'hollow_grief_token'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'tech_grassland_small_d_deliver_grief_token'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_grassland_small_d_deliver_grief_token' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_grassland_small_d_deliver_grief_token' } },
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'hearth_seer_marnel',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_small_city_type_d_consult_marnel'
				}
			},
		]
	},

	# D-1 — Consult Marnel for the token reading
	{
		'task_id': 'grassland_small_city_type_d_consult_marnel',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'hearth_seer_marnel',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'hearth_seer_marnel',
					'standing_text': [
						"The meadow's tales shifted the moment you arrived.",
						"That token you carry — it's the end of a story the hollow never finished.",
						"Come. The Charmroot Den is already listening."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'hearth_seer_marnel',
					'dialog_id': 'marnel_d_token_read'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',   'dialog_id': 'faith_grassland_small_d_consult_marnel'   } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'tech_grassland_small_d_consult_marnel'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grmnaw_grassland_small_d_consult_marnel' } },
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'charmroot_voice',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_small_city_type_d_meet_charmroot_voice'
				}
			},
		]
	},

	# D-2 — Meet the Charmroot Voice (boss intro)
	{
		'task_id': 'grassland_small_city_type_d_meet_charmroot_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'charmroot_voice',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'charmroot_voice',
					'standing_text': [
						"The Charmroot Den hums with a low, mournful resonance.",
						"Bramble says the folk charms near the entrance have gone completely dark.",
						"The grief token has drawn the Voice forward."
					]
				}
			},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'charmroot_voice',
					'dialog_id': 'charmroot_voice_d_awakens'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',  'dialog_id': 'skill_grassland_small_d_meet_charmroot_voice'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_grassland_small_d_meet_charmroot_voice'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',  'dialog_id': 'lyren_grassland_small_d_meet_charmroot_voice'  } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_small_city_type_d_defeat_charmroot_voice'
				}
			},
		]
	},

	# D-3 — Defeat the Charmroot Voice; Mira crafts the mythic accessory
	{
		'task_id': 'grassland_small_city_type_d_defeat_charmroot_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'charmroot_voice_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'charmroot_voice_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_grassland_small_folklore_hollow_talisman'
				}
			},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_grassland_small_d_defeat_charmroot_voice' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',     'dialog_id': 'faith_grassland_small_d_defeat_charmroot_voice'     } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',      'dialog_id': 'tech_grassland_small_d_defeat_charmroot_voice'      } },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"Crystallized grief — I've never worked with anything so delicate.",
						"I've set it into the talisman.",
						"It carries the weight of every unfinished story.",
						"And somehow that makes it stronger than anything I've ever made."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'hearth_seer_marnel',
					'standing_text': [
						"The meadow's tales have returned to their true paths.",
						"Every story the Voice corrupted has resolved itself.",
						"Bramble says the folk charms glow properly again."
					]
				}
			},
		]
	},

]


# ── Type A ── Ch.12 Chapter Tie-In (Ember's Pressed Flower) ──────────────────
# Awarded when Rell farewells the party in Ch.12. Bramble the Curator has
# been preserving a pressed flower found in the meadow fields — he doesn't
# know who it belongs to, but he kept it because it was too beautiful to
# leave. No new NPCs — Bramble is in the city seed.

NPC_DIALOG += [

    {
        'npc_id': 'curator_bramble',
        'dialog_id': 'bramble_a_ch12_pressed_flower',
        'dialog': [
            "Oh, you're looking for something specific? Let me think.",
            "Actually — yes. I found a pressed flower near the old performance fields.",
            "Extraordinary specimen. The petals kept their colour perfectly.",
            "I've been holding it in the archive waiting for someone to claim it.",
            "(carefully retrieving it from a wrapped cloth)",
            "Here. It clearly matters to someone. I can see it in how it was pressed — with real care.",
            "Take it where it needs to go."
        ]
    },

]

TASKS += [

    # A-1 — Meet Bramble to recover Ember's pressed flower
    {
        'task_id': 'grassland_small_city_type_a_ch12_find_keepsake',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'curator_bramble',
        'task_acquire_events': [
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'curator_bramble', 'standing_text': [
                "I found something in the performance fields that belongs to someone.",
                "A pressed flower. Beautiful work. Waiting for the right person to claim it."
            ]}}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'curator_bramble', 'dialog_id': 'bramble_a_ch12_pressed_flower' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',  'dialog_id': 'faith_grassland_small_a_ch12_find_keepsake'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',    'dialog_id': 'nia_grassland_small_a_ch12_find_keepsake'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',  'dialog_id': 'magic_grassland_small_a_ch12_find_keepsake'  } },
            { 'event_type': 'award_item', 'params': { 'item_id': 'embers_pressed_flower' }},
        ]
    },

]


PRIMARY_STORY_SETTINGS = {
	'story_id': 'grassland_small_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}