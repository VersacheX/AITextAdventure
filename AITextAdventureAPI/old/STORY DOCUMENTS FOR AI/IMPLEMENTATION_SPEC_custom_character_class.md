# Implementation Spec — Custom Character Class Selection

**Status:** Ready for implementation
**Scope:** New Game screen, the player-named hero's creation, class inference, the two Chapter 1 joins
**Code base:** latest `AITextAdventure-master` (TUI under `AITextAdventureAPI/tui`, game under `AITextAdventureAPI/old`)

---

## 1. Background and decisions

Leveling is automated: a character with a class spends every stat and power point on its class curve (`Player.auto_allocate_level_points`). The player-named hero is the only character with no class. That has two problems:

- His points never auto-spend (`auto_allocate_level_points` returns early when there's no class), so he develops oddly compared with everyone else.
- In a level 76 save, his learn screen shows **only magic**, even when filtered by each class. A brand-new hero with no class and the same base stats (STR 83, DEX 127, INT 573, CON 104) sees all five classes in the current code: 94 magic, 86 spirit, 72 tech, 46 skill, 45 technique. So that save has `character_class = "magic"` stored on the hero. The only code that can set a class on a character with no `npc_id` is the "infer from first known ability" fallback in `PlayerGame.add_character` (see §5).

**Decisions (from Jay):**

1. The hero chooses a class on the New Game screen.
2. The hero keeps access to **all elements** (`elements_base` stays empty). This is a "for now" rule; a 2- or 4-element choice may come later.
3. Gear and other stat bonuses do **not** count toward ability requirements. They only add to combat power. Requirements keep reading base stats only. **No change**; see §6.
4. No migration for existing saves (consistent with the no-carry-over rule for old saves).

---

## 2. New Game screen: class picker

**File:** `tui/screens/new_game_screen.py`

Add a class choice under the name `Input`. Use a Textual `RadioSet` (or `Select`) with id `#char-class`, showing one option per class with a one-line role:

| Value | Label | Role line |
|---|---|---|
| `technique` | Technique | Front line: high HP, heavy physical hits (STR / CON) |
| `spirit` | Spirit | Healing, protection and revives (INT / CON) |
| `magic` | Magic | Elemental and area damage (INT) |
| `tech` | Tech | Devices and precise elemental attacks (INT / DEX) |
| `skill` | Skill | Speed and precision strikes (DEX / STR) |

Rules:
- Take the class list from `CLASS_LEVEL1_STATS` keys (`game/region_seeds/player_abilities/ability_requirements.py`) so it can't drift. Keep the role lines in a small dict in the screen.
- Default selection: `technique` (matches today's behaviour).
- `#new-game-panel` is `width: 48`; widen it, or put the role line in a `Static` under the picker that updates when the selection changes, so labels don't wrap badly.
- `_submit()` reads the chosen class and passes it to `_build_world(name, cls)`.
- Disable the picker along with the name input and Begin button while the world builds.
- Update the module docstring: class selection is no longer a later roadmap item. Update the matching note in `tui/screens/main_menu_screen.py` too.

---

## 3. Hero creation with a class

**File:** `tui/screens/new_game_screen.py`, `_build_world`

Replace the current creation block:

```python
player = Player(name, 0, 0, 0, False)
pg = PlayerGame()
equip_player_character(player, pg, focus="technique")
pg.add_character(player)
```

with:

```python
from game.objects.player import Player, apply_class_curve

player = Player(name, 0, 0, 0, False)
pg = PlayerGame()

apply_class_curve(player, cls, 1)     # sets character_class, level-1 stats, HP/AP
player.unused_ability_slots = 1       # apply_class_curve zeroes slots; a new character starts with 1
player.elements_base = []             # custom hero: every element (see §4)

equip_player_character(player, pg, focus=cls)
pg.add_character(player)
```

Notes:
- `apply_class_curve` sets `character_class`, `CLASS_LEVEL1_STATS[cls]`, and level-1 HP/AP from `CLASS_HP_RATIO`. It sets `unused_stat_points` and `unused_power_points` to 0, so there are no manual points left to spend at creation. That's intended: from here on, every level-up auto-allocates on the class curve.
- Setting `unused_ability_slots = 1` matches `generate_player` in `combat_balancing_simulation/player_generator.py`, so the hero can learn one level-1 ability straight away.
- `equip_player_character(..., focus=cls)` gives starting weapon and armor for the chosen class instead of the hard-coded technique set.
- Apply the same change to the legacy console path `old/console_game_gameloop.py` `new_game()` (it also hard-codes `focus='technique'`). A simple numbered prompt (1–5) is enough there.

---

## 4. Elements: the hero keeps all of them

- `can_learn` already treats an empty `elements_base` as "all elements". No change to the rule.
- `assign_character_elements` only fills `elements_base` from `CHARACTER_NPC_ELEMENT_MAP` by `npc_id` or `id`. The hero has neither, so it stays empty. Add a comment in `assign_character_elements`: *"A character with no npc_id/id (the player-named hero) keeps an empty element list = every element."*
- **Learn screen display** (`tui/screens/learn_overlay.py`, `_refresh_display`): today the Elements label is hidden when the list is empty. Show `Elements: All` instead, so it's clear the hero isn't element-locked.

---

## 5. Remove class inference from learned abilities

**File:** `old/game/objects/player_game.py`

Two places guess a class from the first ability a character knows:

1. `add_character` (around line 1076): the `# final fallback: infer from first known ability type` loop.
2. The load-time backfill in `__setstate__` (around line 2080): the `if not inferred and cid:` ability loop.

**Delete both ability-based fallbacks.** Keep the map lookups (`CHARACTER_NPC_CLASS_MAP`, `CHARACTER_CLASS_MAP`).

Why: every recruit gets its class from the maps or from `generate_player_character`, and the hero now gets it from the picker. Guessing from abilities can only ever lock the wrong class onto a character. It is the only code path that could have stamped `magic` onto the hero in the level 76 save.

After this change, a character with no class and no map entry stays classless. Nothing in normal play creates one any more. Test harnesses (`generate_player`, `run_combat_simulator.py`) set the class explicitly.

---

## 6. Requirements read base stats only (confirm, no change)

`can_learn` (`old/game/objects/player_ability.py`) compares `getattr(player, stat)`, which is the base stat. Gear, Dummy Guides and Masterworks raise combat power but never unlock abilities. This is the intended design.

- Add one line to the `can_learn` docstring: *"Requirements use base stats only; gear and other bonuses never count (design rule)."*
- Fix the stale docstring in `get_potential_player_abilities`: it still describes the 1.5 scale. The player scale is `PLAYER_REQUIREMENT_SCALE = 2.1`.

---

## 7. Chapter 1 joins: never the hero's class

The first two party members join in Chapter 1 through two `player_character_join` events (`main_story_chapter_1.py`, around lines 576 and 582, `dialog_id: 'begin_game_add_pc'`). Both go to `add_random_player_character`, which calls `generate_player_character` with no npc_id and picks a random core-five class whose character isn't in the party yet. With the hero now holding a class, one of these joins could repeat it, for example a magic hero plus Moxie. That would leave Chapter 1 and the first half of Chapter 2 with only two roles.

**Rule:** for those two Chapter 1 joins only, the random pick excludes the hero's class. Every other join is unchanged, including the Chapter 2 random join (`ch2_add_pc`), the Chapter 3 character NPC and the Chapter 4 final character.

Because the join path is generic, turn this on with an **optional event parameter** and default it to off.

**7.1 Story events** (`game/region_seeds/main_story/main_story_chapter_1.py`): add the flag to both joins.

```python
{
    'event_type': 'player_character_join',
    'params': {
        'dialog_id': 'begin_game_add_pc',
        'exclude_custom_class': True,
    }
},
```

**7.2 Event handler** (`services/task_completion_service.py`, `player_character_join`): pass the flag through.

```python
def player_character_join(params, player_game):
    if params.get('is_final_character'):
        player_game.add_final_character(params.get('dialog_id'))
    else:
        player_game.add_random_player_character(
            params.get('dialog_id'),
            exclude_custom_class=bool(params.get('exclude_custom_class')),
        )
```

**7.3 Party methods** (`old/game/objects/player_game.py`):

```python
def get_custom_character_classes(self) -> set:
    """Classes held by the player-named hero (characters with no npc_id)."""
    return {
        str(getattr(c, 'character_class', '') or '').lower()
        for c in self.get_all_characters()
        if not getattr(c, 'npc_id', None) and getattr(c, 'character_class', None)
    }

def add_random_player_character(self, dialog_id: str, exclude_custom_class: bool = False):
    ...
    exclude = self.get_custom_character_classes() if exclude_custom_class else None
    p = self.generate_player_character(seed=seed, level=self.get_max_character_level(),
                                       exclude_classes=exclude)
    ...  # rest unchanged

def generate_player_character(self, seed, level, character_npc_id=None, exclude_classes=None):
    rng = random.Random(seed)
    if not character_npc_id:
        exist_character_names = [ch.name for ch in self.get_all_characters()]
        candidates = [k for k in const.CHARACTER_CLASS_MAP.keys()
                      if const.CHARACTER_CLASS_MAP[k] not in exist_character_names]
        if exclude_classes:
            filtered = [k for k in candidates if k not in exclude_classes]
            candidates = filtered or candidates   # never leave the pick empty
        atype = rng.choice(candidates)
    ...  # rest unchanged
```

Notes:
- The hero is the only character with no `npc_id`. Every recruit gets one when it joins, so "no npc_id" identifies him without a new field.
- Leave `exclude_classes` out (or `None`) and the pick behaves exactly as today. All other callers stay as they are.
- The two Chapter 1 joins already can't repeat each other, because joined names are excluded. With the flag, the opening party is always three different classes.

---

## 8. Optional cleanup: stray imports

These imports are unused and crash on systems without the libraries. Remove them:

| File | Import |
|---|---|
| `old/game/objects/player_game.py` (line 5) | `pydantic` |
| `old/game/objects/dungeon.py` (line 2) | `turtle` |
| `old/combat_balancing_simulation/hostile_seed_engine.py` (line 12) | `tkinter` |
| `old/services/bar_service.py` (line 1) | `tkinter` |

Confirm each one is unused with a search before deleting it.

---

## 9. Out of scope

- Migrating existing saves. A hero in an existing save keeps whatever class (or no class) it has.
- A choice of 2 or 4 elements for the hero (possible later).
- Counting gear toward requirements (decided against).
- Class filtering for any join other than the two Chapter 1 joins (Chapter 2 random join, Chapter 3 character NPC and Chapter 4 final character stay as they are).

---

## 10. Verification

1. **New Game, each class:** create a hero with each of the five classes. Check that:
   - `character_class` is set;
   - level-1 stats equal `CLASS_LEVEL1_STATS[cls]`;
   - `unused_ability_slots == 1`;
   - `elements_base == []`;
   - the starting weapon suits the class.
2. **Learn screen at level 1:** level-1 abilities of the chosen class, across every element, are listed. No other class appears. The header shows `Elements: All`.
3. **Level-up:** give the hero XP for several levels. Stat and power points auto-spend on the class split (for example, magic +6 INT and +1 to all per level). `unused_stat_points` returns to 0.
4. **Level 77 check (magic hero):** use `apply_class_curve(p, 'magic', 77)`. INT is 550, at or above the level-5 requirement of 548, so the learn list holds magic abilities up to level 5 from every element. (At level 76, INT 543 stops at level 4. That's expected; magic's level-5 unlock is level 77.)
5. **Level 76 check (spirit hero):** use `apply_class_curve(p, 'spirit', 76)`. The list holds spirit abilities, and CON meets the level-4 requirement (164).
6. **No inference:** a `Player` with no class, no `npc_id` and a learned magic ability goes through `add_character` and through save then load. `character_class` stays `None`.
7. **Chapter 1 joins:** for each of the five hero classes, start a new game and complete the opening task about 20 times with different seeds. Neither Chapter 1 recruit ever has the hero's class, and the opening party is always three different classes.
8. **Other joins unchanged:** the Chapter 2 random join can still pick the hero's class (when that character isn't already in the party). A `player_character_join` without the flag behaves exactly as before.
9. **Recruits unchanged:** run the element-map validator and recruit generation. Every roster character keeps its mapped class and elements.
