# ============================================================
# = CHAPTER 18 : CATACLYSM
# ============================================================
#
# [ LOCATION - FROSTGATE SPIRE (CITY 18) ]
# -----------------------------------
# @ = player
# K = Korr (resolute armor shop survivor)
# R = Rhea (loop-sensitive resident)
# V = Velka (cartographer, returning NPC)
# C = Cataclysm (Voidwalker of ordered collapse)
#
# High level: The party arrives in a city undergoing methodical,
# perfectly scheduled self-destruction. Korr and Rhea help them
# locate the source — Cataclysm, a colossal titan of living
# collapse that judges existence itself as inefficient. They
# confront and defeat it, before Korr directs them onward to
# Aurelion Veil and the memories that survive there.

ATTAINABLE_PLAYER_CHARACTERS = []

NPCS = [
	{
		"npc_id": "cataclysm",
		"name": "Cataclysm",
		"description": (
			"A colossal titan of living collapse whose form is made of perfectly ordered fracturing geometry."
			" Cataclysm does not hate life — it simply classifies life as an inefficiency in the equation and"
			" schedules its correction with the cold, procedural certainty of a bureaucratic system that has"
			" achieved total self-belief. It speaks in declarative, all-caps proclamations, each one a verdict."
		),
		"theme_song": "Immediate Music, Darkness on the Edge of Power",
		"psychology": {
			"mbti": "ISTJ-shadow",
			"dominant": "Si - Enforces an eternal, unchangeable protocol of ordered collapse, treating the accumulated inefficiencies of existence as violations requiring systematic correction.",
			"auxiliary": "Te - Executes the scheduled unmaking with absolute procedural efficiency, issuing verdicts and carrying out corrections without deviation or hesitation.",
			"tertiary": "Fi - Has no personal values or emotional code; its only moral framework is the protocol itself.",
			"inferior": "Ne - Cannot conceive of existence outside the equation; purposeful, creative chaos is classified as an anomaly to be eliminated."
		},
		"enneagram": {
			"enneagram_type": "1w9",
			"core_fear": "That imperfection, waste, and inefficiency will persist uncorrected — that the equation will remain permanently unbalanced.",
			"core_desire": "To achieve a perfect, final equilibrium where all inefficiency has been eliminated and the system is at rest.",
			"defense_mechanism": "Reaction Formation — Transforms its drive toward annihilation into a belief that it is performing an act of cosmic righteousness, correcting the universe's ledger.",
			"stress_line": "Moves to Type 4 — Becomes cold, withdrawn, and increasingly singular in focus as resistance to its protocol mounts.",
			"growth_line": "Moves to Type 7 — (Hypothetically) Would discover that existence has value beyond efficiency, and that the equation includes beauty.",
			"instinctual_variant": "sp/so — Operates entirely on systemic self-preservation logic; its social mandate is the enforcement of ordered collapse on all things."
		},
        'image': 'voidwalkers:cataclysm1.jpeg',
		'song_id': 'darkness_on_the_edge_of_power_immediate_music'
	}
]

