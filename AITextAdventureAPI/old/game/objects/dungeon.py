from dataclasses import dataclass, field
from turtle import width
from typing import List, Optional, Tuple, Dict, Any
from enum import Enum
from game.objects.item import Item
import uuid

import game.constants as const
from combat_balancing_simulation.hostile_seed_engine import generate_hostile_from_legacy_seed


class DungeonTileType(Enum):
    FINAL_CHAMBER = 'final_chamber'
    TREASURE_ROOM = 'treasure_room'
    CORRIDOR = 'corridor'
    ENTRANCE = 'entrance'

@dataclass
class DungeonTile:
    x: int
    y: int
    z: int
    passable: bool = True
    discovered: bool = False
    sublocation: Optional[str] = None
    has_rest_point: bool = False
    has_stairs_up: bool = False
    has_stairs_down: bool = False
    tile_type: Optional[DungeonTileType] = None
    # placeholder for placed hostiles/items
    entities: List[Any] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            'x': self.x,
            'y': self.y,
            'z': self.z,
            'passable': self.passable,
            'discovered': self.discovered,
            'sublocation': self.sublocation,
            'has_rest_point': self.has_rest_point,
            'has_stairs_up': self.has_stairs_up,
            'has_stairs_down': self.has_stairs_down,
        }

