#SHALLOWS
# local characters:
#  Ripple - Well respected and known Tide Oracle (faith) — INFJ 9w1
#    She drowned during the first Fracture wave and returned changed.
#    Her pregame is The Vigil — three return visits to Vaultkeeper Syrin,
#    who has been sitting with the moontide orb for years and cannot bring
#    herself to release it.
#
# local bad-guys:
#  UUL'THAR THE TIDE-WAKENED
#   A deep-sea eldritch horror, a fragment of something older than the world.
#   Its presence warps tides, gravity, and the behavior of water itself.
#
# Pregame to unlock moontide_orb — The Vigil:
#   Saltcaller Renlo (region_city_other1) notices Syrin has been more
#   withdrawn than usual. She's barely spoken in days.
#   Vaultkeeper Syrin (region_city_other2) salvaged the moontide orb from
#   a wreck years ago. It belonged to someone who drowned on that ship.
#   She catalogues everything — but she never catalogued this one.
#   She keeps it lit. She doesn't know why she can't put it away.
#
#   Visit 1 — The party finds Syrin at her vault. She's polite but
#             distant. She acknowledges the orb but doesn't explain it.
#             The party just stays a while.
#   Visit 2 — She talks. The ship. The person. Why the orb glows near
#             water. Why she's never been able to file it with the others.
#             The party listens more than it speaks.
#   Visit 3 — She places the orb on the counter herself.
#             "Someone who needs this more than I need to hold it
#              should have it. I think that's you."
#
# Deliver moontide_orb to Ripple → she joins here.
# report_to_ripple end step removed.
#
# STANDING TEXT CONVENTION:
#   set_npc_standing_text in a meet task's task_acquire_events is redundant
#   because the meet event fires its own dialog on completion. The standing
#   text would only be seen if the player walks away before triggering the
#   meet, which is brief and uncommon.
#   set_npc_standing_text IS necessary in deliver task_acquire_events — the
#   player needs a visible hint to bring the item back before the dialog fires.

ATTAINABLE_PLAYER_CHARACTERS = [
    {
        ## total power points = 15 + 15 * 29 = 465
        ## total stat points = 10 + 6 * 29 = 184
        'id': 'ripple',
        'name': 'Ripple',
        'head_armor': 'tidecaller_veil',
        'body_armor': 'abyssal_flow_robe',
        'arm_armor': 'currentweaver_bracers',
        'leg_armor': 'tidebound_greaves',
        'equipped_weapon': 'moontide_staff',
        'max_hp': 1019,
        'current_hp': 1019,
        'max_ap': 400,
        'current_ap': 400,
        'unused_ability_slots': 0,
        'unused_stat_points': 0,
        'unused_power_points': 0,
        'strength': 38,
        'dexterity': 38,
        'intelligence': 158,
        'constitution': 102,
        'level': 30,
        'abilities': [
            'lv2_unique_ability_spirit_ripple_tidal_mend',
            'lv2_unique_ability_spirit_ripple_drowned_blessing',
            'lv3_unique_ability_spirit_ripple_returned_tide',
            'lv3_unique_ability_spirit_ripple_deep_current_surge',
        ]
    }
]

