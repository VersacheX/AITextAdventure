ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'runeforger_bjorn',
		'name': 'Bjorn Runeforger',
		'description': (
			'A muscular craftsman who carves runes into weapons and armor.'
			' Bjorn\'s forge burns with unnatural blue flame.'
			' He insists each rune must be sung into existence.'
		)
	},
	{
		'npc_id': 'speaker_yrsa',
		'name': 'Yrsa Icebound',
		'description': (
			'A mystic who communes with ancestral spirits through ritual chants.'
			' Yrsa\'s voice resonates like wind across frozen cliffs.'
			' She carries the weight of countless whispered histories.'
		)
	},
    {
        'npc_id': 'chant_seer_haldrin',
        'name': 'Haldrin the Chant‑Seer',
        'description': (
            'A mystic who hears rune echoes trapped in the ice and senses when chants fracture.'
        )
    },
    {
        'npc_id': 'rimechant_echo',
        'name': 'Rimechant Echo',
        'description': (
            'A spectral remnant of frozen chants twisted by the Shattered Rune.'
        )
    },
    {
        'npc_id': 'blueforge_spirit',
        'name': 'Blueforge Spirit',
        'description': (
            'A molten‑blue apparition formed from unstable flame deep within the Blueforge Depths.'
        )
    }
]


NPC_DIALOG = [

    # --- Base city standing dialog ---

    {
        'npc_id': 'runeforger_bjorn',
        'dialog_id': 'bjorn_intro',
        'dialog': [
            "The runes resist the flame.",
            "Their meanings twist beneath the ice.",
            "Something breaks their song."
        ]
    },
    {
        'npc_id': 'speaker_yrsa',
        'dialog_id': 'yrsa_intro',
        'dialog': [
            "The chants echo wrong.",
            "Ancestral voices strain to reach us.",
            "A force blocks their path."
        ]
    },
    {
        'npc_id': 'chant_seer_haldrin',
        'dialog_id': 'haldrin_intro',
        'dialog': [
            "The rune echoes fracture.",
            "A Shattered Rune rises — a spirit of broken chants.",
            "If it awakens fully, the ancestors will fall silent."
        ]
    },
    {
        'npc_id': 'rimechant_echo',
        'dialog_id': 'rimechant_echo_intro',
        'dialog': [
            "We are the chants that froze wrong.",
            "The Shattered Rune twists our echoes.",
            "It waits deeper in the Blueforge Depths."
        ]
    },
    {
        'npc_id': 'blueforge_spirit',
        'dialog_id': 'blueforge_spirit_intro',
        'dialog': [
            "The Depths burn with unstable blue flame.",
            "The Shattered Rune gathers strength.",
            "Only its heart remains to be stilled."
        ]
    },
    {
        'npc_id': 'runeforger_bjorn',
        'dialog_id': 'bjorn_closing',
        'dialog': [
            "The runes sing true again.",
            "The forge burns steady.",
            "You've restored the voice of the ancestors."
        ]
    }

]

NPC_DIALOG += [

    # --- Type E: Pageant Decree Shard ---

    {
        'npc_id': 'speaker_yrsa',
        'dialog_id': 'yrsa_decree_shard_discovery',
        'dialog': [
            "During the last deep chant I reached something I didn't expect.",
            "An ancestral voice carrying the memory of a ruling decree — not a battle, not a death.",
            "A formal pact. The kind made between clans at the height of the old Pageant courts.",
            "Part of the physical record is still preserved in the ice somewhere beneath the Rimechant Hall."
        ]
    },
    {
        'npc_id': 'chant_seer_haldrin',
        'dialog_id': 'haldrin_decree_shard_context',
        'dialog': [
            "The Pageant Decree Shards were binding documents — clan agreements forged into stone and distributed.",
            "They were never meant to leave the ice. The Rimechant Echo absorbed one long ago.",
            "It doesn't guard it out of malice. The echo simply doesn't know how to let go.",
            "You'll need to break the bond by force."
        ]
    },
    {
        'npc_id': 'rimechant_echo',
        'dialog_id': 'rimechant_echo_decree_guardian',
        'dialog': [
            "The Shard is part of our chant now.",
            "To take it is to silence a voice that has spoken for centuries.",
            "We will not be silenced."
        ]
    },
    {
        'npc_id': 'speaker_yrsa',
        'dialog_id': 'yrsa_decree_shard_received',
        'dialog': [
            "The ancestral voice quieted the moment you returned.",
            "It said what it needed to say.",
            "This shard is not meant for an archive — it's meant for someone who will act on it.",
            "Carry it. The pact it records will matter again someday."
        ]
    },

]

