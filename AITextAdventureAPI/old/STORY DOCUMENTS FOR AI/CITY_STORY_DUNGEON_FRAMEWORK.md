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

**Confirmed eligible cities (reviewed from seed files):** Ch.6, Ch.7, Ch.10, Ch.12, Ch.18

---

### Type B — Regional Character Quest *(Void Gauntlet Gated)*

Each region's attainable character returns to their home region's **largest city** and draws the player into a dungeon.

| Region | Regional Character | City (Ch.) |
|--------|--------------------|------------|
| Desert | Sable | The Desert Metropolis (1) |
| Mountains | Bragg | Ironveil Foundry (4) |
| Shallows | Ripple | Brineward Harbor (5) |
| Grassland | Nia | Crosswind Bazaar (10) |
| Swamp | Grimnaw | The Necropolis (13) |
| Forest | Thorn | Aurelion Veil (18) |
| Snow | Kor-in | Frostgate Spire (19) |

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
| Boiling Bubble (2) | Sera Flameweaver |
| Highsteeple Crossing (3) | Regent Sylvara |
| Ironveil Foundry (4) | Spark Maddox |
| Bleakwatch Outpost (6) | Commander Drax |
| Gnashwater Hollow (7) | Ghost |
| Nightveil Spire (8) | Elyra Dawnseer |
| Crosswind Bazaar (10) | Voss Caldera |
| Blackwake Bay (11) | Dare |
| Quantford Hollow (12) | Rynn |
| The Necropolis (13) | Anita |
| Tidekin Cove (14) | Andrea Starveil |
| Thornshade Hamlet (16) | Talia Softheart |
| Gallows Rift (17) | Korina Brightvein |
| Aurelion Veil (18) | Osten Dreamweaver |
| Frostgate Spire (19) | Lyric |
| Hollerforge Hollow (21) | Lira Emberforge |

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
| 9  | The Radpost             | Desert    | Small | ~8    | Yes     | E | D |#F#| 9d
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

> **Ch.9 note:** The Radpost carries two Type D chains (Slot 2 and Slot 3) — two distinct mythic items, each gated by the Slot 1 artifact. No character unlock and no regional B makes this city a pure endgame equipment hub.
>
> **Ch.18 note:** Aurelion Veil is the only city with no Type D — its three slots are fully occupied by the Chapter Tie-In (A), the Forest Regional Quest (B), and the Extended Character Unlock (C), making it the most story-dense city in the game.

---

## NPC Rules (All Chain Types)

- **Do not create new NPCs for any chain other than the base city story.**
- B, C, D, E, and F must use NPCs already in the city seed, party members, or documented recurring NPCs.
- Tasks may reference NPCs from other cities the player already knows — explicitly allowed for Type A and Type F.

---

## Implementation Checklist (Per City)

- [ ] Identify the 3 dungeon seeds in the city story
- [ ] Assign each dungeon to its slot type per the table above
- [ ] Audit existing NPCs — confirm no new ones needed
- [ ] **If A:** Update the chapter seed with the mandatory detour task before `advance_chapter`
- [ ] **If B:** Confirm the regional character has a thematic reason to be in this specific city
- [ ] **If C:** Place the extended character at an appropriate location; `character_join` is the final event
- [ ] **If D:** Identify the trigger item, which chapter dungeon it goes in (`dungeon_add_treasure`), and which of Mira / Brawn / Diego receives the deliver quest
- [ ] **If E:** Name the artifact and document which Type D chain it gates in the artifact dependency table
- [ ] **If F:** Identify the recurring NPC anchor and add the faction thread to the F candidates table
- [ ] Verify no `award_task` cross-chain links exist between independent chains