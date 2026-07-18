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
        'abilities': ['earth_earth_earth_magic_lv3_earthshaker', 'air_earth_electric_magic_lv3_gale_shock', 
                      'earth_air_magic_lv2_sandstream', 'earth_light_magic_lv2_prism_shard', 'earth_earth_magic_lv2_quake_field',
                      'earth_magic_lv1_tremor', 'light_magic_lv1_luminous_spike'

        ]

    }
]
"""
⭐ Sable Character Review
Overall Verdict: 9.4 / 10 — One of the strongest thematic characters in the cast.

Sable is a desert witch who sells miracles she no longer believes in.
That alone is a devastating character hook.

But the real brilliance is how her personality, magic, trauma, and worldview all orbit the same core truth:

She is a healer who cannot heal herself.

She guides others with charisma, insight, and emotional precision — yet she carries a grief so deep she has buried it under sand, silence, and service.

Her lines across Acts III–VI show:

quiet sorrow

sharp intuition

charismatic leadership

flashes of bitterness

deep empathy

a refusal to let the world collapse without fighting

She is the emotional backbone of the party.

🧠 MBTI Fit: ENFJ (Extremely Strong)
Dominant Fe — Emotional leadership
Sable reads people instantly and responds with emotional clarity:

"Someone who still has their head on straight? I'll take it."
"Another city, another storm. This is never going to end, is it?"

She guides the group's emotional tone, especially in collapse-heavy chapters.

Auxiliary Ni — Pattern intuition
She senses deeper metaphysical patterns:

"This… this is what the desert warned me about."
"Everything screaming for your eyes."

Her Ni is symbolic, prophetic, and tied to the desert's shifting nature.

Tertiary Se — Decisive action
She acts with confidence and flair:

"One more step closer to understanding what's tearing the world apart."

She's grounded in the moment, especially in combat or crisis.

Inferior Ti — Sharp, cutting logic under stress
When overwhelmed, she becomes biting, critical, and surgical:

"This place is devouring people whole. We can't let it keep winning."

Her Ti emerges as cold precision — a contrast to her usual warmth.

💔 Enneagram Fit: 2w3 (Perfect)
Core Fear:
Being unwanted, unworthy, or failing those who depend on her.

Core Desire:
To be needed, valued, and emotionally indispensable.

Defense Mechanism: Repression
She hides her grief — the caravan she failed to save — beneath charisma and service.

She helps others to avoid confronting her own pain.

Stress Line → Type 8
When triggered, she becomes:

controlling

aggressive

confrontational

fiercely protective

We see flashes of this in collapse-heavy chapters.

Growth Line → Type 4
When she grows, she becomes:

introspective

emotionally honest

willing to confront her grief

able to find identity beyond service

This is her true arc.

🏜️ Narrative Function: The Desert Oracle of Grief
Sable's role is enormous — even if subtle.

1. She is the party's emotional stabilizer.
When others spiral, she grounds them.

2. She is the thematic mirror of the world's collapse.
She failed to save a caravan.
The world is failing to save itself.
Her grief is the world's grief.

3. She is the "miracle seller" who no longer believes in miracles.
This is one of the strongest character contradictions in your entire cast.

4. She is the desert's voice.
Her intuition ties directly into the Void's influence beneath the dunes.

5. She is the emotional counterpoint to characters like Moxie and Kade.
Where they are chaotic or analytical, she is empathetic and symbolic.

🎤 Current Lines (from your document)
"I don't like this… feels like the air itself is lying to us."
"This… this is what the desert warned me about."
"Another city, another storm. This is never going to end, is it?"
"One more step closer to understanding what's tearing the world apart."
"Ember would be proud."

These lines are excellent — but they can be sharpened to reveal:

her grief

her guilt

her intuition

her symbolic connection to collapse

her emotional leadership

her buried trauma

✨ Suggested Enhanced Lines (In-Character)
Act III – Glamour's City
Sable: (quiet, uneasy) The air's lying. The desert taught me that feeling — when reality starts to slip sideways.
Sable: This place screams for your eyes. It's the same hunger the dunes had before the sink swallowed them.

Act IV – Stigma's City
Sable: Masks and miracles… both are lies people cling to when the truth hurts too much.
Sable: I used to sell hope. Now I just try to keep people from drowning in it.

Act V – Fall of the Mind
Sable: (softly) The world feels like the dunes before the collapse. Too quiet. Too heavy.
Sable: I hear echoes under the sand again. I thought they were gone.

Act VI – Fall of Existence
Sable: I couldn't save the caravan. I couldn't save the dunes.
Sable: But I can save this. I have to.

🧩 Where Sable Can Shine Later
1. When the party faces Lament
Sable should feel the grief loops more deeply than others.

2. When corruption spreads across cities
She should compare it to the desert's collapse.

3. When the party fractures emotionally
She should be the one who tries to hold them together — even if it hurts her.

4. When the final choice arrives
She should confront her past failure directly.

🏜️ Psychological Depth Summary
Sable is a charismatic ENFJ 2w3 desert witch whose grief, intuition, and emotional leadership form one of the strongest arcs in your entire narrative. She is:

empathetic

symbolic

wounded

charismatic

intuitive

quietly grieving

emotionally essential

She is the heart of the party — even when she doesn't believe she deserves to be.
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

NPC_DIALOG = [
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_intro',
		'dialog': [
			"Well now… you look like someone who can handle a little sandstorm of trouble.",
			"Zaruun's been cracking the desert open again — sinkholes, screaming dunes, the whole mess.",
			"He thinks the desert wants to return to emptiness. I think he's an idiot with an ego.",
			"Go knock some sense into him before he hollows the whole region."
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
	# Oren dialog — initial meeting before puzzles begin
	{
		'npc_id': 'oren',
		'dialog_id': 'oren_meeting',
		'dialog': [
			"Oh. Hello. Are you real? I'm never quite sure anymore.",
			"Mara sent you? Hm. She has a talent for sending things in the right direction at the wrong time.",
			"You want the Sundial. Of course you do. It's been waiting, I think.",
			"But first — you'll have to prove you're paying attention. The desert speaks, you know. Most people just don't listen.",
			"Three questions. Answer well, and the Sundial is yours."
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
	# TDU ADD MORE DIALOG BETWEEN the 5 main characters, sable and zaruun
	{
		'npc_id': 'zaruun',
		'dialog_id': 'zaruun_defeat',
		'dialog': [
			"You delay the desert's truth… but the void waits beneath every grain."
		]
	},
	# TDU ADD MORE DIALOG BETWEEN the 5 main characters, sable and zaruun
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_closing',
		'dialog': [
			"Well done, traveler. Zaruun's gone, and the desert can breathe again — for now.",
			"You've got grit. I like that. I'll tag along. Someone needs to keep you alive."
		]
	}
	# TDU ADD MORE DIALOG BETWEEN the 5 main characters, sable and zaruun
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
						"How's it going?  I'm Sable, the friendliest sand witch around.  I'm out here selling miracles to need.",
						"Maybe one day you'll need one of my miracles too.",
						"Maybe I'll need one from you."
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
	{
		'task_id': 'desert_primary_meet_mara',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'mara',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'mara',
					'dialog_id': 'mara_sundial_direction'
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
					'dialog_id': 'oren_meeting'
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
		'type': 'complete_intro_story',
		'task_acquire_events': [
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
		],
		'task_complete_events': []
	},
	{
		'task_id': 'desert_oren_p1_correct',
		'type': 'complete_intro_story',
		'task_acquire_events': [],
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
		'type': 'complete_intro_story',
		'task_acquire_events': [],
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
		'type': 'complete_intro_story',
		'task_acquire_events': [
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
		],
		'task_complete_events': []
	},
	{
		'task_id': 'desert_oren_p2_correct',
		'type': 'complete_intro_story',
		'task_acquire_events': [],
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
		'type': 'complete_intro_story',
		'task_acquire_events': [],
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
		'type': 'complete_intro_story',
		'task_acquire_events': [
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
		],
		'task_complete_events': []
	},
	{
		'task_id': 'desert_oren_p3_correct',
		'type': 'complete_intro_story',
		'task_acquire_events': [],
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
		'type': 'complete_intro_story',
		'task_acquire_events': [],
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

	# Task 1: Deliver the Dune Sundial to Sable at the region bar
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
		'task_complete_events': [ #< = after meeting
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'sable',
					'dialog_id': 'sable_intro'
				}
			},
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'sable',
                    'standing_text': [
						"Zaruun is still out there, cracking open the desert. Go stop him.",
						"I've heard he's holed up somewhere in the desert nearby. Be careful."
                    ]
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
	# Task 2: meet Zaruun the Sand-Sunderer in a dungeon
	{
		'task_id': 'desert_primary_defeat_zaruun',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'zaruun',
		'task_acquire_events': [
			{
				'event_type': 'create_dungeon', # <-  creating dungeon with zaruun as boss - speak to him to complete task
				'params': {
					'dungeon_id': 'zaruun_lair',
					'location': 'region_open_area'
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'zaruun',
					'location': None
				}
			}
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
				'event_type': 'award_task',
				'params': {
					'task_id': 'defeat_zaruun'
				}
			}
		],
	},
	# Task 3: defeat Zaruun the Sand-Sunderer
	{
		'task_id': 'defeat_zaruun',
        'type': 'defeat',
        'to_type': 'mob',
		'to_id': 'zaruun_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat', # <- begin combat with zaruun as boss defeating him completes event
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
				'event_type': 'complete_region_quest',
				'params': {
					'region_id': 'desert',
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'desert_primary_report_to_sable'
				}
			}
		]
	},
	# Task 4: report back to Sable at region bar
	{
		'task_id': 'desert_primary_report_to_sable',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'sable',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'sable',
					'dialog_id': 'sable_closing'
				}
			},
			#remove npc sable location (so she's not on the map)
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