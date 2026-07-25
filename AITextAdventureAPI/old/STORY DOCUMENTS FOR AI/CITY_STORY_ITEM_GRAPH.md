# City Story Item Graph

Tracks every special item flowing through city story chains — their award sources, their consumers, and any outstanding data issues.
This document is the resolution reference for the timeline validator's cross-story info annotations.

---

## Item Categories

| Category | Count | Purpose |
|----------|-------|---------|
| E — Artifact | 11 | Awarded by Type E chains. Gates a Type D chain in the same or a different city. |
| F — Faction Item | 4 | Awarded by Type F chains. Gates a Type D chain in a thematically connected city. |
| D — Trigger Item | 6 | Found in chapter dungeons via `dungeon_add_treasure`. Delivered to Mira / Brawn / Diego to unlock a Type D chain. |

---

## Known Issues Summary

| Issue | Items |
|-------|-------|
| **Duplicate award** — item awarded in two separate tasks in the same chain | `shallows_mid_city_e_tidekin_seal`, `snow_mid_city_e_pageant_decree_shard`, `mountains_large_city_e_forge_echo_core`, `shallows_large_city_e_brine_compass` |
| **Missing source** — item defined in constants but never awarded anywhere | `dominion_forge_key`, `swamp_mid_city_e_bayou_memory_vessel` (constants ID mismatch), `grassland_small_city_d_hollow_grief_token` |
| **No remove** — item awarded and consumed by condition (`has_item`) only, never explicitly removed | All cross-city E artifacts (by design — see note below) |

> **Cross-city E artifact remove policy:** When an E artifact gates a D chain in a *different* city, the D chain does not explicitly remove the artifact. The artifact persists in inventory as an inert collectible after the D chain completes. This is intentional — it rewards exploration and serves as a proof-of-journey item. If a remove is required for inventory hygiene, add `remove_item` as the final event in the D chain's last `task_complete_events`. Mark each cross-city pair resolved in the table below when decided.

---

## E — Artifact Items

### `desert_large_city_e_dune_cipher_stone`
**Display name:** Dune Cipher Stone
**Award source:** `desert_large_city_type_e_defeat_choir_echo` ✅
**Consumed by:** `desert_large_city` D chain (same city) — `has_item` gate on first D task ✅
**Remove:** consumed within same-city D deliver task ✅
**Issues:** None

---

### `forest_mid_city_e_mycelia_memory_spore`
**Display name:** Mycelia Memory Spore
**Award source:** `forest_mid_city_type_e_*` chain ✅ *(verify exact task ID in `forest_mid_city_story.py`)*
**Consumed by:** `forest_small_city` D chain (Thornshade Hamlet — retroactive Ch.2 → Ch.16) — `has_item` gate ✅
**Remove:** cross-city — not removed (inert collectible after use, see policy above)
**Issues:** None confirmed. Verify award task ID matches `forest_mid_city_e_mycelia_memory_spore` exactly.

---

### `grassland_mid_city_e_sanctum_seal_fragment`
**Display name:** Sanctum Seal Fragment
**Award source:** `grassland_mid_city_type_e_defeat_sanctum_voice` ✅ *(single award — no duplicate)*
**Consumed by:** `grassland_large_city` D chain (Crosswind Bazaar — Ch.3 E → Ch.10 D) — `has_item` gate
**Remove:** cross-city — not removed (inert collectible after use)
**Issues:** None

---

### `mountains_large_city_e_forge_echo_core`
**Display name:** Forge Echo Core
**Award source (intended):** single award in final task of E chain
**Award source (actual):** ⚠️ **DUPLICATE** — awarded in both `mountains_large_city_type_e_defeat_gearghost` AND `mountains_large_city_type_e_collect_core`
**Consumed by:** `mountains_mid_city` D chain (Gallows Rift) — `has_item` gate
**Remove:** cross-city — not removed after use
**Fix:** Remove `award_item` from `mountains_large_city_type_e_defeat_gearghost`. Keep only the award in `mountains_large_city_type_e_collect_core` (the terminal collect task).

---

### `shallows_large_city_e_brine_compass`
**Display name:** Brine Compass
**Award source (intended):** single award in final task of E chain
**Award source (actual):** ⚠️ **DUPLICATE** — awarded in both `shallows_large_city_type_e_defeat_stormtide_echo` AND `shallows_large_city_type_e_meet_syrin`
**Consumed by:** `shallows_large_city` D chain (same city) — D deliver task removes it ✅
**Fix:** Remove `award_item` from `shallows_large_city_type_e_defeat_stormtide_echo`. Keep only the award in `shallows_large_city_type_e_meet_syrin` (the terminal meet/return task).

---

### `desert_small_city_e_eroded_ledger_plate`
**Display name:** Eroded Ledger Plate
**Award source:** `desert_small_city_type_e_defeat_signal_wraith` ✅ *(single award)*
**Consumed by:** `desert_small_city` D chain (same city) — D deliver task removes it ✅
**Issues:** None

