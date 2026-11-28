# Fracture: Ability Pool Fill Implementation Spec

Every class gets **at least 4 learnable abilities per element at ability Level 1** and **at least 8 per element at Levels 2–5**. This spec lists every ability needed to get there, in full and ready to paste.

## Summary

- **Adds 204 player abilities** (the learnable pool grows from 503 to 707): 114 at Level 1, 4 at Level 2, 20 at Level 3, 31 at Level 4, 35 at Level 5.
- **Data only.** No code changes. The learn screen, `can_learn`, AI leveling and the recruit generator all read the pool, so new entries are picked up automatically.
- **Result:** every class, level and element meets the target. The lowest number of learnable abilities for any character goes from **2 / 14 / 8 / 6 / 4** to **8 / 15 / 13 / 12 / 9** (Levels 1–5).
- **Validator:** the new abilities raise no errors or warnings in the dev-tool ability validator. No existing ability gains a flag (one loses an old warning). Details in §7.

## 1. The rule

- **Target**, for each class and each of the 8 elements (fire, water, earth, air, ice, electric, light, dark): at least **4** abilities at Level 1 and at least **8** at each of Levels 2, 3, 4 and 5. `physical` is not a player element.
- **Counting:** an ability counts once toward **every distinct element** in its `elements` list. This is the learn rule: a character can learn an ability if at least one of its elements matches theirs. A repeated element (`ice, ice`) counts once.
- Only player-learnable abilities count. Signature abilities and anything flagged `non_player_ability` are excluded.
- Each new ability has exactly as many element slots as its level. The first element is the lead element; a repeated element means stronger affinity (existing convention).

## 2. Coverage before and after

Each cell is **before → after**: the number of learnable abilities of that class and level that include that element. Cells that were short are in bold.

### Technique

| Level | Fire | Water | Earth | Air | Ice | Electric | Light | Dark |
|---|---|---|---|---|---|---|---|---|
| 1 (target 4) | **1 → 4** | **1 → 4** | **2 → 4** | **1 → 4** | **1 → 4** | **1 → 4** | **1 → 4** | **1 → 4** |
| 2 (target 8) | 8 | 8 | 9 | 9 | **7 → 8** | **7 → 8** | 8 | 8 |
| 3 (target 8) | 9 → 10 | 9 → 10 | 8 → 9 | 9 → 10 | **7 → 8** | 8 → 9 | **3 → 8** | 8 |
| 4 (target 8) | **7 → 8** | **7 → 8** | 11 → 12 | 8 | **4 → 8** | **5 → 8** | **6 → 8** | **6 → 8** |
| 5 (target 8) | **4 → 8** | **2 → 8** | **6 → 8** | **3 → 8** | **3 → 8** | **2 → 8** | **4 → 8** | **2 → 8** |

### Spirit

| Level | Fire | Water | Earth | Air | Ice | Electric | Light | Dark |
|---|---|---|---|---|---|---|---|---|
| 1 (target 4) | **1 → 4** | **2 → 4** | **1 → 4** | **1 → 4** | **1 → 4** | **1 → 4** | **3 → 4** | **1 → 4** |
| 2 (target 8) | 8 | 8 | 8 | 8 | **7 → 8** | 8 | 8 | **7 → 8** |
| 3 (target 8) | 12 | 11 | 13 | 13 | 9 | 10 | 14 | 12 |
| 4 (target 8) | **7 → 8** | 11 → 14 | **6 → 8** | **6 → 8** | **0 → 8** | **2 → 8** | 16 → 21 | **6 → 9** |
| 5 (target 8) | **5 → 8** | 9 → 11 | **6 → 8** | 9 | **1 → 8** | **1 → 8** | 11 → 15 | **1 → 8** |

### Magic

| Level | Fire | Water | Earth | Air | Ice | Electric | Light | Dark |
|---|---|---|---|---|---|---|---|---|
| 1 (target 4) | **2 → 4** | **1 → 4** | **1 → 4** | **1 → 4** | **1 → 4** | **1 → 4** | **0 → 4** | **1 → 4** |
| 2 (target 8) | 8 | 8 | 8 | 9 | 8 → 9 | 8 | **7 → 8** | 9 |
| 3 (target 8) | **7 → 8** | **7 → 8** | **7 → 8** | **7 → 8** | **7 → 8** | **7 → 8** | **1 → 8** | **7 → 8** |
| 4 (target 8) | **7 → 8** | **5 → 8** | 8 | 8 → 10 | **6 → 8** | **6 → 8** | **4 → 8** | 13 → 14 |
| 5 (target 8) | 10 → 12 | 12 → 16 | 12 → 14 | 13 → 18 | **1 → 8** | **0 → 8** | **5 → 8** | 9 → 12 |

### Tech

| Level | Fire | Water | Earth | Air | Ice | Electric | Light | Dark |
|---|---|---|---|---|---|---|---|---|
| 1 (target 4) | **1 → 4** | **1 → 4** | **1 → 4** | **1 → 4** | **1 → 4** | **1 → 4** | **1 → 4** | **1 → 4** |
| 2 (target 8) | 8 | 8 | 8 | 9 | **7 → 8** | **7 → 8** | 8 | 9 |
| 3 (target 8) | 9 | 9 | 9 | 9 | 9 | 9 → 10 | **7 → 8** | **7 → 8** |
| 4 (target 8) | **5 → 9** | **3 → 8** | **4 → 8** | **5 → 8** | **3 → 8** | **4 → 8** | 10 | **6 → 8** |
| 5 (target 8) | **7 → 8** | **7 → 10** | **7 → 8** | 10 → 14 | **3 → 8** | **4 → 8** | 11 → 14 | **7 → 8** |

### Skill

| Level | Fire | Water | Earth | Air | Ice | Electric | Light | Dark |
|---|---|---|---|---|---|---|---|---|
| 1 (target 4) | **1 → 4** | **1 → 4** | **1 → 4** | **2 → 4** | **1 → 4** | **1 → 4** | **1 → 4** | **2 → 4** |
| 2 (target 8) | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| 3 (target 8) | **7 → 8** | **7 → 8** | **7 → 8** | **7 → 8** | **7 → 8** | **7 → 8** | **1 → 8** | **7 → 8** |
| 4 (target 8) | 20 → 22 | 21 → 23 | 26 → 29 | 28 → 31 | **0 → 8** | **0 → 8** | 26 → 29 | 19 → 21 |
| 5 (target 8) | **4 → 8** | **4 → 8** | **5 → 9** | **6 → 8** | **2 → 8** | **2 → 8** | **4 → 8** | **4 → 8** |

## 3. What gets added

| Class | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 | Total |
|---|---|---|---|---|---|---|
| Technique | 23 | 1 | 5 | 4 | 8 | 41 |
| Spirit | 21 | 1 | – | 8 | 7 | 37 |
| Magic | 24 | 1 | 7 | 4 | 8 | 44 |
| Tech | 24 | 1 | 1 | 7 | 5 | 38 |
| Skill | 22 | – | 7 | 8 | 7 | 44 |
| **Total** | 114 | 4 | 20 | 31 | 35 | **204** |

By effect: 101 damage, 87 status (buffs and debuffs), 8 heal, 7 cure, 1 revive. 83 of the 204 hit every target (`can_aoe: True`).

## 4. Design notes

**Level 1 (114).** Each element of each class gets its missing abilities in the class's own voice. The usual set per element is one single-target attack, one attack that hits every foe, and one stance, buff, debuff or cure:
- **Technique:** weapon and body work, such as strikes, sweeps, stances, shield bashes and war cries.
- **Spirit:** small heals, cures (one per ailment: sleep, stun, confuse, silence, curses), blessings, smites and curses. Spirit had no Level 1 damage; it now has five small smites.
- **Magic:** single-target bolts, hexes and a few area spells. Magic's Level 1 attacks were almost all area spells; it now has single-target bolts too.
- **Tech:** pistols, mines, turrets, jammers, plating and med-mist.
- **Skill:** kicks, darts, thrown stars, footwork, poisons and dirty tricks.

**Levels 2–5 (90).** The shortfalls up here are concentrated: ice and electric almost everywhere, dark for Spirit, light for Magic and Skill at Level 3. To keep the mixes from reading as random, they are grouped into themes:
- **Thundersnow** (ice + electric): Thundersnow Maul, Thundersnow Cleaver, Thundersnow Psalm, Thundersnow Wheel, Sleetstep Flurry, Hailspark Fan.
- **Aurora and the polar night** (ice + electric + dark or light): Aurora Rally, Aurora Benediction, Polar Night Vigil, Aurora of the Long Night, Polar Night Litany, Polar Eclipse, Aurora Dance.
- **Light through ice** (light + ice): Diamond Dust, Sundog Lance, Diamond Edge, Dawnfrost Lunge.
- **Eclipse** (light + dark): Eclipse Hex, Eclipse Emitter, Twilight Feint.

Four Level 5 names nod to the old gods: **Ares' War Banner** (Technique), **Hades' Long Night** (Spirit), **Wrath of Boreas** (Magic) and **Hermes' Stride** (Skill).

**Targeting.** Level 4 debuffs hit every foe, matching the existing Level 4 pattern. At Level 5 there is one single-target finisher, **Executioner's Mark**; the other Level 5 debuffs hit every foe.

**Numbers.**
- **Damage and heals** use the existing median power and AP for that class, level and target type, so a new ability is never a strict upgrade on an old one of the same class.
- **Status and cure** AP is set from the repo's own ability value calculator, at the centre of the existing group for that level. AP therefore rises with how much the ability does.
- **`base_power`** is 1 / 2 / 3 / 5 / 5 (Levels 1–5) on harmful status abilities and 0 on buffs and cures, as in the existing data.
- All `status_keys` are real `STATUS_EFFECTS` entries, and cures name the ailment they remove (or use the `debuff` meta key).

## 5. Implementation

1. Add each block in §6 to the **end** of the named list, inside the closing `]`, under this header comment:
   `# --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---`
2. Copy the entries exactly. Every `id` is unique, follows the element-prefix convention, and clashes with no existing ability id or name (player, signature or enemy-shared).
3. Do not change any existing ability.
4. No other files change.

