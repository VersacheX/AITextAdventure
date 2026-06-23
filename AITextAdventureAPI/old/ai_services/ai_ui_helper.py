# AITextAdventureAPI/old/ai_services/ai_ui_helper.py
# UI helper functions extracted from ai_controlled_demo.py
import os
import time
import textwrap
from typing import Any, List, Optional, Dict

from game import constants as const
from game.constants import ROAD, BUILDING, ALLEY


def clear_screen() -> None:
    """Clear the terminal screen in a platform-aware way."""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_road_or_alley_char(
    tile: Any,
    left_tile: Any = None,
    up_tile: Any = None,
    right_tile: Any = None,
    down_tile: Any = None,
) -> str:
    """Return a character for road/alley tiles using PATH_TILE_MAPPINGS.

    Uses a4-bit mask: N=1, E=2, S=4, W=8 when mapping is a dict. Falls
    back to simple characters when mapping entries are strings.
    """
    try:
        mapping = getattr(const, "PATH_TILE_MAPPINGS", {}) or {}
    except Exception:
        mapping = {}

    def _select(kind_map, mask, default):
        if isinstance(kind_map, dict):
            return kind_map.get(mask, default)
        return kind_map or default

    if tile is None:
        return _select(mapping.get("road"),0, "=")

    kind = (
        "road"
        if getattr(tile, "type", None) == ROAD
        else ("alley" if getattr(tile, "type", None) == ALLEY else None)
    )
    if kind is None:
        return " "

    kind_map = mapping.get(kind)
    if not isinstance(kind_map, dict):
        return _select(kind_map,0, "=" if kind == "road" else '"')

    mask =0
    try:
        if up_tile is not None and getattr(up_tile, "type", None) == getattr(tile, "type", None):
            mask |=1
        if right_tile is not None and getattr(right_tile, "type", None) == getattr(tile, "type", None):
            mask |=2
        if down_tile is not None and getattr(down_tile, "type", None) == getattr(tile, "type", None):
            mask |=4
        if left_tile is not None and getattr(left_tile, "type", None) == getattr(tile, "type", None):
            mask |=8
    except Exception:
        pass

    return kind_map.get(mask, "=" if kind == "road" else '"')


