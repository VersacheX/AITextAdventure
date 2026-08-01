ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'bargaincaller_ress',
		'name': 'Ress the Mire‑Caller',
		'description': (
			'A shrewd dealmaker who trades in charms, curses, and swamp‑born oddities.'
			' Ress\'s lantern glows with shifting green fire that reacts to lies.'
			' He insists every bargain struck in the Court binds both fate and fortune.'
		)
	},
	{
		'npc_id': 'lanternsworn_janrel',
		'name': 'Janrel of the Lantern‑Sworn',
		'description': (
			'A mystic who reads omens in the flicker of swamp‑light flames.'
			' Janrel\'s lantern never extinguishes, even in heavy rain.'
			' She offers guidance to the lost, though her advice often sounds like prophecy.'
		)
	},
	{
		'npc_id': 'oath_reed_selka',
		'name': 'Selka the Oath‑Reed',
		'description': (
			'A swamp oath‑reader who interprets reed‑signs that shift when promises break.'
		)
	},
	{
		'npc_id': 'oathrot_voice',
		'name': 'Oathrot Voice',
		'description': (
			'A whispering presence formed from rotted vows deep within the Channel.'
		)
	},
]

NPC_DIALOG = [

	# --- Base city standing dialog ---

	{
		'npc_id': 'bargaincaller_ress',
		'dialog_id': 'ress_intro',
		'dialog': [
			"The lantern-fire flares at every lie.",
			"Bargains twist in ways no mortal hand could shape.",
			"Something rewrites the Court's fate‑threads."
		]
	},
	{
		'npc_id': 'lanternsworn_janrel',
		'dialog_id': 'janrel_intro',
		'dialog': [
			"The lantern's flame flickers in impossible patterns.",
			"Omen-light bends toward something hidden.",
			"If we ignore this, the swamp will lose its way."
		]
	},
	{
		'npc_id': 'oath_reed_selka',
		'dialog_id': 'selka_intro',
		'dialog': [
			"The reeds whisper of broken promises.",
			"A Broken Pact rises — a spirit of violated bargains.",
			"If it awakens fully, no oath will hold in this mire."
		]
	},
	{
		'npc_id': 'bargaincaller_ress',
		'dialog_id': 'ress_closing',
		'dialog': [
			"The lantern-fire steadies.",
			"The Court's bargains hold true again.",
			"You've restored fate to the swamp."
		]
	},

]

NPC_DIALOG += [

	# --- Type E: Bayou Memory Vessel ---

	{
		'npc_id': 'lanternsworn_janrel',
		'dialog_id': 'janrel_vessel_discovery',
		'dialog': [
			"The lantern showed me something last night I couldn't place.",
			"A vessel — not a container for water or oil. A container for memory.",
			"The swamp has been holding onto something it was never meant to keep.",
			"The omen-light points into the Channel. The vessel is there."
		]
	},
	{
		'npc_id': 'oath_reed_selka',
		'dialog_id': 'selka_vessel_context',
		'dialog': [
			"Memory Vessels were used by the old bayou clans to preserve the last thoughts of the dying.",
			"This one was lost during a flood — the reeds have been whispering about it for decades.",
			"The Oathrot Voice has been absorbing its contents slowly.",
			"You need to pull it out before there's nothing left inside."
		]
	},
	{
		'npc_id': 'oathrot_voice',
		'dialog_id': 'oathrot_voice_vessel_guardian',
		'dialog': [
			"The Vessel feeds us.",
			"Every memory it holds becomes part of our rot.",
			"You would take our sustenance."
		]
	},
    {
        'npc_id': 'lanternsworn_janrel',
        'dialog_id': 'janrel_vessel_received',
        'dialog': [
            "The lantern steadied the moment you returned.",
            "You have it — and the Oathrot Voice no longer does.",
            "When the Broken Pact dissolved, it pressed this into my hands.",
            "A sealed vessel — clay, swamp-fired.",
            "The omen-light reads it as a memory container. Something the Bayou compressed over centuries.",
            "(holding her lantern near it — the flame shifts green)",
            "The Court can't hold it. It belongs further down the swamp.",
            "Gnashwater Hollow was shaped by bargains older than ours.",
            "Whatever is in this vessel — it was made there.",
            "Carry it sealed. If it opens before it arrives, the memory dissipates."
        ]
    }

]

