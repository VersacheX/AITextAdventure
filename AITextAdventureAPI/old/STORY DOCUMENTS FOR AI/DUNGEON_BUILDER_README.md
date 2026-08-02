# Dungeon Builder Guide

This document outlines how to configure and use the `DungeonBuilder` service to create new dungeons for the game.

## Overview

The dungeon generation process is handled by the `DungeonBuilder` class located in `game.services.dungeon_builder_service.py`. This builder uses a settings dictionary provided by a "dungeon seed" configuration file to procedurally generate a `Dungeon` object.

To create a new dungeon, you must create a new Python file in a relevant location (e.g., `game/region_seeds/main_story/dungeons/`) that defines a `DUNGEON_SETTINGS` dictionary.

## Dungeon Settings

The `DUNGEON_SETTINGS` dictionary is the core of a dungeon's definition. Below is a detailed explanation of each key.

### Core Generation Parameters  

These settings control the fundamental structure and layout of the dungeon.

| Key                              | Type              | Description                                                                                                                            | Example                               |
| -------------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `dungeon_id`                     | `str`             | A unique identifier for the dungeon.                                                                                                   | `'seth_hideout_ch3'`                  |
| `display_name`                   | `str`             | The name of the dungeon as it appears to the player.                                                                                   | `'Seth\'s Hideout'`                   |
| `seed`                           | `int` / `str`     | A seed for the random number generator to ensure the dungeon layout is consistent. Using `abs(hash(dungeon_id))` is a common practice. | `abs(hash('seth_hideout_ch3'))`       |
| `floor_count`                    | `int`             | The number of floors (levels) in the dungeon.                                                                                          | `1`                                   |
| `rooms_per_floor`                | `int`             | The number of rooms to generate on each floor.                                                                                         | `3`                                   |
| `room_size_min_max`              | `Tuple[int, int]` | A tuple defining the minimum and maximum area for each room.                                                                           | `(60, 110)`                           |
| `max_neighbors_per_room`         | `int`             | The maximum number of initial connections a room can have to its neighbors.                                                            | `2`                                   |
| `additional_connection_chance`   | `float`           | A value from `0.0` to `1.0` representing the chance of adding extra corridors between rooms to create a more interconnected layout.    | `0.02`                                |
| `min_max_distance_between_rooms` | `Tuple[int, int]` | A tuple defining the minimum and maximum distance between adjacent rooms.                                                              | `(1, 3)`                              |
| `min_max_corridor_width`         | `Tuple[int, int]` | A tuple defining the minimum and maximum width of the corridors connecting rooms.                                                      | `(3, 7)`                              |

### Visual and Gameplay Parameters

These settings affect the appearance and interactive elements of the dungeon. All six visual keys are **required** — omitting any will cause rendering errors.

| Key                 | Type    | Description                                                                                                                              | Example       |
| ------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `open_area_tile`    | `str`   | The character used to render open, passable areas.                                                                                       | `'░'`         |
| `open_area_color`   | `str`   | Hex color string for the open area tile.                                                                                                 | `'#5a6838'`   |
| `impassable_tile`   | `str`   | The character used to render impassable walls or obstacles.                                                                              | `'¤'`         |
| `impassable_color`  | `str`   | Hex color string for the impassable tile.                                                                                                | `'#1e2410'`   |
| `border_tile`       | `str`   | The character used to render the dungeon border.                                                                                         | `'·'`         |
| `border_color`      | `str`   | Hex color string for the border tile.                                                                                                    | `'#3a4820'`   |
| `impassable_chance` | `float` | A value from `0.0` to `1.0` for the chance that a passable tile will be converted to an impassable one, creating obstacles.             | `0.12`        |
| `visible_distance`  | `int`   | The player's line-of-sight radius in tiles.                                                                                              | `8`           |

### Content Definitions

These settings populate the dungeon with NPCs, items, and hostile creatures.

