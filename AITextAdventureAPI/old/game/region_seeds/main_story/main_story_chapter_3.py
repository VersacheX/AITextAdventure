ATTAINABLE_PLAYER_CHARACTERS = [
]

NPCS = [
     {
		'npc_id': 'sylvi',
		'name': 'Sylvi Emberlane',
		'description': (
			'A chaotic thrill seeking performance fire dancer.'
			'  Her edge shifts between flirtateous and dangerous.'
		),
		"psychology": {
			"mbti": "ESFP",
			"dominant": "Se — Lives for sensation, excitement, and the thrill of performance. She reacts instantly to the environment and thrives on attention.",
			"auxiliary": "Fi — Makes choices based on personal feelings and emotional impulses. Her flirtation is genuine when she feels it, and her danger is real when crossed.",
			"tertiary": "Te — When she wants something, she becomes surprisingly direct and assertive, especially in negotiations or gossip exchanges.",
			"inferior": "Ni — Under stress, she becomes paranoid about hidden motives or spirals into dramatic fatalism, imagining worst‑case outcomes."
		},
        "enneagram": {
          "enneagram_type": "7w8",
          "core_fear": "Being trapped in boredom or emotional pain.",
          "core_desire": "To stay free and stimulated by new, intense experiences.",
          "defense_mechanism": "Rationalization — Frames dangerous situations as exciting opportunities, avoiding fear and negative feelings.",
          "stress_line": "Moves to Type 1 — Becomes rigid and demanding when she feels controlled or bored.",
          "growth_line": "Moves to Type 5 — Becomes more introspective and able to find satisfaction in knowledge, not just action.",
          "instinctual_variant": "sx/so — Seeks intensity in her relationships and social performances, always being the center of the excitement."
        },
        'image': 'npcs:sylvi1'
	},
	{
		'npc_id': 'talla_renn',
		'name': 'Talla Renn',
		'description': (
			#street enforcer
			#tough, loyal, regimented
			'A tough and loyal street enforcer known for her regimented approach to justice.'
			"  Talla is a no-nonsense individual who values order and discipline."
			"  She is fiercely protective of her community and will go to great lengths to maintain peace."
		),
		"psychology": {
			"mbti": "ESTJ",
			"dominant": "Te — Direct, commanding, and structured. She enforces rules with precision and expects others to follow orders.",
			"auxiliary": "Si — Relies on established routines, community traditions, and proven methods of maintaining order.",
			"tertiary": "Ne — Occasionally considers alternative strategies or unexpected angles, especially when dealing with unpredictable threats.",
			"inferior": "Fi — Under stress, she becomes rigidly moralistic or emotionally reactive, taking things personally when her values are challenged."
		},
        "enneagram": {
          "enneagram_type": "1w2",
          "core_fear": "Being corrupt, evil, or defective.",
          "core_desire": "To be good, to have integrity, to be balanced.",
          "defense_mechanism": "Reaction Formation — Suppresses her anger and frustration with the chaos, channeling it into a rigid, righteous pursuit of order and justice.",
          "stress_line": "Moves to Type 4 — Becomes moody and withdrawn when she feels her efforts are futile.",
          "growth_line": "Moves to Type 7 — Becomes more spontaneous and able to see the joy in life, not just the duty.",
          "instinctual_variant": "so/sp — Focused on improving her community and maintaining social order to ensure her own security."
        },
		'image': 'npcs:talla_renn1'
	},
	{
		'npc_id': 'relic_guardian',
		'name': 'Relic Guardian',
		'description': (
			'A mystical entity bound to protect a powerful relic within the noble\'s mansion.'
			'  It is said to possess ancient wisdom and formidable powers.'
		),
		"psychology": {
			"mbti": "INTP",
			"dominant": "Ti — Operates on an internal, ancient logic. Its actions follow principles mortals cannot fully understand.",
			"auxiliary": "Ne — Perceives multiple metaphysical possibilities and reacts to intruders in unpredictable, otherworldly ways.",
			"tertiary": "Si — Bound by ancient memory and duty, repeating its purpose across centuries.",
			"inferior": "Fe — Displays strange, unsettling emotional projections when destabilized, as if mimicking feelings it does not truly possess."
		},
        "enneagram": {
          "enneagram_type": "1w9",
          "core_fear": "Being defective or corrupt.",
          "core_desire": "To be good and have integrity.",
          "defense_mechanism": "Reaction Formation — Channels its entire existence into the perfect, incorruptible execution of its duty, suppressing any other impulse.",
          "stress_line": "Moves to Type 4 — Becomes erratic and melancholic when its purpose is violated.",
          "growth_line": "Moves to Type 7 — Becomes more flexible and open to new possibilities beyond its rigid duty.",
          "instinctual_variant": "sp/so — Its entire existence is self-preservation through the perfect preservation of its duty and the relic it guards."
        },
		'image': 'bosses:relic_guardian1'
	}
]

