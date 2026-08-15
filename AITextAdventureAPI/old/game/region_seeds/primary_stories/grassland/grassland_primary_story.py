#GRASSLAND
# local characters:
#  Nia - A rebellious wind-dancer (skill) — ENFP 7w6
#    She lives on the wind, meaning she lives on gossip, people, word-of-mouth.
#    Her pregame hook is a rumor chain: the party hears something juicy,
#    Nia nudges them to spread it around until it lands in the right ear,
#    and that person — grateful or delighted — gives up the heirloom ring.
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
#    She warns that the wind is "running out of tomorrows."
#
# Rumor chain (pregame, unlocks heirloom_ring):
#   Step 1 — Meet Nia at region bar. She's heard something interesting about
#             scribe_althorin — he has a hidden ledger of favours owed across
#             the grasslands. "Talk around. See what stirs."
#   Step 2 — Party tells Sylvi (fire-dancer, gossip magnet). Sylvi loves it
#             but doesn't deal in leverage. Points to Tess — "tell her, not me."
#   Step 3 — Party finds Tess and Sam together. Tess sees the angle instantly.
#             Sam reads deeper — names Seris as the one to verify the rumor's
#             weight before it goes to a buyer.
#   Step 4 — Party tells oathwarden_seris. She confirms the rumor carries truth
#             (her presence compels honesty) and points to Mira as the one
#             who has been searching for Althorin's ledger.
#   Step 5 — Party tells Mira. She pays with an heirloom ring she held as
#             collateral from a debtor who never returned.
#   Deliver ring to Nia → she joins.

ATTAINABLE_PLAYER_CHARACTERS = [
    {
        ## total power points = 15 + 15 * 29 = 465
        ## total stat points = 10 + 6 * 29 = 184
        'id': 'nia',
        'name': 'Nia',
        'arm_armor': 'stormstep_bracers',
        'head_armor': 'zephyr_hood',
        'body_armor': 'galestride_vest',
        'leg_armor': 'windrunner_greaves',
        'equipped_weapon': 'whisperwind_blades',
        'max_hp': 941,
        'current_hp': 941,
        'max_ap': 350,
        'current_ap': 350,
        'unused_ability_slots': 0,
        'unused_stat_points': 0,
        'unused_power_points': 0,
        'strength': 38,
        'dexterity': 224,
        'intelligence': 38,
        'constitution': 38,
        'level': 30,
        'abilities': [
            'lv2_unique_ability_skill_nia_wind_read',
            'lv2_unique_ability_skill_nia_gale_step',
            'lv3_unique_ability_skill_nia_echo_step',
            'lv3_unique_ability_skill_nia_futures_edge',
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
        },
        'image': 'nia1.jpeg',
        'song_id': 'dog_days_are_over_florence_and_the_machine'
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
        },
        'image': 'bosses:serene1.jpeg'
    }
]

