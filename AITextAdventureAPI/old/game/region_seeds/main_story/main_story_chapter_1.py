ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	####NPCS FOR CHAPTER 1
	{
		'npc_id': 'oren',
		'name': 'Oren',
		'description': (
			'An absent minded and mentally diversive dreamer.'
			"  He's not sure if he's wandering reality, or if it's wandering him."
		),
		"psychology": {
			"mbti": "INFP",
			"dominant": "Fi — Lives in an inner world of meaning and personal truth. His sense of identity is fluid, poetic, and introspective. He follows internal feelings rather than logic or structure.",
			"auxiliary": "Ne — His mind drifts into possibilities, metaphors, and alternate interpretations of reality. He sees symbolic meaning everywhere and often speaks in riddles or dreamlike imagery.",
			"tertiary": "Si — Occasionally grounds himself in familiar patterns or memories, but these come in fragments. His past feels hazy, like a half‑remembered dream.",
			"inferior": "Te — When stressed, he becomes disorganized, overwhelmed by practical demands, or frustrated by the need to make concrete decisions."
		},
        "enneagram": {
          "enneagram_type": "9w1",
          "core_fear": "Loss, separation, and fragmentation.",
          "core_desire": "To have inner stability and peace of mind.",
          "defense_mechanism": "Dissociation — Mentally drifts away from conflict or overwhelming reality, retreating into a world of metaphor and dreams.",
          "stress_line": "Moves to Type 6 — Becomes anxious, worried, and dependent on others when his inner peace is shattered.",
          "growth_line": "Moves to Type 3 — Becomes more present, engaged, and able to take purposeful action in the world.",
          "instinctual_variant": "sp/so — Seeks comfort in familiar places (like inns) and gentle social connection, avoiding conflict."
        },
		'image': 'npcs:oren1'
	},
	{
		'npc_id': 'rook',
		'name': 'Rook Halden',
		'description': (
			'Quiet, methodical, and unnervingly patient.  Rook is the bounty hunter'
			" nobody wants after them.  Somehow he always finds a way to get the job done."
		),
		"psychology": {
		"mbti": "ISTJ",
			"dominant": "Si — Relies on experience, routine, and proven methods. He tracks patterns, remembers details, and uses past encounters to predict behavior.",
			"auxiliary": "Te — Efficient, direct, and results‑oriented. He organizes his hunts with precision and expects others to follow instructions without fuss.",
			"tertiary": "Fi — Holds quiet personal values and a private moral code. He rarely expresses emotion, but loyalty and justice matter deeply to him.",
			"inferior": "Ne — Under stress, he becomes suspicious of unpredictable outcomes or overwhelmed by chaotic possibilities. He dislikes surprises and improvisation."
		},
        "enneagram": {
          "enneagram_type": "6w5",
          "core_fear": "Being without support or guidance; being unable to survive on his own.",
          "core_desire": "To have security and support.",
          "defense_mechanism": "Projection — Offloads his own anxiety and doubt by focusing on external threats (like Seth) and seeking reliable allies.",
          "stress_line": "Moves to Type 3 — Becomes arrogant and work-obsessed, focused only on the appearance of success.",
          "growth_line": "Moves to Type 9 — Becomes more relaxed, trusting, and open to different perspectives.",
          "instinctual_variant": "sp/so — Focused on security, anticipating threats, and forming reliable alliances to ensure survival."
        },
		'image': 'npcs:rook1'
	},
	{
		'npc_id': 'seth',
		'name': 'Seth',
		'description': (
			"A scrappy bandit that has been causing trouble in the area."
			"  He's wanted for multiple robberies and assaults."
		),
		"psychology": {
			"mbti": "ESFP",
			"dominant": "Se — Lives moment-to-moment, reacting instantly to danger or opportunity. Fast, instinctive, and physically agile. He reads the environment like a predator and moves before others can think.",
			"auxiliary": "Fi — Makes decisions based on personal feelings, grudges, and loyalties. His rivalry with Rook is emotional, not strategic. He hides a surprisingly soft core under bravado.",
			"tertiary": "Te — When cornered, he becomes sharp, decisive, and surprisingly organized. He can plan short-term escapes or quick tactical moves, but he cannot sustain long-term strategy.",
			"inferior": "Ni — Under stress, he spirals into paranoia or fatalistic thinking. He imagines worst-case scenarios, overinterprets threats, and becomes erratic or self-destructive."
		},
        "enneagram": {
          "enneagram_type": "7w6",
          "core_fear": "Being trapped, deprived, or in pain.",
          "core_desire": "To be free and satisfied, to escape pain and find excitement.",
          "defense_mechanism": "Rationalization — Justifies his thievery and troublemaking as a game or a necessary means of survival to avoid facing his own fears.",
          "stress_line": "Moves to Type 1 — Becomes rigid, critical, and defensive when cornered.",
          "growth_line": "Moves to Type 5 — Becomes more thoughtful, strategic, and capable of seeing the bigger picture beyond immediate gratification.",
          "instinctual_variant": "sp/sx — Focused on securing his own survival and freedom, seeking intense experiences and alliances to stay ahead."
        },
		'image': 'npcs:seth1'
	},
	{
		'npc_id': 'tess',
		'name': 'Tess',
		'description': (
			'Sly, cunning, manipulative, and chaotically charming with a razor wit.'
			"  Tess is the sarcastic one between her and her sister Sam."
			"  Yet even with her sharp tongue she always has a way of getting what she wants."			
		),
		"psychology": {
			"mbti": "ENFP",
			"dominant": "Ne — Reads people instantly, improvises socially, and jumps between ideas with chaotic brilliance. She thrives on unpredictability and opportunity.",
			"auxiliary": "Fi — Makes decisions based on personal values and emotional instincts. Her charm is genuine when she cares, cutting when she doesn’t.",
			"tertiary": "Te — When she wants something, she becomes surprisingly forceful and organized. She can weaponize logic to get her way.",
			"inferior": "Si — Hates routine and repetition. Under stress, she becomes nostalgic, fixated on past slights, or overwhelmed by details she normally ignores."
		},
        "enneagram": {
          "enneagram_type": "7w8",
          "core_fear": "Being deprived, limited, or bored.",
          "core_desire": "To be satisfied and have her needs met, to experience everything.",
          "defense_mechanism": "Rationalization — Frames manipulation and chaos as fun, exciting, or necessary, avoiding the emotional consequences.",
          "stress_line": "Moves to Type 1 — Becomes rigid, critical, and moralistic when her plans fail or she feels trapped.",
          "growth_line": "Moves to Type 5 — Becomes more focused, objective, and able to think through consequences before acting.",
          "instinctual_variant": "so/sx — Socially engaging and charming, using her wit to navigate and influence her environment for new opportunities."
        },
        'image': 'npcs:tess1'
	},
	{
		'npc_id': 'sam',
		'name': 'Sam',
		'description': (
			'Quiet, observant, calculating, and deadly in business,'
			" Sam is the serious one between her and her sister Tess."
			"  Raised by a con artist and a relic smuggler, she's learned to make the most of every situation."
		),
		"psychology": {
			"mbti": "INTJ",
			"dominant": "Ni — Sees long‑term patterns and hidden motives. She reads situations strategically and plans several moves ahead.",
			"auxiliary": "Te — Executes plans with precision. She is efficient, direct, and ruthlessly practical when handling business or danger.",
			"tertiary": "Fi — Holds private emotional convictions and personal loyalties. She rarely shows vulnerability, but her moral compass is strong.",
			"inferior": "Se — Under stress, she becomes hypersensitive to sensory chaos or acts impulsively, abandoning her usual calm strategy."
		},
        "enneagram": {
          "enneagram_type": "5w6",
          "core_fear": "Being useless, helpless, or overwhelmed by the world.",
          "core_desire": "To be capable and competent.",
          "defense_mechanism": "Isolation — Detaches from the chaos to observe and analyze, hoarding information to feel prepared and in control.",
          "stress_line": "Moves to Type 7 — Becomes scattered and avoids problems when her plans fail or she feels incompetent.",
          "growth_line": "Moves to Type 8 — Becomes more confident and assertive, taking direct action based on her knowledge.",
          "instinctual_variant": "sp/so — Focused on self-preservation through knowledge and competence, while keeping a strategic eye on social dynamics."
        },
        'image': 'npcs:sam1'
	},
	{
		'npc_id': 'diego',
		'name': 'Diego',
		'description': (
			'An ex-mercenary turned information broker.'
			"  Diego has a network of contacts in the black market and underground."
			"  He's battle hardened and has connections in a wide network."
		),
		"psychology": {
			"mbti": "ESTP",
			"dominant": "Se — Sharp, reactive, and physically grounded. He reads people and environments instantly, making him dangerous both in combat and negotiation.",
			"auxiliary": "Ti — Analyzes information networks, motives, and opportunities with cool internal logic. He understands systems instinctively.",
			"tertiary": "Fe — Uses charm, humor, and social intuition to manipulate or persuade. He knows how to make people like him—or fear him.",
			"inferior": "Ni — Under stress, he becomes paranoid about hidden threats or future consequences. He may overinterpret signs or assume betrayal."
		},
        "enneagram": {
          "enneagram_type": "8w7",
          "core_fear": "Being controlled or harmed by others.",
          "core_desire": "To be in control of his own life and destiny.",
          "defense_mechanism": "Denial — Projects an aura of strength and control, denying any personal weakness or vulnerability. He's always on top of the situation.",
          "stress_line": "Moves to Type 5 — Becomes secretive and withdrawn, hoarding information and fearing betrayal.",
          "growth_line": "Moves to Type 2 — Uses his power and influence to protect and provide for those he cares about.",
          "instinctual_variant": "sx/so — Seeks intensity and control in his relationships and social network, always positioning himself at the center of the action."
        },
		'image': 'npcs:diego1'
	},
	{
		'npc_id': 'brawn',
		'name': 'Brawn',
		'description': (
			'A burly retired soldier with a passion for ornate and specialized armors.'
			"  Brawn has a keen eye for quality and craftsmanship."
			"  He's an encyclopedia of warfare under an earnest demeanor."
		),
		"psychology": {
			"mbti": "ESFJ",
			"dominant": "Fe — Warm, expressive, and socially attuned. He enjoys helping others and takes pride in being a reliable presence.",
			"auxiliary": "Si — Deeply knowledgeable about armor, history, and craftsmanship. He values tradition and respects the old ways of warfare.",
			"tertiary": "Ne — Occasionally becomes imaginative or curious about unusual relics or cursed items. He enjoys hearing stories behind artifacts.",
			"inferior": "Ti — Under stress, he becomes overly critical or nitpicky about details, or he withdraws into rigid technical judgments."
		},
        "enneagram": {
          "enneagram_type": "2w3",
          "core_fear": "Being unwanted or worthless.",
          "core_desire": "To feel loved and valued.",
          "defense_mechanism": "Repression — Focuses on being helpful and providing for others to earn their appreciation, while ignoring his own needs.",
          "stress_line": "Moves to Type 8 — Becomes demanding and controlling when his efforts are not appreciated.",
          "growth_line": "Moves to Type 4 — Becomes more aware of his own identity and needs, separate from his service to others.",
          "instinctual_variant": "so/sp — Finds value in being a central, helpful figure in his community, ensuring his own security through social connection."
        },
		'image': 'npcs:brawn1'
	}
]

