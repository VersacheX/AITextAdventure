CHARACTER_CLASS_MAP = {
    'technique': 'Chock',
    'spirit': 'Kaera',
    'magic': 'Moxie',
    'tech': 'Kade',
    'skill': 'Poise',
}

PLAYER_NPCS = [
    {
        "npc_id": "technique",
        "name": "Chock",
        "description": "A skilled warrior known for his brutal force and unwavering discipline. Chock is rugged, ornery, and sometimes rude, but his heart is in the right place. He seeks to master his enemies through sheer strength and tactical prowess. He is calm under pressure and values honor above all else.",
		"theme_song": "Hero (instrumental), skillet | Orion, Metallica",
        "psychology": {
            "mbti": "ESTJ",
            "dominant": "Te — Acts decisively and forcefully. He evaluates situations quickly and executes without hesitation, naturally taking command.",
            "auxiliary": "Si — Relies on discipline, training, and proven methods. He respects structure, routines, and personal codes of honor.",
            "tertiary": "Ne — Occasionally flashes creative tactical ideas in combat when standard approaches fail.",
            "inferior": "Fi — Holds deep internal values, but rarely expresses them. Under heavy stress, he becomes uncharacteristically emotional or rigid."
        },
        "enneagram": {
          "enneagram_type": "8w9",
          "core_fear": "Being controlled or harmed by others.",
          "core_desire": "To protect himself (and his inner circle) by controlling his own life and destiny.",
          "defense_mechanism": "Denial — Pushes away vulnerability and weakness, insisting he is always in control and unaffected by threats.",
          "stress_line": "Moves to Type 5 — Withdraws, becomes secretive, and fears the worst, hoarding resources.",
          "growth_line": "Moves to Type 2 — Becomes more compassionate, using his strength to protect and empower others rather than just control.",
          "instinctual_variant": "sp/sx — Focused on self-preservation, control over his environment, and intense one-on-one loyalties."
        },
        "shadow_psychology": {
            "mbti": "ESTJ-shadow",
            "dominant": "Te — Becomes tyrannical and domineering; 'My way or the highway' turns into 'Obey or be crushed'.",
            "auxiliary": "Si — Obsessively clings to past failures and betrayals, becoming paranoid and vengeful.",
            "tertiary": "Ne — Twisted creativity; sees threats and conspiracies in every possibility.",
            "inferior": "Fi — Explosive, self-righteous rage; moral code becomes hypocritical and violently enforced."
        },
        'image': 'chock1.jpeg',
		'song_id': 'hero_instrumental_skillet'
    },
    {
        "npc_id": "spirit",
        "name": "Kaera",
        "description": (
			"A devout cleric with a deep connection to the divine. Kaera serves as the steadfast protector and emotional anchor of the group."
			" Her compassion and healing abilities make her a quiet beacon of hope, and she possesses a calm, reliable presence."
		),
		"theme_song": "Lofticries, Purity Ring AND Never Ending Circles, CHVRCHES",
        "psychology": {
            "mbti": "ISFJ",
            "dominant": "Si — Deeply attuned to past experiences, traditions, and the concrete needs of her companions. She remembers every promise and every wound.",
            "auxiliary": "Fe — Provides emotional support and creates harmony. She instinctively senses when someone is struggling and offers quiet care.",
            "tertiary": "Ti — Analyzes moral and spiritual matters with sharp internal precision.",
            "inferior": "Ne — Under extreme stress, she becomes overwhelmed by too many possibilities and fears sudden chaotic change."
        },
        "enneagram": {
          "enneagram_type": "2w1",
          "core_fear": "Being unwanted or unworthy of love.",
          "core_desire": "To be loved and needed.",
          "defense_mechanism": "Repression — Denies her own needs and feelings to focus entirely on helping others, believing her worth comes from her service.",
          "stress_line": "Moves to Type 8 — Becomes controlling and aggressive when her help is rejected or she feels unappreciated.",
          "growth_line": "Moves to Type 4 — Becomes more self-aware and able to acknowledge her own needs and complex emotions.",
          "instinctual_variant": "so/sp — Socially focused on the group's well-being, creating harmony and ensuring everyone is cared for."
        },
        "shadow_psychology": {
            "mbti": "ISFJ-shadow",
            "dominant": "Si — Becomes trapped in traumatic memories; endlessly replays past failures and losses.",
            "auxiliary": "Fe — Weaponized guilt and obligation; manipulates others through emotional blackmail and martyrdom.",
            "tertiary": "Ti — Cold, critical over-analysis; becomes harshly judgmental of everyone’s ‘flaws’ and ‘sins’.",
            "inferior": "Ne — Paralyzing catastrophic thinking; sees every small change as the beginning of total collapse."
        },
        'image': 'kaera1.jpeg',
		'song_id': 'never_ending_circles_chvrches'
    },
    {
        "npc_id": "magic",
        "name": "Moxie",
        "description": "A brilliant sorcerer with an insatiable curiosity for the arcane and a mischievous streak. Moxie is constantly seeking new spells and magical knowledge to expand her power. Her quick wit, resourcefulness, and playful side make her both dangerous and entertaining.",
		"theme_song": "Bubblegum Bitch, Marina",
        "psychology": {
            "mbti": "ENTP",
            "dominant": "Ne — Constantly generating ideas, possibilities, and wild magical experiments. She thrives on novelty and unpredictability.",
            "auxiliary": "Ti — Breaks down magical systems with sharp logical precision. Her mischief is usually calculated.",
            "tertiary": "Fe — Uses charm and humor to influence others. She can be surprisingly warm when she chooses.",
            "inferior": "Si — Struggles with routine and repetition. Under stress, she becomes fixated on past mistakes or overly rigid details."
        },
        "enneagram": {
          "enneagram_type": "7w8",
          "core_fear": "Being trapped in emotional pain, boredom, or limitation.",
          "core_desire": "To maintain her freedom and happiness, to live a life full of excitement and stimulation.",
          "defense_mechanism": "Rationalization — Reframes negative experiences as exciting adventures or funny stories to avoid feeling pain or fear.",
          "stress_line": "Moves to Type 1 — Becomes critical, rigid, and judgmental when her freedom is threatened.",
          "growth_line": "Moves to Type 5 — Becomes more focused, introspective, and able to sit with complex ideas without needing immediate stimulation.",
          "instinctual_variant": "sx/so — Seeks intense experiences and connections, drawing energy from social engagement and playful provocation."
        },
        "shadow_psychology": {
            "mbti": "ENTP-shadow",
            "dominant": "Ne — Chaotic idea generation; creates endless destructive possibilities and cruel pranks.",
            "auxiliary": "Ti — Sadistic logical detachment; enjoys intellectually dismantling people and their beliefs.",
            "tertiary": "Fe — Cruel mockery and gaslighting; uses social awareness to humiliate and isolate targets.",
            "inferior": "Si — Obsessive rumination; becomes fixated on every slight and past humiliation."
        },
        'image': 'moxie1.jpeg',
		'song_id': 'bubblegum_bitch_marina'
    },
    {
        "npc_id": "tech",
        "name": "Kade",
        "description": "A tech-savvy inventor and engineer who is sarcastic, rude, and incredibly intelligent. Kade uses his technological prowess to create powerful gadgets and elegant solutions. He is always looking for ways to improve and push boundaries, often lightening tense moments with dry humor.",
		"theme_song": "Radioactive, Imagine Dragon (instrumental in deep thought)",
        "psychology": {
            "mbti": "INTJ",
            "dominant": "Ni — Foresees long-term consequences and systemic patterns with cold clarity.",
            "auxiliary": "Te — Executes plans with ruthless efficiency and demands high competence from everyone around him.",
            "tertiary": "Fi — Holds strong internal principles, though he rarely shows them. Becomes surprisingly cutting when they are violated.",
            "inferior": "Se — Under extreme stress, he either becomes paralyzed by details or lashes out with impulsive action."
        },
        "enneagram": {
          "enneagram_type": "5w6",
          "core_fear": "Being useless, helpless, or incapable.",
          "core_desire": "To be capable and competent.",
          "defense_mechanism": "Isolation — Detaches from his emotions to analyze problems with cold, objective logic. Sarcasm is a tool to maintain this distance.",
          "stress_line": "Moves to Type 7 — Becomes scattered, restless, and avoids problems through manic activity or new projects.",
          "growth_line": "Moves to Type 8 — Becomes more confident and decisive in action, using his knowledge to take charge in the real world.",
          "instinctual_variant": "sp/sx — Hoards knowledge and resources to ensure his own competence and survival, engaging intensely with subjects that capture his interest."
        },
        "shadow_psychology": {
            "mbti": "INTJ-shadow",
            "dominant": "Ni — Nihilistic fatalism; sees only inevitable failure and betrayal in every future.",
            "auxiliary": "Te — Becomes a cold tyrant; efficiency above all else, including human cost.",
            "tertiary": "Fi — Self-righteous moral superiority; judges everyone as weak or morally inferior.",
            "inferior": "Se — Reckless hedonism or violent outbursts; loses all impulse control."
        },
        'image': 'kade1.jpeg',
		'song_id': 'radioactive_instrumental_imagine_dragon'
    },
    {
        "npc_id": "skill",
        "name": "Poise",
        "description": "A master of incredible martial arts with unparalleled agility and stealth. Poise moves with deadly skill and precision. She is wise, calm, disciplined, and highly focused. Her charm and cunning make her both a formidable fighter and a valuable companion.",
		"theme_song": "Sail (instrumental), AWOLNATION | Clint Eastwood, Gorillaz",
        "psychology": {
            "mbti": "ISTP",
            "dominant": "Ti — Quietly analytical with internally precise understanding of movement, technique, and opponents.",
            "auxiliary": "Se — Hyper-attuned to the physical world. Her reflexes, agility, and combat instincts are razor sharp.",
            "tertiary": "Ni — Occasionally senses deeper patterns or future threats, giving him a mysterious, focused calm.",
            "inferior": "Fe — Avoids emotional expression. Under stress, she may lash out or completely withdraw."
        },
        "enneagram": {
          "enneagram_type": "9w8",
          "core_fear": "Loss of connection; conflict and fragmentation.",
          "core_desire": "To have inner stability and peace of mind.",
          "defense_mechanism": "Narcotization — Disengages from conflict or emotional turmoil by focusing on physical discipline and maintaining a calm, detached exterior.",
          "stress_line": "Moves to Type 6 — Becomes anxious, worried, and indecisive when her inner peace is threatened.",
          "growth_line": "Moves to Type 3 — Becomes more assertive, goal-oriented, and engaged with the world.",
          "instinctual_variant": "sp/sx — Seeks comfort and peace through physical routines and mastery, forming deep bonds with a select few."
        },
        "shadow_psychology": {
            "mbti": "ISTP-shadow",
            "dominant": "Ti — Detached nihilism; analyzes everything coldly, including why people deserve to die.",
            "auxiliary": "Se — Becomes adrenaline-addicted and reckless; lives only for the thrill of violence.",
            "tertiary": "Ni — Paranoid fatalism; convinced everyone will eventually betray her.",
            "inferior": "Fe — Explosive, misdirected rage; suddenly lashes out with cruel emotional attacks."
        },
        'image': 'poise1.jpeg',
		'song_id': 'sail_instrumental_awolnation'
    }
]