NPC_DIALOG += [

    # --- Type F: Audit Testimony Seal ---

    {
        'npc_id': 'runeforger_bjorn',
        'dialog_id': 'bjorn_marlo_tip',
        'dialog': [
            "An auditor came through last month. Marlo Finch — Council credentials, very official.",
            "He was asking about resource allocations. Forge requisitions, shipment records, that sort of thing.",
            "Left in a hurry when the storms rolled in. Said he'd return. He hasn't."
        ]
    },
    {
        'npc_id': 'marlo_finch',
        'dialog_id': 'marlo_finch_hailward_intro',
        'dialog': [
            "I was starting to think no one would come.",
            "I've been documenting requisition fraud across three snow-region cities.",
            "Hailward Hold is the linchpin — whoever authorized these forge allocations signed off on the entire chain.",
            "I need a witness testimony. Someone in this city saw the original transaction."
        ]
    },
    {
        'npc_id': 'speaker_yrsa',
        'dialog_id': 'yrsa_marlo_testimony',
        'dialog': [
            "The auditor wants the old council records? I was there when those allocations were approved.",
            "I did not agree with the decision then. I will not protect it now.",
            "Tell him I'll sign whatever document he needs."
        ]
    },
    {
        'npc_id': 'marlo_finch',
        'dialog_id': 'marlo_finch_hailward_seal',
        'dialog': [
            "Yrsa's testimony is exactly what I needed.",
            "With this, the audit trail leads directly to the distribution end — which means Bayou Nocturne.",
            "The final transaction was routed south. I'll follow it eventually.",
            "Take this seal. It's a certified copy of everything compiled here.",
            "If you reach the Bayou before I do, show it to whoever's holding the other end of this chain."
        ]
    },

]

