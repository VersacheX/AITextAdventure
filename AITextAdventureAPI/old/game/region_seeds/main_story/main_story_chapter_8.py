# ============================================================
# = CHAPTER 8 : GLAMOUR'S CITY OF SHATTERED ATTENTION
# ============================================================
#
# [ LOCATION - CITY OF ECHOES / CRASH SITE ]
# -----------------------------------
# @ = player
# V = Veyla (scattered singer)
# R = Rusk (order-obsessed citizen)
# J = Jinn (focus lens con artist)
# E = Ember (grounding performer)
# T = Tess & S = Sam (travelers)
# G = Glamour (Voidwalker)
#
# High level: The party's airship crashes. They find themselves in a
# city overwhelmed by sensory chaos, ruled by the Voidwalker Glamour.
# They must navigate the fractured attention of its citizens to find
# and confront the source of the madness, only to be met by a new threat.

ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
    {
        "npc_id": "veyla",
        "name": "Veyla",
        "description": "A singer whose voice was stolen and copied by the city's chaos. She is scattered and struggles to focus, a victim of Glamour's sensory overload.",
        "psychology": {
            "mbti": "INFP",
            "dominant": "Fi - Deeply connected to her internal emotional state, which has been fractured and scattered.",
            "auxiliary": "Ne - Her thoughts jump between fragmented ideas and memories, unable to form a coherent line.",
            "tertiary": "Si - Clings to the memory of who she was before her voice was taken.",
            "inferior": "Te - Completely unable to organize her thoughts or act with purpose in the external world."
        },
        "enneagram": {
          "enneagram_type": "9w1",
          "core_fear": "Fragmentation and loss of self.",
          "core_desire": "To have inner peace and wholeness.",
          "defense_mechanism": "Dissociation — Her mind scatters to escape the overwhelming sensory chaos, unable to hold a single thought.",
          "stress_line": "Moves to Type 6 — Becomes anxious and panicked, unable to trust her own mind.",
          "growth_line": "Moves to Type 3 — Becomes more focused and able to reclaim her voice and sense of self.",
          "instinctual_variant": "sp/so — Withdraws into herself to find peace, but is still passively affected by the social chaos."
        },
        'image': 'npcs:veyla1'
    },
    {
        "npc_id": "rusk",
        "name": "Rusk",
        "description": "A citizen desperately trying to enforce order and quiet hours in a city of chaos. He is wound tight and obsessed with rules as a way to fight back against the madness.",
        "psychology": {
            "mbti": "ISTJ",
            "dominant": "Si - Clings to the memory of how things 'used to be'-ordered, structured, and quiet.",
            "auxiliary": "Te - Tries to impose external order by shouting rules and demanding quiet, though it has no effect.",
            "tertiary": "Fi - Driven by a quiet, desperate conviction that order is morally right and chaos is wrong.",
            "inferior": "Ne - Completely overwhelmed by the unpredictable sensory chaos, leading to frustration and rage."
        },
        "enneagram": {
          "enneagram_type": "1w2",
          "core_fear": "The world being wrong, chaotic, and out of control.",
          "core_desire": "To have order and balance.",
          "defense_mechanism": "Reaction Formation — Channels his fear of chaos into a rigid, angry enforcement of rules he believes are 'right'.",
          "stress_line": "Moves to Type 4 — Becomes withdrawn and resentful when his efforts to create order fail.",
          "growth_line": "Moves to Type 7 — Learns to relax and accept that not everything can be perfectly controlled.",
          "instinctual_variant": "so/sp — Focused on reforming his social environment to match his ideal of order."
        },
        'image': 'npcs:rusk1'
    },
    {
        "npc_id": "jinn",
        "name": "Jinn",
        "description": "A fast-talking con artist selling 'focus lenses' that do nothing. He's a cynical opportunist who has adapted perfectly to a city where clarity is a commodity.",
        "psychology": {
            "mbti": "ENTP",
            "dominant": "Ne - Sees angles and opportunities in the chaos, constantly adapting his sales pitch.",
            "auxiliary": "Ti - Logically understands the system of distraction and exploits it for personal gain.",
            "tertiary": "Fe - Uses charm and feigned helpfulness to sell his useless wares.",
            "inferior": "Si - Has no attachment to the past or 'how things should be,' allowing him to thrive in the chaos."
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
        'image': 'npcs:jinn1'
    },
    {
        "npc_id": "ember",
        "name": "Ember",
        "description": "A traveling street performer and singer who acts as an emotional anchor in collapsing cities. They play music to remind people of real, unprocessed emotion, choosing to witness and soothe suffering rather than flee.",
        "psychology": {
            "mbti": "INFJ",
            "dominant": "Ni - Possesses a deep, intuitive understanding of the world's emotional state and the symbolic importance of their actions.",
            "auxiliary": "Fe - Radically empathetic, focusing on the emotional well-being of the community and providing a grounding presence.",
            "tertiary": "Ti - Has a clear internal framework of why their 'witnessing' is necessary, even if it leads to their own demise.",
            "inferior": "Se - Chooses to remain in overwhelming sensory environments not to enjoy them, but to counteract them, showing immense control over their reaction to the physical world."
        },
        "enneagram": {
          "enneagram_type": "2w1",
          "core_fear": "Being unwanted or failing to help those in need.",
          "core_desire": "To be loved and needed.",
          "defense_mechanism": "Repression — Denies their own fear and exhaustion to continue serving and healing others, finding their worth in their sacrifice.",
          "stress_line": "Moves to Type 8 — Becomes forceful and demanding when their help is rejected or proves futile.",
          "growth_line": "Moves to Type 4 — Acknowledges their own sorrow and finds an identity beyond being a helper.",
          "instinctual_variant": "so/sp — Sacrifices their own well-being for the good of the community, finding security in being needed."
        },
        'image': 'npcs:ember1'
    },
    {
        "npc_id": "scalpel",
        "name": "Scalpel",
        "description": "A blade of pure detachment — violence without emotion, purpose, or hesitation.",
        "theme_song": "Guillotine, Death Grips (instrumental) | The Perfect Drug (instrumental), Nine Inch Nails",
        "psychology": {
          "mbti": "ISTP-shadow",
          "dominant": "Ti — Surgical cruelty; dissects beings as if they were broken mechanisms.",
          "auxiliary": "Se — Hyper-precise predation; acts faster than thought.",
          "tertiary": "Ni — Obsessive fatalism; sees every target as already dead.",
          "inferior": "Fe — Emotional void; mimics empathy only to exploit it."
        },
        "enneagram": {
          "enneagram_type": "5w6",
          "core_fear": "Being overwhelmed or incompetent.",
          "core_desire": "To be capable and competent.",
          "defense_mechanism": "Isolation — Detaches completely from emotion to become a perfect, efficient tool of violence. It is pure, cold logic in action.",
          "stress_line": "Moves to Type 7 — Its violence becomes scattered, chaotic, and unfocused.",
          "growth_line": "Moves to Type 8 — Would learn to use its precision and skill with confidence and purpose, not just detachment.",
          "instinctual_variant": "sp/sx — A reclusive predator, focused on perfecting its own deadly competence."
        },
        'image': 'voidwalkers:scalpel1.jpeg',
        'song_id': 'the_perfect_drug_nine_inch_nails'
    },
      {
        "npc_id": "glamour",
        "name": "Glamour",
        "description": "A radiant predator — beauty weaponized into domination.",
        "theme_song": "Toxic, Britney Spears",
        "psychology": {
          "mbti": "ESFP-shadow",
          "dominant": "Se — Sensory intoxication; overwhelms perception with irresistible allure.",
          "auxiliary": "Fi — Vanity as tyranny; values only adoration and submission.",
          "tertiary": "Te — Punishes rejection with explosive fury.",
          "inferior": "Ni — Paranoia of fading beauty; sees doom in every reflection."
        },
        "enneagram": {
          "enneagram_type": "3w2",
          "core_fear": "Being worthless or without admiration.",
          "core_desire": "To feel valuable and admired.",
          "defense_mechanism": "Identification — Has completely identified with the image of irresistible beauty, needing constant attention to feel real.",
          "stress_line": "Moves to Type 9 — Becomes apathetic and disengaged when her allure fails to capture attention.",
          "growth_line": "Moves to Type 6 — Would learn to find value in genuine connection rather than superficial adoration.",
          "instinctual_variant": "sx/so — Seeks intense, one-on-one adoration and uses it to dominate the social sphere."
        },
        'image': 'voidwalkers:glamour1.jpeg',
        'song_id': 'toxic_britney_spears'
    }
]

