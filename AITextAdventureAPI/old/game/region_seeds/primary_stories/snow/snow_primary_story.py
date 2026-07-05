#SNOW
# local characters:
#  Kor-in - an ice trapper who lost his family (technique)
# local bad-guys:
#  LADY Aeriola Frostborn
#   An aristocratic ice‑sorceress who froze her own heart to “escape time.”
#   She wants to stop the world’s motion entirely — no thaw, no breath, no change.
#
#   Why she opposes Kor‑in:  
#    Kor‑in’s grief is a reminder of the life she abandoned; she wants him to “join the stillness.”
#
#   Void Hint:  
#    She speaks of a “final winter where nothing moves again.”
#
# dialog and story:
#
# Kor‑in & Lady Aeriola
# Protagonist Intro (Kor‑in → Player)
# “You there. You smell like warmth. Good. I need someone alive.”
#
# “Lady Aeriola froze half the valley last night.
# She wants the world still — unmoving — like a corpse.”
#
# “My family vanished in one of her frozen ‘moments.’
# End her madness before she freezes time itself.”
#
# CREATE: DUNGEON
#
# Antagonist Intro (Aeriola → Player)
# “A warm one approaches. How quaint.”
#
# “The world thrashes in chaos.
# I will quiet it.
# You will join the stillness.”
#
# Antagonist Defeat (Aeriola → Player)
# “Warmth… persists.
# The final winter… delayed.”
#
# Protagonist Closing (Kor‑in → Player)
# “She’s gone. Good.
# The snow feels honest again.”
#
# “You fight well.
# I’ll travel with you — until the world stops breathing.”
#
# Reward: Kor‑in joins the cause.

ATTAINABLE_PLAYER_CHARACTERS = [
    { 
        ## total power points = 15 + 15* 29  = 465
        ## total stat points = 10 + 6*29 = 184
        'id': 'korin', 
        'name': 'Kor-in',
        'arm_armor': 'glacial_vambraces_mk2',
        'head_armor': 'glacial_crown',
        'body_armor': 'glacial_breastplate',
        'leg_armor': 'glacial_shins_mk2',
        'equipped_weapon': 'glacial_spear',
        'max_hp': 1169, # 20 + 20 * 29 = 600            + 365
        'current_hp': 1169,
        'max_ap': 250, # 5 + 5 * 29 = 150              + 100
        'current_ap': 250,
        'unused_ability_slots': 0,
        'unused_stat_points': 0,
        'unused_power_points': 0,
        'strength': 158,                                # +120
        'dexterity': 38,        
        'intelligence':38,
        'constitution': 102,                            # + 64
        'level': 30,
        'abilities': ['dark_ice_air_technique_lv3_frost_bite_strike', 'ice_earth_water_technique_lv3_glacial_guard', 
                      'ice_earth_technique_lv2_permafrost_crush', 'ice_ice_technique_lv2_frost_smash', 'ice_air_technique_lv2_hailwind_edge',
                      'ice_light_technique_lv2_crystal_lance', 'ice_technique_lv1_frozen_slash','earth_technique_lv1_armor_up'

        ]

    }
]
"""
Kor-in & Lady Aeriola Frostborn Review
Overall Verdict: Strong potential with a compelling tragic core.
This pairing has real emotional weight. Kor-in’s quiet, grief-driven hunt against Aeriola’s cold, ideological extremism creates a classic personal vengeance vs. philosophical evil dynamic.
Kor-in Assessment
INFP 4w5 – Very Good Fit
Strengths:

Deep, internalized grief that drives him without making him overly dramatic.
Soft-spoken and gentle by nature, but becomes terrifyingly precise when confronting Aeriola’s magic — excellent use of inferior Te.
The image of him shattering ice with his bare hands to try to save his wife is powerful and memorable.

Current Lines (Snow Arc):

“You there. You smell like warmth. Good. I need someone alive.”
“Lady Aeriola froze half the valley last night. She wants the world still — unmoving — like a corpse.”
“My family vanished in one of her frozen 'moments.' End her madness before she freezes time itself.”
“She's gone. Good. The snow feels honest again.”
“You fight well. I'll travel with you — until the world stops breathing.”

These are solid, but they lean a little functional. They tell us what happened, but don’t quite let us feel the depth of his grief.
Suggestions to Deepen Him:

Lean harder into his Fi-Si loop (sacred, wordless grief tied to memories of his wife).
Show the contrast between his gentle nature and the cold precision he shows when fighting Aeriola’s magic.

Improved/Additional Lines:

Kor-in: (quiet, almost whispering) You smell like warmth… like she did. Good. I need someone still breathing.
After defeating Aeriola: Kor-in: (staring at the melting ice, voice hollow) She’s gone. The snow feels honest again… but it will never feel warm.

Lady Aeriola Frostborn Assessment
INTJ 1w9 – Excellent Antagonist
Strengths:

Clear, chilling motivation: She froze her own heart to “escape time” and now wants to impose perfect stillness on the world.
Strong philosophical conflict with the party’s themes of choice, change, and meaning.
Reaction Formation is well realized — she believes freezing everything is a righteous act of purity.

Current Concept: She’s a “titty twister” indeed — an aristocratic, cold, self-righteous villain who thinks she’s saving the world by ending it. That’s deliciously hateable.
Potential Lines for Her:

“Motion is corruption. Change is decay. Only in perfect stillness can purity endure.”
“Your warmth is a disease. I will grant you the mercy of ice.”
“Why do you fight so desperately to keep suffering? I offer an end to all of it.”


Overall Pairing Verdict
This is one of the strongest Regional Hero Arcs conceptually. The contrast between:

Kor-in’s deep, personal, human grief, and
Aeriola’s cold, ideological desire for perfect stillness

…creates excellent thematic tension.
Recommendations:

Give Kor-in 1–2 lines that show the raw pain beneath his calm exterior.
Make Aeriola’s philosophy more explicit and self-righteous in her boss fight dialogue.
Consider a quiet moment after the fight where Kor-in confronts what his vengeance actually means now that it’s done.
"""

