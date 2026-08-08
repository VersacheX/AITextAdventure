# ============================================================
# = CHAPTER 13 : GARBAGE
# ============================================================
#
# [ LOCATION - THE NECROPOLIS ]
# -----------------------------------
# @ = player
# M = Marlo Finch (tracker)
# C = Crypt Warden (gatekeeper)
# E = Echo Merchant (purveyor of truths)
# W = Veiled Widow (grieving soul)
# L, G = Lament & Garbage (Voidwalkers)
# S = Seth (returning pilot)
#
# High level: The party enters the Necropolis, a city of forgotten
# things, to confront Lament. They discover she has a symbiotic
# partner, Garbage, who embodies self-loathing. The party must
# navigate a series of interactions to gain access to the Grand
# Mausoleum, defeat both Voidwalkers, and are finally reunited
# with Seth and the newly repaired airship, the Rustwing.

ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
    {
        "npc_id": "garbage",
        "name": "Garbage",
        "description": "A Voidwalker that embodies self-loathing, fraudulence, and the feeling of worthlessness. It manifests as a rotting, many-mouthed shadow, whispering insecurities and lies to break its victims' spirits.",
        "theme_song": "Creep, Radiohead",
        "psychology": {
            "mbti": "ESTP",
            "dominant": "Se - Focuses on the immediate, tangible flaws and failures of its targets, exploiting them in the moment.",
            "auxiliary": "Ti - Uses a twisted, internal logic to deconstruct a person's self-worth, making its insults feel like objective truths.",
            "tertiary": "Fe - Has a keen, predatory sense of others' emotional vulnerabilities and social anxieties, which it uses to craft personalized psychological attacks.",
            "inferior": "Ni - Lacks any deeper vision or goal beyond the immediate act of tearing others down; it is pure, destructive impulse."
        },
        "enneagram": {
          "enneagram_type": "4w5",
          "core_fear": "Having no identity or significance.",
          "core_desire": "To have an identity, even if it is one of pure worthlessness.",
          "defense_mechanism": "Introjection — Has absorbed all feelings of self-loathing and failure, making it the entirety of its being.",
          "stress_line": "Moves to Type 2 — Lashes out, trying to make others feel as worthless as it does.",
          "growth_line": "Moves to Type 1 — Would learn to find inherent value and create a principled identity.",
          "instinctual_variant": "sp/sx — Utterly consumed by its own internal state of worthlessness, it only interacts with the world to pull it down into the rot."
        },
        'image': 'voidwalkers:garbage1.jpeg',
        'song_id': 'creep_radiohead'
    },
    {
        "npc_id": "crypt_warden",
        "name": "Crypt Warden",
        "description": "Once a person of status, now a hollowed-out shell who tends to the Necropolis. His identity has been frayed by the constant whispers of Lament and Garbage, leaving him a gatekeeper of sorrow.",
        "psychology": {
            "mbti": "ISFJ",
            "dominant": "Si - Clings to the details and duties of his role as warden, as it's the only concrete part of his identity that remains.",
            "auxiliary": "Fe - Is passively attuned to the overwhelming grief of the Necropolis, which has eroded his own emotional state.",
            "tertiary": "Ti - His logical functions are broken; he cannot distinguish between memory and the lies whispered by the Voidwalkers.",
            "inferior": "Ne - Is paralyzed by the possibility that there is no escape from his state, seeing only endless decay."
        },
        "enneagram": {
          "enneagram_type": "9w1",
          "core_fear": "Conflict, fragmentation, and the loss of his own identity.",
          "core_desire": "To have inner peace and stability.",
          "defense_mechanism": "Dissociation — Mentally withdraws from the overwhelming grief and horror of the Necropolis, going through the motions of his duty to survive.",
          "stress_line": "Moves to Type 6 — Becomes anxious and paranoid, unable to trust his own memories.",
          "growth_line": "Moves to Type 3 — Becomes more assertive and able to reclaim his identity.",
          "instinctual_variant": "sp/so — Seeks personal peace by retreating into his duties, while still being part of the Necropolis's grim social fabric."
        },
        "image": "npcs:crypt_warden1"
    },
    {
        "npc_id": "echo_merchant",
        "name": "Echo Merchant",
        "description": "A cynical merchant who sells fractured mirrors that reflect a person's true, often unbearable, self. He is a purveyor of the harsh truths that Garbage feeds on.",
        "psychology": {
            "mbti": "ISTP",
            "dominant": "Ti - Logically understands the transactional nature of truth and despair in the Necropolis and has built a business around it.",
            "auxiliary": "Se - Is grounded in the reality of his trade, observing how his 'products' affect people with detached curiosity.",
            "tertiary": "Ni - Has an underlying intuition that the entire system is corrupt but sees no alternative to participating in it.",
            "inferior": "Fe - Is uncomfortable with the emotional fallout of his mirrors, preferring to remain a neutral, transactional observer."
        },
        "enneagram": {
          "enneagram_type": "5w6",
          "core_fear": "Being overwhelmed by a system he can't control.",
          "core_desire": "To be competent and capable.",
          "defense_mechanism": "Isolation — Detaches from the moral and emotional consequences of his work, viewing it as a purely logical system of supply and demand.",
          "stress_line": "Moves to Type 7 — Becomes scattered and anxious when his business is threatened.",
          "growth_line": "Moves to Type 8 — Uses his understanding of the system to take confident action.",
          "instinctual_variant": "sp/so — Hoards his resources and knowledge for his own security, using his business to navigate the social landscape."
        },
        "image": "npcs:echo_merchant1"
    },
    {
        "npc_id": "veiled_widow",
        "name": "Veiled Widow",
        "description": "A woman trapped in a perpetual cycle of grief over a loss from the first Fracture. She is tormented daily by both Lament's sorrow and Garbage's whispers that she deserves the pain.",
        "psychology": {
            "mbti": "INFP",
            "dominant": "Fi - Her entire being is defined by her deep, internal feelings of loss and self-blame, which have become her core identity.",
            "auxiliary": "Ne - Is lost in a sea of painful possibilities and what-ifs related to her loss, unable to see a path forward.",
            "tertiary": "Si - Relives the memory of her loss with vivid, painful detail every day.",
            "inferior": "Te - Is completely unable to organize her life or take action, trapped by the overwhelming force of her emotions."
        },
        "enneagram": {
          "enneagram_type": "4w5",
          "core_fear": "Having no identity or significance outside of her grief.",
          "core_desire": "To find herself and her significance.",
          "defense_mechanism": "Introjection — Has absorbed her grief and loss, making it the core of her identity and the lens through which she sees the world.",
          "stress_line": "Moves to Type 2 — Becomes overly dependent on others when her grief becomes too much to bear alone.",
          "growth_line": "Moves to Type 1 — Finds a new, principled purpose beyond her personal grief.",
          "instinctual_variant": "sx/sp — Intensely focused on her personal loss and the one-on-one connection she had with the person she lost."
        },
        "image": "npcs:veiled_widow1"
    }
]

