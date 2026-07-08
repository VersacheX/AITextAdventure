# ============================================================
# = CHAPTER 7 : SETH'S AIRSHIP & THE REQUIREMENT
# ============================================================
#
# [ LOCATION - BLEAKWATCH OUTPOST ]
# -----------------------------------
# @ = player
# S = Seth 
# L = Lyren (new character)
#
# High level: The player must complete all regional hero quests to
# stabilize the Riftlands. A new character, Lyren, is introduced
# and joins the party after the player completes a small fetch quest
# for her. Once all conditions are met, the player can finally
# depart on Seth's airship.

ATTAINABLE_PLAYER_CHARACTERS = [
  {
    "id": "lyren",
    "name": "Lyren Vale",
    "level": 35,
    "arm_armor": "petalwoven_bracers",
    "head_armor": "softbloom_cowl",
    "body_armor": "heartroot_wrap",
    "leg_armor": "dewthread_sandals",
    "equipped_weapon": "gentlecurrent_staff",
    "max_hp": 1120,
    "current_hp": 1120,
    "max_ap": 360,
    "current_ap": 360,
    "unused_ability_slots": 0,
    "unused_stat_points": 0,
    "unused_power_points": 0,
    "strength": 40,
    "dexterity": 40,
    "intelligence": 180,
    "constitution": 140,
    "abilities": [
      "water_light_faith_lv2_holy_fountain",
      "air_light_faith_lv2_serene_breath",
      "ice_light_faith_lv2_purging_veil",
      "earth_light_faith_lv2_clarity_balm",
      "light_faith_lv1_minor_heal",
      "light_light_faith_lv4_soulflare_bloom"
    ]
  }
]

NPCS = [
    {
        "npc_id": "lyren",
        "name": "Lyren Vale",
        "description": (
            "A gentle wayfarer attuned to the emotional undercurrents of the world. Lyren feels the Riftwaters long before she sees them."
            "The way light bends, the way people's hearts tighten. She speaks softly, moves quietly, and heals instinctively, as if guided by something older than memory."
        ),
        "theme_song": "Holocene, Bon Iver",
        "psychology": {
            "mbti": "ISFP",
            "dominant": "Fi - Lives by an internal compass of empathy and authenticity. She feels the suffering of others as if it were her own, and her healing comes from emotional resonance rather than doctrine.",
            "auxiliary": "Se - Deeply attuned to sensory detail: the tremble of water, the warmth of a hand, the shift in someone's breath. She reacts instantly to emotional or physical distress.",
            "tertiary": "Ni - Experiences intuitive flashes about people's fates. She senses collapse approaching like a change in weather, though she struggles to articulate it.",
            "inferior": "Te - Under stress, she becomes overwhelmed by practical demands. When forced to make structured decisions, she freezes or lashes out in quiet frustration."
        },
        "enneagram": {
          "enneagram_type": "9w1",
          "core_fear": "Loss of connection; conflict and fragmentation.",
          "core_desire": "To have inner stability and peace.",
          "defense_mechanism": "Narcotization — Disengages from the world's harshness by focusing on small, gentle acts of healing, maintaining her own inner peace.",
          "stress_line": "Moves to Type 6 — Becomes anxious and worried when the world's suffering becomes too overwhelming to ignore.",
          "growth_line": "Moves to Type 3 — Becomes more assertive and purposeful in her healing, taking an active role in mending the world.",
          "instinctual_variant": "sp/so — Seeks personal peace and comfort, which she extends to others through gentle, harmonious interactions."
        },
        'image': 'lyren1.jpeg'
    }
]

