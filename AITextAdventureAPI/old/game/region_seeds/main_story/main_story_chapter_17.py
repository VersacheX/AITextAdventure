# ============================================================
# = CHAPTER 17 : THE RULE OF PARADOX
# ============================================================
#
# [ LOCATION - THE PARADOX CITY (CITY 17) ]
# -----------------------------------
# @ = player
# H = Scribe Halden (paradox record-keeper)
# V = Vex (rule-breaking loophole artist)
# M = Mira (black market dealer)
# D = Displacer Gargantuan (paradox creature boss)
# P = Paradox (Voidwalker boss)
# C = Crux (returning Voidwalker)
#
# High level: The party follows a trail of contradictions — a legend
# about a paradox lock, a dealer who trades in the impossible, a
# creature that exists in two states at once, and finally a confrontation
# with both Paradox and Crux in the heart of the Punishment Engines.

ATTAINABLE_PLAYER_CHARACTERS = []

NPCS = [
	{
		"npc_id": "displacer_gargantuan",
		"name": "Displacer Gargantuan",
		"description": (
			"A massive creature that exists in two temporal states simultaneously — alive and already dead."
			" Its body phases between these states in a constant, sickening flicker. It does not experience"
			" time linearly and therefore speaks in a tense that has no name, describing past events as future"
			" and future events as already accomplished. It is less a thinking being than a living paradox."
		),
		"psychology": {
			"mbti": "ISTJ-shadow",
			"dominant": "Si - Trapped in two versions of its own memory simultaneously, one living and one dead, unable to distinguish which experience is current.",
			"auxiliary": "Te - Acts with the cold, mechanical certainty of something that believes the outcome is already determined.",
			"tertiary": "Fi - Has no values or identity; exists only as the embodiment of its paradoxical state.",
			"inferior": "Ne - Cannot conceive of a third option beyond its two states; the concept of resolution is alien to it."
		},
		"enneagram": {
			"enneagram_type": "9w8",
			"core_fear": "Resolution — the collapse of its paradox into a single, definite state.",
			"core_desire": "To exist in perpetual contradiction, never forced to be only one thing.",
			"defense_mechanism": "Narcotization — Its dual existence numbs it to any external threat; it cannot perceive genuine danger because it already knows every outcome.",
			"stress_line": "Moves to Type 6 — Becomes erratic and reactive when its paradox is genuinely threatened.",
			"growth_line": "Moves to Type 3 — (Hypothetically) Would learn to act with singular, directed purpose.",
			"instinctual_variant": "sp/so — Its entire existence is an act of self-preservation against the resolution that would end it."
		},
		'image': 'bosses:displacer_gargantuan1',
	},
	{
		"npc_id": "paradox",
		"name": "Paradox",
		"description": (
			"The Voidwalker of contradiction — a being that does not destroy meaning directly but makes all"
			" meaning simultaneously true and false, collapsing the difference between choice and its opposite."
			" Where Crux deconstructs, Paradox entangles. It speaks in perfect logical contradictions that"
			" somehow feel undeniable, and it takes a specific, predatory joy in watching coherent minds unravel."
		),
		"theme_song": "Paranoid Android, Radiohead",
		"psychology": {
			"mbti": "ENTP-shadow",
			"dominant": "Ne - Generates an endless, weaponized cascade of equally valid and equally impossible interpretations for every thought, belief, and action.",
			"auxiliary": "Ti - Constructs each paradox with airtight internal logic, making it impossible to dismiss without first being trapped inside it.",
			"tertiary": "Fe - Has a sophisticated, predatory read on which contradiction will hurt each specific person most deeply.",
			"inferior": "Si - Has no stable memory or past of its own; it exists only in the present moment of contradiction."
		},
		"enneagram": {
			"enneagram_type": "7w8",
			"core_fear": "That a single, unambiguous truth might exist and be perceived as such.",
			"core_desire": "To make every possible statement — including its own existence — simultaneously true and false.",
			"defense_mechanism": "Rationalization — Every act of destruction is framed as liberation from the tyranny of singular meaning.",
			"stress_line": "Moves to Type 1 — Becomes violently rigid and punishing when the party refuses to be trapped in its paradoxes.",
			"growth_line": "Moves to Type 5 — (Hypothetically) Would turn its understanding of contradiction into genuine intellectual discovery.",
			"instinctual_variant": "sx/so — Forms devastating one-on-one conceptual attacks on each party member, then uses the collective disorientation to dominate."
		},
        'image': 'voidwalkers:paradox1.jpeg',
		'song_id': 'paranoid_android_radiohead'
	}
]

