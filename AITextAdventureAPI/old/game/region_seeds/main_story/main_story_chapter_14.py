# ============================================================
# = CHAPTER 14: STIGMA
# ============================================================
#
# LOCATION — A city divided by choice: Memory vs. Reputation.
# -----------------------------------
# @ = player
# T = Tess, S = Sam, R = Ravel, H = Hask, C = Caius, J = Jett, E = Elian
#
# High level: The party arrives in a city where citizens must choose
# between two opposing identities. They meet Stigma, a charismatic
# leader offering a third way, only to discover her solution is
# another form of control.

ATTAINABLE_PLAYER_CHARACTERS = []

NPCS = [
    {
        'npc_id': 'ravel',
        'name': 'Ravel',
        'description': (
            "A citizen of Stigma's city who refuses to wear the masks of Memory or Reputation. "
            "They are overwhelmed with shame but determined to destroy their mask to free others."
        ),
        "psychology": {
            "mbti": "INFP",
            "dominant": "Fi - Driven by a powerful internal conviction to be authentic, even when it is dangerous.",
            "auxiliary": "Ne - Sees the possibility of a world without forced personas and acts to create it.",
            "tertiary": "Si - Remembers the pain of wearing the mask, which fuels their desire to destroy it.",
            "inferior": "Te - Struggles to organize their rebellion, relying on the party to take direct action."
        },
        "enneagram": {
          "enneagram_type": "4w5",
          "core_fear": "Having no identity or personal significance; being forced into a false persona.",
          "core_desire": "To find and express her true, authentic self.",
          "defense_mechanism": "Introjection — Defines herself in opposition to the city's false dichotomy, making her rebellion her identity.",
          "stress_line": "Moves to Type 2 — Becomes overly dependent on the party to help her when she feels overwhelmed.",
          "growth_line": "Moves to Type 1 — Becomes a principled and effective leader of the resistance.",
          "instinctual_variant": "sx/so — Intensely focused on her personal quest for authenticity, which has major social implications."
        }
    },
    {
        'npc_id': 'hask',
        'name': 'Hask',
        'description': (
            "An enforcer of appearances in Stigma's city. He is obsessed with maintaining order "
            "by ensuring everyone looks and acts 'right'."
        ),
        "psychology": {
            "mbti": "ESTJ",
            "dominant": "Te - Focused on external order and enforcement. He is direct, commanding, and rule-oriented.",
            "auxiliary": "Si - Relies on the established rules of appearance and behavior to maintain control.",
            "tertiary": "Ne - Sees any deviation from the norm as a potential threat to order.",
            "inferior": "Fi - His personal values are completely subsumed by his role as an enforcer; he has no identity outside of it."
        },
        "enneagram": {
          "enneagram_type": "1w2",
          "core_fear": "The world being wrong, chaotic, or imperfect.",
          "core_desire": "To have order and be right.",
          "defense_mechanism": "Reaction Formation — Channels his fear of chaos into a rigid, angry enforcement of 'purity' and 'unity'.",
          "stress_line": "Moves to Type 4 — Becomes withdrawn and resentful when his authority is challenged.",
          "growth_line": "Moves to Type 7 — Would learn to be more flexible and less judgmental.",
          "instinctual_variant": "so/sp — Focused on enforcing social conformity to maintain order and his own sense of security."
        }
    },
    {
        'npc_id': 'caius',
        'name': 'Caius',
        'description': (
            "An authoritarian figure in the city of Pageant and Edict. They enforce the rules of performance and compliance, viewing order as paramount."
        ),
        "psychology": {
            "mbti": "ESTJ",
            "dominant": "Te - Manages the city's system of performance with cold efficiency, issuing directives and consequences.",
            "auxiliary": "Si - Adheres strictly to the established rules of compliance, performance, and removal.",
            "tertiary": "Ne - Explores new ways to monitor and measure performance to ensure total order.",
            "inferior": "Fi - Believes so strongly in the system that they see no moral issue with 'removing' failures."
        },
        "enneagram": {
          "enneagram_type": "1w9",
          "core_fear": "Disorder, chaos, and imperfection.",
          "core_desire": "To have a perfect, ordered system.",
          "defense_mechanism": "Reaction Formation — Believes his rigid enforcement is a righteous act of maintaining order, denying its cruelty.",
          "stress_line": "Moves to Type 4 — Becomes melancholic and withdrawn when the system is threatened.",
          "growth_line": "Moves to Type 7 — Would learn to be more flexible and humane.",
          "instinctual_variant": "so/sp — Obsessed with maintaining social order through rigid rules to ensure his own sense of rightness and security."
        }
    },
    {
        'npc_id': 'jett',
        'name': 'Jett',
        'description': (
            "The leader of a group of survivors who live in the Heap of Broken Futures. They are cynical but resilient, salvaging what and who the city throws away."
        ),
        "psychology": {
            "mbti": "ISTP",
            "dominant": "Ti - Has a practical, logical understanding of the system and how to survive its flaws.",
            "auxiliary": "Se - Is resourceful and acts based on the immediate needs of survival in a harsh environment.",
            "tertiary": "Ni - Has an intuitive grasp of the Heap and the path to the city's core.",
            "inferior": "Fe - Is detached and cynical, but shows a gruff concern for their fellow scrappers."
        },
        "enneagram": {
          "enneagram_type": "8w9",
          "core_fear": "Being controlled or harmed by the city's system.",
          "core_desire": "To be in control of his own life and protect his community.",
          "defense_mechanism": "Denial — Uses cynicism and a tough exterior to deny his vulnerability and the harshness of his reality.",
          "stress_line": "Moves to Type 5 — Becomes secretive and withdrawn, hoarding resources when his community is threatened.",
          "growth_line": "Moves to Type 2 — Openly uses his strength to protect and provide for his people.",
          "instinctual_variant": "sp/so — Focused on his own and his community's survival, creating a safe space outside the main system."
        }
    },
    {
        'npc_id': 'elian',
        'name': 'The Last Poet',
        'description': (
            "A writer living in fear in the city of Pageant and Edict. Their work is monitored, and they are one non-compliant poem away from being 'removed'."
        ),
        "psychology": {
            "mbti": "INFP",
            "dominant": "Fi - Driven by the need for authentic self-expression, even when it is dangerous.",
            "auxiliary": "Ne - Sees the oppressive nature of the system and the hope of a world without it.",
            "tertiary": "Si - Remembers a time when they could write freely, which fuels their quiet defiance.",
            "inferior": "Te - Is powerless to act directly against the system, relying on their art as their only form of resistance."
        },
        "enneagram": {
          "enneagram_type": "4w5",
          "core_fear": "Having no identity or significance; being silenced.",
          "core_desire": "To find and express his unique, authentic self.",
          "defense_mechanism": "Introjection — Defines himself through his art and his quiet rebellion, creating a meaningful identity in an oppressive world.",
          "stress_line": "Moves to Type 2 — Becomes overly dependent on others to act for him.",
          "growth_line": "Moves to Type 1 — Becomes a principled and vocal leader of the resistance.",
          "instinctual_variant": "sx/sp — Intensely focused on his personal, authentic expression, which he protects by staying withdrawn."
        }
    },
    {
        'npc_id': 'stigma',
        'name': 'Stigma',
        'description': (
            "A seductive void-siren whose presence rewrites desire, identity, and will."
        ),
        "psychology": {
            "mbti": "ENFJ-shadow",
            "dominant": "Fe - Weaponized intimacy; puppeteers emotion until the self dissolves.",
            "auxiliary": "Ni - Predicts vulnerabilities with predatory clarity; every seduction is destiny.",
            "tertiary": "Se - Sensory overload as control; overwhelms perception to bypass resistance.",
            "inferior": "Ti - Logic twisted into justification; rationalizes domination as salvation."
        },
        "enneagram": {
          "enneagram_type": "2w3",
          "core_fear": "Being unwanted or unworthy of love/adoration.",
          "core_desire": "To be loved and needed (by consuming others' identities).",
          "defense_mechanism": "Repression — Denies her own emptiness by focusing on 'healing' and 'saving' others, making them dependent on her.",
          "stress_line": "Moves to Type 8 — Becomes aggressive and controlling when her 'love' is rejected.",
          "growth_line": "Moves to Type 4 — (Hypothetically) Would learn to find her own identity without needing to absorb others.",
          "instinctual_variant": "sx/so — Forms intense, consuming one-on-one bonds to create a loyal social collective that worships her."
        }
    }
]

