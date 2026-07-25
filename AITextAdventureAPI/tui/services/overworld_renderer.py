"""
overworld_renderer: pure functions for composing the overworld map grid.

Extracted from `old/game_screens/overworld_screen.py`'s `display_viewport()`,
`_create_legend()`, and `get_road_or_alley_char()` — rewritten to return
data structures instead of printing to stdout. No Textual imports, no I/O:
every function is a pure transformation of PlayerGame state into text that
the `OverworldScreen` widget can set on a `Static`.
"""
from __future__ import annotations

from typing import Any, List, Optional, Tuple


# ── tile type constants (mirrors game.constants) ───────────────────────────
ROAD = "road"
ALLEY = "alley"
BUILDING = "building"

# Player/aircraft markers
PLAYER_CHAR = "☺"
AIRCRAFT_CHAR = "A"
UNKNOWN_CHAR = "?"

# Default viewport size (columns × rows of tiles visible)
DEFAULT_VIEW_W = 40
DEFAULT_VIEW_H = 22


# ── road/alley character selection ────────────────────────────────────────

def _get_road_or_alley_char(tile: Any, left_t: Any, up_t: Any, right_t: Any, down_t: Any) -> str:
    """Return the appropriate box-drawing character for a road or alley tile.
    Mirrors `old/game_screens/overworld_screen.get_road_or_alley_char()`.
    Uses the 4-bit connectivity mask: N=1, E=2, S=4, W=8.
    """
    try:
        import game.constants as const  # deferred — only needed at render time
        mapping = getattr(const, "PATH_TILE_MAPPINGS", {}) or {}
    except Exception:
        mapping = {}

    if tile is None:
        kind_map = mapping.get("road", {})
        return kind_map.get(0, "=") if isinstance(kind_map, dict) else (kind_map or "=")

    kind = ROAD if tile.type == ROAD else ALLEY if tile.type == ALLEY else None
    if kind is None:
        return " "

    kind_map = mapping.get(kind)
    default = "=" if kind == ROAD else '"'

    if not isinstance(kind_map, dict):
        return kind_map or default

    mask = 0
    if up_t is not None and getattr(up_t, "type", None) == tile.type:
        mask |= 1
    if right_t is not None and getattr(right_t, "type", None) == tile.type:
        mask |= 2
    if down_t is not None and getattr(down_t, "type", None) == tile.type:
        mask |= 4
    if left_t is not None and getattr(left_t, "type", None) == tile.type:
        mask |= 8

    return kind_map.get(mask, default)


# ── legend ─────────────────────────────────────────────────────────────────

def build_legend_lines(cur_area: Any) -> List[str]:
    """Return legend lines for visible buildings in `cur_area`.
    Mirrors `old/game_screens/overworld_screen._create_legend()`.
    """
    if not cur_area or not hasattr(cur_area, "tiles"):
        return []

    unique: dict = {}
    for tile in cur_area.tiles.values():
        if tile.type == BUILDING and isinstance(tile.building, dict):
            name = tile.building.get("name")
            if name and name not in unique:
                unique[name] = tile.building

    if not unique:
        return []

    lines = ["─── Legend ───"]
    for b in sorted(unique.values(), key=lambda b: b.get("char", "")):
        char = _colorize(b.get("char", "?"), b.get("color"))
        display = b.get("display_name", "Unknown")
        lines.append(f" {char}  {display}")
    return lines


# ── header ─────────────────────────────────────────────────────────────────

def build_header(player_game: Any) -> str:
    """Return a centered header string: 'Region – City'."""
    try:
        cur_region, cur_area = player_game.get_region_and_active_area_for_position()
        region_name = cur_region.display_name if cur_region else "Unknown"
        city_name = cur_area.display_name if cur_area else "Unknown"
    except Exception:
        region_name = "Unknown"
        city_name = "Unknown"
    return f"{region_name}  ─  {city_name}"


# ── color markup helper ─────────────────────────────────────────────────────

def _colorize(ch: str, color: Optional[str], bg_color: Optional[str] = None) -> str:
    """Wrap `ch` in Textual Rich color markup, escaping any square brackets
    in the character so it can't be misread as a markup tag.  When `bg_color`
    is provided it is applied as the cell background so that impassable tiles
    share the same background as the open area floor around them.
    """
    if not color and not bg_color:
        return ch
    safe_ch = ch.replace("[", "\\[")
    if color and bg_color:
        return f"[{color} on {bg_color}]{safe_ch}[/]"
    if color:
        return f"[{color}]{safe_ch}[/]"
    return f"[on {bg_color}]{safe_ch}[/]"


