#MOUNTAIN
# local characters:
#  Bragg - a rock tech-smith who builds golems (tech)
#
# local bad-guys:
#  ROKHULD THE CORE-BREAKER
#   A massive, hammer-wielding brute who believes the mountain's heart contains the world's "true ending."
#   He is tunneling downward to reach it.
#
#   Why he opposes Bragg:
#    Bragg builds; Rokhuld destroys.
#    He mocks Bragg's golems as "delaying the inevitable collapse."
#
#   Void Hint:
#    He claims the mountain is hollow because "something below is hungry."
#
# Pregame to unlock coreforge_shard:
#   Sindra Coilrunner (relaytech_sindra, mountains large city) has been
#   having nightmares. The relay conduits in her workshop are bleeding
#   corrupted energy into her sleep — constructs from the corruption are
#   beginning to manifest physically. Three escalating waves of nightmare
#   entities erupt from the conduits. After the third wave is cleared
#   Sindra can finally sleep; she gives the party the coreforge_shard
#   she pulled from the final construct as proof the corruption was real.
#
#   Wave 1: two relay_phantoms.
#   Wave 2: one relay_phantom + two surge_wraiths.
#   Wave 3: one surge_wraith + one conduit_colossus (rare drop: coreforge_shard).
#
# Deliver coreforge_shard to Bragg → he joins here (report_to_bragg removed).

ATTAINABLE_PLAYER_CHARACTERS = [
    {
        ## total power points = 15 + 15 * 29 = 465
        ## total stat points = 10 + 6 * 29 = 184
        'id': 'bragg',
        'name': 'Bragg',
        'head_armor': 'coresight_visor',
        'body_armor': 'forgeplate_harness',
        'arm_armor': 'shockforge_gauntlets',
        'leg_armor': 'stonebinder_greaves',
        'equipped_weapon': 'corebreaker_hammer',
        'max_hp': 941,
        'current_hp': 941,
        'max_ap': 350,
        'current_ap': 350,
        'unused_ability_slots': 0,
        'unused_stat_points': 0,
        'unused_power_points': 0,
        'strength': 38,
        'dexterity': 102,
        'intelligence': 158,
        'constitution': 38,
        'level': 30,
        'abilities': [
            'dark_earth_electric_tech_lv3_petrifying_shock',
            'earth_electric_water_tech_lv3_tectonic_current',
            'fire_earth_tech_lv2_forge_pulse',
            'earth_earth_tech_lv2_seismic_rupture',
            'electric_earth_tech_lv2_grounded_spike',
            'fire_tech_lv1_flux_dampener',
            'earth_tech_lv1_fault_inhibitor',
        ]
    }
]

