# City Story Dungeon Framework

## Overview

Each of the 21 city stories currently has 3 dungeons chained into a single linear quest. This document defines the upgrade framework: those 3 dungeons are **broken apart** into 3 independent quest chains per city, each serving a distinct design purpose.

---

## The Problem

The current structure treats all 3 dungeons as acts of one story. This creates:
- No replay incentive beyond the main throughline
- No meaningful gating or cross-city dependency
- Wasted design space for extended characters, mythic items, and faction callbacks

---

## Quest Chain Types

6 types total. **No slot is locked to a type** — each city's three slots are assigned by fit. Slot 1 = lightest/earliest gated, Slot 3 = hardest/most gated.

| Type | Name | Count | Gate |
|------|------|-------|------|
| A | Chapter Tie-In | 4 | Chapter active (mandatory progression) |
| B | Regional Character Quest | 7 | Chapter 20 Void Gauntlet |
| C | Extended Character Unlock | 16 | City chapter reached |
| D | Mythic Equipment Quest | 21 | E artifact or F faction item delivered |
| E | Artifact Prerequisite Chain | 11 | Chapter reached |
| F | Faction / Recurring NPC Quest | 4 | Per-chain defined |
| | **Total** | **63** | |

---

### Type A — Chapter Tie-In

A quest that intersects directly with the main story chapter of this city. **The player must complete this chain to progress the chapter** — it becomes a mandatory story beat at that exact time and place.

**Requirements:**
- Only on *small* chapters (low task count, no chapter dungeon). See grid.
- The chapter seed must add a task awarding the city quest, required before `advance_chapter`.
- Use only NPCs already in the city. No new NPCs.

**Gating:** Active while the city's chapter is active.

**Confirmed eligible cities (reviewed from seed files):** Ch.6, Ch.7, Ch.12, Ch.18

---

### Type B — Regional Character Quest *(Void Gauntlet Gated)*

Each region's attainable character returns to the most thematically appropriate city in their region and draws the player into a dungeon. Assignment follows narrative fit over city size.

| Region | Regional Character | City (Ch.) | Size |
|--------|--------------------|------------|------|
| Desert | Sable | Nightveil Spire (8) | Mid |
| Mountains | Bragg | Gallows Rift (17) | Mid |
| Shallows | Ripple | Tidekin Cove (14) | Small |
| Grassland | Nia | Crosswind Bazaar (10) | Large |
| Swamp | Grimnaw | The Necropolis (13) | Large |
| Forest | Thorn | Aurelion Veil (18) | Large |
| Snow | Kor-in | Frostgate Spire (19) | Large |

**Requirements:**
- Regional character must already be in the party.
- No new NPC — use `initiate_character_dialog` on the party member.
- Should occupy the hardest dungeon of the three for that city.

**Gating:** Locked until the Chapter 20 Void Gauntlet event.

---

### Type C — Extended Character Unlock

Completing this chain unlocks one of the 16 secret extended characters. The character is the reward at the chain's end, not a guide through it. The extended character may be placed at an appropriate city location and interacted with during the quest.

**Requirements:**
- No additional NPCs beyond the extended character.
- `character_join` is the final `task_complete_event`.

**Gating:** Available once the city's chapter is reached.

| City (Ch.) | Extended Character |
|------------|--------------------|
| Boiling Bubble (2) | Veyr Ashcant |
| Highsteeple Crossing (3) | Regent Sylvara |
| Ironveil Foundry (4) | Spark Maddox |
| Bleakwatch Outpost (6) | Commander Drax |
| Gnashwater Hollow (7) | Ghost |
| Nightveil Spire (8) | Eldon Dawnseer |
| Crosswind Bazaar (10) | Voss Caldera |
| Blackwake Bay (11) | Dare |
| Quantford Hollow (12) | Rynn |
| The Necropolis (13) | Anita |
| Tidekin Cove (14) | Andrea Starveil |
| Thornshade Hamlet (16) | Talon |
| Gallows Rift (17) | Alden Brightvein |
| Frostgate Spire (19) | Lyric |
| Hollerforge Hollow (21) | Lira Emberforge |
| Bayou Nocturne (20) | Osten Dreamweaver |

---

### Type D — Mythic Equipment Quest

This chain leads to a **mythic-tier item** (weapon, armor, or accessory) found nowhere else in the game.

