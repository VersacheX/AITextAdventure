#SHALLOWS
# local characters:
#  Ripple - Well respected and known Tide Oracle (faith)
#
# local bad-guys:
#  UUL’THAR THE TIDE‑WAKENED  
#   A deep‑sea eldritch horror, a fragment of something older than the world.
#   Its presence warps tides, gravity, and the behavior of water itself.
#
#   Why it opposes Ripple:
#    Ripple interprets the tides; Uul’thar rewrites them and wants her silenced.
#
#   Void Hint:
#    It whispers that “the sea remembers the before… and soon, the after.”
#
# dialog and story:
#
# Ripple & Uul’thar
# Protagonist Intro (Ripple → Player)
# “Traveler… the tides are trembling.”
#
# “Something ancient rose from the trench — Uul’thar.
# It bends the sea like wet parchment.”
#
# “I cannot calm the waters while it exists.
# Please… descend and end it.”
#
# CREATE: DUNGEON
#
# Antagonist Intro (Uul’thar → Player)
# “Small thing… walking on borrowed water.”
#
# “The sea remembers the before.
# I will show it the after.”
#
# Antagonist Defeat (Uul’thar → Player)
# “The deep… still… calls…”
#
# Protagonist Closing (Ripple → Player)
# “The tides breathe again.
# Thank you.”
#
# “I will walk with you now.
# The void’s whispers grow louder.”
#
# Reward: Ripple joins the cause.

ATTAINABLE_PLAYER_CHARACTERS = [
    #{'id': 'ripple', 'name': 'Ripple'},
    { 
        ## total power points = 15 + 15* 29  = 465
        ## total stat points = 10 + 6*29 = 184
        'id': 'ripple', 
        'name': 'Ripple',
        'head_armor': 'tidecaller_veil',
        'body_armor': 'abyssal_flow_robe',
        'arm_armor': 'currentweaver_bracers',
        'leg_armor': 'tidebound_greaves',
        'equipped_weapon': 'moontide_staff',
        'max_hp': 1019, # 20 + 20 * 29 = 600            + 365
        'current_hp': 1019,
        'max_ap': 400, # 5 + 5 * 29 = 150              + 100
        'current_ap': 400,
        'unused_ability_slots': 0,
        'unused_stat_points': 0,
        'unused_power_points': 0,
        'strength': 38,                                # +120
        'dexterity': 38,        
        'intelligence':158,
        'constitution': 102,                            # + 64
        'level': 30,
        'abilities': ['light_light_dark_faith_lv3_dusk_balm', 'water_water_water_faith_lv3_poseidon_wrath', 
                      'water_light_faith_lv2_holy_fountain', 'air_water_faith_lv2_mute_cleansing', 'water_water_faith_lv2_deluge_benedict',
                      'light_faith_lv1_minor_heal', 'water_faith_lv1_mending_streams'

        ]

    }
]
"""
Ripple Character Review
Overall Verdict: 8.4 / 10 – Good foundation with room to shine more.
Ripple has a clear, ethereal voice that fits the mystical side of the party. She serves as a calm, empathetic counterbalance to more chaotic or analytical members like Moxie, Grimnaw, and Kade.
How Well She Matches Her Base (INFJ 9w1)
Strong Matches:

Ni + Fe: Her lines focus on symbolic patterns in tides, emotions, and the world’s collapse. She speaks with quiet empathy and a desire for harmony.
Dissociation & Trauma: The drowning backstory is well implied in her fear of deep water and her role as a “tide oracle who returned changed.”
Peace-Seeking 9w1: Calm, soothing presence. She wants to calm the waters (literal and metaphorical).

Current Lines (Shallows Arc):

“Traveler… the tides are trembling.”
“Something ancient rose from the trench — Uul’thar. It bends the sea like wet parchment.”
“I cannot calm the waters while it exists. Please… descend and end it.”
“The tides breathe again. Thank you.”
“I will walk with you now. The void’s whispers grow louder.”

These are solid and atmospheric, but they lean a bit generic.
Strengths

Ethereal, mystical tone that feels distinct.
Good thematic tie-in with water, collapse, and emotional tides.
Her joining the party feels natural (she needs help with Uul’thar and then offers to travel with the group).

Areas for Improvement
1. More Distinct Voice
Her current lines are calm and poetic, but could lean harder into her trauma and unique perspective.
2. Show the Internal Conflict
As someone who drowned and returned changed, she should have subtle hints of fear or dissociation, especially around water or overwhelming chaos.
3. Stronger Party Integration
After joining, she fades into the background. Give her more reactive lines in later chapters.

Suggested Line Improvements
Shallows Arc (Meet Ripple):

Ripple: (voice soft, almost whispering) Traveler… the tides are trembling. Something ancient stirs in the trench. Uul’thar… it bends the sea like wet parchment. I feel it in my bones — the same cold that once pulled me under.

After Defeating Uul’thar:

Ripple: (breathing shakily, eyes distant) The tides breathe again… Thank you. For a moment I feared I would drown in that pressure once more.

When Joining the Party:

Ripple: I will walk with you now. The void’s whispers grow louder… but so does the current of your choices. Perhaps together we can keep the waters from swallowing everything.

Later Game Example (Chapter 19 or 21):

Ripple: (softly, almost to herself) The world is forgetting how to hold itself together… just like the sea forgot how to hold me.


Final Thoughts
Ripple has strong potential as the party’s emotional/mystical compass. She just needs a bit more personal texture — her trauma, her dissociation, and her quiet hope for peace should shine through more clearly.
"""

