# Fracture: Character Elements Implementation Spec

**STATUS: IMPLEMENTED.** `CHARACTER_NPC_ELEMENT_MAP`, `elements_base`, `can_learn`/`player_class_of`/helpers, the startup validator, and the learn-overlay UI are all in place and the validator reports zero warnings.

**Scope:** give every character an element set (`elements_base`) and make the ability list, learning, the character generator and AI leveling all respect it.
This is Part 2 of `IMPLEMENTATION_SPEC_class_growth_elements.md`, pulled out on its own and re-checked against the current build. You can do it **before** the stat-curve work (Part 1). It does not depend on it.

**This spec's element map is final and replaces the map in Part 2 of the class growth spec.**

**Out of scope, do NOT implement here:**
- The stat curve and the requirement scale change from 1.5 to 2.1 (Part 1 of the class growth spec).
- New abilities. Section 6 lists the remaining Tier 5 gaps a separate ability spec should fill.
- Elements on hostiles, or elemental resistance/weakness for players. `elements_base` controls **what a character can learn**, nothing else.

---

## 1. Check against the current build (already done)

| Check | Result |
|---|---|
| Every key in `CHARACTER_NPC_CLASS_MAP` has an element entry | 32 / 32 |
| Recruits' starting abilities match their class **and** at least one element (final map below) | 27 / 27 recruits pass, zero violations (this includes the new Velvet Veil abilities) |
| Every class has at least one character for each of the 8 elements | Yes, all 5 classes (see 2.2) |
| Player-learnable abilities carrying `physical` | None. `physical` only appears on hostile abilities (`non_player_ability: True`), e.g. Compliance Slam, Baton Discipline, Suppression Field |

**`physical` is never a character element.** No player ability uses it, so a character with `physical` in `elements_base` would match nothing.

---

## 2. Data

Add to `game/region_seeds/main_characters.py`, directly under `CHARACTER_NPC_CLASS_MAP`. Re-export it from `game/constants.py` next to line 384:

```python
CHARACTER_NPC_ELEMENT_MAP = {
    # core 5 (keyed by class id, which is their npc_id). They start with no
    # abilities and build their whole kit from the pool, so they get 4 elements.
    'technique': ['earth', 'fire', 'water', 'light'],     # Chock
    'spirit':    ['light', 'water', 'fire', 'earth'],     # Kaera
    'magic':     ['fire', 'ice', 'electric', 'dark'],     # Moxie
    'tech':      ['electric', 'light', 'water', 'air'],   # Kade
    'skill':     ['air', 'light', 'ice', 'earth'],        # Poise
    # main-story
    'lyren': ['water', 'earth'], 'vek': ['fire', 'dark'],
    'warden_hale': ['light', 'earth'], 'seraphine': ['light', 'air'],
    # regional
    'nia': ['air', 'light'], 'sable': ['earth', 'air'], 'thorn': ['earth', 'dark'], 'bragg': ['earth', 'fire'],
    'ripple': ['water', 'dark'], 'kor_in': ['ice', 'air'], 'grimnaw': ['dark', 'electric'],
    # extended
    'voss_caldera': ['earth', 'light'], 'rynn': ['water', 'ice'], 'eldon_dawnseer': ['light', 'dark'],
    'regent_sylvara': ['dark', 'electric'], 'ghost': ['dark', 'water'], 'lira_emberforge': ['fire', 'earth'],
    'osten_dreamweaver': ['dark', 'water'], 'lyric': ['electric', 'ice'], 'dare': ['fire', 'electric'],
    'andrea_starveil': ['light', 'fire'], 'veyr_ashcant': ['fire', 'light'], 'spark_maddox': ['electric', 'fire'],
    'anita': ['dark', 'air'], 'talon': ['earth', 'light'], 'alden_brightvein': ['light', 'electric'],
    'commander_drax': ['light', 'electric'],
}
```

```python
# game/constants.py, beside CHARACTER_NPC_CLASS_MAP (line ~384)
CHARACTER_NPC_ELEMENT_MAP = main_characters.CHARACTER_NPC_ELEMENT_MAP
```

Every recruit has exactly 2 elements; the core five have 4.

### 2.1 Design decisions behind the map