| Level | File | List | New entries |
|---|---|---|---|
| 1 | `old/game/region_seeds/player_abilities/level_1_abilities.py` | `LEVEL_1_PLAYER_ABILITY_SEEDS` | 114 |
| 2 | `old/game/region_seeds/player_abilities/level_2_abilities_by_type/technique.py` | `LEVEL_2_TECHNIQUE_ABILITY_SEEDS` | 1 |
| 2 | `old/game/region_seeds/player_abilities/level_2_abilities_by_type/spirit.py` | `LEVEL_2_SPIRIT_ABILITY_SEEDS` | 1 |
| 2 | `old/game/region_seeds/player_abilities/level_2_abilities_by_type/magic.py` | `LEVEL_2_MAGIC_ABILITY_SEEDS` | 1 |
| 2 | `old/game/region_seeds/player_abilities/level_2_abilities_by_type/tech.py` | `LEVEL_2_TECH_ABILITY_SEEDS` | 1 |
| 3 | `old/game/region_seeds/player_abilities/level_3_abilities_by_type/technique.py` | `LEVEL_3_TECHNIQUE_SEEDS` | 5 |
| 3 | `old/game/region_seeds/player_abilities/level_3_abilities_by_type/magic.py` | `LEVEL_3_MAGIC_SEEDS` | 7 |
| 3 | `old/game/region_seeds/player_abilities/level_3_abilities_by_type/tech.py` | `LEVEL_3_TECH_SEEDS` | 1 |
| 3 | `old/game/region_seeds/player_abilities/level_3_abilities_by_type/skill.py` | `LEVEL_3_SKILL_SEEDS` | 7 |
| 4 | `old/game/region_seeds/player_abilities/level_4_abilities_by_type/technique.py` | `LEVEL_4_TECHNIQUE_ABILITY_SEEDS` | 4 |
| 4 | `old/game/region_seeds/player_abilities/level_4_abilities_by_type/spirit.py` | `LEVEL_4_SPIRIT_ABILITY_SEEDS` | 8 |
| 4 | `old/game/region_seeds/player_abilities/level_4_abilities_by_type/magic.py` | `LEVEL_4_MAGIC_ABILITY_SEEDS` | 4 |
| 4 | `old/game/region_seeds/player_abilities/level_4_abilities_by_type/tech.py` | `LEVEL_4_TECH_ABILITY_SEEDS` | 7 |
| 4 | `old/game/region_seeds/player_abilities/level_4_abilities_by_type/skill.py` | `LEVEL_4_SKILL_ABILITY_SEEDS` | 8 |
| 5 | `old/game/region_seeds/player_abilities/level_5_abilities_by_type/technique.py` | `LEVEL_5_TECHNIQUE_ABILITY_SEEDS` | 8 |
| 5 | `old/game/region_seeds/player_abilities/level_5_abilities_by_type/spirit.py` | `LEVEL_5_SPIRIT_ABILITY_SEEDS` | 7 |
| 5 | `old/game/region_seeds/player_abilities/level_5_abilities_by_type/magic.py` | `LEVEL_5_MAGIC_ABILITY_SEEDS` | 8 |
| 5 | `old/game/region_seeds/player_abilities/level_5_abilities_by_type/tech.py` | `LEVEL_5_TECH_ABILITY_SEEDS` | 5 |
| 5 | `old/game/region_seeds/player_abilities/level_5_abilities_by_type/skill.py` | `LEVEL_5_SKILL_ABILITY_SEEDS` | 7 |

## 6. The abilities

