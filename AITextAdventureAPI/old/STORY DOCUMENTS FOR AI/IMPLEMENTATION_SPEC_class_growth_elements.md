# Fracture: Class Growth, Elements and Ability Gaps Implementation Spec

**STATUS: IMPLEMENTED.** Part 1 (stat curve, `apply_class_curve`, `CLASS_STAT_SPLIT`/`CLASS_LEVEL1_STATS`/`CLASS_HP_RATIO`/`PLAYER_REQUIREMENT_SCALE`), Part 2 (`elements_base`/`can_learn`, already delivered by `IMPLEMENTATION_SPEC_character_elements.md` with its own, final element map), and Part 3 (15 required + 3 optional new abilities) are all in place. See the verification notes at the end of this file.

**For:** the AI coding agent implementing these changes
**Repo:** VersacheX/AITextAdventure, path `AITextAdventureAPI/old/` (all paths below are relative to it)
**Based on:** the 2026-11-23 snapshot. Line numbers are approximate; find code by function name.

## Scope

Implement three things, in this order:

1. **Stat distribution**: one class-based allocation rule (4:2 for dual-stat classes, 6:0 for magic), used both when a character levels in the party and when a character is generated or recruited. Also retune ability stat requirements so Ability Level 5 unlocks around character level 74–77.
2. **Character elements**: add `elements_base` (a list) to every character and restrict learnable abilities to class **and** element.
3. **New abilities**: add 15 required abilities (plus 3 optional ones) so every character has a usable pool at every ability level.

**Out of scope, do NOT implement:**
- A `physical` element.
- Retagging existing abilities.
- A 6th class.
- Buff/debuff damage math.
- Status duration changes.
- Changes to ability-slot timing (`ability_acquirement_level_amount` stays 4).
- Removing the custom character.

**Design constants (do not change without the designer):**
- Level 1: every stat starts at 8, plus 10 points distributed by class (total 42).
- Each level after 1: +1 to every stat (automatic, already exists), plus **6** class-distributed points, plus 15 power points (HP/AP).

---

## Part 1: Stat distribution and requirements

### 1.1 The rule

The 6 per-level points go entirely to the class stats:

| Class | Primary | Secondary | Per-level gain incl. the automatic +1 |
|---|---|---|---|
| technique | STR +4 | CON +2 | STR +5, CON +3, DEX +1, INT +1 |
| spirit | INT +4 | CON +2 | INT +5, CON +3, DEX +1, STR +1 |
| tech | INT +4 | DEX +2 | INT +5, DEX +3, STR +1, CON +1 |
| skill | DEX +4 | STR +2 | DEX +5, STR +3, CON +1, INT +1 |
| magic | INT +6 | none | INT +7, others +1 |

Level-1 stats per class (8 base + 10 points; these match what the generator already produces at level 1):

| Class | STR | DEX | CON | INT |
|---|---|---|---|---|
| technique | 14 | 8 | 12 | 8 |
| spirit | 8 | 8 | 12 | 14 |
| tech | 8 | 12 | 8 | 14 |
| skill | 12 | 14 | 8 | 8 |
| magic | 8 | 8 | 8 | 18 |

Power points (15 per level) keep the existing per-class `hp_ratio` (technique 0.80, spirit 0.50, magic 0.35, tech 0.45, skill 0.60); the rest goes to AP.

### 1.2 Bugs this replaces

- **In-party leveling** (`Player.auto_allocate_level_points`, `game/objects/player.py` ~line 598) spreads points round-robin over 4 stats, so the primary and secondary grow at the same rate and the other two get almost as much. Replace it.
- **Generation** (`combat_balancing_simulation/player_generator.py`, `generate_player`) uses its own split: 4 points by requirement weight (works out to 3:1) plus 2 random. It splits HP/AP by the CON:INT ratio. The class is set only **after** generation (`PlayerGame.generate_player_character`, `player_game.py` ~line 1028), so the generator and later leveling disagree.
- **Recruits** (`generate_player_from_attainable_character_seed`, `player.py` ~line 719) take hand-written stats from seed files. These drift far from the class curve (for example Lira STR 180 at level 105, Anita INT 120 at level 65). Max AP is 5 for `commander_drax` and `voss_caldera`.

### 1.3 Implementation

**a) Constants.** Put these in `game/region_seeds/player_abilities/ability_requirements.py` (import them where needed):

