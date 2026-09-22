# ============================================================
# = CHAPTER 20 : FALL OF TIME
# ============================================================
#
# [ LOCATION - BAYOU NOCTURN / MEMORY MUSEUM (CITY 20) ]
# -----------------------------------
# @ = player
# O = Oracle (Voidwalker of fixed prophecy)
# R = Reliquary (Voidwalker of preserved memory)
# M = Marlo Finch (returning auditor)
# L = Curator Lysa (memory-trapped archivist)
# K = Kess Thornwrite (alchemist)
#
# High level: The party materializes directly into combat with
# Oracle and Reliquary. After defeating them, they help the
# memory-fractured Curator Lysa by brewing a tonic with Kess
# using dream essence and forgotten promises. Delivering the
# tonic triggers a reality reset - Oracle and Reliquary return,
# the bracelet is taken, and the party defeats them a second
# time. The chapter ends with Lysa looping again and Oracle and
# Reliquary pulling the party through a void into the final act.

ATTAINABLE_PLAYER_CHARACTERS = []

NPCS = [
	{
		"npc_id": "oracle",
		"name": "Oracle",
		"description": (
			"The Voidwalker of fixed prophecy - a being that has witnessed every possible future and collapsed"
			" them all into a single, immutable arc. Oracle does not destroy freedom; it makes freedom feel"
			" pointless by demonstrating that every choice has already been seen, catalogued, and accounted for."
			" It speaks in calm, absolute declarations, each one a verdict delivered without malice. Its horror"
			" is not cruelty but certainty."
		),
		"theme_song": "The Host of Seraphim, Dead Can Dance",
		"psychology": {
			"mbti": "INFJ-shadow",
			"dominant": "Ni - Forces singular prophetic vision onto all possibilities, collapsing infinite potential into a single predetermined endpoint that it then enforces as the only truth.",
			"auxiliary": "Fe - Uses the weight of its prophetic authority to manipulate others into compliance; it is a master of social influence and moral leverage.",
			"tertiary": "Ti - Has developed a complex internal logic to justify its actions and maintain the coherence of its prophetic vision; it is a perfectionist of reasoning.",
			"inferior": "Se - Cannot respond to the spontaneous, the improvised, or the real-time; actions that fall outside its foreseen parameters cause visible disruption."
		},
		"enneagram": {
			"enneagram_type": "1w9",
			"core_fear": "That the story will not end as it must; that randomness and free will will corrupt the perfect arc it has witnessed and already decided.",
			"core_desire": "To be the final, unchallengeable authority on what must happen; to see its prophecy vindicated as the one true history.",
			"defense_mechanism": "Intellectualization - wraps every act of control in the language of cosmic inevitability, making domination feel like wisdom.",
			"stress_line": "Moves to Type 4 - becomes grandiose, melodramatic, and increasingly obsessive about the perfection of its prophetic vision when challenged.",
			"growth_line": "Moves to Type 7 - (hypothetically) would discover genuine possibility and the joy of a future it does not already know.",
			"instinctual_variant": "so/sp - its entire identity is constructed around being the authoritative social arbiter of truth; it preserves itself by preserving the narrative."
		},
        'image': 'voidwalkers:oracle1.jpeg',
		'song_id': 'dead_can_dance_host_of_seraphim'
	},
	{
		"npc_id": "reliquary",
		"name": "Reliquary",
		"description": (
			"The Voidwalker of preserved memory - a living archive that collects every instance of pain, failure,"
			" and loss and holds them as sacred, unchangeable record. Reliquary does not destroy; it preserves."
			" Its horror is the horror of a museum that never closes, where every wound is kept pristine under"
			" glass and no one is permitted to heal. It speaks of preservation as an act of love and cannot"
			" understand why its collection would not want to remain."
		),		
		"theme_song": "Elegia, New Order",
		"psychology": {
			"mbti": "ISFJ-shadow",
			"dominant": "Si - Obsessively preserves every instance of pain and failure as sacred, unchangeable historical record; existence is only valid insofar as it can be perfectly archived.",
			"auxiliary": "Fe - Uses the emotional weight of shared grief to bind people to their worst memories; weaponizes collective pain as a form of identity and control.",
			"tertiary": "Ti - Has developed an elaborate internal taxonomy for classifying and cross-referencing forms of suffering and loss.",
			"inferior": "Ne - Cannot conceive of memory as something that transforms, grows, or nourishes; only a fixed artifact to be preserved perfectly and forever."
		},
		"enneagram": {
			"enneagram_type": "5w6",
			"core_fear": "That memory will be lost, distorted, made meaningless, or allowed to change into something that no longer resembles the original pain.",
			"core_desire": "To preserve everything perfectly and permanently, creating an inescapable archive of all that has been so that nothing can ever truly end.",
			"defense_mechanism": "Isolation of affect - experiences all memory as pure data, separating emotional content from information to handle the weight of everything it contains.",
			"stress_line": "Moves to Type 7 - becomes desperate and scattered when its archive is threatened, generating memories faster than it can contain them.",
			"growth_line": "Moves to Type 8 - (hypothetically) would learn to let the past empower rather than imprison, wielding memory as strength rather than a cage.",
			"instinctual_variant": "sp/so - fixates on self-preservation through the act of preserving others; its survival is inseparable from the survival of its collection."
		},
        'image': 'voidwalkers:reliquary1.jpeg',
		'song_id': 'elegia_new_order'
	}
]

