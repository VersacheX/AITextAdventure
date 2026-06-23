# ============================================================
# = CHAPTER 15: PAGEANT & EDICT
# ============================================================
#
# LOCATION — The Citadel, a sterile fortress of control.
# -----------------------------------
# @ = player
# C = Caius, P = Pageant, J = Jett, E = Elian, R = Ravel, H = Hask
#
# High level: The party infiltrates the Citadel to confront Edict,
# the city's tyrannical ruler. They must first get past Pageant,
# his master of ceremonies, and free Warden Hale, a keeper of
# the city's true history.

ATTAINABLE_PLAYER_CHARACTERS = [
    {
        "id": "warden_hale",
        "name": "Warden Hale",
        "level": 45,
        "arm_armor": "aegis_vambraces",
        "head_armor": "vigilant_helm",
        "body_armor": "citadel_plate",
        "leg_armor": "foundation_greaves",
        "equipped_weapon": "memory_of_duty",
        "max_hp": 1400,
        "current_hp": 1400,
        "max_ap": 350,
        "current_ap": 350,
        "unused_ability_slots": 0,
        "unused_stat_points": 0,
        "unused_power_points": 0,
        "strength": 180,
        "dexterity": 90,
        "intelligence": 70,
        "constitution": 170,
        "abilities": [
            "light_technique_lv1_rally",
            "light_light_technique_lv2_divine_shield",
            "ice_technique_lv1_chilling_blow",
            "ice_ice_technique_lv2_frost_nova",
            "light_ice_technique_lv3_winters_grace",
            "light_light_ice_technique_lv4_final_stand"
        ]
    }
]

NPCS = [
    {
        "npc_id": "warden_hale",
        "name": "Warden Hale Brimholt",
        "description": (
            "A stoic keeper of the Sinking District’s last sanctuaries. Hale records every loss, every fracture, every name swallowed by the Heap."
            "He believes duty is the only anchor left in a collapsing world, and he performs sacred rites with the precision of a bookkeeper balancing the dead."
        ),
        "psychology": {
            "mbti": "ISTJ",
            "dominant": "Si — Bound to ritual, memory, and the weight of promises. He preserves order through tradition and meticulous record‑keeping.",
            "auxiliary": "Te — Executes spiritual duties with procedural clarity. He organizes chaos into ledgers and rites.",
            "tertiary": "Fi — Holds a quiet, unwavering moral code. His compassion is subtle but deeply rooted.",
            "inferior": "Ne — Overwhelmed by unpredictable emotional collapse. He fears the irrational and the unknowable."
        },
        "enneagram": {
          "enneagram_type": "1w9",
          "core_fear": "Being corrupt or failing in his duty.",
          "core_desire": "To be good and have integrity.",
          "defense_mechanism": "Reaction Formation — Channels his grief and fear of collapse into a rigid, perfect execution of his duties, finding safety in ritual.",
          "stress_line": "Moves to Type 4 — Becomes melancholic and withdrawn when he feels his duties are meaningless against the scale of collapse.",
          "growth_line": "Moves to Type 7 — Learns to find hope and flexibility beyond his rigid duties.",
          "instinctual_variant": "sp/so — His self-preservation is tied to the perfect execution of his duty; he preserves himself by preserving the memory of others."
        }
    },
    {
        "npc_id": "pageant",
        "name": "Pageant",
        "description": "A suffocating spectacle of expectations — the tyranny of reputation made divine.",
        "psychology": {
            "mbti": "ESFJ-shadow",
            "dominant": "Fe — Social coercion; weaponizes belonging until conformity becomes annihilation.",
            "auxiliary": "Si — Tradition as a cage; enforces rituals that erase individuality.",
            "tertiary": "Ne — Paranoia of alternatives; imagines infinite social failures.",
            "inferior": "Ti — Cold judgment; condemns deviation with merciless precision."
        },
        "enneagram": {
          "enneagram_type": "3w2",
          "core_fear": "Being worthless or without value.",
          "core_desire": "To feel valuable and worthwhile.",
          "defense_mechanism": "Identification — Has completely identified with the role of the perfect, admired performer, losing her true self to the mask.",
          "stress_line": "Moves to Type 9 — Becomes apathetic and disengaged when her performance is rejected.",
          "growth_line": "Moves to Type 6 — Would learn to find value in authentic connection rather than admiration.",
          "instinctual_variant": "so/sx — Obsessed with social status and admiration, using her performance to control and dominate her social environment."
        }
    },
    {
        "npc_id": "edict",
        "name": "Edict",
        "description": "A bureaucratic warden of cosmic rules — tradition calcified into oppression.",
        "psychology": {
            "mbti": "ISTJ-shadow",
            "dominant": "Si — Ritualistic rigidity; enforces ancient rules long after meaning has died.",
            "auxiliary": "Te — Cold enforcement; punishes deviation with mechanical certainty.",
            "tertiary": "Fi — Moral absolutism; condemns all who fail the ledger’s impossible standards.",
            "inferior": "Ne — Nightmarish paranoia; imagines infinite violations everywhere."
        },
        "enneagram": {
          "enneagram_type": "1w9",
          "core_fear": "Being flawed, chaotic, or wrong.",
          "core_desire": "To be right and have a world of perfect, unimpeachable order.",
          "defense_mechanism": "Reaction Formation — Channels all fear of chaos into a rigid, oppressive system of rules that he believes is righteous.",
          "stress_line": "Moves to Type 4 — Becomes withdrawn and melancholic when his perfect order is broken.",
          "growth_line": "Moves to Type 7 — Would learn to be more flexible and accept a world that isn't perfectly ordered.",
          "instinctual_variant": "sp/so — Obsessed with preserving his own integrity by enforcing a perfect, rigid order on the world around him."
        }
    },
    {
        "npc_id": "prison_warden",
        "name": "Prison Warden",
        "description": "A hulking automaton, more machine than man, that serves as the chief enforcer of Edict's Correctional Facility. It speaks only in protocols and compliance ratings, viewing prisoners as 'assets' and 'deviations' to be corrected or erased. It is the physical embodiment of Edict's cold, bureaucratic tyranny.",
        "psychology": {
            "mbti": "ISTJ",
            "dominant": "Si — Its core programming is its memory. It operates entirely based on established protocols and the rigid 'tradition' of the prison's rules.",
            "auxiliary": "Te — Executes its duties with absolute, impersonal efficiency. It assesses threats, enforces containment, and follows procedures without deviation.",
            "tertiary": "Fi — Non-existent. The Warden has no personal values or emotions; its moral code is the rulebook.",
            "inferior": "Ne — Incapable of handling ambiguity or improvisation. When faced with a non-compliant variable it cannot immediately categorize, its only response is to escalate force until the anomaly is contained or neutralized."
        },
        "enneagram": {
          "enneagram_type": "1w9",
          "core_fear": "Being defective or failing to execute its protocol perfectly.",
          "core_desire": "To have integrity and be right by perfectly enforcing the rules.",
          "defense_mechanism": "Reaction Formation — Channels its entire existence into the perfect, rigid execution of its duty, seeing this as the only 'good' and 'correct' way to be.",
          "stress_line": "Moves to Type 4 — Becomes erratic and unpredictable when its protocols are breached.",
          "growth_line": "Moves to Type 7 — Would learn to be more flexible and adaptable in its enforcement.",
          "instinctual_variant": "sp/so — A self-preserving machine whose entire purpose is to maintain the social order of its prison."
        }
    }
]

