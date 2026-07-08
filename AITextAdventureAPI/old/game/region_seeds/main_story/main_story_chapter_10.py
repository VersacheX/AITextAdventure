# ============================================================
# = CHAPTER 10 : HUMAN CHAOS
# ============================================================
#
# [ LOCATION - CROSSWIND BAZAAR ]
# -----------------------------------
# @ = player
# S = Serin (manic reveler)
# P = Pox (stimulant dealer)
# N = Nara (overdosing dancer)
# E = Ember (witness)
# V = Vek (city enforcer)
#
# High level: The party follows Ember to Crosswind Bazaar, a city
# drowning in forced joy and manic celebration. They encounter a
# society addicted to stimulants to avoid emotional crashes. The
# situation devolves into a riot, where they meet Vek, a local
# enforcer trying to maintain order.

ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
    {
        "npc_id": "serin",
        "name": "Serin",
        "description": "A manic reveler terrified of the silence. She forces a constant state of joy and motion, believing that to stop moving is to be consumed by emptiness.",
        "psychology": {
            "mbti": "ESFP",
            "dominant": "Se - Completely absorbed in the immediate sensory experience of the party, chasing the next high.",
            "auxiliary": "Fi - Her actions are driven by a deep, internal fear of feeling 'nothing'. Her 'joy' is a desperate defense mechanism.",
            "tertiary": "Te - When her high is threatened, she can become surprisingly forceful and direct in telling others to keep the party going.",
            "inferior": "Ni - Underneath the mania, she has a paranoid, abstract fear of 'the emptiness' that will come if the celebration stops."
        },
        "enneagram": {
          "enneagram_type": "7w6",
          "core_fear": "Being trapped in emotional pain or boredom.",
          "core_desire": "To be happy and stimulated.",
          "defense_mechanism": "Rationalization — Frames her manic energy as 'joy' and 'freedom' to avoid the underlying terror of what happens when the party stops.",
          "stress_line": "Moves to Type 1 — Becomes rigid and critical of anyone who threatens to stop the fun.",
          "growth_line": "Moves to Type 5 — Becomes more introspective and able to sit with her feelings without needing constant stimulation.",
          "instinctual_variant": "so/sx — A social catalyst, drawing energy from the group's excitement and seeking intense connections within it."
        },
        'image': 'npcs:serin1'
    },
    {
        "npc_id": "pox",
        "name": "Pox",
        "description": "A cynical dealer of stimulants, 'joy tonics', and 'rage shots'. He sees himself not as a predator, but as a pragmatist providing a necessary service in a city that runs on momentum.",
        "psychology": {
            "mbti": "ISTP",
            "dominant": "Ti - Logically analyzes the city's emotional economy and provides a product to meet its demands. He is detached from the moral implications.",
            "auxiliary": "Se - Reacts to the immediate opportunities for profit, adapting his inventory to the crowd's needs.",
            "tertiary": "Ni - Has a background intuition that the whole system is unsustainable, but focuses on the present.",
            "inferior": "Fe - Is awkward and dismissive when confronted with the emotional consequences of his products, preferring to stick to transactional logic."
        },
        "enneagram": {
          "enneagram_type": "5w6",
          "core_fear": "Being useless or overwhelmed by a system he can't control.",
          "core_desire": "To be competent and capable.",
          "defense_mechanism": "Isolation — Detaches from the moral and emotional consequences of his work, viewing it as a purely logical system of supply and demand.",
          "stress_line": "Moves to Type 7 — Becomes scattered and anxious when his business is threatened or the system becomes too chaotic.",
          "growth_line": "Moves to Type 8 — Uses his understanding of the system to take confident, decisive action.",
          "instinctual_variant": "sp/so — Hoards his resources and knowledge for his own security, using his business to navigate the social landscape."
        },
        'image': 'npcs:pox1'
    },
    {
        "npc_id": "nara",
        "name": "Nara",
        "description": "A dancer who has completely surrendered to the manic energy of the festival. She is on the verge of physical and mental collapse but is unable to stop.",
        "psychology": {
            "mbti": "ENFP",
            "dominant": "Ne - Lost in a sea of possibilities, unable to focus on any one thing, constantly seeking the next novel sensation.",
            "auxiliary": "Fi - Her core identity has been subsumed by the 'feeling' of the festival; she believes she is truly 'alive' in this state.",
            "tertiary": "Te - Her actions are completely disorganized, lacking any structure or goal beyond continuing the experience.",
            "inferior": "Si - Has lost all connection to her own physical state, ignoring her body's warning signs of collapse."
        },
        "enneagram": {
          "enneagram_type": "7w8",
          "core_fear": "Being trapped in pain or boredom.",
          "core_desire": "To be free and stimulated.",
          "defense_mechanism": "Rationalization — Frames her manic dancing as 'living life to the fullest' to avoid the reality of her physical and mental collapse.",
          "stress_line": "Moves to Type 1 — Becomes rigid and self-critical when her body starts to fail her.",
          "growth_line": "Moves to Type 5 — Becomes more introspective and able to find joy in quieter, more sustainable ways.",
          "instinctual_variant": "sx/so — Seeks intense experiences and connections within the festival, losing herself in the collective energy."
        },
        'image': 'npcs:nara1'
    },
    {
        "npc_id": "vek",
        "name": "Marshal Vek Drast",
        "description": "A tough, no-nonsense city enforcer with a powerful sense of order and duty. She is trying to keep her city from tearing itself apart from the inside out.",
        "psychology": {
            "mbti": "ENTJ",
            "dominant": "Te - Decisive, commanding, and focused on imposing order on the chaos around her. She takes charge instinctively.",
            "auxiliary": "Ni - Has a clear vision of what a stable, functioning city should look like and works tirelessly towards that goal.",
            "tertiary": "Se - Is physically present and forceful, willing to get her hands dirty to stop a riot or enforce the rules.",
            "inferior": "Fi - Her strong internal principles of duty and order are her primary motivation, but she struggles to express vulnerability or connect on a softer emotional level."
        },
        "enneagram": {
          "enneagram_type": "8w9",
          "core_fear": "Being controlled by chaos or others.",
          "core_desire": "To be in control of her environment and destiny.",
          "defense_mechanism": "Denial — Denies the world's chaos by imposing her own rigid structure upon it, refusing to accept powerlessness.",
          "stress_line": "Moves to Type 5 — Becomes secretive and withdrawn when her strategies fail, fearing the chaos she can't control.",
          "growth_line": "Moves to Type 2 — Uses her strength to protect and empower others, becoming a true leader rather than just a commander.",
          "instinctual_variant": "so/sp — Focused on controlling the social order to ensure her own security and the survival of the group."
        },
        'image': 'vek1.jpeg'
    }
]

