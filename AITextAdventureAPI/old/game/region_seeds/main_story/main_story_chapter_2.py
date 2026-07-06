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
		'name': 'The Demigorgons',
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
			"Chapter 2 - Contradiction is the root of all movement and life."
		]
	},
	{
		'npc_id': 'mira',
		'dialog_id': 'mira_ch2_intro',
		'dialog': [
			"Well now… you actually brought it.",
			"This cursed couplet is older than half the ruins in this region.",
			"Bound and sealed in this cursed form as it has been for so long.",
			"If you want this Grift Stone for Tess, you’ll need to do a little something extra for me first.",
            "Sweetheart, nothing rare comes cheap. And nothing powerful comes without a favor attached.",
            "Tess wants this stone? Fine. But if you want me to part with it, you’re going to earn it."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_deliver_couplet',
		'dialog': [
			"A riddle? Great. I came here to fight, not to think."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_deliver_couplet',
		'dialog': [
			"Fantastic. We’re running errands for smugglers now."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_deliver_couplet',
		'dialog': [
			"Riddles? Delicious. Let’s go shake the universe for a clue."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch2_deliver_couplet',
		'dialog': [
			"If this is the price, we pay it. Keep moving."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch2_deliver_couplet',
		'dialog': [
			"Knowledge is never wasted. Even when it comes from smugglers."
		]
	},
	{
		'npc_id': 'leera',
		'dialog_id': 'leera_ch2_couplet_lore',
		'dialog': [
                "Ah… you seek a riddle for Mira. Then listen carefully.",
                "Void and Existence. Absence and Presence. Chaos and order.",
                "What exists before it is understood… yet changes once it is named?",
                "Apparant in absence, but never there in presence. Some truths hum even when buried.",
            	"Return to Mira with this truth."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_after_leera',
		'dialog': [
			"Ohhh, metaphysics. My favorite flavor of nonsense."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch2_after_leera',
		'dialog': [
			"Void and Existence... These are deep questions..."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_after_leera',
		'dialog': [			
			"Riddles and philosophy. Wonderful."
		]
	},
	{
		'npc_id': 'mira',
		'dialog_id': 'mira_ch2_after_leera',
		'dialog': [
			"So Leera whispered her riddles at you.",
			"Void and Existence… Nature toward each other... Yes, that tracks.",
			"They've been dormant so long they must be reminded.",
			"You’ll need someone who deals in risks and rare odds, Juno",
			"Word is she recently acquired something interesting... Which I now share an interest in, the Resonance Shard"
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
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_after_juno',
		'dialog': [
			"A shard for a concoction? Classic black market barter. This should be entertaining."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_after_juno',
		'dialog': [
			"A resonance shard! Oh my, oh my — the possibilities..."
		]
	},
	{
		'npc_id': 'kess_thornwrite',
		'dialog_id': 'kess_ch2_request',
		'dialog': [
			"Juno wants *that* concoction? Oh stars… she’s bold.",
			"I can brew it, sure, but I’m missing a key ingredient.",
			"I sent someone to fetch it from a nearby ruin… but they never came back.",
			"If you bring me the item, I’ll finish the brew.",
			"Try not to die on me.  I don't want that on my head."
		]
	},
    {
      "npc_id": "technique",
      "dialog_id": "technique_ch2_post_demigorgon",
      "dialog": [
        "That thing hit like a freight. Keep your guard up — there might be more where it came from.",
        "I don't like how it bent the air around it. Feels... not natural."
      ]
    },
    {
      "npc_id": "magic",
      "dialog_id": "magic_ch2_post_demigorgon",
      "dialog": [
        "Strange hum, teeth like carved stone — deliciously alien.",
        "Kess Thornwrite would want a sample of that residue. Dangerous, yes, but informative."
      ]
    },
    {
      "npc_id": "tech",
      "dialog_id": "tech_ch2_post_demigorgon",
      "dialog": [
        "Saw scorch marks and odd sigils. Someone's been experimenting with things they don't understand.",
        "Don't touch the residue. Bag it and report it to someone who can handle it safely."
      ]
    },
	{
		"npc_id": "faith",
		"dialog_id": "faith_ch2_post_demigorgon",
		"dialog": [
			"That creature radiated a dark energy unlike anything I've seen.",
			"We must be cautious. Such forces can corrupt even the purest of hearts."
		]
	},
	{
		"npc_id": "skill",
		"dialog_id": "skill_ch2_post_demigorgon",
		"dialog": [
			"The way it moved... unnatural. Like it was part shadow, part solid.",
			"We need to stay vigilant. There could be more lurking in the darkness."
		]
	},
	{
		"npc_id": "technique",
		"dialog_id": "technique_ch2_random_appearance",
		"dialog": [
			"I still can't wrap my head around how we ended up here. One moment we were in our world celebrating, the next... this.",
			"This place has its own rules. We need to learn them fast if we're going to survive."
		]
	},
	{
		"npc_id": "magic",
		"dialog_id": "magic_ch2_random_appearance",
		"dialog": [
			"This place is falling apart, maybe our other friends are around too.",
			"Reality here is unstable. We need to find a way back before we get trapped."
		]
	},
	{
		"npc_id": "tech",
		"dialog_id": "tech_ch2_random_appearance",
		"dialog": [
			"This place is chaos... fights breaking out everywhere. We need to stay sharp.",
			"These ruptures in reality... they might be our ticket home, if we can figure them out."
		]
	},
	{
		"npc_id": "faith",
		"dialog_id": "faith_ch2_random_appearance",
		"dialog": [
			"Know that the gods are here with us, even in this strange land."
		]
	},
	{
		"npc_id": "skill",
		"dialog_id": "skill_ch2_random_appearance",
		"dialog": [
			"This world is unlike any I've seen. We need to adapt quickly."
		]
	},

	{
		'npc_id': 'kess_thornwrite',
		'dialog_id': 'kess_ch2_after_dungeon',
		'dialog': [
			"You found it!",
			"Perfect. Give me a moment...",
			"...",
			"...",
			"There. One dangerously potent concoction for Juno.",
			"Try not to inhale it. Or do. I’m not your mother."
		]
	},

	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_after_dungeon',
		'dialog': [
			"That ruin had teeth. Good fight. Good pay if anyone's counting."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch2_after_dungeon',
		'dialog': [
			"The shadows there were wrong. I don't miss them."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_after_dungeon',
		'dialog': [
			"Found something useful. Also, something that made me itch in a new way."
		]
	},

	{
		'npc_id': 'juno',
		'dialog_id': 'juno_ch2_after_kess',
		'dialog': [
			"Ahh… Kess actually delivered. Miracles do happen.",
			"Here. The resonance shard Leera spoke of.  Handle it carefully.",
			"Take it back to Mira. She’ll know how to use it."
		]
	},

	{
		'npc_id': 'mira',
		'dialog_id': 'mira_ch2_decoupling',
		'dialog': [
			"You brought the shard. Good.",
			"...",
			"...",
			"This is exactly what I needed. you came for the Grift Stone, and I keep my deals.",
			"As promised, here is the Grift Stone.  You can take the hyperway back to Tess for a small fee."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch2_decoupling',
		'dialog': [
			"Let’s return it quickly. Tess is waiting."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_decoupling',
		'dialog': [
			"Shards, smugglers, secrets… delicious chaos."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_decoupling',
		'dialog': [
			"About time we got something solid out of this."
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
			"You’re back! And you actually got the Grift Stone?",
			"Damn… you guys are full of surprises.",
			"Listen, word’s been spreading.  Someone in Highsteeple Crossing showed up out of nowhere... like you did.",
			"If you’re looking for answers, that’s your next lead."
		]
	},

	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch2_after_tess',
		'dialog': [ 
			"Another stranger showing up out of nowhere? Maybe we know them, Hahah!",
			"Hey if you ever need me again Tess, just holler."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch2_after_tess',
		'dialog': [
			"Someone materialized 'like you did'? How fascinating.",
			"Let's stay sharp though. We never know who we're chasing... or from where? ooowoooooo."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch2_after_tess',
		'dialog': [
			"It's highly likely that all 6 of us ended up here.",
			"This is deeply curious. We must investigate further."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch2_after_tess',
		'dialog': [
			"This is no coincidence. We must seek out this newcomer.",
			"Tess seems to think they are important. We should trust her judgment."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch2_after_tess',
		'dialog': [
			"The threads of fate are weaving a complex tapestry.",
			"Perhaps it is another of our friends from our own universe."
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
						"You're better off avoiding trouble. Stay out of the black market dealings."
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
						"words to the effect of k come back when the couplet is uncoupled"
					]
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_deliver_couplet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_deliver_couplet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_deliver_couplet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_deliver_couplet'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'faith',
					'dialog_id': 'faith_ch2_deliver_couplet'
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
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_after_leera'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'faith',
					'dialog_id': 'faith_ch2_after_leera'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_after_leera'
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
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_after_juno'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_after_juno'
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
			}
		]
	},
	# Task 6 - fetch ingredient dungeon
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
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'abandoned_ruin_ch2', 'item_id': 'grove_lattice', 'location': 'treasure_room'}},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'abandoned_ruin_ch2', 'item_id': 'coreforge_shard', 'location': 'treasure_room'}},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'the_demigorgon',
					'location': None
				}
			},
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
					'dialog_id': 'technique_ch2_after_dungeon'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_after_dungeon'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_after_dungeon'
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
					'npc_id': 'faith',
					'dialog_id': 'faith_ch2_post_demigorgon'
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
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch2_random_appearance'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_random_appearance'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_random_appearance'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'faith',
					'dialog_id': 'faith_ch2_random_appearance'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_random_appearance'
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
					'npc_id': 'faith',
					'dialog_id': 'faith_ch2_decoupling'
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
					'dialog_id': 'technique_ch2_after_tess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch2_after_tess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch2_after_tess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'faith',
					'dialog_id': 'faith_ch2_after_tess'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch2_after_tess'
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