| Key               | Type                   | Description                                                                                                                                                                                                          | Example                                                  |
| ----------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| `npcs`            | `List[Dict]`           | A list of NPC dictionaries to be placed in the dungeon. Each dictionary needs an `id` and a `location` (`'entrance'`, `'final_chamber'`, or `'treasure_room'`).                                                      | `[{'id': 'seth', 'location': 'final_chamber'}]`          |
| `items`           | `List[Dict]`           | A list of item dictionaries to be placed. Each needs an `id` and a `location`.                                                                                                                                       | `[{'id': 'panacea', 'location': 'final_chamber'}]`       |
| `floor_hostiles`  | `Dict[int, List[str]]` | A dictionary mapping a floor number to a list of hostile `id`s that can be **randomly encountered** on that floor. These `id`s should correspond to entries in `HOSTILE_SEEDS`. Bosses should not be in this list.   | `{1: ['rabid_bear', 'cave_spider']}`                     |
| `hostile_seeds`   | `List[Dict]`           | A list of dictionaries defining the **random hostiles** that can be encountered in the dungeon. Their `id`s are used in `floor_hostiles`. See **Hostile Seed Schema** below for all required fields.                 | `[{'id': 'rabid_bear', 'name': 'Rabid Bear', ...}]`      |
| `boss_mob`        | `Dict`                 | Defines the boss encounter, including its `id`, `name`, and a list of `hostiles` that appear in the fight. The `hostiles` list should contain `id`s defined in `BOSS_HOSTILES`.                                      | `{'id': 'demigorgon_1', 'name': 'Demigorgon', ...}`      |
| `boss_hostiles`   | `List[Dict]`           | A separate list of hostile definitions specifically for the boss encounter. Uses the same schema as `hostile_seeds`. The boss `rarity` should always be `'notfound'`.                                                | `[{'id': 'demigorgon_1', 'name': 'The Demigorgon', ...}]`|

---

## Hostile Seed Schema

Every entry in both `hostile_seeds` and `boss_hostiles` must include **all** of the following fields. Omitting any field will cause runtime errors when the hostile is instantiated.

### Identity & Classification

| Field           | Type        | Description                                                                                  | Example             |
| --------------- | ----------- | -------------------------------------------------------------------------------------------- | ------------------- |
| `id`            | `str`       | Unique identifier for this hostile type.                                                     | `'cave_bat'`        |
| `name`          | `str`       | Display name shown to the player.                                                            | `'Cave Bat'`        |
| `hostile_type`  | `str`       | Category of creature. Common values: `'humanoid'`, `'undead'`, `'beast'`, `'elemental'`, `'construct'`, `'creature'`, `'plant'`, `'aberration'`. | `'beast'` |
| `min_spawn_level` | `int`     | Minimum player level at which this hostile can appear.                                       | `3`                 |
| `role`          | `str`       | Combat role. One of: `'damage'`, `'tank'`, `'hazard'`.                                       | `'damage'`          |
| `rarity`        | `str`       | Spawn rarity. One of: `'common'`, `'uncommon'`, `'rare'`, `'superrare'`, `'notfound'` (bosses only). | `'common'` |

### Rewards

| Field          | Type              | Description                                              | Example          |
| -------------- | ----------------- | -------------------------------------------------------- | ---------------- |
| `base_xp`      | `int`             | Base XP awarded on defeat.                               | `28`             |
| `common_drop`  | `str` / `None`    | Item ID of the common drop. `None` for no common drop.   | `'herb_minor'`   |
| `rare_drop`    | `str` / `None`    | Item ID of the rare drop. `None` for no rare drop.       | `'tome_dex'`     |
| `money_range`  | `Tuple[int, int]` | Min/max gold dropped on defeat.                          | `(5, 18)`        |

### Combat Behaviour

| Field              | Type        | Description                                                                          | Example                      |
| ------------------ | ----------- | ------------------------------------------------------------------------------------ | ---------------------------- |
| `basic_attack`     | `str`       | Flavour description of the hostile's basic attack.                                   | `'wing slash'`               |
| `strong_attack`    | `str`       | Flavour description of the hostile's strong attack.                                  | `'sonic screech'`            |
| `player_abilities` | `List[str]` | List of player ability IDs this hostile can use. Empty list if none.                 | `['dark_skill_lv1_tranq_dart']` |

