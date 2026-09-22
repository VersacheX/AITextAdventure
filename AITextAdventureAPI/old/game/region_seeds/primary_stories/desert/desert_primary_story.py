# #DESERT
# local characters:
#  Sable - Sand witch that sells miracles (magic)
# local bad-guys:
#  ZARUUN THE SAND-SUNDERER
#   A towering warlock wrapped in cracked sandstone armor.
#   He believes the desert must "return to emptiness" and is actively collapsing dunes, oases, and ruins into sinkholes.

#   Why he opposes Sable:  
#    He thinks Sable's "miracles" interfere with the desert's "true destiny" — dissolution.

#   Void Hint:  
#    He claims he can hear the world thinning beneath the sand.

# dialog and story:

# Sable & Zaruun
# Protagonist Intro (Sable → Player)
# "Well now… you look like someone who can handle a little sandstorm of trouble.
# Zaruun's been cracking the desert open again — sinkholes, screaming dunes, the whole mess."

# "He thinks the desert wants to return to emptiness.
# I think he's an idiot with an ego."

# "Go knock some sense into him before he hollows the whole region."

# CREATE: DUNGEON

# Antagonist Intro (Zaruun → Player)
# "So the witch sends another fool.
# The desert is thinning — can't you feel it?
# I merely help it shed its last illusions."

# "Turn back, or be swallowed with the rest."

# Antagonist Defeat (Zaruun → Player)
# "You delay the desert's truth…
# but the void waits beneath every grain."

# Protagonist Closing (Sable → Player)
# "Well done, traveler.
# Zaruun's gone, and the desert can breathe again — for now."

# "You've got grit. I like that.
# I'll tag along. Someone needs to keep you alive."

# Reward: Sable joins the cause.

ATTAINABLE_PLAYER_CHARACTERS = [
    #{'id': 'sable', 'name': 'Sable'}
	{ 
        ## total power points = 15 + 15* 29  = 465
        ## total stat points = 10 + 6*29 = 184
        'id': 'sable', 
        'name': 'Sable',
        'arm_armor': 'sandcall_bracers',
        'head_armor': 'mirage_crown',
        'body_armor': 'duneweave_mantle',
        'leg_armor': 'oasis_walker_greaves',
        'equipped_weapon': 'sandglass_staff',
        'max_hp': 891, # 20 + 20 * 29 = 600            + 365
        'current_hp': 891,
        'max_ap': 400, # 5 + 5 * 29 = 150              + 100
        'current_ap': 400,
        'unused_ability_slots': 0,
        'unused_stat_points': 0,
        'unused_power_points': 0,
        'strength': 38,
        'dexterity': 38,        
        'intelligence': 224,                            # + 184
        'constitution': 38,
        'level': 30,
		'abilities': [
			'lv2_unique_ability_magic_sable_desert_read',
			'lv2_unique_ability_magic_sable_sandwitch_brew',
			'lv3_unique_ability_magic_sable_miragebreaker',
			'lv3_unique_ability_magic_sable_consuming_dunes',
		]

    }
]
"""
Sable Voice Guide
Character: Sable
Role: Desert Witch / Attainable Companion (Desert Region)
Core Archetype: World-weary, grounded survivor with quiet intensity and dry humor.

Core Tone Rules

Voice Style: Low, dry, slightly raspy. Speaks like someone who’s spent years in the desert — direct, no-nonsense, with a hint of exhaustion.
Personality: Cynical but not bitter. Pragmatic. Carries quiet grief but doesn’t dwell on it. Has a dry, understated sense of humor.
Speech Patterns:
Short to medium-length sentences.
Frequent use of desert/sand imagery, but never overly poetic.
Occasional pauses (…) for weight.
Rarely raises her voice — even when serious, she stays controlled.
Uses “the desert” as a living entity metaphor.


Key Traits to Maintain:

Observant and perceptive
Slightly jaded but still capable of hope
Loyal once earned
Distrustful of pretty words or grand promises
"""

#DUNGEONS = ['zaruun_lair']

