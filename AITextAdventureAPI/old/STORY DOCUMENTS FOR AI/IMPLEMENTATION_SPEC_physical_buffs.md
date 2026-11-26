# Fracture: Physical Hits, Attack Buffs and Elemental Imbue Implementation Spec

**STATUS: IMPLEMENTED.** All sections applied, including the combat-log immunity messaging. Superseded in one respect by `IMPLEMENTATION_SPEC_pr39-41_followups.md` section 1, which extends physical stacking to basic attacks as well.

**Scope:** make `attack_buff` and `elemental_attack_buff` apply only to physical hits, stop buff elements leaking into non-physical abilities, make element immunity block the whole hit, and set the rules for giving player abilities a `physical` slot.

Checked against the build uploaded 2026-11-25. Line numbers are approximate.

**Design intent (from the designer):**
- Technique hits once, hits hard, is relentless. Skill hits fast and precisely and sets things up.
- The core combo: skill chips away with physical + element strikes that stack `elemental_debuff` on the enemy. Technique stacks `attack_buff` and `elemental_attack_buff` on itself, then lands a physical Level 5 finisher that cashes in every stack.
- **No stack cap.** Stacks are bounded only by duration.

---

## 1. Rules

| Modifier | Basic attack | Ability **with** a `physical` slot | Ability **without** `physical` |
|---|---|---|---|
| `attack_buff` / `attack_debuff` (attacker) | Yes | Yes | **No** |
| `elemental_attack_buff` bonus (attacker) | Yes | Yes | **No** (change) |
| Buff elements added to the hit ("imbue") | Yes | Yes | **No** (change) |
| Armor (target) | Yes | Yes | No |
| `defense_buff` / `defense_debuff` (target) | Yes | Yes | No |
| `elemental_debuff` / `elemental_defense_buff` (target) | By the hit's elements | By the hit's elements, **including imbued ones** | By the ability's own elements |
| Element immunity / weakness / resistance (target) | By the hit's elements | By the hit's elements, **including imbued ones** | By the ability's own elements |

**Imbued elements are real elements of the hit.** A physical/ice strike imbued with fire is a physical/ice/fire hit:
- it gets the fire bonus from the attacker's `elemental_attack_buff`,
- it matches fire `elemental_debuff` stacks on the target,
- a **fire-immune target takes 0 from the whole hit** (section 4).

That's the trade-off of imbuing: more damage against most targets, nothing against the wrong one.

---

## 2. Bug: buff elements are added to every ability today

`status_utils.collect_attack_elements` appends every `elemental_attack_buff` element onto the ability's elements. Both `PlayerAbility` damage paths call it for every ability, then decide physical-ness from the combined list:

```python
# player_ability.py ~317 (and the AoE path ~379)
elems = status_utils.collect_attack_elements(owner, <ability elements>)
is_physical_hit = self._is_physical_hit(elems)
power = status_utils.compute_outgoing_damage(owner, power, elems, is_basic_attack=is_physical_hit)
```

Effects today:
1. A fire buff turns an ice **spell** into ice + fire, so it gets the fire bonus and is checked against fire immunity.
2. A buff whose elements include `physical` would make **every** ability physical (armor, attack_buff, defense_debuff all switch on).
3. `compute_outgoing_damage` applies `elemental_attack_buff` regardless of physical-ness (the comment at ~142 says so).

---

## 3. Code changes

### 3.1 `PlayerAbility` damage paths (`player_ability.py` ~317 and ~379)

Replace the three lines in **both** places with:

```python
own = [str(getattr(e, 'value', e)).lower() for e in (self.elements or [])]
is_physical_hit = self._is_physical_hit(own)            # decide from the ability itself, never from buffs
elems = (status_utils.collect_attack_elements(owner, own)  # imbue only physical hits
         if is_physical_hit else own)
power = status_utils.compute_outgoing_damage(owner, power, elems, is_physical=is_physical_hit)
```

`elems` (imbued for physical hits) keeps flowing into `target.take_damage(..., elements=elems, physical=is_physical_hit)` unchanged, so imbued elements reach the target's debuffs and immunity checks.

### 3.2 `compute_outgoing_damage` (`status_utils.py` ~110)

- Rename the parameter `is_basic_attack` → `is_physical` and update the docstring: it means "basic attack or ability with a physical slot".
- Gate the elemental bonus:

```python
elif sid == 'elemental_attack_buff' and elements and is_physical:
```

- Update the 4 callers:
  - `player.py` ~435: `is_physical=True`
  - `random_hostile.py` ~257: `is_physical=True`
  - `player_ability.py` ~322 and ~381: covered by 3.1

### 3.3 `collect_attack_elements` (`status_utils.py` ~258)

No logic change. Add to the docstring: "Only call for physical hits; non-physical abilities use their own elements."

### 3.4 Leave `compute_power` alone (decision recorded)

`PlayerAbility.compute_power` (~109) still multiplies by `1 + 0.35 × len(self.elements)`, on top of the level multiplier `1 + 0.20 × (level − 1)`. Because a Level N ability has N slots, this is a second level-based scaling (Level 5 = 1.8 × 2.75 ≈ 4.95× base power).

- It reads **the ability's own slots only**. Imbued elements do **not** raise it, and should not: the imbue is already paid for through the `elemental_attack_buff` bonus and the target's `elemental_debuff` matches. Counting it here too would triple-dip.
- If you later decide to simplify the double scaling, do it in a separate balance pass. Don't change it in this spec.

