# Implementation Spec: Character Elements and Cleanup

**Status:** Complete, ready for implementation
**Based on:** the code after PR #42 and PR #43
**Scope:** data and small code changes (§1–8), plus new shared-pool abilities delivered in batches (§9 onward).

## Overview

| # | Change | Files | Size |
|---|---|---|---|
| 1 | Every character has at least 2 elements; 5 element changes | `main_characters.py` | Small |
| 2 | Vek's signature moves changed to match fire + dark | `unique_character_abilities.py` | Small |
| 3 | Restore Vek's description | `main_story_chapter_10.py` | Trivial |
| 4 | Fix resistance / immunity / weakness names that do nothing | ~40 dungeon seed files | Small, wide |
| 5 | Remove the old-save HP fix | `player.py` | Small |
| 6 | Update the older spec notes that say single-element characters are intended | `STORY DOCUMENTS FOR AI/` | Trivial |
| 7 | Carried to the new-abilities work | none | none |
| 8 | Verification (§1–6) | none | none |
| 9 | New abilities: targets and fill plan | none | none |
| 10 | Batch 1: 39 new Level 1 and Level 2 moves | `level_1_abilities.py`, `level_2_abilities_by_type/*.py` | Medium |
| 11 | Batch 2: 46 new Level 5 moves | `level_5_abilities_by_type/*.py` | Medium |
| 12 | Batch 3: 34 new Level 4 moves + Ghost's Undertow Turn | `level_4_abilities_by_type/*.py`, `unique_character_abilities.py`, `extended_characters.py` | Medium |
| 13 | Batch 4: 20 new Level 3 moves | `level_3_abilities_by_type/*.py` | Small |
| 14 | Final check across all batches | none | none |

---

## 1. Character elements: minimum of 2 per character

**New rule:** every playable character has **at least 2 elements**. The core five keep their 4 each. Recruits have exactly 2.

### 1.1 Changes to `CHARACTER_NPC_ELEMENT_MAP`

File: `game/region_seeds/main_characters.py` (map at about lines 53–72).

| Character | Class | Before | After | Reason |
|---|---|---|---|---|
| Nia | skill | `['air', 'water']` | `['air', 'light']` | She is a wind-dancer, so water is off theme. Light fits her bright energy. |
| Ghost | skill | `['dark', 'ice']` | `['dark', 'water']` | Aikido flow and redirection ("be like water"). Takes over skill water from Nia. |
| Thorn | technique | `['earth']` | `['earth', 'dark']` | Corruption and grief. His signature moves (Root Snap, Feral Surge) are already dark + earth. |
| Eldon Dawnseer | spirit | `['light']` | `['light', 'dark']` | Visions that leave "a residue he cannot wash off." His signature moves (Fragment Vision, Dawnsight Strike) are already dark + light. |
| Marshal Vek Drast | technique | `['earth', 'dark']` | `['fire', 'dark']` | Fits her chaotic look, and she no longer has Thorn's exact element pair. See §2 for her moves. |

All other characters stay as they are. Talon stays earth + light (decided).

Resulting lines:

```python
	'lyren': ['water', 'earth'], 'vek': ['fire', 'dark'],
	...
	'nia': ['air', 'light'], 'sable': ['earth', 'air'], 'thorn': ['earth', 'dark'], 'bragg': ['earth', 'fire'],
	...
	'voss_caldera': ['earth', 'light'], 'rynn': ['water', 'ice'], 'eldon_dawnseer': ['light', 'dark'],
	'regent_sylvara': ['dark', 'electric'], 'ghost': ['dark', 'water'], 'lira_emberforge': ['fire', 'earth'],
```

Also update the comment above the map if it says recruits have "1–2 elements". It should say: "Recruits have exactly 2 elements; the core five have 4."

### 1.2 Effects (checked against the current ability pool)

**Every player ability still has at least one character who can learn it** (0 orphaned, same as today).

Learnable moves per ability level (L1/L2/L3/L4/L5). The minimum is 2/6/6/5/4.

| Character | Elements | Pool |
|---|---|---|
| Nia | air + light | 3 / 15 / 8 / 35 / 6 |
| Ghost | dark + water | 3 / 15 / 12 / 31 / 6 |
| Thorn | earth + dark | 3 / 16 / 13 / 12 / 6 |
| Eldon | light + dark | 4 / 14 / 21 / 17 / 11 |
| Vek | fire + dark | 2 / 15 / 14 / 11 / 4 |

Who has each element, by class, after the change:

| Element | Technique | Spirit | Magic | Tech | Skill |
|---|---|---|---|---|---|
| Fire | Chock, **Vek**, Lira | Kaera | Moxie, Veyr | Bragg, Spark | Dare, Andrea |
| Ice | Kor'in | Rynn | Moxie | Lyric | Poise |
| Water | Chock | Kaera, Lyren, Ripple, Rynn | Osten | Kade | **Ghost** |
| Earth | Chock, Warden, **Thorn**, Lira | Kaera, Lyren, Talon | Sable | Bragg, Voss | Poise |
| Air | Kor'in | Seraphine | Sable, Anita | Kade | Poise, Nia |
| Electric | Drax | Alden | Moxie, Sylvara | Kade, Grimnaw, Lyric, Spark | Dare |
| Light | Chock, Warden, Drax | Kaera, Seraphine, **Eldon**, Talon, Alden | Veyr | Kade, Voss | Poise, **Nia**, Andrea |
| Dark | **Vek**, **Thorn** | Ripple, **Eldon** | Moxie, Sylvara, Osten, Anita | Grimnaw | **Ghost** |

Every class still covers all 8 elements.

**Knock-on:** skill ice now belongs only to Poise (Ghost gave it up). Ghost keeps every one of his signature moves through dark:

| Move | Elements |
|---|---|
| Shadow Mark | air, dark |
| Silent Read | dark, ice |
| Disappearing Act | air, dark |
| Void Efface | air, dark, ice |

### 1.3 Save games

Element assignment already reads from the map whenever the class is set or a recruit joins. Old saves do not need to carry over (see §5), so no migration is needed. If `elements_base` is ever re-read on load, it will pick up the new values automatically.

---

## 2. Vek's signature moves: swap in fire and dark

File: `game/region_seeds/player_abilities/unique_character_abilities.py`, lines about 391–430.

None of Vek's four signature moves had fire or dark. **Swap out the off-theme element rather than adding one**, so each move keeps the same number of elements. That keeps element-share and stack math unchanged. Earth stays on each move as her grounding in order. A move does not have to match a character's elements exactly; it only needs one shared element to be learnable.

| Move | Ability ID | Before | After |
|---|---|---|---|
| Command Strike (L2) | `lv2_unique_ability_technique_vek_command_strike` | `["earth", "light"]` | `["earth", "fire"]` |
| Rally Line (L2) | `lv2_unique_ability_technique_vek_rally_line` | `["earth", "electric"]` | `["fire", "earth"]` |
| Dominion Breach (L3) | `lv3_unique_ability_technique_vek_dominion_breach` | `["earth", "earth", "electric"]` | `["dark", "fire", "earth"]` |
| Iron Verdict (L4) | `lv4_unique_ability_technique_vek_iron_verdict` | `["earth", "light", "electric", "earth"]` | `["fire", "dark", "earth", "earth"]` |

**Keep the entry counts.** Dominion Breach keeps 3 entries (now one each of dark, fire and earth). Iron Verdict keeps 4, and its repeated `earth` is a deliberate 2-stack. Do not "clean up" that duplicate.

Rally Line is a buff (`defense_buff`, `constitution_buff`). Its elements only affect who can learn it and its flavor, not the buff math. Leave the ability IDs, names, power, AP cost and status keys unchanged. Chapter 11 references these IDs, so they must not change.

---

## 3. Restore Vek's description

File: `game/region_seeds/main_story/main_story_chapter_10.py`, line about 94.

PR #42 replaced her description with one generic line. Restore the original and keep the `sex` field:

