# Implementation Spec: Chapters 1–2 Dialogue Rewrite

*Part 1 (§1–12) covers Chapter 1. Part 2 (§13–25) covers Chapter 2.*

**Status:** Ready for implementation
**Files:**
- `old/game/region_seeds/main_story/main_story_chapter_1.py` (NPC_DIALOG, TASKS)
- `old/game/region_seeds/main_characters.py` (the `begin_game_add_pc` join lines only)

**Scope:** dialogue text, companion reactions, the order of the opening events, and three stale standing texts. Quest flow, rewards, NPC placement and items are **unchanged**.

---

## 1. Writing rules for this chapter

The party in Chapter 1 is the hero plus **two random** members of the core five. So the dialogue follows these rules:

1. **Every story moment has a reaction for all five companions.** Whoever is present always says something. Absent characters' lines are skipped by the engine, so this costs nothing.
2. **Each line stands alone.** Companions never name or answer each other, and NPC lines never depend on a companion line having played.
3. **Each companion line carries the next-step hint in that character's own voice.** Whichever two are present, the player learns where to go next.
4. **The missing friends are the party's motive.** The opening says three friends are gone. The join lines, Kaera at the bar, Tess's deal and Diego all keep that alive. Tess's deal ("we'll keep our ears open for anyone else who fell out of the sky") is paid off by her existing Chapter 2 return line (the Highsteeple Crossing lead).
5. **No theft.** The old "Seth stole our stuff" thread is gone. Chock's dislike of Seth stays, for no reason except his face. It becomes a running joke across the chapter.

**Voices:**

| Character | Voice |
|---|---|
| Chock (technique, ESTJ) | Blunt, crude, wants to hit things, surly at Seth for no reason |
| Kaera (spirit, ISFJ) | Gentle, protective, senses things, worries about the missing friends |
| Moxie (magic, ENTP) | Chaotic, delighted, jokes, wants to buy or touch every dangerous thing |
| Kade (tech, INTJ) | Analytical, reads systems and economies, dry humour |
| Poise (skill, ISTP) | Clipped, observant, few words, action first |

**ID convention:** the new companion lines use `<class>_ch1_<beat>`, for example `technique_ch1_rook_deal`. Each beat is five `initiate_character_dialog` events in the fixed order technique, spirit, magic, tech, skill.

---

## 2. Opening sequence (`main_story_ch_1_find_the_inn`, task_acquire_events)

### 2.1 New order

The title card moves to right after the opening narration, and the tutorial moves to the end:

1. `initiate_dialog` → `chapter_1_start` (narration, §2.2)
2. `initiate_dialog` → `ch1_narrator_we_do_not_begin` (title card, §2.3)
3. `player_character_join` × 2 (keep `exclude_custom_class: True` from the custom-character spec)
4. `initiate_dialog` → `chapter_1_intro2` (unchanged)
5. `create_npc` seth, then `initiate_dialog` → `seth_preface` (§2.5)
6. **Replace** the `technique_got_jacked` event with the five `seth_preface` reaction events (§2.6)
7. `set_npc_standing_text` seth (§2.5)
8. `initiate_dialog` → `chapter_1_our_stuff_is_missing` (tutorial, §2.7; renaming it to `ch1_tutorial` is optional)
9. The `create_npc` and standing-text events for oren, rook, diego and brawn, unchanged

### 2.2 Narration: `chapter_1_start`

```python
{
	'npc_id': None,
	'dialog_id': 'chapter_1_start',
	'dialog': [
		"You don't know how you got here.",
		"One moment you and your friends were in a bar, knocking back a few µ.",
		"The next, blinding light tore through the room.",
		"Reality folded. When it opened again, three of your friends were gone.",
		"This place looks like chaos. The streets are littered, buildings stand looted, and fights break out on every corner.",
	]
},
```

### 2.3 Title card: `ch1_narrator_we_do_not_begin`

The line isn't a direct Heidegger quote. It's a paraphrase of his idea of "thrownness", so attribute it as one:

```python
{
	'npc_id': None,
	'dialog_id': 'ch1_narrator_we_do_not_begin',
	'dialog': [
		"Chapter 1",
		"We do not begin by knowing where we are. We begin by finding ourselves already there. - after Heidegger",
	]
},
```

### 2.4 Join lines: `begin_game_add_pc` (`main_characters.py`)

Replace the five `begin_game_add_pc` entries. Leave `ch2_add_pc` and the later joins alone. Each line mentions the bar, the missing friends, and finding shelter (the inn hint):

```python
{
	'npc_id': 'technique',
	'dialog_id': 'begin_game_add_pc',
	'dialog': [
		"My head's killing me. Last thing I remember is ordering another round.",
		"Where's everybody else? ...Fine. We find them. Then we find whoever did this and break something.",
		"First, a roof. An inn. Somewhere I can sit down and think.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'begin_game_add_pc',
	'dialog': [
		"Are you hurt? Let me look at you... you're alright. Thank the light.",
		"But the others... I can't feel them anywhere near. We have to find them.",
		"Let's find shelter first. An inn, somewhere safe to gather ourselves.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'begin_game_add_pc',
	'dialog': [
		"Okay. Okay! Who spiked the drinks? Because I want the recipe.",
		"Wait. Where are the other three? Nobody leaves the party early. We're finding them.",
		"Step one: an inn. Step two: a drink. Step three: answers. Probably in that order.",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'begin_game_add_pc',
	'dialog': [
		"Flash, pressure drop, then here. That wasn't a hallucination. That was a transfer.",
		"Six of us were in that bar. If three of us landed here, the other three landed somewhere. Not nowhere.",
		"We need a base of operations. An inn is the logical start.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'begin_game_add_pc',
	'dialog': [
		"Not our bar. Not our city.",
		"Three missing. No blood, no bodies. They're alive.",
		"Shelter first. The inn. Then we hunt.",
	]
},
```

### 2.5 Seth: `seth_preface` and standing text

Punctuation fixes, plus a clearer standing text. "You look good for a few." read as unclear.