class Dungeon:
    """Simple3D dungeon container.

    - coordinates: x,y per level (integer grid); z == level index (0..levels-1)
    - tiles stored as a dict keyed by world coordinates (x,y,z) -> DungeonTile
    - passable indicates walkable floor; non-passable is wall/impassable
    - entrances/exits will be represented as stairs placed on tiles
    - player position is stored on the dungeon instance (`player_pos`) so it is
      independent from any `PlayerGame` objects.
    """

    def __init__(
        self,
        levels: int = 1,
        dungeon_id: Optional[str] = None,
    ):
        self.id = dungeon_id or uuid.uuid4().hex
        self.levels = int(levels)

        self.display_name: str = "Unnamed Dungeon"
        self.open_area_tile: str = "."
        self.impassable_tile: str = "#"
        self.impassable_chance: float = 0.0
        self.visible_distance: int = 5
        self.position: Tuple[int, int] = (0, 0)  # x,y position in region/world map

        # ── tile display colours (#rrggbb strings or None for terminal default) ──
        self.open_area_color: Optional[str] = None
        self.impassable_color: Optional[str] = None
        # border_tile / border_color: the perimeter marker shown adjacent to known tiles
        self.border_tile: str = "*"
        self.border_color: Optional[str] = None

        # the player position within this dungeon (x,y,z) or None if not placed
        self.player_pos: Optional[Tuple[int, int, int]] = None

        # allocate tiles: store by world coords (x,y,z)
        self.tiles: Dict[Tuple[int, int, int], DungeonTile] = {}

        # convenience caches
        self.stairs: List[Tuple[int, int, int, str]] = [] # (x,y,z,dir) dir 'up' or 'down'
        self.locked: bool = False
        self.locked_text: List[str] = []

    def is_locked(self) -> bool:
        return self.locked if hasattr( self, 'locked') else False

    def set_locked_text(self, text_lines: List[str]) -> None:
        self.locked_text = text_lines
        
    def set_locked(self, locked: bool) -> None:
        self.locked = locked
    
    def path_exists(self, position: Tuple[int,int,int]):
        """ Ensure path exists with no impassable dungeon tiles or tiles with entities from the origin to the location.
        Movement allowed in4 cardinal directions on same z and via stairs if present.
        """
        from collections import deque

        origin = (0,0,0)
        # quick check
        if position == origin:
            return True

        start_tile = self.get_tile(origin[0], origin[1], origin[2])
        if not start_tile or not start_tile.passable:
            return False
        if start_tile.entities and len(start_tile.entities) >0:
            # origin occupied by entities — treat as blocked
            return False

        goal_tile = self.get_tile(position[0], position[1], position[2])
        if not goal_tile or not goal_tile.passable:
            return False
        if goal_tile.entities and len(goal_tile.entities) >0:
            return False

        q = deque()
        visited = set()
        q.append(origin)
        visited.add(origin)

        while q:
            x, y, z = q.popleft()
            # cardinal neighbors
            for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                nx, ny, nz = x + dx, y + dy, z
                if (nx, ny, nz) in visited:
                    continue
                nt = self.get_tile(nx, ny, nz)
                if not nt or not nt.passable:
                    continue
                if nt.entities and len(nt.entities) >0:
                    continue
                if (nx, ny, nz) == position:
                    return True
                visited.add((nx, ny, nz))
                q.append((nx, ny, nz))

            # stairs movement
            cur_tile = self.get_tile(x, y, z)
            if cur_tile:
                if cur_tile.has_stairs_up:
                    nx, ny, nz = x, y, z +1
                    if (nx, ny, nz) not in visited:
                        nt = self.get_tile(nx, ny, nz)
                        if nt and nt.passable and not (nt.entities and len(nt.entities) >0):
                            if (nx, ny, nz) == position:
                                return True
                            visited.add((nx, ny, nz))
                            q.append((nx, ny, nz))
                if cur_tile.has_stairs_down:
                    nx, ny, nz = x, y, z -1
                    if (nx, ny, nz) not in visited:
                        nt = self.get_tile(nx, ny, nz)
                        if nt and nt.passable and not (nt.entities and len(nt.entities) >0):
                            if (nx, ny, nz) == position:
                                return True
                            visited.add((nx, ny, nz))
                            q.append((nx, ny, nz))

        return False
    
    def hide_npc(self, npc: Any):
        # if the npc exists in the dungeon, remove it from its current tile
        npc_id = npc.id
        #input (f'Hiding npc {npc_id} from dungeon {self.id}')
        for tile in self.tiles.values():
            # noted  e = {'type': 'npc', 'npc_id': npc_id}
            entity = next((e for e in tile.entities if isinstance(e, dict) and e.get('npc_id') == npc_id), None)
            #print (f' Checking tile ({tile.x},{tile.y},{tile.z}) for npc {npc_id}, found entity: {entity}')
            if entity:
                tile.entities.remove(entity)
                #input   (f' NPC {npc_id} hidden from tile ({tile.x},{tile.y},{tile.z}) in dungeon {self.id}')
                return True

        #input (f'NPC {npc_id} not found in dungeon {self.id} to hide')

    def place_entity_at_location(self, entity: Any, location_type: DungeonTileType):
        lt = location_type

        # debug: list all tiles with matching tile_type
        all_tiles = [t for t in self.tiles.values() if t.tile_type == lt]
        #print(f'place_entity_at_location called for entity={entity} location_type={location_type} -> tiles with type={len(all_tiles)}')
        # for t in all_tiles:
        #     print(f' tile ({t.x},{t.y},{t.z}) passable={t.passable} entities={len(t.entities)} tile_type={t.tile_type}')

        # only consider tiles of the requested type that are reachable from origin
        candidates = []
        for tile in all_tiles:
            if not tile.passable:
                #print(f' skipping tile ({tile.x},{tile.y},{tile.z}) because not passable')
                continue
            # Do not place NPCs/items directly on stairs — this prevents blocking vertical movement.
            if tile.has_stairs_up or tile.has_stairs_down:
                continue
            # Ensure no entities
            if tile.entities:
                continue
            path_ok = self.path_exists((tile.x, tile.y, tile.z))
            #print(f' path check for ({tile.x},{tile.y},{tile.z}): {path_ok}')
            if path_ok:
                candidates.append(tile)

        if not candidates:
            print (f'No candidates found to place entity {entity} at location type {location_type}, ltvalue = {lt}')
            # extra diagnostics: show nearby tiles and why blocked
            for t in all_tiles:
                px = (t.x, t.y, t.z)
                print(f' diag tile {px}: passable={t.passable} entities={t.entities} -- path_exists={self.path_exists(px)}')
            # pause for debugging so you can inspect logs when running interactively
            try:
                input('DEBUG: no placement candidates found - press Enter to continue')
            except Exception:
                pass
            return False

        # choose candidate deterministically from dungeon and entity to keep placement stable
        import random
        key_hash = abs(hash(self.id))
        ent_hash = abs(hash(entity.name if isinstance(entity, Item) else entity.get('npc_id')))
        rng = random.Random((key_hash * ent_hash * max(1, len(self.get_all_entity_locations()))) % (10 **8))
        chosen_tile = rng.choice(candidates)
        chosen_tile.entities.append(entity)
        print(f'Placed entity {entity} at tile ({chosen_tile.x}, {chosen_tile.y}, {chosen_tile.z}) of type {lt}')
        return True

    def place_player_at_location(self, location_type: DungeonTileType):
        lt = location_type

        # debug: list all tiles with matching tile_type
        all_tiles = [t for t in self.tiles.values() if t.tile_type == lt]

        # only consider tiles of the requested type that are reachable from origin
        candidates = []
        for tile in all_tiles:
            if not tile.passable:
                #print(f' skipping tile ({tile.x},{tile.y},{tile.z}) because not passable')
                continue
            # Do not place NPCs/items directly on stairs — this prevents blocking vertical movement.
            if tile.has_stairs_up or tile.has_stairs_down:
                continue
            # Ensure no entities
            if tile.entities:
                continue
            path_ok = self.path_exists((tile.x, tile.y, tile.z))
            #print(f' path check for ({tile.x},{tile.y},{tile.z}): {path_ok}')
            if path_ok:
                candidates.append(tile)

        if not candidates:
            print (f'No candidates found to place player at location type {location_type}, ltvalue = {lt}')
            # extra diagnostics: show nearby tiles and why blocked
            for t in all_tiles:
                px = (t.x, t.y, t.z)
                print(f' diag tile {px}: passable={t.passable} entities={t.entities} -- path_exists={self.path_exists(px)}')
            # pause for debugging so you can inspect logs when running interactively
            try:
                input('DEBUG: no placement candidates found - press Enter to continue')
            except Exception:
                pass
            return False

        # choose candidate deterministically from dungeon and entity to keep placement stable
        import random
        rng = random.Random((max(1, len(self.get_all_entity_locations()))) % (10 **8))
        chosen_tile = rng.choice(candidates)
        self.set_player_pos(chosen_tile.x, chosen_tile.y, chosen_tile.z)
        return True

    def is_player_at_exit(self) -> bool:
        if self.player_pos is None:
            return False
        
        return self.player_pos == (0,0,0)

    def get_level_min_x(self, level: int) -> int:
        # gather all x values for tiles on this level
        xs = [x for (x, y, z) in self.tiles.keys() if z == level]

        if not xs:
            # no tiles exist yet on this level
            return 0

        return min(xs)        

    def get_level_min_y(self, level) -> int:
        # gather all y values for tiles on this level
        ys = [y for (x, y, z) in self.tiles.keys() if z == level]
        if not ys:
            # no tiles exist yet on this level
            return 0
        return min(ys)

    def get_level_width_height(self, level) -> Tuple[int, int]:
        # gather all x,y values for tiles on this level
        xs = [x for (x, y, z) in self.tiles.keys() if z == level]
        ys = [y for (x, y, z) in self.tiles.keys() if z == level]
        if not xs or not ys:
            # no tiles exist yet on this level
            return (0, 0)
        width = max(xs) - min(xs) + 1
        height = max(ys) - min(ys) + 1
        return (width, height)

    def in_bounds(self, x: int, y: int, z: int) -> bool:
        # interpret x,y as world coordinates; compute bounding box from existing tiles
        if not (0 <= z < self.levels):
            return False
        xs = [kx for (kx, ky, kz) in self.tiles.keys() if kz == z]
        ys = [ky for (kx, ky, kz) in self.tiles.keys() if kz == z]
        if not xs or not ys:
            return False
        min_x = min(xs)
        min_y = min(ys)
        max_x = max(xs)
        max_y = max(ys)
        return (min_x <= x <= max_x) and (min_y <= y <= max_y)

    def get_tile(self, x: int, y: int, z: int) -> Optional[DungeonTile]:
        # Return tile by world coordinates if present
        return self.tiles.get((x, y, z))

    def get_all_entity_locations(self) -> List[Tuple[int, int, int, Any]]:
        out: List[Tuple[int, int, int, Any]] = []
        for (x, y, z), tile in self.tiles.items():
            for entity in tile.entities:
                out.append((x, y, z, 'loot' if isinstance(entity, Item) else 'npc')) #'npc' if isinstance(entity, NPC) else 'loot'
        return out

    def reveal_tile(self, x: int, y: int, z: int) -> None:
        t = self.get_tile(x, y, z)
        if t:
            t.discovered = True

    def reveal_tiles_to_player(self) -> None:
        if self.player_pos is None:
            return
        px, py, pz = self.player_pos
        for dx in range(-self.visible_distance, self.visible_distance + 1):
            for dy in range(-self.visible_distance, self.visible_distance + 1):
                dist = abs(dx) + abs(dy)
                if dist <= self.visible_distance:
                    tx, ty = px + dx, py + dy
                    t = self.get_tile(tx, ty, pz)
                    if t:
                        t.discovered = True

    def iter_floor_positions(self, z: int) -> List[DungeonTile]:
        if not (0 <= z < self.levels):
            return []
        return [tile for (x, y, level), tile in self.tiles.items() if level == z]

    def remove_player_from_dungeon(self) -> None:
        self.player_pos = None

    # Player position management (stored on dungeon instance)
    def set_player_pos(self, x: int, y: int, z: int) -> bool:
        if not self.in_bounds(x, y, z):
            return False
        t = self.get_tile(x, y, z)
        if not t or not t.passable:
            return False
        self.player_pos = (x, y, z)
        # reveal the tile for player
        self.reveal_tiles_to_player()
        return True

    def get_player_pos(self) -> Optional[Tuple[int, int, int]]:
        return self.player_pos

    def move_player(self, dx: int, dy: int, dz: int = 0) -> bool:
        if self.player_pos is None:
            return False
        x, y, z = self.player_pos
        nx, ny, nz = x + dx, y + dy, z + dz
        if not self.in_bounds(nx, ny, nz):
            return False
        nt = self.get_tile(nx, ny, nz)
        if not nt or not nt.passable:
            return False
        self.player_pos = (nx, ny, nz)
        self.reveal_tiles_to_player()
        return True

    def iter_boss_locations(self) -> List[Dict[str, Any]]:
        return list(self.sub_boss_mobs) + list(self.boss_mob)

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'width': self.get_level_width_height(self.levels - 1)[0],
            'height': self.get_level_width_height(self.levels - 1)[1],
            'levels': self.levels,
            'tiles': [[[tile.to_dict() for tile in self.iter_floor_positions(z)] for z in range(self.levels)] for level in self.tiles],
            'player_pos': self.player_pos,
            'sub_boss_mobs': self.sub_boss_mobs,
            'boss_mob': self.boss_mob,
        }

    def get_boss_mob(self, pg, boss_mob_id):
        """
        Return list of hostiles for the given boss_mob_id, leveled to the player's max level.

        """
        for dungeon_settings in const.DUNGEON_SETTINGS:
            boss_mob = dungeon_settings.get('boss_mob', {})
            #print (F'Looking for boss mob ID: {boss_mob_id} in dungeon: {dungeon_settings.get("dungeon_id")}')
            if boss_mob.get('id') == boss_mob_id:
                hostiles = []
                for hostile_id in boss_mob.get('hostiles'):
                    boss_hostiles = dungeon_settings.get('boss_hostiles', [])
                    seed = None
                    for bh in boss_hostiles:
                        if bh.get('id') == hostile_id:
                            seed = bh
                            break

                    if seed is None:
                        print   (f'Hostile ID not found in boss hostiles: {hostile_id}')
                        continue
                    
                    hostile = generate_hostile_from_legacy_seed(seed, pg.get_max_character_level(), retain_abilities = True)
                    hostiles.append(hostile)
                    #print(f'Generated hostile for boss mob: {hostile_id} at level {pg.get_max_character_level()}')

                #input (f'Returning boss mob hostiles for boss mob ID: {boss_mob_id}')
                return hostiles

        #if boss mob nt found in dungeon settings, check world boss mobs
        for boss_mob in const.WORLD_BOSS_MOBS:
            if boss_mob.get('id') == boss_mob_id:
                boss_setting = boss_mob
                
                hostiles = []
                for hostile_id in boss_setting.get('hostiles', []):
        
                    #const.WORLD_HOSTILES
                    src_name = const.HOSTILE_SEED_PATHS.get(hostile_id)
                    seed = None
                    if src_name:
                        src_list = getattr(const, src_name, None)
                        if src_list:
                            #print (f'Found hostile seed source "{src_name}" for id "{hid}"')
                            seed = next((s for s in src_list if s.get('id') == hostile_id), None)

                    if seed is None:
                        # skip missing seed entry
                        continue
                    hostile = generate_hostile_from_legacy_seed(seed, pg.get_max_character_level(), retain_abilities=True)
                    hostiles.append(hostile)
                return hostiles


        input ("Boss mob ID not found: {}".format(boss_mob_id))
        return None

    def can_save(self) -> bool:
        """Return True only when the player is standing on a rest-point tile.

        Saving inside a dungeon is restricted to designated rest points.
        Returns False when the player has no position or the current tile
        does not have ``has_rest_point`` set.
        """
        if self.player_pos is None:
            return False
        tile = self.get_tile(*self.player_pos)
        return tile is not None and getattr(tile, "has_rest_point", False)
