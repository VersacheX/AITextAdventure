#GRASSLAND
# local characters:
#  Nia - A rebellious wind-dancer (skill)
#
# local bad-guys:
#  SERENE THE WHISPER-THIEF
#   A masked nomad who steals voices, secrets, and future echoes carried by the wind.
#   She uses them to manipulate events before they happen.
#
#   Why she opposes Nia:  
#    Nia dances with the wind; Serene controls it.
#    She sees Nia as a threat to her monopoly on foresight.
#
#   Void Hint:  
#    She warns that the wind is “running out of tomorrows.”
#
# dialog and story:
#
# Nia & Serene
# Protagonist Intro (Nia → Player)
# “Hey stranger! You hear that? The wind’s whispering wrong.”
#
# “Serene’s been stealing voices and future‑echoes again.
# She thinks she owns the wind.”
#
# “I need someone who can shut her down before she steals tomorrow entirely.”
#
# CREATE: DUNGEON
#
# Antagonist Intro (Serene → Player)
# “A new voice approaches… I’ll take it.”
#
# “The wind has no future left — only what I choose.”
#
# Antagonist Defeat (Serene → Player)
# “My echoes… scattered… tomorrow slips away…”
#
# Protagonist Closing (Nia → Player)
# “Nice work! The wind sounds like itself again.”
#
# “You’re fun. I’m coming with you.
# Someone has to keep the future interesting.”
#
# Reward: Nia joins the cause.

ATTAINABLE_PLAYER_CHARACTERS = [
    #{'id': 'nia', 'name': 'Nia'}
    { 
        ## total power points = 15 + 15* 29  = 465
        ## total stat points = 10 + 6*29 = 184
        'id': 'nia', 
        'name': 'Nia',
        'arm_armor': 'stormstep_bracers',
        'head_armor': 'zephyr_hood',
        'body_armor': 'galestride_vest',
        'leg_armor': 'windrunner_greaves',
        'equipped_weapon': 'whisperwind_blades',
        'max_hp': 941, # 20 + 20 * 29 = 600            + 365
        'current_hp': 941,
        'max_ap': 350, # 5 + 5 * 29 = 150              + 100
        'current_ap': 350,
        'unused_ability_slots': 0,
        'unused_stat_points': 0,
        'unused_power_points': 0,
        'strength': 38,                                # +120
        'dexterity': 224,        
        'intelligence':38,
        'constitution': 38,                            # + 64
        'level': 30,
        'abilities': ['air_air_air_skill_lv3_gale_slash', 'air_earth_electric_skill_lv3_gale_shockwave', 
                      'air_dark_skill_lv2_gale_of_doubt', 'air_light_skill_lv2_dawn_cut', 'air_air_skill_lv2_gust_blitz',
                      'air_skill_lv1_smoke_bomb', 'electric_skill_lv1_lightning_strike'

        ]

    }
]

NPCS = [
    {
        'npc_id': 'nia',
        'name': 'Nia',
        'description': (
            'A rebellious wind-dancer who once heard a future echo of her own death—'
            'a moment that has not yet occurred. She hides her fear beneath bright energy and motion,'
            ' dancing through danger with instinctive grace. She believes the party is tied to the echo she heard.'
        ),
        "theme_song": "Dog Days Are Over — Florence & The Machine",
        "psychology": {
            "mbti": "ENFP",
            "dominant": "Ne — Reads the wind like a stream of possibilities, sensing shifts and future echoes.",
            "auxiliary": "Fi — Acts from personal conviction and emotional authenticity.",
            "tertiary": "Se — Moves with physical spontaneity, reacting instantly to danger.",
            "inferior": "Te — Under stress, becomes scattered or overly reactive, struggling to impose structure."
        },
        "enneagram": {
          "enneagram_type": "7w6",
          "core_fear": "Being trapped by her fate or in emotional pain.",
          "core_desire": "To stay free and happy, outrunning the future she fears.",
          "defense_mechanism": "Rationalization — Stays in constant motion and maintains a bright, energetic exterior to avoid confronting the fear of her prophesied death.",
          "stress_line": "Moves to Type 1 — Becomes rigid and anxious when she feels her fate closing in.",
          "growth_line": "Moves to Type 5 — Becomes more introspective and able to confront her fears with wisdom instead of just motion.",
          "instinctual_variant": "sx/so — Seeks intense experiences and connections, using her energy to engage with the world and keep fear at bay."
        }
    },
    {
        'npc_id': 'serene',
        'name': 'Serene the Whisper-Thief',
        'description': (
            'A masked nomad who steals voices, secrets, and future echoes carried by the wind. '
            'She uses them to manipulate events before they happen.'
        ),
        "psychology": {
            "mbti": "INTJ",
            "dominant": "Ni — Sees the wind as a timeline to be harvested. She interprets future echoes as threads she can pull or sever.",
            "auxiliary": "Te — Executes her foresight with cold precision, stealing voices and secrets to maintain control over outcomes.",
            "tertiary": "Fi — Holds a private, warped sense of righteousness. She believes she alone is worthy to shape tomorrow.",
            "inferior": "Se — When destabilized, she becomes overwhelmed by sensory chaos, losing control of the wind she normally commands."
        },
        "enneagram": {
          "enneagram_type": "5w6",
          "core_fear": "Being helpless or incapable of controlling her destiny.",
          "core_desire": "To be capable and competent by mastering the future.",
          "defense_mechanism": "Isolation — Detaches from the world to observe and collect information (voices, secrets), finding safety in knowledge and foresight.",
          "stress_line": "Moves to Type 7 — Becomes scattered and reckless when her plans are disrupted.",
          "growth_line": "Moves to Type 8 — Uses her knowledge to take decisive, powerful action in the world.",
          "instinctual_variant": "sp/so — Hoards secrets for her own security, using them to manipulate the social landscape from a distance."
        }
    }
]