NPC_DIALOG = [
	{
		'npc_id': None,
		'dialog_id': 'narrator_chapter_intro_3',
		'dialog': [
			"Chapter 3 - As far as consciousness reaches backward… so far reaches identity."
		]
	},
	{
		'npc_id': 'talla_renn',
		'dialog_id': 'talla_ch3_intro',
		'dialog': [
			"You're the ones everyone's been talking about.",
			"I could use some capable hands to help keep the peace around here.",
			"There's a bounty on a bandit named Seth. Bring him in, and I'll see what I can do to help your situation.",
			"Have a word with Rook about how to find him."
		]
	},# a couple chracters respond to talla's intro here...
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch3_after_talla',
		'dialog': [
			"Oh yeah!!! I have a thing for that guy.  Let's get him!",
			"Bringing in bounties is right up my alley."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch3_after_talla',
		'dialog': [
			"I hope this Seth fellow can be redeemed.",
			"Perhaps bringing him in will give us a chance to help him find a better path."
		]
	},
	{ # use character definitions, Chock, Kade, Moxie, Kaera, and Poise
		"npc_id": "technique", # npc_id, dialog_id is multi key so same dialog has all 5 reserved id's technique, tech, magic, faith, skill
		"dialog_id": "pending_character_ch3_lost_memory", # noted pending_character prefix for knowing that it's the one lost
		"dialog": [ 
			"Where... am I? I feel like I should know this place, but it's all a blur.",
			"My memories... they're slipping away. Who am I? Why am I here?",
			"I need to find answers. Maybe someone here can help me remember.  I just know I'm not from here."
		]
	},
	{
		"npc_id": "tech",
		'dialog_id': "pending_character_ch3_lost_memory", # use Kades description to come up with some gamey rude sarcasm
		"dialog": [
			"Ugh, my head... What is this place? I don't remember how I got here.",
			"Feels like my memories are being erased. Who the hell am I? And why can't I remember anything?",
			"I need to figure this out fast. Maybe someone around here knows something.  This place is weird."
		]			
	},
	{
		"npc_id": "magic",
		'dialog_id': "pending_character_ch3_lost_memory", # use Moxie's description to come up with some magical curious lines
		"dialog": [
			"This place... it's unfamiliar, yet strangely captivating. But why can't I remember how I got here?",
			"My memories feel like they're fading away. Who am I? What is my purpose?",
			"I need to find someone who can help me unlock these lost memories.  There's something important I'm missing."
		]
	},
	{
		'npc_id': "faith",
		'dialog_id': "pending_character_ch3_lost_memory", # use Kaera's description to come up with some compassionate hopeful lines
		"dialog": [
			"This place... it feels foreign, there is no peace here. But why can't I remember how I arrived?",
			"My memories are slipping away like grains of sand. Who am I? What is my destiny?",
			"I must find someone who can help me restore my lost memories.  I feel there's a greater purpose I'm meant to fulfill."
		]
	},
	{
		'npc_id': "skill",
		'dialog_id': "pending_character_ch3_lost_memory", # use Poise's description to come up with some disciplined calm lines
		"dialog": [
			"This place... it's unfamiliar, yet there's a strange sense of purpose here. But why can't I remember how I got here?",
			"My memories feel fragmented, like pieces of a puzzle I can't quite solve. Who am I? What is my path?",
			"I need to find someone who can help me piece together these lost memories.  There's something important I'm meant to do."
		]
	}, 
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch3_meet_pending_character1',
		'dialog': [
			"Don't worry, we'll figure this out... I got you.",

		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch3_meet_pending_character1',
		'dialog': [
			"Yeah, yeah, we'll help you out. Just don't expect me to go easy on you."

		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch3_meet_pending_character1',
		'dialog': [
			"Hahaha! that must be rough. I can think of a thousand ways to remind you."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch3_meet_pending_character1',
		'dialog': [
			"We will help you find your way. Together, we can overcome any obstacle."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch3_meet_pending_character1',
		'dialog': [
			"You're not alone.  I will meditate long and hard on this."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'technique_ch3_meet_pending_character2',
		'dialog': [
			"You should follow us around for a while, it'll all come back."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch3_meet_pending_character2',
		'dialog': [
			"Just stick with us, you'll remember in no time."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'magic_ch3_meet_pending_character2',
		'dialog': [
			"I'm gonna remind you, and remind you, and remind you."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'faith_ch3_meet_pending_character2',
		'dialog': [
			"Stay close to us, and your memories will return."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'skill_ch3_meet_pending_character2',
		'dialog': [
			"Follow our lead, and your memories will come back to you."
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'pending_character_ch3_good_where_im_at',
		'dialog': [
			"Thanks, but I think I'll stay here for now. I need to figure things out on my own."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'pending_character_ch3_good_where_im_at',
		'dialog': [
			"Yeah! Not gonna happen though. Fuckin random."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'pending_character_ch3_good_where_im_at',
		'dialog': [
			"Haha, no rush! I'll just chill here and think things over."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'pending_character_ch3_good_where_im_at',
		'dialog': [
			"I'll stay here for the moment. I trust that the right path will reveal itself in time."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'pending_character_ch3_good_where_im_at',
		'dialog': [
			"I'll stay here for now. I must meditate to gather my thoughts and plan my next move."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'tech_ch3_before_rook',
		'dialog': [
			"If you have a bead on Seth, I can use my aerial drone to track him down."
		]
	},
	{
		'npc_id': 'rook',
		'dialog_id': 'rook_ch3_after_talla',
		'dialog': [
			"Last I heard, he was holed up in an old hideout out in the open area.",
			"Be careful though, he's got a few new tricks up his sleeve."
		]
	},	
	{
	   'npc_id': 'seth',
		'dialog_id': 'seth_ch3_sidequest_intro',
		'dialog': [
			"You again! Hey I'm sorry about all the trouble I gave you before.",
			"I heard about how you guys appeared here out of nowhere. Weird stuff.",
			"Listen, I might be able to help you with the person in the bar's memory problem, I'm pretty sure he's one of you.",
			"There's a noble's mansion not far from here. They've got some rare herbs that could help with memory restoration.",
			"I can get you in there, but you'll need to do something for me in return.",
			"Report to Rook that you scarred me off."
		]
	},
	{
		'npc_id': 'kess_thornwrite',
		'dialog_id': 'kess_ch3_after_receiving_scribe_mint',
		'dialog': [
			"Ah, scribe mint! Excellent choice.",
			"This herb is known for its ability to help with memory retention and recall.",
			"I'll prepare a special concoction for you using this.",
			"Now, I also need scarred thyme for a more potent brew. It's a bit harder to come by."
		]
	},
	{
		'npc_id': 'kess_thornwrite',
		'dialog_id': 'kess_ch3_after_receiving_scarred_thyme',
		'dialog': [
			"Scarred thyme! Perfect!",
			"With both the scribe mint and scarred thyme, I can create a powerful memory tonic for you.",
			"...","...",
			"Here you go, anybody who drinks this will remember every last detail... It won't be nice, but it'll work."
		]
	},
	{
		'npc_id': 'rook',
		'dialog_id': 'rook_ch3_after_seth',
		'dialog': [
			"Well fuck! He got away again... You're actually not a very good bounty hunter at all.",
			"Listen, I can't be your goto for information buddy...",
			"If you want to get in the know you really need to talk to people. Sylvi Emberlane is an amazing source of gossip.",
			"You should check around town and see what you can find."
		]
	},
	{
		'npc_id': 'seth',
		'dialog_id': 'seth_ch3_sidequest_complete',
		'dialog': [
			"Wooooo, with that thing gone, you should loot up this place has a lot of nice stuff."
		]
	},

		{
		'npc_id': 'technique',
		'dialog_id': 'character_ch3_we_found_the_tonic',
		'dialog': [
			"Look what we found! This tonic might help restore your memories."
		]
	},
	{
		'npc_id': 'tech',
		'dialog_id': 'character_ch3_we_found_the_tonic',
		'dialog': [
			"Check it out. This thing might help you remember who you are."
		]
	},
	{
		'npc_id': 'magic',
		'dialog_id': 'character_ch3_we_found_the_tonic',
		'dialog': [
			"Whewwww! Down this thing and it'll all come flooding back."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'character_ch3_we_found_the_tonic',
		'dialog': [
			"I have faith in this remedy."
		]
	},
	{
		'npc_id': 'skill',
		'dialog_id': 'character_ch3_we_found_the_tonic',
		'dialog': [
			"An elixer to open the mind.  I hope it brings you back to us."
		]
	},
	{
		'npc_id': 'faith',
		'dialog_id': 'ch3_faith_respond_to_twisted',
		'dialog': [
			"Oh!  That's, ummmmm, nice... eheh!"
		]
	},
	{
		'npc_id': 'technique',
		'dialog_id': 'ch3_technique_respond_to_twisted',
		'dialog': [
			"HAHAHAHA! Bit ruder than usual, but it's good to have you back."
		]
	}
]


TASKS = [
	#### CH 3 TASKS
	### First task must place all npc's in the city for chapter 3, set their standing texts it will be a meet task... other acquire events will be to create another task to meet the unlockable player character npc (new feature)
	{
		'task_id': 'main_story_ch_3_setup_npcs',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'talla_renn',
		'task_acquire_events': [
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'talla_renn',
					'location': 'region_city_shoparmor'
				}
			},
			{
				'event_type': 'set_npc_met',
				'params': {
					'npc_id': 'talla_renn'
				}
			},
			{
				'event_type': 'show_npc',
				'params': {
					'npc_id': 'rook',
					'location': 'region_city_shoparmor'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': { # in ch1 rook sent the players on a bounty to get seth. he always workd for talla. ok second meeting
					'npc_id': 'rook',
					'standing_text': [
						"Looking for someone tough? Talla Renn might have a job for you.",
						"She's always in need of reliable help to keep the streets safe."
					]
				}
			},
			{
				'event_type': 'show_npc',
				'params': {
					'npc_id': 'oren',
					'location': 'region_city_inn'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'oren', # oren met the players in another inn. he's not sure if he's still there or there's still here
					'standing_text': [
						"I've been having these strange dreams... or are they memories?",
						"I've seen you before. Have I been standing here this long?",
						"Is this here or was that there?? or when?"
					]
				}
			},
			{
				'event_type': 'create_npc',
				'params': {
					'npc_id': 'sylvi',
					'location': 'region_city_shopitems'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sylvi', # sylvi is a street performer who has heard of the players exploits in ch1
					'standing_text': [
						"Heard you folks did some pretty wild things around here not long ago.",
						"People are still talking about that stunt you pulled at the old ruins!",
						"... and you raised quite the fuss chasing down Seth."
					]
				}
			},
			{
				'event_type': 'create_character_npc',
				'params': {
					'location': 'region_city_bar'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'meet_character_4',
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': None,
					'dialog_id': 'narrator_chapter_intro_3'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'talla_renn',
					'dialog_id': 'talla_ch3_intro'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch3_after_talla'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'faith',
					'dialog_id': 'faith_ch3_after_talla'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'talla_renn',
					'standing_text': [
						"I could use some capable hands to help keep the peace around here."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_3_meet_rook_after_talla'
				}
			}
		]
	},	
	{
		'task_id': 'meet_character_4',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'pending_character',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'pending_character', # pending_character in the event call (think player_game.getattr(event_type)(**params)) is remapped to what is set in player_game.pending_character
					'dialog_id': 'pending_character_ch3_lost_memory'
				}
			}, # then we initate dialog for all players remending them of where they are from tell him he appeared through a rift not far from where they did.
			# he won't join at this point, this side quest sends the players on the path to restore his memory.
			# it involves seth and a trip back to mira... 
			# this side quest will be locked at a point until the players complete a portion of the main story until they get an item ... not sure when
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch3_meet_pending_character1'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch3_meet_pending_character1'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch3_meet_pending_character1'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'faith',
					'dialog_id': 'faith_ch3_meet_pending_character1'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch3_meet_pending_character1'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'technique_ch3_meet_pending_character2'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch3_meet_pending_character2'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'magic_ch3_meet_pending_character2'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'faith',
					'dialog_id': 'faith_ch3_meet_pending_character2'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'skill_ch3_meet_pending_character2'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'pending_character',
					'dialog_id': 'pending_character_ch3_good_where_im_at'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'unlock_player_character_deliver_memory_tonic' 
				}
			}			
		]
	},
	{
		'task_id': 'main_story_ch_3_meet_rook_after_talla',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rook',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'tech_ch3_before_rook'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rook',
					'dialog_id': 'rook_ch3_after_talla'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_3_bring_in_seth'
				}
			}
		]
	},
	{
		'task_id': 'main_story_ch_3_bring_in_seth',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'seth',
		'task_acquire_events': [
			{
				'event_type': 'create_dungeon',
				'params': {
					'dungeon_id': 'seth_hideout_ch3',
					'location': 'region_open_area'
				}
			},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'seth_hideout_ch3', 'item_id': 'moontide_orb', 'location': 'treasure_room'}}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'seth',
					'dialog_id': 'seth_ch3_sidequest_intro'
				}
			},
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'seth'
				}
			}, # seth sidequest... create new dungeon.  have the players meet Seth there.  this is the nobles mansion to help the players get the item to unlock the players memory
			# there is also a second item there that allows the player to deliver to Mira, for the 2 ingredients needed to cure the chracters amnesia
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_3_deliver_scribe_mint'
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'main_story_ch_3_report_to_rook'
				}
			}
		]
	},
	{
		'task_id': 'main_story_ch_3_deliver_scribe_mint',
		'type': 'deliver',
		'item_id': 'scribe_mint_ch3',
		'to_type': 'npc',
		'to_id': 'kess_thornwrite',
		'task_acquire_events': [
			{
				'event_type': 'create_dungeon',
				'params': {
					'dungeon_id': 'nobles_mansion_ch3',
					'location': 'region_open_area'
				}
			},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'nobles_mansion_ch3', 'item_id': 'scarred_thyme', 'location': 'treasure_room'}},
			{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'nobles_mansion_ch3', 'item_id': 'heirloom_ring', 'location': 'treasure_room'}},
			{
				'event_type': 'lock_dungeon',
				'params': {
					'dungeon_id': 'nobles_mansion_ch3'
				}
			},
			{
				'event_type': 'set_dungeon_locked_text',
				'params': {
					'dungeon_id': 'nobles_mansion_ch3',
					'locked_text': [
						"Seth: If you want me to get you in here to find your ingredients, you better report to rook first."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'deliver_scribe_mint_to_kess_ch3'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'seth',
					'standing_text': [
						"Heyyyyy, you made it.  The mint should be somewhere around here."
					]
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'meet_relic_guardian'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'kess_thornwrite',
					'dialog_id': 'kess_ch3_after_receiving_scribe_mint'
				}
			},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'scribe_mint_ch3',
					'quantity': 1
				}
			},
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'deliver_scarred_thyme_to_kess_ch3'
				}
			}
		]
	},
	{
		'task_id': 'deliver_scarred_thyme_to_kess_ch3',
		'type': 'deliver',
		'item_id': 'scarred_thyme_ch3',
		'to_type': 'npc',
		'to_id': 'kess_thornwrite',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'kess_thornwrite',
					'dialog_id': 'kess_ch3_after_receiving_scarred_thyme'
				}
			}, # award memory_tonic
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'scarred_thyme_ch3',
					'quantity': 1
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'memory_tonic_ch3',
					'quantity': 1
				}
			}
		]
	},
	{ # decidedly the current end to chapter 3
		'task_id': 'main_story_ch_3_report_to_rook',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'rook',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'rook',
					'dialog_id': 'rook_ch3_after_seth'
				}
			},
			{#EVENT - set_npc_standing_text - sylvi ("I've never seen that person at the bar before, They're about as mysterious as you."):
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sylvi', # sylvi is a street performer who has heard of the players exploits in ch1
					'standing_text': [
						"I've never seen that person at the bar before.",
						"They're about as mysterious as you."
					]
				}
			},
			{
				'event_type': 'unlock_dungeon',
				'params': {
					'dungeon_id': 'nobles_mansion_ch3'
				}
			}
		]
	},
	{
		'task_id': 'meet_relic_guardian',
		'type': 'meet',
		'to_type': 'npc',
		'to_id': 'relic_guardian',
		'task_acquire_events': [],
		'task_complete_events': [
			{
				'event_type': 'award_task',
				'params': {
					'task_id': 'defeat_relic_guardian_ch3'
				}
			}
		]
	},
	{
		'task_id': 'defeat_relic_guardian_ch3',
        'type': 'defeat',
        'to_type': 'mob',
		'to_id': 'relic_guardian_1',
		'task_acquire_events': [
			{
				'event_type': 'begin_combat', # <- begin combat with demigorgon as boss defeating him completes event
				'params': {
					'boss_mob_id': 'relic_guardian_1',
					'combat_type': 'boss_battle'
				}
			}
		],
		'task_complete_events': [
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'relic_guardian'
				}
			},
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'seth'
				}
			},
			{
				'event_type': 'dungeon_add_npc',
				'params': {
					'dungeon_id': 'nobles_mansion_ch3',
					'npc_id': 'seth',
					'location': 'final_chamber'
				}
			},
			{
				'event_type': 'award_item',
				'params': {
					'item_id': 'scribe_mint'
				}
			},
			{
				'event_type': 'initiate_dialog',
				'params': {
					'npc_id': 'seth',
					'dialog_id': 'seth_ch3_sidequest_complete'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'seth',
					'standing_text': [
						"Thanks for dealing with that guardian."
					]
				}
			}
		]
	},
	{
		'task_id': 'unlock_player_character_deliver_memory_tonic',
		'type': 'deliver',
		'item_id': 'memory_tonic_ch3',
		'to_type': 'npc',
		'to_id': 'pending_character',
		'task_acquire_events': [],
		'task_complete_events': [
			# NOTE initiate dialog for each chracter technique, tech, magic, faith, skill about restoring the memory
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique', # pending_character in the event call (think player_game.getattr(event_type)(**params)) is remapped to what is set in player_game.pending_character
					'dialog_id': 'character_ch3_we_found_the_tonic'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'tech',
					'dialog_id': 'character_ch3_we_found_the_tonic'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'magic',
					'dialog_id': 'character_ch3_we_found_the_tonic'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'faith',
					'dialog_id': 'character_ch3_we_found_the_tonic'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'skill',
					'dialog_id': 'character_ch3_we_found_the_tonic'
				}
			},
			{
				'event_type': 'remove_item',
				'params': {
					'item_id': 'memory_tonic_ch3'
				}
			},
			{
				'event_type': 'hide_npc',
				'params': {
					'npc_id': 'pending_character'
				}
			},
			# then add the character to the players roster
			{
				'event_type': 'add_pending_character' # param less as the character is already defined in player_game.pending_character
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'faith',
					'dialog_id': 'ch3_faith_respond_to_twisted'
				}
			},
			{
				'event_type': 'initiate_character_dialog',
				'params': {
					'npc_id': 'technique',
					'dialog_id': 'ch3_technique_respond_to_twisted'
				}
			},
			{
				'event_type': 'set_npc_standing_text',
				'params': {
					'npc_id': 'sylvi', # I heard a rift opened up in the town center of a nearby city
					'standing_text': [
						"Word is, rifts have been opening up in Ironveil Foundry.",
						"People are saying strange things are coming through."
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
    'chapter_id': 'main_story_chapter_3',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
    }