```python
        "description": (
            "A tough, no-nonsense city enforcer with a powerful sense of order and duty."
            " She holds her city together through sheer force of will when institutions fail around her."
            " Vek does not ask for help and rarely offers softness, but she shows up — every time — when the world starts tearing people apart."
            " Her sense of order isn't cruelty; it's the only form of care she knows how to give."
        ),
```

Save the file as UTF-8 (the em dashes broke in an earlier PR).

---

## 4. Resistance / immunity / weakness names that do nothing

Combat compares these lists against real element names and status keys. These five names match nothing, so the entries silently do nothing.

**Valid elements:**
- `physical`, `light`, `dark`, `earth`, `air`, `fire`, `water`, `electric`, `ice`

**Valid status keys (as used by player abilities):**
- Control: `stun`, `sleep`, `confuse`, `silence`, `petrify`
- Damage and healing over time: `continuous_damage`, `regen`
- Other: `scanned`
- Stat buffs: `strength_buff`, `dexterity_buff`, `constitution_buff`, `intelligence_buff`, `attack_buff`, `defense_buff`, `elemental_attack_buff`, `elemental_defense_buff`
- Stat debuffs: `strength_debuff`, `dexterity_debuff`, `constitution_debuff`, `intelligence_debuff`, `attack_debuff`, `defense_debuff`, `elemental_debuff`

| Dead name | Where it appears | Action |
|---|---|---|
| `lightning` | 1 weakness, `main_story/dungeons/seth_hideout.py:175` | **Rename to `electric`.** This is a real bug: that enemy currently has no weakness. |
| `poison` | 26 immunities, 8 resistances | **Rename to `continuous_damage`.** |
| `burn` | 11 immunities | **Rename to `continuous_damage`.** |
| `slow` | 68 immunities, 1 resistance | **Remove.** There is no slow status. Mapping it to `dexterity_debuff` would suddenly make 68 enemies immune to a debuff they can be hit by today. |
| `knockback` | 1 immunity, `main_story/dungeons/mountain_ruin.py:52` | **Remove.** There is no knockback mechanic, and that enemy is already immune to stun and petrify. |

Rules for the edit:
- If a list ends up with `continuous_damage` twice (it had both `poison` and `burn`), keep one.
- If a list becomes empty after a removal, leave it as `[]`. Do not delete the key.
- Change only these five names. Do not touch any other entry.

Balance note: the `poison` and `burn` changes make **37 enemy entries** immune to, or resistant against, damage over time. That is the intended meaning of those entries. Now that DoT expires like regen (followups spec §9), resistance halves its duration and immunity blocks it.

Find every occurrence:

```
grep -rnE "['\"](slow|poison|burn|knockback|lightning)['\"]" game/region_seeds --include=*.py
```

Afterwards, the same grep must return nothing.

---

## 5. Remove the old-save HP fix

**Decision:** existing save games do not need to receive this update, now or later. Remove the old-save HP fix rather than repairing it. This also makes the "old-save Voss with 5 AP" problem moot.

File: `game/objects/player.py`

1. **Delete** the whole block in `__setstate__` that starts with the comment `# IMPLEMENTATION_SPEC_leveling.md 1.4: migrate HP for saves made before...` (about lines 152–167), through `self.hp_formula_version = HP_FORMULA_VERSION`.
2. **Delete** the `hp_formula_version` field (about line 70) and its entry in the `__setstate__` defaults dict (about line 126).
3. **Delete** the `HP_FORMULA_VERSION = 2` constant (about line 27). Nothing else references it.
4. Leave the rest of `__setstate__` alone. The defaults dict still protects against missing fields in other ways.

Old pickles that still carry `hp_formula_version` will simply have an unused attribute, which does no harm.

---

## 6. Documentation cleanup

Two older specs in `STORY DOCUMENTS FOR AI/` say single-element characters are intended. That is no longer true.

- `IMPLEMENTATION_SPEC_character_elements.md` line about 64: replace it with "Every recruit has exactly 2 elements; the core five have 4." Update the map listing in that file to match §1.1.
- `IMPLEMENTATION_SPEC_class_growth_elements.md` line about 226 (Part 2): add a note at the top of Part 2 saying "Superseded by IMPLEMENTATION_SPEC_character_elements.md and IMPLEMENTATION_SPEC_elements_and_cleanup.md." Its element map is out of date.

Optional: if the existing startup element-map check counts elements per character, make it warn when a non-core character has fewer than 2. Skip this if it adds any real complexity.

---

## 7. Carried to the new-abilities work

These are decided. They are written up in the batch for their level (see §9.3):

- **Kōri no Kansetsu** (氷の関節, "joint of ice"), a new **skill ice Level 4** move that Poise can learn. It is a freezing joint lock. It fills the skill ice Level 4 gap, which currently has **0 moves**.
- **Ghost: a water aikido move** in the same spirit (redirecting momentum, an undertow-style lock or throw). It is a signature move for Ghost.
- The other aikido ideas for Ghost: Windmill Throw, Borrowed Momentum, Six-Step Shadow.

Gap list to fill in that spec (single-element depth where a character actually uses the element):

| Class | Element | Gap | Affects |
|---|---|---|---|
| Spirit | ice | **0** at L4, 1 at L5 | Rynn |
| Spirit | electric | 2 at L4, 1 at L5 | Alden |
| Spirit | dark | 1 at L5 | Ripple, Eldon |
| Magic | electric | **0** at L5 | Moxie, Sylvara |
| Magic | ice | 1 at L5 | Moxie |
| Magic | light | **0** at L1, 1 at L3 | Veyr |
| Skill | ice | **0** at L4 | Poise (Kōri no Kansetsu covers 1) |
| Skill | electric | **0** at L4 | Dare |
| Skill | light | 1 at L3 | Nia, Andrea, Poise |
| Technique | water / dark / electric | 2 each at L5 | Chock, Vek, Thorn, Drax |
| Technique | light | 3 at L3 | Warden, Drax |
| Tech | ice / water | 3 at L4 | Lyric, Kade |

---

## 8. Verification

1. Every entry in `CHARACTER_NPC_ELEMENT_MAP` has at least 2 elements, and every value is a valid element name.
2. Nia = air + light, Ghost = dark + water, Thorn = earth + dark, Eldon = light + dark, Vek = fire + dark. Talon is unchanged.
3. Every non-`non_player_ability` player ability can be learned by at least one character (its class plus at least one shared element). Expected result: 0 orphaned.
4. Every character's signature moves share at least one element with that character's new elements.
5. Vek's four moves have exactly the element lists in §2, with 2, 2, 3 and 4 entries. Iron Verdict keeps its double `earth`.
6. Vek's Chapter 10 description matches §3 exactly and the file is valid UTF-8.
7. The grep in §4 returns no matches. `seth_hideout.py:175` weakness is `['electric']`.
8. No resistance or immunity list contains `continuous_damage` twice.
9. `grep -rn "hp_formula_version\|HP_FORMULA_VERSION"` returns nothing in game code.
10. A new game starts, recruits join with the correct elements, and loading a save made after this change works.
11. All files compile (`python -m compileall game tui`).

---

## 9. New abilities: targets and fill plan

Added after the first draft. New shared-pool moves are delivered here in batches, each as its own section (§10 onward).

### 9.1 Targets (per class, per ability level, per element)

| Ability level | Minimum moves carrying each element |
|---|---|
| 1 | **2** |
| 2–5 | **8** |

- **8 is a minimum, not a cap.** Cells already over target, such as skill L4 earth at 26, are left alone.
- **Only the shared pool counts.** Character signature moves (`unique_character_abilities.py`) are not part of these counts.
- **How moves are counted:** a move counts once under each different element it carries. A repeated element (for example `["earth", "earth"]`) counts once toward coverage but still stacks in damage.

### 9.2 Element-entry rule (current convention, keep it)

A move's number of element entries equals its ability level: L1 = 1, L2 = 2, L3 = 3, L4 = 4, L5 = 5. Entries may repeat an element, which makes it a stack.

### 9.3 Shortfall and fill plan

The shortfall is 294 element entries, measured against the pool after PR #43. Filling it with multi-element moves takes about **139 new moves** in the **focused** style: Levels 2–3 use at most 2 different elements and Levels 4–5 at most 3, so each move keeps a clear identity. Maxing out every blend would need about 125 moves, but it repeats the skill L4 problem, where blends are everywhere but there are no real ice or electric moves.