NPC_DIALOG = [
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_intro',
        'dialog': [
            "Hey stranger! You hear that? The wind’s whispering wrong.",
            "Serene’s been stealing voices and future‑echoes again. She thinks she owns the wind.",
            "I need someone who can shut her down before she steals tomorrow entirely."
        ]
    },
    {
        'npc_id': 'serene',
        'dialog_id': 'serene_intro',
        'dialog': [
            "A new voice approaches… I’ll take it.",
            "The wind has no future left — only what I choose."
        ]
    },
    {
        'npc_id': 'serene',
        'dialog_id': 'serene_defeat',
        'dialog': [
            "My echoes… scattered… tomorrow slips away…"
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_closing',
        'dialog': [
            "Nice work! The wind sounds like itself again.",
            "You’re fun. I’m coming with you. Someone has to keep the future interesting."
        ]
    }
]

DUNGEONS = []

TASKS = [
	{
		'task_id': 'grassland_primary_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'nia',
					'location': 'region_bar'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'nia',
					'standing_text': [ 
                        "Hey stranger! I'm Nia, I like to dance with the wind and go with the natural flow.",
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'grassland_primary_meet_nia'
				}
			}
		]		
	},
    # Task 1: meet Nia at region bar
    {
        'task_id': 'grassland_primary_meet_nia',
        'type': 'deliver',
        'to_type': 'npc',
        'to_id': 'nia',
        'item_id': 'heirloom_ring',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'nia',
                    'standing_text': [
                        "Hey stranger! You look like someone who can handle themselves.",
                        "The wind feels... off. Like it's carrying whispers of things yet to come.",
                        "If you're up for an adventure, find me the Heirloom Ring."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'nia',
                    'dialog_id': 'nia_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'nia',
                    'standing_text': [
                        "The wind feels... unsettled. Serene is at it again.",
                        "We need to stop her before she steals tomorrow entirely.",
                        "Can you help me track her down?"
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_primary_defeat_serene'
                }
            }
        ]
    },

    # Task 2: meet Serene in dungeon
    {
        'task_id': 'grassland_primary_defeat_serene',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'serene',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'serene_lair',
                    'location': 'region_open_area'
                }
            },
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'serene',
					'location': None
				}
			}
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'serene',
                    'dialog_id': 'serene_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'defeat_serene'
                }
            }
        ]
    },

    # Task 3: defeat Serene
    {
        'task_id': 'defeat_serene',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'serene_1',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'serene_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'serene',
                    'dialog_id': 'serene_defeat'
                }
            },
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'serene' }},
            {
				'event_type': 'complete_region_quest',
				'params': {
					'region_id': 'grassland',
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_primary_report_to_nia'
                }
            }
        ]
    },

    # Task 4: report back to Nia
    {
        'task_id': 'grassland_primary_report_to_nia',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'nia',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'nia',
                    'dialog_id': 'nia_closing'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'nia'
                }
            },
            {
                'event_type': 'character_join',
                'params': {
                    'character_id': 'nia'
                }
            }
        ]
    }
]



PRIMARY_STORY_SETTINGS = {
    'story_id': 'grassland_primary_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
    }