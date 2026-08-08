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
		),
		"image": "snow_large:concordant_ivar1",
		"psychology": {
			"mbti": "INFJ",
			"dominant": "Ni — Perceives the shape of a conflict before anyone has named it; harmony is a pattern he reads, not negotiates.",
			"auxiliary": "Fe — Creates emotional equilibrium in the room through presence and precisely chosen words.",
			"tertiary": "Ti — Applies the frost's own logic — slow, incremental, structural — to every dispute.",
			"inferior": "Se — Physically still; discomfort with the sudden, the loud, the unplanned."
		},
		"enneagram": {
			"enneagram_type": "9w1",
			"core_fear": "Harmony shattered beyond repair — a fracture in the ice that cannot be re-frozen.",
			"core_desire": "A city in which every dispute resolves cleanly and the frost can settle.",
			"defense_mechanism": "Narcotization — Retreats into mediation's quiet rhythm to avoid acknowledging how deep the fractures run.",
			"stress_line": "Moves to Type 6 — Becomes cautious and over-consulting when the Fractured Chime destabilizes his process.",
			"growth_line": "Moves to Type 3 — Steps into decisive leadership when the city's harmony requires more than patience.",
			"instinctual_variant": "so/sp — Community harmony as the primary expression of personal purpose."
		}
	},
	{
		'npc_id': 'artificer_lyndra',
		'name': 'Lyndra Frostlight',
		'description': (
			'A brilliant inventor who blends cold magic with delicate machinery.'
			'  Lyndra\'s creations glow with pale blue radiance.'
			'  She works tirelessly, claiming inspiration strikes like sudden snowfall.'
		),
		"image": "snow_large:artificer_lyndra1",
		"psychology": {
			"mbti": "INTP",
			"dominant": "Ti — Designs frost-engine systems with elegant internal logic; every component is where it must be.",
			"auxiliary": "Ne — Inspiration arrives unpredictably; sudden connections between cold magic and mechanism are her creative core.",
			"tertiary": "Si — Draws on a precise memory of every machine she has built and every failure she has learned from.",
			"inferior": "Fe — Struggles to explain her designs to non-technical audiences; the logic is self-evident to her."
		},
		"enneagram": {
			"enneagram_type": "5w4",
			"core_fear": "A design failure that causes the frost-engines to collapse entirely.",
			"core_desire": "To build a machine that perfectly harmonises cold magic and mechanism.",
			"defense_mechanism": "Isolation — Retreats into the workshop when the engines behave unpredictably, treating it as a systems problem, not a crisis.",
			"stress_line": "Moves to Type 7 — Becomes scattered and restless when the cold magic splinters beyond her current understanding.",
			"growth_line": "Moves to Type 8 — Steps out of the workshop and applies her expertise decisively when the city needs it.",
			"instinctual_variant": "sp/sx — Workshop as sanctuary; forms deep bonds with those who understand what she is building."
		}
	},
	{
		'npc_id': 'glacier_seer_thryna',
		'name': 'Thryna the Glacier‑Seer',
		'description': (
			'A mystic who reads ice harmonics and senses fractures before they form.'
		),
		"image": "snow_large:glacier_seer_thryna1",
		"psychology": {
			"mbti": "INFJ",
			"dominant": "Ni — Perceives ice-fracture patterns as a language; what the glacier is about to do is legible to her before it happens.",
			"auxiliary": "Fe — Communicates her readings with careful, measured compassion; she never wants her warnings to cause panic.",
			"tertiary": "Ti — Cross-checks harmonic readings against the glacier's internal structural logic.",
			"inferior": "Se — So absorbed in the harmonics that the physical cold sometimes takes her by surprise."
		},
		"enneagram": {
			"enneagram_type": "5w4",
			"core_fear": "A fracture she sensed but didn't warn about in time.",
			"core_desire": "To map every ice harmonic until no fracture can form without her knowing first.",
			"defense_mechanism": "Isolation — Retreats into the glacier's harmonics when her readings are dismissed.",
			"stress_line": "Moves to Type 7 — Becomes restless when the Fractured Chime defies every harmonic she knows.",
			"growth_line": "Moves to Type 8 — Acts as a decisive, protective guide when the glacier's crisis demands presence.",
			"instinctual_variant": "sp/sx — Solitary practice; bonds intensely with those willing to listen to the ice with her."
		}
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

# --- Character dialogs: main story chain ---
NPC_DIALOG += [

	# Meet Ivar
	{ 'npc_id': 'tech',    'dialog_id': 'kade_snow_large_meet_ivar',    'dialog': [ "Frost patterns shifting without cause. Harmony is fracturing beneath the ice." ] },
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_large_meet_ivar', 'dialog': [ "Something is awakening in the deep cold. The city's engines will feel it next." ] },
	{ 'npc_id': 'skill',   'dialog_id': 'poise_snow_large_meet_ivar',   'dialog': [ "Lyndra's machines are already humming out of tune." ] },

	# Meet Lyndra
	{ 'npc_id': 'tech',  'dialog_id': 'kade_snow_large_meet_lyndra',  'dialog': [ "Cold magic splintering where it once flowed clean. The frost-engines won't hold if this continues." ] },
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_snow_large_meet_lyndra', 'dialog': [ "Her designs are born of frost. When the frost turns against itself, the whole system fails." ] },
	{ 'npc_id': 'skill', 'dialog_id': 'poise_snow_large_meet_lyndra', 'dialog': [ "Find Thryna. The ice harmonics will tell us what's rising." ] },

	# Find Thryna
	{ 'npc_id': 'tech',    'dialog_id': 'kade_snow_large_find_thryna',    'dialog': [ "A Fractured Chime — spirit of broken harmony. If it awakens fully, the frost will turn against itself." ] },
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_large_find_thryna', 'dialog': [ "The ice harmonics are already trembling toward it. We still it before the discord becomes permanent." ] },
	{ 'npc_id': 'faith',   'dialog_id': 'kaera_snow_large_find_thryna',   'dialog': [ "You've stilled a discord older than the glacier itself. The Snowlands will remember." ] },

]

# --- Character dialogs: Type C (Lyric chain) ---
NPC_DIALOG += [

	# Type C – Find Lyric
	{ 'npc_id': 'tech',    'dialog_id': 'kade_snow_large_c_find_lyric',    'dialog': [ "Seventeen variables collapsed to three. They're mapping the interference patterns because everything here is breaking in a theoretically optimal way." ] },
	{ 'npc_id': 'magic',   'dialog_id': 'moxie_snow_large_c_find_lyric',   'dialog': [ "The maths are fascinating to them. That's either reassuring or extremely concerning." ] },
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_large_c_find_lyric', 'dialog': [ "They don't trust observation alone. We'll need verified data before they'll commit." ] },

	# Type C – Consult Lyndra
	{ 'npc_id': 'tech',  'dialog_id': 'kade_snow_large_c_consult_lyndra',  'dialog': [ "The theorist from the eastern cold-labs. If they say the pattern is solvable, it probably is." ] },
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_snow_large_c_consult_lyndra', 'dialog': [ "But they need proof. Observation alone isn't enough for them." ] },
	{ 'npc_id': 'skill', 'dialog_id': 'poise_snow_large_c_consult_lyndra', 'dialog': [ "Bring the data. Independently verified." ] },

	# Type C – Earn Lyric
	{ 'npc_id': 'tech',  'dialog_id': 'kade_snow_large_c_earn_lyric',  'dialog': [ "Thorough. Methodical. Rare. That's what got them to commit." ] },
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_snow_large_c_earn_lyric', 'dialog': [ "Someone has to keep our conclusions honest. They're volunteering." ] },
	{ 'npc_id': 'technique', 'dialog_id': 'chock_snow_large_c_earn_lyric', 'dialog': [ "Fine. They're in." ] },

]

# --- Character dialogs: Type D (Frostgate Sovereign chain) ---
NPC_DIALOG += [

	# Type D – Deliver Armor Key
	{ 'npc_id': 'tech',  'dialog_id': 'kade_snow_large_d_deliver_armor_key',  'dialog': [ "An Armory Seal from the Frostgate deep vaults. The warplate locked inside hasn't been touched since the last glacier war." ] },
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_snow_large_d_deliver_armor_key', 'dialog': [ "Lyndra knows the cold-forging rites better than anyone." ] },
	{ 'npc_id': 'skill', 'dialog_id': 'poise_snow_large_d_deliver_armor_key', 'dialog': [ "Speak to her." ] },

	# Type D – Consult Lyndra
	{ 'npc_id': 'tech',    'dialog_id': 'kade_snow_large_d_consult_lyndra',    'dialog': [ "The Seal is authentic. The Frostgate Sovereign — forged from harmonized glacier-iron." ] },
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_large_d_consult_lyndra', 'dialog': [ "Deliver the Seal to Thryna. She holds the unlocking rite." ] },
	{ 'npc_id': 'skill',   'dialog_id': 'poise_snow_large_d_consult_lyndra',   'dialog': [ "Then we wake the vault." ] },

	# Type D – Meet Vault Guardian
	{ 'npc_id': 'skill', 'dialog_id': 'poise_snow_large_d_meet_vault_guardian', 'dialog': [ "The Seal awakens the guardian. It will test whether we are worthy of the Sovereign." ] },
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_snow_large_d_meet_vault_guardian', 'dialog': [ "Survive, and the warplate is ours. Clean terms." ] },
	{ 'npc_id': 'technique', 'dialog_id': 'chock_snow_large_d_meet_vault_guardian', 'dialog': [ "We survive." ] },

	# Type D – Defeat Vault Guardian
	{ 'npc_id': 'technique', 'dialog_id': 'chock_snow_large_d_defeat_vault_guardian', 'dialog': [ "The guardian fell. The vault yields." ] },
	{ 'npc_id': 'faith', 'dialog_id': 'kaera_snow_large_d_defeat_vault_guardian', 'dialog': [ "The Frostgate Sovereign is yours — wear it as a promise. That armour has never known defeat." ] },
	{ 'npc_id': 'tech',  'dialog_id': 'kade_snow_large_d_defeat_vault_guardian',  'dialog': [ "See that it still doesn't." ] },

]

# --- Character dialogs: Type B (Aeriola chain) ---
NPC_DIALOG += [

	# B – Meet Aeriola
	{ 'npc_id': 'technique',  'dialog_id': 'chock_snow_large_b_meet_aeriola',  'dialog': [ "She will have reformed around the stored moments. She believes time is hers to stop." ] },
	{ 'npc_id': 'kor_in', 'dialog_id': 'kor_in_snow_large_b_meet_aeriola', 'dialog': [ "She is wrong. Time is not stopped by will. It is stopped by grief. And grief does not last forever." ] },
	{ 'npc_id': 'tech',   'dialog_id': 'kade_snow_large_b_meet_aeriola',   'dialog': [ "Every frozen moment she ever made — she carries them all now. We don't add ours to the collection." ] },

	# B – Defeat Aeriola
	{ 'npc_id': 'technique',  'dialog_id': 'chock_snow_large_b_defeat_aeriola',  'dialog': [ "Stay down. The frost moves again." ] },
	{ 'npc_id': 'kor_in', 'dialog_id': 'kor_in_snow_large_b_defeat_aeriola', 'dialog': [ "She thought stopping time was mercy. What matters is that the frost is moving again." ] },
	{ 'npc_id': 'faith',  'dialog_id': 'kaera_snow_large_b_defeat_aeriola',  'dialog': [ "Things that move can change. Things that stop just wait to be found." ] },

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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'concordant_ivar',
					'dialog_id': 'ivar_intro'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_snow_large_meet_ivar'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_large_meet_ivar' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_snow_large_meet_ivar'   } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'concordant_ivar', 'standing_text': [ "The frost settles. Harmony returns." ] } },
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
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_large_meet_lyndra'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_large_meet_lyndra' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_large_meet_lyndra' } },
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
					'location': 'region_city_other1'
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
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_snow_large_find_thryna'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_large_find_thryna' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',   'dialog_id': 'kaera_snow_large_find_thryna'   } },
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'concordant_ivar',
					'dialog_id': 'ivar_closing'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'glacier_seer_thryna',
					'standing_text': [
						"The ice harmonics tremble.",
						"A Fractured Chime rises — a spirit of broken harmony."
					]
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
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'lyric',
					'dialog_id': 'lyric_intro'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_snow_large_c_find_lyric'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',   'dialog_id': 'moxie_snow_large_c_find_lyric'   } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_large_c_find_lyric' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lyric', 'standing_text': [ "I've been mapping the frost-harmonic interference patterns." ] } },
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
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_large_c_consult_lyndra'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_large_c_consult_lyndra' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_large_c_consult_lyndra' } },
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'lyric',
					'dialog_id': 'lyric_join'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_large_c_earn_lyric'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_large_c_earn_lyric' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_snow_large_c_earn_lyric' } },
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
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_large_d_deliver_armor_key'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_large_d_deliver_armor_key' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_large_d_deliver_armor_key' } },
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'artificer_lyndra',
					'dialog_id': 'lyndra_armor_ritual'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_snow_large_d_consult_lyndra'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_large_d_consult_lyndra' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_snow_large_d_consult_lyndra'   } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'artificer_lyndra', 'standing_text': [ "The Seal awakens the vault guardian." ] } },
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
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'glacier_seer_thryna',
					'dialog_id': 'thryna_armor_boss'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_snow_large_d_meet_vault_guardian' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_snow_large_d_meet_vault_guardian' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_snow_large_d_meet_vault_guardian' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'glacier_seer_thryna', 'standing_text': [ "The Seal awakens the vault guardian." ] } },
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
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_snow_large_d_defeat_vault_guardian' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_snow_large_d_defeat_vault_guardian' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_snow_large_d_defeat_vault_guardian'  } },
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
		'npc_id': 'aeriola',
		'dialog_id': 'aeriola_b_defeated',
		'dialog': [
			"(ice cracking, voice already half-thaw)",
			"You break the moments…",
			"The stillness does not break with me.",
			"Seven places where the world already tried to empty itself.",
			"Seven freezes the void found useful.",
			"You thaw them… and still the quiet deepens.",
			"(almost gentle)",
			"When the last moment moves again… you will understand.",
			"I was never trying to stop the world.",
			"I was trying to keep it from having to feel what comes after the stopping ends."
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

# --- Character dialogs: Type B meet Aeriola (all 16) ---
NPC_DIALOG += [

	{ 'npc_id': 'technique', 'dialog_id': 'chock_snow_large_b_meet_aeriola', 'dialog': [
		"She returned. Reformed around everything the cold kept for her.",
		"Good. We came here to finish this."
	]},
	{ 'npc_id': 'kor_in', 'dialog_id': 'kor_in_snow_large_b_meet_aeriola', 'dialog': [
		"She said 'what your violence took.'",
		"(very still)",
		"She remembers it as violence. She remembers us arriving while she held the city frozen.",
		"She was the one holding it.",
		"(quiet, measured) She is wrong about what happened. She has always been wrong about what happened.",
		"That does not change what we have to do now."
	]},
	{ 'npc_id': 'tech', 'dialog_id': 'kade_snow_large_b_meet_aeriola', 'dialog': [
		"Every frozen moment she ever made. She's carrying all of them.",
		"That's not a weapon. That's a burden she chose to keep.",
		"She thinks it makes her unstoppable. It makes her overloaded."
	]},
	{ 'npc_id': 'faith', 'dialog_id': 'kaera_snow_large_b_meet_aeriola', 'dialog': [
		"She asked the void to give back what she lost.",
		"It answered.",
		"(quietly) That is never the mercy it looks like. The void returns things unchanged — it doesn't heal them.",
		"She has everything she lost. She is still what she was when she lost it."
	]},
	{ 'npc_id': 'skill', 'dialog_id': 'poise_snow_large_b_meet_aeriola', 'dialog': [
		"She's been waiting here since she fell. Reforming. Collecting.",
		"Every frozen moment another layer of defense.",
		"She has had months to prepare this chamber against us specifically.",
		"We hit harder than she's prepared for."
	]},
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_snow_large_b_meet_aeriola', 'dialog': [
		"'Your violence.' That's the framing she settled on.",
		"We interrupted a city-wide time stop that was going to kill everyone in it.",
		"I understand grief rewrites the past. I just prefer my version."
	]},
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_large_b_meet_aeriola', 'dialog': [
		"Fascinating. She's using accumulated temporal mass as structural reinforcement.",
		"Each frozen moment adds density — she's armored herself in stopped time.",
		"(clinical) The theoretical upper limit on that construct is — aggressive.",
		"Target the moments at the edges first. Those will be the least stable."
	]},
	{ 'npc_id': 'lyren', 'dialog_id': 'lyren_snow_large_b_meet_aeriola', 'dialog': [
		"She said she would add our moments to her collection.",
		"(quietly)",
		"She keeps what she stops. She thinks that's how you hold onto things.",
		"It isn't. But she's had a long time with no one to tell her differently."
	]},
	{ 'npc_id': 'ripple', 'dialog_id': 'ripple_snow_large_b_meet_aeriola', 'dialog': [
		"She's been accumulating since we faced her. Every frozen moment the void gave back —",
		"(watching the ice)",
		"The void doesn't give gifts. It returns pressure. She's carrying all of it.",
		"(steadying) She has been waiting here for something to break under the weight.",
		"We don't give her that."
	]},
	{ 'npc_id': 'bragg', 'dialog_id': 'bragg_snow_large_b_meet_aeriola', 'dialog': [
		"She's carrying every fight she ever stopped mid-swing.",
		"All of it about to unfreeze at once.",
		"(cracking knuckles) Good. I was starting to wonder if this would be interesting."
	]},
	{ 'npc_id': 'sable', 'dialog_id': 'sable_snow_large_b_meet_aeriola', 'dialog': [
		"She watched us enter. Didn't move.",
		"That's not patience. That's certainty.",
		"She's been here long enough to know exactly how this chamber works against us.",
		"Assume she's right about everything except the outcome."
	]},
	{ 'npc_id': 'thorn', 'dialog_id': 'thorn_snow_large_b_meet_aeriola', 'dialog': [
		"She called it violence. We called it intervention.",
		"(flat)",
		"You know the difference? The people still breathing when the ice broke.",
		"She doesn't get to rewrite that."
	]},
	{ 'npc_id': 'ghost', 'dialog_id': 'ghost_snow_large_b_meet_aeriola', 'dialog': [
		"She's been alone in here since she fell.",
		"(very quiet)",
		"Months of frozen silence with nothing but collected moments for company.",
		"Whatever she's become — the sanctum shaped it.",
		"Don't give her time to stabilize. She's had enough of that."
	]},
	{ 'npc_id': 'nia', 'dialog_id': 'nia_snow_large_b_meet_aeriola', 'dialog': [
		"She turned her grief into a fortress and moved in.",
		"(soft, almost awed)",
		"I've seen performers build a character so complete they forget they're performing.",
		"She's not performing. That's the terrifying part.",
		"She is entirely this."
	]},
	{ 'npc_id': 'dare', 'dialog_id': 'dare_snow_large_b_meet_aeriola', 'dialog': [
		"She can add to her collection or she can lose what she's already holding.",
		"(grinning)",
		"We break every frozen moment in here. Every. Single. One."
	]},
	{ 'npc_id': 'lyric', 'dialog_id': 'lyric_snow_large_b_meet_aeriola', 'dialog': [
		"A sustained temporal construct reinforced by emotional attachment across multiple collapse events.",
		"The math on that is — I've never seen it work this long.",
		"(studying the chamber)",
		"The instability will be catastrophic. That's either the worst problem or the best vulnerability.",
		"I'll have a recommendation in approximately thirty seconds.",
		"(beat) Twenty."
	]},

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
			{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'aeriolass_frozen_sanctum', 'location': 'final_chamber' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_b_entering_sanctum' }},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'aeriola', 'dialog_id': 'aeriola_b_risen' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique',   'dialog_id': 'chock_snow_large_b_meet_aeriola'   } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in',  'dialog_id': 'kor_in_snow_large_b_meet_aeriola'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_snow_large_b_meet_aeriola'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',   'dialog_id': 'kaera_snow_large_b_meet_aeriola'   } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_snow_large_b_meet_aeriola'   } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic',   'dialog_id': 'moxie_snow_large_b_meet_aeriola'   } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_snow_large_b_meet_aeriola' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',   'dialog_id': 'lyren_snow_large_b_meet_aeriola'   } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple',  'dialog_id': 'ripple_snow_large_b_meet_aeriola'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg',   'dialog_id': 'bragg_snow_large_b_meet_aeriola'   } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable',   'dialog_id': 'sable_snow_large_b_meet_aeriola'   } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',   'dialog_id': 'thorn_snow_large_b_meet_aeriola'   } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ghost',   'dialog_id': 'ghost_snow_large_b_meet_aeriola'   } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',     'dialog_id': 'nia_snow_large_b_meet_aeriola'     } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'dare',    'dialog_id': 'dare_snow_large_b_meet_aeriola'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyric',   'dialog_id': 'lyric_snow_large_b_meet_aeriola'   } },
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
			{ 'event_type': 'initiate_dialog',           'params': { 'npc_id': 'aeriola',    'dialog_id': 'aeriola_b_defeated' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique',  'dialog_id': 'chock_snow_large_b_defeat_aeriola'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in',     'dialog_id': 'kor_in_b_victory'                  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith',      'dialog_id': 'kaera_snow_large_b_defeat_aeriola'  } },
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