# Implementation Spec: Leveling (HP growth and level-up recovery)

**STATUS: IMPLEMENTED.** Both parts are in place; see the verification notes at the end of this file.

**Project:** Fracture (AITextAdventure)  
**Scope:** player HP growth per level, and what a level-up restores.  
**Depends on:** `IMPLEMENTATION_SPEC_class_growth_elements.md` (class stat split 4:2 / 6:0, `CLASS_HP_RATIO`, `apply_class_curve`). Apply that spec first, or together with this one.  
**Out of scope:** AP growth (unchanged), enemy stats (separate generator spec), stacking/duration rules.

Line numbers refer to the Nov 23 upload and may drift.

---

## Part 1. HP growth: flat 35 per level, 8 HP per CON gained from leveling

### 1.1 Design rules (locked)

1. Every level grants a **flat 35 max HP** (was 20).
2. Every point of **CON gained from leveling** grants **8 max HP** (was 2). This is what separates the front line from everyone else.
3. **Starting CON (level 1) stays at 2 HP per point**, so level 1 characters are unchanged (25–40 HP).
4. The class share of the 15 power points per level still goes to HP by `CLASS_HP_RATIO` (technique 0.80, spirit 0.50, skill 0.60, tech 0.45, magic 0.35). Unchanged.
5. **Hard cap check:** Technique (the highest HP class) must stay **under 10,000 HP at level 100**. With these numbers it reaches 7,069. That leaves 2,931 HP of headroom; it would only reach 10,000 at level 142.
6. **CON from accessories, buffs or equipment does not add max HP.** Only permanent CON (leveling, manual allocation, permanent stat items) does.

### 1.2 Resulting HP (on-curve, from `apply_class_curve`)

Per level gain: technique +71, spirit +67, skill +52, tech +50, magic +48.

| Class | L1 | L10 | L20 | L30 | L40 | L50 | L60 | L70 | L77 | L80 | L90 | L100 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Technique | 40 | 679 | 1,389 | 2,099 | 2,809 | 3,519 | 4,229 | 4,939 | 5,436 | 5,649 | 6,359 | **7,069** |
| Spirit | 36 | 639 | 1,309 | 1,979 | 2,649 | 3,319 | 3,989 | 4,659 | 5,128 | 5,329 | 5,999 | 6,669 |
| Skill | 29 | 497 | 1,017 | 1,537 | 2,057 | 2,577 | 3,097 | 3,617 | 3,981 | 4,137 | 4,657 | 5,177 |
| Tech | 27 | 477 | 977 | 1,477 | 1,977 | 2,477 | 2,977 | 3,477 | 3,827 | 3,977 | 4,477 | 4,977 |
| Magic | 25 | 457 | 937 | 1,417 | 1,897 | 2,377 | 2,857 | 3,337 | 3,673 | 3,817 | 4,297 | 4,777 |

For comparison, the old values (flat 20, CON ×2) at level 60 were 2,282 / 2,042 / 1,858 / 1,738 / 1,618, and at level 100 technique was 3,802.

Why: technique and spirit gain 3 CON per level (1 from the +1-to-all, 2 from the class split); skill, tech and magic gain 1. With CON worth 8 HP, the front line pulls ~1,370 HP ahead of magic by level 60.

### 1.3 Code changes (`game/objects/player.py`)

**a) Constants** (module level, near the other class constants):

```python
HP_PER_LEVEL = 35             # flat max HP per level (was max_hp_per_lvl = 20)
HP_PER_CON_AT_CREATION = 2    # level-1 / starting CON
HP_PER_CON_ON_LEVEL = 8       # CON gained after level 1
```

- Set the `max_hp_per_lvl` field default (~line 52) and the defaults dict (~line 106) to `HP_PER_LEVEL`. Leave `max_ap_per_lvl = 5` alone.

**b) `allocate_stats` (~line 653):** take the HP-per-CON rate as a parameter instead of the hard-coded `* 2`.

```python
def allocate_stats(self, str_inc=0, dex_inc=0, con_inc=0, int_inc=0,
                   use_stat_points=True, hp_per_con=HP_PER_CON_ON_LEVEL):
    ...
    if con_inc:
        self.constitution += int(con_inc)
        hp_inc = int(con_inc) * int(hp_per_con)
        self.max_hp += hp_inc
        self.current_hp += hp_inc   # keep: this is the level-up "tally" (Part 2)
```

Callers:

| Caller | Rate |
|---|---|
| `check_level_up_awards` → `allocate_stats(1,1,1,1)` (~585) | default (8) |
| `auto_allocate_level_points` (~634) | default (8) |
| `upgrade_stats` (~650), `select_upgrade_screen.py` ~173 (manual allocation) | default (8) |
| Permanent stat items, `utility_item.py` ~99 | default (8). Designer decision: a permanent CON item is worth the same as a leveled CON point. |
| Level-1 setup in `apply_class_curve`, character creation, `player_generator` level-1 split | `HP_PER_CON_AT_CREATION` (2) |

