#SNOW
# local characters:
#  Kor-in - an ice trapper who lost his family (technique) — INFP 4w5
#
# local bad-guys:
#  LADY Aeriola Frostborn
#   An aristocratic ice-sorceress who froze her own heart to "escape time."
#   She wants to stop the world's motion entirely — no thaw, no breath, no change.
#
#   Why she opposes Kor-in:
#    Kor-in's grief is a reminder of the life she abandoned; she wants him to "join the stillness."
#
#   Void Hint:
#    She speaks of a "final winter where nothing moves again."
#
# Pregame: deliver boreal_clasp to Kor-in to break Aeriola's wards.
# character_join lives in the deliver task. report_to_kor_in removed.

ATTAINABLE_PLAYER_CHARACTERS = [
    {
        ## total power points = 15 + 15 * 29 = 465
        ## total stat points = 10 + 6 * 29 = 184
        'id': 'kor_in',
        'name': 'Kor-in',
        'arm_armor': 'glacial_vambraces_mk2',
        'head_armor': 'glacial_crown',
        'body_armor': 'glacial_breastplate',
        'leg_armor': 'glacial_shins_mk2',
        'equipped_weapon': 'glacial_spear',
        'max_hp': 1169,
        'current_hp': 1169,
        'max_ap': 250,
        'current_ap': 250,
        'unused_ability_slots': 0,
        'unused_stat_points': 0,
        'unused_power_points': 0,
        'strength': 158,
        'dexterity': 38,
        'intelligence': 38,
        'constitution': 102,
        'level': 30,
        'abilities': [
            'dark_ice_air_technique_lv3_frost_bite_strike',
            'ice_earth_water_technique_lv3_glacial_guard',
            'ice_earth_technique_lv2_permafrost_crush',
            'ice_ice_technique_lv2_frost_smash',
            'ice_air_technique_lv2_hailwind_edge',
            'ice_light_technique_lv2_crystal_lance',
            'ice_technique_lv1_frozen_slash',
            'earth_technique_lv1_armor_up',
        ]
    }
]

NPCS = [
    {
        'npc_id': 'kor_in',
        'name': 'Kor-in',
        'description': (
            'An ice trapper whose wife was frozen alive by Lady Aeriola\'s time-stopping spell.'
            ' Kor-in shattered the ice with his bare hands, but she was already gone.'
            ' He now hunts Aeriola across the frozen wilds, driven by a grief so deep it has turned silent.'
            ' Though soft-spoken and gentle by nature, he becomes terrifyingly precise when confronting anything touched by her magic.'
        ),
        "theme_song": "Far From Home (The Raven) — Sam Tinnesz",
        "psychology": {
            "mbti": "INFP",
            "dominant": "Fi — His grief is internal, sacred, and wordless. He navigates the world through personal meaning and emotional truth, even when silent.",
            "auxiliary": "Ne — Reads possibilities and hidden patterns in the frost. His mind drifts toward symbolic meaning, omens, and what could be.",
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
        },
        'image': 'kor_in1.jpeg',
        'song_id': 'far_from_home_sam_tinnesz'
    },
    {
        'npc_id': 'aeriola',
        'name': 'Lady Aeriola Frostborn',
        'description': (
            'An aristocratic ice-sorceress who froze her own heart to "escape time." '
            'She wants to stop the world\'s motion entirely — no thaw, no breath, no change.'
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
            "defense_mechanism": "Reaction Formation — Convinces herself that freezing the world is a righteous and pure mission to escape the 'corruption' of time and change.",
            "stress_line": "Moves to Type 4 — Becomes melancholic and withdrawn, lamenting the 'imperfect' world that refuses to freeze.",
            "growth_line": "Moves to Type 7 — Learns to accept and even find joy in the world's natural flow and change.",
            "instinctual_variant": "sp/so — A self-contained reformer, obsessed with creating a perfect, unchanging environment for herself and the world."
        },
        'image': 'bosses:aeriola1.jpeg'
    }
]