NPC_DIALOG = [
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch18_intro',
		'dialog': [
			"Chapter 18 - When a system knows it is broken, destroying itself is the only honest act left."
		]
	},
	{
		'npc_id': 'korr',
		'dialog_id': 'korr_ch18_intro',
		'dialog': [
			"Something is deep within this city. Something that never sleeps. Something that sees failure and eliminates it.",
			"It does not rage. It does not scream. It simply judges existence itself as inefficient and begins the scheduled unmaking."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch18_big_one',
		'dialog': [
			"So the big one finally shows up."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch18_act_of_defiance',
		'dialog': [
			"It sees our very act of choosing as defiance."
		]
	},
	{
		'npc_id': 'korr',
		'dialog_id': 'korr_ch18_directs_rhea',
		'dialog': [
			"You should speak to Rhea. She has felt its approach longer than any of us."
		]
	},
	{
		'npc_id': 'rhea',
		'dialog_id': 'rhea_ch18_cataclysm_approach',
		'dialog': [
			"It's here. Not just in the city... the city is becoming part of it. The trees are screaming in perfect, orderly patterns. Every branch knows exactly when it will fall.",
			"Cataclysm doesn't hate life. It simply sees it as a flaw in the equation. And it is very, very good at balancing equations."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch18_flaw_it_cannot_solve',
		'dialog': [
			"Then we must be the flaw it cannot solve."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch18_tribute',
		'dialog': [
			"I volunteer as tribute for maximum chaos."
		]
	},
	{
		'npc_id': 'rhea',
		'dialog_id': 'rhea_ch18_find_unfindable',
		'dialog': [
			"I can feel its presence, even if unseen. You need to find a way to find that which cannot be found."
		]
	},
	{
		'npc_id': 'velka',
		'dialog_id': 'velka_ch18_map_reading',
		'dialog': [
			"Look. The lines are rewriting themselves in real time. The only thing that stays true on this map is here (points on a map).",
			"If you go in there, you are walking into the mind of a world that has decided it should not exist."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch18_reason_to_reconsider',
		'dialog': [
			"Then we'll give it a reason to reconsider."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch18_cataclysm_manifests',
		'dialog': [
			"The Choral Sanctum trembles as Cataclysm manifests - a colossal titan of living collapse, its form made of perfectly ordered fracturing geometry."
		]
	},
	{
		'npc_id': 'cataclysm',
		'dialog_id': 'cataclysm_ch18_intro',
		'dialog': [
			"ANOMALIES. EXISTENCE WITHOUT PURPOSE IS WASTE. I WILL BALANCE THE EQUATION."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch18_balance_fists',
		'dialog': [
			"(cracking knuckles) Then come balance these fists, you walking spreadsheet."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch18_not_waste',
		'dialog': [
			"We are not waste. We are the choice that defies your schedule."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch18_loves_monologue',
		'dialog': [
			"Oh I love it when they monologue. Makes the punching feel personal."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch18_perfect_order',
		'dialog': [
			"Your \"perfect order\" is just fear wearing a mask of inevitability."
		]
	},
	{
		'npc_id': 'cataclysm',
		'dialog_id': 'cataclysm_ch18_failure',
		'dialog': [
			"YOU ARE FAILURE. THE SYSTEM WILL CORRECT YOU. ALL THAT IS BUILT MUST FALL. THIS INCLUDES YOU."
		]
	},
	{
		'npc_id': 'cataclysm',
		'dialog_id': 'cataclysm_ch18_fading',
		'dialog': [
			"YOU HAVE ONLY DELAYED THE INEVITABLE... THE SYSTEM WILL ADAPT... IT WILL FIND ANOTHER WAY TO BALANCE...",
			"...Order... always... wins..."
		]
	},
	{
		'npc_id': None,
		'dialog_id': 'narrator_ch18_spire_silent',
		'dialog': [
			"The spire falls silent, leaving the city scarred but breathing. The party stands among the ruins, breathing heavily."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch18_bookkeeping',
		'dialog': [
			"That thing talked like the end of the world was just good bookkeeping."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch18_believed_right',
		'dialog': [
			"It believed it was doing the right thing. The only logical thing."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch18_logic_chaos',
		'dialog': [
			"Yeah, well, logic can eat my sparkly chaotic ass."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch18_irrational_win',
		'dialog': [
			"We just proved existence can be irrational and still win. That's going to have consequences."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch18_world_watching',
		'dialog': [
			"The world is watching now."
		]
	},
	{
		'npc_id': 'korr',
		'dialog_id': 'korr_ch18_returns',
		'dialog': [
			"You made the system flinch. But Cataclysm was only the symptom. The real wound runs deeper.",
			"Go to Aurelion Veil. A city built from living memory, etched in the forest as it grew."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch18_memory_weight',
		'dialog': [
			"Memory... that's what we have left. Not just echoes, but the weight of what we've carried through every fracture.",
			"If this city remembers truly, perhaps we can learn to hold ourselves together again."
		]
	},
	{
		'npc_id': 'vek',
		'dialog_id': 'vek_ch18_go',
		'dialog': [
			"Then that's where we go."
		]
	},
	{
		'npc_id': 'grimnaw',
		'dialog_id': 'grimnaw_ch18_memory_architecture',
		'dialog': [
			"Living memory architecture... I have so many questions."
		]
	},
	# ── Type A hook dialogs ────────────────────────────────────────
    {
        'npc_id': 'velka',
        'dialog_id': 'velka_ch18_map_unstable',
        'dialog': [
            "I can't give you a location. Not yet.",
            "The map is rewriting itself faster than I can read it.",
            "(tracing her finger across shifting lines)",
            "There's one anchor point that isn't moving — a fixed memory somewhere in the forest exchange.",
            "The living wood holds it. Something that doesn't collapse the way everything else does.",
            "Find me that anchor and I can lock the map long enough to give you a real entry point.",
            "Without it... you'd be walking into the mind of a city that's already erased itself."
        ]
    },
    {
        'npc_id': 'velka',
        'dialog_id': 'velka_ch18_still_shifting',
        'dialog': [
            "Still shifting.",
            "The anchor — did you find it yet?",
            "I can't hold the map open much longer."
        ]
    },
    {
        'npc_id': 'velka',
        'dialog_id': 'velka_ch18_anchor_received',
        'dialog': [
            "(pressing the anchor against the map — the lines stop moving for the first time)",
            "There.",
            "Look. The lines are locked. That point — (points on the map) — that's where it is.",
            "If you go in there, you are walking into the mind of a world that has decided it should not exist.",
            "That's your entry."
        ]
    },
]

TASKS = [
	{
		'task_id': 'main_story_ch18_meet_korr',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'korr',
		'task_acquire_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch18_intro' }},
			{ 'event_type': 'show_npc', 'params': { 'npc_id': 'velka', 'location': 'region_city_shopitems' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rhea', 'standing_text': ["This city is dying with such... methodical precision. It's the most unnerving thing I've ever seen."]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'korr', 'standing_text': ["Orderly collapse is still collapse. Do not be fooled by the lack of panic. The end is still the end."]}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'velka', 'standing_text': ["My maps are still accurate, for now. But they have expiration dates. 'The bridge at sector 4 will cease to exist at sundown.'"]}}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'korr', 'dialog_id': 'korr_ch18_intro' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch18_big_one' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch18_act_of_defiance' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'korr', 'dialog_id': 'korr_ch18_directs_rhea' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'korr', 'standing_text': ["The system flinched. But Cataclysm was only the symptom. The real wound runs deeper."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch18_meet_rhea' }}
		]
	},
	{
		'task_id': 'main_story_ch18_meet_rhea',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rhea',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rhea', 'dialog_id': 'rhea_ch18_cataclysm_approach' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch18_flaw_it_cannot_solve' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch18_tribute' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rhea', 'dialog_id': 'rhea_ch18_find_unfindable' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rhea', 'standing_text': ["Cataclysm doesn't hate life. It simply sees it as a flaw in the equation. And it is very, very good at balancing equations."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch18_meet_velka' }}
		]
	},
    {
        'task_id': 'main_story_ch18_meet_velka',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'velka',
        'task_acquire_events': [],
        'task_complete_events': [
            # ── Map unstable: send to city chain, loop until anchor found ──
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'velka', 'dialog_id': 'velka_ch18_map_unstable' }},
            { 'event_type': 'remove_task', 'params': { 'task_id': 'main_story_ch18_meet_velka' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch18_meet_velka' }},
            # ── Anchor in hand: lock the map, proceed ──
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'velka', 'dialog_id': 'velka_ch18_anchor_received' },
              'condition': { 'type': 'is_task_completed', 'params': { 'task_id': 'forest_large_city_type_a_ch18_find_anchor' }}},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch18_reason_to_reconsider' },
              'condition': { 'type': 'is_task_completed', 'params': { 'task_id': 'forest_large_city_type_a_ch18_find_anchor' }}},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'velka', 'standing_text': ["If you go in there, you are walking into the mind of a world that has decided it should not exist."]},
			  'condition': { 'type': 'is_task_completed', 'params': { 'task_id': 'forest_large_city_type_a_ch18_find_anchor' }}},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch18_meet_cataclysm' },
              'condition': { 'type': 'is_task_completed', 'params': { 'task_id': 'forest_large_city_type_a_ch18_find_anchor' }}},
        ]
    },
	{
		'task_id': 'main_story_ch18_meet_cataclysm',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'cataclysm',
		'task_acquire_events': [
			{ 'event_type': 'create_npc', 'params': { 'npc_id': 'cataclysm', 'location': None }},
			{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'collapsing_spire', 'location': 'region_city_open_area' }}
		],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch18_cataclysm_manifests' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'cataclysm', 'dialog_id': 'cataclysm_ch18_intro' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch18_balance_fists' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch18_not_waste' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch18_loves_monologue' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch18_perfect_order' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'cataclysm', 'dialog_id': 'cataclysm_ch18_failure' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'cataclysm', 'standing_text': ["ANOMALIES. EXISTENCE WITHOUT PURPOSE IS WASTE. I WILL BALANCE THE EQUATION."]}},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch18_defeat_cataclysm' }}
		]
	},
	{
		'task_id': 'main_story_ch18_defeat_cataclysm',
		'type': 'defeat',
		'to_type': 'mob',
		'to_id': 'cataclysm_1',
		'task_acquire_events': [
			{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'cataclysm_1', 'combat_type': 'boss_battle' }}
		],
		'task_complete_events': [
			{ 'event_type': 'hide_npc', 'params': { 'npc_id': 'cataclysm' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch18_cataclysm_manifests' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'cataclysm', 'dialog_id': 'cataclysm_ch18_fading' }},
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch18_spire_silent' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch18_bookkeeping' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch18_believed_right' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch18_logic_chaos' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch18_irrational_win' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch18_world_watching' }},
			{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch18_meet_korr_again' }}
		]
	},
	{
		'task_id': 'main_story_ch18_meet_korr_again',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'korr',
		'task_acquire_events': [],
		'task_complete_events': [
			{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'korr', 'dialog_id': 'korr_ch18_returns' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch18_memory_weight' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'vek', 'dialog_id': 'vek_ch18_go' }},
			{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch18_memory_architecture' }},
			{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'korr', 'standing_text': ["The system flinched. But Cataclysm was only the symptom. The real wound runs deeper."]}},
			{ 'event_type': 'advance_chapter' }
		]
	}
]

PRIMARY_STORY_SETTINGS = {
	'chapter_id': 'main_story_chapter_18',
	'tasks': TASKS,
	'npcs': NPCS,
	'npc_dialog': NPC_DIALOG,
	'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}