NPC_DIALOG = [
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch8_airship_intro',
        'dialog': [
            "Alright, settle down back there! The Rustwing's holdin' together with spit and prayer as it is."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch8_airship_intro',
        'dialog': [
            "\"Holdin' together\" is generous. This thing rattles worse than a drunk with the shakes."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch8_airship_intro',
        'dialog': [
            "I don't like this... feels like the air itself is lying to us."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch8_airship_intro',
        'dialog': [
            "Everything's spinning too fast. My head's full of static."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_ch8_airship_intro',
        'dialog': [
            "My tools are screamin'. Somethin' out here is messin' with reality real bad."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch8_airship_response',
        'dialog': [
            "See? This is exactly why I was happy to hand you lot the keys. Too much weird metaphysical bullshit for me."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'faith_ch8_airship_intro',
        'dialog': [
            "The fractures are getting worse. I can feel the strain on everything... even the ship."
        ]
    },
    {
        'npc_id': 'kor_in',
        'dialog_id': 'kor_in_ch8_airship_intro',
        'dialog': [
            "(quietly) ...Like walking on thinning ice."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_ch8_airship_intro',
        'dialog': [
            "The currents feel wrong. Like the world is forgetting how to hold itself together."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch8_airship_intro',
        'dialog': [
            "Ooooh, I'm kind of enjoying this. Bad decisions make great stories."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch8_airship_intro',
        'dialog': [
            "Don't lick the turbulence, Moxie. We have enough problems."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch8_airship_intro',
        'dialog': [
            "Smells like something died and decided not to stay dead."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_ch8_airship_intro',
        'dialog': [
            "(muttering) The decay has a very specific... texture. Not good."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch8_narrator_crash',
        'dialog': [
            "Suddenly, a violent shudder rocks the Rustwing. Alarms blare as the engine sputters, choked by shimmering, distorted air."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch8_crash',
        'dialog': [
            "BRACE! WE'RE GOING DOWN!"
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch8_narrator_intro',
        'dialog': [
            "Chapter 8 - The world is what appears to us... and we are shaped by what we attend to. - Merleau-Ponty"
        ]
    },
    {
        'npc_id': 'veyla',
        'dialog_id': 'veyla_ch8_intro_1',
        'dialog': [
            "Your faces... I know them... no wait...",
            "Everything's too bright, too loud, too MUCH. I can't hold a thought for more than..",
            "Wait, what were we talking about?"
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch8_after_veyla',
        'dialog': [
            "She's scattered like shattered glass. I love it."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch8_after_veyla',
        'dialog': [
            "Focus, lady. Deep breaths."
        ]
    },
    {
        'npc_id': 'veyla',
        'dialog_id': 'veyla_ch8_intro_2',
        'dialog': [
            "I used to sing. Now I just... echo. The city took my voice and made copies.",
            "The Theatre of Echoed Faces...",
            "That's where Glamour's projection hides. I think. Maybe. I remember... fragments."
        ]
    },
    {
        'npc_id': 'jinn',
        'dialog_id': 'jinn_ch8_intro_1',
        'dialog': [
            "Focus lenses! Guaranteed clarity! They don't work.",
            "But hey, the placebo effect is real, right?"
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch8_after_jinn',
        'dialog': [
            "I like him. He's honest about his dishonesty."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch8_after_jinn',
        'dialog': [
            "He's a con artist in a city of illusions. Perfect fit."
        ]
    },
    {
        'npc_id': 'jinn',
        'dialog_id': 'jinn_ch8_intro_2',
        'dialog': [
            "You want to find Glamour?",
            "I know where the projection hides. But it'll cost you.",
            "Or... you could just clear those pylons for Rusk.",
            "That'd make us all happy."
        ]
    },
    {
        'npc_id': 'rusk',
        'dialog_id': 'rusk_ch8_intro_1',
        'dialog': [
            "QUIET HOURS! QUIET HOURS! ...No one listens anymore.",
            "This district used to have ORDER. Rules. Structure.",
            "Now it's just... screaming."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch8_after_rusk',
        'dialog': [
            "Guy's wound tighter than a spring."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch8_after_rusk',
        'dialog': [
            "He's trying to hold reality together with willpower alone."
        ]
    },
    {
        'npc_id': 'rusk',
        'dialog_id': 'rusk_ch8_intro_2',
        'dialog': [
            "If you want to help, shut down the malfunctioning sensory pylons.",
            "They're overloading everyone's minds.",
            "Speak to Ember, they're about the only person around Here who isn't losing their mind."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch8_after_rusk',
        'dialog': [
            "Someone who still has their head on straight? I'll take it."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch8_after_rusk',
        'dialog': [
            "(grunting) Better than nothing. Let's find them."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch8_intro',
        'dialog': [
            "You look lost. Most people do these days. I’m Ember. I sing so they remember there’s still such a thing as real feeling."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'faith_ch8_after_ember',
        'dialog': [
            "Your voice... it's grounding. Like an anchor."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch8_explains',
        'dialog': [
            "Someone has to stay honest. Otherwise this whole city becomes nothing but noise."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch8_to_ember',
        'dialog': [
            "You're not swept up in all this?"
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch8_response_to_technique',
        'dialog': [
            "I feel it pulling at me too. But if I let it take me, who’s left to push back?"
        ]
    },
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_ch8_intro',
        'dialog': [
            "(Eyes narrowed, scanning the crowd) This isn't just chaos. It's a system. Everyone's attention is being pulled, like currency. I wonder who's collecting."
        ]
    },
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_ch8_intro',
        'dialog': [
            "(Quietly) The sensory overload is a weapon. It prevents pattern recognition. They're being managed, not entertained."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch8_to_tess_sam',
        'dialog': [
            "You see it too. Good. Don't let it manage you."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch8_observes_tess_sam',
        'dialog': [
            "They're still bickering. Good. Means reality's still intact."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'faith_ch8_observes_tess_sam',
        'dialog': [
            "Their bond grounds them. We should stay close."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch8_glamour_intro',
        'dialog': [
            "I see three of me. Are they all real?"
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch8_glamour_intro',
        'dialog': [
            "The air hums with fractured attention. Stay focused."
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch8_intro',
        'dialog': [
            "Look at you looking at me. You can't look away. Attention is the only currency that matters here. And you're all bankrupt."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch8_glamour_response',
        'dialog': [
            "It's pulling focus like gravity. I can barely think."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch8_glamour_response',
        'dialog': [
            "Then stop thinking and start hitting!"
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch8_glamour_response',
        'dialog': [
            "This... this is what the desert warned me about. Everything screaming for your eyes."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch8_glamour_response',
        'dialog': [
            "The wind is screaming too many versions of us. It's dizzying."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_ch8_glamour_response',
        'dialog': [
            "My head feels like it's splitting. Make it shut up!"
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch8_taunt',
        'dialog': [
            "(laughing, voice echoing from every mirror) Why fight it? Just watch. Just admire. Just give in.",
            "You're all so much more beautiful when you're distracted."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch8_narrator_scalpel_arrival_1',
        'dialog': [
            "The illusions intensify, then suddenly fracture. Glamour's form flickers and shatters like glass."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch8_narrator_scalpel_arrival_2',
        'dialog': [
            "A colder presence replaces her. Sharp. Surgical. Emotionless."
        ]
    },
    {
        'npc_id': 'scalpel',
        'dialog_id': 'scalpel_ch8_intro',
        'dialog': [
            "Glamour was soft. She needed your eyes. I only need one clean cut."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch8_scalpel_arrival',
        'dialog': [
            "Oh that's... that's a problem."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch8_scalpel_arrival',
        'dialog': [
            "New boss. Same fists."
        ]
    },
    {
        'npc_id': 'scalpel',
        'dialog_id': 'scalpel_ch8_outro',
        'dialog': [
            "Glamour was soft. I am not. This pathetic spire of distractions doesn't matter. The real entertainment awaits at BioHazard.",
            "Come find me there... if you still have the stomach for it."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch8_after_scalpel',
        'dialog': [
            "BioHazard? That sounds deep in the desert... This just keeps getting worse."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch8_after_scalpel',
        'dialog': [
            "Ooh, this one's all business. No flair, just blades. I respect the commitment."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch8_after_scalpel',
        'dialog': [
            "Great. From too much noise to too much blood."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch8_after_scalpel',
        'dialog': [
            "Precision without emotion... This one will be dangerous."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch8_after_scalpel',
        'dialog': [
            "Cold, efficient, and sadistic. My favorite kind of nightmare."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch8_after_scalpel',
        'dialog': [
            "(grunting) Then we follow. No point stopping now."
        ]
    }
]

TASKS = [
    {
        'task_id': 'main_story_ch8_meet_veyla',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'veyla',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'veyla', 'location': 'region_city_inn' }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'rusk', 'location': 'region_city_shoparmor' }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'jinn', 'location': 'region_city_shopitems' }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'ember', 'location': 'region_city_bar' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'tess', 'location': 'region_city_bar' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'sam', 'location': 'region_city_bar' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'veyla', 'standing_text': ["Everything is too loud... too bright... I can't... focus..."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rusk', 'standing_text': ["This district used to have rules! Now it's just noise and madness!"]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'jinn', 'standing_text': ["Focus lenses! Clarity guaranteed! ...Results may vary."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'ember', 'standing_text': ["In a city full of echoes, someone has to stay real."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'tess', 'standing_text': ["This whole city is a giant confidence game, but I can't figure out who's running the table."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'sam', 'standing_text': ["The chaos is a smokescreen. The real trick is happening somewhere we're not looking."]}},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch8_airship_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch8_airship_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch8_airship_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch8_airship_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_ch8_airship_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch8_airship_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch8_airship_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_ch8_airship_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_ch8_airship_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch8_airship_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch8_airship_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch8_airship_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch8_airship_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch8_narrator_crash' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch8_crash' }},
            { 'event_type': 'set_player_location', 'params': { 'location': 'region_open_area' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch8_narrator_intro' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'veyla', 'dialog_id': 'veyla_ch8_intro_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch8_after_veyla' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch8_after_veyla' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'veyla', 'dialog_id': 'veyla_ch8_intro_2' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'veyla', 'standing_text': ["The Theatre of Echoed Faces... that's where Glamour's projection hides. I think. Maybe. I remember... fragments."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch8_meet_jinn' }}
        ]
    },
    {
        'task_id': 'main_story_ch8_meet_jinn',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'jinn',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'jinn', 'dialog_id': 'jinn_ch8_intro_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch8_after_jinn' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch8_after_jinn' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'jinn', 'dialog_id': 'jinn_ch8_intro_2' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'jinn', 'standing_text': ["Theatre of Echoed Faces. That's where Glamour's core projection manifests. Good luck not losing your mind."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch8_meet_rusk' }}
        ]
    },
    {
        'task_id': 'main_story_ch8_meet_rusk',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rusk',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rusk', 'dialog_id': 'rusk_ch8_intro_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch8_after_rusk' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch8_after_rusk' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rusk', 'dialog_id': 'rusk_ch8_intro_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch8_after_rusk' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch8_after_rusk' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rusk', 'standing_text': ["The pylons are scattered throughout the district. Destroy them before everyone loses their minds completely."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch8_meet_ember' }}
        ]
    },
    {
        'task_id': 'main_story_ch8_meet_ember',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'ember',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch8_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch8_after_ember' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch8_explains' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch8_to_ember' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch8_response_to_technique' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'tess', 'dialog_id': 'tess_ch8_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sam', 'dialog_id': 'sam_ch8_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch8_to_tess_sam' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch8_observes_tess_sam' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch8_observes_tess_sam' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'ember', 'standing_text': ["Stay real, friends. The city wants to copy you. Don't let it."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'tess', 'standing_text': ["This whole city is a giant confidence game, but I can't figure out who's running the table."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'sam', 'standing_text': ["The chaos is a smokescreen. The real trick is happening somewhere we're not looking."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch8_meet_glamour' }}
        ]
    },
    {
        'task_id': 'main_story_ch8_meet_glamour',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'glamour',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'glamour', 'location': None }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'scalpel', 'location': None }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'scalpel', 'standing_text': ["Glamour was soft. I only need one clean cut."]}},
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'theatre_of_echoed_faces', 'location': 'region_city_open_area' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'theatre_of_echoed_faces', 'item_id': 'ink_resonance_vial', 'location': 'final_chamber' }},
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch8_glamour_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch8_glamour_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch8_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch8_glamour_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch8_glamour_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch8_glamour_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch8_glamour_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_ch8_glamour_response' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch8_taunt' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch8_narrator_scalpel_arrival_1' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'glamour' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch8_narrator_scalpel_arrival_2' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scalpel', 'dialog_id': 'scalpel_ch8_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch8_scalpel_arrival' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch8_scalpel_arrival' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'glamour', 'standing_text': ["Later bitches."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch8_defeat_scalpel_projection' }}
        ]
    },
    {
        'task_id': 'main_story_ch8_defeat_scalpel_projection',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'scalpel_projection_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'scalpel_projection_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scalpel', 'dialog_id': 'scalpel_ch8_outro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch8_after_scalpel' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch8_after_scalpel' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch8_after_scalpel' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch8_after_scalpel' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch8_after_scalpel' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch8_after_scalpel' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'veyla', 'standing_text': ["Something colder has arrived. I can feel it cutting through the air."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rusk', 'standing_text': ["The chaos is gone, but now there's... precision. Cold precision."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'jinn', 'standing_text': ["Scalpel. That's what they call it. And it doesn't play games."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'ember', 'standing_text': ["I'm traveling to the next city. Someone needs to remind people to stay human."]}},
            { 'event_type': 'advance_chapter' }
        ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_8',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}