**Requirements:**
- Item must have no other acquisition path.
- **Gating:** A trigger item must first be found inside a chapter dungeon (`dungeon_add_treasure`), then delivered to one of three recipients who unlocks the chain — **Mira** (accessory), **Brawn** (armor), or **Diego** (weapon). Alternatively a Type E artifact may serve as the gate.
- No new NPCs. Use existing city NPCs as quest anchors.

*21 total D chains — every city except Ch.18 (already full A+B+C). Ch.9 carries two.*

---

### Type E — Artifact Prerequisite Chain

A dead-end quest that awards a **named artifact** — not a combat item, not a stat boost. The artifact has no direct gameplay value; it is a required ingredient for a Type D mythic chain elsewhere.

**Rules:**
- Does not unlock characters or award mythic items directly.
- The artifact must be consumed as a requirement by at least one Type D chain. Document it below.
- No new NPCs.
- Can be completed before the player knows they need it — artifact waits in inventory.

**Known artifact dependencies** *(populate as D chains are authored):*
> *(None defined yet)*

---

### Type F — Faction / Recurring NPC Quest

A self-contained chain driven by a **non-party NPC who appears across multiple cities**. Provides narrative variety and gives recurring characters story weight without requiring a party join.

**Requirements:**
- The NPC anchor must already exist in at least one other city or chapter.
- Reward is a **named faction item** (consumable, key item, or cosmetic) or a world-state change visible in a future chapter or city. May also gate a Type D chain.
- No new NPCs beyond the recurring anchor.

**Gating:** Per-chain defined based on the faction thread.

**Known recurring NPC candidates:**

| NPC | Known Appearances | Faction Thread |
|-----|-------------------|----------------|
| Marlo Finch | Ch.4, Ch.16, Ch.20 | Auditor conspiracy — tracking corruption across cities |
| Velka | Ch.4, Ch.18 | Mapping the fracture — cartographic mystery thread |
| Kess Thornwrite | Ch.2, Ch.20 | Alchemical ingredient chain across regions |
| Tess | Ch.2, Ch.9+ | Black market artifact recovery |
| Astra Wynn | Ch.5, Ch.19 | Rift observation posts — revisiting rift sites |
| Seth | Ch.3–Ch.13 | Airship salvage / contraband drops |

> *Expand as F chains are authored. Each entry should include cities visited and the artifact or reward it produces.*

---

## Per-City Dungeon Assignment

Slots ordered 1 → 3 by ascending gate difficulty within each city.

| Ch. |                   City | Region    | Size  | Tasks | Ch.Dung | 1 | 2 | 3 |
|----|-------------------------|-----------|-------|-------|---------|---|---|---|
| 1  | The Desert Metropolis   | Desert    | Large | 11    | Yes     | E | D |#F#| 1d
| 2  | Boiling Bubble          | Forest    | Mid   | 11    | Yes     | E | C | D | 2d 1c
| 3  | Highsteeple Crossing    | Grassland | Mid   | ~8    | Yes     | C | D | E | 3d 2c
| 4  | Ironveil Foundry        | Mountains | Large | ~10   | Yes     | C | D | E | 4d 3c
| 5  | Brineward Harbor        | Shallows  | Large | ~8    | Yes     | E | D |#F#| 5d
| 6  | Bleakwatch Outpost      | Snow      | Small | ~7    | No      |*A*| C | D | 6d 4c
| 7  | Gnashwater Hollow       | Swamp     | Small | 5     | No      |*A*| C | D | 7d 5c
| 8  | Nightveil Spire         | Desert    | Mid   | ~9    | Yes     | C | D | B | 8d 6c *desert regional*
| 9  | BioHazard             | Desert    | Small | ~8    | Yes     | E | D |#F#| 9d
| 10 | Crosswind Bazaar        | Grassland | Large | ~6    | No      | C | D | B | 10d 7c *grass regional*
| 11 | Blackwake Bay           | Shallows  | Mid   | ~10   | No      | E | C | D | 11d 8c
| 12 | Quantford Hollow        | Grassland | Small | ~5    | No      |*A*| C | D | 12d 9c
| 13 | The Necropolis          | Swamp     | Large | ~9    | No      | C | D | B | 13d 10c *swamp regional*
| 14 | Tidekin Cove            | Shallows  | Small | ~9    | No      | C | D | B | 14d 11c *shallows regional*
| 15 | Hailward Hold           | Snow      | Mid   | ~12   | Yes     | E | D |#F#| 15d
| 16 | Thornshade Hamlet       | Forest    | Small | ~8    | No      | E | C | D | 16d 12c
| 17 | Gallows Rift            | Mountains | Mid   | ~10   | No      | C | D | B | 17d 13c *mountains regional*
| 18 | Aurelion Veil           | Forest    | Large | ~4    | No      |*A*| D | B | 18d *forest regional*
| 19 | Frostgate Spire         | Snow      | Large | ~8    | No      | C | D | B | 19d 14c *snow regional*
| 20 | Bayou Nocturne          | Swamp     | Mid   | ~9    | No      | E | D | C | 20d 15c
| 21 | Hollerforge Hollow      | Mountains | Small | Final | Yes     | E | C | D | 21d 16c

