# Hostile & Player Ability Generation Guide

> **Purpose**: Step-by-step reference for populating or creating ability seed files under
> `old/game/region_seeds/player_abilities/**`, resolving `HOSTILE_UNKNOWN_ABILITY` errors,
> and maintaining consistency with the `PlayerAbility` model, status system, and ability
> type requirements.

---

## 1. Source-of-Truth Files

| File | What it owns |
|---|---|
| `constants_other.py` | `STATUS_EFFECTS`, `ELEMENTAL_CHAR_KEYS`, `ABILITY_STATUS_KEY_DISPLAY_NAMES`, `HARMFUL_STATUS_EFFECTS`, `PLAYER_ABILITY_SEEDS` assembly |
| `ability_requirements.py` | Per-ability-level stat gates for each ability type |
| `player_ability.py` | `PlayerAbility`, `AbilityType`, `Element`, `EffectType` enums; power formula; status derivation |
| `status_utils.py` | `BLOCKING_STATUS_IDS`, elemental/stat combat modifiers |
| `constants_other.py → PLAYER_ABILITY_SEEDS` | Final merged list consumed by the game and dev-tool validators |

**Never hardcode known elements or status IDs in any other file. Always derive them from the sources above.**

---

## 2. Ability Type Reference

From `ability_requirements.py`:

| `ability_type` | Primary stats | Combat role | Typical effects |
|---|---|---|---|
| `technique` | `strength`, `constitution` | Physical attack / defense | damage, status debuffs (physical), strength/constitution buffs |
| `faith` | `intelligence`, `constitution` | Spiritual attack / defence, healing, debuff | heal, revive, cure, status, damage |
| `magic` | `intelligence` | Magical offense, DoT, debuffs | damage, status (elemental\_debuff, continuous\_damage) |
| `tech` | `intelligence`, `dexterity` | Tech offense, scan, debuffs | damage, status (scanned, silence, debuffs) |
| `skill` | `dexterity` | Speed, crit, evasion, burst | damage (often AoE), status (attack\_buff, dexterity\_buff) |

Stat requirement formula (applied in `get_potential_player_abilities`):
required = int(per_level_val) + int((int(per_level_val) * ((level - 1) * 1.5)) ** 1.25)

---

## 3. Valid Elements

Defined in `constants_other.py → ELEMENTAL_CHAR_KEYS`:
fire  water  earth  air  light  dark  ice  electric

Every entry in an ability's `"elements"` list **must** be one of these values.

---

## 4. Valid Status Keys

`status_keys` values must exist as keys in `constants_other.py → STATUS_EFFECTS`:
elemental_attack_buff   elemental_defense_buff   elemental_debuff
attack_buff             attack_debuff
defense_buff            defense_debuff
strength_buff           strength_debuff
dexterity_buff          dexterity_debuff
intelligence_buff       intelligence_debuff
constitution_buff       constitution_debuff
continuous_damage
petrify   stun   sleep   confuse   silence   scanned

*note* - High level abilities can have multiple status_keys for effect=cure and effect=status

---

## 5. Ability Seed Schema
{
    "id":           str,   # snake_case; see naming convention below
    "name":         str,   # human-readable display name
    "description":  str,   # flavour text, 1–2 sentences
    "ability_type": str,   # one of: technique | faith | magic | tech | skill
    "level":        int,   # 1–5 currently supported
    "elements":    [str],  # exactly N elements where N == ability level; duplicates allowed (e.g. ["fire","fire","water"] for level 3) 
    "base_power":   int,   # see power ranges per level below
    "ap_cost":      int,   # see AP cost ranges per level below
    "effect":       str,   # damage | heal | status | revive | cure
    "status_keys": [str] | None,   # required when effect == "status"
    "can_aoe":      bool,  # True only for AoE variants
    "non_player_ability": bool,  # True = hostile-only; False = player-learnable
}

> `status_keys` is a **list** even for single-status abilities.  
> Omit or set to `None` when `effect != "status"`.

---

## 6. ID Naming Convention
{element(s)}_{ability_type}_lv{level}_{thematic_name}