### Base Stats

| Field     | Type  | Description              |
| --------- | ----- | ------------------------ |
| `base_str` | `int` | Base strength stat.      |
| `base_dex` | `int` | Base dexterity stat.     |
| `base_con` | `int` | Base constitution stat.  |
| `base_int` | `int` | Base intelligence stat.  |
| `base_hp`  | `int` | Base hit point pool.     |
| `base_ap`  | `int` | Base action point pool.  |

### Scaling (per level above `min_spawn_level`)

| Field           | Type  | Description                          |
| --------------- | ----- | ------------------------------------ |
| `str_per_level` | `int` | Strength gained per level.           |
| `dex_per_level` | `int` | Dexterity gained per level.          |
| `con_per_level` | `int` | Constitution gained per level.       |
| `int_per_level` | `int` | Intelligence gained per level.       |

### Elemental Affinities

| Field         | Type        | Description                                                                    | Example                    |
| ------------- | ----------- | ------------------------------------------------------------------------------ | -------------------------- |
| `resistances` | `List[str]` | Elements / damage types this hostile takes reduced damage from.                | `['earth', 'physical']`    |
| `immunities`  | `List[str]` | Status effects or elements this hostile is completely immune to.               | `['sleep', 'stun']`        |
| `weaknesses`  | `List[str]` | Elements / damage types this hostile takes increased damage from.              | `['fire', 'light']`        |

---

## Creating Encounters

### Random Encounters
Random encounters are defined by the `floor_hostiles` dictionary. The `id`s listed for each floor are pulled from the `hostile_seeds` list and can appear randomly as the player explores.

### Boss Encounters
Boss encounters are special, scripted fights and should **not** be included in `floor_hostiles`. A boss is typically set up as an NPC in the `final_chamber`. The game's story or event system will then trigger a specific combat encounter using the `boss_mob` definition.

**This is a critical step**: To make the boss encounter accessible to the player, the boss creature must be placed in the dungeon as an NPC. This is done via the `DUNGEON_NPCS` list. Failing to do this will result in a dungeon where the boss cannot be fought.

To set up a boss:
1.  Define the random monsters in a `HOSTILE_SEEDS` list.
2.  Define the boss creature and any unique minions in a separate `BOSS_HOSTILES` list.
3.  Define the `boss_mob` dictionary, listing the `id`s of the creatures from `BOSS_HOSTILES` that are in the fight.
4.  **Crucially, place the boss as an NPC** in the dungeon using the `npcs` list, usually in the `'final_chamber'`. The `id` must match the NPC from the story event that triggers the fight.
    ```python
    # This places the NPC 'the_demigorgon' in the final room.
    # The player interacts with this NPC to start the boss fight.
    DUNGEON_NPCS = [{'id': 'the_demigorgon', 'location': 'final_chamber'}]
    ```

### From Story Timeline to Dungeon Seed

When building a dungeon based on a story timeline (e.g., `TIMELINE ACT II.mmd`), be aware that the timeline will likely only provide the high-level details. It is the developer's responsibility to fill in the rest.

*   **Boss Definition**: The timeline will typically only specify the main boss NPC (e.g., `create_npc - the_demigorgon`). It will usually **not** define the full `boss_mob` (like minions) or the boss's specific stats and abilities. These must be created in the `BOSS_HOSTILES` list.
*   **Random Hostiles**: The timeline will almost never specify the random monsters for the dungeon floors. You will need to create these and populate the `HOSTILE_SEEDS` and `floor_hostiles` lists.
*   **Hostile Rarity**: As a general guideline, each floor should have a variety of random hostiles, including at least one of each rarity: `common`, `uncommon`, `rare`, and `superrare`. This ensures a balanced and interesting mix of encounters.

## Creating Content for New Dungeons

When creating a new dungeon, you may need to create new items, weapons, armor, and abilities.

