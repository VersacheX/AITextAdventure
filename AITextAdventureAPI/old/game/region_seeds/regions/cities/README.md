# City Building Constants Reference

## Overview

This directory contains building and sublocation constants for all procedurally generated cities in AI Text Adventure. Each region type (Desert, Forest, Grassland, Mountains, Shallows, Snow, Swamp) has three city size variants (Large, Medium, Small) with unique thematic building configurations.

---

## Table of Contents

1. [Directory Structure](#directory-structure)
2. [File Naming Convention](#file-naming-convention)
3. [Constants File Structure](#constants-file-structure)
4. [Region-City Matrix](#region-city-matrix)
5. [Building Configuration](#building-configuration)
6. [Sublocation System](#sublocation-system)
7. [Customization Guide](#customization-guide)
8. [Integration with Story](#integration-with-story)

---

## Directory Structure

```
regions/
??? cities/
    ??? desert/
    ?   ??? constants_buildings_large_city.py
    ?   ??? constants_buildings_mid_city.py
    ?   ??? constants_buildings_small_city.py
 ??? forest/
?   ??? constants_buildings_large_city.py
    ?   ??? constants_buildings_mid_city.py
    ?   ??? constants_buildings_small_city.py
    ??? grassland/
  ?   ??? constants_buildings_large_city.py
    ?   ??? constants_buildings_mid_city.py
    ? ??? constants_buildings_small_city.py
    ??? mountains/
    ?   ??? constants_buildings_large_city.py
    ?   ??? constants_buildings_mid_city.py
    ?   ??? constants_buildings_small_city.py
    ??? shallows/
    ?   ??? constants_buildings_large_city.py
    ?   ??? constants_buildings_mid_city.py
    ?   ??? constants_buildings_small_city.py
    ??? snow/
    ?   ??? constants_buildings_large_city.py
    ?   ??? constants_buildings_mid_city.py
    ?   ??? constants_buildings_small_city.py
    ??? swamp/
   ??? constants_buildings_large_city.py
        ??? constants_buildings_mid_city.py
        ??? constants_buildings_small_city.py
```

**Total:** 7 regions × 3 city sizes = **21 building constants files**

---

## File Naming Convention

### Pattern
```
constants_buildings_[city_size].py
```

### City Sizes
- `large_city` - Major metropolitan areas (ACT III chapters typically)
- `mid_city` - Medium-sized towns (ACT I-II chapters, regional arcs)
- `small_city` - Small villages/outposts (ACT III-V chapters)

### Examples
```python
# Desert large city (Chapter 8 - Nightveil Spire)
desert/constants_buildings_large_city.py

# Forest medium city (Chapter 2 - Boiling Bubble)
forest/constants_buildings_mid_city.py

# Snow small city (Chapter 14 - Hailward Hold)
snow/constants_buildings_small_city.py
```

---

## Constants File Structure

Every city constants file contains these required sections:

### 1. City Metadata
```python
CITY_NAME = "City Display Name"
CITY_DESCRIPTION = (
    "Multi-line atmospheric description "
    "of the city's theme, architecture, and feel."
)
```

**Rules:**
- `CITY_NAME` - Used in UI and dialog
- `CITY_DESCRIPTION` - Sets narrative tone
- Description should be 3-5 sentences

### 2. Room Menu (Inn Lodging)
```python
ROOM_MENU = [
    {"id": "economy", "name": "Display Name", "value": 20, "heal_fraction": 0.75},
    {"id": "luxury", "name": "Display Name", "value": 75, "heal_fraction": 1.0},
]
```

**Fields:**
- `id` - Internal identifier (DO NOT MODIFY)
- `name` - Display name (CUSTOMIZABLE)
- `value` - Cost in currency (CUSTOMIZABLE within reason)
- `heal_fraction` - HP/AP restore percentage (DO NOT MODIFY)

**Standard Room Types:**
| ID | Typical Name | Value Range | Heal Fraction |
|----|--------------|-------------|---------------|
| `public` | Bench/Floor | 5-8 | 0.25-0.30 |
| `economy` | Room/Cot | 18-25 | 0.70-0.75 |
| `luxury` | Suite/Sanctum | 60-80 | 1.0 |

### 3. Drink Menu (Bar Consumables)
```python
DRINK_MENU = [
    {
  "id": "tiny",
     "name": "Display Name",
        "value": 8,
      "hp_fraction": 0.10,
        "ap_fraction": 0.00,
     "min_level": 1
    },
    # ... more drinks
]
```

**Fields:**
- `id` - Internal tier identifier (DO NOT MODIFY)
- `name` - Display name (CUSTOMIZABLE - make thematic!)
- `value` - Cost (CUSTOMIZABLE - use progression)
- `hp_fraction` - HP restore percentage (DO NOT MODIFY)
- `ap_fraction` - AP restore percentage (DO NOT MODIFY)
- `min_level` - Player level requirement (DO NOT MODIFY)

**Standard Drink Tiers:**
| ID | HP Restore | Value Range | Min Level |
|----|------------|-------------|-----------|
| `tiny` | 10% | 3-10 | 1 |
| `small` | 20% | 8-20 | 1 |
| `mid` | 30-35% | 15-40 | 2 |
| `big` | 50-60% | 40-80 | 4 |
| `huge` | 80-90% | 80-170 | 4 |
| `max` | 100% | 150-250 | 4 |

**Design Note:** Drinks intentionally don't scale prices proportionally to benefit. Buying drinks triggers random encounters, so smaller purchases are viable strategies.

### 4. Buildings List
```python
BUILDINGS = [
    {
        "name": "bar",
        "display_name": "The Local Tavern",
        "type": "bar",
        "char": "µ",
        "seed_range": 1000,
        "threshold": 0.03,
        "hostile_prob": 0.4,
     "can_buy": True,
        "can_sell": False,
        "image": "/assets/tiles/bar.svg",
    "color": "#8b3e3e"
    },
    # ... more buildings
]
```

**Fields:**

| Field | Description | Modifiable? | Notes |
|-------|-------------|-------------|-------|
| `name` | Internal identifier | ? NO | Must match system expectations |
| `display_name` | Player-facing name | ? YES | Make it thematic! |
| `type` | Building category | ? NO | Defines behavior |
| `char` | Console map character | ? NO | ASCII/extended ASCII only |
| `seed_range` | Territory radius | ?? RARE | Spacing between buildings |
| `threshold` | Generation probability | ? NO | Controls building density |
| `hostile_prob` | Enemy encounter chance | ?? RARE | Balance carefully |
| `can_buy` | Supports purchases | ? NO | Type-dependent |
| `can_sell` | Supports selling | ? NO | Type-dependent |
| `image` | Web UI tile path | ? YES | Asset path |
| `color` | Map color hex | ? YES | Visual theming |

**Required Building Types (11 total):**

| Name | Type | Char | Description |
|------|------|------|-------------|
| `bar` | `bar` | `µ` | Tavern/pub with drink menu |
| `inn` | `inn` | `@` | Lodging with room menu |
| `shopweapons` | `shop` | `Æ` | Weapon vendor |
| `shopitems` | `shop` | `?` | Utility/consumable vendor |
| `shoparmor` | `shop` | `¥` | Armor vendor |
| `residencelarge` | `residence` | `Î` | Large housing |
| `residencesmall` | `residence` | `î` | Small housing |
| `businesslarge` | `business` | `Ï` | Large commercial |
| `businesssmall` | `business` | `ï` | Small commercial |
| `hyperway` | `hyperway` | `?` | Fast travel station |
| `other1` | `other1` | `O` | Special building 1 |
| `other2` | `other2` | `0` | Special building 2 |

### 5. Sublocation Map
```python
SUBLOC_MAP = {
    "shop": ["backroom", "storage", "display case"],
  "bar": ["backroom", "storage", "back shelf"],
    "inn": ["common room", "guest room", "dresser"],
    "residence": ["kitchen", "bedroom", "closet"],
    "business": ["reception", "office", "file cabinet"],
    "alley": ["trash can", "vehicle", "hidden alcove"],
    "street": ["market stall", "fountain", "vendor stall"],
}
```

**Purpose:** Maps building types to lists of searchable sublocations that can spawn inside them.

**Rules:**
- Keys must match building `type` values
- Values are lists of sublocation names (defined in `SUBLOCATION_DEFS`)
- Can add thematic variants per city

### 6. Sublocation Definitions
```python
SUBLOCATION_DEFS = {
    "backroom": {
        "mode": "searchable",
   "level_delta": 0,
     "searchable": True,
      "loot_chance": 0.10,
        "prompt": "A small backroom.",
        "money_range": (1, 3)
    },
    # ... more definitions
}
```

**Fields:**

| Field | Type | Description | Typical Values |
|-------|------|-------------|----------------|
| `mode` | `str` | Interaction type | `"searchable"`, `"entered"`, `"vertical"` |
| `level_delta` | `int` | Floor offset | `0` (main floor), `-1` (basement), `1+` (upper) |
| `searchable` | `bool` | Can be searched | `True` |
| `loot_chance` | `float` | Probability of loot | `0.04` (rare) to `0.25` (common) |
| `prompt` | `str` | Description text | Atmospheric 1-2 sentences |
| `money_range` | `tuple` | Money drop range | `(min, max)` in currency |

**Loot Chance Guidelines:**
- **0.04-0.08** - Rare (vault boxes, gun safes)
- **0.09-0.14** - Uncommon (drawers, cabinets)
- **0.15-0.20** - Common (chests, storage)
- **0.21-0.25** - High (shops, safes)

---

## Region-City Matrix

### Complete City List (21 Total)

| Region | Large City | Medium City | Small City |
|--------|------------|-------------|------------|
| **Desert** | Nightveil Spire (Ch 8) | Sunhaven Crossing | The Radpost (Ch 9) |
| **Forest** | Thornwood Vale | Boiling Bubble (Ch 2) | Thornshade Hamlet (Ch 16) |
| **Grassland** | Crosswind Bazaar (Ch 10) | Highsteeple Crossing (Ch 3) | Quantford Hollow (Ch 12) |
| **Mountains** | Gallows Rift (Ch 17) | Ironveil Foundry (Ch 4) | Hollerforge Hollow (Ch 21) |
| **Shallows** | Tidekin Cove (Ch 14) | Brineward Harbor (Ch 5) | Blackwake Bay (Ch 11) |
| **Snow** | Frostgate Spire (Ch 19) | Hailward Hold (Ch 15) | Glacier's Edge |
| **Swamp** | Bayou Nocturne (Ch 20) | The Necropolis (Ch 13) | Mistvale |

### City Theme Examples

#### Desert Cities
**Large (Nightveil Spire):**
- Theme: Neo-noir cyberpunk desert metropolis
- Buildings: "The Local", "Stuff That Does Damage", "The Black Market Guild"
- Drinks: Ale, Stout, Cocktail, Triple Hitter, Absinthe, Elixir
- Vibe: Glass towers, neon lights, sandy streets

**Medium (Sunhaven Crossing):**
- Theme: Trade hub with oasis markets
- Buildings: Merchant-focused, bazaar-style
- Drinks: Desert-themed spirits and tonics

**Small (The Radpost):**
- Theme: Brutal outpost arena (Scalpel's Domain - Ch 9)
- Buildings: Bloodspark Arena, fighter lodges
- Special: Violence-as-entertainment theme

#### Forest Cities
**Large (Thornwood Vale):**
- Theme: Ancient forest canopy city
- Buildings: Treehouse-style architecture
- Natural integration with environment

**Medium (Boiling Bubble - Ch 2):**
- Theme: Witch hamlet with mystical breweries
- Buildings: "The Midnight Kettle", "Mist & Mortar", "Ward & Weave"
- Drinks: Night Brew, Mandrake Cordial, Moon Tea, Philter of Vigor
- Sublocations: Cauldrons, potion racks, hearths, warded chests

**Small (Thornshade Hamlet - Ch 16):**
- Theme: Post-meaning existential village
- Special: Chapter 16 "Path Without Meaning" location

#### Grassland Cities
**Large (Crosswind Bazaar - Ch 10):**
- Theme: Endless festival of forced joy (Revelry's influence)
- Special: Chapter 10 "Human Chaos" - no boss fight, only consequences
- Buildings: Festival-themed, manic atmosphere

**Medium (Highsteeple Crossing - Ch 3):**
- Theme: Trading crossroads settlement
- Standard grassland theming

**Small (Quantford Hollow - Ch 12):**
- Theme: Looping district (Lament's Domain)
- Special: Temporal recursion mechanics
- Buildings: "Library of Contradictions"

#### Mountain Cities
**Large (Gallows Rift - Ch 17):**
- Theme: Rulebound citadel (Paradox & Crux)
- Buildings: "Punishment Engines" dungeon district
- Special: Contradictory rules, recursive logic

**Medium (Ironveil Foundry - Ch 4):**
- Theme: Industrial mining city, Catalyst fracture site
- Special: ACT I finale location

**Small (Hollerforge Hollow - Ch 21):**
- Theme: Reality's Foundry, Dominion's Gauntlet
- Special: ACT VI final encounter location

#### Shallows Cities
**Large (Tidekin Cove - Ch 14):**
- Theme: Rave-state authoritarian island (Pageant & Edict)
- Special: "Perform or Be Removed" enforcement
- Buildings: Neon-lit synchronized crowds

**Medium (Brineward Harbor - Ch 5):**
- Theme: Port city, Riftwaters crossing arrival
- Special: ACT II begins here

**Small (Blackwake Bay - Ch 11):**
- Theme: Pirate tavern frenzy (Rapture & Revelry)
- Special: Peak physical/emotional mania
- Buildings: "Shard Expanse" killing grounds

#### Snow Cities
**Large (Frostgate Spire - Ch 19):**
- Theme: Prophetic spiral city (Cataclysm)
- Buildings: "Spiral of Futures" district
- Special: Systemic collapse, controlled destruction

**Medium (Hailward Hold - Ch 15):**
- Theme: Split-Court District (Stigma)
- Special: Court of Memory vs Court of Reputation
- Buildings: "Hall of Mirrors"

**Small (Glacier's Edge):**
- Theme: Frozen outpost
- Standard snow theming

#### Swamp Cities
**Large (Bayou Nocturne - Ch 20):**
- Theme: Memory Museum (Oracle & Reliquary)
- Buildings: Timeline-preserved exhibits
- Special: Past/present intertwine, destiny collapses

**Medium (The Necropolis - Ch 13):**
- Theme: Identity rot city (Garbage)
- Buildings: "Rift-Lost Quarter", "Identity Nexus"
- Special: Self-loathing made flesh

**Small (Mistvale):**
- Theme: Bog village
- Standard swamp theming

---

## Building Configuration

### Building Density Control

**Threshold System:** Buildings spawn based on RNG rolls against their threshold value.

```python
"threshold": 0.03  # 3% of tiles can be this building
```

**Standard Thresholds:**
- `0.02-0.04` - Very rare (1-2 per city): hyperway, special buildings
- `0.06-0.10` - Rare (3-5 per city): inn, bar
- `0.15-0.35` - Uncommon (8-15 per city): shops
- `0.50-0.75` - Common (20-40 per city): large residences
- `0.90-1.0` - Very common (50+ per city): small residences/businesses

### Seed Range (Territory)

**Purpose:** Prevents same building type from spawning too close together.

```python
"seed_range": 6  # Minimum 6-tile spacing
```

**Standard Ranges:**
- `1000` - Unique (only one per city): shops, bar, inn, hyperway
- `6` - Spread out: large buildings
- `4` - Clustered: small buildings

### Hostile Probability

**Purpose:** Chance of enemy encounter when entering building.

```python
"hostile_prob": 0.4  # 40% chance of combat
```

**Standard Probabilities:**
- `0.00` - Safe zones: inn
- `0.01-0.05` - Very safe: shops
- `0.10-0.25` - Moderate risk: residences, special buildings
- `0.30-0.40` - High risk: bars, hyperways
- `0.50+` - Dangerous: dungeon-adjacent areas

**Design Note:** Bar has high hostile_prob (0.4) because drinks trigger encounters. This makes buying drinks inherently risky.

### Character Codes

**Console Map Representation:**

```
? = impassable terrain
  = open area/road
µ = bar
@ = inn
Æ = weapon shop
? = item shop
¥ = armor shop
Î = large residence
î = small residence
Ï = large business
ï = small business
? = hyperway
O = other1
0 = other2
```

**Requirements:**
- Must be ASCII or extended ASCII
- Must be unique per building type
- Should be visually distinct on console

---

## Sublocation System

### Sublocation Categories

#### Shop Sublocations
```python
"shop": ["backroom", "storage", "display case", "shelf unit", "file cabinet", "vault box"]
```

**Purpose:** Items players can search in weapon/armor/item shops.

**Typical Loot Chances:**
- Backroom: 0.10
- Storage: 0.25
- Display case: 0.13
- Vault box: 0.06 (rare but valuable)

#### Bar Sublocations
```python
"bar": ["backroom", "storage", "back shelf", "coat rack", "lockbox", "display case"]
```

**Purpose:** Searchable areas in taverns.

**Special:** Bar has high hostile_prob, so searching is risky.

#### Inn Sublocations
```python
"inn": ["common room", "guest room", "dresser", "drawer", "coat closet", "back shelf"]
```

**Purpose:** Safe zone searchables.

**Special:** Inn hostile_prob = 0.00, making it safe to explore.

#### Residence Sublocations
```python
"residence": ["kitchen", "bedroom", "closet", "bathroom", "cupboard", "pantry",
          "dresser", "storage chest", "lockbox", "drawer"]
```

**Purpose:** Private homes with varied loot.

**Design Note:** More sublocation types = more variety per building.

#### Business Sublocations
```python
"business": ["reception", "office", "bathroom", "file cabinet", "utility cabinet",
         "storage chest", "vault box"]
```

**Purpose:** Commercial offices and guilds.

**High-value:** Vault boxes (0.06 loot chance, 10-60 money range).

#### Street/Alley Sublocations
```python
"alley": ["trash can", "vehicle", "hidden alcove", "vendor stall", "service hatch",
        "dumpster", "alley crate", "graffiti wall"]

"street": ["market stall", "fountain", "vehicle", "vendor stall", "display case",
  "back shelf", "phone booth", "mailbox", "newsstand", "parking meter"]
```

**Purpose:** Open-world searchables outside buildings.

**Thematic:** Neo-noir urban exploration elements.

### Sublocation Definition Fields

#### Mode Types
- `"searchable"` - Can be searched for loot/money
- `"entered"` - Triggers scene/dialog (not implemented in constants)
- `"vertical"` - Stairs/elevator (handled by tile system)

#### Level Delta
```python
"level_delta": 0  # Main floor
"level_delta": -1 # Basement
"level_delta": 1  # Second floor
```

**Purpose:** Determines which floor the sublocation appears on.

**Current Usage:** All constants files use `0` (main floor only).

#### Searchable Flag
```python
"searchable": True  # Can be searched
```

**Purpose:** Enables/disables search interaction.

**Current Usage:** Always `True` in constants files.

#### Loot Chance Balance

**Formula:** `random.random() < loot_chance` determines if item spawns.

**Loot Tiers:**
```
Ultra Rare:  0.04 - 0.06  (gun safe, vault box)
Rare:        0.08 - 0.12  (lockbox, mirror, coat rack)
Uncommon:    0.13 - 0.17  (drawer, dresser, bedroom)
Common:      0.18 - 0.22  (storage, potion rack, dumpster)
Very Common: 0.23 - 0.25  (file cabinet, storage chest)
```

**Design Principles:**
- Vault-like containers: 0.04-0.06 (high risk, high reward)
- Personal storage: 0.15-0.18 (moderate risk/reward)
- Public areas: 0.08-0.12 (low reward)
- Commercial: 0.20-0.25 (reliable loot)

#### Money Range Scaling

**Format:** `(min, max)` tuple in currency units.

**Typical Ranges by Location Type:**
```
Personal items:  (0, 6)   - Small change
Drawers/shelves: (1, 12)  - Moderate finds
Storage areas:   (2, 20)  - Decent hauls
Lockboxes:       (2, 22)  - Above average
Vaults:          (5, 60)  - Jackpot
Gun safes:       (20, 120) - Major score
```

**Design Note:** Money ranges intentionally overlap with loot chances inversely - rare containers have high money but low chance.

#### Prompt Writing Guidelines

**Format:** 1-2 atmospheric sentences.

**Good Prompts:**
```python
"A battered dresser with one drawer stuck — something rattles inside."
"A graffiti-strewn wall hides a loose brick behind a faded tag."
"A heavy gun safe bolted to the floor; the combination is long lost, but worth trying."
```

**Bad Prompts:**
```python
"You see a dresser."
"There is a wall."
"A safe."
```

**Rules:**
- Use sensory details (sight, sound, touch)
- Imply danger or mystery
- Match city theme
- Keep under 120 characters

---

## Customization Guide

### When to Edit vs Not Edit

#### ? SAFE TO CUSTOMIZE

**Display Names:**
```python
"display_name": "The Midnight Kettle"  # Make it thematic!
```

**City Descriptions:**
```python
CITY_DESCRIPTION = (
    "Customize to match your narrative vision."
)
```

**Drink/Room Names:**
```python
{"id": "mid", "name": "Moon Tea", ...}  # Thematic names encouraged
```

**Money Values (within reason):**
```python
{"id": "economy", "value": 18, ...}  # Keep reasonable progression
```

**Sublocation Prompts:**
```python
"prompt": "Evocative atmospheric text."  # Make it immersive
```

**Colors and Images:**
```python
"color": "#6b3a3a"
"image": "/assets/tiles/bar_witch.svg"
```

#### ? DO NOT MODIFY

**Internal IDs:**
```python
"id": "economy"      # System relies on these
"name": "bar"        # Must match game logic
```

**Building Types:**
```python
"type": "bar"        # Defines behavior
```

**Characters:**
```python
"char": "µ"          # Console map character
```

**Fractions:**
```python
"heal_fraction": 0.75  # Game balance
"hp_fraction": 0.30       # Game balance
```

**Mode:**
```python
"mode": "searchable"  # Defines interaction type
```

#### ?? MODIFY WITH CAUTION

**Thresholds:**
```python
"threshold": 0.03   # Affects city density - test changes
```

**Seed Ranges:**
```python
"seed_range": 6     # Affects building spacing
```

**Hostile Probabilities:**
```python
"hostile_prob": 0.4  # Affects combat frequency - balance carefully
```

**Loot Chances:**
```python
"loot_chance": 0.18  # Affects economy - test changes
```

### Creating Thematic Variants

#### Example: Witch City (Forest Mid)

**Standard:**
```python
BUILDINGS = [
    {"name": "bar", "display_name": "The Local", ...}
]
```

**Themed:**
```python
BUILDINGS = [
    {"name": "bar", "display_name": "The Midnight Kettle", ...}
]
```

**Custom Sublocations:**
```python
SUBLOC_MAP = {
"bar": ["cauldron", "tasting shelf"],  # Instead of generic "backroom"
}

SUBLOCATION_DEFS = {
    "cauldron": {
        "mode": "searchable",
        "loot_chance": 0.16,
     "prompt": "A bubbling cauldron scents the air; something glints beneath.",
        "money_range": (1, 12)
    }
}
```

#### Example: Cyberpunk City (Desert Large)

**Themed Buildings:**
```python
{"name": "shopweapons", "display_name": "Stuff That Does Damage"},
{"name": "other1", "display_name": "The Black Market Guild"},
{"name": "other2", "display_name": "Broker's Hideout"}
```

**Modern Sublocations:**
```python
SUBLOC_MAP = {
    "business": ["computer desk", "gun safe"],
    "street": ["phone booth", "parking meter", "newsstand"]
}
```

### Balancing Economy

#### Money Progression

**Early Game (Levels 1-5):**
- Room costs: 5-20
- Drink costs: 3-20
- Money finds: 0-10 per search

**Mid Game (Levels 6-10):**
- Room costs: 18-60
- Drink costs: 15-80
- Money finds: 2-22 per search

**Late Game (Levels 11+):**
- Room costs: 60-75
- Drink costs: 80-200
- Money finds: 5-120 per search

#### Loot Frequency

**Target:** Player should find loot in ~15-20% of searches on average.

**Calculation:**
```
Average loot chance = ?(loot_chance × spawn_probability) / total_sublocations
```

**Example:**
- 10 sublocations
- 5 with 0.10 loot chance
- 3 with 0.18 loot chance
- 2 with 0.06 loot chance

Average = `(5×0.10 + 3×0.18 + 2×0.06) / 10 = 0.116` (11.6%)

**Adjust:** If average too low, increase loot_chance on common sublocations.

---

## Integration with Story

### Chapter-Specific Cities

#### ACT I (Chapters 1-4)
- **Ch 1**: Starting city (randomized region)
- **Ch 2**: Boiling Bubble (Forest Mid) - `forest/constants_buildings_mid_city.py`
- **Ch 3**: Highsteeple Crossing (Grassland Mid) - `grassland/constants_buildings_mid_city.py`
- **Ch 4**: Ironveil Foundry (Mountains Mid) - `mountains/constants_buildings_mid_city.py`

#### ACT II (Chapters 5-7)
- **Ch 5**: Brineward Harbor (Shallows Mid) - `shallows/constants_buildings_mid_city.py`
- **Ch 6-7**: Regional cities (varies based on regional arcs)

#### ACT III (Chapters 8-13)
- **Ch 8**: Nightveil Spire (Desert Large) - `desert/constants_buildings_large_city.py`
- **Ch 9**: The Radpost (Desert Small) - `desert/constants_buildings_small_city.py`
- **Ch 10**: Crosswind Bazaar (Grassland Large) - `grassland/constants_buildings_large_city.py`
- **Ch 11**: Blackwake Bay (Shallows Small) - `shallows/constants_buildings_small_city.py`
- **Ch 12**: Quantford Hollow (Grassland Small) - `grassland/constants_buildings_small_city.py`
- **Ch 13**: The Necropolis (Swamp Mid) - `swamp/constants_buildings_mid_city.py`

#### ACT IV (Chapters 14-15)
- **Ch 14**: Tidekin Cove (Shallows Large) - `shallows/constants_buildings_large_city.py`
- **Ch 15**: Hailward Hold (Snow Mid) - `snow/constants_buildings_mid_city.py`

#### ACT V (Chapters 16-20)
- **Ch 16**: Thornshade Hamlet (Forest Small) - `forest/constants_buildings_small_city.py`
- **Ch 17**: Gallows Rift (Mountains Large) - `mountains/constants_buildings_large_city.py`
- **Ch 18**: Aurelion Veil (Forest Mid) - `forest/constants_buildings_mid_city.py`
- **Ch 19**: Frostgate Spire (Snow Large) - `snow/constants_buildings_large_city.py`
- **Ch 20**: Bayou Nocturne (Swamp Large) - `swamp/constants_buildings_large_city.py`

#### ACT VI (Chapter 21)
- **Ch 21**: Hollerforge Hollow (Mountains Small) - `mountains/constants_buildings_small_city.py`

### Location Reference System

**Format for Task Events:**
```
region_city_[building_name]
```

**Examples:**
```python
# Chapter 8 - Nightveil Spire (Desert Large)
'location': 'region_city_inn'      # @ The Cozy Inn
'location': 'region_city_bar'      # µ The Local
'location': 'region_city_shopitems' # ? Stuff With Utility

# Chapter 2 - Boiling Bubble (Forest Mid)
'location': 'region_city_inn'      # @ The Sleeping Owl Annex
'location': 'region_city_bar'      # µ The Midnight Kettle
'location': 'region_city_shoparmor' # ¥ Ward & Weave (Charms)
```

**Note:** The `region_city_` prefix resolves to the current chapter's city constants file automatically.

### NPCs and Building Types

**Common NPC Placements:**
- `region_city_inn` - Safe meeting spot (0.00 hostile_prob)
- `region_city_bar` - Shady contacts, rebels
- `region_city_shopitems` - Merchants, traders
- `region_city_shopweapons` - Weapon dealers
- `region_city_shoparmor` - Armor crafters

**Example from Chapter 8:**
```python
{
    'event_type': 'create_npc',
    'params': {
        'npc_id': 'veyla',
'location': 'region_city_inn'  # Safe zone
    }
},
{
    'event_type': 'create_npc',
    'params': {
   'npc_id': 'rusk',
        'location': 'region_city_shoparmor'  # Merchant
 }
}
```

---

## Quick Reference Tables

### Building Type Summary

| Building | Type | Char | Can Buy | Can Sell | Typical Hostile % |
|----------|------|------|---------|----------|-------------------|
| Bar | `bar` | `µ` | ? | ? | 20-40% |
| Inn | `inn` | `@` | ? | ? | 0% |
| Weapon Shop | `shop` | `Æ` | ? | ? | 1-2% |
| Item Shop | `shop` | `?` | ? | ? | 1-3% |
| Armor Shop | `shop` | `¥` | ? | ? | 1-2% |
| Large Residence | `residence` | `Î` | ? | ? | 1-6% |
| Small Residence | `residence` | `î` | ? | ? | 10-12% |
| Large Business | `business` | `Ï` | ? | ? | 1-10% |
| Small Business | `business` | `ï` | ? | ? | 1-12% |
| Hyperway | `hyperway` | `?` | ? | ? | 30% |
| Other 1 | `other1` | `O` | ? | ? | 25% |
| Other 2 | `other2` | `0` | ? | ? | 25% |

### Region Theme Summary

| Region | Aesthetic | Key Features |
|--------|-----------|--------------|
| **Desert** | Neo-noir cyberpunk | Glass towers, neon, sandy streets |
| **Forest** | Mystical/witch | Herbs, potions, ancient trees, lanterns |
| **Grassland** | Festival/trade | Markets, open spaces, wind |
| **Mountains** | Industrial/forge | Stone, metal, mines, foundries |
| **Shallows** | Nautical/pirate | Docks, ships, tide, islands |
| **Snow** | Frozen/prophetic | Ice, prophecy, stillness |
| **Swamp** | Decay/memory | Rot, mud, forgotten things |

### Sublocation Loot Tiers

| Tier | Loot Chance | Money Range | Examples |
|------|-------------|-------------|----------|
| Jackpot | 0.04-0.06 | (20, 120) | Gun safe, vault box |
| High Value | 0.20-0.25 | (5, 40) | File cabinet, storage chest |
| Common | 0.15-0.19 | (2, 20) | Dresser, bedroom, dumpster |
| Low Value | 0.08-0.14 | (0, 12) | Drawer, coat rack, shelf |
| Ultra Rare | 0.04-0.06 | (10, 60) | Warded chest, broken altar |

---

## Version History

- **v1.0** - Initial documentation covering all 21 city constants files
- Future: Will be updated as new regions or city types are added

---

## Contact

For questions or issues with city building constants:
- Reference `game/services/city_builder_service.py` for city generation logic
- Reference `STORY DOCUMENTS FOR AI/README_ACT_EDITING.md` for location references in timelines
- See individual constants files for region-specific themes
- Consult `services/README.md` for shop/inn/bar service integration

---

## Final Notes

**Key Principles:**
1. **Thematic Consistency** - Buildings, drinks, and sublocations should match city theme
2. **Balance Carefully** - Loot chances and money ranges affect game economy
3. **Respect System IDs** - Internal identifiers (`id`, `name`, `type`) must not change
4. **Test Changes** - Threshold and hostile_prob changes should be playtested
5. **Atmospheric Writing** - Sublocation prompts set the mood for each city

**The city constants are world-building tools** - Use them to create memorable, thematic locations that support the narrative cascade!
