# ============================================================
# = CHAPTER 6 : THE RIFTLANDS UNVEILED
# ============================================================
#
# [ LOCATION — BLEAKWATCH OUTPOST / RIFTLANDS ]
# -----------------------------------
# @ = player
# S = Seth
# C = Rhett
# A = Riftspawn Aberrant
#
# High level: The player meets with Seth, who reveals he is part of a
# resistance fighting the collapse. The player is sent to clear a
# breach site, defeats a Riftspawn Aberrant, and learns that the
# airship requires regional stabilization before it can be used.

ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
    {
        'npc_id': 'rhett',
        'name': 'Rhett',
        'description': (
            'A grim and weary operative of the resistance.'
            ' He is focused and pragmatic, with little time for pleasantries.'
        ),
        "psychology": {
            "mbti": "ISTP",
            "dominant": "Ti — Analyzes situations with detached logic, focusing on the immediate problem and the most practical solution.",
            "auxiliary": "Se — Highly aware of the physical environment and reacts quickly to immediate threats. Action-oriented and hands-on.",
            "tertiary": "Ni — Has a background sense of the larger pattern of collapse but prefers to focus on tangible, solvable issues.",
            "inferior": "Fe — Uncomfortable with overt emotional displays and can seem blunt or detached. Values competence over charisma."
        },
        "enneagram": {
          "enneagram_type": "5w6",
          "core_fear": "Being useless, helpless, or incompetent.",
          "core_desire": "To be capable and competent in his domain.",
          "defense_mechanism": "Isolation — Withdraws into his workshop, finding safety and control in understanding and fixing machines rather than dealing with people.",
          "stress_line": "Moves to Type 7 — Becomes scattered and anxious when faced with a problem he can't immediately solve.",
          "growth_line": "Moves to Type 8 — Uses his expertise to take confident, decisive action in the world.",
          "instinctual_variant": "sp/sx — His self-preservation is ensured by his mastery of his craft; he engages intensely with any mechanical puzzle."
        },
        'image': 'npcs:rhett1'
    },
    {
        'npc_id': 'riftspawn_aberrant',
        'name': 'Riftspawn Aberrant',
        'description': (
            'A horrifying creature that crawled out of a reality breach.'
            ' It is a chaotic mass of limbs and distorted energy, screeching with alien pain and rage.'
        ),
        "psychology": {
            "mbti": "ESTP",
            "dominant": "Se — A being of pure, chaotic action. It reacts violently and instinctively to everything in its environment.",
            "auxiliary": "Ti — Its movements, while seemingly random, follow a predatory logic aimed at maximizing destruction.",
            "tertiary": "Fe — Expresses itself through raw, terrifying displays of aggression that project its fractured nature onto its surroundings.",
            "inferior": "Ni — Lacks any sense of future or consequence, driven only by the immediate impulse to unmake and destroy."
        },
        "enneagram": {
          "enneagram_type": "7w8",
          "core_fear": "Being trapped, bored, or in pain.",
          "core_desire": "To stay free and stimulated by constant action and adventure.",
          "defense_mechanism": "Rationalization — Frames his reckless diving as a thrilling job, ignoring the immense danger and his own fear.",
          "stress_line": "Moves to Type 1 — Becomes rigid and critical when things don't go his way or he feels trapped.",
          "growth_line": "Moves to Type 5 — Becomes more thoughtful and strategic, learning to assess risks instead of just chasing thrills.",
          "instinctual_variant": "sx/sp — Seeks intense, high-stakes experiences and one-on-one challenges to feel alive."
        },
        'image': 'bosses:riftspawn_aberrant1'
    }
]

