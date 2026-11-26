# Fracture: PR #39–#41 Follow-up Fixes

**Scope:** the fixes decided after the review of PRs #39, #40 and #41 (see `REVIEW_PR39-41.md`).
**Checked against:** the build uploaded 2026-11-25. Paths are relative to `AITextAdventureAPI/old/`; line numbers are approximate.
**Works with:** `IMPLEMENTATION_SPEC_physical_buffs.md`, `IMPLEMENTATION_SPEC_class_growth_elements.md` (Part 1), `IMPLEMENTATION_SPEC_leveling.md`, `IMPLEMENTATION_SPEC_character_text_fixes.md`.

| # | Fix | Type |
|---|---|---|
| 1 | Every physical hit carries at least one `physical` stack, so physical resistance and weakness apply to basic attacks | Code |
| 2 | Abilities are either fully beneficial or fully harmful; fix the 5 mixed ones | Data + small code |
| 3 | Voss Caldera: AP, stats and header (she is a tech user) | Data |
| 4 | Chapter 14: remove Tess's reference to the deleted cargo-hold scene | Story |
| 5 | Every recruit follows the class stat curve; no special cases | Code + data |
| 6 | Skill stat requirement written as two entries, like spirit and tech | Data |
| 7 | Nihilist Camp spawns in the Shallows mid-city's **region** | Story |
| 8 | Brute Knuckle description says "Resists earth" to match its data | Data |
| 9 | `continuous_damage` expires like `regen` instead of lasting until cured | Data (1 line) |

---

## 1. Physical is an element stack on every physical hit

### 1.1 Rules (locked)

1. **A basic attack is one stack of `physical`.** Hostile and player basic attacks alike.
2. **An ability carries as many `physical` stacks as it has `physical` slots** (e.g. `['physical', 'physical', 'fire']` = 2 stacks). Unchanged from the physical-buffs spec.
3. `physical` is resolved per stack by `elemental_multiplier`, exactly like any other element. Multiple physical stacks against a physical resistance or weakness stack the same way multiple fire stacks do.
4. Imbued elements (from `elemental_attack_buff`) are added on top of the physical stack on physical hits (physical-buffs spec).

### 1.2 Code

**`status_utils.py`** — add:

```python
PHYSICAL_ELEMENT = 'physical'

def with_physical_stack(elements, physical: bool) -> list:
    """Normalize a hit's elements; a physical hit always carries >= 1 'physical' stack.

    Basic attacks arrive with no 'physical' element (only imbues, if any), so
    they gain exactly one stack here. Abilities with physical slots already
    carry their own stacks and are left as they are.
    """
    els = [str(getattr(e, 'value', e)).lower() for e in (elements or [])]
    if physical and PHYSICAL_ELEMENT not in els:
        els.insert(0, PHYSICAL_ELEMENT)
    return els
```

**`objects/random_hostile.py` `take_damage` (~119)** and **`objects/player.py` `take_damage` (~378)** — first line after the `amount <= 0` check:

```python
elements = status_utils.with_physical_stack(elements, physical)
```

Everything below already uses `elements`, so `elemental_multiplier` and `compute_incoming_damage` both see the physical stack. Do it inside `take_damage` (not at the callers) so every physical hit is covered, whoever calls it. The armor block and durability loss stay gated on the `physical` flag as they are.

### 1.3 Results (`WEAKNESS_MULT` 1.5, `RESISTANCE_MULT` 0.5)

| Hit | Elements after normalizing | Target | Multiplier |
|---|---|---|---|
| Basic attack | `physical` | resists physical | 0.50 (was 1.0) |
| Basic attack | `physical` | weak to physical | 1.50 (was 1.0) |
| Basic attack, fire imbue | `physical, fire` | resists physical, weak to fire | 1.00 |
| Compliance Slam | `physical, earth, electric, dark` | resists physical, weak to electric | 1.00 |
| 2-physical ability | `physical, physical, fire` | resists physical | 0.67 |
| Fireball (not physical) | `fire` | resists physical | 1.00 (unchanged) |

### 1.4 Knock-on effects (intended)

