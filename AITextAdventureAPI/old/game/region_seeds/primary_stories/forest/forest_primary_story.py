#FOREST
# local characters:
#  Thorn - gruff half-feral forest guardian (technique)
#
# local bad-guys:
#  ELDER Marrowroot
# A druid who fused with a void‑scarred world‑tree, becoming a monstrous prophet of “the coming stillness.”
# he wants to convert humanity to fuse with void touched trees to survice and is corrupting the forest to build an army

# Why he opposes Thorn
# Thorn wishes to protect the forest and those within it.
# Marrowroot wants to corrupt.

# Thorn is feral instinct.
# Marrowroot is void‑driven purpose.

# Void Hint
# He claims:
# “The roots touched the void… and the void touched back.”
# He hears whispers from beneath the world, urging him to “prepare the forest for its next form.”
#
# dialog and story:
#
# Thorn & Marrowroot
# Protagonist Intro (Thorn → Player)
# “You. Outsider. Good. Need help.”
#
# “Marrowroot’s ripping up roots, screaming about the ‘approaching edge.’
# Forest’s scared. I’m angry.”
#
# “Go into his grove. Break him.
# Before he uproots the whole region.”
#
# CREATE: DUNGEON
#
# Antagonist Intro (Marrowroot → Player)
# “You walk where roots recoil.”
#
# “The void touches the world.
# I will pull the forest back before it is devoured.”
#
# Antagonist Defeat (Marrowroot → Player)
# “The roots… still feel it…
# the edge…”
#
# Protagonist Closing (Thorn → Player)
# “He’s gone. Forest calmer now.”
#
# “You strong. I follow.
# World needs guarding.”
#
# Reward: Thorn joins the cause.

ATTAINABLE_PLAYER_CHARACTERS = [
    #{'id': 'thorn', 'name': 'Thorn'}
    { 
        ## total power points = 15 + 15* 29  = 465
        ## total stat points = 10 + 6*29 = 184
        'id': 'thorn', 
        'name': 'Thorn',
        'arm_armor': 'thornbound_gauntlets',
        'head_armor': 'barkhide_helm',
        'body_armor': 'heartwood_carapace',
        'leg_armor': 'rootwalker_greaves',
        'equipped_weapon': 'wildroot_fangblade',
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
        'abilities': ['earth_earth_earth_technique_lv3_earthshaker', 'light_earth_water_technique_lv3_solar_haven', 
                      'earth_water_technique_lv2_mire_cleave', 'earth_earth_technique_lv2_terra_slam', 'earth_light_technique_lv2_rally_up',
                      'earth_technique_lv1_armor_up', 'air_technique_lv1_sonic_strike'

        ]

    }
]

NPCS = [
    {
        'npc_id': 'thorn',
        'name': 'Thorn',
        'description': (
            'A half-feral forest guardian who once raised a great beast from a cub—'
            'only to be forced to mercy-kill it when corruption overtook the woods.'
            ' He acts detached and instinctive, but his loyalty runs deep and painful.'
            ' Thorn senses the same corruption spreading far beyond the forest.'
        ),
        "theme_song": "Way Down We Go — Kaleo",
        "psychology": {
            "mbti": "ESFP",
            "dominant": "Se — Lives through raw sensation and instinct. Hyper-present, reactive, and attuned to movement, threat, and the emotional tone of the environment.",
            "auxiliary": "Fi — Holds a private, deeply personal moral code. His grief over the beast he raised is internalized, shaping fierce loyalty and protective instincts.",
            "tertiary": "Te — Surfaces in moments of crisis as cold, decisive action. When overwhelmed, he becomes brutally efficient and tactical.",
            "inferior": "Ni — Haunts him with flashes of symbolic, prophetic dread. He senses corruption spreading but cannot articulate the future it points toward."
        },
        "enneagram": {
          "enneagram_type": "8w9",
          "core_fear": "Being controlled or harmed, and failing to protect those he cares for.",
          "core_desire": "To protect himself and his domain.",
          "defense_mechanism": "Denial — Pushes away his grief and vulnerability, adopting a tough, detached exterior to maintain a sense of control.",
          "stress_line": "Moves to Type 5 — Withdraws into the forest, becoming secretive and isolated when overwhelmed by grief or threat.",
          "growth_line": "Moves to Type 2 — Uses his strength to actively protect others, channeling his pain into compassion.",
          "instinctual_variant": "sp/sx — A self-reliant protector of his territory, forming intense bonds with the few he trusts."
        }
    },
    {
        'npc_id': 'marrowroot',
        'name': 'Elder Marrowroot',
        'description': (
            'A once‑wise druid who fused with an ancient tree and became something monstrous.'
            ' He believes the forest must uproot itself and retreat from the world’s “approaching edge.”'
        ),
        "psychology": {
            "mbti": "INFJ",
            "dominant": "Ni — Interprets the void’s whispers as prophecy. He sees a singular future where the forest must transform or perish.",
            "auxiliary": "Fe — Frames his corruption as salvation, believing he is guiding the forest toward its 'next form.' He speaks in warnings and moral imperatives.",
            "tertiary": "Ti — Constructs twisted internal logic to justify his actions, rationalizing corruption as evolution.",
            "inferior": "Se — His physical form is unstable; sensory overload drives him into violent, uncontrolled bursts of void‑infused magic."
        },
        "enneagram": {
          "enneagram_type": "1w2",
          "core_fear": "Being corrupt or failing his duty to the forest.",
          "core_desire": "To be good and have integrity.",
          "defense_mechanism": "Reaction Formation — Believes his monstrous transformation is a righteous, necessary act to 'save' the forest, denying its corrupting nature.",
          "stress_line": "Moves to Type 4 — Becomes melancholic and withdrawn, lamenting the 'sacrifice' he has made.",
          "growth_line": "Moves to Type 7 — Learns to accept the world's imperfections and find a more flexible way to protect his home.",
          "instinctual_variant": "so/sp — Entirely focused on the 'salvation' of his community (the forest), sacrificing his own form for it."
        }
    }
]

