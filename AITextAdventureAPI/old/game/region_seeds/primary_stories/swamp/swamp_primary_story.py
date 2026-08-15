#SWAMP
# local characters:
#  Grimnaw - Cursed Gadget dealer/collector (tech) — INTP 5w6
#
# local bad-guys:
#  LICH-KING Miregloom
#   A decayed sorcerer who bound his soul to the swamp's rot to escape the world's fate.
#   His body is a tangle of decayed flesh, bones.
#   He seeks to accelerate the world's decay using a cursed gadget.
#
#   Void Hint:
#    He claims the swamp is "where the world will rot first when the edge arrives."
#
# Pregame: deliver mirethread_pendant to Grimnaw — he joins here.
# report_to_grimnaw removed.

ATTAINABLE_PLAYER_CHARACTERS = [
    {
        ## total power points = 15 + 15 * 29 = 465
        ## total stat points = 10 + 6 * 29 = 184
        'id': 'grimnaw',
        'name': 'Grimnaw',
        'head_armor': 'rotlens_goggles',
        'body_armor': 'mireforged_carapace',
        'arm_armor': 'hexsplice_gauntlets',
        'leg_armor': 'bogwalker_greaves',
        'equipped_weapon': 'cursespark_engine_rod',
        'max_hp': 941,
        'current_hp': 941,
        'max_ap': 350,
        'current_ap': 350,
        'unused_ability_slots': 0,
        'unused_stat_points': 0,
        'unused_power_points': 0,
        'strength': 38,
        'dexterity': 102,
        'intelligence': 158,
        'constitution': 38,
        'level': 30,
        'abilities': [
            'lv2_unique_ability_tech_grimnaw_hex_charge',
            'lv2_unique_ability_tech_grimnaw_resonance_shell',
            'lv3_unique_ability_tech_grimnaw_whisper_resonance',
            'lv3_unique_ability_tech_grimnaw_cursed_circuit',
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
        },
        'image': 'grimnaw1.jpeg',
        'song_id': 'madness_muse'
    },
    {
        'npc_id': 'miregloom',
        'name': 'Lich-King Miregloom',
        'description': (
            'A decayed sorcerer who bound his soul to the swamp\'s rot to escape the world\'s fate.'
            ' His body is a tangle of roots, bones, and swamp-fire.'
        ),
        "psychology": {
            "mbti": "INFP",
            "dominant": "Fi — Holds a deeply personal, corrupted belief that decay is purity and destiny.",
            "auxiliary": "Ne — Interprets rot, death, and swamp-whispers as cosmic signs.",
            "tertiary": "Si — Clings to ancient memories of the world's 'fate,' using them to justify his transformation.",
            "inferior": "Te — When destabilized, lashes out with chaotic, uncontrolled magic."
        },
        "enneagram": {
            "enneagram_type": "4w5",
            "core_fear": "Having no identity or significance.",
            "core_desire": "To find and create a unique identity, separate from the world's fate.",
            "defense_mechanism": "Introjection — Has absorbed the identity of the swamp and its decay, creating a monstrous persona to escape being nothing.",
            "stress_line": "Moves to Type 2 — Becomes clingy and manipulative, trying to force others to join his decay.",
            "growth_line": "Moves to Type 1 — Finds a principled way to exist without being defined by decay.",
            "instinctual_variant": "sp/sx — A withdrawn figure who created an all-consuming identity to preserve himself."
        },
        'image': 'bosses:miregloom1.jpeg'
    }
]