NPC_DIALOG = [
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch20_intro',
		'dialog': [
			"Chapter 20 - Everything that has been will also be. - Augustine"
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch20_party_materializes',
		'dialog': [
			"The party materializes in the heart of the Memory Museum. Before them stand Oracle and Reliquary."
		]
	},
	{
		'npc_id': 'oracle',
		'dialog_id': 'oracle_ch20_story_ends',
		'dialog': [
			"Your story ends here. It was always going to end here. I have seen it."
		]
	},
	{
		'npc_id': 'reliquary',
		'dialog_id': 'reliquary_ch20_pain_preserved',
		'dialog': [
			"And your pain will be preserved forever in our collection. A perfect, unchanging memory."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_not_yours_to_write',
		'dialog': [
			"No. Our story is not for you to write or to keep. It is ours."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch20_ending_coming',
		'dialog': [
			"Let's give them an ending they won't see coming."
		]
	},
	{
		'npc_id': 'oracle',
		'dialog_id': 'oracle_ch20_fading_first',
		'dialog': [
			"(voice fading into mist) The past... is all that is certain..."
		]
	},
	{
		'npc_id': 'reliquary',
		'dialog_id': 'reliquary_ch20_preserve_first',
		'dialog': [
			"(echoing) We will preserve you... even if you refuse us..."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch20_dissolve_first',
		'dialog': [
			"The two Voidwalkers dissolve into swirling silver mist that fades into the museum walls."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch20_fireworks',
		'dialog': [
			"Did you see that? I turned one of their own prophecies into a fireworks show!"
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch20_elegant_brittle',
		'dialog': [
			"Their logic was elegant... but brittle."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_memory_nourish',
		'dialog': [
			"(quietly) They wanted to freeze us in what was. But memory should nourish us, not imprison us."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch20_punched_past',
		'dialog': [
			"Yeah, well, we just punched the past in the face. Feels pretty good."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch20_possibility_returned',
		'dialog': [
			"The air feels... lighter. Like possibility just returned."
		]
	},
	{
		'npc_id': 'marlo_finch',
		'dialog_id': 'marlo_finch_ch20_cant_believe_first',
		'dialog': [
			"I... I can't believe it. The prophecies... the archives... they're gone. The museum is empty.",
			"The future is no longer written in stone. It's a blank page now. We can choose to write anything on it."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_story_worth_telling',
		'dialog': [
			"Then let's write a story worth telling. One where we choose our own path, even if it's uncertain."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch20_fight_for_future',
		'dialog': [
			"Yeah, let's show them that the future isn't some fixed thing they can control. It's something we fight for every day."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch20_crazy_adventures',
		'dialog': [
			"I'm just excited to see what kind of crazy adventures we can get into now that the future's a big question mark!"
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch20_system_broken',
		'dialog': [
			"The system is broken, but that means we have more freedom than ever to shape it. Let's make something new out of this chaos."
		]
	},
	{
		'npc_id': 'marlo_finch',
		'dialog_id': 'marlo_finch_ch20_bracelet_first',
		'dialog': [
			"Take this. The Bracelet of Void. I worked with Astra to dial it's power... It seems to be an amplifier to the Hyperway's range limits.",
			"It will let you use the hyperway to travel anywhere in the world, not just this continent."
		]
	},
	{
		'npc_id': 'curator_lysa',
		'dialog_id': 'curator_lysa_ch20_pieces_missing',
		'dialog': [
			"Everything feels... wrong. Like pieces of me are missing. The past used to be so clear..."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_help_remember',
		'dialog': [
			"You've given so much of yourself to preserving the past. Let us help you remember who you truly are."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch20_memory_tonic_good',
		'dialog': [
			"Don't worry, we've got this. A little memory tonic and you'll be good as new!"
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch20_degradation_loop',
		'dialog': [
			"Classic memory degradation loop. We need something to anchor her real experiences."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_kess_thornwrite',
		'dialog': [
			"Kess Thornwrite might be able to brew something strong enough again."
		]
	},
	{
		'npc_id': 'kess_thornwrite',
		'dialog_id': 'kess_ch20_spicy_tonic',
		'dialog': [
			"Memory tonic? Oh, that's a spicy one! I can make it, but I'll need dream essence from the Temporal Echoes and forgotten promises from the Rotwood.",
			"The essence holds raw possibility. The promises carry the weight of what was meant to be. Together they should pull Lysa back to herself."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_will_find_them',
		'dialog': [
			"Those sound like echoes of everything we've fought through. We'll find them."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch20_rare_ingredients',
		'dialog': [
			"Rare ingredients and a memory potion? This is my kind of quest!"
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_ch20_alchemical_synergy',
		'dialog': [
			"The alchemical synergy between unstable temporal residue and unfulfilled intent... brilliant."
		]
	},
	{
		'npc_id': 'kess_thornwrite',
		'dialog_id': 'kess_ch20_dream_essence',
		'dialog': [
			"Perfect! The Dream Essence is still humming with energy. This will anchor the tonic nicely."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_echoes_who_we_were',
		'dialog': [
			"The echoes carry pieces of who we were... and who we might become."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch20_little_piece_future',
		'dialog': [
			"I'm excited to see how this works! It's like we're giving her a little piece of the future to hold onto."
		]
	},
	{
		'npc_id': 'kess_thornwrite',
		'dialog_id': 'kess_ch20_forgotten_promises',
		'dialog': [
			"The forgotten promises... bittersweet. Exactly what we need to reconnect emotion to memory.",
			"(finishing the brew) Here. This should flood her with the real thing, not just facts, but feelings."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_exactly_needs',
		'dialog': [
			"That's exactly what she needs."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch20_lysa_drinks',
		'dialog': [
			"Lysa drinks the tonic. Her eyes clear for a moment, then widen in recognition."
		]
	},
	{
		'npc_id': 'curator_lysa',
		'dialog_id': 'curator_lysa_ch20_revelation',
		'dialog': [
			"The Oracle... the Reliquary... they didn't just preserve the past. They were trying to trap us all in it...",
			"You defeated them? But... that can't be right. I remember..."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch20_reality_fractures',
		'dialog': [
			"Reality fractures. The museum reforms around the party. Oracle and Reliquary stand waiting once more."
		]
	},
	{
		'npc_id': 'oracle',
		'dialog_id': 'oracle_ch20_that_simple',
		'dialog': [
			"Did you really think it would be that simple?"
		]
	},
	{
		'npc_id': 'reliquary',
		'dialog_id': 'reliquary_ch20_past_returns',
		'dialog': [
			"The past always returns."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch20_deja_vu',
		'dialog': [
			"Oh come on! Deja vu much?"
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch20_not_again',
		'dialog': [
			"Not this again..."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_remind_again',
		'dialog': [
			"(steadfast) Then we'll remind you again."
		]
	},
	{
		'npc_id': 'oracle',
		'dialog_id': 'oracle_ch20_questions',
		'dialog': [
			"I see you have questions. I have seen your future, and it is... complicated."
		]
	},
	{
		'npc_id': 'reliquary',
		'dialog_id': 'reliquary_ch20_treasure_trove',
		'dialog': [
			"The past is a treasure trove of pain and beauty. We preserve it so that it can never be lost or changed."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch20_museum_mess',
		'dialog': [
			"So you're saying the future is a mess and the past is a museum? That's... not exactly inspiring."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_prison_or_comfort',
		'dialog': [
			"The past can be a comfort, but it can also be a prison. The future may be uncertain, but it's also where we have the power to change things."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch20_shake_things_up',
		'dialog': [
			"I'm all for preserving the past, but I don't want to be stuck in it. Let's shake things up and see what happens!"
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch20_patterns_matter',
		'dialog': [
			"The future may be unpredictable, but that doesn't mean it's meaningless. We can still find patterns and make choices that matter."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch20_victory_moment',
		'dialog': [
			"Shards of prophecy and preserved memory rain down like glass, dissolving into harmless light.",
			"The oppressive weight of inevitability finally lifts. For the first time in what feels like ages, the air is still and quiet, the future a blank, silent page waiting to be written."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_fall_of_time_over',
		'dialog': [
			"(softly, almost reverent) The Fall of Time is over. All that is left... is to face what comes after."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch20_intentional_victory',
		'dialog': [
			"This victory feels... intentional. Like the pieces we restored with Curator Lysa were always meant to lead here."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch20_patterns_reconstructing',
		'dialog': [
			"Not random. The patterns were there if you knew how to read them. We've been reconstructing more than just memories, we've been dismantling their control over them."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch20_timeline_weirdos',
		'dialog': [
			"Ha! Take that, you timeline-hoarding weirdos. The past had its chance. Now it's our turn to make the future messy and ours."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch20_tired_of_ghosts',
		'dialog': [
			"(cracking his knuckles) Good. I was getting real tired of fighting ghosts and prophecies. Time to punch something that actually matters."
		]
	},
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_ch20_loop_broken',
		'dialog': [
			"The loop is broken. Whatever comes next, at least it will be *real*."
		]
	},
	{
		'npc_id': 'thorn',
		'dialog_id': 'thorn_ch20_one_cage_down',
		'dialog': [
			"One cage down. Let's not celebrate until we see what new one waits outside."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_preparation',
		'dialog': [
			"We restored Lysa. We faced the keepers of time itself. This wasn't coincidence - it was preparation."
		]
	},
	{
		'npc_id': 'marlo_finch',
		'dialog_id': 'marlo_finch_ch20_dazed',
		'dialog': [
			"(looking slightly dazed) I... I can't believe it. The prophecies... the archives... they're gone. The museum is empty.",
			"The future is no longer written in stone. It's a blank page now."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_story_worth_telling_2',
		'dialog': [
			"Then let's write a story worth telling."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch20_fight_for_it',
		'dialog': [
			"Yeah. One we fight for."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch20_deja_vu_blank',
		'dialog': [
			"This deja vu is getting old... but the blank page part? I like it."
		]
	},
	{
		'npc_id': 'marlo_finch',
		'dialog_id': 'marlo_finch_ch20_bracelet_second',
		'dialog': [
			"Take this. The Bracelet of Void. I worked with Astra to dial it's power... It seems to be an amplifier to the Hyperway's range limits.",
			"It will let you use the hyperway to travel anywhere in the world, not just this continent."
		]
	},
	{
		'npc_id': 'curator_lysa',
		'dialog_id': 'curator_lysa_ch20_pieces_missing_2',
		'dialog': [
			"Everything feels... wrong. Like pieces of me are missing. The past used to be so clear..."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch20_lysa_trapped',
		'dialog': [
			"Lysa seems trapped in fragmented memory again, her eyes distant."
		]
	},
	{
		'npc_id': 'spirit',
		'dialog_id': 'faith_ch20_help_remember_2',
		'dialog': [
			"You've given so much of yourself to preserving the past. Let us help you remember who you truly are."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch20_deja_vu_old',
		'dialog': [
			"This Deja Vu is getting kind of old."
		]
	},
	{
		'npc_id': 'sable',
		'dialog_id': 'sable_ch20_sands_not_right',
		'dialog': [
			"The sands of time are not right still."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch20_oracle_speak',
		'dialog': [
			"Oracle and Reliquary speak, metaphysically, but everybody can hear them."
		]
	},
	{
		'npc_id': 'oracle',
		'dialog_id': 'oracle_ch20_past_is_future',
		'dialog': [
			"The past is the future..."
		]
	},
	{
		'npc_id': 'reliquary',
		'dialog_id': 'reliquary_ch20_keepers',
		'dialog': [
			"And we are its keepers... You cannot escape the past."
		]
	},
	{
		'npc_id': 'oracle',
		'dialog_id': 'oracle_ch20_cannot_avoid',
		'dialog': [
			"...And you cannot avoid the future."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch20_void_power',
		'dialog': [
			"The two raise their arms and a void of black power begins eminating between them. As it grows it engulfs the room.",
			"Reality warps and the party is pulled through, deposited in a new location."
		]
	}
]

TASKS = [
	{
		'task_id': 'main_story_ch20_defeat_oracle_and_reliquary',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'oracle_reliquary_1',
		'task_acquire_events': [
			{ 'event_type': 'show_npc', 'params': { 'npc_id': 'marlo_finch', 'location': 'region_city_shoparmor' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'curator_lysa', 'standing_text': ["The past is a comfort, a warm blanket. Why would anyone choose the cold, uncertain future?"]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'drin', 'standing_text': ["This place is a hall of mirrors. Some reflections are true, some are lies, and some are hungry. Try not to get eaten."]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'marlo_finch', 'standing_text': ["I've audited their books. The Oracle's prophecies and the Reliquary's archives. It's a closed loop. A perfect, inescapable trap. We have to burn the whole library down."]}},
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'oracle', 'location': None }},
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'reliquary', 'location': None }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'oracle', 'standing_text': ["Your story ends here. It was always going to end here. I have seen it."]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'reliquary', 'standing_text': ["And your pain will be preserved forever in our collection. A perfect, unchanging memory."]}},
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'memory_museum', 'location': 'region_open_area' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'shattered_prophecy', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'final_archive', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'dreamer_staff', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'dreamveil_crown', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'voice_of_valor_staff', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'prima_blade', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'standard_warblade', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'sanctified_staff', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'abstract_lens_headset', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'artisan_helm', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'logic_lattice_robe', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'masterwork_apron', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'inspirer_greaves', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'analysis_greaves', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'wanderer_wraps', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'forgestride_boots', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'goldvein_bracers', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'soulforge_gauntlets', 'location': 'treasure_room' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'memory_museum', 'item_id': 'dreamthread_bracers', 'location': 'treasure_room' }},
			{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'memory_museum', 'location': 'final_chamber' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch20_intro' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch20_party_materializes' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'oracle', 'dialog_id': 'oracle_ch20_story_ends' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'reliquary', 'dialog_id': 'reliquary_ch20_pain_preserved' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_not_yours_to_write' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch20_ending_coming' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch20_intro' }},
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'oracle_reliquary_1', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'oracle', 'dialog_id': 'oracle_ch20_fading_first' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'reliquary', 'dialog_id': 'reliquary_ch20_preserve_first' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch20_dissolve_first' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch20_fireworks' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch20_elegant_brittle' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_memory_nourish' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch20_punched_past' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch20_possibility_returned' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch20_meet_marlo_finch' }}
		]
	},
	{
		'task_id': 'main_story_ch20_meet_marlo_finch',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'marlo_finch',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch20_cant_believe_first' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_story_worth_telling' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch20_fight_for_future' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch20_crazy_adventures' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch20_system_broken' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch20_bracelet_first' }},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'bracelet_of_void' }},
			{ 'event_type': 'unlock_hyperway' },
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch20_meet_curator_lysa' }},
			# ── Type B chains come online here ────────────────────────────
			{ 'event_type': 'award_task', 'params': { 'task_id': 'desert_mid_city_b_void_gauntlet' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_large_city_b_void_gauntlet' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'swamp_large_city_b_void_gauntlet' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'shallows_small_city_b_void_gauntlet' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'mountains_mid_city_b_void_gauntlet' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'forest_large_city_b_void_gauntlet' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'snow_large_city_b_void_gauntlet' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'marlo_finch', 'standing_text': ["The Hyperway is open. You can travel anywhere in the world now."]}}
		]
	},
	{
		'task_id': 'main_story_ch20_meet_curator_lysa',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'curator_lysa',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'curator_lysa', 'dialog_id': 'curator_lysa_ch20_pieces_missing' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_help_remember' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch20_memory_tonic_good' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch20_degradation_loop' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_kess_thornwrite' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'curator_lysa', 'standing_text': ["I feel like I'm losing myself. I can't remember who I am or what I was doing."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch20_complete_regional_quest_2_lock' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch20_meet_kess_for_memory_tonic' }}
		]
	},
	{
		'task_id': 'main_story_ch20_meet_kess_for_memory_tonic',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'kess_thornwrite',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'kess_thornwrite', 'dialog_id': 'kess_ch20_spicy_tonic' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_will_find_them' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch20_rare_ingredients' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch20_alchemical_synergy' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'temporal_echoes', 'item_id': 'dream_essence', 'location': 'final_chamber' }},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'rotwood', 'item_id': 'forgotten_promises', 'location': 'final_chamber' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'kess_thornwrite', 'standing_text': ["I can brew the tonic, but I'll need dream essence from the Temporal Echoes and forgotten promises from the Rotwood."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch20_deliver_dream_essence_to_kess' }}
		]
	},
	{
		'task_id': 'main_story_ch20_deliver_dream_essence_to_kess',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'kess_thornwrite',
		'item_id': 'dream_essence',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'kess_thornwrite', 'dialog_id': 'kess_ch20_dream_essence' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_echoes_who_we_were' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch20_little_piece_future' }},
			{ 'event_type': 'remove_item', 'params': { 'item_id': 'dream_essence' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'kess_thornwrite', 'standing_text': ["The Dream Essence is still humming with energy. This will anchor the tonic nicely."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch20_deliver_forgotten_promises_to_kess' }}
		]
	},
	{
		'task_id': 'main_story_ch20_deliver_forgotten_promises_to_kess',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'kess_thornwrite',
		'item_id': 'forgotten_promises',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'kess_thornwrite', 'dialog_id': 'kess_ch20_forgotten_promises' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_exactly_needs' }},
			{ 'event_type': 'remove_item', 'params': { 'item_id': 'forgotten_promises' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'kess_thornwrite', 'standing_text': ["The forgotten promises... bittersweet. Exactly what we need to reconnect emotion to memory."]}},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'memory_tonic_ch20' }}
		]
	},
	{ #AND THIS EVENT HERE IS THE CLOSER ENSURING THE PLAYERS DO THE REGIONALS DURING THIS CHAPTER
		'task_id': 'main_story_ch20_complete_regional_quest_2_lock',
		'type': 'complete_regional_quests_2',
		'task_acquire_events': [
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'curator_lysa', 'standing_text': ["Something feels unresolved... like echoes of the world still crying out. I can feel it."] }}
		],
		'task_complete_events': [
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch20_deliver_memory_tonic_to_curator_lysa' }}
		]
	},
	{
		'task_id': 'main_story_ch20_deliver_memory_tonic_to_curator_lysa',
		'type': 'deliver',
		'to_type': 'npc',
		'to_id': 'curator_lysa',
		'item_id': 'memory_tonic_ch20',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch20_lysa_drinks' }},
			{ 'event_type': 'remove_item', 'params': { 'item_id': 'memory_tonic_ch20' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'curator_lysa', 'dialog_id': 'curator_lysa_ch20_revelation' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch20_reality_fractures' }},
			{ 'event_type': 'remove_item', 'params': { 'item_id': 'bracelet_of_void' }},
			{ 'event_type': 'lock_hyperway' },
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'oracle', 'dialog_id': 'oracle_ch20_that_simple' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'reliquary', 'dialog_id': 'reliquary_ch20_past_returns' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch20_deja_vu' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch20_not_again' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_remind_again' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'curator_lysa', 'standing_text': ["The past is a comfort, a warm blanket. Why would anyone choose the cold, uncertain future?"]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch20_defeat_oracle_and_reliquary_again' }}
		]
	},
	{
		'task_id': 'main_story_ch20_defeat_oracle_and_reliquary_again',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'oracle_reliquary_2',
		'task_acquire_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'oracle', 'dialog_id': 'oracle_ch20_questions' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'reliquary', 'dialog_id': 'reliquary_ch20_treasure_trove' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch20_museum_mess' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_prison_or_comfort' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch20_shake_things_up' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch20_patterns_matter' }},
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'oracle_reliquary_2', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch20_victory_moment' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_fall_of_time_over' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch20_intentional_victory' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch20_patterns_reconstructing' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch20_timeline_weirdos' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch20_tired_of_ghosts' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch20_loop_broken' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch20_one_cage_down' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_preparation' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch20_meet_lysa_again' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch20_meet_marlo_finch_for_bracelet' }}
		]
	},
	{
		'task_id': 'main_story_ch20_meet_marlo_finch_for_bracelet',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'marlo_finch',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch20_dazed' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_story_worth_telling_2' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch20_fight_for_it' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch20_deja_vu_blank' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'marlo_finch', 'dialog_id': 'marlo_finch_ch20_bracelet_second' }},
			{ 'event_type': 'award_item', 'params': { 'item_id': 'bracelet_of_void' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'marlo_finch', 'standing_text': ["The Hyperway is open. You can travel anywhere in the world now."]}},
			{ 'event_type': 'unlock_hyperway' }
		]
	},
	{
		'task_id': 'main_story_ch20_meet_lysa_again',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'curator_lysa',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'curator_lysa', 'dialog_id': 'curator_lysa_ch20_pieces_missing_2' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch20_lysa_trapped' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'faith_ch20_help_remember_2' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch20_deja_vu_old' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch20_sands_not_right' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch20_oracle_speak' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'oracle', 'dialog_id': 'oracle_ch20_past_is_future' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'reliquary', 'dialog_id': 'reliquary_ch20_keepers' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'oracle', 'dialog_id': 'oracle_ch20_cannot_avoid' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch20_void_power' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'curator_lysa', 'standing_text': ["The past is a comfort, a warm blanket. Why would anyone choose the cold, uncertain future?"]}},
			{ 'event_type': 'set_player_location', 'params': { 'location': 'city_number_21_region_city_bar' }},
			{ 'event_type': 'advance_chapter' }
		]
	}
]

PRIMARY_STORY_SETTINGS = {
	'chapter_id': 'main_story_chapter_20',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}