NPCS = [
    {
        'npc_id': 'bragg',
        'name': 'Bragg',
        'description': (
            'A forge-breaker who survived an explosion caused by a micro-fracture—'
            'an event that killed his entire crew. He masks his fear of losing control beneath swagger and bravado.'
            ' Bragg now seeks to understand the fracture that destroyed his forge.'
        ),
        "theme_song": "I Stand Alone, Godsmack",
        "psychology": {
            "mbti": "ESTP",
            "dominant": "Se — Lives through action and physical force, reacting instantly to threats.",
            "auxiliary": "Ti — Breaks down problems with sharp internal logic, especially mechanical ones.",
            "tertiary": "Fe — Uses charm and bravado to influence or defuse others.",
            "inferior": "Ni — Under stress, becomes paranoid about unseen dangers or future collapse."
        },
        "enneagram": {
            "enneagram_type": "8w7",
            "core_fear": "Being controlled or harmed by forces beyond his understanding (like the fracture).",
            "core_desire": "To be in control of his own life and environment.",
            "defense_mechanism": "Denial — Uses bravado and swagger to deny his underlying fear and trauma from the explosion, projecting an image of strength.",
            "stress_line": "Moves to Type 5 — Becomes withdrawn and paranoid when his control is seriously threatened.",
            "growth_line": "Moves to Type 2 — Uses his strength to protect others, turning his trauma into a protective instinct.",
            "instinctual_variant": "sx/sp — Seeks intense challenges and confrontations to prove his strength and control."
        },
        'image': 'bragg1',
        'song_id': 'i_stand_alone_godsmack'
    },
    {
        'npc_id': 'rokhuld',
        'name': 'Rokhuld the Core-Breaker',
        'description': (
            'A massive, hammer-wielding brute who believes the mountain\'s heart contains the world\'s "true ending." '
            'He is tunneling downward to reach it.'
        ),
        "psychology": {
            "mbti": "ISTJ",
            "dominant": "Si — Fixated on the mountain's ancient patterns and the 'truth' he believes lies beneath. He follows a rigid internal sense of duty.",
            "auxiliary": "Te — Executes his mission with relentless efficiency. He destroys anything in his way, including Bragg's golems.",
            "tertiary": "Fi — Holds a private, warped conviction that breaking the mountain is righteous. His morality is internal and unshakeable.",
            "inferior": "Ni — The void exploits his weakest function, filling him with catastrophic visions and the belief that the mountain hides the world's 'final breath.'"
        },
        "enneagram": {
            "enneagram_type": "1w2",
            "core_fear": "Being corrupt or failing in his sacred duty.",
            "core_desire": "To be good and have integrity by fulfilling his perceived purpose.",
            "defense_mechanism": "Reaction Formation — Channels his fear of the world's end into a rigid, destructive quest that he believes is righteous and necessary.",
            "stress_line": "Moves to Type 4 — Becomes melancholic and withdrawn when his progress is halted.",
            "growth_line": "Moves to Type 7 — Learns to find a more flexible and less destructive purpose.",
            "instinctual_variant": "sp/so — A self-contained crusader, focused on his personal mission which he believes will save the world."
        },
        'image': 'bosses:rokhuld1.jpeg'
    }
]