*   **Items, Weapons, and Armor**:
    *   The expected level for dungeon content is roughly `Chapter Number * 5`. When creating hostiles and loot, ensure their `min_spawn_level` reflects this.
    *   You can find existing item definitions in `game/constants_items.py` and in the `game/region_seeds/weapons/` and `game/region_seeds/armor/` directories.
    *   If suitable equipment for the dungeon's level does not exist, you should create a new seed file (e.g., `lv36_45.py`) and add the new items there. Remember to import and add them to the main lists in `constants_items.py`.
    *   **Dungeons must be populated with loot.** Ensure the `DUNGEON_ITEMS` list is filled with a variety of items (consumables, equipment, quest items) placed in different locations like `'treasure_room'` and `'final_chamber'` to reward exploration. An empty or sparse item list makes for an unrewarding dungeon.

*   **Hostile Abilities**:
    *   Hostiles can use player abilities or have their own unique ones.
    *   Player abilities are defined in `game/region_seeds/player_abilities/`.
    *   You can create custom, non-player abilities by adding a new definition to an appropriate ability file (e.g., `level_1_abilities.py`) and setting `"non_player_ability": True`.

## Example Configuration File

Here is a complete example of a dungeon seed file, `my_new_dungeon.py`:

```
from typing import Dict, Any

# 1. Define constants for tiles
OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "¤"

# 2. Define content (NPCs, Items, Hostiles)
DUNGEON_NPCS = [{'id': 'some_npc', 'location': 'final_chamber'}]
DUNGEON_ITEMS = [{'id': 'some_item', 'location': 'treasure_room'}]

# Define random hostiles for the dungeon floors
FLOOR_HOSTILES = {1: ['generic_rat', 'big_spider']}
HOSTILE_SEEDS = [
    {
        'id': 'generic_rat',
        'name': 'Generic Rat',
        'hostile_type': 'beast',
        'min_spawn_level': 1,
        'role': 'damage',
        'rarity': 'common',
        # ... other hostile stats
    },
    {
        'id': 'big_spider',
        'name': 'Big Spider',
        'hostile_type': 'insect',
        'min_spawn_level': 2,
        'role': 'hazard',
        'rarity': 'uncommon',
        # ... other hostile stats
    }
]

# 3. Define the boss encounter and its specific hostiles
BOSS_MOB = {
    'id': 'rat_king_boss',
    'name': 'The Rat King',
    'hostiles': ['rat_king'] # The boss creature
}
BOSS_HOSTILES = [
    {
        'id': 'rat_king',
        'name': 'The Rat King',
        'hostile_type': 'beast',
        'min_spawn_level': 5,
        'role': 'damage',
        'rarity': 'notfound', # Bosses are typically not found randomly
        # ... other boss stats
    }
]


# 4. Assemble the main settings dictionary
DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'my_new_dungeon',
    'display_name': 'My New Dungeon',
    'seed': abs(hash('my_new_dungeon')),
    'floor_count': 1,
    'rooms_per_floor': 4,
    'room_size_min_max': (50, 100),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.1,
    'min_max_distance_between_rooms': (2, 5),
    'min_max_corridor_width': (2, 4),
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'impassable_chance': 0.1,
    'visible_distance': 6,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}
```

By following this structure, you can easily create and customize new dungeons for the game.

## Overworld Boss Encounters

Not all boss fights occur inside a dungeon. Some story chapters trigger a `begin_combat` event while the player is in an overworld region or city location, with no `create_dungeon` wrapping the encounter. Because there is no dungeon seed file to house these definitions, they must be registered in `game/region_seeds/world_enemies.py` instead.

**Rules for overworld boss encounters:**

*The boss's `WORLD_BOSS_MOBS` entry must use the **exact same `id`** that is passed to `begin_combat` in the chapter file (e.g., `'stigma_boss_battle_1'`). A mismatched id will cause the fight to fail silently.
*   The hostile definitions used by that boss must exist in `WORLD_HOSTILES` in the same file.
*   The NPC that the player interacts with to trigger the fight is placed with a `create_npc` event in the chapter's `task_acquire_events` — there is no dungeon `npcs` list involved.