NPC_DIALOG += [

	# --- Type C: Osten Dreamweaver ---

	{
		'npc_id': 'osten_dreamweaver',
		'dialog_id': 'osten_type_c_intro',
		'dialog': [
			"The bayou dreams differently than other places.",
			"The water here holds stories the way skin holds warmth — for a little while after the fire goes out.",
			"I've been transcribing them. There are more than I can carry alone.",
			"You look like someone who has collected a few of their own."
		]
	},
	{
		'npc_id': 'osten_dreamweaver',
		'dialog_id': 'osten_type_c_ress_check',
		'dialog': [
			"Ress called you trustworthy? That's not a word he uses lightly.",
			"He reads people the way the lantern reads lies.",
			"If it didn't flare, you mean what you say."
		]
	},
	{
		'npc_id': 'osten_dreamweaver',
		'dialog_id': 'osten_type_c_join',
		'dialog': [
			"I'll come with you.",
			"The stories I need are moving — they don't stay in one place.",
			"Neither should I."
		]
	},

]

NPC_DIALOG += [

	# --- Type D: Mirebound Sovereign ---

	{
		'npc_id': 'bargaincaller_ress',
		'dialog_id': 'ress_vessel_trade',
		'dialog': [
			"That vessel carries memory older than this city.",
			"The lantern-fire doesn't flare when I hold it — it bows.",
			"There's a blade bound inside a bargain made long before I was born.",
			"Deliver the vessel to Selka. The reeds know the rite to release it."
		]
	},
	{
		'npc_id': 'oath_reed_selka',
		'dialog_id': 'selka_vessel_rite',
		'dialog': [
			"The reeds have waited for this.",
			"The Mirebound Sovereign — a blade forged from the first broken oath in the bayou.",
			"The vessel is the key. But the Court-Guardian will not yield it without a fight.",
			"Face it. Prove the oath is yours to carry."
		]
	},
	{
		'npc_id': 'bargaincaller_ress',
		'dialog_id': 'ress_vessel_reward',
		'dialog': [
			"The lantern blazed the moment you returned.",
			"Not in warning — in recognition.",
			"The Mirebound Sovereign has chosen its bearer. That bargain is sealed."
		]
	},

]

# --- Character dialogs: Type E (Bayou Memory Vessel chain) ---
NPC_DIALOG += [

	# Type E – Investigate Vessel
	{ 'npc_id': 'tech',    'dialog_id': 'kade_swamp_mid_e_investigate_vessel',    'dialog': [ "A vessel for memory, not water or oil. The swamp has been holding onto something it was never meant to keep." ] },
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_mid_e_investigate_vessel', 'dialog': [ "The omen-light points into the Channel. The vessel is there." ] },
	{ 'npc_id': 'skill',   'dialog_id': 'poise_swamp_mid_e_investigate_vessel',   'dialog': [ "Selka will know how long the reeds have been whispering about it." ] },

	# Type E – Consult Selka
	{ 'npc_id': 'tech',    'dialog_id': 'kade_swamp_mid_e_consult_selka',    'dialog': [ "Memory Vessels preserved the last thoughts of the dying. This one was lost in a flood. The Oathrot Voice has been absorbing its contents slowly." ] },
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_mid_e_consult_selka', 'dialog': [ "Pull it out before there's nothing left inside." ] },
	{ 'npc_id': 'skill',   'dialog_id': 'poise_swamp_mid_e_consult_selka',   'dialog': [ "Then we pull it out." ] },

	# Type E – Confront Oathrot Voice
	{ 'npc_id': 'skill', 'dialog_id': 'poise_swamp_mid_e_confront_oathrot_voice', 'dialog': [ "It already decided the Vessel feeds them." ] },
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_swamp_mid_e_confront_oathrot_voice', 'dialog': [ "Every memory it holds becomes part of their rot. They're not going to hand it over." ] },
	{ 'npc_id': 'lyren', 'dialog_id': 'lyren_swamp_mid_e_confront_oathrot_voice', 'dialog': [ "Some voices only know how to keep what the dying left behind." ] },

	# Type E – Defeat Oathrot Voice / Return to Janrel
	{ 'npc_id': 'technique', 'dialog_id': 'chock_swamp_mid_e_return_to_janrel', 'dialog': [ "The lantern steadied the moment we returned. The Voice no longer has it." ] },
	{ 'npc_id': 'faith', 'dialog_id': 'kaera_swamp_mid_e_return_to_janrel', 'dialog': [ "A sealed vessel — clay, swamp-fired. The omen-light reads it as a memory container compressed over centuries." ] },
	{ 'npc_id': 'tech',  'dialog_id': 'kade_swamp_mid_e_return_to_janrel',  'dialog': [ "It belongs further down the swamp. Carry it sealed. If it opens early, the memory dissipates." ] },

]