**Totals — A: 4 · B: 7 · C: 16 · D: 21 · E: 11 · F: 4 = 63**

> **Ch.9 note:** BioHazard carries one Type E (Slot 1), one Type D (Slot 2), and one Type F (Slot 3) — a pure artifact/equipment/faction hub with no character unlock and no regional B.
>
> **Ch.18 note:** Aurelion Veil is the only city with no Type D — its three slots are fully occupied by the Chapter Tie-In (A), the Forest Regional Quest (B), and the Extended Character Unlock (C), making it the most story-dense city in the game.

A tasks 
- ch 6
- + change seth first dialog a little and instead of directly giving the players to the contact seth wants to get the players to do something for him in the local area.
  + i.e. they interact with the npc from city story line ... add a simple meet task after the initial talk with seth and the offering of contact and awarding meet contact conditionally... the meet task should have seth say ... did you do whatever? then an event with condition on the give contact speech and award next task... and a not complete condition on an event to destroy that delete_task for that task then re-award it so it has a replay loop.
- ch 7
- + replace item from relic to a piece of jewelry that is a family heirloom for lyren. have to remove the relic from being added to dungeon
  + this makes the a task an easy get the item task however that's done is up to the city storyline.
- ch 12
- + ch 12 is easy, the second meet rell event should be changed to a deliver task... his set npc standing text saying how grief torn he is over ember and what he left the players searching for at the beginning of the chapter.
  + the delivery of the item found in the a task chain of the city story will reflect what the players found as an addition at the beggining of the current events dialog
- ch 18
- + Velkas map is far too easily accurate... this is how this a chain will resolve.
  + her meet will become similar to the ch6 conditional task complete structure reawarding itself until the players complete the task, thin that case the conditional award task and dialog

---

## NPC Rules (All Chain Types)

- **Do not create new NPCs for any chain other than the base city story.**
- B, C, D, E, and F must use NPCs already in the city seed, party members, or documented recurring NPCs.
- Tasks may reference NPCs from other cities the player already knows — explicitly allowed for Type A and Type F.

---

---

## Implementation Reference Guide

This section tells an AI agent exactly where to find every resource needed to author city dungeon chains. Read this before writing any chain.

---

### Primary Technical Reference

**`AITextAdventureAPI/old/STORY DOCUMENTS FOR AI/README.md`** is the authoritative guide for:
- All valid task types and their required fields
- All valid event types, their params, and behavioral rules
- Location naming conventions (`region_city_inn`, `city_number_N_...`, etc.)
- Dialog extraction and `dialog_id` naming conventions
- NPC psychology (`mbti`, `dominant`, `auxiliary`, `tertiary`, `inferior`)
- Event conditions (`is_task_completed`, `has_item`, `is_chapter_gte`, etc.)
- Boss fight two-task pattern (`meet` → `defeat`)
- Chapter progression rules and anti-patterns

When in doubt about any seed syntax, consult the README first.

---

### Task ID Convention for City Chains

City story tasks do **not** use the `main_story_ch[X]_` prefix. They use the city bucket key as the prefix:
[region]_[size]_city_[chain_type]_[action]_[target]

**Examples:**
desert_mid_city_type_d_deliver_cipher_shard
forest_large_city_type_c_meet_osten
shallows_large_city_type_b_defeat_void_tide
grassland_mid_city_type_a_meet_sylvara
snow_small_city_type_f_deliver_audit_ledger

The `type_[a-f]_` segment makes the chain type explicit in every task ID, which prevents cross-chain `award_task` accidents.

---

### Finding Existing City NPCs

Each city story seed is the **only** place new NPCs may be defined for that city. Secondary chains (B–F) must use NPCs already there.

