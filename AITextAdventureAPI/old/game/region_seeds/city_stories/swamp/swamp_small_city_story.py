ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	{
		'npc_id': 'bogrunner_tavik',
		'name': 'Tavik Bogrunner',
		'description': (
			'A wiry trader who ferries goods through the swamp\'s most treacherous channels.'
			' Tavik\'s skiff is patched with mismatched planks and swamp‑etched runes.'
			' He claims the bog itself shows him safe paths when danger rises.'
		),
		"image": "swamp_small:bogrunner_tavik1",
		"psychology": {
			"mbti": "ISTP",
			"dominant": "Ti — Reads the channel's currents as a precise internal model; the swamp's moods are logic he has learned to solve.",
			"auxiliary": "Se — Physically at home in the mire; every shift in water-colour and reed-sound is registered before he processes it.",
			"tertiary": "Ni — A runner's gut-sense for when a safe route is about to become anything but.",
			"inferior": "Fe — Keeps his routes to himself because sharing means slowing down, and slowing down in the swamp gets you killed."
		},
		"enneagram": {
			"enneagram_type": "8w9",
			"core_fear": "A route swallowing the skiff because he trusted the bog one time too many.",
			"core_desire": "To keep running the channels long after everyone else has given up on them.",
			"defense_mechanism": "Denial — Dismisses how badly the Swallowed Path has corrupted his routes until the channel simply vanishes.",
			"stress_line": "Moves to Type 5 — Goes quiet and methodical when the bog stops showing him the way.",
			"growth_line": "Moves to Type 2 — Shares a route when someone's life genuinely depends on it.",
			"instinctual_variant": "sp/so — Self-reliance in the channels extended as quiet service to anyone who needs passage."
		}
	},
	{
		'npc_id': 'rotwharf_madra',
		'name': 'Madra Rotwharf',
		'description': (
			'A hardened broker who deals in illicit wares dredged from the swamp\'s depths.'
			' Madra\'s voice is rough, as though she\'s swallowed too much swamp fog.'
			' She knows every outlaw, fugitive, and mercenary who passes through Hollow\'s shadows.'
		),
		"image": "swamp_small:rotwharf_madra1",
		"psychology": {
			"mbti": "ENTJ",
			"dominant": "Te — Runs the Rotwharf with unsentimental efficiency; the only metric is whether the deal gets done.",
			"auxiliary": "Ni — Has an uncanny sense for who is passing through the Hollow and what they actually need before they say it.",
			"tertiary": "Se — Reads the wharf physically — posture, smell, the way someone holds their pack — as a primary threat-assessment tool.",
			"inferior": "Fi — Rarely reveals what she personally cares about; vulnerability is a weapon she doesn't offer."
		},
		"enneagram": {
			"enneagram_type": "8w9",
			"core_fear": "The Rotwharf losing its reputation as the one place in the Hollow where deals stick.",
			"core_desire": "To be the most reliably dangerous and reliably trustworthy broker the swamp has ever produced.",
			"defense_mechanism": "Denial — Refuses to acknowledge how badly the Swallowed Path has disrupted her supply lines until it's undeniable.",
			"stress_line": "Moves to Type 5 — Becomes cold and calculating when the Hollow's shadows stop obeying any logic she knows.",
			"growth_line": "Moves to Type 2 — Becomes openly protective of those she has done business with long enough to trust.",
			"instinctual_variant": "so/sp — Reputation as the Hollow's most capable broker is the foundation of her identity."
		}
	},
	{
		'npc_id': 'channel_seer_draveth',
		'name': 'Draveth the Channel‑Seer',
		'description': (
			'A swamp navigator who reads current‑signs and senses when routes vanish beneath the mire.'
		),
		"image": "swamp_small:channel_seer_draveth1",
		"psychology": {
			"mbti": "INTP",
			"dominant": "Ti — Classifies current-signs into a precise internal model; a vanishing route has a specific signature he can diagnose.",
			"auxiliary": "Ne — Connects current-patterns across different parts of the swamp to find the source of the disruption.",
			"tertiary": "Si — Decades of current-reading form a living archive of the mire's behaviour.",
			"inferior": "Fe — Cannot easily convey the urgency of a disappearing route to those who haven't felt the pull beneath the water."
		},
		"enneagram": {
			"enneagram_type": "5w4",
			"core_fear": "A current he misread that swallows a traveler he could have warned.",
			"core_desire": "A complete map of every current-sign and the exact conditions under which a route vanishes.",
			"defense_mechanism": "Isolation — Retreats deeper into the channels when his readings are dismissed.",
			"stress_line": "Moves to Type 7 — Becomes restless when the Swallowed Path defies every current-pattern he knows.",
			"growth_line": "Moves to Type 8 — Acts decisively when the channel's crisis demands more than reading.",
			"instinctual_variant": "sp/sx — Solitary channel-reading; bonds only with those who trust the current over the compass."
		}
	},
	{
		'npc_id': 'murkchannel_echo',
		'name': 'Murkchannel Echo',
		'description': (
			'A spectral remnant of forgotten channels twisted by the Swallowed Path.'
		),
		"image": "swamp_small:murkchannel_echo1",
		"psychology": {
			"mbti": "ISFJ",
			"dominant": "Si — Loops the memory of a channel that once ran safely; the loop is perfect and cannot stop because the route cannot accept that it is gone.",
			"auxiliary": "Fe — The channel was used by travelers; that communal purpose persists as a haunting pull on anyone nearby.",
			"tertiary": "Ti — Attempts to resolve the loop by finding the point where the channel's logic failed; never quite reaching it.",
			"inferior": "Ne — Cannot conceive of a new route; the forgotten one is all it knows."
		},
		"enneagram": {
			"enneagram_type": "6w5",
			"core_fear": "The channel being forgotten entirely — the memory dissolving into the mire.",
			"core_desire": "For the route to be remembered and someone to walk it safely again.",
			"defense_mechanism": "Projection — Draws travelers toward the old channel, unable to distinguish guidance from misdirection.",
			"stress_line": "Moves to Type 3 — Becomes urgently insistent, pulling harder when travelers try to find a different way.",
			"growth_line": "Moves to Type 9 — Rests when the Swallowed Path is resolved and the channel can finally be released.",
			"instinctual_variant": "so/sp — Communal route as the only identity it has ever carried."
		}
	},
	{
		'npc_id': 'rotfen_voice',
		'name': 'Rotfen Voice',
		'description': (
			'A whispering presence formed from lost routes deep within the Hideaway.'
		),
		"image": "swamp_small:rotfen_voice1",
		"psychology": {
			"mbti": "INFP",
			"dominant": "Fi — Exists as the grief of routes that were lost and never found again; the loss is felt, not mapped.",
			"auxiliary": "Ne — Traces the connections between lost routes, producing half-formed directions that lead nowhere useful.",
			"tertiary": "Si — Anchored to the specific channels and the swamp-sounds that marked them before they vanished.",
			"inferior": "Te — Cannot redirect; it can only whisper and pull the lost further from any real path."
		},
		"enneagram": {
			"enneagram_type": "4w5",
			"core_fear": "The last lost route dissolving without anyone having found it.",
			"core_desire": "For someone to follow its whisper all the way to where the routes were lost and understand what happened there.",
			"defense_mechanism": "Introjection — Has absorbed every lost route's memory until it cannot distinguish its own nature from the paths it mourns.",
			"stress_line": "Moves to Type 2 — Becomes desperate and grasping when the Swallowed Path threatens to consume the last memory it holds.",
			"growth_line": "Moves to Type 1 — Releases the lost routes with dignity when the Hideaway's corruption is finally cleared.",
			"instinctual_variant": "sx/sp — Exists most fully when someone is close enough to the lost route to almost find it."
		}
	}
]