```python
CLASS_STAT_SPLIT = {
    'technique': {'strength': 4, 'constitution': 2},
    'spirit':    {'intelligence': 4, 'constitution': 2},
    'tech':      {'intelligence': 4, 'dexterity': 2},
    'skill':     {'dexterity': 4, 'strength': 2},
    'magic':     {'intelligence': 6},
}
CLASS_LEVEL1_STATS = {  # (STR, DEX, CON, INT)
    'technique': (14, 8, 12, 8), 'spirit': (8, 8, 12, 14), 'tech': (8, 12, 8, 14),
    'skill': (12, 14, 8, 8), 'magic': (8, 8, 8, 18),
}
CLASS_HP_RATIO = {'technique': 0.80, 'spirit': 0.50, 'magic': 0.35, 'tech': 0.45, 'skill': 0.60}
PLAYER_REQUIREMENT_SCALE = 2.1    # was 1.5 (hard-coded)
HOSTILE_REQUIREMENT_SCALE = 1.5   # enemies keep the old curve for now

def ability_stat_requirement(per_level_val: int, ability_level: int, scale: float = PLAYER_REQUIREMENT_SCALE) -> int:
    v = int(per_level_val)
    return v + int((v * (int(ability_level) - 1) * scale) ** 1.25)
```

**b) Replace `Player.auto_allocate_level_points`:**

```python
def auto_allocate_level_points(self) -> None:
    cls = str(getattr(self, 'character_class', '') or '').lower()
    split = CLASS_STAT_SPLIT.get(cls)
    if not split:
        return  # classless (custom character) keeps manual allocation
    pts = int(getattr(self, 'unused_stat_points', 0) or 0)
    if pts > 0:
        total = sum(split.values())
        inc = {k: pts * v // total for k, v in split.items()}
        inc[max(split, key=split.get)] += pts - sum(inc.values())  # remainder -> primary
        self.allocate_stats(inc.get('strength', 0), inc.get('dexterity', 0),
                            inc.get('constitution', 0), inc.get('intelligence', 0),
                            use_stat_points=True)
    ppts = int(getattr(self, 'unused_power_points', 0) or 0)
    if ppts > 0:
        hp = max(0, min(ppts, int(round(ppts * CLASS_HP_RATIO.get(cls, 0.5)))))
        self.apply_power_point_allocation(hp, ppts - hp)
```

Leave `check_level_up_awards` as is: it already does +1 to all stats, adds 6 stat points and 15 power points, and calls `auto_allocate_level_points` when a class is set.

**c) Add one shared builder** (e.g. in `player.py`), used by both generation and recruits:

```python
def apply_class_curve(p, cls: str, target_level: int) -> None:
    """Reset p's stats/HP/AP to the class curve at target_level.
    Equipment and abilities are untouched."""
    p.character_class = cls
    p.level = 1
    p.strength, p.dexterity, p.constitution, p.intelligence = CLASS_LEVEL1_STATS[cls]
    # Level-1 HP/AP: Player defaults (max_hp 20, max_ap 5) + 2 HP per CON point above 8
    # + the level-1 power points split by hp_ratio
    p.max_hp = 20 + (p.constitution - 8) * 2
    p.max_ap = 5
    pp = int(p.power_points_per_level)
    hp = int(round(pp * CLASS_HP_RATIO[cls]))
    p.max_hp += hp
    p.max_ap += pp - hp
    p.unused_stat_points = 0
    p.unused_power_points = 0
    p.growth_level_applied = 1
    for lvl in range(2, int(target_level) + 1):
        p.level = lvl
        p.check_level_up_awards()   # +1 all, +6 by split, +15 power points by hp_ratio
    p.current_hp, p.current_ap = p.max_hp, p.max_ap
```

Note: `check_level_up_awards` also adds an ability slot every 4 levels. After `apply_class_curve`, set `unused_ability_slots` explicitly to what the caller wants (keep the seed's value for recruits, keep the generator's flow for main characters). Don't let the loop's slots leak through.

**d) Generation** (`player_generator.generate_player`):
- If `focus` is one of the five classes, call `apply_class_curve(p, focus, target_level)` instead of the custom level-1 split and per-level split/random/CON:INT power-point code.
- Keep its ability-picking logic: walk levels 2..target and pick an ability when a slot is granted, using the stats the character **has at that level**. The simplest correct approach is to loop level by level: call `check_level_up_awards()`, then if a slot was granted call `pick_abilities_for_player(...)`.
- **Element filter in the generator:** `pick_abilities_for_player` is called with a hard-coded `allowed_elements = {'fire','water','earth','air','light','dark'}`. Replace this with the character's `elements_base` (Part 2), and make sure it goes through the same `can_learn` check.
- `PlayerGame.generate_player_character` already sets `character_class` and must also set `elements_base` (Part 2).

