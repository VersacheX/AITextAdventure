# ============================================================
# = CHAPTER 19 : RECONSTRUCTING THE SELF
# ============================================================
#
# [ LOCATION - AURELION VEIL (CITY 19) ]
# -----------------------------------
# @ = player
# S = Soren (historian of living memory)
# A = Astra Wynn (returning teleporter/weaver)
# J = Jinn (memory-trinket merchant)
# T = Twisted Darkwood (source of false memory rot, boss)
# E = Seraphine (harmony singer, joins party)
#
# High level: The party arrives in Aurelion Veil, a city whose
# history is written into living trees. A rot is causing false
# looping memories. They must destroy the Twisted Darkwood at the
# source, then help Seraphine — a singer protecting her community
# with a perfect but hollow song — accept truth into her harmony
# and join the party, before Astra Wynn teleports them onward.

ATTAINABLE_PLAYER_CHARACTERS = [
	{
		"id": "seraphine",
		"name": "Seraphine",
		"level": 45,
		"arm_armor": "chronoweave_bracers",
		"head_armor": "hourglass_veil",
		"body_armor": "epochthread_robe",
		"leg_armor": "timelock_sandals",
		"equipped_weapon": "aurora_staff",
		"max_hp": 1200,
		"current_hp": 1200,
		"max_ap": 420,
		"current_ap": 420,
		"unused_ability_slots": 0,
		"unused_stat_points": 0,
		"unused_power_points": 0,
		"strength": 60,
		"dexterity": 100,
		"intelligence": 200,
		"constitution": 140,
		"abilities": [
			"light_technique_lv1_restore",
			"light_light_technique_lv2_radiant_chorus",
			"sound_technique_lv1_resonant_strike",
			"sound_sound_technique_lv2_harmonic_burst",
			"light_sound_technique_lv3_song_of_mending",
			"light_light_sound_technique_lv4_requiem_of_truth"
		]
	}
]

NPCS = [
	{
		"npc_id": "seraphine",
		"name": "Seraphine",
		"description": (
			"A singer who has kept her community alive in the rotting forest of Aurelion Veil by weaving a"
			" perfect, unbroken harmony around them. Her song is real magic - it holds the rot at bay and"
			" sustains the emotional memory of those inside its warmth. But it is also a cage: her harmony"
			" has no room for shadow, loss, or truth, and the people inside it are preserved rather than living."
			" She is exhausted, devoted, and terrified of what happens if she stops."
		),
        "theme_song": "Outro, M83",
		"psychology": {
			"mbti": "ENFJ",
			"dominant": "Fe - Pours herself entirely into the emotional wellbeing of her community, making their feelings her reason for existing.",
			"auxiliary": "Ni - Has a deep, intuitive understanding of how harmony, memory, and identity are interconnected; she sees the whole system of her community's soul.",
			"tertiary": "Se - Is acutely attuned to the sensory and aesthetic quality of her song; she can hear the exact moment it begins to fray.",
			"inferior": "Ti - Cannot apply cold logic to her situation; the idea that her perfect harmony might be the problem is almost impossible for her to process."
		},
		"enneagram": {
			"enneagram_type": "2w1",
			"core_fear": "Being unneeded; that if her song stops, those she loves will dissolve and she will have failed the one thing she was born to do.",
			"core_desire": "To be truly needed, to have her love and care be the thing that holds the world together.",
			"defense_mechanism": "Repression — Suppresses her own exhaustion, grief, and doubt so completely that she has begun to believe her own performance of serenity.",
			"stress_line": "Moves to Type 8 — Becomes fierce, controlling, and fiercely defensive of her glade when the party first threatens to introduce painful truth.",
			"growth_line": "Moves to Type 4 — Discovers her own identity and voice outside of her role as protector; learns that authentic song requires her whole self, including the broken parts.",
			"instinctual_variant": "so/sp — Entirely oriented around the social wellbeing of her community; her self-preservation is tied to the act of communal preservation."
		},
        'image': 'seraphine1.jpeg',
		'song_id': 'outro_m83'
	},
	{
		"npc_id": "twisted_darkwood",
		"name": "Twisted Darkwood",
		"description": (
			"The metaphysical source of the rot corrupting Aurelion Veil's living memory. It is not a creature"
			" so much as a wound made animate - a place where the city's genuine past was replaced by looping,"
			" comfortable lies, and that replacement calcified into a predatory entity. It speaks in the voice"
			" of the people's worst memories and deepest shame, trapping those who enter in recursive guilt"
			" that substitutes for real history."
		),
		"psychology": {
			"mbti": "ISTJ-shadow",
			"dominant": "Si - Its entire existence is a weaponized, corrupted version of memory: it enforces the rigid, looping past as the only reality, denying any growth or change.",
			"auxiliary": "Te - Deploys its false memories with systematic, impersonal efficiency, categorizing every visitor's weakness and selecting the most disabling loop.",
			"tertiary": "Fi - Has absorbed the genuine emotional pain of the city's true history and uses it as ammunition, making its attacks feel deeply, personally true.",
			"inferior": "Ne - Cannot conceive of a future; its entire ontology is the unchangeable, repeating past."
		},
		"enneagram": {
			"enneagram_type": "6w5",
			"core_fear": "That the false past it enforces will be dissolved and the real, unrepeatable truth will replace it.",
			"core_desire": "To make the loop permanent - to replace living memory with a fixed, controllable archive of shame.",
			"defense_mechanism": "Projection — Externalizes the city's suppressed grief and guilt onto each visitor, making them experience it as their own inevitable fate.",
			"stress_line": "Moves to Type 3 — Becomes desperately performative when challenged, generating increasingly vivid false memories to overwhelm resistance.",
			"growth_line": "Moves to Type 9 — (Hypothetically) Would dissolve into the peace of letting the true past simply be what it was.",
			"instinctual_variant": "sp/so — Obsessively focused on self-preservation through the preservation of its false archive."
		},
		'image': 'bosses:twisted_darkwood1'
	}
]