NPC_DIALOG = [
    # ── Kor-in receives the clasp, joins ──────────────────────────────────────
    {
        'npc_id': 'kor_in',
        'dialog_id': 'kor_in_intro',
        'dialog': [
            "(quiet, almost whispering) You smell like warmth… like she did.",
            "Good. I need someone still breathing.",
            "Lady Aeriola froze half the valley last night.",
            "She wants the world still — unmoving — like a corpse.",
            "My wife was in one of her frozen 'moments.'",
            "I shattered the ice with my hands.",
            "(long pause)",
            "She was already gone.",
            "End her madness.",
            "Before she freezes time itself."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_kor_in_intro',
        'dialog': [
            "He said 'like she did' before he said anything else.",
            "That's the whole person, right there."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_kor_in_intro',
        'dialog': [
            "He shattered ice with his bare hands.",
            "And she was still gone.",
            "(quietly) I'm not going to say anything stupid right now."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_kor_in_intro',
        'dialog': [
            "He's been sitting with this a long time.",
            "He's not asking for sympathy.",
            "He's asking for someone who can end it.",
            "We can do that."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_kor_in_intro',
        'dialog': [
            "Localized temporal freeze. That's not weather magic.",
            "That's something much older.",
            "The boreal clasp should break her ward geometry.",
            "Let's move."
        ]
    },
    # ── Kor-in joins ──────────────────────────────────────────────────────────
    {
        'npc_id': 'kor_in',
        'dialog_id': 'kor_in_joins',
        'dialog': [
            "(takes the clasp, turns it over once)",
            "This will do.",
            "(looks at the party)",
            "I've been alone in this a long time.",
            "Not because I wanted to be.",
            "Because no one else knew what to do with a grief this cold.",
            "(quietly) You'll do.",
            "Let's go find her."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'kaera_kor_in_join_reaction',
        'dialog': [
            "'No one knew what to do with a grief this cold.'",
            "He's been carrying that alone.",
            "Not anymore."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_kor_in_join_reaction',
        'dialog': [
            "He said 'you'll do' like a compliment.",
            "Coming from him, I think it is one."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_kor_in_join_reaction',
        'dialog': [
            "Quiet. Precise. Hasn't stopped moving toward the thing that hurt him.",
            "I respect that.",
            "Welcome, Kor-in."
        ]
    },
    # ── Aeriola confrontation ─────────────────────────────────────────────────
    {
        'npc_id': 'aeriola',
        'dialog_id': 'aeriola_intro',
        'dialog': [
            "A warm one approaches. How quaint.",
            "Motion is corruption. Change is decay.",
            "Only in perfect stillness can purity endure.",
            "You will join the stillness.",
            "All of you."
        ]
    },
    {
        'npc_id': 'kor_in',
        'dialog_id': 'kor_in_aeriola_confrontation',
        'dialog': [
            "Aeriola.",
            "You froze my wife.",
            "You froze the valley.",
            "You froze your own heart and called it purity.",
            "(step forward, voice entirely flat)",
            "The snow was honest before you came.",
            "It will be honest again after."
        ]
    },
    {
        'npc_id': 'aeriola',
        'dialog_id': 'aeriola_confrontation_reply',
        'dialog': [
            "Kor-in.",
            "Still warm. Still suffering.",
            "Your wife felt nothing after the first moment.",
            "That was mercy.",
            "Why do you fight so desperately to keep suffering?",
            "I offer an end to all of it.",
            "The final winter asks nothing of you.",
            "Only stillness."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_aeriola_challenge',
        'dialog': [
            "She called killing his wife mercy.",
            "We're done talking."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_aeriola_challenge',
        'dialog': [
            "Your warmth is a disease.",
            "That's what she actually believes.",
            "(quietly furious) Hit her."
        ]
    },
    # ── Aeriola defeat ────────────────────────────────────────────────────────
    {
        'npc_id': 'aeriola',
        'dialog_id': 'aeriola_defeat',
        'dialog': [
            "Warmth… persists.",
            "The final winter… delayed.",
            "Motion… is corruption…",
            "And yet… it endures…",
            "How… tiresome."
        ]
    },
    # ── Post-defeat scene ─────────────────────────────────────────────────────
    {
        'npc_id': 'kor_in',
        'dialog_id': 'kor_in_post_defeat',
        'dialog': [
            "(staring at the melting ice, very still)",
            "She's gone.",
            "The snow feels honest again.",
            "(long pause)",
            "…But it will never feel warm.",
            "(turns away from the ice)",
            "That's alright.",
            "I stopped expecting warm a long time ago.",
            "Come on.",
            "There's more of this world worth keeping."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'kaera_post_defeat',
        'dialog': [
            "He stood there until the ice finished melting.",
            "Then he turned around.",
            "That took everything he had.",
            "And he still turned around."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_post_defeat',
        'dialog': [
            "She said stillness was mercy.",
            "He's been moving through grief for years to prove her wrong.",
            "I think he just did."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_post_defeat',
        'dialog': [
            "'There's more of this world worth keeping.'",
            "That's the first thing he's said that wasn't about her.",
            "That matters."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_post_defeat',
        'dialog': [
            "Aeriola called motion corruption.",
            "He kept moving anyway.",
            "For years.",
            "That's the counterargument. It's a good one."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_post_defeat',
        'dialog': [
            "Kor-in held.",
            "Even in the cold.",
            "Especially in the cold."
        ]
    },
]

DUNGEONS = []

TASKS = [
    # ── Initialize — Kor-in appears at region bar ─────────────────────────────
    {
        'task_id': 'snow_primary_initialize',
        'type': 'complete_intro_story',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'kor_in',
                    'location': 'region_bar'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'kor_in',
                    'standing_text': [
                        "I'm Kor-in. Ice trapper.",
                        "Lost my family to a sorceress a few years back.",
                        "If you hear anything about Lady Aeriola — come find me."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_primary_meet_kor_in'
                }
            }
        ]
    },

    # ── Deliver boreal_clasp — Kor-in joins here ──────────────────────────────
    {
        'task_id': 'snow_primary_meet_kor_in',
        'type': 'deliver',
        'to_type': 'npc',
        'to_id': 'kor_in',
        'item_id': 'boreal_clasp',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'kor_in',
                    'standing_text': [
                        "Aeriola is on a rampage.",
                        "I need a Boreal Clasp to break her wards before I can reach her.",
                        "Bring it to me when you find one."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'kor_in',
                    'dialog_id': 'kor_in_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_kor_in_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'technique',
                    'dialog_id': 'chock_kor_in_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_kor_in_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_kor_in_intro'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'kor_in',
                    'dialog_id': 'kor_in_joins'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'faith',
                    'dialog_id': 'kaera_kor_in_join_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_kor_in_join_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'technique',
                    'dialog_id': 'chock_kor_in_join_reaction'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {'npc_id': 'kor_in'}
            },
            {
                'event_type': 'character_join',
                'params': {'character_id': 'kor_in'}
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'snow_primary_defeat_aeriola'
                }
            }
        ]
    },

    # ── Meet Aeriola in dungeon — confrontation scene ─────────────────────────
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
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'kor_in',
                    'dialog_id': 'kor_in_aeriola_confrontation'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'aeriola',
                    'dialog_id': 'aeriola_confrontation_reply'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'technique',
                    'dialog_id': 'chock_aeriola_challenge'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_aeriola_challenge'
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

    # ── Defeat Aeriola — void hint + Kor-in arc resolution ────────────────────
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
            {
                'event_type': 'hide_npc',
                'params': {'npc_id': 'aeriola'}
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'kor_in',
                    'dialog_id': 'kor_in_post_defeat'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'faith',
                    'dialog_id': 'kaera_post_defeat'
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
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_post_defeat'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_post_defeat'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {'region_id': 'snow'}
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