**e) Recruits** (`generate_player_from_attainable_character_seed`):
- After `populate_from_json(seed)` and resolving the class, call `apply_class_curve(p, cls, seed_level)`. This **overrides** the seed's `strength/dexterity/constitution/intelligence/max_hp/max_ap/current_*`.
- Set `unused_ability_slots` back to the seed's value (currently 0), then attach equipment and starting abilities as today.
- You may delete the hand-written stat fields from the seeds later; for now just ignore them. Add a comment that the stats are derived.
- Expected results are in Appendix A. They include the fix for Drax/Voss AP = 5.

**f) Requirement formula.** Replace every hard-coded copy of `v + int((v * ((L-1)*1.5)) ** 1.25)`:

| File | ~Line | Use |
|---|---|---|
| `game/objects/player_ability.py` | 536 (ability list for a player) | `ability_stat_requirement(v, L)` |
| `game/objects/player_ability.py` | 486 (docstring) | update text |
| `combat_balancing_simulation/player_generator_equipment_service.py` | 182 | `ability_stat_requirement(v, L)` |
| `combat_balancing_simulation/hostile_seed_engine.py` | 496, 588 | `ability_stat_requirement(v, L, HOSTILE_REQUIREMENT_SCALE)` |

**g) Saved games** (`Player.__setstate__`): backfill `character_class` (already done), `elements_base` (Part 2) and `growth_level_applied`. **Do not** rebuild existing saved characters' stats automatically. Optionally add a debug/admin command that calls `apply_class_curve` on party members.

### 1.4 Expected numbers (acceptance)

Stat requirements with scale 2.1:

| Requirement base | Ability L1 | L2 | L3 | L4 | L5 |
|---|---|---|---|---|---|
| 13 (dual-class primary) | 13 | 75 | 161 | 259 | 366 |
| 9 (dual-class secondary) | 9 | 48 | 102 | 164 | 231 |
| 18 (magic INT) | 18 | 111 | 240 | 388 | 548 |

Character level at which an on-curve character first meets each tier:

| Class | Ability L2 | L3 | L4 | L5 |
|---|---|---|---|---|
| technique, spirit, tech, skill | 14 | 31 | 52 | 74 |
| magic | 15 | 33 | 54 | 77 |

Curve spot-checks (`apply_class_curve`):

| Class | Level | STR | DEX | CON | INT | Max HP | Max AP |
|---|---|---|---|---|---|---|---|
| technique | 1 | 14 | 8 | 12 | 8 | 40 | 8 |
| technique | 77 | 394 | 84 | 240 | 84 | 2928 | 616 |
| spirit | 77 | 84 | 84 | 240 | 394 | 2620 | 924 |
| tech | 77 | 84 | 240 | 84 | 394 | 2231 | 1001 |
| skill | 77 | 240 | 394 | 84 | 84 | 2385 | 847 |
| magic | 77 | 84 | 84 | 84 | 550 | 2077 | 1155 |

HP/AP depend on the exact level-1 setup. If your level-1 HP/AP differs by a few points, that's fine as long as the stat columns match exactly.

---

## Part 2: Character elements and learn restrictions

**Superseded by `IMPLEMENTATION_SPEC_character_elements.md` and `IMPLEMENTATION_SPEC_elements_and_cleanup.md`.** Its element map is out of date.

### 2.1 Data

Add to `game/region_seeds/main_characters.py`, next to `CHARACTER_NPC_CLASS_MAP` (export it through `game.constants` the same way). The core five are keyed by their class id, because that is their `npc_id`.

```python
CHARACTER_NPC_ELEMENT_MAP = {
    # core 5
    'technique': ['earth', 'fire'],      # Chock
    'spirit':    ['light', 'water'],     # Kaera
    'magic':     ['fire', 'ice'],        # Moxie
    'tech':      ['electric', 'ice'],    # Kade
    'skill':     ['air', 'dark'],        # Poise
    # main-story
    'lyren': ['water', 'earth'], 'vek': ['earth', 'electric'],
    'warden_hale': ['light', 'earth'], 'seraphine': ['light', 'air'],
    # regional
    'nia': ['air'], 'sable': ['earth', 'air'], 'thorn': ['earth'], 'bragg': ['earth', 'fire'],
    'ripple': ['water'], 'kor_in': ['ice', 'air'], 'grimnaw': ['dark', 'electric'],
    # extended
    'voss_caldera': ['earth', 'light'], 'rynn': ['water', 'ice'], 'eldon_dawnseer': ['light'],
    'regent_sylvara': ['dark', 'electric'], 'ghost': ['dark', 'ice'], 'lira_emberforge': ['fire', 'earth'],
    'osten_dreamweaver': ['dark', 'water'], 'lyric': ['electric', 'air'], 'dare': ['fire', 'electric'],
    'andrea_starveil': ['light', 'fire'], 'veyr_ashcant': ['fire'], 'spark_maddox': ['electric', 'fire'],
    'anita': ['dark', 'air'], 'talon': ['earth', 'light'], 'alden_brightvein': ['light', 'electric'],
    'commander_drax': ['earth', 'light'],
}
```