NPC_DIALOG = [
    # ── Nia opening hook ──────────────────────────────────────────────────────
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_intro',
        'dialog': [
            "Hey stranger! You hear that? The wind's whispering wrong.",
            "Serene's been stealing voices and future‑echoes again. She thinks she owns the wind.",
            "I need someone who can shut her down before she steals tomorrow entirely.",
            "(leaning in, grinning) But first — I've got something worth knowing.",
            "Scribe Althorin — dry old archivist, keeps to himself — has a ledger.",
            "Not just any ledger. Favours owed. Names, dates, what they owe and to whom. Across the whole grasslands.",
            "I don't know who wants that more than anyone else alive.",
            "But I know somebody does. Talk around. See what stirs.",
            "The wind always finds the right ear."
        ]
    },
    # ── Party reactions to Nia's rumor hook ───────────────────────────────────
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_nia_rumor_reaction',
        'dialog': [
            "A ledger of favours owed. That's not gossip.",
            "That's a map of every obligation across the grasslands.",
            "Who would want something like that…"
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_nia_rumor_reaction',
        'dialog': [
            "Oh, someone absolutely wants this.",
            "Someone who collects leverage like other people collect furniture.",
            "Let's find out who."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_nia_rumor_reaction',
        'dialog': [
            "Information like that has a specific value to a specific person.",
            "We find that person, we find a transaction.",
            "Let's be methodical about this."
        ]
    },
    # ── Tell Sylvi ────────────────────────────────────────────────────────────
    {
        'npc_id': 'sylvi',
        'dialog_id': 'sylvi_hears_althorin_rumor',
        'dialog': [
            "Althorin's ledger? Oh, that's delicious.",
            "Half the grasslands would kill to know what's in that book.",
            "But me? I just want to watch the drama unfold. I don't deal in leverage — I deal in fire.",
            "(tapping her chin) Tess and Sam, though.",
            "They're usually at the same table. Tell them both.",
            "Tess will see the angle. Sam will see the buyer.",
            "Not me — them."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_sylvi_reaction',
        'dialog': [
            "Tess and Sam. Together.",
            "That's either very efficient or very dangerous."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_sylvi_reaction',
        'dialog': [
            "Sylvi burns bright and moves fast. Those two move quiet.",
            "If she's pointing at them, that's the direction."
        ]
    },
    # ── Tell Tess and Sam (joint scene) ───────────────────────────────────────
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_hears_althorin_rumor',
        'dialog': [
            "(slowly) Althorin's ledger.",
            "Do you have any idea what you're carrying around?",
            "That's a map of every skeleton in every closet from here to the capital.",
            "(glancing at Sam) I could use this. I could absolutely use this.",
            "But I won't."
        ]
    },
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_hears_althorin_rumor',
        'dialog': [
            "(quiet) Don't.",
            "You'd spend it on one play. This is worth more than one play.",
            "(to the party) I've heard Althorin's name twice. Both times in the same breath as 'debts.'",
            "Before this goes anywhere near a buyer, it needs weight behind it.",
            "Seris. The oathwarden.",
            "She'll hear it and know if it's true. Her word on it makes it worth ten times what it is now.",
            "Find her first. Then we talk about who wants it."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_tess_sam_reaction',
        'dialog': [
            "Sam just stopped Tess from burning the asset.",
            "And gave us a better path in the same breath.",
            "Seris. The oathwarden. Okay."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_tess_sam_reaction',
        'dialog': [
            "Tess wanted it. Sam said no.",
            "I've never seen that before.",
            "Whatever Seris's word is worth, it must be significant."
        ]
    },
    # ── Tell Seris ────────────────────────────────────────────────────────────
    {
        'npc_id': 'oathwarden_seris',
        'dialog_id': 'seris_hears_althorin_rumor',
        'dialog': [
            "(a long pause)",
            "Althorin's ledger.",
            "I have heard the name on three separate oaths.",
            "Each time, the speaker's voice changed when they said it.",
            "The way a voice changes when it touches something true.",
            "This is not rumour.",
            "(meeting your eyes) There is one person who has asked me, indirectly, whether such a ledger could be verified.",
            "Mira.",
            "She did not say why. She rarely does.",
            "But she asked whether an oathwarden's word could authenticate a record of debts.",
            "Now you know what she was preparing for.",
            "Go to her. Tell her the ledger exists.",
            "Tell her Seris confirmed its weight."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_seris_reaction',
        'dialog': [
            "She didn't ask us any questions.",
            "She already knew. She was just waiting for someone to bring it to her.",
            "Mira asked an oathwarden whether debts could be authenticated.",
            "She's been building toward this for a while."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_seris_reaction',
        'dialog': [
            "Seris confirmed the rumor's weight with about forty words.",
            "That's the most efficient thing I've witnessed all month.",
            "Okay. Mira."
        ]
    },
    # ── Tell Mira ─────────────────────────────────────────────────────────────
    {
        'npc_id': 'mira',
        'dialog_id': 'mira_hears_althorin_rumor',
        'dialog': [
            "(very still) Say that again.",
            "Althorin's ledger. The real one.",
            "(a beat) Seris confirmed it.",
            "Then it's real.",
            "(quietly, almost to herself) Two years.",
            "I've been looking for proof that ledger existed for two years.",
            "I don't carry gold on me — not the kind this warrants.",
            "But I have something.",
            "A debtor left this with me as collateral. Never came back for it.",
            "An heirloom ring. Old family piece.",
            "I kept it because things like this always find a use eventually.",
            "(sets it on the table) It has one now.",
            "Take it. And if you ever find the ledger itself — you know where I am."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_mira_reaction',
        'dialog': [
            "She went still. Mira went still.",
            "That's the most unsettling thing I've seen all week.",
            "The ring is real though. Let's move."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_mira_reaction',
        'dialog': [
            "A ring held two years from a ghost debt.",
            "The wind really does find the right ear.",
            "Nia's going to love this story."
        ]
    },
    # ── Nia receives the ring, joins ──────────────────────────────────────────
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_heirloom_received',
        'dialog': [
            "(eyes wide) You actually got it.",
            "You went to Sylvi — she sent you to Tess and Sam — Sam sent you to Seris — Seris sent you to Mira.",
            "That is exactly how the wind works.",
            "You didn't push it. You just… followed it.",
            "(laughing softly, then quieter) Mira had it as collateral. Two years. From someone who never came back.",
            "The wind remembers everything it's touched.",
            "That's why I listen to it.",
            "(pocketing the ring carefully) Okay. I owe you.",
            "Also — Serene's been getting louder. She's been stealing echoes from the grasslands for weeks now.",
            "I don't know what she's building toward but I can feel it in every step I take.",
            "I'm not letting her take tomorrow.",
            "Let's go find her."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_nia_join_reaction',
        'dialog': [
            "She mapped the entire gossip chain back by heart.",
            "In order.",
            "I respect the process. The wind thing is real.",
            "Welcome aboard, Nia."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_nia_join_reaction',
        'dialog': [
            "Wind-dancer. Acute environmental awareness. Social network spanning the grasslands.",
            "Underrated intelligence asset.",
            "Grudging respect."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_nia_join_reaction',
        'dialog': [
            "Nia moves like the wind she dances with.",
            "I want to spar with her eventually.",
            "Just to see."
        ]
    },
    # ── Serene confrontation ──────────────────────────────────────────────────
    {
        'npc_id': 'serene',
        'dialog_id': 'serene_intro',
        'dialog': [
            "A new voice approaches… I'll take it.",
            "The wind has no future left — only what I choose.",
            "You carry echoes of tomorrow with you.",
            "Interesting. I wonder what they're worth."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_serene_confrontation',
        'dialog': [
            "Serene.",
            "You've been stealing from the wind for years. Voices, futures — things that were never yours.",
            "(quiet, hard) The wind showed me something once. My moment.",
            "I've been running from it.",
            "But I'm done running from you."
        ]
    },
    {
        'npc_id': 'serene',
        'dialog_id': 'serene_confrontation_reply',
        'dialog': [
            "Running. Yes. The wind told me about you too, dancer.",
            "You heard your own end in it and you've been sprinting ever since.",
            "I took that echo, you know. I have it.",
            "Surrender now and I won't show it to your friends."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_serene_challenge',
        'dialog': [
            "She's threatening us with a wind whisper.",
            "Here's a thought — no.",
            "Nia's future is hers. Give it back."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_serene_challenge',
        'dialog': [
            "We've heard enough.",
            "End it."
        ]
    },
    # ── Serene defeat ─────────────────────────────────────────────────────────
    {
        'npc_id': 'serene',
        'dialog_id': 'serene_defeat',
        'dialog': [
            "My echoes… scattered…",
            "Tomorrow… slips away…",
            "The wind doesn't belong to anyone. Not even me.",
            "Not even… you."
        ]
    },
    # ── Post-defeat scene ─────────────────────────────────────────────────────
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_post_defeat',
        'dialog': [
            "(very quiet) She had it.",
            "My echo. She actually had it.",
            "I don't know if destroying her scattered it back into the wind or just… ended it.",
            "(pause)",
            "I think I'm okay with not knowing.",
            "Come on. The wind sounds like itself again."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_post_defeat',
        'dialog': [
            "She said the wind doesn't belong to anyone.",
            "Even at the end she was more interested in being right than in winning.",
            "I'll give her that much."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_post_defeat',
        'dialog': [
            "Nia held.",
            "Whatever she heard in the wind — she didn't let it stop her today."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_post_defeat',
        'dialog': [
            "The echo is gone. Tomorrow's open again.",
            "Let's keep moving before something else decides to steal it."
        ]
    },
]

DUNGEONS = []

TASKS = [
    # ── Initialize — Nia appears at the region bar ────────────────────────────
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
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'nia',
                    'standing_text': [
                        "I heard something worth knowing. Come find me.",
                        "The wind always finds the right ear — let's see if yours are good."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_primary_meet_nia_rumor'
                }
            }
        ]
    },

    # ── Step 1: Meet Nia — she plants the Althorin rumor ─────────────────────
    {
        'task_id': 'grassland_primary_meet_nia_rumor',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'nia',
        'task_acquire_events': [
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
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_nia_rumor_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_nia_rumor_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_nia_rumor_reaction'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'nia',
                    'standing_text': [
                        "Talk around. See what stirs.",
                        "You're carrying something valuable — somebody knows exactly what to do with it.",
                        "Start with Sylvi. She knows everyone."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_primary_tell_sylvi'
                }
            }
        ]
    },

    # ── Step 2: Tell Sylvi ────────────────────────────────────────────────────
    {
        'task_id': 'grassland_primary_tell_sylvi',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'sylvi',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'sylvi',
                    'dialog_id': 'sylvi_hears_althorin_rumor'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_sylvi_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_sylvi_reaction'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'sylvi',
                    'standing_text': [
                        "Tess and Sam are usually at the same table. Tell them both.",
                        "Tess will see the angle. Sam will see the buyer.",
                        "Not me — them."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_primary_tell_tess_and_sam'
                }
            }
        ]
    },

    # ── Step 3: Tell Tess and Sam (joint scene) ───────────────────────────────
    {
        'task_id': 'grassland_primary_tell_tess_and_sam',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'tess',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'tess',
                    'dialog_id': 'tess_hears_althorin_rumor'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'sam',
                    'dialog_id': 'sam_hears_althorin_rumor'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_tess_sam_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_tess_sam_reaction'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'tess',
                    'standing_text': [
                        "Seris first. Her word turns rumour into leverage.",
                        "Once she confirms it, then we talk about who actually wants the ledger."
                    ]
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'sam',
                    'standing_text': [
                        "Seris. The oathwarden. She'll hear the ledger and know if it's true.",
                        "Her confirmation is what makes it worth carrying further. Find her."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_primary_tell_seris'
                }
            }
        ]
    },

    # ── Step 4: Tell Seris — she verifies the rumor's weight ─────────────────
    {
        'task_id': 'grassland_primary_tell_seris',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'oathwarden_seris',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'oathwarden_seris',
                    'dialog_id': 'seris_hears_althorin_rumor'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_seris_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_seris_reaction'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'oathwarden_seris',
                    'standing_text': [
                        "Mira has been searching for Althorin's ledger.",
                        "She asked me whether an oathwarden's word could authenticate a record of debts.",
                        "Now you know what she was preparing for.",
                        "Go to her. Tell her the ledger exists."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_primary_tell_mira'
                }
            }
        ]
    },

    # ── Step 5: Tell Mira — she gives the heirloom ring ──────────────────────
    {
        'task_id': 'grassland_primary_tell_mira',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'mira',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'mira',
                    'dialog_id': 'mira_hears_althorin_rumor'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_mira_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_mira_reaction'
                }
            },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'heirloom_ring'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'mira',
                    'standing_text': [
                        "I don't carry gold on me — not the kind this warrants.",
                        "But I have something. A debtor left this with me as collateral. Never came back for it.",
                        "An heirloom ring. Old family piece. I kept it because things like this always find a use eventually.",
                        "It has one now."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_primary_meet_nia'
                }
            }
        ]
    },

    # ── Deliver heirloom ring to Nia — she joins here ─────────────────────────
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
                        "You found it! Bring it here — I knew the wind would lead you right."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'nia',
                    'dialog_id': 'nia_heirloom_received'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_nia_join_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_nia_join_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_nia_join_reaction'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {'npc_id': 'nia'}
            },
            {
                'event_type': 'character_join',
                'params': {'character_id': 'nia'}
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'grassland_primary_defeat_serene'
                }
            }
        ]
    },

    # ── Meet Serene in dungeon — full confrontation scene ────────────────────
    {
        'task_id': 'grassland_primary_defeat_serene',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'serene',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'serene',
                    'location': None
                }
            },
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'serene_lair',
                    'location': 'region_open_area'
                }
            },
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'serene_lair', 'item_id': 'glacial_spear', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'serene_lair', 'item_id': 'whisperwind_blades', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'serene_lair', 'item_id': 'glacial_crown', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'serene_lair', 'item_id': 'zephyr_hood', 'location': 'treasure_room' }},
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
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'nia',
                    'dialog_id': 'nia_serene_confrontation'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'serene',
                    'dialog_id': 'serene_confrontation_reply'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_serene_challenge'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'technique',
                    'dialog_id': 'chock_serene_challenge'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'serene',
                    'standing_text': [
                        "The wind has no future left — only what I choose.",
                        "You carry echoes of tomorrow with you. Interesting. I wonder what they're worth."
                    ]
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

    # ── Defeat Serene — post-defeat void hint + Nia arc resolution ────────────
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
            {
                'event_type': 'hide_npc',
                'params': {'npc_id': 'serene'}
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'nia',
                    'dialog_id': 'nia_post_defeat'
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
                    'npc_id': 'skill',
                    'dialog_id': 'poise_post_defeat'
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
                'event_type': 'complete_region_quest',
                'params': {'region_id': 'grassland'}
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