- **The core five get 4 elements each.** Recruits join with a 4-ability kit. The core five start with nothing and fill 26 ability slots over 100 levels (1 at the start, +1 every 4 levels), including 4 slots before Tier 2 opens at level 14–15. Four elements give each of them at least 4 Level 1 picks.
- **The main party is light-heavy on purpose.** Across the core five: light 4, dark 1 (Moxie), fire 3, earth 3, water 3, ice 2, electric 2, air 2.
- **Chock and Kaera share the same four elements** (earth, fire, water, light). This is fine: technique and spirit draw from separate pools, so they never compete for the same abilities.
- **Magic may use light** (Veyr). Spirit may use dark (Ripple).
- **Recruit changes from the earlier draft**, each made to fill a class gap. Every recruit's starting kit still matches:

| Recruit | Was | Now | Reason |
|---|---|---|---|
| Vek | earth, electric | earth, dark | Technique needed dark. Order as a leash on what's inside her. |
| Drax | earth, light | light, electric | Keeps electric in technique after Vek's change |
| Ripple | water | water, dark | Spirit needed dark. She drowned and came back. |
| Veyr | fire | fire, light | Magic needed light (stage lights) |
| Lyric | electric, air | electric, ice | Tech needed ice after Kade moved to light |
| Nia | air | air, water | Skill needed water after Poise moved to ice |

### 2.2 Class coverage (characters per element)

| Class | Fire | Water | Earth | Air | Ice | Electric | Light | Dark |
|---|---|---|---|---|---|---|---|---|
| Technique | 2 | 1 | 5 | 1 | 1 | 1 | 3 | 1 |
| Spirit | 1 | 4 | 3 | 1 | 1 | 1 | 5 | 1 |
| Magic | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 4 |
| Tech | 2 | 1 | 2 | 1 | 1 | 4 | 2 | 1 |
| Skill | 2 | 1 | 1 | 2 | 2 | 1 | 2 | 1 |

Every class covers all 8 elements. `physical` is never assigned to a character.

---

## 3. Player field and assignment

### 3.1 Field (`game/objects/player.py`)

- Add under `character_class` (line 78):
  ```python
  elements_base: List[str] = field(default_factory=list)
  ```
- Add `'elements_base': [],` to the `__setstate__` defaults dict (near line 128). While you are there, fix the space-indented `'character_class'` line so the dict is tab-indented throughout.

### 3.2 One helper

Add to `player.py`:

```python
def assign_character_elements(p, char_id=None, overwrite=False) -> None:
    """Set p.elements_base from CHARACTER_NPC_ELEMENT_MAP. Never guesses from class."""
    if getattr(p, 'elements_base', None) and not overwrite:
        return
    emap = getattr(const, 'CHARACTER_NPC_ELEMENT_MAP', {}) or {}
    for key in (char_id, getattr(p, 'npc_id', None), getattr(p, 'id', None)):
        if key and key in emap:
            p.elements_base = list(emap[key])
            return
    p.elements_base = list(getattr(p, 'elements_base', None) or [])
```

Look it up by **id only**. Never fall back to `character_class`. If you did, a custom character with a class but no id would silently inherit a core character's elements. A character not found in the map keeps `[]`, which means "no element gate" (see 4.1).

### 3.3 Call sites (set elements wherever the class is set)

| Where | Line (current) | Change |
|---|---|---|
| `PlayerGame.generate_player_character` | `player_game.py` ~1029, after `player.character_class = atype` | `assign_character_elements(player, char_id=atype, overwrite=True)`. Do this **before** abilities are picked; see 5.1 for passing it into `generate_player`. |
| `PlayerGame.add_pending_character` | ~894 | Delete the redundant `p.character_class = npc_id` (already set by `generate_player_character`). No element call needed. |
| `generate_player_from_attainable_character_seed` | `player.py` ~713 | After the class line: `assign_character_elements(p, char_id=char_id)` |
| `task_completion_service` recruit path | ~664 | After the class line: `assign_character_elements(p, char_id=char_id)` |
| `PlayerGame.add_character` | ~1067 | At the end of the class-inference block: `assign_character_elements(character)` |
| `PlayerGame.__setstate__` backfill | ~2067–2081 | Inside the loop **before** the `continue` for already-classed characters: `assign_character_elements(ch)`. Old saves have classes but no elements, so the backfill must run for them too. |

---

## 4. One gate for listing and learning

### 4.1 `can_learn` (add to `player_ability.py`, near `get_potential_player_abilities`)