---

### `shallows_mid_city_e_tidekin_seal`
**Display name:** Tidekin Seal
**Award source (intended):** single award in final task of E chain
**Award source (actual):** ⚠️ **DUPLICATE** — awarded in both `shallows_mid_city_type_e_defeat_lanternfade_echo` AND `shallows_mid_city_type_e_collect_seal`
**Consumed by:** `shallows_small_city` D chain (Tidekin Cove) — `has_item` gate
**Remove:** cross-city — not removed after use
**Fix:** Remove `award_item` from `shallows_mid_city_type_e_defeat_lanternfade_echo`. Keep only the award in `shallows_mid_city_type_e_collect_seal` (the terminal collect task).

---

### `snow_mid_city_e_pageant_decree_shard`
**Display name:** Pageant Decree Shard
**Award source (intended):** single award in final task of E chain
**Award source (actual):** ⚠️ **DUPLICATE** — awarded in both `snow_mid_city_type_e_defeat_rimechant_echo` AND `snow_mid_city_type_e_collect_shard`
**Consumed by:** `snow_mid_city` D chain (same city) — D deliver task removes it ✅
**Fix:** Remove `award_item` from `snow_mid_city_type_e_defeat_rimechant_echo`. Keep only the award in `snow_mid_city_type_e_collect_shard` (the terminal collect task).

---

### `forest_small_city_e_thornshade_root_graft`
**Display name:** Thornshade Root Graft
**Award source:** `forest_small_city_type_e_*` chain *(verify exact task ID in `forest_small_city_story.py`)*
**Consumed by:** `forest_mid_city` D chain (Boiling Bubble — retroactive Ch.16 → Ch.2) — `has_item` gate
**Remove:** cross-city — not removed after use
**Issues:** Confirm award task ID matches `forest_small_city_e_thornshade_root_graft` exactly.

---

### `swamp_mid_city_e_bayou_memory_vessel`
**Display name:** Bayou Memory Vessel
**Award source (intended):** `swamp_mid_city_type_e_return_to_janrel` (terminal return task)
**Award source (actual):** ⚠️ **MISSING SOURCE** — the item appears with `Sources: None` in the item graph tool. The task awards the item but the constants entry may use a mismatched item ID, or the award event is missing from `swamp_mid_city_type_e_return_to_janrel`.
**Consumed by:** `swamp_mid_city_type_d_deliver_memory_vessel` — deliver task with `remove_item` ✅
**Fix:** Verify `award_item` in `swamp_mid_city_type_e_return_to_janrel` uses exactly `swamp_mid_city_e_bayou_memory_vessel`. Cross-check against `constants_items.py` entry and align IDs.

---

### `mountains_small_city_e_dominion_fragment`
**Display name:** Dominion Fragment *(framework name)*
**Award source (actual):** `mountains_small_city_type_e_defeat_dominion_hollow` awards `forge_dominion_shard` — **ID does not match framework key**
**Consumed by:** `mountains_small_city` D chain (same city, Slot 3) — gated by this artifact
**Remove:** consumed by same-city D chain
**Issues:**
- ⚠️ **ID MISMATCH** — Code awards `forge_dominion_shard`; framework specifies `mountains_small_city_e_dominion_fragment`. One must be renamed to match the other.
- ⚠️ **`dominion_forge_key`** — A separate special item exists in `constants_items.py` with display name "Dominion Forge Key" and `Sources: None`. This item is not referenced by any task. It is likely an orphaned placeholder that predates the E chain rewrite. **Resolution: either wire it in as the trigger key for the D chain, or delete it from constants if superseded by `forge_dominion_shard`.**
- **Recommended fix:** Rename `forge_dominion_shard` → `mountains_small_city_e_dominion_fragment` in `mountains_small_city_story.py` and `constants_items.py`. Remove or repurpose `dominion_forge_key`.

---

## F — Faction Items

### `desert_large_city_f_salvage_manifest`
**Display name:** Salvage Manifest
**Award source:** `desert_large_city_type_f_retrieve_manifest` ✅
**Consumed by:** gates `grassland_mid_city` D chain (Highsteeple Crossing) — `has_item` condition
**Remove:** cross-city — not removed after use (faction item, inert collectible)
**Issues:** None

---

### `shallows_large_city_f_rift_observation_log`
**Display name:** Rift Observation Log
**Award source:** `shallows_large_city_type_f_deliver_to_astra` ✅
**Consumed by:** gates `snow_large_city` D chain (Frostgate Spire) — `has_item` condition
**Remove:** cross-city — not removed after use
**Issues:** None

---

### `desert_small_city_f_contraband_registry`
**Display name:** Contraband Registry
**Award source:** *(not yet confirmed — verify task ID in `desert_small_city_story.py`)*
**Consumed by:** gates `snow_small_city` D chain (Bleakwatch Outpost) — `has_item` condition
**Remove:** cross-city — not removed after use
**Issues:** Confirm award task exists and uses `desert_small_city_f_contraband_registry`.