**File locations:**
AITextAdventureAPI/old/game/region_seeds/city_stories/[region]/[region]_[size]_city_story.py

**Example:** Desert mid city → `city_stories/desert/desert_mid_city_story.py`

Look at the `NPCS = [...]` list at the top of that file. Every `npc_id` in that list is available. No others.

**Exception — Type B:** Regional characters (`sable`, `thorn`, `nia`, `bragg`, `ripple`, `kor_in`, `grimnaw`) are party members. They require no `create_npc` event — use `initiate_character_dialog` directly.

**Exception — Type C:** The extended character being unlocked may be placed at a city location using `create_npc` as their first appearance. Their `npc_id` and full NPC record come from:
AITextAdventureAPI/old/game/region_seeds/extended_characters.py  →  EXTENDED_CHARACTERS_NPCS

---

### Finding the Chapter Dungeon Seeds (for Type A trigger item placement)

Type D chains require a trigger item to be placed inside a chapter dungeon via `dungeon_add_treasure`. To find which dungeons exist in a chapter:

1. Open the chapter file:
   AITextAdventureAPI/old/game/region_seeds/main_story/main_story_chapter_[N].py
2. Search for `create_dungeon` events — these are the dungeons active in that chapter.
3. Choose the most thematically appropriate dungeon and add:
    { 'event_type': 'dungeon_add_treasure',
     'params': { 'dungeon_id': '[dungeon_id]', 'item_id': '[trigger_item_id]', 'location': 'final_chamber' }}
This event goes in the `task_complete_events` of the chapter task that creates or enters that dungeon.

**Note:** The trigger item must be invented (it does not exist yet). Name it descriptively:  
`[region]_[size]_city_[type_d_reward_type]_key` — e.g., `desert_mid_city_armor_key`, `shallows_large_city_accessory_key`.

---

### Finding Items and Equipment

**Existing items:**
AITextAdventureAPI/old/game/region_seeds/weapons/
AITextAdventureAPI/old/game/region_seeds/armor/
AITextAdventureAPI/old/game/constants.py  →  ITEMS dict

**For Type D mythic items:** These do not yet exist — they must be designed and seeded. The item dict belongs in `constants.py` under `ITEMS`. Name mythic items with a `mythic_` prefix:

mythic_[region]_[size]_[weapon|armor|accessory]_[name]

Example: `mythic_desert_mid_void_index_codex` (accessory)

**Deliver quest recipients:**
- **Mira** — accessories. She appears in Ch.2 (Boiling Bubble). `npc_id: 'mira'`
- **Brawn** — armor. `npc_id: 'brawn'` (travels with party from Ch.1)
- **Diego** — weapons. Locate Diego's `npc_id` and city from the chapter files before assigning.

The deliver quest that gates a Type D chain is a **separate standalone task** awarded when the player picks up the trigger item. It is not part of the dungeon chain itself.

---

### Finding Recurring NPCs for Type F

Cross-reference the F candidates table in the Quest Chain Types section with actual chapter appearances:

| NPC | Find them in |
|-----|--------------|
| Marlo Finch | `main_story_chapter_4.py`, `main_story_chapter_16.py`, `main_story_chapter_20.py` |
| Velka | `main_story_chapter_4.py`, `main_story_chapter_18.py` |
| Kess Thornwrite | `main_story_chapter_2.py`, `main_story_chapter_20.py` |
| Tess | `main_story_chapter_2.py` and city stories |
| Astra Wynn | `main_story_chapter_5.py`, `main_story_chapter_19.py` |
| Seth | `main_story_chapter_3.py` through `main_story_chapter_13.py` |

For each F chain, read the NPC's existing dialog in those files to stay consistent with their established voice and role before writing new dialog.

---

### Updating a Chapter Seed for Type A

When a city is assigned Type A, the corresponding chapter file **must** be updated. The process:

1. Open `main_story_chapter_[N].py`
2. Find the final task — the one with `advance_chapter` in `task_complete_events`
3. **Before** `advance_chapter`, insert:
   { 'event_type': 'award_task', 'params': { 'task_id': '[region]_[size]_city_type_a_[first_task]' }}
4. Move `advance_chapter` into the city chain's final task `task_complete_events` instead. The chapter does not advance until the city quest is done.
5. Add a `condition` guard on any existing chapter-endingdialog that should not fire until the city quest completes:
   'condition': { 'type': 'is_task_completed', 'params': { 'task_id': '[region]_[size]_city_type_a_[final_task]' }}

