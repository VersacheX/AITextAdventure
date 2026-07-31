# ============================================================
# = CHAPTER 9 : SCALPEL'S DOMAIN
# ============================================================
#
# [ LOCATION - THE RADPOST / BLOODSPARK ARENA ]
# -----------------------------------
# @ = player
# B = Brann (arena addict)
# L = Lira (overwhelmed healer)
# E = Ember (witness)
# T, S = Tess & Sam (impressionable travelers)
# G, S = Glamour & Scalpel (Voidwalkers)
#
# High level: The party arrives at BioHazard, a city dominated by
# the Bloodspark Arena, where the Voidwalker Scalpel cultivates a
# culture of violence. The party must navigate this brutal environment,
# confront the dual threat of Glamour and Scalpel, and retrieve the
# Bracelet of Existence.

ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
    {
        "npc_id": "brann",
        "name": "Brann",
        "description": "A former arena champion, now a hollowed-out addict to the thrill of combat. He is haunted by what he's become but can't escape the pull of the arena.",
        "psychology": {
            "mbti": "ESTP",
            "dominant": "Se - Lives for the immediate sensory thrill of the fight. His addiction is rooted in the adrenaline and hyper-awareness of combat.",
            "auxiliary": "Ti - Analyzes combat tactics with sharp, internal logic, which made him a champion.",
            "tertiary": "Fe - Has a buried sense of camaraderie and charm, now twisted by his addiction and self-loathing.",
            "inferior": "Ni - Under stress, he becomes fatalistic, seeing no way out of his cycle of violence and believing he is doomed."
        },
        "enneagram": {
          "enneagram_type": "7w8",
          "core_fear": "Being trapped in pain or boredom.",
          "core_desire": "To be free and stimulated.",
          "defense_mechanism": "Rationalization — Frames his addiction to combat as a choice or a thrill, avoiding the reality that he is trapped by it.",
          "stress_line": "Moves to Type 1 — Becomes rigid and self-critical when he can't get his fix of combat.",
          "growth_line": "Moves to Type 5 — Becomes more introspective and able to find meaning beyond the immediate thrill.",
          "instinctual_variant": "sx/sp — Seeks intense, one-on-one experiences (combat) to feel alive and secure his place."
        },
        'image': 'npcs:brann1'
    },
    {
        "npc_id": "lira",
        "name": "Lira",
        "description": "A compassionate but overwhelmed healer who runs a makeshift clinic for the arena's fighters. She is trapped in a cycle of mending wounds for fighters who immediately return to the fray.",
        "psychology": {
            "mbti": "ISFJ",
            "dominant": "Si - Focused on the concrete, immediate duty of patching up wounds. She remembers every fighter she's treated.",
            "auxiliary": "Fe - Driven by a powerful empathy and a desire to care for others, even when it feels hopeless.",
            "tertiary": "Ti - Tries to logically understand why the fighters keep going back, but struggles against the irrationality of their addiction.",
            "inferior": "Ne - Is overwhelmed by the endless, catastrophic possibility of losing every fighter she tries to save, leading to burnout."
        },
        "enneagram": {
          "enneagram_type": "2w1",
          "core_fear": "Being unwanted or unneeded.",
          "core_desire": "To be loved and needed.",
          "defense_mechanism": "Repression — Denies her own exhaustion and despair to continue helping the fighters, believing her worth comes from her service.",
          "stress_line": "Moves to Type 8 — Becomes controlling and angry when her help is futile and the fighters return to the arena.",
          "growth_line": "Moves to Type 4 — Learns to acknowledge her own feelings of hopelessness and find an identity beyond being a caregiver.",
          "instinctual_variant": "so/sp — Focused on the well-being of her community (the fighters), finding her security in being needed by them."
        },
        'image': 'npcs:lira1'
    }
]