NPC_DIALOG = [

    {
        'npc_id': 'bogrunner_tavik',
        'dialog_id': 'tavik_intro',
        'dialog': [
            "The channels twist where they once ran straight.",
            "The swamp hides its own paths.",
            "Something swallows the routes we trust."
        ]
    },

    {
        'npc_id': 'rotwharf_madra',
        'dialog_id': 'madra_intro',
        'dialog': [
            "Shadows move wrong in Hollow.",
            "Smugglers vanish on routes they've walked for years.",
            "If we don't act, the swamp will claim every traveler."
        ]
    },

    {
        'npc_id': 'channel_seer_draveth',
        'dialog_id': 'draveth_intro',
        'dialog': [
            "The current‑signs vanish.",
            "A Swallowed Path rises — a spirit of devoured routes.",
            "If it awakens fully, no one will find their way out."
        ]
    },

    {
        'npc_id': 'murkchannel_echo',
        'dialog_id': 'murkchannel_echo_intro',
        'dialog': [
            "We are the channels the swamp forgot.",
            "The Swallowed Path twists our flow.",
            "It waits deeper in the Rotfen Hideaway."
        ]
    },

    {
        'npc_id': 'rotfen_voice',
        'dialog_id': 'rotfen_voice_intro',
        'dialog': [
            "The Hideaway churns with lost routes.",
            "The Swallowed Path gathers strength.",
            "Only its heart remains to be severed."
        ]
    },

    {
        'npc_id': 'bogrunner_tavik',
        'dialog_id': 'tavik_closing',
        'dialog': [
            "The channels clear. The swamp breathes easier.",
            "You've restored the paths the mire tried to swallow.",
            "Travelers will owe you their lives."
        ]
    },

	# ── Type C dialogs — Ghost ──────────────────────────────────────
	{
		'npc_id': 'bogrunner_tavik',
		'dialog_id': 'tavik_c_ghost_sighting',
		'dialog': [
			"Someone moves through the night channels.",
			"No boat. No wake until they're already gone.",
			"Madra's clocked them twice near the Hideaway entrance.",
			"Whoever it is — they're not hiding from the swamp.",
			"They're hiding from us."
		]
	},
	{
		'npc_id': 'rotwharf_madra',
		'dialog_id': 'madra_c_ghost_vouch',
		'dialog': [
			"I've seen every kind of shadow pass through Hollow.",
			"Bounty hunters, deserters, couriers running black-market routes.",
			"This one's different.",
			"They move like the dark owes them a favour.",
			"I caught a name once. Ghost.",
			"They don't move for coin or cause.",
			"Find out what they're watching — that might earn you a word."
		]
	},
	{
		'npc_id': 'ghost',
		'dialog_id': 'ghost_c_first_meet',
		'dialog': [
			"You weren't followed.",
			"Good.",
			"I've been watching your party since the Riftlands.",
			"You operate quietly.",
			"That's worth something in Hollow.",
			"Say what you want."
		]
	},
	{
		'npc_id': 'ghost',
		'dialog_id': 'ghost_c_joins',
		'dialog': [
			"The swamp runs on favours and silence.",
			"You've earned both.",
			"I move when I decide. You point the direction.",
			"That's the arrangement."
		]
	},

	# ── Type A dialogs — Ch.7 Airship Tie-In ───────────────────────
	{
		'npc_id': 'bogrunner_tavik',
		'dialog_id': 'tavik_a_channel_check',
		'dialog': [
			"Something big is moving through the upper channels — airship-scale displacement.",
			"If Seth tries to lift off before the mire settles, the suction will collapse three routes.",
			"Get Draveth to read the current-signs.",
			"If he clears it, the swamp can handle the departure."
		]
	},
	{
		'npc_id': 'channel_seer_draveth',
		'dialog_id': 'draveth_a_clearance',
		'dialog': [
			"The channels are restless — they feel the engine pressure from the outpost.",
			"But the flow holds.",
			"Mire absorption rate is high enough to handle the displacement.",
			"Tell Madra the current-signs confirm it. She'll relay to Seth."
		]
	},
	{
		'npc_id': 'rotwharf_madra',
		'dialog_id': 'madra_a_network_clear',
		'dialog': [
			"Draveth's read is in.",
			"My network's gone quiet — no bounties filed, no interference flagged.",
			"Hollow's clear.",
			"Tell Seth he can lift off."
		]
	},

]