# --- Character dialogs: Type D (Mirebound Sovereign chain) ---
NPC_DIALOG += [

	# Type D – Deliver Memory Vessel
	{ 'npc_id': 'tech',  'dialog_id': 'kade_swamp_mid_d_deliver_memory_vessel',  'dialog': [ "The lantern-fire bows when it passes. Memory older than this city. There's a blade bound inside a bargain made long before Ress was born." ] },
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_swamp_mid_d_deliver_memory_vessel', 'dialog': [ "Deliver it to Selka. The reeds know the rite to release it." ] },
	{ 'npc_id': 'skill', 'dialog_id': 'poise_swamp_mid_d_deliver_memory_vessel', 'dialog': [ "Move." ] },

	# Type D – Consult Selka
	{ 'npc_id': 'tech',    'dialog_id': 'kade_swamp_mid_d_consult_selka',    'dialog': [ "The Mirebound Sovereign — a blade forged from the first broken oath in the bayou. The vessel is the key." ] },
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_mid_d_consult_selka', 'dialog': [ "The Court-Guardian will not yield it without a fight. Prove the oath is ours to carry." ] },
	{ 'npc_id': 'skill',   'dialog_id': 'poise_swamp_mid_d_consult_selka',   'dialog': [ "Then we prove it." ] },

	# Type D – Meet Court Guardian
	{ 'npc_id': 'skill', 'dialog_id': 'poise_swamp_mid_d_meet_court_guardian', 'dialog': [ "It already decided we must prove we can carry what was never meant to be held." ] },
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_swamp_mid_d_meet_court_guardian', 'dialog': [ "The first broken oath. Bold claim for a guardian." ] },
	{ 'npc_id': 'lyren', 'dialog_id': 'lyren_swamp_mid_d_meet_court_guardian', 'dialog': [ "Some bargains only open for the ones willing to finish them." ] },

	# Type D – Defeat Court Guardian
	{ 'npc_id': 'technique', 'dialog_id': 'chock_swamp_mid_d_defeat_court_guardian', 'dialog': [ "The lantern blazed the moment we returned. Not in warning — in recognition." ] },
	{ 'npc_id': 'faith', 'dialog_id': 'kaera_swamp_mid_d_defeat_court_guardian', 'dialog': [ "The Mirebound Sovereign has chosen its bearer. That bargain is sealed." ] },
	{ 'npc_id': 'tech',  'dialog_id': 'kade_swamp_mid_d_defeat_court_guardian',  'dialog': [ "Carry it with the weight it deserves." ] },

]

# --- Character dialogs: Type C (Osten Dreamweaver chain) ---
NPC_DIALOG += [

	# Type C – Find Osten
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_swamp_mid_c_find_osten', 'dialog': [ "The bayou holds stories the way skin holds warmth — for a little while after the fire goes out. They've been trying to write them all down." ] },
	{ 'npc_id': 'tech',  'dialog_id': 'kade_swamp_mid_c_find_osten',  'dialog': [ "There are more than they can carry alone. We look like people who have collected a few of our own." ] },
	{ 'npc_id': 'faith', 'dialog_id': 'kaera_swamp_mid_c_find_osten', 'dialog': [ "Ress will know whether the lantern trusts them." ] },

	# Type C – Consult Ress
	{ 'npc_id': 'tech',  'dialog_id': 'kade_swamp_mid_c_consult_ress',  'dialog': [ "The lantern hasn't flared once around them in three days. That means something." ] },
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_swamp_mid_c_consult_ress', 'dialog': [ "He reads people the way the lantern reads lies. If it didn't flare, we mean what we say." ] },
	{ 'npc_id': 'skill', 'dialog_id': 'poise_swamp_mid_c_consult_ress', 'dialog': [ "That's enough for them." ] },

	# Type C – Earn Osten
	{ 'npc_id': 'magic', 'dialog_id': 'moxie_swamp_mid_c_earn_osten', 'dialog': [ "The stories they need are moving — they don't stay in one place. Neither should they." ] },
	{ 'npc_id': 'faith', 'dialog_id': 'kaera_swamp_mid_c_earn_osten', 'dialog': [ "They're coming. The bayou's stories travel better with company." ] },
	{ 'npc_id': 'tech',  'dialog_id': 'kade_swamp_mid_c_earn_osten',  'dialog': [ "Good. We could use someone who listens to water." ] },

]