def display_viewport(player_game: Any, region: Any, player: Any, view_w: int, view_h: int, ai_status: Optional[Any] = None, ai_stats: Optional[Dict[str, int]] = None) -> Any:
    """Render a rectangular viewport centered on player and return the active area.

    The function prints to stdout a framed view and returns the active child city or region
    that corresponds to the player's current position.

    New: optional `ai_status` will be shown in a side box to the right of the map.
    `ai_status` may be a string or a dict with keys like `action` and `target` to produce
    a more useful objective line (e.g. {"action":"buy_armor","target":"nearest_armor_shop"} or
    {"action":"move_to_loot","target":(12,3)}).
    `ai_stats` may include keys: 'fights','tasks','loots','purchases','tasks_abandoned','hostiles_defeated'.
    """
    active = region
    if hasattr(region, "child_city") and region.child_city and (player.x, player.y) in region.child_city.tiles:
        active = region.child_city

    cur_region, cur_area = (
        player_game.get_region_and_active_area_for_position((player.x, player.y))
        if player_game
        else (None, None)
    )

    region_name = cur_region.display_name if cur_region else (getattr(region, "display_name", None) or "region")
    city_name = cur_area.display_name if cur_area else (getattr(active, "display_name", None) or f"city_{getattr(active, 'seed',0)}")

    width = view_w +4
    # side box width (characters) when ai_status or ai_stats provided — a bit larger
    side_w =44 if (ai_status or ai_stats) else 0
    total_width = width + (side_w +3 if side_w else 0)

    print("*" * total_width)
    header = f" {region_name} - {city_name} "
    pad = max(0, width - len(header) -2)
    left = pad //2
    right = pad - left
    side_header = " AI STATUS " if (ai_status or ai_stats) else ""
    # print combined header line
    if side_w:
        # center side header within side box
        sh_pad = max(0, side_w - len(side_header))
        sh_left = sh_pad //2
        sh_right = sh_pad - sh_left
        print("*" + " " * left + header + " " * right + "*" + " " + "*" + " " * sh_left + side_header + " " * sh_right + "*")
    else:
        print("*" + " " * left + header + " " * right + "*")
    print("*" * width + (" " *3) + ("*" * side_w if side_w else ""))

    half_w = view_w //2
    half_h = view_h //2
    start_x = player.x - half_w
    end_x = player.x + half_w
    start_y = player.y - half_h
    end_y = player.y + half_h

    def _pick_tile(tx: int, ty: int):
        if hasattr(active, "tiles"):
            t2 = active.tiles.get((tx, ty))
            if t2 is not None:
                return t2
        t2 = player_game.world_tiles.get((tx, ty))
        if t2 is not None:
            return t2
        return region.tiles.get((tx, ty))

    # prepare side box content lines
    side_lines: List[str] = []
    if side_w:
        # show quick player stats at the top of AI status box
        try:
            cur_hp = getattr(player, 'current_hp', None)
            max_hp = getattr(player, 'max_hp', None)
            cur_ap = getattr(player, 'current_ap', None)
            max_ap = getattr(player, 'max_ap', None)
            exp = getattr(player, 'experience', None)
            xp_needed = getattr(player, 'xp_needed_to_level', None)
            money = getattr(player, 'money', None)
            stats_lines = []
            # Insert level at top so HP/AP/XP/Money shift down one row
            level = getattr(player, 'level', None)
            if level is not None:
                stats_lines.append(f"Level: {level}")
            if cur_hp is not None and max_hp is not None:
                stats_lines.append(f"HP: {cur_hp}/{max_hp}")
            elif cur_hp is not None:
                stats_lines.append(f"HP: {cur_hp}")
            if cur_ap is not None and max_ap is not None:
                stats_lines.append(f"AP: {cur_ap}/{max_ap}")
            elif cur_ap is not None:
                stats_lines.append(f"AP: {cur_ap}")
            if exp is not None and xp_needed is not None:
                stats_lines.append(f"XP: {exp}/{xp_needed}")
            elif exp is not None:
                stats_lines.append(f"XP: {exp}")
            if money is not None:
                stats_lines.append(f"Money: {money}")
            # initialize side_lines with stats header
            side_lines.extend(stats_lines)
            side_lines.append("")

            # Add equipment summary at the very top of the AI status box so it
            # appears floated at the top-right of the overall viewport.
            try:
                head = _safe_item_name(getattr(player, 'head_armor', None))
                body = _safe_item_name(getattr(player, 'body_armor', None))
                arms = _safe_item_name(getattr(player, 'arm_armor', None))
                legs = _safe_item_name(getattr(player, 'leg_armor', None))
                eq_line = f"Equip: H:{head} B:{body} A:{arms} L:{legs}"
                # put equipment line at the very top of the side box
                side_lines.insert(0, eq_line)
            except Exception:
                pass
        except Exception:
        # ignore and continue building other status lines
            pass

        # build richer side box content from ai_status and ai_stats
        # ai_status may be a dict with structured info
        if isinstance(ai_status, dict):
            # prefer an explicit description when provided by the logic engine
            desc = ai_status.get('description')
            action = ai_status.get('action') or ai_status.get('task') or ''
            target = ai_status.get('target')
            # if description provided, use it verbatim (most specific)
            if desc:
                side_lines.append(str(desc))
            else:
                # human-friendly action mapping
                action_map = {
                    'buy_armor': 'Moving to armor shop',
                    'buy_items': 'Moving to item shop',
                    'move_to_shop': 'Moving to shop',
                    'move_to_loot': 'Moving to loot',
                    'harvest_loot': 'Raiding loot stash',
                    'explore': 'Exploring area',
                    'wait': 'Waiting',
                    'flee': 'Fleeing',
                }
                if action in action_map:
                    side_lines.append(action_map[action])
                elif action:
                    side_lines.append(str(action).replace('_', ' ').capitalize())
                else:
                    side_lines.append('Idle')

            # include explicit target info when available
            if target is not None:
                if isinstance(target, (tuple, list)) and len(target) >=2:
                    side_lines.append(f"Target: {target[0]},{target[1]}")
                else:
                    side_lines.append(f"Target: {str(target)}")
        else:
            # simple string message
            if ai_status:
                side_lines.append(str(ai_status))
            else:
                side_lines.append('Idle')

        side_lines.append("")

        # stats block
        if ai_stats:
            side_lines.append("Stats:")
            side_lines.append(f"Fights: {int(ai_stats.get('fights',0))}")
            side_lines.append(f"Hostiles defeated: {int(ai_stats.get('hostiles_defeated', ai_stats.get('kills',0))) }")
            side_lines.append(f"Tasks: {int(ai_stats.get('tasks',0))}")
            side_lines.append(f"Tasks abandoned: {int(ai_stats.get('tasks_abandoned',0))}")
            side_lines.append(f"Loots raided: {int(ai_stats.get('loots',0))}")
            side_lines.append(f"Purchases: {int(ai_stats.get('purchases',0))}")
        # ensure there's at least one blank line to render
        if not side_lines:
            side_lines = [""]
        # ensure side_lines has at least view_h lines
        while len(side_lines) < view_h:
            side_lines.append("")
        # truncate to view_h
        side_lines = side_lines[:view_h]

    # gather and print rows with optional side box
    for row_idx, y in enumerate(range(start_y, end_y +1)):
        row_chars = []
        for x in range(start_x, end_x +1):
            if x == player.x and y == player.y:
                color_enabled = False
                try:
                    if os.name != "nt" or os.getenv("WT_SESSION") or os.getenv("TERM"):
                        color_enabled = True
                except Exception:
                    color_enabled = False

                if color_enabled:
                    row_chars.append("\x1b[1;33m@\x1b[0m")
                else:
                    row_chars.append("@")
                continue

            t = None
            if hasattr(active, "tiles"):
                t = active.tiles.get((x, y))
            if t is None and player_game is not None:
                try:
                    t = player_game.world_tiles.get((x, y))
                except Exception:
                    t = None
            if t is None:
                t = region.tiles.get((x, y))

            if t is None:
                row_chars.append("?")
            else:
                if t.type == ROAD:
                    left_t = _pick_tile(x -1, y)
                    up_t = _pick_tile(x, y -1)
                    right_t = _pick_tile(x +1, y)
                    down_t = _pick_tile(x, y +1)
                    row_chars.append(get_road_or_alley_char(t, left_t, up_t, right_t, down_t))
                elif t.type == BUILDING:
                    ch = t.building.get("char") if isinstance(t.building, dict) else "B"
                    row_chars.append(ch if ch else "B")
                elif t.type == "open_area":
                    _, active_area = player_game.get_region_and_active_area_for_position((x, y))
                    type_name = active_area.city_name if active_area.city_name is not None else active_area.region_name
                    attr = f"{type_name.upper()}_OPEN_AREA_CHAR"
                    open_char = getattr(const, attr, " ")
                    row_chars.append(open_char if open_char else " ")
                elif t.type == "impassable":
                    _, active_area = player_game.get_region_and_active_area_for_position((x, y))
                    type_name = active_area.city_name if active_area.city_name is not None else active_area.region_name
                    attr = f"{type_name.upper()}_IMPASSABLE_CHAR"
                    open_char = getattr(const, attr, " ")
                    row_chars.append(open_char if open_char else " ")
                elif t.type == ALLEY:
                    left_t = _pick_tile(x -1, y)
                    up_t = _pick_tile(x, y -1)
                    right_t = _pick_tile(x +1, y)
                    down_t = _pick_tile(x, y +1)
                    row_chars.append(get_road_or_alley_char(t, left_t, up_t, right_t, down_t))
                else:
                    _, active_area = player_game.get_region_and_active_area_for_position((x, y))
                    type_name = active_area.city_name if active_area.city_name is not None else active_area.region_name
                    attr = f"{type_name.upper()}_OPEN_AREA_CHAR"
                    open_char = getattr(const, attr, " ")
                    row_chars.append(open_char if open_char else " ")

        map_row = "* " + "".join(row_chars) + " *"

        if side_w:
            side_text = side_lines[row_idx] if row_idx < len(side_lines) else ""
            side_text = side_text[: side_w -2]
            # pad side text and wrap into a boxed cell
            print(map_row + " " + "*" + " " + side_text.ljust(side_w -2) + " " + "*")
        else:
            print(map_row)

    print("*" * width + (" " *3) + ("*" * side_w if side_w else ""))
    print()

    return active