NPC_DIALOG = [
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch17_intro',
		'dialog': [
			"Chapter 17 - The paradox lies not in reality, but in the way we describe it. - Russell"
		]
	},
	{
		'npc_id': 'scribe_halden',
		'dialog_id': 'scribe_halden_ch17_first_contact',
		'dialog': [
			"You were never here. And yet... here you are. I recorded your arrival yesterday. And tomorrow."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch17_halden_question',
		'dialog': [
			"How can both be true?"
		]
	},
	{
		'npc_id': 'scribe_halden',
		'dialog_id': 'scribe_halden_ch17_legend',
		'dialog': [
			"That is the question that keeps me here. The only clue I have left is this old legend.",
			"It speaks of a box that opens only when two impossible things are true at once."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch17_fairy_tales',
		'dialog': [
			"(frustrated) So we're chasing fairy tales now?"
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch17_loves_paradox',
		'dialog': [
			"No, this is perfect. A box that only works when it shouldn't. I *love* this place."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch17_exploiting_break',
		'dialog': [
			"If both versions of events are true, then logic itself is broken. We're not solving a puzzle. We're exploiting the break."
		]
	},
	{
		'npc_id': 'scribe_halden',
		'dialog_id': 'scribe_halden_ch17_directs_vex',
		'dialog': [
			"Take the legend to Vex. Maybe she can make two impossible things exist at the same time. I never could."
		]
	},
	{
		'npc_id': 'vex',
		'dialog_id': 'vex_ch17_reads_legend',
		'dialog': [
			"Halden finally cracked, huh? Let me see that legend.",
			"Whoa! The text on it shifts while I read it. I'm gonna need som time with this, but from what I get...",
			"This is a true paradox lock. It only opens if two mutually exclusive things are both real. I can solve it... but I need the actual Puzzle Box.",
			"There's a black market dealer in town. You should go talk to her and see if she knows anything about it."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch17_sounds_like_mira',
		'dialog': [
			"Sounds like Mira. Haven't seen her in a while."
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_ch17_both_true',
		'dialog': [
			"(muttering) Two things that cannot both be true... becoming true. This is going to hurt my head."
		]
	},
	{
		'npc_id': 'mira',
		'dialog_id': 'mira_ch17_greeting',
		'dialog': [
			"Back so soon? The Bracelet of Existence must really like you. It keeps dragging trouble my way."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch17_puzzle_box_question',
		'dialog': [
			"What do you know about an impossible puzzle box?"
		]
	},
	{
		'npc_id': 'mira',
		'dialog_id': 'mira_ch17_sends_to_mountains',
		'dialog': [
			"Straight to the point. I like that. I've heard of it, but unfortunately for you, I don't have it. But I do know who does.",
			"Tell you what, out in the mountains there's a ruin with an item called the Echofoil Nullglass, get that for me and by the time you get back I should have your puzzle box."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch17_another_contradiction',
		'dialog': [
			"Another contradiction..."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch17_delightfully_messy',
		'dialog': [
			"This is getting delightfully messy."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch17_gargantuan_entrance',
		'dialog': [
			"Deep in the mountain ruin, the party finds a creature that exists in two places at once.",
			"A massive gargantuan whose body phases between \"alive\" and \"already dead.\""
		]
	},
	{
		'npc_id': 'displacer_gargantuan',
		'dialog_id': 'displacer_gargantuan_ch17_intro',
		'dialog': [
			"I kill you yesterday. I kill you tomorrow. It has already happened."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch17_gargantuan_first',
		'dialog': [
			"...It's not happening. You're not the only one who can be contradictive."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch17_gargantuan_question',
		'dialog': [
			"How do you fight something that is both here and gone?"
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch17_gargantuan_choose',
		'dialog': [
			"Choose both."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch17_confusing',
		'dialog': [
			"How mind-bendingly confusing!"
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch17_between_states',
		'dialog': [
			"We strike in the moment that cannot exist. The space between its two states."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch17_gargantuan_defeat',
		'dialog': [
			"The gargantuan shatters, its two states finally resolving into one, then exploding into nothing."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch17_died_twice',
		'dialog': [
			"(laughing breathlessly) I died twice and survived three times in the same fight. I feel *amazing*."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch17_paradox_resolved',
		'dialog': [
			"Its existence was a paradox. Forcing it to resolve was the only way to win."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch17_impossible_moment',
		'dialog': [
			"We struck the moment that should not have been possible."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch17_back_to_mira',
		'dialog': [
			"Good. Now let's get this thing back to Mira before it starts existing again."
		]
	},
	{
		'npc_id': 'mira',
		'dialog_id': 'mira_ch17_gives_puzzle_box',
		'dialog': [
			"Two deaths held in one crystal. You really do bring me the most impossible things.",
			"Here. The Puzzle Box. Try not to let it open before you're ready. Or do. In this place, both choices are equally wrong."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch17_back_to_vex',
		'dialog': [
			"Finally. Let's get this back to Vex."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch17_becoming_contradictions',
		'dialog': [
			"Every step deeper into this feels like we're becoming more like the contradictions we fight."
		]
	},
	{
		'npc_id': 'vex',
		'dialog_id': 'vex_ch17_opens_box',
		'dialog': [
			"Perfect. Now watch what happens when two things that cannot both be true... become true anyway."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch17_box_opens',
		'dialog': [
			"Vex works the puzzle box. The runes flare, flicker, and contradict themselves violently."
		]
	},
	{
		'npc_id': 'vex',
		'dialog_id': 'vex_ch17_portal_ready',
		'dialog': [
			"That should tear open the path to the heart of the paradox. Ready to fall through reality?"
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_ch17_splitting',
		'dialog': [
			"(muttering) It exists in both states at once. I can't get a read. My instruments agree with each other and that's somehow worse."
		]
	},
	{
		'npc_id': 'vek',
		'dialog_id': 'vek_ch17_no_hesitation',
		'dialog': [
			"Then we move before it does. No hesitation."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch17_transported',
		'dialog': [
			"A blinding, fracturing light explodes from the box, swallowing the party and transporting them into the swirling possibilities."
		]
	},
	{
		'npc_id': 'paradox',
		'dialog_id': 'paradox_ch17_intro',
		'dialog': [
			"To proceed, you must stop. To win, you must lose. Welcome to the end of logic."
		]
	},
	{
		'npc_id': 'crux',
		'dialog_id': 'crux_ch17_architects',
		'dialog': [
			"Your minds are the final contradiction. We are simply the architects of your collapse."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch17_punch_next_week',
		'dialog': [
			"(growling) Talk all you want. I'll still punch you into next week."
		]
	},
	{
		'npc_id': 'paradox',
		'dialog_id': 'paradox_ch17_both_true',
		'dialog': [
			"You already did. And you never will. Both are true."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch17_faithful_contradiction',
		'dialog': [
			"(steady but pained) If we are contradictions, then let us choose to be faithful ones anyway."
		]
	},
	{
		'npc_id': 'crux',
		'dialog_id': 'crux_ch17_spirit_illusion',
		'dialog': [
			"Faith is the first illusion we break. Your gods abandoned this place long ago, little priestess."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch17_scream_paradox',
		'dialog': [
			"(grinning wildly) Being a contradiction is my brand! Let's see how you like it when I make this paradox *scream*!"
		]
	},
	{
		'npc_id': 'paradox',
		'dialog_id': 'paradox_ch17_chaos_hollow',
		'dialog': [
			"Your chaos is hollow without structure to rebel against. Even you are growing tired of screaming into the void, trickster."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch17_unpredictable',
		'dialog': [
			"(cold smirk) Then I'll become the variable you cannot predict or contain."
		]
	},
	{
		'npc_id': 'crux',
		'dialog_id': 'crux_ch17_vision_ends',
		'dialog': [
			"Your precious long-term vision ends here, architect. All futures collapse into the same gray nothing."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch17_choose_move',
		'dialog': [
			"(calm, deadly) Then strike. I choose to move even when movement has no purpose."
		]
	},
	{
		'npc_id': 'paradox',
		'dialog_id': 'paradox_ch17_falling_style',
		'dialog': [
			"Movement without direction is just falling with style. You are already lost, blade."
		]
	},
	{
		'npc_id': 'kor_in',
		'dialog_id': 'kor_in_ch17_dreams',
		'dialog': [
			"(quiet, eyes distant) My dreams used to show me paths... now they show me nothing. Endless nothing."
		]
	},
	{
		'npc_id': 'crux',
		'dialog_id': 'crux_ch17_nothing_honest',
		'dialog': [
			"Good. Nothing is the only honest answer left."
		]
	},
	{
		'npc_id': 'vek',
		'dialog_id': 'vek_ch17_exist_anyway',
		'dialog': [
			"Enough. We reject your contradictions. We choose to exist anyway."
		]
	},
	{
		'npc_id': 'paradox',
		'dialog_id': 'paradox_ch17_already_written',
		'dialog': [
			"(laughing) Choose all you want. The choice and its opposite are already written."
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_ch17_equations_breaking',
		'dialog': [
			"(scribbling furiously) Two states. Simultaneously. And we collapsed the waveform by *refusing the premise*. I've never seen a paradox die from sheer stubbornness before. Remarkable."
		]
	},
	{
		'npc_id': 'paradox',
		'dialog_id': 'paradox_ch17_fading',
		'dialog': [
			"You think you've resolved us...? We are every path not taken... and every path you will never take..."
		]
	},
	{
		'npc_id': 'crux',
		'dialog_id': 'crux_ch17_fading',
		'dialog': [
			"I am the wound between every possibility... Even in your victory... I remain... inside every choice you didn't make..."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch17_bosses_shatter',
		'dialog': [
			"Crux and Paradox shatter like glass made of contradictions. Their forms unravel into thousands of flickering, impossible versions of themselves before collapsing into absolute silence.",
			"The swirling vortex of conflicting realities around the party finally stills."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch17_existential_fun',
		'dialog': [
			"(grinning but shaken) That was the most fun I've had while having an existential crisis."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch17_echo_of_doubts',
		'dialog': [
			"(softly) They were the echo of every doubt we've ever had..."
		]
	},
	{
		'npc_id': 'scribe_halden',
		'dialog_id': 'scribe_halden_ch17_returns',
		'dialog': [
			"The contradictions... they've gone quiet. I can finally think in straight lines again. Thank you.",
			"There's a place you need to go. Frostgate Spire - a frozen city where time itself is caught in a loop.",
			"The people there are trapped reliving the same destruction."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'spirit_ch17_trapped_moments',
		'dialog': [
			"A place trapped between moments... still trying to exist despite everything."
		]
	},
	{
		'npc_id': 'scribe_halden',
		'dialog_id': 'scribe_halden_ch17_fragments',
		'dialog': [
			"Exactly. If any place still holds the fragments needed to rebuild meaning after all this, it's there.",
			"The anchor keeping the loop alive is tied to the same fracture energy you just faced."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch17_break_loop',
		'dialog': [
			"Then the next logical step is clear. We break the loop."
		]
	},
	{
		'npc_id': 'vek',
		'dialog_id': 'vek_ch17_fight_to_remember',
		'dialog': [
			"(nodding firmly) A city fighting to remember itself. Sounds like our kind of fight."
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_ch17_temporal_recursion',
		'dialog': [
			"(adjusting his goggles) Temporal recursion... fascinating. I want to see how the reset patterns behave."
		]
	},
	{
		'npc_id': 'kor_in',
		'dialog_id': 'kor_in_ch17_different_tomorrow',
		'dialog': [
			"(quietly) If they're reliving the same pain... maybe we can give them a different tomorrow."
		]
	},
	{
		'npc_id': 'scribe_halden',
		'dialog_id': 'scribe_halden_ch17_go_frostgate',
		'dialog': [
			"(smiling faintly) Go to Frostgate Spire. Break the cycle there. If you can do that... maybe there's still hope the rest of this broken world can follow."
		]
	}
]

TASKS = [
	{
		'task_id': 'main_story_ch17_meet_scribe_halden',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'scribe_halden',
		'task_acquire_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch17_intro' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'scribe_halden', 'standing_text': ["I record what happened... and what didn't. Both are equally true."]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'vex', 'standing_text': ["Every possibility cancels another. The tighter the contradiction, the easier it is to slip through."]}},
			{ 'event_type': 'show_npc', 'params': { 'npc_id': 'mira', 'location': 'region_city_shopweapons' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'mira', 'standing_text': ["Fancy meeting you here, I see you found the Bracelet of Existence."]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scribe_halden', 'dialog_id': 'scribe_halden_ch17_first_contact' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch17_halden_question' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scribe_halden', 'dialog_id': 'scribe_halden_ch17_legend' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch17_fairy_tales' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch17_loves_paradox' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch17_exploiting_break' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scribe_halden', 'dialog_id': 'scribe_halden_ch17_directs_vex' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'scribe_halden', 'standing_text': ["Compliance is mandatory. Non-compliance is impossible. You are already in violation."]}},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'puzzle_box_legend' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch17_deliver_puzzle_box_legend_to_vex' }}
		]
	},
	{
		'task_id': 'main_story_ch17_deliver_puzzle_box_legend_to_vex',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'vex',
		'item_id': 'puzzle_box_legend',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vex', 'dialog_id': 'vex_ch17_reads_legend' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch17_sounds_like_mira' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch17_both_true' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'vex', 'standing_text': ["Every possibility cancels another. The tighter the contradiction, the easier it is to slip through."]}},
			{ 'event_type': 'remove_item', 'params': { 'item_id': 'puzzle_box_legend' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch17_meet_mira_for_puzzle_box' }}
		]
	},
	{
		'task_id': 'main_story_ch17_meet_mira_for_puzzle_box',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'mira',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'mira', 'dialog_id': 'mira_ch17_greeting' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch17_puzzle_box_question' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'mira', 'dialog_id': 'mira_ch17_sends_to_mountains' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch17_another_contradiction' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch17_delightfully_messy' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'mira', 'standing_text': ["Fancy meeting you here, I see you found the Bracelet of Existence."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch17_deliver_echofoil_nullglass_to_mira' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch17_meet_displacer_gargantuan' }}
		]
	},
	{
		'task_id': 'main_story_ch17_meet_displacer_gargantuan',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'displacer_gargantuan',
		'task_acquire_events': [
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'displacer_gargantuan', 'location': None }},
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'mountain_ruin', 'location': 'region_open_area' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'mountain_ruin', 'item_id': 'rallying_bracers', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'mountain_ruin', 'item_id': 'rallying_crown', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'mountain_ruin', 'item_id': 'brightpath_sandals', 'location': 'treasure_room' }},
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch17_gargantuan_entrance' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'displacer_gargantuan', 'dialog_id': 'displacer_gargantuan_ch17_intro' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch17_gargantuan_first' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch17_gargantuan_question' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch17_gargantuan_choose' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch17_confusing' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch17_between_states' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'displacer_gargantuan', 'standing_text': ["I kill you yesterday. I kill you tomorrow. I kill you today."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch17_defeat_displacer_gargantuan' }}
		]
	},
	{
		'task_id': 'main_story_ch17_defeat_displacer_gargantuan',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'displacer_gargantuan_1',
		'task_acquire_events': [
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'displacer_gargantuan_1', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'hide_npc', 'params': { 'npc_id': 'displacer_gargantuan' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch17_gargantuan_defeat' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch17_died_twice' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch17_paradox_resolved' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch17_impossible_moment' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch17_back_to_mira' }},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'echofoil_nullglass' }}
		]
	},
	{
		'task_id': 'main_story_ch17_deliver_echofoil_nullglass_to_mira',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'mira',
		'item_id': 'echofoil_nullglass',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'mira', 'dialog_id': 'mira_ch17_gives_puzzle_box' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch17_back_to_vex' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch17_becoming_contradictions' }},
			{ 'event_type': 'remove_item', 'params': { 'item_id': 'echofoil_nullglass' }},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'puzzle_box' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'mira', 'standing_text': ["Fancy meeting you here, I see you found the Bracelet of Existence."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch17_deliver_puzzle_box_to_vex' }}
		]
	},
	{
		'task_id': 'main_story_ch17_deliver_puzzle_box_to_vex',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'vex',
		'item_id': 'puzzle_box',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vex', 'dialog_id': 'vex_ch17_opens_box' }},
			{ 'event_type': 'remove_item', 'params': { 'item_id': 'puzzle_box' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch17_box_opens' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'vex', 'dialog_id': 'vex_ch17_portal_ready' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch17_splitting' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch17_no_hesitation' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch17_transported' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'vex', 'standing_text': ["Every possibility cancels another. The tighter the contradiction, the easier it is to slip through."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch17_meet_paradox_and_crux' }}
		]
	},
	{
		'task_id': 'main_story_ch17_meet_paradox_and_crux',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'paradox',
		'task_acquire_events': [
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'paradox', 'location': None }},
			{ 'event_type': 'show_npc', 'params': { 'npc_id': 'crux', 'location': None }},
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'punishment_engines', 'location': 'region_city_open_area' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'punishment_engines', 'item_id': 'prophecy_remnant', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'punishment_engines', 'item_id': 'beacon_staff', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'punishment_engines', 'item_id': 'brightcall_crown', 'location': 'treasure_room' }},
			{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'punishment_engines', 'location': 'entrance' }}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'paradox', 'dialog_id': 'paradox_ch17_intro' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch17_architects' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch17_punch_next_week' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'paradox', 'dialog_id': 'paradox_ch17_both_true' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch17_faithful_contradiction' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch17_spirit_illusion' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch17_scream_paradox' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'paradox', 'dialog_id': 'paradox_ch17_chaos_hollow' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch17_unpredictable' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch17_vision_ends' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch17_choose_move' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'paradox', 'dialog_id': 'paradox_ch17_falling_style' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_ch17_dreams' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch17_nothing_honest' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch17_exist_anyway' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'paradox', 'dialog_id': 'paradox_ch17_already_written' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch17_equations_breaking' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'paradox', 'standing_text': ["To proceed, you must stop. To win, you must lose. Welcome to the end of logic."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch17_defeat_paradox_and_crux' }}
		]
	},
	{
		'task_id': 'main_story_ch17_defeat_paradox_and_crux',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'paradox_crux_1',
		'task_acquire_events': [
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'paradox_crux_1', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'hide_npc', 'params': { 'npc_id': 'paradox' }},
			{ 'event_type': 'hide_npc', 'params': { 'npc_id': 'crux' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'paradox', 'dialog_id': 'paradox_ch17_fading' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch17_fading' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch17_bosses_shatter' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch17_existential_fun' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch17_echo_of_doubts' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch17_meet_scribe_halden_again' }}
		]
	},
	{
		'task_id': 'main_story_ch17_meet_scribe_halden_again',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'scribe_halden',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scribe_halden', 'dialog_id': 'scribe_halden_ch17_returns' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch17_trapped_moments' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scribe_halden', 'dialog_id': 'scribe_halden_ch17_fragments' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch17_break_loop' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch17_fight_to_remember' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch17_temporal_recursion' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_ch17_different_tomorrow' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scribe_halden', 'dialog_id': 'scribe_halden_ch17_go_frostgate' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'scribe_halden', 'standing_text': ["Compliance is mandatory. Non-compliance is impossible. You are already in violation."]}},
			{ 'event_type': 'advance_chapter' }
		]
	}
]

PRIMARY_STORY_SETTINGS = {
	'chapter_id': 'main_story_chapter_17',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}
