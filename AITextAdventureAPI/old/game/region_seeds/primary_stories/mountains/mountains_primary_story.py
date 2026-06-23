#MOUNTAIN
# local characters:
#  Bragg - a rock tech-smith who builds golems (tech)
#
# local bad-guys:
#  ROKHULD THE CORE-BREAKER
#   A massive, hammer‑wielding brute who believes the mountain’s heart contains the world’s “true ending.”
#   He is tunneling downward to reach it.
#
#   Why he opposes Bragg:  
#    Bragg builds; Rokhuld destroys.
#    He mocks Bragg’s golems as “delaying the inevitable collapse.”
#
#   Void Hint:  
#    He claims the mountain is hollow because “something below is hungry.”
#
# dialog and story:
#
# Bragg & Rokhuld
# Protagonist Intro (Bragg → Player)
# “Ah! A traveler with working limbs. Perfect.”
#
# “Rokhuld’s smashing his way toward the mountain’s heart.
# Says the world’s ending is buried down there.”
#
# “He’s breaking my golems, my tunnels, my patience.
# Go stop him before he cracks the whole peak.”
#
# CREATE: DUNGEON
#
# Antagonist Intro (Rokhuld → Player)
# “You stand between me and truth.”
#
# “The mountain hides the world’s final breath.
# I will break it open.”
#
# Antagonist Defeat (Rokhuld → Player)
# “Stone… holds…
# for now…”
#
# Protagonist Closing (Bragg → Player)
# “Ha! You flattened him like a loose cobblestone.”
#
# “You’ve got talent.
# I’ll come along — someone needs to build things while you break them.”
#
# Reward: Bragg joins the cause.

ATTAINABLE_PLAYER_CHARACTERS = [
    #{'id': 'bragg', 'name': 'Bragg'}
    { 
        ## total power points = 15 + 15* 29  = 465
        ## total stat points = 10 + 6*29 = 184
        'id': 'bragg', 
        'name': 'Bragg',
        'head_armor': 'coresight_visor',
        'body_armor': 'forgeplate_harness',
        'arm_armor': 'shockforge_gauntlets',
        'leg_armor': 'stonebinder_greaves',
        'equipped_weapon': 'corebreaker_hammer',
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
        'abilities': ['dark_earth_electric_tech_lv3_petrifying_shock', 'earth_electric_water_tech_lv3_tectonic_current', 
                      'fire_earth_tech_lv2_forge_pulse', 'earth_earth_tech_lv2_seismic_rupture', 'electric_earth_tech_lv2_grounded_spike',
                      'fire_tech_lv1_flux_dampener', 'earth_tech_lv1_fault_inhibitor'

        ]

    }
]

NPCS = [
    {
        'npc_id': 'bragg',
        'name': 'Bragg',
        'description': (
            'A forge-breaker who survived an explosion caused by a micro-fracture—'
            'an event that killed his entire crew. He masks his fear of losing control beneath swagger and bravado.'
            ' Bragg now seeks to understand the fracture that destroyed his forge.'
        ),
        "theme_song": "One-Eyed Bastard, Green Day",
        "psychology": {
            "mbti": "ESTP",
            "dominant": "Se — Lives through action and physical force, reacting instantly to threats.",
            "auxiliary": "Ti — Breaks down problems with sharp internal logic, especially mechanical ones.",
            "tertiary": "Fe — Uses charm and bravado to influence or defuse others.",
            "inferior": "Ni — Under stress, becomes paranoid about unseen dangers or future collapse."
        },
        "enneagram": {
          "enneagram_type": "8w7",
          "core_fear": "Being controlled or harmed by forces beyond his understanding (like the fracture).",
          "core_desire": "To be in control of his own life and environment.",
          "defense_mechanism": "Denial — Uses bravado and swagger to deny his underlying fear and trauma from the explosion, projecting an image of strength.",
          "stress_line": "Moves to Type 5 — Becomes withdrawn and paranoid when his control is seriously threatened.",
          "growth_line": "Moves to Type 2 — Uses his strength to protect others, turning his trauma into a protective instinct.",
          "instinctual_variant": "sx/sp — Seeks intense challenges and confrontations to prove his strength and control."
        }
    },
    {
        'npc_id': 'rokhuld',
        'name': 'Rokhuld the Core-Breaker',
        'description': (
            'A massive, hammer‑wielding brute who believes the mountain’s heart contains the world’s “true ending.” '
            'He is tunneling downward to reach it.'
        ),
        "psychology": {
            "mbti": "ISTJ",
            "dominant": "Si — Fixated on the mountain’s ancient patterns and the ‘truth’ he believes lies beneath. He follows a rigid internal sense of duty.",
            "auxiliary": "Te — Executes his mission with relentless efficiency. He destroys anything in his way, including Bragg’s golems.",
            "tertiary": "Fi — Holds a private, warped conviction that breaking the mountain is righteous. His morality is internal and unshakeable.",
            "inferior": "Ni — The void exploits his weakest function, filling him with catastrophic visions and the belief that the mountain hides the world’s ‘final breath.’"
        },
        "enneagram": {
          "enneagram_type": "1w2",
          "core_fear": "Being corrupt or failing in his sacred duty.",
          "core_desire": "To be good and have integrity by fulfilling his perceived purpose.",
          "defense_mechanism": "Reaction Formation — Channels his fear of the world's end into a rigid, destructive quest that he believes is righteous and necessary.",
          "stress_line": "Moves to Type 4 — Becomes melancholic and withdrawn when his progress is halted.",
          "growth_line": "Moves to Type 7 — Learns to find a more flexible and less destructive purpose.",
          "instinctual_variant": "sp/so — A self-contained crusader, focused on his personal mission which he believes will save the world."
        }
    }
]

