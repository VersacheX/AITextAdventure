# Game Services Reference

## Overview

This directory contains service modules that handle game mechanics, player interactions, shop systems, combat encounters, and task/event execution for AI Text Adventure. These services provide the business logic layer between game objects and the user interface.

---

## Table of Contents

1. [Shop Services](#shop-services)
2. [Player Services](#player-services)
3. [Task & Event System](#task--event-system)
4. [Loot Generation](#loot-generation)
5. [Utility Services](#utility-services)
6. [Common Patterns](#common-patterns)
7. [Integration Guide](#integration-guide)

---

## Shop Services

### `armor_shop_service.py`

**Purpose**: Handles armor shop inventory and transactions.

#### Constants

```python
SELL_RATIO = 0.5  # Player receives 50% of item value when selling
```

#### Key Functions

##### `get_stock(player_level, current_region, count=8)`
```python
from services.armor_shop_service import get_stock

stock = get_stock(
    player_level=10,
    current_region=forest_region,
    count=8
)
# Returns: List[Armor]
```

**Algorithm:**
1. Iterate through `constants.ARMOR_SEEDS` (dict of slot ? list of seeds)
2. Filter seeds where `min_spawn_level <= player_level`
3. Sort by `value` descending (highest value first)
4. Instantiate `Armor` objects for each seed
5. Return full list (ignores `count` parameter intentionally)

**Armor Slots:**
- `head` ? `ArmorType.HEAD`
- `body` ? `ArmorType.BODY`
- `arms` ? `ArmorType.ARMS`
- `legs` ? `ArmorType.LEGS`

##### `buy(player_game, item)`
```python
result = armor_shop_service.buy(
    player_game=pg,
    item=iron_helmet
)
# Returns: {'success': bool, 'error': str?, 'item': Armor?}
```

**Process:**
1. Check `player_game.money >= item.value`
2. Attempt `player_game.pick_up_item(item)` (inventory check)
3. Deduct `item.value` from `player_game.money`
4. Return success/error result

**Error Codes:**
- `insufficient_funds` - Not enough money
- `inventory_full` - No inventory space

##### `sell(player_game, item)`
```python
result = armor_shop_service.sell(
    player_game=pg,
    item=old_helmet
)
# Returns: {'success': bool, 'error': str?, 'price': int?, 'item': Item?}
```

**Process:**
1. Validate item is `Item` instance
2. Calculate `sell_price = int(item.value * SELL_RATIO)`
3. Add `sell_price` to `player_game.money`
4. Remove item via `player_game.remove_single_item_unit(item)`

---

### `weapon_shop_service.py`

**Purpose**: Handles weapon shop inventory and transactions.

#### Key Functions

##### `get_stock(player_level, current_region, count=8)`
```python
from services.weapon_shop_service import get_stock

stock = get_stock(
    player_level=10,
    current_region=desert_region,
    count=8
)
# Returns: List[Weapon]
```

**Algorithm:**
1. Filter `constants.WEAPON_SEEDS` where `min_spawn_level <= player_level`
2. Sort by `value` descending
3. Instantiate `Weapon` objects
4. Return full list

##### `buy(player_game, item)` & `sell(player_game, item)`
Same as `armor_shop_service` (identical implementations).

---

### `utility_shop_service.py`

**Purpose**: Handles utility/consumable item shop.

#### Key Functions

##### `get_stock(player_level, current_region, count=10)`
```python
from services.utility_shop_service import get_stock

stock = get_stock(
    player_level=10,
    current_region=mountains_region,
    count=10
)
# Returns: List[UtilityItem]
```

**Algorithm:**
1. Filter `constants.UTILITY_ITEM_SEEDS` where `min_spawn_level <= player_level`
2. Sort by `value` descending
3. Instantiate `UtilityItem` objects
4. Return full list (ignores `count` intentionally)

##### `buy(player_game, item)` & `sell(player_game, item)`
Same as `armor_shop_service`.

---

### `bar_service.py`

**Purpose**: Handles bar drink menu and consumption (instant HP/AP restore).

#### Key Functions

##### `get_stock(player_level, player_game, current_region)`
```python
from services.bar_service import get_stock

drinks = get_stock(
    player_level=10,
    player_game=pg,
    current_region=city
)
# Returns: List[Dict[str, Any]]
```

**Algorithm:**
1. Determine region-specific drink menu:
   - Format: `{REGION_NAME}_{CITY_NAME}_DRINK_MENU` or `{REGION_NAME}_DRINK_MENU`
   - Example: `constants.FOREST_SMALL_CITY_DRINK_MENU`
2. Filter drinks where `min_level <= player_level`
3. Return drink dictionaries

**Drink Dictionary Structure:**
```python
{
    "id": "ale",
"name": "Ale",
    "value": 10,      # Cost in money
    "hp_fraction": 0.10,  # Restore 10% max HP
"ap_fraction": 0.0,   # Restore 0% AP
 "min_level": 1
}
```

**Example Drink Progression:**
- Ale (10g, 10% HP, level 1)
- Stout (25g, 20% HP, level 2)
- Cocktail (50g, 30% HP, level 3)
- Porter (65g, 40% HP, level 4)
- Rum (80g, 50% HP, level 5)
- Brandy (110g, 60% HP, level 6)
- Whiskey (120g, 70% HP, level 7)
- Cognac (130g, 80% HP, level 8)
- Absinthe (140g, 90% HP, level 9)
- Elixir (200g, 100% HP + 30% AP, level 10)

##### `buy(player_game, drink)`
```python
result = bar_service.buy(
    player_game=pg,
    drink=elixir_dict
)
# Returns: {'success': bool, 'error': str?, 'healed': int, 'ap_restored': int, 'drink': dict}
```

**Process:**
1. Check `player_game.money >= drink['value']`
2. Deduct cost from `player_game.money`
3. For each character in `player_game.characters`:
   - Calculate `hp_amt = max(0, int(player.max_hp * hp_fraction))`
   - Heal character via `player.heal(hp_amt)`
   - Calculate `ap_amt = max(0, int(player.max_ap * ap_fraction))`
   - Restore AP: `player.current_ap = min(player.max_ap, current_ap + ap_amt)`
4. Return result with heal amounts

**Error Codes:**
- `invalid_drink` - Drink parameter is None
- `insufficient_funds` - Not enough money

---

### `inn_service.py`

**Purpose**: Handles inn room rental for resting (HP/AP restoration).

#### Key Functions

##### `get_stock(player_level, player_game, current_region)`
```python
from services.inn_service import get_stock

rooms = get_stock(
    player_level=10,
    player_game=pg,
    current_region=city
)
# Returns: List[Dict[str, Any]]
```

**Algorithm:**
1. Determine region-specific room menu:
   - Format: `{REGION_NAME}_{CITY_NAME}_ROOM_MENU` or `{REGION_NAME}_ROOM_MENU`
2. Filter rooms where `min_level <= player_level`
3. Return room dictionaries

**Room Dictionary Structure:**
```python
{
    "id": "bench",
    "name": "Bench",
    "value": 5,    # Cost
    "heal_fraction": 0.25, # Restore 25% HP/AP
    "min_level": 1
}
```

**Example Room Progression:**
- Bench (5g, 25% restore)
- Room (20g, 75% restore)
- Private Suite (75g, 100% restore)

##### `buy(player_game, room)`
```python
result = inn_service.buy(
    player_game=pg,
    room=private_suite_dict
)
# Returns: {'success': bool, 'error': str?, 'room': dict, 'healed': int, 'ap_restored': int}
```

**Process:**
1. Validate room is not None
2. Check `player_game.money >= room['value']`
3. Deduct cost
4. For each character:
   - Heal HP: `max(1, int(max_hp * heal_fraction))`
   - Restore AP: `max(1, int(max_ap * heal_fraction))`
5. Return result with restoration amounts

**Error Codes:**
- `invalid_room` - Room parameter is None
- `insufficient_funds` - Not enough money

---

## Player Services

### `player_movement_service.py`

**Purpose**: Handles player movement, floor navigation, sublocation interaction, and random encounters.

#### Key Functions

##### `get_allowed_moves(region, player_game)`
```python
from services.player_movement_service import get_allowed_moves

allowed = get_allowed_moves(
    region=current_region,
  player_game=pg
)
# Returns: Dict[str, str]  # {'w': 'north', 'a': 'west', ...}
```

**Algorithm:**
1. Get current tile: `region.get_tile(player_game.x, player_game.y)`
2. Check `player_game.inside` status
3. For each direction in `DIRECTIONAL_MAPPING` (w/a/s/d):
   - Calculate target position `(nx, ny)`
   - **If inside building:**
     - Only allow exit via entrances on main floor (`z == 0`)
  - Check `current_tile.entrances` contains direction
   - **If outside:**
     - Resolve target region/city via `get_region_and_active_area_for_position()`
     - Get target tile
     - Check entrance compatibility (opposite direction must be in target entrances)
     - Check passability:
       - Impassable tiles blocked unless `inside_aircraft`
       - Ocean blocked unless `allow_ocean_flight` enabled
       - Buildings blocked when `inside_aircraft`
4. Return dict of allowed move keys

**Direction Mapping:**
```python
DIRECTIONAL_MAPPING = {
  'w': (0, -1, 'north'),
    'a': (-1, 0, 'west'),
    's': (0, 1, 'south'),
  'd': (1, 0, 'east')
}
```

##### `handle_movement_key(cmd, region, allowed_moves, radius, player_game)`
```python
moved = handle_movement_key(
    cmd='w',
    region=current_region,
    allowed_moves={'w': 'north', 'd': 'east'},
    radius=5,
    player_game=pg
)
# Returns: bool (True if command handled)
```

**Process:**
1. Validate command is 'w', 'a', 's', or 'd'
2. Check command in `allowed_moves`
3. Calculate target position
4. Resolve active area for target
5. **If exiting building:**
   - Only allowed from main floor (`z == 0`)
- Call `player_game.exit()`
6. **If entering building:**
   - Check entrance compatibility
   - Call `player_game.enter(1)` (enter floor 1)
7. **Normal move:**
   - Update position via `player_game.set_position(nx, ny)`
   - Call `player_game.exit()` to ensure outdoor state
8. Return True if handled

##### `get_floor_options(region, player_game)`
```python
can_up, can_down = get_floor_options(
    region=current_region,
    player_game=pg
)
# Returns: (bool, bool)
```

**Algorithm:**
1. Check `player_game.inside` (return `(False, False)` if not inside)
2. Get current tile and floor count
3. **Can go up:**
   - If `player_game.z < (floors - 1)`
4. **Can go down:**
   - If `player_game.z > 0` (above ground floor)
   - OR `player_game.z == 0` and `tile.has_basement`
5. Return tuple

##### `handle_floor_action(cmd, region, pg)`
```python
handled = handle_floor_action(
    cmd='u',
    region=current_region,
  pg=player_game
)
# Returns: bool
```

**Commands:**
- `'u'` - Go up one floor
- `'j'` - Go down one floor

**Process:**
1. Validate inside building
2. **Up:**
   - Check `z + 1 < floors`
   - Increment `pg.z`
3. **Down:**
   - If `z > 0`: Decrement `pg.z`
   - If `z == 0` and `has_basement`: Set `pg.z = -1`
4. Return True if handled

##### `select_sublocation(cmd, sl, player_game)`
```python
handled, name, prompt, item, money = select_sublocation(
    cmd='1',
    sl=sublocation_list,
player_game=pg
)
# Returns: (bool, str?, str?, Item?, int?)
```

**Sublocation Modes:**
- `'entered'` - Enter sublocation (blocked if not on main floor inside building)
- `'vertical'` - Vertical transition (blocked if not on main floor)
- `'searchable'` - Search for loot/money

**Algorithm:**
1. Validate command is numeric
2. Validate selection index within range
3. Get chosen sublocation dict
4. Check mode restrictions (prevent entry/exit from non-main floors)
5. Return results based on mode:
   - **entered/vertical:** `(True, name, enter_prompt, None, None)`
   - **searchable:** `(True, name, search_prompt, item, money)`

##### `check_for_random_mob_encounter(player_game, region_key, force_combat=False)`
```python
from services.player_movement_service import check_for_random_mob_encounter

mobs = check_for_random_mob_encounter(
    player_game=pg,
    region_key='forest',
  force_combat=False
)
# Returns: List[RandomHostile]
```

**Algorithm:**
1. 8% chance of encounter (or 100% if `force_combat=True`)
2. Generate 3 random mobs via `generate_random_mob()`
3. Scale to `player_game.get_max_character_level()`
4. Return mob list (empty list if no encounter)

---

### `city_service.py`

**Purpose**: Utility functions for city-region relationships.

#### Key Functions

##### `get_city_parent_region(city, player_game)`
```python
from services.city_service import get_city_parent_region

parent = get_city_parent_region(
    city=my_city,
    player_game=pg
)
# Returns: City? (parent region or None)
```

**Algorithm:**
1. Iterate `player_game.regions`
2. For each region, check if `region.child_city == city`
3. Return matching region or None

**Use Case:** Find the wilderness region that contains a given city.

---

## Task & Event System

### `task_completion_service.py`

**Purpose**: Executes task acquisition and completion events, orchestrating story progression.

#### Key Functions

##### `execute_acquire_event(event, player_game, parent_task)`
```python
from services.task_completion_service import execute_acquire_event

result = execute_acquire_event(
    event=task_event,
    player_game=pg,
    parent_task=current_task
)
```

**Purpose:** Execute events when a task is acquired (e.g., spawn NPC, create dungeon).

##### `execute_complete_event(event, player_game, parent_task)`
```python
result = execute_complete_event(
    event=completion_event,
    player_game=pg,
    parent_task=current_task
)
```

**Purpose:** Execute events when a task is completed (e.g., award item, trigger dialog).

##### `handle_task_event(event, player_game, parent_task)`
```python
result = handle_task_event(
    event=event_dict_or_object,
    player_game=pg,
    parent_task=task
)
```

**Central dispatcher for all task event types.**

#### Supported Event Types

##### NPC Events

###### `CREATE_NPC`
```python
{
    'event_type': 'create_npc',
    'params': {
   'npc_id': 'nia',
        'location': 'region_bar'  # or 'region_city_inn', 'city_number_2_region_open_area', etc.
    }
}
```

**Algorithm:**
1. Resolve `npc_id` (supports `'final_character'` ? random available character)
2. Find NPC seed in `constants.NPCS`
3. Parse location:
   - `'region_'` ? Use parent region
   - `'region_city_'` ? Use child city
   - `'city_number_X_'` ? Use specific city by index
   - `'{region_type}_{city_type}_'` ? Find by region/city name
4. Find building coords via `find_coords_of_random_building_of_type()`
5. Create `NPC` instance with position
6. Add to `player_game.npcs`

###### `SHOW_NPC`
```python
{
  'event_type': 'show_npc',
    'params': {
        'npc_id': 'seth',
        'location': 'region_city_bar'
    }
}
```

**Algorithm:**
1. Find NPC in `player_game.npcs` by ID
2. Parse location (same logic as CREATE_NPC)
3. Update `npc.position` to new location
4. Return NPC or error if not found

###### `HIDE_NPC`
```python
{
    'event_type': 'hide_npc',
    'params': {
        'npc_id': 'kirn'
    }
}
```

**Algorithm:**
1. Find NPC by ID (supports `'pending_character'` and `'final_character'` aliases)
2. Call `player_game.hide_npc(npc)` (sets `position = None`)

###### `SET_NPC_STANDING_TEXT`
```python
{
    'event_type': 'set_npc_standing_text',
    'params': {
        'npc_id': 'velka',
        'standing_text': [
            "The map shows strange energy patterns.",
            "Something is disturbing the ley lines."
  ]
    }
}
```

**Algorithm:**
1. Find NPC by ID
2. Set `npc.standing_text = params['standing_text']`

###### `SET_NPC_MET`
```python
{
    'event_type': 'set_npc_met',
    'params': {
     'npc_id': 'astra_wynn'
    }
}
```

**Algorithm:**
1. Resolve NPC ID (supports aliases)
2. Call `player_game.set_npc_met(npc_id)`

##### Dialog Events

###### `INITIATE_DIALOG`
```python
{
 'event_type': 'initiate_dialog',
    'params': {
        'npc_id': 'ripple',  # or None for narration
        'dialog_id': 'ripple_intro'
    }
}
```

**Algorithm:**
1. Resolve NPC ID (supports aliases)
2. Find dialog in `constants.NPC_DIALOG` matching `(npc_id, dialog_id)`
3. Find NPC name from `constants.NPCS`
4. Mark NPC as met via `player_game.set_npc_met()`
5. Add dialog lines to `player_game.info_dialogs` via `add_info_dialog_line()`

**Narration:** If `npc_id = None`, displays as narrative text.

###### `INITIATE_CHARACTER_DIALOG`
```python
{
 'event_type': 'initiate_character_dialog',
    'params': {
    'npc_id': 'magic',  # player character ID
        'dialog_id': 'magic_ch5_after_kirn'
    }
}
```

**Algorithm:**
1. Same as INITIATE_DIALOG but adds lines via `add_character_dialog_lines()` instead

**Use Case:** Player character reactions/commentary.

##### Item Events

###### `AWARD_ITEM`
```python
{
    'event_type': 'award_item',
 'params': {
        'item_id': 'tracking_map'
    }
}
```

**Algorithm:**
1. Instantiate item via `instantiate_item_from_id()`
2. Add to inventory via `player_game.pick_up_item(item)`
3. Add info dialog: `"Acquired item: {item.name}"`

###### `REMOVE_ITEM`
```python
{
    'event_type': 'remove_item',
    'params': {
        'item_id': 'stormglass_ember'
    }
}
```

**Algorithm:**
1. Call `player_game.remove_single_item_unit_by_id(item_id)`

##### Money Events

###### `AWARD_MONEY`
```python
{
    'event_type': 'award_money',
    'params': {
  'amount': 100
    }
}
```

**Algorithm:**
1. Call `player_game.add_money(amount)`
2. Add info dialog: `"Acquired money: {amount}"`

##### Dungeon Events

###### `CREATE_DUNGEON`
```python
{
    'event_type': 'create_dungeon',
    'params': {
        'dungeon_id': 'rokhuld_lair',
     'location': 'region_open_area'  # or 'city_number_3_region_open_area'
 }
}
```

**Algorithm:**
1. Find dungeon seed in `constants.DUNGEON_SETTINGS`
2. Build dungeon via `dungeon_builder_service.build_dungeon()`
3. Resolve location region (same logic as NPC location parsing)
4. Find random position via `region.find_random_dungeon_position()`
5. Set `dungeon.position` and add to `player_game.dungeons`

###### `SET_PLAYER_IN_DUNGEON`
```python
{
    'event_type': 'set_player_in_dungeon',
    'params': {
        'dungeon_id': 'rift_dungeon_outskirts',
    'location': 'entrance'  # or 'final_chamber', 'treasure_room', 'corridor'
    }
}
```

**Algorithm:**
1. Find dungeon by ID
2. Convert location string to `DungeonTileType` enum
3. Call `player_game.place_player_in_dungeon_at_location(dungeon_id, location_type)`

###### `REMOVE_PLAYER_FROM_DUNGEON`
```python
{
 'event_type': 'remove_player_from_dungeon',
    'params': {
        'dungeon_id': 'rift_dungeon_outskirts'
    }
}
```

**Algorithm:**
1. Call `player_game.remove_player_from_dungeon(dungeon_id)`

###### `LOCK_DUNGEON` / `UNLOCK_DUNGEON`
```python
{
    'event_type': 'lock_dungeon',
    'params': {
   'dungeon_id': 'seth_hideout'
    }
}
```

**Algorithm:**
1. Call `player_game.lock_dungeon_by_id(dungeon_id)` or `unlock_dungeon_by_id()`

###### `SET_DUNGEON_LOCKED_TEXT`
```python
{
    'event_type': 'set_dungeon_locked_text',
    'params': {
      'dungeon_id': 'ancient_vault',
        'locked_text': "The door is sealed with ancient runes."
    }
}
```

**Algorithm:**
1. Call `player_game.set_dungeon_locked_text_by_id(dungeon_id, locked_text)`

###### `DUNGEON_ADD_TREASURE`
```python
{
    'event_type': 'dungeon_add_treasure',
    'params': {
        'dungeon_id': 'seth_hideout',
        'item_id': 'ornate_bracers',
'location': 'final_chamber'
    }
}
```

**Algorithm:**
1. Find dungeon by ID
2. Instantiate item via `instantiate_item_from_id()`
3. Convert location to `DungeonTileType`
4. Call `dungeon.place_entity_at_location(item, location_type)`

###### `DUNGEON_ADD_NPC`
```python
{
    'event_type': 'dungeon_add_npc',
    'params': {
      'dungeon_id': 'seth_hideout',
        'npc_id': 'seth',
 'location': 'final_chamber'
    }
}
```

**Algorithm:**
1. Find dungeon by ID
2. Resolve NPC ID (supports `'final_character'` alias)
3. Create entity dict: `{'type': 'npc', 'npc_id': npc_id}`
4. Call `dungeon.place_entity_at_location(entity, location_type)`

##### Combat Events

###### `BEGIN_COMBAT`
```python
{
    'event_type': 'begin_combat',
    'params': {
        'boss_mob_id': 'serene_1',
        'combat_type': 'boss_battle'
    }
}
```

**Algorithm:**
1. Extract `boss_mob_id`
2. Call `player_game.set_pending_fight_mob(boss_mob_id)`

**Note:** Combat resolution happens in game loop after event execution.

##### Task Events

###### `AWARD_TASK`
```python
{
    'event_type': 'award_task',
    'params': {
        'task_id': 'main_story_ch5_meet_velka'
    }
}
```

**Algorithm:**
1. Find task seed in `constants.TASKS`
2. Build task via `build_task_from_seed(seed, parent_region)`
3. Call `player_game.acquire_task(new_task)`

##### Character Events

###### `CHARACTER_JOIN`
```python
{
    'event_type': 'character_join',
    'params': {
        'character_id': 'bragg'
    }
}
```

**Algorithm:**
1. Find character seed in `constants.ATTAINABLE_PLAYER_CHARACTERS`
2. Generate player via `generate_player_from_attainable_character_seed()`
3. Add to `player_game.characters`

###### `PLAYER_CHARACTER_JOIN`
```python
{
  'event_type': 'player_character_join',
    'params': {
        'dialog_id': 'join_dialog',
        'is_final_character': True  # or False
    }
}
```

**Algorithm:**
1. If `is_final_character`: Call `player_game.add_final_character(dialog_id)`
2. Else: Call `player_game.add_random_player_character(dialog_id)`

###### `ADD_PENDING_CHARACTER`
```python
{
    'event_type': 'add_pending_character'
}
```

**Algorithm:**
1. Call `player_game.add_pending_character()`

###### `CREATE_CHARACTER_NPC`
```python
{
    'event_type': 'create_character_npc'
}
```

**Algorithm:**
1. Resolve position (same as CREATE_NPC)
2. Call `player_game.add_character_npc(position)` (randomly selects from available characters)

##### Airship Events

###### `SET_AIRCRAFT`
```python
{
    'event_type': 'set_aircraft',
    'params': {
        'location': 'city_number_3_region_open_area'
    }
}
```

**Algorithm:**
1. Parse location (same logic as NPC locations)
2. Find tile coords via `find_coords_of_random_tile_of_type()`
3. Call `player_game.set_aircraft_location(pos)`

###### `CAN_AIRCRAFT_FLY`
```python
{
    'event_type': 'can_aircraft_fly',
    'params': {
        'can_fly': True  # or False
    }
}
```

**Algorithm:**
1. Call `player_game.set_aircraft_flyable(can_fly)`

###### `ALLOW_OCEAN_FLIGHT`
```python
{
    'event_type': 'allow_ocean_flight'
}
```

**Algorithm:**
1. Call `player_game.allow_ocean_flight()`

##### Progression Events

###### `ADVANCE_CHAPTER`
```python
{
    'event_type': 'advance_chapter'
}
```

**Algorithm:**
1. Call `player_game.advance_chapter()`

**Note:** This triggers the next chapter's initial task.

###### `COMPLETE_INTRO_STORY`
```python
{
    'event_type': 'complete_intro_story'
}
```

**Algorithm:**
1. Call `player_game.complete_intro_story()`

**Note:** Gates progression to regional content (Act II).

###### `COMPLETE_REGION_QUEST`
```python
{
    'event_type': 'complete_region_quest',
    'params': {
    'region_id': 'mountains'
    }
}
```

**Algorithm:**
1. Call `player_game.complete_region_quest(region_id)`

**Note:** Contributes to airship unlock requirement (7 regional heroes).

---

## Loot Generation

### `random_loot_service.py`

**Purpose**: Procedurally generates loot drops for sublocations based on player level and rarity weights.

#### Key Functions

##### `generate_loot_for_sublocation(subloc, player_level=1, rng=None)`
```python
from services.random_loot_service import generate_loot_for_sublocation

item = generate_loot_for_sublocation(
    subloc=sublocation_dict,
    player_level=10,
    rng=random.Random(seed)
)
# Returns: Item? (Weapon, Armor, UtilityItem, or SpecialItem)
```

**Algorithm:**
1. Flatten all item seeds via `_flatten_all_seeds(player_level)`
2. Filter seeds by level range: `player_level ± 4`
3. Weight seeds by rarity using `RarityDefaultWeights`:
   - Common: 1.0
   - Uncommon: 0.5
   - Rare: 0.25
   - Epic: 0.1
   - Legendary: 0.05
4. Choose seed via weighted random selection
5. Instantiate item via `_create_item_from_seed()`
6. Set `item.min_spawn_level` and `item.rarity` from seed

**Seed Structure:**
```python
{
    'id': 'iron_sword',
    'name': 'Iron Sword',
  'min_spawn_level': 5,
    'rarity': 'uncommon',  # or 'common', 'rare', 'epic', 'legendary'
'spawn_weight': 0.6,   # Optional override (defaults to rarity weight)
    'value': 50,
    # ... other item-specific fields
    '_seed_type': 'weapon',  # Added by _flatten_all_seeds
    '_slot': 'head'          # For armor only
}
```

#### Internal Helpers

##### `_flatten_all_seeds(player_level)`
```python
seeds = _flatten_all_seeds(player_level=10)
# Returns: List[Dict[str, Any]]
```

**Algorithm:**
1. Calculate level range: `(max(1, level - 4), level + 4)`
2. Adjust max range if exceeds item type max level
3. Collect seeds from:
   - `constants.WEAPON_SEEDS` ? `'_seed_type': 'weapon'`
   - `constants.ARMOR_SEEDS` ? `'_seed_type': 'armor', '_slot': slot`
   - `constants.UTILITY_ITEM_SEEDS` ? `'_seed_type': 'utility'`
   - `constants.SPECIAL_ITEM_SEEDS` ? `'_seed_type': 'special'`
4. Return combined list

##### `_seed_weight(seed)`
```python
weight = _seed_weight(seed_dict)
# Returns: float
```

**Algorithm:**
1. If `seed['spawn_weight']` exists: Return explicit weight
2. Else: Return `RarityDefaultWeights[seed['rarity']]`

##### `_choose_seed_by_weight(candidates, rng)`
```python
seed = _choose_seed_by_weight(
    candidates=seed_list,
    rng=random.Random(seed)
)
# Returns: Dict[str, Any]?
```

**Algorithm:**
1. Compute weight for each candidate
2. Normalize weights to sum to 1.0
3. Use `random.choices()` with weights
4. Return chosen seed or None if no valid weights

##### `_create_item_from_seed(seed)`
```python
item = _create_item_from_seed(seed_dict)
# Returns: Item
```

**Dispatch by `_seed_type`:**
- `'weapon'` ? `_instantiate_weapon(seed)`
- `'armor'` ? `_instantiate_armor(seed, slot)`
- `'utility'` ? `_instantiate_utility(seed)`
- `'special'` ? `_instantiate_special(seed)`

---

## Utility Services

### Location Parsing

**Common pattern used across services:**

#### Location String Format

```python
# Region formats:
'region_bar'         # Current region bar
'region_city_inn'# Current region's child city inn
'region_open_area'          # Current region open area

# Numbered city formats:
'city_number_2_region_city_bar'       # 2nd city's bar
'city_number_3_region_open_area'      # 3rd city's region open area

# Named region/city formats:
'forest_large_city_region_city_inn'   # Forest region's large city inn
'desert_mid_city_region_bar' # Desert region's mid city (region area) bar
```

#### Location Resolution Algorithm

```python
def _get_npc_seed_location(params, parent_task, player_game):
    location_str = params['location']
    
    # Parse city_number_ prefix
    if 'city_number_' in location_str:
        parts = location_str.split('_')
        city_number = int(parts[2])
   used_region = player_game.get_city_by_number(city_number)
      if '_region' in location_str:
            used_region = used_region.get_parent(player_game)
    building_name = parts[-1]
        return used_region.find_coords_of_random_tile_of_type(player_game, building_name)
    
    # Parse {region_type}_{city_type} prefix
    for region_type in constants.REGION_TYPES:
    if region_type in location_str:
for city_type in constants.CITY_TYPES:
       if city_type in location_str:
  used_region = player_game.get_city_by_region_city_name(f"{region_type}_{city_type}")
             if '_region' in location_str:
           used_region = used_region.get_parent(player_game)
         building_name = parts[-1]
   return used_region.find_coords_of_random_tile_of_type(player_game, building_name)
    
    # Default: Use parent_task.acquired_region
    used_region = parent_task.acquired_region
    if 'region_city_' in location_str:
      used_region = used_region.child_city if used_region.child_city else used_region
else:
   if not used_region.isRegion():
            used_region = used_region.get_parent(player_game)
    
    building_name = location_str.replace('region_city_', '').replace('region_', '')
    return used_region.find_coords_of_random_building_of_type(player_game, building_name)
```

---

## Common Patterns

### Pattern 1: Shop Stock and Buy Flow

```python
from services.armor_shop_service import get_stock, buy

# 1. Get shop stock
stock = get_stock(
    player_level=player_game.get_max_character_level(),
    current_region=current_region,
    count=8
)

# 2. Display to player (UI layer)
print("Armor Shop:")
for i, item in enumerate(stock, 1):
    print(f"{i}. {item.name} - {item.value}g")

# 3. Player selects item
selection = int(input("Select item: ")) - 1
selected_item = stock[selection]

# 4. Attempt purchase
result = buy(player_game=player_game, item=selected_item)

# 5. Handle result
if result['success']:
    print(f"Purchased {result['item'].name}!")
else:
    if result['error'] == 'insufficient_funds':
   print("Not enough money.")
    elif result['error'] == 'inventory_full':
        print("Inventory full.")
```

### Pattern 2: Bar/Inn Service Flow

```python
from services.bar_service import get_stock, buy

# 1. Get region-specific menu
drinks = get_stock(
    player_level=player_level,
    player_game=player_game,
    current_region=current_region
)

# 2. Display menu
for i, drink in enumerate(drinks, 1):
    print(f"{i}. {drink['name']} - {drink['value']}g (HP: {drink['hp_fraction']*100:.0f}%, AP: {drink['ap_fraction']*100:.0f}%)")

# 3. Purchase
selection = drinks[int(input("Select: ")) - 1]
result = buy(player_game=player_game, drink=selection)

# 4. Show result
if result['success']:
    print(f"Consumed {result['drink']['name']}!")
    print(f"Healed: {result['healed']} HP, Restored: {result['ap_restored']} AP")
```

### Pattern 3: Movement Validation

```python
from services.player_movement_service import get_allowed_moves, handle_movement_key

# 1. Get allowed moves each frame
allowed = get_allowed_moves(
    region=current_region,
    player_game=player_game
)

# 2. Display directional options
for key, direction in allowed.items():
    print(f"[{key}] {direction}")

# 3. Process movement input
command = input("Move: ").lower()
if handle_movement_key(
    cmd=command,
    region=current_region,
    allowed_moves=allowed,
    radius=5,
    player_game=player_game
):
    # Movement successful - check for encounter
    from services.player_movement_service import check_for_random_mob_encounter
    
    mobs = check_for_random_mob_encounter(
        player_game=player_game,
    region_key=current_region.region_name
  )
    
    if mobs:
        # Initiate combat
        start_combat(mobs)
```

### Pattern 4: Task Event Execution

```python
from services.task_completion_service import execute_complete_event

# When task completes, execute all completion events
for event in task.task_complete_events:
    execute_complete_event(
        event=event,
        player_game=player_game,
        parent_task=task
    )

# Events are processed sequentially:
# 1. Dialog initiated (added to player_game.info_dialogs)
# 2. Items awarded (added to inventory)
# 3. Money awarded
# 4. NPCs shown/hidden
# 5. Next task awarded
# 6. Chapter advanced (if applicable)
```

### Pattern 5: Loot Generation

```python
from services.random_loot_service import generate_loot_for_sublocation

# 1. Check if sublocation yields loot (done externally based on subloc config)
subloc = {
    'name': 'Treasure Chest',
    'mode': 'searchable',
    'loot_chance': 0.3  # 30% chance
}

# 2. Roll for loot
import random
if random.random() < subloc['loot_chance']:
    # 3. Generate appropriate loot
    item = generate_loot_for_sublocation(
 subloc=subloc,
        player_level=player_game.get_max_character_level(),
        rng=random.Random()
    )
    
    # 4. Award to player
    if item:
        player_game.pick_up_item(item)
        print(f"Found: {item.name} ({item.rarity.value})")
```

---

## Integration Guide

### Service Dependencies

```
Shop Services (armor, weapon, utility)
    ??> constants.{TYPE}_SEEDS
    ??> _instantiate_{type}()
    ??> player_game.pick_up_item()
    ??> player_game.remove_single_item_unit()

Bar/Inn Services
    ??> constants.{REGION}_{CITY}_DRINK_MENU
    ??> player.heal()
    ??> player.current_ap (direct modification)

Player Movement Service
    ??> region.get_tile()
    ??> player_game.get_region_and_active_area_for_position()
    ??> player_game.set_position()
    ??> player_game.enter() / exit()
    ??> generate_random_mob()

Task Completion Service
  ??> constants.TASKS, NPCS, NPC_DIALOG, DUNGEON_SETTINGS, etc.
    ??> game.objects.{npc, item, task, dungeon}
    ??> game.services.dungeon_builder_service
    ??> player_game (extensive integration)

Random Loot Service
    ??> constants.{WEAPON|ARMOR|UTILITY|SPECIAL}_ITEM_SEEDS
    ??> _instantiate_{type}()
    ??> RarityDefaultWeights

City Service
    ??> player_game.regions
    ??> region.child_city
```

### Typical Service Usage Flow

#### Game Loop Integration

```python
from services import (
    player_movement_service,
    task_completion_service,
    armor_shop_service,
    bar_service,
    inn_service
)

# Main game loop
while True:
    # 1. Check for pending dialogs (from task completion)
    if player_game.info_dialogs:
        dialog = player_game.info_dialogs.pop(0)
    display_dialog(dialog)
        continue
    
    # 2. Check for pending combat
    if player_game.pending_fight_mob:
        mob_id = player_game.pending_fight_mob
        player_game.pending_fight_mob = None
     start_combat(mob_id)
        continue
  
    # 3. Check for completed tasks
    for task in player_game.tasks:
   if task.check_completion(player_game):
            for event in task.task_complete_events:
         task_completion_service.execute_complete_event(
        event, player_game, task
       )
       player_game.complete_task(task)
    
    # 4. Movement phase
    current_region, active_area = player_game.get_region_and_active_area_for_position()
    
    allowed_moves = player_movement_service.get_allowed_moves(
        region=active_area,
        player_game=player_game
    )
    
    command = get_player_input()
    
    if player_movement_service.handle_movement_key(
        cmd=command,
        region=active_area,
      allowed_moves=allowed_moves,
        radius=5,
   player_game=player_game
  ):
  # Check for random encounter
 mobs = player_movement_service.check_for_random_mob_encounter(
            player_game, active_area.region_name
        )
        if mobs:
     start_combat(mobs)
 continue
    
    # 5. Shop interactions
    if in_shop_context:
     stock = armor_shop_service.get_stock(
            player_game.get_max_character_level(),
         active_area
     )
        # ... handle shop UI
```

#### Task Creation and Completion

```python
# Task definition in constants.py
TASKS = [
    {
      'task_id': 'main_story_ch1_meet_ripple',
        'type': 'meet',
  'to_type': 'npc',
      'to_id': 'ripple',
        'task_acquire_events': [
    {
     'event_type': 'create_npc',
            'params': {
         'npc_id': 'ripple',
        'location': 'region_city_inn'
    }
         }
    ],
        'task_complete_events': [
        {
                'event_type': 'initiate_dialog',
             'params': {
 'npc_id': 'ripple',
'dialog_id': 'ripple_intro'
     }
            },
            {
            'event_type': 'award_item',
        'params': {
          'item_id': 'travel_pass'
      }
 },
       {
                'event_type': 'award_task',
      'params': {
           'task_id': 'main_story_ch1_investigate_fracture'
       }
            }
     ]
    }
]

# Task lifecycle
# 1. Task acquired (e.g., from advance_chapter or previous task)
task = build_task_from_seed(seed, region)
player_game.acquire_task(task)

# 2. Acquire events execute (NPC spawned at inn)
for event in task.task_acquire_events:
    task_completion_service.execute_acquire_event(
event, player_game, task
    )

# 3. Player meets NPC
player_game.set_position(inn_x, inn_y)
if task.check_completion(player_game):
    # 4. Complete events execute (dialog, item, next task)
    for event in task.task_complete_events:
    task_completion_service.execute_complete_event(
            event, player_game, task
        )
    player_game.complete_task(task)
```

---

## Performance Considerations

### Shop Services
- **Bottleneck:** Sorting large seed lists by value
- **Optimization:** Pre-sort seeds in constants, filter only
- **Typical Time:** <1ms per `get_stock()` call

### Movement Service
- **Bottleneck:** `get_region_and_active_area_for_position()` lookups
- **Optimization:** Cache active area per frame
- **Typical Time:** 1-5ms per movement validation

### Task Completion Service
- **Bottleneck:** Location parsing (string splitting, region searches)
- **Optimization:** Pre-compile location references during task build
- **Typical Time:** 5-20ms per event (varies by event type)

### Loot Service
- **Bottleneck:** Flattening seeds, weighted selection
- **Optimization:** Cache flattened seed list per player level
- **Typical Time:** 2-10ms per loot roll

---

## Debugging Tools

### Check Allowed Moves
```python
def debug_movement(region, player_game):
  """Print detailed movement analysis."""
    allowed = get_allowed_moves(region, player_game)
    print(f"Position: ({player_game.x}, {player_game.y}, {player_game.z})")
    print(f"Inside: {player_game.inside}")
    print(f"Inside Aircraft: {player_game.inside_aircraft}")
    print(f"Allowed moves: {allowed}")
    
    if player_game.inside:
        tile = region.get_tile(player_game.x, player_game.y)
        print(f"Current tile: {tile.type}")
        if tile.type == 'building':
            print(f"  Entrances: {tile.entrances}")
       print(f"  Floors: {tile.floors}")
     print(f"  Has basement: {tile.has_basement}")
```

### Validate Task Events
```python
def validate_task_events(task):
  """Check task event structure."""
    for event in task.task_acquire_events + task.task_complete_events:
        ev_type = event.event_type.value
        params = event.params
        
        print(f"Event: {ev_type}")
     
        # Check required params
        if ev_type == 'create_npc':
  assert 'npc_id' in params, "Missing npc_id"
   assert 'location' in params, "Missing location"
        elif ev_type == 'award_item':
         assert 'item_id' in params, "Missing item_id"
        elif ev_type == 'award_task':
        assert 'task_id' in params, "Missing task_id"
        
  print(f"  Params: {params} ?")
```

### Trace Event Execution
```python
def trace_event_execution(event, player_game, parent_task):
    """Log detailed event execution."""
print(f"\n=== Executing Event ===")
    print(f"Type: {event.event_type.value}")
    print(f"Params: {event.params}")
    print(f"Parent Task: {parent_task.task_id if parent_task else 'None'}")
    
    result = task_completion_service.handle_task_event(
        event, player_game, parent_task
    )
    
print(f"Result: {result}")
    print(f"======================\n")
    return result
```

---

## Version History

- **v1.0** - Initial documentation covering all 9 service modules
- Future: Will be updated as new services are added

---

## Contact

For questions or issues with game services, refer to:
- `game/objects/` - Game object definitions
- `game/constants.py` - Seed data and configuration
- Individual service files for algorithm-specific details
- `STORY DOCUMENTS FOR AI/README.md` - Timeline conversion guide