Examples:
- `fire_air_technique_lv2_blazing_rush`
- `dark_magic_lv1_void_bolt`
- `light_fire_electric_air_tech_lv4_photon_rupture`
- `cold_execution_technique_lv3_cold_execution` ← hostile-only

For **hostile-only** abilities the same convention applies; add `"non_player_ability": True`.
*note* - if a hostile seed asked for abiulities to be generated has > `generic_name` upgrade to naming convention in hostile seed

---

## 7. Power and AP Ranges by Level

| Level | `len(elements)` | `base_power` (damage) | `base_power` (heal/status) | `ap_cost` |
|---|---|---|---|---|
| 1 | **1** | 10–18 | 8–14 | 8–15 |
| 2 | **2** | 28–42 | 20–32 | 20–35 |
| 3 | **3** | 55–75 | 38–58 | 45–65 |
| 4 | **4** | 90–120 | 60–90 | 70–100 |
| 5 | **5** | 130–180 | 90–130 | 100–140 |

AoE abilities use **lower** `base_power` (~80 % of single-target) and **higher** `ap_cost` (~15 % more).  
Status-primary abilities (`effect == "status"`) use `base_power: 0` unless they also deal chip damage (then use ~50 % of the damage range; see `LOW_DMG_STATUS_MOD = 0.5` in `status_utils.py`).

---

## 8. File and Module Layout

old/game/region_seeds/player_abilities/
├── ability_requirements.py          # stat gate source of truth — do not edit for content
├── level_1_abilities.py             # imports level_1_abilities_by_type/* or inline list
├── level_2_abilities.py
├── level_3_abilities.py
├── level_4_abilities.py
├── level_5_abilities.py
├── level_1_abilities_by_type/
│   ├── __init__.py
│   ├── technique.py  faith.py  magic.py  tech.py  skill.py
├── level_2_abilities_by_type/ ...   (same structure)
├── level_3_abilities_by_type/ ...
├── level_4_abilities_by_type/ ...
└── level_5_abilities_by_type/ ...   (create if needed)

### Creating a new by-type file
# level_X_abilities_by_type/technique.py
LEVEL_X_TECHNIQUE_ABILITY_SEEDS = [
    {
        "id": "...",
        ...
        "non_player_ability": False,
    },
]

### Creating / updating the `__init__.py`
# level_X_abilities_by_type/__init__.py
from game.region_seeds.player_abilities.level_X_abilities_by_type.faith     import LEVEL_X_FAITH_ABILITY_SEEDS
from game.region_seeds.player_abilities.level_X_abilities_by_type.magic     import LEVEL_X_MAGIC_ABILITY_SEEDS
from game.region_seeds.player_abilities.level_X_abilities_by_type.skill     import LEVEL_X_SKILL_ABILITY_SEEDS
from game.region_seeds.player_abilities.level_X_abilities_by_type.technique import LEVEL_X_TECHNIQUE_ABILITY_SEEDS
from game.region_seeds.player_abilities.level_X_abilities_by_type.tech      import LEVEL_X_TECH_ABILITY_SEEDS

__all__ = [
    "LEVEL_X_FAITH_ABILITY_SEEDS",
    "LEVEL_X_MAGIC_ABILITY_SEEDS",
    "LEVEL_X_SKILL_ABILITY_SEEDS",
    "LEVEL_X_TECHNIQUE_ABILITY_SEEDS",
    "LEVEL_X_TECH_ABILITY_SEEDS",
]

### Wiring into the top-level file
# level_X_abilities.py
from game.region_seeds.player_abilities.level_X_abilities_by_type import (
    LEVEL_X_FAITH_ABILITY_SEEDS, LEVEL_X_MAGIC_ABILITY_SEEDS,
    LEVEL_X_SKILL_ABILITY_SEEDS, LEVEL_X_TECHNIQUE_ABILITY_SEEDS,
    LEVEL_X_TECH_ABILITY_SEEDS,
)

LEVEL_X_PLAYER_ABILITY_SEEDS = []
LEVEL_X_PLAYER_ABILITY_SEEDS.extend(LEVEL_X_TECHNIQUE_ABILITY_SEEDS)
LEVEL_X_PLAYER_ABILITY_SEEDS.extend(LEVEL_X_FAITH_ABILITY_SEEDS)
LEVEL_X_PLAYER_ABILITY_SEEDS.extend(LEVEL_X_MAGIC_ABILITY_SEEDS)
LEVEL_X_PLAYER_ABILITY_SEEDS.extend(LEVEL_X_TECH_ABILITY_SEEDS)
LEVEL_X_PLAYER_ABILITY_SEEDS.extend(LEVEL_X_SKILL_ABILITY_SEEDS)