### 6.1 Level 1: `old/game/region_seeds/player_abilities/level_1_abilities.py` → `LEVEL_1_PLAYER_ABILITY_SEEDS` (114)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    # Technique: fire
    {"id": "fire_technique_lv1_ember_haymaker", "name": "Ember Haymaker", "description": "A wild, swinging punch wreathed in sparks.", "ability_type": "technique", "level": 1, "elements": ["fire"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "fire_technique_lv1_brushfire_sweep", "name": "Brushfire Sweep", "description": "A low, burning arc of the blade that catches every foe in reach.", "ability_type": "technique", "level": 1, "elements": ["fire"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "fire_technique_lv1_kindled_grip", "name": "Kindled Grip", "description": "Heat floods the arms so every swing lands heavier.", "ability_type": "technique", "level": 1, "elements": ["fire"], "base_power": 0, "ap_cost": 6, "effect": "status", "status_keys": ["strength_buff"], "can_aoe": False},
    # Technique: water
    {"id": "water_technique_lv1_undertow_throw", "name": "Undertow Throw", "description": "Grab, twist and drag the foe under like a riptide.", "ability_type": "technique", "level": 1, "elements": ["water"], "base_power": 13, "ap_cost": 8, "effect": "damage", "can_aoe": False},
    {"id": "water_technique_lv1_breaker_sweep", "name": "Breaker Sweep", "description": "A wide swing that crashes through the enemy line like surf.", "ability_type": "technique", "level": 1, "elements": ["water"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "water_technique_lv1_tidewall_stance", "name": "Tidewall Stance", "description": "Settle low and let elemental blows roll off like water off stone.", "ability_type": "technique", "level": 1, "elements": ["water"], "base_power": 0, "ap_cost": 9, "effect": "status", "status_keys": ["elemental_defense_buff", "defense_buff"], "can_aoe": False},
    # Technique: earth
    {"id": "earth_technique_lv1_quake_stomp", "name": "Quake Stomp", "description": "A heel-drop that cracks the ground under every nearby foe.", "ability_type": "technique", "level": 1, "elements": ["earth"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "earth_technique_lv1_guard_breaker", "name": "Guard Breaker", "description": "A shoulder-driven blow that splits the foe's guard and footing.", "ability_type": "technique", "level": 1, "elements": ["earth"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["defense_debuff", "strength_debuff"], "can_aoe": False},
    # Technique: air
    {"id": "air_technique_lv1_windshear_cut", "name": "Windshear Cut", "description": "A rising slash that rides the updraft it creates.", "ability_type": "technique", "level": 1, "elements": ["air"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "air_technique_lv1_cyclone_spin", "name": "Cyclone Spin", "description": "A full-body spin, blade out, that buffets everyone close.", "ability_type": "technique", "level": 1, "elements": ["air"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "air_technique_lv1_tailwind_footwork", "name": "Tailwind Footwork", "description": "Light, wind-carried steps that speed every follow-up.", "ability_type": "technique", "level": 1, "elements": ["air"], "base_power": 0, "ap_cost": 7, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": False},
    # Technique: ice
    {"id": "ice_technique_lv1_rime_hammer", "name": "Rime Hammer", "description": "A frost-crusted hammer blow that rings like cracking ice.", "ability_type": "technique", "level": 1, "elements": ["ice"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "ice_technique_lv1_shatterline", "name": "Shatterline", "description": "A ground strike that sends a line of ice spikes through the enemy ranks.", "ability_type": "technique", "level": 1, "elements": ["ice"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "ice_technique_lv1_numbing_chop", "name": "Numbing Chop", "description": "A cold chop to the wrist that leaves the foe slow and clumsy.", "ability_type": "technique", "level": 1, "elements": ["ice"], "base_power": 1, "ap_cost": 8, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": False},
    # Technique: electric
    {"id": "electric_technique_lv1_spark_knuckle", "name": "Spark Knuckle", "description": "A charged punch that crackles on impact.", "ability_type": "technique", "level": 1, "elements": ["electric"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "electric_technique_lv1_arc_cleave", "name": "Arc Cleave", "description": "A wide cleave that throws arcs between every foe it touches.", "ability_type": "technique", "level": 1, "elements": ["electric"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "electric_technique_lv1_live_wire", "name": "Live Wire", "description": "Static hums through the muscles and quickens every swing.", "ability_type": "technique", "level": 1, "elements": ["electric"], "base_power": 0, "ap_cost": 10, "effect": "status", "status_keys": ["attack_buff", "strength_buff"], "can_aoe": False},
    # Technique: light
    {"id": "light_technique_lv1_dawn_thrust", "name": "Dawn Thrust", "description": "A straight thrust that flares like first light.", "ability_type": "technique", "level": 1, "elements": ["light"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "light_technique_lv1_halo_sweep", "name": "Halo Sweep", "description": "A circling cut that leaves a ring of light around you.", "ability_type": "technique", "level": 1, "elements": ["light"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "light_technique_lv1_blinding_bash", "name": "Blinding Bash", "description": "A shield bash with a flash of light that leaves the foe swinging blind.", "ability_type": "technique", "level": 1, "elements": ["light"], "base_power": 1, "ap_cost": 11, "effect": "status", "status_keys": ["attack_debuff", "dexterity_debuff"], "can_aoe": False},
    # Technique: dark
    {"id": "dark_technique_lv1_shade_rend", "name": "Shade Rend", "description": "A tearing slash that seems to come from the foe's own shadow.", "ability_type": "technique", "level": 1, "elements": ["dark"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "dark_technique_lv1_umbral_reap", "name": "Umbral Reap", "description": "A scything swing that reaps through the dark.", "ability_type": "technique", "level": 1, "elements": ["dark"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "dark_technique_lv1_menacing_roar", "name": "Menacing Roar", "description": "A roar from the dark that saps the nerve of every foe.", "ability_type": "technique", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 12, "effect": "status", "status_keys": ["attack_debuff", "strength_debuff"], "can_aoe": True},
    # Spirit: fire
    {"id": "fire_spirit_lv1_hearth_mend", "name": "Hearth Mend", "description": "Warmth from a remembered hearth that closes small wounds.", "ability_type": "spirit", "level": 1, "elements": ["fire"], "base_power": 10, "ap_cost": 10, "effect": "heal", "can_aoe": False},
    {"id": "fire_spirit_lv1_wakefire", "name": "Wakefire", "description": "A spark of warmth that shakes an ally out of unnatural sleep.", "ability_type": "spirit", "level": 1, "elements": ["fire"], "base_power": 0, "ap_cost": 10, "effect": "cure", "status_keys": ["sleep"], "can_aoe": False},
    {"id": "fire_spirit_lv1_censure_flame", "name": "Censure Flame", "description": "A judging flame that singes the wicked.", "ability_type": "spirit", "level": 1, "elements": ["fire"], "base_power": 11, "ap_cost": 7, "effect": "damage", "can_aoe": False},
    # Spirit: water
    {"id": "water_spirit_lv1_wellspring_mist", "name": "Wellspring Mist", "description": "A cool mist that eases the whole party's wounds.", "ability_type": "spirit", "level": 1, "elements": ["water"], "base_power": 8, "ap_cost": 11, "effect": "heal", "can_aoe": True},
    {"id": "water_spirit_lv1_baptismal_rinse", "name": "Baptismal Rinse", "description": "A rinse of holy water that washes curses and weakness from an ally.", "ability_type": "spirit", "level": 1, "elements": ["water"], "base_power": 0, "ap_cost": 7, "effect": "cure", "status_keys": ["debuff"], "can_aoe": False},
    # Spirit: earth
    {"id": "earth_spirit_lv1_rooted_vigil", "name": "Rooted Vigil", "description": "A slow chant that roots the party's feet and steadies their breath.", "ability_type": "spirit", "level": 1, "elements": ["earth"], "base_power": 0, "ap_cost": 7, "effect": "status", "status_keys": ["constitution_buff"], "can_aoe": True},
    {"id": "earth_spirit_lv1_clay_poultice", "name": "Clay Poultice", "description": "A poultice of blessed clay pressed into an ally's wounds.", "ability_type": "spirit", "level": 1, "elements": ["earth"], "base_power": 10, "ap_cost": 10, "effect": "heal", "can_aoe": False},
    {"id": "earth_spirit_lv1_grounding_touch", "name": "Grounding Touch", "description": "A hand on the shoulder that grounds a stunned ally back into the fight.", "ability_type": "spirit", "level": 1, "elements": ["earth"], "base_power": 0, "ap_cost": 13, "effect": "cure", "status_keys": ["stun"], "can_aoe": False},
    # Spirit: air
    {"id": "air_spirit_lv1_second_wind", "name": "Second Wind", "description": "A deep, guided breath that restores a little vigor.", "ability_type": "spirit", "level": 1, "elements": ["air"], "base_power": 10, "ap_cost": 10, "effect": "heal", "can_aoe": False},
    {"id": "air_spirit_lv1_clearing_breeze", "name": "Clearing Breeze", "description": "A fresh breeze that blows the fog out of a confused mind.", "ability_type": "spirit", "level": 1, "elements": ["air"], "base_power": 0, "ap_cost": 15, "effect": "cure", "status_keys": ["confuse"], "can_aoe": False},
    {"id": "air_spirit_lv1_gust_rebuke", "name": "Gust Rebuke", "description": "A sharp rebuke carried on a gust of spirit-wind.", "ability_type": "spirit", "level": 1, "elements": ["air"], "base_power": 11, "ap_cost": 7, "effect": "damage", "can_aoe": False},
    # Spirit: ice
    {"id": "ice_spirit_lv1_snowfall_hush", "name": "Snowfall Hush", "description": "A hush like falling snow that lulls a foe to sleep.", "ability_type": "spirit", "level": 1, "elements": ["ice"], "base_power": 1, "ap_cost": 11, "effect": "status", "status_keys": ["sleep"], "can_aoe": False},
    {"id": "ice_spirit_lv1_frost_ward", "name": "Frost Ward", "description": "A thin rime of blessed frost over each ally that turns aside elemental harm.", "ability_type": "spirit", "level": 1, "elements": ["ice"], "base_power": 0, "ap_cost": 8, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
    {"id": "ice_spirit_lv1_rime_smite", "name": "Rime Smite", "description": "A cold rebuke that bites at the soul.", "ability_type": "spirit", "level": 1, "elements": ["ice"], "base_power": 11, "ap_cost": 7, "effect": "damage", "can_aoe": False},
    # Spirit: electric
    {"id": "electric_spirit_lv1_quickening_spark", "name": "Quickening Spark", "description": "A spark of spirit that jolts an ally into quicker action.", "ability_type": "spirit", "level": 1, "elements": ["electric"], "base_power": 0, "ap_cost": 7, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": False},
    {"id": "electric_spirit_lv1_static_smite", "name": "Static Smite", "description": "A crack of judgment that leaps from palm to foe.", "ability_type": "spirit", "level": 1, "elements": ["electric"], "base_power": 11, "ap_cost": 7, "effect": "damage", "can_aoe": False},
    {"id": "electric_spirit_lv1_voice_spark", "name": "Voice Spark", "description": "A small charge to the throat that restores a silenced ally's voice.", "ability_type": "spirit", "level": 1, "elements": ["electric"], "base_power": 0, "ap_cost": 12, "effect": "cure", "status_keys": ["silence"], "can_aoe": False},
    # Spirit: light
    {"id": "light_spirit_lv1_sanctuary_glow", "name": "Sanctuary Glow", "description": "A soft glow that slowly restores the whole party.", "ability_type": "spirit", "level": 1, "elements": ["light"], "base_power": 0, "ap_cost": 10, "effect": "status", "status_keys": ["regen"], "can_aoe": True},
    # Spirit: dark
    {"id": "dark_spirit_lv1_mourners_hex", "name": "Mourner's Hex", "description": "A mourning curse that makes the foe's blows feel heavy and pointless.", "ability_type": "spirit", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["attack_debuff", "strength_debuff"], "can_aoe": False},
    {"id": "dark_spirit_lv1_shadow_mend", "name": "Shadow Mend", "description": "Borrowed shadow quietly knits an ally's wounds closed.", "ability_type": "spirit", "level": 1, "elements": ["dark"], "base_power": 10, "ap_cost": 10, "effect": "heal", "can_aoe": False},
    {"id": "dark_spirit_lv1_grave_smite", "name": "Grave Smite", "description": "A cold touch from beyond that drains the warmth from a foe.", "ability_type": "spirit", "level": 1, "elements": ["dark"], "base_power": 11, "ap_cost": 7, "effect": "damage", "can_aoe": False},
    # Magic: fire
    {"id": "fire_magic_lv1_ember_hex", "name": "Ember Hex", "description": "A smoldering curse that keeps burning long after the spell ends.", "ability_type": "magic", "level": 1, "elements": ["fire"], "base_power": 1, "ap_cost": 10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
    {"id": "fire_magic_lv1_searing_ray", "name": "Searing Ray", "description": "A thin ray of flame that bores into one target.", "ability_type": "magic", "level": 1, "elements": ["fire"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    # Magic: water
    {"id": "water_magic_lv1_riptide_bolt", "name": "Riptide Bolt", "description": "A spiraling bolt of pressurized water.", "ability_type": "magic", "level": 1, "elements": ["water"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "water_magic_lv1_drowsy_mist", "name": "Drowsy Mist", "description": "A damp, heavy mist that drags the target into sleep.", "ability_type": "magic", "level": 1, "elements": ["water"], "base_power": 1, "ap_cost": 10, "effect": "status", "status_keys": ["sleep"], "can_aoe": False},
    {"id": "water_magic_lv1_brine_hex", "name": "Brine Hex", "description": "A salt-sting curse that leaves the target soaked and exposed.", "ability_type": "magic", "level": 1, "elements": ["water"], "base_power": 1, "ap_cost": 7, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
    # Magic: earth
    {"id": "earth_magic_lv1_stone_bullet", "name": "Stone Bullet", "description": "A shard of stone flung at bone-breaking speed.", "ability_type": "magic", "level": 1, "elements": ["earth"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "earth_magic_lv1_quicksand_hex", "name": "Quicksand Hex", "description": "The ground softens under the target, slowing every step and loosening its guard.", "ability_type": "magic", "level": 1, "elements": ["earth"], "base_power": 1, "ap_cost": 11, "effect": "status", "status_keys": ["dexterity_debuff", "defense_debuff"], "can_aoe": False},
    {"id": "earth_magic_lv1_dust_veil", "name": "Dust Veil", "description": "A swirl of enchanted dust that dulls every foe's elemental guard.", "ability_type": "magic", "level": 1, "elements": ["earth"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
    # Magic: air
    {"id": "air_magic_lv1_wind_blade", "name": "Wind Blade", "description": "A crescent of compressed air that slices one target.", "ability_type": "magic", "level": 1, "elements": ["air"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "air_magic_lv1_vacuum_hush", "name": "Vacuum Hush", "description": "Pulls the air from the target's lungs and steals its voice.", "ability_type": "magic", "level": 1, "elements": ["air"], "base_power": 1, "ap_cost": 12, "effect": "status", "status_keys": ["silence"], "can_aoe": False},
    {"id": "air_magic_lv1_tailwind", "name": "Tailwind", "description": "A friendly wind at an ally's back that quickens every move.", "ability_type": "magic", "level": 1, "elements": ["air"], "base_power": 0, "ap_cost": 7, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": False},
    # Magic: ice
    {"id": "ice_magic_lv1_ice_needle", "name": "Ice Needle", "description": "A needle of ice that strikes faster than the eye can follow.", "ability_type": "magic", "level": 1, "elements": ["ice"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "ice_magic_lv1_chilling_hex", "name": "Chilling Hex", "description": "A creeping frost that stiffens the target's joints.", "ability_type": "magic", "level": 1, "elements": ["ice"], "base_power": 1, "ap_cost": 8, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": False},
    {"id": "ice_magic_lv1_sleet_spray", "name": "Sleet Spray", "description": "A spray of stinging sleet that pelts every foe.", "ability_type": "magic", "level": 1, "elements": ["ice"], "base_power": 9, "ap_cost": 10, "effect": "damage", "can_aoe": True},
    # Magic: electric
    {"id": "electric_magic_lv1_spark_bolt", "name": "Spark Bolt", "description": "A quick, needle-thin bolt of lightning.", "ability_type": "magic", "level": 1, "elements": ["electric"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "electric_magic_lv1_static_hex", "name": "Static Hex", "description": "A static charge that locks the target's muscles for a moment.", "ability_type": "magic", "level": 1, "elements": ["electric"], "base_power": 1, "ap_cost": 13, "effect": "status", "status_keys": ["stun"], "can_aoe": False},
    {"id": "electric_magic_lv1_ion_field", "name": "Ion Field", "description": "A crackling field that strips elemental guard from every foe.", "ability_type": "magic", "level": 1, "elements": ["electric"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
    # Magic: light
    {"id": "light_magic_lv1_lumen_dart", "name": "Lumen Dart", "description": "A dart of condensed light.", "ability_type": "magic", "level": 1, "elements": ["light"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "light_magic_lv1_solar_flare", "name": "Solar Flare", "description": "A flash of searing sunlight that scorches every foe.", "ability_type": "magic", "level": 1, "elements": ["light"], "base_power": 9, "ap_cost": 10, "effect": "damage", "can_aoe": True},
    {"id": "light_magic_lv1_dazzle", "name": "Dazzle", "description": "A burst of shifting colors that leaves the target confused.", "ability_type": "magic", "level": 1, "elements": ["light"], "base_power": 1, "ap_cost": 15, "effect": "status", "status_keys": ["confuse"], "can_aoe": False},
    {"id": "light_magic_lv1_clarity", "name": "Clarity", "description": "A clear, bright calm that sharpens an ally's focus.", "ability_type": "magic", "level": 1, "elements": ["light"], "base_power": 0, "ap_cost": 6, "effect": "status", "status_keys": ["intelligence_buff"], "can_aoe": False},
    # Magic: dark
    {"id": "dark_magic_lv1_shadow_bolt", "name": "Shadow Bolt", "description": "A bolt of solid shadow.", "ability_type": "magic", "level": 1, "elements": ["dark"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "dark_magic_lv1_dread_hex", "name": "Dread Hex", "description": "A whispered dread that clouds the target's mind and weakens its strikes.", "ability_type": "magic", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["intelligence_debuff", "attack_debuff"], "can_aoe": False},
    {"id": "dark_magic_lv1_gloom_rot", "name": "Gloom Rot", "description": "A creeping rot that eats at the target over time.", "ability_type": "magic", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
    # Tech: fire
    {"id": "fire_tech_lv1_flare_pistol", "name": "Flare Pistol", "description": "A signal pistol loaded with a burning magnesium round.", "ability_type": "tech", "level": 1, "elements": ["fire"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "fire_tech_lv1_incendiary_mine", "name": "Incendiary Mine", "description": "A pressure mine that bursts into a ring of fire.", "ability_type": "tech", "level": 1, "elements": ["fire"], "base_power": 12, "ap_cost": 13, "effect": "damage", "can_aoe": True},
    {"id": "fire_tech_lv1_thermal_plating", "name": "Thermal Plating", "description": "Heat-treated plates clamp onto an ally's armor.", "ability_type": "tech", "level": 1, "elements": ["fire"], "base_power": 0, "ap_cost": 9, "effect": "status", "status_keys": ["defense_buff", "elemental_defense_buff"], "can_aoe": False},
    # Tech: water
    {"id": "water_tech_lv1_hydro_jet", "name": "Hydro Jet", "description": "A pressure washer turned weapon.", "ability_type": "tech", "level": 1, "elements": ["water"], "base_power": 12, "ap_cost": 8, "effect": "damage", "can_aoe": False},
    {"id": "water_tech_lv1_coolant_mist", "name": "Coolant Mist", "description": "A coolant mist laced with med-gel that slowly closes the party's wounds.", "ability_type": "tech", "level": 1, "elements": ["water"], "base_power": 0, "ap_cost": 10, "effect": "status", "status_keys": ["regen"], "can_aoe": True},
    {"id": "water_tech_lv1_slick_spray", "name": "Slick Spray", "description": "A spray of slick polymer that leaves the target slipping.", "ability_type": "tech", "level": 1, "elements": ["water"], "base_power": 1, "ap_cost": 8, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": False},
    # Tech: earth
    {"id": "earth_tech_lv1_rivet_gun", "name": "Rivet Gun", "description": "A heavy-duty rivet gun fired at point-blank range.", "ability_type": "tech", "level": 1, "elements": ["earth"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "earth_tech_lv1_barricade_drop", "name": "Barricade Drop", "description": "Deployable barricades snap up in front of the party.", "ability_type": "tech", "level": 1, "elements": ["earth"], "base_power": 0, "ap_cost": 11, "effect": "status", "status_keys": ["defense_buff", "constitution_buff"], "can_aoe": True},
    {"id": "earth_tech_lv1_seismic_charge", "name": "Seismic Charge", "description": "A shaped charge that rattles the ground under the enemy line.", "ability_type": "tech", "level": 1, "elements": ["earth"], "base_power": 12, "ap_cost": 13, "effect": "damage", "can_aoe": True},
    # Tech: air
    {"id": "air_tech_lv1_pneumatic_bolt", "name": "Pneumatic Bolt", "description": "A compressed-air bolt that punches clean through light armor.", "ability_type": "tech", "level": 1, "elements": ["air"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "air_tech_lv1_gust_turret", "name": "Gust Turret", "description": "A small turbine turret that blasts the area with grit-laden wind.", "ability_type": "tech", "level": 1, "elements": ["air"], "base_power": 12, "ap_cost": 13, "effect": "damage", "can_aoe": True},
    {"id": "air_tech_lv1_jet_boots", "name": "Jet Boots", "description": "Strap-on thrusters that make an ally faster for a while.", "ability_type": "tech", "level": 1, "elements": ["air"], "base_power": 0, "ap_cost": 7, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": False},
    # Tech: ice
    {"id": "ice_tech_lv1_cryo_grenade", "name": "Cryo Grenade", "description": "A grenade that bursts into flash-frozen shrapnel.", "ability_type": "tech", "level": 1, "elements": ["ice"], "base_power": 12, "ap_cost": 14, "effect": "damage", "can_aoe": True},
    {"id": "ice_tech_lv1_cryo_clamp", "name": "Cryo Clamp", "description": "A clamp of liquid nitrogen that numbs the target's limbs.", "ability_type": "tech", "level": 1, "elements": ["ice"], "base_power": 1, "ap_cost": 13, "effect": "status", "status_keys": ["dexterity_debuff", "strength_debuff"], "can_aoe": False},
    {"id": "ice_tech_lv1_heat_sink", "name": "Heat Sink", "description": "A clip-on heat sink that soaks up elemental energy before it reaches an ally.", "ability_type": "tech", "level": 1, "elements": ["ice"], "base_power": 0, "ap_cost": 11, "effect": "status", "status_keys": ["elemental_defense_buff", "constitution_buff"], "can_aoe": False},
    # Tech: electric
    {"id": "electric_tech_lv1_shock_baton", "name": "Shock Baton", "description": "A baton that discharges on contact.", "ability_type": "tech", "level": 1, "elements": ["electric"], "base_power": 13, "ap_cost": 8, "effect": "damage", "can_aoe": False},
    {"id": "electric_tech_lv1_tesla_coil", "name": "Tesla Coil", "description": "A portable coil that arcs to everything nearby.", "ability_type": "tech", "level": 1, "elements": ["electric"], "base_power": 12, "ap_cost": 13, "effect": "damage", "can_aoe": True},
    {"id": "electric_tech_lv1_overcharge_cell", "name": "Overcharge Cell", "description": "A battery pack jacked into an ally's gear that boosts every system.", "ability_type": "tech", "level": 1, "elements": ["electric"], "base_power": 0, "ap_cost": 10, "effect": "status", "status_keys": ["attack_buff", "intelligence_buff"], "can_aoe": False},
    # Tech: light
    {"id": "light_tech_lv1_focus_laser", "name": "Focus Laser", "description": "A focused cutting laser.", "ability_type": "tech", "level": 1, "elements": ["light"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "light_tech_lv1_flashbang", "name": "Flashbang", "description": "A blinding, deafening charge that throws off the enemy line's aim and focus.", "ability_type": "tech", "level": 1, "elements": ["light"], "base_power": 1, "ap_cost": 12, "effect": "status", "status_keys": ["attack_debuff", "intelligence_debuff"], "can_aoe": True},
    {"id": "light_tech_lv1_targeting_laser", "name": "Targeting Laser", "description": "Paints the target with a laser so every hit finds a weak spot.", "ability_type": "tech", "level": 1, "elements": ["light"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["scanned", "defense_debuff"], "can_aoe": False},
    # Tech: dark
    {"id": "dark_tech_lv1_suppressed_shot", "name": "Suppressed Shot", "description": "A suppressed round fired from the shadows.", "ability_type": "tech", "level": 1, "elements": ["dark"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "dark_tech_lv1_blackout_canister", "name": "Blackout Canister", "description": "Thick black smoke that leaves the enemy line stumbling blind.", "ability_type": "tech", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 12, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True},
    {"id": "dark_tech_lv1_signal_jammer", "name": "Signal Jammer", "description": "Jams the target's comms and casting with white noise.", "ability_type": "tech", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 12, "effect": "status", "status_keys": ["silence"], "can_aoe": False},
    # Skill: fire
    {"id": "fire_skill_lv1_ember_kick", "name": "Ember Kick", "description": "A snapping kick that leaves a trail of sparks.", "ability_type": "skill", "level": 1, "elements": ["fire"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
    {"id": "fire_skill_lv1_firecracker_toss", "name": "Firecracker Toss", "description": "A handful of firecrackers tossed at the enemy's feet.", "ability_type": "skill", "level": 1, "elements": ["fire"], "base_power": 7, "ap_cost": 8, "effect": "damage", "can_aoe": True},
    {"id": "fire_skill_lv1_kindled_reflexes", "name": "Kindled Reflexes", "description": "A quick breathing trick that heats the blood and speeds the hands.", "ability_type": "skill", "level": 1, "elements": ["fire"], "base_power": 0, "ap_cost": 7, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": False},
    # Skill: water
    {"id": "water_skill_lv1_ripple_palm", "name": "Ripple Palm", "description": "A palm strike that sends a ripple through the target's body.", "ability_type": "skill", "level": 1, "elements": ["water"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
    {"id": "water_skill_lv1_rain_of_needles", "name": "Rain of Needles", "description": "A fan of thin needles thrown like a sudden rain.", "ability_type": "skill", "level": 1, "elements": ["water"], "base_power": 7, "ap_cost": 8, "effect": "damage", "can_aoe": True},
    {"id": "water_skill_lv1_fluid_guard", "name": "Fluid Guard", "description": "Loose, flowing footwork that makes you hard to pin down.", "ability_type": "skill", "level": 1, "elements": ["water"], "base_power": 0, "ap_cost": 10, "effect": "status", "status_keys": ["defense_buff", "dexterity_buff"], "can_aoe": False},
    # Skill: earth
    {"id": "earth_skill_lv1_sling_stone", "name": "Sling Stone", "description": "A sling stone, aimed true.", "ability_type": "skill", "level": 1, "elements": ["earth"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
    {"id": "earth_skill_lv1_caltrop_scatter", "name": "Caltrop Scatter", "description": "Iron caltrops scattered across the enemy's path.", "ability_type": "skill", "level": 1, "elements": ["earth"], "base_power": 7, "ap_cost": 8, "effect": "damage", "can_aoe": True},
    {"id": "earth_skill_lv1_dirt_in_the_eyes", "name": "Dirt in the Eyes", "description": "A fistful of grit flung at the face.", "ability_type": "skill", "level": 1, "elements": ["earth"], "base_power": 1, "ap_cost": 11, "effect": "status", "status_keys": ["attack_debuff", "dexterity_debuff"], "can_aoe": False},
    # Skill: air
    {"id": "air_skill_lv1_whirling_kick", "name": "Whirling Kick", "description": "A spinning kick that clips everyone in reach.", "ability_type": "skill", "level": 1, "elements": ["air"], "base_power": 7, "ap_cost": 8, "effect": "damage", "can_aoe": True},
    {"id": "air_skill_lv1_gust_feint", "name": "Gust Feint", "description": "A feint inside a sudden gust that leaves the foe turning the wrong way.", "ability_type": "skill", "level": 1, "elements": ["air"], "base_power": 1, "ap_cost": 15, "effect": "status", "status_keys": ["confuse"], "can_aoe": False},
    # Skill: ice
    {"id": "ice_skill_lv1_icicle_dart", "name": "Icicle Dart", "description": "A dart of ice that melts away after it hits.", "ability_type": "skill", "level": 1, "elements": ["ice"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
    {"id": "ice_skill_lv1_black_ice_trip", "name": "Black Ice Trip", "description": "A sweep across slick ice that sends the foe sprawling.", "ability_type": "skill", "level": 1, "elements": ["ice"], "base_power": 1, "ap_cost": 11, "effect": "status", "status_keys": ["dexterity_debuff", "defense_debuff"], "can_aoe": False},
    {"id": "ice_skill_lv1_cold_focus", "name": "Cold Focus", "description": "A cold, still breath before the next strike.", "ability_type": "skill", "level": 1, "elements": ["ice"], "base_power": 0, "ap_cost": 10, "effect": "status", "status_keys": ["attack_buff", "dexterity_buff"], "can_aoe": False},
    # Skill: electric
    {"id": "electric_skill_lv1_static_palm", "name": "Static Palm", "description": "A palm strike that discharges built-up static.", "ability_type": "skill", "level": 1, "elements": ["electric"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
    {"id": "electric_skill_lv1_spark_shuriken", "name": "Spark Shuriken", "description": "Charged throwing stars that arc between targets.", "ability_type": "skill", "level": 1, "elements": ["electric"], "base_power": 7, "ap_cost": 8, "effect": "damage", "can_aoe": True},
    {"id": "electric_skill_lv1_nerve_strike", "name": "Nerve Strike", "description": "A precise jab to a nerve cluster that locks the foe in place.", "ability_type": "skill", "level": 1, "elements": ["electric"], "base_power": 1, "ap_cost": 13, "effect": "status", "status_keys": ["stun"], "can_aoe": False},
    # Skill: light
    {"id": "light_skill_lv1_flashstep_strike", "name": "Flashstep Strike", "description": "Step through a flash of light and strike before the foe can turn.", "ability_type": "skill", "level": 1, "elements": ["light"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
    {"id": "light_skill_lv1_mirror_flash", "name": "Mirror Flash", "description": "A flash off a polished blade that dazzles the target.", "ability_type": "skill", "level": 1, "elements": ["light"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["attack_debuff", "intelligence_debuff"], "can_aoe": False},
    {"id": "light_skill_lv1_sunlit_flurry", "name": "Sunlit Flurry", "description": "A blur of strikes that catches the light, and every nearby foe.", "ability_type": "skill", "level": 1, "elements": ["light"], "base_power": 7, "ap_cost": 8, "effect": "damage", "can_aoe": True},
    # Skill: dark
    {"id": "dark_skill_lv1_shadow_step", "name": "Shadow Step", "description": "Melt into the shadows, then reappear exactly where you need to be.", "ability_type": "skill", "level": 1, "elements": ["dark"], "base_power": 0, "ap_cost": 6, "effect": "status", "status_keys": ["attack_buff", "defense_buff"], "can_aoe": False},
    {"id": "dark_skill_lv1_venom_needle", "name": "Venom Needle", "description": "A needle coated in slow poison.", "ability_type": "skill", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
```

### 6.2 Level 2 (4)

**Technique**: `old/game/region_seeds/player_abilities/level_2_abilities_by_type/technique.py` → `LEVEL_2_TECHNIQUE_ABILITY_SEEDS` (1)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "ice_electric_technique_lv2_thundersnow_maul", "name": "Thundersnow Maul", "description": "A maul swung through a sleet storm, landing with frost and thunder.", "ability_type": "technique", "level": 2, "elements": ["ice", "electric"], "base_power": 35, "ap_cost": 29, "effect": "damage", "can_aoe": False},
```

**Spirit**: `old/game/region_seeds/player_abilities/level_2_abilities_by_type/spirit.py` → `LEVEL_2_SPIRIT_ABILITY_SEEDS` (1)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "ice_dark_spirit_lv2_cold_comfort", "name": "Cold Comfort", "description": "Quiet comfort from the long night that soothes the party's wounds and wards them.", "ability_type": "spirit", "level": 2, "elements": ["ice", "dark"], "base_power": 0, "ap_cost": 44, "effect": "status", "status_keys": ["regen", "elemental_defense_buff"], "can_aoe": True},
```

**Magic**: `old/game/region_seeds/player_abilities/level_2_abilities_by_type/magic.py` → `LEVEL_2_MAGIC_ABILITY_SEEDS` (1)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "light_ice_magic_lv2_diamond_dust", "name": "Diamond Dust", "description": "Glittering ice crystals hang in the light, then slice through every foe.", "ability_type": "magic", "level": 2, "elements": ["light", "ice"], "base_power": 29, "ap_cost": 33, "effect": "damage", "can_aoe": True},
```

**Tech**: `old/game/region_seeds/player_abilities/level_2_abilities_by_type/tech.py` → `LEVEL_2_TECH_ABILITY_SEEDS` (1)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "ice_electric_tech_lv2_superconductor_spike", "name": "Superconductor Spike", "description": "A supercooled spike that turns the target into a perfect conductor, then discharges.", "ability_type": "tech", "level": 2, "elements": ["ice", "electric"], "base_power": 29, "ap_cost": 24, "effect": "damage", "can_aoe": False},
```

### 6.3 Level 3 (20)

**Technique**: `old/game/region_seeds/player_abilities/level_3_abilities_by_type/technique.py` → `LEVEL_3_TECHNIQUE_SEEDS` (5)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "light_light_fire_technique_lv3_sunforged_cleave", "name": "Sunforged Cleave", "description": "A two-handed cleave that burns with the heat of a newly forged blade.", "ability_type": "technique", "level": 3, "elements": ["light", "light", "fire"], "base_power": 91, "ap_cost": 80, "effect": "damage", "can_aoe": False},
    {"id": "light_ice_water_technique_lv3_dawnfrost_lunge", "name": "Dawnfrost Lunge", "description": "A long, cold lunge that glitters like frost at sunrise.", "ability_type": "technique", "level": 3, "elements": ["light", "ice", "water"], "base_power": 95, "ap_cost": 85, "effect": "damage", "can_aoe": False},
    {"id": "light_earth_light_technique_lv3_bastion_of_dawn", "name": "Bastion of Dawn", "description": "A shield raised to the sun that steels the whole party behind it.", "ability_type": "technique", "level": 3, "elements": ["light", "earth", "light"], "base_power": 0, "ap_cost": 87, "effect": "status", "status_keys": ["defense_buff", "constitution_buff", "elemental_defense_buff"], "can_aoe": True},
    {"id": "light_air_light_technique_lv3_halo_whirlwind", "name": "Halo Whirlwind", "description": "A spinning sweep that leaves a ring of light around the wielder.", "ability_type": "technique", "level": 3, "elements": ["light", "air", "light"], "base_power": 71, "ap_cost": 77, "effect": "damage", "can_aoe": True},
    {"id": "light_electric_light_technique_lv3_dazzling_bash", "name": "Dazzling Bash", "description": "A shield bash and a flash of light that stuns the foe and spoils its aim.", "ability_type": "technique", "level": 3, "elements": ["light", "electric", "light"], "base_power": 3, "ap_cost": 75, "effect": "status", "status_keys": ["stun", "attack_debuff"], "can_aoe": False},
```

**Magic**: `old/game/region_seeds/player_abilities/level_3_abilities_by_type/magic.py` → `LEVEL_3_MAGIC_SEEDS` (7)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "light_light_fire_magic_lv3_sunlance", "name": "Sunlance", "description": "A lance of concentrated sunlight that burns straight through.", "ability_type": "magic", "level": 3, "elements": ["light", "light", "fire"], "base_power": 91, "ap_cost": 80, "effect": "damage", "can_aoe": False},
    {"id": "light_light_water_magic_lv3_prism_rain", "name": "Prism Rain", "description": "Rain that splits the light into a thousand cutting colors.", "ability_type": "magic", "level": 3, "elements": ["light", "light", "water"], "base_power": 85, "ap_cost": 93, "effect": "damage", "can_aoe": True},
    {"id": "light_light_earth_magic_lv3_glass_prison", "name": "Glass Prison", "description": "Light hardens into glass around the target and locks it in place.", "ability_type": "magic", "level": 3, "elements": ["light", "light", "earth"], "base_power": 3, "ap_cost": 108, "effect": "status", "status_keys": ["petrify"], "can_aoe": False},
    {"id": "light_light_air_magic_lv3_mirage", "name": "Mirage", "description": "Bent light and shimmering air show the target enemies that are not there.", "ability_type": "magic", "level": 3, "elements": ["light", "light", "air"], "base_power": 3, "ap_cost": 101, "effect": "status", "status_keys": ["confuse", "dexterity_debuff"], "can_aoe": False},
    {"id": "light_light_ice_magic_lv3_sundog_lance", "name": "Sundog Lance", "description": "Twin false suns flare in the ice haze, then strike as one.", "ability_type": "magic", "level": 3, "elements": ["light", "light", "ice"], "base_power": 91, "ap_cost": 80, "effect": "damage", "can_aoe": False},
    {"id": "light_light_electric_magic_lv3_solar_storm", "name": "Solar Storm", "description": "A storm of charged sunlight that crackles across the battlefield.", "ability_type": "magic", "level": 3, "elements": ["light", "light", "electric"], "base_power": 85, "ap_cost": 93, "effect": "damage", "can_aoe": True},
    {"id": "light_light_dark_magic_lv3_eclipse_hex", "name": "Eclipse Hex", "description": "For a moment the target's world goes dark, and its voice goes with it.", "ability_type": "magic", "level": 3, "elements": ["light", "light", "dark"], "base_power": 3, "ap_cost": 92, "effect": "status", "status_keys": ["silence", "elemental_debuff"], "can_aoe": False},
```

**Tech**: `old/game/region_seeds/player_abilities/level_3_abilities_by_type/tech.py` → `LEVEL_3_TECH_SEEDS` (1)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "dark_light_electric_tech_lv3_eclipse_emitter", "name": "Eclipse Emitter", "description": "Alternating pulses of light and dark that scramble the target's senses.", "ability_type": "tech", "level": 3, "elements": ["dark", "light", "electric"], "base_power": 3, "ap_cost": 99, "effect": "status", "status_keys": ["confuse", "elemental_debuff"], "can_aoe": False},
```

**Skill**: `old/game/region_seeds/player_abilities/level_3_abilities_by_type/skill.py` → `LEVEL_3_SKILL_SEEDS` (7)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "light_light_fire_skill_lv3_sunflash_kick", "name": "Sunflash Kick", "description": "A spinning kick that lands in a flash of hot light.", "ability_type": "skill", "level": 3, "elements": ["light", "light", "fire"], "base_power": 63, "ap_cost": 55, "effect": "damage", "can_aoe": False},
    {"id": "light_light_water_skill_lv3_moonwater_step", "name": "Moonwater Step", "description": "Footwork like moonlight on water: there one moment, gone the next.", "ability_type": "skill", "level": 3, "elements": ["light", "light", "water"], "base_power": 0, "ap_cost": 72, "effect": "status", "status_keys": ["dexterity_buff", "defense_buff", "elemental_defense_buff"], "can_aoe": False},
    {"id": "light_light_earth_skill_lv3_glass_caltrops", "name": "Glass Caltrops", "description": "Polished caltrops that catch the light, and the feet of every foe.", "ability_type": "skill", "level": 3, "elements": ["light", "light", "earth"], "base_power": 52, "ap_cost": 56, "effect": "damage", "can_aoe": True},
    {"id": "light_light_air_skill_lv3_pinwheel_flash", "name": "Pinwheel Flash", "description": "A spinning throw of mirrored blades that dazzles the whole enemy line.", "ability_type": "skill", "level": 3, "elements": ["light", "light", "air"], "base_power": 3, "ap_cost": 79, "effect": "status", "status_keys": ["attack_debuff", "dexterity_debuff"], "can_aoe": True},
    {"id": "light_light_ice_skill_lv3_diamond_edge", "name": "Diamond Edge", "description": "A blade edge rimed with ice that glitters like diamond as it cuts.", "ability_type": "skill", "level": 3, "elements": ["light", "light", "ice"], "base_power": 65, "ap_cost": 58, "effect": "damage", "can_aoe": False},
    {"id": "light_light_electric_skill_lv3_flash_reflex", "name": "Flash Reflex", "description": "Senses sharpened to a spark: every move comes a beat early.", "ability_type": "skill", "level": 3, "elements": ["light", "light", "electric"], "base_power": 0, "ap_cost": 77, "effect": "status", "status_keys": ["dexterity_buff", "dexterity_buff", "attack_buff"], "can_aoe": False},
    {"id": "light_light_dark_skill_lv3_twilight_feint", "name": "Twilight Feint", "description": "A feint between light and shadow that leaves the foe guarding the wrong side.", "ability_type": "skill", "level": 3, "elements": ["light", "light", "dark"], "base_power": 3, "ap_cost": 81, "effect": "status", "status_keys": ["confuse", "defense_debuff"], "can_aoe": False},
```

### 6.4 Level 4 (31)

**Technique**: `old/game/region_seeds/player_abilities/level_4_abilities_by_type/technique.py` → `LEVEL_4_TECHNIQUE_ABILITY_SEEDS` (4)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "ice_ice_electric_light_technique_lv4_thundersnow_cleaver", "name": "Thundersnow Cleaver", "description": "A heavy cleaver blow that brings down frost and thunder together.", "ability_type": "technique", "level": 4, "elements": ["ice", "ice", "electric", "light"], "base_power": 143, "ap_cost": 120, "effect": "damage", "can_aoe": False},
    {"id": "electric_ice_dark_water_technique_lv4_stormsurge_rend", "name": "Stormsurge Rend", "description": "A rending sweep that crashes through the enemy line like a winter storm.", "ability_type": "technique", "level": 4, "elements": ["electric", "ice", "dark", "water"], "base_power": 108, "ap_cost": 128, "effect": "damage", "can_aoe": True},
    {"id": "light_ice_electric_fire_technique_lv4_aurora_rally", "name": "Aurora Rally", "description": "A rallying cry under shimmering northern lights that sharpens every ally's blows.", "ability_type": "technique", "level": 4, "elements": ["light", "ice", "electric", "fire"], "base_power": 0, "ap_cost": 108, "effect": "status", "status_keys": ["attack_buff", "strength_buff", "elemental_attack_buff", "dexterity_buff"], "can_aoe": True},
    {"id": "dark_ice_ice_earth_technique_lv4_black_ice_crusher", "name": "Black Ice Crusher", "description": "A crushing overhead strike that buries the foe under black ice.", "ability_type": "technique", "level": 4, "elements": ["dark", "ice", "ice", "earth"], "base_power": 137, "ap_cost": 113, "effect": "damage", "can_aoe": False},
```

**Spirit**: `old/game/region_seeds/player_abilities/level_4_abilities_by_type/spirit.py` → `LEVEL_4_SPIRIT_ABILITY_SEEDS` (8)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "ice_electric_air_light_spirit_lv4_aurora_benediction", "name": "Aurora Benediction", "description": "Ribbons of aurora light settle over the party, quickening hands and minds.", "ability_type": "spirit", "level": 4, "elements": ["ice", "electric", "air", "light"], "base_power": 0, "ap_cost": 108, "effect": "status", "status_keys": ["elemental_attack_buff", "intelligence_buff", "dexterity_buff", "attack_buff"], "can_aoe": True},
    {"id": "ice_electric_air_water_spirit_lv4_thundersnow_psalm", "name": "Thundersnow Psalm", "description": "A psalm that calls down sleet and thunder on every foe.", "ability_type": "spirit", "level": 4, "elements": ["ice", "electric", "air", "water"], "base_power": 104, "ap_cost": 123, "effect": "damage", "can_aoe": True},
    {"id": "ice_electric_dark_light_spirit_lv4_polar_night_vigil", "name": "Polar Night Vigil", "description": "A vigil kept through the long dark that restores the whole party.", "ability_type": "spirit", "level": 4, "elements": ["ice", "electric", "dark", "light"], "base_power": 127, "ap_cost": 142, "effect": "heal", "can_aoe": True},
    {"id": "ice_electric_dark_ice_spirit_lv4_midwinter_judgment", "name": "Midwinter Judgment", "description": "Cold, crackling judgment that falls on a single foe.", "ability_type": "spirit", "level": 4, "elements": ["ice", "electric", "dark", "ice"], "base_power": 126, "ap_cost": 107, "effect": "damage", "can_aoe": False},
    {"id": "ice_electric_fire_light_spirit_lv4_hearthlight_thaw", "name": "Hearthlight Thaw", "description": "A thawing warmth that frees every ally from stone and shock.", "ability_type": "spirit", "level": 4, "elements": ["ice", "electric", "fire", "light"], "base_power": 0, "ap_cost": 88, "effect": "cure", "status_keys": ["petrify", "stun"], "can_aoe": True},
    {"id": "ice_electric_light_light_spirit_lv4_northern_lights_mend", "name": "Northern Lights Mend", "description": "The northern lights gather in one ally's wounds and seal them.", "ability_type": "spirit", "level": 4, "elements": ["ice", "electric", "light", "light"], "base_power": 147, "ap_cost": 121, "effect": "heal", "can_aoe": False},
    {"id": "ice_earth_light_water_spirit_lv4_permafrost_ward", "name": "Permafrost Ward", "description": "A ward as deep and unmoving as permafrost settles over the party.", "ability_type": "spirit", "level": 4, "elements": ["ice", "earth", "light", "water"], "base_power": 0, "ap_cost": 116, "effect": "status", "status_keys": ["defense_buff", "elemental_defense_buff", "constitution_buff", "regen"], "can_aoe": True},
    {"id": "ice_earth_dark_water_spirit_lv4_burial_frost", "name": "Burial Frost", "description": "A grave-cold curse that seeps into every foe's bones, sapping strength and life.", "ability_type": "spirit", "level": 4, "elements": ["ice", "earth", "dark", "water"], "base_power": 5, "ap_cost": 142, "effect": "status", "status_keys": ["continuous_damage", "constitution_debuff", "strength_debuff", "attack_debuff"], "can_aoe": True},
```

**Magic**: `old/game/region_seeds/player_abilities/level_4_abilities_by_type/magic.py` → `LEVEL_4_MAGIC_ABILITY_SEEDS` (4)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "light_water_ice_electric_magic_lv4_prismatic_deluge", "name": "Prismatic Deluge", "description": "A deluge lit from within that freezes and shocks as it falls.", "ability_type": "magic", "level": 4, "elements": ["light", "water", "ice", "electric"], "base_power": 107, "ap_cost": 125, "effect": "damage", "can_aoe": True},
    {"id": "light_water_ice_fire_magic_lv4_thermal_prism", "name": "Thermal Prism", "description": "Light bends through steam and ice, then focuses into a scorching beam.", "ability_type": "magic", "level": 4, "elements": ["light", "water", "ice", "fire"], "base_power": 145, "ap_cost": 123, "effect": "damage", "can_aoe": False},
    {"id": "light_water_electric_air_magic_lv4_storm_halo", "name": "Storm Halo", "description": "A crackling halo of rain and light that sharpens the party's spellwork.", "ability_type": "magic", "level": 4, "elements": ["light", "water", "electric", "air"], "base_power": 0, "ap_cost": 117, "effect": "status", "status_keys": ["intelligence_buff", "elemental_attack_buff", "dexterity_buff", "elemental_defense_buff"], "can_aoe": True},
    {"id": "light_light_dark_air_magic_lv4_blinding_verdict", "name": "Blinding Verdict", "description": "A verdict of blinding light that leaves every foe lost and exposed.", "ability_type": "magic", "level": 4, "elements": ["light", "light", "dark", "air"], "base_power": 5, "ap_cost": 138, "effect": "status", "status_keys": ["confuse", "attack_debuff", "elemental_debuff"], "can_aoe": True},
```

**Tech**: `old/game/region_seeds/player_abilities/level_4_abilities_by_type/tech.py` → `LEVEL_4_TECH_ABILITY_SEEDS` (7)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "electric_water_ice_air_tech_lv4_storm_cell_projector", "name": "Storm Cell Projector", "description": "Seeds a miniature thunderstorm over the enemy line.", "ability_type": "tech", "level": 4, "elements": ["electric", "water", "ice", "air"], "base_power": 103, "ap_cost": 118, "effect": "damage", "can_aoe": True},
    {"id": "ice_water_earth_fire_tech_lv4_thermal_shock_drill", "name": "Thermal Shock Drill", "description": "A drill bit cycled between red-hot and supercooled until the target cracks.", "ability_type": "tech", "level": 4, "elements": ["ice", "water", "earth", "fire"], "base_power": 125, "ap_cost": 104, "effect": "damage", "can_aoe": False},
    {"id": "earth_electric_water_air_tech_lv4_magnetic_mire_field", "name": "Magnetic Mire Field", "description": "An electromagnetic field that turns the ground beneath the enemy to sucking mud.", "ability_type": "tech", "level": 4, "elements": ["earth", "electric", "water", "air"], "base_power": 5, "ap_cost": 120, "effect": "status", "status_keys": ["dexterity_debuff", "defense_debuff", "elemental_debuff", "attack_debuff"], "can_aoe": True},
    {"id": "fire_earth_ice_dark_tech_lv4_bunker_buster", "name": "Bunker Buster", "description": "A shaped charge that burrows in before it detonates.", "ability_type": "tech", "level": 4, "elements": ["fire", "earth", "ice", "dark"], "base_power": 123, "ap_cost": 101, "effect": "damage", "can_aoe": False},
    {"id": "water_fire_ice_electric_tech_lv4_pressure_cooker_mine", "name": "Pressure Cooker Mine", "description": "A mine that flash-boils its payload into a scalding blast.", "ability_type": "tech", "level": 4, "elements": ["water", "fire", "ice", "electric"], "base_power": 109, "ap_cost": 129, "effect": "damage", "can_aoe": True},
    {"id": "air_earth_water_ice_tech_lv4_climate_shield", "name": "Climate Shield", "description": "Deployable weather shielding that keeps the party safe from the elements.", "ability_type": "tech", "level": 4, "elements": ["air", "earth", "water", "ice"], "base_power": 0, "ap_cost": 115, "effect": "status", "status_keys": ["elemental_defense_buff", "defense_buff", "constitution_buff", "regen"], "can_aoe": True},
    {"id": "dark_electric_fire_dark_tech_lv4_blackout_virus", "name": "Blackout Virus", "description": "A virus that spreads through the enemy line and crashes everything: no casting, no movement, no thought.", "ability_type": "tech", "level": 4, "elements": ["dark", "electric", "fire", "dark"], "base_power": 5, "ap_cost": 148, "effect": "status", "status_keys": ["silence", "stun", "intelligence_debuff"], "can_aoe": True},
```

**Skill**: `old/game/region_seeds/player_abilities/level_4_abilities_by_type/skill.py` → `LEVEL_4_SKILL_ABILITY_SEEDS` (8)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "ice_electric_air_light_skill_lv4_sleetstep_flurry", "name": "Sleetstep Flurry", "description": "A flurry of strikes delivered between flakes of charged sleet.", "ability_type": "skill", "level": 4, "elements": ["ice", "electric", "air", "light"], "base_power": 140, "ap_cost": 120, "effect": "damage", "can_aoe": False},
    {"id": "electric_ice_fire_earth_skill_lv4_hailspark_fan", "name": "Hailspark Fan", "description": "Throwing stars that alternate frost and spark as they fan out.", "ability_type": "skill", "level": 4, "elements": ["electric", "ice", "fire", "earth"], "base_power": 112, "ap_cost": 132, "effect": "damage", "can_aoe": True},
    {"id": "ice_electric_water_dark_skill_lv4_tripwire_freeze", "name": "Tripwire Freeze", "description": "Iced, charged wire strung across the enemy's path.", "ability_type": "skill", "level": 4, "elements": ["ice", "electric", "water", "dark"], "base_power": 5, "ap_cost": 147, "effect": "status", "status_keys": ["dexterity_debuff", "stun", "elemental_debuff"], "can_aoe": True},
    {"id": "electric_ice_air_air_skill_lv4_static_blur", "name": "Static Blur", "description": "The party moves in a crackling blur, too fast to follow.", "ability_type": "skill", "level": 4, "elements": ["electric", "ice", "air", "air"], "base_power": 0, "ap_cost": 138, "effect": "status", "status_keys": ["dexterity_buff", "attack_buff", "dexterity_buff", "regen"], "can_aoe": True},
    {"id": "ice_electric_light_earth_skill_lv4_thundersnow_wheel", "name": "Thundersnow Wheel", "description": "A cartwheel kick that throws sparking ice in every direction.", "ability_type": "skill", "level": 4, "elements": ["ice", "electric", "light", "earth"], "base_power": 110, "ap_cost": 129, "effect": "damage", "can_aoe": True},
    {"id": "electric_ice_dark_fire_skill_lv4_blackfrost_jolt", "name": "Blackfrost Jolt", "description": "A jab of black frost with a buried charge that bursts a moment later.", "ability_type": "skill", "level": 4, "elements": ["electric", "ice", "dark", "fire"], "base_power": 135, "ap_cost": 113, "effect": "damage", "can_aoe": False},
    {"id": "ice_electric_water_earth_skill_lv4_numbing_needles", "name": "Numbing Needles", "description": "A fan of frozen needles carrying a nerve-numbing charge into every foe.", "ability_type": "skill", "level": 4, "elements": ["ice", "electric", "water", "earth"], "base_power": 5, "ap_cost": 126, "effect": "status", "status_keys": ["dexterity_debuff", "strength_debuff", "continuous_damage"], "can_aoe": True},
    {"id": "electric_ice_light_air_skill_lv4_aurora_dance", "name": "Aurora Dance", "description": "A whirling dance under shimmering lights that leaves every foe dizzy and slow.", "ability_type": "skill", "level": 4, "elements": ["electric", "ice", "light", "air"], "base_power": 5, "ap_cost": 113, "effect": "status", "status_keys": ["confuse", "dexterity_debuff"], "can_aoe": True},
```

### 6.5 Level 5 (35)

**Technique**: `old/game/region_seeds/player_abilities/level_5_abilities_by_type/technique.py` → `LEVEL_5_TECHNIQUE_ABILITY_SEEDS` (8)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "fire_fire_water_electric_dark_technique_lv5_hellforge_hammer", "name": "Hellforge Hammer", "description": "A hammer blow straight from the forge, quenched in storm water on the way down.", "ability_type": "technique", "level": 5, "elements": ["fire", "fire", "water", "electric", "dark"], "base_power": 188, "ap_cost": 169, "effect": "damage", "can_aoe": False},
    {"id": "water_fire_air_ice_dark_technique_lv5_riptide_reaver", "name": "Riptide Reaver", "description": "A reaver's swing that drags the whole enemy line into a churning undertow.", "ability_type": "technique", "level": 5, "elements": ["water", "fire", "air", "ice", "dark"], "base_power": 170, "ap_cost": 177, "effect": "damage", "can_aoe": True},
    {"id": "earth_water_electric_light_air_technique_lv5_mountain_splitter", "name": "Mountain Splitter", "description": "A blow with the patience of erosion and the force of a landslide.", "ability_type": "technique", "level": 5, "elements": ["earth", "water", "electric", "light", "air"], "base_power": 192, "ap_cost": 174, "effect": "damage", "can_aoe": False},
    {"id": "air_earth_ice_electric_dark_technique_lv5_skyfall_cyclone", "name": "Skyfall Cyclone", "description": "Leap into a howling cyclone and come down on every foe at once.", "ability_type": "technique", "level": 5, "elements": ["air", "earth", "ice", "electric", "dark"], "base_power": 173, "ap_cost": 180, "effect": "damage", "can_aoe": True},
    {"id": "ice_water_light_dark_fire_technique_lv5_glacial_executioner", "name": "Glacial Executioner", "description": "A slow, inevitable blade that falls like a calving glacier.", "ability_type": "technique", "level": 5, "elements": ["ice", "water", "light", "dark", "fire"], "base_power": 192, "ap_cost": 174, "effect": "damage", "can_aoe": False},
    {"id": "electric_electric_water_air_light_technique_lv5_ares_war_banner", "name": "Ares' War Banner", "description": "Plant the war god's banner in crackling ground; every ally fights faster and harder beneath it.", "ability_type": "technique", "level": 5, "elements": ["electric", "electric", "water", "air", "light"], "base_power": 0, "ap_cost": 160, "effect": "status", "status_keys": ["attack_buff", "attack_buff", "strength_buff", "dexterity_buff", "elemental_attack_buff", "constitution_buff"], "can_aoe": True},
    {"id": "light_fire_ice_electric_dark_technique_lv5_dawnbreaker", "name": "Dawnbreaker", "description": "A charge that splits the dark like sunrise and scatters every foe in its path.", "ability_type": "technique", "level": 5, "elements": ["light", "fire", "ice", "electric", "dark"], "base_power": 177, "ap_cost": 186, "effect": "damage", "can_aoe": True},
    {"id": "dark_electric_water_air_ice_technique_lv5_executioners_mark", "name": "Executioner's Mark", "description": "A brutal opening blow that marks the foe for the kill: guard broken, strength failing.", "ability_type": "technique", "level": 5, "elements": ["dark", "electric", "water", "air", "ice"], "base_power": 5, "ap_cost": 178, "effect": "status", "status_keys": ["stun", "defense_debuff", "elemental_debuff", "strength_debuff", "constitution_debuff"], "can_aoe": False},
```

**Spirit**: `old/game/region_seeds/player_abilities/level_5_abilities_by_type/spirit.py` → `LEVEL_5_SPIRIT_ABILITY_SEEDS` (7)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "light_ice_electric_dark_water_spirit_lv5_aurora_of_the_long_night", "name": "Aurora of the Long Night", "description": "An aurora ripples across the dark sky and mends every ally beneath it.", "ability_type": "spirit", "level": 5, "elements": ["light", "ice", "electric", "dark", "water"], "base_power": 125, "ap_cost": 148, "effect": "heal", "can_aoe": True},
    {"id": "dark_ice_electric_light_light_spirit_lv5_midwinter_return", "name": "Midwinter Return", "description": "Called back across the dark, a fallen ally wakes to cold air and northern lights.", "ability_type": "spirit", "level": 5, "elements": ["dark", "ice", "electric", "light", "light"], "base_power": 160, "ap_cost": 200, "effect": "revive", "can_aoe": False},
    {"id": "electric_ice_dark_fire_light_spirit_lv5_polar_night_litany", "name": "Polar Night Litany", "description": "A litany chanted through the long dark that turns every ally's weapons bright and cold.", "ability_type": "spirit", "level": 5, "elements": ["electric", "ice", "dark", "fire", "light"], "base_power": 0, "ap_cost": 181, "effect": "status", "status_keys": ["elemental_attack_buff", "elemental_attack_buff", "attack_buff", "strength_buff", "intelligence_buff", "dexterity_buff"], "can_aoe": True},
    {"id": "ice_ice_electric_dark_fire_spirit_lv5_judgment_of_the_north", "name": "Judgment of the North", "description": "A pillar of frozen lightning that falls on a single foe.", "ability_type": "spirit", "level": 5, "elements": ["ice", "ice", "electric", "dark", "fire"], "base_power": 174, "ap_cost": 156, "effect": "damage", "can_aoe": False},
    {"id": "dark_dark_ice_electric_fire_spirit_lv5_hades_long_night", "name": "Hades' Long Night", "description": "The lord of the underworld lets the long night fall on every foe.", "ability_type": "spirit", "level": 5, "elements": ["dark", "dark", "ice", "electric", "fire"], "base_power": 5, "ap_cost": 175, "effect": "status", "status_keys": ["sleep", "continuous_damage", "attack_debuff", "intelligence_debuff"], "can_aoe": True},
    {"id": "ice_electric_dark_earth_light_spirit_lv5_spring_thaw", "name": "Spring Thaw", "description": "The first thaw of spring breaks every hold on the party: stone, shock, madness and silence.", "ability_type": "spirit", "level": 5, "elements": ["ice", "electric", "dark", "earth", "light"], "base_power": 0, "ap_cost": 178, "effect": "cure", "status_keys": ["petrify", "stun", "confuse", "silence"], "can_aoe": True},
    {"id": "earth_ice_electric_dark_water_spirit_lv5_glacier_sanctum", "name": "Glacier Sanctum", "description": "The party is sealed in a sanctum of ancient ice that hums with stored lightning.", "ability_type": "spirit", "level": 5, "elements": ["earth", "ice", "electric", "dark", "water"], "base_power": 0, "ap_cost": 173, "effect": "status", "status_keys": ["defense_buff", "defense_buff", "elemental_defense_buff", "elemental_defense_buff", "constitution_buff", "regen"], "can_aoe": True},
```

**Magic**: `old/game/region_seeds/player_abilities/level_5_abilities_by_type/magic.py` → `LEVEL_5_MAGIC_ABILITY_SEEDS` (8)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "electric_electric_ice_light_air_magic_lv5_wrath_of_boreas", "name": "Wrath of Boreas", "description": "The god of the north wind exhales sleet and lightning over every foe.", "ability_type": "magic", "level": 5, "elements": ["electric", "electric", "ice", "light", "air"], "base_power": 165, "ap_cost": 171, "effect": "damage", "can_aoe": True},
    {"id": "ice_ice_electric_water_dark_magic_lv5_frozen_lightning", "name": "Frozen Lightning", "description": "A bolt of lightning frozen mid-strike, then driven through one foe.", "ability_type": "magic", "level": 5, "elements": ["ice", "ice", "electric", "water", "dark"], "base_power": 202, "ap_cost": 181, "effect": "damage", "can_aoe": False},
    {"id": "electric_ice_light_light_fire_magic_lv5_celestial_arc", "name": "Celestial Arc", "description": "An arc of white-hot starlight and frost that splits the target.", "ability_type": "magic", "level": 5, "elements": ["electric", "ice", "light", "light", "fire"], "base_power": 202, "ap_cost": 181, "effect": "damage", "can_aoe": False},
    {"id": "electric_ice_dark_dark_water_magic_lv5_polar_eclipse", "name": "Polar Eclipse", "description": "A dark, frozen storm that saps every foe's guard and speed.", "ability_type": "magic", "level": 5, "elements": ["electric", "ice", "dark", "dark", "water"], "base_power": 5, "ap_cost": 169, "effect": "status", "status_keys": ["elemental_debuff", "dexterity_debuff", "continuous_damage"], "can_aoe": True},
    {"id": "ice_electric_earth_ice_air_magic_lv5_ice_age_tempest", "name": "Ice Age Tempest", "description": "A storm out of the ice age, all hail and thunder.", "ability_type": "magic", "level": 5, "elements": ["ice", "electric", "earth", "ice", "air"], "base_power": 168, "ap_cost": 175, "effect": "damage", "can_aoe": True},
    {"id": "electric_ice_fire_water_air_magic_lv5_ball_lightning", "name": "Ball Lightning", "description": "A slow, humming sphere of lightning that hunts its target and bursts.", "ability_type": "magic", "level": 5, "elements": ["electric", "ice", "fire", "water", "air"], "base_power": 202, "ap_cost": 181, "effect": "damage", "can_aoe": False},
    {"id": "electric_electric_ice_dark_air_magic_lv5_stormcallers_hex", "name": "Stormcaller's Hex", "description": "A curse that pins every foe beneath its own private storm.", "ability_type": "magic", "level": 5, "elements": ["electric", "electric", "ice", "dark", "air"], "base_power": 5, "ap_cost": 164, "effect": "status", "status_keys": ["stun", "elemental_debuff", "defense_debuff", "intelligence_debuff"], "can_aoe": True},
    {"id": "electric_light_water_air_earth_magic_lv5_heavens_circuit", "name": "Heaven's Circuit", "description": "A circuit of light links the party, sharing strength and speed.", "ability_type": "magic", "level": 5, "elements": ["electric", "light", "water", "air", "earth"], "base_power": 0, "ap_cost": 158, "effect": "status", "status_keys": ["intelligence_buff", "elemental_attack_buff", "dexterity_buff", "regen"], "can_aoe": True},
```

**Tech**: `old/game/region_seeds/player_abilities/level_5_abilities_by_type/tech.py` → `LEVEL_5_TECH_ABILITY_SEEDS` (5)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "ice_ice_electric_water_air_tech_lv5_cryogenic_railgun", "name": "Cryogenic Railgun", "description": "A railgun that fires slugs cooled to near absolute zero.", "ability_type": "tech", "level": 5, "elements": ["ice", "ice", "electric", "water", "air"], "base_power": 201, "ap_cost": 181, "effect": "damage", "can_aoe": False},
    {"id": "electric_ice_earth_light_air_tech_lv5_superconductor_grid", "name": "Superconductor Grid", "description": "A floor grid of superconducting cable that speeds and shields the party.", "ability_type": "tech", "level": 5, "elements": ["electric", "ice", "earth", "light", "air"], "base_power": 0, "ap_cost": 162, "effect": "status", "status_keys": ["dexterity_buff", "intelligence_buff", "elemental_defense_buff", "regen"], "can_aoe": True},
    {"id": "ice_electric_dark_dark_water_tech_lv5_stasis_field", "name": "Stasis Field", "description": "A field that slows time and temperature for every foe inside it.", "ability_type": "tech", "level": 5, "elements": ["ice", "electric", "dark", "dark", "water"], "base_power": 5, "ap_cost": 176, "effect": "status", "status_keys": ["stun", "dexterity_debuff", "elemental_debuff", "defense_debuff"], "can_aoe": True},
    {"id": "electric_ice_fire_light_air_tech_lv5_thermal_inversion_bomb", "name": "Thermal Inversion Bomb", "description": "A bomb that violently swaps heat and cold across the whole blast.", "ability_type": "tech", "level": 5, "elements": ["electric", "ice", "fire", "light", "air"], "base_power": 166, "ap_cost": 174, "effect": "damage", "can_aoe": True},
    {"id": "ice_ice_light_air_water_tech_lv5_zero_point_lance", "name": "Zero-Point Lance", "description": "A lance of zero-point energy that freezes matter solid at the tip.", "ability_type": "tech", "level": 5, "elements": ["ice", "ice", "light", "air", "water"], "base_power": 205, "ap_cost": 186, "effect": "damage", "can_aoe": False},
```

**Skill**: `old/game/region_seeds/player_abilities/level_5_abilities_by_type/skill.py` → `LEVEL_5_SKILL_ABILITY_SEEDS` (7)

```python
    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "ice_electric_fire_light_earth_skill_lv5_frostlight_thousand_cuts", "name": "Frostlight Thousand Cuts", "description": "A thousand cuts in a single breath, each one cold and bright.", "ability_type": "skill", "level": 5, "elements": ["ice", "electric", "fire", "light", "earth"], "base_power": 188, "ap_cost": 169, "effect": "damage", "can_aoe": False},
    {"id": "electric_ice_water_dark_air_skill_lv5_thunderstep_cyclone", "name": "Thunderstep Cyclone", "description": "A spinning dash through the enemy line that leaves frost and lightning in its wake.", "ability_type": "skill", "level": 5, "elements": ["electric", "ice", "water", "dark", "air"], "base_power": 158, "ap_cost": 164, "effect": "damage", "can_aoe": True},
    {"id": "fire_ice_electric_water_light_skill_lv5_hermes_stride", "name": "Hermes' Stride", "description": "Borrowed from the messenger god: every ally moves like the wind for a while.", "ability_type": "skill", "level": 5, "elements": ["fire", "ice", "electric", "water", "light"], "base_power": 0, "ap_cost": 181, "effect": "status", "status_keys": ["dexterity_buff", "dexterity_buff", "attack_buff", "elemental_attack_buff", "regen"], "can_aoe": True},
    {"id": "water_ice_electric_dark_earth_skill_lv5_undertow_venom", "name": "Undertow Venom", "description": "Poisoned needles that drag every foe down like a cold undertow.", "ability_type": "skill", "level": 5, "elements": ["water", "ice", "electric", "dark", "earth"], "base_power": 5, "ap_cost": 164, "effect": "status", "status_keys": ["continuous_damage", "dexterity_debuff", "constitution_debuff", "attack_debuff"], "can_aoe": True},
    {"id": "earth_ice_electric_fire_light_skill_lv5_fault_line_strike", "name": "Fault Line Strike", "description": "A heel-drop that splits the ground along a crackling, frozen fault.", "ability_type": "skill", "level": 5, "elements": ["earth", "ice", "electric", "fire", "light"], "base_power": 200, "ap_cost": 185, "effect": "damage", "can_aoe": False},
    {"id": "light_ice_electric_dark_water_skill_lv5_prism_smoke", "name": "Prism Smoke", "description": "Smoke laced with prism dust and static that leaves the enemy line blind and turned around.", "ability_type": "skill", "level": 5, "elements": ["light", "ice", "electric", "dark", "water"], "base_power": 5, "ap_cost": 184, "effect": "status", "status_keys": ["attack_debuff", "dexterity_debuff", "confuse", "elemental_debuff"], "can_aoe": True},
    {"id": "dark_dark_fire_air_earth_skill_lv5_ashen_assassination", "name": "Ashen Assassination", "description": "A strike from the smoke of a burning field, aimed at the one spot that matters.", "ability_type": "skill", "level": 5, "elements": ["dark", "dark", "fire", "air", "earth"], "base_power": 188, "ap_cost": 169, "effect": "damage", "can_aoe": False},
```

## 7. Acceptance checks

**7.1 Coverage.** Run from the `old/` folder. Expect no assertion error and 707 learnable abilities.

```python
from collections import Counter
from game.constants import PLAYER_ABILITY_SEEDS
EL = ['fire', 'water', 'earth', 'air', 'ice', 'electric', 'light', 'dark']
TARGET = {1: 4, 2: 8, 3: 8, 4: 8, 5: 8}
pool = [a for a in PLAYER_ABILITY_SEEDS if not a.get('non_player_ability')]
print(len(pool))  # 707
assert len({a['id'] for a in PLAYER_ABILITY_SEEDS}) == len(PLAYER_ABILITY_SEEDS), 'duplicate id'
assert all(len(a['elements']) >= a['level'] for a in pool)
c = Counter()
for a in pool:
    for e in set(a['elements']):
        c[(a['ability_type'], a['level'], e)] += 1
short = [(t, L, e, c[(t, L, e)]) for t in ['technique', 'spirit', 'magic', 'tech', 'skill']
         for L in range(1, 6) for e in EL if c[(t, L, e)] < TARGET[L]]
assert not short, short
```

**7.2 Per character.** With stats ignored (class and element only), every recruit can learn at least 8 / 15 / 13 / 12 / 9 abilities at Levels 1–5. Each two-element recruit has exactly 8 at Level 1. Full table in Appendix A.

**7.3 Dev-tool ability validator** (Data Management → Abilities → validate):

| | Before | After |
|---|---|---|
| Abilities scanned | 503 | 707 |
| Errors (progression break) | 4 | 4 (same four, all existing) |
| Warnings (AP mispriced, support efficiency) | 9 | 8 (Venom Trace no longer flagged) |
| Info / notice (balance weak / strong) | 115 | 157 (42 of them on new abilities) |

Expected on the new abilities: **no errors and no warnings**. The 42 info/notice notes are the same kind the existing set carries, mostly single-target damage reading "weak" against area attacks of the same level; existing peers at the same price get the same note. No existing ability gains a flag.

**7.4 Startup element-map validator:** still zero warnings (no change to the element map or any recruit kit).

**7.5 In game:** open the learn screen for any recruit. Every level shows the counts in Appendix A once the stat requirements are met.

## 8. Out of scope

- Existing abilities, including the four existing progression-break errors and eight existing warnings.
- Stat requirements, ability-slot timing and the learn rule itself.
- Signature abilities and enemy ability kits.

## Appendix A: Learnable abilities per character (class and element only)

| Character | Class | Elements | Before (L1–L5) | After (L1–L5) |
|---|---|---|---|---|
| Chock | Technique | earth, fire, water, light | 5 / 27 / 20 / 14 / 6 | 16 / 27 / 25 / 18 / 14 |
| Kaera | Spirit | light, water, fire, earth | 7 / 26 / 35 / 17 / 11 | 16 / 26 / 35 / 24 / 18 |
| Moxie | Magic | fire, ice, electric, dark | 5 / 27 / 18 / 14 / 12 | 16 / 28 / 22 / 18 / 20 |
| Kade | Tech | electric, light, water, air | 4 / 26 / 23 / 10 / 14 | 16 / 27 / 24 / 16 / 19 |
| Poise | Skill | air, light, ice, earth | 5 / 26 / 15 / 35 / 7 | 16 / 26 / 22 / 43 / 14 |
| Lyren Vale | Spirit | water, earth | 3 / 15 / 20 / 12 / 9 | 8 / 15 / 20 / 15 / 12 |
| Vek | Technique | fire, dark | 2 / 15 / 14 / 11 / 4 | 8 / 15 / 15 / 14 / 10 |
| Warden Hale | Technique | light, earth | 3 / 16 / 10 / 14 / 6 | 8 / 16 / 15 / 17 / 11 |
| Seraphine | Spirit | light, air | 4 / 15 / 23 / 16 / 11 | 8 / 15 / 23 / 22 / 15 |
| Nia | Skill | air, light | 3 / 15 / 8 / 35 / 6 | 8 / 15 / 15 / 39 / 12 |
| Sable | Magic | earth, air | 2 / 16 / 11 / 11 / 13 | 8 / 16 / 13 / 13 / 18 |
| Thorn | Technique | earth, dark | 3 / 16 / 13 / 12 / 6 | 8 / 16 / 14 / 14 / 13 |
| Bragg | Tech | earth, fire | 2 / 15 / 18 / 8 / 9 | 8 / 15 / 18 / 14 / 11 |
| Ripple | Spirit | water, dark | 3 / 14 / 21 / 13 / 10 | 8 / 15 / 21 / 18 / 17 |
| Kor-in | Technique | ice, air | 2 / 15 / 13 / 11 / 5 | 8 / 16 / 15 / 15 / 12 |
| Grimnaw | Tech | dark, electric | 2 / 15 / 14 / 9 / 9 | 8 / 16 / 15 / 14 / 13 |
| Voss Caldera | Tech | earth, light | 2 / 15 / 14 / 10 / 12 | 8 / 15 / 15 / 14 / 15 |
| Rynn | Spirit | water, ice | 3 / 14 / 17 / 11 / 9 | 8 / 15 / 17 / 19 / 16 |
| Eldon Dawnseer | Spirit | light, dark | 4 / 14 / 21 / 17 / 11 | 8 / 15 / 21 / 24 / 18 |
| Regent Sylvara | Magic | dark, electric | 2 / 16 / 12 / 14 / 9 | 8 / 16 / 14 / 17 / 17 |
| Ghost | Skill | dark, water | 3 / 15 / 12 / 31 / 6 | 8 / 15 / 14 / 34 / 11 |
| Lira Emberforge | Technique | fire, earth | 3 / 16 / 16 / 12 / 6 | 8 / 16 / 18 / 14 / 12 |
| Osten Dreamweaver | Magic | dark, water | 2 / 16 / 12 / 13 / 13 | 8 / 16 / 14 / 17 / 18 |
| Lyric | Tech | electric, ice | 2 / 14 / 18 / 6 / 4 | 8 / 15 / 19 / 13 / 9 |
| Dare | Skill | fire, electric | 2 / 15 / 12 / 20 / 5 | 8 / 15 / 14 / 28 / 12 |
| Andrea Starveil | Skill | light, fire | 2 / 15 / 8 / 32 / 5 | 8 / 15 / 15 / 37 / 10 |
| Veyr Ashcant | Magic | fire, light | 2 / 14 / 8 / 9 / 11 | 8 / 15 / 15 / 13 / 15 |
| Maddox "Spark" Quill | Tech | electric, fire | 2 / 14 / 16 / 7 / 9 | 8 / 15 / 17 / 13 / 13 |
| Anita | Magic | dark, air | 2 / 16 / 12 / 15 / 13 | 8 / 16 / 14 / 17 / 20 |
| Talon | Spirit | earth, light | 4 / 15 / 24 / 17 / 11 | 8 / 15 / 24 / 23 / 16 |
| Alden Brightvein | Spirit | light, electric | 4 / 15 / 22 / 16 / 11 | 8 / 15 / 22 / 23 / 18 |
| Commander Drax | Technique | light, electric | 2 / 14 / 10 / 9 / 4 | 8 / 15 / 15 / 12 / 11 |
| Custom hero (all elements) | Technique | all | 9 / 36 / 24 / 14 / 6 | 32 / 37 / 29 / 18 / 14 |
| Custom hero (all elements) | Spirit | all | 11 / 35 / 40 / 17 / 11 | 32 / 36 / 40 / 25 / 18 |
| Custom hero (all elements) | Magic | all | 8 / 36 / 22 / 15 / 13 | 32 / 37 / 29 / 19 / 21 |
| Custom hero (all elements) | Tech | all | 8 / 36 / 28 / 10 / 14 | 32 / 37 / 29 / 17 / 19 |
| Custom hero (all elements) | Skill | all | 10 / 36 / 22 / 35 / 7 | 32 / 36 / 29 / 43 / 14 |
