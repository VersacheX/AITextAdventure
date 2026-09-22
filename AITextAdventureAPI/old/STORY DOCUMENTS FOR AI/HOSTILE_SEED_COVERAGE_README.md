# Hostile Seed Coverage — AI Governance Document

## Purpose

Every region has four zones that must each have at least one hostile seed covering every 10-level band from **Lv 1 to Lv 100**. This document governs how to fill those gaps correctly and how to assign non-player abilities to hostiles.

The validator (`city_region_validator.py`) reports `REGION_HOSTILE_COVERAGE_GAP` for each missing band. All 7 regions × 4 zones × 8 bands (Lv 21–100) = **224 individual files** must be created or extended.

---

## Validator Reality & Field Notes (READ FIRST)

> Reconstructed from the current `city_region_validator.py`, `hostile_validator.py`,
> `old/game/constants.py` (`REGION_DATA`), and the existing seed/aggregator files.
> These notes correct and extend the older guidance below. **When the two disagree,
> trust this section** — it reflects what the code actually checks today.

### 1. The real failing rule is R4 `REGION_HOSTILE_RARITY_GAP`, not R1 band coverage

The 10-level-band model in this doc is necessary but **not sufficient**. The hard
errors come from a **sliding 5-level window** check in `city_region_validator.py`:

- Window size is **5** (`_RARITY_WINDOW = 5`), sliding: Lv 1–5, 2–6, 3–7, … 96–100.
- For **each** rarity in `("common", "uncommon", "rare", "superrare")`, **every**
  window must contain at least one seed whose `min_spawn_level` falls inside it.
- A seed at level `N` covers the windows starting at `N-4 … N` (reaches back 4
  levels, forward 0).
- Each error line `add a '<rarity>' hostile seed at Lv N` is the validator's own
  greedy minimal-fill suggestion (`_minimal_rarity_additions` places seeds at the
  right edge of the earliest uncovered window). **Placing a seed at exactly the
  suggested Lv N is the most efficient fix** — one seed there typically clears
  several stacked error lines at once.

**Practical consequence:** because each seed only covers a 5-wide window, you need
a seed of every required rarity roughly every 5 levels — including `rare` and
`superrare`. This overrides the "~5% superrare per band" advice below: you will
need far more `rare`/`superrare` coverage than that ratio implies. A workable
pattern per 10-level band is ~2 seeds low (e.g. Lv 21, 23) and ~2 high (e.g. Lv 26,
29), spread across rarities so no single rarity has a gap wider than 5 levels.

### 2. Band-file names and export names are NOT uniform across zones

Do **not** assume `lv31to40.py`, `lv41to50.py`, … exist everywhere. Confirmed splits vary per zone, e.g.:

- `desert/enemies_large`: per-10 up to 60, then wide — `… lv61to80, lv81to100`.
- `desert/enemies_mid`: `lv1to10, lv11to20, lv21to30, lv31to50, lv51to100`.
- `shallows/*` and `swamp/*` large: per-10 files `lv21to30 … lv91to100`.

Export names also differ:

- Most band files export `RANDOM_HOSTILE_SEEDS = [...]`.
- Some early files (notably shallows/swamp) export `SEEDS_LV1TO10` / `SEEDS_LV11TO20`
  instead, and the aggregator imports them under an alias.

**Rule:** open the zone's `constants_enemies_*.py` aggregator first and mirror
whatever import style, module names, and export names it already uses. Match the
existing convention for that specific zone rather than forcing this doc's names.

### 3. Registration is TWO layers, not one

A new band file must be wired in at **both** levels or it will never load:

1. **Aggregator** — `constants_enemies_<size>_city.py` (cities) or
   `constants_enemies_<region>.py` (overworld). Add the `import` and append the
   list. Aggregators use either `RANDOM_HOSTILE_SEEDS.extend(...)` **or** `A + B + C`
   concatenation, and either absolute (`game.region_seeds…`) or relative
   (`.enemies_large…`) imports — match the file.
2. **`old/game/constants.py` `REGION_DATA`** already imports each aggregator's
   `RANDOM_HOSTILE_SEEDS` (e.g. `DESERT_LARGE_CITY_RANDOM_HOSTILE_SEEDS`). You do
   **not** normally edit `constants.py` — it re-reads the aggregator — but note the
   overworld zone is composed as
   `<REGION>_RANDOM_HOSTILE_SEEDS + <REGION>_REGION_HOSTILE_SEEDS`, so overworld
   seeds can live in two different modules that are concatenated.

### 3b. Shared per-region hostiles (`enemies_shared/`) — PREFERRED for rarity fill

Because every zone in a region shares the same biome identity, hostiles authored
to fill rarity gaps can be written **once** and reused by all four zones (large /
mid / small city + overworld). This avoids duplicating near-identical seeds four
times per region.

Convention (established for Desert, mirror it per region):

