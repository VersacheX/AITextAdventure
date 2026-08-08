"""
combat_renderer: builds Rich-markup text for the combat screen's widgets.

Displays the same information as the legacy `old/combat_balancing_simulation/
hostile_details_screen.py` / `player_details_screen.py` ASCII-box formatters,
but produces plain Rich markup for a Textual `Static` widget instead of
'*'-bordered console text blocks — matching how `overworld_renderer.py` and
`inventory_screen.py`'s `_build_card_text()` already render `old/` game
objects for Textual.
"""
from __future__ import annotations

from typing import Any, List

from rich.markup import escape as rich_escape

from tui.services.combat_service import is_unit_player


def _status_text(entity: Any) -> str:
    statuses = getattr(entity, "statuses", None) or []
    parts = [
        rich_escape(str(s.get("name") or s.get("id") or ""))
        for s in statuses
        if isinstance(s, dict) and (s.get("name") or s.get("id"))
    ]
    if not parts:
        return ""
    return f"[yellow]{', '.join(parts)}[/yellow]"


def _active_marker(*, is_active: bool) -> str:
    return "[bold green]>[/bold green] " if is_active else ""


def build_player_card_text(unit: Any, *, is_active: bool) -> str:
    """Return Rich-markup text for one player's combat card."""
    p = unit.entity
    name = rich_escape(str(getattr(p, "name", "?")))
    lines: List[str] = [f"{_active_marker(is_active=is_active)}[bold]{name}[/bold]  Lv.{getattr(p, 'level', 0)}"]

    if not unit.is_alive():
        lines.append("[dim red]-- DEFEATED --[/dim red]")
        return "\n".join(lines)

    lines.append(f"HP {getattr(p, 'current_hp', 0)}/{getattr(p, 'max_hp', 0)}")
    lines.append(f"AP {getattr(p, 'current_ap', 0)}/{getattr(p, 'max_ap', 0)}")

    status = _status_text(p)
    if status:
        lines.append(status)

    return "\n".join(lines)


def build_hostile_card_text(unit: Any, *, is_active: bool) -> str:
    """Return Rich-markup text for one hostile's combat card."""
    h = unit.entity
    name = rich_escape(str(getattr(h, "name", "?")))
    rarity = getattr(h, "rarity", "common")
    lines: List[str] = [
        f"{_active_marker(is_active=is_active)}[bold]{name}[/bold]  Lv.{getattr(h, 'level', 0)}  [dim]({rarity})[/dim]"
    ]

    if not unit.is_alive():
        lines.append("[dim red]-- DEFEATED --[/dim red]")
        return "\n".join(lines)

    lines.append(f"HP {getattr(h, 'current_hp', 0)}/{getattr(h, 'max_hp', 0)}")
    lines.append(f"AP {getattr(h, 'current_ap', 0)}/{getattr(h, 'max_ap', 0)}")

    status = _status_text(h)
    if status:
        lines.append(status)

    return "\n".join(lines)


def build_timeline_rows(sim: Any, width: int = 60) -> List[str]:
    """Return Rich-markup lines for a proportional turn-order timeline.

    The acting unit (lowest next_action_in) appears at the left edge.
    All other units are placed proportionally across the track.
    When two names would overlap, the later one is bumped to a row above.
    A track line with ``|`` ends and ``+`` markers closes the display.
    """
    alive = [u for u in sim.units if u.is_alive()]
    if not alive:
        return []

    ordered = sorted(alive, key=lambda u: u.next_action_in)
    min_t = ordered[0].next_action_in
    max_t = ordered[-1].next_action_in
    # Use a stable floor so the scale doesn't jump dramatically between turns.
    # compute_action_delay() returns at most 10.0 (base=10, DEX=0), so a floor
    # of 10.0 keeps unit positions visually consistent across the full combat.
    span = max(max_t - min_t, 10.0)

    TRUNC = 7

    def _col(t: float) -> int:
        return int((t - min_t) / span * (width - 1))

    def _label(u: Any, rank: int) -> str:
        name   = rich_escape(str(getattr(u.entity, "name", "?"))[:TRUNC])
        player = is_unit_player(u)
        if rank == 0:
            colour = "bold bright_green" if player else "bold bright_red"
        else:
            colour = "cyan" if player else "red"
        return f"[{colour}]{name}[/{colour}]"

    # Build (col, markup, plain_len) — nudge tied units right so they
    # don't all collapse onto the same column.
    entries: List[tuple] = []
    for rank, u in enumerate(ordered):
        col  = _col(u.next_action_in)
        used = {e[0] for e in entries}
        while col in used and col < width - 1:
            col += 1
        plen = len(str(getattr(u.entity, "name", "?"))[:TRUNC])
        entries.append((col, _label(u, rank), plen))

    # ── assign rows (base = index 0, overflows stack above) ──────────────
    rows: List[List[tuple]] = [[]]

    for entry in entries:
        col, markup, plen = entry
        placed = False
        for row in rows:
            conflict = any(
                abs(col - rc) < max(plen, rlen) + 1
                for rc, _, rlen in row
            )
            if not conflict:
                row.append(entry)
                placed = True
                break
        if not placed:
            rows.append([entry])

    # ── render name rows (overflow rows above, base row last) ────────────
    result_lines: List[str] = []
    for row in reversed(rows):
        parts  = sorted(row, key=lambda x: x[0])
        line   = ""
        cursor = 0
        for col, markup, plen in parts:
            if col > cursor:
                line += " " * (col - cursor)
            line += markup
            cursor = col + plen
        if cursor < width:
            line += " " * (width - cursor)
        result_lines.append(line)

    # ── track line ────────────────────────────────────────────────────────
    track = ["-"] * width
    track[0]  = "|"
    track[-1] = "|"
    for u in ordered:
        c = _col(u.next_action_in)
        if 0 < c < width - 1:
            track[c] = "+"
    result_lines.append("[dim]" + rich_escape("".join(track)) + "[/dim]")

    return result_lines