NPC_DIALOG = [
    {
        'npc_id': None,
        'dialog_id': 'ch7_narrator_intro',
        'dialog': [
            "Chapter 7 - A world is not healed by isolated will, but by many working as one."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch7_meet_lyren',
        'dialog': [
            "(softly, eyes distant) The land... it aches. Not just the ground. The hearts walking upon it. I can feel every fracture like a wound that never closed."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch7_to_lyren_1',
        'dialog': [
            "You speak as if the world itself is alive. As if it is suffering."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch7_explains_1',
        'dialog': [
            "It is. And it grows worse with every passing day. Seth believes the airship can carry us forward... but a machine alone cannot mend what is broken. We need anchors. Pieces of what once held meaning."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch7_to_lyren_1',
        'dialog': [
            "Oooh, cryptic *and* poetic. I like her already."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch7_to_lyren_1',
        'dialog': [
            "Skip the poetry. What do you need?"
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch7_explains_2',
        'dialog': [
            "(small, gentle smile) A Fragrant Hibiscus... said to bloom only where hope once refused to die. And an Ancient Relic from the old ruin -- something that still remembers what the world was before the fractures.",
            "Bring them to me. They may help us stabilize the region long enough for Seth to prepare the Rustwing."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch7_to_lyren_1',
        'dialog': [
            "(nodding quietly) Symbols have power. We will find them."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch7_to_lyren_1',
        'dialog': [
            "Great. Treasure hunt for sentimental value. My favorite."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch7_receives_hibiscus',
        'dialog': [
            "(taking the hibiscus carefully, closing her eyes as she breathes in its scent)",
            "...It's still alive. Even after everything... it kept its fragrance. Like a small act of defiance.",
            "(softly, almost to herself) These were the first flowers my mother planted after... I thought they'd all gone."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch7_after_hibiscus',
        'dialog': [
            "(gently) Then this one still carries her hope."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch7_response_to_faith',
        'dialog': [
            "(nodding slowly) That's what I needed. Not just the flower itself...",
            "but proof that something can still remember what it was supposed to be. Even when the world tries to forget."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch7_after_hibiscus',
        'dialog': [
            "(grinning) You really do turn everything into poetry, don't you?"
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch7_response_to_magic',
        'dialog': [
            "(looking at him with quiet intensity) Everything broken still holds its original shape somewhere inside.",
            "If we forget that... then the Fracture has already won."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch7_receives_relic',
        'dialog': [
            "(holding the relic with both hands, voice barely above a whisper) This one remembers... before the fractures. Before fear became the only constant."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch7_after_relic',
        'dialog': [
            "Will it be enough?"
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch7_joins_1',
        'dialog': [
            "Enough to heal the world? It will take all of us choosing to stand together."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch7_after_relic',
        'dialog': [
            "Then that is what we will do."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch7_after_relic',
        'dialog': [
            "Damn right. I didn't come this far to watch everything fall apart."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch7_after_relic',
        'dialog': [
            "Group hug? No? Too soon?"
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch7_after_relic',
        'dialog': [
            "Let's not get carried away. But... she's right. Isolated efforts won't cut it anymore."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch7_joins_2',
        'dialog': [
            "(softly) Thank you. All of you. I will come with you, I cannot sit by while the world burns."
        ]
    },
    {
        'npc_id': 'seth',
        'dialog_id': 'seth_ch7_airship_ready',
        'dialog': [
            "Alright! She's ready! Everyone aboard!"
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch7_airship_ready',
        'dialog': [
            "Finally! Let's fly this bucket!"
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch7_airship_ready',
        'dialog': [
            "If we crash, I'm blaming Seth AND physics."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch7_airship_ready',
        'dialog': [
            "May the winds guide us safely."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch7_airship_ready',
        'dialog': [
            "Eyes open. Worlds don't shift quietly."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch7_airship_ready',
        'dialog': [
            "Strap in. Or don't. Your funeral."
        ]
    }
]

TASKS = [
    {
        'task_id': 'main_story_ch7_complete_regional_quests',
        'type': 'complete_regional_quests',
        'to_type': 'npc',
        'to_id': 'seth',
        'task_acquire_events': [
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'lyren', 'location': 'region_city_inn' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch7_meet_lyren' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'ch7_narrator_intro' }}
        ],
        'task_complete_events': [
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch7_meet_seth_to_prepare_airship' }}
        ]
    },
    {
        'task_id': 'main_story_ch7_meet_lyren',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'lyren',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch7_meet_lyren' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch7_to_lyren_1' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch7_explains_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch7_to_lyren_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch7_to_lyren_1' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch7_explains_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch7_to_lyren_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch7_to_lyren_1' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lyren', 'standing_text': ["The land is breaking down faster than we can fix it. Help stabilize the region before Seth can prepare the airship for departure."]}},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'seth_hideout_ch3', 'item_id': 'fragrant_hibiscus', 'location': 'final_chamber' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'abandoned_ruin_ch2', 'item_id': 'ancient_relic', 'location': 'final_chamber' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch7_deliver_hibiscus_to_lyren' }}
        ]
    },
    {
        'task_id': 'main_story_ch7_deliver_hibiscus_to_lyren',
        'type': 'deliver',
        'item_id': 'fragrant_hibiscus',
        'to_type': 'npc',
        'to_id': 'lyren',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch7_receives_hibiscus' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch7_after_hibiscus' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch7_response_to_faith' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch7_after_hibiscus' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch7_response_to_magic' }},
            { 'event_type': 'remove_item', 'params': { 'item_id': 'fragrant_hibiscus' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch7_deliver_relic_to_lyren' }}
        ]
    },
    {
        'task_id': 'main_story_ch7_deliver_relic_to_lyren',
        'type': 'deliver',
        'item_id': 'ancient_relic',
        'to_type': 'npc',
        'to_id': 'lyren',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch7_receives_relic' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch7_after_relic' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch7_joins_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch7_after_relic' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch7_after_relic' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch7_after_relic' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch7_after_relic' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch7_joins_2' }},
            { 'event_type': 'remove_item', 'params': { 'item_id': 'ancient_relic' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'lyren' }},
            { 'event_type': 'character_join', 'params': { 'character_id': 'lyren' }}
        ]
    },
    {
        'task_id': 'main_story_ch7_meet_seth_to_prepare_airship',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'seth',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'seth', 'dialog_id': 'seth_ch7_airship_ready' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch7_airship_ready' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch7_airship_ready' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch7_airship_ready' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch7_airship_ready' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch7_airship_ready' }},
            { 'event_type': 'remove_task', 'params': { 'task_id': 'meet_astra_wynn_go_back' }},
            { 'event_type': 'advance_chapter' }
        ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_7',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}