**Type A eligible chapters** (confirmed small): Ch.6, Ch.7, Ch.10, Ch.12, Ch.18

---

### Finding NPC Dialog Voice Reference

Before writing any NPC dialog, read the existing `NPC_DIALOG` entries for that NPC in their city story file and in any chapter file where they appear. Match vocabulary, sentence rhythm, and thematic concerns exactly.

For extended characters (Type C), their personality profiles are in:
AITextAdventureAPI/old/game/region_seeds/extended_characters.py  →  EXTENDED_CHARACTERS_NPCS

Each entry has a full `psychology` block (MBTI + enneagram). Write their dialog to match their `dominant` cognitive function.

For regional characters (Type B), their profiles are in:
AITextAdventureAPI/old/game/region_seeds/main_characters.py  →  ATTAINABLE_PLAYER_CHARACTERS equivalent
AITextAdventureAPI/old/STORY DOCUMENTS FOR AI/ATTAINABLE CHARACTERS.txt


---

### City Story File Structure Reference

A complete city story file follows this shape (use `desert_mid_city_story.py` as the canonical example):

ATTAINABLE_PLAYER_CHARACTERS = []   # populated only if a character joins in base story
NPCS = [...]                        # all NPCs that exist in this city
NPC_DIALOG = [...]                  # all dialog entries for those NPCs
TASKS = [...]                       # the base city quest chain
PRIMARY_STORY_SETTINGS = {
    'story_id': '[region]_[size]_city_story',
    'tasks': TASKS,
    'npcs': NPCS,
    'npc_dialog': NPC_DIALOG,
    'attainable_player_characters': ATTAINABLE_PLAYER_CHARACTERS,
}

Secondary chains (B–F) are added as additional `TASKS +=` blocks and their dialogs as additional `NPC_DIALOG +=` blocks in the **same file**. Each independent chain must be clearly comment-separated.

> ⚠️ **AUTHORING RULE — No old linear chains:** The original city story files contain a base linear quest chain. **These must be completely removed during the rewrite.** Keep only `initialize` and `regional_complete_gate` (or equivalent). Everything after them is replaced by the 3 typed chain slots. Do not append typed chains on top of old linear chains.

> ⚠️ **AUTHORING RULE — No `create_dungeon` in E or F chains:** Type E and Type F chains are fully NPC-driven. NPCs are placed at `region_open_area` or existing city locations via `create_npc`. No `create_dungeon` events belong in E or F chains. Dungeon events are reserved for Type B and Type D chains only.

**Each independent chain must be clearly comment-separated:**
---

## Build Order & Dependency Chart

### Why Build Order Matters

D chains cannot be authored until their gate is defined. C chains reference extended character profiles. B chains require the Ch.20 Void Gauntlet event. A chains require chapter seed surgery. **E and F chains have no prerequisites — they must be authored first**, because their artifact/faction item IDs become hard references in every downstream chain's condition or deliver event.

**Build in this sequence:**

| Phase | Type | Reason |
|-------|------|--------|
| 1 | **E** — all 11 | No prerequisites. Produces artifact IDs referenced by D chains. |
| 2 | **F** — all 4 | No prerequisites. Produces faction item IDs referenced by D chains. |
| 3 | **D** — all 21 | Requires E artifact or F item IDs from Phase 1/2. Requires trigger item seeded in chapter dungeon (`dungeon_add_treasure`). |
| 4 | **C** — all 16 | Requires extended character profile from `extended_characters.py`. No item dependencies. |
| 5 | **B** — all 7 | Requires Ch.20 Void Gauntlet event to exist in `main_story_chapter_20.py`. Requires regional character party profiles. |
| 6 | **A** — all 4 | Requires chapter seed surgery (`advance_chapter` migration). Must be last to avoid breaking active chapter flow during development. |

---

### E → D Dependency Map

Each E artifact is a named collectible that gates a specific D chain in another city (or the same city for same-city pairs). The artifact is consumed as a `has_item` condition on the D chain's first task, or as a deliver quest to Mira/Brawn/Diego.

