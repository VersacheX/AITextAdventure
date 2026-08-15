# ============================================================
# = CHAPTER 11 : RAPTURE & REVELRY
# ============================================================
#
# [ LOCATION - BLACKWAKE BAY / FESTIVAL OF DELIGHT ]
# -----------------------------------
# @ = player
# K = Kael (resistance fighter)
# H = Hessa (seer)
# R, R = Rapture & Revelry (Voidwalkers)
# T, S = Tess & Sam (travelers)
# V = Vek (resistance fighter)
#
# High level: The party travels to Blackwake Bay to stop the
# Voidwalkers Rapture and Revelry. Ember stays behind in Crosswind
# Bazaar. After defeating the bosses, the party returns to find
# that Ember was killed in the chaotic backlash, leading them to
# their next destination to honor her last wish.

ATTAINABLE_PLAYER_CHARACTERS = [
    {
        "id": "vek",
        "name": "Vek",
        "level": 50,
        "arm_armor": "campaign_vambraces",
        "head_armor": "commanders_helm",
        "body_armor": "warfront_plate",
        "leg_armor": "warfront_greaves",
        "equipped_weapon": "dominion_halberd",
        "max_hp": 1800,
        "current_hp": 1800,
        "max_ap": 450,
        "current_ap": 450,
        "unused_ability_slots": 0,
        "unused_stat_points": 0,
        "unused_power_points": 0,
        "strength": 200,
        "dexterity": 95,
        "intelligence": 95,
        "constitution": 180,
		"abilities": [
			"lv2_unique_ability_technique_vek_command_strike",
			"lv2_unique_ability_technique_vek_rally_line",
			"lv3_unique_ability_technique_vek_dominion_breach",
			"lv4_unique_ability_technique_vek_iron_verdict",
		]
    }
]