TASKS = [
	{
		'task_id': 'swamp_mid_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'bargaincaller_ress',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'bargaincaller_ress',
					'standing_text': [
						"Charms and curses have stories—tell me yours and I will listen."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'lanternsworn_janrel',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'lanternsworn_janrel',
					'standing_text': [
						"The lantern sees more than light—sit and speak, and I will share what it shows."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_mid_city_type_e_investigate_vessel'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_mid_city_type_c_find_osten'
				}
			}
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE E — Bayou Memory Vessel
	# Artifact ID: swamp_mid_city_e_bayou_memory_vessel
	# Gates: swamp_small_city (Ch.7) Type D — retroactive
	#        swamp_mid_city Type D (this file, slot 2)
	# =========================================================

	{
		'task_id': 'swamp_mid_city_type_e_investigate_vessel',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'lanternsworn_janrel',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'lanternsworn_janrel',
					'dialog_id': 'janrel_vessel_discovery'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_swamp_mid_e_investigate_vessel'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_mid_e_investigate_vessel' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_swamp_mid_e_investigate_vessel'   } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lanternsworn_janrel', 'standing_text': [ "The lantern showed me something last night.", "A vessel. Deep in the Channel. The swamp has been holding it for too long." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_mid_city_type_e_consult_selka'
				}
			}
		]
	},
	{
		'task_id': 'swamp_mid_city_type_e_consult_selka',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'oath_reed_selka',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'oath_reed_selka',
					'location': 'region_city_other2'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'oath_reed_selka',
					'dialog_id': 'selka_vessel_context'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_swamp_mid_e_consult_selka'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_mid_e_consult_selka' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_swamp_mid_e_consult_selka'   } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'oath_reed_selka', 'standing_text': [ "Memory Vessels were used by the old bayou clans to preserve the last thoughts of the dying.", "This one was lost during a flood — the reeds have been whispering about it for decades.", "The Oathrot Voice has been absorbing its contents slowly. You need to pull it out before there's nothing left inside." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_mid_city_type_e_confront_oathrot_voice'
				}
			}
		]
	},
	{
		'task_id': 'swamp_mid_city_type_e_confront_oathrot_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'oathrot_voice',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'oathrot_voice',
					'location': None
				}
			},
			{
				'event_type': 'create_dungeon',
				'params': {
					'dungeon_id': 'swamp_mid_city_oathrot_channel',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'oathrot_voice',
					'standing_text': [
						"The Vessel is ours.",
						"Its memories feed us.",
						"You will not take them."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'oathrot_voice',
					'dialog_id': 'oathrot_voice_vessel_guardian'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_swamp_mid_e_confront_oathrot_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_swamp_mid_e_confront_oathrot_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_swamp_mid_e_confront_oathrot_voice' } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_mid_city_type_e_defeat_oathrot_voice'
				}
			}
		]
	},
	{
		'task_id': 'swamp_mid_city_type_e_defeat_oathrot_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'oathrot_voice',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'oathrot_voice',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'oathrot_voice'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_mid_city_type_e_return_to_janrel'
				}
			}
		]
	},
	{
		'task_id': 'swamp_mid_city_type_e_return_to_janrel',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'lanternsworn_janrel',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'lanternsworn_janrel',
					'dialog_id': 'janrel_vessel_received'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_swamp_mid_e_return_to_janrel' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_swamp_mid_e_return_to_janrel' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_swamp_mid_e_return_to_janrel'  } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lanternsworn_janrel', 'standing_text': [ "The lantern steadied the moment you returned.", "You have it — and the Oathrot Voice no longer does.", "When the Broken Pact dissolved, it pressed this into my hands." ] } },
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'swamp_mid_city_e_bayou_memory_vessel'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_mid_city_type_d_deliver_memory_vessel'
				}
			}
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE D — Mythic Equipment Quest (slot 2)
	# Gate: swamp_mid_city_e_bayou_memory_vessel (from Type E above)
	# Mythic reward: mythic_swamp_mid_mirebound_sovereign (weapon → Diego)
	# =========================================================

	{
		'task_id': 'swamp_mid_city_type_d_deliver_memory_vessel',
		'type': 'deliver',
		'item_id': 'swamp_mid_city_e_bayou_memory_vessel',
		'to_type': 'npc',
		'to_id': 'bargaincaller_ress',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'bargaincaller_ress',
					'dialog_id': 'ress_vessel_trade'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_swamp_mid_d_deliver_memory_vessel'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_swamp_mid_d_deliver_memory_vessel' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_swamp_mid_d_deliver_memory_vessel' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'bargaincaller_ress', 'standing_text': [ "That vessel carries memory older than this city.", "The lantern-fire doesn't flare when I hold it — it bows.", "There's a blade bound inside a bargain made long before I was born.", "Deliver the vessel to Selka. The reeds know the rite to release it." ] } },
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'swamp_mid_city_e_bayou_memory_vessel'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_mid_city_type_d_consult_selka'
				}
			}
		]
	},
	{
		'task_id': 'swamp_mid_city_type_d_consult_selka',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'oath_reed_selka',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'oath_reed_selka',
					'dialog_id': 'selka_vessel_rite'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',    'dialog_id': 'kade_swamp_mid_d_consult_selka'    } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_mid_d_consult_selka' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill',   'dialog_id': 'poise_swamp_mid_d_consult_selka'   } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'oath_reed_selka', 'standing_text': [ "The reeds have waited for this.", "The Mirebound Sovereign — a blade forged from the first broken oath in the bayou.", "The vessel is the key. But the Court-Guardian will not yield it without a fight.", "Face it. Prove the oath is yours to carry." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_mid_city_type_d_meet_court_guardian'
				}
			}
		]
	},
	{
		'task_id': 'swamp_mid_city_type_d_meet_court_guardian',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'oathrot_voice',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_swamp_mid_d_meet_court_guardian' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_swamp_mid_d_meet_court_guardian' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_swamp_mid_d_meet_court_guardian' } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_mid_city_type_d_defeat_court_guardian'
				}
			}
		]
	},
	{
		'task_id': 'swamp_mid_city_type_d_defeat_court_guardian',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'mirebound_court_guardian_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'mirebound_court_guardian_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'bargaincaller_ress',
					'dialog_id': 'ress_vessel_reward'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_swamp_mid_mirebound_sovereign'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'chock_swamp_mid_d_defeat_court_guardian' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_swamp_mid_d_defeat_court_guardian' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_swamp_mid_d_defeat_court_guardian'  } },
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE C — Osten Dreamweaver
	# Extended Character: osten_dreamweaver
	# Final event: character_join
	# Awarded by: swamp_mid_city_initialize (is_chapter_gte 20)
	# =========================================================

	{
		'task_id': 'swamp_mid_city_type_c_find_osten',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'osten_dreamweaver',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'osten_dreamweaver',
					'location': 'region_city_other2'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'osten_dreamweaver',
					'dialog_id': 'osten_type_c_intro'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_swamp_mid_c_find_osten' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_swamp_mid_c_find_osten'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_swamp_mid_c_find_osten' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'osten_dreamweaver', 'standing_text': [ "The bayou holds stories the way skin holds warmth — for a little while after the fire goes out.", "I've been trying to write them all down, but there are more than I can carry alone.", "You look like people who have collected a few of your own." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_mid_city_type_c_consult_ress'
				}
			}
		]
	},
	{
		'task_id': 'swamp_mid_city_type_c_consult_ress',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'bargaincaller_ress',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'osten_dreamweaver',
					'dialog_id': 'osten_type_c_ress_check'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_swamp_mid_c_consult_ress'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_swamp_mid_c_consult_ress' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'poise_swamp_mid_c_consult_ress' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'bargaincaller_ress', 'standing_text': [ "The lantern hasn't flared once around them in three days.", "That means something. It means they mean what they say." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_mid_city_type_c_earn_osten'
				}
			}
		]
	},
	{
		'task_id': 'swamp_mid_city_type_c_earn_osten',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'osten_dreamweaver',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'osten_dreamweaver',
					'dialog_id': 'osten_type_c_join'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_swamp_mid_c_earn_osten' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'kaera_swamp_mid_c_earn_osten' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech',  'dialog_id': 'kade_swamp_mid_c_earn_osten'  } },
			{
				'event_type': 'hide_npc',
				'params': { 'npc_id': 'osten_dreamweaver' }
			},
			{
				'event_type': 'character_join',
				'params': { 'character_id': 'osten_dreamweaver' }
			},
		]
	},

]

PRIMARY_STORY_SETTINGS = {
	'story_id': 'swamp_mid_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}