```python
ABILITY_REQ_SCALE = 1.5   # Part 1 of the class growth spec changes this to 2.1

def ability_stat_requirement(per_level: int, level: int) -> int:
    per_level = int(per_level)
    return per_level + int((per_level * (level - 1) * ABILITY_REQ_SCALE) ** 1.25)

def _val(x) -> str:
    return str(getattr(x, 'value', x) or '').lower()

def player_class_of(player):
    cls = getattr(player, 'character_class', None)
    if not cls:
        cid = getattr(player, 'npc_id', None) or getattr(player, 'id', None)
        cls = (getattr(const, 'CHARACTER_NPC_CLASS_MAP', {}) or {}).get(cid)
    return _val(cls) if cls else ''

def can_learn(player, ability, check_stats: bool = True) -> bool:
    """Class tree + element set (+ stat requirements). Works for seed dicts and PlayerAbility objects."""
    get = (lambda k: ability.get(k)) if isinstance(ability, dict) else (lambda k: getattr(ability, k, None))
    if get('non_player_ability'):
        return False
    atype = _val(get('ability_type'))
    cls = player_class_of(player)
    if cls and atype != cls:
        return False
    base = {_val(e) for e in (getattr(player, 'elements_base', None) or [])}
    if base and not base & {_val(e) for e in (get('elements') or [])}:
        return False                       # needs at least ONE matching element slot
    if check_stats:
        level = int(get('level') or 1)
        reqs = {e.get('ability_type'): e.get('required_stats_per_ability_level') or []
                for e in ABILITY_TYPE_REQUIREMENTS}
        for req in reqs.get(atype, []):
            for stat, per_level in req.items():
                if int(getattr(player, stat, 0) or 0) < ability_stat_requirement(per_level, level):
                    return False
    return True
```

Rules:
- An ability needs **at least one** element slot matching the character. Duplicates don't matter: `fire, fire, earth` is learnable by any fire **or** earth character.
- An empty `elements_base` means no element restriction (custom character, unknown ids).
- `ability_stat_requirement` gives the class growth spec one place to change the scale later.

### 4.2 Wire it in

| Where | Line (current) | Change |
|---|---|---|
| `get_potential_player_abilities` | `player_ability.py` ~521–560 | Delete the inline `player_class` lookup, class check and requirement loop. Keep the `non_player_ability` and owned skips, then add `if player is not None and not can_learn(player, a): continue` |
| `Player.learn_ability` | `player.py` ~663–676 | Replace the class-only block with `if not can_learn(self, ability, check_stats=False): return False`. Use `check_stats=False` here because the list screen already filters on stats, and the generator (5.1) checks stats itself. Avoids double-gating on rounding. |
| `pick_abilities_for_player` | `player_generator_equipment_service.py` ~91–125 | After the `non_player_ability` skip: `if not can_learn(player, a, check_stats=False): continue`. Keep `meets_ability_requirements` for stats. Remove the `allowed_elements` parameter, or leave it and treat `None` as "use the player's elements". |
| `generate_player` | `player_generator.py` ~180 | Remove the hard-coded `allowed_elements = {'fire','water','earth','air','light','dark'}` (see 5.1). |
| `_choose_ability_for_player` | `ai_services/ai_leveling_logic.py` ~8 | Add `candidates = [s for s in candidates if can_learn(p, s)]` before sorting (see 5.2). |

Import `can_learn` inside the functions in `player.py` and the generator service to avoid a circular import (`player_ability` already imports `player` indirectly through constants).

### 4.3 Show it (small, recommended)

In `tui/screens/learn_overlay.py`, add the character's elements to the header or detail pane, e.g. `Elements: Earth · Fire`. Otherwise players will wonder why their Kade can't see a fire spell. Optionally add the same to the party overlay row.

---

## 5. Bugs found while checking (fix with this pass)

### 5.1 The generator never offers ice or electric
`player_generator.py` ~180 passes `allowed_elements = {'fire','water','earth','air','light','dark'}`. Any ability whose elements are only ice/electric is invisible to generated characters. Today that blocks Moxie's ice and electric picks and Kade's electric picks. It also ignores the character entirely, so Moxie can currently be generated with a pure-water spell.

