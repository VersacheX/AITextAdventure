﻿# Mermaid Timeline to Python Chapter Conversion Guide

## Overview

This document describes the systematic process for converting Mermaid timeline (`.mmd`) files into Python chapter files (`.py`) for the AI Text Adventure game. This ensures consistency across all story chapters and maintains compatibility with the game's task and event systems.

---

## Source Files

### Mermaid Timeline Files (Input)
Located in: `AITextAdventureAPI\old\STORY DOCUMENTS FOR AI\`

- `TIMELINE ACT I.mmd` ? Chapter 1-4 (Awakening through Fracture Point)
- `TIMELINE ACT II.mmd` ? Chapter 5-7 (Riftwaters Crossing)
- `TIMELINE ACT III.mmd` ? Chapter 8-13 (Fall of the Body)
- `TIMELINE ACT IV.mmd` ? Chapter 14-15 (Fall of the Heart)
- `TIMELINE ACT V.mmd` ? Chapter 16-20 (Fall of Time)
- `TIMELINE ACT VI.mmd` ? Chapter 21 (Final Encounter)
- `REGION TIMELINE.mmd` ? Regional Hero Arcs (7 regions) **[NOT YET PROVIDED]**

### Python Chapter Files (Output)
Located in: `AITextAdventureAPI\old\game\region_seeds\main_story\`

- `main_story_chapter_1.py` through `main_story_chapter_21.py`

### Reference Files
- `task.py` - Defines task types and structure
- `task_completion_service.py` - Defines event types and execution
- Existing chapter files (1-7) - Templates for structure

---

## Conversion Process

> **IMPORTANT NOTE:** The primary goal of this process is to create a 1:1 translation of the Mermaid timeline into a Python chapter file. **Do not alter the sequence or location of events.** The order of dialogue, `award_task` events, and especially `advance_chapter` events must be preserved exactly as they appear in the `.mmd` file. The timeline may intentionally place an `advance_chapter` event before the final task of a section to facilitate narrative branching or parallel events. Moving it to the end of the task list will break the intended story flow.

### Step 1: Analyze Mermaid Timeline Structure

Mermaid timelines use this format:

```
timeline
    title The Fracture Saga - ACT II - Chapter 5

    section Chapter 5 - Riftwaters Crossing
        TASK - Return to Kirn - Tracking Signal:
            ► ACQUIRED:
                EVENT - show_npc - velka (region_city_inn):
            ► COMPLETED:
                Kirn - Dialog line 1:
                Kirn - Dialog line 2:
                EVENT - award_task - meet_velka
