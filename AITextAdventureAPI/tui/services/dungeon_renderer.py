"""
dungeon_renderer: pure functions for composing the dungeon minimap grid.

Extracted from `old/game_screens/dungeon_screen.py`'s `_render_minimap()` —
rewritten to return data structures instead of printing to stdout. No Textual
imports, no I/O: every function is a pure transformation of Dungeon/PlayerGame
state into text that the `DungeonScreen` widget can set on a `Static`.

Tile legend (matches legacy):
  ☺  player
  .  passable floor (open_area_tile)
  #  impassable wall (impassable_tile)
  ?  undiscovered
  *  perimeter (empty cell adjacent to a known tile)
  ß  NPC entity
  ◘  item entity
  ↕  stairs up + down
  ↓  stairs up (displayed inverted: going deeper)
  ↑  stairs down (origin / surface)
"""
from __future__ import annotations

from typing import Any, List, Optional


# ── per-tile character lookup ──────────────────────────────────────────────

def _tile_char(dungeon: Any, wx: int, wy: int, z: int, reveal_all: bool) -> str:
    """Return the display character for world coordinate (wx, wy, z).
    Mirrors the inner loop of `old/game_screens/dungeon_screen._render_minimap()`.
    """
    from game.objects.player import ItemType  # noqa: PLC0415

    tile = dungeon.get_tile(wx, wy, z)
    if tile is None:
        return " "

    visible = reveal_all or tile.discovered
    if not visible:
        return "?"

    ch = dungeon.open_area_tile if tile.passable else dungeon.impassable_tile

    if tile.entities:
        for ent in tile.entities:
            if isinstance(ent, dict) and ent.get("type") == "npc":
                ch = "ß"
                break
            if isinstance(ent, ItemType):
                ch = "◘"

    # stairs markers override entity marks for visibility
    has_up = getattr(tile, "has_stairs_up", False)
    has_down = getattr(tile, "has_stairs_down", False)
    if has_up and has_down:
        ch = "↕"
    elif has_up:
        ch = "↓"  # going deeper → displayed as ↓
    elif has_down:
        ch = "↑"  # back toward surface → displayed as ↑

    # origin marker
    if wx == 0 and wy == 0 and z == 0:
        ch = "↑"

    return ch


# ── full minimap viewport ──────────────────────────────────────────────────

def build_minimap_lines(
    dungeon: Any,
    view_w: int = 72,
    view_h: int = 23,
    reveal_all: bool = False,
) -> List[str]:
    """Return a list of `view_h` strings, each `view_w` characters wide,
    representing the dungeon minimap centered on the player.  No borders —
    the caller (DungeonScreen) handles Textual widget layout.

    Mirrors `old/game_screens/dungeon_screen._render_minimap()`.
    """
    player_pos = dungeon.get_player_pos()
    if player_pos is None:
        return ["(no player position)" for _ in range(view_h)]

    px, py, pz = player_pos
    z = pz

    # compute world offset so the player is centered
    ox = px - view_w // 2
    oy = py - view_h // 2

    # build grid
    grid: List[List[str]] = [[" " for _ in range(view_w)] for _ in range(view_h)]

    for gy in range(view_h):
        for gx in range(view_w):
            wx = ox + gx
            wy = oy + gy
            grid[gy][gx] = _tile_char(dungeon, wx, wy, z, reveal_all)

    # mark perimeter: any ' ' adjacent to a known (non-space) tile becomes '*'
    for gy in range(view_h):
        for gx in range(view_w):
            if grid[gy][gx] != " ":
                continue
            for ddx, ddy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx2, ny2 = gx + ddx, gy + ddy
                if 0 <= nx2 < view_w and 0 <= ny2 < view_h:
                    t = dungeon.get_tile(nx2 + ox, ny2 + oy, z)
                    if t and (reveal_all or t.discovered):
                        grid[gy][gx] = "*"
                        break

    # remaining spaces become '?'
    for gy in range(view_h):
        for gx in range(view_w):
            if grid[gy][gx] == " ":
                grid[gy][gx] = "?"

    # player marker at center
    cx, cy = view_w // 2, view_h // 2
    if 0 <= cx < view_w and 0 <= cy < view_h:
        grid[cy][cx] = "☺"

    return ["".join(row) for row in grid]


# ── header ─────────────────────────────────────────────────────────────────

def build_header(dungeon: Any) -> str:
    """Return a header string for the dungeon screen."""
    player_pos = dungeon.get_player_pos()
    if player_pos is None:
        return dungeon.display_name
    _, _, z = player_pos
    return f"{dungeon.display_name}  —  Floor {z + 1}"


# ── stats panel ────────────────────────────────────────────────────────────

def build_stats_lines(dungeon: Any, pg: Any) -> List[str]:
    """Return text lines for the stats sidebar.
    Shows party HP/level, floor info, and nearby entities.
    """
    lines: List[str] = ["─── Party ───"]
    try:
        party = pg.get_active_party()
        for p in party:
            hp = getattr(p, "current_hp", "?")
            max_hp = getattr(p, "max_hp", "?")
            level = getattr(p, "level", "?")
            name = getattr(p, "name", "?")
            lines.append(f" {name}")
            lines.append(f"   Lv {level}  HP {hp}/{max_hp}")
    except Exception:
        lines.append(" (unavailable)")

    lines.append("")
    lines.append("─── Floor ───")
    player_pos = dungeon.get_player_pos()
    if player_pos:
        px, py, pz = player_pos
        lines.append(f" Z:{pz + 1}  ({px},{py})")
    else:
        lines.append(" ?")

    lines.append("")
    lines.append("─── Legend ───")
    lines.append(" ☺ You")
    lines.append(" ß NPC")
    lines.append(" ◘ Item")
    lines.append(" ↑ Surface/Exit")
    lines.append(" ↓ Deeper")
    lines.append(" ↕ Both stairs")

    # nearby entities on current floor
    entity_locs = dungeon.get_all_entity_locations()
    if entity_locs and player_pos:
        lines.append("")
        lines.append("─── Nearby ───")
        ppos = player_pos[:2]
        for ex, ey, ez, kind in entity_locs:
            if ez == player_pos[2]:
                dist = abs(ex - player_pos[0]) + abs(ey - player_pos[1])
                lines.append(f" {kind}  ({ex},{ey})  d{dist}")

    return lines