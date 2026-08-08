ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'vigilant_karrek',
		'name': 'Karrek Windbreak',
		'description': (
			'A hardened watchman who stands guard through the fiercest storms.'
			' Karrek\'s cloak is patched with scraps from past expeditions.'
			' He claims the wind itself warns him of approaching danger.'
		),
		"image": "snow_small:vigilant_karrek1",
		"psychology": {
			"mbti": "ISTJ",
			"dominant": "Si — Has catalogued every wind-shift and storm-pattern the outpost has produced; danger has a specific sound.",
			"auxiliary": "Te — Issues warnings and directives with immediate, unambiguous precision.",
			"tertiary": "Fi — Carries private grief for every person lost to a storm he couldn't warn in time.",
			"inferior": "Ne — Deeply unsettled when the wind behaves in patterns he has never recorded."
		},
		"enneagram": {
			"enneagram_type": "6w5",
			"core_fear": "A storm arriving without warning because he missed the sign.",
			"core_desire": "To be the wind's interpreter — the voice between the storm and the outpost.",
			"defense_mechanism": "Projection — Attributes every unusual wind-shift to an identifiable external cause to maintain the illusion of control.",
			"stress_line": "Moves to Type 3 — Becomes performatively authoritative when the Stormhollow defies his reading.",
			"growth_line": "Moves to Type 9 — Accepts that some storms cannot be predicted and trusts his people to weather them.",
			"instinctual_variant": "so/sp — Outpost safety through personal vigilance; the watch is his identity."
		}
	},
	{
		'npc_id': 'survivor_mira',
		'name': 'Mira Frostline',
		'description': (
			'A resourceful trader who deals in survival gear and hard‑earned wisdom.'
			' Mira\'s smile is rare but genuine, like sunlight on fresh snow.'
			' She has a story for every scar she carries.'
		),
		"image": "snow_small:survivor_mira1",
		"psychology": {
			"mbti": "ISTP",
			"dominant": "Ti — Assesses every survival situation with rapid internal logic; the solution is obvious to her, rarely to others.",
			"auxiliary": "Se — Reads the physical environment — cold, wind, ice-thickness — with automatic, practiced precision.",
			"tertiary": "Ni — Has a trader's gut-sense for when a supply route is about to close or a storm is about to shift.",
			"inferior": "Fe — Her smile is rare because warmth costs energy she can't always afford; she shows it when she means it."
		},
		"enneagram": {
			"enneagram_type": "8w9",
			"core_fear": "Being caught unprepared in a storm with nothing left to trade or survive with.",
			"core_desire": "To be the most prepared, most capable person in any cold situation.",
			"defense_mechanism": "Denial — Refuses to acknowledge how bad things have gotten until the route goes completely silent.",
			"stress_line": "Moves to Type 5 — Goes quiet and methodical when the outpost's situation defies every resource calculation.",
			"growth_line": "Moves to Type 2 — Opens up and shares hard-won wisdom freely when the outpost is at its most vulnerable.",
			"instinctual_variant": "sp/so — Self-reliance in service of community survival; she trades to keep others alive as much as herself."
		}
	},
	{
		'npc_id': 'gale_seer_orlena',
		'name': 'Orlena the Gale‑Seer',
		'description': (
			'A wind-reader who interprets storm-patterns and senses disturbances in the frost.'
			' Orlena\'s breath fogs the air even on calm days.'
			' She says the cold carries the outpost\'s oldest warnings.'
		),
		"image": "snow_small:gale_seer_orlena1",
		"psychology": {
			"mbti": "INFJ",
			"dominant": "Ni — Reads storm-patterns as a language; the frost carries warnings she receives before they can be seen.",
			"auxiliary": "Fe — Delivers warnings with measured care; she understands the difference between alarming people and preparing them.",
			"tertiary": "Ti — Cross-checks each pattern against the outpost's wind history before committing to a reading.",
			"inferior": "Se — Absorbed in the frost's deeper language; physical urgency sometimes catches her mid-reading."
		},
		"enneagram": {
			"enneagram_type": "5w4",
			"core_fear": "A storm-pattern she misread that left the outpost unprepared.",
			"core_desire": "A complete reading of every warning the frost has ever carried.",
			"defense_mechanism": "Isolation — Retreats into the cold's deeper patterns when her warnings are dismissed.",
			"stress_line": "Moves to Type 7 — Becomes restless when the Stormhollow produces patterns she cannot classify.",
			"growth_line": "Moves to Type 8 — Acts as a decisive guide when the outpost cannot afford to wait for a clearer reading.",
			"instinctual_variant": "sp/sx — Solitary frost-reading; bonds intensely with those willing to stand in the cold and listen."
		}
	},
	{
		'npc_id': 'stormhollow_voice',
		'name': 'Stormhollow Voice',
		'description': (
			'A roaring presence formed from hollow wind-channels and trapped battle-echoes.'
			' It guards the warden plate with the fury of every storm that ever buried the outpost.'
		),
		"image": "snow_small:stormhollow_voice1",
		"psychology": {
			"mbti": "ISTJ",
			"dominant": "Si — Guards with the encoded memory of every storm that ever buried the outpost; the fury is historical, not personal.",
			"auxiliary": "Te — Enforces its territory with absolute, uncompromising protocol.",
			"tertiary": "Fi — A faint echo of the soldiers who died in the storms it carries; the warden plate is their memorial.",
			"inferior": "Ne — Cannot conceive of a world where the outpost no longer needs its fury."
		},
		"enneagram": {
			"enneagram_type": "8w9",
			"core_fear": "The outpost falling because its guardian fury was not enough.",
			"core_desire": "To keep every storm that ever threatened the outpost permanently contained within itself.",
			"defense_mechanism": "Denial — Cannot acknowledge that the storms are over and the fury has become the threat.",
			"stress_line": "Moves to Type 5 — Becomes cold and methodical when its roar doesn't drive intruders away.",
			"growth_line": "Moves to Type 2 — Releases the warden plate when it finally trusts those who will honour it.",
			"instinctual_variant": "sp/so — Collective battle-memory made permanent; it stands because soldiers once stood together."
		}
	},
]