Then add to `constants_other.py`:
from game.region_seeds.player_abilities.level_X_abilities import LEVEL_X_PLAYER_ABILITY_SEEDS
# ...
PLAYER_ABILITY_SEEDS.extend(LEVEL_X_PLAYER_ABILITY_SEEDS)

---

## 9. Element Coverage Rules

Derived from inline comments in the existing level modules.

| Level | Elements per ability | Coverage rule |
|---|---|---|
| 1 | exactly 1 | One ability per element (8 × 5 types = 40 minimum) |
| 2 | exactly 2 | All 36 unique unordered pairs including same-element doubles (e.g. `fire,fire`), × 5 types |
| 3 | exactly 3 | One ability per type per 3-element combination; duplicates allowed (e.g. `fire,fire,water`) |
| 4 | exactly 4 | One ability per type per 4-element combination; duplicates allowed |
| 5 | exactly 5 | One ability per type per 5-element combination; duplicates allowed |

For each combination there must be **one representative of each ability type**:
`technique`, `faith`, `magic`, `tech`, `skill`.

---

## 10. Hostile-Only Abilities (`non_player_ability: True`)

Hostile abilities live in the **same** `PLAYER_ABILITY_SEEDS` list but are tagged:
{
    ...,
    "non_player_ability": True,
}

They are **filtered out** of the player learn-screen by `get_potential_player_abilities()` but
are still resolved by the validator and by hostile combat logic.  
Add them to the most thematically appropriate by-type file at the matching level, or create a
dedicated `hostile_only.py` file at any level and import it into `level_X_abilities.py`.

### Researching NPC/Hostile data before authoring

For named hostiles (bosses / story NPCs) referenced in the error table:

1. Find the hostile seed in `old/game/region_seeds/regions/enemies/**` or a dungeon seed file.
2. Note: `name`, `hostile_type`, `role`, `rarity`, `dungeon`, `region`, and any `npc_id`.
3. If an `npc_id` exists, look up the corresponding NPC record in the city/story seed files
   for personality, archetype, speech style, and backstory.
4. Use this data to write a thematic `description` and choose fitting `elements` and `effect`.
5. Map the hostile's combat `role` to ability type — this mirrors the priority order in
   `hostile_seed_engine.py → get_role_based_abilities()`:

   | Hostile `role` | Engine priority order | Recommended ability types |
   |---|---|---|
   | `support` | support buffs → hazard status → damage | `faith` (heals, buffs, revives), then `tech`/`skill` |
   | `hazard` | hazard status first, then damage | `faith` or `magic` for harmful status effects (`continuous_damage`, `confuse`, `sleep`, `silence`, `*_debuff`); NOT `technique` or `skill` |
   | `damage` | damage first, then filler | `technique` (physical), `magic` (elemental), `tech` (precision), `skill` (burst/AoE) |
   | `tank` / `guardian` | hazard → damage | `technique` with constitution emphasis; `faith` for defense buffs |
   | `debuffer` / `assassin` | hazard → damage | `skill` or `tech` for debuffs and status |

   > **Key rule**: `hazard`-role hostiles use **harmful status effects** as their primary
   > combat tool. The engine selects `effect == "status"` abilities with a `status_key` in
   > `HARMFUL_STATUS_EFFECTS` before damage abilities. Author their abilities accordingly —
   > `faith` and `magic` (which map to `intelligence`) are the correct types for a
   > psychologically-themed hazard boss (e.g. Lament, Garbage). Using `technique` or `skill`
   > for a `hazard` hostile means the engine will deprioritise those abilities in favour of
   > any available status ability — give them what the engine will actually reach for first.

---

## 11. Resolving `HOSTILE_UNKNOWN_ABILITY` Errors

The dev-tool validator reports this when a hostile's `player_abilities` list references an ID
not present in `PLAYER_ABILITY_SEEDS`.