NPCS = [
    {
        'npc_id': 'ripple',
        'name': 'Ripple',
        'description': (
            'A tide oracle who drowned during the first Fracture wave—'
            'and returned changed. She now fears deep water even as she channels its power.'
            ' Ripple speaks in patient, measured words that often land truer than she intends.'
            ' She believes the party stands at the center of the next collapse,'
            ' and she has seen enough of the tide\'s patterns to know that fighting it is different from surviving it.'
        ),
        "theme_song": "We Move Lightly, Dustin O'Halloran",
        "psychology": {
            "mbti": "INFJ",
            "dominant": "Ni — Perceives symbolic patterns in tides, emotions, and collapse events.",
            "auxiliary": "Fe — Guides others with quiet empathy and emotional clarity.",
            "tertiary": "Ti — Analyzes metaphysical structures with internal precision.",
            "inferior": "Se — Overwhelmed by sensory chaos, especially water-related trauma."
        },
        "enneagram": {
            "enneagram_type": "9w1",
            "core_fear": "Conflict, fragmentation, and being overwhelmed by the chaotic world.",
            "core_desire": "To have inner and outer peace.",
            "defense_mechanism": "Dissociation — Mentally withdraws from her own trauma and the chaotic world, adopting a calm, detached persona.",
            "stress_line": "Moves to Type 6 — Becomes anxious and fearful when her peace is disturbed or she is forced to confront her trauma.",
            "growth_line": "Moves to Type 3 — Becomes more assertive and engaged, using her powers with purpose.",
            "instinctual_variant": "sp/so — Seeks personal peace and comfort, while gently trying to bring harmony to the world around her."
        },
        'image': 'ripple1.jpeg',
        'song_id': 'we_move_lightly_dustin_ohalloran'
    },
    {
        'npc_id': 'uulthar',
        'name': "Uul'thar the Tide-Wakened",
        'description': (
            'A deep-sea eldritch horror, a fragment of something older than the world.'
            ' Its presence warps tides, gravity, and the behavior of water itself.'
        ),
        "psychology": {
            "mbti": "INTP",
            "dominant": "Ti — Rewrites the rules of tides and gravity with cold, alien logic.",
            "auxiliary": "Ne — Perceives countless possible configurations of water, pressure, and void-geometry.",
            "tertiary": "Si — Remembers the 'before' — ancient patterns long forgotten by mortals.",
            "inferior": "Se — Its physical manifestation distorts reality; sensory presence becomes overwhelming."
        },
        "enneagram": {
            "enneagram_type": "5w4",
            "core_fear": "Being overwhelmed or invaded by a world it doesn't understand.",
            "core_desire": "To understand the universe on its own terms.",
            "defense_mechanism": "Isolation — Remains detached in the depths, observing and manipulating reality from a distance.",
            "stress_line": "Moves to Type 7 — Actions become chaotic when its sanctuary is breached.",
            "growth_line": "Moves to Type 8 — Manifests power directly to reshape the world.",
            "instinctual_variant": "sp/sx — Reclusive, interacting with the world only through intense focused manipulations."
        },
        'image': 'bosses:uulthar1.jpeg'
    }
]