- **129 hostile seeds** resist `physical`. Basic attacks against them now do half damage. That is the point of the resistance, but expect those fights to run longer for technique and skill.
- **Skill → technique combo:** an `elemental_debuff` applied by a skill ability with a `physical` slot stamps `physical` into the debuff's elements. Every later physical hit (basic or ability) now matches it in `compute_incoming_damage`, so a skill user's chip strikes open the target up for the technique user's basics and finisher.
- **Player side:** an accessory with `'physical'` in `resistances` now halves incoming hostile basic attacks. None has it today. **Brute Knuckle** keeps `resistances: ['earth']`; its description is corrected in section 8.

Out of scope: basic attacks still ignore the equipped weapon's elements. Leave as is unless you want weapons to imbue.

---

## 2. Beneficial or harmful: one or the other

### 2.1 Rule (locked)

A status ability is **either entirely beneficial** (every key is a `*_buff` or `regen`, cast on the caster's side) **or entirely harmful** (no buff or regen key, cast on the enemy). No ability mixes the two.

### 2.2 Code: `PlayerAbility._is_beneficial_ability` (`objects/player_ability.py` ~455)

Today it returns True if **any** key is a buff, and it never counts `regen`. Make it "all keys beneficial", with `regen` included:

```python
BENEFICIAL_STATUS_PATTERNS = ('*_buff', 'regen')

if eff == EffectType.STATUS:
    keys = [str(getattr(k, 'value', k)).lower() for k in (self.status_keys or [])]
    return bool(keys) and all(self._matches_patterns(k, list(BENEFICIAL_STATUS_PATTERNS)) for k in keys)
```

With the data below fixed, no current ability changes target because of this. It stops a future mixed ability from silently flipping sides, and a regen-only ability now goes to allies instead of the enemy.

### 2.3 Data fixes (`region_seeds/player_abilities/`)

| Ability (file ~line) | Owner | `status_keys` before → after |
|---|---|---|
| `light_dark_skill_lv2_shattered_reflection_pose` (`level_2_abilities_by_type/skill.py` ~82) | Mirror Dancer | `dexterity_buff, dexterity_debuff` → **`dexterity_debuff, confuse`** |
| `dark_fire_air_spirit_lv3_encore_of_ruin` (`level_3_abilities_by_type/spirit.py` ~119) | Masquerader | `continuous_damage, defense_debuff, regen` → **`continuous_damage, defense_debuff, constitution_debuff`** |
| `contradiction_loop` (`level_5_abilities_by_type/tech.py` ~16) | Crux | `confuse, silence, attack_buff` → **`confuse, silence, attack_debuff`** |
| `earth_fire_water_air_skill_lv4_quake_stride` (`level_4_abilities_by_type/skill.py` ~5) | player | `defense_debuff, dexterity_debuff, attack_debuff, regen` → **`defense_debuff, dexterity_debuff, attack_debuff`** |
| `light_dark_air_water_skill_lv4_dusk_shimmer` (`level_4_abilities_by_type/skill.py` ~28) | player | `intelligence_debuff, attack_debuff, dexterity_debuff, regen` → **`intelligence_debuff, attack_debuff, dexterity_debuff`** |

Descriptions that change to match (Quake Stride and Dusk Shimmer never mentioned regen, so theirs stay):

| Ability | New `description` |
|---|---|
| Shattered Reflection | `The Mirror Dancer strikes a theatrical pose, splintering its image into mocking copies until the target loses its footing and can no longer tell which dancer is real.` |
| Encore of Ruin | `Demanding one more performance than the body can give, the Masquerader whips the crowd into a frenzy that burns through every foe present, cracking their guard and wearing their bodies down.` |
| Contradiction Loop | `Crux identifies an irresolvable logical contradiction in his target and feeds it back endlessly — every response the target gives only deepens the trap, until the mind stalls, the voice fails and every blow falters.` |

The Contradiction Loop text **replaces** its row in `IMPLEMENTATION_SPEC_character_text_fixes.md` section 4.3 (it already uses "his").

---

## 3. Voss Caldera

Voss is **female** and a **tech** user (INT primary, DEX secondary), as mapped in `CHARACTER_NPC_CLASS_MAP` and as all her unique abilities are typed. Her profile and story text are already correct; her equipment descriptions are covered in `IMPLEMENTATION_SPEC_character_text_fixes.md` section 5.

`region_seeds/extended_characters.py`, Voss's stat block (~686–700):

| Field | Before | After |
|---|---|---|
| header line 2 (~687) | `# ESTJ · 3w4 · corporate brawler — STR primary, CON secondary, brawler` | `# ESTJ · 3w4 · corporate operator — INT primary, DEX secondary, tech` |
| `strength` / `dexterity` / `constitution` / `intelligence` | 52 / 130 / 52 / 186 | **57 / 159 / 57 / 259** |
| `max_hp` / `current_hp` | 934 | **2,477** |
| `max_ap` / `current_ap` | **5** | **650** |

650 AP is what the tech curve gives at level 50 (section 5); it is in the 500–600+ range a level-50 tech user should have. Her maul and plate can stay as flavour.

---

## 4. Chapter 14: Tess's opening line

#39 removed the Chapter 13 cargo-hold scene. `region_seeds/main_story/main_story_chapter_14.py` ~181, dialog `tess_ch14_intro`, first line:

| Before | After |
|---|---|
| `Before you start: yes, we were in the cargo hold. Yes, Seth threatened to throw us overboard. No, he didn't.` | `Before you ask: we got here on our own. You're not the only ones who can follow money across an ocean.` |

The rest of her lines and Sam's `sam_ch14_intro` ("We're still following the Grift Stone trail…") stand on their own.

---

## 5. Every recruit follows the class curve

### 5.1 Rule (locked)

Recruits are not special cases. Every recruited character's stats, HP and AP come from their class rule at their join level: 8 base + the class level-1 split, then per level +1 to all stats, +6 split by class (4:2, magic 6:0), 15 power points split by `CLASS_HP_RATIO`, +5 AP, and the leveling spec's HP (35 per level + 8 per leveled CON).

| Class | Primary | Secondary |
|---|---|---|
| technique | STR +4 | CON +2 |
| spirit | INT +4 | CON +2 |
| tech | INT +4 | DEX +2 |
| skill | DEX +4 | STR +2 |
| magic | INT +6 | — |

### 5.2 Code

This is `apply_class_curve` from `IMPLEMENTATION_SPEC_class_growth_elements.md` section 1.3c, called on recruits as in 1.3e. If that is already in, nothing new is needed here. If not, implement it now:

- In `generate_player_from_attainable_character_seed` (`objects/player.py` ~722), after `populate_from_json(seed)` and resolving `character_class`, call `apply_class_curve(p, cls, seed['level'])`.
- Then reset `unused_ability_slots` to the seed's value and attach equipment and starting abilities as today.

### 5.3 Data: write the curve into the seeds

So the data says what the game does (and future AI agents don't "fix" it back), replace the hand-written values with these. They apply to every recruit, not only the late joiners. Under the rule everyone gains about 10 stat points per level (6 split + the +1 to all), so **every** recruit rises; the late joiners were only "high" compared with hand-written numbers that were all too low.

Where each stat block lives (under `region_seeds/`). Set `current_hp`/`current_ap` equal to `max_hp`/`max_ap`.

| Recruits | File |
|---|---|
| sable, thorn, bragg, ripple, kor_in, grimnaw, nia | `primary_stories/<region>/<region>_primary_story.py` (desert, forest, mountains, shallows, snow, swamp, grassland) |
| lyren / vek / warden_hale / seraphine | `main_story/main_story_chapter_7.py` / `_11.py` / `_15.py` / `_19.py` |
| the 16 extended characters | `extended_characters.py` |


| Recruit id | Class | Level | STR | DEX | CON | INT | Max HP | Max AP | Was (STR/DEX/CON/INT, HP, AP) |
|---|---|---|---|---|---|---|---|---|---|
| `bragg` | tech | 30 | 37 | 99 | 37 | 159 | 1,477 | 390 | 38/102/38/158, 941 HP, 350 AP |
| `grimnaw` | tech | 30 | 37 | 99 | 37 | 159 | 1,477 | 390 | 38/102/38/158, 941 HP, 350 AP |
| `kor_in` | technique | 30 | 159 | 37 | 99 | 37 | 2,099 | 240 | 158/38/102/38, 1,169 HP, 250 AP |
| `nia` | skill | 30 | 99 | 159 | 37 | 37 | 1,537 | 330 | 93/169/38/38, 941 HP, 350 AP |
| `ripple` | spirit | 30 | 37 | 37 | 99 | 159 | 1,979 | 360 | 38/38/102/158, 1,019 HP, 400 AP |
| `sable` | magic | 30 | 37 | 37 | 37 | 221 | 1,417 | 450 | 38/38/38/224, 891 HP, 400 AP |
| `thorn` | technique | 30 | 159 | 37 | 99 | 37 | 2,099 | 240 | 158/38/102/38, 1,169 HP, 250 AP |
| `lyren` | spirit | 35 | 42 | 42 | 114 | 184 | 2,314 | 420 | 40/40/140/180, 1,120 HP, 360 AP |
| `commander_drax` | technique | 40 | 209 | 47 | 129 | 47 | 2,809 | 320 | 148/14/72/18, 748 HP, 150 AP |
| `eldon_dawnseer` | spirit | 40 | 47 | 47 | 129 | 209 | 2,649 | 480 | 20/26/86/120, 436 HP, 305 AP |
| `ghost` | skill | 40 | 129 | 209 | 47 | 47 | 2,057 | 440 | 80/110/30/32, 424 HP, 245 AP |
| `regent_sylvara` | magic | 40 | 47 | 47 | 47 | 291 | 1,897 | 600 | 20/20/64/142, 432 HP, 305 AP |
| `spark_maddox` | tech | 40 | 47 | 129 | 47 | 209 | 1,977 | 520 | 30/130/24/68, 502 HP, 155 AP |
| `veyr_ashcant` | magic | 40 | 47 | 47 | 47 | 291 | 1,897 | 600 | 22/24/68/138, 440 HP, 305 AP |
| `vek` | technique | 50 | 259 | 57 | 159 | 57 | 3,519 | 400 | 200/95/180/95, 1,800 HP, 450 AP |
| `voss_caldera` | tech | 50 | 57 | 159 | 57 | 259 | 2,477 | 650 | 52/130/52/186, 934 HP, 5 AP |
| `dare` | skill | 55 | 174 | 284 | 62 | 62 | 2,837 | 605 | 100/188/56/56, 675 HP, 211 AP |
| `rynn` | spirit | 60 | 67 | 67 | 189 | 309 | 3,989 | 720 | 28/34/110/200, 674 HP, 455 AP |
| `anita` | magic | 65 | 72 | 72 | 72 | 466 | 3,097 | 975 | 66/66/66/210, 789 HP, 395 AP |
| `warden_hale` | technique | 65 | 334 | 72 | 204 | 72 | 4,584 | 520 | 225/100/200/90, 2,000 HP, 500 AP |
| `andrea_starveil` | skill | 70 | 219 | 359 | 77 | 77 | 3,617 | 770 | 120/240/70/70, 860 HP, 267 AP |
| `talon` | spirit | 80 | 87 | 87 | 249 | 409 | 5,329 | 960 | 30/44/148/270, 900 HP, 605 AP |
| `alden_brightvein` | spirit | 85 | 92 | 92 | 264 | 434 | 5,664 | 1,020 | 32/46/158/286, 958 HP, 642 AP |
| `seraphine` | spirit | 85 | 92 | 92 | 264 | 434 | 5,664 | 1,020 | 120/200/280/400, 2,400 HP, 840 AP |
| `lira_emberforge` | technique | 95 | 484 | 102 | 294 | 102 | 6,714 | 760 | 460/95/300/95, 1,289 HP, 399 AP |
| `lyric` | tech | 95 | 102 | 294 | 102 | 484 | 4,727 | 1,235 | 95/140/95/340, 997 HP, 717 AP |
| `osten_dreamweaver` | magic | 100 | 107 | 107 | 107 | 711 | 4,777 | 1,500 | 100/100/100/600, 1,074 HP, 755 AP |

Notes:
- HP assumes `IMPLEMENTATION_SPEC_leveling.md` (35 per level, 8 per leveled CON). If that spec isn't in yet, the stat and AP columns are still exact; HP will come out lower until it is.
- Stale header comments to update while editing: **Ghost** ("STR primary, DEX secondary" → "DEX primary, STR secondary, skill"), **Lira** ("DEX primary, STR secondary, agile" → "STR primary, CON secondary, technique"), **Voss** (section 3).
- Tier unlocks: with the requirement scale from the class-growth spec, each recruit can use the ability tiers their level allows, the same as the core five.

---

## 6. Skill requirement format

Skill is now a two-stat class, so write it the same way as spirit and tech: one dict per stat.

`region_seeds/player_abilities/ability_requirements.py`:

```python
# before
{"ability_type": "skill", "required_stats_per_ability_level": [{"dexterity": 13, "strength": 9  }]},
# after
{"ability_type": "skill", "required_stats_per_ability_level": [{"dexterity": 13}, {"strength": 9}]},
```

Make the same change to the copy in the `hostile_seed_engine.py` docstring (~558).

Player gating doesn't change (both shapes mean "meet every stat"). The hostile ability picker now scores skill the same way as spirit and tech.

---

## 7. Nihilist Camp location

`region_seeds/main_story/main_story_chapter_11.py` ~955:

```python
# before
{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'nihilist_camp', 'location': 'shallows_mid_city_open_area' }}
# after
{ 'event_type': 'create_dungeon', 'params': { 'dungeon_id': 'nihilist_camp', 'location': 'shallows_mid_city_region_open_area' }}
```

`_get_location_region_area_from_params` (`services/task_completion_service.py` ~436) finds `shallows` + `mid_city`, resolves the Shallows mid city, then sees `_region` (without `region_city`) and climbs to that city's parent region. Same pattern as `grassland_mid_city_region_open_area` elsewhere.

---

## 8. Brute Knuckle description

`game/constants_accesories.py` ~152. The data stays `resistances: ['earth']` (a level-9 item that halved every basic attack would be too strong once section 1 lands). Only the text changes:

```python
# before
'description': 'A weighted knuckle guard that adds raw force to every swing. Resists physical, weak to electric.',
# after
'description': 'A weighted knuckle guard that adds raw force to every swing. Resists earth, weak to electric.',
```

---

## 9. Damage over time expires like regen

### 9.1 Problem

`continuous_damage` in `game/constants_other.py` ~293 has `"duration_per_level": -1`. `PlayerAbility` (`objects/player_ability.py` ~207–225) turns that into `duration = -1`, and both `tick_statuses` methods (`objects/player.py` ~339, `objects/random_hostile.py` ~493) keep a `-1` status forever. Each cast appends a new descriptor, so stacks never fall off and there is no ceiling on how many can build up. Only a cure (Balm, a cleanse, a dispel) removes them.

### 9.2 Fix (locked)

Give it the same lifecycle as `regen` and every other timed status:

```python
"continuous_damage": {
    "id": "continuous_damage",
    "display": "Cont Dmg",
    "name": "Continuous Damage",
    "type": "continuous damage",
    "duration_per_level": 2,      # was -1; same as regen
    "magnitude_per_level": 0.5,
    "min_damage_per_turn": 1,
},
```

No code change is needed. The existing path already gives `duration = max(1, int(level + 2))`, applies the caster's `percent_reduction`, and `tick_statuses` counts it down and drops it at 0. Stacks now wear off one by one, so the number active at once is limited by cast rate against duration, as with regen.

### 9.3 New durations (before `percent_reduction`)

| Ability level | Turns | Target resists `continuous_damage` (halved) | Target weak (×1.5) |
|---|---|---|---|
| 1 | 3 | 1 | 4 |
| 2 | 4 | 2 | 6 |
| 3 | 5 | 2 | 7 |
| 4 | 6 | 3 | 9 |
| 5 | 7 | 3 | 10 |

### 9.4 Knock-on effects (intended)

- **Resistance and weakness now matter.** `add_status` only halves a duration above 1 and never extends `-1`, so today `continuous_damage` in `resistances` or `weaknesses` does nothing. After the fix, the hostiles in `murkchannel_run` and `abandoned_ruin_ch2` that resist it, and any accessory that does, get shorter DoTs. Immunity is unchanged (still blocked).
- **Balm and cleanses** still remove it early; they become a choice rather than the only way out.
- **Dev TUI valuation:** no change. `ability_value_calculator.py` values `continuous_damage` and `regen` the same way (base `STATUS_WEIGHTS` entry plus a capped per-level bonus) and never reads duration. Its base weight is 8.0 against regen's 6.0; you may want to bring them closer now that both expire the same way (optional).
- **Existing saves:** a DoT already sitting on a character with `turns_remaining: -1` stays until cured. If statuses are saved, the loader can convert any `continuous_damage` with `-1` to 3 turns; otherwise nothing is needed.
- `petrify` and `scanned` remain permanent (`-1`); this change is only for `continuous_damage`.

---

## 10. Verification

1. Basic attack (no buffs) on a hostile with `resistances: ['physical']`: the multiplier is 0.5. With `weaknesses: ['physical']`: 1.5.
2. Basic attack with a fire `elemental_attack_buff` on a target that resists physical and is weak to fire: 1.0.
3. A non-physical spell on a physical-resistant target: unchanged.
4. A hostile basic attack on a player gets the same physical stack (both `take_damage` paths).
5. `take_damage(..., physical=False)` (DoT ticks, spells) never gains a physical stack.
6. Crux casts Contradiction Loop: the player is confused and silenced and gets `attack_debuff`; Crux gets nothing.
7. The Masquerader casts Encore of Ruin: no regen on the party.
8. `_is_beneficial_ability()` is True for `['attack_buff', 'regen']`, False for `['regen', 'silence']`, True for `['regen']`.
9. Recruit Voss: 650 AP, INT 259, DEX 159. Recruit Lira at 95: STR 484, CON 294.
10. Skill ability list for a skill character is the same before and after section 6.
11. Chapter 11: the Nihilist Camp appears in the Shallows region outside the mid city, not inside it.
12. Chapter 14 plays with no mention of the cargo hold.
13. Brute Knuckle's tooltip reads "Resists earth, weak to electric."
14. A level-3 DoT applied to a hostile with no resistance shows 5 turns, deals its tick each turn and is gone after 5 ticks.
15. Cast the same DoT three turns running: three stacks, then they drop off one per turn in the order applied, with no stack left after the last one runs out.
16. Against a hostile that resists `continuous_damage`, a level-3 DoT lasts 2 turns.

---

## STATUS: IMPLEMENTED (2026-11-25 follow-up pass)

All ten sections of this spec are implemented and verified against the current build:

| # | Fix | Status |
|---|---|---|
| 1 | Physical element stack on every physical hit | ✅ `status_utils.with_physical_stack` added; wired into `objects/player.py` and `objects/random_hostile.py` `take_damage` |
| 2 | Beneficial/harmful ability split | ✅ `_is_beneficial_ability` rewritten to require all status keys to be beneficial; all 5 listed abilities' `status_keys`/descriptions fixed |
| 3 | Voss Caldera stats | ✅ header, stats, HP, AP updated in `extended_characters.py` |
| 4 | Chapter 14 Tess line | ✅ cargo-hold reference removed in `main_story_chapter_14.py` |
| 5 | Recruit class curve | ✅ Data (5.3): all 27 recruits' stat blocks (STR/DEX/CON/INT, max_hp, max_ap) rewritten to the table's exact values, across `primary_stories/{grassland,shallows,desert,forest,mountains,snow,swamp}`, `main_story_chapter_{7,11,15,19}.py` and `extended_characters.py`. Ghost/Lira/Voss stale header comments corrected. Code (5.2): no pre-existing `apply_class_curve` found anywhere in the codebase; **not implemented** this pass since every current recruit's values are now hand-written exactly per the table — revisit only if/when `IMPLEMENTATION_SPEC_class_growth_elements.md` Part 1 lands and dynamic (non-seeded) recruit generation is needed. |
| 6 | Skill requirement as two entries | ✅ `ability_requirements.py` and the `hostile_seed_engine.py` docstring copy both updated |
| 7 | Nihilist Camp location | ✅ `main_story_chapter_11.py` dungeon location changed to `shallows_mid_city_region_open_area` |
| 8 | Brute Knuckle description | ✅ text now says "Resists earth, weak to electric" (data unchanged) |
| 9 | `continuous_damage` duration | ✅ `duration_per_level` changed from `-1` to `2` in `constants_other.py` |
| 10 | Verification | ✅ Checklist items 1, 2, 3, 5, 6, 7, 8, 9 confirmed by direct script execution (physical stack multipliers, Contradiction Loop/Encore of Ruin status_keys, `_is_beneficial_ability` True/False/True, Voss/Lira stat values). Items 10–16 (hostile ability-picker parity, chapter dialog playthrough, tooltip text, DoT tick/stack timing in a live combat) were not run in an interactive session and should be spot-checked in-game. |

**Known follow-up:** `apply_class_curve` is still unimplemented in code. If a future spec (e.g. dynamically-leveled recruits, or the class-growth spec's Part 1) needs it, add it to `objects/player.py` near `auto_allocate_level_points` and wire it into `generate_player_from_attainable_character_seed` as section 5.2 describes.