NPC_DIALOG = [
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_intro',
        'dialog': [
            "You. Outsider. Good. Need help.",
            "Marrowroot’s ripping up roots, screaming about the ‘approaching edge.’ Forest’s scared. I’m angry.",
            "Go into his grove. Break him. Before he uproots the whole region."
        ]
    },
    {
        'npc_id': 'marrowroot',
        'dialog_id': 'marrowroot_intro',
        'dialog': [
            "You walk where roots recoil.",
            "The void touches the world. I will pull the forest back before it is devoured."
        ]
    },
    {
        'npc_id': 'marrowroot',
        'dialog_id': 'marrowroot_defeat',
        'dialog': [
            "The roots… still feel it… the edge…"
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_closing',
        'dialog': [
            "He’s gone. Forest calmer now.",
            "You strong. I follow. World needs guarding."
        ]
    }
]

DUNGEONS = []

TASKS = [
	{
		'task_id': 'forest_primary_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'thorn',
					'location': 'region_bar'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'thorn',
					'standing_text': [ 
                        "Heya! I Thorn. You new around here?",
                        "I am guardian forest. You be good to forest."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'forest_primary_meet_thorn'
				}
			}
		]		
	},
    # Task 1: meet Thorn at region bar
    {
        'task_id': 'forest_primary_meet_thorn',
        'type': 'deliver',
        'to_type': 'npc',
        'to_id': 'thorn',
        'item_id': 'grove_lattice',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'thorn',
                    'standing_text': [ # set npc text to roughly ask for players to find grove lattice
                        "You. Outsider. Good. Need help.",
                        "Marrowroot’s ripping up roots, screaming about ‘approaching edge.’ Forest’s scared. I’m angry.",
                        "Find me Grove Lattive to break his wards."
                    ]
                }
            
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'thorn',
                    'dialog_id': 'thorn_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'thorn',
                    'standing_text': [
                        "Marrowroot's gone mad. He's corrupts the forest. Stop him.",
                        "Whhy you wait?",
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_primary_defeat_marrowroot'
                }
            }
        ]
    },

    # Task 2: meet Marrowroot in dungeon
    {
        'task_id': 'forest_primary_defeat_marrowroot',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'marrowroot',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'marrowroot_lair',
                    'location': 'region_open_area'
                }
            },
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'marrowroot',
					'location': None
				}
			}
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'marrowroot',
                    'dialog_id': 'marrowroot_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'defeat_marrowroot'
                }
            }
        ]
    },

    # Task 3: defeat Marrowroot
    {
        'task_id': 'defeat_marrowroot',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'marrowroot_1',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'marrowroot_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'marrowroot',
                    'dialog_id': 'marrowroot_defeat'
                }
            },
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'marrowroot' } },
            {
				'event_type': 'complete_region_quest',
				'params': {
					'region_id': 'forest'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_primary_report_to_thorn'
                }
            }
        ]
    },

    # Task 4: report back to Thorn
    {
        'task_id': 'forest_primary_report_to_thorn',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'thorn',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'thorn',
                    'dialog_id': 'thorn_closing'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'thorn'
                }
            },
            {
                'event_type': 'character_join',
                'params': {
                    'character_id': 'thorn'
                }
            }
        ]
    }
]



PRIMARY_STORY_SETTINGS = {
    'story_id': 'forest_primary_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
    }