# Compatibility helper: render side-by-side boxed window used by the console demo
def render_compat_combat_box(left_lines: List[str], right_lines: List[str], left_title: str = "Player", right_title: str = "Hostile", left_w: int = None, right_w: int = None, gap: int =6) -> None:
 """Render a boxed side-by-side window compatible with the console game demo.

 left_lines and right_lines are lists of strings. The function prints a framed
 box with both columns and titles. Column widths are auto-computed when not provided.
 """
 # compute widths
 try:
    left_max = max((len(l) for l in left_lines), default=0)
 except Exception:
    left_max =0
 try:
    right_max = max((len(l) for l in right_lines), default=0)
 except Exception:
    right_max =0

 if not left_w:
    left_w = max(left_max,20)
 if not right_w:
    right_w = max(right_max,20)

 content_w = left_w + gap + right_w
 box_w = content_w +4

 # top border and title line
 print("*" * box_w)
 title_line = '* ' + left_title.center(left_w) + ' ' * gap + right_title.center(right_w) + ' *'
 print(title_line)
 print("*" * box_w)

 rows = max(len(left_lines), len(right_lines))
 for i in range(rows):
    left = left_lines[i] if i < len(left_lines) else ''
 right = right_lines[i] if i < len(right_lines) else ''
 line = '* ' + left.ljust(left_w) + ' ' * gap + right.ljust(right_w) + ' *'
 print(line)

 print("*" * box_w)


