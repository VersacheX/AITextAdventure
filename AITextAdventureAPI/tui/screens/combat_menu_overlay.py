"""
CombatMenuOverlay: centered floating ability/item picker for the combat screen.

Replaces the old bottom-docked panel with a proper centered dialog that shows:
  - A scrollable list of choices on the left
  - A rich detail panel on the right (for abilities: name, AP cost, power,
    effect, elements, description; for items: name, quantity, description)

Navigate with Up/Down, confirm with Enter, cancel with Escape.
"""
from __future__ import annotations

from typing import Any, Callable, List, Optional, Tuple

from rich.markup import escape as rich_escape
from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Label, ListItem, ListView, Static


# ── detail builders ───────────────────────────────────────────────────────────

def build_ability_detail(ability: Any, current_ap: int) -> str:
    """Return Rich-markup detail text for one ability."""
    if ability is None:
        return "[dim]No ability selected.[/dim]"

    lines: list[str] = []
    name        = rich_escape(str(getattr(ability, "name", "?")))
    description = rich_escape(str(getattr(ability, "description", "") or ""))
    ap_cost     = getattr(ability, "ap_cost", 0) or 0
    level       = getattr(ability, "level", 1)
    effect      = getattr(ability, "effect", None)
    eff_val     = rich_escape(effect.value if hasattr(effect, "value") else str(effect or ""))
    atype       = getattr(ability, "ability_type", None)
    atype_val   = rich_escape(atype.value if hasattr(atype, "value") else str(atype or ""))
    elements    = getattr(ability, "elements", []) or []
    status_keys = getattr(ability, "status_keys", []) or []
    can_aoe     = getattr(ability, "can_aoe", False)

    try:
        power = ability.compute_power()
    except Exception:
        power = getattr(ability, "base_power", 0)

    lines.append(f"[bold]{name}[/bold]")
    if description:
        lines.append("")
        lines.append(description)

    lines.append("")
    lines.append(f"Type    : [cyan]{atype_val}[/cyan]")
    lines.append(f"Effect  : [green]{eff_val}[/green]")
    lines.append(f"Level   : {level}")
    lines.append(f"Power   : {power}")
    lines.append(f"AP Cost : {ap_cost}  [dim](have {current_ap})[/dim]")

    if can_aoe:
        lines.append("[bold yellow]AOE — hits all targets[/bold yellow]")
    if elements:
        lines.append(
            "Elements: "
            + ", ".join(
                rich_escape(e.value if hasattr(e, "value") else str(e))
                for e in elements
            )
        )
    if status_keys:
        lines.append("Status  : " + ", ".join(rich_escape(str(k)) for k in status_keys))

    if current_ap < ap_cost:
        lines.append("")
        lines.append(f"[bold red]Not enough AP ({current_ap}/{ap_cost})[/bold red]")

    return "\n".join(lines)


def build_item_detail(item: Any) -> str:
    """Return Rich-markup detail text for one utility item."""
    if item is None:
        return "[dim]No item selected.[/dim]"

    lines: list[str] = []
    name        = rich_escape(str(getattr(item, "name", "?")))
    description = rich_escape(str(getattr(item, "description", "") or ""))
    quantity    = getattr(item, "quantity", 1)
    effect      = getattr(item, "effect", None) or getattr(item, "effect_type", None)
    eff_val     = rich_escape(effect.value if hasattr(effect, "value") else str(effect or ""))

    lines.append(f"[bold]{name}[/bold]  x{quantity}")
    if description:
        lines.append("")
        lines.append(description)
    if eff_val:
        lines.append("")
        lines.append(f"Effect: [green]{eff_val}[/green]")

    return "\n".join(lines)


# ── list row ──────────────────────────────────────────────────────────────────

class _MenuItem(ListItem):
    """Single selectable row carrying an arbitrary payload."""

    def __init__(self, label: str, payload: Any) -> None:
        super().__init__(Label(label))
        self.payload = payload


# ── overlay widget ────────────────────────────────────────────────────────────

