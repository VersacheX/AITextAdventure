# ============================================================
# = CHAPTER 5 : RIFTWATERS CROSSING
# ============================================================
#
# [ NEW CITY — RIFTFALL / STORMS ]
# -----------------------------------
# @ = player
# K = Kirn (magic courier)
# V = Velka (occult cartographer)
# S = Sylvi (performer)
# A = Astra Wynn (riftcaller)
# D = Dorian Pikefall (collector)
#
# High level: The player traces the signal from the second bracelet
# across the dangerous Riftwaters, requiring the help of a specialist
# to teleport. They arrive to find the bracelet was stolen.

ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
    {
        'npc_id': 'astra_wynn',
        'name': 'Astra Wynn',
        'description': (
            'A reckless and powerful Riftcaller who walks through reflections instead of doorways.'
            ' She treats reality as a suggestion and enjoys the chaos of the unknown.'
        ),
        "psychology": {
            "mbti": "ENTP",
            "dominant": "Ne — Sees reality as a web of possibilities to be explored and manipulated. Thrives on novelty and unpredictability.",
            "auxiliary": "Ti — Understands the internal logic of rifts and teleportation, even if she can’t explain it in conventional terms. Her methods are experimental but precise.",
            "tertiary": "Fe — Uses a detached, almost playful charm to interact with others. Her confidence is both unsettling and reassuring.",
            "inferior": "Si — Dislikes stability and routine. Under stress, she might become fixated on a minor, irrelevant detail or past failure."
        },
        "enneagram": {
          "enneagram_type": "7w8",
          "core_fear": "Being trapped, limited, or bored by a stable, predictable reality.",
          "core_desire": "To stay free and stimulated by exploring the unknown.",
          "defense_mechanism": "Rationalization — Frames reckless reality-bending as 'fun' and 'interesting' to avoid the inherent danger and fear.",
          "stress_line": "Moves to Type 1 — Becomes rigid and critical when her methods are questioned or her freedom is threatened.",
          "growth_line": "Moves to Type 5 — Becomes more focused and deeply knowledgeable about the mechanics of rifts, not just the thrill of them.",
          "instinctual_variant": "sx/so — Seeks intense, one-on-one experiences with the fabric of reality, and enjoys showing off her unique abilities."
        },
        'image': 'npcs:astra_wynn1'
    },
    {
        'npc_id': 'dorian_pikefall',
        'name': 'Dorian Pikefall',
        'description': (
            'A well-meaning but perpetually anxious collector of rare artifacts.'
            ' He seems to have a talent for being in the wrong place at the worst possible time.'
        ),
        "psychology": {
            "mbti": "ISFJ",
            "dominant": "Si — Relies on his detailed knowledge of artifacts and their histories. He is meticulous and values the known over the unknown.",
            "auxiliary": "Fe — Expresses his anxiety and fear openly. He is polite and seeks harmony, even when terrified.",
            "tertiary": "Ti — Can logically recount the details of events, even when panicked. He tries to make sense of his misfortune.",
            "inferior": "Ne — Becomes overwhelmed by catastrophic possibilities and future uncertainties, leading to his constant state of anxiety."
        },
        "enneagram": {
          "enneagram_type": "6w7",
          "core_fear": "Being without support, security, or guidance.",
          "core_desire": "To feel secure and supported.",
          "defense_mechanism": "Projection — Projects his intense anxiety onto the world, seeing threats everywhere and seeking authority figures to protect him.",
          "stress_line": "Moves to Type 3 — Becomes frantic and obsessed with appearances, trying to look competent while panicking.",
          "growth_line": "Moves to Type 9 — Becomes more trusting and calm, able to handle uncertainty without constant fear.",
          "instinctual_variant": "sp/so — Obsessed with his own safety and security, which he tries to ensure through social status and alliances."
        },
        'image': 'npcs:dorian_pikefall1'
    },
    {
        'npc_id': 'static_wraith',
        'name': 'Static Wraith',
        'description': (
            'A restless spirit born from the chaotic energy of the Riftwaters. It hums with static electricity and is drawn to sources of power.'
            ' It is aggressive and territorial, attacking anything that comes too close.'
        ),
        "psychology": {
            "mbti":      "N/A",
            "dominant":  "N/A",
            "auxiliary": "N/A",
            "tertiary":  "N/A",
            "inferior":  "N/A",
        },
        "enneagram": {
            "enneagram_type":       "N/A",
            "core_fear":            "N/A",
            "core_desire":          "N/A",
            "defense_mechanism":    "N/A",
            "stress_line":          "N/A",
            "growth_line":          "N/A",
            "instinctual_variant":  "N/A",
        },
        'image': 'bosses:static_wraith1'
    }
]