NPC_DIALOG = [
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch14_intro',
        'dialog': [
            "Chapter 14 - You are judged for what you were... and punished for not becoming what you’re supposed to be."
        ]
    },
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_ch14_intro',
        'dialog': [
            "Look at this. A whole city built on a binary choice. Memory or Reputation.",
            "It's the oldest con in the book - limit the options to control the outcome."
        ]
    },
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_ch14_intro',
        'dialog': [
            "The system is designed to enforce self-policing. They're not just choosing a mask; they're choosing a cage.",
            "The real power isn't in the masks, but in the act of choosing one."
        ]
    },
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_ch14_performance',
        'dialog': [
            "Exactly! And everyone's so committed to the performance. I wonder who's selling the tickets to this show."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch14_trapped',
        'dialog': [
            "You see this as a performance? These people seem trapped."
        ]
    },
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_ch14_best_traps',
        'dialog': [
            "Of course it's a performance! The best traps always are. They make you think you're choosing your own identity, but the house always wins."
        ]
    },
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_ch14_ravel_opportunity',
        'dialog': [
            "The woman over there—Ravel. She's the only variable not accounted for in the system. She's not playing.",
            "That makes her either a threat or an opportunity. We should start with her."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch14_poke_system',
        'dialog': [
            "(Grinning) Finally, someone speaking my language. Let's go poke the system."
        ]
    },
    {
        'npc_id': 'ravel',
        'dialog_id': 'ravel_ch14_intro',
        'dialog': [
            "...You're not from here. Your eyes aren't split down the middle.",
            "This city wants you to choose - Red for Memory, Blue for Reputation. Both are prisons."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch14_breaks_something',
        'dialog': [
            "(gently) Forcing people to pick a side like this… it breaks something inside them."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch14_false_dichotomy',
        'dialog': [
            "(grinning) Classic false dichotomy. Create two bad options, make everyone fight over which cage feels better."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch14_social_control',
        'dialog': [
            "(arms crossed) And the ones who refuse to choose become the enemy. Efficient social control."
        ]
    },
    {
        'npc_id': 'ravel',
        'dialog_id': 'ravel_ch14_hate_me',
        'dialog': [
            "(A flicker of respect in her eyes) You see it. Most don't. They're too afraid of being left out.",
            "I tried wearing both masks. Nearly lost myself. Now I wear nothing... and they hate me for it."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch14_stand_whole',
        'dialog': [
            "It takes strength to stand whole when the world demands you fracture."
        ]
    },
    {
        'npc_id': 'lyren_vale',
        'dialog_id': 'lyren_ch14_broken_version',
        'dialog': [
            "(softly) Everything broken still carries pieces of what it was meant to be… You don’t have to choose their broken version of you."
        ]
    },
    {
        'npc_id': 'ravel',
        'dialog_id': 'ravel_ch14_hask_stigma',
        'dialog': [
            "(Looking toward the armor shop) Hask, the enforcer, watches me. He calls me an error.",
            "He says a new leader is coming to 'cleanse' the city. Stigma."
        ]
    },
    {
        'npc_id': 'tess',
        'dialog_id': 'tess_ch14_beautiful_grift',
        'dialog': [
            '(A sharp, dangerous grin) "Cleanse." That\'s a fun word for a hostile takeover.',
            "So, Stigma creates the problem, lets it fester, and then rides in as the savior. It's a beautiful grift. I almost respect it."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch14_predator_skin',
        'dialog': [
            "(low growl) Sounds like another predator wearing a savior’s skin."
        ]
    },
    {
        'npc_id': 'hask',
        'dialog_id': 'hask_ch14_intro',
        'dialog': [
            "You've been speaking with the dissenter, Ravel.",
            "I saw you. Her refusal to choose is a crack in the foundation of this city."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch14_put_together',
        'dialog': [
            "She seemed more put-together than anyone else we've met here."
        ]
    },
    {
        'npc_id': 'hask',
        'dialog_id': 'hask_ch14_error_cleansed',
        'dialog': [
            "She is an error. And errors must be corrected.",
            "True unity requires a single, authentic self - nothing less.",
            "No messy contradictions. No defiance.",
            "A new leader is coming. Someone who understands that real order demands purity.",
            "She will cleanse this city of its pathetic division."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch14_tyranny',
        'dialog': [
            "(calm but firm) Forcing people into one shape is not unity. It is tyranny wearing a mask of order."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch14_dust',
        'dialog': [
            "(quiet, dangerous calm) A blade that cuts away everything that doesn't fit eventually leaves nothing but dust."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch14_terrified_of_real',
        'dialog': [
            "(smirking) Funny. The more you talk about \"purity,\" the more you sound like you're terrified of anything real."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch14_brittle',
        'dialog': [
            "Your system is fragile. One unapproved thought and it all collapses. That's not strength. That's brittle."
        ]
    },
    {
        'npc_id': 'lyren_vale',
        'dialog_id': 'lyren_ch14_fractures_deeper',
        'dialog': [
            "(soft but resolute) Broken things can still be beautiful. Forcing them to be \"perfect\" only makes the fractures deeper."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch14_earning_it',
        'dialog': [
            "(stepping forward, cracking his knuckles) You want unity? Try earning it instead of demanding it at gunpoint."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch14_intro',
        'dialog': [
            "(stepping forward with a warm, radiant smile that somehow feels both kind and dangerous)",
            "Hask speaks the truth, though he lacks poetry.",
            "You've sought out the cracks in this city. Good. It shows you're looking for something real.",
            "(gesturing gracefully to the divided streets outside)",
            "Most people who arrive here quickly pick a color - red or blue - and disappear into it.",
            "But you... you resist. You question. You intrigue me."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch14_who_are_you',
        'dialog': [
            "(wary but polite) Who are you?"
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch14_family',
        'dialog': [
            "(soft laugh, eyes sparkling) I am Stigma. And I am building something better than this fractured place.",
            "A family. A home. One not bound by the cages of memory or the performance of reputation."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch14_cult_leader',
        'dialog': [
            "(grinning) A cult leader with style. I’m listening."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch14_how_exactly',
        'dialog': [
            "(arms crossed, skeptical) A noble goal. But how exactly do you plan to build this \"family\"?"
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch14_tidekin_cove',
        'dialog': [
            "(leaning in slightly, voice warm and intimate) By showing people there are worse prisons than the ones they already know.",
            "The city of Tidekin Cove, to the south, is a monument to false performance - ruled by a tyrant named Edict who demands perfect compliance.",
            "Go there. See it with your own eyes. Breathe their air. Then return to me, and you will be ready to understand what I’m truly offering."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch14_prove_a_point',
        'dialog': [
            "You want us to fly to another city just to prove a point?"
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch14_the_abyss',
        'dialog': [
            "(smiling gently) I want you to prove you’re not afraid to look into the abyss. Caius at the inn there will be waiting for you.",
            "Find him. Observe. Then come back to me.",
            "(her smile deepens with quiet intensity) I think you’ll like what you see... or rather, what you finally stop pretending not to see."
        ]
    },
    {
        'npc_id': 'caius',
        'dialog_id': 'caius_ch14_intro',
        'dialog': [
            "You're the ones she sent. Stigma's new favorites.",
            "I can see it in your eyes... that hopeful little spark she gives everyone.",
            "You've seen this place. You've breathed the air. That's all she wanted.",
            "Now go back. Tell her what you saw. Tell her the system is perfect."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch14_nightmare',
        'dialog': [
            "Perfect? This place is a high-strung nightmare. Everyone's smiling like their face is stapled in place."
        ]
    },
    {
        'npc_id': 'caius',
        'dialog_id': 'caius_ch14_stigma_worse',
        'dialog': [
            "(leaning in closer, whispering urgently) Exactly. And Stigma wants to \"fix\" it by burning it all down and replacing it with her own version.",
            "Edict is cold, controlling, and obsessed with order... but at least his rules are clear.",
            "Stigma? She gets inside your head. She makes you believe you're broken unless you belong to her 'family.' She's not saving anyone. She's collecting them."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch14_no_better',
        'dialog': [
            "(frowning) You're saying she's no better than Edict?"
        ]
    },
    {
        'npc_id': 'caius',
        'dialog_id': 'caius_ch14_demands_soul',
        'dialog': [
            "(shaking his head) She's worse. Edict demands performance. Stigma demands your soul.",
            "She'll smile while she rewrites who you are. I've seen what happens to people who fully drink her poison... they stop being people."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch14_played',
        'dialog': [
            "(coldly) So we've been played."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch14_manipulator',
        'dialog': [
            "(grunting) Great. Another manipulator pretending to be the solution."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch14_burn_both',
        'dialog': [
            "Then the real question is, which poison do we choose... or do we burn both?"
        ]
    },
    {
        'npc_id': 'caius',
        'dialog_id': 'caius_ch14_get_out',
        'dialog': [
            "(whispering) Just get out while you still can. Tell her whatever she wants to hear.",
            "Before Edict realizes you're here... and before Stigma decides you're too useful to let go."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch14_return',
        'dialog': [
            "(eyes lighting up) You’re back. And you have the stink of Edict’s city on you. Good. Tell me what did you see?",
            "The forced smiles? The hollow performances? That is the enemy. Not just Edict, but the very idea of him."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch14_another_manipulator',
        'dialog': [
            "(voice heavy) We saw fear wearing a mask of perfection. But we also saw something else."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch14_another_manipulator',
        'dialog': [
            "(cold, direct) We saw another manipulator. One who smiles while she rewrites people from the inside."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch14_control',
        'dialog': [
            "(no longer grinning) You talk about freedom and family, but everything you do is about control. You just hide it better than he does."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch14_belonging',
        'dialog': [
            "Control? I offer belonging. I offer healing.",
            "I offer a place where you don’t have to choose between painful memory and empty performance.",
            "You felt it in Tidekin Cove, didn’t you? The suffocating weight of expectation. I can free you from all of that."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch14_choose_you',
        'dialog': [
            "By making us choose *you* instead? By turning us into another one of your perfect little masks?"
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch14_predation',
        'dialog': [
            "You prey on people’s fear of being incomplete. That’s not salvation. That’s predation."
        ]
    },
    {
        'npc_id': 'lyren_vale',
        'dialog_id': 'lyren_ch14_erase_parts',
        'dialog': [
            "You speak of family... but families don’t demand you erase parts of yourself to belong."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch14_venom',
        'dialog': [
            "(her warm smile finally cracks, revealing something colder underneath)",
            "So that’s how it is.",
            "Even after everything... you still cling to your broken little selves.",
            "(voice shifting, now laced with venom)",
            "Then I was wrong about you. You’re not ready to be saved.",
            "You’re just more garbage waiting to be thrown away."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch14_done_with_tools',
        'dialog': [
            "We’re done being your tools."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch14_end_this',
        'dialog': [
            "Time to end this."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch14_stigma_defeat',
        'dialog': [
            "Stigma’s form flickers and shatters under the final blow. The warm, magnetic aura she projected collapses into something cold and hollow.",
            "For a moment, her true face is visible — desperate, furious, and deeply afraid.",
            "Then her body fractures like glass, dissolving into threads of pink and violet light that scatter into the wind."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch14_defeat',
        'dialog': [
            "(gasping, voice breaking) You... fools... I was trying to save you from becoming nothing...",
            "(laughing bitterly as her form unravels) Fine. Run back to Edict and his cold little kingdom of rules. See how long that lasts.",
            "(voice fading into an echo) You’ll come crawling back... when the masks start to feel comfortable again..."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch14_aftermath',
        'dialog': [
            "The last traces of Stigma’s presence vanish. The air feels suddenly heavier, as if a false warmth has been stripped away, leaving only raw truth behind."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch14_stigma_aftermath',
        'dialog': [
            "She wasn’t saving anyone. She was collecting broken people... and making them more broken. Turning their pain into chains she could hold.",
            "I wanted to believe someone could offer real belonging in all this chaos... but not like that."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch14_stigma_aftermath',
        'dialog': [
            "Cult leaders are always the same. They just dress it up nicer. “Join my family.” “Let me fix you.” Same poison, prettier bottle.",
            "At least now we know what she really was — a pretty parasite."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch14_stigma_aftermath',
        'dialog': [
            "We’ve been played from the start. She created the division, then positioned herself as the only solution. Classic controlled opposition.",
            "Edict might be a tyrant, but at least his control is honest. Stigma wanted to own who we are."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch14_stigma_aftermath',
        'dialog': [
            "(cracking his knuckles, voice low and angry) Talking about unity while trying to erase everything that makes someone themselves...",
            "Yeah. I’ve had enough of her “family.”",
            "Time to find the bastard in the Citadel. Let’s see if he’s any better."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch14_stigma_aftermath',
        'dialog': [
            "(quiet, steady) She fed on fear of being incomplete. That kind of hunger doesn’t die easily.",
            "Even if she escaped, her ideas may still linger here."
        ]
    },
    {
        'npc_id': 'lyren_vale',
        'dialog_id': 'lyren_ch14_stigma_aftermath',
        'dialog': [
            "Everything she touched still carries the echo of what it was meant to be... but she tried to silence those echoes. That’s the real crime.",
            "We carry real connection. Not the version she wanted to force on us."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch14_stigma_aftermath',
        'dialog': [
            "(low growl) Another predator wearing a savior’s skin. Good riddance."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch14_stigma_aftermath',
        'dialog': [
            "(voice tight) She made belonging feel like safety... but it was just another cage with better lighting."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch14_face_edict',
        'dialog': [
            "We’ve seen both sides of this sickness. Time to face the one still sitting on the throne."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch14_face_edict',
        'dialog': [
            "Edict’s next. Let’s end this properly."
        ]
    }
]

TASKS = [
    {
        'task_id': 'main_story_ch14_meet_tess',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'tess',
        'task_acquire_events': [
            {'event_type': 'create_npc', 'params': {'npc_id': 'ravel', 'location': 'region_city_bar'}},
            {'event_type': 'create_npc', 'params': {'npc_id': 'hask', 'location': 'region_city_shoparmor'}},
            {'event_type': 'show_npc', 'params': {'npc_id': 'tess', 'location': 'region_city_bar'}},
            {'event_type': 'show_npc', 'params': {'npc_id': 'sam', 'location': 'region_city_bar'}},
            {'event_type': 'create_npc', 'params': {'npc_id': 'caius', 'location': 'city_number_15_region_city_inn'}},
            {'event_type': 'create_npc', 'params': {'npc_id': 'jett', 'location': 'city_number_15_region_city_shopitems'}},
            {'event_type': 'create_npc', 'params': {'npc_id': 'elian', 'location': 'city_number_15_region_city_bar'}},
            {'event_type': 'create_dungeon', 'params': {'dungeon_id': 'the_citadel', 'location': 'city_number_15_region_city_open_area'}},
            {'event_type': 'lock_dungeon', 'params': {'dungeon_id': 'the_citadel'}},
            {'event_type': 'set_dungeon_locked_text', 'params': {'dungeon_id': 'the_citadel', 'locked_text': "The Citadel is locked tight. Only one who conforms may enter."}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'sam', 'standing_text': ["You don't have to choose a side, Tess. Just be yourself."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'caius', 'standing_text': ["The city is divided. Choose your side, or be left out."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'jett', 'standing_text': ["The red side is for those who embrace their past. The blue side is for those who reject it. Which will you choose?"]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'elian', 'standing_text': ["The city is a stage. The red side plays the role of memory, the blue side plays the role of reputation. Which will you perform?"]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'ravel', 'standing_text': ["I refuse to choose. I won't let them define me."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'hask', 'standing_text': ["Order requires unity. Unity requires a single, authentic self. Choose wisely."]}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch14_intro'}}
        ],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'tess', 'dialog_id': 'tess_ch14_intro'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'sam', 'dialog_id': 'sam_ch14_intro'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'tess', 'dialog_id': 'tess_ch14_performance'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch14_trapped'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'tess', 'dialog_id': 'tess_ch14_best_traps'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'sam', 'dialog_id': 'sam_ch14_ravel_opportunity'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch14_poke_system'}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'tess', 'standing_text': ["This whole city is a rigged game. I love it. Let's find out who's dealing."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'sam', 'standing_text': ["The binary choice is a fallacy. The true power lies with those who set the terms. We need to find them."]}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch14_meet_ravel'}}
        ]
    },
    {
        'task_id': 'main_story_ch14_meet_ravel',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'ravel',
        'task_acquire_events': [],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'ravel', 'dialog_id': 'ravel_ch14_intro'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch14_breaks_something'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch14_false_dichotomy'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch14_social_control'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'ravel', 'dialog_id': 'ravel_ch14_hate_me'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch14_stand_whole'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'lyren_vale', 'dialog_id': 'lyren_ch14_broken_version'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'ravel', 'dialog_id': 'ravel_ch14_hask_stigma'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'tess', 'dialog_id': 'tess_ch14_beautiful_grift'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'thorn', 'dialog_id': 'thorn_ch14_predator_skin'}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'ravel', 'standing_text': ["Hask thinks order is about appearances. He's wrong. It's about being whole."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'sam', 'standing_text': ["Ravel's refusal to choose is a threat to the system. She's a wild card that could disrupt everything."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'tess', 'standing_text': ["Ravel's not playing by the rules. She's a wildcard. I like her."]}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch14_meet_hask'}}
        ]
    },
    {
        'task_id': 'main_story_ch14_meet_hask',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'hask',
        'task_acquire_events': [],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'hask', 'dialog_id': 'hask_ch14_intro'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch14_put_together'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'hask', 'dialog_id': 'hask_ch14_error_cleansed'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch14_tyranny'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'skill', 'dialog_id': 'skill_ch14_dust'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch14_terrified_of_real'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch14_brittle'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'lyren_vale', 'dialog_id': 'lyren_ch14_fractures_deeper'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch14_earning_it'}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'hask', 'standing_text': ["Stigma will bring true unity. The division ends with her."]}},
            {'event_type': 'create_npc', 'params': {'npc_id': 'stigma', 'location': 'region_city_bar'}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch14_meet_stigma'}}
        ]
    },
    {
        'task_id': 'main_story_ch14_meet_stigma',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'stigma',
        'task_acquire_events': [],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'stigma', 'dialog_id': 'stigma_ch14_intro'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch14_who_are_you'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'stigma', 'dialog_id': 'stigma_ch14_family'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch14_cult_leader'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch14_how_exactly'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'stigma', 'dialog_id': 'stigma_ch14_tidekin_cove'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch14_prove_a_point'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'stigma', 'dialog_id': 'stigma_ch14_the_abyss'}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'stigma', 'standing_text': ["Tidekin Cove is a test. See the lies, and then we can talk about the truth."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'ravel', 'standing_text': ["Stigma... she's offering belonging. But at what cost?"]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'hask', 'standing_text': ["Stigma will bring true unity. The division ends with her."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'tess', 'standing_text': ["She seems so sure... maybe picking a side isn't so bad if it's with her."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'sam', 'standing_text': ["I don't trust her. Something about that smile feels too perfect."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'jett', 'standing_text': ["Stigma talks about a new family... but we've heard promises like that before."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'elian', 'standing_text': ["A new leader promising to end the masks... or just give us prettier ones?"]}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch14_meet_caius_in_tidekin'}}
        ]
    },
    {
        'task_id': 'main_story_ch14_meet_caius_in_tidekin',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'caius',
        'task_acquire_events': [],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'caius', 'dialog_id': 'caius_ch14_intro'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch14_nightmare'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'caius', 'dialog_id': 'caius_ch14_stigma_worse'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch14_no_better'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'caius', 'dialog_id': 'caius_ch14_demands_soul'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch14_played'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch14_manipulator'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'skill', 'dialog_id': 'skill_ch14_burn_both'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'caius', 'dialog_id': 'caius_ch14_get_out'}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'caius', 'standing_text': ["Go back to Stigma. Tell her you understand. Before Edict understands you're here."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'jett', 'standing_text': ["Word travels fast. You went to Tidekin Cove... came back looking like you saw something ugly. Stigma’s ‘family’ isn’t sounding so friendly anymore, is it?"]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'elian', 'standing_text': ["You returned from Tidekin Cove quieter than when you left. Whatever you saw there has shaken your faith in Stigma’s promises."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'ravel', 'standing_text': ["Your faces say you didn’t like what you found. Maybe you’re starting to see through her."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'hask', 'standing_text': ["You've returned from Tidekin Cove. If You saw the rot there and still stand with Stigma, then You are truly ready for the cleansing."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'sam', 'standing_text': ["Something in You eyes changed. I don’t trust Stigma’s smile anymore."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'tess', 'standing_text': ["You just got back from Tidekin Cove... You look like You saw behind the curtain. I still want to believe Stigma can fix things... but I’m starting to wonder."]}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch14_return_to_stigma'}}
        ]
    },
    {
        'task_id': 'main_story_ch14_return_to_stigma',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'stigma',
        'task_acquire_events': [],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'stigma', 'dialog_id': 'stigma_ch14_return'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch14_another_manipulator'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch14_another_manipulator'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch14_control'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'stigma', 'dialog_id': 'stigma_ch14_belonging'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch14_choose_you'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'skill', 'dialog_id': 'skill_ch14_predation'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'lyren_vale', 'dialog_id': 'lyren_ch14_erase_parts'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'stigma', 'dialog_id': 'stigma_ch14_venom'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch14_done_with_tools'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch14_end_this'}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch14_defeat_stigma'}}
        ]
    },
    {
        'task_id': 'main_story_ch14_defeat_stigma',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'stigma_boss_battle_1',
        'task_acquire_events': [
            {'event_type': 'begin_combat', 'params': {'boss_mob_id': 'stigma_boss_battle_1', 'combat_type': 'boss_battle'}}
        ],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch14_stigma_defeat'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'stigma', 'dialog_id': 'stigma_ch14_defeat'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch14_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch14_stigma_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch14_stigma_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch14_stigma_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch14_stigma_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'skill', 'dialog_id': 'skill_ch14_stigma_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'lyren_vale', 'dialog_id': 'lyren_ch14_stigma_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'thorn', 'dialog_id': 'thorn_ch14_stigma_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'nia', 'dialog_id': 'nia_ch14_stigma_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch14_face_edict'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch14_face_edict'}},
            {'event_type': 'hide_npc', 'params': {'npc_id': 'stigma'}},
            {'event_type': 'advance_chapter'}
        ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_14',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}