---

## 4. Whole-hit element immunity (current code is share-based)

The agreed rule was: **if any element of the hit is immune, the whole hit deals 0.** `status_utils.elemental_multiplier` (~32) currently **skips** immune slots and averages the rest, so a physical/ice/fire hit on a fire-immune target deals 2/3 instead of 0.

Fix:

```python
def elemental_multiplier(elements, immunities=None, weaknesses=None, resistances=None) -> float:
    els = [str(getattr(e, 'value', e)).lower() for e in (elements or [])]
    if not els:
        return 1.0
    imm = {str(e).lower() for e in (immunities or [])}
    if any(e in imm for e in els):
        return 0.0                      # any immune slot blocks the whole hit
    weak = {str(e).lower() for e in (weaknesses or [])}
    res = {str(e).lower() for e in (resistances or [])}
    total = 0.0
    for e in els:
        m = 1.0
        if e in weak:
            m *= WEAKNESS_MULT
        if e in res:
            m *= RESISTANCE_MULT
        total += m
    return total / len(els)             # weak/resist stay share-based
```

Both `Player.take_damage` and `RandomHostile.take_damage` already call this, so one change covers both sides.

**Combat log:** when this returns 0 because of immunity, log something like `"Fire-immune! The strike has no effect."` so the player learns why the imbued hit did nothing.

---

## 5. Giving player abilities a `physical` slot

No player ability has `physical` today, so technique's finishers get nothing from `attack_buff`. Retagging and new abilities belong to the new-abilities pass, but these rules must hold:

1. **`physical` counts as one of the N slots.** A Level N ability still has exactly N elements, e.g. Level 5 `['physical', 'fire', 'fire', 'earth', 'light']`. Hostile Velvet Veil abilities already follow this.
2. **The element gate ignores `physical`.** No character has `physical` in `elements_base`, so a player ability with `physical` must also carry at least one real element to be learnable. That means **no pure-physical Level 1 player abilities.** In `can_learn` (character elements spec), drop `physical` from the ability's elements before the gate check:
   ```python
   ab_elems = {_val(e) for e in (get('elements') or [])} - {'physical'}
   if base and not base & ab_elems:
       return False
   ```
3. **Who gets physical:** technique heavy hitters (finishers, power strikes) and skill strikes (the chip-and-expose combos). Spirit, magic and tech stay non-physical unless a specific ability calls for it.
4. **Physical abilities are reduced by armor.** That's intended: the brawler trades armor penetration for buff scaling.
5. Update the startup validator: a player ability whose only element is `physical` is an error.

---

## 6. Stacking without a cap: what to expect

No cap, by design. Known behaviour so balancing isn't surprised by it:

- **Imbue stacks grow faster than linearly.** Each `elemental_attack_buff` status adds its elements to the hit, and each status's bonus is `magnitude × 0.01 × (attack_count × status_count)`. With k fire imbue stacks on a physical/fire hit, the fire attack count is 1 + k, and k statuses each pay on it, so the attacker-side bonus grows with k × (1 + k): roughly with the **square** of the stack count.
- **Target-side debuffs multiply on top.** `elemental_debuff` also scales by attack_count × status_count, and imbued elements raise attack_count. Attacker and target modifiers multiply each other.
- **Imbuing dilutes weak/resist.** Weak/resist are averaged over slots, so extra imbued fire slots water down an ice weakness on the target.

**Number limits: none needed.** Python integers have no byte limit, and floats only overflow near 10^308; damage is turned back into an `int` every hit. Two cosmetic guards are worth adding:
- **Overkill:** clamp applied damage to the target's current HP when reporting/logging, if you don't want "dealt 4,812,330" on a 20k-HP enemy. (Optionally still show the raw number for fun.)
- **Display width:** format large numbers (e.g. `4.8M`) in the combat log/renderer so the layout doesn't break.

Only code that hands numbers to fixed-width types (numpy, a typed DB column, a compiled extension) would need a hard clamp. None exists in the combat path today.

---

## 7. Tests

1. Basic attack with `attack_buff` → boosted. Non-physical ability with `attack_buff` → not boosted.
2. Ability with a `physical` slot and `attack_buff` → boosted.
3. Non-physical ice spell with a fire `elemental_attack_buff` → elements passed to `take_damage` are exactly `['ice']`; no elemental bonus applied.
4. Physical/ice ability with a fire `elemental_attack_buff` → elements include `fire`; elemental bonus applied.
5. Same hit as 4 against a **fire-immune** target → 0 damage, immunity message logged.
6. Same hit as 4 against a target with a fire `elemental_debuff` → debuff bonus applies (imbued fire matches).
7. A buff whose elements include `physical` does **not** make a non-physical ability physical (no armor, no attack_buff).
8. `elemental_multiplier(['ice','fire'], immunities=['fire'])` → 0.0; `(['ice','fire'], weaknesses=['ice'])` → share-based value unchanged from today.
9. `compute_power` for a physical/ice Level 2 ability is identical with and without a fire imbue active.
10. `can_learn`: a technique character with earth can learn `['physical','earth']`; nobody can learn `['physical']` alone; the validator flags a pure-physical player ability.
11. Hostile basic attacks still get `attack_buff` and `elemental_attack_buff` (`random_hostile.py` caller updated).
12. 20 stacks of `elemental_attack_buff` + 20 stacks of `elemental_debuff` on one physical finisher: no exception, result is an `int`, combat log formats it within the layout.