NPCS = [
    {
        'npc_id': 'ripple',
        'name': 'Ripple',        
        'description': (
            'A tide oracle who drowned during the first Fracture wave—'
            'and returned changed. She now fears deep water even as she channels its power.'
            ' Ripple believes the party stands at the center of the next collapse.'
        ),
        "theme_song": "We Move Lightly, Dustin O'Halloran",
        "psychology": {
            "mbti": "INFJ",
            "dominant": "Ni — Perceives symbolic patterns in tides, emotions, and collapse events.",
            "auxiliary": "Fe — Guides others with quiet empathy and emotional clarity.",
            "tertiary": "Ti — Analyzes metaphysical structures with internal precision.",
            "inferior": "Se — Overwhelmed by sensory chaos, especially water-related trauma."
        },
        "enneagram": {
          "enneagram_type": "9w1",
          "core_fear": "Conflict, fragmentation, and being overwhelmed by the chaotic world.",
          "core_desire": "To have inner and outer peace.",
          "defense_mechanism": "Dissociation — Mentally withdraws from her own trauma (drowning) and the chaotic world, adopting a calm, detached persona.",
          "stress_line": "Moves to Type 6 — Becomes anxious and fearful when her peace is disturbed or she is forced to confront her trauma.",
          "growth_line": "Moves to Type 3 — Becomes more assertive and engaged, using her powers with purpose.",
          "instinctual_variant": "sp/so — Seeks personal peace and comfort, while gently trying to bring harmony to the world around her."
        },
        'image': 'ripple1.jpeg'
    },
    {
        'npc_id': 'uulthar',
        'name': 'Uul’thar the Tide‑Wakened',
        'description': (
            'A deep‑sea eldritch horror, a fragment of something older than the world.'
            ' Its presence warps tides, gravity, and the behavior of water itself.'
        ),
        "psychology": {
            "mbti": "INTP",
            "dominant": "Ti — Rewrites the rules of tides and gravity with cold, alien logic. It sees natural laws as editable structures.",
            "auxiliary": "Ne — Perceives countless possible configurations of water, pressure, and void‑geometry.",
            "tertiary": "Si — Remembers the ‘before’ — ancient patterns of the world long forgotten by mortals.",
            "inferior": "Se — Its physical manifestation distorts reality; sensory presence becomes overwhelming and unstable."
        },
        "enneagram": {
          "enneagram_type": "5w4",
          "core_fear": "Being overwhelmed or invaded by a world it doesn't understand.",
          "core_desire": "To understand the universe on its own terms.",
          "defense_mechanism": "Isolation — Remains detached and hidden in the depths, observing and manipulating reality from a safe distance.",
          "stress_line": "Moves to Type 7 — Its actions become chaotic and unpredictable when its sanctuary is breached.",
          "growth_line": "Moves to Type 8 — Manifests its power directly and confidently to reshape the world.",
          "instinctual_variant": "sp/sx — A reclusive being focused on its own understanding and survival, interacting with the world only through intense, focused manipulations."
        }
    }
]