# --- Character dialogs: Type E (Pageant Decree Shard chain) ---
NPC_DIALOG += [

    # Type E – Investigate Decree
    { 'npc_id': 'tech',    'dialog_id': 'kade_snow_mid_e_investigate_decree',    'dialog': [ "An ancestral voice carrying the memory of a formal decree — not a battle, not a death. A pact made between clans at the height of the old Pageant courts." ] },
    { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_mid_e_investigate_decree', 'dialog': [ "Part of the physical record is still preserved in the ice beneath the Rimechant Hall." ] },
    { 'npc_id': 'skill',   'dialog_id': 'poise_snow_mid_e_investigate_decree',   'dialog': [ "Haldrin will know how the Echo has been holding it." ] },

    # Type E – Consult Haldrin
    { 'npc_id': 'tech',    'dialog_id': 'kade_snow_mid_e_consult_haldrin',    'dialog': [ "The Pageant Decree Shards were binding documents — clan agreements forged into stone. The Rimechant Echo absorbed one long ago." ] },
    { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_mid_e_consult_haldrin', 'dialog': [ "It doesn't guard out of malice. The echo simply doesn't know how to let go. The bond has to be broken by force." ] },
    { 'npc_id': 'skill',   'dialog_id': 'poise_snow_mid_e_consult_haldrin',   'dialog': [ "Then we break it." ] },

    # Type E – Confront Rimechant Echo
    { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_e_confront_rimechant_echo', 'dialog': [ "It already decided the Shard is part of its chant." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_mid_e_confront_rimechant_echo', 'dialog': [ "'To take it is to silence a voice that has spoken for centuries.' Dramatic. Accurate, maybe." ] },
    { 'npc_id': 'lyren', 'dialog_id': 'lyren_snow_mid_e_confront_rimechant_echo', 'dialog': [ "Some voices only know how to keep speaking. They never learned how to finish." ] },

    # Type E – Defeat Rimechant Echo / Return to Yrsa
    { 'npc_id': 'technique', 'dialog_id': 'chock_snow_mid_e_return_to_yrsa', 'dialog': [ "The bond is broken. The ancestral voice quieted the moment we returned." ] },
    { 'npc_id': 'faith', 'dialog_id': 'kaera_snow_mid_e_return_to_yrsa', 'dialog': [ "It said what it needed to say. This shard is not meant for an archive — it's meant for someone who will act on it." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_e_return_to_yrsa',  'dialog': [ "The pact it records will matter again someday. Carry it." ] },

]

# --- Character dialogs: Type F (Audit Testimony Seal chain) ---
NPC_DIALOG += [

    # Type F – Find Marlo Trail
    { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_f_find_marlo_trail',  'dialog': [ "An auditor with Council credentials asking about forge requisitions and shipment records. Left in a hurry when the storms rolled in." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_mid_f_find_marlo_trail', 'dialog': [ "Said he'd return. He hasn't. Classic." ] },
    { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_f_find_marlo_trail', 'dialog': [ "Find him." ] },

    # Type F – Find Marlo
    { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_f_find_marlo',  'dialog': [ "Requisition fraud across three snow-region cities. Hailward Hold is the linchpin — whoever authorized the forge allocations signed off on the entire chain." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_mid_f_find_marlo', 'dialog': [ "He needs a witness who saw the original transaction. Yrsa was there." ] },
    { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_f_find_marlo', 'dialog': [ "Get her testimony." ] },

    # Type F – Get Yrsa Testimony
    { 'npc_id': 'faith', 'dialog_id': 'kaera_snow_mid_f_get_yrsa_testimony', 'dialog': [ "She was there when those allocations were approved. She did not agree with the decision then. She will not protect it now." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_f_get_yrsa_testimony',  'dialog': [ "She'll sign whatever document he needs. Long past time someone investigated those records." ] },
    { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_f_get_yrsa_testimony', 'dialog': [ "Return to Marlo." ] },

    # Type F – Return to Marlo
    { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_f_return_to_marlo',  'dialog': [ "With this, the audit trail leads directly to the distribution end — Bayou Nocturne. The final transaction was routed south." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_mid_f_return_to_marlo', 'dialog': [ "A certified copy of everything compiled here. If we reach the Bayou first, we show it to whoever's holding the other end of the chain." ] },
    { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_f_return_to_marlo', 'dialog': [ "Take the seal." ] },

]

# --- Character dialogs: Type D (Blueforge Warplate chain) ---
NPC_DIALOG += [

    # Type D – Deliver Decree Shard
    { 'npc_id': 'brawn', 'dialog_id': 'brawn_snow_mid_d_decree_shard', 'dialog': 
        [ 
            "That shard…",
            "(holds it against the anvil for a second, listening)",
            "Rune-frequency I’ve never felt in any metal. It’s not forge-heat. It’s declaration — something that was spoken into the stone and never finished.",
            "Something in Hailward Hold is still answering it. Every tool on my rack just hummed the same note.",
            "Bjorn carves these marks for a living. He’ll know exactly which Depths this is calling to.",
            "Take it to him before the blue flame finishes noticing you’re carrying it.",
            "And if the ancestral chants start getting drowned out while you’re walking… keep moving."
        ]
    },
    { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_d_deliver_decree_shard',  'dialog': [ "The rune-frequency vibrating off it is unlike anything Brawn has felt. Something in Hailward Hold resonates with it." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_mid_d_deliver_decree_shard', 'dialog': [ "Bjorn carves runes for a living. He'll know exactly what this is calling to." ] },
    { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_d_deliver_decree_shard', 'dialog': [ "Find him before the Depths notice it too." ] },

    # Type D – Consult Bjorn
    { 'npc_id': 'tech',    'dialog_id': 'kade_snow_mid_d_consult_bjorn',    'dialog': [ "The rune-frequency matches the Blueforge Depths' resonance signature almost exactly. The Spirit has been drawing heat from his forge for years." ] },
    { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_mid_d_consult_bjorn', 'dialog': [ "Present the shard and it will surface. Silence it correctly and the blue-forge metal crystallizes." ] },
    { 'npc_id': 'skill',   'dialog_id': 'poise_snow_mid_d_consult_bjorn',   'dialog': [ "Then we present it." ] },

    # Type D – Meet Blueforge Spirit
    { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_d_meet_blueforge_spirit', 'dialog': [ "It already decided the blue-forge metal is its and we must survive its flame to claim it." ] },
    { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_mid_d_meet_blueforge_spirit', 'dialog': [ "The frequency it's fed on since the first forge burned here. It's been waiting a long time." ] },
    { 'npc_id': 'lyren', 'dialog_id': 'lyren_snow_mid_d_meet_blueforge_spirit', 'dialog': [ "Some spirits only know how to hold what the runes once declared. We take it back." ] },

    # Type D – Defeat Blueforge Spirit
    { 'npc_id': 'technique', 'dialog_id': 'chock_snow_mid_d_defeat_blueforge_spirit', 'dialog': [ "It's down. Take the blue-forge crystal." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_d_defeat_blueforge_spirit',  'dialog': [ "Nothing has ever sung like this. Brawn will hammer it into warplate that holds against ice or rift." ] },
    { 'npc_id': 'faith', 'dialog_id': 'kaera_snow_mid_d_defeat_blueforge_spirit', 'dialog': [ "The blue flame burns clean again. The runes sing the way they're supposed to." ] },

]

# --- Character dialogs: Type E post-chain (Shard path) ---
NPC_DIALOG += [

    # Type E – Consult Bjorn (Shard path)
    { 'npc_id': 'tech',    'dialog_id': 'kade_snow_mid_e_consult_bjorn',    'dialog': [ "The pattern is from the old Hold ceremonies. Hailward's founders used it to open their greatest works." ] },
    { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_mid_e_consult_bjorn', 'dialog': [ "A decree shard means something was declared and never answered. The Hold will know what to do with it." ] },
    { 'npc_id': 'skill',   'dialog_id': 'poise_snow_mid_e_consult_bjorn',   'dialog': [ "Collect it from Yrsa." ] },

    # Type E – Collect Shard
    { 'npc_id': 'faith', 'dialog_id': 'kaera_snow_mid_e_collect_shard', 'dialog': [ "The ancestors sent this up from the Depths when the Shattered Rune fell. A formal declaration of something." ] },
    { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_e_collect_shard',  'dialog': [ "Bjorn says the rune patterns match a forge-mark used only in Hailward Hold ceremonial work. It must go back there." ] },
    { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_e_collect_shard', 'dialog': [ "The decree wants to be completed." ] },

]


TASKS = [
	{
		'task_id': 'snow_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'runeforger_bjorn',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'runeforger_bjorn',
					'standing_text': [
						"Runes remember deeds—sit by the forge and tell me one of yours."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'speaker_yrsa',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'speaker_yrsa',
					'standing_text': [
						"Ancestral winds carry many tales—speak softly and the cliffs will answer."
					]
				}
			}
		],
		'task_complete_events': [
            # Type E — no gate condition, artifact waits in inventory
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_type_e_investigate_decree'
                }
            },
            # Type F — Marlo active from Ch.4
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_type_f_find_marlo_trail'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_type_d_deliver_decree_shard'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_type_e_consult_bjorn'
                }
            }
		]
	},

]

TASKS += [

    # =========================================================
    # TYPE E — Pageant Decree Shard
    # Artifact ID: snow_mid_city_e_pageant_decree_shard
    # Gates: snow_mid_city Type D (Slot 2) — same city
    # Awarded by: snow_mid_city_initialize
    # =========================================================

    {
        'task_id': 'snow_mid_city_type_e_investigate_decree',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'speaker_yrsa',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'speaker_yrsa',
                    'dialog_id': 'yrsa_decree_shard_discovery'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_snow_mid_e_investigate_decree'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_mid_e_investigate_decree' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_snow_mid_e_investigate_decree'   } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'speaker_yrsa', 'standing_text': [ "The ancestral voice is calling for the shard to be returned to the Hold." ] } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_type_e_consult_haldrin'
                }
            }
        ]
    },

    {
        'task_id': 'snow_mid_city_type_e_consult_haldrin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'chant_seer_haldrin',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'chant_seer_haldrin',
                    'location': 'region_city_other1'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'chant_seer_haldrin',
                    'dialog_id': 'haldrin_decree_shard_context'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_snow_mid_e_consult_haldrin'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_mid_e_consult_haldrin' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_snow_mid_e_consult_haldrin'   } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'chant_seer_haldrin', 'standing_text': [ "The Shard is part of the chant now. The echo doesn't know how to let go." ] } },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'rimechant_echo',
                    'location': None
                }
            },
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'snow_mid_city_rimechant_hall',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rimechant_echo',
                    'standing_text': [
                        "The Shard is part of our chant.",
                        "You cannot have it."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_type_e_confront_rimechant_echo'
                }
            }
        ]
    },

    {
        'task_id': 'snow_mid_city_type_e_confront_rimechant_echo',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rimechant_echo',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rimechant_echo',
                    'dialog_id': 'rimechant_echo_decree_guardian'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_e_confront_rimechant_echo' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_mid_e_confront_rimechant_echo' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_snow_mid_e_confront_rimechant_echo' } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_type_e_defeat_rimechant_echo'
                }
            }
        ]
    },

    {
        'task_id': 'snow_mid_city_type_e_defeat_rimechant_echo',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'rimechant_echo',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'rimechant_echo',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'rimechant_echo'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_type_e_return_to_yrsa'
                }
            }
        ]
    },

    {
        'task_id': 'snow_mid_city_type_e_return_to_yrsa',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'speaker_yrsa',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'speaker_yrsa',
                    'dialog_id': 'yrsa_decree_shard_received'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_snow_mid_e_return_to_yrsa' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_snow_mid_e_return_to_yrsa' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_e_return_to_yrsa'  } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'speaker_yrsa', 'standing_text': [ "The ancestral voice is quiet now. The shard is not meant for an archive — it's meant for someone who will act on it." ] } },
        ]
    },

]