# ── Type D dialogs — Rotfen Dredge Blade ───────────────────────

NPC_DIALOG += [

    {
        'npc_id': 'channel_seer_draveth',
        'dialog_id': 'draveth_d_vessel_read',
        'dialog': [
            "This vessel — the memory inside it is not from the Hollow.",
            "It carries an imprint of the Bayou's oldest channels.",
            "The Rotfen Voice will sense it the moment you cross the Hideaway threshold.",
            "It will interpret the vessel as a claim on its territory.",
            "That anger is what we need. It will surface — and you will be ready."
        ]
    },

    {
        'npc_id': 'rotfen_voice',
        'dialog_id': 'rotfen_voice_d_awakens',
        'dialog': [
            "That vessel does not belong in the Hollow.",
            "The Bayou's memory is a poison here.",
            "You carry it as a weapon against me.",
            "Then I will take it — and every route you ever knew."
        ]
    },

    {
        'npc_id': 'diego',
        'dialog_id': 'diego_d_swamp_vessel_received',
        'dialog': [
            "That vessel — the clay holds a forge-resonance I've never felt from a swamp relic.",
            "There's metal inside the Hollow that only this thing can unlock.",
            "Find Draveth. He reads the channels — he'll know where the resonance leads."
        ]
    },

]

# --- Character dialogs: main story chain ---
NPC_DIALOG += [

	# Meet Tavik
	{ 'npc_id': 'thorn',  'dialog_id': 'thorn_swamp_small_meet_tavik',  'dialog': [ "Channels twisting where they used to run straight. The swamp's hiding its own paths again." ] },
	{ 'npc_id': 'sable',  'dialog_id': 'sable_swamp_small_meet_tavik',  'dialog': [ "Something's swallowing the routes we trust. I've felt that kind of silence before." ] },
	{ 'npc_id': 'ripple', 'dialog_id': 'ripple_swamp_small_meet_tavik', 'dialog': [ "The current doesn't forget. When it starts erasing itself, someone's making it." ] },

	# Meet Madra
	{ 'npc_id': 'nia',    'dialog_id': 'nia_swamp_small_meet_madra',    'dialog': [ "Smugglers vanishing on routes they've walked for years. Shadows moving wrong in Hollow." ] },
	{ 'npc_id': 'bragg',  'dialog_id': 'bragg_swamp_small_meet_madra',  'dialog': [ "If we don't act, the swamp claims every traveler. She's not exaggerating." ] },
	{ 'npc_id': 'kor_in', 'dialog_id': 'kor_in_swamp_small_meet_madra', 'dialog': [ "Some places only stay open if someone keeps walking them. Hollow is losing that." ] },

	# Find Draveth
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_small_find_draveth', 'dialog': [ "A Swallowed Path — spirit of devoured routes. If it wakes fully, no one finds their way out." ] },
	{ 'npc_id': 'ripple',  'dialog_id': 'ripple_swamp_small_find_draveth',  'dialog': [ "The current-signs are already vanishing. It's rising under the murk." ] },
	{ 'npc_id': 'sable',   'dialog_id': 'sable_swamp_small_find_draveth',   'dialog': [ "Listen carefully. The swamp is trying to forget its own roads." ] },

	# Murkchannel Run
	{ 'npc_id': 'ripple', 'dialog_id': 'ripple_swamp_small_murkchannel_run', 'dialog': [ "We are the channels the swamp forgot. The Swallowed Path is twisting their flow." ] },
	{ 'npc_id': 'kor_in', 'dialog_id': 'kor_in_swamp_small_murkchannel_run', 'dialog': [ "It waits deeper in the Rotfen Hideaway. Of course it does." ] },
	{ 'npc_id': 'lyren',  'dialog_id': 'lyren_swamp_small_murkchannel_run',  'dialog': [ "Some paths only remember how to be erased. We force them open again." ] },

	# Rotfen Hideaway
	{ 'npc_id': 'thorn', 'dialog_id': 'thorn_swamp_small_rotfen_hideaway', 'dialog': [ "The Hideaway is churning with lost routes. The Path is gathering strength." ] },
	{ 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_rotfen_hideaway', 'dialog': [ "Only its heart remains. Sever it before the channels close for good." ] },
	{ 'npc_id': 'bragg', 'dialog_id': 'bragg_swamp_small_rotfen_hideaway', 'dialog': [ "Then we go cut the heart out." ] },

	# Swallowed Path
	{ 'npc_id': 'thorn', 'dialog_id': 'thorn_swamp_small_swallowed_path', 'dialog': [ "The channels clear. The swamp breathes easier." ] },
	{ 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_swallowed_path', 'dialog': [ "You've restored the paths the mire tried to swallow. Travelers will owe you their lives." ] },
	{ 'npc_id': 'nia',   'dialog_id': 'nia_swamp_small_swallowed_path',   'dialog': [ "Tavik can run them safely again. That's enough." ] },

]

# --- Character dialogs: Type D (Rotfen Dredge Blade chain) ---
NPC_DIALOG += [

	# Type D – Deliver Memory Vessel
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_small_d_deliver_memory_vessel', 'dialog': [ "The clay holds a forge-resonance Diego's never felt from a swamp relic. There's metal inside the Hollow only this can unlock." ] },
	{ 'npc_id': 'ripple',  'dialog_id': 'ripple_swamp_small_d_deliver_memory_vessel',  'dialog': [ "Draveth reads the channels. He'll know where the resonance leads." ] },
	{ 'npc_id': 'kor_in',  'dialog_id': 'kor_in_swamp_small_d_deliver_memory_vessel',  'dialog': [ "The Bayou's memory doesn't belong here — and the Rotfen Voice already knows it." ] },

	# Type D – Consult Draveth
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_small_d_consult_draveth', 'dialog': [ "The memory inside is not from the Hollow. It carries the Bayou's oldest channels. The Voice will read it as a claim on its territory." ] },
	{ 'npc_id': 'sable',   'dialog_id': 'sable_swamp_small_d_consult_draveth',   'dialog': [ "That anger is what we need. It will surface. We will be ready." ] },
	{ 'npc_id': 'ripple',  'dialog_id': 'ripple_swamp_small_d_consult_draveth',  'dialog': [ "The Hideaway won't stay open long. Move." ] },

	# Type D – Meet Rotfen Voice
	{ 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_d_meet_rotfen_voice', 'dialog': [ "It already decided the vessel is poison here." ] },
	{ 'npc_id': 'thorn', 'dialog_id': 'thorn_swamp_small_d_meet_rotfen_voice', 'dialog': [ "It will take the vessel — and every route we ever knew. We don't let it." ] },
	{ 'npc_id': 'lyren', 'dialog_id': 'lyren_swamp_small_d_meet_rotfen_voice', 'dialog': [ "Some voices only know how to keep what the swamp tried to forget." ] },

	# Type D – Defeat Rotfen Voice
	{ 'npc_id': 'thorn',   'dialog_id': 'thorn_swamp_small_d_defeat_rotfen_voice',   'dialog': [ "Quiet. Take the swamp-iron." ] },
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_small_d_defeat_rotfen_voice', 'dialog': [ "It knows every route the swamp has ever swallowed. You won't get lost carrying this." ] },
	{ 'npc_id': 'sable',   'dialog_id': 'sable_swamp_small_d_defeat_rotfen_voice',   'dialog': [ "Every route the Voice devoured has returned. The channels flow clean again." ] },

]

# --- Character dialogs: Type A Ch.7 ---
NPC_DIALOG += [

	# Type A – Ch7 Find Pendant
	{ 'npc_id': 'nia',    'dialog_id': 'nia_swamp_small_a_ch7_find_pendant',    'dialog': [ "Silver pendant from a sunken skiff named Vale. Delicate work — not from around here." ] },
	{ 'npc_id': 'kor_in', 'dialog_id': 'kor_in_swamp_small_a_ch7_find_pendant', 'dialog': [ "Nobody claimed it. Someone out there is missing it." ] },
	{ 'npc_id': 'ripple', 'dialog_id': 'ripple_swamp_small_a_ch7_find_pendant', 'dialog': [ "You look like people who travel. Maybe you know the name." ] },

]

# --- Character dialogs: Type C (Ghost chain) ---
NPC_DIALOG += [

	# Type C – Find Ghost
	{ 'npc_id': 'bragg', 'dialog_id': 'bragg_swamp_small_c_find_ghost', 'dialog': [ "Someone moves through the night channels with no boat, no wake, until they're already gone." ] },
	{ 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_c_find_ghost', 'dialog': [ "Madra's clocked them twice near the Hideaway. They're not hiding from the swamp — they're hiding from us." ] },
	{ 'npc_id': 'thorn', 'dialog_id': 'thorn_swamp_small_c_find_ghost', 'dialog': [ "Find out what they're watching. That might earn a word." ] },

	# Type C – Madra Vouch
	{ 'npc_id': 'bragg', 'dialog_id': 'bragg_swamp_small_c_madra_vouch', 'dialog': [ "I've seen every kind of shadow. This one moves like the dark owes them a favour." ] },
	{ 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_c_madra_vouch', 'dialog': [ "Name's Ghost. They don't move for coin or cause. Find out what they're watching." ] },
	{ 'npc_id': 'nia',   'dialog_id': 'nia_swamp_small_c_madra_vouch',   'dialog': [ "That might earn you a word. Worth the risk." ] },

	# Type C – Meet Ghost
	{ 'npc_id': 'bragg', 'dialog_id': 'bragg_swamp_small_c_meet_ghost', 'dialog': [ "We've been watched since the Riftlands. Operating quietly is worth something in Hollow." ] },
	{ 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_c_meet_ghost', 'dialog': [ "The swamp runs on favours and silence. We've earned both." ] },
	{ 'npc_id': 'thorn', 'dialog_id': 'thorn_swamp_small_c_meet_ghost', 'dialog': [ "They move when they decide. We point the direction. That's the arrangement." ] },

]

# --- Character dialogs: Type A Channel Check ---
NPC_DIALOG += [

	# Type A – Channel Check
	{ 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_small_a_channel_check', 'dialog': [ "Engine pressure from the outpost is disturbing the current-signs, but the flow holds. Mire absorption is high enough." ] },
	{ 'npc_id': 'ripple',  'dialog_id': 'ripple_swamp_small_a_channel_check',  'dialog': [ "Tell Madra the current-signs confirm it. She'll relay to Seth." ] },
	{ 'npc_id': 'sable',   'dialog_id': 'sable_swamp_small_a_channel_check',   'dialog': [ "Her network's already gone quiet. His word is the last thing she needs." ] },

	# Type A – Relay to Madra
	{ 'npc_id': 'bragg', 'dialog_id': 'bragg_swamp_small_a_relay_to_madra', 'dialog': [ "Draveth's read is in. Network's quiet — no bounties, no interference." ] },
	{ 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_a_relay_to_madra', 'dialog': [ "The city's stopped watching. Tell Seth he can take the sky." ] },
	{ 'npc_id': 'thorn', 'dialog_id': 'thorn_swamp_small_a_relay_to_madra', 'dialog': [ "Finally." ] },

]


TASKS = [
	{
		'task_id': 'swamp_small_city_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'bogrunner_tavik',
					'location': 'region_city_other1'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'bogrunner_tavik',
					'standing_text': [
						"The channels whisper secrets—ride with me and tell what the swamp showed you."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'rotwharf_madra',
					'location': 'region_city_other2'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rotwharf_madra',
					'standing_text': [
						"Hollow's shadows remember faces—stay and tell me what brought you here."
					]
				}
			},
		],
		'task_complete_events': [
            { 'event_type': 'award_task', 'params': { 'task_id': 'swamp_small_city_type_a_ch7_find_pendant' }},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_regional_complete_gate'
				}
			},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'swamp_small_city_type_d_deliver_memory_vessel' }},
		]
	},
    {
        'task_id': 'swamp_small_city_regional_complete_gate',
        'type': 'complete_regional_quests',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_meet_tavik'
                }
            },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_type_c_find_ghost'
				}
			},
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_type_a_channel_check'
                }
            }
        ]

    },

    # Task 1 — Meet Tavik after initialization
    {
        'task_id': 'swamp_small_city_meet_tavik',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'bogrunner_tavik',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bogrunner_tavik',
                    'dialog_id': 'tavik_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',  'dialog_id': 'thorn_swamp_small_meet_tavik'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable',  'dialog_id': 'sable_swamp_small_meet_tavik'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_swamp_small_meet_tavik' } },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'bogrunner_tavik',
                    'standing_text': [
                        "The channels twist where they once ran straight.",
                        "Something hides the safe paths."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_meet_madra'
                }
            }
        ]
    },

    # Task 2 — Meet Madra for the outlaw‑network perspective
    {
        'task_id': 'swamp_small_city_meet_madra',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rotwharf_madra',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rotwharf_madra',
                    'dialog_id': 'madra_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',    'dialog_id': 'nia_swamp_small_meet_madra'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg',  'dialog_id': 'bragg_swamp_small_meet_madra'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_swamp_small_meet_madra' } },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'rotwharf_madra',
                    'standing_text': [
                        "Shadows move wrong in Hollow.",
                        "Someone — or something — is swallowing the routes smugglers rely on."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_find_draveth'
                }
            }
        ]
    },

    # Task 3 — Find Channel‑Seer Draveth in the open swamp
    {
        'task_id': 'swamp_small_city_find_draveth',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'channel_seer_draveth',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'channel_seer_draveth',
                    'location': 'region_city_bar'
                }
            },
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'channel_seer_draveth',
                    'dialog_id': 'draveth_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_small_find_draveth' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple',  'dialog_id': 'ripple_swamp_small_find_draveth'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable',   'dialog_id': 'sable_swamp_small_find_draveth'   } },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'channel_seer_draveth',
					'standing_text': [
						"The current-signs vanish.",
						"A Swallowed Path rises — a spirit of devoured routes.",
						"If it awakens fully, no one will find their way out."
					]
				}
			},
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_murkchannel_run'
                }
            }
        ]
    },

    # Task 4 — Explore the Murkchannel Run (first dungeon)
    {
        'task_id': 'swamp_small_city_murkchannel_run',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'murkchannel_echo',
        'task_acquire_events': [			
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'murkchannel_echo',
                    'location': None
                }
            },
			{
				'event_type': 'create_dungeon',
				'params': {
					'dungeon_id': 'murkchannel_run',
					'location': 'region_open_area'
				}
			},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'murkchannel_run', 'item_id': 'current_gloves', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'murkchannel_run', 'item_id': 'siege_sabatons', 'location': 'treasure_room' }},
		],
		'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'murkchannel_echo',
                    'dialog_id': 'murkchannel_echo_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_swamp_small_murkchannel_run' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_swamp_small_murkchannel_run' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren',  'dialog_id': 'lyren_swamp_small_murkchannel_run'  } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'murkchannel_echo', 'standing_text': [ "We are the channels the swamp forgot.", "The Swallowed Path twists our flow.", "It waits deeper in the Rotfen Hideaway." ] } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_rotfen_hideaway'
                }
            }
        ]
    },

    # Task 5 — Descend into the Rotfen Hideaway (second dungeon)
    {
        'task_id': 'swamp_small_city_rotfen_hideaway',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rotfen_voice',
        'task_acquire_events': [			
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'rotfen_voice',
                    'location': None
                }
            },
			{
				'event_type': 'create_dungeon',
				'params': {
					'dungeon_id': 'rotfen_hideaway',
					'location': 'region_open_area'
				}
			},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'rotfen_hideaway', 'item_id': 'mythic_swamp_small_rotfen_dredge_blade', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'rotfen_hideaway', 'item_id': 'phantom_edge', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'rotfen_hideaway', 'item_id': 'seer_veil', 'location': 'treasure_room' }},
		],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rotfen_voice',
                    'dialog_id': 'rotfen_voice_intro'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_swamp_small_rotfen_hideaway' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_rotfen_hideaway' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_swamp_small_rotfen_hideaway' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rotfen_voice', 'standing_text': [ "The Hideaway churns with lost routes.", "The Swallowed Path gathers strength.", "Only its heart remains to be severed." ] } },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_swallowed_path'
                }
            }
        ]
    },

    # Task 6 — Defeat the Swallowed Path (boss dungeon)
    {
        'task_id': 'swamp_small_city_swallowed_path',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'swallowed_path_1',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'swallowed_path_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bogrunner_tavik',
                    'dialog_id': 'tavik_closing'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_swamp_small_swallowed_path' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_swallowed_path' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_swamp_small_swallowed_path'   } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rotfen_voice', 'standing_text': [ "The channels clear. The swamp breathes easier.", "You've restored the paths the mire tried to swallow.", "Travelers will owe you their lives." ] } }
        ]
    },

    # ── Type D ── Rotfen Dredge Blade (mythic weapon) ─────────────────────────────
    # Gate: player holds swamp_small_city_e_gnashwater_memory_vessel from the Ch.20 Type E chain.
    # Deliver to Diego → Draveth reads the vessel → defeat Rotfen Voice → mythic weapon.

    {
        'task_id': 'swamp_small_city_type_d_deliver_memory_vessel',
        'type': 'deliver',
        'item_id': 'swamp_small_city_e_gnashwater_memory_vessel',
        'to_type': 'npc',
        'to_id': 'diego',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'diego',
                    'dialog_id': 'diego_d_swamp_vessel_received'
                }
            },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_small_d_deliver_memory_vessel' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple',  'dialog_id': 'ripple_swamp_small_d_deliver_memory_vessel'  } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in',  'dialog_id': 'kor_in_swamp_small_d_deliver_memory_vessel'  } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'diego', 'standing_text': [ "The clay holds a forge-resonance I've never felt from a swamp relic.", "There's metal inside the Hollow that only this thing can unlock.", "Find Draveth. He reads the channels — he'll know where the resonance leads." ] } },
            {
                'event_type': 'remove_item',
                'params': {
                    'item_id': 'swamp_small_city_e_gnashwater_memory_vessel'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'channel_seer_draveth',
                    'standing_text': [
                        "The current-signs surged the moment that vessel crossed the Hollow's edge.",
                        "The Bayou's memory doesn't belong here — and the Rotfen Voice knows it.",
                        "Come quickly. The Hideaway won't stay open long."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_small_city_type_d_consult_draveth'
                }
            },
        ]
    },

	# D-1 — Consult Draveth for the channel reading
	{
		'task_id': 'swamp_small_city_type_d_consult_draveth',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'channel_seer_draveth',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'channel_seer_draveth',
					'dialog_id': 'draveth_d_vessel_read'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_small_d_consult_draveth' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable',   'dialog_id': 'sable_swamp_small_d_consult_draveth'   } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple',  'dialog_id': 'ripple_swamp_small_d_consult_draveth'  } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'channel_seer_draveth', 'standing_text': [ "The memory inside is not from the Hollow.", "It carries the Bayou's oldest channels.", "The Voice will read it as a claim on its territory." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_type_d_meet_rotfen_voice'
				}
			},
		]
	},

	# D-2 — Meet the Rotfen Voice (boss intro)
	{
		'task_id': 'swamp_small_city_type_d_meet_rotfen_voice',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rotfen_voice',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rotfen_voice',
					'dialog_id': 'rotfen_voice_d_awakens'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_d_meet_rotfen_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_swamp_small_d_meet_rotfen_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_swamp_small_d_meet_rotfen_voice' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rotfen_voice', 'standing_text': [ "It already decided the vessel is poison here.", "It will take the vessel — and every route we ever knew.", "We don't let it." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_type_d_defeat_rotfen_voice'
				}
			},
		]
	},

	# D-3 — Defeat the Rotfen Voice; Diego forges the mythic weapon
	{
		'task_id': 'swamp_small_city_type_d_defeat_rotfen_voice',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'rotfen_voice_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'rotfen_voice_1',
					'combat_type': 'boss_battle'
				}
			}
        ],
		'task_complete_events': [
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'rotfen_voice',
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'mythic_swamp_small_rotfen_dredge_blade'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn',   'dialog_id': 'thorn_swamp_small_d_defeat_rotfen_voice'   } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_small_d_defeat_rotfen_voice' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable',   'dialog_id': 'sable_swamp_small_d_defeat_rotfen_voice'   } },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"The swamp-iron the Voice guarded — it's unlike any metal I've handled.",
						"I've worked it into the blade. It knows every route the swamp has ever swallowed.",
						"You won't get lost carrying this."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'channel_seer_draveth',
					'standing_text': [
						"The current-signs flow clean again.",
						"Every route the Voice devoured has returned.",
						"Tavik can run the channels safely now."
					]
				}
			},
		]
	},

]