New moves needed (focused):

| Class | L1 | L2 | L3 | L4 | L5 | Total |
|---|---|---|---|---|---|---|
| Technique | 7 | 1 | 5 | 5 | 13 | 31 |
| Spirit | 6 | 1 | 0 | 8 | 9 | 24 |
| Magic | 8 | 1 | 7 | 4 | 8 | 28 |
| Tech | 8 | 1 | 1 | 9 | 5 | 24 |
| Skill | 6 | 0 | 7 | 8 | 11 | 32 |
| **Total** | **35** | **4** | **20** | **34** | **46** | **139** |

Batches:

| Batch | Scope | Section |
|---|---|---|
| 1 | Level 1 + Level 2 (39 moves) | §10 |
| 2 | Level 5 (46 moves) | §11 |
| 3 | Level 4 (34 moves), including **Kōri no Kansetsu** and Ghost's **Undertow Turn** | §12 |
| 4 | Level 3 (20 moves) | §13 |

Ghost's other aikido ideas (Windmill Throw, Borrowed Momentum, Six-Step Shadow) are signature moves. They go in a later batch and do not count toward the shared-pool targets.

### 9.4 Rules for every batch

- **IDs** follow the existing pattern `{elements}_{class}_lv{N}_{snake_name}`, for example `fire_technique_lv1_kindled_fury`. IDs and names must be unique across all player and character abilities.
- **One direction per move:** every status in a move is either all beneficial or all harmful (followups spec §2).
- **Only valid status keys:** use only the keys listed in §4.
- **No new stat requirements are needed.** Requirements are computed from class and ability level.
- **Seeds go in the existing files:**
  - Level 1: `level_1_abilities.py`, under the matching class block.
  - Level 2 and up: `level_N_abilities_by_type/<class>.py`.
- Update a file's header comment where it states a count. For example, `level_1_abilities.py` says "1 ability per element"; it is now 2.

---

## 10. Batch 1: Level 1 and Level 2 (39 moves)

The power and AP values below follow the existing norms for each class at that level. They were chosen to sit beside the current move in that class and element, not to copy it. For example, if an element already has a damage move, the new one is a buff or debuff, and the other way round.

### 10.1 Technique, Level 1 (7)

Current L1 technique norms:
- Damage: 14 power, 9 AP
- Disabling status (stun, silence): 1 power, 12–13 AP
- Self buff: 0 power, 7 AP

| ID | Name | Element | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `fire_technique_lv1_kindled_fury` | Kindled Fury | fire | status | `attack_buff` | 0 | 7 | no | A burst of inner heat that drives every swing harder. |
| `ice_technique_lv1_rime_grip` | Rime Grip | ice | status | `dexterity_debuff` | 3 | 9 | no | A freezing clinch that stiffens the target's limbs. |
| `water_technique_lv1_riptide_sweep` | Riptide Sweep | water | status | `strength_debuff` | 3 | 9 | no | A low, dragging sweep that pulls the footing out from under a foe. |
| `air_technique_lv1_gale_cleave` | Gale Cleave | air | damage | none | 14 | 9 | no | A cutting swing carried on a rush of wind. |
| `electric_technique_lv1_spark_cut` | Spark Cut | electric | damage | none | 14 | 9 | no | A charged edge that cracks on impact. |
| `light_technique_lv1_dawn_resolve` | Dawn Resolve | light | status | `strength_buff` | 0 | 7 | no | A steadying breath of light that firms the arm and the will. |
| `dark_technique_lv1_dread_glare` | Dread Glare | dark | status | `defense_debuff` | 3 | 9 | no | A look from the dark that cracks a foe's guard. |

Kindled Fury and Dawn Resolve are self-buffs. They pair with the physical-buff rules, and their `attack_buff` and `strength_buff` apply to physical abilities as well as basic attacks.

### 10.2 Spirit, Level 1 (6)

Current L1 spirit norms:
- Heal: 9 power, 10 AP
- Cure: 0 power, 8–15 AP
- Blessing: 0 power, 7–9 AP, often AoE
- Debuff: 2 power, 8 AP
- Disabling status: 0 power, 13 AP

| ID | Name | Element | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `fire_spirit_lv1_searing_rebuke` | Searing Rebuke | fire | damage | none | 9 | 10 | no | A word of judgment that burns where it lands. |
| `ice_spirit_lv1_hush_of_winter` | Hush of Winter | ice | status | `sleep` | 0 | 13 | no | A cold, quiet hymn that lulls a foe into stillness. |
| `earth_spirit_lv1_rootbound_mend` | Rootbound Mend | earth | heal | none | 9 | 10 | no | Living roots knit torn flesh closed. |
| `air_spirit_lv1_clearing_breeze` | Clearing Breeze | air | cure | `confuse`, `sleep` | 0 | 10 | no | A clean breath of wind that clears a clouded mind. |
| `electric_spirit_lv1_quickening_spark` | Quickening Spark | electric | status | `intelligence_buff` | 0 | 8 | yes | A bright current that sharpens focus. |
| `dark_spirit_lv1_penance` | Penance | dark | status | `attack_debuff` | 2 | 8 | no | A heavy, unseen weight of guilt that slows the hand. |

This gives spirit its first L1 damage move (Searing Rebuke) and a second L1 heal (Rootbound Mend).

### 10.3 Magic, Level 1 (8)

Current L1 magic norms:
- Damage: 9 power, 10 AP, AoE; or 10 power, 9 AP, single target

Magic light currently has **0** L1 moves, so it gets 2.

| ID | Name | Element | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `light_magic_lv1_radiant_bolt` | Radiant Bolt | light | damage | none | 9 | 10 | yes | A lance of searing light. |
| `light_magic_lv1_dazzle` | Dazzle | light | status | `attack_debuff` | 2 | 9 | no | A flare of light that blinds and throws off a foe's aim. |
| `ice_magic_lv1_frost_lock` | Frost Lock | ice | status | `dexterity_debuff` | 2 | 9 | no | Frost creeps into the joints and slows every movement. |
| `water_magic_lv1_drowning_hex` | Drowning Hex | water | status | `silence` | 1 | 12 | no | Phantom water fills the throat and smothers the voice. |
| `earth_magic_lv1_gravel_spike` | Gravel Spike | earth | damage | none | 10 | 9 | no | A spike of packed stone erupts beneath the target. |
| `air_magic_lv1_thin_air` | Thin Air | air | status | `intelligence_debuff` | 2 | 9 | no | The air around the target thins until thought itself falters. |
| `electric_magic_lv1_static_spark` | Static Spark | electric | damage | none | 10 | 9 | no | A snapping arc of static aimed at one foe. |
| `dark_magic_lv1_hex_of_doubt` | Hex of Doubt | dark | status | `confuse` | 1 | 13 | no | A whispered curse that turns a foe against their own instincts. |

### 10.4 Tech, Level 1 (8)

Current L1 tech norms:
- Damage: 12–13 power, 9–12 AP
- Status device: 0 power, 7–8 AP, AoE
- Stun: 0 power, 13 AP

Tech had few L1 damage options, so most of these are damage moves.

| ID | Name | Element | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `fire_tech_lv1_flare_shot` | Flare Shot | fire | damage | none | 13 | 9 | no | A compact launcher fires a burning flare. |
| `water_tech_lv1_hydro_jet` | Hydro Jet | water | damage | none | 13 | 9 | no | A pressurized jet that hits like a hammer. |
| `air_tech_lv1_air_cannon` | Air Cannon | air | damage | none | 13 | 9 | no | A wrist cannon that fires a compressed blast of air. |
| `earth_tech_lv1_seismic_spike` | Seismic Spike | earth | damage | none | 13 | 9 | no | A driven spike that sends a jolt through the ground. |
| `electric_tech_lv1_arc_pistol` | Arc Pistol | electric | damage | none | 13 | 9 | no | A sidearm that fires a tight bolt of current. |
| `light_tech_lv1_flashbang` | Flashbang | light | status | `confuse` | 0 | 13 | no | A blinding, deafening burst that scrambles a target. |
| `ice_tech_lv1_coolant_spray` | Coolant Spray | ice | status | `dexterity_debuff` | 0 | 8 | yes | A freezing mist of coolant that slows everything it touches. |
| `dark_tech_lv1_signal_jammer` | Signal Jammer | dark | status | `silence` | 0 | 12 | no | A black-box jammer that cuts a target off mid-word. |

