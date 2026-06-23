#SWAMP
# local characters:
#  Grimnaw - Cursed Gadget dealer/collector (tech)
#
# local bad-guys:
#  LICH‑KING Miregloom  
#   A decayed sorcerer who bound his soul to the swamp’s rot to escape the world’s fate.
#   His body is a tangle of decayed flesh, bones.
#   He seeks to accelerate the world's decay by using a cursed gadget. He wishes to spread rot and death to all lands.
#   Grimnaw knows about it and the power it holds, and wants it stopped.
#
#   Void Hint:
#    He claims the swamp is “where the world will rot first when the edge arrives.”
#
# dialog and story:
#
# Grimnaw & Miregloom
# Protagonist Intro (Grimnaw → Player)
# “Heheheh! You! Yes, you’ll do nicely.”
#
# “Miregloom’s raising the dead again.
# Claims the swamp is the world’s first grave.”
#
# “He’s bad for business.
# Go knock his bones loose.”
#
# CREATE: DUNGEON
#
# Antagonist Intro (Miregloom → Player)
# “Another soul wanders into my rot.”
#
# “The world will decay soon.
# I merely begin the process.”
#
# Antagonist Defeat (Miregloom → Player)
# “Rot… postponed…”
#
# Protagonist Closing (Grimnaw → Player)
# “Hah! You did it!
# Swamp smells better already.”
#
# “I’ll tag along.
# Someone needs to keep the relics in line.”
#
# Reward: Grimnaw joins the cause.

ATTAINABLE_PLAYER_CHARACTERS = [
    #{'id': 'grimnaw', 'name': 'Grimnaw'},
    { 
        ## total power points = 15 + 15* 29  = 465
        ## total stat points = 10 + 6*29 = 184
        'id': 'grimnaw', 
        'name': 'Grimnaw',
        'head_armor': 'rotlens_goggles',
        'body_armor': 'mireforged_carapace',
        'arm_armor': 'hexsplice_gauntlets',
        'leg_armor': 'bogwalker_greaves',
        'equipped_weapon': 'cursespark_engine_rod',
        'max_hp': 941, # 20 + 20 * 29 = 600            + 365
        'current_hp': 941,
        'max_ap': 350, # 5 + 5 * 29 = 150              + 100
        'current_ap': 350,
        'unused_ability_slots': 0,
        'unused_stat_points': 0,
        'unused_power_points': 0,
        'strength': 38,                                # +120
        'dexterity': 102,        
        'intelligence':158,
        'constitution': 38,                            # + 64
        'level': 30,
        'abilities': ['dark_earth_electric_tech_lv3_petrifying_shock', 'dark_dark_dark_tech_lv3_shadow_enhancer', 
                      'ice_dark_tech_lv2_shadowfrost_emitter', 'dark_dark_tech_lv2_abyssal_core', 'dark_air_lv2_echo_displacer',
                      'fire_tech_lv1_flux_dampener', 'electric_tech_lv1_taze_charge'

        ]

    }
]