NPCS = [
    {
        "npc_id": "kael",
        "name": "Kael",
        "description": "A grim and focused resistance fighter who has seen his city fall to the manic influence of Rapture and Revelry. He is pragmatic and desperate for a way to break the cycle.",
        "psychology": {
            "mbti": "ISTJ",
            "dominant": "Si - Relies on his past experiences of the city before its fall to understand what has been lost. He is detail-oriented and dutiful.",
            "auxiliary": "Te - Organizes his thoughts and plans with logical efficiency, focusing on practical solutions to fight the Voidwalkers.",
            "tertiary": "Fi - Driven by a quiet, deeply held conviction to save his home, even if he doesn't express it emotionally.",
            "inferior": "Ne - Struggles to see possibilities outside of the current crisis, making him seem pessimistic and rigid."
        },
        "enneagram": {
          "enneagram_type": "6w5",
          "core_fear": "Being without support or guidance; his city being destroyed.",
          "core_desire": "To have security and stability.",
          "defense_mechanism": "Projection — Projects his anxiety onto the external threat of the Voidwalkers, seeking reliable allies and a solid plan to feel secure.",
          "stress_line": "Moves to Type 3 — Becomes arrogant and focused on the appearance of success when his plans fail.",
          "growth_line": "Moves to Type 9 — Becomes more trusting and open to new ideas.",
          "instinctual_variant": "sp/so — Focused on his own and his city's survival, he seeks to build a reliable social defense system."
        },
        "image": "npcs:kael1"
    },
    {
        "npc_id": "hessa",
        "name": "Hessa",
        "description": "A seer overwhelmed by visions of the city's potential destruction. She sees countless burning futures and is desperately looking for a path that avoids total annihilation.",
        "psychology": {
            "mbti": "INFJ",
            "dominant": "Ni - Experiences powerful, often terrifying, intuitive visions of the future. She sees the underlying patterns of the chaos.",
            "auxiliary": "Fe - Feels the collective anxiety and pain of the city, which fuels her desire to find a solution.",
            "tertiary": "Ti - Tries to logically analyze her visions to find the single thread that could lead to salvation.",
            "inferior": "Se - Is disconnected from the physical world, often lost in her visions and overwhelmed by the sensory chaos of the festival."
        },
        "enneagram": {
          "enneagram_type": "6w5",
          "core_fear": "Being without support or guidance in the face of certain doom.",
          "core_desire": "To find security and certainty.",
          "defense_mechanism": "Projection — Projects her fear onto her visions, seeking external help (the party) to avert the disaster she foresees.",
          "stress_line": "Moves to Type 3 — Becomes frantic and performs her role as a seer with desperate authority.",
          "growth_line": "Moves to Type 9 — Learns to have faith and find peace even in the face of uncertainty.",
          "instinctual_variant": "so/sp — Focused on the survival of the collective, driven by her visions of social collapse."
        },
        "image": "npcs:hessa1"
    },
    {
        "npc_id": "nihilist_leader",
        "name": "Nihilist Leader",
        "description": "A charismatic figure who preys on the despair left in the wake of forced celebration. He preaches that since all joy is false, nothing matters, offering the cold comfort of apathy.",
        "psychology": {
            "mbti": "INTP",
            "dominant": "Ti - Has constructed a cold, internal logic that concludes all effort is meaningless. He uses this logic to deconstruct the hopes of others.",
            "auxiliary": "Ne - Explores all the possibilities that lead to ruin and decay, presenting them as inevitable truths.",
            "tertiary": "Si - Is fixated on past failures (both personal and societal) as proof of his nihilistic worldview.",
            "inferior": "Fe - Is completely detached from the emotional impact of his words, seeing the despair he creates in others as a logical outcome rather than a cruel act."
        },
        "enneagram": {
          "enneagram_type": "5w4",
          "core_fear": "Being overwhelmed by a meaningless world.",
          "core_desire": "To understand the world, even if that understanding leads to nihilism.",
          "defense_mechanism": "Isolation — Detaches from all emotion and meaning, viewing the world as a purely logical system that is fundamentally flawed.",
          "stress_line": "Moves to Type 7 — His nihilism becomes scattered and manic, lashing out in chaotic ways.",
          "growth_line": "Moves to Type 8 — Would use his understanding to take confident action and create meaning.",
          "instinctual_variant": "sp/so — A reclusive intellectual who shares his nihilistic worldview as a way of navigating a social world he sees as meaningless."
        },
        'image': 'bosses:nihilist_leader1'
    },
    {
        "npc_id": "rapture",
        "name": "Rapture",
        "description": "A predator of sensation — violence as ecstasy, destruction as sport.",
        "theme_song": "Smells Like Teen Spirit, Nirvana or Zero, Smashing Pumpkins",
        "psychology": {
          "mbti": "ESTP-shadow",
          "dominant": "Se — Sensory domination; overwhelms reality with raw, predatory immediacy.",
          "auxiliary": "Ti — Precision cruelty; calculates the most efficient way to break a body or mind.",
          "tertiary": "Fe — Mocking social manipulation; provokes chaos for entertainment.",
          "inferior": "Ni — Fatalistic impulses; sees only the thrill of the next destructive moment."
        },
        "enneagram": {
          "enneagram_type": "8w7",
          "core_fear": "Being controlled or limited.",
          "core_desire": "To be in control of its environment through physical dominance.",
          "defense_mechanism": "Denial — Denies any form of weakness or restraint, asserting its power through constant, escalating violence.",
          "stress_line": "Moves to Type 5 — Becomes withdrawn and paranoid when confronted by a force it cannot dominate.",
          "growth_line": "Moves to Type 2 — Would use its strength to protect rather than to harm.",
          "instinctual_variant": "sx/sp — Seeks intense, one-on-one confrontations and physical challenges to assert its dominance."
        },
        'image': 'voidwalkers:rapture1.jpeg',
        'song_id': 'zero_instrumental_smashing_pumpkins'
    },
    {
        "npc_id": "revelry",
        "name": "Revelry",
        "description": "A manic prophet of freedom — a cult of joy that ends in ruin.",
        "theme_song": "Heads Will Roll (A‑Trak Remix), Yeah Yeah Yeahs AND Dance Till We Die, Zola Jesus",
        "psychology": {
          "mbti": "ENFP-shadow",
          "dominant": "Ne — Ecstatic chaos; spawns endless possibilities with no grounding.",
          "auxiliary": "Fi — Values inverted; worships destruction as liberation.",
          "tertiary": "Te — Impulsive, explosive action; enforces chaos with manic force.",
          "inferior": "Si — Rejects continuity; every moment must be a new, louder collapse."
        },
        "enneagram": {
          "enneagram_type": "7w6",
          "core_fear": "Being trapped in pain, boredom, or negative emotion.",
          "core_desire": "To be stimulated and happy at all times.",
          "defense_mechanism": "Rationalization — Frames its destructive chaos as 'freedom' and 'joy', avoiding the reality of the suffering it causes.",
          "stress_line": "Moves to Type 1 — Becomes rigid and moralistic, insisting its way is the only 'true' way to be free.",
          "growth_line": "Moves to Type 5 — Would learn to find joy in peace and contemplation, not just manic energy.",
          "instinctual_variant": "so/sx — A social catalyst for chaos, drawing energy from the group's manic excitement."
        },
        'image': 'voidwalkers:revelry1.jpeg',
        'song_id': 'heads_will_roll_yeah_yeah_yeahs'
    }
]