---

### `snow_mid_city_f_audit_testimony_seal`
**Display name:** Audit Testimony Seal
**Award source:** `snow_mid_city_type_f_return_to_marlo` ✅
**Consumed by:** gates `swamp_mid_city` D chain (Bayou Nocturne) — `has_item` condition
**Remove:** cross-city — not removed after use
**Issues:** None

---

## D — Standard Trigger Items

These items are seeded in chapter dungeons via `dungeon_add_treasure`. They are picked up during normal chapter progression and then delivered to Mira, Brawn, or Diego to unlock the D chain.

| Item ID | Display Name | Source Dungeon | Source Task | Deliver To | D Chain City | Status |
|---------|-------------|----------------|-------------|------------|-------------|--------|
| `mountains_large_city_d_foundry_resonance_key` | Foundry Resonance Key | Ch.4 chapter dungeon | `main_story_ch4_meet_kirn` (verify) | Brawn | Ironveil Foundry (4) | ✅ Source confirmed in Ch.4 |
| `desert_mid_city_d_ink_resonance_vial` | Ink Resonance Vial | Ch.8 chapter dungeon | *(verify)* | Mira | Nightveil Spire (8) | ⚠️ Verify `dungeon_add_treasure` exists |
| `shallows_mid_city_d_corsair_tide_fragment` | Corsair Tide Fragment | Ch.5 chapter dungeon | *(verify)* | Diego | Blackwake Bay (11) | ⚠️ Verify `dungeon_add_treasure` exists |
| `grassland_small_city_d_hollow_grief_token` | Hollow Grief Token | Ch.3 dungeon (`nobles_mansion_ch3`, `final_chamber`) | `main_story_ch_3_bring_in_seth` | Mira | Quantford Hollow (12) | ⚠️ **MISSING SOURCE** — `Sources: None` in item graph. `dungeon_add_treasure` event not confirmed in `main_story_chapter_3.py`. Must be added. |
| `swamp_large_city_d_necropolis_marrow_shard` | Necropolis Marrow Shard | Ch.4 dungeon (`rift_dungeon_ch4`, `treasure_room`) | `main_story_ch4_meet_kirn` | Diego | The Necropolis (13) | ✅ Source confirmed |
| `forest_large_city_d_veil_memory_leaf` | Veil Memory Leaf | Ch.2 chapter dungeon | *(verify)* | Mira | Aurelion Veil (18) | ⚠️ Verify `dungeon_add_treasure` exists |

> **`Windcarver's Token`** — Sources: `nobles_mansion_ch3 (final_chamber)` — `main_story_ch_3_bring_in_seth`. This is a separate item from `grassland_small_city_d_hollow_grief_token`. The `Windcarver's Token` is awarded by the Ch.3 dungeon but its consumer (which deliver task or has_item gate uses it) is not yet confirmed. Verify whether this is a leftover from a superseded design or the intended trigger for a different D chain. If not consumed anywhere, it should either be wired to a chain or removed from the dungeon loot.

---

## Resolution Checklist

- [ ] Fix **4 duplicate award** chains: remove `award_item` from defeat tasks, keep only in terminal collect/return task
  - [ ] `mountains_large_city_type_e_defeat_gearghost` — remove `award_item` for `mountains_large_city_e_forge_echo_core`
  - [ ] `shallows_large_city_type_e_defeat_stormtide_echo` — remove `award_item` for `shallows_large_city_e_brine_compass`
  - [ ] `shallows_mid_city_type_e_defeat_lanternfade_echo` — remove `award_item` for `shallows_mid_city_e_tidekin_seal`
  - [ ] `snow_mid_city_type_e_defeat_rimechant_echo` — remove `award_item` for `snow_mid_city_e_pageant_decree_shard`
- [ ] Fix **Bayou Memory Vessel** ID mismatch — align `swamp_mid_city_type_e_return_to_janrel` award ID and `constants_items.py` entry
- [ ] Fix **Dominion Fragment** ID mismatch — rename `forge_dominion_shard` → `mountains_small_city_e_dominion_fragment` and clean up `dominion_forge_key` orphan
- [ ] Add **`dungeon_add_treasure`** to `main_story_chapter_3.py` for `grassland_small_city_d_hollow_grief_token`
- [ ] Verify `dungeon_add_treasure` placement for `desert_mid_city_d_ink_resonance_vial`, `shallows_mid_city_d_corsair_tide_fragment`, `forest_large_city_d_veil_memory_leaf`
- [ ] Confirm `desert_small_city_f_contraband_registry` award task exists in `desert_small_city_story.py`
- [ ] Clarify `Windcarver's Token` — wire to a D chain deliver task or remove from `nobles_mansion_ch3` loot
- [ ] Decide cross-city E/F artifact remove policy per item and add `remove_item` to D chain finals where needed