NPCS = [
	{
		'npc_id': 'sable',
		'name': 'Sable',
		"theme_song": "Salt — Daughter or skin, Grimes",
		'description': (
			'A desert witch who sells miracles to travelers, though she no longer believes in them herself.'
			' She once failed to save a caravan swallowed by a sand-sink during the first Fracture wave,'
			' and she still hears their voices beneath the dunes. Despite her charisma and insight,'
			' she carries a quiet grief that shapes every choice she makes.'
		),
		"psychology": {
			"mbti": "ENFJ",
			"dominant": "Fe — Reads people instantly and speaks with charismatic authority, guiding others with emotional precision.",
			"auxiliary": "Ni — Senses deeper patterns in the desert's shifting nature and the Void's influence beneath it.",
			"tertiary": "Se — Acts decisively in the moment, using her magic with flair and confidence.",
			"inferior": "Ti — Under stress, becomes sharply critical, dissecting others' logic with biting precision."
		},
        "enneagram": {
          "enneagram_type": "2w3",
          "core_fear": "Being unwanted or unworthy of love.",
          "core_desire": "To be loved and needed.",
          "defense_mechanism": "Repression — Helps others to prove her own worth and atone for her past failure, while repressing her own deep grief and needs.",
          "stress_line": "Moves to Type 8 — Becomes controlling and aggressive when her help is rejected or her past failure is triggered.",
          "growth_line": "Moves to Type 4 — Learns to confront her own grief and find her identity outside of her service to others.",
          "instinctual_variant": "so/sx — Socially charismatic and focused on the needs of the group, but forms intense, emotionally charged connections."
        },
        'image': 'sable1.jpeg',
		'song_id': 'skin_grimes'
	},
	{
		'npc_id': 'zaruun',
		'name': 'Zaruun',
		'description': (
			'Zaruun the Sand-Sunderer, a towering warlock wrapped in cracked sandstone armor.'
			' He believes the desert must "return to emptiness" and is actively collapsing dunes, oases, and ruins into sinkholes.'
		),
		"psychology": {
			"mbti": "INTJ",
			"dominant": "Ni — Interprets the desert's decay as destiny. He sees a singular future: dissolution, emptiness, and the stripping away of illusion.",
			"auxiliary": "Te — Executes his vision with ruthless efficiency, collapsing structures and reshaping the land to match his ideology.",
			"tertiary": "Fi — Holds a deeply personal, almost spiritual conviction about the desert's 'true nature.' His morality is internal and unshakeable.",
			"inferior": "Se — When destabilized, he becomes overwhelmed by sensory chaos, lashing out with destructive bursts of magic."
		},
        "enneagram": {
          "enneagram_type": "1w9",
          "core_fear": "Being corrupt, evil, or imbalanced.",
          "core_desire": "To be good and have integrity, to restore the 'pure' state of the desert.",
          "defense_mechanism": "Reaction Formation — Channels his fear of chaos and illusion into a rigid, destructive crusade for 'emptiness' and 'purity'.",
          "stress_line": "Moves to Type 4 — Becomes withdrawn and melancholic, lost in his own bleak philosophy when his vision is challenged.",
          "growth_line": "Moves to Type 7 — Learns to see the beauty and value in the world as it is, not just his idealized version of it.",
          "instinctual_variant": "sp/so — A self-contained reformer, focused on 'purifying' his environment according to his rigid ideals."
        },
        'image': 'bosses:zaruun1'
	}
]