# ── per-tile character ──────────────────────────────────────────────────────

def _tile_char(x: int, y: int, player_game: Any) -> str:
    """Return the display character (optionally wrapped in Textual color
    markup) for world coordinate (x, y).
    Priority: player marker → aircraft marker → tile type.
    Mirrors the inner loop of `old/game_screens/overworld_screen.display_viewport()`.
    """
    # aircraft marker
    if getattr(player_game, "aircraft_location", None) == (x, y):
        return AIRCRAFT_CHAR

    # player marker
    if x == player_game.x and y == player_game.y:
        return PLAYER_CHAR

    # resolve tile from world_tiles (same priority order as legacy)
    t = player_game.world_tiles.get((x, y))
    if t is None:
        # try active child city tiles
        try:
            _, active = player_game.get_region_and_active_area_for_position((x, y))
            if active and hasattr(active, "tiles"):
                t = active.tiles.get((x, y))
        except Exception:
            pass

    if t is None:
        return " "

    try:
        import game.constants as const
    except Exception:
        const = None  # type: ignore[assignment]

    tile_type = getattr(t, "type", None)

    if tile_type == ROAD or tile_type == ALLEY:
        def _pick(tx: int, ty: int) -> Any:
            return player_game.world_tiles.get((tx, ty))

        return _get_road_or_alley_char(
            t,
            _pick(x - 1, y),
            _pick(x, y - 1),
            _pick(x + 1, y),
            _pick(x, y + 1),
        )

    if tile_type == BUILDING:
        bld = getattr(t, "building", None)
        ch = bld.get("char") if isinstance(bld, dict) else None
        color = bld.get("color") if isinstance(bld, dict) else None
        return _colorize(ch if ch else "B", color)

    if tile_type == "open_area":
        try:
            dungeon = player_game.get_dungeon_at_position((x, y))
            if dungeon is not None:
                ch = getattr(const, "DUNGEON_ENTRANCE_CHAR", "D") if const else "D"
                return _colorize(ch, "#af1111")
            _, active = player_game.get_region_and_active_area_for_position((x, y))
            if active and const:
                type_name = getattr(active, "city_name", None) or getattr(active, "region_name", "")
                ch = getattr(const, f"{type_name.upper()}_OPEN_AREA_CHAR", None) or "."
                color = getattr(const, f"{type_name.upper()}_OPEN_AREA_COLOR", None)
                return _colorize(ch, color)
        except Exception:
            pass
        return "."

    if tile_type == "impassable":
        try:
            _, active = player_game.get_region_and_active_area_for_position((x, y))
            if active and const:
                type_name = getattr(active, "city_name", None) or getattr(active, "region_name", "")
                ch = getattr(const, f"{type_name.upper()}_IMPASSABLE_CHAR", None) or "#"
                impassable_color = getattr(const, f"{type_name.upper()}_IMPASSABLE_COLOR", None)
                open_color       = getattr(const, f"{type_name.upper()}_OPEN_AREA_COLOR",  None)
                return _colorize(ch, impassable_color, open_color)
        except Exception:
            pass
        return "#"

    return "."


# ── full viewport ───────────────────────────────────────────────────────────

def build_viewport_lines(
    player_game: Any,
    view_w: int = DEFAULT_VIEW_W,
    view_h: int = DEFAULT_VIEW_H,
) -> List[str]:
    """Return a list of `view_h` strings, each `view_w` characters wide,
    representing the map centered on the player.  No borders — the caller
    (OverworldScreen) handles Textual widget layout.
    """
    cx, cy = player_game.x, player_game.y
    half_w = view_w // 2
    half_h = view_h // 2

    lines: List[str] = []
    for y in range(cy - half_h, cy + half_h + 1):
        row = ""
        for x in range(cx - half_w, cx + half_w + 1):
            row += _tile_char(x, y, player_game)
        lines.append(row)
    return lines


# ── stats panel ────────────────────────────────────────────────────────────

def build_stats_lines(player_game: Any) -> List[str]:
    """Return text lines for the stats sidebar panel.
    Shows party members (name / level / HP) and gold.
    """
    lines: List[str] = ["─── Party ───"]
    try:
        party = player_game.get_active_party()
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
    lines.append("─── Gold ───")
    try:
        lines.append(f" {player_game.money:,} g")
    except Exception:
        lines.append(" ?")

    lines.append("")
    lines.append("─── Position ───")
    try:
        lines.append(f" ({player_game.x}, {player_game.y})")
    except Exception:
        lines.append(" ?")

    return lines