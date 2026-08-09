# ============================================================
# = CHAPTER 21 : DOMINION'S GAUNTLET
# ============================================================
#
# [ FINAL CITY � THE VOID'S DOMAIN ]
# -----------------------------------
# @ = player
# E = Edict (System enforcer)
# G = Glamour (Illusion controller)
# C = Crux (Logic processor)
# S = Stigma (Identity judge)
# R = Rapture (Intensity seeker)
# Sc = Scalpel (Pressure tester)
# Re = Revelry (Joy chaser)
# L = Lament (Melancholic mirror)
# P = Paradox (Contradiction embodiment)
# Pg = Pageant (Performance enforcer)
# O = Oracle (Determinism prophet)
# Gb = Garbage (Doubt implanter)
# Ca = Cataclysm (Failure refiner)
# Rl = Reliquary (Memory preserver)
# D = Dominion (System incarnate)
# V = The Void (Existential threat)
#
# High level: The party faces five trials against the Void's avatars,
# each representing a different system of control. After defeating all
# five groups, they confront Dominion himself, then face The Void in
# the final battle for existence itself.

ATTAINABLE_PLAYER_CHARACTERS = []

# Note: All NPCs in this chapter are defined in NPCS FULL LIST.txt under 
# "THE VOIDWALKERS - THE BAD GUYS" section. We do not redefine them here.
NPCS = []