NPC_DIALOG = [
    {
        'npc_id': None,
        'dialog_id': 'ch9_narrator_intro',
        'dialog': [
            "Chapter 9 - The danger isn't when it hurts... it's when you start to enjoy it."
        ]
    },
    {
        'npc_id': 'brann',
        'dialog_id': 'brann_ch9_intro',
        'dialog': [
            "Scalpel twists thrill into hunger. Don't feed it. I used to fight for glory. Now I fight because I can't stop."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch9_to_brann',
        'dialog': [
            "You were a champion?"
        ]
    },
    {
        'npc_id': 'brann',
        'dialog_id': 'brann_ch9_addict_1',
        'dialog': [
            "Was. Now I'm just another addict."
        ]
    },
    {
        'npc_id': 'brann',
        'dialog_id': 'brann_ch9_addict_2',
        'dialog': [
            "If you're going in there, understand the rules - escalation. Every fight gets faster, harder, deadlier."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch9_to_brann',
        'dialog': [
            "Of course it's a death spiral designed to break people. Why wouldn't it be?"
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch9_to_brann',
        'dialog': [
            "Controlled violence with intent. This one is dangerous."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch9_to_brann',
        'dialog': [
            "This place feeds on pain. We must be careful not to become what it wants."
        ]
    },
    {
        'npc_id': 'lira',
        'dialog_id': 'lira_ch9_intro_1',
        'dialog': [
            "I can't keep up... they won't stop fighting."
        ]
    },
    {
        'npc_id': 'lira',
        'dialog_id': 'lira_ch9_intro_2',
        'dialog': [
            "Every day I stitch them back together. Every day they go back in."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch9_to_lira',
        'dialog': [
            "This is cruelty disguised as sport."
        ]
    },
    {
        'npc_id': 'lira',
        'dialog_id': 'lira_ch9_request',
        'dialog': [
            "If you can... please. Rescue the trapped fighters. Some of them are caught in the shifting walls."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch9_to_lira',
        'dialog': [
            "People getting trapped in walls? That's new levels of fucked up."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch9_to_lira',
        'dialog': [
            "(growling) Then we break the walls. Simple."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch9_to_lira',
        'dialog': [
            "This place is devouring people whole. We can't let it keep winning."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch9_intro',
        'dialog': [
            "You came here too. Good. Someone needs to witness what violence really costs."
        ]
    },
    {
        'npc_id': 'lira',
        'dialog_id': 'lira_ch9_about_ember',
        'dialog': [
            "They've been here for days. Singing to the dying. Helping me carry the weight."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch9_to_ember',
        'dialog': [
            "You're a healer."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch9_response',
        'dialog': [
            "I’m a reminder. That even when everything’s bleeding, people can still choose not to become monsters."
        ]
    },
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_ch9_arena_analysis',
        'dialog': [
            "(Watching the arena entrance, a calculating look in her eyes) This isn't just a fight. It's a performance.",
            "They're selling the *idea* of violence. The crowd isn't just watching, they're buying in."
        ]
    },
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_ch9_arena_analysis',
        'dialog': [
            "It's a feedback loop. The fighters' adrenaline fuels the crowd's bloodlust, which in turn pushes the fighters further.",
            "The system is designed for escalation, not victory."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch9_to_tess_sam',
        'dialog': [
            "You two sound way too analytical about a slaughterhouse."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch9_to_tess_sam',
        'dialog': [
            "Oh this is delicious. They're not just watching the show, they're reverse-engineering the grift."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch9_warning',
        'dialog': [
            "Be careful. Understanding the machine doesn’t protect you from becoming another gear in it.",
            "This place wants you to see the system, to admire its efficiency, and then to crave it."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch9_agrees',
        'dialog': [
            "Ember is right. We need to end this quickly before the corruption takes deeper root."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch9_agrees',
        'dialog': [
            "Their excitement is a different kind. Not of bloodlust, but of understanding. It is still a vulnerability."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch9_observes',
        'dialog': [
            "The psychological bleed is already starting. Fascinating... and troubling."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch9_narrator_boss_intro',
        'dialog': [
            "The air in the arena chamber grows thick and feverish. Lights swirl unnaturally as two presences manifest."
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch9_boss_intro_1',
        'dialog': [
            "(voice echoing from every direction, seductive and hungry) There you are~ Look at them. Look at all of you.",
            "So many pretty eyes fixed on me. Don't you feel it? The need to be seen? To be adored?"
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch9_boss_intro_2',
        'dialog': [
            "Feed me your attention.",
            "Feed me everything."
        ]
    },
    {
        'npc_id': 'scalpel',
        'dialog_id': 'scalpel_ch9_boss_intro_1',
        'dialog': [
            "(cold, precise, slicing through the chaos) Enough theatrics."
        ]
    },
    {
        'npc_id': 'scalpel',
        'dialog_id': 'scalpel_ch9_boss_intro_2',
        'dialog': [
            "Glamour plays with the surface. I cut to the core."
        ]
    },
    {
        'npc_id': 'scalpel',
        'dialog_id': 'scalpel_ch9_boss_intro_3',
        'dialog': [
            "You've interfered long enough. Now you will learn what real precision feels like."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch9_boss_response',
        'dialog': [
            "Two at once? Finally, something worth punching!"
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch9_boss_response',
        'dialog': [
            "Ooooh, this is going to be *fun*. One wants us to watch, the other wants to dissect us. I can't pick a favorite!"
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch9_boss_response',
        'dialog': [
            "Their synergy is dangerous. One pulls focus while the other strikes. Stay sharp."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch9_boss_response',
        'dialog': [
            "There is no humanity left in either of them. Only hunger and cruelty."
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch9_boss_taunt',
        'dialog': [
            "(laughing wildly) Yes! Get angry! Get excited! Look at me!"
        ]
    },
    {
        'npc_id': 'scalpel',
        'dialog_id': 'scalpel_ch9_boss_taunt',
        'dialog': [
            "(voice like a scalpel across glass) Look all you want. It changes nothing. You will bleed. You will break.",
            "And you will do it beautifully."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch9_narrator_after_boss',
        'dialog': [
            "The arena falls eerily silent. The frenzied crowd slowly regains awareness, as if waking from a fever dream.",
            "The air feels lighter, but the weight of what just happened lingers."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch9_bracelet_found',
        'dialog': [
            "(softly, eyes widening as the bracelet appears) The Bracelet of Existence..."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch9_bracelet_found',
        'dialog': [
            "Heavy. Feels like it's got the weight of the whole damn world in it."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch9_bracelet_found',
        'dialog': [
            "Ooooh, it's practically humming. I can feel the power crawling up my arms. This thing is *alive*."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch9_bracelet_found',
        'dialog': [
            "Finally. After all this chaos... one of the two pieces we need. Don't lose it."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch9_bracelet_found',
        'dialog': [
            "The air around it feels... stable. Like reality itself is trying to hold on tighter."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch9_bracelet_found',
        'dialog': [
            "One more step closer to understanding what's tearing the world apart."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch9_bracelet_found',
        'dialog': [
            "(grunting approvingly) Good. We're collecting pieces. Keep going."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch9_return_to_ember',
        'dialog': [
            "We should return to Ember. She'll want to know the arena has quieted..."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch9_after_boss',
        'dialog': [
            "You're back... and the air feels different. Did you succeed?"
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch9_report_to_ember',
        'dialog': [
            "Glamour and Scalpel are gone. The arena has fallen silent."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch9_thankful',
        'dialog': [
            "(soft smile, relieved) Then some humanity has been reclaimed today. Thank you.",
            "(turning to Tess and Sam, voice warm and grounding) You two... you saw the trap for what it was. You held on."
        ]
    },
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_ch9_recovering',
        'dialog': [
            "(shaking her head, a flicker of her usual charm returning) Barely. It's a nasty piece of work, getting people to crave their own destruction. I almost respect it."
        ]
    },
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_ch9_recovering',
        'dialog': [
            "It was an efficient system. But unsustainable. All such systems eventually collapse under their own weight."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch9_reassurance',
        'dialog': [
            "It was never you. Scalpel's domain pushes those thoughts into your mind. You are stronger than its lies."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch9_recovering',
        'dialog': [
            "They were adorable when they were bloodthirsty. But I like them better like this."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch9_recovering',
        'dialog': [
            "The corruption is receding. They'll recover."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch9_departs',
        'dialog': [
            "I've done what I can here. I'm heading to Crosswind Bazaar next.",
            "People there are being drowned in forced joy and manic celebration."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch9_to_ember_depart',
        'dialog': [
            "Crosswind Bazaar... that's a loud, chaotic place. You sure you want to walk straight into more of this madness alone?"
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch9_to_ember_depart',
        'dialog': [
            "After what we just saw? It feels risky. But if anyone can keep their head there, it's you."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch9_to_ember_depart',
        'dialog': [
            "(grunting) More crowds. More frenzy. Not sure I like the sound of it."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch9_to_ember_depart',
        'dialog': [
            "Logically, it makes sense. We're already committed to this path. Might as well keep moving."
        ]
    }
]

TASKS = [
    {
        'task_id': 'main_story_ch9_meet_brann',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'brann',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'brann', 'location': 'region_city_bar' }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'lira', 'location': 'region_city_inn' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'ember', 'location': 'region_city_inn' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'tess', 'location': 'region_city_inn' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'sam', 'location': 'region_city_inn' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'brann', 'standing_text': ["The arena will test you. Don't let Scalpel make you enjoy it."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lira', 'standing_text': ["I can't keep patching them up... they're all breaking."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'ember', 'standing_text': ["The arena's influence is spreading. We need to stop it before it consumes the next city."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'tess', 'standing_text': ["I've seen this kind of hustle before. You get the marks hooked on the emotion, then you own them."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'sam', 'standing_text': ["The system is elegant in its cruelty. I want to see how it breaks."]}},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch9_narrator_intro' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'brann', 'dialog_id': 'brann_ch9_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch9_to_brann' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'brann', 'dialog_id': 'brann_ch9_addict_1' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'brann', 'dialog_id': 'brann_ch9_addict_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch9_to_brann' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch9_to_brann' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch9_to_brann' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'brann', 'standing_text': ["The arena will test you. Don't let Scalpel make you enjoy it."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch9_meet_lira' }}
        ]
    },
    {
        'task_id': 'main_story_ch9_meet_lira',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lira',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lira', 'dialog_id': 'lira_ch9_intro_1' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lira', 'dialog_id': 'lira_ch9_intro_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch9_to_lira' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lira', 'dialog_id': 'lira_ch9_request' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch9_to_lira' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch9_to_lira' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch9_to_lira' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lira', 'standing_text': ["The walls shift when Scalpel watches. People get trapped. Please help them."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch9_meet_ember_in_scalpel_domain' }}
        ]
    },
    {
        'task_id': 'main_story_ch9_meet_ember_in_scalpel_domain',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'ember',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch9_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lira', 'dialog_id': 'lira_ch9_about_ember' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch9_to_ember' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch9_response' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'tess', 'dialog_id': 'tess_ch9_arena_analysis' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sam', 'dialog_id': 'sam_ch9_arena_analysis' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch9_to_tess_sam' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch9_to_tess_sam' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch9_warning' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch9_agrees' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch9_agrees' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch9_observes' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'ember', 'standing_text': ["The arena calls, but stay human. Don't let Scalpel's domain own your desires."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'tess', 'standing_text': ["I've seen this kind of hustle before. You get the marks hooked on the emotion, then you own them."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'sam', 'standing_text': ["The system is elegant in its cruelty. I want to see how it breaks."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch9_meet_glamour_and_scalpel' }}
        ]
    },
    {
        'task_id': 'main_story_ch9_meet_glamour_and_scalpel',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'scalpel',
        'task_acquire_events': [
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'bloodspark_arena_gauntlet', 'location': 'region_city_open_area' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch9_narrator_boss_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch9_boss_intro_1' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch9_boss_intro_2' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scalpel', 'dialog_id': 'scalpel_ch9_boss_intro_1' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scalpel', 'dialog_id': 'scalpel_ch9_boss_intro_2' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scalpel', 'dialog_id': 'scalpel_ch9_boss_intro_3' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch9_boss_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch9_boss_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch9_boss_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch9_boss_response' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch9_boss_taunt' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scalpel', 'dialog_id': 'scalpel_ch9_boss_taunt' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch9_defeat_glamour_and_scalpel' }}
        ]
    },
    {
        'task_id': 'main_story_ch9_defeat_glamour_and_scalpel',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'glamour_scalpel_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'glamour_scalpel_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'glamour' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'scalpel' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch9_narrator_after_boss' }},
            { 'event_type': 'award_item', 'params': { 'item_id': 'bracelet_of_existence' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch9_bracelet_found' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch9_bracelet_found' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch9_bracelet_found' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch9_bracelet_found' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch9_bracelet_found' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch9_bracelet_found' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch9_bracelet_found' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch9_return_to_ember' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'brann', 'standing_text': ["The arena feels... different now. Maybe there's hope."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lira', 'standing_text': ["The wounded are finally resting. Thank the stars."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'tess', 'standing_text': ["The high is gone. Now comes the crash. I've seen this look on people's faces before. They're vulnerable."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'sam', 'standing_text': ["The system broke. Now we see the cost. Every grift has a price."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch9_return_to_ember_after_scalpel' }}
        ]
    },
    {
        'task_id': 'main_story_ch9_return_to_ember_after_scalpel',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'ember',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch9_after_boss' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch9_report_to_ember' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch9_thankful' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'tess', 'dialog_id': 'tess_ch9_recovering' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sam', 'dialog_id': 'sam_ch9_recovering' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch9_reassurance' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch9_recovering' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch9_recovering' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch9_departs' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch9_to_ember_depart' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch9_to_ember_depart' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch9_to_ember_depart' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch9_to_ember_depart' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'tess', 'standing_text': ["I feel... more like myself again. Time to find the next angle."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'sam', 'standing_text': ["The immediate threat is neutralized. Now to analyze the fallout."]}},
            { 'event_type': 'advance_chapter' }
        ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_9',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}