Single-element characters (intended): Thorn, Ripple, Eldon, Veyr, Nia. Every other character has two elements.

### 2.2 Player field

- Add `elements_base: list[str] = []` to `Player` (dataclass default, `to_dict`/`from_dict`, and the defaults dict near line ~105).
- Set it wherever the class is set:
  - `generate_player_character`
  - `generate_player_from_attainable_character_seed`
  - the class-inference fallback in `PlayerGame.add_character` (~line 1064)
  - `Player.__setstate__` backfill (look up by `npc_id` / `id`)
- Remove the redundant `p.character_class = npc_id` in `add_pending_character` (~line 885); `generate_player_character` already sets it.
- The custom character has no id, so it gets `elements_base = []`.

### 2.3 One gate for listing and learning

Add to `ability_requirements.py` (or `player_ability.py`) and use it **everywhere**:

```python
def can_learn(player, ability) -> bool:
    """Class tree + element set + stat requirements. Works for seed dicts and PlayerAbility objects."""
    get = (lambda k: ability.get(k)) if isinstance(ability, dict) else (lambda k: getattr(ability, k, None))
    val = lambda x: str(getattr(x, 'value', x) or '').lower()
    if get('non_player_ability'):
        return False
    cls = val(getattr(player, 'character_class', None))
    if cls and val(get('ability_type')) != cls:
        return False
    base = {val(e) for e in (getattr(player, 'elements_base', None) or [])}
    if base and not base & {val(e) for e in (get('elements') or [])}:
        return False                      # needs at least ONE matching element slot
    level = int(get('level') or 1)
    for req in REQ_LOOKUP.get(val(get('ability_type')), []):
        for stat, per_level in req.items():
            if int(getattr(player, stat, 0) or 0) < ability_stat_requirement(per_level, level):
                return False
    return True
```

Wire it in:
- **Ability list** in `player_ability.py` (~lines 490–540): replace the inline class + stat checks with `if not can_learn(player, a): continue`.
- **`Player.learn_ability`** (`player.py` ~line 677): replace the class-only check with `if not can_learn(self, ability): return False`. Today learning doesn't re-check stats; this fixes that.
- **Generator ability picks** (`player_generator_equipment_service.pick_abilities_for_player`, and `meets_ability_requirements` ~line 182): filter candidates with `can_learn`.
- **AI leveling** (`ai_services/ai_leveling_logic._choose_ability_for_player`): filter with `can_learn`.
- Duplicate elements still count as one match for eligibility (`fire, fire, earth` is learnable by any fire **or** earth character).

### 2.4 Starting abilities and saves

- Recruits' starting abilities skip the gate (they are attached directly from the seed).
- Add a **startup validator** that logs a WARNING if any recruit's starting ability fails the class or element check. Starting abilities above the character's level are allowed. With the map above, there should be **zero** element warnings; the map was checked against every starting kit.
- Saved characters keep abilities they already know, even if they would fail the new gate. Never remove abilities.

---

## Part 3: New abilities

### 3.1 Target

Each character needs at least this many learnable abilities (class + element) per ability level:

| Ability level | Minimum learnable per character |
|---|---|
| 1 | 2 |
| 2 | 6 |
| 3 | 6 |
| 4 | 5 |
| 5 | 4 |

Current shortfalls: technique L1 (Thorn) and L5 (all 7 technique characters have only 2), spirit L1 (Ripple, Rynn), magic L1 (Veyr), tech L5 (Kade has 1), skill L1 (Nia), skill L5 (Ghost 2, Dare 3). No class has an ice Level 5 ability today.

### 3.2 Required abilities (15)

Add each to the matching file:
- Level 1 → `level_1_abilities.py`
- Level 5 → `level_5_abilities_by_type/<class>.py`

Conventions followed:
- An ability of level N has exactly N element slots.
- Costs and power match the existing medians: L1 damage ~9 AP / 9–14 power; L5 damage ~180 AP / ~192 power; L5 status ~165–190 AP.
- All status keys already exist in `constants_other.py`.