### 10.5 Skill, Level 1 (6)

Current L1 skill norms:
- Damage: 8 power, 5 AP
- Stat debuff: 5 power, 8 AP
- Disabling status: 1 power, 11 AP

| ID | Name | Element | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `fire_skill_lv1_ember_kick` | Ember Kick | fire | damage | none | 8 | 5 | no | A spinning kick that trails sparks. |
| `earth_skill_lv1_pebble_volley` | Pebble Volley | earth | damage | none | 8 | 5 | no | A rapid flick of stones, each aimed at a weak point. |
| `ice_skill_lv1_chill_needle` | Chill Needle | ice | status | `stun` | 1 | 12 | no | A frozen needle to a nerve point that locks the body for a moment. |
| `water_skill_lv1_mist_veil` | Mist Veil | water | status | `dexterity_buff` | 0 | 6 | no | A thin veil of mist that makes the user hard to pin down. |
| `electric_skill_lv1_static_jolt` | Static Jolt | electric | status | `defense_debuff` | 5 | 8 | no | A palm strike that leaves a foe's guard twitching and open. |
| `light_skill_lv1_blinding_powder` | Blinding Powder | light | status | `attack_debuff` | 5 | 8 | no | A pinch of glittering powder thrown straight into the eyes. |

Mist Veil gives Ghost (dark + water) an early water evasion move. Chill Needle costs 1 more AP than Tranq Dart because stun is stronger than sleep.

### 10.6 Level 2 (4)

Current L2 norms:
- Technique damage: 36 power, 30 AP
- Spirit damage: 35 power, 30 AP
- Magic damage: 33–35 power, 27–29 AP
- Tech damage: 30 power, 25 AP

| ID | Name | Class | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|---|
| `ice_electric_technique_lv2_frostcharge_cleave` | Frostcharge Cleave | technique | `["ice", "electric"]` | damage | none | 36 | 30 | no | A frost-rimed blade that discharges on contact. |
| `ice_dark_spirit_lv2_hollow_frost` | Hollow Frost | spirit | `["ice", "dark"]` | damage | none | 35 | 30 | no | A cold that comes from the empty places between prayers. |
| `light_magic_lv2_lumen_spear` | Lumen Spear | magic | `["light", "light"]` | damage | none | 34 | 28 | no | A single, concentrated spear of light. |
| `ice_electric_tech_lv2_cryo_arc_emitter` | Cryo-Arc Emitter | tech | `["ice", "electric"]` | damage | none | 30 | 25 | no | A dual-coil emitter that fires a freezing arc of current. |

Lumen Spear is a single-target light move. It sits beside the existing magic light + light AoE move.

### 10.7 Batch 1 verification

1. 39 new seeds exist with unique IDs and names, and all compile.
2. Every class has **at least 2 moves per element at L1** and **at least 8 per element at L2** (shared pool only).
3. Every new move's element-entry count equals its level (L1 = 1, L2 = 2).
4. No new move mixes beneficial and harmful statuses, and all status keys are valid.
5. The element validator still reports 0 warnings, and no player ability is orphaned (§8 check 3).
6. Spot check in game: Ghost can see Mist Veil, Nia can see Blinding Powder, Veyr can see Radiant Bolt and Dazzle, and Thorn and Vek can see Dread Glare.

---

## 11. Batch 2: Level 5 (46 moves)

Every new L5 move has **5 element entries using at most 3 different elements** (the focused style in §9.3). Repeated entries are deliberate stacks; keep them exactly as listed. Seeds go in `level_5_abilities_by_type/<class>.py`, above the `#### NON PLAYER ABILITIES` block.

### 11.1 Technique (13)

Current L5 technique norms: single-target damage 192 power / 180 AP; AoE damage 186 / 176; party status 0 / 170.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `water_dark_electric_technique_lv5_drowned_thunder` | Drowned Thunder | `["water", "water", "dark", "dark", "electric"]` | damage | none | 192 | 180 | no | A crushing blow that drags the foe under like a black current, then discharges. |
| `electric_water_ice_technique_lv5_stormsurge_hammer` | Stormsurge Hammer | `["electric", "electric", "water", "water", "ice"]` | damage | none | 186 | 176 | yes | A two-handed slam that sends a freezing, electrified wave across the field. |
| `ice_air_water_technique_lv5_hailstorm_rend` | Hailstorm Rend | `["ice", "ice", "air", "air", "water"]` | damage | none | 192 | 180 | no | A whirling cut that carries a storm of hail through the target. |
| `water_fire_dark_technique_lv5_boiling_abyss_strike` | Boiling Abyss Strike | `["water", "water", "fire", "fire", "dark"]` | damage | none | 192 | 180 | no | A scalding, steam-wreathed blow from somewhere much deeper than the user. |
| `light_water_air_technique_lv5_tidal_resolve` | Tidal Resolve | `["light", "light", "water", "air", "air"]` | status | `attack_buff`, `strength_buff`, `regen` | 0 | 170 | yes | A battle cry that rolls over the party like a rising tide. |
| `earth_ice_water_technique_lv5_glacial_landslide` | Glacial Landslide | `["earth", "earth", "ice", "ice", "water"]` | damage | none | 186 | 176 | yes | A ground-splitting stomp that buries the field under frozen rubble. |
| `electric_air_fire_technique_lv5_thunderclap_cyclone` | Thunderclap Cyclone | `["electric", "electric", "air", "air", "fire"]` | damage | none | 186 | 176 | yes | A spinning sweep that tears the air open with thunder and sparks. |
| `dark_light_electric_technique_lv5_eclipse_discharge` | Eclipse Discharge | `["dark", "dark", "light", "light", "electric"]` | damage | none | 192 | 180 | no | Light and shadow collide in the blade, then break loose all at once. |
| `ice_electric_air_technique_lv5_frozen_thunder_drop` | Frozen Thunder Drop | `["ice", "ice", "electric", "electric", "air"]` | status | `stun`, `defense_debuff` | 5 | 175 | no | A leaping axe-drop that freezes and jolts the target where it stands. |
| `fire_electric_light_technique_lv5_sunforge_overdrive` | Sunforge Overdrive | `["fire", "fire", "electric", "electric", "light"]` | status | `attack_buff`, `attack_buff`, `elemental_attack_buff`, `strength_buff` | 0 | 170 | no | The user stokes body and weapon to a white-hot charge before the big hit. |
| `dark_ice_air_technique_lv5_black_blizzard_rush` | Black Blizzard Rush | `["dark", "dark", "ice", "air", "air"]` | damage | none | 192 | 180 | no | A charging assault through a whiteout of black snow. |
| `earth_fire_dark_technique_lv5_cinderpit_collapse` | Cinderpit Collapse | `["earth", "earth", "fire", "dark", "dark"]` | damage | none | 186 | 176 | yes | The ground caves into a burning pit beneath every foe. |
| `light_dark_earth_technique_lv5_twilight_guillotine` | Twilight Guillotine | `["light", "light", "dark", "dark", "earth"]` | damage | none | 194 | 178 | no | A falling execution strike that lands at the line between day and night. |

Technique was short on every element (only 6 L5 moves). Two are buffs: **Sunforge Overdrive** is a self-buff built for a big physical finisher (it follows the physical-buff rules), and **Tidal Resolve** is a party buff. **Frozen Thunder Drop** is the one control move.

### 11.2 Spirit (9)