NPC_DIALOG = [

	# ── Intro dialogs ───────────────────────────────────────────────
	{
		'npc_id': 'vigilant_karrek',
		'dialog_id': 'karrek_intro',
		'dialog': [
			"The wind shifts in patterns I've never recorded.",
			"Something moves through the storm that shouldn't be there.",
			"Bleakwatch has survived worse — but not without knowing what's coming."
		]
	},
	{
		'npc_id': 'survivor_mira',
		'dialog_id': 'mira_intro',
		'dialog': [
			"Supply routes have gone quiet.",
			"The cold comes from the wrong direction.",
			"If the outpost loses its watch, the whole frontier falls dark."
		]
	},
	{
		'npc_id': 'gale_seer_orlena',
		'dialog_id': 'orlena_intro',
		'dialog': [
			"The storm-patterns fracture near the hollow.",
			"A Stormhollow Voice stirs — a spirit of trapped battle-wind.",
			"If it breaks free, no signal will carry across the snow line."
		]
	},
	{
		'npc_id': 'vigilant_karrek',
		'dialog_id': 'karrek_closing',
		'dialog': [
			"The wind reads clean again.",
			"Whatever drove those patterns — it's gone.",
			"Bleakwatch stands. That's all that matters."
		]
	},

]

NPC_DIALOG += [

	# ── Type C dialogs — Commander Drax ────────────────────────────
	{
		'npc_id': 'commander_drax',
		'dialog_id': 'drax_c_first_meet',
		'dialog': [
			"You're not garrison. You move like field-trained.",
			"I've been watching your party since you crossed the frost-line.",
			"Bleakwatch has a wall. What it doesn't have is people worth standing behind it.",
			"Prove you're worth my time and I'll consider the offer."
		]
	},
	{
		'npc_id': 'vigilant_karrek',
		'dialog_id': 'karrek_c_vouch',
		'dialog': [
			"Drax doesn't move for anyone. That's not stubbornness — it's policy.",
			"He's lost units before to commanders who moved too fast.",
			"Tell him I watched you on the storm-approach and you didn't flinch.",
			"Coming from me, that's the only credential that opens his door."
		]
	},
	{
		'npc_id': 'commander_drax',
		'dialog_id': 'drax_c_joins',
		'dialog': [
			"Karrek doesn't say that about anyone.",
			"He's watched soldiers break on that approach for twenty years.",
			"Fine. I'll move.",
			"But understand — I lead from the front.",
			"You position me at the rear and I walk."
		]
	},

]