**When auditing a chapter for missing world content**, check every `begin_combat` event and ask: does it have a parent `create_dungeon` in its task setup chain? If not, the mob belongs in `world_enemies.py`.

### Known overworld boss encounters (by act and chapter)

| Chapter | Boss Mob ID | Location | Hostile(s) | Combat Type | Notes |
| --- | --- | --- | --- | --- | --- |
| Ch10 - Human Chaos | `festival_rioters_1` | city streets (overworld) | `manic_rioter` x3 | `combat` | First rioter wave. Breaks out directly in the city streets after the crowd surges. No `create_dungeon` or `create_npc` involved. |
| Ch10 - Human Chaos | `festival_rioters_2` | city streets (overworld) | `manic_rioter`, `frenzied_rioter` x2 | `combat` | Second escalating wave. Immediately follows wave 1. |
| Ch10 - Human Chaos | `festival_rioters_3` | city streets (overworld) | `frenzied_rioter`, `festival_berserker` | `combat` | Final wave. Vek takes over the city cleanup after this resolves. |
| Ch14 - Stigma | `stigma_boss_battle_1` | `region_city_bar` (overworld) | `stigma` | `boss_battle` | Stigma placed via `create_npc` in the city bar. Distinct from the generic `stigma_1` entry which is reserved for secondary encounters. |


from typing import Dict, Any, List

# 1. Define tile and color constants
OPEN_AREA_TILE   = '░'
IMPASSABLE_TILE  = '¤'
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR  = '#5a6838'
IMPASSABLE_COLOR = '#1e2410'
BORDER_TILE      = '·'
BORDER_COLOR     = '#3a4820'

# 2. Define content (NPCs, Items, Hostiles)
DUNGEON_NPCS = [{'id': 'some_npc', 'location': 'final_chamber'}]
DUNGEON_ITEMS = [{'id': 'some_item', 'location': 'treasure_room'}]

FLOOR_HOSTILES = {1: ['generic_rat', 'big_spider']}
HOSTILE_SEEDS = [
    {
        'id': 'generic_rat',
        'name': 'Generic Rat',
        'hostile_type': 'beast',
        'min_spawn_level': 1,
        'role': 'damage',
        'rarity': 'common',
        'base_xp': 6,
        'common_drop': 'herb_minor',
        'rare_drop': None,
        'money_range': (1, 5),
        'basic_attack': 'gnaws at exposed skin',
        'strong_attack': 'rabid lunge',
        'player_abilities': [],
        'base_str': 2, 'base_dex': 3, 'base_con': 2, 'base_int': 1,
        'base_hp': 12, 'base_ap': 2,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 1, 'int_per_level': 0,
        'resistances': [],
        'immunities': [],
        'weaknesses': ['fire'],
    },
    {
        'id': 'big_spider',
        'name': 'Big Spider',
        'hostile_type': 'creature',
        'min_spawn_level': 2,
        'role': 'hazard',
        'rarity': 'uncommon',
        'base_xp': 14,
        'common_drop': 'ointment',
        'rare_drop': None,
        'money_range': (2, 8),
        'basic_attack': 'bites with venom-coated fangs',
        'strong_attack': 'web bind',
        'player_abilities': [],
        'base_str': 2, 'base_dex': 5, 'base_con': 3, 'base_int': 1,
        'base_hp': 20, 'base_ap': 2,
        'str_per_level': 0, 'dex_per_level': 2, 'con_per_level': 1, 'int_per_level': 0,
        'resistances': [],
        'immunities': ['poison'],
        'weaknesses': ['fire'],
    },
]