NPC_DIALOG = [
    # ── Renlo notices Syrin is withdrawn ──────────────────────────────────────
    {
        'npc_id': 'saltcaller_renlo',
        'dialog_id': 'renlo_notices_syrin',
        'dialog': [
            "Syrin's barely spoken in four days.",
            "That's not like her. She talks to everything — relics, lanterns, the water stains on the floor.",
            "Something's got her stuck.",
            "She won't tell me what. You might have better luck.",
            "Just... don't rush her.",
            "She moves at tide-speed."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'kaera_renlo_reaction',
        'dialog': [
            "He said she talks to relics.",
            "Something stopped her talking.",
            "That's worth paying attention to."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_renlo_reaction',
        'dialog': [
            "Four days of silence from someone who narrates everything.",
            "Yeah. Let's go see."
        ]
    },
    # ── First visit: the party finds Syrin, mostly just stays ─────────────────
    {
        'npc_id': 'vaultkeeper_syrin',
        'dialog_id': 'syrin_vigil_1',
        'dialog': [
            "(without looking up) The vault is open.",
            "If you're here for the relics, take your time.",
            "(long pause, her lantern casting underwater light across the shelves)",
            "...",
            "Sorry. I'm not very good company today.",
            "I'll be fine."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'kaera_vigil_1',
        'dialog': [
            "We're not here for the relics.",
            "We'll stay a while, if that's alright."
        ]
    },
    {
        'npc_id': 'vaultkeeper_syrin',
        'dialog_id': 'syrin_vigil_1_response',
        'dialog': [
            "(looks up, uncertain)",
            "...Alright."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_vigil_1',
        'dialog': [
            "(sits. says nothing.)"
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_vigil_1',
        'dialog': [
            "(quietly, looking at the shelves)",
            "Every one of these came from a wreck.",
            "She knows all their names."
        ]
    },
    # ── Second visit: Syrin opens up ──────────────────────────────────────────
    {
        'npc_id': 'vaultkeeper_syrin',
        'dialog_id': 'syrin_vigil_2',
        'dialog': [
            "(when the party arrives) You came back.",
            "(a beat) I didn't think you would.",
            "(she turns, the moontide orb in her hands — glowing faintly)",
            "I pulled this from the Hollowed Reach. Three years ago.",
            "A merchant vessel. It went down in the first Fracture storm.",
            "Everyone aboard drowned.",
            "The orb was in the captain's quarters. Still lit when I found it.",
            "(pause)",
            "Everything I salvage gets catalogued. Named. Filed.",
            "I couldn't file this one.",
            "I told myself it was because I hadn't identified the owner yet.",
            "(quietly) That's not why.",
            "I just... couldn't put it away.",
            "The light looks like it's still waiting for something.",
            "I don't know what.",
            "I've been keeping it lit for three years and I still don't know what."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'kaera_vigil_2',
        'dialog': [
            "Sometimes we keep things lit because we can't bear to be the one who lets them go dark.",
            "That's not wrong.",
            "It's just heavy."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_vigil_2',
        'dialog': [
            "Three years is a long time to hold something without knowing why.",
            "You haven't put it down.",
            "That means something."
        ]
    },
    {
        'npc_id': 'vaultkeeper_syrin',
        'dialog_id': 'syrin_vigil_2_response',
        'dialog': [
            "(softly) Come back tomorrow.",
            "I think I'm working toward something.",
            "I just need a little more time with it."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_vigil_2',
        'dialog': [
            "(walking away, quietly)",
            "She said 'I'm working toward something.'",
            "She doesn't know what yet.",
            "But she's moving."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_vigil_2',
        'dialog': [
            "We didn't say much.",
            "That was right."
        ]
    },
    # ── Third visit: Syrin releases the orb ───────────────────────────────────
    {
        'npc_id': 'vaultkeeper_syrin',
        'dialog_id': 'syrin_vigil_3',
        'dialog': [
            "(the orb is on the counter when the party arrives — not in her hands)",
            "I've been thinking about what you said.",
            "About keeping things lit.",
            "(a long pause)",
            "I think I've been treating this like it was my grief to carry.",
            "But it isn't.",
            "Whoever owned this — they're gone.",
            "The ship is gone.",
            "I'm the only one left who remembers it existed.",
            "And I've been holding it so tightly that I couldn't pass the light forward.",
            "(slides the orb across the counter)",
            "Someone who needs this more than I need to hold it should have it.",
            "I think that's you.",
            "(quietly) I don't know what you're doing out there.",
            "But the tides are wrong in a way I've never felt before.",
            "Take it. Use it for whatever matters."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'kaera_vigil_3',
        'dialog': [
            "Syrin.",
            "Thank you for letting us sit with you."
        ]
    },
    {
        'npc_id': 'vaultkeeper_syrin',
        'dialog_id': 'syrin_vigil_3_response',
        'dialog': [
            "(small, tired smile)",
            "Thank you for coming back.",
            "That was the part I didn't expect."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_vigil_3',
        'dialog': [
            "She put it down.",
            "Three years and she put it down."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_vigil_3',
        'dialog': [
            "'I couldn't pass the light forward.'",
            "That's going to stay with me."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_vigil_3',
        'dialog': [
            "We showed up.",
            "Three times.",
            "That was apparently the whole thing."
        ]
    },
    # ── Ripple receives the orb, joins ────────────────────────────────────────
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_intro',
        'dialog': [
            "(voice soft, almost whispering) Traveler… the tides are trembling.",
            "Something ancient stirs in the trench. Uul'thar.",
            "It bends the sea like wet parchment.",
            "I feel it in my bones — the same cold that once pulled me under.",
            "I cannot calm the waters while it exists.",
            "Please… descend and end it."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_orb_received',
        'dialog': [
            "(takes the orb, holds it near the window — it glows)",
            "...",
            "Syrin had this.",
            "Three years.",
            "(quiet) I know that kind of holding.",
            "After I came back from the water I didn't know how to be a person who had drowned.",
            "I kept very still for a long time.",
            "Thought if I stopped moving the grief would stop too.",
            "(looks up)",
            "It doesn't stop.",
            "You just get better at carrying it forward.",
            "(steadying herself)",
            "Uul'thar rewrites the tides and wants me silenced.",
            "But the tides remembered me once.",
            "Let's go remind them they're not his to rewrite."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'kaera_ripple_join_reaction',
        'dialog': [
            "She made the connection between herself and Syrin without us saying a word.",
            "That's what Ripple does.",
            "She reads the current of things."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_ripple_join_reaction',
        'dialog': [
            "'The tides remembered me once.'",
            "She said it like a fact.",
            "I believe her."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_ripple_join_reaction',
        'dialog': [
            "She's been at the edge of this for a long time.",
            "She just needed something to hold while she stepped forward.",
            "Welcome, Ripple."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_ripple_join_reaction',
        'dialog': [
            "A tide oracle who fears deep water.",
            "Channeling the thing that almost ended her.",
            "That takes a particular kind of courage.",
            "Noted."
        ]
    },
    # ── Uul'thar confrontation ────────────────────────────────────────────────
    {
        'npc_id': 'uulthar',
        'dialog_id': 'uulthar_intro',
        'dialog': [
            "Small thing… walking on borrowed water.",
            "The sea remembers the before.",
            "I will show it the after."
        ]
    },
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_uulthar_confrontation',
        'dialog': [
            "Uul'thar.",
            "I drowned in the first Fracture wave.",
            "The sea pulled me down and the sea brought me back.",
            "You don't speak for it.",
            "You never did."
        ]
    },
    {
        'npc_id': 'uulthar',
        'dialog_id': 'uulthar_confrontation_reply',
        'dialog': [
            "The sea brought you back because it had not finished with you.",
            "It has finished now.",
            "The after begins."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_uulthar_challenge',
        'dialog': [
            "The after begins when we say it does.",
            "Not before."
        ]
    },
    {
        'npc_id': 'spirit',
        'dialog_id': 'kaera_uulthar_challenge',
        'dialog': [
            "The tides belong to no one.",
            "Least of all something that wants to erase them."
        ]
    },
    # ── Uul'thar defeat ───────────────────────────────────────────────────────
    {
        'npc_id': 'uulthar',
        'dialog_id': 'uulthar_defeat',
        'dialog': [
            "The deep… still… calls…",
            "The before… is not… forgotten…",
            "The sea remembers… everything…"
        ]
    },
    # ── Post-defeat scene ─────────────────────────────────────────────────────
    {
        'npc_id': 'ripple',
        'dialog_id': 'ripple_post_defeat',
        'dialog': [
            "(breathing shakily, eyes distant)",
            "The tides breathe again.",
            "…Thank you.",
            "For a moment I felt the same cold.",
            "The same pull.",
            "(quietly) But I came back before.",
            "I came back again.",
            "I think I understand now why the tides kept me.",
            "(to the party) The void's whispers grow louder out there.",
            "But so does the current of your choices.",
            "Perhaps together we can keep the waters from swallowing everything."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'moxie_post_defeat',
        'dialog': [
            "She said 'the same pull' and kept moving.",
            "I don't think she's ever said that out loud before."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'poise_post_defeat',
        'dialog': [
            "She held.",
            "Whatever the cold was — she held."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'chock_post_defeat',
        'dialog': [
            "It said the sea remembers everything.",
            "She said the same thing about herself.",
            "I'm choosing to believe her version."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'kade_post_defeat',
        'dialog': [
            "Uul'thar called the after inevitable.",
            "She showed up anyway.",
            "That's the whole argument against inevitability, right there."
        ]
    },
]

DUNGEONS = []

TASKS = [
    # ── Initialize — Ripple appears at region bar ─────────────────────────────
    # Standing text here is neutral: no story hints, no forward references.
    # The player hasn't been told anything yet — Ripple is just present.
    {
        'task_id': 'shallows_primary_initialize',
        'type': 'complete_intro_story',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'ripple',
                    'location': 'region_bar'
                }
            }
        ],
        'task_complete_events': [            
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'ripple',
                    'standing_text': [
                        "The tides speak to those who listen.",
                        "I am Ripple. Tide Oracle of the Shallows.",
                        "If you seek guidance, I am here."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_primary_meet_renlo'
                }
            }
        ]
    },

    # ── Step 1: Renlo notices Syrin is withdrawn ──────────────────────────────
    # task_acquire_events updates Ripple's standing text now that the player
    # has been pointed toward Renlo. This is the correct place for a
    # directional hint — it fires before the player reaches Renlo, giving
    # them a nudge if they return to Ripple first.
    # Note: set_npc_standing_text on the meet target (Renlo) is redundant here
    # since the meet dialog fires immediately on arrival. It is omitted.
    {
        'task_id': 'shallows_primary_meet_renlo',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'saltcaller_renlo',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'ripple',
                    'standing_text': [
                        "Talk to Renlo at the market.",
                        "He notices things the water touches.",
                        "He may know something useful."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'saltcaller_renlo',
                    'dialog_id': 'renlo_notices_syrin'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'spirit',
                    'dialog_id': 'kaera_renlo_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_renlo_reaction'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'saltcaller_renlo',
                    'standing_text': [
                        "Go see Syrin. Just don't rush her.",
                        "She moves at tide-speed."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_primary_vigil_1'
                }
            }
        ]
    },

    # ── First visit: the party finds Syrin, mostly just stays ─────────────────
    {
        'task_id': 'shallows_primary_vigil_1',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vaultkeeper_syrin',
        'task_acquire_events': [
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'dialog_id': 'syrin_vigil_1'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'spirit',
                    'dialog_id': 'kaera_vigil_1'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'dialog_id': 'syrin_vigil_1_response'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_vigil_1'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_vigil_1'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'standing_text': [
                        "Come back when you're ready.",
                        "I'll be here."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_primary_vigil_2'
                }
            }
        ]
    },

    # ── Second visit: Syrin opens up ──────────────────────────────────────────
    {
        'task_id': 'shallows_primary_vigil_2',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vaultkeeper_syrin',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'dialog_id': 'syrin_vigil_2'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'spirit',
                    'dialog_id': 'kaera_vigil_2'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_vigil_2'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'dialog_id': 'syrin_vigil_2_response'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_vigil_2'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_vigil_2'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'standing_text': [
                        "Come back tomorrow.",
                        "I think I'm working toward something."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_primary_vigil_3'
                }
            }
        ]
    },

    # ── Third visit: Syrin releases the orb ───────────────────────────────────
    {
        'task_id': 'shallows_primary_vigil_3',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'vaultkeeper_syrin',
        'task_acquire_events': [],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'dialog_id': 'syrin_vigil_3'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'spirit',
                    'dialog_id': 'kaera_vigil_3'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'dialog_id': 'syrin_vigil_3_response'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_vigil_3'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_vigil_3'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_vigil_3'
                }
            },
            {
                'event_type': 'award_item',
                'params': {
                    'item_id': 'moontide_orb'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'vaultkeeper_syrin',
                    'standing_text': [
                        "The vault feels lighter.",
                        "That's not a bad thing."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_primary_meet_ripple'
                }
            }
        ]
    },

    # ── Deliver moontide_orb to Ripple — she joins here ───────────────────────
    # set_npc_standing_text in task_acquire_events is necessary here: this is
    # a deliver task. The player must go find the item then return. The
    # standing text is the only hint visible while they are away.
    {
        'task_id': 'shallows_primary_meet_ripple',
        'type': 'deliver',
        'to_type': 'npc',
        'to_id': 'ripple',
        'item_id': 'moontide_orb',
        'task_acquire_events': [
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'ripple',
                    'standing_text': [
                        "The tides are trembling more than ever.",
                        "If you found what you were looking for — bring it to me.",
                        "We are running out of time."
                    ]
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'ripple',
                    'dialog_id': 'ripple_intro'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'ripple',
                    'dialog_id': 'ripple_orb_received'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'spirit',
                    'dialog_id': 'kaera_ripple_join_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'magic',
                    'dialog_id': 'moxie_ripple_join_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'skill',
                    'dialog_id': 'poise_ripple_join_reaction'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'tech',
                    'dialog_id': 'kade_ripple_join_reaction'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {'npc_id': 'ripple'}
            },
            {
                'event_type': 'character_join',
                'params': {'character_id': 'ripple'}
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'shallows_primary_defeat_uulthar'
                }
            }
        ]
    },

    # ── Meet Uul'thar in dungeon — confrontation scene ────────────────────────
    {
        'task_id': 'shallows_primary_defeat_uulthar',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'uulthar',
        'task_acquire_events': [
            {
                'event_type': 'create_npc',
                'params': {
                    'npc_id': 'uulthar',
                    'location': None
                }
            },
            {
                'event_type': 'create_dungeon',
                'params': {
                    'dungeon_id': 'uulthar_lair',
                    'location': 'region_open_area'
                }
            },
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'uulthar_lair', 'item_id': 'moontide_staff', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'uulthar_lair', 'item_id': 'abyssal_flow_robe', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'uulthar_lair', 'item_id': 'tidecaller_veil', 'location': 'treasure_room' }},
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'uulthar',
                    'dialog_id': 'uulthar_intro'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'ripple',
                    'dialog_id': 'ripple_uulthar_confrontation'
                }
            },
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'uulthar',
                    'dialog_id': 'uulthar_confrontation_reply'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'technique',
                    'dialog_id': 'chock_uulthar_challenge'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'spirit',
                    'dialog_id': 'kaera_uulthar_challenge'
                }
            },
            {
                'event_type': 'set_npc_standing_text',
                'params': {
                    'npc_id': 'uulthar',
                    'standing_text': [
                        "The after begins.",
                        "The tides are mine to rewrite."
                    ]
                }
            },
            {
                'event_type': 'award_task',
                'params': {
                    'task_id': 'defeat_uulthar'
                }
            }
        ]
    },

    # ── Defeat Uul'thar — void hint + Ripple arc resolution ──────────────────
    {
        'task_id': 'defeat_uulthar',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'uulthar_1',
        'task_acquire_events': [
            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'uulthar_1',
                    'combat_type': 'boss_battle'
                }
            }
        ],
        'task_complete_events': [
            {
                'event_type': 'initiate_dialog',
                'params': {
                    'npc_id': 'uulthar',
                    'dialog_id': 'uulthar_defeat'
                }
            },
            {
                'event_type': 'hide_npc',
                'params': {'npc_id': 'uulthar'}
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'ripple',
                    'dialog_id': 'ripple_post_defeat'
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
                    'npc_id': 'skill',
                    'dialog_id': 'poise_post_defeat'
                }
            },
            {
                'event_type': 'initiate_character_dialog',
                'params': {
                    'npc_id': 'technique',
                    'dialog_id': 'chock_post_defeat'
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
                'event_type': 'complete_region_quest',
                'params': {'region_id': 'shallows'}
            }
        ]
    }
]


PRIMARY_STORY_SETTINGS = {
    'story_id': 'shallows_primary_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}