```python
{
	'npc_id': 'seth',
	'dialog_id': 'seth_preface',
	'dialog': [
		"Whoa! That was crazy! You just appeared out of nowhere...",
		"Hey, look, these streets aren't safe. Be careful who you trust.",
		"And if Tess and Sam ask, you didn't see me. I am not paying that tab today.",
		"Gotta run... It's tuff out here!",
	]
},
```

Seth's standing text:

```python
"Still here? Like I said, trust nobody. Especially not me."
```

### 2.6 Reactions to Seth: beat `seth_preface`

These replace `technique_got_jacked`. Add the five events at step 6:

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch1_seth_preface' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch1_seth_preface' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch1_seth_preface' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch1_seth_preface' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch1_seth_preface' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch1_seth_preface',
	'dialog': [
		"I don't like that guy.",
		"Don't know why. It's his face. I want to hit his face.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch1_seth_preface',
	'dialog': [
		"He warned us, then ran like something was chasing him.",
		"I hope whoever he owes is kinder than this city looks.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch1_seth_preface',
	'dialog': [
		"A total stranger tells us to trust no one, then sprints off? I love him.",
		"I don't trust him. But I love him.",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch1_seth_preface',
	'dialog': [
		"Tess and Sam. He owes them money, which means they have leverage here.",
		"Names worth remembering.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch1_seth_preface',
	'dialog': [
		"He looked at our hands before our faces.",
		"Thief.",
	]
},
```

### 2.7 Tutorial: `chapter_1_our_stuff_is_missing`

Updated for automated leveling. Characters no longer spend points by hand.

```python
{
	'npc_id': None,
	'dialog_id': 'chapter_1_our_stuff_is_missing',
	'dialog': [
		"Find a residence or business (î Î ï Ï), then press (i) to manage your party.",
		"Check in often. When a character has a free ability slot, teach them something new.",
		"Most buildings are safe. The bars and the subways are not.",
		"If you get low, head to the @inn.",
	]
},
```

---

## 3. Oren (`main_story_ch_1_find_the_inn`, task_complete_events)

Replace `tech_says_somehow_i_think_were_there` with the five `oren` events. Kade's joke is kept in his line, and every line points to the item shop, where Rook is.

```python
{
	'npc_id': 'oren',
	'dialog_id': 'oren_intro',
	'dialog': [
		"Oh! Hey there. You look like you're not from here either. Like me. I'm Oren, just wandering and exploring.",
		"Not sure if it's reality wandering me, or if I'm wandering reality.",
		"I always seem to find my way to the @inn. Every city has an @inn.",
		"If you ever want to find the other side of another one, head to the ₨. It'll get you there.",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch1_oren' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch1_oren' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch1_oren' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch1_oren' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch1_oren' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch1_oren',
	'dialog': [
		"Guy's not all there.",
		"Forget the riddles. We've got nothing on us. Item shop, now.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch1_oren',
	'dialog': [
		"He's lost, but he isn't afraid. I envy that a little.",
		"We should gather supplies before we go anywhere. The item shop, perhaps.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch1_oren',
	'dialog': [
		"I like him! He's a fortune cookie that forgot the fortune.",
		"Ooh, also: shopping. Item shop. Go go go.",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch1_oren',
	'dialog': [
		"Somehow I think we're there.",
		"Logistics first. We have no supplies. The item shop.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch1_oren',
	'dialog': [
		"He said the ₨.",
		"Supplies next. Item shop.",
	]
},
```

Oren's standing text: unchanged.

---

## 4. Rook's deal (`main_story_ch_1_find_item_shop`)

Rook is described as quiet, methodical and patient, so he's rewritten to be terse. The salesman tic ("tell ya what") is gone. His grudge against Seth now shows, which backs up Seth's "personal vendetta".

Replace the `skill_loves_caffeine_shots` and `technique_ready_to_bust_bounty` events with the five `rook_deal` events.

```python
{
	'npc_id': 'rook',
	'dialog_id': 'rook_intro',
	'dialog': [
		"You're new. And broke. I can tell from here.",
		"Name's Rook. I collect bounties. There's one on a bandit called Seth. He's holed up in a hideout on the outskirts.",
		"He's slipped me four times. Bring him to me and you'll be paid.",
		"Here's something up front. Buy Caffeine Shots and Pocket Salves. You'll need both.",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch1_rook_deal' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch1_rook_deal' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch1_rook_deal' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch1_rook_deal' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch1_rook_deal' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch1_rook_deal',
	'dialog': [
		"Seth? The guy with the face?",
		"Oh, I'm in. Outskirts. Let's go.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch1_rook_deal',
	'dialog': [
		"Bounty or not, we bring him back alive. Agreed?",
		"Supplies first, then the outskirts.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch1_rook_deal',
	'dialog': [
		"Caffeine Shots? He had me at caffeine.",
		"Shop, caffeine, bandit. Best errand list ever.",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch1_rook_deal',
	'dialog': [
		"Paid work and a read on the local economy. Efficient.",
		"Stock up, then the hideout on the outskirts.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch1_rook_deal',
	'dialog': [
		"Fast target. Hideout. Outskirts.",
		"Stock up first.",
	]
},
```

Rook's standing text after the deal (replaces "Bring him to me and I'll give you half the bounty…"):

```python
"Seth's hideout is on the outskirts. He's slippery. Don't let him talk his way out."
```

Rook's standing text **before** the deal ("You look like fresh meat for the grinder.") is unchanged.

---

## 5. Seth's hideout (`main_story_ch_1_meet_seth` and `main_story_ch_1_defeat_seth`)

### 5.1 Before the fight

Replace `technique_you_got_it_coming` with the five `seth_fight` events.

```python
{
	'npc_id': 'seth',
	'dialog_id': 'seth_intro',
	'dialog': [
		"So Rook sent you to run me down?",
		"That guy's got it bad for me. This personal vendetta of his is really getting old.",
		"Well, you're here now. Let's see what you've got!",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch1_seth_fight' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch1_seth_fight' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch1_seth_fight' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch1_seth_fight' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch1_seth_fight' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch1_seth_fight',
	'dialog': [
		"You've got it coming, Seth.",
		"Mostly for the face.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch1_seth_fight',
	'dialog': [
		"We don't have to do this the hard way, Seth.",
		"...But we will if we must.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch1_seth_fight',
	'dialog': [
		"Ooh, a boss fight! Somebody hold my drink.",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch1_seth_fight',
	'dialog': [
		"He keeps the exits behind him. Pressure him and he'll make mistakes.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch1_seth_fight',
	'dialog': [
		"He's fast.",
		"I'm faster.",
	]
},
```

### 5.2 After the fight

Replace `skill_that_guy_was_fast` and `magic_haha_he_cant_wait_to_get_away` with the five `seth_escape` events. Every line points back to Rook.

```python
{
	'npc_id': 'seth',
	'dialog_id': 'seth_ch1_defeat',
	'dialog': [
		"Ha! Ha! You guys are good. I'm not sticking around for the finale, though. See ya!",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch1_seth_escape' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch1_seth_escape' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch1_seth_escape' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch1_seth_escape' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch1_seth_escape' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch1_seth_escape',
	'dialog': [
		"Get back here!",
		"...I wasn't done with his face. Fine. Let's go tell Rook.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch1_seth_escape',
	'dialog': [
		"He's hurt, but he'll live. I'm glad of that.",
		"Let's tell Rook what happened.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch1_seth_escape',
	'dialog': [
		"Hahaha! Look at him run!",
		"Rook is going to love this. Or hate it. Let's go find out.",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch1_seth_escape',
	'dialog': [
		"We didn't catch him, but we proved we could. That's worth something to Rook.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch1_seth_escape',
	'dialog': [
		"That guy was fast.",
		"Report to Rook.",
	]
},
```

Seth's standing text after the meet: change it to match the new defeat line, `"Ha! Ha! You guys are good. I'm not sticking around for the finale, though. See ya!"`.

---

## 6. Back to Rook (`main_story_ch_1_report_to_rook`)

Replace `tech_knocking_back_a_few` and `technique_good_idea_after_good_idea` with the five `rook_report` events. All of them point to the bar. Kaera's line brings back the missing friends.

```python
{
	'npc_id': 'rook',
	'dialog_id': 'rook_ch1_closing',
	'dialog': [
		"So you found him. And he got away.",
		"...He always does. Still, I hear you left a mark. That's more than most manage.",
		"Half the bounty. Fair is fair.",
		"You look like you need a drink. The bar's that way. Get yourself a µ.",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch1_rook_report' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch1_rook_report' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch1_rook_report' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch1_rook_report' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch1_rook_report' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch1_rook_report',
	'dialog': [
		"Free money and a bar. You know, I'm starting to like this place.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch1_rook_report',
	'dialog': [
		"A bar... that's where all of this started.",
		"Maybe someone there has heard something about the others.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch1_rook_report',
	'dialog': [
		"Last time we had drinks, we got teleported to another world.",
		"Let's see what happens this time! Bar!",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch1_rook_report',
	'dialog': [
		"Bars are where information leaks. We go for the gossip, not the drinks.",
		"...Mostly the gossip.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch1_rook_report',
	'dialog': [
		"Bar. Listen more than we drink.",
	]
},
```

Rook's standing text (fixes the stale "Bring him to me…"; harmless because he's hidden right after, but correct):

```python
"Seth will turn up again. He always does."
```

---

## 7. Tess and Sam (`main_story_ch_1_meet_tess_and_sam`)

### 7.1 New event order (task_complete_events)

1. `initiate_dialog` tess → `tess_intro_s1`
2. Five `tess_meet` events (replaces `magic_to_sam_1`)
3. `initiate_dialog` sam → `sam_intro_s1`
4. `initiate_dialog` tess → `tess_intro_s2`
5. Five `tess_deal` events (replaces `technique_to_sam_1` and `tech_interested_in_gear`)
6. The standing texts and `award_task` events, unchanged

### 7.2 Dialogue

"Sylvi" is removed: she's never introduced in Chapter 1. Tess now has teeth, Seth's tab gets its payoff, and Tess reads the party's missing friends off their faces. That sets up the deal Chapter 2 pays off.

```python
{
	'npc_id': 'tess',
	'dialog_id': 'tess_intro_s1',
	'dialog': [
		"Oooh! Here they are, Sam. The ones who fell out of the sky and roughed up Seth for Rook.",
		"...And then let him run off. Charming.",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch1_tess_meet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch1_tess_meet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch1_tess_meet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch1_tess_meet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch1_tess_meet' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch1_tess_meet',
	'dialog': [
		"He had it coming.",
		"Something about his face.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch1_tess_meet',
	'dialog': [
		"We didn't want to hurt him. He didn't leave us much choice.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch1_tess_meet',
	'dialog': [
		"Hahaha! My reputation precedes me. Already!",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch1_tess_meet',
	'dialog': [
		"Word travels fast here. Noted.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch1_tess_meet',
	'dialog': [
		"He ran. He'll be back.",
	]
},
```

```python
{
	'npc_id': 'sam',
	'dialog_id': 'sam_intro_s1',
	'dialog': [
		"Rook doesn't share his bounties. You must have impressed him.",
		"Seth knows us too. Small world, messy debts.",
	]
},
{
	'npc_id': 'tess',
	'dialog_id': 'tess_intro_s2',
	'dialog': [
		"Did that weasel say anything about our tab? ...Of course he didn't.",
		"So. You're new, you're nearly broke, and you're missing people. Don't look so surprised, it's all over your faces.",
		"Here's the deal. You help us out, and we'll keep our ears open for anyone else who fell out of the sky.",
		"Head over to the Æ and talk to Diego. Tell him Tess and Sam sent you.",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch1_tess_deal' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch1_tess_deal' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch1_tess_deal' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch1_tess_deal' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch1_tess_deal' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch1_tess_deal',
	'dialog': [
		"Deal. And if Seth shows up again, he's mine.",
		"Diego. The Æ. Let's move.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch1_tess_deal',
	'dialog': [
		"Thank you. Truly. Any word of them would mean everything.",
		"Let's find Diego at the Æ.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch1_tess_deal',
	'dialog': [
		"A secret errand from two mysterious sisters? Say less.",
		"To the Æ!",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch1_tess_deal',
	'dialog': [
		"Their network for our labor. A fair trade.",
		"Diego, at the Æ.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch1_tess_deal',
	'dialog': [
		"Diego. Æ. Go.",
	]
},
```

Standing texts for Tess and Sam: unchanged. The Mnemonic Logger side quest (`sam_gives_logger` plus its five reactions) is unchanged; it already follows the five-reaction pattern.

---

## 8. Diego (`main_story_ch_1_meet_diego`)

Replace `technique_diego_intro` and `magic_interested_in_mira` with the five `diego` events. Diego now nods to the missing friends, and the typos are fixed ("officionado", "trouble makers").

```python
{
	'npc_id': 'diego',
	'dialog_id': 'diego_intro',
	'dialog': [
		"Hmmmmm! Can't say I've seen your faces before, and I've seen a lot of ugly faces.",
		"Those troublemakers Tess and Sam sent you? Interesting.",
		"I'm Diego. Ex-merc, glorified information salesman.",
		"The girls asked me to track down a relic for them called the Grift Stone.",
		"I traced it to a black market dealer named Mira.",
		"She stays in a nearby city and likes to frequent the µ, unloading shady shit to shady people.",
		"She won't give it up easy, though. Talk to Brawn at the Armory, and maybe pick up some ¥ while you're there.",
		"He's a real armor aficionado. He'll most likely have something she'd be interested in.",
		"And yes, Tess told me you've misplaced some friends. I'll keep an ear out. No charge... this time.",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch1_diego' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch1_diego' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch1_diego' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch1_diego' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch1_diego' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch1_diego',
	'dialog': [
		"Armory? Finally. I could do with an upgrade.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch1_diego',
	'dialog': [
		"He'll listen for them. That's something.",
		"Mira sounds dangerous. Let's be prepared. Brawn at the Armory first.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch1_diego',
	'dialog': [
		"Oooh hoo hoooo!!! A black market dealer!",
		"I wonder what Mira has for sale! Armory first, I guess. Boo.",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch1_diego',
	'dialog': [
		"A trade chain. Brawn's goods for Mira's stone.",
		"Start at the Armory.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch1_diego',
	'dialog': [
		"Brawn. Armory.",
	]
},
```

Diego's, Tess's and Sam's standing texts: unchanged.

---

## 9. Brawn (`main_story_ch_1_meet_brawn`)

Replace `technique_brawn_intro` and `skill_brawn_intro` with the five `brawn` events. Brawn now shows his "encyclopedia of warfare" side. Kade's line hints that the bracers are in the hideout's final chamber, where `dungeon_add_treasure` places them.

```python
{
	'npc_id': 'brawn',
	'dialog_id': 'brawn_intro',
	'dialog': [
		"Ho there! So Diego sent you, eh?",
		"He reckons I've got something Mira would want. He's right. I do.",
		"But I need a favour first. Seth swiped a pair of my ornate bracers. I'd bet my pension on it.",
		"Bracers like those were worn by honor guards three wars back. They don't belong in a bandit's sack.",
		"Search his hideout and bring them home.",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch1_brawn' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch1_brawn' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch1_brawn' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch1_brawn' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch1_brawn' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch1_brawn',
	'dialog': [
		"Seth again? Good.",
		"I wasn't done with his face.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch1_brawn',
	'dialog': [
		"They clearly mean a great deal to him. We'll bring them back.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch1_brawn',
	'dialog': [
		"Breaking back into the bandit's hideout? Yes. I love a sequel.",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch1_brawn',
	'dialog': [
		"We know the hideout's layout now. If he's stashing loot, it's in the final chamber.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch1_brawn',
	'dialog': [
		"Stolen gear. Simple job. We move.",
	]
},
```

Brawn's standing text: unchanged.

---

## 10. Delivering the bracers (`main_story_ch_1_deliver_ornate_bracers`)

Keep `technique_brawn_ornate_bracers` as the first event ("You know these things don't look like they can take much of a hit."). Brawn's new line answers it, and it still stands on its own if Chock isn't present.

Replace `magic_likes_cursed_couplet` with the five `couplet` events. They go after both Brawn dialogs (`brawn_ch1_closing` and the conditional `brawn_ch1_closing_no_logger`). Every line points to Boiling Bubble.

```python
{
	'npc_id': 'brawn',
	'dialog_id': 'brawn_ch1_closing',
	'dialog': [
		"Aha! You found them! Aren't they beautiful?",
		"Don't let their looks fool you. These were never made for hitting. They were made to be remembered.",
		"Now, Mira. Take her this cursed couplet I came across. She'll want it.",
		"She's in Boiling Bubble at the moment, and she loves the bar there.",
		"Trade it to her for the Grift Stone.",
	]
},
{
	'npc_id': 'brawn',
	'dialog_id': 'brawn_ch1_closing_no_logger',
	'dialog': [
		"And speak to Sam before you go. She has something that'll help you out.",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch1_couplet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch1_couplet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch1_couplet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch1_couplet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch1_couplet' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch1_couplet',
	'dialog': [
		"Cursed? Great. You're carrying it.",
		"Boiling Bubble. Let's get rid of it.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch1_couplet',
	'dialog': [
		"There's something sorrowful bound up in it.",
		"Let's get it to Mira quickly. Boiling Bubble.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch1_couplet',
	'dialog': [
		"I might be interested in it too?!? That thing looks powerful.",
		"...Fine. Boiling Bubble. But I'm holding it on the way.",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch1_couplet',
	'dialog': [
		"A cursed object as currency. This economy is fascinating.",
		"Next stop, Boiling Bubble.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch1_couplet',
	'dialog': [
		"Boiling Bubble. Bar. Mira.",
	]
},
```

Standing texts after delivery: unchanged.

---

## 11. Remove the old dialogue entries

These dialog_ids are replaced. Delete the entries from NPC_DIALOG, along with any event that still points at them:

| Old dialog_id | Replaced by |
|---|---|
| `technique_got_jacked` | `*_ch1_seth_preface` |
| `tech_says_somehow_i_think_were_there` | `*_ch1_oren` |
| `skill_loves_caffeine_shots`, `technique_ready_to_bust_bounty` | `*_ch1_rook_deal` |
| `technique_you_got_it_coming` | `*_ch1_seth_fight` |
| `skill_that_guy_was_fast`, `magic_haha_he_cant_wait_to_get_away` | `*_ch1_seth_escape` |
| `tech_knocking_back_a_few`, `technique_good_idea_after_good_idea` | `*_ch1_rook_report` |
| `magic_to_sam_1` | `*_ch1_tess_meet` |
| `technique_to_sam_1`, `tech_interested_in_gear` | `*_ch1_tess_deal` |
| `technique_diego_intro`, `magic_interested_in_mira` | `*_ch1_diego` |
| `technique_brawn_intro`, `skill_brawn_intro` | `*_ch1_brawn` |
| `magic_likes_cursed_couplet` | `*_ch1_couplet` |

Keep: `technique_brawn_ornate_bracers` and the five `*_reacts_to_logger` entries.

---

## 12. Verification

1. Run the story timeline validator. There are no missing dialog_ids and no orphaned entries from §11.
2. Play Chapter 1 three times with different random pairs, making sure Chock is absent at least once. Every story moment shows two companion lines, and each one says where to go next.
3. The opening order is: narration → "Chapter 1" title card → two join lines → Seth → reactions → tutorial.
4. The tutorial no longer tells players to spend stat or power points by hand.
5. No line mentions Seth stealing from the party.
6. Search the file for "Sylvi", "preceeding" and "officionado": no matches.

---

# Part 2: Chapter 2

**Files:**
- `old/game/region_seeds/main_story/main_story_chapter_2.py` (NPCS, NPC_DIALOG, TASKS)
- `old/game/region_seeds/main_characters.py` (the `ch2_add_pc` join lines only)

**Scope:** the same as Part 1. Dialogue, companion reactions and standing texts change. Quest flow, rewards, items, dungeons and the Demigorgon fight are **unchanged**. The writing rules in §1 apply, and new companion IDs use `<class>_ch2_<beat>`.

## 13. What Chapter 2 fixes

| Problem | Fix |
|---|---|
| Mira's standing text after the couplet is a placeholder: "words to the effect of k come back when the couplet is uncoupled" | Real line (§15) |
| Mira never tells you to see Leera, and the companions react to "a riddle" Mira never gave | Mira names Leera at the @inn; the reactions point there (§15) |
| Companions at Leera already say "Resonance Shard… find Juno" before Mira mentions it; the same three entries play again at Mira | Two separate beats: Leera → back to Mira, Mira → Juno (§16, §17) |
| Juno says "the resonance shard Leera spoke of"; it was Mira | Fixed (§21) |
| Moxie says "I already like her" about Kess; Kess is male in his description | "him" (§19) |
| The Chapter 2 recruit joins mid-fight sounding like a stranger, and nobody reacts to finding a lost friend | Kess's missing courier **is** your friend. The join lines recognise the party, and the post-fight lines carry the reunion (§19, §20) |
| After the fight, ten generic `*_ch2_random_appearance` lines play on top of the five `*_ch2_post_demigorgon` lines | Merged into one beat (§20) |
| Partial reaction sets: Demigorgon meet (1 of 5), Juno (2), Kess after the ruin (3) | Full sets of five |
| Diego's standing text says "stay out of the black market dealings" right after he sent you to a black market dealer | Rewritten with irony (§14) |
| Poise's "threads of fate weaving a complex tapestry" | Poise's own voice (§23) |
| NPC name "The Demigorgons" (plural) for one creature | "The Demigorgon" |
| Typos: "Apparant", "you came" lower case after a full stop | Fixed |
| `moxie_ch2_after_leera` is never used | Delete |

---

## 14. Chapter start (`main_story_ch_2_deliver_cursed_couplet_to_mira`, task_acquire_events)

Standing texts. Tess, Sam and Brawn are unchanged. Diego's becomes:

```python
"Mira's a shark. Smile, trade, and count your fingers after.",
```

Title card: Hegel's wording is "contradiction is the root of all movement and vitality" (*Science of Logic*). Use the accurate version:

```python
{
	'npc_id': None,
	'dialog_id': 'ch2_narrator_contradiction',
	'dialog': [
		"Chapter 2",
		"Contradiction is the root of all movement and vitality. - Hegel",
	]
},
```

NPC fix in `NPCS`: `the_demigorgon` name `'The Demigorgons'` → `'The Demigorgon'`.

---

## 15. Mira and the couplet (`main_story_ch_2_deliver_cursed_couplet_to_mira`, task_complete_events)

Mira is cold, calculating and seductive, so the rewrite drops the repeated "Grift Stone for Tess" and sends you to Leera. Replace the five `*_ch2_deliver_couplet` reactions with the five `mira_couplet` events.

```python
{
	'npc_id': 'mira',
	'dialog_id': 'mira_ch2_intro',
	'dialog': [
		"Well now... you actually brought it.",
		"This couplet is older than half the ruins in this region. Two things, bound into one, and cursed to stay that way.",
		"You want the Grift Stone. Sweetheart, nothing rare comes cheap, and nothing powerful comes without a favor attached.",
		"Get this curse read. Leera, the lorekeeper at the @inn, knows the old bindings.",
		"Bring me what she tells you, and we'll talk.",
		"...And you've lost someone. Everyone who comes to me has. Do my favor, and maybe I'll hear something.",
	]
},
```

Mira's standing text (replaces the placeholder):
```python
"Leera at the @inn can read the couplet's curse. Come back when you know what it needs.",
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch2_mira_couplet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch2_mira_couplet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch2_mira_couplet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch2_mira_couplet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch2_mira_couplet' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch2_mira_couplet',
	'dialog': [
		"A curse? Great. I came here to fight, not to read.",
		"Fine. Lorekeeper. Inn. Let's go.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch2_mira_couplet',
	'dialog': [
		"Something bound against its will... I felt it when we carried it.",
		"Let's find Leera at the inn.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch2_mira_couplet',
	'dialog': [
		"A cursed antique and a mysterious lorekeeper? This is the best errand yet.",
		"Inn! Leera! Go!",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch2_mira_couplet',
	'dialog': [
		"Fantastic. We're running errands for smugglers now.",
		"Leera, at the inn. She has the information.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch2_mira_couplet',
	'dialog': [
		"Leera. Inn.",
	]
},
```

---

## 16. Leera's riddle (`main_story_ch_2_uncouple_couplet`)

Replace the three `*_ch2_after_leera` events here with the five `leera` events. These reactions point back to **Mira**, not Juno. Also remove the duplicate Leera `set_npc_standing_text` at the end of the task (it's set twice with the same text).

```python
{
	'npc_id': 'leera',
	'dialog_id': 'leera_ch2_couplet_lore',
	'dialog': [
		"Ah... you carry Mira's couplet. Then listen carefully.",
		"Void and Existence. Absence and Presence. Chaos and order.",
		"What exists before it is understood... yet changes once it is named?",
		"Apparent in absence, never there in presence. Some truths hum even when buried.",
		"Two things bound this long forget they were ever two. They must be reminded.",
		"Return to Mira with this truth.",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch2_leera' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch2_leera' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch2_leera' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch2_leera' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch2_leera' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch2_leera',
	'dialog': [
		"I understood about half of that.",
		"Mira can have the other half. Back to the bar.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch2_leera',
	'dialog': [
		"Void and Existence... two halves that forgot each other.",
		"Mira will know what it means. Let's return to her.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch2_leera',
	'dialog': [
		"Ohhh, metaphysics. My favorite flavor of nonsense.",
		"Back to Mira, before I start answering the riddle out loud.",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch2_leera',
	'dialog': [
		"A riddle about something that hums. That's a frequency.",
		"Report back to Mira.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch2_leera',
	'dialog': [
		"Riddle's for Mira. Back to the bar.",
	]
},
```

---

## 17. Back to Mira (`main_story_ch_2_return_to_mira_after_leera`)

Replace the five `*_ch2_after_leera` events here with the five `mira_riddle` events. These now point to Juno at the item shop.

```python
{
	'npc_id': 'mira',
	'dialog_id': 'mira_ch2_after_leera',
	'dialog': [
		"So Leera whispered her riddles at you.",
		"Void and Existence, bound so long they've forgotten they were ever two. Yes, that tracks.",
		"Something that hums can remind them. A Resonance Shard.",
		"Juno has one. She deals in risk and rare odds, and she just won it.",
		"Find her at the item shop. And don't let her talk you into a game.",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch2_mira_riddle' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch2_mira_riddle' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch2_mira_riddle' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch2_mira_riddle' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch2_mira_riddle' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch2_mira_riddle',
	'dialog': [
		"A gambler. Great. I hate cards.",
		"Item shop. Let's get this shard.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch2_mira_riddle',
	'dialog': [
		"A shard to remind them what they were. There's something gentle in that.",
		"Let's find Juno at the item shop.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch2_mira_riddle',
	'dialog': [
		"A gambler with a magic rock? I am absolutely playing her game.",
		"...Fine. Item shop.",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch2_mira_riddle',
	'dialog': [
		"Dependency chain: Juno's shard, Mira's curse, Tess's stone.",
		"Item shop.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch2_mira_riddle',
	'dialog': [
		"Juno. Item shop. Don't gamble.",
	]
},
```

Mira's and Leera's standing texts: unchanged.

---

## 18. Juno (`main_story_ch_2_meet_juno`)

Juno's dialogue is unchanged. Replace `tech_ch2_after_juno` and `magic_ch2_after_juno` with the five `juno` events, pointing to Kess at the weapon shop.

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch2_juno' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch2_juno' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch2_juno' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch2_juno' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch2_juno' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch2_juno',
	'dialog': [
		"We do a favor so we can do a favor so we can do a favor.",
		"Kess. Weapon shop. Whatever.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch2_juno',
	'dialog': [
		"Contraband... I don't love it. But we need that shard.",
		"Let's find Kess.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch2_juno',
	'dialog': [
		"A volatile, contraband concoction? Now we're talking.",
		"Weapon shop! Kess!",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch2_juno',
	'dialog': [
		"A shard for a concoction. Classic black market barter.",
		"Kess Thornwrite, at the weapon shop.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch2_juno',
	'dialog': [
		"Kess. Weapon shop.",
	]
},
```

---

## 19. Kess and the ruin (`main_story_ch_2_meet_kess_thornwrite`, `main_story_ch_2_meet_demigorgon`)

### 19.1 Kess's request

The key idea: **Kess's missing courier is the friend who joins you in the ruin.** Kess plants it without naming anyone.

```python
{
	'npc_id': 'kess_thornwrite',
	'dialog_id': 'kess_ch2_request',
	'dialog': [
		"Juno wants *that* concoction? Oh stars... she's bold.",
		"I can brew it, sure, but I'm missing a key ingredient.",
		"I sent a courier to fetch it from a ruin outside the city. New in town, said they needed the coin, didn't ask questions.",
		"They never came back.",
		"Bring me the ingredient, and bring them back too if you can. Try not to die on me. I don't want that on my head.",
	]
},
```

The five existing `*_ch2_after_kess` reactions stay; replace their text:

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch2_after_kess',
	'dialog': [
		"New in town, needs coin, doesn't ask questions? ...That sounds like one of us.",
		"Ruin outside the city. Let's go.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch2_after_kess',
	'dialog': [
		"Someone new to this world, alone in a ruin... we have to hurry.",
		"The ruin outside the city.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch2_after_kess',
	'dialog': [
		"A volatile brew, a spooky ruin and a missing courier? I already like him.",
		"To the ruin!",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch2_after_kess',
	'dialog': [
		"A stranger with no history taking odd jobs. We fit the same profile.",
		"The ruin outside the city. Move.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch2_after_kess',
	'dialog': [
		"Courier's new here. Like us.",
		"Ruin. Now.",
	]
},
```

### 19.2 The join (`ch2_add_pc` in `main_characters.py`)

The join happens at the Demigorgon meet, mid-encounter. The new member **recognises the party**. They are one of the three who vanished from the bar, and they were Kess's courier. Replace the five `ch2_add_pc` entries:

```python
{
	'npc_id': 'technique',
	'dialog_id': 'ch2_add_pc',
	'dialog': [
		"...You. YOU! Took you long enough!",
		"Some chemist paid me to fetch a weed out of this hole. Then THAT showed up.",
		"Hug later. Hit that thing now.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'ch2_add_pc',
	'dialog': [
		"It's you... it's really you. I prayed someone would find me.",
		"I took a job gathering herbs here so I could eat. I didn't know this thing was guarding them.",
		"Please... I can't hold it back alone.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'ch2_add_pc',
	'dialog': [
		"Oh, thank everything, familiar faces! I was about to start naming it.",
		"Courier job, they said. Easy money, they said.",
		"Okay, reunion later, monster now!",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'ch2_add_pc',
	'dialog': [
		"You're here. Good. My odds just improved considerably.",
		"I took a supply run to fund the search for you. The ingredient is behind that.",
		"Discuss later. Engage now.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'ch2_add_pc',
	'dialog': [
		"You found me.",
		"Courier job. Ingredient's behind it.",
		"Fight. Talk after.",
	]
},
```

### 19.3 Before the fight (`main_story_ch_2_meet_demigorgon`)

Replace `technique_ch2_meet_demigorgon` with the five `demigorgon_meet` events. The new member is in the party by now, so these lines must work whether the speaker just joined or has been here all along.

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch2_demigorgon_meet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch2_demigorgon_meet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch2_demigorgon_meet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch2_demigorgon_meet' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch2_demigorgon_meet' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch2_demigorgon_meet',
	'dialog': [
		"Oooooh. Looks like we bit off more than we can chew.",
		"Good. I'm hungry.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch2_demigorgon_meet',
	'dialog': [
		"Stay close to me. All of us. I won't lose anyone again.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch2_demigorgon_meet',
	'dialog': [
		"It's big, it's ugly, and it's between us and a reunion. Light it up!",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch2_demigorgon_meet',
	'dialog': [
		"Unknown entity. High threat. Focus fire.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch2_demigorgon_meet',
	'dialog': [
		"Together. Now.",
	]
},
```

---

## 20. After the Demigorgon (`main_story_ch_2_defeat_demigorgon`)

Replace **all ten** companion events (`*_ch2_post_demigorgon` and `*_ch2_random_appearance`) with the five `post_demigorgon` events. Each line does two things: it reacts to the creature, and it lands the reunion in a way that works for both the joiner and the old members ("we found one of us, so the others are out there too"). Every line points back to Kess.

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch2_post_demigorgon' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch2_post_demigorgon' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch2_post_demigorgon' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch2_post_demigorgon' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch2_post_demigorgon' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch2_post_demigorgon',
	'dialog': [
		"That thing hit like a freight train. And it bent the air. Not natural.",
		"But we're four now. One down, two to go. Let's get the weed back to Kess.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch2_post_demigorgon',
	'dialog': [
		"That creature radiated something dark. Such forces can corrupt even the purest hearts.",
		"But we found each other. If we survived this, the others can too. Let's return to Kess.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch2_post_demigorgon',
	'dialog': [
		"Strange hum, teeth like carved stone. Deliciously alien.",
		"And look at us! Half a reunion! The other two are out there somewhere. To Kess!",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch2_post_demigorgon',
	'dialog': [
		"Scorch marks, odd sigils. Someone has been experimenting with things they don't understand.",
		"Data point: we all landed in this world, alive. That makes the other two likely. Back to Kess.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch2_post_demigorgon',
	'dialog': [
		"It moved like shadow pretending to be solid.",
		"We found one. We'll find the rest. Kess first.",
	]
},
```

---

## 21. Kess, Juno and the shard (`main_story_ch_2_deliver_rare_ingredient`, `main_story_ch_2_return_to_juno_after_kess`)

### 21.1 Kess after the ruin

Kess notices his courier came back. Replace `technique_ch2_after_dungeon`, `skill_ch2_after_dungeon` and `tech_ch2_after_dungeon` with the five `after_ruin` events.

```python
{
	'npc_id': 'kess_thornwrite',
	'dialog_id': 'kess_ch2_after_dungeon',
	'dialog': [
		"You found it! And my courier, alive! Oh, stars, that's a weight off.",
		"Keep the advance, I'm not asking for it back.",
		"Give me a moment...",
		"...",
		"...",
		"There. One dangerously potent concoction for Juno.",
		"Try not to inhale it. Or do. I'm not your mother.",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch2_after_ruin' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch2_after_ruin' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch2_after_ruin' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch2_after_ruin' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch2_after_ruin' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch2_after_ruin',
	'dialog': [
		"That ruin had teeth. Good fight.",
		"Now let's get this stuff to Juno before it explodes.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch2_after_ruin',
	'dialog': [
		"Thank you, Kess, for worrying about them.",
		"Let's bring this to Juno.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch2_after_ruin',
	'dialog': [
		"He said 'try not to inhale it' like it's a suggestion.",
		"Juno! Quickly! Before I get curious.",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch2_after_ruin',
	'dialog': [
		"Volatile compound, unlabeled, carried by hand. Excellent safety culture.",
		"To Juno.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch2_after_ruin',
	'dialog': [
		"Concoction. Juno. Careful.",
	]
},
```

### 21.2 Juno hands over the shard

Fix the attribution: Leera never mentioned the shard; Mira did. The five existing `*_juno_ch2_after_kess` reactions are unchanged.

```python
{
	'npc_id': 'juno',
	'dialog_id': 'juno_ch2_after_kess',
	'dialog': [
		"Ahh... Kess actually delivered. Miracles do happen.",
		"Here. The Resonance Shard Mira's been after. Handle it carefully.",
		"Take it back to Mira. She'll know how to use it.",
	]
},
```

---

## 22. The uncoupling (`main_story_ch_2_return_to_mira_for_decoupling`)

The uncoupling happens in the dialogue now, not only in Mira's standing text. Mira keeping both bracelets plants the Bracelet of Void (Chapter 4) and the Bracelet of Existence (Chapter 9). It also points to the hyperway by its map symbol, Ṣ, the same way other hints name the @inn, µ, Æ and ₨.

```python
{
	'npc_id': 'mira',
	'dialog_id': 'mira_ch2_decoupling',
	'dialog': [
		"You brought the shard. Good.",
		"...",
		"(The shard hums. The couplet shudders, and splits in two.)",
		"Void... and Existence. Two bracelets, reminded of what they were.",
		"These stay with me. You came for the Grift Stone, and I keep my deals.",
		"Take the Ṣ hyperway back to Tess. It's a small fee. Cheaper than walking.",
	]
},
```

Of the five `*_ch2_decoupling` reactions, replace two and keep three:

```python
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch2_decoupling',
	'dialog': [
		"Two magic bracelets out of one curse, and she keeps both? Rude.",
		"...Hyperway! Back to Tess!",
	]
},
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch2_decoupling',
	'dialog': [
		"About time we got something solid out of this.",
		"Hyperway. Tess. Let's go.",
	]
},
```

Keep `spirit_ch2_decoupling`, `skill_ch2_decoupling` and `tech_ch2_decoupling` as they are; each already points to Tess. Standing texts for Mira, Leera and Juno are unchanged.

**Monster Hunter (Diego):** unchanged. It's one of the best scenes in the chapter, and its five reactions are already in character.

---

## 23. Tess and the next lead (`main_story_ch_2_return_to_tess_with_grift_stone`)

Tess pays off her Chapter 1 promise ("we'll keep our ears open for anyone else who fell out of the sky"). Replace the five `*_ch2_after_tess` reactions with the five `tess_lead` events. Every line points to Highsteeple Crossing.

```python
{
	'npc_id': 'tess',
	'dialog_id': 'tess_ch2_return',
	'dialog': [
		"You're back! And you actually got the Grift Stone?",
		"Damn... you guys are full of surprises.",
		"...And you found one of your strays! Told you this city talks.",
		"We promised to keep our ears open, and we did. Someone in Highsteeple Crossing showed up out of nowhere... like you did.",
		"Sam and I are hearing other whispers too: weird arrivals, old relic routes, too much money moving too fast.",
		"We'll keep pulling threads on our side. If you're looking for answers, Highsteeple is your next lead.",
	]
},
```

```python
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'technique', 'dialog_id': 'technique_ch2_tess_lead' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'spirit', 'dialog_id': 'spirit_ch2_tess_lead' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'magic', 'dialog_id': 'magic_ch2_tess_lead' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'tech', 'dialog_id': 'tech_ch2_tess_lead' } },
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'skill', 'dialog_id': 'skill_ch2_tess_lead' } },
```

```python
{
	'npc_id': 'technique',
	'dialog_id': 'technique_ch2_tess_lead',
	'dialog': [
		"Another one fell out of the sky? Two left. Could be one of ours.",
		"Highsteeple Crossing. Let's go. And Tess, if you ever need me, just holler.",
	]
},
{
	'npc_id': 'spirit',
	'dialog_id': 'spirit_ch2_tess_lead',
	'dialog': [
		"Someone alone and confused in Highsteeple... I know how that feels.",
		"We have to go to them.",
	]
},
{
	'npc_id': 'magic',
	'dialog_id': 'magic_ch2_tess_lead',
	'dialog': [
		"Someone materialized 'like you did'? Oooh, a mystery guest!",
		"Highsteeple Crossing! Ooowoooooo!",
	]
},
{
	'npc_id': 'tech',
	'dialog_id': 'tech_ch2_tess_lead',
	'dialog': [
		"Six of us were in that bar. Four are accounted for. The probability that this is one of ours is high.",
		"Highsteeple Crossing.",
	]
},
{
	'npc_id': 'skill',
	'dialog_id': 'skill_ch2_tess_lead',
	'dialog': [
		"Two still missing.",
		"Highsteeple. Now.",
	]
},
```

Sam's standing text is unchanged (it already gives the Highsteeple lead). Tess's is unchanged.

**Note on the count:** "four of us" in §20 and §23 is correct from the party's point of view: the hero, the two Chapter 1 friends and the Chapter 2 courier, out of six at the bar. If the party is ever bigger or smaller at that point, those lines need a recount.

---

## 24. Remove the old Chapter 2 dialogue entries

| Old dialog_id(s) | Replaced by |
|---|---|
| `*_ch2_deliver_couplet` (5) | `*_ch2_mira_couplet` |
| `*_ch2_after_leera` (5) | `*_ch2_leera` and `*_ch2_mira_riddle` |
| `moxie_ch2_after_leera` | nothing (unused) |
| `tech_ch2_after_juno`, `magic_ch2_after_juno` | `*_ch2_juno` |
| `technique_ch2_meet_demigorgon` | `*_ch2_demigorgon_meet` |
| `*_ch2_post_demigorgon` (5), `*_ch2_random_appearance` (5) | `*_ch2_post_demigorgon` (new text, same ids; delete the old entries first) |
| `technique_ch2_after_dungeon`, `skill_ch2_after_dungeon`, `tech_ch2_after_dungeon` | `*_ch2_after_ruin` |
| `*_ch2_after_tess` (5) | `*_ch2_tess_lead` |

Note: `*_ch2_post_demigorgon` keeps its id but gets new text. Replace the existing five entries rather than adding duplicates.

---

## 25. Chapter 2 verification

1. Run the story timeline validator: no missing dialog_ids, no orphans from §24, no duplicate dialog_id/npc_id pairs.
2. Play Chapter 2 with at least three different party mixes. Every story moment shows a line from each companion present, and each line says where to go next.
3. Mira's standing text after the couplet is the real line, not the placeholder.
4. The order of hints is right: Mira → Leera → Mira → Juno → Kess → ruin → Kess → Juno → Mira → Tess. No companion mentions Juno or the shard before Mira does.
5. The Chapter 2 recruit's join line recognises the party, and the post-fight lines treat them as a found friend.
6. Search the file for "words to the effect", "Apparant", "The Demigorgons" and "Leera spoke of": no matches.