NPC_DIALOG = [
	{
		'npc_id': None,
		'dialog_id': 'chapter_1_start',
		'dialog': [
			"You don't know how you got here.",
			"One moment you and your friends were in a bar, knocking back a few µ.",
			"The next, blinding light tore through the room.",
			"Reality folded. When it opened again, three of your friends were gone.",
			"This place looks like chaos. The streets are littered, buildings stand looted, and fights break out on every corner."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'ch1_narrator_we_do_not_begin',
		'dialog': [
			"Chapter 1",
			"We do not begin by knowing where we are. We begin by finding ourselves already there. - after Heidegger"
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'chapter_1_intro2',
		'dialog': [
			"A thuggish man in a black bandana and a leather jacket runs out to you from the alley."

		]
	},
	{
		'npc_id': 'seth',
		'dialog_id': 'seth_preface',
		'dialog': [
			"Whoa! That was crazy! You just appeared out of nowhere...",
			"Hey, look, these streets aren't safe. Be careful who you trust.",
			"And if Tess and Sam ask, you didn't see me. I am not paying that tab today.",
			"Gotta run... It's tuff out here!"
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch1_seth_preface',
		'dialog': [
			"I don't like that guy.",
			"Don't know why. It's his face. I want to hit his face."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch1_seth_preface',
		'dialog': [
			"He warned us, then ran like something was chasing him.",
			"I hope whoever he owes is kinder than this city looks."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch1_seth_preface',
		'dialog': [
			"A total stranger tells us to trust no one, then sprints off? I love him.",
			"I don't trust him. But I love him."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch1_seth_preface',
		'dialog': [
			"Tess and Sam. He owes them money, which means they have leverage here.",
			"Names worth remembering."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch1_seth_preface',
		'dialog': [
			"He looked at our hands before our faces.",
			"Thief."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'chapter_1_our_stuff_is_missing',
		'dialog': [
			"Find a residence or business (î Î ï Ï), then press (i) to manage your party.",
			"Check in often. When a character has a free ability slot, teach them something new.",
			"Most buildings are safe. The bars and the subways are not.",
			"If you get low, head to the @inn."
		]
	},
	{
		'npc_id': 'oren',
		'dialog_id': 'oren_intro',
		'dialog': [
			"Oh! Hey there. You look like you're not from here either. Like me. I'm Oren, just wandering and exploring.",
			"Not sure if it's reality wandering me, or if I'm wandering reality.",
			"I always seem to find my way to the @inn. Every city has an @inn.",
			"If you ever want to find the other side of another one, head to the ₨. It'll get you there."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch1_oren',
		'dialog': [
			"Guy's not all there.",
			"Forget the riddles. We've got nothing on us. Item shop, now."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch1_oren',
		'dialog': [
			"He's lost, but he isn't afraid. I envy that a little.",
			"We should gather supplies before we go anywhere."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch1_oren',
		'dialog': [
			"I like him! He's a fortune cookie that forgot the fortune.",
			"Ooh, also: shopping. Go go go."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch1_oren',
		'dialog': [
			"Somehow I think we're there.",
			"Logistics first. We have no supplies."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch1_oren',
		'dialog': [
			"He said the ₨.",
			"Supplies next. Item shop."
		]
	},
	{
		'npc_id': 'rook',
		'dialog_id': 'rook_intro',
		'dialog': [
			"You're new. And broke. I can tell from here.",
			"Name's Rook. I collect bounties. There's one on a bandit called Seth. He's holed up in a hideout on the outskirts.",
			"He's slipped me four times. Bring him to me and you'll be paid.",
			"Here's something up front. Buy Caffeine Shots and Pocket Salves. You'll need both."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch1_rook_deal',
		'dialog': [
			"Seth? The guy with the face?",
			"Oh, I'm in."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch1_rook_deal',
		'dialog': [
			"Bounty or not, we bring him back alive. Agreed?",
			"Supplies first."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch1_rook_deal',
		'dialog': [
			"Caffeine Shots? He had me at caffeine.",
			"Best errand list ever."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch1_rook_deal',
		'dialog': [
			"Paid work and a read on the local economy. Efficient.",
			"Stock up."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch1_rook_deal',
		'dialog': [
			"Fast target. Hideout. Outskirts.",
			"Stock up first."
		]
	},
	{
		'npc_id': 'seth',
		'dialog_id': 'seth_intro',
		'dialog': [
			"So Rook sent you to run me down?",
			"That guy's got it bad for me. This personal vendetta of his is really getting old.",
			"Well, you're here now. Let's see what you've got!"
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch1_seth_fight',
		'dialog': [
			"You've got it coming, Seth.",
			"Mostly for the face."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch1_seth_fight',
		'dialog': [
			"We don't have to do this the hard way, Seth.",
			"...But we will if we must."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch1_seth_fight',
		'dialog': [
			"Ooh, a boss fight! Somebody hold my drink."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch1_seth_fight',
		'dialog': [
			"He keeps the exits behind him. Pressure him and he'll make mistakes."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch1_seth_fight',
		'dialog': [
			"He's fast.",
			"I'm faster."
		]
	},
	{
		'npc_id': 'seth',		
		'dialog_id': 'seth_ch1_defeat',
		'dialog': [
			"Ha! Ha! You guys are good. I'm not sticking around for the finale, though. See ya!"
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch1_seth_escape',
		'dialog': [
			"Get back here!",
			"...I wasn't done with his face. Fine. Let's go tell Rook."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch1_seth_escape',
		'dialog': [
			"He's hurt, but he'll live. I'm glad of that.",
			"Rook should hear what happened."
		]
	},
	{
		'npc_id': 'magic', 
		'dialog_id': 'magic_ch1_seth_escape',
		'dialog': [
			"Hahaha! Look at him run!",
			"Rook is going to love this. Or hate it."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch1_seth_escape',
		'dialog': [
			"We didn't catch him, but we proved we could. That's worth something."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch1_seth_escape',
		'dialog': [
			"That guy was fast.",
			"Report."
		]
	},
	{
		'npc_id': 'rook',
		'dialog_id': 'rook_ch1_closing',
		'dialog': [
			"So you found him. And he got away.",
			"...He always does. Still, I hear you left a mark. That's more than most manage.",
			"Half the bounty. Fair is fair.",
			"You look like you need a drink. The bar's that way. Get yourself a µ."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch1_rook_report',
		'dialog': [
			"Free money and a bar. It's about time, I need a fucking drink."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch1_rook_report',
		'dialog': [
			"A bar... that's where all of this started.",
			"Maybe someone there has heard something about the others."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch1_rook_report',
		'dialog': [
			"Last time we had drinks, we got teleported to another world.",
			"Let's see what happens this time!"
		]
	},
	{
		'npc_id': 'tech', 
		'dialog_id': 'tech_ch1_rook_report',
		'dialog': [
			"Bars are where information leaks. We go for the gossip, not the drinks.",
			"...Mostly the gossip."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch1_rook_report',
		'dialog': [
			"Bar. Listen more than we drink."
		]
	},
	{
		'npc_id': 'tess',
		'dialog_id': 'tess_intro_s1',
		'dialog': [
			"Oooh! Here they are, Sam. The ones who fell out of the sky and roughed up Seth for Rook.",
			"...And then let him run off. Charming."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch1_tess_meet',
		'dialog': [
			"He had it coming.",
			"Something about his face."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch1_tess_meet',
		'dialog': [
			"We didn't want to hurt him. He didn't leave us much choice."
		]
	},
	{
		'npc_id': 'magic', 
		'dialog_id': 'magic_ch1_tess_meet',
		'dialog': [
			"Hahaha! My reputation precedes me. Already!"
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch1_tess_meet',
		'dialog': [
			"Word travels fast here. Noted."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch1_tess_meet',
		'dialog': [
			"He ran. He'll be back."
		]
	},
	{
		'npc_id': 'sam',
		'dialog_id': 'sam_intro_s1',
		'dialog': [
			"Rook doesn't share his bounties. You must have impressed him.",
			"Seth knows us too. Small world, messy debts."
		]
	},
	{
		'npc_id': 'tess',
		'dialog_id': 'tess_intro_s2',
		'dialog': [
			"Did that weasel say anything about our tab? ...Of course he didn't.",
			"So. You're new, you're nearly broke, and you're missing people. Don't look so surprised, it's all over your faces.",
			"Here's the deal. You help us out, and we'll keep our ears open for anyone else who fell out of the sky.",
			"Head over to the Æ and talk to Diego. Tell him Tess and Sam sent you."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch1_tess_deal',
		'dialog': [
			"Deal. And if Seth shows up again, he's mine.",
			"Diego. Let's move."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch1_tess_deal',
		'dialog': [
			"Thank you. Truly. Any word of them would mean everything.",
			"Let's find Diego."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch1_tess_deal',
		'dialog': [
			"A secret errand from two mysterious sisters? Say less.",
			"To the Æ!"
		]
	},
	{
		'npc_id': 'tech', 
		'dialog_id': 'tech_ch1_tess_deal',
		'dialog': [
			"Their network for our labor. A fair trade.",
			"Diego, at the Æ."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch1_tess_deal',
		'dialog': [
			"Diego. Æ. Go."
		]
	},
	
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_gives_logger',
        'dialog': [
            "If you're going to be dealing with all sorts of characters, you should have this.",
            "It's a Mnemonic Logger. It keeps track of contacts you make who want to be seen. It might help you separate the snakes from the saints.",
            "Just... try to stay out of trouble. This city has enough of it."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_reacts_to_logger',
        'dialog': [
            "A log? Good. Information is a weapon. Let's make sure ours is sharp."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_reacts_to_logger',
        'dialog': [
            "Fascinating. A device for cataloging social encounters. I wonder if it logs sarcasm levels."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'spirit_reacts_to_logger',
        'dialog': [
            "This could be a blessing. Understanding who people are is the first step to helping them."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_reacts_to_logger',
        'dialog': [
            "A list of targets and allies. Efficient. I like it."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_reacts_to_logger',
        'dialog': [
            "Ooh, a little black book! Does it have pictures? Let's see who we can annoy first."
        ]
    },
	{
		'npc_id': 'diego',
		'dialog_id': 'diego_intro',
		'dialog': [
			"Hmmmmm! Can't say I've seen your faces before, and I've seen a lot of ugly faces.",
			"Those troublemakers Tess and Sam sent you? Interesting.",
			"I'm Diego. Ex-merc, glorified information salesman.",
			"The girls asked me to track down a relic for them called the Grift Stone.",
			"I traced it to a black market dealer named Mira.",
			"She stays in a nearby city and likes to frequent the µ, unloading shady shit to shady people.",
			"She won't give it up easy, though. Talk to Brawn at the Armory, and maybe pick up some ¥ while you're there.",
			"He's a real armor aficionado. He'll most likely have something she'd be interested in.",
			"And yes, Tess told me you've misplaced some friends. I'll keep an ear out. No charge... this time."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch1_diego',
		'dialog': [
			"Armory? Finally. I could do with an upgrade."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch1_diego',
		'dialog': [
			"He'll listen for them. That's something.",
			"Mira sounds dangerous. Let's be prepared."
		]
	},
	{
		'npc_id': 'magic', 
		'dialog_id': 'magic_ch1_diego',
		'dialog': [
			"Oooh hoo hoooo!!! A black market dealer!",
			"I wonder what Mira has for sale! Armory first, I guess. Boo."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch1_diego',
		'dialog': [
			"A trade chain. Brawn's goods for Mira's stone.",
			"Start at the Armory."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch1_diego',
		'dialog': [
			"Brawn. Armory."
		]
	},
	{
		'npc_id': 'brawn',
		'dialog_id': 'brawn_intro',
		'dialog': [
			"Ho there! So Diego sent you, eh?",
			"He reckons I've got something Mira would want. He's right. I do.",
			"But I need a favour first. Seth swiped a pair of my ornate bracers. I'd bet my pension on it.",
			"Bracers like those were worn by honor guards three wars back. They don't belong in a bandit's sack.",
			"Search his hideout and bring them home."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch1_brawn',
		'dialog': [
			"Seth again? Good.",
			"I wasn't done with his face."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch1_brawn',
		'dialog': [
			"They clearly mean a great deal to him. We'll bring them back."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch1_brawn',
		'dialog': [
			"Breaking back into the bandit's hideout? Yes. I love a sequel."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch1_brawn',
		'dialog': [
			"We know the hideout's layout now. If he's stashing loot, it's in the final chamber."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch1_brawn',
		'dialog': [
			"Stolen gear. Simple job. We move."
		]
	},
	{
		'npc_id': 'technique', 
		'dialog_id': 'technique_brawn_ornate_bracers',
		'dialog': [
			"You know these things don't look like they can take much of a hit."
		]
	},
	{
		'npc_id': 'brawn',
		'dialog_id': 'brawn_ch1_closing',
		'dialog': [
			"Aha! You found them! Aren't they beautiful?",
			"Don't let their looks fool you. These were never made for hitting. They were made to be remembered.",
			"Now, Mira. Take her this cursed couplet I came across. She'll want it.",
			"She's in Boiling Bubble at the moment, and she loves the bar there.",
			"Trade it to her for the Grift Stone."
		]
	},
	{
		'npc_id': 'brawn',
		'dialog_id': 'brawn_ch1_closing_no_logger',
		'dialog': [
			"And speak to Sam before you go. She has something that'll help you out."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch1_couplet',
		'dialog': [
			"Cursed? Great. You're carrying it.",
			"Boiling Bubble. Let's get rid of it."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch1_couplet',
		'dialog': [
			"There's something sorrowful bound up in it.",
			"Let's get it to Mira quickly. Boiling Bubble."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch1_couplet',
		'dialog': [
			"I might be interested in it too?!? That thing looks powerful.",
			"...Fine. Boiling Bubble. But I'm holding it on the way."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch1_couplet',
		'dialog': [
			"A cursed object as currency. This economy is fascinating.",
			"Next stop, Boiling Bubble."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch1_couplet',
		'dialog': [
			"Boiling Bubble. Bar. Mira."
		]
	}

]

# TEST_DIALOG = [
# 	{
# 		'npc_id': None,
# 		'dialog_id': 'ch1_choice_look_for_friends',
# 		'dialog': [
# 			"You decide to look for your missing friends first.",
# 			"Someone in this city must know something."
# 		]
# 	},
# 	{
# 		'npc_id': None,
# 		'dialog_id': 'ch1_choice_find_somewhere_safe',
# 		'dialog': [
# 			"You decide to find somewhere safe to regroup.",
# 			"The inn seems like the best bet for now."
# 		]
# 	},
# 	{
# 		'npc_id': None,
# 		'dialog_id': 'ch1_choice_look_around',
# 		'dialog': [
# 			"You decide to take stock of your surroundings first.",
# 			"A reckless charge into chaos never helped anyone."
# 		]
# 	}
# 	# ,
# 	# {
# 	# 	'npc_id': None,
# 	# 	'dialog_id': 'condition_test_narrator',
# 	# 	'dialog': ["conditions work."]
# 	# }
# ]

# NPC_DIALOG += TEST_DIALOG
TASKS = [
	# Task 1: main_story_ch_1_find_the_inn
	{
		'task_id': 'main_story_ch_1_find_the_inn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'oren',
		'task_acquire_events': [			
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': None,
					'dialog_id': 'chapter_1_start'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': None,
					'dialog_id': 'ch1_narrator_we_do_not_begin'
				}
			},
			{
				'event_type': 'player_character_join',
				'params': {
					'dialog_id': 'begin_game_add_pc',
					'exclude_custom_class': True,
				}
			},		
			{
				'event_type': 'player_character_join',
				'params': {
					'dialog_id': 'begin_game_add_pc',
					'exclude_custom_class': True,
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': None,
					'dialog_id': 'chapter_1_intro2'
				}
			},
			{
				'event_type': 'create_npc', 'params': { 'npc_id': 'seth', 'location': None }
			},			
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'seth',
					'dialog_id': 'seth_preface'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch1_seth_preface'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch1_seth_preface'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch1_seth_preface'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch1_seth_preface'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch1_seth_preface'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'seth',
					'standing_text': [
						"Still here? Like I said, trust nobody. Especially not me."
					]
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': None,
					'dialog_id': 'chapter_1_our_stuff_is_missing'
				}
			},
			{
				'event_type': 'create_npc', 'params': { 'npc_id': 'oren', 'location': 'region_city_inn' }
			},
			{
				'event_type': 'create_npc', 'params': { 'npc_id': 'rook', 'location': 'region_city_shopitems' }
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rook',
					'standing_text': [						
						"You look like fresh meat for the grinder."
					]
				}
			},
			{
				'event_type': 'create_npc', 'params': { 'npc_id': 'diego', 'location': 'region_city_shopweapons' }
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"Information is the most valuable currency.",
						"Know where to look and who to ask."
					]
				}
			},
			{
				'event_type': 'create_npc', 'params': { 'npc_id': 'brawn', 'location': 'region_city_shoparmor' }
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'brawn',
					'standing_text': [
						"Quality armor is an investment in your survival.",
						"Don't skimp on your protection."
					]
				}
			}
			# ,
			# #INITIATE OPTION DIALOG WITH 3 OPTIONS. HAVE THE TASKS DO NOTHING EXCEPT CALL NARRATOR DIALOG [initiate_dialog npc_id=None] STATING THE CHOICE THEY MADE
			# {
			# 	'event_type': 'initiate_option_dialog',
			# 	'params': {
			# 		'message': "The city is in chaos. What do you do first?",
			# 		'options': [
			# 			('Look for your missing friends', 'ch1_option_look_for_friends'),
			# 			('Find somewhere safe to regroup',  'ch1_option_find_somewhere_safe'),
			# 			('Look around and take stock',      'ch1_option_look_around'),
			# 		]
			# 	}
			# }
		],
		'task_complete_events': [ 
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'oren',
					'dialog_id': 'oren_intro'
				}
			},			
			###TEMP - HOW TO GET SLAUGHTERED BY GARBAGE AT THE BEGINNING
			# {
			# 	'event_type': 'create_npc',
			# 	'params': {
			# 		'npc_id': 'garbage',
			# 		'location': None
			# 	}
			# },
			# {
			# 	'event_type': 'begin_combat', # <- begin combat with garbage with no reward as it's just an event, not an acquire event in a defeat task
			# 	'params': {
			# 		'boss_mob_id': 'garbage_1',
			# 		'combat_type': 'boss_battle'
			# 	}
			# }
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch1_oren'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch1_oren'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch1_oren'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch1_oren'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch1_oren'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'oren',
					'standing_text': [
						"Why are you still here? .. Why am I still here?",
						"Where is here.?.  What is here?.?",
						"...Remember to go to the ₨...",
						"I remember her saying."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_1_find_item_shop'
				}
			}
		]
	},
	# # Option stub: look for friends
	# {
	# 	'task_id': 'ch1_option_look_for_friends',
	# 	'type': 'deliver',
	# 	'item_id': 'rift_core',
	# 	'to_type': 'npc',
	# 	'to_id': 'kadeem',
	# 	'task_acquire_events': [
	# 		{
	# 			'event_type': 'initiate_dialog',
	# 			'params': {
	# 				'npc_id': None,
	# 				'dialog_id': 'ch1_choice_look_for_friends'
	# 			}
	# 		},
	# 		{
	# 			'event_type': 'award_item',
	# 			'params': {
	# 				'item_id': 'lucky_charm'
	# 			}
	# 		},
	# 		{
	# 			'event_type': 'award_item',
	# 			'params': {
	# 				'item_id': 'worn_ring'
	# 			}
	# 		},
	# 		{
	# 			'event_type': 'award_item',
	# 			'params': {
	# 				'item_id': 'worn_ring'
	# 			}
	# 		},
	# 		{
	# 			'event_type': 'award_item',
	# 			'params': {
	# 				'item_id': 'toughened_cord'
	# 			}
	# 		}
	# 	],
	# 	'task_complete_events': []
	# },
	# # Option stub: find somewhere safe
	# {
	# 	'task_id': 'ch1_option_find_somewhere_safe',
	# 	'type': 'deliver',
	# 	'item_id': 'phase_crystal',
	# 	'to_type': 'npc',
	# 	'to_id': 'alchemist_mirlo',
	# 	'task_acquire_events': [
	# 		{
	# 			'event_type': 'initiate_dialog',
	# 			'params': {
	# 				'npc_id': None,
	# 				'dialog_id': 'ch1_choice_find_somewhere_safe'
	# 			}
	# 		},
	# 		{
	# 			'event_type': 'award_item',
	# 			'params': {
	# 				'item_id': 'toughened_cord'
	# 			}
	# 		},
	# 		{
	# 			'event_type': 'award_item',
	# 			'params': {
	# 				'item_id': 'worn_ring'
	# 			}
	# 		},
	# 		{
	# 			'event_type': 'award_item',
	# 			'params': {
	# 				'item_id': 'worn_ring'
	# 			}
	# 		},
	# 		{
	# 			'event_type': 'award_item',
	# 			'params': {
	# 				'item_id': 'lucky_charm',
	# 				'quantity': 1
	# 			}
	# 		}
	# 	],
	# 	'task_complete_events': []
	# },
	# # Option stub: look around
	# {
	# 	'task_id': 'ch1_option_look_around',
	# 	'type': 'deliver',
	# 	'item_id': 'demigorgon_tooth',
	# 	'to_type': 'npc',
	# 	'to_id': 'emberwitch_thera',
	# 	'task_acquire_events': [
	# 		{
	# 			'event_type': 'initiate_dialog',
	# 			'params': {
	# 				'npc_id': None,
	# 				'dialog_id': 'ch1_choice_look_around'
	# 			}
	# 		},
	# 		{
	# 			'event_type': 'award_item',
	# 			'params': {
	# 				'item_id': 'worn_ring'
	# 			}
	# 		},
	# 		{
	# 			'event_type': 'award_item',
	# 			'params': {
	# 				'item_id': 'worn_ring'
	# 			}
	# 		},
	# 		{
	# 			'event_type': 'award_item',
	# 			'params': {
	# 				'item_id': 'worn_ring'
	# 			}
	# 		},
	# 		{
	# 			'event_type': 'award_item',
	# 			'params': {
	# 				'item_id': 'toughened_cord'
	# 			}
	# 		}
	# 	],
	# 	'task_complete_events': []
	# },
	#Task 2 find item shop
	{
		'task_id': 'main_story_ch_1_find_item_shop',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rook',
		'task_acquire_events': [
			# {
			# 	'event_type': 'initiate_dialog',
			# 	'params': {
			# 		'npc_id': None,
			# 		'dialog_id': 'condition_test_narrator'
			# 	},
			# 	'condition': {
			# 		'type': 'is_task_completed',
			# 		'params': { 'task_id': 'main_story_ch_1_find_the_inn' }
			# 	}
			# }
		],
		'task_complete_events': [ 
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rook',
					'dialog_id': 'rook_intro'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch1_rook_deal'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch1_rook_deal'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch1_rook_deal'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch1_rook_deal'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch1_rook_deal'
				}
			},
			{
				'event_type': 'award_money',
				'params': {
					'amount': '200'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rook',
					'standing_text': [
						"Seth's hideout is on the outskirts. He's slippery. Don't let him talk his way out."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_1_meet_seth'
				}
			}
		]
	},
	# Task 3: meet Seth in a dungeon
	{
		'task_id': 'main_story_ch_1_meet_seth',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'seth',
		'task_acquire_events': [
			{
				'event_type': 'create_dungeon',
				'params': {
					'dungeon_id': 'seth_hideout',
					'location': 'region_open_area'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'seth',
					'dialog_id': 'seth_intro'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch1_seth_fight'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch1_seth_fight'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch1_seth_fight'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch1_seth_fight'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch1_seth_fight'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'seth',
					'standing_text': [
						"Ha! Ha! You guys are good. I'm not sticking around for the finale, though. See ya!"
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_1_defeat_seth'
				}
			}
		],
	},
	# Task 4: defeat Seth
	{
		'task_id': 'main_story_ch_1_defeat_seth',
        'type': 'defeat',
        'to_type': 'mob',
		'to_id': 'seth_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat', 
				'params': {
					'boss_mob_id': 'seth_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'seth',
					'dialog_id': 'seth_ch1_defeat'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch1_seth_escape'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch1_seth_escape'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch1_seth_escape'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch1_seth_escape'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch1_seth_escape'
				}
			},
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'seth'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_1_report_to_rook'
				}
			}
		]
	},
	# Task 5: report back to Rook at original location
	{
		'task_id': 'main_story_ch_1_report_to_rook',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rook',
		'task_acquire_events': [], 
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rook',
					'dialog_id': 'rook_ch1_closing'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch1_rook_report'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch1_rook_report'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch1_rook_report'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch1_rook_report'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch1_rook_report'
				}
			},
			{
				'event_type': 'award_money',
				'params': {
					'amount': '400'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'rook',
					'standing_text': [
						"Seth will turn up again. He always does."
					]
				}
			},
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'rook'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_1_meet_tess_and_sam'
				}
			}
		]
	},
	# TASK 6: meet tess and sam at the bar
	{
		'task_id': 'main_story_ch_1_meet_tess_and_sam',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'tess',
		'task_acquire_events': [
			{
				'event_type': 'create_npc', 'params': { 'npc_id': 'tess', 'location': 'region_city_bar' }
			},
			{
				'event_type': 'create_npc', 'params': { 'npc_id': 'sam', 'location': 'region_city_bar' }
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sam',
					'standing_text': [
						"Those new arrivals look like they can handle themselves. Maybe they can help us out."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'tess',
					'dialog_id': 'tess_intro_s1'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch1_tess_meet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch1_tess_meet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch1_tess_meet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch1_tess_meet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch1_tess_meet'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'sam',
					'dialog_id': 'sam_intro_s1'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'tess',
					'dialog_id': 'tess_intro_s2'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch1_tess_deal'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch1_tess_deal'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch1_tess_deal'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch1_tess_deal'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch1_tess_deal'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'tess',
					'standing_text': [
						"Diego'll be at the Æ. Tell him Tess and Sam sent you."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sam',
					'standing_text': [
						"I hope Diego has an update for us."
					]		
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_1_meet_diego'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'side_quest_get_logger_from_sam'
				}
			}
		]
	},
	{
        'task_id': 'side_quest_get_logger_from_sam',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'sam',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'sam',
                    'dialog_id': 'sam_gives_logger'
                }
            },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'mnemonic_logger'
                }
            },
            {
                'event_type': 'unlock_npc_log'
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'technique',
                    'dialog_id': 'technique_reacts_to_logger'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'tech_reacts_to_logger'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'spirit',
                    'dialog_id': 'spirit_reacts_to_logger'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'skill_reacts_to_logger'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'magic_reacts_to_logger'
                }
            },
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sam',
					'standing_text': [
						"That logger should help you keep track of your progress."
					]
				}
			}
        ]
    },
	# TASK 7: meet diego at the Æ
	{
		'task_id': 'main_story_ch_1_meet_diego',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'diego',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'diego',
					'dialog_id': 'diego_intro'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch1_diego'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch1_diego'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch1_diego'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch1_diego'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch1_diego'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'tess',
					'standing_text': [
						"That makes sense, Brawn does deal with some specialized armors."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sam',
					'standing_text': [
						"Hmmmmm... A relic dealer that frequents µ... Sounds like a dangerous place."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"Brawn at the Armory might have something Mira wants. Go see him and maybe pick up some ¥ while you're there."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_1_meet_brawn'
				}
			}
		]
	},
	# Task 8 - meet brawn at the shoparmor
	{
		'task_id': 'main_story_ch_1_meet_brawn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'brawn',
		'task_acquire_events': [
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'brawn',
					'dialog_id': 'brawn_intro'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch1_brawn'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch1_brawn'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch1_brawn'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch1_brawn'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch1_brawn'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'tess',
					'standing_text': [
						"Hahahaha! Seth's so much trouble. Come back after you give the bracers to Brawn. These updates are epic."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sam',
					'standing_text': [
						"Those ornate bracers must be something special if Brawn wants them back so badly. Hope you find them quickly."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"That retired soldier lost his bracers?",
						"Wonder what Seth saw in those?"
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'brawn',
					'standing_text': [
						"What are you standing around here for?"
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_1_deliver_ornate_bracers'
				}
			}
		]
	},
	# Task 9 - deliver ornate bracers
	{
		'task_id': 'main_story_ch_1_deliver_ornate_bracers',
		'type': 'deliver',
		'item_id': 'ornate_bracers',
		'to_type': 'npc',
		'to_id': 'brawn',
		'task_acquire_events': [
			{
				'event_type': 'dungeon_add_treasure',
				'params': {
					'dungeon_id': 'seth_hideout',
					'item_id': 'ornate_bracers',
					'location': 'final_chamber'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_brawn_ornate_bracers'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'brawn',
					'dialog_id': 'brawn_ch1_closing'
				}
			},
			{ # raise dialog for brawn if the players do not have a mnemonic_logger
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'brawn',
					'dialog_id': 'brawn_ch1_closing_no_logger'
				},
				'condition': {
					'type': 'has_item',
					'params': { 'item_id': 'mnemonic_logger' },
					'operator': 'is_not'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch1_couplet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch1_couplet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch1_couplet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch1_couplet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch1_couplet'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'tess',
					'standing_text': [
						"Oooooooh! That's a cute couplet..."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sam',
					'standing_text': [
						"That couplet looks ancient. I wonder what powers it holds?"
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"Still not sure what you're arrival here means.",
						"Maybe Mira will know things I don't with her deep connections in the black market."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'brawn',
					'standing_text': [
						"Remember to give Mira my regards?"
					]
				}
			},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'ornate_bracers'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'cursed_couplet'
				}
			},
			{
				'event_type': 'advance_chapter'
			}
		]
	}
    
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_1',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
    }