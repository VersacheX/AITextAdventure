# #DESERT
# local characters:
#  Sable - Sand witch that sells miracles (magic)
# local bad-guys:
#  ZARUUN THE SAND-SUNDERER
#   A towering warlock wrapped in cracked sandstone armor.
#   He believes the desert must “return to emptiness” and is actively collapsing dunes, oases, and ruins into sinkholes.

#   Why he opposes Sable:  
#    He thinks Sable’s “miracles” interfere with the desert’s “true destiny” — dissolution.

#   Void Hint:  
#    He claims he can hear the world thinning beneath the sand.

# dialog and story:

# Sable & Zaruun
# Protagonist Intro (Sable → Player)
# “Well now… you look like someone who can handle a little sandstorm of trouble.
# Zaruun’s been cracking the desert open again — sinkholes, screaming dunes, the whole mess.”

# “He thinks the desert wants to return to emptiness.
# I think he’s an idiot with an ego.”

# “Go knock some sense into him before he hollows the whole region.”

# CREATE: DUNGEON

# Antagonist Intro (Zaruun → Player)
# “So the witch sends another fool.
# The desert is thinning — can’t you feel it?
# I merely help it shed its last illusions.”

# “Turn back, or be swallowed with the rest.”

# Antagonist Defeat (Zaruun → Player)
# “You delay the desert’s truth…
# but the void waits beneath every grain.”

# Protagonist Closing (Sable → Player)
# “Well done, traveler.
# Zaruun’s gone, and the desert can breathe again — for now.”

# “You’ve got grit. I like that.
# I’ll tag along. Someone needs to keep you alive.”

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

“Someone who still has their head on straight? I’ll take it.”
“Another city, another storm. This is never going to end, is it?”

She guides the group’s emotional tone, especially in collapse-heavy chapters.

Auxiliary Ni — Pattern intuition
She senses deeper metaphysical patterns:

“This… this is what the desert warned me about.”
“Everything screaming for your eyes.”

Her Ni is symbolic, prophetic, and tied to the desert’s shifting nature.

Tertiary Se — Decisive action
She acts with confidence and flair:

“One more step closer to understanding what’s tearing the world apart.”

She’s grounded in the moment, especially in combat or crisis.

Inferior Ti — Sharp, cutting logic under stress
When overwhelmed, she becomes biting, critical, and surgical:

“This place is devouring people whole. We can’t let it keep winning.”

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
Sable’s role is enormous — even if subtle.

1. She is the party’s emotional stabilizer.
When others spiral, she grounds them.

2. She is the thematic mirror of the world’s collapse.
She failed to save a caravan.
The world is failing to save itself.
Her grief is the world’s grief.

3. She is the “miracle seller” who no longer believes in miracles.
This is one of the strongest character contradictions in your entire cast.

4. She is the desert’s voice.
Her intuition ties directly into the Void’s influence beneath the dunes.

5. She is the emotional counterpoint to characters like Moxie and Kade.
Where they are chaotic or analytical, she is empathetic and symbolic.

🎤 Current Lines (from your document)
“I don’t like this… feels like the air itself is lying to us.”
“This… this is what the desert warned me about.”
“Another city, another storm. This is never going to end, is it?”
“One more step closer to understanding what’s tearing the world apart.”
“Ember would be proud.”

These lines are excellent — but they can be sharpened to reveal:

her grief

her guilt

her intuition

her symbolic connection to collapse

her emotional leadership

her buried trauma

✨ Suggested Enhanced Lines (In-Character)
Act III – Glamour’s City
Sable: (quiet, uneasy) The air’s lying. The desert taught me that feeling — when reality starts to slip sideways.
Sable: This place screams for your eyes. It’s the same hunger the dunes had before the sink swallowed them.

Act IV – Stigma’s City
Sable: Masks and miracles… both are lies people cling to when the truth hurts too much.
Sable: I used to sell hope. Now I just try to keep people from drowning in it.

Act V – Fall of the Mind
Sable: (softly) The world feels like the dunes before the collapse. Too quiet. Too heavy.
Sable: I hear echoes under the sand again. I thought they were gone.

Act VI – Fall of Existence
Sable: I couldn’t save the caravan. I couldn’t save the dunes.
Sable: But I can save this. I have to.

🧩 Where Sable Can Shine Later
1. When the party faces Lament
Sable should feel the grief loops more deeply than others.

2. When corruption spreads across cities
She should compare it to the desert’s collapse.

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

She is the heart of the party — even when she doesn’t believe she deserves to be.
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
			"auxiliary": "Ni — Senses deeper patterns in the desert’s shifting nature and the Void’s influence beneath it.",
			"tertiary": "Se — Acts decisively in the moment, using her magic with flair and confidence.",
			"inferior": "Ti — Under stress, becomes sharply critical, dissecting others’ logic with biting precision."
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
			"dominant": "Ni — Interprets the desert’s decay as destiny. He sees a singular future: dissolution, emptiness, and the stripping away of illusion.",
			"auxiliary": "Te — Executes his vision with ruthless efficiency, collapsing structures and reshaping the land to match his ideology.",
			"tertiary": "Fi — Holds a deeply personal, almost spiritual conviction about the desert’s ‘true nature.’ His morality is internal and unshakeable.",
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
			"Zaruun’s been cracking the desert open again — sinkholes, screaming dunes, the whole mess.",
			"He thinks the desert wants to return to emptiness. I think he’s an idiot with an ego.",
			"Go knock some sense into him before he hollows the whole region."
		]
	},
	# TDU: add dialog for meeting Mara for sundial task chain and oren
	{
		'npc_id': 'zaruun',
		'dialog_id': 'zaruun_intro',
		'dialog': [
			"So the witch sends another fool.",
			"The desert is thinning — can’t you feel it? I merely help it shed its last illusions.",
			"Turn back, or be swallowed with the rest."
		]
	},
	# TDU ADD MORE DIALOG BETWEEN the 5 main characters, sable and zaruun
	{
		'npc_id': 'zaruun',
		'dialog_id': 'zaruun_defeat',
		'dialog': [
			"You delay the desert’s truth… but the void waits beneath every grain."
		]
	},
	# TDU ADD MORE DIALOG BETWEEN the 5 main characters, sable and zaruun
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_closing',
		'dialog': [
			"Well done, traveler. Zaruun’s gone, and the desert can breathe again — for now.",
			"You’ve got grit. I like that. I’ll tag along. Someone needs to keep you alive."
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
			}
			# TDU (TODO DESERT UPGRADE): add award task meet mara for sundial task chain
		]		
	},
	# TDU: add task for meeting Mara for sundial task chain
	# TDU: follow documentation in D:\dev\source\repos\AITextAdventure\AITextAdventureAPI\old\STORY DOCUMENTS FOR AI\Regional_Stories_Ideas.md
	# TDU: add task for meeting oren, also task trees in order to complete the 3 option dialog puzzles
	# TDU: on the correct 3rd choice award sundial
	# TDU: DO NOT TOUCH ANY THING ELSE IN THE TASKS
	# Task 1: meet Sable at region bar coordinates
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
						"I've heard he’s holed up somewhere in the desert nearby. Be careful."
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