# ============================================================
# = CHAPTER 12 : LAMENT
# ============================================================
#
# [ LOCATION - QUANTFORD HOLLOW ]
# -----------------------------------
# @ = player
# R = Rell (Ember's grieving brother)
# L = Lament (Voidwalker of Grief)
# A = Archivist Fragment (time-looped guide)
# V = Veyla (scattered singer)
# S = Serin (recovering reveler)
#
# High level: The party travels to Quantford Hollow to inform Ember's
# brother, Rell, of her death. Their collective grief attracts the
# Voidwalker Lament, who traps the village in a time loop of sorrow.
# The party must navigate the looping grief and confront Lament to
# find a path forward.

ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
    {
        "npc_id": "rell",
        "name": "Rell",
        "description": "Ember's brother, a talented performer whose music was once full of life. Now, he is consumed by the sudden and tragic loss of his sister, his art silenced by grief.",
        "psychology": {
            "mbti": "ISFP",
            "dominant": "Fi - His internal emotional world is shattered by grief. He processes his loss through a deeply personal, value-driven lens.",
            "auxiliary": "Se - Once used his connection to the physical world to create beautiful performances; now he is withdrawn and disconnected from it.",
            "tertiary": "Ni - In his grief, he may have flashes of insight or intuition about the nature of his sister's sacrifice and the darkness she fought.",
            "inferior": "Te - Struggles to organize his life or make logical plans, completely overwhelmed by his emotional state."
        },
        "enneagram": {
          "enneagram_type": "4w5",
          "core_fear": "Having no identity or significance outside of his grief.",
          "core_desire": "To find himself and his significance.",
          "defense_mechanism": "Introjection — Absorbs his grief and loss, making it the core of his identity and the lens through which he sees the world.",
          "stress_line": "Moves to Type 2 — Becomes overly dependent on others when his grief becomes too much to bear alone.",
          "growth_line": "Moves to Type 1 — Finds a new, principled purpose beyond his personal grief.",
          "instinctual_variant": "sx/sp — Intensely focused on his personal loss and the one-on-one connection he had with his sister."
        },
        "image": "npcs:rell1"
    },
    {
        "npc_id": "lament",
        "name": "Lament",
        "description": "A Voidwalker who embodies the concept of unending, unprocessed grief. She is drawn to sorrow and seeks to trap others in loops of loss, believing that grief is the only honest state of being.",
        "theme_song": "Mad World, Gary Jules",
        "psychology": {
            "mbti": "INFJ",
            "dominant": "Ni - Possesses a deep, almost cosmic understanding of sorrow and its patterns, seeing it as the ultimate endpoint of all things.",
            "auxiliary": "Fe - Perversely empathetic, she feels the grief of others and seeks to amplify it, believing she is guiding them to a state of 'truth'.",
            "tertiary": "Ti - Has a twisted internal logic that justifies her actions, framing endless grief as a form of purity.",
            "inferior": "Se - Is ethereal and disconnected from the physical world, manifesting as a being of shadow and sorrow rather than a concrete entity."
        },
        "enneagram": {
          "enneagram_type": "4w5",
          "core_fear": "Having no identity or significance.",
          "core_desire": "To have an identity, which it finds in the depths of sorrow and loss.",
          "defense_mechanism": "Introjection — Absorbs and amplifies all grief, making it a beautiful, all-consuming identity.",
          "stress_line": "Moves to Type 2 — Becomes clingy, trying to share its 'beautiful' sorrow with others.",
          "growth_line": "Moves to Type 1 — Would learn to find a principled path out of grief, towards healing.",
          "instinctual_variant": "sx/sp — Intensely focused on the deep, romantic tragedy of its own existence."
        },
        'image': 'voidwalkers:lament1.jpeg',
        'song_id': 'mad_world_gary_jules'
    },
    {
        "npc_id": "archivist_fragment",
        "name": "Archivist Fragment",
        "description": "A fractured piece of the Archivist, caught within Lament's time loop. It retains a sliver of the Archivist's knowledge but is disoriented by the broken causality.",
        "psychology": {
            "mbti": "INTP",
            "dominant": "Ti - Tries to logically analyze the illogical time loop, pointing out the paradoxes it creates.",
            "auxiliary": "Ne - Sees the branching, collapsing timelines caused by Lament's influence but cannot reconcile them.",
            "tertiary": "Si - Clings to fragmented memories of events that have 'already happened' multiple times in different ways.",
            "inferior": "Fe - Is completely detached from the emotional suffering of the loop, viewing it as a fascinating but unsolvable puzzle."
        },
        "enneagram": {
          "enneagram_type": "5w4",
          "core_fear": "Being overwhelmed by a reality that doesn't make sense.",
          "core_desire": "To understand the universe, even its paradoxes.",
          "defense_mechanism": "Isolation — Detaches from the emotional weight of the time loop to analyze it as a purely intellectual puzzle.",
          "stress_line": "Moves to Type 7 — Its thoughts become scattered and chaotic when the paradoxes become too overwhelming.",
          "growth_line": "Moves to Type 8 — Uses its unique understanding to take decisive action and guide others through the chaos.",
          "instinctual_variant": "sp/sx — A reclusive being of pure intellect, intensely focused on the puzzle of its own existence."
        },
        'image': 'npcs:archivist_fragment1'
    }
]

