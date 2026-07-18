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
			"In one moment you and your compadres were in a bar knocking back a few µ.",
			"And the next, blinding lights crashed through the dim establishment.",
			"Reality shifted around you, and you found yourself here with three of your friends missing.",
			"This place looks like chaos.  The streets are littered, buildings look looted, and people can be seen breaking out in fights."
		]
	},
    {
		'npc_id': None,
		'dialog_id': 'ch1_narrator_we_do_not_begin',
		'dialog': [
			"Chapter 1",
			"We do not begin by knowing where we are.  We begin by finding ourselves already there."
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
			"Whoa! that was crazy! You appeared out of nowhere...",
			"Hey Look, these streets aren't safe, be careful who you trust.",
			"Gotta run... It's tuff out here!"
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'chapter_1_our_stuff_is_missing',
		'dialog': [
			"You should get somewhere safe to check your things.  Most buildings are safe, except for the bars.",
			"Find a residence or business (î Î ï Ï), then press (i) to manage your party.",
			"Make sure to spend any power points you have to upgrade your stats and ensure your characters learn any abilities",
			"If you get low head to the @inn."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_got_jacked',
		'dialog': [
			"If you ask me the first person to question trusting is the guy sayin be careful who to trust."
		]
	},
	{
		'npc_id': 'oren',
		'dialog_id': 'oren_intro',
		'dialog': [
			"Oh!, Hey there.  You look like you're not from here like me.  I'm Oren, just wandering and exploring.",
			"Not sure if it's reality wandering me, or if I'm wandering reality.",
			"I seem to always find a way to the @inn.  Every city has an @inn.",
			"If you ever intend to find the other side in another one, head to the ₨ to get you there."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_says_somehow_i_think_were_there',
		'dialog': [
			"Somehow I think we're there."
		]
	},
	{
		'npc_id': 'rook',
		'dialog_id': 'rook_intro',
		'dialog': [
			"You're looking short on funds there my guy.  I'm Rook, the bounty hunter. I'll tell ya what, I'll cut ya a deal.",
			"I have a bounty for a nearby bandit Seth's head.  He's camped up in the outskirts nearby.  Bring it back to me and I'll give ya some cash.",
			"Tell you what, I'll give you a little up front so you can get started.  I recommend buying some Caffeine Shots and Pocket Salves."
		]
	},
	{
		'npc_id': 'skill', # skill(Poise) loves energy drinks
		'dialog_id': 'skill_loves_caffeine_shots',
		'dialog': [
			"Oh I am down on that.  Nobody can ever get enough caffeine. Let's Go!"
		]
	},
	{
		'npc_id': 'technique', # technique(Chock) is ready to bust some bounty
		'dialog_id': 'technique_ready_to_bust_bounty',
		'dialog': [
			"I've been waiting to hear somebody say I get paid to bust that guy up all day!  Let's go get 'em!"
		]
	},
	{
		'npc_id': 'seth',
		'dialog_id': 'seth_intro',
		'dialog': [
			"So Rook sent you to run me down?",
			"That guy's got it bad for me.  This personal vendetta of his is really getting old.",
			"Well, you're here now.  Let's see what you've got!"
		]
	},
	{
		'npc_id': 'technique', # technique(Chock) is ready to bust some bounty
		'dialog_id': 'technique_you_got_it_coming',
		'dialog': [
			"You got it coming, Seth!",
			"We're taking you down!"
		]
	},
	{
		'npc_id': 'seth',		
		'dialog_id': 'seth_ch1_defeat',
		'dialog': [
			"Ha!Ha! You guys are good. I don't intend to hang around for you to finish the job. See you later!"
		]
	},
	{
		'npc_id': 'skill', # skill(Poise) that guy was fast
		'dialog_id': 'skill_that_guy_was_fast',
		'dialog': [
			"That guy was fast!"
		]
	},
	{
		'npc_id': 'magic', 
		'dialog_id': 'magic_haha_he_cant_wait_to_get_away',
		'dialog': [
			"Hahaha! Look at him run!"
		]
	},
	{
		'npc_id': 'rook',
		'dialog_id': 'rook_ch1_closing',
		'dialog': [
			"So ya managed to find him.  He's pretty crafty, it's no doubt he got away.",
			"Still funny to hear he got his ass kicked.",
			"Tell you what, I'll give you half of what I intended.",
			"With all that cash you should head to the bar and get a µ."
		]
	},
	{
		'npc_id': 'tech', 
		'dialog_id': 'tech_knocking_back_a_few',
		'dialog': [
			"I wouldn't mind knocking back a few drinks!"
		]
	},
	{
		'npc_id': 'technique', 
		'dialog_id': 'technique_good_idea_after_good_idea',
		'dialog': [
			"You know I'm beginning to like this place!"
		]
	},
	{
		'npc_id': 'tess',
		'dialog_id': 'tess_intro_s1',
		'dialog': [
			"Oooh! Here they are Sam. The ones Sylvi was talking about."
		]
	},
	{
		'npc_id': 'magic', 
		'dialog_id': 'magic_to_sam_1',
		'dialog': [
			"Hahaha! My reputation always preceeding me."
		]
	},
	{
		'npc_id': 'sam',
		'dialog_id': 'sam_intro_s1',
		'dialog': [
			"Heard they went and busted up Seth pretty good for Rook. They could be useful."
		]
	},
	{
		'npc_id': 'technique', 
		'dialog_id': 'technique_to_sam_1',
		'dialog': [
			"That guy had it coming. I knew the moment I saw him I wanted to punch him in the face."
		]
	},
	{
		'npc_id': 'tess',
		'dialog_id': 'tess_intro_s2',
		'dialog': [
			"They definitely look like they can handle themselves.",
			"Tell you what guys, you help us out and we'll help you out.",
			"Head over and speak to Diego at the Æ.",
			"Tell him Tess and Sam sent you. He'll tell you what you need to know from there."
		]
	},
	{
		'npc_id': 'tech', 
		'dialog_id': 'tech_interested_in_gear',
		'dialog': [
			"I'm interested to find out what kind of cool gear this world has."
		]
	},
	
    {
        'npc_id': 'sam',
        'dialog_id': 'sam_gives_logger',
        'dialog': [
            "Tess mentioned you were helping out. If you're going to be dealing with all sorts of characters, you should have this.",
            "It's a Mnemonic Logger. It'll keep track of everyone you meet. Might help you separate the snakes from the saints.",
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
        'npc_id': 'faith',
        'dialog_id': 'faith_reacts_to_logger',
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
			"Hmmmmm!  I can't say I've seen your faces before, and I've seen a lot of ugly faces.",
			"Those trouble makers Tess and Sam sent you?  Interesting.",
			"I'm Diego. Ex-merc, glorified information salesman.",
			"Those girls asked me to track down a relic for them called The Grift Stone.",
			"I managed to track it to a black market dealer named Mira.",
			"She stays in a nearby city and likes to frequent the µ unloading shady shit to shady people.",
			"She won't give it up easy though.  Talk to Brawn at the Armory and maybe pick up some ¥ while you're there.",
			"He's a real armor officionado, he'll most likely have something she'd be interested in."		
		]
	},
	{ #response to diego
		'npc_id': 'technique', #also a, soldier, technique or Chock respects diegos scars and wonders what kind of hostiles this world offers
		'dialog_id': 'technique_diego_intro',
		'dialog': [
			"Wouldn't mind a peek at some armor, I could do with a little upgrade."
		]
		
	},
	{
		'npc_id': 'magic', 
		'dialog_id': 'magic_interested_in_mira',
		'dialog': [
			"Oooh hoo hoooo!!! I wonder what interesting items Mira has for sale!"
		]
	},
	{
		'npc_id': 'brawn',
		'dialog_id': 'brawn_intro',
		'dialog': [
			"Ho there! ... So Diego sent you?",
			"Ha! He said I have something for you to trade with Mira?",
			"As a matter of fact I have something she would love.",
			"You're going to have to do something for me first though.",
			"I'm pretty sure Seth jacked a pair of my ornate bracers.",
			"Head back to his hideout and see if you can find them in there."
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
			"Aha! you found them!!! Aren't they beautiful.",
			"Ok Mira will be interested in this cursed couplet I came across.",
			"She's in Boiling Bubble at the moment and loves to hang out at the bar.",
			"If you run into her give her the couplet for the Grift Stone...",
			"Remember to give her my regards."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_likes_cursed_couplet',
		'dialog': [
			"I might be interested in it too?!? That thing looks powerful."
		]
	}

]

TEST_DIALOG = [
	{
		'npc_id': None,
		'dialog_id': 'ch1_choice_look_for_friends',
		'dialog': [
			"You decide to look for your missing friends first.",
			"Someone in this city must know something."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'ch1_choice_find_somewhere_safe',
		'dialog': [
			"You decide to find somewhere safe to regroup.",
			"The inn seems like the best bet for now."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'ch1_choice_look_around',
		'dialog': [
			"You decide to take stock of your surroundings first.",
			"A reckless charge into chaos never helped anyone."
		]
	}
	# ,
	# {
	# 	'npc_id': None,
	# 	'dialog_id': 'condition_test_narrator',
	# 	'dialog': ["conditions work."]
	# }
]

NPC_DIALOG += TEST_DIALOG
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
				'event_type': 'player_character_join',
				'params': {
					'dialog_id': 'begin_game_add_pc'
				}
			},		
			{
				'event_type': 'player_character_join',
				'params': {
					'dialog_id': 'begin_game_add_pc'
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
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': None,
					'dialog_id': 'chapter_1_our_stuff_is_missing'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_got_jacked'
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
			},
            {
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': None,
					'dialog_id': 'ch1_narrator_we_do_not_begin'
				}
			},
			#INITIATE OPTION DIALOG WITH 3 OPTIONS. HAVE THE TASKS DO NOTHING EXCEPT CALL NARRATOR DIALOG [initiate_dialog npc_id=None] STATING THE CHOICE THEY MADE
			{
				'event_type': 'initiate_option_dialog',
				'params': {
					'message': "The city is in chaos. What do you do first?",
					'options': [
						('Look for your missing friends', 'ch1_option_look_for_friends'),
						('Find somewhere safe to regroup',  'ch1_option_find_somewhere_safe'),
						('Look around and take stock',      'ch1_option_look_around'),
					]
				}
			}
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
					'npc_id': 'tech',
					'dialog_id': 'tech_says_somehow_i_think_were_there'
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
	# Option stub: look for friends
	{
		'task_id': 'ch1_option_look_for_friends',
		'type': 'deliver',
		'item_id': 'rift_core',
		'to_type': 'npc',
		'to_id': 'kadeem',
		'task_acquire_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': None,
					'dialog_id': 'ch1_choice_look_for_friends'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'lucky_charm'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'worn_ring'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'worn_ring'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'toughened_cord'
				}
			}
		],
		'task_complete_events': []
	},
	# Option stub: find somewhere safe
	{
		'task_id': 'ch1_option_find_somewhere_safe',
		'type': 'deliver',
		'item_id': 'phase_crystal',
		'to_type': 'npc',
		'to_id': 'alchemist_mirlo',
		'task_acquire_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': None,
					'dialog_id': 'ch1_choice_find_somewhere_safe'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'toughened_cord'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'worn_ring'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'worn_ring'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'lucky_charm',
					'quantity': 1
				}
			}
		],
		'task_complete_events': []
	},
	# Option stub: look around
	{
		'task_id': 'ch1_option_look_around',
		'type': 'deliver',
		'item_id': 'demigorgon_tooth',
		'to_type': 'npc',
		'to_id': 'emberwitch_thera',
		'task_acquire_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': None,
					'dialog_id': 'ch1_choice_look_around'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'worn_ring'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'worn_ring'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'worn_ring'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'toughened_cord'
				}
			}
		],
		'task_complete_events': []
	},
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
					'npc_id': 'skill',
					'dialog_id': 'skill_loves_caffeine_shots'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ready_to_bust_bounty'
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
						"Bring him to me and I'll give you half the bounty. He's camped up in a hideout somewhere in the outskirts."
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
			#,{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'seth_hideout', 'item_id': 'dune_sundial', 'location': 'treasure_room'}}
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
					'dialog_id': 'technique_you_got_it_coming'
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
					'npc_id': 'skill',
					'dialog_id': 'skill_that_guy_was_fast'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_haha_he_cant_wait_to_get_away'
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
					'npc_id': 'tech',
					'dialog_id': 'tech_knocking_back_a_few'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_good_idea_after_good_idea'
				}
			},
			{
				'event_type': 'award_money',
				'params': {
					'amount': '400'
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
					'npc_id': 'magic',
					'dialog_id': 'magic_to_sam_1'
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
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_to_sam_1'
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
					'npc_id': 'tech',
					'dialog_id': 'tech_interested_in_gear'
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
                    'npc_id': 'faith',
                    'dialog_id': 'faith_reacts_to_logger'
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
					'dialog_id': 'technique_diego_intro'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_interested_in_mira'
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
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_likes_cursed_couplet'
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