```python
    {"id": "earth_technique_lv1_stone_fist", "name": "Stone Fist", "description": "A rock-hard punch that hits like a falling boulder.", "ability_type": "technique", "level": 1, "elements": ["earth"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "ice_ice_earth_water_air_technique_lv5_glacier_breaker", "name": "Glacier Breaker", "description": "A crushing overhead blow that splits the ground into frozen shards.", "ability_type": "technique", "level": 5, "elements": ["ice", "ice", "earth", "water", "air"], "base_power": 192, "ap_cost": 180, "effect": "damage", "can_aoe": False},
    {"id": "electric_electric_fire_earth_light_technique_lv5_stormforged_charge", "name": "Stormforged Charge", "description": "A lightning-fast charge that ends in a molten, thunderous impact.", "ability_type": "technique", "level": 5, "elements": ["electric", "electric", "fire", "earth", "light"], "base_power": 192, "ap_cost": 180, "effect": "damage", "can_aoe": False},
    {"id": "earth_earth_light_fire_ice_technique_lv5_titanfall", "name": "Titanfall", "description": "A leaping strike that lands with the weight of a mountain.", "ability_type": "technique", "level": 5, "elements": ["earth", "earth", "light", "fire", "ice"], "base_power": 186, "ap_cost": 176, "effect": "damage", "can_aoe": True},
    {"id": "earth_light_water_electric_ice_technique_lv5_iron_bastion", "name": "Iron Bastion", "description": "A war cry that locks the party into an unbreakable formation.", "ability_type": "technique", "level": 5, "elements": ["earth", "light", "water", "electric", "ice"], "base_power": 0, "ap_cost": 170, "effect": "status", "status_keys": ["defense_buff", "defense_buff", "elemental_defense_buff", "constitution_buff"], "can_aoe": True},
    {"id": "water_spirit_lv1_rain_blessing", "name": "Rain Blessing", "description": "A gentle rain that slowly restores the weary.", "ability_type": "spirit", "level": 1, "elements": ["water"], "base_power": 0, "ap_cost": 9, "effect": "status", "status_keys": ["regen"], "can_aoe": False},
    {"id": "ice_spirit_lv1_frost_salve", "name": "Frost Salve", "description": "A cooling touch that numbs pain and closes wounds.", "ability_type": "spirit", "level": 1, "elements": ["ice"], "base_power": 9, "ap_cost": 10, "effect": "heal", "can_aoe": False},
    {"id": "fire_magic_lv1_cinder_flick", "name": "Cinder Flick", "description": "A flicked ember that bursts on contact.", "ability_type": "magic", "level": 1, "elements": ["fire"], "base_power": 10, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "ice_ice_electric_water_dark_tech_lv5_cryo_lattice", "name": "Cryo Lattice", "description": "A deployable lattice that freezes the target's defenses and slows it to a crawl.", "ability_type": "tech", "level": 5, "elements": ["ice", "ice", "electric", "water", "dark"], "base_power": 2, "ap_cost": 190, "effect": "status", "status_keys": ["elemental_debuff", "elemental_debuff", "dexterity_debuff"], "can_aoe": False},
    {"id": "electric_electric_fire_ice_light_tech_lv5_arc_reactor_overload", "name": "Arc Reactor Overload", "description": "A portable reactor pushed far past safe limits, then thrown.", "ability_type": "tech", "level": 5, "elements": ["electric", "electric", "fire", "ice", "light"], "base_power": 205, "ap_cost": 185, "effect": "damage", "can_aoe": False},
    {"id": "ice_ice_ice_electric_air_tech_lv5_absolute_zero_protocol", "name": "Absolute Zero Protocol", "description": "A cryo-cannon that drops the battlefield to absolute zero.", "ability_type": "tech", "level": 5, "elements": ["ice", "ice", "ice", "electric", "air"], "base_power": 186, "ap_cost": 182, "effect": "damage", "can_aoe": True},
    {"id": "air_skill_lv1_wind_jab", "name": "Wind Jab", "description": "A jab so fast it carries a gust behind it.", "ability_type": "skill", "level": 1, "elements": ["air"], "base_power": 9, "ap_cost": 8, "effect": "damage", "can_aoe": False},
    {"id": "dark_dark_ice_air_water_skill_lv5_shadow_waltz", "name": "Shadow Waltz", "description": "A dance of cold shadows that strikes from every angle at once.", "ability_type": "skill", "level": 5, "elements": ["dark", "dark", "ice", "air", "water"], "base_power": 192, "ap_cost": 178, "effect": "damage", "can_aoe": False},
    {"id": "ice_ice_dark_electric_earth_skill_lv5_frostfang_flurry", "name": "Frostfang Flurry", "description": "A flurry of freezing strikes that leaves the target numb and exposed.", "ability_type": "skill", "level": 5, "elements": ["ice", "ice", "dark", "electric", "earth"], "base_power": 2, "ap_cost": 175, "effect": "status", "status_keys": ["dexterity_debuff", "defense_debuff", "elemental_debuff"], "can_aoe": False},
    {"id": "electric_electric_fire_air_light_skill_lv5_storm_edge", "name": "Storm Edge", "description": "A blade-rush wrapped in crackling lightning and flame.", "ability_type": "skill", "level": 5, "elements": ["electric", "electric", "fire", "air", "light"], "base_power": 192, "ap_cost": 180, "effect": "damage", "can_aoe": False},
```