Current L5 spirit norms: party status 0 / 160–190; AoE heal 125 / 148; cure 60 / 180.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `ice_dark_electric_spirit_lv5_winter_requiem` | Winter Requiem | `["ice", "ice", "dark", "dark", "electric"]` | status | `sleep`, `intelligence_debuff` | 0 | 175 | yes | A cold funeral hymn that sends every foe into a numbed sleep. |
| `electric_ice_dark_spirit_lv5_purging_current` | Purging Current | `["electric", "electric", "ice", "ice", "dark"]` | cure | `stun`, `sleep`, `confuse`, `silence` | 0 | 170 | yes | A clean jolt of holy current that snaps allies out of every stupor. |
| `electric_ice_fire_spirit_lv5_thunderfrost_blessing` | Thunderfrost Blessing | `["electric", "electric", "ice", "ice", "fire"]` | status | `elemental_attack_buff`, `elemental_attack_buff`, `attack_buff` | 0 | 165 | yes | A blessing that charges every weapon with storm, frost and flame. |
| `ice_dark_earth_spirit_lv5_grave_frost` | Grave Frost | `["ice", "ice", "dark", "dark", "earth"]` | status | `constitution_debuff`, `defense_debuff`, `dexterity_debuff` | 5 | 170 | no | The chill of the grave settles into a foe and does not leave. |
| `electric_dark_fire_spirit_lv5_judgment_storm` | Judgment Storm | `["electric", "electric", "dark", "dark", "fire"]` | damage | none | 165 | 170 | yes | Divine wrath falls as a storm of black lightning and fire. |
| `ice_earth_electric_spirit_lv5_glacier_ward` | Glacier Ward | `["ice", "ice", "earth", "earth", "electric"]` | status | `defense_buff`, `elemental_defense_buff`, `constitution_buff` | 0 | 170 | yes | A shell of blessed ice and stone forms around the party. |
| `ice_fire_dark_spirit_lv5_pale_pyre` | Pale Pyre | `["ice", "ice", "fire", "dark", "dark"]` | damage | none | 192 | 180 | no | A cold, colorless flame that burns from the inside. |
| `light_electric_dark_spirit_lv5_eclipse_mending` | Eclipse Mending | `["light", "electric", "electric", "dark", "dark"]` | heal | none | 125 | 148 | yes | Shadow and current knit the whole party back together. |
| `ice_electric_dark_spirit_lv5_silent_aurora` | Silent Aurora | `["ice", "ice", "electric", "electric", "dark"]` | status | `silence`, `stun` | 0 | 180 | no | A shimmering curtain of light falls and leaves the target without voice or motion. |

These fill spirit's ice, electric and dark holes (Rynn, Alden, Ripple, Eldon). Spirit had no L5 damage moves at all; **Judgment Storm** (AoE) and **Pale Pyre** (single target) add two. **Eclipse Mending** is a dark-and-electric party heal, so Ripple, Eldon and Alden get an L5 heal outside light.

### 11.3 Magic (8)

Current L5 magic norms: single-target damage 205–215 power / 185–198 AP; AoE damage 165 / 170; status 0 / 160–185.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `ice_electric_light_magic_lv5_aurora_lance` | Aurora Lance | `["ice", "ice", "electric", "electric", "light"]` | damage | none | 205 | 185 | no | A spear of frozen, charged light drawn from the polar sky. |
| `electric_light_ice_magic_lv5_prism_storm` | Prism Storm | `["electric", "electric", "light", "light", "ice"]` | damage | none | 165 | 170 | yes | A storm of refracted lightning that strikes everything at once. |
| `ice_dark_electric_magic_lv5_black_ice_tempest` | Black Ice Tempest | `["ice", "ice", "dark", "dark", "electric"]` | status | `continuous_damage`, `dexterity_debuff`, `elemental_debuff` | 0 | 165 | yes | A tempest of black ice shards that keeps cutting long after it passes. |
| `water_ice_electric_magic_lv5_frozen_maelstrom` | Frozen Maelstrom | `["water", "water", "ice", "ice", "electric"]` | damage | none | 165 | 170 | yes | A whirlpool that freezes mid-spin and shatters with a crack of thunder. |
| `air_electric_ice_magic_lv5_tempest_rime` | Tempest Rime | `["air", "air", "electric", "electric", "ice"]` | damage | none | 205 | 185 | no | A focused cyclone of frost and lightning that grinds the target down. |
| `fire_ice_electric_magic_lv5_frostfire_arc` | Frostfire Arc | `["fire", "fire", "ice", "ice", "electric"]` | damage | none | 208 | 190 | no | Opposing elements forced into one arc, unstable and devastating. |
| `earth_ice_electric_magic_lv5_glacial_faultline` | Glacial Faultline | `["earth", "earth", "ice", "electric", "electric"]` | status | `stun`, `defense_debuff` | 2 | 185 | no | The ground splits beneath the target and fills with frozen current. |
| `electric_light_fire_magic_lv5_judgment_bolt` | Judgment Bolt | `["electric", "electric", "electric", "light", "fire"]` | damage | none | 215 | 198 | no | A single colossal bolt that strikes like a verdict. |

Magic had **0** L5 electric moves; all 8 now carry electric and 7 carry ice. **Judgment Bolt** is the triple-electric capstone nuke for Moxie and Sylvara. Aurora Lance, Prism Storm and Judgment Bolt add light for Veyr.

### 11.4 Tech (5)

Current L5 tech norms: single-target damage 200–205 power / 182–186 AP; AoE damage 186 / 182; status 0 / 180–190.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `fire_ice_electric_tech_lv5_thermal_shock_cannon` | Thermal Shock Cannon | `["fire", "fire", "ice", "ice", "electric"]` | damage | none | 205 | 185 | no | A cannon that fires superheated and supercooled rounds in the same instant. |
| `electric_ice_water_tech_lv5_hydro_cryo_railgun` | Hydro-Cryo Railgun | `["electric", "electric", "ice", "water", "water"]` | damage | none | 200 | 182 | no | A rail-driven slug of pressurized water that freezes in flight. |
| `earth_ice_electric_tech_lv5_seismic_cryo_mines` | Seismic Cryo-Mines | `["earth", "earth", "ice", "ice", "electric"]` | damage | none | 186 | 182 | yes | A spread of buried mines that erupt in frozen, electrified shrapnel. |
| `dark_ice_electric_tech_lv5_null_frost_virus` | Null Frost Virus | `["dark", "dark", "ice", "electric", "electric"]` | status | `silence`, `intelligence_debuff`, `elemental_debuff` | 0 | 190 | yes | A cold-running virus that crashes every system it reaches. |
| `ice_light_air_tech_lv5_coolant_halo_drone` | Coolant Halo Drone | `["ice", "ice", "light", "light", "air"]` | status | `regen`, `elemental_defense_buff`, `defense_buff` | 0 | 180 | yes | A hovering drone that wraps the party in a cooling, shielding halo. |

Mainly ice and electric for Lyric, with one each of fire, water, earth and dark. **Coolant Halo Drone** is a party defence move.

### 11.5 Skill (11)

