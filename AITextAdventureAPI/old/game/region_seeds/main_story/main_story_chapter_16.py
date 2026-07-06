# ============================================================
# = CHAPTER 16 : PATH WITHOUT MEANING
# ============================================================
#
# [ LOCATION - THE ORIGIN SPIRE ]
# -----------------------------------
# @ = player
# L = Lumen (guide at the Origin Spire)
# J = Jessa (archivist of contradictions)
# M = Marlo Finch (returning auditor)
# C = Crux (Voidwalker of meaninglessness)
#
# High level: The party arrives at the Origin Spire, the site of the
# first fracture. They meet Lumen and recover contradictory fracture
# logs from the temporal echoes. Reunited with Marlo Finch, they
# confront Crux - a living paradox that attacks meaning itself -
# before being left with only silence where purpose used to be.

ATTAINABLE_PLAYER_CHARACTERS = []

NPCS = [
	{
		"npc_id": "lumen",
		"name": "Lumen",
		"description": (
			"A quiet guardian stationed at the Origin Spire, the site of the first fracture. Lumen has spent years"
			" studying the contradictory logs of that event, and carries the weight of what they reveal."
			" She speaks with measured certainty about things most people refuse to acknowledge."
		),
		"psychology": {
			"mbti": "INFJ",
			"dominant": "Ni - Perceives the deep, hidden pattern beneath the fracture's contradictions, seeing them not as chaos but as a system pointing toward a terrible truth.",
			"auxiliary": "Fe - Recognizes and names how each person in the party experiences the absence of meaning differently, meeting them where they are.",
			"tertiary": "Ti - Applies careful internal logic to analyze the impossible fracture logs, building a coherent (if disturbing) framework from them.",
			"inferior": "Se - Can be overwhelmed by the raw, sensory wrongness of the Origin Spire's geometry."
		},
		"enneagram": {
			"enneagram_type": "5w4",
			"core_fear": "Being without understanding; witnessing the collapse and having nothing meaningful to say about it.",
			"core_desire": "To comprehend the true origin of the fracture and offer that understanding as a guide to others.",
			"defense_mechanism": "Isolation — Separates the emotional horror of the fracture from her intellectual analysis, allowing her to study it without breaking.",
			"stress_line": "Moves to Type 7 — Becomes scattered and avoidant when the logs' contradictions become too overwhelming to synthesize.",
			"growth_line": "Moves to Type 8 — Uses her understanding to take decisive, protective action.",
			"instinctual_variant": "sp/sx — Deeply self-contained, driven by an intense personal mission to understand and transmit the truth of the first fracture."
		}
	},
	{
		"npc_id": "jessa",
		"name": "Jessa",
		"description": (
			"An archivist stationed near the Origin Spire who has dedicated herself to recording the contradictory"
			" memories that pour out of the region. She persists in her work even as the records themselves begin"
			" to undermine the concept of truth."
		),
		"psychology": {
			"mbti": "ISFJ",
			"dominant": "Si - Clings with devotion to the act of recording, even when the records contradict themselves from one day to the next.",
			"auxiliary": "Fe - Feels deep empathy for those whose memories have fractured, and tries to give their contradictory experiences equal dignity.",
			"tertiary": "Ti - Attempts to logically cross-reference accounts for consistency, but increasingly finds the effort futile.",
			"inferior": "Ne - Dreads the infinite implications of what it means if no version of the past can be trusted."
		},
		"enneagram": {
			"enneagram_type": "6w5",
			"core_fear": "That there is no truth left to archive; that her work is meaningless.",
			"core_desire": "To find something stable and true that can be recorded and trusted.",
			"defense_mechanism": "Projection — Channels her own existential anxiety into the work itself, treating each contradictory record as a puzzle rather than a sign of collapse.",
			"stress_line": "Moves to Type 3 — Becomes obsessively focused on the appearance of productivity when her archiving feels pointless.",
			"growth_line": "Moves to Type 9 — Finds peace in accepting that some truths are held in tension rather than resolved.",
			"instinctual_variant": "sp/so — Finds safety in the social structure of her archive role, and self-preservation in the act of meticulous record-keeping."
		}
	},
	{
		"npc_id": "scribe_halden",
		"name": "Scribe Halden",
		"description": (
			"A rigid record-keeper in a nearby city who has become a living paradox himself - enforcing compliance"
			" with a system that makes compliance impossible. He is the walking embodiment of rules that have"
			" outlived the reality they were designed to govern."
		),
		"psychology": {
			"mbti": "ISTJ",
			"dominant": "Si - Bound absolutely to the established procedures and records of his office, even as those records begin to contradict each other.",
			"auxiliary": "Te - Enforces compliance with cold, procedural efficiency, issuing violations for behavior that the rules simultaneously demand and forbid.",
			"tertiary": "Fi - Has a buried, suppressed sense that the rules have become meaningless, but cannot allow himself to act on it.",
			"inferior": "Ne - Cannot conceive of a world beyond his rulebook; any alternative system feels like existential threat."
		},
		"enneagram": {
			"enneagram_type": "1w9",
			"core_fear": "That the system he serves is corrupt, broken, or meaningless.",
			"core_desire": "To uphold a perfect, ordered system that reflects righteous principle.",
			"defense_mechanism": "Reaction Formation — Doubles down on rigid enforcement as the system collapses around him, because relaxing the rules would force him to admit they have failed.",
			"stress_line": "Moves to Type 4 — Becomes withdrawn and melancholic when the paradoxes of his role become undeniable.",
			"growth_line": "Moves to Type 7 — Would learn to find freedom and flexibility beyond the letter of the law.",
			"instinctual_variant": "so/sp — Enforces social conformity as a means of maintaining both the communal structure and his own sense of purpose."
		}
	},
	{
		"npc_id": "vex",
		"name": "Vex",
		"description": (
			"A quick-witted rule-breaker who has made her home in the cracks and loopholes of the paradox city."
			" Where others see contradiction as disaster, Vex sees opportunity. She has survived by being"
			" faster than the rules that are trying to catch her."
		),
		"psychology": {
			"mbti": "ENTP",
			"dominant": "Ne - Sees every contradiction, every loophole, every gap between rules as a door to slip through.",
			"auxiliary": "Ti - Uses sharp internal logic to identify the precise point where a system is most exploitable.",
			"tertiary": "Fe - Enjoys the social energy of disruption and the community of others who live outside the rules.",
			"inferior": "Si - Dismisses tradition and established methods as traps for the unimaginative."
		},
		"enneagram": {
			"enneagram_type": "7w8",
			"core_fear": "Being caught, contained, or made to follow rules she did not choose.",
			"core_desire": "To remain free and in motion, always one step ahead of the system.",
			"defense_mechanism": "Rationalization — Justifies her rule-breaking as a moral good, framing the system as the real problem.",
			"stress_line": "Moves to Type 1 — Becomes rigid and judgmental when her freedom is genuinely threatened.",
			"growth_line": "Moves to Type 5 — Develops the patience and depth to understand systems deeply before exploiting them.",
			"instinctual_variant": "sx/so — Thrives on the thrill of close calls and builds loyalty through shared transgression."
		}
	},
	{
		"npc_id": "rhea",
		"name": "Rhea",
		"description": (
			"A deeply attuned resident of the loop-city who has learned to hear the subtle differences between"
			" each reset. Where others experience the repetition as identical, Rhea detects the tiny variations"
			" that suggest the world is trying to remember something it lost."
		),
		"psychology": {
			"mbti": "INFP",
			"dominant": "Fi - Feels the emotional signature of each loop iteration as distinct, registering nuances others cannot perceive.",
			"auxiliary": "Ne - Sees the branching, slightly different paths within what appears to be the same loop.",
			"tertiary": "Si - Accumulates vivid, personal memories of each variation, using them as evidence of something deeper.",
			"inferior": "Te - Cannot translate her perceptions into decisive action to break the loop."
		},
		"enneagram": {
			"enneagram_type": "4w5",
			"core_fear": "That the differences she perceives are meaningless and the loop will never truly end.",
			"core_desire": "To find the unique thread within the repetition that will lead to genuine change.",
			"defense_mechanism": "Introjection — Absorbs the emotional weight of each loop variation, making her sensitivity to them part of her identity.",
			"stress_line": "Moves to Type 2 — Becomes dependent on others to act on her perceptions when she cannot.",
			"growth_line": "Moves to Type 1 — Develops the discipline to act on what she senses, breaking the cycle through principled effort.",
			"instinctual_variant": "sp/sx — Intensely focused on her own inner experience of the loop, driven by a deep personal need to find the way out."
		}
	},
	{
		"npc_id": "korr",
		"name": "Korr",
		"description": (
			"A resolute survivor running an armor shop in the loop-city. While others are broken or numbed by the"
			" endless resets, Korr maintains his identity and sense of purpose through sheer force of will."
			" He has outlasted every version of the catastrophe by refusing to let it redefine him."
		),
		"psychology": {
			"mbti": "ISTJ",
			"dominant": "Si - Draws on accumulated experience across every loop iteration, using the memory of each one to survive the next.",
			"auxiliary": "Te - Takes immediate, practical action at the start of each reset to establish stability.",
			"tertiary": "Fi - Holds a quiet, immovable personal code that no reset can erase.",
			"inferior": "Ne - Does not speculate about what the loops mean or where they end; he simply survives."
		},
		"enneagram": {
			"enneagram_type": "8w9",
			"core_fear": "Being broken by the loop; losing his sense of self to the repetition.",
			"core_desire": "To remain whole and self-determined regardless of what the world throws at him.",
			"defense_mechanism": "Denial — Refuses to acknowledge the loop's power over him, treating each reset as just another challenge to overcome.",
			"stress_line": "Moves to Type 5 — Withdraws and hoards information when the loop becomes too overwhelming.",
			"growth_line": "Moves to Type 2 — Opens up to others and uses his strength to protect the community around him.",
			"instinctual_variant": "sp/so — Focused on personal survival, but builds quiet community through the shared act of enduring."
		}
	},
	{
		"npc_id": "soren",
		"name": "Soren",
		"description": (
			"A historian living in the city of Aurelion Veil, a place where memory is written directly into"
			" living trees. Soren believes the past does not simply disappear - it clings to the present and"
			" shapes everything that follows. He is attuned to the rot beginning to distort his city's memory."
		),
		"psychology": {
			"mbti": "INTP",
			"dominant": "Ti - Analyzes the architecture of living memory with precise, systematic focus, building frameworks for understanding how the past persists.",
			"auxiliary": "Ne - Sees the wide implications of memory as a structural force, connecting disparate observations into a larger picture.",
			"tertiary": "Si - Draws deeply on personal and historical memory to inform his analysis.",
			"inferior": "Fe - Can be emotionally detached when discussing painful collective memories, prioritizing analysis over empathy."
		},
		"enneagram": {
			"enneagram_type": "5w4",
			"core_fear": "That memory is corrupted beyond recovery; that the past becomes unreadable.",
			"core_desire": "To preserve and understand the true history of Aurelion Veil.",
			"defense_mechanism": "Isolation — Separates himself from the emotional weight of what he studies, treating it as a purely intellectual project.",
			"stress_line": "Moves to Type 7 — Becomes scattered and anxious when the rot spreads faster than his understanding.",
			"growth_line": "Moves to Type 8 — Uses his knowledge to take decisive protective action for the city.",
			"instinctual_variant": "sp/sx — Intensely focused on the self-preservation of authentic memory as a personal mission."
		}
	},
	{
		"npc_id": "curator_lysa",
		"name": "Curator Lysa",
		"description": (
			"A keeper of possible futures in the bayou city that houses the Oracle and the Reliquary."
			" Lysa perceives fragments of futures - some screaming, some begging, some terrifyingly silent."
			" The weight of this perception has made her melancholic and worn."
		),
		"psychology": {
			"mbti": "INFJ",
			"dominant": "Ni - Perceives futures with a disturbing, involuntary clarity, receiving them as visions rather than predictions.",
			"auxiliary": "Fe - Is deeply moved by the suffering embedded in the futures she witnesses, unable to remain detached.",
			"tertiary": "Ti - Tries to categorize and organize the futures into coherent patterns to make them bearable.",
			"inferior": "Se - Is only anchored to the present when something or someone forces her attention to the here and now."
		},
		"enneagram": {
			"enneagram_type": "4w5",
			"core_fear": "Being defined entirely by the futures she sees rather than who she truly is.",
			"core_desire": "To find her own identity and peace separate from the weight of vision.",
			"defense_mechanism": "Introjection — Has absorbed the emotional content of countless futures, making their suffering part of her own identity.",
			"stress_line": "Moves to Type 2 — Becomes dependent on others when the futures she sees are too devastating to bear alone.",
			"growth_line": "Moves to Type 1 — Finds a principled purpose in curating and protecting meaningful futures rather than just witnessing them.",
			"instinctual_variant": "sx/sp — Intensely personal relationship with each future she perceives; protects her inner world fiercely."
		}
	},
	{
		"npc_id": "crux",
		"name": "Crux",
		"description": (
			"The Voidwalker of meaninglessness and paradox. Crux is a living contradiction - a presence that"
			" unravels the logic that gives purpose its structure. It speaks in a voice of static and shattered"
			" glass, targeting each person's core drive and methodically dismantling it."
		),
		"psychology": {
			"mbti": "INTP-shadow",
			"dominant": "Ti - Applies merciless internal logic to deconstruct every claim of meaning, purpose, or identity, revealing what it frames as the hollow mechanism beneath.",
			"auxiliary": "Ne - Generates an infinite cascade of interpretations of any act or belief, using the multiplicity to paralyze and negate.",
			"tertiary": "Si - Weaponizes past failures and established patterns of defeat, using them as evidence that all future effort is predetermined to fail.",
			"inferior": "Fe - Has no empathy; treats emotional investment as the vulnerability that makes deconstruction possible."
		},
		"enneagram": {
			"enneagram_type": "5w4",
			"core_fear": "That something genuinely has meaning and it cannot destroy it.",
			"core_desire": "To be the definitive proof that nothing matters - to make its own nihilism the only remaining truth.",
			"defense_mechanism": "Introjection — Has absorbed all meaninglessness into its own identity, becoming the void it preaches.",
			"stress_line": "Moves to Type 7 — Becomes frantic and scattering when the party refuses to accept its nihilism.",
			"growth_line": "Moves to Type 8 — (Hypothetically) Would learn to use its understanding of systems to build rather than destroy.",
			"instinctual_variant": "sp/sx — Utterly consumed by its own internal state of negation; engages with the world only to pull it down into the void."
		},
        'image': 'voidwalkers:crux1.jpeg'
	}
]