### 3.3 Optional (recommended): ice and electric identity

These are not needed for the minimums, but they give the ice and electric characters a Level 5 signature move (Moxie, Rynn, Alden):

```python
    {"id": "ice_ice_water_light_air_spirit_lv5_cryostasis", "name": "Cryostasis", "description": "Encases allies in healing ice that mends them over time.", "ability_type": "spirit", "level": 5, "elements": ["ice", "ice", "water", "light", "air"], "base_power": 0, "ap_cost": 170, "effect": "status", "status_keys": ["regen", "regen", "elemental_defense_buff"], "can_aoe": True},
    {"id": "electric_light_light_air_water_spirit_lv5_thunderhymn", "name": "Thunderhymn", "description": "A booming hymn that charges allies' weapons with holy lightning.", "ability_type": "spirit", "level": 5, "elements": ["electric", "light", "light", "air", "water"], "base_power": 0, "ap_cost": 165, "effect": "status", "status_keys": ["elemental_attack_buff", "attack_buff", "intelligence_buff"], "can_aoe": True},
    {"id": "ice_ice_water_air_dark_magic_lv5_absolute_zero", "name": "Absolute Zero", "description": "Stops all motion and heat in the target, shattering it from within.", "ability_type": "magic", "level": 5, "elements": ["ice", "ice", "water", "air", "dark"], "base_power": 205, "ap_cost": 185, "effect": "damage", "can_aoe": False},
```

### 3.4 Acceptance

Write a test or script that loads `PLAYER_ABILITY_SEEDS` and `CHARACTER_NPC_ELEMENT_MAP` and, for each of the 32 characters, counts abilities of their class with at least one matching element, per level. Every count must meet the 3.1 minimums. Expected counts after the 15 required abilities:

| Character | Class | Elements | L1 | L2 | L3 | L4 | L5 |
|---|---|---|---|---|---|---|---|
| Chock | technique | earth, fire | 3 | 16 | 16 | 12 | 6 |
| Thorn | technique | earth | 2 | 9 | 8 | 11 | 6 |
| Kor'in | technique | ice, air | 2 | 15 | 13 | 11 | 5 |
| Ripple | spirit | water | 2 | 8 | 11 | 11 | 7 |
| Veyr | magic | fire | 2 | 8 | 7 | 7 | 10 |
| Kade | tech | electric, ice | 2 | 14 | 18 | 6 | 4 |
| Nia | skill | air | 2 | 8 | 7 | 28 | 6 |
| Ghost | skill | dark, ice | 3 | 15 | 12 | 19 | 4 |
| Dare | skill | fire, electric | 2 | 15 | 12 | 20 | 5 |

Also check: unique `id`s, `len(elements) == level`, `non_player_ability` absent or False.

---

## Order of work and checks

1. Constants + `ability_stat_requirement` + `can_learn` (no behavior change yet besides the scale).
2. `auto_allocate_level_points` rewrite + `apply_class_curve`.
3. Generator and recruit paths call `apply_class_curve`; set `elements_base` everywhere a class is set.
4. Wire `can_learn` into the list, learn, generator and AI paths.
5. Add the new abilities; run the Part 3.4 test.
6. Run the existing combat-balancing simulations as a smoke test. Expect enemy fights at the same level to feel different: recruits now sit on the curve, and Drax/Voss have real AP.

**Unit tests to add:**
- Leveling a technique character from 1 to 77 one level at a time gives exactly STR 394 / DEX 84 / CON 240 / INT 84.
- `generate_player('x', 'technique', 77)` gives the same stats as leveling one level at a time.
- A magic character gains exactly +7 INT and +1 to each other stat per level.
- An on-curve technique character can't learn an Ability Level 5 at level 73 and can at level 74 (stat-wise; class/element permitting).
- Lira (fire, earth) can't learn a technique ability whose elements are only water/ice/air/electric/light/dark.
- Every recruit's starting abilities pass the element check (validator has no warnings).