NPC_DIALOG = [
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_intro',
        'dialog': [
            "Ah! A traveler with working limbs. Perfect.",
            "Rokhuld’s smashing his way toward the mountain’s heart. Says the world’s ending is buried down there.",
            "He’s breaking my golems, my tunnels, my patience. Go stop him before he cracks the whole peak."
        ]
    },
    {
        'npc_id': 'rokhuld',
        'dialog_id': 'rokhuld_intro',
        'dialog': [
            "You stand between me and truth.",
            "The mountain hides the world’s final breath.",
            "I will break it open."
        ]
    },
    {
        'npc_id': 'rokhuld',
        'dialog_id': 'rokhuld_defeat',
        'dialog': [
            "Stone… holds… for now…"
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_closing',
        'dialog': [
            "Ha! You flattened him like a loose cobblestone.",
            "You’ve got talent. I’ll come along — someone needs to build things while you break them."
        ]
    }
]

DUNGEONS = []

TASKS = [
	{
		'task_id': 'mountains_primary_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'bragg',
					'location': 'region_bar'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'bragg',
					'standing_text': [ 
                        "Heyo! I'm Bragg, I build golems around these parts and help to stabilize the mining networks.",
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'mountains_primary_meet_bragg'
				}
			}
		]		
	},
    # Task 1: meet Bragg at region bar
    {
        'task_id': 'mountains_primary_meet_bragg',
        'type': 'deliver',
        'to_type': 'npc',
        'to_id': 'bragg',
        'item_id': 'coreforge_shard',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',# tell the players to find the coreforge shard
                'params': {
                    'npc_id': 'bragg',
                    'standing_text': [
                        "If you find a Coreforge Shard, bring it to me.",
                        "Rokhuld's on a rampage below. I him before he breaks the whole mountain!"
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bragg',
                    'dialog_id': 'bragg_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'bragg',
                    'standing_text': [
                        "Rokhuld's on a rampage below. Stop him before he breaks the whole mountain!",
                        "What a dick head. Why are you still standing around?",
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_primary_defeat_rokhuld'
                }
            }
        ]
    },

    # Task 2: meet Rokhuld in dungeon
    {
        'task_id': 'mountains_primary_defeat_rokhuld',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rokhuld',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'rokhuld_lair',
                    'location': 'region_open_area'
                }
            },
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'rokhuld',
					'location': None
				}
			}
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rokhuld',
                    'dialog_id': 'rokhuld_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'defeat_rokhuld'
                }
            }
        ]
    },

    # Task 3: defeat Rokhuld
    {
        'task_id': 'defeat_rokhuld',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'rokhuld_1',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'rokhuld_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rokhuld',
                    'dialog_id': 'rokhuld_defeat'
                }
            },
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'rokhuld' }},
			{
				'event_type': 'complete_region_quest',
				'params': {
					'region_id': 'mountains',
				}
			},
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_primary_report_to_bragg'
                }
            }
        ]
    },

    # Task 4: report back to Bragg
    {
        'task_id': 'mountain_primary_report_to_bragg',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'bragg',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bragg',
                    'dialog_id': 'bragg_closing'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'bragg'
                }
            },
            {
                'event_type': 'character_join',
                'params': {
                    'character_id': 'bragg'
                }
            }
        ]
    }
]



PRIMARY_STORY_SETTINGS = {
    'story_id': 'mountains_primary_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
    }