NPC_DIALOG = [
    {
        'npc_id': None,
        'dialog_id': 'ch10_narrator_intro',
        'dialog': [
            "Chapter 10 - When feeling becomes mandatory, humanity becomes optional."
        ]
    },
    {
        'npc_id': 'serin',
        'dialog_id': 'serin_ch10_intro',
        'dialog': [
            "Keep moving! Keep dancing! Don't stop! Don't you dare stop!",
            "If you stop smiling the joy leaves you... and then the emptiness comes..."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch10_to_serin',
        'dialog': [
            "This is beautiful chaos. I almost respect it."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch10_to_serin',
        'dialog': [
            "She's smiling like a maniac but looks ready to drop dead."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch10_to_serin',
        'dialog': [
            "You're exhausted. Your body is breaking."
        ]
    },
    {
        'npc_id': 'serin',
        'dialog_id': 'serin_ch10_response',
        'dialog': [
            "Better to burn out than feel nothing! You should speak to Pox, you can go all night, just let your body vibe."
        ]
    },
    {
        'npc_id': 'pox',
        'dialog_id': 'pox_ch10_intro',
        'dialog': [
            "I make stimulants. Joy tonics. Rage shots. Anything to keep the party going.",
            "People pay anything to avoid the crash. Even if it kills them faster."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch10_to_pox',
        'dialog': [
            "You're literally selling addiction as entertainment."
        ]
    },
    {
        'npc_id': 'pox',
        'dialog_id': 'pox_ch10_response',
        'dialog': [
            "I'm selling survival. The city runs on momentum now. Slow down and you die inside."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch10_intro',
        'dialog': [
            "They’re burning themselves alive with joy. I’m trying to remind them there’s still such a thing as real feeling… even when it’s painful.",
            "That's what it wants. It wants you addicted to the wave."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch10_to_ember',
        'dialog': [
            "Please stay with us. This place will consume you."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch10_response',
        'dialog': [
            "I know. But if no one stays to see what this is really doing to them… then it just wins."
        ]
    },
    {
        'npc_id': 'nara',
        'dialog_id': 'nara_ch10_manic',
        'dialog': [
            "(laughing wildly) I don't care! I feel alive! I feel everything!"
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch10_narrator_nara_collapse',
        'dialog': [
            "Nara dances wildly, sweating, eyes bloodshot, but still forcing laughter."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch10_observes_nara',
        'dialog': [
            "She's on the verge of collapse..."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch10_observes_nara',
        'dialog': [
            "Her body is breaking but she can't stop."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch10_narrator_riot_starts',
        'dialog': [
            "The crowd surges violently outside, fueled by manic energy."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch10_rioter1_dialog',
        'dialog': [
            "MORE! GIVE US MORE! I CAN STILL FEEL SOMETHING!"
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch10_rioter2_dialog',
        'dialog': [
            "DON'T STOP THE MUSIC! IF IT STOPS I'LL DIE INSIDE!"
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch10_intro',
        'dialog': [
            "(shoving through the crowd, voice cutting like a whip) Back off! You're trampling people! Have you all lost your damn minds?!"
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch10_riot_response',
        'dialog': [
            "(stepping up beside the stranger, cracking his knuckles) Finally, something that makes sense.",
            "These idiots need to be knocked out of it!"
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch10_riot_response',
        'dialog': [
            "This is escalating too fast. The emotional contagion is turning into a riot."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch10_narrator_riot_surge',
        'dialog': [
            "The rioters surge forward, eyes wild with manic hunger, completely lost to the wave."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch10_narrator_riot1_end',
        'dialog': [
            "The crowd surges violently, eyes glazed with manic frenzy. Rioters lash out at anything that moves."
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch10_riot1_end',
        'dialog': [
            "(shoving through the chaos, voice booming) Stand down! You're killing each other over nothing!"
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch10_riot1_end',
        'dialog': [
            "Finally, someone who gets it! Let's knock some sense into these idiots!"
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_ch10_riot1_end',
        'dialog': [
            "This ain't a fight - it's a damn stampede!"
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch10_riot1_end',
        'dialog': [
            "The wind is screaming with them... they're completely lost!"
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch10_riot1_end',
        'dialog': [
            "This is like trying to fight a tornado made of people!"
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch10_narrator_riot2_end',
        'dialog': [
            "The second wave crashes harder. Bodies slam together. The manic energy turns feral."
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch10_riot2_end',
        'dialog': [
            "(breathing heavily, wiping blood from her lip) These people are gone. The wave has them completely."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch10_riot2_end',
        'dialog': [
            "Yeah... this ain't right. They're not even fighting us. They're just breaking."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch10_riot2_end',
        'dialog': [
            "The emotional infection is spreading faster than we can contain."
        ]
    },
    {
        'npc_id': 'korin',
        'dialog_id': 'korin_ch10_riot2_end',
        'dialog': [
            "(quietly) Like frostbite... it numbs you before it destroys you."
        ]
    },
    {
        'npc_id': 'ember',
        'dialog_id': 'ember_ch10_departs',
        'dialog': [
            "(voice strained, stepping back from the fray) I... I don't think I can help here. Not anymore. This coruption here is too deep.",
            "I’m heading to Blackwake Bay. The ports are drowning in the same kind of frenzy. Someone still needs to remind them what real feeling feels like."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch10_to_ember_departs',
        'dialog': [
            "Be careful, Ember. We'll meet you there when we can."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch10_to_ember_departs',
        'dialog': [
            "Another city, another storm. This is never going to end, is it?"
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch10_riot3_end',
        'dialog': [
            "(wiping sweat and blood, breathing hard) ...It's finally breaking. The wave is dying down. I can handle the rest from here.",
            "Go. Find your singer before she walks into worse."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch10_to_vek_end',
        'dialog': [
            "You sure? You look like hell."
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch10_response_end',
        'dialog': [
            "I've looked worse. This is my city. I'll clean it up."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch10_to_vek_end',
        'dialog': [
            "Thank you, Vek. We won't forget this."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch10_end',
        'dialog': [
            "One more storm to chase..."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch10_end',
        'dialog': [
            "(grunting) Then we follow Ember. No point stopping now."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch10_end',
        'dialog': [
            "Blackwake Bay it is. Hope the ports aren't as crazy as this."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch10_end',
        'dialog': [
            "Crazy is fine. Boring is the real killer."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch10_end',
        'dialog': [
            "Logically, we're already committed. Might as well keep momentum."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch10_end',
        'dialog': [
            "The corruption is spreading. We move."
        ]
    }
]

TASKS = [
    {
        'task_id': 'main_story_ch10_meet_serin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'serin',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'serin', 'location': 'region_city_bar' }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'pox', 'location': 'region_city_shopitems' }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'nara', 'location': 'region_city_bar' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'ember', 'location': 'region_city_bar' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'pox', 'standing_text': ["Joy tonics! Rage shots! Anything to keep the wave going. Don't let the emptiness catch you."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'nara', 'standing_text': ["Can't stop... won't stop... have to keep moving..."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'ember', 'standing_text': ["They're burning so brightly... but the fire is consuming them. Someone has to offer a gentler light."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'mira', 'standing_text': ["Got something to ride the high longer? Or something to finally crash it? Your choice, traveler."]}},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch10_narrator_intro' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'serin', 'dialog_id': 'serin_ch10_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch10_to_serin' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch10_to_serin' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch10_to_serin' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'serin', 'dialog_id': 'serin_ch10_response' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'serin', 'standing_text': ["Dance! Laugh! Never stop! The crash is worse than the high!"]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch10_meet_pox' }}
        ]
    },
    {
        'task_id': 'main_story_ch10_meet_pox',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'pox',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'pox', 'dialog_id': 'pox_ch10_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch10_to_pox' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'pox', 'dialog_id': 'pox_ch10_response' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'pox', 'standing_text': ["The Festival Heart keeps the wave going. Break it and the whole city crashes."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch10_meet_ember_in_festival' }}
        ]
    },
    {
        'task_id': 'main_story_ch10_meet_ember_in_festival',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'ember',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch10_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch10_to_ember' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch10_response' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'nara', 'dialog_id': 'nara_ch10_manic' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch10_narrator_nara_collapse' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch10_observes_nara' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch10_observes_nara' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch10_narrator_riot_starts' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch10_rioter1_dialog' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch10_rioter2_dialog' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch10_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch10_riot_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch10_riot_response' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch10_narrator_riot_surge' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'nara', 'standing_text': ["Can't stop... won't stop..."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'ember', 'standing_text': ["I'll keep singing. Maybe one person will slow down long enough to feel something real."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch10_defeat_rioters_1' }}
        ]
    },
    {
        'task_id': 'main_story_ch10_defeat_rioters_1',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'festival_rioters_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'festival_rioters_1', 'combat_type': 'combat' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch10_narrator_riot1_end' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch10_riot1_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch10_riot1_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_ch10_riot1_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch10_riot1_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch10_riot1_end' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch10_defeat_rioters_2' }}
        ]
    },
    {
        'task_id': 'main_story_ch10_defeat_rioters_2',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'festival_rioters_2',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'festival_rioters_2', 'combat_type': 'combat' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch10_narrator_riot2_end' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch10_riot2_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch10_riot2_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch10_riot2_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'korin', 'dialog_id': 'korin_ch10_riot2_end' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'ember', 'dialog_id': 'ember_ch10_departs' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch10_to_ember_departs' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch10_to_ember_departs' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'ember' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch10_defeat_rioters_3' }}
        ]
    },
    {
        'task_id': 'main_story_ch10_defeat_rioters_3',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'festival_rioters_3',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'festival_rioters_3', 'combat_type': 'combat' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch10_riot3_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch10_to_vek_end' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch10_response_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch10_to_vek_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch10_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch10_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch10_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch10_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch10_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch10_end' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'ember' }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'vek', 'location': 'region_city_bar' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'vek', 'standing_text': ["I can handle the rest. Go find your singer before she walks into worse."]}},
            { 'event_type': 'advance_chapter' }
        ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_10',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}