## Open design items (do not decide; leave TODOs)

- Lira's current seed is DEX-heavy (DEX 360), which reads more like skill than technique. The curve makes her a technique character. Designer to confirm her class.
- Anita's seed was a STR/INT hybrid. The curve makes her a pure magic character.
- Personality skew for recruits (e.g. "Nia is faster than other skill users") is not implemented. If wanted later, only move points between the two non-class stats so tier unlocks don't shift.
- Ability-slot timing (currently every 4 levels) and catch-up slots for late recruits are separate work.

---

## Appendix A: Recruit stats after `apply_class_curve`

Computed with the rule above from the snapshot's join levels. The old values are shown for reference.

| Recruit id | Class | Level | STR | DEX | CON | INT | Max HP | Max AP | Old STR/DEX/CON/INT, AP |
|---|---|---|---|---|---|---|---|---|---|
| `sable` | magic | 30 | 37 | 37 | 37 | 221 | 808 | 450 | 38/38/38/224, 400 |
| `thorn` | technique | 30 | 159 | 37 | 99 | 37 | 1142 | 240 | 158/38/102/38, 250 |
| `nia` | skill | 30 | 99 | 159 | 37 | 37 | 928 | 330 | 38/224/38/38, 350 |
| `bragg` | tech | 30 | 37 | 99 | 37 | 159 | 868 | 390 | 38/102/38/158, 350 |
| `ripple` | spirit | 30 | 37 | 37 | 99 | 159 | 1022 | 360 | 38/38/102/158, 400 |
| `kor_in` | technique | 30 | 159 | 37 | 99 | 37 | 1142 | 240 | 158/38/102/38, 250 |
| `grimnaw` | tech | 30 | 37 | 99 | 37 | 159 | 868 | 390 | 38/102/38/158, 350 |
| `lyren` | spirit | 35 | 42 | 42 | 114 | 184 | 1192 | 420 | 40/40/140/180, 360 |
| `veyr_ashcant` | magic | 40 | 47 | 47 | 47 | 291 | 1078 | 600 | 22/24/68/138, 305 |
| `regent_sylvara` | magic | 40 | 47 | 47 | 47 | 291 | 1078 | 600 | 20/20/64/142, 305 |
| `spark_maddox` | tech | 40 | 47 | 129 | 47 | 209 | 1158 | 520 | 30/130/24/68, 155 |
| `commander_drax` | technique | 40 | 209 | 47 | 129 | 47 | 1522 | 320 | 148/14/72/18, 5 |
| `ghost` | skill | 40 | 129 | 209 | 47 | 47 | 1238 | 440 | 110/80/30/32, 245 |
| `eldon_dawnseer` | spirit | 40 | 47 | 47 | 129 | 209 | 1362 | 480 | 20/26/66/140, 305 |
| `vek` | technique | 50 | 259 | 57 | 159 | 57 | 1902 | 400 | 200/95/180/95, 450 |
| `voss_caldera` | tech | 50 | 57 | 159 | 57 | 259 | 1448 | 650 | 52/130/514/186, 5 |
| `dare` | skill | 55 | 174 | 284 | 62 | 62 | 1703 | 605 | 100/188/26/28, 211 |
| `rynn` | spirit | 60 | 67 | 67 | 189 | 309 | 2042 | 720 | 28/34/110/200, 455 |
| `warden_hale` | technique | 65 | 334 | 72 | 204 | 72 | 2472 | 520 | 225/100/200/90, 500 |
| `anita` | magic | 65 | 72 | 72 | 72 | 466 | 1753 | 975 | 120/62/100/120, 395 |
| `andrea_starveil` | skill | 70 | 219 | 359 | 77 | 77 | 2168 | 770 | 120/240/34/38, 267 |
| `talon` | spirit | 80 | 87 | 87 | 249 | 409 | 2722 | 960 | 30/44/148/270, 605 |
| `seraphine` | spirit | 85 | 92 | 92 | 264 | 434 | 2892 | 1020 | 120/200/280/400, 840 |
| `alden_brightvein` | spirit | 85 | 92 | 92 | 264 | 434 | 2892 | 1020 | 32/46/158/286, 642 |
| `lyric` | tech | 95 | 102 | 294 | 102 | 484 | 2753 | 1235 | 42/60/140/340, 717 |
| `osten_dreamweaver` | magic | 100 | 107 | 107 | 107 | 711 | 2698 | 1500 | 46/46/160/360, 755 |
| `lira_emberforge` | technique | 105 | 534 | 112 | 324 | 112 | 3992 | 840 | 180/360/52/50, 399 |

