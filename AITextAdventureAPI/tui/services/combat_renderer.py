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


def build_turn_order_text(sim: Any) -> str:
    """Return a compact Rich-markup line listing the upcoming turn order."""
    alive = [u for u in sim.units if u.is_alive()]
    ordered = sorted(alive, key=lambda u: u.next_action_in)
    names = [rich_escape(str(getattr(u.entity, "name", "?"))) for u in ordered[:8]]
    if not names:
        return ""
    names[0] = f"[bold]{names[0]}[/bold]"
    return "Turn order:  " + "  ->  ".join(names)