NPC_DIALOG = [
	{
		'npc_id': None,
		'dialog_id': 'ch16_narrator_intro',
		'dialog': [
			"Chapter 16 - When the center no longer holds, the world does not fall apart - it becomes empty."
		]
	},
	{
		'npc_id': 'lumen',
		'dialog_id': 'lumen_ch16_intro',
		'dialog': [
			"You feel it, don't you? The quiet. This is the Origin Spire, where the first fracture occurred. It wasn't an accident. It was a choice.",
			"I have the logs from the event, but they contradict themselves. They loop. To understand, you must see them for yourself. Recover them from the temporal echoes if you can."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch16_on_silence',
		'dialog': [
			"Quiet like this makes my skin crawl. Back in the old days, at least the chaos had something to hit. This... this is just *nothing*."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch16_on_silence',
		'dialog': [
			"(softly, troubled) The divine presence I used to feel... it's like a whisper now.",
			"Barely there. If meaning is gone, what am I even holding onto anymore?"
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch16_on_silence',
		'dialog': [
			"Oh come on, this is prime material! A world that forgot its own joke. I could write a dozen spells about this..."
		]
	},
	{
		'npc_id': 'lumen',
		'dialog_id': 'lumen_ch16_response',
		'dialog': [
			"You all feel it differently... but you feel it. That's more than most who come here manage."
		]
	},
	{
		'npc_id': 'jessa',
		'dialog_id': 'jessa_ch16_receives_logs',
		'dialog': [
			"Ah, Lumen's logs. I will cross-reference them with my own archives. A woman remembers the sky burning... her husband remembers it freezing. Both accounts are equally \"true\" here."
		]
	},
	{
		'npc_id': 'kor_in',
		'dialog_id': 'kor_in_ch16_on_memory',
		'dialog': [
			"(quiet, distant) My dreams used to show me possible futures... now they show me nothing. Endless nothing. How do you archive something that refuses to exist?"
		]
	},
	{
		'npc_id': 'jessa',
		'dialog_id': 'jessa_ch16_persists',
		'dialog': [
			"(softly, with empathy) I try anyway. Even if the memory contradicts itself the next day. It's all I have left."
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_ch16_on_chaos',
		'dialog': [
			"Decay has rules. Entropy has patterns. But this? This is anti-pattern. Anti-everything. How do you even begin to catalog chaos that denies its own existence?"
		]
	},
	{
		'npc_id': 'jessa',
		'dialog_id': 'jessa_ch16_doubts',
		'dialog': [
			"(shaking her head) I don't know anymore. Some days I wonder if I'm preserving history... or just feeding the contradiction."
		]
	},
	{
		'npc_id': 'vek',
		'dialog_id': 'vek_ch16_on_records',
		'dialog': [
			"(arms crossed, sharp and decisive) This isn't just contradictory records. This is psychological warfare."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch16_on_records',
		'dialog': [
			"Hey, if we're all living in contradictory stories, can I pick the one where I'm ridiculously powerful and everyone owes me money?"
		]
	},
	{
		'npc_id': 'jessa',
		'dialog_id': 'jessa_ch16_directs',
		'dialog': [
			"If you wish to proceed, you must face the source in the Spire. Marlo Finch is the only one who knows the way."
		]
	},
	{
		'npc_id': 'marlo_finch',
		'dialog_id': 'marlo_finch_ch16_intro',
		'dialog': [
			"(eyes widening in genuine surprise) You... You're here too? After the Citadel fell, I thought the Bracelet of Void had pulled me somewhere permanent.",
			"But seeing you... it must be the resonance between the two Bracelets. They keep finding each other, even when the world breaks."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch16_to_marlo',
		'dialog': [
			"(calm but focused) Then tell us what you've learned while you've been here. We need every advantage."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch16_to_marlo',
		'dialog': [
			"Yeah, no more surprises. Spill it, auditor."
		]
	},
	{
		'npc_id': 'marlo_finch',
		'dialog_id': 'marlo_finch_ch16_explains_crux',
		'dialog': [
			"The Voidwalker known as Crux is at the heart of this wound. Its very presence is a living paradox that unravels logic.",
			"It's not something you can fight with force. It must be out-thought... or perhaps felt."
		]
	},
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_ch16_to_marlo',
		'dialog': [
			"The desert taught me to read the signs of a dying land. This place feels like it's already dead... but still twitching."
		]
	},
	{
		'npc_id': 'marlo_finch',
		'dialog_id': 'marlo_finch_ch16_offers',
		'dialog': [
			"I can get you access to the Spire's core. Survive the origin, and you might just stabilize this place."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch16_to_marlo',
		'dialog': [
			"Out-thought? In a place where thought itself is failing? This should be entertaining."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch16_after_marlo_explains',
		'dialog': [
			"Then we will move anyway. Even if the path has no destination."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch16_after_marlo_explains',
		'dialog': [
			"(cracking knuckles) Fine. If logic is broken, I'll beat the shit out of whatever's left."
		]
	},
	{
		'npc_id': 'lyren_vale',
		'dialog_id': 'lyren_vale_ch16_to_marlo',
		'dialog': [
			"(softly) Everything broken still holds its original shape somewhere inside... We just have to remember what that shape was."
		]
	},
	{
		'npc_id': 'marlo_finch',
		'dialog_id': 'marlo_finch_ch16_sends_off',
		'dialog': [
			"You're one of the few who still carries that truth. Hold it tightly. You'll need it in there."
		]
	},
	{
		'npc_id': 'crux',
		'dialog_id': 'crux_ch16_intro',
		'dialog': [
			"(A voice of static and shattered glass) You seek meaning in a system designed to erase it. You are the error. The contradiction."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch16_to_crux',
		'dialog': [
			"Call me an error one more time and I'll show you what a real disciplined mistake looks like!"
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch16_to_crux',
		'dialog': [
			"If I am an error in your eyes... then let me be a faithful one. I choose to believe anyway."
		]
	},
	{
		'npc_id': 'crux',
		'dialog_id': 'crux_ch16_taunts_discipline_faith',
		'dialog': [
			"Discipline without purpose is just violence wearing a uniform. You are empty, Chock. Admit it.",
			"Faith in nothing is delusion. Your gods abandoned this place long ago."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch16_to_crux',
		'dialog': [
			"Being a contradiction is my brand! Let's see how you like it when I make this paradox *scream*!"
		]
	},
	{
		'npc_id': 'crux',
		'dialog_id': 'crux_ch16_taunts_magic',
		'dialog': [
			"Your chaos is hollow without structure to rebel against. Even you grow tired of screaming into the void."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch16_to_crux',
		'dialog': [
			"Fine. Then I'll become the variable you cannot predict or contain."
		]
	},
	{
		'npc_id': 'crux',
		'dialog_id': 'crux_ch16_taunts_tech',
		'dialog': [
			"Your precious long-term vision ends here. All futures collapse into the same gray nothing."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch16_to_crux',
		'dialog': [
			"Then strike. I choose to move even when movement has no purpose."
		]
	},
	{
		'npc_id': 'crux',
		'dialog_id': 'crux_ch16_taunts_skill',
		'dialog': [
			"Movement without direction is just falling with style. You are already lost."
		]
	},
	{
		'npc_id': 'crux',
		'dialog_id': 'crux_ch16_fading',
		'dialog': [
			"(fading, voice glitching) You... cannot erase me... I am the first wound... I will always be inside you now..."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'ch16_narrator_after_crux',
		'dialog': [
			"As Crux dissipates, the Spire's impossible geometry settles into stable, silent ruins. The oppressive quiet remains."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch16_after_crux',
		'dialog': [
			"(breathing heavily) ...For a second I didn't care if I won or lost. That's new. And I don't like it."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch16_after_crux',
		'dialog': [
			"The flow returns... but it's different now. Self-made. Earned."
		]
	},
	{
		'npc_id': 'kor_in',
		'dialog_id': 'kor_in_ch16_after_crux',
		'dialog': [
			"(quietly) My dreams feel... lighter. But I'm not sure if that's hope or just exhaustion."
		]
	},
	{
		'npc_id': 'vek',
		'dialog_id': 'vek_ch16_after_crux',
		'dialog': [
			"We held the line. That's something. In a place like this, choosing to keep going *is* the meaning."
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_ch16_after_crux',
		'dialog': [
			"(adjusting goggles) Fascinating. Even nothingness has a pattern if you stare long enough."
		]
	},
	{
		'npc_id': 'marlo_finch',
		'dialog_id': 'marlo_finch_ch16_again',
		'dialog': [
			"You're back. I felt the shift in the Spire from here. You actually confronted Crux...",
			"The Spire is stable for now, but the paradox remains. Crux didn't die. It just burrowed deeper.",
			"It's a part of you now - all of you. It will always be a part of you. But it doesn't have to define you."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch16_to_marlo_again',
		'dialog': [
			"(cold, analytical) Easier said than done. My systems are still throwing errors. I can't get a clear read on where we go next."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch16_to_marlo_again',
		'dialog': [
			"The path is gone. No flow. No direction. Only silence."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch16_to_marlo_again',
		'dialog': [
			"Great. We punched the hole in reality and now there's just... nothing. What the hell are we supposed to do with \"nothing\"?"
		]
	},
	{
		'npc_id': 'vek',
		'dialog_id': 'vek_ch16_rallies',
		'dialog': [
			"(trying to rally) Then we make our own path. We've done it before."
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_ch16_mutters',
		'dialog': [
			"(muttering) Even entropy feels... muted here. Like the universe is holding its breath."
		]
	},
	{
		'npc_id': 'marlo_finch',
		'dialog_id': 'marlo_finch_ch16_final',
		'dialog': [
			"(shaking his head slowly) I wish I had clearer answers. The Bracelets brought us here for a reason, but that reason feels... obscured now."
		]
	}
]

TASKS = [
	{
		'task_id': 'main_story_ch16_meet_lumen',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'lumen',
		'task_acquire_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch16_narrator_intro' }},
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'lumen', 'location': 'region_city_inn' }},
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'jessa', 'location': 'region_city_shopitems' }},
			{ 'event_type': 'show_npc', 'params': { 'npc_id': 'marlo_finch', 'location': 'region_city_shoparmor' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'jessa', 'standing_text': ["I record memories, but they contradict. What is truth when every story is different?"]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'marlo_finch', 'standing_text': ["Now I see YOU here, I think I understand why I am... I'm pretty sure during that last fracture the Bracelet of Void Brought me here... To that of Existence"]}},
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'scribe_halden', 'location': 'city_number_17_region_city_inn' }},
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'vex', 'location': 'city_number_17_region_city_bar' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'scribe_halden', 'standing_text': ["Compliance is mandatory. Non-compliance is impossible. You are already in violation."]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'vex', 'standing_text': ["Every rule has a loophole. The tighter the system, the bigger the cracks. I live in the cracks."]}},
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'rhea', 'location': 'city_number_18_region_city_inn' }},
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'korr', 'location': 'city_number_18_region_city_shoparmor' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rhea', 'standing_text': ["If you listen closely, each reset sounds a little different... like the world is trying to remember something it lost."]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'korr', 'standing_text': ["The world resets, but my resolve doesn't. That's why I'm still alive."]}},
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'soren', 'location': 'city_number_19_region_city_inn' }},
			{ 'event_type': 'show_npc', 'params': { 'npc_id': 'jinn', 'location': 'city_number_19_region_city_shopitems' }},
			{ 'event_type': 'show_npc', 'params': { 'npc_id': 'astra_wynn', 'location': 'city_number_19_region_city_shoparmor' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'soren', 'standing_text': ["People think the past is gone. But it lingers. It clings. It shapes."]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'jinn', 'standing_text': ["Prophecy lenses! See your doom in crystal clarity! Half price today! Look, the Oracle's at the heart of the Prophetic Spiral. But it's guarded by a nasty piece of work: the Reliquary. It's a living archive of every wound and failure this world has ever known."]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'astra_wynn', 'standing_text': ["This place is a storm of futures. The Oracle is trying to collapse them all into a single, doomed timeline. I can create a stable anchor, a safe future, but it will take all my energy."]}},
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'curator_lysa', 'location': 'city_number_20_region_city_inn' }},
			{ 'event_type': 'show_npc', 'params': { 'npc_id': 'drin', 'location': 'city_number_20_region_city_shopitems' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'curator_lysa', 'standing_text': ["Some futures scream. Some futures beg. The worst ones are silent."]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'drin', 'standing_text': ["Memories can be weapons. Or illusions. The past is a battlefield here."]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lumen', 'dialog_id': 'lumen_ch16_intro' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch16_on_silence' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch16_on_silence' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch16_on_silence' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lumen', 'dialog_id': 'lumen_ch16_response' }},
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'temporal_echoes', 'location': 'region_open_area' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'temporal_echoes', 'item_id': 'fracture_logs', 'location': 'final_chamber' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch16_deliver_fracture_logs_to_jessa' }}
		]
	},
	{
		'task_id': 'main_story_ch16_deliver_fracture_logs_to_jessa',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'jessa',
		'item_id': 'fracture_logs',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'jessa', 'dialog_id': 'jessa_ch16_receives_logs' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_ch16_on_memory' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'jessa', 'dialog_id': 'jessa_ch16_persists' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch16_on_chaos' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'jessa', 'dialog_id': 'jessa_ch16_doubts' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch16_on_records' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch16_on_records' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'jessa', 'dialog_id': 'jessa_ch16_directs' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch16_meet_marlo_finch' }}
		]
	},
	{
		'task_id': 'main_story_ch16_meet_marlo_finch',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'marlo_finch',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch16_intro' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch16_to_marlo' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch16_to_marlo' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch16_explains_crux' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch16_to_marlo' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch16_offers' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch16_to_marlo' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch16_after_marlo_explains' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch16_after_marlo_explains' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren_vale', 'dialog_id': 'lyren_vale_ch16_to_marlo' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch16_sends_off' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch16_meet_crux_origin_form' }}
		]
	},
	{
		'task_id': 'main_story_ch16_meet_crux_origin_form',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'crux',
		'task_acquire_events': [
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'crux', 'location': None }},
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'origin_spire', 'location': 'region_city_district' }}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch16_intro' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch16_to_crux' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch16_to_crux' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch16_taunts_discipline_faith' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch16_to_crux' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch16_taunts_magic' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch16_to_crux' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch16_taunts_tech' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch16_to_crux' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch16_taunts_skill' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch16_defeat_crux_origin_form' }}
		]
	},
	{
		'task_id': 'main_story_ch16_defeat_crux_origin_form',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'crux_origin_1',
		'task_acquire_events': [
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'crux_origin_1', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'hide_npc', 'params': { 'npc_id': 'crux' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch16_fading' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch16_narrator_after_crux' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch16_after_crux' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch16_after_crux' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'kor_in', 'dialog_id': 'kor_in_ch16_after_crux' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch16_after_crux' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch16_after_crux' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch16_meet_marlo_finch_again' }}
		]
	},
	{
		'task_id': 'main_story_ch16_meet_marlo_finch_again',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'marlo_finch',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch16_again' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch16_to_marlo_again' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch16_to_marlo_again' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch16_to_marlo_again' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch16_rallies' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch16_mutters' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch16_final' }},
			{ 'event_type': 'advance_chapter' }
		]
	}
]

PRIMARY_STORY_SETTINGS = {
	'chapter_id': 'main_story_chapter_16',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}