Current L5 skill norms: single-target damage 192 power / 178–180 AP; AoE damage 165 / 170; status 2–5 / 160–175.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `air_ice_electric_skill_lv5_hailspark_cyclone` | Hailspark Cyclone | `["air", "air", "ice", "electric", "electric"]` | damage | none | 165 | 170 | yes | A spinning kick that throws a ring of hail and sparks. |
| `dark_ice_electric_skill_lv5_black_ice_assassination` | Black Ice Assassination | `["dark", "dark", "ice", "ice", "electric"]` | damage | none | 192 | 178 | no | A silent strike from the shadows with a blade of frozen current. |
| `water_ice_electric_skill_lv5_sleetstorm_barrage` | Sleetstorm Barrage | `["water", "water", "ice", "electric", "electric"]` | status | `stun`, `dexterity_debuff` | 2 | 175 | no | A flurry of pressure-point strikes through a curtain of charged sleet. |
| `ice_light_electric_skill_lv5_glintfrost_shuriken_storm` | Glintfrost Shuriken Storm | `["ice", "ice", "light", "electric", "electric"]` | damage | none | 165 | 170 | yes | A storm of glittering ice shuriken that crackle as they land. |
| `earth_ice_fire_skill_lv5_avalanche_roll` | Avalanche Roll | `["earth", "earth", "ice", "ice", "fire"]` | damage | none | 192 | 180 | no | A rolling dive that hits like a landslide of hot stone and ice. |
| `water_dark_ice_skill_lv5_black_tide_freeze` | Black Tide Freeze | `["water", "water", "dark", "ice", "ice"]` | status | `sleep`, `defense_debuff` | 2 | 175 | no | A redirecting throw into dark water that freezes the target still. |
| `electric_fire_light_skill_lv5_sunspark_blitz` | Sunspark Blitz | `["electric", "electric", "fire", "light", "light"]` | damage | none | 192 | 180 | no | A blinding, lightning-fast rush of strikes from every side. |
| `earth_electric_dark_skill_lv5_grounded_volt_snare` | Grounded Volt Snare | `["earth", "electric", "electric", "dark", "dark"]` | status | `strength_debuff`, `dexterity_debuff`, `silence` | 3 | 170 | yes | A web of charged wire springs from the ground and binds every foe. |
| `water_fire_light_skill_lv5_steam_mirage` | Steam Mirage | `["water", "water", "fire", "light", "light"]` | status | `dexterity_buff`, `dexterity_buff`, `attack_buff` | 0 | 160 | yes | A veil of shining steam that hides the party's every move. |
| `fire_dark_air_skill_lv5_ashen_gust_ambush` | Ashen Gust Ambush | `["fire", "fire", "dark", "dark", "air"]` | damage | none | 192 | 178 | no | A sudden gust of black ash, and the user is already behind the target. |
| `earth_water_light_skill_lv5_dawn_tide_kata` | Dawn Tide Kata | `["earth", "water", "water", "light", "light"]` | status | `dexterity_buff`, `defense_buff`, `regen` | 0 | 165 | no | A flowing morning form that steadies body and breath. |

Skill was short on every element. Ice and electric get 6 new moves each (Poise, Dare). **Black Tide Freeze** is a water-and-dark aikido-style throw that suits Ghost. **Steam Mirage** and **Dawn Tide Kata** are the buffs; **Grounded Volt Snare** is the smoke-bomb-style AoE control move.

### 11.6 Batch 2 verification

1. 46 new L5 seeds exist with unique IDs and names (no clash with existing moves or Batch 1), and all compile.
2. Every new move has exactly 5 element entries and at most 3 different elements.
3. Every class has **at least 8 moves per element at L5** (shared pool only). Expected counts after Batch 2, in the order fire / ice / water / earth / air / electric / light / dark:
   - Technique 8 / 8 / 8 / 9 / 8 / 8 / 8 / 8
   - Spirit 8 / 8 / 9 / 8 / 9 / 8 / 12 / 8
   - Magic 12 / 8 / 13 / 13 / 14 / 8 / 8 / 10
   - Tech 8 / 8 / 8 / 8 / 11 / 8 / 12 / 8
   - Skill 8 / 8 / 8 / 8 / 8 / 8 / 8 / 8
4. No new move mixes beneficial and harmful statuses, and every status key is valid (§4).
5. Cure moves list the statuses they remove in `status_keys` (Purging Current: stun, sleep, confuse, silence), matching how existing cures work.
6. No player ability is orphaned (§8 check 3), and the element validator reports 0 warnings.
7. Spot check in game at a high enough level: Moxie and Sylvara see Judgment Bolt; Rynn sees Winter Requiem; Ghost sees Black Tide Freeze; Chock sees Sunforge Overdrive.

---

## 12. Batch 3: Level 4 (34 shared moves + 1 Ghost signature move)

Every new L4 move has **4 element entries using at most 3 different elements**. Repeated entries are deliberate stacks; keep them exactly as listed. Shared moves go in `level_4_abilities_by_type/<class>.py`, above the non-player block if there is one.

Kōri no Kansetsu's display name keeps the macron (`"name": "Kōri no Kansetsu"`), and its ID uses plain `o`. Save the file as UTF-8.

### 12.1 Technique (5)

Current L4 technique norms: single-target damage 140–146 power / 117–120 AP; AoE damage 108 / 126; party status 0 / 105.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `ice_dark_electric_technique_lv4_blackfrost_rend` | Blackfrost Rend | `["ice", "ice", "dark", "electric"]` | damage | none | 144 | 119 | no | A frozen, crackling cut that leaves the wound black with cold. |
| `ice_light_electric_technique_lv4_aurora_cleaver` | Aurora Cleaver | `["ice", "light", "light", "electric"]` | damage | none | 142 | 118 | no | A shining overhead chop that flashes like the northern lights. |
| `water_ice_electric_technique_lv4_stormfloe_sweep` | Stormfloe Sweep | `["water", "water", "ice", "electric"]` | damage | none | 108 | 126 | yes | A wide sweep that throws a wave of charged ice floes across the field. |
| `light_ice_dark_technique_lv4_pale_vigil` | Pale Vigil | `["light", "light", "ice", "dark"]` | status | `defense_buff`, `elemental_defense_buff` | 0 | 105 | yes | The party sets its feet like a frozen wall at dusk. |
| `fire_earth_air_technique_lv4_furnace_gale_breaker` | Furnace Gale Breaker | `["fire", "fire", "earth", "air"]` | damage | none | 146 | 120 | no | A furnace-hot blow driven home by a roaring wind. |

Mostly ice and electric, plus light and dark for Warden, Drax, Vek and Thorn. **Pale Vigil** is the one party buff.

### 12.2 Spirit (8)

Current L4 spirit norms: single heal 150 / 132; AoE heal 122 / 135; damage 112–135 / 110–118; status 0–1 / 110–115.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `ice_dark_electric_spirit_lv4_hoarfrost_penance` | Hoarfrost Penance | `["ice", "ice", "dark", "electric"]` | status | `intelligence_debuff`, `silence` | 1 | 115 | no | A cold rebuke that freezes the words in a foe's throat. |
| `electric_ice_dark_spirit_lv4_stormglass_judgment` | Stormglass Judgment | `["electric", "electric", "ice", "dark"]` | damage | none | 130 | 112 | no | A pane of frozen lightning shatters over the condemned. |
| `ice_earth_electric_spirit_lv4_frozen_bedrock_ward` | Frozen Bedrock Ward | `["ice", "earth", "earth", "electric"]` | status | `defense_buff`, `constitution_buff` | 0 | 110 | yes | Blessed stone and ice rise to brace every ally. |
| `ice_earth_electric_spirit_lv4_glacier_mend` | Glacier Mend | `["ice", "ice", "earth", "electric"]` | heal | none | 150 | 132 | no | Clean glacial cold closes even deep wounds. |
| `ice_air_electric_spirit_lv4_snowsquall_litany` | Snowsquall Litany | `["ice", "air", "air", "electric"]` | status | `dexterity_buff`, `intelligence_buff` | 0 | 110 | yes | A brisk, chanted prayer that quickens body and mind. |
| `ice_fire_electric_spirit_lv4_frostfire_vigil` | Frostfire Vigil | `["ice", "fire", "electric", "electric"]` | status | `elemental_attack_buff`, `attack_buff` | 0 | 110 | yes | A vigil flame that burns cold and arms the party with it. |
| `ice_air_light_spirit_lv4_winters_embrace` | Winter's Embrace | `["ice", "ice", "air", "light"]` | heal | none | 122 | 135 | yes | A soft snowfall that settles over the party and soothes every hurt. |
| `ice_water_light_spirit_lv4_thawing_grace` | Thawing Grace | `["ice", "water", "water", "light"]` | cure | `continuous_damage`, `dexterity_debuff`, `strength_debuff` | 0 | 120 | yes | A spring thaw that washes away lingering harm. |

Spirit had **0** L4 ice moves; all 8 now carry ice (Rynn), and 6 carry electric (Alden). The set covers spirit's whole toolkit: heals (**Glacier Mend**, **Winter's Embrace**), a cure (**Thawing Grace**), three party buffs, a debuff and a damage move.

### 12.3 Magic (4)