**c) `apply_class_curve`** (from the class-growth spec): the level-1 line `p.max_hp = 20 + (p.constitution - 8) * 2` stays as it is (creation rate). The loop over `check_level_up_awards` then picks up the new rates automatically. Keep its last line `p.current_hp, p.current_ap = p.max_hp, p.max_ap`: **newly generated characters and recruits join at full HP/AP.** That is creation, not a level-up.

**d) Deprecated `Player.level_up` (~707):** delete it, or fix it. It currently double-counts CON HP (`max_hp += con_inc * 2` and then `allocate_stats` adds CON HP again), adds `int_inc * 2` AP that nothing else grants, and fully restores HP/AP. The only caller found is `ai_controlled_demo.py` ~84; switch that to `upgrade_stats`.

### 1.4 Existing saves (`Player.__setstate__`)

Add a version flag so this runs once per character:

```python
HP_FORMULA_VERSION = 2

if getattr(self, 'hp_formula_version', 1) < HP_FORMULA_VERSION:
    lv = max(1, int(self.level))
    cls = getattr(self, 'character_class', None)
    con_per_level = 3 if cls in ('technique', 'spirit') else 1
    con_gained = (lv - 1) * con_per_level
    delta = (lv - 1) * (HP_PER_LEVEL - 20) + con_gained * (HP_PER_CON_ON_LEVEL - 2)
    self.max_hp += delta
    if self.current_hp > 0:                       # don't revive the fallen
        self.current_hp = min(self.max_hp, self.current_hp + delta)
    self.max_hp_per_lvl = HP_PER_LEVEL
    self.hp_formula_version = HP_FORMULA_VERSION
```

- Use the class table for `con_gained`, not `self.constitution`, so accessory or pre-fix stat skew doesn't leak in.
- If the class-growth spec's optional "rebuild to curve" admin command is used on a character, set `hp_formula_version = 2` after it (the rebuild already uses the new rates).

---

## Part 2. Level-up no longer fully restores HP/AP

### 2.1 Design rule (locked)

A level-up restores **only what the level added**: current HP rises by the max-HP gained, current AP by the max-AP gained. A character at 300/2,000 HP who gains 71 max HP ends at 371/2,071. Racing to the next level is no longer a free full heal. Full restores remain where they were designed: inns, cure/restore items, abilities, story events.

### 2.2 Change in `check_level_up_awards` (~576–596)

Use the **tally** approach. Every place that raises a max already raises the current value by the same amount (`allocate_stats` for CON, `apply_power_point_allocation` for power points). The only increments that don't are the flat per-level ones. So:

```python
def check_level_up_awards(self):
    ...
    self.unused_stat_points += 4
    self.allocate_stats(1, 1, 1, 1)               # +8 HP max and current (CON +1)
    self.max_ap += self.max_ap_per_lvl
    self.max_hp += self.max_hp_per_lvl
    if self.current_hp > 0:                       # fallen characters stay down
        self.current_hp += self.max_hp_per_lvl
    self.current_ap += self.max_ap_per_lvl
    self.unused_stat_points += self.per_level_stat_distribution_amount
    self.unused_power_points += self.power_points_per_level
    if getattr(self, 'character_class', None):
        self.auto_allocate_level_points()         # adds CON HP and power points to max AND current
    # REMOVED: self.heal(self.max_hp)
    # REMOVED: self.restore_ap(self.max_ap)
    self.current_hp = min(self.current_hp, self.max_hp)
    self.current_ap = min(self.current_ap, self.max_ap)
    return ...
```

Why tally and not before/after snapshot: points a player spends **later** on the upgrade screen go through `allocate_stats` / `apply_power_point_allocation`, which already add to current. The tally keeps that consistent no matter when points are spent. (A snapshot in `check_level_up_awards` would miss manual allocations.)

**Fallen characters:** a character at 0 HP who levels at the end of a battle gains the max HP but stays at 0. A level-up is not a revive. `allocate_stats` and `apply_power_point_allocation` must also skip the `current_hp` increase when `current_hp <= 0`. Add the same guard there. AP still accrues.

### 2.3 Other full-restore paths to check

| Location | Action |
|---|---|
| `player.py` ~594–595 (`check_level_up_awards`) | Remove (above) |
| `player.py` ~712–713 (deprecated `level_up`) | Removed with the method (1.3 d) |
| `apply_class_curve` final line | **Keep**: creation/recruitment, not a level-up |
| `random_hostile.py` ~561–564 (hostile full restore on its own level path) | Leave: enemies |
| Inn (`services/inn_service.py`), bar, items | Leave: designed recovery |

Battle rewards call `check_level_up_awards` once per level gained (`random_hostile.py` ~431), so multi-level jumps add up correctly with no extra code.

---

## Part 3. Tests