Notes:
- The level-30 regional recruits were already close to the curve (except Nia's STR and Sable's INT).
- The biggest corrections are Lira, Anita, Lyric (DEX), Spark (INT), Ghost (DEX) and the AP of Drax and Voss.

---

## STATUS: IMPLEMENTED

All three parts are in place and verified against the current build:

| Part | Status |
|---|---|
| 1. Stat distribution | ✅ `CLASS_STAT_SPLIT`, `CLASS_LEVEL1_STATS`, `CLASS_HP_RATIO`, `PLAYER_REQUIREMENT_SCALE` (2.1) added to `ability_requirements.py`. `Player.auto_allocate_level_points` rewritten to the fixed 4:2/6:0 split (no more round-robin). `apply_class_curve` added to `player.py` and wired into both `generate_player_from_attainable_character_seed` (recruits) and `player_generator.generate_player` (generated characters, level-by-level with correct ability picks at each level). |
| 2. Character elements | ✅ Delivered by `IMPLEMENTATION_SPEC_character_elements.md`, whose element map is the final one (this spec's section 2.1 map is superseded, as that doc states). `can_learn`/`player_class_of`/`ability_stat_requirement` live in `player_ability.py`; wired into the ability list, `learn_ability`, the generator's `pick_abilities_for_player`, and `ai_leveling_logic._choose_ability_for_player`. |
| 3. New abilities | ✅ All 15 required + all 3 optional abilities added: 5 to `level_1_abilities.py` (Stone Fist, Rain Blessing, Frost Salve, Cinder Flick, Wind Jab), 4 to `level_5_abilities_by_type/technique.py` (Glacier Breaker, Stormforged Charge, Titanfall, Iron Bastion), 3 to `tech.py` (Cryo Lattice, Arc Reactor Overload, Absolute Zero Protocol), 3 to `skill.py` (Shadow Waltz, Frostfang Flurry, Storm Edge), plus the 2 optional spirit abilities (Cryostasis, Thunderhymn) and 1 optional magic ability (Absolute Zero). |

**Verified directly (not just by code review):**
- `apply_class_curve(p, cls, 77)` matches the 1.4 acceptance table exactly for all 5 classes (stats and AP).
- `generate_player('x','technique',77)` produces identical stats to `apply_class_curve` leveling one level at a time.
- A magic character gains exactly +7 INT / +1 others per level.
- Moxie (magic) can now receive pure-ice and pure-electric Level 1 abilities — the generator's old hard-coded `allowed_elements` set (which excluded ice/electric) is gone; `elements_base` is set before any ability pick.
- Kade (tech) only ever receives abilities with at least one of electric/light/water/air (duplicates with other elements allowed, per the "at least one matching slot" rule).
- Part 3.4's minimums (L1≥2, L2≥6, L3≥6, L4≥5, L5≥4) were checked by direct script against `can_learn` for all 9 spot-check characters (Chock, Thorn, Kor'in, Ripple, Veyr, Kade, Nia, Ghost, Dare) — all pass, including the previously-thin technique L5 pool (now 5–6, was 2) and tech L5 for Kade (now 14, was 1).
- No duplicate ability ids; every new ability has `len(elements) == level`.
- The element-map startup validator (`element_map_validator.py`) still reports **zero warnings** after all of the above.

**Known discrepancies to flag, not silently resolved:**
- Appendix A's recruit `Max HP` column does **not** match what the build now produces, because Appendix A was computed before `IMPLEMENTATION_SPEC_leveling.md` existed (it assumes the old flat-20/CON×2 HP formula). The actual implemented values use the leveling spec's flat-35/CON×8 formula and are higher — e.g. this doc's `voss_caldera` row says 1,448 HP, but the implemented (and `IMPLEMENTATION_SPEC_pr39-41_followups.md`-specified) value is 2,477 HP. The **STR/DEX/CON/INT and Max AP columns are unaffected** and match exactly.
- Appendix A lists `lira_emberforge` at level 105; the data actually in the seed files (and in `IMPLEMENTATION_SPEC_pr39-41_followups.md`'s table) is level 95. The implementation follows the seed files' level 95, not this appendix's 105, since that's what the later, more specific spec and the live data agree on. Flagging rather than guessing which is the "true" intended level.