| E Source City (Ch.) | Artifact Name *(placeholder — refine during authoring)* | → Gates D at | Target City (Ch.) | Region Logic |
|---|---|---|---|---|
| The Desert Metropolis (1) | Dune Cipher Stone | → | The Desert Metropolis (1) | Same city — Slot 1 unlocks Slot 2 |
| Boiling Bubble (2) | Mycelia Memory Spore | → | Thornshade Hamlet (16) | Forest region cross — early herb → late hamlet |
| Highsteeple Crossing (3) | Sanctum Seal Fragment | → | Crosswind Bazaar (10) | Grassland region cross — sanctum relic → trade hub |
| Ironveil Foundry (4) | Forge Echo Core | → | Gallows Rift (17) | Mountains region cross — foundry → mid-mountain dungeon |
| Brineward Harbor (5) | Brine Compass | → | Brineward Harbor (5) | Same city — Slot 1 unlocks Slot 2 |
| BioHazard (9) | Eroded Ledger Plate | → | BioHazard (9) | Same city — Slot 1 unlocks Slot 2 |
| Blackwake Bay (11) | Tidekin Seal | → | Tidekin Cove (14) | Shallows region cross — mid harbor → small cove |
| Hailward Hold (15) | Pageant Decree Shard | → | Hailward Hold (15) | Same city — Slot 1 unlocks Slot 2 |
| Thornshade Hamlet (16) | Thornshade Root Graft | → | Boiling Bubble (2) | Forest region retroactive — player returns to Ch.2 city |
| Bayou Nocturne (20) | Bayou Memory Vessel | → | Gnashwater Hollow (7) | Swamp region retroactive — player returns to Ch.7 city |
| Hollerforge Hollow (21) | Dominion Fragment | → | Hollerforge Hollow (21) | Same city — Slot 1 unlocks Slot 3 |

> **Retroactive gates (Ch.16→Ch.2, Ch.20→Ch.7):** The player returns to an early-game city with a late-game artifact to unlock a dungeon that was always there but previously inaccessible. This rewards exploration and creates a reason to revisit early cities in endgame.

---

### F → D Dependency Map

Each F faction item is the reward of a recurring NPC quest chain. It gates a D chain in a thematically connected city.

| F Source City (Ch.) | Recurring NPC | Faction Item Name *(placeholder)* | → Gates D at | Target City (Ch.) | Connection |
|---|---|---|---|---|---|
| The Desert Metropolis (1) | Seth | Seth's Salvage Manifest | → | Highsteeple Crossing (3) | Seth is active in Ch.3; his contraband trail leads there |
| Brineward Harbor (5) | Astra Wynn | Rift Observation Log | → | Frostgate Spire (19) | Astra reappears in Ch.19; log connects both rift sites |
| BioHazard (9) | Tess | Contraband Registry | → | Bleakwatch Outpost (6) | Tess's black market network; Bleakwatch is a frontier hub |
| Hailward Hold (15) | Marlo Finch | Audit Testimony Seal | → | Bayou Nocturne (20) | Marlo reappears in Ch.20; audit trail concludes there |

---

### Standard Trigger Item Map (D chains with no E/F dependency)

These 6 D chains are gated only by a trigger item found in a chapter dungeon and delivered to Mira, Brawn, or Diego. The trigger item must be seeded via `dungeon_add_treasure` in the specified chapter dungeon.

| D Target City (Ch.) | Trigger Item Name *(placeholder)* | Source Chapter Dungeon | Deliver To | Mythic Type |
|---|---|---|---|---|
| Ironveil Foundry (4) | Foundry Resonance Key | Ch.4 chapter dungeon | Brawn | Armor |
| Nightveil Spire (8) | Ink Resonance Vial | Ch.8 chapter dungeon | Mira | Accessory |
| Blackwake Bay (11) | Corsair Tide Fragment | Ch.5 chapter dungeon *(nearest Shallows dungeon)* | Diego | Weapon |
| Quantford Hollow (12) | Hollow Grief Token | Ch.3 chapter dungeon *(nearest Grassland dungeon)* | Mira | Accessory |
| The Necropolis (13) | Necropolis Marrow Shard | Ch.9 chapter dungeon *(nearest available)* | Diego | Weapon |
| Aurelion Veil (18) | Veil Memory Leaf | Ch.2 chapter dungeon *(Forest region)* | Mira | Accessory |

> **No-dungeon chapter sourcing:** For D chains whose chapter has no dungeon (Ch.11, 12, 13, 18), the trigger item is placed in the nearest same-region chapter dungeon. When authoring, verify the source dungeon still exists in the player's active game state at the chapter where the D chain becomes available.