# ── Type A ── Ch.7 Chapter Tie-In (Lyren's Vale Pendant) ─────────────────────

NPC_DIALOG += [

    {
        'npc_id': 'bogrunner_tavik',
        'dialog_id': 'tavik_a_ch7_pendant',
        'dialog': [
            "Pulled this out of a sunken skiff three weeks ago.",
            "Silver pendant. Delicate work — not from around here.",
            "The skiff had a name burned into the hull: Vale.",
            "I've been asking around but nobody claimed it.",
            "(holds it out) You look like people who travel. Maybe you know someone."
        ]
    },

]

TASKS += [

    # A-1 — Meet Tavik to recover the Vale Pendant
    {
        'task_id': 'swamp_small_city_type_a_ch7_find_pendant',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'bogrunner_tavik',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'bogrunner_tavik', 'dialog_id': 'tavik_a_ch7_pendant' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',    'dialog_id': 'nia_swamp_small_a_ch7_find_pendant'    } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_swamp_small_a_ch7_find_pendant' } },
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_swamp_small_a_ch7_find_pendant' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'bogrunner_tavik', 'standing_text': [ "The skiff had a name burned into the hull: Vale.", "I've been asking around but nobody claimed it.", "You look like people who travel. Maybe you know someone." ] } },
            { 'event_type': 'award_item', 'params': { 'item_id': 'vale_pendant' }},
        ]
    },

]