PLAYER_NPC_JOIN_DIALOGS = [
	### the first set are when the party first arrives in the new world . they appeared through portal don't know where they are each unit hasa dialog for the situation that is individual as only 2 arrive and that selection is random
	{
		'npc_id': 'technique', 
		'dialog_id': 'begin_game_add_pc', 
		'dialog': [
			"Whoa... where are we? This place looks... ancient.",
			"I don't know how we got here, but we need to stick together if we're going to figure this out.",
			"Let's find some shelter and gather our thoughts."
	]},
	{
		'npc_id': 'spirit', 
		'dialog_id': 'begin_game_add_pc', 
		'dialog': [
			"This land feels... different. Like it's alive in a way I've never felt before.",
			"We must be cautious. There could be dangers lurking around every corner.",
			"But I sense a purpose here. We were brought for a reason."
	]},
	{
		'npc_id': 'magic', 
		'dialog_id': 'begin_game_add_pc', 
		'dialog': [
			"Fascinating! The ambient magic here is unlike anything I've studied.",
			"We should explore and see what secrets this place holds.",
			"But first, let's ensure we're safe and have a plan."
	]},
	{
		'npc_id': 'tech', 
		'dialog_id': 'begin_game_add_pc', 
		'dialog': [
			"Hmm, the technology here seems primitive, yet there's something intriguing about it.",
			"We need to assess our surroundings and figure out how to adapt.",
			"Survival is our first priority; everything else can wait."
	]},
	{
		'npc_id': 'skill', 
		'dialog_id': 'begin_game_add_pc', 
		'dialog': [
			"This environment is unfamiliar, but I can feel its challenges ahead.",
			"We must rely on our skills and instincts to navigate this place.",
			"Let's stay alert and work together to overcome whatever lies ahead."
	]},
	### CHAPTER 2 JOINS ... "this world is crazy... Everywhere is chaos... took a job to get ingredients.  need help with gorgon ... basic concept
	### WE are actually coming to see the newly added character in a fight, so they urgently need help
	{
		'npc_id': 'technique',
		'dialog_id': 'ch2_add_pc',
		'dialog': [
			"This world is in chaos. I took a job to gather ingredients, but it was more dangerous than I expected.",
			"Care to give me a hand here?"
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'ch2_add_pc',
		'dialog': [
			"The turmoil in this world is overwhelming. I was gathering ingredients for a ritual when things went awry.",
			"I don't think I can handle this monster."
		]
	},
	{
		   'npc_id': 'magic',
		   'dialog_id': 'ch2_add_pc',
		   'dialog': [
			   "The magical disturbances here are unlike anything I've seen. I was collecting rare components when I was ambushed.",
			   "I could use some assistance against this creature."
		   ]
	},
	{
		   'npc_id': 'tech',
		   'dialog_id': 'ch2_add_pc',
		   'dialog': [
			   "This world's technology is wild. I was scavenging for parts when I ran into trouble.",
			   "I need backup to deal with this threat."
		   ]
	},
	{
		   'npc_id': 'skill',
		   'dialog_id': 'ch2_add_pc',
		   'dialog': [
			   "The chaos in this place is intense. I was on a job to acquire some items when I got caught off guard.",
			   "I could use some help taking down this beast."
		   ]
	},
	{
		'npc_id': 'technique', ## character just restored their memory and is ready to go with th party
		'dialog_id': 'add_pending_character',
		'dialog': [
			"That was fucking weird.  What are you pussies looking at?",
			"Let's go make something bleed."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'add_pending_character',
		'dialog': [
			"It's all coming back to me...  Oh god, you heathens!",
			"The god's have pitied you so far. I'll come along for the entartainment."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'add_pending_character',
		'dialog': [
			"Yessssssss! Now I remember everything... EVERYTHING!!! HAHAHA!",
			"Ughhhhhh! Including all you ugly losers!"
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'add_pending_character',
		'dialog': [
			"Now I remember you nerds.  I suppose you're gonna need my genius.  I'll tag along, until I rip this reality."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'add_pending_character',
		'dialog': [
			"Chaos unravels the mystery and I can see once again.",
			"It's amazing you failures managed that."
		]
	}
]