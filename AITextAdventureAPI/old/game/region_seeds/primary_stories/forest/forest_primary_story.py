#FOREST
# local characters:
#  Thorn - gruff half-feral forest guardian (technique)
#
# local bad-guys:
#  ELDER Marrowroot
# A druid who fused with a void-scarred world-tree, becoming a monstrous prophet of "the coming stillness."
# He wants to convert humanity to fuse with void-touched trees to survive and is corrupting the forest to build an army.
#
# Grove Lattice acquisition side chain:
#  Mirlo the Moonbrewer (Boiling Bubble) has a grove lattice but needs a lunar resonance catalyst.
#  Juno (Boiling Bubble, previously encountered in ch2) has the catalyst — but only as a card game prize.
#  Win the catalyst from Juno (3-round guessing game, doubling buy-in), deliver to Mirlo, receive grove lattice.
#  If the player already holds grove_lattice from the ch2 dungeon drop, the side chain is skipped.

ATTAINABLE_PLAYER_CHARACTERS = [
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
        },
        'image': 'thorn1.jpeg',
        'song_id': 'way_down_we_go_kaleo'
    },
    {
        'npc_id': 'marrowroot',
        'name': 'Elder Marrowroot',
        'description': (
            'A once-wise druid who fused with an ancient tree and became something monstrous.'
            ' He believes the forest must uproot itself and retreat from the world\'s "approaching edge."'
        ),
        "psychology": {
            "mbti": "INFJ",
            "dominant": "Ni — Interprets the void's whispers as prophecy. He sees a singular future where the forest must transform or perish.",
            "auxiliary": "Fe — Frames his corruption as salvation, believing he is guiding the forest toward its 'next form.' He speaks in warnings and moral imperatives.",
            "tertiary": "Ti — Constructs twisted internal logic to justify his actions, rationalizing corruption as evolution.",
            "inferior": "Se — His physical form is unstable; sensory overload drives him into violent, uncontrolled bursts of void-infused magic."
        },
        "enneagram": {
          "enneagram_type": "1w2",
          "core_fear": "Being corrupt or failing his duty to the forest.",
          "core_desire": "To be good and have integrity.",
          "defense_mechanism": "Reaction Formation — Believes his monstrous transformation is a righteous, necessary act to 'save' the forest, denying its corrupting nature.",
          "stress_line": "Moves to Type 4 — Becomes melancholic and withdrawn, lamenting the 'sacrifice' he has made.",
          "growth_line": "Moves to Type 7 — Learns to accept the world's imperfections and find a more flexible way to protect his home.",
          "instinctual_variant": "so/sp — Entirely focused on the 'salvation' of his community (the forest), sacrificing his own form for it."
        },
        'image': 'bosses:marrowroot1.jpeg'
    }
]