TASKS += [

    # =========================================================
    # TYPE F — Audit Testimony Seal
    # Faction Item ID: snow_mid_city_f_audit_testimony_seal
    # Recurring NPC: marlo_finch (Ch.4, Ch.16, Ch.20)
    # Gates: swamp_mid_city (Bayou Nocturne, Ch.20) Type D (Slot 2)
    # Awarded by: snow_mid_city_initialize (is_chapter_gte 4)
    # =========================================================

    {
        'task_id': 'snow_mid_city_type_f_find_marlo_trail',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'runeforger_bjorn',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'runeforger_bjorn',
                    'dialog_id': 'bjorn_marlo_tip'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_f_find_marlo_trail'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_mid_f_find_marlo_trail' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_f_find_marlo_trail' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'runeforger_bjorn', 'standing_text': [ "An auditor came through last month. Marlo Finch — Council credentials, very official. He was asking about resource allocations. Forge requisitions, shipment records, that sort of thing." ] } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_type_f_find_marlo'
                }
            }
        ]
    },

    {
        'task_id': 'snow_mid_city_type_f_find_marlo',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'marlo_finch',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'marlo_finch',
                    'dialog_id': 'marlo_finch_hailward_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_f_find_marlo'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_mid_f_find_marlo' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_f_find_marlo' } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_type_f_get_yrsa_testimony'
                }
            }
        ]
    },

    {
        'task_id': 'snow_mid_city_type_f_get_yrsa_testimony',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'speaker_yrsa',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'speaker_yrsa',
                    'dialog_id': 'yrsa_marlo_testimony'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_snow_mid_f_get_yrsa_testimony' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_f_get_yrsa_testimony'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_f_get_yrsa_testimony' } },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'speaker_yrsa',
                    'standing_text': [
                        "An auditor needs testimony about the old council allocations?",
                        "It's long past time someone investigated those records."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_mid_city_type_f_return_to_marlo'
                }
            }
        ]
    },

    {
        'task_id': 'snow_mid_city_type_f_return_to_marlo',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'marlo_finch',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'marlo_finch',
                    'dialog_id': 'marlo_finch_hailward_seal'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_f_return_to_marlo'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_mid_f_return_to_marlo' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_f_return_to_marlo' } },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'snow_mid_city_f_audit_testimony_seal'
                }
            }
        ]
    },

]