**Step-by-step fix:**

1. Copy the missing ID from the error message (e.g. `cold_execution`).
2. Identify the hostile that uses it and research it (section 10 above).
3. Decide on level (1–5) and ability type.
4. Author the seed dict following the schema in section 5.
5. Set `"non_player_ability": True` if it is boss/hostile-exclusive.
6. Add it to the appropriate `level_X_abilities_by_type/{type}.py` file.
7. Confirm the ID in the seed exactly matches the string used in the hostile's
   `player_abilities` list (case-sensitive).
8. Restart the dev TUI or invalidate the ability catalog cache to re-validate.

---

## 12. AI-Assisted Batch Generation Workflow

Use the following prompt template when asking an AI model to generate a batch of abilities:
Context files to supply:
  - ability_requirements.py  (stat gates)
  - constants_other.py       (STATUS_EFFECTS, ELEMENTAL_CHAR_KEYS)
  - player_ability.py        (schema, enums, power formula)
  - This guide (HOSTILE_ABILITY_GENERATION.md)

Instruction:
  Generate {N} ability seeds for ability_type="{type}", level={L}.
  Elements must come from: fire water earth air light dark ice electric.
  Status keys must come from STATUS_EFFECTS keys.
  Use "non_player_ability": True if hostile-only.
  Follow the ID naming convention: {element(s)}_{type}_lv{L}_{name}.
  Each ability must have exactly {L} elements (equal to its level). Duplicate elements are allowed (e.g. ["fire","fire","water"] for level 3).
  Power range for level {L}: {base_power_range}.
  AP cost range: {ap_cost_range}.
  Output as a Python list of dicts, no extra prose.


Supply the hostile's name, dungeon, region, and NPC data when generating hostile-exclusive abilities.

---

## 13. Validation Checklist

Before committing new ability seeds, verify:

- [ ] `id` is unique across **all** entries in `PLAYER_ABILITY_SEEDS`
- [ ] `ability_type` is one of: `technique`, `faith`, `magic`, `tech`, `skill`
- [ ] Every entry in `elements` is a key of `ELEMENTAL_CHAR_KEYS`
- [ ] Every entry in `status_keys` is a key of `STATUS_EFFECTS`
- [ ] `status_keys` is present (and non-empty) when `effect == "status"`
- [ ] `status_keys` is `None` or absent when `effect != "status"`
- [ ] `can_aoe` is explicitly set (`True` or `False`)
- [ ] `non_player_ability` is explicitly set
- [ ] `len(elements) == level` — element count must exactly equal the ability level (duplicates allowed)
- [ ] `base_power` and `ap_cost` are within the level's recommended ranges (section 7)
- [ ] The seed is imported into `level_X_abilities.py` and that module is imported in `constants_other.py`
- [ ] The ID string in the hostile seed's `player_abilities` list exactly matches the ability `id`

Run the dev TUI **Abilities** tab validation to confirm no new errors appear after changes.

---

## 14. Quick-Reference Example: Hostile-Only Ability
# level_3_abilities_by_type/technique.py  (append to existing list)
{
    "id": "cold_execution_technique_lv3_cold_execution",
    "name": "Cold Execution",
    "description": "A precise, emotionless strike that bypasses defence through sheer clinical efficiency.",
    "ability_type": "technique",
    "level": 3,
    "elements": ["ice", "dark", "air"],
    "base_power": 62,
    "ap_cost": 55,
    "effect": "damage",
    "status_keys": None,
    "can_aoe": False,
    "non_player_ability": True,
},

> Then update the hostile seed's `player_abilities` list to use the exact string
> `"cold_execution_technique_lv3_cold_execution"`.

---

## 15. Hostile Ability Error Index (from validator output)

The following IDs were flagged as `HOSTILE_UNKNOWN_ABILITY` and need to be authored.
Each must be added to `PLAYER_ABILITY_SEEDS` with `"non_player_ability": True` unless
the hostile can teach the ability to the player.