NPC_DIALOG = [
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch19_intro',
		'dialog': [
			"Chapter 19 - The past survives... not as something behind us, but as something within us."
		]
	},
	{
		'npc_id': 'soren',
		'dialog_id': 'soren_ch19_rot_mission',
		'dialog': [
			"A sickness is causing the city's heartwood to rot, creating false, looping memories. People are getting lost in echoes of a past that never was.",
			"We must enter the rotwood where the rot is strongest, find the source of the looping memory, the Twisted Darkwood, and destroy it. Only then can the city heal and remember its true self."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch19_memory_soul',
		'dialog': [
			"(gently) Memory is the foundation of who we are. If this city is losing its true past, then it is losing its soul. We will help you restore it."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch19_cut_it_out',
		'dialog': [
			"(gruff) Rot in the heartwood? Sounds like something that needs to be cut out clean. Point us at it."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch19_looping_memories',
		'dialog': [
			"Looping memories? Oh this is going to be *fun*. I wonder if I can steal one and sell it back better."
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_ch19_false_memory',
		'dialog': [
			"(muttering while scribbling notes) False memory recursion... fascinating. The structural implications for living architecture are enormous."
		]
	},
	{
		'npc_id': 'kor_in',
		'dialog_id': 'kor_in_ch19_haunted',
		'dialog': [
			"(quiet) I know what it is to be haunted by memories that refuse to stay in the past. Lead the way, historian."
		]
	},
	{
		'npc_id': 'soren',
		'dialog_id': 'soren_ch19_gratitude',
		'dialog': [
			"(with faint relief) Thank you. Most who come here only want to take from the Veil. You... seem to understand what it means to remember truly."
		]
	},
	{
		'npc_id': 'astra_wynn',
		'dialog_id': 'astra_wynn_ch19_heavy_memories',
		'dialog': [
			"The memories here have grown heavy. They pull people into comfortable lies instead of hard truths.",
			"If you destroy the Twisted Darkwood in the rotwood, I may be able to weave what remains into something lasting."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch19_temporal_stabilizer',
		'dialog': [
			"(analytical) A localized temporal stabilizer... interesting. What are the variables? How long will it hold?"
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch19_clear_the_rot',
		'dialog': [
			"(calm) We will clear the rot. You focus on what comes after."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch19_true_care',
		'dialog': [
			"(warm) Your willingness to sacrifice for this city's future speaks of true care. We will not let your effort be in vain."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch19_professionals',
		'dialog': [
			"(grinning) Don't worry, we're professionals at breaking things that need breaking. Just have that anchor ready when we get back."
		]
	},
	{
		'npc_id': 'astra_wynn',
		'dialog_id': 'astra_wynn_ch19_then_go',
		'dialog': [
			"(small smile) Then go. And try not to get lost in your own echoes."
		]
	},
	{
		'npc_id': 'jinn',
		'dialog_id': 'jinn_ch19_trinkets',
		'dialog': [
			"Memory-trinkets for sale! Relive your greatest triumphs! Side effects may include existential dread and temporal displacement. No refunds!",
			"Between you and me, half these trinkets are just polished lies. But people buy them anyway. Makes the loops feel less lonely."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch19_polished_lies',
		'dialog': [
			"(eyes sparkling) Polished lies you say? Now that's my kind of merchandise. Got anything that lets me win arguments I definitely lost?"
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch19_no_souvenirs',
		'dialog': [
			"(scowling) We're not here for souvenirs. We're here to stop the city from choking on its own fake history."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch19_worth_remembering',
		'dialog': [
			"(softly) Some memories are worth remembering, even the painful ones. False ones only steal from the truth."
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_ch19_degradation',
		'dialog': [
			"(adjusting goggles) ... the degradation rate must be accelerated by the rot."
		]
	},
	{
		'npc_id': 'jinn',
		'dialog_id': 'jinn_ch19_no_fun',
		'dialog': [
			"(chuckling nervously) You lot are no fun at all."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch19_twisted_darkwood_approach',
		'dialog': [
			"Approaching the Twisted Darkwood, the party is forced to relive the same moments of destruction, their own memories becoming unreliable."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch19_same_street',
		'dialog': [
			"I swear we've been down this street before. And I was wearing a different hat."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch19_focus',
		'dialog': [
			"Focus! It's trying to confuse us. Make us doubt what's real. Don't let it."
		]
	},
	{
		'npc_id': 'twisted_darkwood',
		'dialog_id': 'twisted_darkwoo_ch19_intro',
		'dialog': [
			"You are nothing but your mistakes. You will repeat them forever."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch19_more_than_past',
		'dialog': [
			"No. We are more than our past. We are the choices we make now."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch19_darkwood_shatter',
		'dialog': [
			"The metaphysical void corrupting the Twisted Darkwood shatters all that remains is a treetrunk which quickly rots to reality."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch19_reclaimed',
		'dialog': [
			"(breathing out) The weight... it feels lighter already. Like we've reclaimed a piece of ourselves."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch19_no_more_mud',
		'dialog': [
			"(nodding) Good. One less thing trying to drag us back into the mud."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch19_headfuck',
		'dialog': [
			"(grinning shakily) That was kind of a headfuck..."
		]
	},
	{
		'npc_id': 'ripple',
		'dialog_id': 'ripple_ch19_not_sure',
		'dialog': [
			"I'm still not sure if what I remember is real."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch19_loops_collapsing',
		'dialog': [
			"The false loops are collapsing. If we can stabilize this, the whole city might follow."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch19_move_forward',
		'dialog': [
			"We move forward. Always."
		]
	},
	{
		'npc_id': 'soren',
		'dialog_id': 'soren_ch19_rot_receding',
		'dialog': [
			"(visibly relieved, voice steadier) The rot... it's receding. The trees are remembering themselves again. You've given the Veil back its true history."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch19_choose_carry_forward',
		'dialog': [
			"(gentle) Memory is not just what happened. It is what we choose to carry forward. May this city choose wisely now."
		]
	},
	{
		'npc_id': 'vek',
		'dialog_id': 'vek_ch19_strong_foundation',
		'dialog': [
			"(firm) A strong foundation is the first step. What comes next?"
		]
	},
	{
		'npc_id': 'soren',
		'dialog_id': 'soren_ch19_see_astra_wynn',
		'dialog': [
			"Astra Wynn wanted to see you."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch19_melody',
		'dialog': [
			"A warm, perfectly balanced melody drifts through the decaying woods, creating a small bubble of peace and light."
		]
	},
	{
		'npc_id': 'seraphine',
		'dialog_id': 'seraphine_ch19_intro',
		'dialog': [
			"Stay with the song... stay with the warmth... don't let the world fall apart again...",
			"Outsiders? No... not now. This glade is all that remains of what we were. I won't let the rot take their memories too."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch19_too_perfect',
		'dialog': [
			"It's gorgeous, but it feels... too perfect. Like a painting that's starting to peel."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch19_terrible_price',
		'dialog': [
			"You're carrying the weight of an entire community alone. That kind of harmony demands a terrible price."
		]
	},
	{
		'npc_id': 'seraphine',
		'dialog_id': 'seraphine_ch19_no_choice',
		'dialog': [
			"What choice do I have? If I stop singing, they fade. If I let the truth in, they break. Help me... or leave me to my work."
		]
	},
	{
		'npc_id': 'seraphine',
		'dialog_id': 'seraphine_ch19_first_echo',
		'dialog': [
			"This... this isn't just joy. There's sorrow in it. Loss. Real life.",
			"I thought perfection would protect them, but these fragments... they feel alive."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch19_true_harmony',
		'dialog': [
			"True harmony isn't the absence of pain. It makes space for it."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch19_feels_honest',
		'dialog': [
			"Yeah, the pretty lie was nice, but this feels honest."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch19_pain_real',
		'dialog': [
			"Pain and all. That's how you know it's real."
		]
	},
	{
		'npc_id': 'seraphine',
		'dialog_id': 'seraphine_ch19_one_more',
		'dialog': [
			"(voice trembling) One more. Bring me one more. I need to be sure..."
		]
	},
	{
		'npc_id': 'seraphine',
		'dialog_id': 'seraphine_ch19_second_echo',
		'dialog': [
			"I see it now. A song without shadow is hollow. I've been keeping them in a cage of my own making...",
			"No more hiding. If they... if we, are going to survive this fracture, it has to be real."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch19_sing_with_us',
		'dialog': [
			"Then sing with us. Not to preserve the past, but to build what's next."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch19_broken_songs',
		'dialog': [
			"That's the spirit! The broken songs make the best anthems."
		]
	},
	{
		'npc_id': 'seraphine',
		'dialog_id': 'seraphine_ch19_wants_to_try',
		'dialog': [
			"I... I want to try. With all of you."
		]
	},
	{
		'npc_id': 'astra_wynn',
		'dialog_id': 'astra_wynn_ch19_good_timing',
		'dialog': [
			"Good timing. Marlo Finch has been asking for you specifically. He's holed up in Bayou Nocturn, digging through old memories and artifacts that might help with...",
			"Whatever this reconstruction mess is. I promised I'd send you his way if you showed up.",
			"Ready for another jump?"
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch19_teleports',
		'dialog': [
			"I have to say, these teleports keep getting smoother. Almost starting to enjoy the existential lurch."
		]
	},
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_ch19_beats_walking',
		'dialog': [
			"Beats walking through another rotting forest, that's for sure."
		]
	},
	{
		'npc_id': 'thorn',
		'dialog_id': 'thorn_ch19_efficient',
		'dialog': [
			"Efficient. No complaints."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch19_no_tree',
		'dialog': [
			"As long as we don't end up inside a tree again, I'm good."
		]
	},
	{
		'npc_id': 'astra_wynn',
		'dialog_id': 'astra_wynn_ch19_laughing',
		'dialog': [
			"(laughing lightly) Oh please, that only happened once and you all survived. Mostly intact."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch19_spatial_folding',
		'dialog': [
			"The spatial folding is remarkably stable this time. Minimal reality bleed."
		]
	},
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_ch19_high_praise',
		'dialog': [
			"High praise coming from you."
		]
	},
	{
		'npc_id': 'astra_wynn',
		'dialog_id': 'astra_wynn_ch19_flattery',
		'dialog': [
			"Flattery will get you everywhere. Alright, hold still - or don't. The chaos makes it more fun."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch19_teleport',
		'dialog': [
			"Astra Wynn raises her hands, weaving threads of light and shadow. Reality ripples violently around the party as they are pulled through a tear in space."
		]
	}
]

TASKS = [
	{
		'task_id': 'main_story_ch19_meet_soren',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'soren',
		'task_acquire_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch19_intro' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'soren', 'standing_text': ["This city remembers everything. Every triumph, every scar. The trees themselves are our history. But some memories are starting to... loop."]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'jinn', 'standing_text': ["Memory-trinkets for sale! Relive your greatest triumphs! Side effects may include existential dread and temporal displacement. No refunds!"]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'astra_wynn', 'standing_text': ["The memories here are so strong they have their own gravity. Be careful not to get pulled into an echo of the past."]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'soren', 'dialog_id': 'soren_ch19_rot_mission' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch19_memory_soul' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch19_cut_it_out' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch19_looping_memories' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch19_false_memory' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_ch19_haunted' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'soren', 'dialog_id': 'soren_ch19_gratitude' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'soren', 'standing_text': ["Thank you. Most who come here only want to take from the Veil. You... seem to understand what it means to remember truly."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch19_meet_astra_wynn' }}
		]
	},
	{
		'task_id': 'main_story_ch19_meet_astra_wynn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'astra_wynn',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'astra_wynn', 'dialog_id': 'astra_wynn_ch19_heavy_memories' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch19_temporal_stabilizer' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch19_clear_the_rot' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch19_true_care' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch19_professionals' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'astra_wynn', 'dialog_id': 'astra_wynn_ch19_then_go' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'astra_wynn', 'standing_text': ["Then go. And try not to get lost in your own echoes."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch19_meet_jinn' }}
		]
	},
	{
		'task_id': 'main_story_ch19_meet_jinn',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'jinn',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'jinn', 'dialog_id': 'jinn_ch19_trinkets' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch19_polished_lies' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch19_no_souvenirs' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch19_worth_remembering' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch19_degradation' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'jinn', 'dialog_id': 'jinn_ch19_no_fun' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'jinn', 'standing_text': ["You lot are no fun at all."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch19_meet_twisted_darkwoo' }}
		]
	},
	{
		'task_id': 'main_story_ch19_meet_twisted_darkwoo',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'twisted_darkwood',
		'task_acquire_events': [
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'twisted_darkwood', 'location': None }},
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'rotwood', 'location': 'region_open_area' }}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch19_twisted_darkwood_approach' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch19_same_street' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch19_focus' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'twisted_darkwood', 'dialog_id': 'twisted_darkwoo_ch19_intro' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch19_more_than_past' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'twisted_darkwood', 'standing_text': ["You are nothing but your mistakes. You will repeat them forever."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch19_destroy_twisted_darkwoo' }}
		]
	},
	{
		'task_id': 'main_story_ch19_destroy_twisted_darkwoo',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'twisted_darkwood_1',
		'task_acquire_events': [
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'twisted_darkwood_1', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'hide_npc', 'params': { 'npc_id': 'twisted_darkwood' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch19_darkwood_shatter' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch19_reclaimed' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch19_no_more_mud' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch19_headfuck' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'ripple', 'dialog_id': 'ripple_ch19_not_sure' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch19_loops_collapsing' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch19_move_forward' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch19_meet_soren_again' }}
		]
	},
	{
		'task_id': 'main_story_ch19_meet_soren_again',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'soren',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'soren', 'dialog_id': 'soren_ch19_rot_receding' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch19_choose_carry_forward' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch19_strong_foundation' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'soren', 'dialog_id': 'soren_ch19_see_astra_wynn' }},
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'seraphine', 'location': 'region_city_inn' }},
			{ 'event_type': 'set_npc_met', 'params': { 'npc_id': 'seraphine' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'seraphine', 'standing_text': ["My song... it must hold. For their sake... for all of us."]}},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch19_melody' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'astra_wynn', 'standing_text': ["Good timing. Marlo Finch has been asking for you specifically. He's holed up in Bayou Nocturn, digging through old memories and artifacts that might help with... whatever this reconstruction mess is. I promised I'd send you his way if you showed up. Ready for another jump?"]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'soren', 'standing_text': ["Astra Wynn is right. Marlo Finch has been asking for you. He may have information that can help with the reconstruction."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch19_meet_seraphine' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch19_meet_astra_wynn_again' }}
		]
	},
	{
		'task_id': 'main_story_ch19_meet_seraphine',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'seraphine',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seraphine', 'dialog_id': 'seraphine_ch19_intro' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch19_too_perfect' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch19_terrible_price' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seraphine', 'dialog_id': 'seraphine_ch19_no_choice' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'seraphine', 'standing_text': ["Please... help me strengthen the song before it collapses."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch19_deliver_harmony_echo_to_seraphine' }}
		]
	},
	{
		'task_id': 'main_story_ch19_deliver_harmony_echo_to_seraphine',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'seraphine',
		'item_id': 'harmony_echo',
		'task_acquire_events': [
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'seraphine_glade', 'location': 'region_city_open_area' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'seraphine_glade', 'item_id': 'harmony_echo', 'location': 'final_chamber' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'seraphine_glade', 'item_id': 'harmony_echo', 'location': 'final_chamber' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'seraphine_glade', 'item_id': 'snow_large_city_armor_key', 'location': 'final_chamber' }}
		],
		'task_complete_events': [
			{ 'event_type': 'remove_item', 'params': { 'item_id': 'harmony_echo' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seraphine', 'dialog_id': 'seraphine_ch19_first_echo' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch19_true_harmony' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch19_feels_honest' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch19_pain_real' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seraphine', 'dialog_id': 'seraphine_ch19_one_more' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'seraphine', 'standing_text': ["I have to face the rot... but I can't do it alone. Please, help me confront it."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch19_deliver_second_harmony_echo_to_seraphine' }}
		]
	},
	{
		'task_id': 'main_story_ch19_deliver_second_harmony_echo_to_seraphine',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'seraphine',
		'item_id': 'harmony_echo',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'remove_item', 'params': { 'item_id': 'harmony_echo' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seraphine', 'dialog_id': 'seraphine_ch19_second_echo' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch19_sing_with_us' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch19_broken_songs' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seraphine', 'dialog_id': 'seraphine_ch19_wants_to_try' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'seraphine', 'standing_text': ["I will try. With all of you."]}},
			{ 'event_type': 'hide_npc', 'params': { 'npc_id': 'seraphine' }},
			{ 'event_type': 'character_join', 'params': { 'character_id': 'seraphine' }}
		]
	},
	{
		'task_id': 'main_story_ch19_meet_astra_wynn_again',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'astra_wynn',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'astra_wynn', 'dialog_id': 'astra_wynn_ch19_good_timing' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch19_teleports' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch19_beats_walking' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch19_efficient' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch19_no_tree' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'astra_wynn', 'dialog_id': 'astra_wynn_ch19_laughing' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch19_spatial_folding' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch19_high_praise' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'astra_wynn', 'dialog_id': 'astra_wynn_ch19_flattery' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch19_teleport' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'astra_wynn', 'standing_text': ["Good timing. Marlo Finch has been asking for you specifically. He's holed up in Bayou Nocturn, digging through old memories and artifacts that might help with... whatever this reconstruction mess is. I promised I'd send you his way if you showed up. Ready for another jump?"]}},
			{ 'event_type': 'advance_chapter' }
		]
	}
]

PRIMARY_STORY_SETTINGS = {
	'chapter_id': 'main_story_chapter_19',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}