# ── Type E ── Pageant Decree Shard → gates Snow Mid Type D ────────────────────
# Yrsa Icebound recovered a shard of carved bone from the Blueforge Depths —
# it carries a fragment of an ancestral decree. No new NPCs. No dungeon.

NPC_DIALOG += [

	{
		'npc_id': 'speaker_yrsa',
		'dialog_id': 'yrsa_e_decree_shard',
		'dialog': [
			"The ancestors sent this up from the Depths when the Shattered Rune fell.",
			"A shard of carved bone — a decree fragment.",
			"The chant etched into it is a pageant rite. A formal declaration of something.",
			"(quiet) I can read the cadence but not the full sentence.",
			"Bjorn says the rune patterns match a forge-mark used only in Hailward Hold ceremonial work.",
			"It must go back there. The decree wants to be completed."
		]
	},
	{
		'npc_id': 'runeforger_bjorn',
		'dialog_id': 'bjorn_e_decree_context',
		'dialog': [
			"This pattern — I know this mark.",
			"It's from the old Hold ceremonies. Hailward's founders used it to open their greatest works.",
			"A decree shard means something was declared and never answered.",
			"The Hold will know what to do with it. They always do."
		]
	},

]

TASKS += [

	# E-1 — Consult Bjorn about the shard
	{
		'task_id': 'snow_mid_city_type_e_consult_bjorn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'runeforger_bjorn',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'runeforger_bjorn', 'dialog_id': 'bjorn_e_decree_context' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_snow_mid_e_consult_bjorn'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_mid_e_consult_bjorn' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_snow_mid_e_consult_bjorn'   } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'runeforger_bjorn', 'standing_text': [ "The rune patterns match a forge-mark used only in Hailward Hold ceremonial work. It must go back there." ] } },
			{ 'event_type': 'award_task', 'params': { 'task_id': 'snow_mid_city_type_e_collect_shard' }},
		]
	},

	# E-2 — Collect from Yrsa
	{
		'task_id': 'snow_mid_city_type_e_collect_shard',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'speaker_yrsa',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'speaker_yrsa', 'dialog_id': 'yrsa_e_decree_shard' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_snow_mid_e_collect_shard' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_e_collect_shard'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_e_collect_shard' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'speaker_yrsa', 'standing_text': [ "The ancestors sent this up from the Depths when the Shattered Rune fell. A formal declaration of something." ] } },
			{ 'event_type': 'award_item', 'params': { 'item_id': 'snow_mid_city_e_pageant_decree_shard' }},
		]
	},

]



