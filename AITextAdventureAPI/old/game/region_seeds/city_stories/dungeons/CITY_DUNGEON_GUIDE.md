# City Dungeon Authoring Guide

This folder contains one `.py` dungeon seed file per city-story dungeon.

> **Primary reference:** For full `DUNGEON_SETTINGS` schema, content creation rules (items, hostiles, bosses, abilities), and overworld vs. dungeon encounter distinctions, see the authoritative guide:
> [`AITextAdventureAPI/old/STORY DOCUMENTS FOR AI/DUNGEON_BUILDER_README.md`](../../STORY%20DOCUMENTS%20FOR%20AI/DUNGEON_BUILDER_README.md)

---

## City Dungeon Patterns

City-story dungeons are always created by a `create_dungeon` event in a task's `task_acquire_events`. They are smaller, more focused encounters than main-story dungeons and follow one of two structural patterns:

### Pattern A — E-chain Artifact Dungeon

Used in **Type E** (Artifact Prerequisite) quest chains. The dungeon contains a boss that guards an artifact item. The player defeats the boss, claims the artifact, and exits.

- Typically 1 floor, 3–4 rooms.
- Boss is placed as an NPC in the `final_chamber` via `create_npc` in the same task.
- The boss's `begin_combat` event lives in the *next* task (`defeat` type), not in the dungeon task itself.
- No random encounter variety is required, but at least one floor hostile set should be defined.

### Pattern B — B-chain Regional Boss Dungeon (Void Gauntlet gated)

Used in **Type B** (Regional Character Quest) chains. The dungeon is the arena for the regional character's nemesis. Entry is via a `gated` self-completing task; the player is immediately moved to the `final_chamber` by `set_player_in_dungeon` in the next meet task.

- Typically 1 floor, 3–5 rooms.
- Boss must be placed via the dungeon seed's `npcs` list (location `'final_chamber'`).
- Boss definition goes in `boss_hostiles` + `boss_mob`; random floors go in `hostile_seeds` + `floor_hostiles`.
- The `gated` task fires `create_dungeon` **and** `complete_task` on itself, so the player transitions immediately.

---

## Level Expectations

City dungeon level should reflect the chapter the city is encountered in:
- Expected player level ≈ `chapter_number × 5`
- Set hostile `min_spawn_level` accordingly.

| Chapter range | Approx. level | Notes |
|---|---|---|
| Ch.1–4 | lv 5–20 | Early game; avoid high-rarity hostiles |
| Ch.5–10 | lv 25–50 | Mid-game; at least one `rare` per floor |
| Ch.11–16 | lv 55–80 | Late mid; `superrare` expected |
| Ch.17–21 | lv 85–105 | End-game; full rarity spread required |

Rarity rule (from `DUNGEON_BUILDER_README.md`): each floor should have at least one hostile of each rarity: `common`, `uncommon`, `rare`, and `superrare`.

---

## Registration

Every dungeon seed file in this folder must be registered in `game/constants.py`:
# In constants.py — import section (city dungeons)
from game.region_seeds.city_stories.dungeons.my_dungeon import DUNGEON_SETTINGS as MY_DUNGEON_SETTINGS

# In constants.py — DUNGEON_SETTINGS list
DUNGEON_SETTINGS += [MY_DUNGEON_SETTINGS]

Add the import alongside the other city dungeon imports (group them by region for readability).

---

## Dungeon Index

| `dungeon_id` | City story | Chain type | Chapter | Pattern |
|---|---|---|---|---|
| `murkchannel_run` | `swamp_small` | A (meet boss) | Ch.7 | A |
| `rotfen_hideaway` | `swamp_small` | A (meet boss) | Ch.7 | A |
| `the_swallowed_path` | `swamp_small` | A (boss defeat) | Ch.7 | A |
| `swamp_mid_city_oathrot_channel` | `swamp_mid` | E (artifact) | Ch.20 | A |
| `miregloom_resurrection_pit` | `swamp_large` | B (regional) | Ch.13 | B |
| `shallows_large_city_stormtide_vault` | `shallows_large` | E (artifact) | Ch.5 | A |
| `shallows_large_city_undertow_vault` | `shallows_large` | D (mythic weapon) | Ch.5 | A |
| `uulthars_tidal_maw` | `shallows_small` | B (regional) | Ch.14 | B |
| `mountains_large_city_conduit_maw` | `mountains_large` | D (mythic armor) | Ch.4 | A |
| `rokhulls_fracture_core` | `mountains_mid` | B (regional) | Ch.17 | B |
| `desert_large_city_choir_vault` | `desert_large` | E (artifact) | Ch.1 | A |
| `zaruuns_sanctum` | `desert_mid` | B (regional) | Ch.8 | B |
| `marrowroots_deep_grove` | `forest_large` | B (regional) | Ch.18 | B |
| `serenes_wind_vault` | `grassland_large` | B (regional) | Ch.10 | B |
| `grassland_mid_city_sanctum_vault` | `grassland_mid` | E (artifact) | Ch.3 | A |
| `aeriolass_frozen_sanctum` | `snow_large` | B (regional) | Ch.19 | B |

---

## File Naming Convention

Name each file after the `dungeon_id`:
murkchannel_run.py
rotfen_hideaway.py
the_swallowed_path.py
swamp_mid_city_oathrot_channel.py
miregloom_resurrection_pit.py
...