```

**Key Elements to Extract:**
- **Task Name**: `TASK - [Name] - [Type]`
- **Acquisition Conditions**: Under `► ACQUIRED:`
    - This block contains events that fire when the task is given to the player.
    - If a task has no acquisition events, this block should contain the text `(no acquired events):`.
- **Completion Actions**: Under `► COMPLETED:`
    - This block contains all dialogue and events that fire when the player completes the task's objective.
- **Dialog Lines**: `Speaker - Dialog text`
- **Events**: `EVENT - [event_type] - [params]`
- **Note on Descriptive Text**: Purely descriptive text (e.g., "Travel to the next city") should not be included in the timeline script, as it is not a functional game event.

---

### Step 2: Map Task Types

From `task.py`, valid task types are:

| Mermaid Indicator | Python Task Type | `to_type` | Description |
|-------------------|------------------|-----------|-------------|
| `Meet [NPC Name]` | `meet` | `npc` | Meet an NPC character |
| `Deliver [Item] to [NPC]` | `deliver` | `npc` | Deliver item to NPC |
| `Fetch [Item]` | `fetch` | `npc` | Retrieve an item |
| `Defeat [Enemy]` | `defeat` | `mob` | Defeat a boss/enemy |
| `Travel to [Location]` | `goto` | `coordinates` | Go to specific location |
| `Complete Intro Story` | `complete_intro_story` | N/A | Story gate |
| `Complete Regional Quests` | `complete_regional_quests` | N/A | Regional gate |

---

### Step 3: Map Event Types

From `task_completion_service.py`, valid event types:

#### NPC Events
```python
{ 'event_type': 'create_npc', 'params': { 'npc_id': 'npc_name', 'location': 'region_city_inn' }}
{ 'event_type': 'show_npc', 'params': { 'npc_id': 'npc_name', 'location': 'region_city_bar' }}
{ 'event_type': 'hide_npc', 'params': { 'npc_id': 'npc_name' }}
{ 'event_type': 'set_npc_met', 'params': { 'npc_id': 'npc_name' }}
{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'npc_name', 'standing_text': ['line1', 'line2'] }}
```

#### Dialog Events
```python
{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'npc_name', 'dialog_id': 'dialog_id' }}
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'character_name', 'dialog_id': 'dialog_id' }}
{ 'event_type': 'initiate_option_dialog', 'params': {
    'message': 'What do you want to do?',
    'options': [
        ('Fight the guard', 'ch1_fight_seth'),
        ('Sneak past',      'ch1_sneak'),
        ('Talk your way out', 'ch1_negotiate'),
    ]
}}
```
> **`initiate_option_dialog`** presents a blocking choice prompt to the player.
> The player selects exactly one option; the corresponding `target_task_id` is
> immediately awarded via the normal `award_task` flow.  Escape is disabled —
> the player must choose.  Only one option dialog can be pending at a time.
> Any `info_dialogs` in the queue are displayed in full before the option
> prompt appears, so dialogue lines always precede the player's choice.

#### Item Events
```python
{ 'event_type': 'award_item', 'params': { 'item_id': 'item_name' }}
{ 'event_type': 'remove_item', 'params': { 'item_id': 'item_name' }}
{ 'event_type': 'award_money', 'params': { 'amount': 100 }}
```

#### Dungeon Events
```python
{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'dungeon_name', 'location': 'region_open_area' }}
{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'dungeon_name', 'location': 'entrance' }}
{ 'event_type': 'remove_player_from_dungeon', 'params': { 'dungeon_id': 'dungeon_name' }}
{ 'event_type': 'lock_dungeon', 'params': { 'dungeon_id': 'dungeon_name' }}
{ 'event_type': 'unlock_dungeon', 'params': { 'dungeon_id': 'dungeon_name' }}
{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'dungeon_name', 'item_id': 'item_name', 'location': 'final_chamber' }}
{ 'event_type': 'dungeon_add_npc', 'params': { 'dungeon_id': 'dungeon_name', 'npc_id': 'npc_name', 'location': 'corridor' }}
```

#### Combat Events
```python
{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'enemy_name_1', 'combat_type': 'boss_battle' }}
```

#### Task Events
```python
{ 'event_type': 'award_task', 'params': { 'task_id': 'task_id_name' }}
```

#### Character Events
```python
{ 'event_type': 'character_join', 'params': { 'character_id': 'character_name' }}
{ 'event_type': 'player_character_join', 'params': { 'dialog_id': 'join_dialog_id', 'is_final_character': True }}
```

#### Party Events
```python
{ 'event_type': 'set_player_location', 'params': { 'location': 'region_city_open_area' }}
```

#### Progression Events
```python
{ 'event_type': 'advance_chapter' }
{ 'event_type': 'complete_intro_story' }
{ 'event_type': 'complete_region_quest', 'params': { 'region_id': 'desert' }}
{ 'event_type': 'unlock_npc_log' }
```

#### Airship Events
```python
{ 'event_type': 'set_aircraft', 'params': { 'location': 'region_city_open_area' }}
{ 'event_type': 'can_aircraft_fly', 'params': { 'can_fly': True }}
{ 'event_type': 'allow_ocean_flight' }
```

---

### Event System Behavioral Guide

This guide provides a detailed explanation of how each event type functions, its impact on the game state (`player_game`), and specific details on location resolution.

---

#### **NPC Events**

These events manage the lifecycle, visibility, and properties of Non-Player Characters (NPCs).

*   **`create_npc`**
    *   **Behavior:** Instantiates a new NPC from its template in `const.NPCS` and adds it to the `player_game.npcs` list. This makes the NPC exist in the game world.
    *   **Placement Logic:** The `location` parameter dictates the NPC's coordinates.
        *   If `location` is `None`, the NPC is created but not placed on the map (e.g., for a dungeon-specific or event-only appearance).
        *   If `location` is a string (e.g., `'region_city_inn'`), the system resolves it to a specific `(x, y, z)` coordinate by finding a random tile matching that building type within the contextually appropriate area (current city, another specified city, or the wilderness).
    *   **`player_game` Interaction:** Calls `player_game.add_npc(npc_object)`.

*   **`show_npc`**
    *   **Behavior:** Sets or updates the position of an existing NPC. This is used to make a hidden NPC appear or to move an already visible NPC to a new location.
    *   **Placement Logic:** It finds the NPC in `player_game.npcs` by `npc_id`. It then resolves the `location` string into new coordinates, identical to the `create_npc` logic, and updates the NPC's `position` attribute.
    *   **`player_game` Interaction:** Directly modifies the `.position` attribute of the specified NPC object within the `player_game.npcs` list.

*   **`hide_npc`**
    *   **Behavior:** Makes an NPC invisible on the world map by setting their position to `None`. The NPC object is retained in memory, allowing it to be revealed again with `show_npc`.
    *   **`player_game` Interaction:** Calls `player_game.hide_npc(npc_object)`, which sets the NPC's `.position` to `None`.

*   **`set_npc_met`**
    *   **Behavior:** Flags an NPC as "met" by the player. This is a crucial event for story progression and world-building.
    *   **Effect:** When an NPC is set as met, they are immediately added to the player's in-game "NPC Log." This allows the player to read about characters they may have heard about but not yet spoken to, providing context and driving curiosity.
    *   **`player_game` Interaction:** Calls `player_game.set_npc_met(npc_id)`.

*   **`set_npc_standing_text`**
    *   **Behavior:** Updates the passive, ambient dialogue an NPC speaks when the player is nearby.
    *   **`player_game` Interaction:** Finds the NPC by `npc_id` and updates its `standing_text` attribute.

---

#### **Dungeon Events**

These events control the creation, content, and player's interaction with dungeon environments.

*   **`create_dungeon`**
    *   **Behavior:** Generates a complete dungeon map from a template in `const.DUNGEON_SETTINGS` and places its entrance icon on the world map.
    *   **Placement Logic:** The `location` parameter determines the coordinates for the dungeon's entrance in the overworld, typically in a wilderness area (`region_open_area`).
    *   **`player_game` Interaction:** Calls `player_game.add_dungeon(dungeon_object)`.

*   **`set_player_in_dungeon`**
    *   **Behavior:** Transitions the player's view from the world map into the specified dungeon's interior map.
    *   **Placement Logic:** The `location` parameter (e.g., `'entrance'`, `'corridor'`, `'final_chamber'`) determines the player's starting tile within the dungeon. The system finds a random tile of the specified type and places the player there.
    *   **`player_game` Interaction:** Calls `player_game.place_player_in_dungeon_at_location(dungeon_id, location_type)`.

*   **`remove_player_from_dungeon`**
    *   **Behavior:** Exits the player from the dungeon interior back to the world map, placing them at the dungeon's entrance coordinates.
    *   **`player_game` Interaction:** Calls `player_game.remove_player_from_dungeon(dungeon_id)`.

*   **`dungeon_add_npc`**
    *   **Behavior:** Places an NPC within a dungeon. This NPC exists only within the dungeon's map.
    *   **Placement Logic:** Uses the `location` parameter (e.g., `'final_chamber'`) to place the NPC on a random tile of that type inside the dungeon.
    *   **`player_game` Interaction:** Finds the dungeon by `dungeon_id` and calls its internal `place_entity_at_location()` method.

*   **`dungeon_add_treasure`**
    *   **Behavior:** Places an item (treasure) within a dungeon for the player to find.
    *   **Placement Logic:** Identical to `dungeon_add_npc`, it uses the `location` parameter to place the item on a specific tile type.
    *   **`player_game` Interaction:** Finds the dungeon and calls its `place_entity_at_location()` method.

*   **`lock_dungeon` / `unlock_dungeon`**
    *   **Behavior:** Controls whether the player can enter a dungeon from the world map.
    *   **`player_game` Interaction:** Calls `player_game.lock_dungeon_by_id()` or `player_game.unlock_dungeon_by_id()`.

*   **`set_dungeon_locked_text`**
    *   **Behavior:** Sets the message the player sees when trying to enter a locked dungeon.
    *   **`player_game` Interaction:** Calls `player_game.set_dungeon_locked_text_by_id()`.

---

#### **Party Events**
*Note: These events manage the player's party members and their interactions or the player on the whole.*

*   **`set_player_location`**
    *   **Behavior:** Teleports the player to a new location on the world map. This is used for major story transitions, such as moving to a new city or region.
    *   **Placement Logic:** The `location` parameter is resolved to specific coordinates using the same logic as NPC placement.
    *   **`player_game` Interaction:** Calls `player_game.set_player_location(location)`.

#### **Character Events (Legacy)**

*Note: These events are primarily used in the introductory chapters (1-4) and are considered legacy. Later chapters use different narrative mechanics for character introductions.*

*   **`player_character_join`**
    *   **Behavior:** Adds a new, randomly selected playable character to the player's party from the pool of available recruits.
    *   **`player_game` Interaction:** Calls `player_game.add_random_player_character()`.

*   **`create_character_npc`**
    *   **Behavior:** Creates a temporary NPC version of a potential party member for an introductory scene.
    *   **`player_game` Interaction:** Calls `player_game.add_character_npc(position)`.

---

### Step 3: Map Event Types

From `task_completion_service.py`, valid event types:

#### NPC Events
```python
{ 'event_type': 'create_npc', 'params': { 'npc_id': 'npc_name', 'location': 'region_city_inn' }}
{ 'event_type': 'show_npc', 'params': { 'npc_id': 'npc_name', 'location': 'region_city_bar' }}
{ 'event_type': 'hide_npc', 'params': { 'npc_id': 'npc_name' }}
{ 'event_type': 'set_npc_met', 'params': { 'npc_id': 'npc_name' }}
{ 'event_type': 'set_npc_standing_text', 'params': { 'npc_id': 'npc_name', 'standing_text': ['line1', 'line2'] }}
```

#### Dialog Events
```python
{ 'event_type': 'initiate_dialog', 'params': { 'npc_id': 'npc_name', 'dialog_id': 'dialog_id' }}
{ 'event_type': 'initiate_character_dialog', 'params': { 'npc_id': 'character_name', 'dialog_id': 'dialog_id' }}
```

#### Item Events
```python
{ 'event_type': 'award_item', 'params': { 'item_id': 'item_name' }}
{ 'event_type': 'remove_item', 'params': { 'item_id': 'item_name' }}
{ 'event_type': 'award_money', 'params': { 'amount': 100 }}
```

#### Dungeon Events
```python
{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'dungeon_name', 'location': 'region_open_area' }}
{ 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': 'dungeon_name', 'location': 'entrance' }}
{ 'event_type': 'remove_player_from_dungeon', 'params': { 'dungeon_id': 'dungeon_name' }}
{ 'event_type': 'lock_dungeon', 'params': { 'dungeon_id': 'dungeon_name' }}
{ 'event_type': 'unlock_dungeon', 'params': { 'dungeon_id': 'dungeon_name' }}
{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'dungeon_name', 'item_id': 'item_name', 'location': 'final_chamber' }}
{ 'event_type': 'dungeon_add_npc', 'params': { 'dungeon_id': 'dungeon_name', 'npc_id': 'npc_name', 'location': 'corridor' }}
{ 'event_type': 'set_dungeon_locked_text', 'params': { 'dungeon_id': 'dungeon_name', 'locked_text': 'You cannot enter yet.' } }
```

#### Combat Events
```python
{ 'event_type': 'begin_combat', 'params': { 'boss_mob_id': 'enemy_name_1', 'combat_type': 'boss_battle' }}
```

#### Task Events
```python
{ 'event_type': 'award_task', 'params': { 'task_id': 'task_id_name' }}
{ 'event_type': 'cancel_task', 'params': { 'task_id': 'task_id_name' }}
{ 'event_type': 'remove_task', 'params': { 'task_id': 'task_id_name' }}
```

#### Character Events
```python
{ 'event_type': 'character_join', 'params': { 'character_id': 'character_name' }}
{ 'event_type': 'player_character_join', 'params': { 'dialog_id': 'join_dialog_id', 'is_final_character': True }}
```

#### Party Events
```python
{ 'event_type': 'set_player_location', 'params': { 'location': 'region_city_open_area' }}
```

#### Progression Events
```python
{ 'event_type': 'advance_chapter' }
{ 'event_type': 'complete_intro_story' }
{ 'event_type': 'complete_region_quest', 'params': { 'region_id': 'desert' }}
{ 'event_type': 'unlock_npc_log' }
```

#### Airship Events
```python
{ 'event_type': 'set_aircraft', 'params': { 'location': 'region_city_open_area' }}
{ 'event_type': 'can_aircraft_fly', 'params': { 'can_fly': True }}
{ 'event_type': 'allow_ocean_flight' }
```

#### World Events - hyypertravel is un/locked in later chapters when the player is given/removed the bracelet_of_void
```python
{ 'event_type': 'remove_ocean' }
{ 'event_type': 'unlock_hypertravel' }
{ 'event_type': 'lock_hypertravel' }
```


---

### Step 3b: Event Conditions

Any event in `task_acquire_events` or `task_complete_events` can carry an optional `condition` key.  When present, `handle_task_event` evaluates the condition against the live game state **before** executing the event.  If the condition is not met the event is **silently skipped** and the rest of the chain continues normally.

#### Syntax

{
    'event_type': 'award_item',
    'params': { 'item_id': 'silver_key' },
    'condition': {
        'type': 'is_task_completed',
        'params': { 'task_id': 'ch3_open_vault' }
    }
}


#### Available Condition Types

All types are defined in `TaskEventConditionType` (`task.py`).

##### Task State

# True if the named task exists and is marked completed
{ 'type': 'is_task_completed', 'params': { 'task_id': 'ch1_meet_kirn' }}

# True if the named task exists and is NOT yet completed
{ 'type': 'is_task_active', 'params': { 'task_id': 'ch1_meet_kirn' }}

# True if the named task is absent or already completed (not currently active)
{ 'type': 'is_task_not_active', 'params': { 'task_id': 'ch1_meet_kirn' }}


##### Inventory / Economy

# True if player holds at least 1 unit of the item
{ 'type': 'has_item', 'params': { 'item_id': 'bracelet_of_void' }}

# True if player has at least the given amount of gold
{ 'type': 'has_money', 'params': { 'amount': 500 }}

##### NPC State

# True if the NPC has been met (npc.met == True)
{ 'type': 'is_npc_met',     'params': { 'npc_id': 'velka' }}

# True if the NPC has NOT yet been met
{ 'type': 'is_npc_not_met', 'params': { 'npc_id': 'velka' }}


##### World / Progression
# True if player_game.intro_complete is True
{ 'type': 'is_intro_complete', 'params': {} }

# True if current_chapter >= the given value
{ 'type': 'is_chapter_gte', 'params': { 'chapter': 5 }}

# True if current_chapter <= the given value
{ 'type': 'is_chapter_lte', 'params': { 'chapter': 7 }}

#### Rules

1. Conditions are **per-event**, not per-task.  Different events within the same task can have different (or no) conditions.
2. An unconditional event always fires.  Only add a `condition` key when branching is needed.
3. If a condition type is unrecognised at runtime, the event is skipped and a debug prompt is raised — treat this as a bug.
4. Conditions do **not** chain (no `AND` / `OR` at the seed level).  If multiple conditions are needed, split the logic across separate tasks or use the most restrictive single condition.

#### Example: Conditional Dialog Branch

# Show a different line if the player already completed a side quest
{ 'event_type': 'initiate_dialog',
  'params': { 'npc_id': 'kirn', 'dialog_id': 'kirn_ch5_post_sidequest' },
  'condition': { 'type': 'is_task_completed', 'params': { 'task_id': 'desert_sidequest_final' }}},

{ 'event_type': 'initiate_dialog',
  'params': { 'npc_id': 'kirn', 'dialog_id': 'kirn_ch5_default' },
  'condition': { 'type': 'is_task_not_active', 'params': { 'task_id': 'desert_sidequest_final' }}},

---


### Step 4: Location Reference System

Locations use a hierarchical naming convention:

#### City-Based Locations
```python
'region_city_inn'   # Inn in current region's city
'region_city_bar'        # Bar in current region's city
'region_city_shopitems'     # Item shop
'region_city_shopweapons'   # Weapon shop
'region_city_shoparmor'     # Armor shop
'region_city_open_area'     # Open area near city
'region_city_district'      # City district (for dungeons)
'region_open_area'          # Region wilderness
```

#### Numbered City References - city_number is the chapter number of that city... chapter 1 city is city_number_1, chapter 5 city is city_number_5, etc.
```python
'city_number_2_region_city_inn'        # Inn in 2nd city
'city_number_3_region_open_area'    # Open area near 3rd city
```

#### Region-Specific References - review D:\dev\source\repos\AITextAdventure\AITextAdventureAPI\old\game\region_seeds\regions\cities\README.md for the Complete City List
```python
'desert_large_city_region_city_inn'  # Inn in desert's large city
'forest_mid_city_region_open_area'# Open area near forest's mid city
```

---

### Step 5: Python File Structure Template

```python
# ============================================================
# = CHAPTER [X] : [CHAPTER NAME]
# ============================================================
#
# [ LOCATION — DESCRIPTION ]
# -----------------------------------
# @ = player
# [NPC Letters] = [NPC Names and roles]
#
# High level: [Brief chapter summary]