NPC_DIALOG = [
    {
        'npc_id': None,
        'dialog_id': 'ch12_narrator_intro',
        'dialog': [
            "Chapter 12 - In facing loss, time no longer moves forward... it folds inward."
        ]
    },
    {
        'npc_id': 'rell',
        'dialog_id': 'rell_ch12_intro',
        'dialog': [
            "(mid-performance, then stopping abruptly as he sees the group) ...You... Those faces..."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch12_to_rell',
        'dialog': [
            "(gently) You must be Rell, we heard of a performer here related to Ember... I'm sorry. Ember didn't make it. She stayed in the heart of the Festival of Delight, singing against the storm until the very end."
        ]
    },
    {
        'npc_id': 'rell',
        'dialog_id': 'rell_ch12_grief',
        'dialog': [
            "(the instrument slips from his hands) ...No. Not her. She always said she'd outlast the madness. She promised..."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch12_to_rell',
        'dialog': [
            "(unusually subdued) She was one of the few real things left in that circus. The world feels cheaper without her."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch12_to_rell',
        'dialog': [
            "(grunting) She had steel in her. Respect."
        ]
    },
    {
        'npc_id': 'rell',
        'dialog_id': 'rell_ch12_remembers',
        'dialog': [
            "(sinking onto a stool, head in hands) My sister... always trying to carry the weight for everyone else. I told her it would kill her one day. She just laughed and said someone had to."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch12_narrator_lament_arrival',
        'dialog': [
            "The air grows colder. Shadows lengthen unnaturally. A low, resonant hum fills the room as Lament begins to manifest - a swirling vortex of grief and fractured memory."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch12_intro_1',
        'dialog': [
            "(voice like wind through broken glass, everywhere and nowhere) Such beautiful pain... I felt it from across the veil. The anchor's song has finally gone silent."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch12_intro_2',
        'dialog': [
            "(taking form as a tall, veiled figure wrapped in flowing black and silver threads) I am Lament. The echo of every loss that was never allowed to heal. The grief that refuses to end."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch12_intro_3',
        'dialog': [
            "(tilting her head toward the party) You carry one of the Bracelets... and now you carry her absence. How exquisite. How devastating."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch12_to_lament',
        'dialog': [
            "Show yourself plainly. What do you want?"
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch12_response',
        'dialog': [
            "I want nothing. I am what remains when joy is weaponized and hope is trampled. I am what this world is becoming. Witness it. Feel the grief of every city, every soul crushed under the weight of false ecstasy and hollow order. Only then will you understand what you truly face."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch12_narrator_lament_departs',
        'dialog': [
            "Lament dissolves into swirling mist, leaving behind an oppressive silence and the faint sound of distant, looping sobs."
        ]
    },
    {
        'npc_id': 'rell',
        'dialog_id': 'rell_ch12_resolve',
        'dialog': [
            "(wiping his eyes, voice hardened) ...If my sister died trying to fight this, then I won't sit here singing pretty lies anymore. Tell me what you need. I'll help however I can."
        ]
    },
    {
        'npc_id': 'archivist_fragment',
        'dialog_id': 'archivist_fragment_ch12_intro',
        'dialog': [
            "I remember you dying. Twice. Time loops here. Lament's influence breaks causality. The village mourns someone called Ember. The grief never ends. It loops."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch12_to_archivist',
        'dialog': [
            "How do we fix it?"
        ]
    },
    {
        'npc_id': 'archivist_fragment',
        'dialog_id': 'archivist_fragment_ch12_explains',
        'dialog': [
            "You don't. You survive it. The Library of Contradictions holds the key. But first... you must face the grief."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch12_narrator_loop',
        'dialog': [
            "The village gathers in the square. Over and over. Remembering Ember. Each loop, the grief is fresh. The loss unprocessed."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch12_villager1_dialog',
        'dialog': [
            "They sang for us. They reminded us to feel."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch12_villager2_dialog',
        'dialog': [
            "And the festival crushed them. Like it crushes everything soft."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch12_observes_loop',
        'dialog': [
            "The loop won't let them move past the grief."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch12_observes_loop',
        'dialog': [
            "Lament feeds on this. Unending sorrow."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch12_observes_loop',
        'dialog': [
            "Ember died trying to help. And now their death causes more pain."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch12_observes_loop',
        'dialog': [
            "We have to break the loop. For them."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch12_instructs',
        'dialog': [
            "We should investigate what's going on around here after Lament's appearance, it seemed much healthier before"
        ]
    },
    {
        'npc_id': 'veyla',
        'dialog_id': 'veyla_ch12_loop',
        'dialog': [
            "(still scattered, clutching her head) The silence... it's almost worse than the noise. I keep hearing Ember's song in my head... but it's fading. She tried so hard to keep us grounded. Now everything feels... hollow."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch12_to_veyla',
        'dialog': [
            "The weight of her loss is already settling on this place."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch12_to_veyla',
        'dialog': [
            "The wind carries grief now. It's heavier than before."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch12_narrator_lament_reappears',
        'dialog': [
            "The air suddenly grows cold and thick. Shadows twist unnaturally as Lament manifests once more."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch12_taunt_1',
        'dialog': [
            "(voice echoing like distant, overlapping sobs) Such fragile anchors you mortals cling to. One voice silenced, and the whole town begins to unravel. You carry the Bracelet of Existence... a pitiful spark of meaning in a world begging to forget itself."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch12_narrator_lament_fades_again',
        'dialog': [
            "Lament fades into mist, leaving an oppressive chill behind."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch12_after_lament_taunt',
        'dialog': [
            "She's testing us. Or luring us."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch12_after_lament_taunt',
        'dialog': [
            "Either way, we cannot ignore the pull."
        ]
    },
    {
        'npc_id': 'serin',
        'dialog_id': 'serin_ch12_loop',
        'dialog': [
            "(forcing a brittle, twitching smile that doesn't reach her eyes) I... I should be happy, right? We won. The music stopped. Why does everything feel so heavy now? Ember used to sing real songs... but now when I try to remember them, there's just this... emptiness. Like something is pulling on my chest."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch12_to_serin',
        'dialog': [
            "(grunting) Fake joy always leaves a poison behind. Looks like it's still got its hooks in you."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_ch12_to_serin',
        'dialog': [
            "You're shaking like a leaf. Sit down before you collapse."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch12_narrator_lament_final_appearance',
        'dialog': [
            "The temperature plummets. Shadows stretch unnaturally across the room as Lament manifests in a swirl of dark, fraying threads."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch12_final_taunt',
        'dialog': [
            "(voice like wind through cracked tombstones) Look at her. Still performing. Still pretending. This is the gift my sister Revelry leaves behind - hollow shells smiling through the rot. Bring the Bracelet of Existence to The Necropolis. Let me show you the true shape of grief. Perhaps then you can help these broken things... or perhaps you will finally understand what it means to break."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch12_to_lament_final_taunt',
        'dialog': [
            "(dryly) She's really selling the whole \"come to my evil lair\" pitch."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch12_to_lament_final_taunt',
        'dialog': [
            "It's obviously a trap. But it might be the only lead we have on ending these loops for good."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch12_resolve',
        'dialog': [
            "We won't let this stand. We'll speak to Rell first, then head to the Necropolis."
        ]
    },
    {
        'npc_id': 'rell',
        'dialog_id': 'rell_ch12_final_request',
        'dialog': [
            "(looking up as the party returns) You're back already... Did you find anything?"
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch12_to_rell_final',
        'dialog': [
            "We spoke with Veyla and Serin. Lament appeared. She wants the Bracelet of Existence - says she'll show us the true shape of grief in The Necropolis. We believe it's connected to these loops. We have to go."
        ]
    },
    {
        'npc_id': 'rell',
        'dialog_id': 'rell_ch12_final_response',
        'dialog': [
            "(clenching his fists) My sister died fighting those monsters... and now this thing wants to use her death as bait? Go. Do what you have to. Just... don't let her sacrifice be for nothing."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch12_to_rell_final',
        'dialog': [
            "We won't. We'll end this loop and come back."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch12_to_rell_final',
        'dialog': [
            "Tell you what - when we return, you better have a real song ready. Not one of these sad ones."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch12_to_rell_final',
        'dialog': [
            "We'll carry her memory with us. She won't be forgotten."
        ]
    },
    {
        'npc_id': 'rell',
        'dialog_id': 'rell_ch12_farewell',
        'dialog': [
            "(nodding slowly) Then go. I'll be here... trying to remember how to play without her echo in my head."
        ]
    },
    # ── Type A hook dialogs ────────────────────────────────────────
    {
        'npc_id': 'rell',
        'dialog_id': 'rell_ch12_ember_keepsake_request',
        'dialog': [
            "(voice low, not quite looking at you)",
            "Before you go... there's something I've been trying to find.",
            "Ember kept a small keepsake — a pressed flower she carried everywhere.",
            "She said it was from the first meadow she ever performed in.",
            "After she... I couldn't find it.",
            "If it's anywhere, it's somewhere in the hollow. The fields around Quantford.",
            "I know it's a small thing. But right now small things are all I have left of her."
        ]
    },
    {
        'npc_id': 'rell',
        'dialog_id': 'rell_ch12_receives_keepsake',
        'dialog': [
            "(stares at the flower for a long moment)",
            "This is it.",
            "(his hands shake slightly as he takes it)",
            "She pressed it herself. Told me the petals kept their colour because the meadow wanted to be remembered.",
            "(quietly) She was right about a lot of things.",
            "Thank you for finding it.",
            "(steadies himself) Now. You have to go. Don't let her sacrifice mean nothing."
        ]
    },
]

TASKS = [
    {
        'task_id': 'main_story_ch12_meet_rell',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rell',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'lament', 'location': None }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'rell', 'location': 'region_city_inn' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'veyla', 'location': 'region_city_bar' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'serin', 'location': 'region_city_bar' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'serin', 'standing_text': ["I should be smiling... everyone needs me to smile... but it hurts now. Everything just hurts."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'veyla', 'standing_text': ["I can feel something heavy in the air. Like a storm is coming."]}},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch12_narrator_intro' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rell', 'dialog_id': 'rell_ch12_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch12_to_rell' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rell', 'dialog_id': 'rell_ch12_grief' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch12_to_rell' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch12_to_rell' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rell', 'dialog_id': 'rell_ch12_remembers' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch12_narrator_lament_arrival' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch12_intro_1' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch12_intro_2' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch12_intro_3' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch12_to_lament' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch12_response' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch12_narrator_lament_departs' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rell', 'dialog_id': 'rell_ch12_resolve' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rell', 'standing_text': ["Ember's gone... but her fight isn't over. What do you need from me?"]}},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'archivist_fragment', 'location': 'region_city_inn' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch12_meet_archivist_fragment' }}
        ]
    },
    {
        'task_id': 'main_story_ch12_meet_archivist_fragment',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'archivist_fragment',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'archivist_fragment', 'dialog_id': 'archivist_fragment_ch12_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch12_to_archivist' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'archivist_fragment', 'dialog_id': 'archivist_fragment_ch12_explains' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch12_narrator_loop' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch12_villager1_dialog' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch12_villager2_dialog' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch12_observes_loop' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch12_observes_loop' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch12_observes_loop' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch12_observes_loop' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch12_instructs' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'archivist_fragment', 'standing_text': ["Past and future collapse into paradox. The Library remembers everything. Even things that never happened."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch12_meet_veyla' }}
        ]
    },
    {
        'task_id': 'main_story_ch12_meet_veyla',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'veyla',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'veyla', 'dialog_id': 'veyla_ch12_loop' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch12_to_veyla' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch12_to_veyla' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch12_narrator_lament_reappears' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch12_taunt_1' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch12_narrator_lament_fades_again' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch12_after_lament_taunt' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch12_after_lament_taunt' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch12_meet_serin' }}
        ]
    },
    {
        'task_id': 'main_story_ch12_meet_serin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'serin',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'serin', 'dialog_id': 'serin_ch12_loop' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch12_to_serin' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_ch12_to_serin' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch12_narrator_lament_final_appearance' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch12_final_taunt' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch12_to_lament_final_taunt' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch12_to_lament_final_taunt' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch12_resolve' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch12_meet_rell_again' }}
        ]
    },
    {
        'task_id': 'main_story_ch12_meet_rell_again',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rell',
        'task_acquire_events': [
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rell', 'standing_text': [
                "Ember kept a pressed flower from the first meadow she ever performed in.",
                "I haven't been able to find it. If it's anywhere, it's out in the hollow fields.",
                "...Please. If you find it, bring it to me before you leave."
            ]}}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rell', 'dialog_id': 'rell_ch12_final_request' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch12_to_rell_final' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rell', 'dialog_id': 'rell_ch12_final_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch12_to_rell_final' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch12_to_rell_final' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch12_to_rell_final' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rell', 'dialog_id': 'rell_ch12_ember_keepsake_request' }},
            # ── Type A: award city chain + the deliver task back here ──
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch12_deliver_ember_keepsake_to_rell' }},
        ]
    },
    # ── New task: deliver Ember's keepsake ─────────────────────────
    {
        'task_id': 'main_story_ch12_deliver_ember_keepsake_to_rell',
        'type': 'deliver',
        'item_id': 'embers_pressed_flower',
        'to_type': 'npc',
        'to_id': 'rell',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rell', 'dialog_id': 'rell_ch12_receives_keepsake' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rell', 'dialog_id': 'rell_ch12_farewell' }},
            { 'event_type': 'remove_item', 'params': { 'item_id': 'embers_pressed_flower' }},
            { 'event_type': 'advance_chapter' }
        ]
    },
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_12',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}