Current L4 magic norms: single-target damage 140–144 power / 110–121 AP; AoE status 15 / 125–145.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `light_water_ice_magic_lv4_moonlit_glacier` | Moonlit Glacier | `["light", "light", "water", "ice"]` | damage | none | 142 | 120 | no | A glacier of moonlit water forms above the target and drops. |
| `water_light_electric_magic_lv4_halo_torrent` | Halo Torrent | `["water", "water", "light", "electric"]` | damage | none | 140 | 118 | no | A ring of shining, charged water closes around the target. |
| `fire_water_light_magic_lv4_scalding_halo` | Scalding Halo | `["fire", "water", "light", "light"]` | status | `continuous_damage`, `attack_debuff` | 15 | 125 | yes | A crown of boiling light settles over every foe. |
| `ice_electric_light_magic_lv4_polar_flash` | Polar Flash | `["ice", "electric", "light", "light"]` | damage | none | 144 | 121 | no | A blinding polar flare that freezes and shocks at once. |

All 4 carry light, filling Veyr's L4 gap, plus water, ice and electric.

### 12.4 Tech (9)

Current L4 tech norms: single-target damage 122–130 power / 110–118 AP; AoE damage 105 / 120–122; status 0–25 / 120–132.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `water_ice_electric_tech_lv4_supercooled_arc_jet` | Supercooled Arc Jet | `["water", "water", "ice", "electric"]` | damage | none | 128 | 115 | no | A jet of supercooled water that carries current all the way in. |
| `earth_ice_water_tech_lv4_frostbore_drill` | Frostbore Drill | `["earth", "earth", "ice", "water"]` | damage | none | 130 | 118 | no | A cryo-cooled drill bit that bores straight through armour. |
| `fire_water_ice_tech_lv4_thermal_cycler` | Thermal Cycler | `["fire", "water", "ice", "ice"]` | status | `dexterity_debuff`, `defense_debuff` | 20 | 120 | yes | A device that flash-heats and flash-freezes the area until everything cracks. |
| `air_ice_earth_tech_lv4_blizzard_turbine` | Blizzard Turbine | `["air", "air", "ice", "earth"]` | damage | none | 105 | 120 | yes | A deployed turbine that blasts the field with gravel and sleet. |
| `ice_dark_electric_tech_lv4_cryo_void_taser` | Cryo-Void Taser | `["ice", "dark", "electric", "electric"]` | status | `stun`, `intelligence_debuff` | 25 | 132 | no | A black-cased taser that freezes the nervous system mid-thought. |
| `water_earth_fire_tech_lv4_geyser_mortar` | Geyser Mortar | `["water", "water", "earth", "fire"]` | damage | none | 105 | 122 | yes | A mortar round that erupts into a scalding geyser on landing. |
| `water_electric_air_tech_lv4_hydro_storm_turret` | Hydro-Storm Turret | `["water", "electric", "electric", "air"]` | damage | none | 128 | 115 | no | An auto-turret that fires bolts of charged, wind-driven water. |
| `earth_fire_dark_tech_lv4_slag_shrapnel_bomb` | Slag Shrapnel Bomb | `["earth", "fire", "fire", "dark"]` | damage | none | 105 | 120 | yes | A bomb packed with molten slag and black-iron shrapnel. |
| `earth_electric_air_tech_lv4_lightning_rod_array` | Lightning Rod Array | `["earth", "electric", "air", "air"]` | status | `elemental_defense_buff`, `defense_buff` | 0 | 120 | yes | A ring of grounding rods that draws hostile energy away from the party. |

Tech had the smallest L4 pool of any class (10 moves). These add ice and water for Lyric and Kade, earth and fire for Bragg, Voss and Spark, and dark for Grimnaw.

### 12.5 Skill (8)

Current L4 skill norms: AoE damage 100–116 power / 115–128 AP; status 0–15 / 120.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `ice_electric_air_skill_lv4_kori_no_kansetsu` | Kōri no Kansetsu | `["ice", "ice", "electric", "air"]` | status | `stun`, `dexterity_debuff` | 15 | 120 | no | Joint of Ice. A freezing joint lock that locks the limb, then the whole body. |
| `ice_electric_dark_skill_lv4_frostvolt_feint` | Frostvolt Feint | `["ice", "electric", "dark", "dark"]` | status | `confuse`, `defense_debuff` | 0 | 120 | yes | A feint so cold and quick that foes strike at where the user used to be. |
| `ice_electric_fire_skill_lv4_sparkfrost_fan` | Sparkfrost Fan | `["ice", "ice", "electric", "fire"]` | damage | none | 105 | 120 | yes | A thrown war fan that trails frost and sparks. |
| `ice_electric_water_skill_lv4_sleet_step` | Sleet Step | `["ice", "electric", "water", "water"]` | status | `dexterity_buff`, `elemental_defense_buff` | 0 | 120 | yes | The party moves like sleet in the wind: hard to see and harder to hit. |
| `ice_electric_earth_skill_lv4_hailstrike_combo` | Hailstrike Combo | `["ice", "electric", "electric", "earth"]` | damage | none | 112 | 125 | yes | A chain of strikes that lands like hail on stone. |
| `ice_electric_light_skill_lv4_glimmer_frost_kunai` | Glimmer Frost Kunai | `["ice", "electric", "light", "light"]` | damage | none | 108 | 122 | yes | A spread of gleaming, frost-edged kunai. |
| `ice_electric_air_skill_lv4_thunderstep_chill` | Thunderstep Chill | `["ice", "electric", "electric", "air"]` | status | `dexterity_buff`, `attack_buff` | 0 | 120 | yes | A crackling cold rhythm that quickens every ally's step and strike. |
| `ice_electric_dark_skill_lv4_numbing_needle_rain` | Numbing Needle Rain | `["ice", "ice", "electric", "dark"]` | status | `sleep`, `intelligence_debuff` | 15 | 120 | yes | A rain of chilled needles that dulls nerves until foes drop. |

Skill had **0** L4 ice and **0** L4 electric moves; all 8 carry both. **Kōri no Kansetsu** (氷の関節, "joint of ice") is Poise's freezing joint lock. It is single-target, unlike most skill L4 moves, because a lock holds one person. **Sleet Step** adds water for Ghost.

### 12.6 Ghost signature move: Undertow Turn

This is a **signature move**, not part of the shared pool, so it does not count toward the §9 targets. It is Ghost's water aikido move: he takes the foe's own momentum and turns it into the throw.

File: `game/region_seeds/player_abilities/unique_character_abilities.py`, after `lv4_unique_ability_skill_ghost_void_efface`. Follow the same format as Ghost's other signature moves, including `"non_player_ability": True`.

```python
    {
        "id": "lv4_unique_ability_skill_ghost_undertow_turn",
        "name": "Undertow Turn",
        "description": "Ghost meets the attack, gives way like water, and turns the foe's own momentum into a crushing throw.",
        "ability_type": "skill", "level": 4,
        "elements": ["water", "water", "dark", "air"],
        "base_power": 112, "ap_cost": 120, "effect": "damage",
        "can_aoe": False,
        "non_player_ability": True,
    },
```

Then add `'lv4_unique_ability_skill_ghost_undertow_turn'` to the end of Ghost's `abilities` list in `game/region_seeds/extended_characters.py` (about line 664), after `void_efface`.

Power uses the top of the skill L4 damage range because it hits only one target. Ghost's remaining aikido ideas (Windmill Throw, Borrowed Momentum, Six-Step Shadow) are still open for a later signature-move pass.

### 12.7 Batch 3 verification

1. 34 new shared L4 seeds and 1 Ghost signature move exist with unique IDs and names (no clash with existing moves or Batches 1–2), and all compile.
2. Every new move has exactly 4 element entries and at most 3 different elements.
3. Every class has **at least 8 moves per element at L4** (shared pool only). Expected counts after Batch 3, in the order fire / ice / water / earth / air / electric / light / dark:
   - Technique 8 / 8 / 8 / 12 / 9 / 8 / 8 / 8
   - Spirit 8 / 8 / 12 / 8 / 8 / 8 / 18 / 8
   - Magic 8 / 8 / 8 / 8 / 8 / 8 / 8 / 13
   - Tech 8 / 8 / 8 / 9 / 8 / 8 / 10 / 8
   - Skill 21 / 8 / 22 / 27 / 30 / 8 / 27 / 21
