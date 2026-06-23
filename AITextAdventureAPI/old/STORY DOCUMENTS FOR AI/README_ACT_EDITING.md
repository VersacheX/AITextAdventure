# Mermaid Timeline Editing Guide for Acts I-VI

## Overview

This document provides guidelines for editing the Mermaid timeline files (`.mmd`) that define the narrative structure of AI Text Adventure. These timelines are the **source of truth** for story progression and must follow strict formatting rules to ensure successful conversion to Python chapter files.

---

## Table of Contents

1. [File Structure](#file-structure)
2. [Act Structure Reference](#act-structure-reference)
3. [City and Location Reference](#city-and-location-reference)
4. [Timeline Syntax Rules](#timeline-syntax-rules)
5. [Task Block Structure](#task-block-structure)
6. [Event Syntax](#event-syntax)
7. [Dialog Formatting](#dialog-formatting)
8. [Common Patterns](#common-patterns)
9. [Act-Specific Guidelines](#act-specific-guidelines)
10. [Validation Checklist](#validation-checklist)

---

## File Structure

### Timeline Files
Located in: `AITextAdventureAPI\old\STORY DOCUMENTS FOR AI\`

| File | Chapters | Act Theme |
|------|----------|-----------|
| `TIMELINE ACT I.mmd` | 1-4 | The World in Becoming (Existential Chaos) |
| `TIMELINE ACT II.mmd` | 5-7 | The Humanist Act (World-Building & Regional Fracture) |
| `TIMELINE ACT III.mmd` | 8-13 | The Fall of the Body (Sensation & Impulse Collapse) |
| `TIMELINE ACT IV.mmd` | 14-15 | The Fall of the Heart (Emotion & Identity Collapse) |
| `TIMELINE ACT V.mmd` | 16-20 | The Fall of the Mind (Logic & Structure Collapse) |
| `TIMELINE ACT VI.mmd` | 21 | The Fall of Existence (Metaphysics Collapse) |
| `REGION TIMELINE.mmd` | Regional | 7 Regional Hero Arcs (Acts II-III) |

---

## Act Structure Reference

### The True Functional Cascade Model

The world collapses in this specific order:

```
ACT I (Ch 1-4)    ? Existential Chaos (world forming)
ACT II (Ch 5-7)   ? Humanist Act (regional stabilization)
ACT III (Ch 8-13) ? Fall of Body (sensation & impulse)
ACT IV (Ch 14-15) ? Fall of Heart (emotion & identity)
ACT V (Ch 16-20)  ? Fall of Mind (logic & structure)
ACT VI (Ch 21)    ? Fall of Existence (metaphysics)
```

### Voidwalker Progression

Each act introduces specific Voidwalkers:

**ACT III (Body):**
- Ch 8: Glamour ? Scalpel
- Ch 9: Scalpel's Domain
- Ch 10: Human Chaos (Rapture & Revelry influence, no boss)
- Ch 11: Rapture & Revelry (fought together)
- Ch 12: Lament (transition begins)
- Ch 13: Garbage (identity rot)

**ACT IV (Heart):**
- Ch 14: Stigma (moral pressure)
- Ch 15: Pageant & Edict (performance + authority)

**ACT V (Mind):**
- Ch 16: Path Without Meaning (hangover)
- Ch 17: Paradox & Crux (cognitive collapse)
- Ch 18: Reconstructing the Self
- Ch 19: Cataclysm (systemic collapse)
- Ch 20: Oracle & Reliquary (destiny collapse)

**ACT VI (Existence):**
- Ch 21: Dominion's Gauntlet ? The Void

---

## City and Location Reference

### Region Types and Cities

From `game\region_seeds\regions\cities\README.md`:

#### Desert Cities
- **Nightveil Spire** (Large) - Ch 8 (Glamour)
- **The Radpost** (Outpost) - Ch 9 (Scalpel)
- **Sunhaven Crossing** (Medium)
- **Dustshore** (Small)

#### Forest Cities
- **Thornshade Hamlet** (Village) - Ch 16 (Path Without Meaning)
- **Boiling Bubble** (Large) - Ch 2
- **Aurelion Veil** (Medium) - Ch 18 (Reconstructing Self)
- **Verdant Hollow** (Small)

#### Grassland Cities
- **Crosswind Bazaar** (Large) - Ch 10 (Human Chaos)
- **Highsteeple Crossing** (Medium) - Ch 3
- **Quantford Hollow** (Village) - Ch 12 (Lament)
- **Meadowrun** (Small)

#### Mountain Cities
- **Gallows Rift** (Large) - Ch 17 (Paradox & Crux)
- **Ironveil Foundry** (Medium) - Ch 4
- **Hollerforge Hollow** (Small) - Ch 21 (Dominion's Gauntlet)

#### Shallows Cities
- **Tidekin Cove** (Large) - Ch 15 (Pageant & Edict)
- **Brineward Harbor** (Medium) - Ch 5
- **Blackwake Bay** (Small) - Ch 11 (Rapture & Revelry)

#### Snow Cities
- **Frostgate Spire** (Large) - Ch 19 (Cataclysm)
- **Hailward Hold** (Medium) - Ch 14 (Stigma)
- **Glacier's Edge** (Small)

#### Swamp Cities
- **Bayou Nocturne** (Large) - Ch 20 (Oracle & Reliquary)
- **The Necropolis** (Medium) - Ch 13 (Garbage)
- **Mistvale** (Small)

### Location Reference Patterns

```
region_city_inn     # Inn in current region's city
region_city_bar           # Bar in current region's city
region_city_shopitems        # Item shop
region_city_shopweapons      # Weapon shop
region_city_shoparmor  # Armor shop
region_city_open_area      # Open area near city
region_city_district    # City district (for dungeons)
region_open_area  # Region wilderness
```

---

## Timeline Syntax Rules

### Basic Timeline Header

```mermaid
timeline
    title The Fracture Saga - ACT [NUM] - Chapter [X]

    section Chapter [X] - [Chapter Title]
        TASK - [Task Name] - [Task Type]:
            ? ACQUIRED:
  [Acquisition condition]:
            ? COMPLETED:
 [Completion actions]:
            EVENT - [event_type] - [params]:
```

### Indentation Rules

**CRITICAL:** Mermaid timelines are **indentation-sensitive**. Use **4 spaces** for each level:

```
timeline
    title The Fracture Saga - ACT III - Chapter 8

    section Chapter 8 - Glamour's City
     TASK - Arrive at Nightveil Spire - Desert City:
    ? ACQUIRED:
      Airship lands at third continent:
 Travel to Nightveil Spire Desert City:
     ? COMPLETED:
            Narrator - The city shimmers with illusions.:
    EVENT - award_task - meet_veyla

        TASK - Meet Veyla - NPC:
  ? ACQUIRED:
            EVENT - create_npc - veyla - region_city_inn:
            ? COMPLETED:
    Veyla - Your faces… I know them… no wait—:
            EVENT - award_task - meet_rusk
```

**Rules:**
- Base level: `timeline`, `title`, `section` ? **0 spaces**
- Task level: `TASK - [Name]` ? **8 spaces** (2 indents)
- Acquired/Completed: `? ACQUIRED:`, `? COMPLETED:` ? **12 spaces** (3 indents)
- Content under Acquired/Completed ? **12 spaces** (3 indents)
- Dialog lines ? **12 spaces** (3 indents)
- Events ? **12 spaces** (3 indents)

---

## Task Block Structure

### Standard Task Template

```
        TASK - [Task Name] - [Task Type]:
      ? ACQUIRED:
     [Acquisition condition line 1]:
            [Acquisition condition line 2]:
     EVENT - [event_type] - [params]:
            ? COMPLETED:
    [Completion description]:
       [Speaker] - [Dialog line]:
    [Speaker] - [Dialog line]:
   EVENT - [event_type] - [params]:
     EVENT - [event_type] - [params]:
```

### Task Type Indicators

| Indicator | Task Type | Description |
|-----------|-----------|-------------|
| `Meet [NPC]` | `meet` | Meet an NPC character |
| `Deliver [Item] to [NPC]` | `deliver` | Deliver item to NPC |
| `Fetch [Item]` | `fetch` | Retrieve an item |
| `Defeat [Enemy]` | `defeat` | Defeat a boss/enemy |
| `Travel to [Location]` | `goto` | Go to specific location |
| `Event` | Special | Story progression events |
| `Dungeon` | Special | Dungeon exploration |
| `NPC` | `meet` | Generic NPC interaction |
| `Location` | `goto` | Location arrival |

### Task Naming Conventions

**Format:** `TASK - [Action] [Target] - [Type]`

**Examples:**
- `TASK - Meet Velka - NPC`
- `TASK - Defeat Glamour Projection - MOB`
- `TASK - Deliver Cursed Couplet to Mira - NPC`
- `TASK - Travel to Nightveil Spire - Desert City`
- `TASK - Explore Theatre of Echoed Faces - Dungeon`
- `TASK - Glamour Replaced by Scalpel - Transition`

---

## Event Syntax

### Event Format

```
EVENT - [event_type] - [param1] - [param2] - [param3]
```

### Common Event Types

#### NPC Events
```
EVENT - create_npc - [npc_id] - [location]
EVENT - show_npc - [npc_id] - [location]
EVENT - hide_npc - [npc_id]
EVENT - set_npc_met - [npc_id]
EVENT - set_npc_standing_text - [npc_id] - [text]
```

#### Task Events
```
EVENT - award_task - [task_id]
```

#### Dialog Events
```
EVENT - initiate_dialog - [npc_id] - [dialog_id]
EVENT - initiate_character_dialog - [character_id] - [dialog_id]
```

#### Item Events
```
EVENT - award_item - [item_id]
EVENT - remove_item - [item_id]
EVENT - award_money - [amount]
```

#### Dungeon Events
```
EVENT - create_dungeon - [dungeon_id] - [location]
EVENT - set_player_in_dungeon - [dungeon_id] - [dungeon_location]
EVENT - remove_player_from_dungeon - [dungeon_id]
EVENT - lock_dungeon - [dungeon_id]
EVENT - unlock_dungeon - [dungeon_id]
EVENT - set_dungeon_locked_text - [dungeon_id] - [text]
EVENT - dungeon_add_treasure - [dungeon_id] - [item_id] - [location]
EVENT - dungeon_add_npc - [dungeon_id] - [npc_id] - [location]
```

#### Combat Events
```
EVENT - begin_combat - boss_battle - [boss_mob_id]
```

#### Progression Events
```
EVENT - advance_chapter
EVENT - complete_intro_story
EVENT - complete_region_quest - [region_id]
```

#### Character Events
```
EVENT - character_join - [character_id]
EVENT - player_character_join - [dialog_id] - is_final_character
EVENT - add_pending_character
EVENT - create_character_npc - [location]
```

#### Airship Events
```
EVENT - set_aircraft - [location]
EVENT - can_aircraft_fly - [can_fly]
EVENT - allow_ocean_flight
```

### Multi-Parameter Events

When events have multiple parameters, separate with ` - `:

```
EVENT - create_npc - veyla - region_city_inn
EVENT - dungeon_add_treasure - theatre_of_echoed_faces - focus_lens - final_chamber
EVENT - set_npc_standing_text - rusk - The pylons are scattered. Destroy them.
```

---

## Dialog Formatting

### Dialog Line Format

```
[Speaker] - [Dialog text]:
```

**Rules:**
1. Always end with colon `:`
2. Use proper speaker names (NPC names or "Narrator")
3. Preserve ellipsis, dashes, and punctuation within dialog
4. Keep character voice consistent

### Speaker Types

**NPCs:**
```
Velka - The maps are wrong.:
Rusk - QUIET HOURS! QUIET HOURS! …No one listens anymore.:
```

**Narrator:**
```
Narrator - The city shimmers with illusions. Mirrors line every surface.:
Narrator - As Glamour's projection shatters, the air grows cold.:
```

**Player Characters:**
```
Chock - Ooooooooh! I'm gonna find that guy and take him to pound town!:
Moxie - Hahaha! Look at him run!:
Kade - I wouldn't mind knocking back a few drinks!:
Kaera - This place is falling apart, maybe our friends are around too.:
Poise - This world is unlike any I've seen. We need to adapt quickly.:
```

### Multi-Line Dialog

Keep consecutive lines from same speaker together:

```
Seth - So Rook sent you to run me down?:
Seth - That guy's got it bad for me.:
Seth - This personal vendetta of his is really getting old.:
```

### Dialog with Special Characters

Preserve special characters:

```
Velka - I can't tell… is this memory or prophecy?:
Moxie - Ohhh, dangerous curios. My favorite kind. Let me at it!:
Poise - Stay calm. Precision over passion.:
```

---

## Common Patterns

### Pattern 1: Simple NPC Meeting

```
    TASK - Meet [NPC Name] - NPC:
      ? ACQUIRED:
 EVENT - create_npc - [npc_id] - [location]:
            ? COMPLETED:
            [NPC] - [Greeting dialog]:
      [NPC] - [Request or information]:
    EVENT - set_npc_standing_text - [npc_id] - [standing_text]:
            EVENT - award_task - [next_task_id]
```

### Pattern 2: Item Delivery

```
        TASK - Deliver [Item] to [NPC] - NPC:
       ? ACQUIRED:
     Deliver item [item_id] to [NPC]:
        ? COMPLETED:
        [NPC] - [Receives item dialog]:
            [NPC] - [Next instructions]:
  EVENT - remove_item - [item_id]:
          EVENT - award_item - [reward_item_id]:
      EVENT - award_task - [next_task_id]
```

### Pattern 3: Dungeon Boss Fight (Two-Task Pattern)

```
        TASK - Meet [Boss] - NPC:
      ? ACQUIRED:
  EVENT - create_npc - [boss_id] - None:
    ? COMPLETED:
   [Boss] - [Threatening dialog]:
    EVENT - award_task - defeat_[boss]

        TASK - Defeat [Boss] - MOB:
          ? ACQUIRED:
            EVENT - begin_combat - boss_battle - [boss_id]_1:
  ? COMPLETED:
            [Boss] - [Death dialog]:
        EVENT - hide_npc - [boss_id]:
            EVENT - complete_region_quest - [region_id]:
         EVENT - award_task - [next_task_id]
```

### Pattern 4: Dungeon Exploration

```
        TASK - Explore [Dungeon Name] - Dungeon:
? ACQUIRED:
            EVENT - create_dungeon - [dungeon_id] - [location]:
     EVENT - set_player_in_dungeon - [dungeon_id] - entrance:
  ? COMPLETED:
            Narrator - [Dungeon description]:
            [Character] - [Reaction]:
      EVENT - award_task - [next_task_id]
```

### Pattern 5: Character Reactions

After major events, include player character reactions:

```
            Chock - [Bold, direct reaction]:
   Moxie - [Playful, chaotic reaction]:
            Kade - [Analytical, sarcastic reaction]:
Kaera - [Spiritual, empathetic reaction]:
            Poise - [Disciplined, calm reaction]:
```

### Pattern 6: Chapter Transition

Final task of each chapter:

```
 TASK - [Final Task Name] - [Type]:
     ? ACQUIRED:
            [Setup]:
    ? COMPLETED:
  [Resolution dialog]:
     EVENT - [final_event]:
 EVENT - advance_chapter
```

---

## Act-Specific Guidelines

### ACT I (Chapters 1-4) - Existential Chaos

**Theme:** World forming, party gathering, mechanics introduction

**Key Elements:**
- Introduction of 5 core party members (one per chapter)
- Catalyst boss fight at end (triggers world stabilization)
- Bracelet of Void and Bracelet of Existence introduced
- Seth as recurring ally/antagonist

**Required Events:**
- `complete_intro_story` at end of Ch 4
- Character joins after each chapter (Chs 2-4)

**Example Structure:**
```
        TASK - Defeat Catalyst - Boss Fight:
            ? ACQUIRED:
      EVENT - begin_combat - boss_battle - catalyst_1:
   ? COMPLETED:
    Narrator - Reality screams as Catalyst falls.:
          EVENT - hide_npc - catalyst:
            EVENT - complete_intro_story:
    EVENT - advance_chapter
```

### ACT II (Chapters 5-7) - Humanist Act

**Theme:** World stabilization, regional focus, airship requirement

**Key Elements:**
- Riftwaters crossing via teleportation (Ch 5)
- Regional hero arcs gate (Ch 7)
- Seth's airship becomes available
- 7 regional heroes must be recruited (from `REGION TIMELINE.mmd`)

**Required Events:**
- `complete_regional_quests` gate in Ch 7
- `set_aircraft` and `can_aircraft_fly` at end of Ch 7

**Example Structure:**
```
        TASK - Requires All Regional Arcs Completed - Gate:
            ? ACQUIRED:
            Gate for regional content:
        ? COMPLETED:
         Seth - Complete all seven regional hero arcs.:
            EVENT - award_task - prepare_airship_for_departure

        TASK - Prepare Airship for Departure - Event:
         ? ACQUIRED:
         EVENT - create_aircraft - the_rustwing - region_city_open_area:
          ? COMPLETED:
            Seth - She's old, but she flies. Usually.:
            EVENT - can_aircraft_fly - True:
EVENT - advance_chapter
```

### ACT III (Chapters 8-13) - Fall of the Body

**Theme:** Sensation & impulse collapse, Voidwalker battles begin

**Key Elements:**
- Glamour ? Scalpel transition (Ch 8)
- First team-up boss fight: Rapture & Revelry (Ch 11)
- Ch 10 has **no boss fight** (human chaos consequences only)
- Lament introduces emotional collapse (Ch 12)
- Garbage = identity rot (Ch 13)

**Voidwalker Pattern:**
```
        TASK - Defeat [Voidwalker 1] and [Voidwalker 2] - MOB:
       ? ACQUIRED:
  EVENT - create_npc - [voidwalker1] - None:
          EVENT - create_npc - [voidwalker2] - None:
   EVENT - begin_combat - boss_battle - [voidwalker1]_1 - [voidwalker2]_1:
       ? COMPLETED:
            [Voidwalker 1] - [Death line]:
       [Voidwalker 2] - [Death line]:
          EVENT - hide_npc - [voidwalker1]:
  EVENT - hide_npc - [voidwalker2]:
      EVENT - award_task - [next_task_id]
```

**Important:** Use city names from reference:
- Ch 8: Nightveil Spire (Desert Large)
- Ch 9: The Radpost (Desert Outpost)
- Ch 10: Crosswind Bazaar (Grassland Large)
- Ch 11: Blackwake Bay (Shallows Small)
- Ch 12: Quantford Hollow (Grassland Village)
- Ch 13: The Necropolis (Swamp Medium)

### ACT IV (Chapters 14-15) - Fall of the Heart

**Theme:** Emotion & identity collapse, performance as control

**Key Elements:**
- Stigma = moral pressure, shame weaponization (Ch 14)
- Pageant + Edict = performance + authority (Ch 15)
- Rave-state authoritarian island in Ch 15
- Tess and Sam emotional breakpoint

**Chapter 15 Special Location:**
```
        TASK - Enter Heap of Broken Futures - District:
            ? ACQUIRED:
          Entering district:
        ? COMPLETED:
            Narrator - Neon lights and synchronized crowds.:
      Narrator - "Perform or Be Removed" flashes.:
```

**Cities:**
- Ch 14: Hailward Hold (Snow Medium)
- Ch 15: Tidekin Cove (Shallows Large)

### ACT V (Chapters 16-20) - Fall of the Mind

**Theme:** Logic & structure collapse, cognitive failure

**Key Elements:**
- Ch 16 = hangover chapter (no boss fight)
- Ch 17 = Paradox + Crux team-up
- Ch 18 = identity reconstruction attempt
- Ch 19 = Cataclysm (systemic collapse)
- Ch 20 = Oracle + Reliquary (destiny collapse)

**Chapter 16 Pattern (No Boss):**
```
        TASK - Enter Ruin Echo District - Location:
      ? ACQUIRED:
       Entering ruin district:
     ? COMPLETED:
 Narrator - Actions feel disconnected from consequences.:
            Narrator - Choices feel weightless.:
   EVENT - award_task - [next_task_id]
```

**Cities:**
- Ch 16: Thornshade Hamlet (Forest Village)
- Ch 17: Gallows Rift (Mountain Large)
- Ch 18: Aurelion Veil (Forest Medium)
- Ch 19: Frostgate Spire (Snow Large)
- Ch 20: Bayou Nocturne (Swamp Large)

### ACT VI (Chapter 21) - Fall of Existence

**Theme:** Metaphysics collapse, final encounter

**Key Elements:**
- Dominion's Gauntlet = fight all previous Voidwalkers again
- Sequential stripping: identity ? purpose ? memory ? humanity
- The Void = final boss
- Bracelet of Existence and Bracelet of Void reforge
- Four possible endings

**Trial Pattern:**
```
     TASK - Defeat [Voidwalker A] and [Voidwalker B] Trial - MOB:
            ? ACQUIRED:
  EVENT - create_npc - [voidwalker_a]_trial - None:
  EVENT - create_npc - [voidwalker_b]_trial - None:
            EVENT - begin_combat - boss_battle - [voidwalker_a]_trial_1 - [voidwalker_b]_trial_1:
            ? COMPLETED:
        [Voidwalker A] - [Repeat thematic line]:
 [Voidwalker B] - [Repeat thematic line]:
            EVENT - hide_npc - [voidwalker_a]_trial:
        EVENT - hide_npc - [voidwalker_b]_trial:
    EVENT - award_task - [next_trial]
```

**Cities:**
- Ch 21: Hollerforge Hollow (Mountain Small)

---

## Validation Checklist

Before finalizing timeline edits, verify:

### Structure
- [ ] **Indentation**: All lines use correct 4-space indents
- [ ] **Section Headers**: `section Chapter [X] - [Title]` format
- [ ] **Task Names**: Follow `TASK - [Action] [Target] - [Type]` pattern

### Content
- [ ] **City Names**: Match reference list exactly
- [ ] **Location References**: Use correct `region_city_*` or `region_open_area` format
- [ ] **Speaker Names**: Consistent capitalization and spelling
- [ ] **Dialog Lines**: All end with colon `:`

### Events
- [ ] **Event Format**: `EVENT - [type] - [param1] - [param2]` with proper separators
- [ ] **Task Chain**: Each task awards next task or advances chapter
- [ ] **Boss Fights**: Use two-task pattern (meet ? defeat)
- [ ] **Dungeon Flow**: Create ? Enter ? Exit sequence

### Act Compliance
- [ ] **ACT I**: `complete_intro_story` at end of Ch 4
- [ ] **ACT II**: `complete_regional_quests` gate in Ch 7
- [ ] **ACT III**: Correct city assignments, Ch 10 has no boss
- [ ] **ACT IV**: Tess/Sam crisis moments included
- [ ] **ACT V**: Ch 16 hangover chapter (no boss), cognitive themes
- [ ] **ACT VI**: Trial pattern for all Voidwalker pairs

### Character Reactions
- [ ] **Major Events**: Include reactions from 3-5 party members
- [ ] **Voice Consistency**: 
  - Chock (bold, direct)
  - Moxie (playful, chaotic)
  - Kade (analytical, sarcastic)
  - Kaera (spiritual, empathetic)
  - Poise (disciplined, calm)

### Regional Arc Compliance (REGION TIMELINE.mmd)
- [ ] **7 Regional Heroes**: Desert, Forest, Grassland, Mountain, Shallows, Snow, Swamp
- [ ] **Task Pattern**: Meet hero ? Deliver item ? Defeat villain ? Report back
- [ ] **Event Flow**: Create NPC ? Award task ? Begin combat ? Hide NPC ? Character join

---

## Common Editing Scenarios

### Scenario 1: Adding a New NPC

```
        TASK - Meet [New NPC] - NPC:
            ? ACQUIRED:
            EVENT - create_npc - [npc_id] - [location]:
        ? COMPLETED:
            [NPC] - [Introduction dialog]:
    [NPC] - [Information or request]:
   [Character] - [Reaction to NPC]:
      EVENT - set_npc_standing_text - [npc_id] - [permanent text]:
    EVENT - award_task - [next_task_id]
```

### Scenario 2: Adding a Dungeon

```
        TASK - Explore [Dungeon Name] - Dungeon:
     ? ACQUIRED:
    EVENT - create_dungeon - [dungeon_id] - [location]:
 EVENT - set_player_in_dungeon - [dungeon_id] - entrance:
            ? COMPLETED:
            Narrator - [Atmospheric description]:
            [Character] - [Reaction to dungeon]:
            [Character] - [Strategic observation]:
EVENT - award_task - [boss_encounter_task_id]
```

### Scenario 3: Modifying Dialog

**Before:**
```
          Velka - The maps are wrong.:
```

**After (more character):**
```
 Velka - The maps are wrong. They're shifting under my hands.:
            Velka - Arcane lines are rewriting themselves.:
```

### Scenario 4: Adding Character Reactions

**Before:**
```
    EVENT - award_task - meet_drin
```

**After:**
```
     Chock - If the maps are fighting back, something's provoking them.:
          Kaera - A disturbance like this… it feels alive. We should hurry.:
   Kade - Great. Reality's glitching again.:
        EVENT - award_task - meet_drin
```

### Scenario 5: Changing City Location

**Before:**
```
            Travel to Generic City:
```

**After (using reference):**
```
   Travel to Nightveil Spire Desert City:
```

---

## Regional Timeline Special Rules

`REGION TIMELINE.mmd` follows a different structure:

### Regional Arc Pattern

```
    section [Region] Arc - [Hero] vs [Villain]
        TASK - [Region] Primary Initialize - Event:
      ? ACQUIRED:
         Complete intro story:
     ? COMPLETED:
        EVENT - create_npc - [hero_id] - region_bar:
            [Hero] - [Greeting]:
            EVENT - award_task - meet_[hero_id]

     TASK - Meet [Hero] - NPC:
        ? ACQUIRED:
            [Hero] already exists at location:
        ? COMPLETED:
            [Hero] - [Problem description]:
         EVENT - award_task - deliver_[item]_to_[hero]

        TASK - Deliver [Item] to [Hero] - NPC:
 ? ACQUIRED:
         Deliver item [item_id] to [Hero]:
    ? COMPLETED:
            [Hero] - [Thanks and villain info]:
     EVENT - remove_item - [item_id]:
        EVENT - set_npc_standing_text - [hero_id] - [updated text]:
   EVENT - award_task - defeat_[villain]

        TASK - Meet [Villain] - NPC:
        ? ACQUIRED:
  EVENT - create_dungeon - [villain]_lair - region_open_area:
            EVENT - create_npc - [villain] - None:
   ? COMPLETED:
      [Villain] - [Threatening dialog]:
      EVENT - award_task - defeat_[villain]_boss_fight

   TASK - Defeat [Villain] - MOB:
            ? ACQUIRED:
   EVENT - begin_combat - boss_battle - [villain]_1:
            ? COMPLETED:
         [Villain] - [Death line]:
            EVENT - hide_npc - [villain]:
        EVENT - complete_region_quest - [region_id]:
     EVENT - award_task - report_to_[hero]

        TASK - Report to [Hero] - NPC:
            ? ACQUIRED:
            Returning to [Hero]:
         ? COMPLETED:
[Hero] - [Victory celebration]:
      EVENT - hide_npc - [hero_id]:
     EVENT - character_join - [hero_id]
```

**7 Required Regional Arcs:**
1. Desert - Sable vs Zaruun
2. Forest - Thorn vs Elder Marrowroot
3. Grassland - Nia vs Serene
4. Mountain - Bragg vs Rokhuld
5. Shallows - Ripple vs Uul'thar
6. Snow - Kor-in vs Lady Aeriola
7. Swamp - Grimnaw vs Lich-King Miregloom

---

## Troubleshooting

### Issue: Indentation Errors

**Symptom:** Timeline doesn't render or converts incorrectly

**Fix:** Check that all content lines under `? ACQUIRED:` and `? COMPLETED:` use exactly 12 spaces (3 indents)

### Issue: Event Not Triggering

**Symptom:** Event doesn't execute in Python conversion

**Fix:**
- Verify event syntax: `EVENT - [type] - [param1] - [param2]`
- Check event type is valid (see Event Syntax section)
- Ensure event is under `? COMPLETED:` section

### Issue: Dialog Not Displaying

**Symptom:** Dialog lines missing in game

**Fix:**
- Verify line ends with colon `:`
- Check speaker name matches NPC ID
- Ensure dialog is under `? COMPLETED:` section

### Issue: Task Not Chaining

**Symptom:** Story progression stops

**Fix:**
- Verify previous task has `EVENT - award_task - [next_task_id]`
- Check task ID matches exactly (case-sensitive)
- Ensure task is in correct chapter file

### Issue: City Not Found

**Symptom:** Location reference fails

**Fix:**
- Check city name against reference list
- Verify region type is correct
- Use exact spelling from city reference

---

## Quick Reference: Event Parameters

### NPC Locations
```
region_city_inn
region_city_bar
region_city_shopitems
region_city_shopweapons
region_city_shoparmor
region_city_open_area
region_city_district
region_open_area
None (for dungeon NPCs)
```

### Dungeon Locations
```
entrance
corridor
treasure_room
final_chamber
```

### Task Types
```
meet
deliver
fetch
defeat
goto
complete_intro_story
complete_regional_quests
```

### Boss Naming
```
[boss_name]_1 (for mob IDs)
[boss_name]_trial_1 (for ACT VI trials)
```

---

## Version History

- **v1.0** - Initial guide with Acts I-VI coverage
- Future: Will be updated as timeline format evolves

---

## Contact

For questions or issues with timeline editing:
- Reference `README.md` for Python conversion process
- Check `task.py` for valid task types
- Check `task_completion_service.py` for valid event types
- Review `game\region_seeds\regions\cities\README.md` for city names

---

## Final Notes

**Remember:**
1. **Indentation is critical** - Use 4 spaces per level
2. **City names must match reference** - Check spelling
3. **Dialog lines end with colons** - Always
4. **Events chain tasks together** - Verify flow
5. **Act themes drive story** - Stay consistent with cascade model
6. **Character voices matter** - Keep reactions authentic
7. **Regional arcs required** - All 7 must complete before Ch 8

**The timeline is the source of truth** - Changes here propagate to Python, so edit carefully!

### Writing Spicy Dialogue

You are a master of spicy, character-driven dialog for The Fracture Saga.

Rules:
- Stay 100% faithful to each character's MBTI, Enneagram (core fear/desire/wing), and psychology profile.
- Every major line must contain emotional texture + at least one callback to past events (Ember, bracelets, specific Voidwalkers, party failures).
- Layer dark humor, sexual tension, violence, vulnerability, and philosophical bite.
- Use physical stage directions in *italics*.
- Make Voidwalkers personally vicious using the target's exact fears.
- Banter must feel alive and overlapping.

"Spicy" dialogue is sharp, personal, and raises the stakes. It moves beyond simple statements to attack the core of a character's or a philosophy's identity. Use these principles to upgrade dialogue from functional to memorable.

#### 1. Weaponize Philosophy
Don't just state a philosophy; turn it into a weapon. The Voidwalkers' arguments should be seductive, logical, and directly challenge the party's worldview.

*   **Standard:** `Stigma - We assign roles to people.`
*   **Spicy:** `Stigma - You can feel it the moment you step in here, can't you? That quiet question everyone carries: "What am I, really, when it matters?" That question introduces instability. So we remove it.:`

The spicy version is an invasive, personal observation that makes the abstract concept of "assigning roles" feel like a necessary, almost merciful act.

#### 2. Make it Personal
Use a character's known history, personality, or insecurities against them. This is the core of the hero-voidwalker dynamic. The Voidwalkers represent the characters' "ugliest selves" and should know exactly where to strike.

*   **Standard:** `Kaera - That's wrong.`
*   **Spicy (Stigma vs. Kaera):** `Stigma - Let's simplify this. You see someone hurt, and you help them. Again. And again. So tell me- what are you without that?:`

This directly attacks Kaera's identity as a helper, reframing her greatest strength as a fragile dependency. It forces her to defend not just her actions, but her very sense of self.

#### 3. Use Subtext and Innuendo
Imply threats and insults rather than stating them outright. This creates more tension and forces the reader to engage with the underlying meaning.

*   **Standard:** `Pageant - You are all performing for me.`
*   **Spicy:** `Pageant - You all carry yourselves so carefully. The effort it takes to look like you're in control... even when you aren't.:`

The spicy version is a condescending observation that undermines the party's composure. It's not a direct accusation, but a judgment of their internal state, which is far more insulting.

#### 4. Contrast Character Voices
Amplify conflict by juxtaposing different character perspectives. A moment of philosophical horror for one character can be a moment of gleeful chaos for another.

*   **Monolithic Reaction:** `Everyone - This is bad.`
*   **Spicy Contrast:**
    `Kaera - They're smiling-while everything is falling apart...:`
    `Lament - Because stopping means feeling it.:`
    `Revelry - You get it. Right? The rush. The alive feeling.:`
    `Moxie - Yeah... until it isn't anymore.:`

This exchange deepens the theme by showing the horror (Kaera), the tragic reasoning (Lament), the seductive appeal (Revelry), and the pragmatic cynicism (Moxie) of the situation all at once.

#### 5. Cut to the Core
The most powerful lines are often short, direct, and delivered after a long, philosophical monologue. They act as a sharp rebuttal that cuts through the noise.

*   **Verbose:** `Dominion - [Long speech about the perfection of systemic resolution and the futility of choice].`
*   **Spicy Rebuttal:** `Chock - Good.:`

Chock's one-word answer is powerful because it doesn't just disagree; it accepts Dominion's premise (that choice creates instability) and embraces it as a positive. It completely reframes the argument with maximum efficiency.

---

## Common Patterns

### Pattern 1: Simple NPC Meeting

```
    TASK - Meet [NPC Name] - NPC:
      ? ACQUIRED:
 EVENT - create_npc - [npc_id] - [location]:
            ? COMPLETED:
            [NPC] - [Greeting dialog]:
      [NPC] - [Request or information]:
    EVENT - set_npc_standing_text - [npc_id] - [standing_text]:
            EVENT - award_task - [next_task_id]
```

### Pattern 2: Item Delivery

```
        TASK - Deliver [Item] to [NPC] - NPC:
       ? ACQUIRED:
     Deliver item [item_id] to [NPC]:
        ? COMPLETED:
        [NPC] - [Receives item dialog]:
            [NPC] - [Next instructions]:
  EVENT - remove_item - [item_id]:
          EVENT - award_item - [reward_item_id]:
      EVENT - award_task - [next_task_id]
```

### Pattern 3: Dungeon Boss Fight (Two-Task Pattern)

```
        TASK - Meet [Boss] - NPC:
      ? ACQUIRED:
  EVENT - create_npc - [boss_id] - None:
    ? COMPLETED:
   [Boss] - [Threatening dialog]:
    EVENT - award_task - defeat_[boss]

        TASK - Defeat [Boss] - MOB:
          ? ACQUIRED:
            EVENT - begin_combat - boss_battle - [boss_id]_1:
  ? COMPLETED:
            [Boss] - [Death dialog]:
        EVENT - hide_npc - [boss_id]:
            EVENT - complete_region_quest - [region_id]:
         EVENT - award_task - [next_task_id]
```

### Pattern 4: Dungeon Exploration

```
        TASK - Explore [Dungeon Name] - Dungeon:
? ACQUIRED:
            EVENT - create_dungeon - [dungeon_id] - [location]:
     EVENT - set_player_in_dungeon - [dungeon_id] - entrance:
  ? COMPLETED:
            Narrator - [Dungeon description]:
            [Character] - [Reaction]:
      EVENT - award_task - [next_task_id]
```

### Pattern 5: Character Reactions

After major events, include player character reactions:

```
            Chock - [Bold, direct reaction]:
   Moxie - [Playful, chaotic reaction]:
            Kade - [Analytical, sarcastic reaction]:
Kaera - [Spiritual, empathetic reaction]:
            Poise - [Disciplined, calm reaction]:
```

### Pattern 6: Chapter Transition

Final task of each chapter:

```
 TASK - [Final Task Name] - [Type]:
     ? ACQUIRED:
            [Setup]:
    ? COMPLETED:
  [Resolution dialog]:
     EVENT - [final_event]:
 EVENT - advance_chapter