NPC_DIALOG = [
    {
        'npc_id': None,
        'dialog_id': 'ch5_narrator_intro',
        'dialog': [
            "Chapter 5 - Life can only be understood backward… but it must be lived forward."
        ]
    },
    {
        'npc_id': 'kirn',
        'dialog_id': 'kirn_ch5_tracking_signal',
        'dialog': [
            "You're back… good. I was hoping the signal wasn't a fluke. I placed a tracking sigil on the Bracelet of Existence.",
            "After the fracture, the sigil went dead… until now.",
            "It's faint, but it's there… and it's coming from somewhere across the Riftwaters.",
            "Velka can trace the signal with her maps. Go speak to her."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch5_after_kirn',
        'dialog': [
            "A ghost signal waking up after everything went to hell? Now that's interesting. I wonder what else decided to come back online..."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch5_after_kirn',
        'dialog': [
            "Across the Riftwaters, huh? Sounds like a pain in the ass already. But if that's where the bracelet is, then that's where we're going."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch5_after_kirn',
        'dialog': [
            "Great. Another unstable crossing. Just what we needed. At least we have a lead instead of wandering blind again."
        ]
    },
    {
        'npc_id': 'velka',
        'dialog_id': 'velka_ch5_map_signal',
        'dialog': [
            "The world has changed more than you know. Continents have split, merged, and rewritten themselves.",
            "The signal you're chasing lies beyond the Riftwaters… storms that tear reality apart.",
            "I can give you the map of the signal's location, but teleportation is the only way to reach it."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch5_after_velka',
        'dialog': [
            "Then we must find someone who can cross storms without crossing the sea."
        ]
    },
    {
        'npc_id': 'kirn',
        'dialog_id': 'kirn_ch5_suggests_sylvi',
        'dialog': [
            "Sylvi Emberlane might know someone."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch5_after_velka',
        'dialog': [
            "Storms that tear reality apart… sounds like a warm‑up."
        ]
    },
    {
        'npc_id': 'sylvi',
        'dialog_id': 'sylvi_ch5_riftcaller_intro',
        'dialog': [
            "Teleportation across the Riftwaters? Oh honey… that's not something you ask just anyone.",
            "But I might know someone who knows someone. There's a woman. A Riftcaller.",
            "She doesn't walk through doors — she walks through reflections. Name's Astra Wynn.",
            "She won't talk to strangers. But she owes me a favor. Bring me my Stormglass Ember, and I'll call her."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch5_after_sylvi',
        'dialog': [
            "A reflection-walker? Now that sounds like real power. I’d love to see how that works."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch5_after_sylvi',
        'dialog': [
            "Everything in this damn world is either trying to kill us, mess with our heads, or both. Starting to get real tired of it."
        ]
    },
    {
        'npc_id': 'sylvi',
        'dialog_id': 'sylvi_ch5_response_to_technique',
        'dialog': [
            "(laughs) That’s the spirit of the place, big guy. Keeps things interesting, doesn’t it?"
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch5_static_wraiths',
        'dialog': [
            "These bastards are damn annoying. Like angry lightbulbs that don’t know when to die."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch5_static_wraiths',
        'dialog': [
            "That humming… it’s completely off. Sets my teeth on edge. I really don’t like it."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch5_static_wraiths',
        'dialog': [
            "Of course they hum. They’re literally made of static. What did you expect, opera?"
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch5_static_wraiths',
        'dialog': [
            "Stay focused. They’re fast, don’t let them flank you."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch5_defeated_static_wraiths',
        'dialog': [
            "Finally. Those things were a real pain in the ass. Felt like fighting a swarm of pissed-off hornets made of lightning."
        ]
    },
    
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch5_defeated_static_wraiths',
        'dialog': [
            "Look at this… the Stormglass Ember. Still warm. You can feel the residual energy pulsing through it. Beautiful."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch5_defeated_static_wraiths',
        'dialog': [
            "Yeah, beautiful. Just don’t drop it. Last thing we need is another reality-tearing accident because we broke the wrong shiny object."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch5_defeated_static_wraiths',
        'dialog': [
            "It’s stable for now. We should get it back to Sylvi before anything else decides to crawl out of these alleys."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch5_defeated_static_wraiths_2',
        'dialog': [
            "Agreed. I’ve had enough of this place."
        ]
    },

    {
        'npc_id': 'sylvi',
        'dialog_id': 'sylvi_ch5_receives_ember',
        'dialog': [
            "You actually found it. Good. Try not to drop it — it bites."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch5_narrator_ember_fractures',
        'dialog': [
            "Sylvi whispers into the ember. It fractures into mirrored shards. The air ripples."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch5_ember_fractures',
        'dialog': [
            "Ohhh that's pretty. Do it again."
        ]
    },
    {
        'npc_id': 'sylvi',
        'dialog_id': 'sylvi_ch5_ember_fractures_response',
        'dialog': [
            "If I do it again, reality might fold in half."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch5_ember_fractures_response',
        'dialog': [
            "...Do it again."
        ]
    },
    {
        'npc_id': 'astra_wynn',
        'dialog_id': 'astra_ch5_intro',
        'dialog': [
            "Sylvi. You called."
        ]
    },
    {
        'npc_id': 'sylvi',
        'dialog_id': 'sylvi_ch5_request_riftcall',
        'dialog': [
            "They need a Riftcall. Across the Riftwaters."
        ]
    },
    {
        'npc_id': 'astra_wynn',
        'dialog_id': 'astra_ch5_agrees',
        'dialog': [
            "Dangerous. Reckless. I like it. I can anchor to the signal you're chasing. No amplifiers needed — but the jump won't be gentle."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch5_after_astra',
        'dialog': [
            "Gentle hasn't been on the menu for a while."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch5_after_astra',
        'dialog': [
            "We trust your guidance."
        ]
    },
    {
        'npc_id': 'astra_wynn',
        'dialog_id': 'astra_ch5_warning',
        'dialog': [
            "Oh, don't. I barely trust myself. Stand still. The Riftwaters distort identity.",
            "Try not to think about who you were. I will anchor you to the signal's echo.",
            "Where you land… depends on how well reality cooperates."
        ]
    },
    {
        'npc_id': 'astra_wynn',
        'dialog_id': 'astra_ch5_teleporting_to_highsteeple_crossing',
        'dialog': [
            "Hold on tight. This is going to be a bumpy ride."
        ]
    },
    {
        'npc_id': 'astra_wynn',
        'dialog_id': 'astra_ch5_teleporting_to_brinewood_harbor',
        'dialog': [
            "Here we go. Don't forget to scream if you see something scary."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch5_before_riftcall',
        'dialog': [
            "Reality never cooperates. That's why it's fun."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch5_before_riftcall',
        'dialog': [
            "Quiet your mind. Or at least try."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch5_narrator_riftcall',
        'dialog': [
            "The world folds. The sky bends. Reality snaps sideways."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch5_after_riftcall',
        'dialog': [
            "Teleported straight into a fight. Figures."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch5_after_riftcall',
        'dialog': [
            "The rift welcomed us with open teeth."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch5_after_riftcall',
        'dialog': [
            "I think my spine inverted for a second."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch5_after_riftcall',
        'dialog': [
            "Stay close. This place feels… wrong."
        ]
    },
    {
        'npc_id': 'dorian_pikefall',
        'dialog_id': 'dorian_ch5_intro',
        'dialog': [
            "Oh thank the stars! Actual people! You're not thieves, are you? Please tell me you're not here to rob me too..."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch5_after_dorian',
        'dialog': [
            "Honestly, would we tell you if we were?"
        ]
    },
    {
        'npc_id': 'dorian_pikefall',
        'dialog_id': 'dorian_ch5_explains_1',
        'dialog': [
            "I— I'm Dorian Pikefall. Collector. Traveler. Victim of extremely poor timing."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch5_after_dorian',
        'dialog': [
            "He's cute when he's terrified."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch5_after_dorian',
        'dialog': [
            "He looks like he's always terrified."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch5_after_dorian_2',
        'dialog': [
            "Please be gentle with him. He's clearly been through something."
        ]
    },
    {
        'npc_id': 'dorian_pikefall',
        'dialog_id': 'dorian_ch5_explains_2',
        'dialog': [
            "I had it... The Bracelet of Existence. I was transporting it for a client. Then it was stolen from me near the breach site.",
            "Some shimmering distortion... like a tear in the air. It just took it."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch5_after_dorian',
        'dialog': [
            "His pulse is erratic. He's telling the truth."
        ]
    },
    {
        'npc_id': 'dorian_pikefall',
        'dialog_id': 'dorian_ch5_outro_1',
        'dialog': [
            "The storms… they're getting worse. The sky cracked open last night. I heard voices in the thunder."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch5_after_dorian_3',
        'dialog': [
            "The land cries out. Something is deeply wrong here."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch5_after_dorian_2',
        'dialog': [
            "Good. I was getting bored."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch5_after_dorian_2',
        'dialog': [
            "Voices in the thunder? Ooooh, maybe they're hiring."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch5_after_dorian_2',
        'dialog': [
            "Or maybe it's the sound of the world dying. Again."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch5_after_dorian_2',
        'dialog': [
            "Stay alert. The air tastes wrong. Like metal and memory."
        ]
    },
    {
        'npc_id': 'dorian_pikefall',
        'dialog_id': 'dorian_ch5_outro_2',
        'dialog': [
            "If you're looking for answers about that bracelet... you should talk to Seth.",
            "He's usually at the bar in Bleakwatch Outpost. Sketchy type, but he knows things."
        ]
    }
]

TASKS = [
    {
        'task_id': 'main_story_ch5_return_to_kirn',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'kirn',
        'task_acquire_events': [
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'velka', 'standing_text': ["The maps are shifting. Something is twisting the city's shape."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'drin', 'standing_text': ["My illusions are becoming real. It's that bracelet Kirn has."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'marlo_finch', 'standing_text': ["That bracelet is a ledger of collapse. I need to audit it."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'sylvi', 'standing_text': ["Looking for a way across the Riftwaters? Not many can make that journey."]}},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch5_narrator_intro' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'kirn', 'dialog_id': 'kirn_ch5_tracking_signal' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch5_after_kirn' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch5_after_kirn' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch5_after_kirn' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'kirn', 'standing_text': ["Talk to Velka about following the tracking sigil, she knows things."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch5_meet_velka' }}
        ]
    },
    {
        'task_id': 'main_story_ch5_meet_velka',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'velka',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'velka', 'dialog_id': 'velka_ch5_map_signal' }},
            { 'event_type': 'award_item', 'params': { 'item_id': 'tracking_map' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch5_after_velka' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'kirn', 'dialog_id': 'kirn_ch5_suggests_sylvi' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch5_after_velka' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'velka', 'standing_text': ["The signal is across the Riftwaters. You'll need more than a map to get there. Find Sylvi Emberlane."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch5_meet_sylvi' }}
        ]
    },
    {
        'task_id': 'main_story_ch5_meet_sylvi',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'sylvi',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sylvi', 'dialog_id': 'sylvi_ch5_riftcaller_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch5_after_sylvi' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch5_after_sylvi' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sylvi', 'dialog_id': 'sylvi_ch5_response_to_technique' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'sylvi', 'standing_text': ["Bring me my Stormglass Ember from Stormglass Alley, and I'll summon Astra Wynn for you."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch5_meet_static_wraiths' }}
        ]
    },
    {
        'task_id': 'main_story_ch5_meet_static_wraiths',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'static_wraith',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'static_wraith', 'location': None }},
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'stormglass_alley', 'location': 'region_city_open_area' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'stormglass_alley', 'item_id': 'corsair_tide_fragment', 'location': 'final_chamber' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch5_static_wraiths' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch5_static_wraiths' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch5_static_wraiths' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch5_static_wraiths' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'static_wraith', 'standing_text': ["*static screeching*"]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch5_defeat_static_wraiths' }}
        ]
    },
    {
        'task_id': 'main_story_ch5_defeat_static_wraiths',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'static_wraith_mob',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'static_wraith_mob', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'static_wraith' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch5_defeated_static_wraiths' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch5_defeated_static_wraiths' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch5_defeated_static_wraiths' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch5_defeated_static_wraiths' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch5_defeated_static_wraiths_2' }},
            { 'event_type': 'award_item', 'params': { 'item_id': 'stormglass_ember' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch5_deliver_ember_to_sylvi' }}
        ]
    },
    {
        'task_id': 'main_story_ch5_deliver_ember_to_sylvi',
        'type': 'deliver',
        'item_id': 'stormglass_ember',
        'to_type': 'npc',
        'to_id': 'sylvi',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sylvi', 'dialog_id': 'sylvi_ch5_receives_ember' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch5_narrator_ember_fractures' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch5_ember_fractures' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sylvi', 'dialog_id': 'sylvi_ch5_ember_fractures_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch5_ember_fractures_response' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'sylvi', 'standing_text': ["Astra Wynn will be here shortly. Don't wander off."]}},
            { 'event_type': 'remove_item', 'params': { 'item_id': 'stormglass_ember' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch5_meet_astra_wynn' }}
        ]
    },
    {
        'task_id': 'main_story_ch5_meet_astra_wynn',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'astra_wynn',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'astra_wynn', 'location': 'city_number_3_region_city_shopitems' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'astra_wynn', 'dialog_id': 'astra_ch5_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sylvi', 'dialog_id': 'sylvi_ch5_request_riftcall' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'astra_wynn', 'dialog_id': 'astra_ch5_agrees' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch5_after_astra' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch5_after_astra' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'astra_wynn', 'dialog_id': 'astra_ch5_warning' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch5_before_riftcall' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch5_before_riftcall' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch5_narrator_riftcall' }},
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'rift_dungeon_outskirts', 'location': 'region_open_area' }},
            { 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'rift_dungeon_outskirts', 'location': 'final_chamber' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch5_after_riftcall' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch5_after_riftcall' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch5_after_riftcall' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch5_after_riftcall' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'astra_wynn', 'location': 'city_number_5_region_city_shopitems' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'astra_wynn', 'standing_text': ["The reflections are restless tonight."]} },
            { 'event_type': 'award_task', 'params': { 'task_id': 'meet_astra_wynn_go_back' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch5_meet_dorian_pikefall' }}
        ]
    },
    {
        'task_id': 'meet_astra_wynn_go_back',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'astra_wynn',
        'task_acquire_events': [
            { 'event_type': 'remove_task', 'params': { 'task_id': 'meet_astra_wynn_go_forward' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'astra_wynn', 'dialog_id': 'astra_ch5_teleporting_to_highsteeple_crossing' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'astra_wynn', 'location': 'city_number_3_region_city_shopitems' }},
            { 'event_type': 'set_player_location', 'params': { 'location': 'city_number_3_region_city_shopitems' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'meet_astra_wynn_go_forward' }}
        ]
    },
    {
        'task_id': 'meet_astra_wynn_go_forward',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'astra_wynn',
        'task_acquire_events': [
            { 'event_type': 'remove_task', 'params': { 'task_id': 'meet_astra_wynn_go_back' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'astra_wynn', 'dialog_id': 'astra_ch5_teleporting_to_brinewood_harbor' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'astra_wynn', 'location': 'city_number_5_region_city_shopitems' }},
            { 'event_type': 'set_player_location', 'params': { 'location': 'city_number_5_region_city_shopitems' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'meet_astra_wynn_go_back' }}
        ]
    },
    {
        'task_id': 'main_story_ch5_meet_dorian_pikefall',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'dorian_pikefall',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'dorian_pikefall', 'location': 'region_city_shopitems' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dorian_pikefall', 'dialog_id': 'dorian_ch5_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch5_after_dorian' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dorian_pikefall', 'dialog_id': 'dorian_ch5_explains_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch5_after_dorian' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch5_after_dorian' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch5_after_dorian_2' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dorian_pikefall', 'dialog_id': 'dorian_ch5_explains_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch5_after_dorian' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dorian_pikefall', 'dialog_id': 'dorian_ch5_outro_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch5_after_dorian_3' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch5_after_dorian_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch5_after_dorian_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch5_after_dorian_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch5_after_dorian_2' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dorian_pikefall', 'dialog_id': 'dorian_ch5_outro_2' }},
            { 'event_type': 'award_item', 'params': { 'item_id': 'dorians_sketch_of_distortion' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'dorian_pikefall', 'standing_text': ["I saw something strange near the breach site. A shimmering distortion carrying something that glowed like your bracelet. Seth at Bleakwatch Outpost might know more."]}},
            { 'event_type': 'advance_chapter' }
        ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_5',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}