4. No new move mixes beneficial and harmful statuses, and every status key is valid (§4).
5. Kōri no Kansetsu shows its macron correctly in the ability list and combat log.
6. Ghost joins with 5 signature moves, including Undertow Turn.
7. No player ability is orphaned (§8 check 3), and the element validator reports 0 warnings.

---

## 13. Batch 4: Level 3 (20 moves)

Every new L3 move has **3 element entries using at most 2 different elements**. Repeated entries are deliberate stacks; keep them exactly as listed. Seeds go in `level_3_abilities_by_type/<class>.py`, above the non-player block if there is one. Spirit already meets every L3 target, so it gets nothing in this batch.

### 13.1 Technique (5)

Current L3 technique norms: single-target damage 95 power / 85 AP; AoE damage 78 / 98; self status 0 / 80.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `light_ice_technique_lv3_hoarlight_slash` | Hoarlight Slash | `["light", "light", "ice"]` | damage | none | 95 | 85 | no | A gleaming cut that leaves a line of frost behind it. |
| `light_fire_technique_lv3_sunbrand_strike` | Sunbrand Strike | `["light", "light", "fire"]` | damage | none | 95 | 85 | no | A blow that sears a mark of light into the target. |
| `light_earth_technique_lv3_bastion_oath` | Bastion Oath | `["light", "earth", "earth"]` | status | `defense_buff`, `constitution_buff` | 0 | 80 | no | A sworn stance that roots the user like a fortress wall. |
| `light_dark_technique_lv3_duskfall_sweep` | Duskfall Sweep | `["light", "dark", "dark"]` | damage | none | 78 | 98 | yes | A wide sweep that drags the last light of dusk across every foe. |
| `light_air_technique_lv3_skyglint_cleave` | Skyglint Cleave | `["light", "light", "air"]` | damage | none | 95 | 85 | no | A leaping cleave that flashes like sunlight off a high blade. |

All carry light (Warden, Drax, Chock); Hoarlight Slash also adds ice for Kor'in. **Bastion Oath** is a self-guard buff.

### 13.2 Magic (7)

Current L3 magic norms: single-target damage 95–100 power / 85–90 AP; AoE damage 85 / 95; status 3 / 85 single or 0 / 89 AoE.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `light_fire_magic_lv3_solar_lance` | Solar Lance | `["light", "light", "fire"]` | damage | none | 95 | 85 | no | A lance of sunfire hurled straight through the target. |
| `light_ice_magic_lv3_diamond_dust` | Diamond Dust | `["light", "ice", "ice"]` | damage | none | 85 | 95 | yes | A glittering storm of frozen light that cuts everything it touches. |
| `light_water_magic_lv3_mirror_tide` | Mirror Tide | `["light", "water", "water"]` | status | `confuse` | 3 | 85 | no | A shimmering wave shows the target a reflection it cannot trust. |
| `light_earth_magic_lv3_crystal_spire` | Crystal Spire | `["light", "earth", "earth"]` | damage | none | 95 | 85 | no | A spire of glowing crystal erupts beneath the target. |
| `light_air_magic_lv3_dazzling_gale` | Dazzling Gale | `["light", "light", "air"]` | status | `attack_debuff`, `dexterity_debuff` | 0 | 89 | yes | A bright, whirling wind that blinds and staggers every foe. |
| `light_electric_magic_lv3_ion_halo` | Ion Halo | `["light", "electric", "electric"]` | damage | none | 85 | 95 | yes | A ring of charged light expands and burns through the field. |
| `light_dark_magic_lv3_eclipse_bolt` | Eclipse Bolt | `["light", "dark", "dark"]` | damage | none | 100 | 90 | no | A bolt of darkness rimmed with burning light. |

Magic L3 had only 1 light move. Each new move pairs light with one other element, so Veyr gains 7 options and every other magic element reaches 8.

### 13.3 Tech (1)

Current L3 tech norms: status 8 power / 67 AP single target.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `light_dark_tech_lv3_umbral_floodlight` | Umbral Floodlight | `["light", "dark", "dark"]` | status | `scanned`, `defense_debuff` | 8 | 67 | no | A dark-spectrum floodlight that exposes every weak point. |

Tops up light and dark.

### 13.4 Skill (7)

Current L3 skill norms: AoE damage 54–55 power / 65 AP; single-target status 3–13 / 86–90.

| ID | Name | Elements | Effect | Status keys | Power | AP | AoE | Description |
|---|---|---|---|---|---|---|---|---|
| `light_fire_skill_lv3_flare_palm` | Flare Palm | `["light", "light", "fire"]` | damage | none | 54 | 65 | yes | A palm strike that bursts into a flash of burning light. |
| `light_ice_skill_lv3_glacier_glint` | Glacier Glint | `["light", "ice", "ice"]` | status | `dexterity_debuff`, `attack_debuff` | 13 | 86 | no | A flash of light off a blade of ice, aimed straight at the eyes. |
| `light_water_skill_lv3_moonwater_step` | Moonwater Step | `["light", "water", "water"]` | status | `dexterity_buff`, `regen` | 0 | 86 | no | A calm, flowing step taken like moonlight on water. |
| `light_earth_skill_lv3_glass_grit_toss` | Glass Grit Toss | `["light", "earth", "earth"]` | status | `attack_debuff` | 3 | 86 | no | A handful of glittering grit that blinds a foe mid-swing. |
| `light_air_skill_lv3_sunwind_flurry` | Sunwind Flurry | `["light", "light", "air"]` | damage | none | 55 | 65 | yes | A flurry of strikes so fast they glint like wind-blown sunlight. |
| `light_electric_skill_lv3_flash_wire_snare` | Flash-Wire Snare | `["light", "electric", "electric"]` | status | `stun` | 5 | 90 | no | A glinting wire snaps tight and jolts the target rigid. |
| `light_dark_skill_lv3_shadowlight_feint` | Shadowlight Feint | `["light", "dark", "dark"]` | status | `confuse` | 4 | 90 | no | A feint of light and shadow that leaves a foe striking at nothing. |

Same pattern as magic: light paired with each other element, for Nia, Andrea and Poise. **Moonwater Step** gives Ghost another water option.

### 13.5 Batch 4 verification

1. 20 new L3 seeds exist with unique IDs and names (no clash with existing moves or Batches 1–3), and all compile.
2. Every new move has exactly 3 element entries and at most 2 different elements.
3. Every class has **at least 8 moves per element at L3**. Expected counts after Batch 4, in the order fire / ice / water / earth / air / electric / light / dark:
   - Technique 10 / 8 / 9 / 9 / 10 / 8 / 8 / 9
   - Magic 8 / 8 / 8 / 8 / 8 / 8 / 8 / 8
   - Tech 9 / 9 / 9 / 9 / 9 / 9 / 8 / 8
   - Skill 8 / 8 / 8 / 8 / 8 / 8 / 8 / 8
   - Spirit unchanged (already at or above 8 everywhere)
4. No new move mixes beneficial and harmful statuses, and every status key is valid (§4).

---

## 14. Final check: all four batches together

After Batches 1–4, the shared player pool grows from **503 to 642 moves** (+139: 39 at L1–2, 20 at L3, 34 at L4, 46 at L5). Ghost's Undertow Turn is a signature move and is not counted.

Run this once after everything is in:

1. **Every class meets every target:** at least 2 moves per element at L1, and at least 8 per element at L2, L3, L4 and L5 (shared pool only, signature moves excluded). Expected result: 0 shortfalls across all 5 classes × 5 levels × 8 elements.
2. Every move's element-entry count equals its level (§9.2).
3. Every player ability can be learned by at least one character (§8 check 3), using the new element map from §1.
4. No duplicate IDs or names across `PLAYER_ABILITY_SEEDS` and `unique_character_abilities.py`.
5. The element validator reports 0 warnings, and `python -m compileall game tui` passes.
6. Play-through spot check: start a new game, level a core character to 13 and confirm they see 8 Level 1 options (2 per element across their 4 elements). Recruit any two-element character and confirm their ability list shows options at every unlocked level.