NPC_DIALOG = [
    {
        'npc_id': None,
        'dialog_id': 'ch13_narrator_intro',
        'dialog': [
            "Chapter 13 - The worst lie isn't what the world tells you... it's what you start telling yourself."
        ]
    },
    {
        'npc_id': 'marlo_finch',
        'dialog_id': 'marlo_finch_ch13_intro',
        'dialog': [
            "You came. Good. I tracked the Bracelet's resonance here. Lament and Garbage are feeding off each other.",
            "Grief creates self-loathing. Self-loathing deepens grief. It's a perfect cycle of decay."
        ]
    },
    {
        'npc_id': 'marlo_finch',
        'dialog_id': 'marlo_finch_ch13_instructs',
        'dialog': [
            "Keep the Bracelet of Existence. It's resisting their influence better than anything I've seen. Don't give it up."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch13_to_marlo',
        'dialog': [
            "Noted. Any idea where their center of power is?"
        ]
    },
    {
        'npc_id': 'marlo_finch',
        'dialog_id': 'marlo_finch_ch13_directs',
        'dialog': [
            "The Grand Mausoleum at the heart of the necropolis. That's where the worst of it festers.",
            "If you want to get in you should speak to the Crypt Warden. He's been... changed by his time there, but he knows the place better than anyone."
        ]
    },
    {
        'npc_id': 'crypt_warden',
        'dialog_id': 'crypt_warden_ch13_intro',
        'dialog': [
            "(voice hollow) Names... I used to remember names. Now they're all just... dust. Lament walks these halls. She collects our regrets like flowers."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch13_to_warden',
        'dialog': [
            "Sounds like a real charmer."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch13_to_warden',
        'dialog': [
            "The thrall is heavy here. Identities are fraying."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch13_narrator_lament_appears',
        'dialog': [
            "The air ripples. Lament appears in a swirl of black threads and weeping mist."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch13_to_warden',
        'dialog': [
            "(soft, sorrowful) Such devoted mourners. They carry their failures like crowns. Will you join them?",
            "Bring the Bracelet to the Grand Mausoleum. Let me show you what true emptiness feels like."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch13_narrator_lament_fades',
        'dialog': [
            "Lament fades. The Warden slumps further."
        ]
    },
    {
        'npc_id': 'crypt_warden',
        'dialog_id': 'crypt_warden_ch13_directs',
        'dialog': [
            "...She's always watching. Always whispering.",
            "If you want the key to The Grand Mausoleum, the Veiled Widow has it..",
            "but you will need to bring her the Voice of Lost Loved Ones from the Echo Merchant."
        ]
    },
    {
        'npc_id': 'echo_merchant',
        'dialog_id': 'echo_merchant_ch13_intro',
        'dialog': [
            "(holding up fractured mirrors) Want to see who you really are? Only a few coins.",
            "Most people break after one look. Garbage loves those ones."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch13_to_merchant',
        'dialog': [
            "We were actually told to see you. We need something called the Voice of Lost Loved Ones."
        ]
    },
    {
        'npc_id': 'echo_merchant',
        'dialog_id': 'echo_merchant_ch13_explains',
        'dialog': [
            "(nodding, voice low) Ah, the Voice. It's a special mirror. It doesn't just show you your reflection...",
            "it shows you the voices of those you've lost."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch13_to_merchant',
        'dialog': [
            "Oh that is so creepy. I love it."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch13_narrator_garbage_appears',
        'dialog': [
            "Garbage's presence manifests as a rotting, many-mouthed shadow behind the merchant."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch13_whispers',
        'dialog': [
            "(whispering from multiple directions) Look closer. You were always worthless. Always a fraud. Always alone."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch13_reacts_to_garbage',
        'dialog': [
            "(visibly shaken for a moment) ...Shut up."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch13_reacts_to_garbage',
        'dialog': [
            "(forced grin) Nice try, but I've got better insults for myself."
        ]
    },
    {
        'npc_id': 'echo_merchant',
        'dialog_id': 'echo_merchant_ch13_gives_item',
        'dialog': [
            "(voice trembling) See? Even they can't escape it. Here, take the Voice of Lost Loved Ones.",
            "I just hope the Veiled Widow gives you the key."
        ]
    },
    {
        'npc_id': 'veiled_widow',
        'dialog_id': 'veiled_widow_ch13_intro',
        'dialog': [
            "(voice cracking) I lost him in the first Fracture. Now I lose him every day... over and over.",
            "Lament says this pain is honest. Garbage says I deserve it."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch13_narrator_bosses_appear',
        'dialog': [
            "Both Lament and Garbage briefly manifest, their voices overlapping."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch13_to_widow',
        'dialog': [
            "Grief is the only truth left."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch13_to_widow',
        'dialog': [
            "And you are the rot that remains."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch13_to_bosses',
        'dialog': [
            "Enough. We will not let you consume them."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch13_taunt',
        'dialog': [
            "Look at the little saint, trying to heal a wound that wants to fester. You can't fix what is fundamentally broken."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch13_to_garbage',
        'dialog': [
            "I can fix your face with my fist. Keep talking."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch13_to_garbage',
        'dialog': [
            "Your entire existence is a parasitic feedback loop. Predictable. And boring."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch13_taunt',
        'dialog': [
            "Your defiance is a fleeting spark. It will be swallowed by the sorrow you refuse to acknowledge."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch13_final_taunt',
        'dialog': [
            "You think you're heroes? You're just garbage that hasn't been thrown away yet."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch13_invitation',
        'dialog': [
            "Come to the Mausoleum. We will show you the beauty in the end."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch13_narrator_bosses_fade',
        'dialog': [
            "Garbage and Lament fade, leaving the Widow trembling."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch13_gives_item',
        'dialog': [
            "(gently holding out the mirror) We brought you this. A way to remember his voice, not just the loss."
        ]
    },
    {
        'npc_id': 'veiled_widow',
        'dialog_id': 'veiled_widow_ch13_gives_key',
        'dialog': [
            "(taking the mirror, her hands shaking as a faint, warm voice emanates from it) That voice...",
            "I haven't heard it clearly in so long. They want me to drown in my grief, but this...",
            "this is a memory worth holding. Thank you. Take this key. End their reign of sorrow."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_ch13_observes_widow',
        'dialog': [
            "Her grief is a tide, but even tides can be calmed. She needed an anchor, not an endless storm."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch13_boss_intro',
        'dialog': [
            "(voice soft yet crushing, echoing from every tomb) You carry her song still... Ember's final note. How noble. How utterly futile."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch13_boss_intro',
        'dialog': [
            "(multiple rotting mouths speaking at once) And yet you still pretend you matter. Pretend *any* of this matters. How deliciously pathetic."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch13_boss_response',
        'dialog': [
            "(gripping his weapon) We've heard enough of your bullshit. Time to end this."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch13_boss_response',
        'dialog': [
            "(grinning fiercely) Two for the price of one? My favorite kind of bad decision."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch13_boss_response',
        'dialog': [
            "(voice steady but pained) For Ember. For every person you've broken with false joy and endless grief."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch13_boss_response',
        'dialog': [
            "(growling) You feed on pain like parasites. We're done being your meal."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch13_boss_response',
        'dialog': [
            "(winds swirling around her) The storm ends here. No more feeding on broken hearts."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_ch13_boss_response',
        'dialog': [
            "(hammer crackling with energy) You've had your fun tearing people down. My turn."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch13_boss_taunt',
        'dialog': [
            "(tilting her head, almost sorrowful) You fight so hard to feel meaningful. But meaning is the first illusion we strip away."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch13_boss_taunt',
        'dialog': [
            "(laughing with wet, crumbling voices) Look at you - heroes carrying a shiny bracelet like it can save you.",
            "You're all just future garbage waiting to be thrown away."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch13_boss_response',
        'dialog': [
            "(quietly, deadly calm) Words won't save you this time."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch13_boss_response',
        'dialog': [
            "(cold smirk) Your cycle is predictable. Grief breeds self-loathing. Self-loathing deepens grief. Elegant. But fragile."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch13_final_words',
        'dialog': [
            "(voice rising into a wail) Then come. Let us show you the beauty in surrender."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch13_final_words',
        'dialog': [
            "(bodies shifting and reforming) Break them. Make them see what they truly are."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch13_narrator_after_boss',
        'dialog': [
            "The Grand Mausoleum trembles violently.",
            "Cracks of light pierce the oppressive darkness as the symbiotic cycle between grief and self-loathing finally shatters.",
            "The air grows lighter. The constant whispering of failure and loss begins to fade."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch13_after_boss',
        'dialog': [
            "(breathing hard, looking at the fading remnants) It's done... The weight is lifting."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch13_after_boss',
        'dialog': [
            "(wiping sweat and blood) About damn time. Felt like fighting two sides of the same miserable coin."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch13_after_boss',
        'dialog': [
            "(laughing breathlessly) They really hated that we refused to hate ourselves. Sensitive types."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch13_after_boss',
        'dialog': [
            "(sheathing her weapons) Their power fed on each other. Break one pillar, the whole structure collapses."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch13_after_boss',
        'dialog': [
            "(scanning the area) The Bracelet held strong. It resisted their corruption better than anything else we've seen."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch13_after_boss',
        'dialog': [
            "(quietly) Ember would be proud. She fought the same fight - refusing to let despair or false joy win."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch13_after_boss',
        'dialog': [
            "(grunting) One less shadow on the world. Good."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_ch13_after_boss',
        'dialog': [
            "(softly) The tide of grief recedes... for now."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_ch13_after_boss',
        'dialog': [
            "(adjusting his goggles) Identities are stabilizing. People might remember who they were before the rot set in."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch13_narrator_rustwing_returns',
        'dialog': [
            "In the distance, the familiar roar of engines echoes across the necropolis.",
            "The Rustwing descends, patched and battle-worn but flying true."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch13_returns',
        'dialog': [
            "OI! You lot look like death warmed over!"
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch13_to_seth',
        'dialog': [
            "SETH!"
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch13_banter_1',
        'dialog': [
            "The one and only. Missed me?"
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch13_to_seth',
        'dialog': [
            "How did you fix the ship?"
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch13_banter_2',
        'dialog': [
            "Blood, sweat, and a lot of stolen parts. She's not pretty, but she flies."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch13_to_seth',
        'dialog': [
            "You came back."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch13_banter_3',
        'dialog': [
            "Course I did. Someone's gotta keep you idiots alive."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch13_to_seth',
        'dialog': [
            "We thought you'd abandoned us."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch13_banter_4',
        'dialog': [
            "Nah. Just had to make sure the ship could actually carry your sorry arses. Look. I know things are rough.",
            "The world's falling apart. You're falling apart. So here's the deal. The ship's yours."
        ]
    },
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_ch13_to_seth',
        'dialog': [
            "What?"
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch13_gives_ship',
        'dialog': [
            "You heard me. The Rustwing. She's yours now. I'm tired of flying her anyway. Too much responsibility."
        ]
    },
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_ch13_to_seth',
        'dialog': [
            "You're... giving us the airship?"
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch13_clarifies',
        'dialog': [
            "On loan. With interest. Emotional interest. You've got work to do. The world's not gonna save itself.",
            "And I figure... if anyone's gonna stop this collapse, it's you."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch13_to_seth_gift',
        'dialog': [
            "That's surprisingly touching."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch13_final_words',
        'dialog': [
            "Don't get used to it. Now get in before I change my mind."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'ch13_narrator_new_freedom',
        'dialog': [
            "The Rustwing hums with possibility. Freedom. Choice."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch13_new_freedom',
        'dialog': [
            "We can go anywhere."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch13_new_freedom',
        'dialog': [
            "That's... that's terrifying."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch13_new_freedom',
        'dialog': [
            "And liberating."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch13_new_freedom',
        'dialog': [
            "So where to?"
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch13_departs',
        'dialog': [
            "Anywhere but here. Trust me. The world's wide open. Find meaning. Find purpose. Find whatever keeps you going."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch13_what_about_you',
        'dialog': [
            "What about you?"
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch13_farewell',
        'dialog': [
            "Me? I'm gonna find a bar and pretend the world isn't ending. Don't crash her! She's temperamental!"
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch13_act_end',
        'dialog': [
            "The body has fallen. Sensation. Impulse. Identity."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch13_act_end',
        'dialog': [
            "With this airship we can really expand our reach and find out what the fuck is going on here and maybe find a way home."
        ]
    }
]

TASKS = [
    {
        'task_id': 'main_story_ch13_meet_marlo_finch',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'marlo_finch',
        'task_acquire_events': [
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'marlo_finch', 'location': 'region_city_shoparmor' }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'garbage', 'location': None }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'crypt_warden', 'location': 'region_city_inn' }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'echo_merchant', 'location': 'region_city_shopitems' }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'veiled_widow', 'location': 'region_city_bar' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'seth', 'location': 'region_city_bar' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'garbage', 'standing_text': ["I am the rot that festers in your soul."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'seth', 'standing_text': ["The Necropolis is a graveyard of forgotten things. It's where the city buries its secrets and its failures."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'crypt_warden', 'standing_text': ["I used to be someone. Now I'm just... a shadow in the Necropolis."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'echo_merchant', 'standing_text': ["I sell mirrors that show you your true self. Most people can't handle the truth."]}},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'veiled_widow', 'standing_text': ["I lost someone in the first Fracture. Now I lose them every day... over and over."]}},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch13_narrator_intro' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch13_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch13_instructs' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch13_to_marlo' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch13_directs' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'marlo_finch', 'standing_text': ["The Grand Mausoleum is their sanctum. Be careful."]}},
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'grand_mausoleum', 'location': 'region_city_district' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'grand_mausoleum', 'item_id': 'swamp_small_city_e_gnashwater_memory_vessel', 'location': 'treasure_room' }},
            { 'event_type': 'lock_dungeon', 'params': { 'dungeon_id': 'grand_mausoleum' }},
            { 'event_type': 'set_dungeon_locked_text', 'params': { 'dungeon_id': 'grand_mausoleum', 'locked_text': "The Grand Mausoleum is locked tight. You'll need to find a way in."}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch13_meet_crypt_warden' }}
        ]
    },
    {
        'task_id': 'main_story_ch13_meet_crypt_warden',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'crypt_warden',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crypt_warden', 'dialog_id': 'crypt_warden_ch13_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch13_to_warden' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch13_to_warden' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch13_narrator_lament_appears' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch13_to_warden' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch13_narrator_lament_fades' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crypt_warden', 'dialog_id': 'crypt_warden_ch13_directs' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'crypt_warden', 'standing_text': ["The Grand Mausoleum... that's where they wait."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch13_meet_echo_merchant' }}
        ]
    },
    {
        'task_id': 'main_story_ch13_meet_echo_merchant',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'echo_merchant',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'echo_merchant', 'dialog_id': 'echo_merchant_ch13_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch13_to_merchant' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'echo_merchant', 'dialog_id': 'echo_merchant_ch13_explains' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch13_to_merchant' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch13_narrator_garbage_appears' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch13_whispers' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch13_reacts_to_garbage' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch13_reacts_to_garbage' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'echo_merchant', 'dialog_id': 'echo_merchant_ch13_gives_item' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'echo_merchant', 'standing_text': ["The mirrors don't lie... but they do break people."]}},
            { 'event_type': 'award_item', 'params': { 'item_id': 'voice_of_lost_loved_ones' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch13_meet_veiled_widow' }}
        ]
    },
    {
        'task_id': 'main_story_ch13_meet_veiled_widow',
        'type': 'deliver',
        'to_type': 'npc',
        'to_id': 'veiled_widow',
        'item_id': 'voice_of_lost_loved_ones',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'veiled_widow', 'dialog_id': 'veiled_widow_ch13_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch13_narrator_bosses_appear' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch13_to_widow' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch13_to_widow' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch13_to_bosses' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch13_taunt' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch13_to_garbage' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch13_to_garbage' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch13_taunt' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch13_final_taunt' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch13_invitation' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch13_narrator_bosses_fade' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch13_gives_item' }},
            { 'event_type': 'remove_item', 'params': { 'item_id': 'voice_of_lost_loved_ones' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'veiled_widow', 'dialog_id': 'veiled_widow_ch13_gives_key' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_ch13_observes_widow' }},
            { 'event_type': 'award_item', 'params': { 'item_id': 'key_to_grand_mausoleum' }},
            { 'event_type': 'unlock_dungeon', 'params': { 'dungeon_id': 'grand_mausoleum' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'veiled_widow', 'standing_text': ["The Grand Mausoleum... that's where they make their home."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch13_meet_lament_with_garbage' }}
        ]
    },
    {
        'task_id': 'main_story_ch13_meet_lament_with_garbage',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lament',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch13_boss_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch13_boss_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch13_boss_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch13_boss_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch13_boss_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch13_boss_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch13_boss_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_ch13_boss_response' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch13_boss_taunt' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch13_boss_taunt' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch13_boss_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch13_boss_response' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch13_final_words' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch13_final_words' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lament', 'standing_text': ["The Grand Mausoleum is their sanctum. Be careful."]}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch13_defeat_lament_and_garbage' }}
        ]
    },
    {
        'task_id': 'main_story_ch13_defeat_lament_and_garbage',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'lament_garbage_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'lament_garbage_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'lament' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch13_narrator_after_boss' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch13_after_boss' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch13_after_boss' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch13_after_boss' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch13_after_boss' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch13_after_boss' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch13_after_boss' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch13_after_boss' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_ch13_after_boss' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch13_after_boss' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch13_narrator_rustwing_returns' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch13_meet_seth_about_airship' }}
        ]
    },
    {
        'task_id': 'main_story_ch13_meet_seth_about_airship',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'seth',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch13_returns' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch13_to_seth' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch13_banter_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch13_to_seth' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch13_banter_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch13_to_seth' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch13_banter_3' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch13_to_seth' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch13_banter_4' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'tess', 'dialog_id': 'tess_ch13_to_seth' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch13_gives_ship' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'sam', 'dialog_id': 'sam_ch13_to_seth' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch13_clarifies' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch13_to_seth_gift' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch13_final_words' }},
            { 'event_type': 'set_aircraft', 'params': { 'location': 'region_city_open_area' }},
            { 'event_type': 'can_aircraft_fly', 'params': { 'can_fly': True }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch13_narrator_new_freedom' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch13_new_freedom' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch13_new_freedom' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch13_new_freedom' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch13_new_freedom' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch13_departs' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch13_what_about_you' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch13_farewell' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch13_act_end' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch13_act_end' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'seth', 'standing_text': ["The Rustwing is yours now. Use it wisely."]}},
            { 'event_type': 'advance_chapter' }
        ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_13',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
  'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}