NPC_DIALOG = [
    {
        'npc_id': None,
        'dialog_id': 'ch6_narrator_intro',
        'dialog': [
            "Chapter 6 - Life, left to itself, tends toward chaos… unless something holds it together."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_resistance_reveal',
        'dialog': [
            "Oh hey! You made it. Didn't think you'd get across the Riftwaters in one piece. Look… I didn't tell you everything. I'm part of a group. A resistance. We're trying to stop the collapse."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch6_after_seth_reveal',
        'dialog': [
            "You doubted us? I'm offended."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch6_after_seth_reveal',
        'dialog': [
            "You? In a resistance?"
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_useful',
        'dialog': [
            "Yeah yeah, laugh it up. I'm useful sometimes."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch6_after_seth_reveal',
        'dialog': [
            "Define \"useful.\""
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_i_know_people',
        'dialog': [
            "…I know people."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch6_after_seth_reveal',
        'dialog': [
            "Seth, if you're trying to help, we're grateful. Even if your methods are… unconventional."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_kaera_gets_it',
        'dialog': [
            "See? Kaera gets it."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch6_to_seth',
        'dialog': [
            "She's being polite. Don't get excited."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_contact_intro',
        'dialog': [
            "I have a contact who can help you investigate the breach. Meet him at the city outskirts bar."
        ]
    },
    {
        'npc_id': 'rhett',
        'dialog_id': 'contact_ch6_intro',
        'dialog': [
            "You're the outsiders Seth told me about. Good. We need hands. Something is stirring in the wilds. Something that's twisting the land."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch6_after_contact',
        'dialog': [
            "Wonderful. More unstable terrain. Exactly what I wanted today."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch6_after_contact',
        'dialog': [
            "Alright. Unstable ground means we stay sharp and move smart. Let’s get this done right."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch6_after_contact',
        'dialog': [
            "We should move carefully. Something here feels… off. Like the land itself is unsettled."
        ]
    },
    {
        'npc_id': 'rhett',
        'dialog_id': 'contact_ch6_response',
        'dialog': [
            "…You people are strange."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch6_after_contact',
        'dialog': [
            "Thank you. We try."
        ]
    },
    {
        'npc_id': 'riftspawn_aberrant',
        'dialog_id': 'aberrant_ch6_intro',
        'dialog': [
            "*distorted screeching*"
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch6_aberrant_intro',
        'dialog': [
            "Oh that's disgusting. I love it."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch6_aberrant_intro',
        'dialog': [
            "It's got too many limbs. I'm taking some off."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch6_aberrant_intro',
        'dialog': [
            "Look at it bend reality! Adorable."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch6_aberrant_intro',
        'dialog': [
            "Focus. It's predicting our movements."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch6_aberrant_intro',
        'dialog': [
            "Its aura is fractured… like it's in pain."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch6_after_aberrant',
        'dialog': [
            "This creature… it was shaped by the same force that warped the Riftwaters."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch6_after_aberrant',
        'dialog': [
            "And now it's shaped like paste."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch6_after_aberrant',
        'dialog': [
            "Good fight... Weird fight. But good."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch6_after_aberrant',
        'dialog': [
            "I want a sample. Nobody touch anything."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch6_after_aberrant',
        'dialog': [
            "Too late. Moxie touched it."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch6_after_aberrant_2',
        'dialog': [
            "You know I can't resist touching things."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_report_findings',
        'dialog': [
            "So it's true… the Riftlands are destabilizing faster than we thought. And if the Bracelet of Existence is here… someone is using it."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch6_bracelet_theory',
        'dialog': ["Or wearing it as jewelry."]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch6_bracelet_theory',
        'dialog': ["Or weaponizing it."]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch6_bracelet_theory',
        'dialog': ["Or losing control of it."]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch6_bracelet_theory',
        'dialog': ["Whatever the case, we must find it."]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_airship_reveal',
        'dialog': [
            "Either way… we're gonna need my airship."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch6_airship_reveal',
        'dialog': [
            "You have an airship?"
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_airship_confirm',
        'dialog': [
            "…Yes?"
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch6_airship_reveal',
        'dialog': [
            "Oh this is going to be FUN."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_stabilization_1',
        'dialog': [
            "Alright, cards on the table. My crew and I? We're trying to stop the collapse. The rifts, the storms, the distortions…",
            "they're all connected."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_stabilization_2',
        'dialog': [
            "The Riftlands are unstable. Too unstable. If we try to fly without stabilizing the region…",
            "the airship will tear itself apart."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_stabilization_3',
        'dialog': [
            "That Riftland Stabilizer Core looks like it may be useful in strengthing the Rustwing against these storms.",
            "Let me take it off your hands to make a few upgrades."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_stabilization_4',
        'dialog': [
            "There are seven local resistance members.",
            "Each one holds things together in their local region. Help them, and the land stabilizes.",
            "Ignore them, and we all die horribly. You can find them in city outskirt bars."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_stabilization_5',
        'dialog': [
            "I'm not taking off until all seven are handled.",
            "You want to find that bracelet? Earn it."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch6_after_seth_quest',
        'dialog': [
            "We suspected as much. Patterns don't break themselves. Someone breaks them."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch6_after_seth_quest',
        'dialog': [
            "Ooooh, a secret resistance? Seth, you should've led with that. I love a dramatic reveal."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch6_after_seth_quest',
        'dialog': [
            "Hah! I knew you were hiding something. You've got that shifty look."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch6_after_seth_quest',
        'dialog': [
            "If your intentions are righteous, then we stand with you. But deception breeds danger."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch6_after_seth_quest',
        'dialog': [
            "Just tell us the plan before Chock punches the wrong person again."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch6_after_seth_quest_2',
        'dialog': [
            "So we fix the region. Great. Add \"world maintenance\" to our job list."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch6_after_seth_quest_2',
        'dialog': [
            "If the airship explodes mid‑flight, I call dibs on haunting Seth."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch6_after_seth_quest_2',
        'dialog': [
            "A machine cannot run on broken parts. Neither can a world."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch6_after_seth_quest_3',
        'dialog': [
            "Motivating. Nothing like imminent doom to get the blood pumping."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch6_after_seth_quest_2',
        'dialog': [
            "Seven heroes? Sounds like seven fights. I'm in."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch6_after_seth_quest_2',
        'dialog': [
            "These guardians must be under great strain. We should aid them swiftly."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch6_after_seth_quest_3',
        'dialog': [
            "Let's just hope they're competent. I'm tired of cleaning up after amateurs."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch6_after_seth_quest_4',
        'dialog': [
            "Ugh, homework. Fine."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch6_after_seth_quest_3',
        'dialog': [
            "Seven? Easy. I'll do eight just to show off."
        ]
    },
    # ── Type A hook dialogs ────────────────────────────────────────
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_local_errand',
        'dialog': [
            "Before I hand you off to my contact — I need something from you first.",
            "Karrek Windbreak. Watchman stationed at the outpost's storm post.",
            "He's been tracking something in those hollow wind-channels near the breach site.",
            "I can't brief my contact properly without knowing what Karrek saw.",
            "Talk to him. Come back to me with what he found."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_still_waiting',
        'dialog': [
            "You talk to Karrek yet?",
            "I need that storm report before I can send you to my contact.",
            "He's at the storm post. Won't take long."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch6_karrek_done',
        'dialog': [
            "Good. That's what I needed.",
            "Now I can brief him properly.",
            "My contact's at the city outskirts bar. His name's Rhett. Tell him Seth sent you."
        ]
    },
]

TASKS = [
    {
        'task_id': 'main_story_ch6_meet_seth',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'seth',
        'task_acquire_events': [
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'seth', 'location': 'region_city_bar' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch6_narrator_intro' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_resistance_reveal' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch6_after_seth_reveal' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch6_after_seth_reveal' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_useful' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch6_after_seth_reveal' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_i_know_people' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch6_after_seth_reveal' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_kaera_gets_it' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch6_to_seth' }},
            # ── Type A hook: Seth sends them to Karrek before handing off contact ──
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_local_errand' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'seth', 'standing_text': ["Talk to Karrek at the storm post first. Then I'll send you to my contact."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch6_check_back_with_seth' }},
        ]
    },
    # ── New task: check back with Seth after Karrek ─────────────────
    {
        'task_id': 'main_story_ch6_check_back_with_seth',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'seth',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_still_waiting' },
              'condition': { 'type': 'is_task_not_active', 'params': { 'task_id': 'snow_small_city_type_a_ch6_meet_karrek' }}},
            { 'event_type': 'remove_task', 'params': { 'task_id': 'main_story_ch6_check_back_with_seth' },
              'condition': { 'type': 'is_task_not_active', 'params': { 'task_id': 'snow_small_city_type_a_ch6_meet_karrek' }}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch6_check_back_with_seth' },
              'condition': { 'type': 'is_task_not_active', 'params': { 'task_id': 'snow_small_city_type_a_ch6_meet_karrek' }}},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_karrek_done' },
              'condition': { 'type': 'is_task_completed', 'params': { 'task_id': 'snow_small_city_type_a_ch6_meet_karrek' }}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch6_meet_seth_local_contact' },
              'condition': { 'type': 'is_task_completed', 'params': { 'task_id': 'snow_small_city_type_a_ch6_meet_karrek' }}},
        ]
    },
    {
        'task_id': 'main_story_ch6_meet_seth_local_contact',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rhett',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'rhett', 'location': 'region_bar' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rhett', 'dialog_id': 'contact_ch6_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch6_after_contact' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch6_after_contact' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch6_after_contact' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rhett', 'dialog_id': 'contact_ch6_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch6_after_contact' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rhett', 'standing_text': ["Clear the breach site. Something crawled out of it, and we need it stopped."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch6_meet_riftspawn_aberrant' }}
        ]
    },
    {
        'task_id': 'main_story_ch6_meet_riftspawn_aberrant',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'riftspawn_aberrant',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'riftspawn_aberrant', 'location': None }},
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'riftland_breach_site', 'location': 'region_open_area' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'riftspawn_aberrant', 'dialog_id': 'aberrant_ch6_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch6_aberrant_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch6_aberrant_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch6_aberrant_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch6_aberrant_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch6_aberrant_intro' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch6_defeat_riftspawn_aberrant' }}
        ]
    },
    {
        'task_id': 'main_story_ch6_defeat_riftspawn_aberrant',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'riftspawn_aberrant_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'riftspawn_aberrant_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'riftspawn_aberrant' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch6_after_aberrant' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch6_after_aberrant' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch6_after_aberrant' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch6_after_aberrant' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch6_after_aberrant' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch6_after_aberrant_2' }},
            { 'event_type': 'award_item', 'params': { 'item_id': 'riftland_stabilizer_core' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch6_report_to_seth' }}
        ]
    },
    {
        'task_id': 'main_story_ch6_report_to_seth',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'seth',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_report_findings' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch6_bracelet_theory' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch6_bracelet_theory' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch6_bracelet_theory' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch6_bracelet_theory' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_airship_reveal' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch6_airship_reveal' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_airship_confirm' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch6_airship_reveal' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_stabilization_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch6_after_seth_quest' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch6_after_seth_quest' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch6_after_seth_quest' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch6_after_seth_quest' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch6_after_seth_quest' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_stabilization_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch6_after_seth_quest_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch6_after_seth_quest_2' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_stabilization_3' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch6_after_seth_quest_2' }},
            { 'event_type': 'remove_item', 'params': { 'item_id': 'riftland_stabilizer_core' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_stabilization_4' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch6_after_seth_quest_3' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch6_after_seth_quest_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch6_after_seth_quest_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch6_after_seth_quest_3' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch6_stabilization_5' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch6_after_seth_quest_4' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch6_after_seth_quest_3' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'seth', 'standing_text': ["I'll prepare the airship. But we need to stabilize the region first."]}},
            { 'event_type': 'advance_chapter' }
        ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_6',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}