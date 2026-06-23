# Game Services Reference

## Overview

This directory contains procedural generation and world-building services for AI Text Adventure. These services handle everything from individual city layouts to continent-scale world generation, dungeon creation, and spatial organization.

---

## Table of Contents

1. [World Generation](#world-generation)
2. [Region Building](#region-building)
3. [City Building](#city-building)
4. [Dungeon Building](#dungeon-building)
5. [Continent Management](#continent-management)
6. [Utility Services](#utility-services)
7. [Common Patterns](#common-patterns)
8. [Integration Guide](#integration-guide)

---

## World Generation

### `world_map_generator.py`

**Purpose**: High-level orchestration for creating entire game worlds with multiple regions.

#### Key Functions

##### `generate_world(pg, num_regions, seed_base, min_size, verbose)`
```python
pg = PlayerGame()
generate_world(
    pg=pg,
    num_regions=30,
    seed_base=12345,
    min_size=1000,
    verbose=True
)
```

**Parameters:**
- `pg`: PlayerGame instance to populate
- `num_regions`: Target number of regions to create
- `seed_base`: Base seed for deterministic generation (multiplied by iteration index)
- `min_size`: Minimum empty area required for region placement
- `verbose`: Enable progress logging

**Process:**
1. Iterates `num_regions` times
2. For each iteration, uses `seed_base * (i + 1)` as RNG seed
3. Calls `choose_origin()` to find valid perimeter location
4. Creates region via `pg.create_region_at(origin)`
5. Stops early if city limit (21) is reached

##### `choose_origin(pg, rng, min_size, attempts)`
```python
origin = choose_origin(
    pg=player_game,
    rng=random.Random(seed),
    min_size=1000,
    attempts=600
)
# Returns: (x, y) or None
```

**Selection Criteria:**
- Must be on perimeter of existing world tiles (actual edge detection)
- Must have sufficient empty area (`min_size` tiles)
- Must maintain minimum distance from existing regions (default: 10 tiles)
- Uses spatial validation via `pg.can_build_city_in_range()`

##### `perimeter_candidates(pg, margin, step)`
```python
candidates = perimeter_candidates(
    pg=player_game,
    margin=32,
    step=8
)
# Returns: List[(x, y)]
```

**Edge Detection Algorithm:**
- Finds all empty 4-neighbor cells adjacent to occupied tiles
- Returns actual perimeter rather than rectangular bounds
- Applies thinning via `step` parameter for performance
- Fallback to bounding-box perimeter if no tiles exist

#### Usage Pattern
```python
from game.services.world_map_generator import generate_world
from game.objects.player_game import PlayerGame

# Create empty world
pg = PlayerGame()

# Generate 30 regions with deterministic seed
generate_world(
    pg=pg,
 num_regions=30,
    seed_base=42,
    min_size=800,
    verbose=True
)

# Result: pg.regions populated, pg.world_tiles contains all tiles
print(f"Created {len(pg.regions)} regions")
print(f"Total tiles: {len(pg.world_tiles)}")
```

---

## Region Building

### `region_builder_service.py`

**Purpose**: High-level region construction orchestration and helper wrappers.

#### Key Functions

##### `create_region_city(region_settings)`
```python
rc = create_region_city({
    "region_name": "forest",
    "city_name": "Thornwood",
    "display_name": "Thornwood Village",
    "max_size": 1200,
    "population_density": 0.6,
    "hasResidence": True,
    "hasBusiness": True,
    "hasShops": True,
    "hasBar": True,
    "hasInn": True,
    "road_spacing": 8,
    "alley_spacing": 4,
    "alley_offset": 2
})
```

**Creates**: Empty `City` instance configured from settings dictionary.

**Settings Structure:**
- `region_name`: Biome identifier (e.g., "forest", "desert")
- `city_name`: Internal city name
- `display_name`: User-facing name
- `max_size`: Maximum tile count
- `population_density`: 0.0-1.0 building density
- `has*`: Boolean flags for building types
- `road_spacing`, `alley_spacing`, `alley_offset`: Grid parameters

##### `create_region(rc, origin, shifted_location, main_tiles, ...)`
```python
region_tiles = create_region(
    rc=region_city,
    origin=(0, 0),
    shifted_location=(100, 100),
    main_tiles=main_city_tiles,
    neighbor_offsets=[(1,0), (-1,0), (0,1), (0,-1), ...],
    center_x=50,
    center_y=50,
    ignored_set=set(),
  region_settings=settings,
    player_game=pg
)
```

**Process:**
1. Compute midpoint and radius from `main_tiles`
2. Create base shape (hex, diamond, square, circle, or star - randomly chosen)
3. Apply perimeter-driven growth to fill to `max_size`
4. Call `rc.ensure_required_buildings()` to place special buildings
5. Create tiles via `rc.create_tile()` for each position
6. Populate tiles with `rc.populate_tiles()`

**Shape Selection:**
- 20% chance: Hexagon
- 20% chance: Diamond
- 20% chance: Square
- 20% chance: Circle
- 20% chance: Star (3-7 points, random)

##### `prepare_main_context(main_city, origin, ignored_locations)`
```python
context = prepare_main_context(
    main_city=parent_city,
    origin=(0, 0),
    ignored_locations=[(5, 5), (10, 10)]
)
# Returns dict with:
# - ignored_set
# - minx, maxx, miny, maxy (bbox)
# - main_tiles
# - perimeter
# - neighbor_offsets (8-directional)
# - center_x, center_y
```

**Purpose**: Pre-compute spatial context for region generation.

---

### `region_shape_service.py`

**Purpose**: Geometric shape generation primitives for region layouts.

#### Shape Functions

All shape functions follow this signature:
```python
filled_tiles = make_filled_shape(
  center_x, center_y,
    size_param,
    current_tiles,  # modified in-place
    ignored_tiles
)
# Returns: Set[(x, y)] of newly added tiles
```

##### `make_filled_circle(x, y, radius, current_tiles, ignored_tiles)`
```python
tiles = make_filled_circle(
    x=50, y=50,
    radius=15,
    current_tiles=existing,
    ignored_tiles=blocked
)
```

**Algorithm**: `dx^2 + dy^2 <= radius^2` (true circular shape)

##### `make_filled_square(cx, cy, half_size, current_tiles, ignored_tiles)`
```python
tiles = make_filled_square(
    cx=50, cy=50,
    half_size=10,  # 21x21 square
    current_tiles=existing,
    ignored_tiles=blocked
)
```

**Algorithm**: Axis-aligned square with center at `(cx, cy)`

##### `make_filled_diamond(cx, cy, radius, current_tiles, ignored_tiles)`
```python
tiles = make_filled_diamond(
    cx=50, cy=50,
    radius=15,
current_tiles=existing,
    ignored_tiles=blocked
)
```

**Algorithm**: Manhattan distance `|dx| + |dy| <= radius`

##### `make_filled_hex(cx, cy, radius, current_tiles, ignored_tiles)`
```python
tiles = make_filled_hex(
    cx=50, cy=50,
radius=12,
    current_tiles=existing,
    ignored_tiles=blocked
)
```

**Algorithm**: Axial hex coordinates with cube distance check

##### `make_filled_star(cx, cy, outer_radius, points, inner_ratio, current_tiles, ignored_tiles)`
```python
tiles = make_filled_star(
    cx=50, cy=50,
    outer_radius=20,
    points=5,
    inner_ratio=0.5,
    current_tiles=existing,
    ignored_tiles=blocked
)
```

**Algorithm**: 
- Generates `points * 2` vertices (alternating outer/inner radii)
- Uses point-in-polygon test for fill
- `inner_ratio` controls indentation depth (0.0-1.0)

#### Pattern Recognition
- All functions modify `current_tiles` **in-place** (side effect)
- All functions skip tiles already in `current_tiles` or `ignored_tiles`
- All functions return only **newly added** tiles

---

### `region_frontier_service.py`

**Purpose**: Frontier-based region expansion and growth algorithms.

#### Key Functions

##### `randomized_frontier_perimeter_pathing(midpoint_x, midpoint_y, current_tiles, ignored_set, neighbor_offsets, max_size)`
```python
added = randomized_frontier_perimeter_pathing(
    midpoint_x=50,
    midpoint_y=50,
    current_tiles=existing_tiles,  # modified in-place
    ignored_set=blocked_tiles,
    neighbor_offsets=[(1,0), (-1,0), (0,1), (0,-1), ...],
    max_size=1000
)
# Returns: List[(x, y)] in addition order
```

**Algorithm:**
1. Find perimeter tiles (tiles touching empty space)
2. Seed queue with neighbors of perimeter tiles
3. Randomize initial queue order
4. While queue not empty and size < max_size:
   - Occasionally pick random queue element (18% chance) for variance
   - Otherwise dequeue from front (BFS)
   - If candidate not adjacent to `current_tiles`, defer (max 6 times)
   - Add tile and its neighbors (shuffled order)
   - Apply adjacency fix for tiles near ignored zones

**Defer Mechanism:**
- Prevents isolated tiles by requiring adjacency to existing area
- Tiles deferred >6 times are dropped
- Queue cycle limit prevents infinite loops

**Adjacency Fix:**
```python
# Automatically adds required tiles when a tile is:
# - Adjacent to free space
# - 2 tiles away from ignored zone
# Prevents single-tile gaps
```

##### `perimeter_driven_growth(current_tiles, ignored_set, neighbor_offsets, max_size, shuffle_interval)`
```python
added = perimeter_driven_growth(
    current_tiles=existing_tiles,
    ignored_set=blocked_tiles,
    neighbor_offsets=[(1,0), (-1,0), (0,1), (0,-1), ...],
    max_size=1000,
    shuffle_interval=10
)
```

**Algorithm** (preserves initial shape better than BFS):
1. Compute initial perimeter
2. While size < max_size and perimeter exists:
   - Pop first perimeter tile
   - Check all 8 neighbors
   - Add neighbors that:
     - Are not in `current_tiles` or `ignored_set`
     - Are adjacent to existing tiles
   - Apply adjacency fix rule
   - Add newly added tiles to perimeter
3. Shuffle perimeter every `shuffle_interval` iterations

**Comparison:**
- `randomized_frontier_perimeter_pathing`: Faster, more organic/blobby
- `perimeter_driven_growth`: Slower, preserves initial shape better

##### `find_perimiter_points(midpoint_x, midpoint_y, current_tiles, ignored_set, neighbor_offsets, max_size)`
```python
perimeter = find_perimiter_points(
    midpoint_x=50,
  midpoint_y=50,
    current_tiles=region_tiles,
    ignored_set=blocked,
    neighbor_offsets=offsets,
    max_size=100
)
# Returns: List[(x, y)] sorted by distance to midpoint (closest first)
```

**Use Case**: Find expansion candidates for frontier algorithms.

---

### `region_fractal_service.py`

**Purpose**: Fractal/organic noise-based region masks for natural-looking borders.

#### Key Functions

##### `generate_fractal_mask(center, approx_tiles, seed, scale, octaves, padding)`
```python
mask = generate_fractal_mask(
    center=(50, 50),
    approx_tiles=1000,
    seed=12345,
    scale=6.0,
    octaves=3,
    padding=2
)
# Returns: List[(x, y)] ordered by score (highest first)
```

**Algorithm:**
1. Estimate radius from `approx_tiles` (circle approximation)
2. Add `padding` to radius for selection room
3. For each tile in circular area:
   - Compute multi-octave value via sin/cos waves
   - Add hash-based perturbation for splotchiness
4. Sort by score descending
5. Return ordered coordinate list

**Parameters:**
- `scale`: Base spatial frequency (higher = larger features)
- `octaves`: Number of frequencies to combine (more = more detail)
- `padding`: Extra tiles beyond radius for flexibility

**Usage Pattern:**
```python
# Generate organic mask
mask = generate_fractal_mask(
    center=(0, 0),
    approx_tiles=800,
  seed=42,
  scale=8.0,
    octaves=4
)

# Use only top N tiles for tight natural shape
selected = mask[:800]
```

##### `carve_fractal_shape(rc, mask, main_tiles, ignored_set, region_tiles, max_size)`
```python
added_count = carve_fractal_shape(
    rc=region_city,
    mask=fractal_mask,
    main_tiles=city_tiles,
    ignored_set=blocked,
    region_tiles=region_set,  # modified in-place
    max_size=1000
)
# Returns: int (number of tiles added)
```

**Purpose**: Apply fractal mask to actual City instance, creating tiles.

**Process:**
1. Iterate mask in priority order
2. Skip if in `main_tiles`, `ignored_set`, or `region_tiles`
3. Call `rc.get_or_create_tile(x, y)`
4. Add to `region_tiles` if successful
5. Stop when `max_size` reached

---

## City Building

### `city_builder_service.py`

**Purpose**: City-scale procedural generation (buildings, roads, districts).

#### Key Functions

##### `build_city_map(seed)`
```python
city, center = build_city_map(seed=12345)
# Returns: (City instance, (center_x, center_y))
```

**Algorithm:**
1. Create empty `City(seed)`
2. 50% chance: `draw_character_bitmap()` (themed shapes)
3. 50% chance: `draw_random_splotches()` (organic blocks)
4. Ensure center tile exists
5. Convert tile set to `Tile` objects in `city.tiles`

**Tile Budget:**
- Uses `city.max_size` (default 200)
- Spatial bound: `max_dim = ceil(sqrt(max_tiles) * 1.25)`

##### `draw_character_bitmap(max_tiles, max_dim, tiles)`
```python
draw_character_bitmap(
  max_tiles=200,
    max_dim=20,
    tiles=tile_set  # modified in-place
)
```

**Algorithm:**
1. Pick random bitmap from `CITY_BITMAPS`
2. Normalize coords to (0, 0) origin
3. Downsample if exceeds `max_dim` (skip rows/cols)
4. Scale up (integer scaling) to fill `max_tiles` budget
5. Center around (0, 0)
6. Trim to exact `max_tiles` if needed

**Bitmap Format:**
```python
CITY_BITMAPS = [
    [
        "       tttttttt ",
        "     ttttttt ttt       ",
    "     ttt ttttt tt      ",
 "     tttttttttttt      ",
        "tttttt   "
    ],
    # ... more shapes
]
# 't' = tile placement, ' ' = empty
```

##### `draw_random_splotches(max_tiles, max_dim, tiles)`
```python
draw_random_splotches(
    max_tiles=200,
    max_dim=20,
    tiles=tile_set  # modified in-place
)
```

**Algorithm:**
1. Stamp random rectangles until `max_tiles` reached
2. Rectangle constraints:
   - Width/height: 1-7
   - Area: <= 25 tiles
3. Origin within `(-max_dim/2, max_dim/2)` bounds
4. Skip rectangles that exceed spatial bounds
5. Center and clip if needed

**Use Case**: Creates organic, irregular city layouts.

##### `translate_city(city, shifted_location)`
```python
translate_city(
    city=my_city,
    shifted_location=(100, 50)  # dx, dy
)
```

**Purpose**: Move entire city by offset (in-place mutation).

**Process:**
1. Create `new_tiles = {}`
2. For each `(x, y), tile` in `city.tiles`:
   - Update `tile.x = x + dx`
   - Update `tile.y = y + dy`
   - Store as `new_tiles[(x + dx, y + dy)] = tile`
3. Replace `city.tiles = new_tiles`

##### `give_roads_personality(city)` *(stub)*
```python
give_roads_personality(city)
# TODO: Carve cul-de-sacs, turns, non-grid patterns
```

**Future**: Modify grid roads to add organic character.

##### `place_open_area_buildings(city, city_area, building_chance)` *(stub)*
```python
place_open_area_buildings(
    city=my_city,
    city_area=open_tiles,
    building_chance=0.05
)
# TODO: Randomly place buildings in open areas
```

---

## Dungeon Building

### `dungeon_builder_service.py`

**Purpose**: Multi-floor dungeon generation with rooms, corridors, and entity placement.

#### Core Class: `DungeonBuilder`

##### Constructor
```python
builder = DungeonBuilder({
    "dungeon_id": "ancient_crypt",
    "seed": 12345,
    "floor_count": 3,
    "room_size_min_max": (81, 120),  # 9x9 to ~11x11
    "rooms_per_floor": 6,
    "max_neighbors_per_room": 2,
    "additional_connection_chance": 0.1,
    "min_max_distance_between_rooms": (5, 12),
    "min_max_corridor_width": (3, 6),
    "display_name": "The Ancient Crypt",
    "open_area_tile": FLOOR_TILE,
    "impassable_tile": WALL_TILE,
    "impassable_chance": 0.05,
    "visible_distance": 5,
    "npcs": [
        {"id": "boss_lich", "location": "final_chamber"}
    ],
    "items": [
        {"id": "magic_key", "location": "treasure_room"}
    ]
})

dungeon = builder.build()
```

**Settings Breakdown:**

| Key | Type | Description |
|-----|------|-------------|
| `dungeon_id` | str | Unique identifier |
| `seed` | int | RNG seed (can be string, gets hashed) |
| `floor_count` | int | Number of vertical floors |
| `room_size_min_max` | (int, int) | Room area range (tiles) |
| `rooms_per_floor` | int | Target room count per floor |
| `max_neighbors_per_room` | int | Max connections per room |
| `additional_connection_chance` | float | Probability of extra connections |
| `min_max_distance_between_rooms` | (int, int) | Room spacing range |
| `min_max_corridor_width` | (int, int) | Corridor width range |
| `impassable_chance` | float | Rock/obstacle density |
| `npcs` | List[dict] | NPC placement specs |
| `items` | List[dict] | Item placement specs |

##### `build() -> Dungeon`
```python
dungeon = builder.build()
```

**Process (per floor):**
1. **Create first room**: Centered at (0, 0) or aligned with previous floor's exit
2. **Grow room graph**: Add rooms via `_grow_rooms()` until target count reached
3. **Carve rooms**: Create `DungeonTile` objects for room floors
4. **Carve corridors**: Connect neighboring rooms with L-shaped passages
5. **Mark entrance**: Center of first room on floor 0 = `DungeonTileType.ENTRANCE`
6. **Choose exit stair**: Room farthest from entrance = stairs up
7. **Link floors**: Ensure stairs down on floor above match stairs up below

**Post-floor processing:**
1. **Mark final chamber**: Farthest room from start across all floors
2. **Mark treasure rooms**: All non-entrance, non-final rooms
3. **Place stairs**: Ensure bidirectional stair linkage between floors
4. **Naturalize**: Optional perimeter smoothing (30% chance per perimeter tile)
5. **Place NPCs/items**: Use location hints (`final_chamber`, `treasure_room`, etc.)
6. **Add impassables**: Randomly convert passable tiles to obstacles (respects paths)

#### Room Generation

##### `_create_first_room(z, center)`
```python
self._create_first_room(
    z=0,
    center=(50, 50)  # optional alignment
)
```

**Purpose**: Seed room graph with starting room at floor origin.

##### `_grow_rooms()`
```python
self._grow_rooms()  # populates self.rooms
```

**Algorithm:**
1. While `len(rooms) < rooms_per_floor`:
   - Pick random parent room (must have < `max_neighbors_per_room` connections)
   - Attempt to place new room near parent via `_attempt_place_room_near()`
   - Connect parent ? child if placement succeeds
2. Optional: Add extra connections based on `additional_connection_chance`

##### `_attempt_place_room_near(parent, new_id)`
```python
new_room = self._attempt_place_room_near(
    parent=parent_room,
    new_id=5
)
# Returns: room dict or None
```

**Algorithm:**
1. Generate random room size from `room_size_min_max`
2. Pick random direction (up/down/left/right)
3. Pick random distance from `min_max_distance_between_rooms`
4. Compute candidate position relative to parent edge
5. Check overlap with existing rooms via `_overlaps_any_room()`
6. Retry up to 32 times, return None if all fail

**Room Dictionary Structure:**
```python
{
    'id': 5,         # globally unique across all floors
  'x': 10,            # top-left corner
    'y': 20,
    'z': 1,             # floor level
    'w': 9,         # width
    'h': 9,       # height
    'neighbors': [3, 7] # connected room IDs
}
```

#### Corridor Generation

##### `_carve_corridor(dungeon, a, b, z)`
```python
self._carve_corridor(
    dungeon=dungeon_instance,
    a=room_a,
    b=room_b,
    z=1
)
```

**Algorithm (L-shaped corridors):**
1. Pick random interior points in rooms A and B
2. Choose random corridor width from `min_max_corridor_width`
3. 50% chance:
   - Horizontal from A to B's x
   - Vertical from B's x to B's y
4. 50% chance:
   - Vertical from A to B's y
   - Horizontal from B's y to B's x
5. Mark corridor tiles as `DungeonTileType.CORRIDOR`

##### `_carve_rect(dungeon, x, y, w, h, z)`
```python
_carve_rect(
    dungeon=dungeon,
x=10, y=20,
    w=5, h=8,
    z=1
)
```

**Purpose**: Bulk-create passable tiles in rectangular area.

#### Special Tile Marking

##### Final Chamber Detection
```python
# Farthest room from start (floor 0, first room)
start_room = all_rooms[0]  # z == 0
farthest = max(all_rooms, key=lambda r: distance_to(start_room, r))

# Mark inner area (exclude walls) as FINAL_CHAMBER
for x in range(room['x'] + 1, room['x'] + room['w'] - 1):
    for y in range(room['y'] + 1, room['y'] + room['h'] - 1):
        tile = dungeon.get_tile(x, y, room['z'])
        if tile and tile.passable:
        tile.tile_type = DungeonTileType.FINAL_CHAMBER
```

##### Treasure Room Marking
```python
# All rooms except entrance (floor 0, first room) and final chamber
for room in all_rooms:
 if room not in [entrance_room, final_room]:
        # Mark entire room floor as TREASURE_ROOM
   for y in range(room['y'], room['y'] + room['h']):
      for x in range(room['x'], room['x'] + room['w']):
      tile.tile_type = DungeonTileType.TREASURE_ROOM
```

#### Entity Placement

##### `_place_npcs_and_items(dungeon)`
```python
self._place_npcs_and_items(dungeon)
```

**Algorithm:**
1. For each item spec:
   - Parse `location` hint (e.g., `"final_chamber"`)
   - Call `dungeon.place_entity_at_location(item, location_type)`
2. For each NPC spec:
   - Parse `location` hint
   - Create entity dict: `{'type': 'npc', 'npc_id': npc_id}`
   - Call `dungeon.place_entity_at_location(entity, location_type)`

**Location Hints:**
- `"final_chamber"` ? Farthest room
- `"treasure_room"` ? Any non-entrance, non-final room
- `"entrance"` ? First room floor 0
- `"corridor"` ? Any corridor tile

#### Obstacle Placement

##### `_add_impassables(dungeon, z)`
```python
self._add_impassables(dungeon, z=1)
```

**Algorithm:**
1. For each passable tile on floor `z`:
   - Check `not_origin()` (skip (0, 0, 0))
   - Check `not_blocking_connections()` (must preserve paths between rooms)
   - Check `not_blocking_npc_paths()` (must preserve path from origin to all NPCs)
2. If all checks pass and random() < `impassable_chance`:
   - Set `tile.passable = False`

##### `path_exists_if_location_blocked(goal, block_position, dungeon)`
```python
exists = self.path_exists_if_location_blocked(
    goal=(10, 20, 1),
    block_position=(5, 10, 1),
    dungeon=dungeon
)
# Returns: bool (True if path remains if position blocked)
```

**Algorithm**: Breadth-first search from origin (0, 0, 0) to `goal`, treating `block_position` as impassable. Supports 4-directional movement and stairs.

#### Naturalization

##### `_naturalize(dungeon, z)`
```python
self._naturalize(dungeon, z=0)
```

**Algorithm:**
1. Find perimeter tiles (impassable with at least one passable neighbor)
2. For each perimeter tile:
   - 30% chance to convert to passable
   - Infer `tile_type` from adjacent tiles (or default to `CORRIDOR`)
3. Creates more organic, less grid-like dungeon edges

---

## Continent Management

### `continent_service.py`

**Purpose**: Continental-scale world organization, ocean generation, and spatial distribution.

#### Key Functions

##### `build_continents_and_ocean(player_game, num_continents, rng_seed, spread_radius, ocean_padding)`
```python
result = build_continents_and_ocean(
    player_game=pg,
    num_continents=6,
    rng_seed=12345,
    spread_radius=140,
    ocean_padding=10
)

# Returns dict:
# {
#     "continents": [bbox1, bbox2, ...],  # List of (minx, maxx, miny, maxy)
#     "ocean_bbox": (minx, maxx, miny, maxy),
#     "ocean_region": City instance,
#     "continent_compositions": [
#  {"continent_number": 1, "city_names": ["City A", "City B"]},
#         ...
#     ]
# }
```

**Process:**
1. **City Assignment**: Distribute city-bearing regions into 6 continents
   - Explicit city counts: `[4, 3, 6, 2, 5, 1]` (total 21 cities)
   - Rotate order so player's starting region is first
- First continent anchored (player's home, never moved)
2. **Citiless Assignment**: Assign non-city regions to nearest continent
3. **Radial Spread**: Place continents on radial angles around world center
   - Skip first continent (anchor)
   - Safe radius computed from max continent extent
4. **Tightening**: Pull continents closer if gaps too large (30-70 tile range)
5. **Ocean Generation**: Create rectangular ocean region filling world bounds + padding

##### City Count Distribution
```python
requested_counts = [4, 3, 6, 2, 5, 1]  # Must sum to 21
```

**Rules:**
- **Continent 1**: Player's starting region (anchor, never moves) + 3 more cities
- **Continent 2**: 3 cities
- **Continent 3**: 6 cities (largest)
- **Continent 4**: 2 cities
- **Continent 5**: 5 cities
- **Continent 6**: 1 city (smallest)

##### `assign_city_regions_to_continents(player_game, continent_city_counts)`
```python
continents = assign_city_regions_to_continents(
player_game=pg,
    continent_city_counts=[4, 3, 6, 2, 5, 1]
)
# Returns: List[List[City]] (6 continent groups)
```

**Algorithm:**
1. Find player's starting region via `find_region_for_player()`
2. Get all city-bearing regions via `ordered_city_regions()`
3. Rotate list so player's region is first
4. Partition sequentially into continent groups

##### `assign_citiless_regions_to_continents(player_game, continents)`
```python
assign_citiless_regions_to_continents(
    player_game=pg,
    continents=continent_groups  # modified in-place
)
```

**Algorithm:**
1. Compute centroid for each continent
2. For each citiless region:
   - Compute region center
   - Find nearest continent center
   - Append region to that continent
   - Update continent center for next iteration

##### `spread_continents_radial(player_game, continents, rng, radius, skip_first)`
```python
spread_continents_radial(
    player_game=pg,
    continents=continent_groups,
    rng=random.Random(seed),
    radius=140,
    skip_first=True  # Don't move first continent (player anchor)
)
```

**Algorithm:**
1. Compute world center from all tiles
2. Compute safe radius: `max(radius, (2 * max_extent) + padding)`
3. For each continent (skip first if `skip_first=True`):
   - Compute current center
 - Assign target position: `world_center + (cos(angle), sin(angle)) * radius`
   - Translate all regions in continent by delta

**Angle Distribution:**
```python
angle_step = 2? / num_continents
angles = [base_angle + i * angle_step for i in range(num_continents)]
# base_angle randomized to avoid alignment bias
```

##### `pull_continents_closer_by_tiles(player_game, continents, anchor_index, min_gap, max_gap, max_iters, step_cap)`
```python
pull_continents_closer_by_tiles(
    player_game=pg,
    continents=continent_groups,
    anchor_index=0,  # Player's continent (fixed)
    min_gap=30,
    max_gap=70,
    max_iters=30,
 step_cap=12
)
```

**Algorithm:**
1. Compute anchor continent boundary tiles
2. For each iteration (max `max_iters`):
   - For each non-anchor continent:
     - Compute boundary-to-boundary distance to anchor
     - If distance > `max_gap`:
       - Compute pull vector toward anchor center
       - Move continent by min(`step_cap`, distance - target_gap)
     - Target gap = `(min_gap + max_gap) / 2`
   - Stop if no continent moved this iteration

**Distance Calculation:**
```python
# min_distance_between_tile_sets() uses spatial hash grid
# Falls back to bounding-box gap if no tiles in search radius
# Search radius: 2 cells around each tile (configurable)
```

##### `build_ocean_region_from_bbox(player_game, bbox, seed)`
```python
ocean = build_ocean_region_from_bbox(
    player_game=pg,
    bbox=(minx, maxx, miny, maxy),
    seed=99999
)
```

**Algorithm:**
1. Create empty `City(seed)`
2. Set `region_name = 'shallows'` (uses shallow water rendering)
3. For each (x, y) in bounding box:
   - Skip if tile already exists in `world_tiles`
   - Create impassable water tile
4. Merge into `player_game` and append to `regions`

##### `translate_region_tiles(region, dx, dy, player_game)`
```python
translate_region_tiles(
    region=my_region,
    dx=100,
    dy=50,
    player_game=pg
)
```

**Purpose**: Move region and all child cities by offset (in-place).

**Side Effects:**
- Updates `Tile.x` and `Tile.y` for all tiles
- Calls `translate_entities_at_location()` for NPCs/dungeons/aircraft
- Uses guard set to prevent duplicate entity moves

##### `translate_entities_at_location(x, y, dx, dy, player_game)`
```python
translate_entities_at_location(
    x=50, y=50,
    dx=100, dy=50,
    player_game=pg
)
```

**Entities Handled:**
- **Dungeons**: `dungeon.position = (x, y)` ? `(x + dx, y + dy)`
- **NPCs**: `npc.position = (x, y, z)` ? `(x + dx, y + dy, z)`
- **Aircraft**: `aircraft_location = (x, y)` ? `(x + dx, y + dy)`

**Guard Mechanism:**
```python
# Stored on PlayerGame to prevent duplicate moves during one pass
moved = getattr(player_game, "_continent_translate_moved_entities", set())
key = ("dungeon", dungeon.id)  # or ("npc", npc_id) or ("aircraft", "aircraft_location")
if key in moved:
    continue
moved.add(key)
```

##### `update_player_game_world_tiles_after_translation(player_game)`
```python
update_player_game_world_tiles_after_translation(pg)
```

**Purpose**: Rebuild `pg.world_tiles` from `pg.regions` after translations.

**Algorithm:**
1. Clear `player_game.world_tiles`
2. For each region in `player_game.regions`:
   - Merge `region.tiles` into `world_tiles`
   - If `region.child_city` exists, merge `child_city.tiles` too

---

## Utility Services

### Spatial Utilities

#### `bbox_and_center_from_tiles(tiles)`
```python
(bbox, center) = bbox_and_center_from_tiles(tile_set)
# bbox: (min_x, max_x, min_y, max_y)
# center: (cx, cy)
```

#### `collect_region_tiles(region)`
```python
tiles = collect_region_tiles(region)
# Returns: Set[(x, y)] from region.tiles.keys()
```

#### `continent_center_from_regions(regions)`
```python
center = continent_center_from_regions(continent_regions)
# Returns: (cx, cy) centroid across all regions + child cities
```

#### `continent_tiles(cont)`
```python
tiles = continent_tiles(continent_regions)
# Returns: Set[(x, y)] from all regions + child cities in continent
```

#### `boundary_tiles(tiles)`
```python
perimeter = boundary_tiles(region_tiles)
# Returns: Set[(x, y)] with at least one 4-neighbor missing
```

#### `continent_extent_radius(cont)`
```python
radius = continent_extent_radius(continent_regions)
# Returns: float (approx radius based on bbox diagonal / 2)
```

### Distance Utilities

#### `min_distance_between_tile_sets(a, b, search_radius_cells)`
```python
dist = min_distance_between_tile_sets(
    a=continent1_tiles,
    b=continent2_tiles,
    search_radius_cells=3
)
# Returns: float (Euclidean distance, fallback to bbox gap if too far)
```

**Algorithm:**
1. Build spatial hash grid for set `b` (cell_size=16)
2. For each tile in set `a`:
   - Check neighboring cells (radius = `search_radius_cells`)
   - Track minimum squared distance
3. If no tiles found in search radius:
   - Fall back to `_bbox_gap()` between bounding boxes

#### `_bbox_gap(a, b)`
```python
gap = _bbox_gap(bbox_a, bbox_b)
# Returns: float (min Euclidean distance, 0 if overlap/touch)
```

**Use Case**: Fast approximate distance when tile-level precision not needed.

---

## Common Patterns

### Pattern 1: Create Region at World Edge

```python
from game.services.world_map_generator import choose_origin, generate_world
from game.objects.player_game import PlayerGame

pg = PlayerGame()

# Generate 30 regions sequentially
generate_world(
    pg=pg,
    num_regions=30,
    seed_base=42,
  min_size=800,
    verbose=True
)

# Regions automatically placed on perimeter
print(f"Created {len(pg.regions)} regions")
```

### Pattern 2: Build Custom Region

```python
from game.services.region_builder_service import create_region_city, create_region, prepare_main_context

# 1. Create configured region city
settings = {
    "region_name": "forest",
    "city_name": "Darkwood",
    "display_name": "Darkwood Village",
    "max_size": 1200,
    "population_density": 0.7,
    "hasBar": True,
    "hasInn": True
}
rc = create_region_city(settings)

# 2. Prepare spatial context
context = prepare_main_context(
    main_city=None,  # No parent city
  origin=(100, 100),
    ignored_locations=[]
)

# 3. Generate region tiles
create_region(
    rc=rc,
 origin=(100, 100),
  shifted_location=(100, 100),
    main_tiles=set(),
    neighbor_offsets=context["neighbor_offsets"],
    center_x=context["center_x"],
    center_y=context["center_y"],
    ignored_set=context["ignored_set"],
    region_settings=settings,
    player_game=pg
)

# 4. Merge into world
pg.merge_region(rc)
pg.regions.append(rc)
```

### Pattern 3: Generate Dungeon

```python
from game.services.dungeon_builder_service import build_dungeon

settings = {
  "dungeon_id": "lost_temple",
  "seed": 77777,
    "floor_count": 2,
    "room_size_min_max": (64, 100),
    "rooms_per_floor": 5,
    "max_neighbors_per_room": 3,
    "min_max_distance_between_rooms": (4, 10),
    "min_max_corridor_width": (2, 5),
    "display_name": "The Lost Temple",
    "impassable_chance": 0.03,
  "npcs": [
     {"id": "guardian_statue", "location": "final_chamber"}
    ],
    "items": [
        {"id": "ancient_key", "location": "treasure_room"}
    ]
}

dungeon = build_dungeon(settings)

# Place in world
dungeon.position = (50, 50)  # World coordinates
pg.dungeons.append(dungeon)
```

### Pattern 4: Organize into Continents

```python
from game.services.continent_service import build_continents_and_ocean

# After generating regions with cities
result = build_continents_and_ocean(
    player_game=pg,
    num_continents=6,
    rng_seed=12345,
    spread_radius=150,
    ocean_padding=15
)

# Access results
print(f"Continent bboxes: {result['continents']}")
print(f"Ocean bbox: {result['ocean_bbox']}")
for comp in result["continent_compositions"]:
    print(f"Continent {comp['continent_number']}: {comp['city_names']}")
```

### Pattern 5: Custom Shape Region

```python
from game.services.region_shape_service import make_filled_star
from game.services.region_frontier_service import perimeter_driven_growth

# 1. Create star-shaped base
current_tiles = set()
ignored = set()
star_tiles = make_filled_star(
 cx=0, cy=0,
    outer_radius=15,
    points=7,
    inner_ratio=0.4,
    current_tiles=current_tiles,
    ignored_tiles=ignored
)

# 2. Expand using perimeter growth
added = perimeter_driven_growth(
    current_tiles=current_tiles,
    ignored_set=ignored,
    neighbor_offsets=[(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)],
max_size=1000,
    shuffle_interval=15
)

# 3. Convert to City tiles
for (x, y) in current_tiles:
    rc.tiles[(x, y)] = Tile(x, y, 'open_area')
```

---

## Integration Guide

### Service Dependencies

```
world_map_generator
    ??> PlayerGame.create_region_at()
        ??> region_builder_service.create_region_city()
        ??> region_builder_service.create_region()
            ??> region_shape_service.make_filled_*()
       ??> region_frontier_service.perimeter_driven_growth()
??> (optional) region_fractal_service.generate_fractal_mask()

city_builder_service.build_city_map()
    ??> draw_character_bitmap() OR draw_random_splotches()

dungeon_builder_service.build_dungeon()
    ??> DungeonBuilder.build()

continent_service.build_continents_and_ocean()
    ??> assign_city_regions_to_continents()
    ??> assign_citiless_regions_to_continents()
    ??> spread_continents_radial()
    ??> pull_continents_closer_by_tiles()
    ??> build_ocean_region_from_bbox()
```

### Typical World Generation Flow

```python
from game.objects.player_game import PlayerGame
from game.services.world_map_generator import generate_world
from game.services.continent_service import build_continents_and_ocean

# 1. Create empty world
pg = PlayerGame()

# 2. Generate regions
generate_world(
    pg=pg,
    num_regions=35,  # Will create until 21 cities reached
    seed_base=42,
    min_size=800,
    verbose=True
)

# 3. Organize into continents
result = build_continents_and_ocean(
    player_game=pg,
    num_continents=6,
    rng_seed=12345,
    spread_radius=140,
    ocean_padding=10
)

# 4. Generate dungeons for regions (example)
from game.services.dungeon_builder_service import build_dungeon

for region in pg.regions:
    if should_have_dungeon(region):
        dungeon_settings = create_dungeon_settings_for_region(region)
  dungeon = build_dungeon(dungeon_settings)
        dungeon.position = region.get_center_position()
        pg.dungeons.append(dungeon)

# 5. World ready for gameplay
print(f"World complete: {len(pg.regions)} regions, {len(pg.dungeons)} dungeons")
```

### Performance Considerations

#### Region Generation
- **Bottleneck**: Perimeter-driven growth (quadratic tile checks)
- **Optimization**: Use `randomized_frontier_perimeter_pathing` for speed (trades shape fidelity)
- **Typical Time**: ~0.1-0.5s per region (1000 tiles) on modern hardware

#### Dungeon Generation
- **Bottleneck**: Path validation for impassable placement
- **Optimization**: Pre-compute room connectivity graph, cache BFS results
- **Typical Time**: ~0.05-0.2s per dungeon (3 floors, 6 rooms each)

#### Continent Operations
- **Bottleneck**: Tile-level distance calculations during continent tightening
- **Optimization**: Spatial hash grid + bbox fallback
- **Typical Time**: ~0.5-2s for 6 continents with 35 regions

#### Memory Usage
- **Tile Storage**: ~100-200 bytes per tile (Python overhead)
- **Typical World**: 30-40 regions × 1000 tiles = ~30-40MB tile data
- **Large Worlds**: Can reach 100MB+ with many regions/dungeons

### Debugging Tools

#### Visualize Region Shape
```python
def print_region_tiles(tiles, bbox=None):
    if not tiles:
        return
    if bbox is None:
        xs = [x for x, _ in tiles]
        ys = [y for _, y in tiles]
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)
    else:
      minx, maxx, miny, maxy = bbox
    
    for y in range(miny, maxy + 1):
        row = []
        for x in range(minx, maxx + 1):
            row.append('?' if (x, y) in tiles else ' ')
        print(''.join(row))

# Usage
region_tiles = set(region.tiles.keys())
print_region_tiles(region_tiles)
```

#### Validate Dungeon Connectivity
```python
def validate_dungeon_paths(dungeon):
    """Check that all rooms are reachable from entrance."""
 from collections import deque
    
    start = dungeon.get_player_start_position()
    if not start:
 return False, "No start position"
    
    visited = set()
  queue = deque([start])
    
    while queue:
        pos = queue.popleft()
        if pos in visited:
      continue
        visited.add(pos)
        
     tile = dungeon.get_tile(*pos)
        if not tile or not tile.passable:
     continue
        
        # Check 4 neighbors + stairs
        x, y, z = pos
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            queue.append((x+dx, y+dy, z))
        if tile.has_stairs_up:
            queue.append((x, y, z+1))
 if tile.has_stairs_down:
      queue.append((x, y, z-1))
    
    total_passable = sum(1 for t in dungeon.tiles.values() if t.passable)
return len(visited) == total_passable, f"{len(visited)}/{total_passable} tiles reachable"

# Usage
valid, msg = validate_dungeon_paths(my_dungeon)
print(f"Dungeon valid: {valid} ({msg})")
```

#### Check Continent Distribution
```python
def analyze_continent_distribution(result):
    """Print continent size and composition stats."""
    for i, comp in enumerate(result["continent_compositions"]):
  cities = comp["city_names"]
        print(f"Continent {comp['continent_number']}:")
        print(f"  Cities: {len(cities)}")
    print(f"  Names: {', '.join(cities)}")
        
        bbox = result["continents"][i]
        width = bbox[1] - bbox[0]
        height = bbox[3] - bbox[2]
        print(f"  Size: {width} × {height} tiles")
        print()

# Usage
result = build_continents_and_ocean(pg, 6, 12345, 140, 10)
analyze_continent_distribution(result)
```

---

## Version History

- **v1.0** - Initial documentation covering all 8 service modules
- Future: Will be updated as new generation algorithms are added

---

## Contact

For questions or issues with procedural generation services, refer to:
- `game/objects/city.py` - City data structures
- `game/objects/dungeon.py` - Dungeon data structures
- `game/objects/player_game.py` - World state management
- Individual service files for algorithm-specific details
