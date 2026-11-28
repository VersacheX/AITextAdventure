ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
	#### CH 2 NPCS
	{
		'npc_id': 'mira',
		'name': 'Mira',
		'description': (
			'A cunning and elusive black market dealer/smuggler.'
			"  Mira specializes in rare and illegal artifacts."
			"  She is known for her sharp negotiation skills and ability to evade capture."
			"  She is cold, calculating, and can be incredibly seductive."
		),
		"psychology": {
			"mbti": "INTJ",
			"dominant": "Ni — Sees hidden patterns in artifacts, curses, and people. She anticipates motives and outcomes long before others notice anything.",
			"auxiliary": "Te — Efficient, ruthless, and transactional. She negotiates with precision and expects competence from everyone she deals with.",
			"tertiary": "Fi — Holds private emotional convictions and personal boundaries. Her seductive charm is controlled, never impulsive.",
			"inferior": "Se — Under stress, she becomes hypersensitive to danger or acts impulsively, abandoning her usual icy composure."
		},
        "enneagram": {
          "enneagram_type": "8w7",
          "core_fear": "Being controlled or harmed by others.",
          "core_desire": "To be in control of her own life and destiny.",
          "defense_mechanism": "Denial — Projects an image of untouchable competence and control, denying any vulnerability or dependence on others.",
          "stress_line": "Moves to Type 5 — Becomes secretive, paranoid, and withdrawn when she feels her control slipping.",
          "growth_line": "Moves to Type 2 — Uses her power and resources to protect and empower those she deems worthy, showing a hidden capacity for loyalty.",
          "instinctual_variant": "sx/sp — Forms intense, controlling one-on-one alliances, using seduction and power to ensure her security."
        },
		'image': 'npcs:mira1'
	},
	{
		'npc_id': 'leera',
		'name': 'Leera',
		'description': (
			'A poetic lorekeeper and archivist with a mystical aura.'
			"  Leera possesses a soft voice and a sharp mind."
			"  She often speaks in riddles and metaphors, weaving tales of ancient knowledge and forgotten lore."
		),
		"psychology": {
			"mbti": "INFJ",
			"dominant": "Ni — Speaks in symbols, riddles, and layered meaning. She perceives the deeper nature of artifacts and cosmic forces.",
			"auxiliary": "Fe — Communicates gently, guiding others with emotional clarity and calm presence.",
			"tertiary": "Ti — Quietly analyzes ancient lore and metaphysical structures, forming elegant internal theories.",
			"inferior": "Se — Overwhelmed by chaotic or intense sensory environments; retreats inward when overstimulated."
		},
        "enneagram": {
          "enneagram_type": "4w5",
          "core_fear": "Having no identity or personal significance.",
          "core_desire": "To find herself and her significance; to create an identity.",
          "defense_mechanism": "Introjection — Absorbs the mystical and poetic qualities of the lore she studies, making it part of her unique identity.",
          "stress_line": "Moves to Type 2 — Becomes overly helpful and clingy when she feels insignificant or misunderstood.",
          "growth_line": "Moves to Type 1 — Becomes more objective and principled, acting on her wisdom rather than just feeling it.",
          "instinctual_variant": "sp/sx — Protects her unique identity by withdrawing into her world of lore, sharing it only in intense, meaningful interactions."
        },
		'image': 'npcs:leera1'
	},
	{
		'npc_id': 'juno',
		'name': 'Juno',
		'description': (
			'A smooth-talking ex-noble turned professional gambler.'
			"  Juno is known for her calculating mind and ability to read people."
			"  She always seems to have a smile on her face, but there's a sharp edge beneath the surface."
		),
		"psychology": {
			"mbti": "ENTP",
			"dominant": "Ne — Constantly scanning for angles, opportunities, and tells. She thrives on unpredictability and risk.",
			"auxiliary": "Ti — Calculates odds, motives, and strategies with surgical precision beneath her playful exterior.",
			"tertiary": "Fe — Uses charm, smiles, and social finesse to manipulate or disarm opponents.",
			"inferior": "Si — Under stress, becomes fixated on past losses or mistakes, losing her usual flexibility."
		},
        "enneagram": {
          "enneagram_type": "3w4",
          "core_fear": "Being worthless or without inherent value.",
          "core_desire": "To feel valuable and worthwhile.",
          "defense_mechanism": "Identification — Adapts her persona to be the charming, successful gambler everyone admires, masking her fear of failure behind a winning smile.",
          "stress_line": "Moves to Type 9 — Becomes disengaged and apathetic when faced with failure, losing her drive.",
          "growth_line": "Moves to Type 6 — Becomes more cooperative and committed to others, finding value beyond her own success.",
          "instinctual_variant": "so/sx — Craves admiration and status within her social circle, using her charm to win high-stakes games and relationships."
        },
		'image': 'npcs:juno1'
	},
	{
		'npc_id': 'kess_thornwrite',
		'name': 'Kess Thornwrite',
		'description': (
			#Apothecary specializing in illegal brews and mood altering potions
			#cheerful/ nosy 
			'An eccentric apothecary specializing in illegal brews and mood-altering potions.'
			"  Kess is known for his cheerful demeanor and insatiable curiosity."
			"  He has a knack for concocting unique and potent mixtures, often pushing the boundaries of legality."
		),
		"psychology": {
			"mbti": "ENFP",
			"dominant": "Ne — Explores bizarre ideas, experimental brews, and unpredictable combinations. His curiosity is endless and chaotic.",
			"auxiliary": "Fi — Makes decisions based on personal ethics and emotional impulses. He genuinely cares but in unconventional ways.",
			"tertiary": "Te — When focused, he becomes surprisingly organized and efficient in his brewing process.",
			"inferior": "Si — Forgets details, repeats mistakes, or becomes overwhelmed by routine. Under stress, he fixates on past failures."
		},
        "enneagram": {
          "enneagram_type": "7w6",
          "core_fear": "Being deprived, in pain, or bored.",
          "core_desire": "To be satisfied and happy, to have a life full of stimulating experiences.",
          "defense_mechanism": "Rationalization — Frames his dangerous and illegal brewing as exciting experiments, avoiding the potential negative consequences.",
          "stress_line": "Moves to Type 1 — Becomes rigid and critical when his experiments fail or his freedom is curtailed.",
          "growth_line": "Moves to Type 5 — Becomes more focused and knowledgeable, turning his chaotic curiosity into deep expertise.",
          "instinctual_variant": "so/sp — Engages socially with cheerful energy, sharing his creations to generate excitement and secure his resources."
        },
		'image': 'npcs:kess1'
	},
	{
		'npc_id': 'the_demigorgon',
		'name': 'The Demigorgon',
		'description': (
			#otherworldy being
			'An otherworldly being of immense power and mystery.'
			"  The Demigorgon is shrouded in enigma, with motives and intentions that are often inscrutable."
		),
		"psychology": {
			"mbti": "INTJ",
			"dominant": "Ni — Perceives reality through cosmic patterns and metaphysical structures. Its vision extends beyond linear time.",
			"auxiliary": "Te — Acts with cold, efficient purpose. Its actions follow an internal logic incomprehensible to mortals.",
			"tertiary": "Fi — Displays alien forms of value or judgment, often interpreted as malice or indifference.",
			"inferior": "Se — When manifesting physically, its presence distorts the environment, as if sensory reality strains under its existence."
		},
        "enneagram": {
          "enneagram_type": "5w4",
          "core_fear": "Being useless, incapable, or overwhelmed by the world.",
          "core_desire": "To be competent and understand the universe.",
          "defense_mechanism": "Isolation — Detaches from the physical world to observe and understand its underlying principles from a distance.",
          "stress_line": "Moves to Type 7 — Its actions become scattered and chaotic when its understanding is challenged.",
          "growth_line": "Moves to Type 8 — Manifests its knowledge with decisive, world-altering power.",
          "instinctual_variant": "sp/sx — A being of pure observation and knowledge, interacting with the world only through intense, focused bursts of energy."
        },
		'image': 'bosses:demigorgon1'
	}


]