NPC_DIALOG += [

	# ── Type D dialogs — Bleakwatch Warden Plate ───────────────────
	{
		'npc_id': 'vigilant_karrek',
		'dialog_id': 'karrek_d_registry',
		'dialog': [
			"A contraband registry from Tess\'s network — these log black-market warden equipment.",
			"The outpost\'s original warden plate disappeared during the second siege.",
			"This entry traces the last known location to the Stormhollow.",
			"Brawn will know what to make of it — that plate\'s design is old-order military."
		]
	},
	{
		'npc_id': 'gale_seer_orlena',
		'dialog_id': 'orlena_d_storm_read',
		'dialog': [
			"Brawn\'s right — the storm-patterns around the hollow carry the warden frequency.",
			"The plate has been down there since the siege.",
			"The Stormhollow Voice absorbed the battle-wind that buried it.",
			"Force it out and the plate surfaces with the storm it was trapped in.",
			"Be ready — it won\'t surrender the warden\'s armour quietly."
		]
	},
	{
		'npc_id': 'stormhollow_voice',
		'dialog_id': 'stormhollow_voice_awakens',
		'dialog': [
			"The warden\'s plate is mine.",
			"Every storm that buried this outpost feeds me.",
			"I am the battle-wind that never stopped.",
			"You will not strip the hollow of its armour."
		]
	},
	{
		'npc_id': 'vigilant_karrek',
		'dialog_id': 'karrek_d_reward',
		'dialog': [
			"The storm broke clean when you came back.",
			"That plate — it hasn\'t breathed open air since the second siege.",
			"Brawn says it\'s the finest warden-grade steel he\'s handled.",
			"The outpost\'s warden returns to the wall. Fitting."
		]
	},

]