NPC_DIALOG = [
    # ── Grimnaw receives the pendant, joins ───────────────────────────────────
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_intro',
        'dialog': [
            "Heheheh! You! Yes, you'll do nicely.",
            "Miregloom's raising the dead again. Claims the swamp is the world's first grave.",
            "(muttering, turning the pendant over) Deliciously wrong, by the way.",
            "I've seen older things. Things that whispered.",
            "He's bad for business and worse for my research.",
            "Go knock his bones loose.",
            "(pause, then brightening) Oh — and if you find his phylactery, don't destroy it.",
            "The necrotic resonance patterns would be enormously instructive.",
            "...And might quiet the voice for a while."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_grimnaw_intro',
        'dialog': [
            "He said 'quiet the voice' like it was a footnote.",
            "It wasn't a footnote."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_grimnaw_intro',
        'dialog': [
            "He built a device that opened a fracture.",
            "Something answered.",
            "He's been trying to understand it ever since.",
            "I would do exactly the same thing.",
            "That doesn't make it less terrifying."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_grimnaw_intro',
        'dialog': [
            "He said 'you'll do nicely' like he was selecting a tool.",
            "I'm choosing to take that as a compliment.",
            "Barely."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_grimnaw_intro',
        'dialog': [
            "The pendant activated something in him.",
            "Not fear. Recognition.",
            "He knows exactly what Miregloom is doing.",
            "That's useful."
        ]
    },
    # ── Grimnaw joins ─────────────────────────────────────────────────────────
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_joins',
        'dialog': [
            "(examines the pendant one more time, then pockets it)",
            "Right. I'm coming with you.",
            "Don't misread that as sentiment.",
            "Miregloom is using cursed relics I catalogued.",
            "That makes him my problem structurally.",
            "(quieter, almost to himself) Also the whisper gets louder near his lair.",
            "And I want to know why.",
            "(cheerful again) Mostly the first reason."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_grimnaw_join_reaction',
        'dialog': [
            "He said 'mostly the first reason' and immediately looked away.",
            "Adorable.",
            "Welcome aboard, Grimnaw."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'kaera_grimnaw_join_reaction',
        'dialog': [
            "He's carrying something he doesn't have words for yet.",
            "He'll find them eventually.",
            "Until then — we move together."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_grimnaw_join_reaction',
        'dialog': [
            "Cursed gadgeteer with a fracture problem and a voice in his head.",
            "Honestly? Fits right in.",
            "Let's go."
        ]
    },
    # ── Miregloom confrontation ───────────────────────────────────────────────
    {
        'npc_id': 'miregloom',
        'dialog_id': 'miregloom_intro',
        'dialog': [
            "Another soul wanders into my rot.",
            "The world will decay soon. I merely begin the process.",
            "The swamp is where the world will rot first when the edge arrives.",
            "I have prepared it well.",
            "Join me. Decay is honest.",
            "It takes everything equally."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_miregloom_confrontation',
        'dialog': [
            "Miregloom.",
            "Your necrotic field geometry is elegantly structured.",
            "I mean that genuinely.",
            "(beat)",
            "The phylactery binding is also impressive.",
            "I'd love a sample.",
            "(flat) But you weaponized my relics.",
            "That's a boundary.",
            "Decay has rules. Entropy has patterns.",
            "You broke both.",
            "So — bones loose. Immediately."
        ]
    },
    {
        'npc_id': 'miregloom',
        'dialog_id': 'miregloom_confrontation_reply',
        'dialog': [
            "Grimnaw.",
            "Still hearing the whisper?",
            "I hear it too.",
            "It told me the swamp would endure.",
            "It told me decay is the only honesty left.",
            "You built a door and something walked through.",
            "That thing and I are old acquaintances.",
            "You should stop fighting it.",
            "You will rot eventually.",
            "Everything does."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_miregloom_reply',
        'dialog': [
            "(very still for a moment)",
            "...",
            "No.",
            "The whisper is a data point.",
            "You are a variable that needs to be removed.",
            "(to the party) Now, please."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_miregloom_challenge',
        'dialog': [
            "He said 'data point' and 'variable' when he meant 'terrifying' and 'end this.'",
            "I understood perfectly.",
            "Moving."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_miregloom_challenge',
        'dialog': [
            "Miregloom knows about the whisper.",
            "That means it has reach beyond the fracture.",
            "We file that and deal with Miregloom first.",
            "In that order."
        ]
    },
    # ── Miregloom defeat ──────────────────────────────────────────────────────
    {
        'npc_id': 'miregloom',
        'dialog_id': 'miregloom_defeat',
        'dialog': [
            "Rot… postponed…",
            "The whisper… remembers you… Grimnaw…",
            "It will… find its way back…",
            "Decay… is patient…"
        ]
    },
    # ── Post-defeat scene ─────────────────────────────────────────────────────
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_post_defeat',
        'dialog': [
            "Hah! You did it!",
            "Swamp smells better already.",
            "(crouching immediately over the collapsed lich)",
            "...Ah. The phylactery shattered on impact.",
            "Pity.",
            "The necrotic resonance patterns would have been delicious.",
            "(standing, quieter)",
            "He said the whisper remembers me.",
            "Which means the whisper is consistent across subjects.",
            "Which means it has memory.",
            "Which means it's either a system or an entity.",
            "(muttering, pulling out a notebook)",
            "Either way — new data.",
            "(looking up at the party, almost surprised they're still there)",
            "...Right. Yes. Good work.",
            "Someone needs to keep the relics in line out there.",
            "I'll tag along."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_post_defeat',
        'dialog': [
            "He was taking notes before Miregloom finished falling.",
            "That is either the most unhinged thing I've ever seen or the most focused.",
            "Possibly both."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_post_defeat',
        'dialog': [
            "The whisper has memory.",
            "He said it like a discovery.",
            "I think for him it was.",
            "And I think it frightened him more than anything Miregloom did."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_post_defeat',
        'dialog': [
            "One less lich.",
            "One more question Grimnaw won't be able to leave alone.",
            "Pretty much exactly what I expected."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_post_defeat',
        'dialog': [
            "He called it new data.",
            "He meant 'I'm scared and I need to understand this before it destroys me.'",
            "Both things are true at once.",
            "That takes its own kind of courage."
        ]
    },
]

DUNGEONS = []

TASKS = [
    # ── Initialize — Grimnaw appears at region bar ────────────────────────────
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
                        "How goes it? I'm Grimnaw.",
                        "Dark twisted tech, cursed relics, anomalous resonance — that's my area.",
                        "Something's wrong in the swamp. Miregloom wrong.",
                        "Get me a Mirethread Pendant and I can get you access to find him."
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

    # ── Deliver mirethread_pendant — Grimnaw joins here ───────────────────────
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
                    'standing_text': [
                        "Miregloom is on a rampage.",
                        "Get me the Mirethread Pendant.",
                        "I can use it to break through his wards."
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
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_grimnaw_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_grimnaw_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'technique',
                    'dialog_id': 'chock_grimnaw_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_grimnaw_intro'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'grimnaw',
                    'dialog_id': 'grimnaw_joins'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_grimnaw_join_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'faith',
                    'dialog_id': 'kaera_grimnaw_join_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'technique',
                    'dialog_id': 'chock_grimnaw_join_reaction'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {'npc_id': 'grimnaw'}
            },
            {
                'event_type': 'character_join',
                'params': {'character_id': 'grimnaw'}
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'swamp_primary_defeat_miregloom'
                }
            }
        ]
    },

    # ── Meet Miregloom in dungeon — confrontation scene ───────────────────────
    {
        'task_id': 'swamp_primary_defeat_miregloom',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'miregloom',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'miregloom',
                    'location': None
                }
            },
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'miregloom_lair',
                    'location': 'region_open_area'
                }
            },
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'miregloom_lair', 'item_id': 'cursespark_engine_rod', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'miregloom_lair', 'item_id': 'mireforged_carapace', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'miregloom_lair', 'item_id': 'rotlens_goggles', 'location': 'treasure_room' }},
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
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'grimnaw',
                    'dialog_id': 'grimnaw_miregloom_confrontation'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'miregloom',
                    'dialog_id': 'miregloom_confrontation_reply'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'grimnaw',
                    'dialog_id': 'grimnaw_miregloom_reply'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_miregloom_challenge'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_miregloom_challenge'
                }
            },
            { 'event_type': 'set_npc_standing_text',
              'params': {
                  'npc_id': 'miregloom',
                  'standing_text': [
                      "The swamp stirs.",
                      "Its secrets are mine to command."
                  ]
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

    # ── Defeat Miregloom — void hint + Grimnaw arc beat ───────────────────────
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
            {
                'event_type': 'hide_npc',
                'params': {'npc_id': 'miregloom'}
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'grimnaw',
                    'dialog_id': 'grimnaw_post_defeat'
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
                    'npc_id': 'tech',
                    'dialog_id': 'kade_post_defeat'
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
                    'npc_id': 'skill',
                    'dialog_id': 'poise_post_defeat'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {'region_id': 'swamp'}
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