NPC_DIALOG = [
    {
        'npc_id': None,
        'dialog_id': 'ch11_narrator_intro',
        'dialog': [
            "Chapter 11 - When you chase feeling long enough... you stop being able to feel at all."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch11_intro',
        'dialog': [
            "This place is a pressure cooker of emotion. It's like the whole city is on the edge of breaking.",
            "While here I've learned Rapture and Revelry are feeding off it. They're amplifying the extremes."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_to_ember_intro',
        'dialog': [
            "We need to find them and stop this before it spirals out of control."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch11_to_ember_intro',
        'dialog': [
            "The emotional bleed is accelerating. We should move before it gets worse."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch11_to_ember_intro',
        'dialog': [
            "Logically, we’re already committed. Might as well keep momentum."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch11_directs',
        'dialog': [
            "Talk to the people from this town and try to find out what they know."
        ]
    },
    {
        'npc_id': 'kael',
        'dialog_id': 'kael_ch11_intro',
        'dialog': [
            "You're the ones who fought the rioters. Good. We need fighters.",
            "This city is burning itself out. Rapture feeds the violence, Revelry feeds the party. It's an endless loop of adrenaline and exhaustion."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch11_to_kael',
        'dialog': [
            "One feeds the violence, the other feeds the party. It's actually kind of brilliant in a horrible way."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch11_to_kael',
        'dialog': [
            "Their synergy is extremely dangerous. We need to break the cycle at its source."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_to_kael',
        'dialog': [
            "Ember was right. This place is devouring people's souls under the guise of celebration."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch11_to_kael',
        'dialog': [
            "(grunting) Then we hit it hard and fast. No point letting it fester."
        ]
    },
    {
        'npc_id': 'kael',
        'dialog_id': 'kael_ch11_directs',
        'dialog': [
            "The worst of it is concentrated in the heart of the Festival of Delight. That's where their power is focused. Hessa has been watching the timelines. She'll know the best way to strike."
        ]
    },
    {
        'npc_id': 'hessa',
        'dialog_id': 'hessa_ch11_intro',
        'dialog': [
            "I've seen a thousand futures burn. In every one, this city is the kindling.",
            "Rapture and Revelry have turned the Festival of Delight into a living pyre. The deeper you go, the more reality itself starts to fracture under the weight of their excess."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_to_hessa',
        'dialog': [
            "Then we end it here. No more lives lost to this madness."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch11_to_hessa',
        'dialog': [
            "We must be precise. Their power feeds on emotional extremes. Calm focus will be our greatest weapon."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch11_narrator_ember_arrives',
        'dialog': [
            "Ember comes in from the street, looking weary but resolute."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch11_stays',
        'dialog': [
            "I’ve spoken with enough people here... seen what this 'festival' is doing to them.",
            "I’m staying. They need someone to remind them what real feeling feels like - not this forced euphoria.",
            "I’ll keep doing what I can for those who are breaking."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch11_to_ember_stays',
        'dialog': [
            "You sure? This place is swallowing people whole."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch11_response_to_magic',
        'dialog': [
            "(small, tired smile) That’s exactly why I can’t leave. If I run now… who’s left to remember what this actually costs?",
            "Someone has to keep caring when it hurts."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_to_ember_stays',
        'dialog': [
            "(gently, with respect) Then we’ll carry your hope with us. Stay safe, Ember."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch11_to_ember_stays',
        'dialog': [
            "(nodding once) A soldier’s choice. Respect."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch11_narrator_boss_intro',
        'dialog': [
            "The air in the Festival Heart is electric, thick with the smell of ozone and spilled wine.",
            "Manic laughter and screams echo in a sickening harmony. At the center, two figures pulse with chaotic energy."
        ]
    },
    {
        'npc_id': 'revelry',
        'dialog_id': 'revelry_ch11_intro',
        'dialog': [
            "(A whirlwind of color and sound) MORE! ALWAYS MORE! Can you feel it? The joy! The freedom! Why would you ever want it to stop?"
        ]
    },
    {
        'npc_id': 'rapture',
        'dialog_id': 'rapture_ch11_intro',
        'dialog': [
            "(A predator of sensation, still and coiled) They don't want it to stop. They want the thrill. The edge. The moment the bone snaps and the world feels real."
        ]
    },
    {
        'npc_id': 'revelry',
        'dialog_id': 'revelry_ch11_taunt_1',
        'dialog': [
            "We give them what they crave! A world without consequence! A party that never ends!"
        ]
    },
    {
        'npc_id': 'rapture',
        'dialog_id': 'rapture_ch11_taunt_1',
        'dialog': [
            "We give them truth. Pain is truth. Fear is truth. The rest is just noise."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch11_boss_response',
        'dialog': [
            "You're monsters. You're twisting people into puppets."
        ]
    },
    {
        'npc_id': 'revelry',
        'dialog_id': 'revelry_ch11_response',
        'dialog': [
            "(Laughs, a sound like breaking glass) We're liberators! We free them from their boring, quiet lives! We gave them a fire to dance in!"
        ]
    },
    {
        'npc_id': 'rapture',
        'dialog_id': 'rapture_ch11_response',
        'dialog': [
            "And you are the fuel. Your fear, your anger, your desperate hope... it all burns so beautifully."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch11_narrator_aftermath_1',
        'dialog': [
            "The manic energy suddenly implodes. The Festival Heart falls deathly silent as Rapture and Revelry shatter apart like glass under too much pressure.",
            "The artificial euphoria that had gripped the people at the festival begins to unravel. Manic laughter dies out.",
            "The streets grow quieter as people blink, confused, as if waking from a fever dream."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch11_aftermath_1',
        'dialog': [
            "(breathing heavily) Finally. Those two were a special kind of sick."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch11_aftermath_1',
        'dialog': [
            "The emotional feedback loop is collapsing. Their influence is breaking."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_aftermath_1',
        'dialog': [
            "(looking toward the city) Ember... she’s still out there with the others. I hope she’s safe."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch11_aftermath_1',
        'dialog': [
            "(unusually subdued) They’re all going to feel everything at once now. The real stuff. The ugly stuff."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch11_aftermath_1',
        'dialog': [
            "Better to feel pain than live in a lie. They have a chance to heal."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch11_aftermath_1',
        'dialog': [
            "(grunting) Better lost than broken. At least now they can start again."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_aftermath_2',
        'dialog': [
            "We should get back. The people will need help recovering... and I need to find Ember."
        ]
    },
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_ch11_breaks_news_1',
        'dialog': [
            "(looking exhausted but relieved) You're back. We saw the lights from the Festival Heart go dark... then everything just... stopped.",
            "The screaming, the laughing - all of it."
        ]
    },
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_ch11_breaks_news_2',
        'dialog': [
            "(voice shaky) The rioters lost control completely. It turned into a mob.",
            "People were trampling each other trying to get closer to the center... it was chaos.",
            "Ember was right in the middle of it. She was still trying to reach people — still singing...",
            "Still trying to remind them what real feelings felt like instead of that forced madness..."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch11_narrator_finds_ember',
        'dialog': [
            "The group notices Ember's body lying nearby, covered by a worn cloak. She looks peaceful, but clearly gone."
        ]
    },
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_ch11_breaks_news_3',
        'dialog': [
            "(voice tight, looking down) ...She didn't make it. One of the surges caught her while she was trying to pull someone out of the crowd."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_mourns_ember_1',
        'dialog': [
            "(quiet, heavy, voice breaking) ...Ember...",
            "(tears already falling) She stayed until the very end. Even as everything was collapsing around her, she was still trying to give people something real to hold onto.",
            "She told me... not to let the world forget how to feel — even the sadness."
        ]
    },
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_ch11_mourns_ember',
        'dialog': [
            "(eyes welling up instantly) No... She was still out here with us. Helping people. Singing to the ones who were breaking down..."
        ]
    },
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_ch11_mourns_ember',
        'dialog': [
            "(voice tight) She knew the risk. She chose to stay anyway."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_mourns_ember_2',
        'dialog': [
            "(voice cracking, tears falling) She stayed until the end. Even as everything was collapsing...",
            "she was still trying to give people something real to hold onto. She told me not to let the world forget how to feel — even the sadness."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch11_mourns_ember',
        'dialog': [
            "(looking down, fists clenched) Damn it. She had more heart than most warriors I’ve known...",
            "She stood her ground when the rest of us went for the throat."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch11_mourns_ember',
        'dialog': [
            "(soft, respectful) Her presence was steady. She reminded us why we fight. We will carry that with us."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch11_mourns_ember',
        'dialog': [
            "(unusually quiet, no smirk) ...She was tough. Braver than I gave her credit for.",
            "I thought she'd pull through just to annoy us with another song."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch11_mourns_ember',
        'dialog': [
            "(looking away, voice low) The emotional backlash from those two Voidwalkers was catastrophic.",
            "She was in the wrong place at the exact wrong time. ...She shouldn't have had to die for this."
        ]
    },
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_ch11_ember_brother',
        'dialog': [
            "Ember once said if anything happened to her, she has a brother in Quantford Hollow named Rell. Some kind of performer.",
            "She wanted him to know that no matter how dark the night there will always be light in the morning."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_new_quest',
        'dialog': [
            "Then we honor that. We go to Quantford Hollow."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch11_new_quest',
        'dialog': [
            "Damn right. I'm not letting her last request die with her."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch11_new_quest',
        'dialog': [
            "Road trip it is. Hopefully Rell throws better parties than this shithole."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch11_new_quest',
        'dialog': [
            "Another town. Another ghost to deliver bad news to. Wonderful."
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch11_condolences',
        'dialog': [
            "(nodding solemnly) I heard what happened at the Festival. Ember fought harder than most. You have my condolences."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_to_vek',
        'dialog': [
            "Thank you, Vek. She gave everything so others could feel again."
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch11_status_report',
        'dialog': [
            "The city is still raw, but we're stabilizing. People are starting to remember who they were before the madness took them."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch11_to_vek',
        'dialog': [
            "Good. World needs more people like you keeping order when it all goes to hell."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch11_to_vek',
        'dialog': [
            "And here I thought you'd be the type to enjoy a little chaos."
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch11_response_to_magic',
        'dialog': [
            "Chaos has its place. Just not when it eats people alive."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_informs_vek',
        'dialog': [
            "We're heading to Quantford Hollow next. Ember had a brother there — Rell. We need to tell him what happened."
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch11_about_rell',
        'dialog': [
            "Rell... yeah, I've crossed paths with him. He's a good man, but this news will hit him hard.",
            "Before you go, there's one last problem. A camp of nihilists still preaching that 'nothing matters' in the old festival grounds.",
            "They're feeding on the leftover despair. Deal with them, and I'll feel better about you heading out."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch11_to_vek',
        'dialog': [
            "Of course there are still stragglers..."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch11_to_vek_nihilists',
        'dialog': [
            "Finally, something I can hit."
        ]
    },
    {
        'npc_id': 'nihilist_leader',
        'dialog_id': 'nihilist_leader_ch11_intro',
        'dialog': [
            "(voice hollow, eyes empty) Why fight? Why feel? In the end, everything collapses. Everything rots.",
            "Ember proved it — even the brightest song ends in silence."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch11_to_nihilist',
        'dialog': [
            "Wow. You really know how to bring down the mood."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch11_to_nihilist',
        'dialog': [
            "Nihilism as a sales pitch. How original."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch11_to_nihilist',
        'dialog': [
            "Talking's over. You want silence? I'll give you some."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch11_to_nihilist',
        'dialog': [
            "His words carry weight... but they are poison."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_to_nihilist',
        'dialog': [
            "Grief does not justify dragging others into despair. We will not let you spread this further."
        ]
    },
    {
        'npc_id': 'nihilist_leader',
        'dialog_id': 'nihilist_leader_ch11_taunt',
        'dialog': [
            "(laughing bitterly) Then strike me down. It changes nothing. The wave is coming..."
        ]
    },
    {
        'npc_id': 'nihilist_leader',
        'dialog_id': 'nihilist_leader_ch11_outro',
        'dialog': [
            "(gasping as he falls) See...? Even victory... feels empty..."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch11_after_nihilist',
        'dialog': [
            "Keep telling yourself that."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch11_after_nihilist',
        'dialog': [
            "Dramatic to the end. I almost respect it."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_after_nihilist',
        'dialog': [
            "No one's pain should become a weapon against the living."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch11_after_nihilist',
        'dialog': [
            "Another echo of the same sickness... Let's hope this was the last of them."
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch11_after_nihilist',
        'dialog': [
            "(arms crossed, nodding with respect) You handled them cleanly. The city's safer for it. Thank you."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_to_vek_after_nihilist',
        'dialog': [
            "We couldn't leave this place still bleeding."
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch11_joins',
        'dialog': [
            "I've been thinking... I've done what I can here. The resistance needs strong hands across the continents.",
            "If you'll have me, I'd like to join you on the Rustwing. Someone needs to keep order while the rest of you do the impossible."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch11_vek_joins',
        'dialog': [
            "(grinning) Finally. Someone who knows how to throw a punch and keep a cool head."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch11_vek_joins',
        'dialog': [
            "Welcome to the circus, Commander."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch11_vek_joins',
        'dialog': [
            "Your tactical experience will be useful. Try not to lecture us too much."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch11_vek_joins',
        'dialog': [
            "Your strength and sense of duty are welcome, Vek. We would be honored."
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch11_settled',
        'dialog': [
            "Then it's settled."
        ]
    }
]

TASKS = [
    {
        'task_id': 'main_story_ch11_meet_ember_in_rapture_revelry',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'ember',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'kael', 'location': 'region_city_bar' }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'hessa', 'location': 'region_city_inn' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'ember', 'location': 'region_city_inn' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'kael', 'standing_text': ["The Festival Heart is the anchor. Break it and the whole city crashes."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'hessa', 'standing_text': ["I can't keep patching them up... they're all breaking."]}},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch11_narrator_intro' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch11_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_to_ember_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch11_to_ember_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch11_to_ember_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch11_directs' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'ember', 'standing_text': ["Rapture and Revelry are feeding off the city's emotions, amplifying the extremes. We need to stop them before it spirals out of control."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch11_meet_kael' }}
        ]
    },
    {
        'task_id': 'main_story_ch11_meet_kael',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'kael',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'kael', 'dialog_id': 'kael_ch11_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch11_to_kael' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch11_to_kael' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_to_kael' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch11_to_kael' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'kael', 'dialog_id': 'kael_ch11_directs' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'kael', 'standing_text': ["Hessa can see the paths. She's waiting for you. Break the cycle, for Ember."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch11_meet_hessa' }}
        ]
    },
    {
        'task_id': 'main_story_ch11_meet_hessa',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'hessa',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'hessa', 'dialog_id': 'hessa_ch11_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_to_hessa' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch11_to_hessa' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch11_narrator_ember_arrives' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch11_stays' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch11_to_ember_stays' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch11_response_to_magic' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_to_ember_stays' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch11_to_ember_stays' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'hessa', 'standing_text': ["The Festival of Delight is the heart of their power. The deeper you go, the more reality fractures under the weight of their excess."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'ember', 'standing_text': ["I’m staying. They need someone to remind them what real feeling feels like - not this forced euphoria. I’ll keep doing what I can for those who are breaking."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch11_meet_revelry' }}
        ]
    },
    {
        'task_id': 'main_story_ch11_meet_revelry',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'revelry',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'rapture', 'location': None }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'revelry', 'location': None }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rapture', 'standing_text': ["They don't want it to stop. They want the thrill. The edge. The moment the bone snaps and the world feels real."]}},
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'festival_of_delight', 'location': 'region_open_area' }}
        ],
        'task_complete_events': [
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'festival_of_delight', 'item_id': 'watch_of_perpetuation', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'festival_of_delight', 'item_id': 'morale_blade', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'festival_of_delight', 'item_id': 'stagelight_crown', 'location': 'treasure_room' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch11_narrator_boss_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'revelry', 'dialog_id': 'revelry_ch11_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rapture', 'dialog_id': 'rapture_ch11_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'revelry', 'dialog_id': 'revelry_ch11_taunt_1' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rapture', 'dialog_id': 'rapture_ch11_taunt_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch11_boss_response' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'revelry', 'dialog_id': 'revelry_ch11_response' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rapture', 'dialog_id': 'rapture_ch11_response' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'revelry', 'standing_text': ["We give them what they crave! A world without consequence! A party that never ends!"]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch11_defeat_rapture_and_revelry' }}
        ]
    },
    {
        'task_id': 'main_story_ch11_defeat_rapture_and_revelry',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'rapture_revelry_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'rapture_revelry_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch11_narrator_aftermath_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch11_aftermath_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch11_aftermath_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_aftermath_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch11_aftermath_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch11_aftermath_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch11_aftermath_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_aftermath_2' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'revelry' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'tess', 'location': 'region_city_inn' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'sam', 'location': 'region_city_inn' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'ember' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'tess', 'standing_text': ["I... I feel like I can breathe again. Like I can think again."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'hessa', 'standing_text': ["The Festival Heart is broken. The city is reeling. We need to help them heal."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'kael', 'standing_text': ["The city is vulnerable now. We need to protect it while it recovers."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch11_meet_sam_after_rapture_revelry' }}
        ]
    },
    {
        'task_id': 'main_story_ch11_meet_sam_after_rapture_revelry',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'sam',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sam', 'dialog_id': 'sam_ch11_breaks_news_1' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'tess', 'dialog_id': 'tess_ch11_breaks_news_2' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch11_narrator_finds_ember' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sam', 'dialog_id': 'sam_ch11_breaks_news_3' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_mourns_ember_1' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'tess', 'dialog_id': 'tess_ch11_mourns_ember' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sam', 'dialog_id': 'sam_ch11_mourns_ember' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_mourns_ember_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch11_mourns_ember' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch11_mourns_ember' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch11_mourns_ember' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch11_mourns_ember' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sam', 'dialog_id': 'sam_ch11_ember_brother' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_new_quest' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch11_new_quest' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch11_new_quest' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch11_new_quest' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'sam', 'standing_text': ["We need to get to Quantford Hollow. Ember had a brother there — Rell. We need to tell him what happened."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch11_meet_vek_again' }},
            { 'event_type': 'advance_chapter' }
        ]
    },
    {
        'task_id': 'main_story_ch11_meet_vek_again',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vek',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch11_condolences' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_to_vek' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch11_status_report' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch11_to_vek' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch11_to_vek' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch11_response_to_magic' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_informs_vek' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch11_about_rell' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch11_to_vek' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch11_to_vek_nihilists' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'vek', 'standing_text': ["Ember was a good person. I'm sorry for your loss."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch11_meet_nihilist_leader' }}
        ]
    },
    {
        'task_id': 'main_story_ch11_meet_nihilist_leader',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'nihilist_leader',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'nihilist_leader', 'location': None }},
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'nihilist_camp', 'location': 'region_open_area' }}
        ],
        'task_complete_events': [
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'nihilist_camp', 'item_id': 'ring_of_eternal_flame', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'nihilist_camp', 'item_id': 'encore_blades', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'nihilist_camp', 'item_id': 'hearthroot_robe', 'location': 'treasure_room' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'nihilist_leader', 'dialog_id': 'nihilist_leader_ch11_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch11_to_nihilist' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch11_to_nihilist' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch11_to_nihilist' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch11_to_nihilist' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_to_nihilist' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'nihilist_leader', 'dialog_id': 'nihilist_leader_ch11_taunt' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'nihilist_leader', 'standing_text': ["Nothing matters. Nothing lasts. Nothing is real."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch11_defeat_nihilist_leader' }}
        ]
    },
    {
        'task_id': 'main_story_ch11_defeat_nihilist_leader',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'nihilist_leader_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'nihilist_leader_1', 'combat_type': 'combat' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'nihilist_leader', 'dialog_id': 'nihilist_leader_ch11_outro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch11_after_nihilist' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch11_after_nihilist' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_after_nihilist' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch11_after_nihilist' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'nihilist_leader' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch11_meet_vek_after_nihilist' }}
        ]
    },
    {
        'task_id': 'main_story_ch11_meet_vek_after_nihilist',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vek',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch11_after_nihilist' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_to_vek_after_nihilist' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch11_joins' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch11_vek_joins' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch11_vek_joins' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch11_vek_joins' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch11_vek_joins' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch11_settled' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'vek', 'standing_text': ["I will join you on the Rustwing. Someone needs to keep order while the rest of you do the impossible."]}},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'vek' }},
            { 'event_type': 'character_join', 'params': { 'character_id': 'vek' }}
        ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_11',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}