# 3. Define the boss encounter
BOSS_MOB = {
    'id': 'rat_king_boss',
    'name': 'The Rat King',
    'hostiles': ['rat_king'],
}
BOSS_HOSTILES = [
    {
        'id': 'rat_king',
        'name': 'The Rat King',
        'hostile_type': 'beast',
        'min_spawn_level': 5,
        'role': 'damage',
        'rarity': 'notfound',
        'base_xp': 320,
        'common_drop': 'herb_minor',
        'rare_drop': 'tome_str',
        'money_range': (20, 60),
        'basic_attack': 'slams with a sceptre of bound rat-bones',
        'strong_attack': 'rat swarm',
        'player_abilities': [],
        'base_str': 6, 'base_dex': 5, 'base_con': 6, 'base_int': 3,
        'base_hp': 800, 'base_ap': 40,
        'str_per_level': 1, 'dex_per_level': 1, 'con_per_level': 1, 'int_per_level': 0,
        'resistances': [],
        'immunities': ['poison'],
        'weaknesses': ['fire', 'light'],
    },
]

# 4. Assemble the main settings dictionary
DUNGEON_SETTINGS: Dict[str, Any] = {
    'dungeon_id': 'my_new_dungeon',
    'display_name': 'My New Dungeon',
    'seed': abs(hash('my_new_dungeon')),
    'floor_count': 1,
    'rooms_per_floor': 3,
    'room_size_min_max': (50, 90),
    'max_neighbors_per_room': 2,
    'additional_connection_chance': 0.05,
    'min_max_distance_between_rooms': (1, 3),
    'min_max_corridor_width': (2, 4),
    'open_area_tile': OPEN_AREA_TILE,
    'impassable_tile': IMPASSABLE_TILE,
    'open_area_color': OPEN_AREA_COLOR,
    'impassable_color': IMPASSABLE_COLOR,
    'border_tile': BORDER_TILE,
    'border_color': BORDER_COLOR,
    'impassable_chance': IMPASSABLE_CHANCE,
    'visible_distance': 6,
    'npcs': DUNGEON_NPCS,
    'items': DUNGEON_ITEMS,
    'floor_hostiles': FLOOR_HOSTILES,
    'hostile_seeds': HOSTILE_SEEDS,
    'boss_mob': BOSS_MOB,
    'boss_hostiles': BOSS_HOSTILES,
}



By following this structure, you can easily create and customize new dungeons for the game.

## Overworld Boss Encounters

Not all boss fights occur inside a dungeon. Some story chapters trigger a `begin_combat` event while the player is in an overworld region or city location, with no `create_dungeon` wrapping the encounter. Because there is no dungeon seed file to house these definitions, they must be registered in `game/region_seeds/world_enemies.py` instead.

**Rules for overworld boss encounters:**

*   The boss's `WORLD_BOSS_MOBS` entry must use the **exact same `id`** that is passed to `begin_combat` in the chapter file (e.g., `'stigma_boss_battle_1'`). A mismatched id will cause the fight to fail silently.
*   The hostile definitions used by that boss must exist in `WORLD_HOSTILES` in the same file.
*   The NPC that the player interacts with to trigger the fight is placed with a `create_npc` event in the chapter's `task_acquire_events` — there is no dungeon `npcs` list involved.

**When auditing a chapter for missing world content**, check every `begin_combat` event and ask: does it have a parent `create_dungeon` in its task setup chain? If not, the mob belongs in `world_enemies.py`.

### Known overworld boss encounters (by act and chapter)

| Chapter | Boss Mob ID | Location | Hostile(s) | Combat Type | Notes |
| --- | --- | --- | --- | --- | --- |
| Ch10 - Human Chaos | `festival_rioters_1` | city streets (overworld) | `manic_rioter` x3 | `combat` | First rioter wave. Breaks out directly in the city streets after the crowd surges. No `create_dungeon` or `create_npc` involved. |
| Ch10 - Human Chaos | `festival_rioters_2` | city streets (overworld) | `manic_rioter`, `frenzied_rioter` x2 | `combat` | Second escalating wave. Immediately follows wave 1. |
| Ch10 - Human Chaos | `festival_rioters_3` | city streets (overworld) | `frenzied_rioter`, `festival_berserker` | `combat` | Final wave. Vek takes over the city cleanup after this resolves. |
| Ch14 - Stigma | `stigma_boss_battle_1` | `region_city_bar` (overworld) | `stigma` | `boss_battle` | Stigma placed via `create_npc` in the city bar. Distinct from the generic `stigma_1` entry which is reserved for secondary encounters. |