# City Timeline Files — Overview & Authoring Guide

## What Are City Timelines?

City Timeline files (`CITY TIMELINE ACT *.mmd`) are Mermaid `timeline` documents that represent the **city-story arcs** for each chapter of the game. They are the city-story counterpart to the main `TIMELINE ACT *.mmd` files and follow the same formatting rules defined in `README.md`.

Each city-story arc is a self-contained regional quest that plays out in the city the player visits during a given chapter. It is independent of the main story but shares the same engine, event system, and task/dialog conventions.

---

## Act-to-Chapter Mapping

Chapter-to-city assignment is defined by `CHAPTER_CITY_ORDER` in:
AITextAdventureAPI/old/game/region_seeds/world_constants.py

Act boundaries are defined by `CONTINENT_COMPOSITION`:
CONTINENT_COMPOSITION = [4, 3, 6, 2, 5, 1]

Each number represents how many chapters belong to that act:

| Act | Chapters | Cities |
|-----|----------|--------|
| I   | 1–4      | desert_large_city, forest_mid_city, grassland_mid_city, mountains_large_city |
| II  | 5–7      | shallows_large_city, snow_small_city, swamp_small_city |
| III | 8–13     | desert_mid_city, desert_small_city, grassland_large_city, shallows_mid_city, grassland_small_city, swamp_large_city |
| IV  | 14–15    | snow_mid_city, shallows_small_city |
| V   | 16–20    | forest_small_city, mountains_mid_city, forest_large_city, snow_large_city, swamp_mid_city |
| VI  | 21       | mountains_small_city |

---

## Source Files

### Input — Python City Story Files
AITextAdventureAPI/old/game/region_seeds/city_stories/{region}/{region}_{size}_city_story.py

Each file exports:
- `NPCS` — NPC definitions
- `NPC_DIALOG` — dialog entries keyed by `npc_id` and `dialog_id`
- `TASKS` — the full task chain including acquire/complete events
- `PRIMARY_STORY_SETTINGS` — the settings dict consumed by the engine

### Output — City Timeline Mermaid Files
AITextAdventureAPI/old/STORY DOCUMENTS FOR AI/CITY TIMELINE ACT I.mmd
AITextAdventureAPI/old/STORY DOCUMENTS FOR AI/CITY TIMELINE ACT II.mmd
... (one file per act)

### Conversion Reference
AITextAdventureAPI/old/STORY DOCUMENTS FOR AI/README.md

All event types, dialog rules, task types, and location conventions defined there apply equally to city timeline files.

---

## City Timeline File Structure

Each file contains one `timeline` block with one `section` per chapter city in that act.

timeline
    title The Fracture Saga - CITY TIMELINE ACT {N} - Chapters {X} to {Y}

    section Chapter {N} - {City Name}
        TASK - City Arrival - Initialize:
            ► ACQUIRED:
                ...NPC creation and standing text events...
                Narrator - Chapter {N} City - {Flavor description}:
            ► COMPLETED:
                EVENT - award_task - {region}_city_meet_{first_npc}

        TASK - Meet {NPC} - NPC:
            ...
        TASK - Find {NPC} - NPC:
            ...
        TASK - Explore {Dungeon} - Dungeon:
            ...
        TASK - Descend into {Dungeon} - Dungeon:
            ...
        TASK - Defeat {Boss} - MOB:
            ► ACQUIRED:
                EVENT - create_dungeon - {boss_dungeon} (region_open_area):
                EVENT - begin_combat - {boss_id}_1 (boss_battle):
            ► COMPLETED:
                {closing NPC dialog lines}:
                EVENT - complete_region_quest - {region_city_id}



---

## City Timeline Rules

### 1. Initialization Task
Every section opens with a **City Arrival - Initialize** task. Its `ACQUIRED` block contains:
- `create_npc` events for the two city NPCs
- `set_npc_standing_text` events with their welcoming lines
- A `Narrator` line providing chapter flavor text

Its `COMPLETED` block awards the first meet task only.

This mirrors the `*_initialize` task found in each Python source file and follows README Step 12: all chapter setup belongs in the first task's `ACQUIRED` block.

### 2. Task Naming
City tasks use the Python task IDs verbatim from the source file (e.g. `shallows_large_city_meet_renlo`). Do not invent new IDs.

### 3. Dialog Extraction
Dialog lines are taken directly from `NPC_DIALOG` entries in the Python source file:
- Remove trailing colons from dialog lines
- Group consecutive lines from the same speaker into one block
- Speaker name matches the NPC's display name, not their `npc_id`

### 4. No `advance_chapter`
City stories end with `complete_region_quest`, **not** `advance_chapter`. City arcs are regional sidequests, not main-story chapter gates.

### 5. Dungeon Task Pattern
Every dungeon task follows this shape:
- `ACQUIRED`: `create_dungeon` + `create_npc (None)` for the dungeon NPC
- `COMPLETED`: dialog from the dungeon NPC, then `award_task` for the next step

### 6. Boss Task Pattern
The final task always has type `MOB`:
- `ACQUIRED`: `create_dungeon` for the boss arena + `begin_combat`
- `COMPLETED`: closing dialog from the first city NPC + `complete_region_quest`

### 7. Marker Style
Use `► ACQUIRED:` and `► COMPLETED:` (with the `►` character), matching the rest of the project's Mermaid conventions.

---

## Completed Files

| File | Act | Chapters | Status |
|------|-----|----------|--------|
| `CITY TIMELINE ACT I.mmd` | I | 1–4 | Complete |
| `CITY TIMELINE ACT II.mmd` | II | 5–7 | Complete |
| `CITY TIMELINE ACT III.mmd` | III | 8–13 | Complete |
| `CITY TIMELINE ACT IV.mmd` | IV | 14–15 | Complete |
| `CITY TIMELINE ACT V.mmd` | V | 16–20 | Complete |
| `CITY TIMELINE ACT VI.mmd` | VI | 21 | Not yet built |

---

## Authoring Checklist

Before finalising a city timeline act file, verify:

- [ ] Section count matches the number of chapters in that act (`CONTINENT_COMPOSITION`)
- [ ] City names match `CHAPTER_CITY_ORDER` (check `world_constants.py`)
- [ ] Task IDs are taken verbatim from the Python source files
- [ ] `ACQUIRED` / `COMPLETED` markers use `►`
- [ ] Every section begins with `City Arrival - Initialize`
- [ ] Dialog lines have no trailing colons
- [ ] Boss tasks end with `complete_region_quest`, not `advance_chapter`
- [ ] `create_npc (None)` is used for dungeon NPCs (not placed on the world map)
- [ ] `begin_combat` always uses `boss_battle` as the combat type
- [ ] Narrator lines are present in the initialization task