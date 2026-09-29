import math
import random
from typing import Dict, Any, List, Tuple, Optional
from game.objects.dungeon import Dungeon, DungeonTile, DungeonTileType
from game.objects.player import ItemType

# assumes Dungeon and DungeonTile are imported from your module



class DungeonBuilder:
    def __init__(self, settings: Dict[str, Any]):
        self.settings = settings
        # seed handling � you can pass an int or a string; strings get hashed
        seed = settings.get("seed")
        self.dungeon_id = settings["dungeon_id"]
        self.rng = random.Random(abs(hash(seed)))
        self.floor_count = settings.get("floor_count",1)
        self.room_size_min_max = settings["room_size_min_max"] # (min_area, max_area)
        self.rooms_per_floor = settings["rooms_per_floor"]
        self.max_neighbors_per_room = settings["max_neighbors_per_room"]
        self.additional_connection_chance = settings.get("additional_connection_chance", 0.0)
        self.min_max_distance_between_rooms = settings["min_max_distance_between_rooms"]  # (min, max)
        self.min_max_corridor_width = settings["min_max_corridor_width"]  # (min_w, max_w)
        #DUNGEON_NPCS = [ {'id': 'zaruun','location': 'final_chamber'} ]
        self.npcs_spec = settings.get("npcs", [])
        #DUNGEON_ITEMS = [ {'id': 'herb_major', 'location': 'treasure_room'} ]
        self.item_specs = settings.get("items", [])

        self.display_name = settings.get("display_name", "Unnamed Dungeon")
        self.impassable_chance = settings.get("impassable_chance", 0.05)
        self.open_area_tile = settings.get("open_area_tile", None)
        self.impassable_tile = settings.get("impassable_tile", None)
        self.visible_distance = settings.get("visible_distance", 5)
        # DUNGEON_SETTINGS: Dict[str, Any] = {
        #     "dungeon_id": "rokhuld_lair",
        #     "seed": abs(hash("rokhuld_lair")),
        #     "floor_count": 1,
        #     "room_size_min_max": (81, 120),  # a 9x9 area is 81
        #     "rooms_per_floor": 6,
        #     "max_neighbors_per_room": 2,
        #     "additional_connection_chance": 0.0,
        #     "min_max_distance_between_rooms": (5,12),
        #     "min_max_corridor_width": (3,6),
        #     "display_name": "Rokhuld's Deep Core",
        #     "open_area_tile": OPEN_AREA_TILE,
        #     "impassable_tile": IMPASSABLE_TILE,
        #     "impassable_chance": IMPASSABLE_CHANCE,
        #     "floor_hostiles": FLOOR_HOSTILES,
        #     "hostile_seeds": HOSTILE_SEEDS,
        #     "npcs": NPCS  
        # }

        # grid size: we�ll derive from a loose bound; you can later bake this per dungeon

        # runtime structures
        self.rooms: List[Dict[str, Any]] = [] # per-floor rooms
        # collect rooms across all floors for final/treasure marking
        self.all_rooms: List[Dict[str, Any]] = []
        # global unique room id counter
        self.room_id_counter: int =0
        self.invalid_impassable_positions: Dict[Tuple[int, int, int], Any] = {}



    # ---------------------------
    # Public entrypoint
    # ---------------------------
    def build(self) -> Dungeon:
        dungeon = Dungeon(levels=self.floor_count,
                          dungeon_id=self.dungeon_id)

        # Reset per-build state so a reused builder never carries impassable
        # coordinates from a previously generated dungeon: those coordinates
        # describe a different tile layout and would wrongly skip valid
        # placements (or hit stale "blocks_required_path" entries).
        self.invalid_impassable_positions = {}
        self.all_rooms = []
        self.room_id_counter = 0

        dungeon.display_name = self.display_name
        dungeon.open_area_tile = self.open_area_tile
        dungeon.impassable_tile = self.impassable_tile
        dungeon.impassable_chance = self.impassable_chance
        dungeon.visible_distance = self.visible_distance
        dungeon.open_area_color = self.settings.get("open_area_color", None)
        dungeon.impassable_color = self.settings.get("impassable_color", None)
        dungeon.border_tile = self.settings.get("border_tile", "*")
        dungeon.border_color = self.settings.get("border_color", None)

        # Build each floor independently. Align next floor under previous exit stair.
        prev_exit_xy: Optional[Tuple[int,int]] = None
        for z in range(self.floor_count):
            # reset per-floor rooms
            self.rooms = []

            #1. create first room around center for this floor
            # if prev_exit_xy is set, center the first room on that coordinate so floors align vertically
            if prev_exit_xy is not None:
                self._create_first_room(z, center=prev_exit_xy)
            else:
                self._create_first_room(z)

            #2�5. expand graph, place rooms, connect them
            self._grow_rooms()

            # add these rooms to the global room list
            # ensure rooms have globally unique ids (they are assigned when created)
            self.all_rooms.extend(self.rooms)

            # carve rooms into the dungeon tiles for this floor
            for room in self.rooms:
                self._carve_room(dungeon, room, z)

            # carve corridors between connected rooms on this floor
            carved_pairs = set()
            for room in self.rooms:
                for neighbor_id in room['neighbors']:
                    pair = tuple(sorted((room['id'], neighbor_id)))
                    if pair in carved_pairs:
                        continue
                    carved_pairs.add(pair)
                    neighbor = self._get_room_by_id(neighbor_id)
                    self._carve_corridor(dungeon, room, neighbor, z)

            # Mark entrance for floor0: label the entire first room as the
            # ENTRANCE (mirrors how FINAL_CHAMBER / TREASURE_ROOM cover a whole
            # room), and put the player on the room center. The single center
            # tile at origin is reserved for the player, so entities placed at
            # the 'entrance' location have the rest of the room to occupy.
            if z ==0 and self.rooms:
                start_room = self.rooms[0]
                sx = start_room['x'] + start_room['w'] //2
                sy = start_room['y'] + start_room['h'] //2
                for yy in range(start_room['y'], start_room['y'] + start_room['h']):
                    for xx in range(start_room['x'], start_room['x'] + start_room['w']):
                        t = dungeon.get_tile(xx, yy, z)
                        if t and t.passable:
                            t.tile_type = DungeonTileType.ENTRANCE
                try:
                    dungeon.set_player_pos(sx, sy, z)
                except Exception:
                    pass
            
            # After carving rooms and corridors for this floor, choose an exit stair location
            # pick the room farthest from this floor's start (self.rooms[0]) and mark its center as stair up
            if self.rooms:
                floor_start = self.rooms[0]
                fsx = floor_start['x'] + floor_start['w'] //2
                fsy = floor_start['y'] + floor_start['h'] //2
                def room_center_local(r):
                    return (r['x'] + r['w'] //2, r['y'] + r['h'] //2)
                exit_room = max(self.rooms, key=lambda r: (room_center_local(r)[0] - fsx) **2 + (room_center_local(r)[1] - fsy) **2)
                ex = exit_room['x'] + exit_room['w'] //2
                ey = exit_room['y'] + exit_room['h'] //2
                # ensure a tile exists at exit location
                exit_tile = dungeon.get_tile(ex, ey, z)
                if exit_tile is None:
                    dungeon.tiles[(ex, ey, z)] = DungeonTile(x=ex, y=ey, z=z, passable=True)
                    exit_tile = dungeon.get_tile(ex, ey, z)
                # Don't mark stairs up on final top floor
                if z < self.floor_count -1:
                    exit_tile.has_stairs_up = True
                    dungeon.stairs.append((ex, ey, z, 'up'))
                    # record exit for next floor alignment
                    prev_exit_xy = (ex, ey)
                else:
                    prev_exit_xy = None

        # After building all floors, determine final chamber as farthest room from start across all_rooms
        final_room = None
        if self.all_rooms:
            # find start room center (first room of floor0 is the one with z==0 and the smallest id on that floor)
            start_room = next((r for r in self.all_rooms if r['z'] ==0), self.all_rooms[0])
            sx = start_room['x'] + start_room['w'] //2
            sy = start_room['y'] + start_room['h'] //2

            print (f'start room {start_room}')
            def room_center(room):
                return (room['x'] + room['w'] //2, room['y'] + room['h'] //2)

            farthest_room = max(
                self.all_rooms,
                key=lambda r: (room_center(r)[0] - sx) **2 + (room_center(r)[1] - sy) **2
            )
            final_room = farthest_room

            # mark inner area of farthest room as final chamber
            rx1 = final_room['x'] +1
            ry1 = final_room['y'] +1
            rx2 = final_room['x'] + final_room['w'] -2
            ry2 = final_room['y'] + final_room['h'] -2
            z = final_room.get('z',0)
            #print (f'final room {final_room} at z={z}')
            if rx1 <= rx2 and ry1 <= ry2:
                for nx in range(rx1, rx2 +1):
                    for ny in range(ry1, ry2 +1):
                        t = dungeon.get_tile(nx, ny, z)
                        if t and t.passable:
                            #print (f'Marking final chamber tile at ({nx},{ny},{z})')
                            t.tile_type = DungeonTileType.FINAL_CHAMBER

            #input(f'Final chamber set at room id {final_room["id"]} on floor {final_room.get("z",0)}')
            
        # Mark other rooms (non-entrance, non-final) as TREASURE_ROOM
        entrance_id = None
        final_id = None
        if self.all_rooms:
            entrance_room = next((r for r in self.all_rooms if r['z'] ==0), None)
            if entrance_room:
                entrance_id = entrance_room['id']
            if final_room is not None:
                final_id = final_room['id']

        for room in self.all_rooms:
            rid = room['id']
            if rid == entrance_id and room['z'] ==0:
                continue
            if final_id is not None and rid == final_id and room['z'] == final_room.get('z'):
                continue
            # mark entire room floor as TREASURE_ROOM but don't overwrite explicit types
            for yy in range(room['y'], room['y'] + room['h']):
                for xx in range(room['x'], room['x'] + room['w']):
                    t = dungeon.get_tile(xx, yy, room.get('z',0))
                    if t and t.passable and t.tile_type is None:
                        t.tile_type = DungeonTileType.TREASURE_ROOM

        # Ensure stairs down markers exist on floors above previous exit positions
        # For each stair 'up' recorded at (x,y,z), add a corresponding 'down' at (x,y,z+1) if a tile exists
        for (sx, sy, sz, dir) in list(dungeon.stairs):
            if dir == 'up':
                up_pos = (sx, sy, sz +1)
                t = dungeon.get_tile(*up_pos)
                if t is None:
                    # create tile under the stair to ensure linkage
                    dungeon.tiles[up_pos] = DungeonTile(x=sx, y=sy, z=sz +1, passable=True)
                    t = dungeon.get_tile(*up_pos)
                if t:
                    t.has_stairs_down = True
                    dungeon.stairs.append((t.x, t.y, t.z, 'down'))

        #6. perimeter sweep / naturalization � left as a later polish hook
        for z in range(self.floor_count):
            self._naturalize(dungeon,z)

        #7. place npcs based on special locations like 'final_chamber'
        self._place_npcs_and_items(dungeon)

        # (8) loot � hook for later

        #9. replace passable tiles with impassable tiles to "add rocks"
        # Collect the connectivity targets a single time across the whole
        # dungeon (all floors' rooms + all placed entities) so obstacle
        # placement can never disconnect an earlier floor's room or entrance.
        required_targets = self._collect_required_targets(dungeon)
        for z in range(self.floor_count):
            self._add_impassables(dungeon, z, required_targets)

        return dungeon

    def _add_impassables(self, dungeon: Dungeon, z: int, required_targets: List[Tuple[int, int, int]]) -> None:
        """
        Randomly replaces some passable tiles with impassable tiles to add obstacles.
        """
        impassable_count =0
        not_passable =0
        for (x, y, tz), tile in dungeon.tiles.items():
            if tz != z:
                #print(f'Skipping tile at z={tz}, looking for z={z}')
                continue
            if tile.passable:
                # Roll the impassable chance FIRST. The blocking-path check below
                # runs a full BFS sweep over the dungeon, so we must only pay
                # that cost for the small fraction of tiles we actually intend to
                # convert — otherwise build time explodes on large dungeons.
                if self.rng.random() >= dungeon.impassable_chance:
                    continue
                pos = (x, y, z)
                # ensure impassable tile placement is not on origin
                if not self.not_origin(pos):
                    continue
                if pos in self.invalid_impassable_positions:
                    continue
                # Single BFS from origin with this tile blocked; verify every
                # required target (room + npc) is still reachable.
                if not self._not_blocking_required_targets(pos, dungeon, required_targets):
                    self.invalid_impassable_positions[pos] = 'blocks_required_path'
                    continue
                #print(f'Converting tile at ({x},{y},{z}) to impassable')
                tile.passable = False
                impassable_count += 1
            else:
                not_passable +=1
        #input(f"Added {impassable_count} impassable tiles to dungeon {dungeon.id}... already not passable: {not_passable}")

    def _collect_required_targets(self, dungeon: Dungeon) -> List[Tuple[int, int, int]]:
        """Collect the set of tile coordinates that must remain reachable from
        origin: one representative passable tile per room (across every floor)
        plus every tile that currently holds an entity (NPC/item).
        """
        targets: List[Tuple[int, int, int]] = []
        seen: set = set()

        for room in self.all_rooms:
            cx = room['x'] + room.get('w', 1) // 2
            cy = room['y'] + room.get('h', 1) // 2
            cz = room.get('z', 0)
            center_tile = dungeon.get_tile(cx, cy, cz)
            if center_tile and center_tile.passable:
                room_goal = (cx, cy, cz)
            else:
                room_goal = None
                for yy in range(room['y'], room['y'] + room.get('h', 1)):
                    for xx in range(room['x'], room['x'] + room.get('w', 1)):
                        t = dungeon.get_tile(xx, yy, cz)
                        if t and t.passable:
                            room_goal = (xx, yy, cz)
                            break
                    if room_goal is not None:
                        break
            if room_goal is not None and room_goal not in seen:
                seen.add(room_goal)
                targets.append(room_goal)

        for tile in dungeon.tiles.values():
            if tile.entities and len(tile.entities) > 0:
                npc_pos = (tile.x, tile.y, tile.z)
                if npc_pos not in seen:
                    seen.add(npc_pos)
                    targets.append(npc_pos)

        return targets

    def _not_blocking_required_targets(self, position: Tuple[int, int, int], dungeon: Dungeon, required_targets: List[Tuple[int, int, int]]) -> bool:
        """Return True if blocking `position` still leaves every required target
        reachable from origin. Runs a single BFS instead of one per target."""
        if not required_targets:
            return True
        reachable = self._reachable_from_origin(position, dungeon)
        return all(target in reachable for target in required_targets)

    def not_origin(self, origin) -> bool:
        x, y, z = origin
        return not (x == 0 and y == 0 and z==0)

    def not_blocking_npc_paths(self, position: Tuple[int, int, int], dungeon: Dungeon) -> bool:
        # use dungeon_tile.entities for dungeon_tile in dungeon.tiles.items to find npc locations
        npc_positions = [(tile.x, tile.y, tile.z) for tile in dungeon.tiles.values() if tile.entities and len(tile.entities) > 0]
        if not npc_positions:
            return True
        # Single BFS from origin (with `position` blocked) instead of one BFS
        # per NPC: if every NPC tile is in the reachable set, none are cut off.
        reachable = self._reachable_from_origin(position, dungeon)
        return all(npc_pos in reachable for npc_pos in npc_positions)

    def _reachable_from_origin(self, block_position: Optional[Tuple[int, int, int]], dungeon: Dungeon) -> set:
        """Single BFS from origin (0,0,0) returning the set of reachable tile
        coordinates when the tile at `block_position` is treated as impassable.

        Movement is 4-directional on the same z-level plus stairs. The blocked
        tile's passable flag is restored before returning so the dungeon is not
        permanently mutated. Callers test target membership against the result,
        which is far cheaper than running an independent BFS per target.
        """
        from collections import deque

        origin = (0, 0, 0)
        blocked_tile = dungeon.get_tile(*block_position) if block_position else None
        orig_blocked_state = None
        visited: set = set()
        try:
            if blocked_tile:
                orig_blocked_state = blocked_tile.passable
                blocked_tile.passable = False

            start_tile = dungeon.get_tile(*origin)
            if not start_tile or not start_tile.passable:
                return visited

            q = deque([origin])
            visited.add(origin)
            while q:
                x, y, z = q.popleft()
                neighbors = [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z)]
                cur_tile = dungeon.get_tile(x, y, z)
                if cur_tile:
                    if cur_tile.has_stairs_up:
                        neighbors.append((x, y, z + 1))
                    if cur_tile.has_stairs_down:
                        neighbors.append((x, y, z - 1))
                for npos in neighbors:
                    if npos in visited:
                        continue
                    nt = dungeon.get_tile(*npos)
                    if not nt or not nt.passable:
                        continue
                    visited.add(npos)
                    q.append(npos)
            return visited
        finally:
            if blocked_tile and orig_blocked_state is not None:
                blocked_tile.passable = orig_blocked_state

    #start is always origin (0,0,0)
    def path_exists_if_location_blocked(self, goal: Tuple[int, int, int], block_position: Tuple[int, int, int], dungeon: Dungeon) -> bool:
        """Return True if there exists any path from origin (0,0,0) to goal when
        the tile at `block_position` is considered blocked (impassable).

        Uses breadth-first search on the dungeon's tiles. Movement allowed in
        4 cardinal directions on the same z-level, and via stairs if present.
        The dungeon object is not mutated permanently: the passable flag for the
        blocked tile is restored after the check.
        """
        from collections import deque

        origin = (0, 0, 0)

        # Quick checks
        if goal == origin:
            return True

        goal_tile = dungeon.get_tile(*goal)
        if not goal_tile or not goal_tile.passable:
            #print(f'Goal tile at {goal} is not passable or does not exist: {goal_tile}')
            return False

        # Save original passable state for block_position (if any)
        blocked_tile = dungeon.get_tile(*block_position) if block_position else None
        orig_blocked_state = None
        try:
            if blocked_tile:
                orig_blocked_state = blocked_tile.passable
                #input(f'Forcing block of tile at {block_position}')
                blocked_tile.passable = False

            start_tile = dungeon.get_tile(*origin)
            if not start_tile or not start_tile.passable:
                return False

            q = deque()
            visited = set()
            q.append(origin)
            visited.add(origin)

            while q:
                x, y, z = q.popleft()
                # neighbors:4-directional on the same z
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny, nz = x + dx, y + dy, z
                    if (nx, ny, nz) in visited:
                        continue
                    nt = dungeon.get_tile(nx, ny, nz)
                    if not nt or not nt.passable:
                        continue
                    if (nx, ny, nz) == goal:
                        return True
                    visited.add((nx, ny, nz))
                    q.append((nx, ny, nz))

                # stairs: allow moving up/down if tile has stairs
                cur_tile = dungeon.get_tile(x, y, z)
                if cur_tile:
                    if cur_tile.has_stairs_up:
                        nx, ny, nz = x, y, z + 1
                        if (nx, ny, nz) not in visited:
                            nt = dungeon.get_tile(nx, ny, nz)
                            if nt and nt.passable:
                                if (nx, ny, nz) == goal:
                                    return True
                                visited.add((nx, ny, nz))
                                q.append((nx, ny, nz))
                    if cur_tile.has_stairs_down:
                        nx, ny, nz = x, y, z - 1
                        if (nx, ny, nz) not in visited:
                            nt = dungeon.get_tile(nx, ny, nz)
                            if nt and nt.passable:
                                if (nx, ny, nz) == goal:
                                    return True
                                visited.add((nx, ny, nz))
                                q.append((nx, ny, nz))

            return False
        finally:
            # restore blocked tile passable state
            if blocked_tile and orig_blocked_state is not None:
                blocked_tile.passable = orig_blocked_state

    def not_blocking_connections(self, position: Tuple[int, int, int], dungeon: Dungeon) -> bool:
        # Single BFS from origin (with `position` blocked); then verify every
        # room still has at least one reachable passable tile. This replaces the
        # previous one-BFS-per-room approach.
        reachable = self._reachable_from_origin(position, dungeon)
        for room in self.rooms:
            cx = room['x'] + room.get('w', 1) // 2
            cy = room['y'] + room.get('h', 1) // 2
            cz = room.get('z', 0)
            center_tile = dungeon.get_tile(cx, cy, cz)
            if center_tile and center_tile.passable:
                room_goal = (cx, cy, cz)
            else:
                room_goal = None
                for yy in range(room['y'], room['y'] + room.get('h', 1)):
                    for xx in range(room['x'], room['x'] + room.get('w', 1)):
                        t = dungeon.get_tile(xx, yy, cz)
                        if t and t.passable:
                            room_goal = (xx, yy, cz)
                            break
                    if room_goal is not None:
                        break
            # if we couldn't find any floor tile for this room, nothing to verify
            if room_goal is None:
                continue
            if room_goal not in reachable:
                return False
        return True



    def _naturalize(self, dungeon: Dungeon, z: int) -> None:
        """
            Should sweep the perimiter one time adding randomize frontier path to8 directional tiles as long as this does not create new connections between rooms.
            a single sweep will un-square the edges
        """
        # gather perimeter tiles
        perimiter_array = []
        for (x, y, tz), tile in dungeon.tiles.items():
            if tz != z:
                continue
            if not tile.passable:
                # check8 directions for any passable tile
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        if dx ==0 and dy ==0:
                            continue
                        neighbor = dungeon.get_tile(x + dx, y + dy, z)
                        if neighbor and neighbor.passable:
                            perimiter_array.append((x, y))
                            break
                    else:
                        continue
                    break
        # attempt to naturalize each perimiter tile
        for (x, y) in perimiter_array:
            if self.rng.random() <0.3: #30% chance to naturalize
                key = (x, y, z)
                t = dungeon.tiles.get(key)
                if t is None:
                    # create tile and try to infer an appropriate tile_type
                    inferred_type = None
                    # look for an adjacent passable tile that has a tile_type set
                    for dx in [-1,0,1]:
                        for dy in [-1,0,1]:
                            if dx ==0 and dy ==0:
                                continue
                            nb = dungeon.get_tile(x + dx, y + dy, z)
                            if nb and nb.passable and nb.tile_type is not None:
                                inferred_type = nb.tile_type
                                break
                        if inferred_type is not None:
                            break
                    # default to corridor when no inference possible
                    if inferred_type is None:
                        inferred_type = DungeonTileType.CORRIDOR

                    dungeon.tiles[key] = DungeonTile(x=x, y=y, z=z, passable=True, tile_type=inferred_type)
                else:
                    t.passable = True
                    # if tile has no explicit tile_type, try to infer from neighbors
                    if t.tile_type is None:
                        inferred_type = None
                        for dx in [-1,0,1]:
                            for dy in [-1,0,1]:
                                if dx ==0 and dy ==0:
                                    continue
                                nb = dungeon.get_tile(x + dx, y + dy, z)
                                if nb and nb.passable and nb.tile_type is not None:
                                    inferred_type = nb.tile_type
                                    break
                            if inferred_type is not None:
                                break
                        if inferred_type is None:
                            inferred_type = DungeonTileType.CORRIDOR
                        t.tile_type = inferred_type
        

    # ---------------------------
    # Room construction
    # ---------------------------
    def _create_first_room(self, z:int, center: Optional[Tuple[int,int]] = None):
        min_area, max_area = self.room_size_min_max
        area = self.rng.randint(min_area, max_area)
        side = int(math.sqrt(area))
        w = max(3, side)
        h = max(3, side)

        # First room centered at world origin (0,0)
        if center is not None:
            x, y = center
        else:
            x = -w //2
            y = -h //2

        # assign a globally unique id
        rid = self.room_id_counter
        self.room_id_counter +=1

        room = {
            'id': rid,
            'x': x,
            'y': y,
            'z': z,
            'w': w,
            'h': h,
            'neighbors': []
        }
        self.rooms.append(room)

    def _grow_rooms(self):
        target = self.rooms_per_floor

        # use global counter to ensure unique ids across floors
 
        while len(self.rooms) < target:
            parent = self.rng.choice(self.rooms)
            if len(parent['neighbors']) >= self.max_neighbors_per_room:
                # try another parent, but don't get stuck forever
                # if all saturated and additional_connection_chance == 0, we break
                if all(len(r['neighbors']) >= self.max_neighbors_per_room for r in self.rooms):
                    break
                continue

            # assign a new global id
            new_id = self.room_id_counter
            self.room_id_counter +=1
            new_room = self._attempt_place_room_near(parent, new_id)
            if new_room is None:
                # failed to place; try another parent
                continue

            # connect parent <-> new room
            parent['neighbors'].append(new_room['id'])
            new_room['neighbors'].append(parent['id'])

            self.rooms.append(new_room)

        # optional: additional connections between random rooms
        if self.additional_connection_chance > 0.0:
            for i, room in enumerate(self.rooms):
                if self.rng.random() < self.additional_connection_chance:
                    other = self.rng.choice(self.rooms)
                    if other['id'] == room['id']:
                        continue
                    if other['id'] not in room['neighbors']:
                        room['neighbors'].append(other['id'])
                        other['neighbors'].append(room['id'])

    def _attempt_place_room_near(self, parent: Dict[str, Any], new_id: int) -> Optional[Dict[str, Any]]:
        min_area, max_area = self.room_size_min_max
        area = self.rng.randint(min_area, max_area)
        side = int(math.sqrt(area))
        w = max(3, side)
        h = max(3, side)

        min_dist, max_dist = self.min_max_distance_between_rooms

        for _ in range(32):  # safety limit
            # pick a direction: up, down, left, right
            dx, dy = self.rng.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            dist = self.rng.randint(min_dist, max_dist)

            # place relative to parent edge
            if dx == 1:  # to the right
                x = parent['x'] + parent['w'] + dist
                y = parent['y'] + self.rng.randint(-parent['h']//2, parent['h']//2)
                z = parent['z']
            elif dx == -1:  # to the left
                x = parent['x'] - dist - w
                y = parent['y'] + self.rng.randint(-parent['h']//2, parent['h']//2)
                z = parent['z']
            elif dy == 1:  # below
                x = parent['x'] + self.rng.randint(-parent['w']//2, parent['w']//2)
                y = parent['y'] + parent['h'] + dist
                z = parent['z']
            else:  # above
                x = parent['x'] + self.rng.randint(-parent['w']//2, parent['w']//2)
                y = parent['y'] - dist - h
                z = parent['z']

            # # clamp roughly into map bounds
            # x = max(1, min(self.width - w - 1, x))
            # y = max(1, min(self.height - h - 1, y))

            candidate = {'id': new_id, 'x': x, 'y': y, 'w': w, 'h': h, 'z': z, 'neighbors': []}  # include z in candidate
            if not self._overlaps_any_room(candidate):
                return candidate

        return None  # failed to find a spot

    def _overlaps_any_room(self, candidate: Dict[str, Any]) -> bool:
        cx1, cy1, cx2, cy2 = self._room_bounds(candidate)
        for room in self.rooms:
            rx1, ry1, rx2, ry2 = self._room_bounds(room)
            # add a 1-tile padding to avoid touching walls unless you want that
            if cx1 <= rx2 + 1 and cx2 >= rx1 - 1 and cy1 <= ry2 + 1 and cy2 >= ry1 - 1:
                return True
        return False

    @staticmethod
    def _room_bounds(room: Dict[str, Any]) -> Tuple[int, int, int, int]:
        x1 = room['x']
        y1 = room['y']
        x2 = x1 + room['w'] - 1
        y2 = y1 + room['h'] - 1
        return x1, y1, x2, y2

    def _get_room_by_id(self, room_id: int) -> Dict[str, Any]:
        for r in self.rooms:
            if r['id'] == room_id:
                return r
        raise KeyError(f"Room id {room_id} not found")

    # ---------------------------
    # Carving into Dungeon tiles
    # ---------------------------
    def _carve_room(self, dungeon: Dungeon, room: Dict[str, Any], z: int) -> None:
        for y in range(room['y'], room['y'] + room['h']):
            for x in range(room['x'], room['x'] + room['w']):
                # create floor tile (passable) instead of relying on existing bounds
                if 0 <= z < dungeon.levels:
                    key = (x, y, z)
                    t = dungeon.tiles.get(key)
                    if t is None:
                        dungeon.tiles[key] = DungeonTile(x=x, y=y, z=z, passable=True)
                    else:
                        t.passable = True

    def _carve_corridor(self, dungeon: Dungeon, a: Dict[str, Any], b: Dict[str, Any], z: int) -> None:
        # pick random points inside each room as corridor endpoints
        ax = self.rng.randint(a['x'] + 1, a['x'] + a['w'] - 2)
        ay = self.rng.randint(a['y'] + 1, a['y'] + a['h'] - 2)
        bx = self.rng.randint(b['x'] + 1, b['x'] + b['w'] - 2)
        by = self.rng.randint(b['y'] + 1, b['y'] + b['h'] - 2)

        min_w, max_w = self.min_max_corridor_width
        width = self.rng.randint(min_w, max_w)

        # simple L-shaped corridor: horizontal then vertical (or vice versa)
        if self.rng.random() < 0.5:
            self._carve_rect(dungeon, min(ax, bx), ay - width//2,
                             abs(bx - ax) + 1, width, z)
            self._carve_rect(dungeon, bx - width//2, min(ay, by),
                             width, abs(by - ay) + 1, z)
        else:
            self._carve_rect(dungeon, ax - width//2, min(ay, by),
                             width, abs(by - ay) + 1, z)
            self._carve_rect(dungeon, min(ax, bx), by - width//2,
                             abs(bx - ax) + 1, width, z)

    @staticmethod
    def _carve_rect(dungeon: Dungeon, x: int, y: int, w: int, h: int, z: int) -> None:
        for yy in range(y, y + h):
            for xx in range(x, x + w):
                # create floor tile (passable) instead of relying on in_bounds
                if 0 <= z < dungeon.levels:
                    key = (xx, yy, z)
                    t = dungeon.tiles.get(key)
                    if t is None:
                        dungeon.tiles[key] = DungeonTile(x=xx, y=yy, z=z, passable=True)
                        # mark as corridor tile
                        dungeon.tiles[key].tile_type = DungeonTileType.CORRIDOR
                    else:
                        t.passable = True
                        # prefer not to overwrite an explicit final chamber or entrance
                        if t.tile_type is None:
                            t.tile_type = DungeonTileType.CORRIDOR

    # ---------------------------
    # NPC & ITEM placement
    # ---------------------------
    def _place_npcs_and_items(self, dungeon: Dungeon) -> None:
        from game.objects.item import instantiate_item_from_id
        if not self.npcs_spec and not self.item_specs:
            return

        for item in self.item_specs:
            #input (f'Placing item spec: {item}')
            loc = item.get("location")
            item_id = item.get("id")
            depth = item.get("depth")  # optional 0-100 depth percentage
            item = instantiate_item_from_id(item_id)
            dungeon.place_entity_at_location(item, DungeonTileType(loc), depth=depth)

        #npcs can block items... but may not be placed on the same tile
        for npc in self.npcs_spec:
            loc = npc.get("location")
            npc_id = npc.get("id")
            depth = npc.get("depth")  # optional 0-100 depth percentage
            entity = {'type': 'npc', 'npc_id': npc_id}
            dungeon.place_entity_at_location(entity, DungeonTileType(loc), depth=depth)

# ---------------------------
# Convenience entrypoint
# ---------------------------

def build_dungeon(dungeon_settings: Dict[str, Any]) -> Dungeon:
    builder = DungeonBuilder(dungeon_settings)
    return builder.build()