# ── Type D ── Blueforge Warplate (mythic armor) ───────────────────────────────
# Gate: player holds pageant_decree_shard from the Type E chain (same city, Slot 1 → Slot 2).
# Deliver to Brawn → Bjorn reads the shard → defeat Blueforge Spirit → mythic armor.
# No new NPCs — uses runeforger_bjorn, blueforge_spirit, and brawn (Ch.1 party anchor).

NPC_DIALOG += [

	{
		'npc_id': 'runeforger_bjorn',
		'dialog_id': 'bjorn_d_shard_read',
		'dialog': [
			"This decree shard — the rune-frequency carved into it is ancient.",
			"It matches the Blueforge Depths' resonance signature almost exactly.",
			"The Blueforge Spirit has been drawing heat from my forge for years.",
			"It feeds on the same frequency the Pageant Decree was written in.",
			"Present the shard at the Depths entrance — it will surface.",
			"Silence it correctly and the blue-forge metal crystallizes.",
			"Brawn can work blue-forge crystal into armor unlike anything I've ever hammered."
		]
	},

	{
		'npc_id': 'blueforge_spirit',
		'dialog_id': 'blueforge_spirit_d_awakens',
		'dialog': [
			"The decree shard reaches the Depths.",
			"You carry the rune-frequency I have fed on since the first forge burned here.",
			"You want the blue-forge metal.",
			"Survive my flame and it is yours."
		]
	},

]