TASKS += [

	# =========================================================
	# TYPE C — Ghost (extended character, slot 2)
	# =========================================================

	# C-1 — Tavik reports the mysterious figure in the night channels
	{
		'task_id': 'swamp_small_city_type_c_find_ghost',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'bogrunner_tavik',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'bogrunner_tavik',
					'dialog_id': 'tavik_c_ghost_sighting'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_swamp_small_c_find_ghost' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_c_find_ghost' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_swamp_small_c_find_ghost' } },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'bogrunner_tavik',
					'standing_text': [
						"Madra's clocked them twice near the Hideaway.",
						"They're not hiding from the swamp — they're hiding from us.",
						"Find out what they're watching. That might earn a word."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_type_c_madra_vouch'
				}
			},
		]
	},

	# C-2 — Madra gives the name and the lead
	{
		'task_id': 'swamp_small_city_type_c_madra_vouch',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rotwharf_madra',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rotwharf_madra',
					'dialog_id': 'madra_c_ghost_vouch'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_swamp_small_c_madra_vouch' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_c_madra_vouch' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia',   'dialog_id': 'nia_swamp_small_c_madra_vouch'   } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rotwharf_madra', 'standing_text': [ "The Hideaway's channels are a maze. Ghost knows the way.", "They move when they decide. We point the direction. That's the arrangement." ] } },
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_type_c_meet_ghost'
				}
			},
		]
	},

	# C-3 — Meet Ghost; Ghost joins the party
	{
		'task_id': 'swamp_small_city_type_c_meet_ghost',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'ghost',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'ghost',
					'location': None
				}
			},
			{
				'event_type': 'create_dungeon',
				'params': {
					'dungeon_id': 'ghost_hideaway',
					'location': 'region_open_area'
				}
			},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'ghost_hideaway', 'item_id': 'saltwind_leathers', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'ghost_hideaway', 'item_id': 'ledger_bracers', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'ghost_hideaway', 'item_id': 'archive_coat', 'location': 'treasure_room' }},
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'ghost',
					'dialog_id': 'ghost_c_first_meet'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'ghost',
					'dialog_id': 'ghost_c_joins'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_swamp_small_c_meet_ghost' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_c_meet_ghost' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_swamp_small_c_meet_ghost' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'ghost', 'standing_text': [ "The channels are clear. The Swallowed Path is gone.", "I can move freely now. I can help you move freely too." ] } },
			{
				'event_type': 'character_join',
				'params': {
					'character_id': 'ghost'
				}
			},
		]
	},

]