```
regions/cities/<region>/enemies_shared/
    __init__.py                 ? aggregates all bands into one RANDOM_HOSTILE_SEEDS
    lv1to20_rarity_fill.py
    lv21to40_rarity_fill.py
    lv41to60_rarity_fill.py
    lv61to80_rarity_fill.py
    lv81to100_rarity_fill.py
```

- Each `lv<a>to<b>_rarity_fill.py` exports `RANDOM_HOSTILE_SEEDS = [...]` and holds
  the seeds for that band.
- **Make the shared roster self-sufficient for ANY zone.** The desert file was
  built reactively (one seed per validator-suggested level, tuned to the large
  city). The problem: mid/small cities have *different* existing seeds, so those
  exact levels don't clear their windows — you end up chasing residual gaps per
  zone. Instead, build the shared roster so it covers every window on its own:
  **place one seed of every required rarity (`common`, `uncommon`, `rare`,
  `superrare`) at each 5-level mark — Lv 5, 10, 15, … 100.** A seed at level N
  covers the sliding windows starting N-4..N, so multiples of 5 blanket all
  windows 1-5 … 96-100 regardless of what a zone already defines. That is 20 marks
  × 4 rarities = **80 seeds** split across the five band files (this is how Forest
  was built). Any zone importing the shared package is then fully covered.
- **Work small city first.** The small city usually has the fewest existing seeds,
  so a shared roster that satisfies the small city will satisfy mid and large too.
  Validate small ? mid ? large per region.
- `enemies_shared/__init__.py` imports every band module and concatenates them into
  a single package-level `RANDOM_HOSTILE_SEEDS`, so each city aggregator needs only
  **one** import — not one per band:

  ```python
  from game.region_seeds.regions.cities.<region>.enemies_shared import (
      RANDOM_HOSTILE_SEEDS as RARITY_FILL_HOSTILES,
  )
  # then, matching the aggregator's existing style:
  RANDOM_HOSTILE_SEEDS.extend(RARITY_FILL_HOSTILES or [])   # extend-style files
  # or
  RANDOM_HOSTILE_SEEDS = LV1TO10 + ... + RARITY_FILL_HOSTILES  # concat-style files
  ```

- **Namespace shared ids to avoid collisions.** Prefix shared seed ids with
  `<region>_shared_` (e.g. `forest_shared_root_golem`) so they never clash with a
  zone's own band-file ids.
- **Import the same shared package into every zone aggregator that needs the fill**
  (`constants_enemies_large_city.py`, `constants_enemies_mid_city.py`,
  `constants_enemies_small_city.py`, and the overworld `constants_enemies_<region>.py`).
  Match each aggregator's existing import style (absolute vs relative) and
  composition style (`.extend()` vs `+`).
- **Duplicate ids across zones are safe here by design.** The same seed id
  surfacing in multiple zones resolves to identical data, so there is no data-
  integrity concern from the overlap — every zone simply gets the same shared
  hostile definition.
- Keep zone-specific flavour hostiles in the zone's own `enemies_<size>/` band
  files; use `enemies_shared/` only for the reusable region-wide roster.

### 4. Other validators also fire on your new seeds (`hostile_validator.py`)

R4 is only the coverage rule. Each seed you add is independently checked:

- **H1 unknown rarity** — must be `common|uncommon|rare|superrare` (`notfound` is
  also recognised but don't use it).
- **H2 missing attacks** — `basic_attack` must be non-empty.
- **H3 missing base stats** — `base_hp` and `base_ap` must be > 0.
- **H4 ability count vs rarity** — minimum ability counts are enforced
  (`_RARITY_ABILITY_COUNTS`): `common 0`, `uncommon ?1`, `rare ?2`, `superrare ?3`
  (`notfound 4`). This is the **hard floor** — stricter than the "common 0-1 /
  uncommon 1-2 …" ranges below.
- **H4b unknown ability** — every id in `player_abilities` must exist in
  `PLAYER_ABILITY_SEEDS`. **Do not invent ability ids.** Verify against the
  `level_*_abilities*` modules; the tables in this doc are a starting point, confirm
  before use.
- **H5 missing type** — `hostile_type` must be set.
- **H6 unknown drop item** — `common_drop` / `rare_drop` must be `None` or a real id
  drawn from `SEED_UTILITY_IDS`, `SEED_SPECIAL_IDS`, `SEED_WEAPON_IDS`,
  `SEED_ACCESSORY_IDS`, or `SEED_ARMOR_IDS` (defined in `constants_items.py` and
  `constants_accesories.py`). The verified consumable ids are
  `herb_minor`, `herb_med`, `herb_major`, `elixir_full_heal`, `stimulant_small`,
  `stimulant_med`, `stimulant_large`, `stimulant_full`, `revive_kit`,
  `defibrillator`, `ointment`, `petrify_salve`, `wake_potion`, `shock_patch`,
  `clarity_tonic`, `vocalsalve`, `panacea`, and the `tome_*` line. Note the healing
  herb id is **`herb_med`** (not `herb_medium`) and the AP items are `stimulant_*`.
  Weapon/armor/accessory drop ids come from the level-banded seed modules
  (`region_seeds/weapons/*`, `region_seeds/armor/*`) and `ACCESSORY_SEEDS`.

### 5. Fast validation loop

- Dev TUI: **Validate Regions** (runs `validate_region_data(REGION_DATA)`).
- Headless: `old/check_bands.py` imports `REGION_DATA` and runs the validator,
  printing error/warning counts per zone — handy for a quick pass/fail after
  editing one city.

### 6. Suggested per-zone workflow (city by city)

1. Read the zone's `constants_enemies_*.py` to learn its module/export conventions.
2. Collect that zone's `REGION_HOSTILE_RARITY_GAP` lines from the report.
3. For each suggested `Lv N` + rarity, author one themed seed at exactly `Lv N`
   (grouping several suggestions into shared band files where naming allows).
4. Satisfy the H4 ability floor for the seed's rarity using verified ability ids.
5. Wire the new band file(s) into the aggregator, matching its import style.
6. Re-run validation; confirm that zone's error count drops to 0 before moving on.

---

## Directory Structure

```
old/game/region_seeds/regions/
??? enemies/                            ? overworld hostile seeds
?   ??? desert/
?   ?   ??? lv1to10.py
?   ?   ??? lv11to20.py
?   ?   ??? lv21to30.py  ? needs lv31+ files
?   ??? forest/
?   ??? grassland/
?   ??? mountains/
?   ??? shallows/
?   ??? snow/
?   ??? swamp/
??? cities/
    ??? desert/
    ?   ??? enemies_large/              ? large city hostile seeds
    ?   ?   ??? lv1to10.py
    ?   ?   ??? lv11to20.py
    ?   ?   ??? lv21to30.py  ? needs lv31+ files
    ?   ??? enemies_mid/
    ?   ??? enemies_small/
    ??? forest/
    ??? grassland/
    ??? mountains/
    ??? shallows/
    ??? snow/
    ??? swamp/
```

Each `constants_enemies_<size>_city.py` (and `constants_enemies_<region>.py` for overworld) imports the per-band modules and aggregates them. New band files must be added **both** as standalone `lv##to##.py` modules **and** imported in the parent constants file.

---

## File Naming Convention

```
lv21to30.py   ? min_spawn_level 21–30
lv31to40.py   ? min_spawn_level 31–40
lv41to50.py   ? min_spawn_level 41–50
lv51to60.py   ? min_spawn_level 51–60
lv61to70.py   ? min_spawn_level 61–70
lv71to80.py   ? min_spawn_level 71–80
lv81to90.py   ? min_spawn_level 81–90
lv91to100.py  ? min_spawn_level 91–100
```

Each file must export `RANDOM_HOSTILE_SEEDS = [...]`.

---

## Hostile Seed Schema

Every seed is one dict in the list. All fields are required unless noted.

```python
{
  "id":               str,   # unique snake_case, e.g. "dune_scorpion_alpha"
  "name":             str,   # display name
  "hostile_type":     str,   # see Hostile Types below
  "role":             str,   # see Roles below
  "min_spawn_level":  int,   # the lowest level at which this hostile can appear
  "rarity":           str,   # "common" | "uncommon" | "rare" | "superrare"
  "base_xp":          int,   # xp rewarded at min_spawn_level
  "common_drop":      str | None,  # item_id or consumable key
  "rare_drop":        str | None,  # item_id or consumable key
  "money_range":      tuple[int,int],  # (min, max) gold dropped
  "basic_attack":     str,   # short flavor text for the basic attack
  "strong_attack":    str,   # short flavor text for the strong attack
  "player_abilities": list[str] | None,  # ability IDs (see Abilities section)
  "base_str":         int,
  "base_dex":         int,
  "base_con":         int,
  "base_int":         int,
  "base_hp":          int,
  "base_ap":          int,
  "str_per_level":    int,   # stat growth per level above min_spawn_level
  "dex_per_level":    int,
  "con_per_level":    int,
  "int_per_level":    int,
}
```

---

## Hostile Types

| `hostile_type` | Description |
|---|---|
| `humanoid` | Person-shaped — bandits, soldiers, cultists, etc. |
| `creature` | Animals, beasts, monsters |
| `undead` | Zombies, skeletons, ghosts, revenants |
| `elemental` | Fire spirits, ice golems, storm entities |
| `eldritch` | Mind-bending, cosmic horror, dream eaters |
| `construct` | Mechanical, clockwork, arcane automata |

---

## Roles

| `role` | Combat behavior |
|---|---|
| `damage` | Primary attacker — high STR or DEX, moderate HP |
| `hazard` | Applies status effects and debuffs — high INT |
| `support` | Heals allies or buffs self — high CON |

---

## Stat Scaling Guide by Level Band

Use these as baselines. Scale up by ~15–20% per 10 levels. Adjust for role and rarity.

| Band | base_hp | base_ap | base_str | base_dex | base_con | base_int | base_xp |
|---|---|---|---|---|---|---|---|
| Lv 21–30 | 60–120 | 4–8 | 4–10 | 3–8 | 4–9 | 3–8 | 80–400 |
| Lv 31–40 | 120–220 | 6–10 | 7–15 | 5–12 | 7–14 | 5–12 | 250–700 |
| Lv 41–50 | 200–380 | 8–12 | 12–22 | 8–18 | 12–20 | 8–18 | 600–1400 |
| Lv 51–60 | 350–600 | 10–14 | 18–32 | 12–25 | 18–30 | 12–25 | 1200–2500 |
| Lv 61–70 | 550–900 | 12–16 | 26–45 | 18–35 | 26–42 | 18–35 | 2200–4500 |
| Lv 71–80 | 800–1400 | 14–18 | 36–60 | 25–48 | 36–58 | 25–48 | 4000–8000 |
| Lv 81–90 | 1200–2000 | 16–22 | 50–80 | 35–65 | 50–78 | 35–65 | 7000–14000 |
| Lv 91–100 | 1800–3000 | 18–26 | 70–110 | 50–90 | 70–108 | 50–90 | 12000–24000 |

**Per-level growth** (str/dex/con/int_per_level):
- Lv 21–40: 1–3 per stat
- Lv 41–60: 2–5 per stat
- Lv 61–80: 3–7 per stat
- Lv 81–100: 5–10 per stat

**Rarity affects base_xp multiplier:**
- `common`: ×1.0
- `uncommon`: ×1.3
- `rare`: ×1.8
- `superrare`: ×2.8

---

## How Many Seeds Per Band?

Minimum per file: **3–5 seeds** covering different `min_spawn_level` values within the band (e.g. 21, 23, 26, 29 for the 21–30 band). Aim for at least 2 different roles and 2 different types per band. More variety is always better.

---

## Consumable / Drop Keys

Verified ids from `constants_items.py` (`UTILITY_ITEM_SEEDS` ? `SEED_UTILITY_IDS`).
Use these exact strings for `common_drop` / `rare_drop`:

### HP / AP restoratives

| Key | Item | Rarity | min_spawn_level |
|---|---|---|---|
| `"herb_minor"` | Pocket Salve (heal 25%) | common | 1 |
| `"herb_med"` | Patch Kit (heal 50%) | uncommon | 4 |
| `"herb_major"` | Curative Salve (heal 75%) | rare | 10 |
| `"elixir_full_heal"` | Stimpak (heal 100%) | superrare | 15 |
| `"stimulant_small"` | Caffeine Shot (AP 25%) | common | 1 |
| `"stimulant_med"` | Energy Drink (AP 50%) | uncommon | 4 |
| `"stimulant_large"` | Adrenaline Shot (AP 75%) | rare | 10 |
| `"stimulant_full"` | Neuro Stim (AP 100%) | superrare | 15 |

> Note the healing item is `herb_med` (**not** `herb_medium`), and the AP items use
> the `stimulant_*` prefix. `herb_major` is a **rare** drop despite the name.

### Revives / status cures

| Key | Item |
|---|---|
| `"revive_kit"` | Revival Kit (revive 50%) |
| `"defibrillator"` | Defibrillator (revive 100%) |
| `"ointment"` | Balm — cure continuous_damage |
| `"petrify_salve"` | Limestone Salve — cure petrify |
| `"wake_potion"` | Wake Draught — cure sleep |
| `"shock_patch"` | Shock Patch — cure stun |
| `"clarity_tonic"` | Clarity Tonic — cure confuse |
| `"vocalsalve"` | Vocal Salve — cure silence |
| `"panacea"` | Doc's Panacea — cure all debuffs |

### Stat tomes (`rarity: notfound` — use sparingly, high-tier only)

`"tome_hp"`, `"tome_ap"`, `"tome_str"`, `"tome_dex"`, `"tome_int"`, `"tome_con"`
(+1), and the `*_superrare` variants (`"tome_str_superrare"`, etc., +5).

| Key | Item |
|---|---|
| `None` | No drop |

For higher-rarity hostiles, rare drops can reference **weapon** ids from
`region_seeds/weapons/*` (`SEED_WEAPON_IDS`), **armor** ids from
`region_seeds/armor/*` (`SEED_ARMOR_IDS`, keyed by slot: head/body/arms/legs), or
**accessory** ids from `ACCESSORY_SEEDS` in `constants_accesories.py`
(`SEED_ACCESSORY_IDS`, e.g. `"toughened_cord"`, `"warlord_signet"`,
`"voidborn_seal"`). Always pick an item whose `min_spawn_level` / `min_level`
matches the hostile's band, and confirm the exact id exists before using it.

---

## Non-Player Abilities (`player_abilities`)

The `player_abilities` field takes a **list of ability ID strings**, or `None` / `[]` for no special abilities.

> **Rule:** Only use `non_player_ability: True` abilities for hostiles Lv 21+. Lv 1–20 hostiles may reference standard player ability IDs from Lv 1–2 ability files.

### Level 1 Hostile Abilities (Lv 1–30 hostiles)

These are defined in `level_1_abilities.py` and have `"non_player_ability": True`.

| ID | Effect | Elements |
|---|---|---|
| `level_1_hostile_ability_electric_tech_hack_overload` | `intelligence_debuff` | electric |
| `level_1_hostile_ability_poison_dart` | `continuous_damage` | dark |
| `level_1_hostile_ability_streamlet` | damage | water |
| `level_1_hostile_ability_dark_magic_daze_whisper` | `confuse` | dark |
| `level_1_hostile_ability_light_spirit_prism_burst` | `dexterity_debuff` | light |
| `level_1_hostile_ability_air_skill_quick_shot` | `dexterity_debuff` | air |
| `level_1_hostile_ability_dark_skill_corrosive_spit` | `strength_debuff` | dark |
| `level_1_hostile_ability_fire_spirit_ember_shield` | `strength_debuff` | fire |
| `level_1_hostile_ability_air_magic_gale_surge` | `dexterity_debuff` | air |
| `level_1_hostile_ability_air_skill_gale_dash` | `dexterity_debuff` | air |
| `level_1_hostile_ability_electric_magic_chain_lightning` | damage (AoE) | electric |
| `level_1_hostile_ability_fire_spirit_hearthsong` | `attack_buff` | fire |
| `level_1_hostile_ability_bone_spear` | damage | dark |
| `level_1_hostile_ability_shadow_lash` | damage | dark |
| `level_1_hostile_ability_shadow_flicker` | evasion/status | dark |
| `level_1_hostile_ability_smoke_screen` | `dexterity_debuff` | air |
| `level_1_hostile_ability_reinforce_frame` | `defense_buff` | earth |
| `level_1_hostile_ability_inspire` | `attack_buff` | light |
| `level_1_hostile_ability_night_whisper` | `confuse` | dark |
| `level_1_hostile_ability_earth_magic_sap_bloom` | status | earth |
| `level_1_hostile_ability_arcane_blast` | damage | (none) |
| `level_1_hostile_ability_air_skill_gale_dash` | `dexterity_debuff` | air |

Standard Lv 1 player abilities also usable (no `non_player_ability` flag required for hostiles):

- `fire_technique_lv1_scorch_slash`, `earth_technique_lv1_armor_up`, `dark_technique_lv1_night_claw`
- `light_spirit_lv1_minor_heal`, `dark_magic_lv1_shadow_tendril`, `fire_magic_lv1_fireball`
- `air_skill_lv1_smoke_bomb`, `ice_skill_lv1_ice_shuriken`

### Level 2 Hostile Abilities (Lv 21–50 hostiles)

Defined in `level_2_abilities_by_type/`.

| ID | Type | Effect | Elements |
|---|---|---|---|
| `lv2_hostile_ability_dark_dark_spirit_void_veil` | faith | `elemental_debuff` | dark/dark |
| `lv2_hostile_ability_air_water_spirit_gale_of_silence` | faith | `silence` | air/water |
| `lv2_hostile_ability_water_light_fae_glimmer` | faith | `confuse` | water/light |
| `lv2_hostile_ability_dark_light_spirit_calm_bleat` | faith | heal | dark/light |
| `lv2_hostile_ability_earth_air_spirit_thornbind` | faith | status | earth/air |
| `lv2_hostile_ability_fire_earth_magic_pyroclasm` | magic | damage | fire/earth |
| `lv2_hostile_ability_dark_electric_magic_abyssal_storm` | magic | damage | dark/electric |
| `lv2_hostile_ability_water_electric_magic_maelstrom_burst` | magic | damage | water/electric |
| `lv2_hostile_ability_ice_light_magic_frost_nova` | magic | damage | ice/light |
| `lv2_hostile_ability_ice_light_magic_stellar_fall` | magic | damage | ice/light |
| `lv2_hostile_ability_water_dark_magic_gloom_tide` | magic | damage | water/dark |
| `lv2_hostile_ability_dark_air_skill_nightmare_wave` | skill | status | dark/air |
| `lv2_hostile_ability_dark_ice_skill_void_spike` | skill | damage | dark/ice |
| `lv2_hostile_ability_fire_water_tech_steam_grenade` | tech | damage/status | fire/water |
| `lv2_hostile_ability_earth_light_tech_primal_disunion` | tech | debuff | earth/light |
| `lv2_hostile_ability_dark_electric_tech_nether_catalyst_bomb` | tech | damage | dark/electric |
| `lv2_hostile_ability_dark_water_tech_void_spatter` | tech | status | dark/water |
| `lv2_hostile_ability_electric_earth_tech_ion_leech` | tech | debuff | electric/earth |
| `earth_fire_technique_lv2_berserker_tech` | technique | damage | earth/fire |
| `earth_earth_technique_lv2_earth_sunder` | technique | damage | earth/earth |
| `earth_earth_technique_lv2_brutal_swing` | technique | damage | earth/earth |
| `earth_light_technique_lv2_stone_guard` | technique | `defense_buff` | earth/light |
| `air_air_technique_lv2_whirlwind_barrage` | technique | damage | air/air |
| `earth_electric_lv2_technique_chain_reactor` | technique | damage | earth/electric |

Standard Lv 2 player abilities also usable for Lv 21–50 hostiles:
- `fire_dark_skill_lv2_embersmoke`, `air_light_skill_lv2_dawn_cut`
- `dark_dark_magic_lv2_umbra_storm`, `electric_fire_magic_lv2_arclance`
- `fire_air_tech_lv2_aero_flare`

### Level 3 Hostile Abilities (Lv 41–70 hostiles)

Defined in `level_3_abilities_by_type/`. These have thematic/narrative names. Use for elite or boss-adjacent variants.

Notable IDs: `suffocating_allure`, `the_epic_you_never_were`, `obligation_chain`, `wild_possibility`, `singularity_of_grief`, `weight_of_memory`, `seductive_void`, `performance_is_mandatory`, `glitch_cascade`, `paradox_touch`, `entropic_spiral`, `static_erasure`, `detached_slaughter`, `seizing_the_moment`, `predator_rush`, `rot_of_potential`

### Level 4 Hostile Abilities (Lv 61–90 hostiles)

Defined in `level_4_abilities_by_type/`. Used for powerful elites.

Notable IDs: `radiant_lie`, `collapse_of_joy`, `endless_tragedy`, `the_darkness_consuming`, `mask_of_expectation`, `crushing_reputation`, `infuriating_revelation`, `they_arent_who_you_are`, `eternal_nerve`, `beauty_as_weapon`, `manic_freedom`, `distortion_of_reality`, `collapse_of_self`, `void_refraction`, `identity_collapse`, `inescapable_edict`, `curtain_call_offensive`, `impossibility_storm`, `demonic_fury`, `structural_paradox`, `perfect_cut`, `thrill_of_ruin`, `logic_collapse`, `cold_execution`, `blood_spectacle`, `absolute_disgust`, `ancient_rule`, `ritual_punishment`, `scheduled_obliteration`

### Level 5 Hostile Abilities (Lv 81–100 hostiles)

Defined in `level_5_abilities_by_type/`. Reserved for highest-tier enemies.

Notable IDs: `procedural_inevitability`, `certainty_field`, `doubt_erasure`, `calm_enforcement`, `inescapable_prophecy`, `fate_lock`, `eternal_wound`, `burden_of_the_lost`, `unwanted_knowing`, `inescapable_fate`, `absolution`, `calamity`, `vision_of_ruin`, `memory_of_suffering`, `crushing_despair`, `hollow_silence`, `the_emptiness`, `paradox_embrace`, `euphoric_cascade`, `sensory_overload`, `intrusive_truth`, `self_sabotage`, `inevitable_failure`, `void_lattice`, `eternal_void`, `unfinity`, `adrenaline_surge`, `reckless_abandon`, `thrill_addiction`, `the_rush`, `contradiction_loop`, `simulated_truth`, `system_lockdown`, `impossible_truth`, `systematic_destruction`, `refinement_loop`, `inevitability_matrix`, `absolute_destruction`, `objective_elimination`, `rule_enforcement`

### Appriate Abilities for creature type, hazard, or support role hostiles can be found in the respective level 2–5 ability files. Use thematic judgment to select abilities that fit the hostile's type and narrative.

Hostiles Should follow ability requirement count per hostile rarity (common 0-1, uncommon 1-2, rare 2-3, superrare 3-4, notfound 3-4) and per hostile level band (see table below).

## Creating new abilities for hostiles

It is ok to create new abilities for hostiles which follow the naming conventions...
When creating new abilities, be sure to include them in the appropriate level_#_abilities_by_type/ file and mark them with `"non_player_ability": True`. Avoid creating abilities that are too similar to existing ones unless they have a unique effect or thematic twist. Always ensure that new abilities are balanced for the level band and role of the hostile.

---

## Ability Assignment Guidelines

| Hostile Level | Recommended Abilities |
|---|---|
| Lv 1–20 | 0–1 ability; Lv 1 hostile abilities or basic Lv 1 player abilities |
| Lv 21–30 | 0–2; Lv 1 hostile abilities or Lv 2 hostile/player abilities |
| Lv 31–50 | 1–2; Lv 2 hostile abilities preferred; Lv 3 for elites |
| Lv 51–70 | 1–3; Lv 3 abilities; Lv 4 for rare/superrare |
| Lv 71–90 | 2–3; Lv 4 abilities; Lv 5 for superrare |
| Lv 91–100 | 2–4; Lv 5 abilities |

- **`damage` role** hostiles: pick damage-effect abilities
- **`hazard` role** hostiles: pick status/debuff abilities
- **`support` role** hostiles: pick heal/buff abilities
- `player_abilities: None` or `[]` is valid for pure melee/physical brutes

---

## Adding a New Band File — Step by Step

1. **Create** `lv##to##.py` in the correct enemies directory (e.g. `regions/cities/desert/enemies_large/lv31to40.py`)
2. **Write** 3–6 seeds, all within the band's level range, varied roles and types
3. **Open** the parent `constants_enemies_large_city.py` (or `constants_enemies_<region>.py`)
4. **Import** the new module and append to the aggregated list:

```python
from game.region_seeds.regions.cities.desert.enemies_large.lv31to40 import RANDOM_HOSTILE_SEEDS as LV31TO40_HOSTILES

RANDOM_HOSTILE_SEEDS = (
    LV1TO10_HOSTILES
    + LV11TO20_HOSTILES
    + LV21TO30_HOSTILES
    + LV31TO40_HOSTILES  # ? add here
)
```

5. **Validate** by running `Validate Regions` in the dev TUI — the gap for that band should disappear.

---

## Work Tracker

### Zones Needing Coverage (Lv 21–100)

Each cell = bands still needed. ? = complete (Lv 21–30 file exists for desert large as example).

| Region | Overworld | Large City | Mid City | Small City |
|---|---|---|---|---|
| Desert | 31–100 | 31–100 | 21–100 | 21–100 |
| Forest | 21–100 | 21–100 | 21–100 | 21–100 |
| Grassland | 21–100 | 21–100 | 21–100 | 21–100 |
| Mountains | 21–100 | 21–100 | 21–100 | 21–100 |
| Shallows | 21–100 | 21–100 | 21–100 | 21–100 |
| Snow | 21–100 | 21–100 | 21–100 | 21–100 |
| Swamp | 21–100 | 21–100 | 21–100 | 21–100 |

Total bands needed: **7 regions × 4 zones × 8 bands = 224 files** (minus any already created like `desert/enemies_large/lv21to30.py`).

### Recommended Creation Order

Work one region at a time, all four zones together, before moving to the next region. This keeps the thematic identity consistent.

1. Desert (urban, heat, neon, sand, corruption)
2. Swamp (rot, decay, voodoo, murk, undead)
3. Forest (nature, predators, fae, wood, ambush)
4. Mountains (iron, forge, stone, constructs, avalanche)
5. Shallows (tide, salt, corsair, aquatic, storm)
6. Snow (frost, ice, endurance, isolation, blizzard)
7. Grassland (plains, wind, nomad, cavalry, open sky)

---

## Thematic Guidance Per Region

### Desert
- Early (21–40): street gangs, sand predators, arcane merchants, heat elementals
- Mid (41–70): cult enforcers, desert wraiths, mirage entities, scorpion constructs
- Late (71–100): void-touched sandstorm beings, ancient tomb guardians, dune titans

### Swamp
- Early (21–40): bog crawlers, rotted husks, murk poachers, swamp witches
- Mid (41–70): bone warlocks, plague carriers, mire constructs, soul weavers
- Late (71–100): lich lords, corruption elementals, swamp dreadnoughts

### Forest
- Early (21–40): feral beasts, poacher gangs, corrupted dryads, root golems
- Mid (41–70): moonhunters, blight wolves, arcane wardens, shade raptors
- Late (71–100): ancient forest spirits, void-touched predators, colossal tree wraiths

### Mountains
- Early (21–40): mining raiders, stone elementals, iron-clad mercenaries, golem scouts
- Mid (41–70): forge cultists, avalanche beasts, adamant constructs, rune wardens
- Late (71–100): mountain titans, geode horrors, forge-daemon amalgams

### Shallows
- Early (21–40): corsair crews, tide elementals, abyssal hounds, jellyfish horrors
- Mid (41–70): deep sea predators, ghost ships, brine constructs, sirens
- Late (71–100): kraken spawn, tidal dreadnoughts, void-sea entities

### Snow
- Early (21–40): frost raiders, ice elementals, blizzard wraiths, frozen constructs
- Mid (41–70): permafrost golems, glacial hunters, rune-ice shamans
- Late (71–100): avalanche titans, ancient frost demons, polar void horrors

### Grassland
- Early (21–40): bandit cavalry, wind elementals, rogue nomads, grass serpents
- Mid (41–70): storm riders, dust wraiths, arcane nomad mages, steppe predators
- Late (71–100): wind titans, void-touched storm entities, ancient grassland guardians

---

## Example: Complete Band File

`regions/cities/desert/enemies_large/lv31to40.py`

```python
# Level 31–40 hostile seeds for the Great Dune City (large desert metropolis).

RANDOM_HOSTILE_SEEDS = [
    # min_spawn_level == 31
    {"id": "sand_cult_invoker", "name": "Sand Cult Invoker", "hostile_type": "humanoid", "role": "hazard",
     "min_spawn_level": 31, "rarity": "uncommon", "base_xp": 320,
     "common_drop": "stimulant_large", "rare_drop": "tome_int", "money_range": (80, 300),
     "basic_attack": "curses with a sand-etched glyph", "strong_attack": "void sand eruption",
     "player_abilities": ["lv2_hostile_ability_earth_light_tech_primal_disunion", "lv2_hostile_ability_dark_electric_magic_abyssal_storm"],
     "base_str": 8, "base_dex": 6, "base_con": 9, "base_int": 16, "base_hp": 140, "base_ap": 10,
     "str_per_level": 1, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 4},

    {"id": "dune_iron_enforcer", "name": "Dune Iron Enforcer", "hostile_type": "humanoid", "role": "damage",
     "min_spawn_level": 32, "rarity": "common", "base_xp": 260,
     "common_drop": "herb_major", "rare_drop": "stimulant_large", "money_range": (70, 260),
     "basic_attack": "heavy armored punch", "strong_attack": "iron dune slam",
     "player_abilities": ["earth_earth_technique_lv2_brutal_swing"],
     "base_str": 16, "base_dex": 5, "base_con": 14, "base_int": 3, "base_hp": 200, "base_ap": 7,
     "str_per_level": 4, "dex_per_level": 1, "con_per_level": 3, "int_per_level": 0},

    {"id": "glass_asp", "name": "Glass Asp", "hostile_type": "creature", "role": "damage",
     "min_spawn_level": 34, "rarity": "rare", "base_xp": 480,
     "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": (100, 380),
     "basic_attack": "crystalline fang strike", "strong_attack": "venom surge",
     "player_abilities": ["lv2_hostile_ability_dark_ice_skill_void_spike", "level_1_hostile_ability_poison_dart"],
     "base_str": 12, "base_dex": 14, "base_con": 10, "base_int": 4, "base_hp": 180, "base_ap": 9,
     "str_per_level": 3, "dex_per_level": 4, "con_per_level": 2, "int_per_level": 0},

    {"id": "chrome_shaman", "name": "Chrome Shaman", "hostile_type": "humanoid", "role": "support",
     "min_spawn_level": 36, "rarity": "uncommon", "base_xp": 350,
     "common_drop": "tome_int", "rare_drop": "tome_con", "money_range": (90, 340),
     "basic_attack": "chrome staff jab", "strong_attack": "resonance pulse",
     "player_abilities": ["lv2_hostile_ability_dark_light_spirit_calm_bleat", "level_1_hostile_ability_reinforce_frame"],
     "base_str": 6, "base_dex": 8, "base_con": 12, "base_int": 14, "base_hp": 160, "base_ap": 12,
     "str_per_level": 1, "dex_per_level": 2, "con_per_level": 3, "int_per_level": 3},

    {"id": "sandstorm_elemental", "name": "Sandstorm Elemental", "hostile_type": "elemental", "role": "hazard",
     "min_spawn_level": 38, "rarity": "rare", "base_xp": 560,
     "common_drop": "stimulant_large", "rare_drop": "stimulant_large", "money_range": (120, 420),
     "basic_attack": "abrasive sand blast", "strong_attack": "blinding vortex",
     "player_abilities": ["lv2_hostile_ability_air_water_spirit_gale_of_silence", "lv2_hostile_ability_dark_air_skill_nightmare_wave"],
     "base_str": 10, "base_dex": 12, "base_con": 8, "base_int": 12, "base_hp": 220, "base_ap": 11,
     "str_per_level": 2, "dex_per_level": 3, "con_per_level": 2, "int_per_level": 3},
]
```

---

## Notes for AI Agents

- **Do not invent ability IDs.** Only use IDs listed in this document or found in the ability files. If a thematic ability doesn't exist, use `None` or the closest matching existing ID.
- **Do not skip the parent constants import.** A band file that isn't imported will never be loaded by the game — the validator will still report a gap.
- **Match biome theme.** A swamp hostile at Lv 75 should feel like a swamp elite, not a generic fighter.
- **Vary roles within each band.** Don't write 5 `damage` hostiles — mix in at least one `hazard` or `support`.
- **Keep rarity distribution natural.** Aim for ~50% `common`, ~30% `uncommon`, ~15% `rare`, ~5% `superrare` per band.
- **Stat sanity check:** `base_hp` should roughly equal `(base_con × 8) + 20` at minimum. High-INT hazard hostiles should have lower STR. High-STR damage hostiles should have lower INT.