| Missing ID | Hostile | Dungeon | Region | Suggested type |
|---|---|---|---|---|
| `cold_execution` | Scalpel / Scalpel's Projection | Bloodspark Arena / Theatre of Echoed Faces | BioHazard / Nightveil Spire | technique |
| `perfect_cut` | Scalpel | Bloodspark Arena | BioHazard | technique / skill |
| `detached_slaughter` | Scalpel | Bloodspark Arena | BioHazard | technique |
| `radiant_lie` | Glamour | Bloodspark Arena | BioHazard | faith / magic |
| `beauty_as_weapon` | Glamour | Bloodspark Arena | BioHazard | skill / faith |
| `suffocating_allure` | Glamour | Bloodspark Arena | BioHazard | faith |
| `blood_spectacle` | Rapture | Festival of Delight | Blackwake Bay | technique / skill |
| `thrill_of_ruin` | Rapture | Festival of Delight | Blackwake Bay | technique |
| `seizing_the_moment` | Rapture | Festival of Delight | Blackwake Bay | skill |
| `manic_freedom` | Revelry | Festival of Delight | Blackwake Bay | skill / magic |
| `collapse_of_joy` | Revelry | Festival of Delight | Blackwake Bay | magic |
| `wild_possibility` | Revelry | Festival of Delight | Blackwake Bay | magic / tech |
| `absolute_disgust` | Garbage | Grand Mausoleum | The Necropolis | magic / tech |
| `distortion_of_reality` | Garbage | Grand Mausoleum | The Necropolis | magic |
| `the_epic_you_never_were` | Garbage | Grand Mausoleum | The Necropolis | faith / magic |
| `endless_tragedy` | Lament | Grand Mausoleum | The Necropolis | faith / magic |
| `collapse_of_self` | Lament | Grand Mausoleum | The Necropolis | magic |
| `singularity_of_grief` | Lament | Grand Mausoleum | The Necropolis | magic |
| `void_refraction` | Stigma | The Citadel / Overworld | Hailward Hold | magic / dark |
| `the_darkness_consuming` | Stigma | The Citadel / Overworld | Hailward Hold | magic |
| `you_can_be_me` | Stigma | The Citadel / Overworld | Hailward Hold | faith / magic |
| `mask_of_expectation` | Pageant | The Velvet Veil / The Citadel | Hailward Hold | faith / skill |
| `crushing_reputation` | Pageant | The Velvet Veil / The Citadel | Hailward Hold | technique / faith |
| `obligation_chain` | Pageant | The Velvet Veil / The Citadel | Hailward Hold | faith |
| `ancient_rule` | Edict | The Citadel | Hailward Hold | faith / technique |
| `inescapable_edict` | Edict | The Citadel | Hailward Hold | faith |
| `ritual_punishment` | Edict | The Citadel | Hailward Hold | technique / faith |
| `impossibility_storm` | Crux / Crux - Origin Form | Punishment Engines / Origin Spire | Gallows Rift / Thornshade Hamlet | magic / tech |
| `debuff_the_wicked` | Crux | Punishment Engines | Gallows Rift | tech / faith |
| `demonic_fury` | Paradox | Punishment Engines | Gallows Rift | technique / magic |
| `infuriating_revelation` | Paradox | Punishment Engines | Gallows Rift | magic |
| `they_arent_who_you_are` | Paradox | Punishment Engines | Gallows Rift | faith / magic |
| `absolute_destruction` | Cataclysm | Collapsing Spire | Aurelion Veil | magic / technique |
| `calamity` | Cataclysm | Collapsing Spire | Aurelion Veil | magic |
| `eternal_nerve` | Cataclysm | Collapsing Spire | Aurelion Veil | technique / faith |
| `inevitability_matrix` | Dominion | Overworld | — | tech / magic |
| `inescapable_fate` | Dominion | Overworld | — | faith / magic |
| `void_lattice` | Dominion | Overworld | — | magic / tech |
| `eternal_void` | Void | Overworld | — | magic |
| `absolution` | Void | Overworld | — | faith |
| `unfinity` | Void | Overworld | — | magic |
| `contradiction_loop` | Crux Trial / Paradox Trial | The System of Compliance / Sensation | Hollerforge Hollow | tech / magic |
| `simulated_truth` | Crux Trial | The System of Compliance | Hollerforge Hollow | tech |
| `objective_elimination` | Crux Trial | The System of Compliance | Hollerforge Hollow | technique / tech |
| `system_lockdown` | Edict Trial | The System of Compliance | Hollerforge Hollow | tech / faith |
| `rule_enforcement` | Edict Trial | The System of Compliance | Hollerforge Hollow | technique / faith |
| `procedural_inevitability` | Edict Trial | The System of Compliance | Hollerforge Hollow | faith |
| `certainty_field` | Glamour Trial | The System of Compliance | Hollerforge Hollow | magic / faith |
| `doubt_erasure` | Glamour Trial | The System of Compliance | Hollerforge Hollow | faith |
| `calm_enforcement` | Glamour Trial | The System of Compliance | Hollerforge Hollow | faith / tech |
| `adrenaline_surge` | Rapture Trial | The System of Identity | Hollerforge Hollow | skill / technique |
| `reckless_abandon` | Rapture Trial | The System of Identity | Hollerforge Hollow | skill |
| `thrill_addiction` | Rapture Trial | The System of Identity | Hollerforge Hollow | skill / magic |
| `crushing_despair` | Lament Trial | The System of Sensation | Hollerforge Hollow | magic / faith |
| `hollow_silence` | Lament Trial | The System of Sensation | Hollerforge Hollow | magic |
| `the_emptiness` | Lament Trial | The System of Sensation | Hollerforge Hollow | magic |
| `impossible_truth` | Paradox Trial | The System of Sensation | Hollerforge Hollow | magic / tech |
| `paradox_embrace` | Paradox Trial | The System of Sensation | Hollerforge Hollow | magic |
| `euphoric_cascade` | Revelry Trial | The System of Sensation | Hollerforge Hollow | magic / skill |
| `sensory_overload` | Revelry Trial | The System of Sensation | Hollerforge Hollow | magic |
| `the_rush` | Revelry Trial | The System of Sensation | Hollerforge Hollow | skill |
| `intrusive_truth` | Garbage Trial | The System of Perception | Hollerforge Hollow | magic / tech |
| `self_sabotage` | Garbage Trial | The System of Perception | Hollerforge Hollow | magic |
| `unwanted_knowing` | Garbage Trial | The System of Perception | Hollerforge Hollow | faith / magic |
| `inescapable_prophecy` | Oracle / Oracle Trial | The System of Perception / Memory Museum | Hollerforge Hollow / Bayou Nocturne | faith / magic |
| `vision_of_ruin` | Oracle | Memory Museum | Bayou Nocturne | magic / faith |
| `fate_lock` | Oracle | Memory Museum | Bayou Nocturne | faith |
| `eternal_wound` | Reliquary | Memory Museum / The System of Memory | Bayou Nocturne / Hollerforge Hollow | faith / technique |
| `memory_of_suffering` | Reliquary | Memory Museum | Bayou Nocturne | faith / magic |
| `burden_of_the_lost` | Reliquary | Memory Museum | Bayou Nocturne | faith |
| `systematic_destruction` | Cataclysm Trial | The System of Memory | Hollerforge Hollow | tech / magic |
| `refinement_loop` | Cataclysm Trial | The System of Memory | Hollerforge Hollow | tech |
| `inevitable_failure` | Cataclysm Trial | The System of Memory | Hollerforge Hollow | magic / faith |

---

The guide covers everything needed to systematically resolve the missing ability errors:

- **Sections 1–4** establish which files are authoritative for types, elements, and status keys — no hardcoding anywhere else.
- **Section 5–6** give the exact seed schema and ID naming convention mirroring the existing files.
- **Section 7** provides level-scaled power/AP ranges derived from the existing seeds.
- **Section 8** shows the module layout, how to create a new by-type file, its `__init__.py`, and how to wire it into `constants_other.py`.
- **Section 10** covers the NPC research workflow for named boss hostiles.
- **Section 11** is the step-by-step fix for each `HOSTILE_UNKNOWN_ABILITY` error.
- **Section 12** is a reusable AI prompt template for batch generation.
- **Section 13** is a pre-commit validation checklist.
- **Section 14** gives a concrete hostile-only ability example using `cold_execution`.
- **Section 15** is the full index of every missing ID from the validator output, pre-categorised by hostile, dungeon, region, and suggested ability type.