NPC_DIALOG = [
	### CHAPTER 2 DIALOGS
    {
		'npc_id': None,
		'dialog_id': 'ch2_narrator_contradiction',
		'dialog': [
			"Chapter 2",
			"Contradiction is the root of all movement and vitality. - Hegel"
		]
	},
	{
		'npc_id': 'mira',
		'dialog_id': 'mira_ch2_intro',
		'dialog': [
			"Well now... you actually brought it.",
			"This couplet is older than half the ruins in this region. Two things, bound into one, and cursed to stay that way.",
			"You want the Grift Stone. Sweetheart, nothing rare comes cheap, and nothing powerful comes without a favor attached.",
			"Get this curse read. Leera, the lorekeeper at the @inn, knows the old bindings.",
			"Bring me what she tells you, and we'll talk.",
			"...And you've lost someone. Everyone who comes to me has. Do my favor, and maybe I'll hear something."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_mira_couplet',
		'dialog': [
			"A curse? Great. I came here to fight, not to read.",
			"Fine. Lorekeeper. Inn. Let's go."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_mira_couplet',
		'dialog': [
			"Fantastic. We're running errands for smugglers now.",
			"Leera, at the inn. She has the information."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_mira_couplet',
		'dialog': [
			"A cursed antique and a mysterious lorekeeper? This is the best errand yet.",
			"Inn! Leera! Go!"
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch2_mira_couplet',
		'dialog': [
			"Leera. Inn."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch2_mira_couplet',
		'dialog': [
			"Something bound against its will... I felt it when we carried it.",
			"Let's find Leera at the inn."
		]
	},
	{
		'npc_id': 'leera',
		'dialog_id': 'leera_ch2_couplet_lore',
		'dialog': [
				"Ah... you carry Mira's couplet. Then listen carefully.",
				"Void and Existence. Absence and Presence. Chaos and order.",
				"What exists before it is understood... yet changes once it is named?",
				"Apparent in absence, never there in presence. Some truths hum even when buried.",
				"Two things bound this long forget they were ever two. They must be reminded.",
				"Return to Mira with this truth."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_leera',
		'dialog': [
			"I understood about half of that.",
			"Mira can have the other half. Back to the bar."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch2_leera',
		'dialog': [
			"Void and Existence... two halves that forgot each other.",
			"Mira will know what it means. Let's return to her."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_leera',
		'dialog': [
			"Ohhh, metaphysics. My favorite flavor of nonsense.",
			"Back to Mira, before I start answering the riddle out loud."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_leera',
		'dialog': [			
			"A riddle about something that hums. That's a frequency.",
			"Report back to Mira."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch2_leera',
		'dialog': [
			"Riddle's for Mira. Back to the bar."
		]
	},
	{
		'npc_id': 'mira',
		'dialog_id': 'mira_ch2_after_leera',
		'dialog': [
			"So Leera whispered her riddles at you.",
			"Void and Existence, bound so long they've forgotten they were ever two. Yes, that tracks.",
			"Something that hums can remind them. A Resonance Shard.",
			"Juno has one. She deals in risk and rare odds, and she just won it.",
			"Find her at the item shop. And don't let her talk you into a game."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_mira_riddle',
		'dialog': [
			"A gambler. Great. I hate cards.",
			"Item shop. Let's get this shard."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch2_mira_riddle',
		'dialog': [
			"Juno. Item shop. Don't gamble."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_mira_riddle',
		'dialog': [
			"Dependency chain: Juno's shard, Mira's curse, Tess's stone.",
			"Item shop."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch2_mira_riddle',
		'dialog': [
			"A shard to remind them what they were. There's something gentle in that.",
			"Let's find Juno at the item shop."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_mira_riddle',
		'dialog': [
			"A gambler with a magic rock? I am absolutely playing her game.",
			"...Fine. Item shop."
		]
	},
	{
		'npc_id': 'juno',
		'dialog_id': 'juno_ch2_intro',
		'dialog': [
			"Mira sent you? That means trouble or profit. Usually both.",
			"Yes, I have what you’re looking for, but I’m not giving it away for free.",
			"Kess owes me a concoction. Something volatile, something contraband.",
			"Bring it to me, and the shard is yours."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_juno',
		'dialog': [
			"We do a favor so we can do a favor so we can do a favor.",
			"Kess. Weapon shop. Whatever."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch2_juno',
		'dialog': [
			"Contraband... I don't love it. But we need that shard.",
			"Let's find Kess."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_juno',
		'dialog': [
			"A volatile, contraband concoction? Now we're talking.",
			"Weapon shop! Kess!"
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_juno',
		'dialog': [
			"A shard for a concoction. Classic black market barter.",
			"Kess Thornwrite, at the weapon shop."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch2_juno',
		'dialog': [
			"Kess. Weapon shop."
		]
	},
	{
		'npc_id': 'kess_thornwrite',
		'dialog_id': 'kess_ch2_request',
		'dialog': [
			"Juno wants *that* concoction? Oh stars... she's bold.",
			"I can brew it, sure, but I'm missing a key ingredient.",
			"I sent a courier to fetch it from a ruin outside the city. New in town, said they needed the coin, didn't ask questions.",
			"They never came back.",
			"Bring me the ingredient, and bring them back too if you can. Try not to die on me. I don't want that on my head."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_after_kess',
		'dialog': [
			"New in town, needs coin, doesn't ask questions? ...That sounds like one of us.",
			"Ruin outside the city. Let's go."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_after_kess',
		'dialog': [
			"A volatile brew, a spooky ruin and a missing courier? I already like him.",
			"To the ruin!"
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_after_kess',
		'dialog': [
			"A stranger with no history taking odd jobs. We fit the same profile.",
			"The ruin outside the city. Move."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch2_after_kess',
		'dialog': [
			"Someone new to this world, alone in a ruin... we have to hurry.",
			"The ruin outside the city."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch2_after_kess',
		'dialog': [
			"Courier's new here. Like us.",
			"Ruin. Now."
		]
	},
	{
		"npc_id": "technique",
		"dialog_id": "technique_ch2_demigorgon_meet",
		"dialog": [
			"Oooooh. Looks like we bit off more than we can chew.",
			"Good. I'm hungry."
		]
	},
	{
		"npc_id": "spirit",
		"dialog_id": "spirit_ch2_demigorgon_meet",
		"dialog": [
			"Stay close to me. All of us. I won't lose anyone again."
		]
	},
	{
		"npc_id": "magic",
		"dialog_id": "magic_ch2_demigorgon_meet",
		"dialog": [
			"It's big, it's ugly, and it's between us and a reunion. Light it up!"
		]
	},
	{
		"npc_id": "tech",
		"dialog_id": "tech_ch2_demigorgon_meet",
		"dialog": [
			"Unknown entity. High threat. Focus fire."
		]
	},
	{
		"npc_id": "skill",
		"dialog_id": "skill_ch2_demigorgon_meet",
		"dialog": [
			"Together. Now."
		]
	},
	{
	  "npc_id": "technique",
	  "dialog_id": "technique_ch2_post_demigorgon",
	  "dialog": [
		"That thing hit like a freight train. And it bent the air. Not natural.",
		"But we're four now. One down, two to go. Let's get the weed back to Kess."
	  ]
	},
	{
	  "npc_id": "magic",
	  "dialog_id": "magic_ch2_post_demigorgon",
	  "dialog": [
		"Strange hum, teeth like carved stone. Deliciously alien.",
		"And look at us! Half a reunion! The other two are out there somewhere. To Kess!"
	  ]
	},
	{
	  "npc_id": "tech",
	  "dialog_id": "tech_ch2_post_demigorgon",
	  "dialog": [
		"Scorch marks, odd sigils. Someone has been experimenting with things they don't understand.",
		"Data point: we all landed in this world, alive. That makes the other two likely. Back to Kess."
	  ]
	},
	{
		"npc_id": "spirit",
		"dialog_id": "spirit_ch2_post_demigorgon",
		"dialog": [
			"That creature radiated something dark. Such forces can corrupt even the purest hearts.",
			"But we found each other. If we survived this, the others can too. Let's return to Kess."
		]
	},
	{
		"npc_id": "skill",
		"dialog_id": "skill_ch2_post_demigorgon",
		"dialog": [
			"It moved like shadow pretending to be solid.",
			"We found one. We'll find the rest. Kess first."
		]
	},

	{
		'npc_id': 'kess_thornwrite',
		'dialog_id': 'kess_ch2_after_dungeon',
		'dialog': [
			"You found it! And my courier, alive! Oh, stars, that's a weight off.",
			"Keep the advance, I'm not asking for it back.",
			"Give me a moment...",
			"...",
			"...",
			"There. One dangerously potent concoction for Juno.",
			"Try not to inhale it. Or do. I'm not your mother."
		]
	},

	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_after_ruin',
		'dialog': [
			"That ruin had teeth. Good fight.",
			"Now let's get this stuff to Juno before it explodes."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch2_after_ruin',
		'dialog': [
			"Thank you, Kess, for worrying about them.",
			"Let's bring this to Juno."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_after_ruin',
		'dialog': [
			"He said 'try not to inhale it' like it's a suggestion.",
			"Juno! Quickly! Before I get curious."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_after_ruin',
		'dialog': [
			"Volatile compound, unlabeled, carried by hand. Excellent safety culture.",
			"To Juno."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch2_after_ruin',
		'dialog': [
			"Concoction. Juno. Careful."
		]
	},

	{
		'npc_id': 'juno',
		'dialog_id': 'juno_ch2_after_kess',
		'dialog': [
			"Ahh… Kess actually delivered. Miracles do happen.",
			"Here. The Resonance Shard Mira's been after. Handle it carefully.",
			"Take it back to Mira. She’ll know how to use it."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_juno_ch2_after_kess',
		'dialog': [
			"Finally. One less favor hanging over our heads."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_juno_ch2_after_kess',
		'dialog': [
			"Resonance Shard acquired. Let’s get it to Mira before it starts doing something unfortunate."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_juno_ch2_after_kess',
		'dialog': [
			"Shiny, dangerous, and slightly illegal. Perfect."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_juno_ch2_after_kess',
		'dialog': [
			"May this shard bring the balance that was promised."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_juno_ch2_after_kess',
		'dialog': [
			"Shard in hand. Back to Mira."
		]
	},
	{
		'npc_id': 'mira',
		'dialog_id': 'mira_ch2_decoupling',
		'dialog': [
			"You brought the shard. Good.",
			"...",
			"(The shard hums. The couplet shudders, and splits in two.)",
			"Void... and Existence. Two bracelets, reminded of what they were.",
			"These stay with me. You came for the Grift Stone, and I keep my deals.",
			"Take the Ṣ hyperway back to Tess. It's a small fee. Cheaper than walking."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch2_decoupling',
		'dialog': [
			"Let’s return it quickly. Tess is waiting."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_decoupling',
		'dialog': [
			"Two magic bracelets out of one curse, and she keeps both? Rude.",
			"...Hyperway! Back to Tess!"
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_decoupling',
		'dialog': [
			"About time we got something solid out of this.",
			"Hyperway. Tess. Let's go."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch2_decoupling',
		'dialog': [
			"We did the work. Let's see where this leads."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_decoupling',
		'dialog': [
			"Grift Stone secured. Now, back to Tess — and whatever mess follows."
		]
	},
	{
		'npc_id': 'tess',
		'dialog_id': 'tess_ch2_return',
		'dialog': [
			"You're back! And you actually got the Grift Stone?",
			"Damn... you guys are full of surprises.",
			"...And you found one of your strays! Told you this city talks.",
			"We promised to keep our ears open, and we did. Someone in Highsteeple Crossing showed up out of nowhere... like you did.",
			"Sam and I are hearing other whispers too: weird arrivals, old relic routes, too much money moving too fast.",
			"We'll keep pulling threads on our side. If you're looking for answers, Highsteeple is your next lead."
		]
	},

	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_tess_lead',
		'dialog': [ 
			"Another one fell out of the sky? Two left. Could be one of ours.",
			"Highsteeple Crossing. Let's go. And Tess, if you ever need me, just holler."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_tess_lead',
		'dialog': [
			"Someone materialized 'like you did'? Oooh, a mystery guest!",
			"Highsteeple Crossing! Ooowoooooo!"
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_tess_lead',
		'dialog': [
			"Six of us were in that bar. Four are accounted for. The probability that this is one of ours is high.",
			"Highsteeple Crossing."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch2_tess_lead',
		'dialog': [
			"Someone alone and confused in Highsteeple... I know how that feels.",
			"We have to go to them."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch2_tess_lead',
		'dialog': [
			"Two still missing.",
			"Highsteeple. Now."
		]
	},
	{
		'npc_id': 'diego',
		'dialog_id': 'diego_ch2_monster_hunter',
		'dialog': [
			"So the rumors are true. You went toe to toe with one of those things crawling out of the ruins and walked away.",
			"I've seen a lot of hardened killers in my time. Most of them don't come back from a hunt like that.",
			"Word travels fast in my circles. People are already asking who put that beast in the ground.",
			"Take this. Consider it a mark of the trade — you're a Monster Hunter now, whether you asked for it or not.",
			"Keep your ears open. Things are only going to get uglier from here, and I know how to find the work that pays."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_monster_hunter',
		'dialog': [
			"A title! Oh, I do love a good title. Moxie the Monster Hunter — no, no, all of us, obviously.",
			"Ooooh, does this mean more delicious beasties to poke and prod? Yes please!"
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch2_monster_hunter',
		'dialog': [
			"To hunt these creatures is a heavy burden, not a trophy.",
			"Still... if it protects the innocent from what festers in those ruins, then it is a duty I will bear gladly."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_monster_hunter',
		'dialog': [
			"Monster Hunter, huh? Now that's a title I can respect.",
			"Point me at the next one, Diego. I'm just getting warmed up."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch2_monster_hunter',
		'dialog': [
			"A hunter earns the name in the field, not from a stranger's hand.",
			"But the work is honest. I'll take it."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_monster_hunter',
		'dialog': [
			"So we kill something horrifying and get a shiny badge for it. Efficient.",
			"Fine. If there's a broker keeping tabs on the payouts, I want to see the numbers."
		]
	}
]

TASKS = [
    #### CHAPTER 2 TASKS
	# Task 1 - deliver cursed_couplet
	{
		'task_id': 'main_story_ch_2_deliver_cursed_couplet_to_mira',
		'type': 'deliver',
		'item_id': 'cursed_couplet',
		'to_type': 'npc',
		'to_id': 'mira',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'tess',
					'standing_text': [
						"Find Mira in the city bar. She deals in rare and illegal artifacts."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sam',
					'standing_text': [
						"Keep your nose clean. The city guard cracks down hard."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'brawn',
					'standing_text': [
						"If you ever find anything nice out there, you should bring it by and show it off."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'diego',
					'standing_text': [
						"Mira's a shark. Smile, trade, and count your fingers after."
					]
				}
			},
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'oren'
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'mira',
					'location': 'region_city_bar'
				}
			},
			{
				'event_type': 'set_npc_met',
				'params': {
					'npc_id': 'mira'
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'leera',
					'location': 'region_city_inn'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'leera',
					'standing_text': [
						"Knowledge is the key to unbinding what is bound."
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'juno',
					'location': 'region_city_shopitems'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'juno',
					'standing_text': [
						'You can be rich every day of your life and stand in one place.',
						'If you know how to play the odds, risk is just a lesson in patience.'
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'kess_thornwrite',
					'location': 'region_city_shopweapons'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'kess_thornwrite',
					'standing_text': [
						"Looking for something to take the edge off? I might have just the thing."
					]
				}
			},
            {
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': None,
					'dialog_id': 'ch2_narrator_contradiction'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'mira',
					'dialog_id': 'mira_ch2_intro'
				}
			},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'cursed_couplet'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"Leera at the @inn can read the couplet's curse. Come back when you know what it needs."
					]
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_mira_couplet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch2_mira_couplet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_mira_couplet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_mira_couplet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_mira_couplet'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_2_uncouple_couplet'
				}
			}
		]
	},
	# Task 2 - uncouple cursed couplet
	{
		'task_id': 'main_story_ch_2_uncouple_couplet',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'leera',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'leera',
					'dialog_id': 'leera_ch2_couplet_lore'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'leera',
					'standing_text': [
						"Return to Mira with this truth. She will know what must come next."
					]
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_leera'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch2_leera'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_leera'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_leera'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_leera'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_2_return_to_mira_after_leera'
				}
			}
		]
	},
	# Task 3 - return to mira after leera
	{
		'task_id': 'main_story_ch_2_return_to_mira_after_leera',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'mira',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'mira',
					'dialog_id': 'mira_ch2_after_leera'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_mira_riddle'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_mira_riddle'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_mira_riddle'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_mira_riddle'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch2_mira_riddle'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"Find Juno. Word is she recently acquired something… interesting."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'leera',
					'standing_text': [
						"The couplet’s truth has been spoken. Your path now winds through risk and chance."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_2_meet_juno'
				}
			}
		]
	},
    # Task 4 - meet juno
	{
		'task_id': 'main_story_ch_2_meet_juno',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'juno',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"Juno's playing her games again. Bring her what she wants and don't get swindled."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'juno',
					'dialog_id': 'juno_ch2_intro'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_juno'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch2_juno'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_juno'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_juno'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_juno'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'juno',
					'standing_text': [
						"Bring me that concoction Kess owes me, and the shard is yours."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_2_meet_kess_thornwrite'
				}
			}
		]
	},
    # Task 5 - meet kess
	{
		'task_id': 'main_story_ch_2_meet_kess_thornwrite',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'kess_thornwrite',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'kess_thornwrite',
					'dialog_id': 'kess_ch2_request'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_after_kess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_after_kess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_after_kess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch2_after_kess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_after_kess'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'kess_thornwrite',
					'standing_text': [
						"Bring me the missing ingredient from the nearby ruin, and I'll finish the brew."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_2_deliver_rare_ingredient'
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'the_demigorgon',
					'location': None
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'the_demigorgon',
					'standing_text': [
						"Grrrr. Arghhh!"
					]
				}
			}
		]
	},
	
	{
		'task_id': 'main_story_ch_2_meet_demigorgon',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'the_demigorgon',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'player_character_join',
				'params': {
					'dialog_id': 'ch2_add_pc'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_demigorgon_meet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch2_demigorgon_meet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_demigorgon_meet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_demigorgon_meet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_demigorgon_meet'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'the_demigorgon',
					'standing_text': [
						"Grrrr. Arghhh!"
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_2_defeat_demigorgon'
				}
			}
		],
	},
	# Task 4: defeat The Demigorgon
	{
		'task_id': 'main_story_ch_2_defeat_demigorgon',
        'type': 'defeat',
        'to_type': 'mob',
		'to_id': 'demigorgon_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat',
				'params': {
					'boss_mob_id': 'demigorgon_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'the_demigorgon'
				}
			},
			{
			    'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_post_demigorgon'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_post_demigorgon'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_post_demigorgon'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch2_post_demigorgon'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_post_demigorgon'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'demigorgon_tooth'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'rare_ingredient_ch2'
				}
			}
		]
	},
	{
		'task_id': 'main_story_ch_2_deliver_rare_ingredient',
		'type': 'deliver',
		'item_id': 'rare_ingredient_ch2',
		'to_type': 'npc',
		'to_id': 'kess_thornwrite',
		'task_acquire_events': [
			{
				'event_type': 'create_dungeon',
				'params': {
					'dungeon_id': 'abandoned_ruin_ch2',
					'location': 'region_open_area'
				}
			},
			#{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'abandoned_ruin_ch2', 'item_id': 'grove_lattice', 'location': 'treasure_room'}},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'abandoned_ruin_ch2', 'item_id': 'veil_memory_leaf', 'location': 'treasure_room'}},
			#{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'abandoned_ruin_ch2', 'item_id': 'coreforge_shard', 'location': 'treasure_room'}},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_2_meet_demigorgon' 
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'kess_thornwrite',
					'dialog_id': 'kess_ch2_after_dungeon'
				}
			},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'rare_ingredient_ch2'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_after_ruin'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch2_after_ruin'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_after_ruin'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_after_ruin'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_after_ruin'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'kess_thornwrite',
					'standing_text': [
						"Take the concoction to Juno. She's expecting it."
					]
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'volatile_concoction_ch2'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_2_return_to_juno_after_kess'
				}
			}
		]
	},
    # Task 7 - return to juno
	{
		'task_id': 'main_story_ch_2_return_to_juno_after_kess',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'juno',
		'item_id': 'volatile_concoction_ch2',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'juno',
					'dialog_id': 'juno_ch2_after_kess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_juno_ch2_after_kess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_juno_ch2_after_kess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_juno_ch2_after_kess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_juno_ch2_after_kess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_juno_ch2_after_kess'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'juno',
					'standing_text': [
						"Take the shard back to Mira. She'll know how to use it."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'kess_thornwrite',
					'standing_text': [
						"That ruin was dangerous. Be careful with what you bring back next time."
					]
				}
			},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'volatile_concoction_ch2'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'resonance_shard_ch2'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_2_return_to_mira_for_decoupling'
				}
			}
		]
	},
    # Task 8 - return to mira
	{
		'task_id': 'main_story_ch_2_return_to_mira_for_decoupling',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'mira',
		'item_id': 'resonance_shard_ch2',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'mira',
					'dialog_id': 'mira_ch2_decoupling'
				}
			},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'resonance_shard_ch2'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'grift_stone'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch2_decoupling'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_decoupling'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_decoupling'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_decoupling'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_decoupling'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'mira',
					'standing_text': [
						"The curse is broken. The couplet is now two bracelets: The Bracelet of Void… and the Bracelet of Existence."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'leera',
					'standing_text': [
						"The bindings are undone. May the freed spirits find peace."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'juno',
					'standing_text': [
						"Risk and chance have their rewards. Well done."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_2_return_to_tess_with_grift_stone'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'monster_hunter'
				}
			}
		]
	},
	# Monster Hunter - meet Diego
	{
		'task_id': 'monster_hunter',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'diego',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'diego',
					'dialog_id': 'diego_ch2_monster_hunter'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'monster_hunter'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_monster_hunter'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch2_monster_hunter'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_monster_hunter'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_monster_hunter'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_monster_hunter'
				}
			}
		]
	},
	# Task 9 - return to tess
	{
		'task_id': 'main_story_ch_2_return_to_tess_with_grift_stone',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'tess',
		'item_id': 'grift_stone',
		'task_acquire_events': [
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sam',
					'standing_text': [
						"Tess is eager to see what you've brought back. Don't keep her waiting."
					]
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'tess',
					'dialog_id': 'tess_ch2_return'
				}
			},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'grift_stone'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_tess_lead'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_tess_lead'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_tess_lead'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'spirit',
					'dialog_id': 'spirit_ch2_tess_lead'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_tess_lead'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'tess',
					'standing_text': [
						"Thanks for helping with the Grift Stone. You actually have some talent."
					]
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sam',
					'standing_text': [
						"Someone in Highsteeple Crossing showed up out of nowhere… like you did. If you’re looking for answers, that’s your next lead."
					]
				}
			},
			{
				'event_type': 'advance_chapter'
			}
		]
	}
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_2',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
    }