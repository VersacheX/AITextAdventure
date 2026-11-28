# Implementation Spec: Chapter 4, Final Character Required Before Catalyst

**Status:** Ready for implementation
**Scope:** one story file, `old/game/region_seeds/main_story/main_story_chapter_4.py`. No engine changes.

---

## 1. Problem

At the end of `main_story_ch4_meet_kirn` (Task 3), the rift opens and **both** of these tasks are awarded together:

- `main_story_ch4_meet_final_character` (Task 4)
- `main_story_ch4_meet_catalyst` (Task 5)

So the player can walk past the final character in the corridor, talk to Catalyst, fight him and finish the chapter with only four party members. The fifth character is optional when it should be required.

## 2. Design

- Catalyst's meet task is awarded only **after** the final character joins.
- Until then, talking to Catalyst shows standing text that turns the player away. The engine already does this: when there is no active task for an NPC in a dungeon, talking to them shows their standing text (`PlayerGame` dungeon NPC handling, the `if not task_completed:` branch).
- The rift is already locked until Catalyst falls, so the player can't leave, and the final character becomes a required find.

## 3. Changes

All changes are in `main_story_chapter_4.py`.

### 3.1 Task 3 (`main_story_ch4_meet_kirn`): Catalyst's first standing text

Replace the Catalyst standing text set right after `create_npc` for `catalyst`. Its current text is "I am the Catalyst. The fracture's herald and harbinger." and "You cannot stop the collapse…".

```python
{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'catalyst', 'standing_text': [
    "You come before me... incomplete.",
    "One of your number still wanders the rift. I will not waste the collapse on a fraction.",
    "Find them. Then return, and be ended whole."
] } },
```

Catalyst should **not** say "cannot face you". He's the herald and an ENTJ, so he refuses, he doesn't fear. The existing herald lines are kept: the meet task's own completion events already set them (Task 5, unchanged).

### 3.2 Task 3: move the Catalyst award

At the end of Task 3's `task_complete_events`, **remove**:

```python
{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch4_meet_catalyst' } }
```

Keep `award_task main_story_ch4_meet_final_character` where it is.

### 3.3 Task 4 (`main_story_ch4_meet_final_character`): award Catalyst after the join

Add this as the **last** event in `task_complete_events`, after `player_character_join` so the character is in the party first:

```python
{ 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch4_meet_catalyst' } }
```

### 3.4 Unchanged

- Task 5 (`main_story_ch4_meet_catalyst`): its dialog, the character reactions, the herald standing text, and awarding `main_story_ch4_defeat_catalyst`.
- Task 6 (defeat Catalyst), the dungeon lock and unlock, and the final character's placement in `corridor`.

## 4. Out of scope

- Existing saves already inside the rift with `main_story_ch4_meet_catalyst` active. No migration, per the no-carry-over rule.

## 5. Verification

1. Run the story timeline validator. There are no new errors, and `main_story_ch4_meet_catalyst` is now reachable only from `main_story_ch4_meet_final_character`.
2. **Skip path:** enter the rift and go straight to Catalyst. All three new standing lines show, no boss intro plays, no fight starts, and the party is still four.
3. **Required path:** talk to the final character. Their intro and join dialogs play and they join (the party is five). Then talk to Catalyst: `catalyst_ch4_intro` plays, the character reactions follow, and `main_story_ch4_defeat_catalyst` starts the boss fight.
4. **Order:** the quest log shows the Catalyst meet task only after the final character has joined.
5. After Catalyst's defeat, the rift unlocks and the Chapter 4 ending plays as before.