NPCS = [
    {
        'npc_id': 'korin',
        'name': 'Kor-in',
        'description': (
            'An ice trapper whose wife was frozen alive by Lady Aeriola’s time-stopping spell.'
            ' Kor-in shattered the ice with his bare hands, but she was already gone.'
            ' He now hunts Aeriola across the frozen wilds, driven by a grief so deep it has turned silent.'
            ' Though soft-spoken and gentle by nature, he becomes terrifyingly precise when confronting anything touched by her magic.'
        ),
        "theme_song": "Far From Home (The Raven) — Sam Tinnesz",
        "psychology": {
            "mbti": "INFP",
            "dominant": "Fi — His grief is internal, sacred, and wordless. He navigates the world through personal meaning and emotional truth, even when silent.",
            "auxiliary": "Ne — Reads possibilities and hidden patterns in the frost. His mind drifts toward symbolic meaning, omens, and what *could* be.",
            "tertiary": "Si — Clings to memories of his wife: her warmth, her voice, the life they shared. These memories anchor him but also reopen wounds.",
            "inferior": "Te — Emerges as terrifying precision in battle. When triggered, he becomes cold, efficient, and ruthlessly goal-focused."
        },
        "enneagram": {
          "enneagram_type": "4w5",
          "core_fear": "Having no identity or significance outside of his grief.",
          "core_desire": "To find himself and his significance through his quest for vengeance.",
          "defense_mechanism": "Introjection — Has fully absorbed his grief and loss, making it the core of his identity and the driver of all his actions.",
          "stress_line": "Moves to Type 2 — Becomes overly helpful or dependent on the party when his quest falters.",
          "growth_line": "Moves to Type 1 — Finds a new, principled purpose beyond his personal grief, fighting for a greater good.",
          "instinctual_variant": "sx/sp — His entire being is focused on an intense, all-consuming quest tied to the person he lost."
        }
    },
    {
        'npc_id': 'aeriola',
        'name': 'Lady Aeriola Frostborn',
        'description': (
            'An aristocratic ice‑sorceress who froze her own heart to “escape time.” '
            'She wants to stop the world’s motion entirely — no thaw, no breath, no change.'
        ),
        "psychology": {
            "mbti": "INTJ",
            "dominant": "Ni — Envisions a 'final winter' where time stops and all motion ceases. She interprets stillness as purity and truth.",
            "auxiliary": "Te — Executes her vision with ruthless precision, freezing valleys and halting time in localized 'moments.'",
            "tertiary": "Fi — Her emotions are not gone; they are locked away. Her morality is twisted into a belief that stillness is salvation.",
            "inferior": "Se — Overwhelmed by the chaos of life and sensation, she rejects the physical world entirely, freezing it to maintain control."
        },
        "enneagram": {
          "enneagram_type": "1w9",
          "core_fear": "Being corrupt, chaotic, or flawed.",
          "core_desire": "To be good, pure, and have integrity by achieving a state of perfect stillness.",
          "defense_mechanism": "Reaction Formation — Convinces herself that her destructive act of freezing the world is a righteous and pure mission to escape the 'corruption' of time and change.",
          "stress_line": "Moves to Type 4 — Becomes melancholic and withdrawn, lamenting the 'imperfect' world that refuses to freeze.",
          "growth_line": "Moves to Type 7 — Learns to accept and even find joy in the world's natural flow and change.",
          "instinctual_variant": "sp/so — A self-contained reformer, obsessed with creating a 'perfect', unchanging environment for herself and, by extension, the world."
        }
    }
]