def type_victory_message(msg: str, delay: float =0.1) -> None:
	"""Type out a victory message character-by-character, then pause."""
	try:
		for ch in msg:
			print(ch, end="", flush=True)
			time.sleep(delay)
		# finish the line and pause once
		print()
		time.sleep(1.0)
	except Exception:
		try:
			print(msg)
		except Exception:
			pass

def ai_fight_screen(player: Any, hostiles: List[Any], player_game: Any, turn_results: List[str], player_health: int, player_max_health: int, ai_status: Optional[str] = None) -> None:
    """Display the AI-controlled fight screen with per-turn updates and status.

    Args:
        player: The player character object.
        hostiles: List of hostile character objects.
        player_game: The game instance managing player and world state.
        turn_results: List of strings describing results of each turn.
        player_health: Current health of the player.
        player_max_health: Maximum health of the player.
        ai_status: Optional status message for AI actions.
    """
    # Render initial state
    left_lines = [f"Player Health: {player_health}/{player_max_health}"]
    right_lines = [f"Hostile {h.name} Health: {h.health}/{h.max_health}" for h in hostiles]
    render_compat_combat_box(left_lines, right_lines, left_title="Battle Status", right_title="Hostiles")

    # Type out the AI status message if provided
    if ai_status:
        print("\nAI Status:")
        type_victory_message(ai_status, delay=0.05)

    # Process each turn result
    for result in turn_results:
        print()  # Blank line before each turn result
        type_victory_message(result, delay=0.05)

        # Simple check for battle end conditions
        if "defeated" in result.lower() or "win" in result.lower():
            break

        # Re-render the state after each turn
        player_health = player.health  # Update current health
        hostiles = [h for h in hostiles if h.health > 0]  # Remove defeated hostiles
        left_lines[0] = f"Player Health: {player_health}/{player_max_health}"
        right_lines = [f"Hostile {h.name} Health: {h.health}/{h.max_health}" for h in hostiles]
        render_compat_combat_box(left_lines, right_lines, left_title="Battle Status", right_title="Hostiles")

        # Deliberate pause to let players see the updated status
        time.sleep(1.5)

    # Final message display
    if any(h.health > 0 for h in hostiles):
        type_victory_message("The battle continues...", delay=0.05)
    else:
        type_victory_message("All hostiles defeated!", delay=0.05)

def _safe_item_name(item: Any) -> str:
	"""Return a safe short name for an item-like object for UI display.

	Handles None, strings, dicts and objects with `name`/`display_name` attributes.
	Falls back to class name or str(item) when necessary.
	"""
	try:
		if item is None:
			return "None"
		if isinstance(item, str):
			return item
		if isinstance(item, dict):
			return str(item.get("name") or item.get("display_name") or item.get("title") or "")
		# object with name/display_name/title attributes
		name = getattr(item, "name", None) or getattr(item, "display_name", None) or getattr(item, "title", None)
		if name:
			return str(name)
		# fallback to class name
		cls = getattr(item, "__class__", None)
		if cls is not None:
			return getattr(cls, "__name__", str(item))
		return str(item)
	except Exception:
		return ""