class CombatMenuOverlay(Widget):
    """Centered floating dialog for ability / item selection in combat.

    Parameters
    ----------
    title : str
        Dialog heading.
    entries : list of (label, payload)
        Selectable rows. ``payload`` is passed to ``on_select`` on confirm.
    on_select : callable(payload | None)
        Called with the chosen payload or ``None`` on cancel.
    detail_fn : callable(payload) -> str, optional
        Builds the Rich-markup text for the right detail panel when a row
        is highlighted. Defaults to no detail.
    """

    can_focus = True
    can_focus_children = False

    BINDINGS = [
        Binding("up",     "cursor_up",   "Up",     show=False),
        Binding("down",   "cursor_down", "Down",   show=False),
        Binding("enter",  "confirm",     "Select", show=True),
        Binding("escape", "cancel",      "Cancel", show=True),
    ]

    DEFAULT_CSS = """
    CombatMenuOverlay {
        layer: overlay;
        width: 72;
        height: 22;
        background: $surface;
        border: thick $accent;
        layout: vertical;
    }

    #menu-dialog-title {
        width: 100%;
        height: 1;
        text-align: center;
        text-style: bold;
        background: $boost;
        color: $text;
        padding: 0 1;
    }

    #menu-dialog-body {
        height: 1fr;
        layout: horizontal;
    }

    #menu-list-col {
        width: 28;
        height: 100%;
        border-right: solid $accent 50%;
    }

    #menu-list {
        width: 100%;
        height: 100%;
    }

    #menu-detail-col {
        width: 1fr;
        height: 100%;
        padding: 1;
        overflow-y: auto;
    }

    #menu-footer {
        height: 1;
        background: $panel;
        border-top: solid $accent 40%;
        padding: 0 1;
        color: $text-muted;
    }
    """

    def __init__(
        self,
        title: str,
        entries: List[Tuple[str, Any]],
        on_select: Callable[[Optional[Any]], None],
        *,
        detail_fn: Optional[Callable[[Any], str]] = None,
    ) -> None:
        super().__init__()
        self._title     = title
        self._entries   = entries
        self._on_select = on_select
        self._detail_fn = detail_fn
        self._cursor    = 0

    def compose(self) -> ComposeResult:
        yield Static(self._title, id="menu-dialog-title")
        with Horizontal(id="menu-dialog-body"):
            with Vertical(id="menu-list-col"):
                with ListView(id="menu-list"):
                    for label, payload in self._entries:
                        yield _MenuItem(label, payload)
            with Vertical(id="menu-detail-col"):
                yield Static(
                    self._get_detail(0),
                    id="menu-detail",
                    markup=True,
                )
        yield Static(
            "[dim]↑↓ navigate   Enter select   Esc cancel[/dim]",
            id="menu-footer",
        )

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        # Centre the dialog over whatever screen it was mounted into
        try:
            sw = self.screen.size.width
            sh = self.screen.size.height
            self.styles.offset = ((sw - 72) // 2, (sh - 22) // 2)
        except Exception:
            pass
        try:
            lv = self.query_one("#menu-list", ListView)
            lv.focus()
            if self._entries:
                lv.index = 0
        except Exception:
            self.focus()

    # ── detail helper ─────────────────────────────────────────────────────

    def _get_detail(self, index: int) -> str:
        if not self._entries or index >= len(self._entries):
            return "[dim]Nothing to show.[/dim]"
        _, payload = self._entries[index]
        if self._detail_fn is not None:
            try:
                return self._detail_fn(payload) or ""
            except Exception:
                pass
        return ""

    def _refresh_detail(self, index: int) -> None:
        try:
            self.query_one("#menu-detail", Static).update(self._get_detail(index))
        except Exception:
            pass

    # ── navigation ────────────────────────────────────────────────────────

    def action_cursor_up(self) -> None:
        if not self._entries:
            return
        self._cursor = (self._cursor - 1) % len(self._entries)
        try:
            self.query_one("#menu-list", ListView).index = self._cursor
        except Exception:
            pass
        self._refresh_detail(self._cursor)

    def action_cursor_down(self) -> None:
        if not self._entries:
            return
        self._cursor = (self._cursor + 1) % len(self._entries)
        try:
            self.query_one("#menu-list", ListView).index = self._cursor
        except Exception:
            pass
        self._refresh_detail(self._cursor)

    def action_confirm(self) -> None:
        if not self._entries:
            self._on_select(None)
            self.remove()
            return
        _, payload = self._entries[self._cursor]
        self._on_select(payload)
        self.remove()

    def action_cancel(self) -> None:
        self._on_select(None)
        self.remove()

    # ── mouse / ListView highlight sync ───────────────────────────────────

    @on(ListView.Highlighted, "#menu-list")
    def _on_highlighted(self, event: ListView.Highlighted) -> None:
        if event.item is None:
            return
        try:
            items = list(self.query_one("#menu-list", ListView).query(_MenuItem))
            self._cursor = items.index(event.item)
            self._refresh_detail(self._cursor)
        except Exception:
            pass

    @on(ListView.Selected, "#menu-list")
    def _on_selected(self, event: ListView.Selected) -> None:
        if isinstance(event.item, _MenuItem):
            self._on_select(event.item.payload)
        else:
            self._on_select(None)
        self.remove()