TASKS += [

	# D-0 — Deliver snow_mid_city_e_pageant_decree_shard to Brawn (standalone deliver; unlocks D chain)
	{
		'task_id': 'snow_mid_city_type_d_deliver_decree_shard',
		'type': 'deliver',
		'item_id': 'snow_mid_city_e_pageant_decree_shard',
		'to_type': 'npc',
		'to_id': 'brawn',
		'task_acquire_events': [
		],
		'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'brawn', 'dialog_id': 'brawn_snow_mid_d_decree_shard' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_d_deliver_decree_shard'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_mid_d_deliver_decree_shard' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_d_deliver_decree_shard' } },
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'snow_mid_city_e_pageant_decree_shard'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_mid_city_type_d_consult_bjorn'
				}
			},
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'brawn',
                    'standing_text': [
                        "The rune-frequency vibrating off that shard is unlike anything I've felt.",
                        "Something in Hailward Hold resonates with it."
                    ]
                }
            }
		]
	},

	# D-1 — Consult Bjorn for the rune-frequency reading
	{
		'task_id': 'snow_mid_city_type_d_consult_bjorn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'runeforger_bjorn',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'runeforger_bjorn',
					'dialog_id': 'bjorn_d_shard_read'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_snow_mid_d_consult_bjorn'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_mid_d_consult_bjorn' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_snow_mid_d_consult_bjorn'   } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'runeforger_bjorn', 'standing_text': [ "The rune-frequency matches the Blueforge Depths' resonance signature almost exactly. The Spirit has been drawing heat from my forge for years." ] } },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'blueforge_spirit',
                    'location': None
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'blueforge_spirit',
                    'standing_text': [
                        "A molten-blue glow bleeds from the Depths entrance.",
                        "Yrsa says her ancestral chants are being drowned out by a deep forge-hum.",
                        "The decree shard has drawn the Spirit to the surface."
                    ]
                }
            },
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'snow_mid_city_blueforge_depths',
                    'location': 'region_open_area'
                }
            },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_mid_city_type_d_meet_blueforge_spirit'
				}
			}
		]
	},

	# D-2 — Meet the Blueforge Spirit (boss intro)
	{
		'task_id': 'snow_mid_city_type_d_meet_blueforge_spirit',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'blueforge_spirit',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'blueforge_spirit',
					'dialog_id': 'blueforge_spirit_d_awakens'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_mid_d_meet_blueforge_spirit' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_mid_d_meet_blueforge_spirit' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_snow_mid_d_meet_blueforge_spirit' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'blueforge_spirit', 'standing_text': [ "The decree shard reaches the Depths. You carry the rune-frequency I have fed on since the first forge burned here. You want the blue-forge metal. Survive my flame and it is yours." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_mid_city_type_d_defeat_blueforge_spirit'
				}
			},
		]
	},

	# D-3 — Defeat the Blueforge Spirit; Brawn forges the mythic armor
	{
		'task_id': 'snow_mid_city_type_d_defeat_blueforge_spirit',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'blueforge_spirit_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'blueforge_spirit_1',
					'combat_type': 'boss_battle'
				}
			}
        ],
		'task_complete_events': [
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'blueforge_spirit'
                }
            },
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_snow_mid_blueforge_warplate'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_snow_mid_d_defeat_blueforge_spirit' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_mid_d_defeat_blueforge_spirit'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_snow_mid_d_defeat_blueforge_spirit' } },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'brawn',
					'standing_text': [
						"Blue-forge crystal — I've worked every metal the world has offered me.",
						"Nothing has ever sung like this.",
						"I've hammered it into the warplate.",
						"It will hold against anything the ice or the rift can throw at you."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'runeforger_bjorn',
					'standing_text': [
						"The blue flame burns clean again.",
						"No more drain. No more resistance.",
						"The runes sing the way they're supposed to."
					]
				}
			},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
	'story_id': 'snow_mid_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}