ATTAINABLE_PLAYER_CHARACTERS = [
    # Add character dicts if any characters join this chapter
]

NPCS = [
    {
        'npc_id': 'npc_name',
    'name': 'Display Name',
        'description': (
   'Multi-line description.'
     ' Second line of description.'
        ),
        "psychology": {
         "mbti": "INTJ",
     "dominant": "Ni — Description",
            "auxiliary": "Te — Description",
  "tertiary": "Fi — Description",
    "inferior": "Se — Description"
        }
    }
]

NPC_DIALOG = [
    {
        'npc_id': 'npc_name',
        'dialog_id': 'dialog_id',
        'dialog': [
        "First line of dialog.",
      "Second line of dialog."
        ]
    }
]

TASKS = [
    {
        'task_id': 'main_story_ch[X]_task_name',
        'type': 'meet',  # or deliver, fetch, defeat, goto, etc.
    'to_type': 'npc',  # or mob, coordinates
        'to_id': 'npc_name',  # or mob_name, or [x, y, z]
        'item_id': 'item_name',  # Only for deliver/fetch tasks
        'task_acquire_events': [
         # Events that trigger when task is acquired
  ],
        'task_complete_events': [
     # Events that trigger when task is completed
      ]
    }
]

PRIMARY_STORY_SETTINGS = {
    'chapter_id': 'main_story_chapter_[X]',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
 'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}
```

---

### Step 6: Dialog Extraction Rules

#### From Mermaid Format:
```
Kirn - You're back… good. I was hoping the signal wasn't a fluke.:
Kirn - I placed a tracking sigil on the Bracelet of Existence.:
```

#### To Python Format:
```python
{
 'npc_id': 'kirn',
    'dialog_id': 'kirn_ch5_tracking_signal',
    'dialog': [
        "You're back… good. I was hoping the signal wasn't a fluke.",
        "I placed a tracking sigil on the Bracelet of Existence."
    ]
}
```

**Rules:**
1. Remove colons at end of dialog lines
2. Group consecutive lines from same speaker into single dialog entry
3. Use `None` for `npc_id` if narrator/environment text
4. Generate unique `dialog_id` using pattern: `[npc_id]_ch[X]_[context]`
5. Character reactions use `[character_type]_ch[X]_[context]` pattern

---

### Step 7: MBTI Psychology Integration

All NPCs require MBTI psychology profiles following this structure:

```python
"psychology": {
    "mbti": "INTJ",  # 4-letter type
    "dominant": "Ni — Primary cognitive function description",
  "auxiliary": "Te — Secondary cognitive function description",
    "tertiary": "Fi — Tertiary cognitive function description",
  "inferior": "Se — Inferior cognitive function description"
}
```

**Common MBTI Types by Character Role:**

| Role | Type | Typical Traits |
|------|------|----------------|
| Strategic Planner | INTJ | Visionary, systematic, independent |
| Tactician | ENTJ | Commanding, efficient, decisive |
| Analyst | INTP | Logical, innovative, detached |
| Rebel/Fighter | ESTP | Action-oriented, pragmatic, bold |
| Healer/Support | INFJ | Empathetic, insightful, idealistic |
| Warrior | ISTJ | Disciplined, reliable, traditional |
| Sage/Mystic | INFP | Values-driven, introspective, creative |
| Leader | ENFJ | Charismatic, organized, inspiring |

---

### Step 8: Task ID Naming Convention

```
'main_story_ch[X]_[action]_[target]'
```

**Examples:**
- `main_story_ch5_return_to_kirn`
- `main_story_ch5_meet_velka`
- `main_story_ch5_retrieve_stormglass_ember`
- `main_story_ch5_defeat_riftspawn_aberrant`
- `main_story_ch6_investigate_dorian`

**Rules:**
1. Always prefix with `main_story_ch[X]_`
2. Use snake_case for all parts
3. Action verbs: `meet`, `defeat`, `deliver`, `retrieve`, `investigate`, `report`, `discover`
4. Keep concise but descriptive

---

### Step 9: Event Parameter Patterns

#### Create NPC Pattern
```python
{
    'event_type': 'create_npc',
    'params': {
        'npc_id': '[npc_id]',
    'location': '[location_reference]'  # or None for dungeon NPCs
    }
}
```

#### Begin Combat Pattern
```python
{
    'event_type': 'begin_combat',
    'params': {
        'boss_mob_id': '[enemy_name]_1',  # Always append _1 for instance
        'combat_type': 'boss_battle'
    }
}
```

#### Award Task Pattern
```python
{
    'event_type': 'award_task',
    'params': {
        'task_id': 'main_story_ch[X]_[next_task_name]'
    }
}
```

---

### Step 10: Character Dialog Reaction System

When translating dialogue from the Mermaid timeline, it is crucial to use the correct `npc_id` for player character reactions. The timeline may use placeholder names, which must be mapped to their official in-game `npc_id`s.

**Player Character ID Mapping:**

| Timeline Name | In-Game `npc_id` | Character Name |
|---------------|------------------|----------------|
| `Chock`       | `technique`      | Chock          |
| `Kade`        | `tech`           | Kade           |
| `Kaera`       | `faith`          | Kaera          |
| `Poise`       | `skill`          | Poise          |
| `Moxie`       | `magic`          | Moxie          |

Use the `npc_id` from this table when creating `initiate_character_dialog` events.

Player characters react to events based on their personality types:
```python
# Technique (ESTP) - Bold, direct, action-oriented
{
 'npc_id': 'technique',
    'dialog_id': 'technique_ch5_after_kirn',
'dialog': ["If it screams, I punch it. Simple."]
}

# Tech (INTP) - Analytical, sarcastic, logical
{
    'npc_id': 'tech',
    'dialog_id': 'tech_ch5_after_kirn',
    'dialog': ["Please don't punch the signal. Or do. I'm curious what happens."]
}

# Magic (ENTP) - Playful, chaotic, curious
{
    'npc_id': 'magic',
    'dialog_id': 'magic_ch5_after_kirn',
    'dialog': ["Ooooh, a ghost signal. I hope it screams."]
}

# Faith (INFJ) - Spiritual, empathetic, idealistic
{
    'npc_id': 'spirit',
    'dialog_id': 'faith_ch5_after_velka',
 'dialog': ["Then we must find someone who can cross storms without crossing the sea."]
}

# Skill (ISTJ) - Disciplined, calm, precise
{
    'npc_id': 'skill',
 'dialog_id': 'skill_ch5_after_velka',
    'dialog': ["Storms that tear reality apart… sounds like a warm?up."]
}
```

---

### Step 11: Special Task Types

#### Complete Intro Story (Gate)
```python
{
    'task_id': 'main_story_ch4_defeat_catalyst',
    'type': 'defeat',
    'to_type': 'mob',
    'to_id': 'catalyst_1',
    'task_acquire_events': [...],
    'task_complete_events': [
    { 'event_type': 'complete_intro_story' },
        { 'event_type': 'advance_chapter' }
    ]
}
```

#### Complete Regional Quests (Gate)
```python
{
    'task_id': 'main_story_ch7_await_regional_completion',
    'type': 'complete_regional_quests',
    'to_type': 'npc',
    'to_id': 'seth',
    'task_acquire_events': [...],
    'task_complete_events': [
        { 'event_type': 'can_aircraft_fly', 'params': { 'can_fly': True }},
        { 'event_type': 'advance_chapter' }
    ]
}
```

---

### Step 12: Chapter Progression Flow

Every chapter should follow this pattern:

1.  **Initial Task and Chapter Setup:** The first task of a chapter (e.g., `meet_npc`, `deliver_item`) is acquired automatically when the previous chapter's `advance_chapter` event fires. **All setup logic for the new chapter must be placed in the `ACQUIRED` block of this first task.** This includes creating/showing NPCs, setting initial standing text, and displaying introductory narrator dialogue.
    *   **CORRECT:** The `ACQUIRED` block of `TASK - Meet Twin Envoys of Stigma` contains all the `create_npc` and `show_npc` events.
    *   **INCORRECT:** Creating a separate `TASK - Setup Chapter [X] - Event:` to handle setup. This is an anti-pattern and should be avoided. All setup events should be consolidated into the first real task.
2.  **Interconnected Tasks:** The player progresses through a chain of tasks. The completion of one task triggers events and dialogue, which typically culminates in an `award_task` event for the next objective.
3.  **Task Completion and Dialogue Flow:** A single task completion can trigger a long, continuous sequence of dialogue and events. A new task should only be awarded when the player is given a new, distinct objective (e.g., meet a new person, find an item, defeat an enemy). Do not split up a continuous story sequence into multiple tasks.
4.  **Final Task and Chapter Advancement:** The final task of a chapter will conclude with an `advance_chapter` event in its `COMPLETED` block, which begins the cycle anew for the next chapter.

**Example Flow:**
```python
# Chapter X final task
'task_complete_events': [
    { 'event_type': 'initiate_dialog', 'params': {...} },
    { 'event_type': 'advance_chapter' }  # This triggers Chapter X+1
]
```

---

### Step 13: Dungeon Integration

When a task involves a dungeon:

```python
# Create dungeon
{
  'event_type': 'create_dungeon',
    'params': {
      'dungeon_id': '[dungeon_name]',
     'location': '[location_reference]'
    }
}

# Place player in dungeon
{
    'event_type': 'set_player_in_dungeon',
    'params': {
        'dungeon_id': '[dungeon_name]',
    'location': 'entrance'  # or 'corridor', 'final_chamber'
    }
}

# Remove player from dungeon (after completion)
{
    'event_type': 'remove_player_from_dungeon',
    'params': {
        'dungeon_id': '[dungeon_name]'
    }
}
```

---

### Step 14: Boss Fight Pattern

Standard boss encounter structure:

```python
# Task 1: Meet the boss (triggers dialog)
{
    'task_id': 'main_story_ch[X]_meet_[boss]',
    'type': 'meet',
    'to_type': 'npc',
    'to_id': '[boss_name]',
    'task_acquire_events': [],
    'task_complete_events': [
        { 'event_type': 'initiate_dialog', 'params': { 'npc_id': '[boss_name]', 'dialog_id': '[boss]_intro' }},
      { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch[X]_defeat_[boss]' }}
    ]
}

# Task 2: Defeat the boss (combat)
{
    'task_id': 'main_story_ch[X]_defeat_[boss]',
    'type': 'defeat',
    'to_type': 'mob',
    'to_id': '[boss_name]_1',
    'task_acquire_events': [
        { 'event_type': 'begin_combat', 'params': { 'boss_mob_id': '[boss_name]_1', 'combat_type': 'boss_battle' }}
    ],
    'task_complete_events': [
        { 'event_type': 'hide_npc', 'params': { 'npc_id': '[boss_name]' }},
        { 'event_type': 'remove_player_from_dungeon', 'params': { 'dungeon_id': '[dungeon_name]' }},
        { 'event_type': 'award_item', 'params': { 'item_id': '[reward_item]' }},
        { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch[X]_next_task' }}
    ]
}
```

---

### Step 15: Validation Checklist

Before finalizing a chapter file, verify:

- [ ] **File Structure**: Matches template exactly
- [ ] **Chapter ID**: Correct in `PRIMARY_STORY_SETTINGS`
- [ ] **Task IDs**: Follow naming convention `main_story_ch[X]_[action]_[target]`
- [ ] **Dialog IDs**: Follow pattern `[npc_id]_ch[X]_[context]`
- [ ] **Task Types**: Only use valid types from `task.py`
- [ ] **Event Types**: Only use valid types from `task_completion_service.py`
- [ ] **NPC Psychology**: All NPCs have complete MBTI profiles
- [ ] **Location References**: Use correct location naming system
- [ ] **Task Chain**: Each task properly awards next task
- [ ] **Chapter Transition**: Final task includes `advance_chapter` event
- [ ] **Dialog Format**: No colons at end of dialog lines
- [ ] **Boss Fights**: Follow two-task pattern (meet ? defeat)
- [ ] **Character Reactions**: Include appropriate player character dialog
- [ ] **Item Handling**: Proper `award_item` and `remove_item` events
- [ ] **Event Conditions**: Any `condition` key uses a valid type from `TaskEventConditionType`; `params` match the expected shape for that type

---

## Common Patterns Reference

### Pattern 1: Simple NPC Meeting
```python
{
    'task_id': 'main_story_ch[X]_meet_[npc]',
    'type': 'meet',
    'to_type': 'npc',
    'to_id': '[npc_id]',
    'task_acquire_events': [
     { 'event_type': 'create_npc', 'params': { 'npc_id': '[npc_id]', 'location': '[location]' }}
    ],
    'task_complete_events': [
      { 'event_type': 'initiate_dialog', 'params': { 'npc_id': '[npc_id]', 'dialog_id': '[npc]_intro' }},
      { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch[X]_next_task' }}
    ]
}
```

### Pattern 2: Item Delivery
```python
{
    'task_id': 'main_story_ch[X]_deliver_[item]_to_[npc]',
    'type': 'deliver',
    'item_id': '[item_id]',
'to_type': 'npc',
    'to_id': '[npc_id]',
    'task_acquire_events': [],
    'task_complete_events': [
   { 'event_type': 'initiate_dialog', 'params': { 'npc_id': '[npc_id]', 'dialog_id': '[npc]_receives_item' }},
        { 'event_type': 'remove_item', 'params': { 'item_id': '[item_id]' }},
  { 'event_type': 'award_item', 'params': { 'item_id': '[reward_item]' }},
        { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch[X]_next_task' }}
    ]
}
```

### Pattern 3: Dungeon Exploration with Boss
```python
# Enter dungeon task
{
    'task_id': 'main_story_ch[X]_explore_[dungeon]',
    'type': 'meet',
    'to_type': 'special_sublocation',
    'to_id': '[dungeon]_core',
    'task_acquire_events': [
  { 'event_type': 'create_dungeon', 'params': { 'dungeon_id': '[dungeon]', 'location': '[location]' }},
        { 'event_type': 'set_player_in_dungeon', 'params': { 'dungeon_id': '[dungeon]', 'location': 'entrance' }}
    ],
    'task_complete_events': [
        { 'event_type': 'award_task', 'params': { 'task_id': 'main_story_ch[X]_defeat_[boss]' }}
    ]
}
```

### Pattern 4: Character Recruitment
```python
{
    'task_id': 'main_story_ch[X]_recruit_[character]',
 'type': 'meet',
    'to_type': 'npc',
    'to_id': '[character_id]',
    'task_acquire_events': [],
    'task_complete_events': [
     { 'event_type': 'initiate_dialog', 'params': { 'npc_id': '[character_id]', 'dialog_id': '[character]_join' }},
   { 'event_type': 'hide_npc', 'params': { 'npc_id': '[character_id]' }},
     { 'event_type': 'player_character_join', 'params': { 'dialog_id': '[character]_join_dialog', 'is_final_character': True }}
    ]
}
```

---

## Troubleshooting

### Issue: pending_character
**Dialog rules - initiate_dialog**
- The pending_character is an world standing NPC which represents one of the 5 main characters: Chock, Kade, Kaera, Moxie, or Poise. These characters are not yet recruited into the party and are represented as NPCs in the world.
- A pending character intitiate_dialog event will have an npc_id of pending_character. the identifier as 'dialog_id': 'pending_character_ch3_good_where_im_at'. in the dialogs section there must be one of each character for the pending character by npc_id in kade, kaera, moxie, poise, and chock. the dialog_id must be unique for each character and follow the pattern: [character]_ch[X]_[context]. the dialog_id must match the dialog_id in the initiate_dialog event.
- Pending characters are represented in the Timeline as (Pending) {character name} and are triggered after an initiate_dialog event with npc_id=pending_character._

### Issue: twisted_character
**Dialog rules - initiate_character_dialog**
- The pending character drinks a tonic in the story and becomes the twisted character
- if npc_id = twisted_character, the dialog_id must be unique for each character and follow the pattern: [character]_ch[X]_[context]. the dialog_id must match the dialog_id in the initiate_character_dialog event.
- twisted_character outbursts are usually triggered based on story events and the moment. of the 5 characters that can be twisted: kade, kaera, moxie, poise, and chock.  Their twisted dialogs should appear in story at moments they are most stressed.
- Twisted characters are represented in the Timeline as (Twisted) {character name} and are triggered after an initiate_character_dialog event with npc_id=twisted_character.

### Issue: Unicode
**Check:**
- All strings are properly closed with matching quotes
- No special characters that may cause encoding issues (e.g., em dashes, smart quotes)
- Use standard ASCII characters always

### Issue: Task not triggering
**Check:**
- Previous task includes `award_task` event with correct task ID
- Task ID matches exactly (case-sensitive)
- Task type and parameters are valid

### Issue: Dialog not displaying
**Check:**
- Dialog ID exists in `NPC_DIALOG` list
- NPC ID matches exactly
- `initiate_dialog` or `initiate_character_dialog` event is present

### Issue: NPC not appearing
**Check:**
- `create_npc` or `show_npc` event in `task_acquire_events`
- Location reference is valid
- NPC exists in `NPCS` list

### Issue: Chapter not advancing
**Check:**
- Final task includes `advance_chapter` event in `task_complete_events`
- Task completion conditions are met

### Issue: Cancel and Remove Task
**Check:**
- 'cancel_task' is used to complete a task without triggering it's events
- 'remove_task' is used to remove a task from the player's task list without completing it
---

## Version History

- **v1.0** - Initial documentation (Chapters 1-7 complete)
- Future: Will be updated as Acts III-VI are converted

---

## Contact

For questions or issues with the conversion process, refer to:
- `task.py` for task type definitions
- `task_completion_service.py` for event handling
- Existing chapter files (1-7) for reference examples