---

### Full Dependency Summary (All 21 D Chains)

| D City | Ch. | Slot | Gated By | Gate Source |
|--------|-----|------|----------|-------------|
| The Desert Metropolis | 1 | 2 | E artifact | Ch.1 E — Dune Cipher Stone |
| Boiling Bubble | 2 | 3 | E artifact | Ch.16 E — Thornshade Root Graft *(retroactive)* |
| Highsteeple Crossing | 3 | 2 | F item | Ch.1 F — Seth's Salvage Manifest |
| Ironveil Foundry | 4 | 2 | Trigger item | Ch.4 dungeon → Brawn |
| Brineward Harbor | 5 | 2 | E artifact | Ch.5 E — Brine Compass |
| Bleakwatch Outpost | 6 | 3 | F item | Ch.9 F — Contraband Registry |
| Gnashwater Hollow | 7 | 3 | E artifact | Ch.20 E — Bayou Memory Vessel *(retroactive)* |
| Nightveil Spire | 8 | 2 | Trigger item | Ch.8 dungeon → Mira |
| BioHazard | 9 | 2 | E artifact | Ch.9 E — Eroded Ledger Plate |
| Crosswind Bazaar | 10 | 2 | E artifact | Ch.3 E — Sanctum Seal Fragment |
| Blackwake Bay | 11 | 3 | Trigger item | Ch.5 dungeon → Diego |
| Quantford Hollow | 12 | 3 | Trigger item | Ch.3 dungeon → Mira |
| The Necropolis | 13 | 2 | Trigger item | Ch.9 dungeon → Diego |
| Tidekin Cove | 14 | 2 | E artifact | Ch.11 E — Tidekin Seal |
| Hailward Hold | 15 | 2 | E artifact | Ch.15 E — Pageant Decree Shard |
| Thornshade Hamlet | 16 | 3 | E artifact | Ch.2 E — Mycelia Memory Spore |
| Gallows Rift | 17 | 2 | E artifact | Ch.4 E — Forge Echo Core |
| Aurelion Veil | 18 | 2 | Trigger item | Ch.2 dungeon → Mira |
| Frostgate Spire | 19 | 2 | F item | Ch.5 F — Rift Observation Log |
| Bayou Nocturne | 20 | 2 | F item | Ch.15 F — Audit Testimony Seal |
| Hollerforge Hollow | 21 | 3 | E artifact | Ch.21 E — Dominion Fragment |

---

### Key Reference IDs

When authoring any chain, use these IDs exactly — they are referenced across multiple files.

**E artifact item IDs:**

desert_large_city_e_dune_cipher_stone
forest_mid_city_e_mycelia_memory_spore
grassland_mid_city_e_sanctum_seal_fragment
mountains_large_city_e_forge_echo_core
shallows_large_city_e_brine_compass
desert_small_city_e_eroded_ledger_plate
shallows_mid_city_e_tidekin_seal
snow_mid_city_e_pageant_decree_shard
forest_small_city_e_thornshade_root_graft
swamp_mid_city_e_bayou_memory_vessel
mountains_small_city_e_dominion_fragment

**F faction item IDs:**
desert_large_city_f_salvage_manifest
shallows_large_city_f_rift_observation_log
desert_small_city_f_contraband_registry
snow_mid_city_f_audit_testimony_seal

**Standard trigger item IDs:**
mountains_large_city_d_foundry_resonance_key
desert_mid_city_d_ink_resonance_vial
shallows_mid_city_d_corsair_tide_fragment
grassland_small_city_d_hollow_grief_token
swamp_large_city_d_necropolis_marrow_shard
forest_large_city_d_veil_memory_leaf

---

## City Story Gate Reference

Before authoring any secondary chain, you must identify which gate pattern the city uses. Secondary chain `award_task` events are **not** self-contained — they must be triggered from within the city's existing task chain at the correct unlock point.

### Gate Pattern A — `complete_regional_quests` gate (e.g. desert_large_city)

Some cities have an explicit `complete_regional_quests` task as their second task. The secondary chains are awarded from this task's `task_complete_events`, each with their own gating condition:
# In desert_large_city_regional_complete_gate task_complete_events:
{ 'event_type': 'award_task', 'params': { 'task_id': 'desert_large_city_meet_kadeem' }},  # base story
{ 'event_type': 'award_task', 'params': { 'task_id': 'desert_large_city_type_e_...' }},   # E chain (no extra gate)
{ 'event_type': 'award_task',                                                              # C chain
  'params': { 'task_id': 'desert_large_city_type_c_...' },
  'condition': { 'type': 'is_chapter_gte', 'params': { 'chapter': 1 }}},