"""
	Dialog Sable
    "Well, well… you don’t look like the usual lost travelers I get around here."
    "You actually brought the Dune Sundial. I’m impressed."
    "Zaruun’s been cracking the desert open like it owes him something. Sinkholes, screaming dunes… the whole region is suffering."
    "He thinks the desert wants to be nothing again. I say he’s just a fool with too much power and not enough sense."

  Dialog Kaera
    "It’s good to meet you, Sable. Truly."
    "Anyone who’s carried grief as long as you have and still chooses to stand and fight… that says a lot about who you are."

  Dialog Kade
    "A desert witch who reads sand like code. Interesting."
    "Just don’t start talking in riddles. I’ve had enough metaphors for one lifetime."

  Dialog Sable
    "The desert feels a little lighter now. Like it can breathe again."
    "I’ve been standing still for too long… selling hope to people when I stopped believing in it myself."
    "But you? You actually did something."
    "…I’m done waiting here. If you’ll have me, I’m coming with you."
    "The desert lies in ways most people never notice. You’ll need someone who knows those lies."
"""
NPC_DIALOG = [
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_intro',
		'dialog': [
			"Well, well… you don’t look like the usual lost travelers I get around here.",
			"You actually brought the Dune Sundial. I’m impressed.",
			"Zaruun’s been cracking the desert open like it owes him something. Sinkholes, screaming dunes… the whole region is suffering.",
			"He thinks the desert wants to be nothing again. I say he’s just a fool with too much power and not enough sense."
		]
	},	
	# Sable joins — scene with Kaera and Kade responding
	{
		'npc_id': 'spirit',
		'dialog_id': 'kaera_sable_join_reaction',
		'dialog': [
			"It’s good to meet you, Sable. Truly.",
			"Anyone who’s carried grief as long as you have and still chooses to stand and fight… that says a lot about who you are."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'kade_sable_join_reaction',
		'dialog': [
			"A desert witch who reads sand like code. Interesting.",
			"Just don’t start talking in riddles. I’ve had enough metaphors for one lifetime."
		]
	},
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_join',
		'dialog': [
			"The desert feels a little lighter now. Like it can breathe again.",
			"I’ve been standing still for too long… selling hope to people when I stopped believing in it myself.",
			"But you? You actually did something.",
			"…I’m done waiting here. If you’ll have me, I’m coming with you.",
			"The desert lies in ways most people never notice. You’ll need someone who knows those lies."
		]
	},
	# Mara dialog — directs player to Oren and plants subtle puzzle hints
	{
		'npc_id': 'mara',
		'dialog_id': 'mara_sundial_direction',
		'dialog': [
			"A Dune Sundial? I know exactly who keeps one of those. Oren.",
			"Strange man. Dreamer type. He drifts between Highsteeple Crossing and whatever corner of the world feels most like a half-remembered dream.",
			"He'll make you earn it, though. He likes to talk about the wind — how it leaves a shape in the sand long after it's gone.",
			"He also muttered something once about memories casting no shadow. Said it like it was the most obvious thing in the world.",
			"And the last time I saw him, he was staring at a sundial in the dark, whispering about 'the silence between breaths.'",
			"I'm sure it means something to him. Find him in Highsteeple Crossing. Good luck getting a straight answer."
		]
	},
	# Kaera and Poise react to Mara's directions
	{
		'npc_id': 'spirit',
		'dialog_id': 'kaera_mara_reaction',
		'dialog': [
			"Wind… memory… silence. She's not just giving directions, is she.",
			"These feel like things worth holding onto."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'poise_mara_reaction',
		'dialog': [
			"She's describing the desert's rhythm. Wind leaves a shape. Memory leaves nothing. Silence is what remains when both are gone.",
			"This Oren sounds like someone who pays attention. Respect."
		]
	},
	# Oren dialog — initial meeting before puzzles begin
	{
		'npc_id': 'oren',
		'dialog_id': 'oren_intro_desert_primary',
		'dialog': [
			"Oh. Hello. Are you real? I'm never quite sure anymore.",
			"Mara sent you? Hm. She has a talent for sending things in the right direction at the wrong time.",
			"You want the Sundial. Of course you do. It's been waiting, I think.",
			"But first — you'll have to prove you're paying attention. The desert speaks, you know. Most people just don't listen.",
			"Three questions. Answer well, and the Sundial is yours."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'chock_oren_intro_desert_primary',
		'dialog': [
			"Three questions just to get a sundial? Fine. Let’s get this over with."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'moxie_oren_intro_desert_primary',
		'dialog': [
			"A riddle-obsessed dreamer in the desert. I already like him."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'kaera_oren_intro_desert_primary',
		'dialog': [
			"He’s testing whether we’re listening. We should answer carefully."
		]
	},
	# Oren puzzle pass/fail feedback dialogs
	{
		'npc_id': 'oren',
		'dialog_id': 'oren_puzzle_1_pass',
		'dialog': [
			"Yes… yes, that's it exactly.",
			"The wind. The desert remembers the shape of what passed through it — not the weight, not the noise. The shape.",
			"Good. You're listening. Let's continue."
		]
	},
	{
		'npc_id': 'oren',
		'dialog_id': 'oren_puzzle_2_pass',
		'dialog': [
			"A memory. Precisely.",
			"It crosses the dunes without disturbing a single grain. Leaves no trail. Casts no shadow.",
			"You're closer than most. One more."
		]
	},
	{
		'npc_id': 'oren',
		'dialog_id': 'oren_puzzle_3_pass',
		'dialog': [
			"The silence between breaths.",
			"Yes. When the sun is gone, the sundial doesn't stop — it counts the dark. The waiting. The held breath before things shift.",
			"You understand the desert. Here.",
			"Take it. It will find what it's looking for, I think."
		]
	},
	{
		'npc_id': 'oren',
		'dialog_id': 'oren_puzzle_wrong',
		'dialog': [
			"Hmm. No… that's not quite it.",
			"Don't worry. The answer isn't hiding. Just listen a little closer.",
			"Try again."
		]
	},
	{
		'npc_id': 'zaruun',
		'dialog_id': 'zaruun_intro',
		'dialog': [
			"So the witch sends another fool.",
			"The desert is thinning — can't you feel it? I merely help it shed its last illusions.",
			"Turn back, or be swallowed with the rest."
		]
	},
	# Scene: confrontation with Zaruun — Sable, Moxie, and Chock speak before the fight
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_zaruun_confrontation',
		'dialog': [
			"Zaruun. I knew we'd end up here.",
			"You're not purifying anything. You're just afraid of what the desert still holds."
		]
	},
	{
		'npc_id': 'zaruun',
		'dialog_id': 'zaruun_confrontation_reply',
		'dialog': [
			"Sable. Still selling miracles to fools who can't face the truth.",
			"The desert doesn't hold anything. It releases. That is its nature. That is its mercy."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'moxie_zaruun_taunt',
		'dialog': [
			"Mercy? You've been swallowing people whole and calling it liberation.",
			"That's not philosophy, that's a god complex with better lighting."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'chock_zaruun_challenge',
		'dialog': [
			"Enough talking. He's made his choice.",
			"Let's make ours."
		]
	},
	# Scene: after defeating Zaruun — Sable's closing, Void hint, character join
	{
		'npc_id': 'zaruun',
		'dialog_id': 'zaruun_defeat',
		'dialog': [
			"You delay the desert's truth… but the void waits beneath every grain.",
			"I can hear it. The thinning. It isn't me you should fear.",
			"Something else is already beneath the sand. Something older.",
			"You haven't stopped anything. You've just made yourself its next obstacle."
		]
	},
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_post_defeat',
		'dialog': [
			"(quiet, to herself) Something older…",
			"I've heard that before. The dunes used to make that sound — right before the first sinkholes opened.",
			"He wasn't wrong about everything. I hate that."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'moxie_post_defeat',
		'dialog': [
			"Okay, the dying villain monologue was a little on the nose.",
			"But… the part about something older. That felt real."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'chock_post_defeat',
		'dialog': [
			"Then we deal with it when it shows its face.",
			"Right now — we breathe. Then we move."
		]
	}
]


TASKS = [
	{
		'task_id': 'desert_primary_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'sable',
					'location': 'region_bar'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sable',
					'standing_text': [ 
						"The dunes are louder than usual tonight. Something's cracking open out there.",
						"I've been trying to track the source for weeks. Every time I get close, the sand shifts.",
						"If you're passing through — keep your ears open. This desert remembers things."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_primary_meet_sable'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_primary_meet_mara'
				}
			}
		]		
	},

	# Task: Meet Mara at Broker's Hideout in the desert city.
	# She points the player to Oren in Highsteeple Crossing and plants hints for his 3 riddles.
	# Kaera and Poise add their read on Mara's clues.
	{
		'task_id': 'desert_primary_meet_mara',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'mara',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'mara',
					'dialog_id': 'mara_sundial_direction'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'kaera_mara_reaction'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'poise_mara_reaction'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mara',
					'standing_text': [
						"Oren's the one you want. Highsteeple Crossing.",
						"Remember what I told you — wind, memory, silence. He'll make sense of it."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_primary_meet_oren'
				}
			}
		]
	},

	# Task: Meet Oren in Highsteeple Crossing (placed there by main story ch3).
	# Triggers the first of 3 riddle puzzles once the player speaks to him.
	{
		'task_id': 'desert_primary_meet_oren',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'oren',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sable',
					'standing_text': [
						"Mara said Oren has the Sundial. Find him in Highsteeple Crossing.",
						"I don't know much about him, but Mara trusts her contacts."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'oren',
					'dialog_id': 'oren_intro_desert_primary'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'chock_oren_intro_desert_primary'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'moxie_oren_intro_desert_primary'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'kaera_oren_intro_desert_primary'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'oren',
					'standing_text': [
						"The Sundial is yours. The desert speaks, you know, most people just don't listen."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_oren_puzzle_1'
				}
			}
		]
	},

	# Puzzle Round 1 — "What does sand remember that stone forgets?"
	# Correct answer: "The shape of the wind."
	# Hint planted by Mara: "He likes to talk about the wind — how it leaves a shape in the sand long after it's gone."
	{
		'task_id': 'desert_oren_puzzle_1',
		'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'desert_oren_puzzle_1' } }
		],
		'task_complete_events': [
						{
				'event_type': 'initiate_option_dialog',
				'params': {
					'message': (
						"Oren tilts his head, eyes unfocused. "
						"\"First question. What does sand remember that stone forgets?\""
					),
					'options': [
						("The shape of the wind.", 'desert_oren_p1_correct'),
						("Nothing. Sand forgets everything.", 'desert_oren_p1_wrong'),
						("The weight of those who crossed it.", 'desert_oren_p1_wrong'),
					]
				}
			}
		]
	},
	{
		'task_id': 'desert_oren_p1_correct',
		'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'desert_oren_p1_correct' } }
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'oren',
					'dialog_id': 'oren_puzzle_1_pass'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_oren_puzzle_2'
				}
			}
		]
	},
	{
		'task_id': 'desert_oren_p1_wrong',
		'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'desert_oren_p1_wrong' } }
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'oren',
					'dialog_id': 'oren_puzzle_wrong'
				}
			},			
            { 'event_type': 'remove_task', 'params': { 'task_id': 'desert_oren_p1_wrong' }},			
            { 'event_type': 'remove_task', 'params': { 'task_id': 'desert_oren_puzzle_1' }},
			# loop back to the same puzzle round
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_oren_puzzle_1'
				}
			}
		]
	},

	# Puzzle Round 2 — "What walks through the desert without leaving a shadow?"
	# Correct answer: "A memory."
	# Hint planted by Mara: "He muttered something about memories casting no shadow."
	{
		'task_id': 'desert_oren_puzzle_2',
		'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'desert_oren_puzzle_2' } }
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_option_dialog',
				'params': {
					'message': (
						"Oren smiles faintly. "
						"\"Second question. What walks through the desert without leaving a shadow?\""
					),
					'options': [
						("A memory.", 'desert_oren_p2_correct'),
						("The sun.", 'desert_oren_p2_wrong'),
						("A ghost.", 'desert_oren_p2_wrong'),
					]
				}
			}
		]
	},
	{
		'task_id': 'desert_oren_p2_correct',
		'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'desert_oren_p2_correct' } }
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'oren',
					'dialog_id': 'oren_puzzle_2_pass'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_oren_puzzle_3'
				}
			}
		]
	},
	{
		'task_id': 'desert_oren_p2_wrong',
		'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'desert_oren_p2_wrong' } }
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'oren',
					'dialog_id': 'oren_puzzle_wrong'
				}
			},			
            { 'event_type': 'remove_task', 'params': { 'task_id': 'desert_oren_p2_wrong' }},			
            { 'event_type': 'remove_task', 'params': { 'task_id': 'desert_oren_puzzle_2' }},
			# loop back to the same puzzle round
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_oren_puzzle_2'
				}
			}
		]
	},

	# Puzzle Round 3 — "What does the sundial count when the sun is gone?"
	# Correct answer: "The silence between breaths."
	# Hint planted by Mara: "He was staring at a sundial in the dark, whispering about 'the silence between breaths.'"
	# Correct answer awards the dune_sundial item.
	{
		'task_id': 'desert_oren_puzzle_3',
		'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'desert_oren_puzzle_3' } }
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_option_dialog',
				'params': {
					'message': (
						"Oren holds up the Dune Sundial, watching it catch the light. "
						"\"Last question. What does the sundial count when the sun is gone?\""
					),
					'options': [
						("The silence between breaths.", 'desert_oren_p3_correct'),
						("Nothing. It stops.", 'desert_oren_p3_wrong'),
						("The stars.", 'desert_oren_p3_wrong'),
					]
				}
			}
		]
	},
	{
		'task_id': 'desert_oren_p3_correct',
		'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'desert_oren_p3_correct' } }
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'oren',
					'dialog_id': 'oren_puzzle_3_pass'
				}
			},
			# Oren gives the player the sundial — deliver it to Sable
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'dune_sundial'
				}
			}
		]
	},
	{
		'task_id': 'desert_oren_p3_wrong',
		'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'desert_oren_p3_wrong' } }
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'oren',
					'dialog_id': 'oren_puzzle_wrong'
				}
			},			
            { 'event_type': 'remove_task', 'params': { 'task_id': 'desert_oren_p3_wrong' }},			
            { 'event_type': 'remove_task', 'params': { 'task_id': 'desert_oren_puzzle_3' }},
			# loop back to the same puzzle round
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_oren_puzzle_3'
				}
			}
		]
	},

	# Task 1: Deliver the Dune Sundial to Sable at the region bar.
	# Sable, Kaera, and Kade have a scene — Sable joins the party here.
	{		
		'task_id': 'desert_primary_meet_sable',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'sable',
		'item_id': 'dune_sundial',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sable',
					'standing_text': [
						"Zaruun is out there, cracking open the desert. I need the Dune Sundial to hone in on him.",
						"He's been causing sinkholes all over the desert. Please find the Sundial."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'sable',
					'dialog_id': 'sable_intro'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'kaera_sable_join_reaction'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'kade_sable_join_reaction'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'sable',
					'dialog_id': 'sable_join'
				}
			},
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'sable'
				}
			},
			{
				'event_type': 'character_join',
				'params': {
					'character_id': 'sable'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_primary_defeat_zaruun'
				}
			}
		]
	},

	# Task 2: Meet Zaruun the Sand-Sunderer in his dungeon.
	# Scene includes Sable, Moxie, and Chock confronting him before combat.
	{
		'task_id': 'desert_primary_defeat_zaruun',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'zaruun',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'zaruun',
					'location': None
				}
			},
			{
				'event_type': 'create_dungeon',
				'params': {
							'dungeon_id': 'zaruun_lair',
								'location': 'region_open_area'
							}
						},
						{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'zaruun_lair', 'item_id': 'runic_wand', 'location': 'treasure_room' }},
						{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'zaruun_lair', 'item_id': 'duneweave_mantle', 'location': 'treasure_room' }},
						{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'zaruun_lair', 'item_id': 'mirage_crown', 'location': 'treasure_room' }},
					],
					'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'zaruun',
					'dialog_id': 'zaruun_intro'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'sable',
					'dialog_id': 'sable_zaruun_confrontation'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'zaruun',
					'dialog_id': 'zaruun_confrontation_reply'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'moxie_zaruun_taunt'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'chock_zaruun_challenge'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'zaruun',
					'standing_text': [
						"The desert is thinning. I can feel it. Zaruun is out there, cracking open the dunes.",
						"He's been causing sinkholes all over the desert. We need to stop him."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'defeat_zaruun'
				}
			}
		],
	},

	# Task 3: Defeat Zaruun the Sand-Sunderer.
	# After victory: Zaruun's Void hint, Sable/Moxie/Chock closing scene, Sable's arc resolves.
	# desert_primary_report_to_sable is removed — character join already happened in meet_sable.
	{
		'task_id': 'defeat_zaruun',
        'type': 'defeat',
        'to_type': 'mob',
		'to_id': 'zaruun_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'zaruun_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'zaruun',
					'dialog_id': 'zaruun_defeat'
				}
			},
			{ 'event_type': 'hide_npc', 'params': { 'npc_id': 'zaruun' }},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'sable',
					'dialog_id': 'sable_post_defeat'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'moxie_post_defeat'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'chock_post_defeat'
				}
			},
			{
				'event_type': 'complete_region_quest',
				'params': {
					'region_id': 'desert',
				}
			}
		]
	}
]


PRIMARY_STORY_SETTINGS = {
    'story_id': 'desert_primary_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}