NPC_DIALOG = [
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_intro',
        'dialog': [
            "Traveler… the tides are trembling.",
            "Something ancient rose from the trench — Uul’thar. It bends the sea like wet parchment.",
            "I cannot calm the waters while it exists. Please… descend and end it."
        ]
    },
    {
        'npc_id': 'uulthar',
        'dialog_id': 'uulthar_intro',
        'dialog': [
            "Small thing… walking on borrowed water.",
            "The sea remembers the before. I will show it the after."
        ]
    },
    {
        'npc_id': 'uulthar',
        'dialog_id': 'uulthar_defeat',
        'dialog': [
            "The deep… still… calls…"
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_closing',
        'dialog': [
            "The tides breathe again. Thank you.",
            "I will walk with you now. The void’s whispers grow louder."
        ]
    }
]

DUNGEONS = []

TASKS = [
	{
		'task_id': 'shallows_primary_initialize',
		'type': 'complete_intro_story',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'ripple',
					'location': 'region_bar'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'ripple',
					'standing_text': [ 
                        "Heyyyyyy! I'm Ripple the Tide Oracle.  I interpret the movements of the sea to help guide travelers.",
                        "Do you need guidance?"
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'shallows_primary_meet_ripple'
				}
			}
		]		
	},
    # Task 1: meet Ripple at region bar
    {
        'task_id': 'shallows_primary_meet_ripple',
        'type': 'deliver',
        'to_type': 'npc',
        'to_id': 'ripple',
        'item_id': 'moontide_orb',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'ripple',
                    'standing_text': [
                        "The sea is restless... We must act swiftly.",# get the moontide orb
                        "Find me the moontide orb. "                        
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'ripple',
                    'dialog_id': 'ripple_intro'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'ripple',
                    'standing_text': [
                        "The sea is restless... We must act swiftly.",
                        "Uul’thar must be stopped before it rewrites the tides forever."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_primary_defeat_uulthar'
                }
            }
        ]
    },

    # Task 2: meet Uul’thar in dungeon
    {
        'task_id': 'shallows_primary_defeat_uulthar',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'uulthar',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'uulthar_lair',
                    'location': 'region_open_area'
                }
            },
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'uulthar',
					'location': None
				}
			}
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'uulthar',
                    'dialog_id': 'uulthar_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'defeat_uulthar'
                }
            }
        ]
    },

    # Task 3: defeat Uul’thar
    {
        'task_id': 'defeat_uulthar',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'uulthar_1',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'uulthar_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'uulthar',
                    'dialog_id': 'uulthar_defeat'
                }
            },
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'uulthar' }},
			{
				'event_type': 'complete_region_quest',
				'params': {
					'region_id': 'shallows',
				}
			},
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_primary_report_to_ripple'
                }
            }
        ]
    },

    # Task 4: report back to Ripple
    {
        'task_id': 'shallows_primary_report_to_ripple',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'ripple',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'ripple',
                    'dialog_id': 'ripple_closing'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {
                    'npc_id': 'ripple'
                }
            },
            {
                'event_type': 'character_join',
                'params': {
                    'character_id': 'ripple'
                }
            }
        ]
    }
]


PRIMARY_STORY_SETTINGS = {
    'story_id': 'shallows_primary_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
    }