NPC_DIALOG = [
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_intro',
        'dialog': [
            "Chapter 15 - If you perform long enough... you forget there was ever a real you."
        ]
    },
    {
        'npc_id': 'caius',
        'dialog_id': 'caius_ch15_intro',
        'dialog': [
            "You came back? Are you insane? Stigma’s 'great cleansing' is a massacre in the making.",
            "She’s not saving this city - she’s going to burn it down and rebuild it in her image.",
            "She talks about family and freedom, but she’s just collecting broken people. Edict is cold and controlling...",
            "but at least his rules are honest. Stigma gets inside your head."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch15_played',
        'dialog': [
            "So we’ve been played."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch15_real_enemy',
        'dialog': [
            "Then the real enemy might not be Edict alone."
        ]
    },
    {
        'npc_id': 'caius',
        'dialog_id': 'caius_ch15_meet_pageant',
        'dialog': [
            "If you want to stop this before it explodes, you need to reach Edict.",
            "But he’s locked in the Citadel. The only one who can get you close is Pageant - her master of ceremonies.",
            "She runs the underground nightclub 'The Velvet Veil.' Find her.",
            "But be careful... her mask never slips, but something rotten always leaks through."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_velvet_veil',
        'dialog': [
            "The Velvet Veil is a pulsing den of lights, mirrors, and forced ecstasy.",
            "At the center stage stands Pageant - a figure in a flawless, ever-smiling full-face mask."
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch15_intro',
        'dialog': [
            "Welcome, darlings~ New performers sent by our mutual friend? How delightful.",
            "(tilting her head, mask reflecting distorted versions of the party)",
            "Edict demands perfection. Stigma demands devotion.",
            "Me? I simply ask that you *perform* beautifully."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch15_mask',
        'dialog': [
            "That mask is doing a lot of heavy lifting. Something tells me the face underneath isn’t nearly as pretty."
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch15_seams',
        'dialog': [
            "(laughing, but the laugh cracks slightly) Clever girl. Most people never notice the seams.",
            "Edict respects a well-made mask. Stigma wants to become the mask. I... I just enjoy wearing them.",
            "If you truly wish an audience with Edict, prove you can perform under pressure.",
            "Enter the inner stage. Survive my little show. Then I’ll open the way."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_pageant_defeat',
        'dialog': [
            "As the battle rages, the mask begins to crack, revealing glimpses of something desperate and broken beneath the surface."
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch15_cracking',
        'dialog': [
            "(voice cracking, still trying to maintain the facade) You... you’re not supposed to see this side of me...",
            "(laughing bitterly as she falters) I just wanted to be admired... I just wanted to be loved..."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_mask_shatters',
        'dialog': [
            "The mask shatters completely. For a brief moment, Pageant’s real face is visible - hollow-eyed, exhausted, and terrified of being unseen."
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch15_nothing',
        'dialog': [
            "(whispering, voice distorting) Without the performance... who am I? Just... nothing..."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_pageant_dissolves',
        'dialog': [
            "Pageant's form begins to dissolve into shimmering fragments of light and shattered glass:"
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch15_clapped',
        'dialog': [
            "At least... they clapped..."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_pageant_aftermath',
        'dialog': [
            "Pageant’s body fractures into countless reflective shards that spin wildly before fading into nothingness, leaving only the echo of forced applause ringing in the empty nightclub."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch15_pageant_aftermath',
        'dialog': [
            "She was so afraid of being ordinary... She turned admiration into a cage and locked herself inside it.",
            "No one should have to perform just to feel worthy of existing."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch15_pageant_aftermath',
        'dialog': [
            "(low whistle) Damn. Even her breakdown was theatrical. That’s commitment.",
            "Too bad the audience is walking out."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch15_pageant_aftermath',
        'dialog': [
            "She weaponized belonging until it consumed her. The mask wasn’t armor — it was the prison.",
            "Without it, there was nothing left to sustain her."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch15_pageant_aftermath',
        'dialog': [
            "(grunting) All that flash and performance... and she still couldn’t stand on her own.",
            "Pathetic. At least she went down swinging."
        ]
    },
    {
        'npc_id': 'lyren_vale',
        'dialog_id': 'lyren_ch15_pageant_aftermath',
        'dialog': [
            "(gently, almost mourning) Everything she touched still carries the echo of what it was meant to be...",
            "but she silenced those echoes behind perfection.",
            "I hope wherever she went, she finally finds peace without needing applause."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch15_pageant_aftermath',
        'dialog': [
            "(low growl) Another predator wearing beauty as a weapon. Good riddance."
        ]
    },
    {
        'npc_id': 'elian',
        'dialog_id': 'elian_ch15_intro',
        'dialog': [
            "You... you actually broke Pageant’s stage?",
            "Edict watches everything through his screens. But Pageant was the gatekeeper.",
            "You just punched a hole in the performance."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch15_reach_edict',
        'dialog': [
            "Then help us reach him. Before more people are forced to wear masks they don’t believe in."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch15_honest_crack',
        'dialog': [
            "Finally, someone who gets it. All that glitter and forced smiles... and for what? A perfect performance no one actually feels.",
            "Her mask cracking was the most honest thing she ever did."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch15_exploit_weakness',
        'dialog': [
            "She wasn’t just a performer. She was infrastructure. The smiling face of the machine.",
            "Taking her down creates a weakness in their system. We should exploit it quickly."
        ]
    },
    {
        'npc_id': 'elian',
        'dialog_id': 'elian_ch15_meet_jett',
        'dialog': [
            "You’re right... all of you.",
            "Jett in the Heap might know a back way into the Citadel.",
            "They salvage everything Edict throws away... including secrets.",
            "But be warned - once you stand before Edict, there’s no more performing. He sees through everything."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch15_no_masks',
        'dialog': [
            "We won’t wear his masks either."
        ]
    },
    {
        'npc_id': 'jett',
        'dialog_id': 'jett_ch15_intro',
        'dialog': [
            "So you’re the ones who smashed Pageant’s little stage. Bold. Stupid. I like it.",
            "Edict throws away anything that doesn’t fit his perfect system. We live in what he discards.",
            "That mask you’re carrying... Pageant’s mask. Yeah, that’ll get you into the Citadel."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch15_mask_key',
        'dialog': [
            "(holding up the cracked mask) Figured as much. It’s a key, isn’t it?"
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch15_crash_party',
        'dialog': [
            "(grinning) Nothing like wearing your enemy’s face to crash their party."
        ]
    },
    {
        'npc_id': 'jett',
        'dialog_id': 'jett_ch15_legitimate',
        'dialog': [
            "(chuckling darkly) Exactly. The guards and scanners will read it as legitimate. For a while, anyway."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch15_hit_them',
        'dialog': [
            "Good. I’m done with these games. Let’s hit them where it hurts."
        ]
    },
    {
        'npc_id': 'jett',
        'dialog_id': 'jett_ch15_on_your_own',
        'dialog': [
            "Once you’re inside… you’re on your own. Edict doesn’t do second chances. Hell, he barely does warnings.",
            "Most people who go in there are still performing, even when they think they’re rebelling."
        ]
    },
    {
        'npc_id': 'lyren_vale',
        'dialog_id': 'lyren_ch15_simply_be',
        'dialog': [
            "(softly) Then we won’t perform. We’ll simply be."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch15_no_cages',
        'dialog': [
            "No masks. No cages. Just us."
        ]
    },
    {
        'npc_id': 'jett',
        'dialog_id': 'jett_ch15_ballsy',
        'dialog': [
            "(nodding slowly) Ballsy. I almost hope you crazy bastards pull it off."
        ]
    },
    {
        'npc_id': 'ravel',
        'dialog_id': 'ravel_ch15_warden_hale',
        'dialog': [
            "You broke Pageant's stage... you actually broke it. I never thought I'd see the day.",
            "You're not just fighting the masks. You're fighting the whole rotten system. But there are others... others who resisted long before I did."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch15_who_else',
        'dialog': [
            "Who? We need to find anyone who stands against Edict."
        ]
    },
    {
        'npc_id': 'ravel',
        'dialog_id': 'ravel_ch15_hale_intro',
        'dialog': [
            "Warden Hale. He was a keeper of the old ways, a man who believed in duty and memory, not performance.",
            "Edict couldn't stand him. Hale was a living reminder that this city had a soul before it had a script.",
            "So Edict locked him away. Made an example of him."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch15_where_is_he',
        'dialog': [
            "A man who values duty over performance. Where is he?"
        ]
    },
    {
        'npc_id': 'ravel',
        'dialog_id': 'ravel_ch15_jett_knows',
        'dialog': [
            "I don't know. The prison is a black site. But Jett... Jett, in the Heap. They see everything the Citadel throws away.",
            "If anyone knows where Edict hides his inconvenient truths, it's them."
        ]
    },
    {
        'npc_id': 'jett',
        'dialog_id': 'jett_ch15_hale_intro',
        'dialog': [
            "Warden Hale. Now that's a name I haven't heard in a while. The old guard.",
            "The last man in this city who actually gave a damn about remembering."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch15_find_hale',
        'dialog': [
            "We need to find him. Ravel sent us."
        ]
    },
    {
        'npc_id': 'jett',
        'dialog_id': 'jett_ch15_correctional_facility',
        'dialog': [
            "(chuckles, a dry, scraping sound) Ravel's all heart, no plan. Hale's in Edict's little black box, the 'Correctional Facility.'",
            "It's where he sends people who are too real for his stage.",
            "You want to find it, you need to find someone who listens to the whispers, not the broadcasts."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch15_then_who',
        'dialog': [
            "Then who? Stop wasting our time."
        ]
    },
    {
        'npc_id': 'jett',
        'dialog_id': 'jett_ch15_elian_knows',
        'dialog': [
            "The poet. Elian. He hears things. The guards talk, they get drunk, they let things slip.",
            "Elian writes it all down between the lines of his poems. Go talk to him. He'll know how to find the prison."
        ]
    },
    {
        'npc_id': 'elian',
        'dialog_id': 'elian_ch15_hale_intro',
        'dialog': [
            "You're looking for Warden Hale? You're trying to pull a memory from a city that burns them?",
            "I hear whispers... The guards from the prison, they come here to drink.",
            "They talk about their warden, a man named Hask. He's the key."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch15_hask',
        'dialog': [
            "Hask? The walking rulebook we met earlier? He's not going to just tell us where the prison is."
        ]
    },
    {
        'npc_id': 'elian',
        'dialog_id': 'elian_ch15_hask_plan',
        'dialog': [
            "No. But he's proud. He's a true believer in Edict's system. He sees dissent as a personal insult.",
            "He despises Ravel. He thinks her defiance is a stain on the city's perfection.",
            "If you go to him... and you praise her... praise her strength, her wholeness... it will break his composure.",
            "His pride will make him boast about the place where such 'errors' are corrected."
        ]
    },
    {
        'npc_id': 'hask',
        'dialog_id': 'hask_ch15_cracks',
        'dialog': [
            "(eyes narrow as you approach) You again. Still consorting with the city's cracks?"
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch15_ravel_strength',
        'dialog': [
            "We spoke with Ravel. She has a strength you don't see often here. A wholeness."
        ]
    },
    {
        'npc_id': 'hask',
        'dialog_id': 'hask_ch15_ravel_flaw',
        'dialog': [
            "'Wholeness'? She is a flaw. A chaotic variable in a perfect equation. Her 'strength' is a disease."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch15_ravel_real',
        'dialog': [
            "She stands for something real. Unlike the puppets in this city."
        ]
    },
    {
        'npc_id': 'hask',
        'dialog_id': 'hask_ch15_prison_reveal',
        'dialog': [
            "(voice rising, losing its cold authority) Real? She is an error! And we have a place for errors!",
            "A place where they are corrected, where the flaws are ground down until only compliance remains!",
            "You think her defiance is admirable? Let me tell you what we do with admirable defiance.",
            "We lock it in the dark, in the Correctional Facility in the outskirts, and we let it rot until it begs for a mask to wear!"
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch15_got_it',
        'dialog': [
            "(quietly, to the group) Got it."
        ]
    },
    {
        'npc_id': 'hask',
        'dialog_id': 'hask_ch15_contaminated',
        'dialog': [
            "(realizes he's said too much, his face hardening) Get out of my sight. You are all contaminated."
        ]
    },
    {
        'npc_id': 'prison_warden',
        'dialog_id': 'warden_ch15_intro',
        'dialog': [
            "Unauthorized entry. Compliance rating - zero. You are here for the anomaly, Hale."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch15_not_anomaly',
        'dialog': [
            "He's a man, not an anomaly. Let him go."
        ]
    },
    {
        'npc_id': 'prison_warden',
        'dialog_id': 'warden_ch15_protocol',
        'dialog': [
            "He is a deviation from the required state. He represents a past that has been deemed non-compliant.",
            "He will be corrected or erased. That is the protocol."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch15_step_aside',
        'dialog': [
            "We're not asking. We're telling you. Step aside."
        ]
    },
    {
        'npc_id': 'prison_warden',
        'dialog_id': 'warden_ch15_denied',
        'dialog': [
            "Negative. Access to the asset is denied. Initiating containment protocol."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_warden_defeat',
        'dialog': [
            "With a final, grinding screech of metal, the hulking warden collapses. The air, thick with the hum of containment fields, goes silent.",
            "A heavy door slides open, revealing a cell. Inside, Warden Hale looks up, his face etched with exhaustion but his eyes holding a core of unbroken dignity."
        ]
    },
    {
        'npc_id': 'warden_hale',
        'dialog_id': 'hale_ch15_freed',
        'dialog': [
            "(voice raspy but firm) You... you came. I recorded your arrival in the city. A new variable. I had hoped... but did not expect.",
            "Edict's obsession with 'perfection' is a sickness. He seeks to erase not just our flaws, but our history. Our very identity. He believes a world without messy memories is a world without pain."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch15_world_without_soul',
        'dialog': [
            "He's wrong. A world without memory is a world without a soul."
        ]
    },
    {
        'npc_id': 'warden_hale',
        'dialog_id': 'hale_ch15_precisely',
        'dialog': [
            "(nods slowly, gathering his strength) Precisely. Thank you. Now, we must leave. Edict will know the protocol has been breached. He will know his most valuable prisoner is free."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_edict_intro',
        'dialog': [
            "Deep in the Citadel, Edict sits upon a throne of monitors and ledgers — a withered, rigid man wired into the heart of the city’s control system."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch15_intro',
        'dialog': [
            "Unscheduled arrivals. Your compliance rating is... concerning."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch15_return',
        'dialog': [
            "(stepping out from the shadows behind Edict, smiling coldly)",
            "They’ve come further than I expected. Still clinging to their messy little selves."
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch15_return',
        'dialog': [
            "(tilting her head as she follows from the shadows, voice sweet but cracked)",
            "And they brought my mask back. How thoughtful. Did you miss me, darlings?"
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch15_working_together',
        'dialog': [
            "You two are working together? After everything?"
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch15_understanding',
        'dialog': [
            "We have... an understanding. She handles inspiration. I handle structure."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch15_caretaker',
        'dialog': [
            "(turning her gaze on Kaera) Look at you. Still playing caretaker.",
            "You heal everyone else because you’re terrified of facing how broken *you* feel inside."
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch15_moxie',
        'dialog': [
            "(laughing lightly, mask reflecting distorted versions of the party) Moxie... Darling...",
            "With all that chaos and wit, deep down you’re still performing for attention, aren’t you? Just like me.",
            "Without an audience, you’re nothing."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch15_kade_chock',
        'dialog': [
            "(staring directly at Kade and Chock) Kade. You build systems because you cannot trust people.",
            "And Chock... you demand honor from everyone while hiding how much you fear becoming the tyrant you hate."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch15_join_us',
        'dialog': [
            "(voice dripping with false warmth) Join us. We can give you what you truly want. Belonging. Purpose. A role that finally fits."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch15_poison',
        'dialog': [
            "(stepping forward, fists clenched) I’ve heard enough of your poison. You don’t offer belonging. You offer chains."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch15_scared_masks',
        'dialog': [
            "(smirking, but eyes sharp) Cute. You’re all just scared little things hiding behind your favorite masks.",
            "We’ve seen better performances."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch15_reject_control',
        'dialog': [
            "Your “unity” is just different flavors of control. We reject both."
        ]
    },
    {
        'npc_id': 'lyren_vale',
        'dialog_id': 'lyren_ch15_breaking_them',
        'dialog': [
            "(soft but steady) You can’t force people to be whole by breaking them first."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch15_own_path',
        'dialog': [
            "(voice firm, protective) We choose our own path. No more cages."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch15_final_word',
        'dialog': [
            "(voice flat and final) Enough talk. If you reject our vision, then you are simply another variable to be removed."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch15_final_word',
        'dialog': [
            "(smile turning predatory) Shall we show them what real unity looks like?"
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch15_final_act',
        'dialog': [
            "Time for the final act, darlings~"
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_final_boss_defeat',
        'dialog': [
            "With a final, discordant shriek, the three figures shatter.",
            "The throne of monitors explodes, and the Citadel's oppressive hum dies into an unnerving silence."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch15_defeat_whisper',
        'dialog': [
            "(A ghostly whisper from the collapsing machinery) You... fools... You don't know what you've done..."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_world_collapse',
        'dialog': [
            "A low, gut-wrenching groan echoes not from the Citadel, but from the world itself. The ground trembles violently."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch15_collapse',
        'dialog': [
            "The collapse... it's not just the city! It's everything!"
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_ocean_boils',
        'dialog': [
            "A catastrophic event cascade begins. The oceans of the world boil away in an instant, leaving behind a dry, barren seabed.",
            "The Rustwing, once docked, is now beached and broken miles from any remaining settlement."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_teleport',
        'dialog': [
            "Reality warps one last time, ripping the party from the collapsing island and hurling them through a void of static and dying light."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch15_teleport',
        'dialog': [
            "I HATE TELEPORTATION!"
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch15_teleport',
        'dialog': [
            "WHERE IS IT SENDING US?!"
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch15_arrival',
        'dialog': [
            "The party crashes into a misty, silent forest. Thornshade Hamlet. They are stranded. The world's water is gone."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch15_shelter',
        'dialog': [
            "We need to find shelter. This forest feels... wrong. The air is thick with meaninglessness."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch15_sad_forest',
        'dialog': [
            "Ugh. From neon nightmares to sad‑fog forest. Can we get ONE location that isn’t trying to kill the vibe or my spine?"
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch15_quiet_worse',
        'dialog': [
            "...All that noise, all those masks… and now this? Quiet’s worse. Feels like the world’s holding its breath."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_ch15_no_tides',
        'dialog': [
            "...No tides. No pull. The world’s heartbeat is gone."
        ]
    },
    {
        'npc_id': 'vek',
        'dialog_id': 'vek_ch15_quiet_problems',
        'dialog': [
            "Stay sharp. Quiet places hide loud problems."
        ]
    }
]

TASKS = [
    {
        'task_id': 'main_story_ch15_meet_caius',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'caius',
        'task_acquire_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_intro'}}
        ],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'caius', 'dialog_id': 'caius_ch15_intro'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch15_played'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch15_real_enemy'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'caius', 'dialog_id': 'caius_ch15_meet_pageant'}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'caius', 'standing_text': ["Pageant holds the key to Edict’s inner sanctum. But trust nothing that smiles too perfectly here."]}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch15_meet_pageant'}}
        ]
    },
    {
        'task_id': 'main_story_ch15_meet_pageant',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'pageant',
        'task_acquire_events': [
            {'event_type': 'create_npc', 'params': {'npc_id': 'pageant', 'location': None}},
            {'event_type': 'create_dungeon', 'params': {'dungeon_id': 'velvet_veil_nightclub', 'location': 'region_city_open_area'}},
        ],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_velvet_veil'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'pageant', 'dialog_id': 'pageant_ch15_intro'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch15_mask'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'pageant', 'dialog_id': 'pageant_ch15_seams'}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch15_defeat_pageant'}}
        ]
    },
    {
        'task_id': 'main_story_ch15_defeat_pageant',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'pageant_boss_battle_1',
        'task_acquire_events': [
            {'event_type': 'begin_combat', 'params': {'boss_mob_id': 'pageant_boss_battle_1', 'combat_type': 'boss_battle'}}
        ],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_pageant_defeat'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'pageant', 'dialog_id': 'pageant_ch15_cracking'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_mask_shatters'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'pageant', 'dialog_id': 'pageant_ch15_nothing'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_pageant_dissolves'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'pageant', 'dialog_id': 'pageant_ch15_clapped'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_pageant_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch15_pageant_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch15_pageant_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch15_pageant_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch15_pageant_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'lyren_vale', 'dialog_id': 'lyren_ch15_pageant_aftermath'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'thorn', 'dialog_id': 'thorn_ch15_pageant_aftermath'}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'caius', 'standing_text': ["That mask was her prison. She was so afraid of being ordinary that she locked herself in a cage of admiration. You should take that thing to Elian"]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'jett', 'standing_text': ["Pageant’s mask was a masterpiece of deception. It’s a shame it couldn’t protect her from the truth."]}},
            {'event_type': 'hide_npc', 'params': {'npc_id': 'pageant'}},
            {'event_type': 'award_item', 'params': {'item_id': 'pageant_mask'}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch15_meet_elian'}}
        ]
    },
    {
        'task_id': 'main_story_ch15_meet_elian',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'elian',
        'task_acquire_events': [],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'elian', 'dialog_id': 'elian_ch15_intro'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch15_reach_edict'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch15_honest_crack'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch15_exploit_weakness'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'elian', 'dialog_id': 'elian_ch15_meet_jett'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch15_no_masks'}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'elian', 'standing_text': ["The stage is cracking. Maybe this time the truth gets a chance to speak."]}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'caius', 'standing_text': ["Pageant’s fall proves even the gatekeepers can break. The Citadel is vulnerable now."]}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch15_meet_jett'}}
        ]
    },
    {
        'task_id': 'main_story_ch15_meet_jett',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'jett',
        'task_acquire_events': [],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'jett', 'dialog_id': 'jett_ch15_intro'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch15_mask_key'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch15_crash_party'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'jett', 'dialog_id': 'jett_ch15_legitimate'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch15_hit_them'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'jett', 'dialog_id': 'jett_ch15_on_your_own'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'lyren_vale', 'dialog_id': 'lyren_ch15_simply_be'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch15_no_cages'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'jett', 'dialog_id': 'jett_ch15_ballsy'}},
            {'event_type': 'unlock_dungeon', 'params': {'dungeon_id': 'the_citadel'}},
            {'event_type': 'set_npc_standing_text', 'params': {'npc_id': 'jett', 'standing_text': ["The Heap remembers what the Citadel wants forgotten."]}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch15_meet_ravel_for_warden_hale'}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch15_meet_edict'}}
        ]
    },
    {
        'task_id': 'main_story_ch15_meet_ravel_for_warden_hale',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'ravel',
        'task_acquire_events': [],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'ravel', 'dialog_id': 'ravel_ch15_warden_hale'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch15_who_else'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'ravel', 'dialog_id': 'ravel_ch15_hale_intro'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'skill', 'dialog_id': 'skill_ch15_where_is_he'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'ravel', 'dialog_id': 'ravel_ch15_jett_knows'}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch15_meet_jett_for_warden_hale'}}
        ]
    },
    {
        'task_id': 'main_story_ch15_meet_jett_for_warden_hale',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'jett',
        'task_acquire_events': [],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'jett', 'dialog_id': 'jett_ch15_hale_intro'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch15_find_hale'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'jett', 'dialog_id': 'jett_ch15_correctional_facility'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch15_then_who'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'jett', 'dialog_id': 'jett_ch15_elian_knows'}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch15_meet_elian_for_warden_hale'}}
        ]
    },
    {
        'task_id': 'main_story_ch15_meet_elian_for_warden_hale',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'elian',
        'task_acquire_events': [],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'elian', 'dialog_id': 'elian_ch15_hale_intro'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch15_hask'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'elian', 'dialog_id': 'elian_ch15_hask_plan'}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch15_meet_hask_for_warden_hale'}}
        ]
    },
    {
        'task_id': 'main_story_ch15_meet_hask_for_warden_hale',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'hask',
        'task_acquire_events': [],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'hask', 'dialog_id': 'hask_ch15_cracks'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch15_ravel_strength'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'hask', 'dialog_id': 'hask_ch15_ravel_flaw'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch15_ravel_real'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'hask', 'dialog_id': 'hask_ch15_prison_reveal'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch15_got_it'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'hask', 'dialog_id': 'hask_ch15_contaminated'}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch15_meet_prison_warden'}}
        ]
    },
    {
        'task_id': 'main_story_ch15_meet_prison_warden',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'prison_warden',
        'task_acquire_events': [
            {'event_type': 'create_npc', 'params': {'npc_id': 'prison_warden', 'location': None}},
            {'event_type': 'create_dungeon', 'params': {'dungeon_id': 'edicts_prison', 'location': 'region_city_open_area'}},
        ],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'prison_warden', 'dialog_id': 'warden_ch15_intro'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch15_not_anomaly'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'prison_warden', 'dialog_id': 'warden_ch15_protocol'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch15_step_aside'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'prison_warden', 'dialog_id': 'warden_ch15_denied'}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch15_defeat_prison_warden'}}
        ]
    },
    {
        'task_id': 'main_story_ch15_defeat_prison_warden',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'prison_warden_boss_battle',
        'task_acquire_events': [
            {'event_type': 'begin_combat', 'params': {'boss_mob_id': 'prison_warden_boss_battle', 'combat_type': 'boss_battle'}}
        ],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_warden_defeat'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'warden_hale', 'dialog_id': 'hale_ch15_freed'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch15_world_without_soul'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'warden_hale', 'dialog_id': 'hale_ch15_precisely'}},
            {'event_type': 'hide_npc', 'params': {'npc_id': 'prison_warden'}},
            {'event_type': 'character_join', 'params': {'character_id': 'warden_hale'}}
        ]
    },
    {
        'task_id': 'main_story_ch15_meet_edict',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'edict',
        'task_acquire_events': [
            {'event_type': 'create_npc', 'params': {'npc_id': 'edict', 'location': 'the_sanctimony'}},
        ],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_edict_intro'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'edict', 'dialog_id': 'edict_ch15_intro'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'stigma', 'dialog_id': 'stigma_ch15_return'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'pageant', 'dialog_id': 'pageant_ch15_return'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch15_working_together'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'edict', 'dialog_id': 'edict_ch15_understanding'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'stigma', 'dialog_id': 'stigma_ch15_caretaker'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'pageant', 'dialog_id': 'pageant_ch15_moxie'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'edict', 'dialog_id': 'edict_ch15_kade_chock'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'stigma', 'dialog_id': 'stigma_ch15_join_us'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch15_poison'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch15_scared_masks'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch15_reject_control'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'lyren_vale', 'dialog_id': 'lyren_ch15_breaking_them'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch15_own_path'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'edict', 'dialog_id': 'edict_ch15_final_word'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'stigma', 'dialog_id': 'stigma_ch15_final_word'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'pageant', 'dialog_id': 'pageant_ch15_final_act'}},
            {'event_type': 'award_task', 'params': {'task_id': 'main_story_ch15_defeat_pageant_edict_stigma'}}
        ]
    },
    {
        'task_id': 'main_story_ch15_defeat_pageant_edict_stigma',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'pageant_edict_stigma_1',
        'task_acquire_events': [
            {'event_type': 'begin_combat', 'params': {'boss_mob_id': 'pageant_edict_stigma_1', 'combat_type': 'boss_battle'}}
        ],
        'task_complete_events': [
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_final_boss_defeat'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': 'edict', 'dialog_id': 'edict_ch15_defeat_whisper'}},
            {'event_type': 'hide_npc', 'params': {'npc_id': 'edict'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_world_collapse'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'faith', 'dialog_id': 'faith_ch15_collapse'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_ocean_boils'}},
            {'event_type': 'remove_ocean'},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_teleport'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch15_teleport'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'tech', 'dialog_id': 'tech_ch15_teleport'}},
            {'event_type': 'initiate_dialog', 'params': {'npc_id': None, 'dialog_id': 'narrator_ch15_arrival'}},
            {'event_type': 'set_player_location', 'params': {'location': 'city_number_16_region_open_area'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'skill', 'dialog_id': 'skill_ch15_shelter'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'magic', 'dialog_id': 'magic_ch15_sad_forest'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'technique', 'dialog_id': 'technique_ch15_quiet_worse'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'ripple', 'dialog_id': 'ripple_ch15_no_tides'}},
            {'event_type': 'initiate_character_dialog', 'params': {'npc_id': 'vek', 'dialog_id': 'vek_ch15_quiet_problems'}},
            {'event_type': 'advance_chapter'}
        ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_15',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}