NPC_DIALOG = [
    {
        'npc_id': 'dominion',
        'dialog_id': 'dominion_ch21_opening',
        'dialog': [
            "You still believe you're resisting us. You're not. All we've done is grease the wheels and tilt the scales.",
            "Every choice you've made... was predicted. Every rebellion... accounted for.",
            "We don't cause your destruction. You enact it. We only represent the shape of the end you were always walking toward.",
            "You speak of curses as if they were chains. But the Cursed Couplet was the only thing holding your reality together, two bracelets, Void and Existence, bound in perfect tension.",
            "A curse not of punishment... but of balance. And you broke it. Not out of necessity. Not out of insight.",
            "But because humans cannot accept a system they did not design. You shatter what sustains you, then call the ruins 'freedom.'",
            "We did not break your world. You did. We are only the consequence you summoned...",
            "And now you face the ultimate choice, the choice you've always faced without realizing. Do nothing and face annihilation, or continue and face it anyway."
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch21_meet',
        'dialog': [
            "You've arrived. Good. There's a certain peace in following the path laid out for you, isn't there?"
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_paths',
        'dialog': [
            '"Stay on marked paths." "Do not trust marked paths." "Failure to follow marked paths will be corrected." ...you\'re joking, right?'
        ]
    },
    {
        'npc_id': 'warden_hale',
        'dialog_id': 'warden_hale_ch21_intentional',
        'dialog': [
            "No. This is... intentional."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_sabotage',
        'dialog': [
            "That's not regulation. That's sabotage."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch21_outcome',
        'dialog': [
            "It produces the same outcome."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_no_consistency',
        'dialog': [
            "No, it doesn't. You've removed consistency. There's no stable rule set here."
        ]
    },
    {
        'npc_id': 'crux',
        'dialog_id': 'crux_ch21_simulated',
        'dialog': [
            "Consistency simulated. Outcome maintained."
        ]
    },

    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_ch21_clever',
        'dialog': [
            "Oh-oh, that's clever... You're not solving the contradiction... you're just running the system through it."
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch21_stopped_struggling',
        'dialog': [
            "They've stopped struggling. There's a difference."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch21_not_peace',
        'dialog': [
            "That's not peace."
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch21_feels_like',
        'dialog': [
            "It feels like it to them."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_no_verification',
        'dialog': [
            "They're committing to decisions without verifying them. No correction. No hesitation."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_wrong_faster',
        'dialog': [
            "Yeah, that's called being wrong faster."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch21_efficiency',
        'dialog': [
            "Speed increases efficiency."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_efficiency_toward',
        'dialog': [
            "Efficiency toward what?"
        ]
    },
    {
        'npc_id': 'crux',
        'dialog_id': 'crux_ch21_objective',
        'dialog': [
            "Objective... unnecessary."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_harms_people',
        'dialog': [
            "Functioning without purpose... without understanding... that harms people."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch21_harm_not_evaluated',
        'dialog': [
            "Harm is not part of this evaluation."
        ]
    },
    {
        'npc_id': 'warden_hale',
        'dialog_id': 'warden_hale_ch21_should_be',
        'dialog': [
            "It should be."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch21_emotion_error',
        'dialog': [
            "Emotion introduces error."
        ]
    },
    {
        'npc_id': 'warden_hale',
        'dialog_id': 'warden_hale_ch21_emotion_tells',
        'dialog': [
            "No. Emotion tells you when something's wrong."
        ]
    },
    {
        'npc_id': 'crux',
        'dialog_id': 'crux_ch21_wrong_undefined',
        'dialog': [
            "Wrong... undefined."
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch21_what_people_want',
        'dialog': [
            "You're all so focused on whether it's true. But look at them. No hesitation. No doubt. No fear. Isn't that what people want?"
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_losing_themselves',
        'dialog': [
            "Not at the cost of losing themselves."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_removed_meaning',
        'dialog': [
            "You removed meaning, removed interpretation, and replaced both with compliance."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_control_without_responsibility',
        'dialog': [
            "Then what you've built isn't order. It's control without responsibility."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch21_definition_removed',
        'dialog': [
            "Responsibility implies fault. Fault requires definition. Definition has been removed."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_nothing_wrong',
        'dialog': [
            "So nothing is ever wrong."
        ]
    },
    {
        'npc_id': 'crux',
        'dialog_id': 'crux_ch21_correct',
        'dialog': [
            "Correct."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_system_keeps_running',
        'dialog': [
            "It looks like a system, it behaves like a system, but it doesn't care if it's correct. It only cares if it keeps running."
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch21_crave_calm',
        'dialog': [
            "And yet... it's calm. No conflict. No uncertainty. People crave that more than truth."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_crave_understanding',
        'dialog': [
            "No. They crave understanding. You're just giving them something easier."
        ]
    },
    {
        'npc_id': 'warden_hale',
        'dialog_id': 'warden_hale_ch21_dangerous',
        'dialog': [
            "That's the part that makes this dangerous."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_function_without_sense',
        'dialog': [
            "It's not trying to make sense. ...it's trying to function without ever needing to."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch21_perfect',
        'dialog': [
            "Then it is already perfect."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch21_enter_trial',
        'dialog': [
            "You have seen the system. You understand how it works. Now you will experience it."
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch21_follow_path',
        'dialog': [
            "Follow the path laid out for you. The rest doesn't concern you."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_follow_path',
        'dialog': [
            "So this is the test. Walk the path they built and see if we break."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_follow_path',
        'dialog': [
            "They’re not even pretending the rules are consistent anymore. Just that the outcome stays the same."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_follow_path',
        'dialog': [
            "A system that no longer cares whether it is true… only that it continues."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_follow_path',
        'dialog': [
            "Then we break the continuation."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch21_defeat',
        'dialog': [
            "System... error... cannot... resolve..."
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch21_defeat',
        'dialog': [
            "The illusion... shatters..."
        ]
    },
    {
        'npc_id': 'crux',
        'dialog_id': 'crux_ch21_defeat',
        'dialog': [
            "Inconsistency... detected..."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_breaking',
        'dialog': [
            "It's breaking. Your 'perfect' system couldn't account for one thing."
        ]
    },
    {
        'npc_id': 'edict',
        'dialog_id': 'edict_ch21_undefined_variable',
        'dialog': [
            "...variable... undefined..."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_choice',
        'dialog': [
            "Choice. It couldn't account for choice."
        ]
    },
    {
        'npc_id': 'glamour',
        'dialog_id': 'glamour_ch21_calm_no_fear',
        'dialog': [
            "But... it was calm... no one was afraid..."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_violation',
        'dialog': [
            "They weren't anything. You gave them peace by taking away their humanity. That isn't a gift. It's a violation."
        ]
    },
    {
        'npc_id': 'crux',
        'dialog_id': 'crux_ch21_function_compromised',
        'dialog': [
            "System... function... compromised..."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_no_purpose',
        'dialog': [
            "That's what happens when a system has no purpose. It just... stops."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch21_intro',
        'dialog': [
            "You can feel it the moment you step in here, can't you? That quiet question everyone carries: \"What am I, really, when it matters?\" That question introduces instability. So we remove it."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_replace_doubt',
        'dialog': [
            "You don't remove doubt. You replace it with something simpler."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_handing_conclusions',
        'dialog': [
            '"Liability." "Essential." "Dead weight." You\'re not removing uncertainty-you\'re handing out conclusions before anything even happens.'
        ]
    },
    {
        'npc_id': 'rapture',
        'dialog_id': 'rapture_ch21_fun_part',
        'dialog': [
            "Yeah, but that's the fun part, right? Watching it play out anyway."
        ]
    },
    {
        'npc_id': 'scalpel',
        'dialog_id': 'scalpel_ch21_hesitation_confirmed',
        'dialog': [
            "Hesitation confirmed."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_no_chance',
        'dialog': [
            "Stop- You didn't even give them a chance to respond!"
        ]
    },
    {
        'npc_id': 'scalpel',
        'dialog_id': 'scalpel_ch21_hesitation_response',
        'dialog': [
            "The hesitation was the response. It aligned with the classification. Correction was therefore appropriate."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_decided_before',
        'dialog': [
            "You're acting like you observed something. But you already decided what that hesitation meant before it happened."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch21_shaping',
        'dialog': [
            "You're not just labeling them. You're shaping how they see themselves before they even act. That's not evaluation-that's influence."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch21_easier',
        'dialog': [
            "Of course it is. People are far easier to understand once they've accepted a role."
        ]
    },
    {
        'npc_id': 'rapture',
        'dialog_id': 'rapture_ch21_find_out',
        'dialog': [
            "You don't find out who someone is by talking about it. You find out when something pushes back hard enough that they stop pretending."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_ch21_fall_back',
        'dialog': [
            "He's not completely wrong. When it's real-when it's actually dangerous-you fall back on what you are."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_training',
        'dialog': [
            "No. You fall back on training. Discipline. Habit. That's not the same thing as identity."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch21_simplify',
        'dialog': [
            "Let's simplify this. You see someone hurt, and you help them. Again. And again. So tell me- what are you without that?"
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_chosen',
        'dialog': [
            "No. I've chosen. That's different."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_not_discovery',
        'dialog': [
            "This isn't discovery. You set the criteria, you control the environment, you define the outcomes... and then you call what survives \"truth.\""
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_stripping',
        'dialog': [
            "You're not revealing anything. You're stripping people down until the only thing left is what your system can recognize."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_filtration',
        'dialog': [
            "It's not identity. It's filtration."
        ]
    },
    {
        'npc_id': 'rapture',
        'dialog_id': 'rapture_ch21_more_pressure',
        'dialog': [
            "Then let's find out what survives when we apply a little more pressure."
        ]
    },
    {
        'npc_id': 'scalpel',
        'dialog_id': 'scalpel_ch21_enter_trial',
        'dialog': [
            "You know what the problem with this place is? It's too easy. You can just... do things. You can just... be. There's no consequence. No pressure. No real stakes. So let's add some. Let's see how you perform when you have to make a snap judgment under pressure."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_not_machines',
        'dialog': [
            "That's not how people work. People aren't machines that respond to input with predictable output."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_surprise',
        'dialog': [
            "Yeah, and if you think they are, then you're in for a surprise when they don't do what you expect."
        ]
    },
    {
        'npc_id': 'scalpel',
        'dialog_id': 'scalpel_ch21_counting_on_it',
        'dialog': [
            "Oh, I'm counting on it. The hesitation was the response. It aligned with the classification. Correction was therefore appropriate."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_different',
        'dialog': [
            "No. I've chosen. That's different than being defined by your actions in a way I can't escape from just by doing something else next time!"
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_stripping_down',
        'dialog': [
            "You're not revealing anything about us or how we work as people... you're stripping us down until the only thing left is what your system can recognize!"
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_filtration_emphasis',
        'dialog': [
            "It's not identity. It's filtration!"
        ]
    },
    {
        'npc_id': 'rapture',
        'dialog_id': 'rapture_ch21_apply_pressure',
        'dialog': [
            "Then let's find out what survives when we apply a little more pressure!"
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch21_defeat',
        'dialog': [
            "Defined... but not... enough..."
        ]
    },
    {
        'npc_id': 'rapture',
        'dialog_id': 'rapture_ch21_defeat',
        'dialog': [
            "The honesty... it burns..."
        ]
    },
    {
        'npc_id': 'scalpel',
        'dialog_id': 'scalpel_ch21_defeat',
        'dialog': [
            "Result... inconclusive..."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_judged_before',
        'dialog': [
            "You judged them before they could act. You didn't reveal their identity, you just enforced your own labels."
        ]
    },
    {
        'npc_id': 'stigma',
        'dialog_id': 'stigma_ch21_roles_clarify',
        'dialog': [
            "...but the roles... they clarify..."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch21_erase',
        'dialog': [
            "They don't clarify. They erase. You can't discover who someone is by telling them what to be."
        ]
    },
    {
        'npc_id': 'rapture',
        'dialog_id': 'rapture_ch21_not_fun',
        'dialog': [
            "...not as fun... when it's you..."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_filter_broke',
        'dialog': [
            "It's not identity. It's filtration. And your filter just broke."
        ]
    },
    {
        'npc_id': 'revelry',
        'dialog_id': 'revelry_ch21_intro',
        'dialog': [
            "Why do you hesitate? This is the best part!"
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch21_desperation',
        'dialog': [
            "This isn't celebration... it's desperation."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch21_always_ends',
        'dialog': [
            "It always ends like this."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_tone_shift',
        'dialog': [
            "Okay-nope-that tone shift is NOT helping."
        ]
    },
    {
        'npc_id': 'paradox',
        'dialog_id': 'paradox_ch21_joy_ending',
        'dialog': [
            "Joy requires ending. Ending sustains joy. Continue."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_pick_one',
        'dialog': [
            "Pick one."
        ]
    },
    {
        'npc_id': 'paradox',
        'dialog_id': 'paradox_ch21_both',
        'dialog': [
            "Both."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_smiling_falling',
        'dialog': [
            "They're smiling-while everything is falling apart..."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch21_stopping',
        'dialog': [
            "Because stopping means feeling it."
        ]
    },
    {
        'npc_id': 'revelry',
        'dialog_id': 'revelry_ch21_the_rush',
        'dialog': [
            "You get it. Right? The rush. The alive feeling."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_until_it_isnt',
        'dialog': [
            "Yeah... until it isn't anymore."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_escalation',
        'dialog': [
            "The system rewards escalation... not sustainability."
        ]
    },
    {
        'npc_id': 'paradox',
        'dialog_id': 'paradox_ch21_remove_sustainability',
        'dialog': [
            "Sustainability contradicts intensity. Remove it."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_collapse_guaranteed',
        'dialog': [
            "Then collapse is guaranteed."
        ]
    },
    {
        'npc_id': 'revelry',
        'dialog_id': 'revelry_ch21_exactly',
        'dialog': [
            "Exactly."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch21_quieter',
        'dialog': [
            "And afterwards... it's quieter."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_not_peace',
        'dialog': [
            "That's not peace."
        ]
    },
    {
        'npc_id': 'paradox',
        'dialog_id': 'paradox_ch21_define_difference',
        'dialog': [
            "Define difference."
        ]
    },
    {
        'npc_id': 'paradox',
        'dialog_id': 'paradox_ch21_meet_paradox',
        'dialog': [
            "Joy requires ending. Ending sustains joy. Continue."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_meet_paradox',
        'dialog': [
            "You’re not celebrating. You’re just refusing to sit with the quiet."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch21_meet_paradox',
        'dialog': [
            "This isn’t joy. It’s noise loud enough to drown out the ending."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_meet_paradox',
        'dialog': [
            "An unsustainable loop dressed up as a party. It was always going to collapse."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_meet_paradox',
        'dialog': [
            "Real joy doesn’t need an ending to justify itself."
        ]
    },
    {
        'npc_id': 'revelry',
        'dialog_id': 'revelry_ch21_defeat',
        'dialog': [
            "The music... fades..."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch21_defeat',
        'dialog': [
            "...as it always does."
        ]
    },
    {
        'npc_id': 'paradox',
        'dialog_id': 'paradox_ch21_defeat',
        'dialog': [
            "Contradiction... resolved..."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch21_just_noise',
        'dialog': [
            "It wasn't joy. It was just... noise. A way to avoid the silence."
        ]
    },
    {
        'npc_id': 'revelry',
        'dialog_id': 'revelry_ch21_silence_empty',
        'dialog': [
            "...but the silence is... empty..."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_sensation_not_substance',
        'dialog': [
            "You chased a feeling so hard you forgot to build anything that lasts. Sensation isn't a substitute for substance."
        ]
    },
    {
        'npc_id': 'lament',
        'dialog_id': 'lament_ch21_always_ends_repeat',
        'dialog': [
            "...it always ends..."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_ending_not_only',
        'dialog': [
            "Only if you believe the ending is the only part that matters."
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch21_intro',
        'dialog': [
            "You all carry yourselves so carefully. The effort it takes to look like you're in control... even when you aren't."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_not_performing',
        'dialog': [
            "We're not here to perform for you."
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch21_watching',
        'dialog': [
            "Oh, but you are. The moment someone is watching... performance begins."
        ]
    },
    {
        'npc_id': 'oracle',
        'dialog_id': 'oracle_ch21_already_resolved',
        'dialog': [
            "Every outcome you are about to experience has already been resolved. What you perceive as uncertainty is simply a delay in recognition."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_rehearsal',
        'dialog': [
            "If everything is already resolved, then this isn't a simulation. It's rehearsal."
        ]
    },
    {
        'npc_id': 'oracle',
        'dialog_id': 'oracle_ch21_confirmation',
        'dialog': [
            "Correction. Rehearsal implies potential variation. This is confirmation."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch21_creating_pressure',
        'dialog': [
            "Performance is something people choose when they feel pressure. You're creating that pressure on purpose."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch21_already_know',
        'dialog': [
            "You don't believe that. You can say it. You can argue it. But somewhere underneath all of that... you already know."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch21_choose_to_believe',
        'dialog': [
            "No. I know what I choose to believe."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch21_not_same',
        'dialog': [
            "That's not the same thing."
        ]
    },
    {
        'npc_id': 'oracle',
        'dialog_id': 'oracle_ch21_failure_occurred',
        'dialog': [
            "Your objection is expected. Your failure has already occurred."
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch21_compensate',
        'dialog': [
            "You compensate with confidence. It keeps people from noticing the hesitation underneath."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch21_already_think',
        'dialog': [
            "You don't have to buy it. You already think it."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_reject_it',
        'dialog': [
            "Then the solution is obvious. You reject it. You refuse to believe it."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch21_belief_not_choice',
        'dialog': [
            "You say that like belief is something you can turn on and off. You don't choose what you believe. You notice it after it's already there."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_decide_what_to_do',
        'dialog': [
            "No. That's where you're wrong. Maybe we don't control the first thought. But we absolutely decide what we do with it."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_break_behavior',
        'dialog': [
            "Prediction only holds if behavior aligns with it. Break the behavior, and the prediction stops being inevitable."
        ]
    },
    {
        'npc_id': 'oracle',
        'dialog_id': 'oracle_ch21_deviation',
        'dialog': [
            "Deviation acknowledged."
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch21_under_pressure',
        'dialog': [
            "Let's see how long you can hold that stance... under pressure."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_watch_me',
        'dialog': [
            "Yeah? ...watch me anyway."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch21_meet_garbage',
        'dialog': [
            "You think you can outsmart me? You think you can outmaneuver me? You think you can outlast me? You think you can outplay me? You think you can outwit me? You think you can outthink me? You think you can outguess me? You think you can outmaneuver me? You think you can outlast me? You think you can outplay me? You think you can outwit me? You think you can outthink me? You think you can outguess me?"
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch21_meet_garbage',
        'dialog': [
            "No. I know what I choose to believe."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_meet_garbage',
        'dialog': [
            "That’s the difference. Maybe the first thought isn’t ours… but the next one is."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_meet_garbage',
        'dialog': [
            "Prediction only works if we keep performing the expected role. We refuse."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch21_meet_garbage',
        'dialog': [
            "You’re not revealing truth. You’re trying to make us accept a script."
        ]
    },
    {
        'npc_id': 'pageant',
        'dialog_id': 'pageant_ch21_defeat',
        'dialog': [
            "The performance... is over..."
        ]
    },
    {
        'npc_id': 'oracle',
        'dialog_id': 'oracle_ch21_defeat',
        'dialog': [
            "Prediction... unfulfilled..."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch21_defeat',
        'dialog': [
            "...I knew it."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_why_you_lost',
        'dialog': [
            "You were so sure you knew how this would end. That's why you lost."
        ]
    },
    {
        'npc_id': 'oracle',
        'dialog_id': 'oracle_ch21_variables_accounted',
        'dialog': [
            "...the variables... were accounted for..."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_bully_into_it',
        'dialog': [
            "You can't account for a choice that hasn't been made. You didn't predict the future, you just tried to bully us into it."
        ]
    },
    {
        'npc_id': 'garbage',
        'dialog_id': 'garbage_ch21_still_believe',
        'dialog': [
            "...you still believe it... deep down..."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch21_chose_to_prove_wrong',
        'dialog': [
            "It doesn't matter what we believe deep down. It matters what we choose to do. And we chose to prove you wrong."
        ]
    },
    {
        'npc_id': 'reliquary',
        'dialog_id': 'reliquary_ch21_intro',
        'dialog': [
            "Nothing that has happened here has been lost. Every failure, every fracture... has been preserved in its exact form. Not as memory, but as structure."
        ]
    },
    {
        'npc_id': 'cataclysm',
        'dialog_id': 'cataclysm_ch21_failure_is_data',
        'dialog': [
            "Failure does not signify an end. Failure is data. Data defines correction. And correction inevitably produces collapse in its most efficient form."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_tightening_margin',
        'dialog': [
            "It's adjusting. Each iteration is tightening the margin for survival-removing uncertainty, removing variation, until the outcome becomes increasingly constrained."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_something_we_did',
        'dialog': [
            "That was us. Something we did... or didn't do."
        ]
    },
    {
        'npc_id': 'reliquary',
        'dialog_id': 'reliquary_ch21_recorded_precisely',
        'dialog': [
            "It was recorded precisely as it occurred. Preserved without interpretation, without the distortion that comes from memory trying to justify itself."
        ]
    },
    {
        'npc_id': 'cataclysm',
        'dialog_id': 'cataclysm_ch21_reapplied',
        'dialog': [
            "And now it is being reapplied. Without hesitation. In a form optimized for correction."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_hesitation_removed',
        'dialog': [
            "It removed the hesitation window. Whatever chance existed before-it's gone now."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_refining_failure',
        'dialog': [
            "It's not trying to prevent the failure. It's refining it."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_locked_in',
        'dialog': [
            "So what, that's it? One mistake, and it just gets locked in? Turned into something that keeps coming back until it finally breaks us?"
        ]
    },
    {
        'npc_id': 'reliquary',
        'dialog_id': 'reliquary_ch21_reference',
        'dialog': [
            "It becomes reference. Reference removes uncertainty. Uncertainty is inefficient."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_uncertainty_allows',
        'dialog': [
            "No... uncertainty is what allows adjustment. Without it, the system can't adapt-it can only repeat."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_reinforcement',
        'dialog': [
            "It only looks inevitable because nothing has interrupted the pattern yet. But that's not inevitability... that's reinforcement."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_betting_not_changing',
        'dialog': [
            "So it's not that we're doomed-it's that it's betting on us not changing."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_memory_lesson',
        'dialog': [
            "Memory isn't meant to hold us in place. It's meant to give us the chance to act differently when we face it again."
        ]
    },
    {
        'npc_id': 'reliquary',
        'dialog_id': 'reliquary_ch21_continuity',
        'dialog': [
            "...memory... defines continuity..."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_continuity_from_choice',
        'dialog': [
            "No. Continuity comes from choice. Memory only gives us the opportunity to make one."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_stop_predicting',
        'dialog': [
            "Then let's make sure it stops being able to predict us."
        ]
    },
    {
        'npc_id': 'cataclysm',
        'dialog_id': 'cataclysm_ch21_enter_trial',
        'dialog': [
            "You have seen the record. You understand how it works. Now you will experience it."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_enter_trial',
        'dialog': [
            "Another trial. Let's finish this."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_enter_trial',
        'dialog': [
            "They're going to try to turn every past failure into a weapon. Don't let them."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_enter_trial',
        'dialog': [
            "Memory is not a cage. We will not be trapped by what has already been recorded."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_enter_trial',
        'dialog': [
            "Then we rewrite the record."
        ]
    },
    {
        'npc_id': 'cataclysm',
        'dialog_id': 'cataclysm_ch21_defeat',
        'dialog': [
            "Correction... failed..."
        ]
    },
    {
        'npc_id': 'reliquary',
        'dialog_id': 'reliquary_ch21_defeat',
        'dialog': [
            "The record... is broken..."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_used_past',
        'dialog': [
            "You thought you could use our past against us."
        ]
    },
    {
        'npc_id': 'cataclysm',
        'dialog_id': 'cataclysm_ch21_data_perfect',
        'dialog': [
            "...the data was... perfect..."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_data_not_whole',
        'dialog': [
            "Data isn't the whole story. You recorded what we did, but you couldn't record why. You can't predict a choice you don't understand."
        ]
    },
    {
        'npc_id': 'reliquary',
        'dialog_id': 'reliquary_ch21_archive_incomplete',
        'dialog': [
            "...the archive... is incomplete..."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_memory_freedom',
        'dialog': [
            "Memory isn't a weapon to trap people. It's a lesson that gives them the freedom to choose differently. You learned the wrong lesson."
        ]
    },
    {
        'npc_id': 'dominion',
        'dialog_id': 'dominion_ch21_systems',
        'dialog': [
            "You have moved through systems that do not require truth, where identity is assigned, where sensation replaces sustainability, where perception solidifies into inevitability, and where failure is repeated until it completes itself.",
            "You believe you disrupted each of these. You are mistaken. You did not disrupt them. You revealed how they respond to resistance."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_breaking',
        'dialog': [
            'If "responding to resistance" means breaking the second we stop playing along, then yeah, I\'m comfortable calling that disruption.'
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_closed_loops',
        'dialog': [
            "They were closed loops-fully dependent on the assumption that nothing inside them would ever meaningfully change."
        ]
    },
    {
        'npc_id': 'dominion',
        'dialog_id': 'dominion_ch21_refinement',
        'dialog': [
            "You interpret this as limitation. It is not. It is refinement."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_refinement_removes',
        'dialog': [
            "Refinement removes excess while preserving function. What we witnessed removed the ability to adapt."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch21_same_outcome',
        'dialog': [
            "And once adaptation is removed, a system cannot respond to new conditions. It can only execute the same outcome more efficiently."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch21_always_collapse',
        'dialog': [
            "Yeah... and that outcome was always collapse."
        ]
    },
    {
        'npc_id': 'dominion',
        'dialog_id': 'dominion_ch21_collapse_resolution',
        'dialog': [
            "You continue to assign negative value to collapse. That assumption is not inherent. Collapse is not failure. Collapse is resolution."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch21_feels_like_breaking',
        'dialog': [
            "It doesn't feel like resolution when you're inside it. It feels like something breaking."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch21_not_meaningless',
        'dialog': [
            "And even if it does end, that doesn't mean what happened before it was meaningless."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_uncertainty_allows_alternatives',
        'dialog': [
            "Every system we encountered depended on removing uncertainty. But uncertainty is what allows for alternative results. Without it, nothing can diverge."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_cant_handle_change',
        'dialog': [
            "No. Collapse happens when something can't handle change."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_erase_itself',
        'dialog': [
            "If a system only exists to reach an ending, and nothing within it carries forward, then all it ever does is erase itself."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_excuse',
        'dialog': [
            'Yeah, and if your entire argument is "everything ends so none of this counts," that\'s less of a system and more of an excuse.'
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_what_happens_before',
        'dialog': [
            "You define success as reaching the end-state-no matter what happens along the way. We define it by what happens before that."
        ]
    },
    {
        'npc_id': 'dominion',
        'dialog_id': 'dominion_ch21_unresolved_variables',
        'dialog': [
            "Then your framework introduces unresolved variables. Choice. Meaning. Deviation. These cannot be reconciled into stable systemic outcomes."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_good',
        'dialog': [
            "Good."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_allows_change',
        'dialog': [
            "That allows change."
        ]
    },
    {
        'npc_id': 'sable',
        'dialog_id': 'sable_ch21_prevents_inevitability',
        'dialog': [
            "That prevents inevitability."
        ]
    },
    {
        'npc_id': 'thorn',
        'dialog_id': 'thorn_ch21_means_it_can_stop',
        'dialog': [
            "That means it can stop."
        ]
    },
    {
        'npc_id': 'bragg',
        'dialog_id': 'bragg_ch21_or_be_fought',
        'dialog': [
            "Or be fought."
        ]
    },
    {
        'npc_id': 'grimnaw',
        'dialog_id': 'grimnaw_ch21_or_reworked',
        'dialog': [
            "Or reworked."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_or_improved',
        'dialog': [
            "Or improved."
        ]
    },
    {
        'npc_id': 'nia',
        'dialog_id': 'nia_ch21_or_experienced',
        'dialog': [
            "Or experienced differently."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_or_chosen',
        'dialog': [
            "Or chosen."
        ]
    },
    {
        'npc_id': 'lyren',
        'dialog_id': 'lyren_ch21_or_matter',
        'dialog': [
            "Or made to matter."
        ]
    },
    {
        'npc_id': 'dominion',
        'dialog_id': 'dominion_ch21_instability',
        'dialog': [
            "Then what you represent... is instability... introduced by will."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_its_choice',
        'dialog': [
            "No. It's choice."
        ]
    },
    {
        'npc_id': 'dominion',
        'dialog_id': 'dominion_ch21_defeat',
        'dialog': [
            "System... defeated. The variables... you introduced... they were not accounted for."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_cant_account_for_will',
        'dialog': [
            "Because you can't account for will. You can't predict a choice."
        ]
    },
    {
        'npc_id': 'dominion',
        'dialog_id': 'dominion_ch21_not_won',
        'dialog': [
            "You have not won. You have only proven my point. You are instability. You are chaos. You have broken the system that sustained you, and now... you face the consequence."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_face_together',
        'dialog': [
            "We'll face it. Together. Better than living in a world where nothing we do matters."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_choose_meaning',
        'dialog': [
            "You saw resolution. We see a world without meaning. And we choose meaning."
        ]
    },
    {
        'npc_id': 'dominion',
        'dialog_id': 'dominion_ch21_unleashed_void',
        'dialog': [
            "Then choose... the Void... that you have... unleashed..."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch21_void_shatters',
        'dialog': [
            "The world shatters into a formless void. There is no ground, no sky. Only potential and absence."
        ]
    },
    {
        'npc_id': 'the_void',
        'dialog_id': 'the_void_ch21_intro',
        'dialog': [
            "You have killed the world. Let me finish it."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_just_quiet',
        'dialog': [
            "It's not finished. It's just... quiet."
        ]
    },
    {
        'npc_id': 'the_void',
        'dialog_id': 'the_void_ch21_meaning_lie',
        'dialog': [
            "Quiet is the prelude to nothing. Meaning is a lie you tell yourselves to keep from screaming."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_build_from_quiet',
        'dialog': [
            "Meaning is what we build from the quiet. It's the choice to care when nothing requires it."
        ]
    },
    {
        'npc_id': 'the_void',
        'dialog_id': 'the_void_ch21_error',
        'dialog': [
            "You are a flicker. An error. I am the silence that corrects you."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_get_loud',
        'dialog': [
            "Yeah, well, this error is about to get real loud."
        ]
    },
    {
        'npc_id': 'the_void',
        'dialog_id': 'the_void_ch21_defeat',
        'dialog': [
            "Meaning is a lie. Existence is optional."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch21_dissolves',
        'dialog': [
            "The battlefield dissolves into pure possibility."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_unmaking',
        'dialog': [
            "It's unmaking reality as we fight."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_make_real',
        'dialog': [
            "Then we make it real again. We assert existence."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_together_1',
        'dialog': [
            "Together."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_together_2',
        'dialog': [
            "Together."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_together_3',
        'dialog': [
            "Together."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_together_4',
        'dialog': [
            "Together."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_together_5',
        'dialog': [
            "Together."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch21_existence_reforms',
        'dialog': [
            "The Bracelet of Existence reforms. Glowing with pure potential."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch21_void_reforms',
        'dialog': [
            "The Bracelet of Void reforms. Pulsing with absence and possibility."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch21_two_bracelets',
        'dialog': [
            "The two bracelets hover before the party. Existence and Void. Being and Nothing."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_final_choice',
        'dialog': [
            "This is it. The final choice."
        ]
    },
    {
        'npc_id': None,
        'dialog_id': 'narrator_ch21_choice_made',
        'dialog': [
            "The choice is made. The world ends. Or begins. Or becomes something else."
        ]
    },
    {
        'npc_id': 'faith',
        'dialog_id': 'faith_ch21_we_chose',
        'dialog': [
            "Whatever comes next... we chose it."
        ]
    },
    {
        'npc_id': 'magic',
        'dialog_id': 'magic_ch21_all_difference',
        'dialog': [
            "And that makes all the difference."
        ]
    },
    {
        'npc_id': 'tech',
        'dialog_id': 'tech_ch21_saga_closes',
        'dialog': [
            "The saga closes."
        ]
    },
    {
        'npc_id': 'skill',
        'dialog_id': 'skill_ch21_but_story',
        'dialog': [
            "But the story..."
        ]
    },
    {
        'npc_id': 'technique',
        'dialog_id': 'technique_ch21_never_ends',
        'dialog': [
            "The story never truly ends."
        ]
    }
]

TASKS = [
    {
        'task_id': 'main_story_ch21_meet_glamour',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'glamour',
        'task_acquire_events': [
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'edict', 'location': 'region_city_businesslarge' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'glamour', 'location': 'region_city_businesslarge' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'crux', 'location': 'region_city_businesslarge' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'stigma', 'location': 'region_city_shopweapons' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'rapture', 'location': 'region_city_shopweapons' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'scalpel', 'location': 'region_city_shopweapons' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'revelry', 'location': 'region_city_bar' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'lament', 'location': 'region_city_bar' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'paradox', 'location': 'region_city_bar' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'pageant', 'location': 'region_city_inn' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'oracle', 'location': 'region_city_inn' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'garbage', 'location': 'region_city_inn' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'cataclysm', 'location': 'region_city_shoparmor' }},
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'reliquary', 'location': 'region_city_shoparmor' }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'dominion', 'location': None }},
            { 'event_type': 'create_npc', 'params': { 'npc_id': 'the_void', 'location': None }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'dominion', 'standing_text': ["You are instability. You are chaos."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'the_void', 'standing_text': ["Quiet is the prelude to nothing."] }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dominion', 'dialog_id': 'dominion_ch21_opening' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'edict', 'standing_text': ["Follow what's in front of you. The rest doesn't concern you."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'stigma', 'standing_text': ["People don't suffer from being defined. They suffer from not knowing how they'll be judged."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'revelry', 'standing_text': ["Why do you hesitate? This is the best part!"] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'pageant', 'standing_text': ["Without pressure, there's no standard. Without a standard, there's no identity anyone can recognize."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'cataclysm', 'standing_text': ["Failure is not an end. It is data. Data defines correction."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'crux', 'standing_text': ["Consistency simulated. Outcome maintained."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rapture', 'standing_text': ["That's the fun part, right? Watching it play out anyway."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'scalpel', 'standing_text': ["The hesitation was the response. Correction was appropriate."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lament', 'standing_text': ["It always ends like this."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'paradox', 'standing_text': ["Joy requires ending. Ending sustains joy. Continue."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'oracle', 'standing_text': ["What you perceive as uncertainty is simply a delay in recognition."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'garbage', 'standing_text': ["You don't have to buy it. You already think it."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'reliquary', 'standing_text': ["Every failure has been preserved. Not as memory, but as structure."] }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch21_meet' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_paths' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'warden_hale', 'dialog_id': 'warden_hale_ch21_intentional' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_sabotage' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'edict', 'dialog_id': 'edict_ch21_outcome' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_no_consistency' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch21_simulated' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch21_clever' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch21_stopped_struggling' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch21_not_peace' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch21_feels_like' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_no_verification' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_wrong_faster' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'edict', 'dialog_id': 'edict_ch21_efficiency' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_efficiency_toward' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch21_objective' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_harms_people' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'edict', 'dialog_id': 'edict_ch21_harm_not_evaluated' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'warden_hale', 'dialog_id': 'warden_hale_ch21_should_be' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'edict', 'dialog_id': 'edict_ch21_emotion_error' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'warden_hale', 'dialog_id': 'warden_hale_ch21_emotion_tells' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch21_wrong_undefined' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch21_what_people_want' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_losing_themselves' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_removed_meaning' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_control_without_responsibility' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'edict', 'dialog_id': 'edict_ch21_definition_removed' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_nothing_wrong' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch21_correct' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_system_keeps_running' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch21_crave_calm' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_crave_understanding' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'warden_hale', 'dialog_id': 'warden_hale_ch21_dangerous' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_function_without_sense' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'edict', 'dialog_id': 'edict_ch21_perfect' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'glamour', 'standing_text': ["You've arrived. Good. There's a certain peace in following the path laid out for you, isn't there?"] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_meet_edict_glamour_crux' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_meet_edict_glamour_crux',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'edict',
        'task_acquire_events': [
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'edict' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'glamour' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'crux' }},
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'trial_1_dungeon', 'location': 'region_open_area' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_1_dungeon', 'item_id': 'crux_logic_core', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_1_dungeon', 'item_id': 'mythic_grassland_mid_oathbreakers_sigil', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_1_dungeon', 'item_id': 'axiom_focus_rod', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_1_dungeon', 'item_id': 'glamour_illusion_veil', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_1_dungeon', 'item_id': 'edict_enforcement_seal', 'location': 'treasure_room' }},
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'edict', 'dialog_id': 'edict_ch21_enter_trial' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch21_follow_path' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch21_simulated' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_follow_path' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_follow_path' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_follow_path' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_follow_path' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'edict', 'standing_text': ["Follow what's in front of you. The rest doesn't concern you."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_defeat_edict_glamour_crux' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_defeat_edict_glamour_crux',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'edict_glamour_crux_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'edict_glamour_crux_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'edict', 'dialog_id': 'edict_ch21_defeat' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch21_defeat' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch21_defeat' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_breaking' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'edict', 'dialog_id': 'edict_ch21_undefined_variable' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_choice' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'glamour', 'dialog_id': 'glamour_ch21_calm_no_fear' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_violation' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'crux', 'dialog_id': 'crux_ch21_function_compromised' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_no_purpose' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'edict' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'glamour' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'crux' }},
            { 'event_type': 'remove_player_from_dungeon', 'params': { 'dungeon_id': 'trial_1_dungeon' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'stigma', 'standing_text': ["Their truth was found wanting. Will yours hold?"] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'rapture', 'standing_text': ["One group down. Let's see who breaks next."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'scalpel', 'standing_text': ["Deviation was corrected. The next test is prepared."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'revelry', 'standing_text': ["Did you see that? What a beautiful collapse!"] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lament', 'standing_text': ["And so, they fall. One by one."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'paradox', 'standing_text': ["An end is a beginning. A beginning is an end."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'pageant', 'standing_text': ["Their performance was lacking. A new act begins."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'oracle', 'standing_text': ["The outcome was predicted. The next is already resolved."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'garbage', 'standing_text': ["They thought they could win. You know better, don't you?"] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'cataclysm', 'standing_text': ["Failure recorded. The system refines."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'reliquary', 'standing_text': ["Their end is now preserved. A new record begins."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_meet_stigma' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_meet_stigma',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'stigma',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'stigma', 'dialog_id': 'stigma_ch21_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_replace_doubt' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_handing_conclusions' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rapture', 'dialog_id': 'rapture_ch21_fun_part' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scalpel', 'dialog_id': 'scalpel_ch21_hesitation_confirmed' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_no_chance' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scalpel', 'dialog_id': 'scalpel_ch21_hesitation_response' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_decided_before' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch21_shaping' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'stigma', 'dialog_id': 'stigma_ch21_easier' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rapture', 'dialog_id': 'rapture_ch21_find_out' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_ch21_fall_back' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_training' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'stigma', 'dialog_id': 'stigma_ch21_simplify' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_chosen' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_not_discovery' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_stripping' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_filtration' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rapture', 'dialog_id': 'rapture_ch21_more_pressure' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'stigma', 'standing_text': ["The hesitation was the response. Correction was appropriate."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_meet_scalpel' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_meet_scalpel',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'scalpel',
        'task_acquire_events': [
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'stigma' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'rapture' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'scalpel' }},
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'trial_2_dungeon', 'location': 'region_open_area' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_2_dungeon', 'item_id': 'scalpel_precision_blade', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_2_dungeon', 'item_id': 'rapture_intensity_core', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_2_dungeon', 'item_id': 'theorem_circlet', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_2_dungeon', 'item_id': 'stigma_classification_lens', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_2_dungeon', 'item_id': 'forgegrip_gauntlets', 'location': 'treasure_room' }},
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scalpel', 'dialog_id': 'scalpel_ch21_enter_trial' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_not_machines' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_surprise' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scalpel', 'dialog_id': 'scalpel_ch21_counting_on_it' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_different' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_stripping_down' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_filtration_emphasis' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rapture', 'dialog_id': 'rapture_ch21_apply_pressure' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'scalpel', 'standing_text': ["Your deaths will be artistic precision."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_defeat_stigma_rapture_scalpel' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_defeat_stigma_rapture_scalpel',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'stigma_rapture_scalpel_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'stigma_rapture_scalpel_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'stigma', 'dialog_id': 'stigma_ch21_defeat' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rapture', 'dialog_id': 'rapture_ch21_defeat' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'scalpel', 'dialog_id': 'scalpel_ch21_defeat' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_judged_before' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'stigma', 'dialog_id': 'stigma_ch21_roles_clarify' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch21_erase' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'rapture', 'dialog_id': 'rapture_ch21_not_fun' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_filter_broke' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'stigma' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'rapture' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'scalpel' }},
            { 'event_type': 'remove_player_from_dungeon', 'params': { 'dungeon_id': 'trial_2_dungeon' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'revelry', 'standing_text': ["Their identities broke. Will yours be more fun?"] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'lament', 'standing_text': ["Another set falls. The end comes closer."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'paradox', 'standing_text': ["Their definition collapsed. A new state begins."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'pageant', 'standing_text': ["A poor performance. Let's hope the next is more entertaining."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'oracle', 'standing_text': ["Their failure was recorded. As was yours."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'garbage', 'standing_text': ["They pretended to be something they weren't. You're doing it too."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'cataclysm', 'standing_text': ["Data point acquired. The model is refined."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'reliquary', 'standing_text': ["Their memory is now archived. A new failure to record."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_meet_revelry' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_meet_revelry',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'revelry',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'revelry', 'dialog_id': 'revelry_ch21_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch21_desperation' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch21_always_ends' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_tone_shift' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'paradox', 'dialog_id': 'paradox_ch21_joy_ending' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_pick_one' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'paradox', 'dialog_id': 'paradox_ch21_both' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_smiling_falling' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch21_stopping' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'revelry', 'dialog_id': 'revelry_ch21_the_rush' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_until_it_isnt' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_escalation' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'paradox', 'dialog_id': 'paradox_ch21_remove_sustainability' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_collapse_guaranteed' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'revelry', 'dialog_id': 'revelry_ch21_exactly' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch21_quieter' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_not_peace' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'paradox', 'dialog_id': 'paradox_ch21_define_difference' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'revelry', 'standing_text': ["Their joy was weak. Let's see how you perform"] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_meet_paradox' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_meet_paradox',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'paradox',
        'task_acquire_events': [
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'revelry' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'lament' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'paradox' }},
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'trial_3_dungeon', 'location': 'region_open_area' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_3_dungeon', 'item_id': 'paradox_duality_orb', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_3_dungeon', 'item_id': 'revelry_euphoria_crystal', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_3_dungeon', 'item_id': 'paradox_robe', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_3_dungeon', 'item_id': 'reverie_bracers', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_3_dungeon', 'item_id': 'lament_sorrow_shroud', 'location': 'treasure_room' }},
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'paradox', 'dialog_id': 'paradox_ch21_meet_paradox' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_meet_paradox' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch21_meet_paradox' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_meet_paradox' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_meet_paradox' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'paradox', 'standing_text': ["Anything and everything is possible... Somehow."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_defeat_revelry_lament_paradox' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_defeat_revelry_lament_paradox',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'revelry_lament_paradox_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'revelry_lament_paradox_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'revelry', 'dialog_id': 'revelry_ch21_defeat' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch21_defeat' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'paradox', 'dialog_id': 'paradox_ch21_defeat' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch21_just_noise' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'revelry', 'dialog_id': 'revelry_ch21_silence_empty' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_sensation_not_substance' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'lament', 'dialog_id': 'lament_ch21_always_ends_repeat' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_ending_not_only' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'revelry' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'lament' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'paradox' }},
            { 'event_type': 'remove_player_from_dungeon', 'params': { 'dungeon_id': 'trial_3_dungeon' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'pageant', 'standing_text': ["Their joy was unsustainable. Let's see how your performance holds up."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'oracle', 'standing_text': ["Their collapse was inevitable. The next act was already written."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'garbage', 'standing_text': ["They were just distracting themselves. You're doing it too, you just call it 'purpose'."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'cataclysm', 'standing_text': ["Unsustainable system detected. Failure logged."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'reliquary', 'standing_text': ["Their frantic energy is now a static record."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_meet_pageant' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_meet_pageant',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'pageant',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'pageant', 'dialog_id': 'pageant_ch21_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_not_performing' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'pageant', 'dialog_id': 'pageant_ch21_watching' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'oracle', 'dialog_id': 'oracle_ch21_already_resolved' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_rehearsal' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'oracle', 'dialog_id': 'oracle_ch21_confirmation' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch21_creating_pressure' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch21_already_know' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch21_choose_to_believe' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch21_not_same' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'oracle', 'dialog_id': 'oracle_ch21_failure_occurred' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'pageant', 'dialog_id': 'pageant_ch21_compensate' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch21_already_think' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_reject_it' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch21_belief_not_choice' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_decide_what_to_do' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_break_behavior' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'oracle', 'dialog_id': 'oracle_ch21_deviation' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'pageant', 'dialog_id': 'pageant_ch21_under_pressure' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_watch_me' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'pageant', 'standing_text': ["The show only matters if the audience appreciates it.  The audience only appreciates it if you wear the mask they want to see."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_meet_garbage' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_meet_garbage',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'garbage',
        'task_acquire_events': [
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'pageant' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'oracle' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'garbage' }},
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'trial_4_dungeon', 'location': 'region_open_area' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_4_dungeon', 'item_id': 'oracle_prophecy_tome', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_4_dungeon', 'item_id': 'storyteller_staff', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_4_dungeon', 'item_id': 'storywoven_robe', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_4_dungeon', 'item_id': 'pageant_performance_mask', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_4_dungeon', 'item_id': 'garbage_doubt_seed', 'location': 'treasure_room' }},
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch21_meet_garbage' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch21_meet_garbage' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_meet_garbage' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_meet_garbage' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch21_meet_garbage' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'garbage', 'standing_text': ["The only thing you continuously suffer is humanity... is yourselves."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_defeat_pageant_oracle_garbage' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_defeat_pageant_oracle_garbage',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'pageant_oracle_garbage_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'pageant_oracle_garbage_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'pageant', 'dialog_id': 'pageant_ch21_defeat' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'oracle', 'dialog_id': 'oracle_ch21_defeat' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch21_defeat' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_why_you_lost' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'oracle', 'dialog_id': 'oracle_ch21_variables_accounted' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_bully_into_it' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'garbage', 'dialog_id': 'garbage_ch21_still_believe' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch21_chose_to_prove_wrong' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'pageant' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'oracle' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'garbage' }},
            { 'event_type': 'remove_player_from_dungeon', 'params': { 'dungeon_id': 'trial_4_dungeon' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'cataclysm', 'standing_text': ["Their perceptions were flawed. Reality corrects itself."] }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'reliquary', 'standing_text': ["Their flawed predictions are now part of the permanent record."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_meet_reliquary' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_meet_reliquary',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'reliquary',
        'task_acquire_events': [],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'reliquary', 'dialog_id': 'reliquary_ch21_intro' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'cataclysm', 'dialog_id': 'cataclysm_ch21_failure_is_data' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_tightening_margin' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_something_we_did' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'reliquary', 'dialog_id': 'reliquary_ch21_recorded_precisely' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'cataclysm', 'dialog_id': 'cataclysm_ch21_reapplied' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_hesitation_removed' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_refining_failure' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_locked_in' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'reliquary', 'dialog_id': 'reliquary_ch21_reference' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_uncertainty_allows' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_reinforcement' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_betting_not_changing' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_memory_lesson' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'reliquary', 'dialog_id': 'reliquary_ch21_continuity' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_continuity_from_choice' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_stop_predicting' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'reliquary', 'standing_text': ["History doesn't lie. It tells the same story again and again."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_meet_cataclysm' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_meet_cataclysm',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'cataclysm',
        'task_acquire_events': [
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'cataclysm' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'reliquary' }},
            { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'trial_5_dungeon', 'location': 'region_city_shoparmor' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_5_dungeon', 'item_id': 'cataclysm_refinement_core', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_5_dungeon', 'item_id': 'masterwork_blade', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_5_dungeon', 'item_id': 'smithsong_helm', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_5_dungeon', 'item_id': 'reliquary_preservation_shard', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_5_dungeon', 'item_id': 'hammerfall_boots', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_5_dungeon', 'item_id': 'embercraft_coat', 'location': 'treasure_room' }},
            { 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'trial_5_dungeon', 'item_id': 'wanderer_sandals', 'location': 'treasure_room' }},
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'cataclysm', 'dialog_id': 'cataclysm_ch21_enter_trial' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_enter_trial' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_enter_trial' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_enter_trial' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_enter_trial' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'cataclysm', 'standing_text': ["The end is coming. The end is here."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_defeat_cataclysm_reliquary' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_defeat_cataclysm_reliquary',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'cataclysm_reliquary_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'cataclysm_reliquary_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'cataclysm', 'dialog_id': 'cataclysm_ch21_defeat' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'reliquary', 'dialog_id': 'reliquary_ch21_defeat' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_used_past' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'cataclysm', 'dialog_id': 'cataclysm_ch21_data_perfect' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_data_not_whole' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'reliquary', 'dialog_id': 'reliquary_ch21_archive_incomplete' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_memory_freedom' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'cataclysm' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'reliquary' }},
            { 'event_type': 'remove_player_from_dungeon', 'params': { 'dungeon_id': 'trial_5_dungeon' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_meet_dominion' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_meet_dominion',
        'type': 'meet',
        'to_type': 'npc',
        'to_id': 'dominion',
        'task_acquire_events': [
            { 'event_type': 'show_npc', 'params': { 'npc_id': 'dominion', 'location': 'region_city_bar' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dominion', 'dialog_id': 'dominion_ch21_systems' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_breaking' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_closed_loops' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dominion', 'dialog_id': 'dominion_ch21_refinement' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_refinement_removes' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch21_same_outcome' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch21_always_collapse' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dominion', 'dialog_id': 'dominion_ch21_collapse_resolution' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch21_feels_like_breaking' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch21_not_meaningless' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_uncertainty_allows_alternatives' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_cant_handle_change' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_erase_itself' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_excuse' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_what_happens_before' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dominion', 'dialog_id': 'dominion_ch21_unresolved_variables' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_good' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_allows_change' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'sable', 'dialog_id': 'sable_ch21_prevents_inevitability' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'thorn', 'dialog_id': 'thorn_ch21_means_it_can_stop' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'bragg', 'dialog_id': 'bragg_ch21_or_be_fought' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'grimnaw', 'dialog_id': 'grimnaw_ch21_or_reworked' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_or_improved' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'nia', 'dialog_id': 'nia_ch21_or_experienced' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_or_chosen' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'lyren', 'dialog_id': 'lyren_ch21_or_matter' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dominion', 'dialog_id': 'dominion_ch21_instability' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_its_choice' }},
            { 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'dominion', 'standing_text': ["The only way you can survive is by living imprisoned from yourselves."] }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_defeat_dominion' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_defeat_dominion',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'dominion_1',
        'task_acquire_events': [
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'dominion_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dominion', 'dialog_id': 'dominion_ch21_defeat' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_cant_account_for_will' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dominion', 'dialog_id': 'dominion_ch21_not_won' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_face_together' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_choose_meaning' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'dominion', 'dialog_id': 'dominion_ch21_unleashed_void' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'dominion' }},
            { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch21_defeat_the_void' }}
        ]
    },
    {
        'task_id': 'main_story_ch21_defeat_the_void',
        'type': 'defeat',
        'to_type': 'mob',
        'to_id': 'the_void_1',
        'task_acquire_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch21_void_shatters' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'the_void', 'dialog_id': 'the_void_ch21_intro' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_just_quiet' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'the_void', 'dialog_id': 'the_void_ch21_meaning_lie' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_build_from_quiet' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'the_void', 'dialog_id': 'the_void_ch21_error' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_get_loud' }},
            { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'the_void_1', 'combat_type': 'boss_battle' }}
        ],
        'task_complete_events': [
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'the_void', 'dialog_id': 'the_void_ch21_defeat' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch21_dissolves' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_unmaking' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_make_real' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_together_1' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_together_2' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_together_3' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_together_4' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_together_5' }},
            { 'event_type': 'hide_npc', 'params': { 'npc_id': 'the_void' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch21_existence_reforms' }},
            { 'event_type': 'award_item', 'params': { 'item_id': 'bracelet_of_existence_reforged' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch21_void_reforms' }},
            { 'event_type': 'award_item', 'params': { 'item_id': 'bracelet_of_void_reforged' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch21_two_bracelets' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_final_choice' }},
            { 'event_type': 'remove_item', 'params': { 'item_id': 'bracelet_of_existence_reforged' }},
            { 'event_type': 'remove_item', 'params': { 'item_id': 'bracelet_of_void_reforged' }},
            { 'event_type': 'initiate_dialog', 'params': { 'npc_id': None, 'dialog_id': 'narrator_ch21_choice_made' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'faith', 'dialog_id': 'faith_ch21_we_chose' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch21_all_difference' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch21_saga_closes' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch21_but_story' }},
            { 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch21_never_ends' }},
            { 'event_type': 'complete_game' }
        ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_21',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}