NPC_DIALOG = [
    # ── Thorn bar standing / lattice hook ─────────────────────────────────────
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_intro',
        'dialog': [
            "You. Outsider. Good. Need help.",
            "Marrowroot's ripping up roots, screaming about the 'approaching edge.' Forest's scared. I'm angry.",
            "His wards are thick. I need a grove lattice to break through.",
            "Mirlo in Boiling Bubble had one last I heard. Go find it.",
            "Then come back. We go into his grove and end this."
        ]
    },
    # ── Mirlo grove lattice hook ──────────────────────────────────────────────
    {
        'npc_id': 'alchemist_mirlo',
        'dialog_id': 'mirlo_grove_lattice_hook',
        'dialog': [
            "Oh — a grove lattice? Yes, I have one.",
            "Fascinating specimen. I've been using it as a lunar resonance anchor for my experiments.",
            "The problem is, the anchor only works if I replace it with a proper lunar resonance catalyst.",
            "Stabilized lunar essence, bound in an alchemical shell. Juno won one off a courier last week.",
            "She won't sell it. She'd rather gamble it. Everything's a game to that woman.",
            "Win it from her, bring it to me, and the grove lattice is yours."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_mirlo_reaction',
        'dialog': [
            "A lunar resonance catalyst won at cards by a professional gambler.",
            "Obviously.",
            "Let's go find Juno."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_mirlo_reaction',
        'dialog': [
            "So the item we need is trapped in a gambling loop with a woman who calculates odds for a living.",
            "Wonderful. This should be efficient."
        ]
    },
    # ── Juno gambling chain ───────────────────────────────────────────────────
    {
        'npc_id': 'juno',
        'dialog_id': 'juno_forest_gamble_intro',
        'dialog': [
            "Well. You again.",
            "Looking for something? Let me guess — Mirlo sent you.",
            "He wants his anchor back, and I want entertainment.",
            "Three cards. You pick the one with the moon on the back. Simple.",
            "First game costs a thousand gold. Lose, and the next round doubles.",
            "Win at any point, the catalyst is yours.",
            "Ready to play?"
        ]
    },
    {
        'npc_id': 'juno',
        'dialog_id': 'juno_gamble_win',
        'dialog': [
            "...Well. You actually got it.",
            "Not many do on the first try.",
            "Here. The catalyst. Mirlo'll be pleased.",
            "Come back when you want to lose money on something more interesting."
        ]
    },
    {
        'npc_id': 'juno',
        'dialog_id': 'juno_gamble_lose_r1',
        'dialog': [
            "Ha. Wrong card.",
            "The buy-in doubles if you want another shot. Two thousand.",
            "Or you can walk away. Up to you."
        ]
    },
    {
        'npc_id': 'juno',
        'dialog_id': 'juno_gamble_lose_r2',
        'dialog': [
            "Two in a row. Impressive, in the wrong direction.",
            "Last chance. Four thousand.",
            "I admire the persistence. Most people quit after the first."
        ]
    },
    {
        'npc_id': 'juno',
        'dialog_id': 'juno_gamble_lose_r3',
        'dialog': [
            "Three rounds. You lost all three.",
            "I respect the commitment. I really do.",
            "Come back when you've refilled your pockets. I'll be here."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_juno_gamble_reaction',
        'dialog': [
            "Statistically, we should win one-in-three. Emotionally, I believe we'll win immediately.",
            "Probably."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_juno_gamble_reaction',
        'dialog': [
            "A one-in-three guess with escalating stakes.",
            "This is not a puzzle. This is paying for the privilege of randomness.",
            "Fine. Pick something."
        ]
    },
    # ── Mirlo receives catalyst, hands over lattice ───────────────────────────
    {
        'npc_id': 'alchemist_mirlo',
        'dialog_id': 'mirlo_catalyst_received',
        'dialog': [
            "You got it! From Juno? I'm genuinely surprised.",
            "She usually just keeps winning until the other person gives up.",
            "Here — the grove lattice. Handle it carefully.",
            "The lunar resonance in it is still active. Should be perfect for what you need."
        ]
    },
    # ── Thorn receives the lattice and joins ──────────────────────────────────
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_grove_lattice_received',
        'dialog': [
            "Grove lattice. Good.",
            "This breaks his wards. Now we can reach him.",
            "You didn't have to go that far for the forest.",
            "...But you did.",
            "I come with you. Forest can't be protected by one guardian anymore."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_thorn_join_reaction',
        'dialog': [
            "A half-feral guardian with a fangblade and trust issues.",
            "I like him already."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_thorn_join_reaction',
        'dialog': [
            "Instinct-driven. High threat threshold. Low tolerance for the unnecessary.",
            "Useful. Welcome aboard."
        ]
    },
    # ── Marrowroot confrontation scene ────────────────────────────────────────
    {
        'npc_id': 'marrowroot',
        'dialog_id': 'marrowroot_intro',
        'dialog': [
            "You walk where roots recoil.",
            "The void touches the world. I will pull the forest back before it is devoured."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_marrowroot_confrontation',
        'dialog': [
            "You were a guardian. Like me.",
            "What you're doing to the forest — it's not saving it. I've seen what you call 'saving.'",
            "It screams."
        ]
    },
    {
        'npc_id': 'marrowroot',
        'dialog_id': 'marrowroot_confrontation_reply',
        'dialog': [
            "The forest screams because it feels the edge approaching.",
            "I hear it too, Thorn. I have always heard it.",
            "You call it corruption. I call it preparation.",
            "The roots touched the void… and the void touched back. That is not death. That is evolution."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_marrowroot_challenge',
        'dialog': [
            "I've heard enough.",
            "You're not saving anything. You're just the loudest thing rotting in here.",
            "Let's end this."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_marrowroot_observation',
        'dialog': [
            "He's fused with the tree. The void corruption is structural — woven into the bark.",
            "Fascinating and horrifying.",
            "Mostly horrifying."
        ]
    },
    # ── Post-defeat scene ─────────────────────────────────────────────────────
    {
        'npc_id': 'marrowroot',
        'dialog_id': 'marrowroot_defeat',
        'dialog': [
            "The roots… still feel it… the edge…",
            "The void does not wait for permission.",
            "You have not stopped it. You have only delayed what the forest already knows.",
            "Listen to the roots… before they stop speaking entirely."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_post_defeat',
        'dialog': [
            "(quiet) He was a guardian.",
            "Same corruption that took him… took something I raised once.",
            "Forest remembers everything. Grief too.",
            "...We move. Before more of it spreads."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_post_defeat',
        'dialog': [
            "He said 'the void doesn't wait for permission.'",
            "That's the part that's going to bother me.",
            "The rest was sad. That part was a warning."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_post_defeat',
        'dialog': [
            "One less monster wearing a martyr's face.",
            "Forest's calmer already. Let's not give whatever he was listening to time to find a new host."
        ]
    },
    {
        'npc_id': 'juno',
        'dialog_id': 'juno_not_enough_gold_r1',
        'dialog': [
            "A thousand gold. That's the entry.",
            "Come back when you have it."
        ]
    },
    {
        'npc_id': 'juno',
        'dialog_id': 'juno_not_enough_gold_r2',
        'dialog': [
            "Two thousand. Not a copper less.",
            "Go earn it and come back."
        ]
    },
    {
        'npc_id': 'juno',
        'dialog_id': 'juno_not_enough_gold_r3',
        'dialog': [
            "Four thousand. Last round.",
            "You're not there yet. Come back when you are."
        ]
    },
    {
        'npc_id': 'juno',
        'dialog_id': 'juno_pity_catalyst',
        'dialog': [
            "...Okay. Stop.",
            "I've watched you lose seven thousand gold chasing something worth maybe two hundred.",
            "Here. Take it.",
            "Consider it a charitable donation. Don't tell anyone — it'll ruin my reputation."
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
                        "Forest is wrong tonight. Something moves in it that shouldn't.",
                        "If you go out there — be quiet. And watch the roots."
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
            },
            # Side chain: acquire grove lattice via Mirlo → Juno.
            # Skipped if player already has grove_lattice (ch2 dungeon drop).
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_primary_meet_mirlo_for_lattice'
                },
                'condition': {
                    'type': 'has_item',
                    'params': { 'item_id': 'grove_lattice' },
                    'operator': 'is_not'
                }
            }
        ]
    },

    # Side chain Task A: Meet Mirlo in Boiling Bubble — he hooks the lattice/catalyst trade
    {
        'task_id': 'forest_primary_meet_mirlo_for_lattice',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'alchemist_mirlo',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'thorn',
                    'standing_text': [
                        "Marrowroot's wards are thick. Need a grove lattice to break through.",
                        "Mirlo in Boiling Bubble had one last I heard. Go find it."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'alchemist_mirlo',
                    'dialog_id': 'mirlo_grove_lattice_hook'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_mirlo_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_mirlo_reaction'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'alchemist_mirlo',
                    'standing_text': [
                        "Win the catalyst from Juno and bring it to me.",
                        "The grove lattice is yours the moment you do."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_primary_meet_juno_gamble'
                }
            }
        ]
    },

    # Side chain Task B: Meet Juno — she introduces the card game
    {
        'task_id': 'forest_primary_meet_juno_gamble',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'juno',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'juno',
                    'standing_text': [
                        "Three cards. One moon. You know what you're here for.",
                        "First game is a thousand gold."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'juno',
                    'dialog_id': 'juno_forest_gamble_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_juno_gamble_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_juno_gamble_reaction'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'forest_primary_meet_juno_r1'
                }
            }
        ]
    },
    # ROUND 1
    {
        'task_id': 'forest_primary_meet_juno_r1',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'juno',
        'task_acquire_events': [
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'juno', 'standing_text': [
                "1,000 gold. Ready when you are."
            ]}}
        ],
        'task_complete_events': [
            # Has funds — show the card game
            {
                'event_type': 'initiate_option_dialog',
                'params': {
                    'message': "Juno fans three cards face-down. \"One moon. Pick one. Cost: 1,000 gold.\"",
                    'options': [
                        ("The left card.",   'forest_juno_r1_win'),
                        ("The middle card.", 'forest_juno_r1_lose'),
                        ("The right card.",  'forest_juno_r1_lose'),
                    ]
                },
                'condition': { 'type': 'has_money', 'params': { 'amount': 1000 }, 'operator': 'is' }
            },
            # No funds — tell them and re-queue this meet so they can return
            {
                'event_type': 'initiate_dialog',
                'params': { 'npc_id': 'juno', 'dialog_id': 'juno_not_enough_gold_r1' },
                'condition': { 'type': 'has_money', 'params': { 'amount': 1000 }, 'operator': 'is_not' }
            },
            {
                'event_type': 'remove_task',
                'params': { 'task_id': 'forest_primary_meet_juno_r1' },
                'condition': { 'type': 'has_money', 'params': { 'amount': 1000 }, 'operator': 'is_not' }
            },
            {
                'event_type': 'award_task',
                'params': { 'task_id': 'forest_primary_meet_juno_r1' },
                'condition': { 'type': 'has_money', 'params': { 'amount': 1000 }, 'operator': 'is_not' }
            },
        ]
    },
    {
        'task_id': 'forest_juno_r1_win',
        'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'forest_juno_r1_win' } }
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'juno', 'dialog_id': 'juno_gamble_win' } },
            { 'event_type': 'award_item',  'params': { 'item_id': 'lunar_resonance_catalyst' } },
            { 'event_type': 'award_task',  'params': { 'task_id': 'forest_primary_deliver_catalyst_to_mirlo' } }
        ]
    },
    {
        'task_id': 'forest_juno_r1_lose',
        'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'forest_juno_r1_lose' } }
        ],
        'task_complete_events': [
            { 'event_type': 'remove_money', 'params': { 'amount': 1000 } },
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'juno', 'dialog_id': 'juno_gamble_lose_r1' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'juno', 'standing_text': [
                "Next round is 2,000 gold. Come back when you're ready."
            ]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'forest_primary_meet_juno_r2' } }
        ]
    },

    # ── Round 2 ───────────────────────────────────────────────────────────────
    {
        'task_id': 'forest_primary_meet_juno_r2',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'juno',
        'task_acquire_events': [
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'juno', 'standing_text': [
                "Double or nothing. 2,000 gold. Ready when you are."
            ]}}
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_option_dialog',
                'params': {
                    'message': "Juno reshuffles with a smirk. \"Double or nothing. 2,000 gold. Pick your card.\"",
                    'options': [
                        ("The left card.",   'forest_juno_r2_win'),
                        ("The middle card.", 'forest_juno_r2_lose'),
                        ("The right card.",  'forest_juno_r2_lose'),
                    ]
                },
                'condition': { 'type': 'has_money', 'params': { 'amount': 2000 }, 'operator': 'is' }
            },
            {
                'event_type': 'initiate_dialog',
                'params': { 'npc_id': 'juno', 'dialog_id': 'juno_not_enough_gold_r2' },
                'condition': { 'type': 'has_money', 'params': { 'amount': 2000 }, 'operator': 'is_not' }
            },
            {
                'event_type': 'remove_task',
                'params': { 'task_id': 'forest_primary_meet_juno_r2' },
                'condition': { 'type': 'has_money', 'params': { 'amount': 2000 }, 'operator': 'is_not' }
            },
            {
                'event_type': 'award_task',
                'params': { 'task_id': 'forest_primary_meet_juno_r2' },
                'condition': { 'type': 'has_money', 'params': { 'amount': 2000 }, 'operator': 'is_not' }
            },
        ]
    },
    {
        'task_id': 'forest_juno_r2_win',
        'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'forest_juno_r2_win' } }
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'juno', 'dialog_id': 'juno_gamble_win' } },
            { 'event_type': 'award_item',  'params': { 'item_id': 'lunar_resonance_catalyst' } },
            { 'event_type': 'award_task',  'params': { 'task_id': 'forest_primary_deliver_catalyst_to_mirlo' } }
        ]
    },
    {
        'task_id': 'forest_juno_r2_lose',
        'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'forest_juno_r2_lose' } }
        ],
        'task_complete_events': [
            { 'event_type': 'remove_money', 'params': { 'amount': 2000 } },
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'juno', 'dialog_id': 'juno_gamble_lose_r2' } },
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'juno', 'standing_text': [
                "Last chance. 4,000 gold. Don't waste my time."
            ]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'forest_primary_meet_juno_r3' } }
        ]
    },

    # ── Round 3 ───────────────────────────────────────────────────────────────
    {
        'task_id': 'forest_primary_meet_juno_r3',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'juno',
        'task_acquire_events': [
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'juno', 'standing_text': [
                "Last round. 4,000 gold. One card. Make it count."
            ]}}
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_option_dialog',
                'params': {
                    'message': "Juno raises an eyebrow. \"Last chance. 4,000 gold. Choose carefully.\"",
                    'options': [
                        ("The left card.",   'forest_juno_r3_win'),
                        ("The middle card.", 'forest_juno_r3_lose'),
                        ("The right card.",  'forest_juno_r3_lose'),
                    ]
                },
                'condition': { 'type': 'has_money', 'params': { 'amount': 4000 }, 'operator': 'is' }
            },
            {
                'event_type': 'initiate_dialog',
                'params': { 'npc_id': 'juno', 'dialog_id': 'juno_not_enough_gold_r3' },
                'condition': { 'type': 'has_money', 'params': { 'amount': 4000 }, 'operator': 'is_not' }
            },
            {
                'event_type': 'remove_task',
                'params': { 'task_id': 'forest_primary_meet_juno_r3' },
                'condition': { 'type': 'has_money', 'params': { 'amount': 4000 }, 'operator': 'is_not' }
            },
            {
                'event_type': 'award_task',
                'params': { 'task_id': 'forest_primary_meet_juno_r3' },
                'condition': { 'type': 'has_money', 'params': { 'amount': 4000 }, 'operator': 'is_not' }
            },
        ]
    },
    {
        'task_id': 'forest_juno_r3_win',
        'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'forest_juno_r3_win' } }
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'juno', 'dialog_id': 'juno_gamble_win' } },
            { 'event_type': 'award_item',  'params': { 'item_id': 'lunar_resonance_catalyst' } },
            { 'event_type': 'award_task',  'params': { 'task_id': 'forest_primary_deliver_catalyst_to_mirlo' } }
        ]
    },
    {
        'task_id': 'forest_juno_r3_lose',
        'type': 'gated',
        'task_acquire_events': [
            { 'event_type': 'complete_task', 'params': { 'task_id': 'forest_juno_r3_lose' } }
        ],
        'task_complete_events': [
            { 'event_type': 'remove_money', 'params': { 'amount': 4000 } },
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'juno', 'dialog_id': 'juno_gamble_lose_r3' } },
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'juno', 'dialog_id': 'juno_pity_catalyst' } },
            { 'event_type': 'award_item',  'params': { 'item_id': 'lunar_resonance_catalyst' } },
            { 'event_type': 'award_task',  'params': { 'task_id': 'forest_primary_deliver_catalyst_to_mirlo' } }
        ]
    },

    # Side chain Task C: Deliver catalyst to Mirlo, receive grove lattice
    {
        'task_id': 'forest_primary_deliver_catalyst_to_mirlo',
        'type': 'deliver',
        'to_type': 'npc',
        'to_id': 'alchemist_mirlo',
        'item_id': 'lunar_resonance_catalyst',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'alchemist_mirlo',
                    'standing_text': [
                        "You got the catalyst? Bring it here!",
                        "The grove lattice is yours the moment you hand it over."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'alchemist_mirlo',
                    'dialog_id': 'mirlo_catalyst_received'
                }
            },
            { 'event_type': 'remove_item', 'params': { 'item_id': 'lunar_resonance_catalyst' } },
            { 'event_type': 'award_item',  'params': { 'item_id': 'grove_lattice' } },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'alchemist_mirlo',
                    'standing_text': [
                        "The catalyst is in place. The moonbrews are stable again.",
                        "Mostly."
                    ]
                }
            }
        ]
    },

    # Main Task 1: Deliver grove lattice to Thorn — he joins here
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
                    'standing_text': [
                        "Marrowroot's wards are thick. Need a grove lattice to break through.",
                        "Find one. Then we go."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'thorn',
                    'dialog_id': 'thorn_grove_lattice_received'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_thorn_join_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_thorn_join_reaction'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': { 'npc_id': 'thorn' }
            },
            {
                'event_type': 'character_join',
                'params': { 'character_id': 'thorn' }
            },
            {
                'event_type': 'award_task',
                'params': { 'task_id': 'forest_primary_defeat_marrowroot' }
            }
        ]
    },

    # Main Task 2: Meet Marrowroot in his dungeon — confrontation scene before combat
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
                'params': { 'npc_id': 'marrowroot', 'dialog_id': 'marrowroot_intro' }
            },
            {
                'event_type': 'initiate_dialog',
                'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_marrowroot_confrontation' }
            },
            {
                'event_type': 'initiate_dialog',
                'params': { 'npc_id': 'marrowroot', 'dialog_id': 'marrowroot_confrontation_reply' }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': { 'npc_id': 'technique', 'dialog_id': 'chock_marrowroot_challenge' }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_marrowroot_observation' }
            },
            {
                'event_type': 'award_task',
                'params': { 'task_id': 'defeat_marrowroot' }
            }
        ]
    },

    # Main Task 3: Defeat Marrowroot — Void hint, Thorn grief scene, complete_region_quest
    # forest_primary_report_to_thorn removed — Thorn already joined at deliver step
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
                'params': { 'npc_id': 'marrowroot', 'dialog_id': 'marrowroot_defeat' }
            },
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'marrowroot' } },
            {
                'event_type': 'initiate_dialog',
                'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_post_defeat' }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': { 'npc_id': 'magic', 'dialog_id': 'moxie_post_defeat' }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': { 'npc_id': 'technique', 'dialog_id': 'chock_post_defeat' }
            },
            {
                'event_type': 'complete_region_quest',
                'params': { 'region_id': 'forest' }
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