# --- Character dialogs: main story chain ---
NPC_DIALOG += [

	# Meet Karrek
	{ 'npc_id': 'tech',    'dialog_id': 'kade_snow_small_meet_karrek',    'dialog': [ "Wind patterns he's never recorded. Something moves through the storm that shouldn't be there." ] },
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_small_meet_karrek', 'dialog': [ "Bleakwatch has survived worse — but not without knowing what's coming." ] },
	{ 'npc_id': 'skill',   'dialog_id': 'poise_snow_small_meet_karrek',   'dialog': [ "Mira will know what the quiet supply routes mean." ] },

	# Meet Survivor Mira
	{ 'npc_id': 'faith', 'dialog_id': 'kaera_snow_small_meet_survivor_mira', 'dialog': [ "Supply routes gone quiet. The cold coming from the wrong direction." ] },
	{ 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_meet_survivor_mira',  'dialog': [ "If the outpost loses its watch, the whole frontier falls dark." ] },
	{ 'npc_id': 'skill', 'dialog_id': 'poise_snow_small_meet_survivor_mira', 'dialog': [ "Find Orlena. The storm-patterns near the hollow are fracturing." ] },

	# Find Orlena
	{ 'npc_id': 'tech',    'dialog_id': 'kade_snow_small_find_orlena',    'dialog': [ "A Stormhollow Voice — spirit of trapped battle-wind. If it breaks free, no signal will carry across the snow line." ] },
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_small_find_orlena', 'dialog': [ "The storm-patterns are already fracturing toward it. We still it before the frontier goes dark." ] },
	{ 'npc_id': 'technique',   'dialog_id': 'chock_snow_small_find_orlena',   'dialog': [ "The wind reads clean again. Bleakwatch stands. That's all that matters." ] },

]

# --- Character dialogs: Type C (Commander Drax chain) ---
NPC_DIALOG += [

	# Type C – Find Drax
	{ 'npc_id': 'technique', 'dialog_id': 'chock_snow_small_c_find_drax', 'dialog': [ "He's been watching since we crossed the frost-line. Bleakwatch has a wall. What it doesn't have is people worth standing behind it." ] },
	{ 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_c_find_drax',  'dialog': [ "Prove we're worth his time and he'll consider the offer. Fair terms for a commander who's lost units before." ] },
	{ 'npc_id': 'bragg', 'dialog_id': 'bragg_snow_small_c_find_drax', 'dialog': [ "Karrek's the one who opens his door." ] },

	# Type C – Consult Karrek
	{ 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_c_consult_karrek',  'dialog': [ "Drax doesn't move for anyone. That's policy, not stubbornness. He's lost units to commanders who moved too fast." ] },
	{ 'npc_id': 'technique', 'dialog_id': 'chock_snow_small_c_consult_karrek', 'dialog': [ "Tell him we didn't flinch on the storm-approach. Coming from Karrek, that's the only credential that works." ] },
	{ 'npc_id': 'bragg', 'dialog_id': 'bragg_snow_small_c_consult_karrek', 'dialog': [ "He's already half-decided. This just confirms it." ] },

	# Type C – Earn Drax
	{ 'npc_id': 'technique', 'dialog_id': 'chock_snow_small_c_earn_drax', 'dialog': [ "Karrek doesn't say that about anyone. He's watched soldiers break on that approach for twenty years." ] },
	{ 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_c_earn_drax',  'dialog': [ "He leads from the front. Position him at the rear and he walks. Understood." ] },
	{ 'npc_id': 'bragg', 'dialog_id': 'bragg_snow_small_c_earn_drax', 'dialog': [ "Fine. He's in." ] },

]

# --- Character dialogs: Type D (Bleakwatch Warden Plate chain) ---
NPC_DIALOG += [

	# Type D – Deliver Contraband Registry
	{ 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_d_deliver_contraband_registry',  'dialog': [ "A contraband registry from Tess's network — black-market warden equipment. The outpost's original plate disappeared during the second siege." ] },
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_snow_small_d_deliver_contraband_registry', 'dialog': [ "This entry traces the last known location to the Stormhollow. Brawn will know the design." ] },
	{ 'npc_id': 'skill', 'dialog_id': 'poise_snow_small_d_deliver_contraband_registry', 'dialog': [ "Orlena next. The gale is already reading something armoured down there." ] },

	# Type D – Consult Orlena
	{ 'npc_id': 'tech',    'dialog_id': 'kade_snow_small_d_consult_orlena',    'dialog': [ "The storm-patterns around the hollow carry the warden frequency. The plate has been down there since the siege." ] },
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_small_d_consult_orlena', 'dialog': [ "The Stormhollow Voice absorbed the battle-wind that buried it. Force it out and the plate surfaces with the storm it was trapped in." ] },
	{ 'npc_id': 'skill',   'dialog_id': 'poise_snow_small_d_consult_orlena',   'dialog': [ "It won't surrender the armour quietly." ] },

	# Type D – Meet Stormhollow Voice
	{ 'npc_id': 'skill', 'dialog_id': 'poise_snow_small_d_meet_stormhollow_voice', 'dialog': [ "It already decided the warden's plate is its." ] },
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_snow_small_d_meet_stormhollow_voice', 'dialog': [ "Every storm that buried this outpost feeds it. The battle-wind that never stopped." ] },
	{ 'npc_id': 'lyren', 'dialog_id': 'lyren_snow_small_d_meet_stormhollow_voice', 'dialog': [ "Some voices only know how to keep the armour of the ones who fell. We take it back." ] },

	# Type D – Defeat Stormhollow Voice
	{ 'npc_id': 'technique', 'dialog_id': 'chock_snow_small_d_defeat_stormhollow_voice', 'dialog': [ "The storm broke clean when we came back." ] },
	{ 'npc_id': 'faith', 'dialog_id': 'kaera_snow_small_d_defeat_stormhollow_voice', 'dialog': [ "That plate hasn't breathed open air since the second siege. The outpost's warden returns to the wall." ] },
	{ 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_d_defeat_stormhollow_voice',  'dialog': [ "Brawn says it's the finest warden-grade steel he's handled. Fitting." ] },

]

# --- Character dialogs: Type A Ch.6 ---
NPC_DIALOG += [

	# Type A – Ch6 Meet Karrek
	{ 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_a_ch6_meet_karrek',  'dialog': [ "Storm-pattern fractures near the hollow for three days. Something moved through that breach site that wasn't weather." ] },
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_snow_small_a_ch6_meet_karrek', 'dialog': [ "The hollow is listening. Whatever crawled out — it knows we're watching too." ] },
	{ 'npc_id': 'skill', 'dialog_id': 'poise_snow_small_a_ch6_meet_karrek', 'dialog': [ "Take the reading to Seth. He'll know what it means." ] },

]


TASKS = [

	# ── Intro scaffold ───────────────────────────────────────────────
	{
		'task_id': 'snow_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'vigilant_karrek',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'vigilant_karrek',
					'standing_text': [
						"The wind warns before anything else does — learn to listen."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'survivor_mira',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'survivor_mira',
					'standing_text': [
						"Survival gear, hard-won wisdom — I trade in both."
					]
				}
			},
		],
		'task_complete_events': [
            { 'event_type': 'award_task', 'params': { 'task_id': 'snow_small_city_type_a_ch6_meet_karrek' }},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_meet_karrek'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_c_find_drax'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_d_deliver_contraband_registry'
				}
			}
		]
	},
	{
		'task_id': 'snow_small_city_meet_karrek',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'vigilant_karrek',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vigilant_karrek',
					'dialog_id': 'karrek_intro'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_snow_small_meet_karrek'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_small_meet_karrek' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_snow_small_meet_karrek'   } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'vigilant_karrek', 'standing_text': [ "The wind shifts in patterns I've never recorded.", "Something moves through the storm that shouldn't be there.", "Bleakwatch has survived worse — but not without knowing what's coming." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_meet_survivor_mira'
				}
			}
		]
	},
	{
		'task_id': 'snow_small_city_meet_survivor_mira',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'survivor_mira',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'survivor_mira',
					'dialog_id': 'mira_intro'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_snow_small_meet_survivor_mira' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_meet_survivor_mira'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_small_meet_survivor_mira' } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_find_orlena'
				}
			}
		]
	},
	{
		'task_id': 'snow_small_city_find_orlena',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'gale_seer_orlena',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'gale_seer_orlena',
					'location': 'region_bar'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'gale_seer_orlena',
					'dialog_id': 'orlena_intro'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_snow_small_find_orlena'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_small_find_orlena' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique',   'dialog_id': 'chock_snow_small_find_orlena'   } },
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vigilant_karrek',
					'dialog_id': 'karrek_closing'
				}
			},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'gale_seer_orlena', 'standing_text': [ "The storm-patterns fracture near the hollow. A Stormhollow Voice stirs — a spirit of trapped battle-wind. If it breaks free, no signal will carry across the snow line." ] } }
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE C — Commander Drax (extended character, slot 2)
	# Gated by is_chapter_gte: 6
	# Awarded by: snow_small_city_initialize (conditional)
	# =========================================================

	{
		'task_id': 'snow_small_city_type_c_find_drax',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'commander_drax',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'commander_drax',
					'location': 'region_city_other1'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'commander_drax',
					'dialog_id': 'drax_c_first_meet'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_snow_small_c_find_drax' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_c_find_drax'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_snow_small_c_find_drax' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'commander_drax', 'standing_text': [ "You're not garrison. You move like field-trained. I've been watching your party since you crossed the frost-line. Bleakwatch has a wall. What it doesn't have is people worth standing behind it. Prove you're worth my time and I'll consider the offer." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_c_consult_karrek'
				}
			},
		]
	},
	{
		'task_id': 'snow_small_city_type_c_consult_karrek',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'vigilant_karrek',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vigilant_karrek',
					'dialog_id': 'karrek_c_vouch'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_c_consult_karrek'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_snow_small_c_consult_karrek' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_snow_small_c_consult_karrek' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'vigilant_karrek', 'standing_text': [ "Drax doesn't move for anyone. That's not stubbornness — it's policy. He's lost units before to commanders who moved too fast. Tell him I watched you on the storm-approach and you didn't flinch. Coming from me, that's the only credential that opens his door." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_c_earn_drax'
				}
			},
		]
	},
	{
		'task_id': 'snow_small_city_type_c_earn_drax',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'commander_drax',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'commander_drax',
					'dialog_id': 'drax_c_joins'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_snow_small_c_earn_drax' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_c_earn_drax'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_snow_small_c_earn_drax' } },
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'commander_drax'
				}
			},
			{
				'event_type': 'character_join',
				'params': {
					'character_id': 'commander_drax'
				}
			},
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE D — Mythic Equipment Quest (slot 3)
	# Gate: desert_small_city_f_contraband_registry (Tess F chain, Ch.9)
	# Deliver to: Brawn (armor)
	# Mythic reward: mythic_snow_small_bleakwatch_warden_plate
	# =========================================================

	{
		'task_id': 'snow_small_city_type_d_deliver_contraband_registry',
		'type': 'deliver',
		'item_id': 'desert_small_city_f_contraband_registry',
		'to_type': 'npc',
		'to_id': 'brawn',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_d_deliver_contraband_registry'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_small_d_deliver_contraband_registry' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_small_d_deliver_contraband_registry' } },
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'desert_small_city_f_contraband_registry'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vigilant_karrek',
					'dialog_id': 'karrek_d_registry'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'brawn',
					'standing_text': [
						"That registry traces the last known location of the outpost's original warden plate to the Stormhollow.",
						"Orlena will know what the gale is reading."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_d_consult_orlena'
				}
			}
		]
	},
	{
		'task_id': 'snow_small_city_type_d_consult_orlena',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'gale_seer_orlena',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'gale_seer_orlena',
					'dialog_id': 'orlena_d_storm_read'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_snow_small_d_consult_orlena'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_small_d_consult_orlena' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_snow_small_d_consult_orlena'   } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'gale_seer_orlena', 'standing_text': [ "The storm-patterns around the hollow carry the warden frequency. The plate has been down there since the siege. The Stormhollow Voice absorbed the battle-wind that buried it. Force it out and the plate surfaces with the storm it was trapped in. Be ready — it won't surrender the warden's armour quietly." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_d_meet_stormhollow_voice'
				}
			}
		]
	},
	{
		'task_id': 'snow_small_city_type_d_meet_stormhollow_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'stormhollow_voice',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'stormhollow_voice',
					'location': None
				}
			},
			{
				'event_type': 'create_dungeon',
				'params': {
					'dungeon_id': 'stormhollow_voice_1',
					'location': 'region_open_area'
				}
			}

		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'stormhollow_voice',
					'dialog_id': 'stormhollow_voice_awakens'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_small_d_meet_stormhollow_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_small_d_meet_stormhollow_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_snow_small_d_meet_stormhollow_voice' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'stormhollow_voice', 'standing_text': [ "The warden's plate is mine. Every storm that buried this outpost feeds me. I am the battle-wind that never stopped. You will not strip the hollow of its armour." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_small_city_type_d_defeat_stormhollow_voice'
				}
			}
		]
	},
	{
		'task_id': 'snow_small_city_type_d_defeat_stormhollow_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'stormhollow_voice_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'stormhollow_voice_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'stormhollow_voice'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'vigilant_karrek',
					'dialog_id': 'karrek_d_reward'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_snow_small_bleakwatch_warden_plate'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_snow_small_d_defeat_stormhollow_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_snow_small_d_defeat_stormhollow_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_d_defeat_stormhollow_voice'  } },
		]
	},

]
# ── Type A ── Ch.6 Chapter Tie-In (Karrek storm report) ───────────────────────
# Awarded by Ch.6 Seth after his resistance reveal. Player must speak to Karrek
# at the storm post and collect his breach-approach reading before Seth will
# hand over his contact (Rhett). No new NPCs — Karrek is in the city seed.