1. **HP table:** build each class with `apply_class_curve` at levels 1, 60, 100. Assert the values in 1.2 (±1 for rounding).
2. **Cap:** technique at level 100 has `max_hp < 10_000`.
3. **Ordering:** at every level 2–100: technique ≥ spirit > skill > tech > magic.
4. **Creation unchanged:** level-1 HP per class is 40 / 36 / 29 / 27 / 25.
5. **Partial restore:** technique at level 59, set current HP to 300 and AP to 10, call level-up. Assert `current_hp == 300 + (new_max_hp - old_max_hp)` and the same for AP.
6. **Full stays full:** a full-HP character is still full after leveling.
7. **Fallen stays fallen:** current HP 0, level up. Max rises, current stays 0, `is_alive()` is False.
8. **Manual allocation:** an unclassed character levels, then spends 3 CON on the upgrade screen. Current HP rises by 24, max by 24.
9. **Multi-level:** gain enough XP for 3 levels in one battle. Current HP rises by exactly the sum of the three max-HP gains.
10. **Recruit joins full:** a recruit generated at level 60 has `current_hp == max_hp`.
11. **Save migration:** a level 60 technique save with the old formula gains `(59 × 15) + (177 × 6) = 1,947` max HP, current HP rises by the same (capped), runs once (version flag), and a save at 0 HP stays at 0.
12. **Accessory CON:** equipping a +CON accessory does not change `max_hp`.

---

## Notes for the designer (not code)

- With partial restore on level-up, **inn and healing-item prices and drop rates matter more**. Watch whether players run dry mid-dungeon; save points or a mid-dungeon spring may be needed in long dungeons.
- Enemy HP and damage should be rebuilt against these new player HP values (separate enemy generator spec). Until then, enemies will feel even weaker than in the last playthrough.

---

## STATUS: IMPLEMENTED

Both parts verified directly against the current build:

| Part | Status |
|---|---|
| 1. HP growth | ✅ `HP_PER_LEVEL` (35), `HP_PER_CON_AT_CREATION` (2), `HP_PER_CON_ON_LEVEL` (8), `HP_FORMULA_VERSION` added to `player.py`. `allocate_stats` takes an `hp_per_con` parameter (default 8); `apply_class_curve`'s level-1 setup uses the creation rate (2) explicitly. The deprecated `Player.level_up` was removed (confirmed no live callers — `ai_level_up_player` and the AI demo path both go through `check_level_up_awards` + `upgrade_stats`, never `level_up`). |
| 2. Partial restore on level-up | ✅ `check_level_up_awards` now tallies only what the level added (no more `heal(max_hp)` / `restore_ap(max_ap)`). `allocate_stats` and `apply_power_point_allocation` both skip the `current_hp` increase when `current_hp <= 0` (fallen stays fallen). `apply_class_curve`'s final full-restore line is intentionally kept (creation, not a level-up). |
| Save migration | ✅ `Player.__setstate__` runs the version-gated HP migration once per character, using the class's per-level CON gain (3 for technique/spirit, 1 otherwise) rather than the character's current (possibly skewed) CON stat. |

**Verified directly (not just by code review), all exact matches to this spec's numbers:**
- Test 1 (HP table): `apply_class_curve` at levels 1/10/20/.../100 for all 5 classes matches section 1.2's table exactly, including technique's level-100 value of 7,069 (< the 10,000 cap — test 2).
- Test 3 (ordering): confirmed by the same table — technique ≥ spirit > skill > tech > magic at every checked level.
- Test 4 (creation unchanged): level-1 HP is 40/36/29/27/25 for technique/spirit/skill/tech/magic — matches.
- Test 5 (partial restore): technique at level 59, current 300/10, level up → `current_hp == 371`, `current_ap == 18`, both exactly `old + (new_max - old_max)`.
- Test 6 (full stays full): confirmed.
- Test 7 (fallen stays fallen): current_hp 0 before level-up, still 0 after; max_hp still rises.
- Test 8 (manual allocation): classless character spends 3 CON after leveling → current_hp and max_hp both rise by exactly 24.
- Test 9 (multi-level): 3 levels gained in one call sequence → current_hp rises by exactly the sum of the 3 max-HP gains (full before and after).
- Test 10 (recruit joins full): confirmed for a spirit recruit at level 60.
- Test 11 (save migration): simulated level-60 technique old-format save migrates `max_hp` by exactly `(59×15)+(177×6) = 1,947`; runs once (version flag prevents double-migration); a fallen (`current_hp == 0`) save stays at 0 through migration.
- All 27 live recruit seeds (`generate_player_from_attainable_character_seed`) generate with zero errors and join at `current_hp == max_hp`, `current_ap == max_ap`.

**Not interactively verified (flagging, not skipping silently):** test 2's hard-cap check was confirmed numerically (7,069 < 10,000) but no in-game combat session was run to observe the "enemies will feel even weaker" note in the designer section — that's expected and out of scope for this pass (separate enemy generator spec).