NPC_DIALOG = [
    # ── Sindra nightmare chain ────────────────────────────────────────────────
    {
        'npc_id': 'relaytech_sindra',
        'dialog_id': 'sindra_nightmare_intro',
        'dialog': [
            "Oh — you came at the right time. Or the wrong time. I can't tell anymore.",
            "Three nights running. Machines that aren't there. Sparks that make shapes.",
            "The conduits are fine — I checked. Everything checks out.",
            "(quietly) But they're still coming through.",
            "It's like the relay grid is dreaming and the dreams are getting out.",
            "I don't know what to do. I stopped sleeping.",
            "(the workshop hums — then a conduit flares) ...",
            "There. You see that? That's not a normal arc.",
            "Stay close."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_sindra_nightmare_intro',
        'dialog': [
            "Relay feedback doesn't spontaneously generate constructs.",
            "Something is using the conduit grid as a door.",
            "Sindra, get behind us."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_sindra_nightmare_intro',
        'dialog': [
            "The sparks have shapes and the shapes have intent.",
            "That's not machinery. That's something wearing machinery.",
            "Hit it."
        ]
    },
    # ── After wave 1 ──────────────────────────────────────────────────────────
    {
        'npc_id': 'relaytech_sindra',
        'dialog_id': 'sindra_after_wave_1',
        'dialog': [
            "That — that was them. Exactly what I've been seeing.",
            "They just — walked right out of the conduit housing.",
            "I'm not losing my mind."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_after_wave_1',
        'dialog': [
            "No. You're not.",
            "There are more coming. I can feel the grid building pressure again."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_after_wave_1',
        'dialog': [
            "They're getting faster between waves.",
            "Whatever is feeding them is close."
        ]
    },
    # ── After wave 2 ──────────────────────────────────────────────────────────
    {
        'npc_id': 'relaytech_sindra',
        'dialog_id': 'sindra_after_wave_2',
        'dialog': [
            "The surge wraiths — those are the ones that drain you.",
            "In the dreams they just stand there and pull the warmth out of everything.",
            "(steadying herself) There's something bigger behind all of this. I can feel it in the hum."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_after_wave_2',
        'dialog': [
            "The resonance frequency is climbing. Something large is about to come through.",
            "Sindra — if this breaks your conduit housing it won't be fixable tonight.",
            "Be ready."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_after_wave_2',
        'dialog': [
            "I've fought things that came out of voids, cracks, tears, and one very aggressive painting.",
            "A relay conduit is new. Points for creativity.",
            "Let's finish this."
        ]
    },
    # ── After wave 3 (colossus defeated, shard awarded) ───────────────────────
    {
        'npc_id': 'relaytech_sindra',
        'dialog_id': 'sindra_after_wave_3',
        'dialog': [
            "(long exhale) ...",
            "It's quiet. The hum stopped.",
            "Three nights I couldn't sleep and it took you — what — twenty minutes.",
            "(crouching, examining the collapsed colossus) Look at this.",
            "There's a shard embedded in the core housing. Pure forged resonite.",
            "That shouldn't exist in a construct like this. It's not relay material.",
            "It's deeper — mountain deep. The kind of thing Bragg would recognize.",
            "(hands it over) Take it. I don't want it near my conduits.",
            "And tell Bragg... whatever that thing was, it came from below his territory.",
            "He should know."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_after_wave_3',
        'dialog': [
            "Rokhuld's been cracking the mountain open below.",
            "Whatever he's disturbing, it's finding other ways out.",
            "Sindra's conduits were just the nearest crack."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_after_wave_3',
        'dialog': [
            "Sindra. Go sleep.",
            "Actually sleep. It's done."
        ]
    },
    {
        'npc_id': 'relaytech_sindra',
        'dialog_id': 'sindra_farewell',
        'dialog': [
            "(almost laughing) Yeah.",
            "Yeah, I think I will.",
            "Thank you. Seriously."
        ]
    },
    # ── Bragg intro (receives coreforge_shard, joins) ─────────────────────────
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_intro',
        'dialog': [
            "(wiping soot from his hands, grinning) Ah! Fresh limbs with working brains. Perfect.",
            "Rokhuld's smashing my golems to dust. Says the world's end is buried in the mountain's heart.",
            "I lost enough people to one explosion already. Go crack his skull before he cracks the whole peak."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_bragg_intro',
        'dialog': [
            "He said 'I lost people' like it was a footnote.",
            "It wasn't a footnote."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_bragg_intro',
        'dialog': [
            "He builds golems to replace what he lost.",
            "That's either brilliant engineering or avoidance.",
            "Probably both."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_bragg_intro',
        'dialog': [
            "The shard came from deep in Rokhuld's territory.",
            "Bragg recognized it in under a second.",
            "He knows this mountain."
        ]
    },
    # ── Bragg receives shard and joins ────────────────────────────────────────
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_shard_received',
        'dialog': [
            "(turning the shard over in his hand, expression shifting)",
            "...This is coreforge resonite. Deep seam. Pre-fracture grade.",
            "Sindra pulled this out of a construct that walked out of her conduits.",
            "That means Rokhuld cracked something loose down there that's already bleeding upward.",
            "(sets the shard down carefully)",
            "I built this whole operation to understand what happened to my crew.",
            "A micro-fracture. One crack I didn't see coming.",
            "If Rokhuld opens the core... that won't be a micro-fracture.",
            "(picks up his hammer) I'm coming with you.",
            "Someone needs to build things while you lot break the world.",
            "...And someone who actually knows what's down there probably shouldn't stay up here."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_bragg_join_reaction',
        'dialog': [
            "He went from grinning to quiet to absolutely decided in about four seconds.",
            "I respect the pace.",
            "Welcome aboard, Bragg."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_bragg_join_reaction',
        'dialog': [
            "Structural analysis. Mechanical expertise. First-hand knowledge of fracture events.",
            "He's useful.",
            "Also the hammer is large. That helps."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_bragg_join_reaction',
        'dialog': [
            "He moves like someone who's already decided how he's going to die and made peace with it.",
            "That's either wisdom or a very bad sign.",
            "Either way — glad he's on our side."
        ]
    },
    # ── Rokhuld confrontation ─────────────────────────────────────────────────
    {
        'npc_id': 'rokhuld',
        'dialog_id': 'rokhuld_intro',
        'dialog': [
            "You stand between me and truth.",
            "The mountain hides the world's final breath.",
            "I will break it open."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_rokhuld_confrontation',
        'dialog': [
            "Rokhuld.",
            "I've seen what a fracture does. One small crack. One.",
            "You're not finding truth down there. You're finding the same thing that took my crew.",
            "Step back."
        ]
    },
    {
        'npc_id': 'rokhuld',
        'dialog_id': 'rokhuld_confrontation_reply',
        'dialog': [
            "Your crew died because they feared the depth.",
            "The mountain's heart does not punish courage.",
            "It punishes hesitation.",
            "I will not hesitate."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_rokhuld_challenge',
        'dialog': [
            "He's not going to listen.",
            "He never was."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_rokhuld_challenge',
        'dialog': [
            "He turned Bragg's grief into an argument for cracking open the mountain.",
            "I've heard enough."
        ]
    },
    # ── Rokhuld defeat ────────────────────────────────────────────────────────
    {
        'npc_id': 'rokhuld',
        'dialog_id': 'rokhuld_defeat',
        'dialog': [
            "Stone… holds…",
            "for now…",
            "Something below is still hungry.",
            "You… have only sealed the surface."
        ]
    },
    # ── Post-defeat scene ─────────────────────────────────────────────────────
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_post_defeat',
        'dialog': [
            "(quiet for a beat) 'Something below is still hungry.'",
            "Yeah.",
            "I know.",
            "That's why I'm here.",
            "(to the party) Come on. Let's not give it time to find another crack."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_post_defeat',
        'dialog': [
            "He said 'sealed the surface.'",
            "Not 'stopped it.'",
            "I noticed that too."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_post_defeat',
        'dialog': [
            "The mountain is stable for now.",
            "For now is doing a lot of work in that sentence."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_post_defeat',
        'dialog': [
            "Bragg held.",
            "That's what matters right now."
        ]
    },
]

DUNGEONS = []

TASKS = [
    # ── Initialize — Bragg appears at region bar ──────────────────────────────
    {
        'task_id': 'mountains_primary_initialize',
        'type': 'complete_intro_story',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'bragg',
                    'location': 'region_bar'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'bragg',
                    'standing_text': [
                        "Heyo! I'm Bragg — I build golems and keep the mining networks from collapsing.",
                        "Something's been disturbing the deep tunnels lately. Ask around the city.",
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_primary_meet_sindra'
                }
            }
        ]
    },

    # ── Meet Sindra — she describes the nightmares, wave 1 erupts ────────────
    {
        'task_id': 'mountains_primary_meet_sindra',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'relaytech_sindra',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'relaytech_sindra',
                    'standing_text': [
                        "Three nights without sleep. The conduits are fine on paper.",
                        "They're not fine.",
                        "Come find me if you want to see for yourself."
                    ]
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'bragg',
                    'standing_text': [
                        "Sindra's been jumpy. She says the relay conduits are doing something they shouldn't.",
                        "She's not the type to imagine things. Go see what she's dealing with."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'relaytech_sindra',
                    'dialog_id': 'sindra_nightmare_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_sindra_nightmare_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_sindra_nightmare_intro'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_primary_nightmare_wave_1'
                }
            }
        ]
    },

    # ── Wave 1: two relay_phantoms ────────────────────────────────────────────
    {
        'task_id': 'mountains_primary_nightmare_wave_1',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'sindra_nightmare_1',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'sindra_nightmare_1',
                    'combat_type': 'combat'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'relaytech_sindra',
                    'dialog_id': 'sindra_after_wave_1'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'technique',
                    'dialog_id': 'chock_after_wave_1'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_after_wave_1'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_primary_nightmare_wave_2'
                }
            }
        ]
    },

    # ── Wave 2: relay_phantom + two surge_wraiths ─────────────────────────────
    {
        'task_id': 'mountains_primary_nightmare_wave_2',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'sindra_nightmare_2',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'sindra_nightmare_2',
                    'combat_type': 'combat'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'relaytech_sindra',
                    'dialog_id': 'sindra_after_wave_2'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_after_wave_2'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_after_wave_2'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_primary_nightmare_wave_3'
                }
            }
        ]
    },

    # ── Wave 3: surge_wraith + conduit_colossus ───────────────────────────────
    {
        'task_id': 'mountains_primary_nightmare_wave_3',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'sindra_nightmare_3',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'sindra_nightmare_3',
                    'combat_type': 'combat'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'relaytech_sindra',
                    'dialog_id': 'sindra_after_wave_3'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'technique',
                    'dialog_id': 'chock_after_wave_3'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_after_wave_3'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'relaytech_sindra',
                    'dialog_id': 'sindra_farewell'
                }
            },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'coreforge_shard'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'relaytech_sindra',
                    'standing_text': [
                        "The conduits are quiet now. First time in days.",
                        "Go find Bragg. Tell him what came out of that thing."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_primary_meet_bragg'
                }
            }
        ]
    },

    # ── Deliver coreforge_shard to Bragg — he joins here ─────────────────────
    {
        'task_id': 'mountains_primary_meet_bragg',
        'type': 'deliver',
        'to_type': 'npc',
        'to_id': 'bragg',
        'item_id': 'coreforge_shard',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'bragg',
                    'standing_text': [
                        "You found something? Bring it here.",
                        "If Sindra pulled it out of a construct, I need to see it."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bragg',
                    'dialog_id': 'bragg_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_bragg_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_bragg_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_bragg_intro'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bragg',
                    'dialog_id': 'bragg_shard_received'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_bragg_join_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_bragg_join_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_bragg_join_reaction'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {'npc_id': 'bragg'}
            },
            {
                'event_type': 'character_join',
                'params': {'character_id': 'bragg'}
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'mountains_primary_defeat_rokhuld'
                }
            }
        ]
    },

    # ── Meet Rokhuld in dungeon — confrontation scene before combat ───────────
    {
        'task_id': 'mountains_primary_defeat_rokhuld',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'rokhuld',
        'task_acquire_events': [
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'rokhuld_lair',
                    'location': 'region_open_area'
                }
            },
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'rokhuld',
                    'location': None
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rokhuld',
                    'dialog_id': 'rokhuld_intro'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bragg',
                    'dialog_id': 'bragg_rokhuld_confrontation'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rokhuld',
                    'dialog_id': 'rokhuld_confrontation_reply'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'technique',
                    'dialog_id': 'chock_rokhuld_challenge'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_rokhuld_challenge'
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'defeat_rokhuld'
                }
            }
        ]
    },

    # ── Defeat Rokhuld — void hint + Bragg arc resolution ────────────────────
    {
        'task_id': 'defeat_rokhuld',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'rokhuld_1',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'rokhuld_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'rokhuld',
                    'dialog_id': 'rokhuld_defeat'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {'npc_id': 'rokhuld'}
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'bragg',
                    'dialog_id': 'bragg_post_defeat'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_post_defeat'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_post_defeat'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_post_defeat'
                }
            },
            {
                'event_type': 'complete_region_quest',
                'params': {'region_id': 'mountains'}
            }
        ]
    }
]


PRIMARY_STORY_SETTINGS = {
    'story_id': 'mountains_primary_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}