NPC_DIALOG += [

    {
        'npc_id': 'vigilant_karrek',
        'dialog_id': 'karrek_a_ch6_storm_report',
        'dialog': [
            "Seth sent you? Good timing.",
            "I've been logging storm-pattern fractures near the hollow for three days.",
            "The wind doesn't lie — something moved through that breach site that wasn't weather.",
            "Take this reading. Seth will know what it means.",
            "(pressing a sealed wind-chart into your hands)",
            "Tell him: the hollow is listening. Whatever crawled out — it knows we're watching too."
        ]
    },

]

TASKS += [

    # A-1 — Meet Karrek for the storm report (completes the gate)
    {
        'task_id': 'snow_small_city_type_a_ch6_meet_karrek',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vigilant_karrek',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vigilant_karrek', 'dialog_id': 'karrek_a_ch6_storm_report' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_small_a_ch6_meet_karrek'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_small_a_ch6_meet_karrek' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_small_a_ch6_meet_karrek' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'vigilant_karrek', 'standing_text': [ "Storm-pattern fractures near the hollow for three days. Something moved through that breach site that wasn't weather. The hollow is listening. Whatever crawled out — it knows we're watching too." ] } }
        ]
    },

]
PRIMARY_STORY_SETTINGS = {
	'story_id': 'snow_small_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}