NPCS = [
    {
        'npc_id': 'grimnaw',
        'name': 'Grimnaw',
        'description': (
            'A cursed gadgeteer who once built a device that accidentally opened a micro-fracture—'
            'and something whispered back. He claims to be rational, but fears his own mind.'
            ' Grimnaw now seeks to understand the voice that answered him.'
        ),
        "theme_song": "Madness, Muse",
        "psychology": {
            "mbti": "INTP",
            "dominant": "Ti — Dissects systems and anomalies with cold internal logic.",
            "auxiliary": "Ne — Generates strange possibilities and unpredictable theories.",
            "tertiary": "Si — Recalls the whisper with obsessive clarity.",
            "inferior": "Fe — Displays unsettling emotional mimicry when destabilized."
        },
        "enneagram": {
          "enneagram_type": "5w6",
          "core_fear": "Being helpless, incapable, or overwhelmed by forces he can't understand.",
          "core_desire": "To be capable and competent by understanding the whisper.",
          "defense_mechanism": "Isolation — Detaches from his fear by treating the whisper as a purely intellectual problem to be solved, hoarding knowledge to feel safe.",
          "stress_line": "Moves to Type 7 — Becomes scattered and manic when his theories fail and his fear breaks through.",
          "growth_line": "Moves to Type 8 — Uses his knowledge to confidently confront the source of the whisper.",
          "instinctual_variant": "sp/sx — A reclusive investigator, obsessed with the intense, singular mystery that threatens his sanity."
        }
    },
    {
        'npc_id': 'miregloom',
        'name': 'Lich‑King Miregloom',
        'description': (
            'A decayed sorcerer who bound his soul to the swamp’s rot to escape the world’s fate.'
            ' His body is a tangle of roots, bones, and swamp‑fire.'
        ),
        "psychology": {
            "mbti": "INFP",
            "dominant": "Fi — Holds a deeply personal, corrupted belief that decay is purity and destiny. His morality is internal and absolute.",
            "auxiliary": "Ne — Interprets rot, death, and swamp‑whispers as cosmic signs. Sees decay as a branching future.",
            "tertiary": "Si — Clings to ancient memories of the world’s ‘fate,’ using them to justify his transformation.",
            "inferior": "Te — When destabilized, he lashes out with chaotic, uncontrolled magic, unable to structure his power."
        },
        "enneagram": {
          "enneagram_type": "4w5",
          "core_fear": "Having no identity or significance.",
          "core_desire": "To find and create a unique identity for himself, separate from the world's fate.",
          "defense_mechanism": "Introjection — Has absorbed the identity of the swamp and its decay, creating a monstrous but unique persona to escape being nothing.",
          "stress_line": "Moves to Type 2 — Becomes clingy and manipulative, trying to force others to join him in his decay.",
          "growth_line": "Moves to Type 1 — Finds a principled way to exist without needing to be defined by decay.",
          "instinctual_variant": "sp/sx — A withdrawn figure who has created an intense, all-consuming identity to preserve himself."
        }
    }
]

NPC_DIALOG = [
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_intro',
        'dialog': [
            "Heheheh! You! Yes, you’ll do nicely.",
            "Miregloom’s raising the dead again. Claims the swamp is the world’s first grave.",
            "He’s bad for business. Go knock his bones loose."
        ]
    },
    {
        'npc_id': 'miregloom',
        'dialog_id': 'miregloom_intro',
        'dialog': [
            "Another soul wanders into my rot.",
            "The world will decay soon. I merely begin the process."
        ]
    },
    {
        'npc_id': 'miregloom',
        'dialog_id': 'miregloom_defeat',
        'dialog': [
            "Rot… postponed…"
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_closing',
        'dialog': [
            "Hah! You did it! Swamp smells better already.",
            "I’ll tag along. Someone needs to keep the relics in line."
        ]
    }
]

TASKS = [
	{
		'task_id': 'swamp_primary_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'grimnaw',
					'location': 'region_bar'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'grimnaw',
					'standing_text': [ 
                        "How goes it?  I'm Grinmaw.  If it's dark twisted tech I'm about it.",
                        "It's amazing the power of the ancient."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'swamp_primary_meet_grimnaw'
				}
			}
		]		
	},
    # Task 1: meet Grimnaw at region bar
    {
        'task_id': 'swamp_primary_meet_grimnaw',
        'type': 'deliver',
        'to_type': 'npc',
        'to_id': 'grimnaw',
        'item_id': 'mirethread_pendant',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'grimnaw',
                    'standing_text': [# get the mirethread_pendant
                        "Get me the Mirethread Pendant and I can grant you access to find Miregloom."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'grimnaw',
                    'dialog_id': 'grimnaw_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_primary_defeat_miregloom'
                }
            }
        ]
    },

    # Task 2: meet Miregloom in dungeon
    {
        'task_id': 'swamp_primary_defeat_miregloom',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'miregloom',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'miregloom_lair',
                    'location': 'region_open_area'
                }
            },
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'miregloom',
					'location': None
				}
			}
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'miregloom',
                    'dialog_id': 'miregloom_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'defeat_miregloom'
                }
            }
        ]
    },

    # Task 3: defeat Miregloom
    {
        'task_id': 'defeat_miregloom',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'miregloom_1',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'miregloom_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'miregloom',
                    'dialog_id': 'miregloom_defeat'
                }
            },
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'miregloom' } },
            {
				'event_type': 'complete_region_quest',
				'params': {
					'region_id': 'swamp',
				}
			},
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_primary_report_to_grimnaw'
                }
            }
        ]
    },

    # Task 4: report back to Grimnaw
    {
        'task_id': 'swamp_primary_report_to_grimnaw',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'grimnaw',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'grimnaw',
                    'dialog_id': 'grimnaw_closing'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'grimnaw'
                }
            },
            {
                'event_type': 'character_join',
                'params': {
                    'character_id': 'grimnaw'
                }
            }
        ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'story_id': 'swamp_primary_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
    }