### Gate Pattern B — `complete_intro_story` only (e.g. grassland_large_city)

Cities without a `complete_regional_quests` task award secondary chains directly from the `initialize` task's `task_complete_events`:
# In grassland_large_city_initialize task_complete_events:
{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_large_city_meet_savran' }},  # base story
{ 'event_type': 'award_task', 'params': { 'task_id': 'grassland_large_city_type_e_...' }},   # E chain

**Before authoring any secondary chain for a city:**
1. Open the city story file
2. Check whether a `complete_regional_quests` task exists
3. If yes → add secondary `award_task` events to that task's `task_complete_events`
4. If no → add them to the `initialize` task's `task_complete_events`
5. Apply appropriate `condition` gates to each secondary chain's `award_task` per the dependency chart

**Gating conditions by type at the award point:**

| Type | Condition at `award_task` |
|------|--------------------------|
| E | None — award immediately, artifact waits in inventory |
| F | `is_chapter_gte` matching the F chain's defined gate chapter |
| C | `is_chapter_gte` matching the city's own chapter number |
| D | Do not award here — D is awarded by the deliver quest to Mira/Brawn/Diego, which fires when the player picks up the trigger item |
| B | Do not award here — B is awarded by the Ch.20 Void Gauntlet event |
| A | Do not award here — A is awarded by the chapter seed's final task |

---

## Regional B Quest Tracking (`complete_regional_quests_2`)

Type B chains represent a second wave of regional completion — one per region, all gated behind the Ch.20 Void Gauntlet. The game already tracks the first regional wave via `complete_regional_quests`. A second parallel system is required.

**Required engine work (do not author B chains until this exists):**

1. Add `completed_regional_quests_2: []` to `player_game` — a list tracking completed B chain region IDs, identical in structure to `completed_regional_quests`.
2. Add a `complete_regional_quest_2` event type that appends a `region_id` to this list, mirroring `complete_region_quest`.
3. Add a `complete_regional_quests_2` task type that gates on all 7 entries being present, mirroring `complete_regional_quests`.

**Usage in city story files:**

Each Type B chain's final task fires:
{ 'event_type': 'complete_regional_quest_2', 'params': { 'region_id': '[region]' }}

**Usage in Ch.20:**

The Ch.20 Oracle/Reliquary dungeon task chain checks whether `complete_regional_quests_2` is finished. If not, the player is reset to re-run the dungeon on their next attempt. The gate does not block progression — it resets silently until all 7 B chains are done, at which point the final memory tonic event fires without interruption.
# In the Oracle/Reliquary dungeon task — conditional reset pattern:
{ 'event_type': 'award_task',
  'params': { 'task_id': 'ch20_oracle_reliquary_retry' },
  'condition': { 'type': 'is_task_not_active', 'params': { 'task_id': 'complete_regional_quests_2_gate' }}},
{ 'event_type': 'award_task',
  'params': { 'task_id': 'ch20_memory_tonic_final' },
  'condition': { 'type': 'is_task_completed', 'params': { 'task_id': 'complete_regional_quests_2_gate' }}},

### Pre-Author Checklist (Per Chain)

Before writing a single task:

- [ ] Read the city story file (`city_stories/[region]/[region]_[size]_city_story.py`) — know every NPC by name and role
- [ ] Read existing `NPC_DIALOG` — know each NPC's established voice
- [ ] Confirm the dungeon IDs available in this city (from `create_dungeon` events in `TASKS`)
- [ ] For **B** — re-read the regional character's profile in `extended_characters.py` or `ATTAINABLE CHARACTERS.txt`
- [ ] For **C** — read the extended character's profile in `extended_characters.py`
- [ ] For **D** — identify the trigger item, which chapter dungeon it goes in, and which of Mira/Brawn/Diego receives it; design the mythic item entry for `constants.py`
- [ ] For **E** — name the artifact and identify which D chain it will gate before writing anything
- [ ] For **F** — read the recurring NPC's existing dialog in all their chapter appearances
- [ ] For **A** — read the full chapter file and plan the `advance_chapter` migration before touching the city seed