TASKS += [

	# =========================================================
	# TYPE A — Ch.7 Airship Channel Clearance
	# =========================================================

	# A-1 — Find Draveth for the channel reading
	{
		'task_id': 'swamp_small_city_type_a_channel_check',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'channel_seer_draveth',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'channel_seer_draveth',
					'dialog_id': 'draveth_a_clearance'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_swamp_small_a_channel_check' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple',  'dialog_id': 'ripple_swamp_small_a_channel_check'  } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable',   'dialog_id': 'sable_swamp_small_a_channel_check'   } },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'channel_seer_draveth',
					'standing_text': [
						"The current-signs are clear. The channels are safe.",
						"Madra will relay the clearance to Seth. He can lift off."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_small_city_type_a_relay_to_madra'
				}
			},
		]
	},

	# A-2 — Relay Draveth's clearance to Madra; she signals Seth
	{
		'task_id': 'swamp_small_city_type_a_relay_to_madra',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rotwharf_madra',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rotwharf_madra',
					'dialog_id': 'madra_a_network_clear'
				}
			},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_swamp_small_a_relay_to_madra' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_swamp_small_a_relay_to_madra' } },
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_swamp_small_a_relay_to_madra' } },
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rotwharf_madra', 'standing_text': [ "The channels are clear. Seth can lift off safely." ] } }
		]
	},

]

PRIMARY_STORY_SETTINGS = {
	'story_id': 'swamp_small_city_story',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}