Fix:
- `generate_player_character` sets `elements_base` (3.3).
- Pass the element set into `generate_player`, e.g. `generate_player(..., elements_base=CHARACTER_NPC_ELEMENT_MAP.get(atype, []))`. Set `p.elements_base` at the top of `generate_player`, before the level loop, so `pick_abilities_for_player` → `can_learn` sees it on every pick.

### 5.2 AI leveling ignores class and non-player flags
`_choose_ability_for_player` picks the highest-level unknown seed of **any** type, including `non_player_ability` hostile moves. With `can_learn` (full stat check) this goes away. Only affects the AI demo / auto-leveling path.

### 5.3 Saved games
- Saved characters keep every ability they already know, even ones that fail the new gate. **Never remove abilities.**
- Elements are backfilled on load (3.3, `__setstate__` row). Nothing else migrates.

---

## 6. Where pools are still thin (fixed by new abilities, not by elements)

Learnable abilities per tier with the final map, current build:

**Core five** (slots earned in each tier with the planned stat curve: 4 / 4 / 5 / 6 / 7)

| Character | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Tier 5 |
|---|---|---|---|---|---|
| Chock | 4 | 27 | 20 | 14 | **2** |
| Kaera | 6 | 26 | 35 | 17 | 9 |
| Moxie | 4 | 27 | 18 | 14 | 11 |
| Kade | 4 | 26 | 23 | 10 | 11 |
| Poise | 4 | 26 | 15 | 35 | 4 |

Tier 1 is solved: every core character has at least 4 Level 1 picks for the 4 slots before Tier 2. No new Level 1 abilities are needed.

**Remaining gaps (Tier 5, minimum 4):**

| Character | Class | Tier 5 learnable |
|---|---|---|
| Chock, Vek, Warden Hale, Thorn, Kor'in, Lira | technique | 2 |
| Drax | technique | 1 |
| Lyric | tech | 1 |
| Ghost | skill | 2 |
| Dare | skill | 3 |

All Tier 1–4 minimums are met for everyone. Recruits join at level 30 or later with their kits, so a thin Level 1 pool (Thorn 1, Rynn 1, Veyr 1) does not matter for them.

The Tier 5 gap is a **class** gap: technique has only 2 Level 5 abilities in total. Elements can't fix it. New Level 5 abilities (a separate spec) should target:
- technique: at least 4 new, together covering all 8 elements, with light, electric and dark well represented;
- tech: ice and electric (for Lyric);
- skill: dark, ice, fire and electric (for Ghost and Dare).

## 7. Startup validator

Add a one-time check at startup (or in the dev TUI) that logs a WARNING for:
- a key in `CHARACTER_NPC_CLASS_MAP` missing from `CHARACTER_NPC_ELEMENT_MAP`, or the reverse;
- an element value not in `Element` or equal to `physical`;
- a core-five character without exactly 4 elements, or a recruit with more than 2;
- a class with no character for one of the 8 elements;
- any recruit starting ability that fails `can_learn(..., check_stats=False)`. Starting abilities above the character's level are allowed; they're attached directly from the seed and skip the gate.

Expected result on the current build: **zero warnings**.

---

## 8. Tests

1. `CHARACTER_NPC_ELEMENT_MAP` keys == `CHARACTER_NPC_CLASS_MAP` keys; core five have 4 elements, recruits 1–2; all valid, none `physical`; every class covers all 8 elements.
2. A recruit built with `generate_player_from_attainable_character_seed` (e.g. Lyren) has `elements_base == ['water', 'earth']`.
3. `generate_player_character(character_npc_id='tech')` gives Kade `['electric', 'light', 'water', 'air']`, and every generated ability has at least one of them.
4. Generated Moxie can receive a pure-ice or pure-electric ability (regression for 5.1); generated Kade never receives a pure-ice ability.
5. `can_learn(lira, technique ability with only water/ice/air/electric/light/dark)` → False; with one `earth` slot → True.
6. `can_learn` with a matching element but the wrong class → False.
7. `can_learn` on a `non_player_ability` → False, even when class and element match.
8. Custom character (`elements_base == []`) can learn any ability of its class (stats permitting).
9. `learn_ability` refuses an off-element ability and does **not** use up an ability slot.
10. `get_potential_player_abilities(kade)` contains no ability without electric, light, water or air.
11. Loading an old save backfills `elements_base` for every named character, and keeps an already-known off-element ability.
12. `_choose_ability_for_player` never returns an off-class, off-element or non-player ability.
13. Validator (7) reports zero warnings.