NPC_DIALOG = [
    {
        'npc_id': 'korin',
        'dialog_id': 'korin_intro',
        'dialog': [
            "You there. You smell like warmth. Good. I need someone alive.",
            "Lady Aeriola froze half the valley last night. She wants the world still — unmoving — like a corpse.",
            "My family vanished in one of her frozen 'moments.' End her madness before she freezes time itself."
        ]
    },
    {
        'npc_id': 'aeriola',
        'dialog_id': 'aeriola_intro',
        'dialog': [
            "A warm one approaches. How quaint.",
            "The world thrashes in chaos. I will quiet it.",
            "You will join the stillness."
        ]
    },
    {
        'npc_id': 'aeriola',
        'dialog_id': 'aeriola_defeat',
        'dialog': [
            "Warmth… persists. The final winter… delayed."
        ]
    },
    {
        'npc_id': 'korin',
        'dialog_id': 'korin_closing',
        'dialog': [
            "She's gone. Good. The snow feels honest again.",
            "You fight well. I'll travel with you — until the world stops breathing."
        ]
    }
]

DUNGEONS = []

TASKS = [
	{
		'task_id': 'snow_primary_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'korin',
					'location': 'region_bar'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'korin',
					'standing_text': [ 
                        "Ho there!  I'm Korin.  One of the best ice trappers around.  I lost my family to a psychotic sorceress a few years back",
                        "Which is why I'm always holed up in here.  If you ever hear anything about her whereabouts come let me know."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'snow_primary_meet_korin'
				}
			}
		]		
	},
    # Task 1: meet Kor-in at region bar
    {
        'task_id': 'snow_primary_meet_korin',
        'type': 'deliver',
        'to_type': 'npc',
        'to_id': 'korin',
        'item_id': 'boreal_clasp',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'korin',
                    'standing_text': [# get the boreal_clasp
                        "Aeriola is on a rampage.  I need a Boreal Clasp to break her wards."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'korin',
                    'dialog_id': 'korin_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'korin',
                    'standing_text': [
                        "The world is frozen in her grasp. We must act swiftly.",
                        "Will you help me stop Lady Aeriola?"
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_primary_defeat_aeriola'
                }
            }
        ]
    },

    # Task 2: meet Lady Aeriola in dungeon
    {
        'task_id': 'snow_primary_defeat_aeriola',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'aeriola',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'aeriola_lair',
                    'location': 'region_open_area'
                }
            },
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'aeriola',
					'location': None
				}
			}
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'aeriola',
                    'dialog_id': 'aeriola_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'defeat_aeriola'
                }
            }
        ]
    },

    # Task 3: defeat Lady Aeriola
    {
        'task_id': 'defeat_aeriola',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'aeriola_1',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'aeriola_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'aeriola',
                    'dialog_id': 'aeriola_defeat'
                }
            },
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'aeriola' }},
            {
				'event_type': 'complete_region_quest',
				'params': {
					'region_id': 'snow',
				}
			},
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_primary_report_to_korin'
                }
            }
        ]
    },

    # Task 4: report back to Kor-in
    {
        'task_id': 'snow_primary_report_to_korin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'korin',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'korin',
                    'dialog_id': 'korin_closing'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'korin'
                }
            },
            {
                'event_type': 'character_join',
                'params': {
                    'character_id': 'korin'
                }
            }
        ]
    }
]


PRIMARY_STORY_SETTINGS = {
    'story_id': 'snow_primary_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
    }