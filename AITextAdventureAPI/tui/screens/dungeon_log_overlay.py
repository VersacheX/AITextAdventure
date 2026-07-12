"""
DungeonLogOverlay: floating dungeon-log panel for InventoryScreen.

Lists all dungeons known to the player game (pg.dungeons).
Unlocked dungeons are shown normally; locked ones are shown dim.

Right panel shows: display name, world coordinates, floor count,
lock status, locked text (if any), and description from the seed
constants when available.

The CSS class "inv-overlay" is added in on_mount so InventoryScreen
can query and remove it generically.
"""
from __future__ import annotations

from typing import Any, Callable, List, Optional

from rich.markup import escape as rich_escape
from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, ScrollableContainer, Vertical
from textual.widget import Widget
from textual.widgets import Button, Label, ListItem, ListView, Static


# ── helpers ───────────────────────────────────────────────────────────────────

def _get_dungeons(pg: Any) -> List[Any]:
    """Return all dungeons on the player game, sorted by display_name."""
    dungeons = list(getattr(pg, "dungeons", []) or [])
    dungeons.sort(key=lambda d: str(getattr(d, "display_name", "") or ""))
    return dungeons


def _dungeon_row_markup(dungeon: Any) -> str:
    name   = rich_escape(str(getattr(dungeon, "display_name", None) or getattr(dungeon, "id", "Dungeon")))
    locked = getattr(dungeon, "locked", False)
    levels = getattr(dungeon, "levels", 1)
    pos    = getattr(dungeon, "position", (0, 0))
    x, y   = (pos[0], pos[1]) if pos and len(pos) >= 2 else (0, 0)

    coord_str  = f"[dim]({x}, {y})[/dim]"
    floors_str = f"[dim]{levels}F[/dim]"

    if locked:
        return f"[dim]🔒 {name}  {floors_str}  {coord_str}[/dim]"
    return f"{name}  {floors_str}  {coord_str}"


def _get_seed_description(dungeon_id: str) -> str:
    """Try to pull a description from DUNGEON_SETTINGS seed constants."""
    try:
        import game.constants as const
        for ds in getattr(const, "DUNGEON_SETTINGS", []) or []:
            if ds.get("dungeon_id") == dungeon_id or ds.get("id") == dungeon_id:
                return str(ds.get("description", "") or "")
    except Exception:
        pass
    return ""


def _build_dungeon_detail(dungeon: Any) -> str:
    if dungeon is None:
        return "[dim]Select a dungeon to see details.[/dim]"

    lines: list[str] = []
    name   = rich_escape(str(getattr(dungeon, "display_name", None) or getattr(dungeon, "id", "?")))
    did    = rich_escape(str(getattr(dungeon, "id", "?")))
    levels = getattr(dungeon, "levels", 1)
    locked = getattr(dungeon, "locked", False)
    pos    = getattr(dungeon, "position", (0, 0))
    x, y   = (pos[0], pos[1]) if pos and len(pos) >= 2 else (0, 0)

    lines.append(f"[bold]{name}[/bold]")
    lines.append(f"[dim]id: {did}[/dim]")
    lines.append("")
    lines.append(f"Coordinates : ({x}, {y})")
    lines.append(f"Floors      : {levels}")

    if locked:
        lines.append("")
        lines.append("[bold red]🔒 Locked[/bold red]")
        locked_text = getattr(dungeon, "locked_text", []) or []
        if locked_text:
            for lt in locked_text:
                lines.append(f"  [dim]{rich_escape(str(lt))}[/dim]")
    else:
        lines.append("")
        lines.append("[green]✓ Unlocked[/green]")

    desc = _get_seed_description(getattr(dungeon, "id", ""))
    if desc:
        lines.append("")
        lines.append(rich_escape(desc))

    return "\n".join(lines)


# ── row widget ────────────────────────────────────────────────────────────────

class _DungeonRow(ListItem):
    def __init__(self, dungeon: Any) -> None:
        super().__init__(Label(_dungeon_row_markup(dungeon)))
        self.dungeon = dungeon


# ── overlay widget ────────────────────────────────────────────────────────────

class DungeonLogOverlay(Widget):
    """
    Floating dungeon-log panel docked to the bottom of InventoryScreen.

    Up / Down navigate the list; clicking or highlighting updates the detail panel.
    Escape or ✕ closes.
    """

    can_focus = True

    BINDINGS = [
        Binding("up",     "cursor_up",     "Up",    show=False),
        Binding("down",   "cursor_down",   "Down",  show=False),
        Binding("escape", "request_close", "Close", show=True),
    ]

    DEFAULT_CSS = """
    DungeonLogOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 18;
        background: $surface;
        border-top: solid $accent;
    }

    DungeonLogOverlay > Vertical {
        height: 100%;
    }

    #dl-title-bar {
        height: 1;
        background: $boost;
    }

    #dl-header {
        width: 1fr;
        text-align: center;
        text-style: bold;
        padding: 0 1;
    }

    #dl-close-x {
        width: 3;
        min-width: 3;
        height: 1;
        border: none;
        color: $error;
        background: $boost;
    }

    #dl-body {
        height: 1fr;
        layout: horizontal;
    }

    #dl-list {
        width: 1fr;
        height: 100%;
        border-right: solid $accent 40%;
    }

    #dl-detail-scroll {
        width: 1fr;
        height: 100%;
        padding: 0 1;
    }

    #dl-detail {
        width: 100%;
    }

    #dl-hint {
        height: 1;
        padding: 0 1;
        color: $text 50%;
        text-align: center;
    }
    """

    def __init__(
        self,
        player_game: Any,
        on_close: Callable[[str | None], None],
    ) -> None:
        super().__init__()
        self._pg       = player_game
        self._on_close = on_close

    # ── compose ───────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal(id="dl-title-bar"):
                yield Static("── Dungeon Log ──", id="dl-header")
                yield Button("✕", id="dl-close-x", variant="default")
            with Horizontal(id="dl-body"):
                yield ListView(id="dl-list")
                with ScrollableContainer(id="dl-detail-scroll"):
                    yield Static(
                        "[dim]Select a dungeon to see details.[/dim]",
                        id="dl-detail",
                    )
            yield Static(
                "[dim]↑↓:navigate  🔒=locked  Esc:close[/dim]",
                id="dl-hint",
            )

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self._rebuild_list()
        self.query_one("#dl-list", ListView).focus()

    def on_key(self, event: Any) -> None:
        if event.key == "escape":
            event.stop()
            self.action_request_close()

    # ── helpers ───────────────────────────────────────────────────────────

    def _rebuild_list(self) -> None:
        dungeons = _get_dungeons(self._pg)
        lv       = self.query_one("#dl-list", ListView)
        lv.clear()

        for d in dungeons:
            lv.append(_DungeonRow(d))

        unlocked = sum(1 for d in dungeons if not getattr(d, "locked", False))
        total    = len(dungeons)
        self.query_one("#dl-header", Static).update(
            f"── Dungeon Log ({unlocked} unlocked / {total} total) ──"
        )

        if dungeons:
            self._update_detail(dungeons[0])
            self.call_after_refresh(self._highlight_first_row)
        else:
            self._update_detail(None)

    def _highlight_first_row(self) -> None:
        lv = self.query_one("#dl-list", ListView)
        if len(lv) > 0:
            lv.index = 0

    def _update_detail(self, dungeon: Optional[Any]) -> None:
        self.query_one("#dl-detail", Static).update(_build_dungeon_detail(dungeon))

    # ── events ────────────────────────────────────────────────────────────

    @on(ListView.Highlighted, "#dl-list")
    def _on_highlighted(self, event: Any) -> None:
        event.stop()
        child = event.item
        if isinstance(child, _DungeonRow):
            self._update_detail(child.dungeon)

    @on(ListView.Selected, "#dl-list")
    def _on_selected(self, event: Any) -> None:
        event.stop()
        child = event.item
        if isinstance(child, _DungeonRow):
            self._update_detail(child.dungeon)
        self.query_one("#dl-list", ListView).focus()

    @on(Button.Pressed, "#dl-close-x")
    def _on_close_btn(self) -> None:
        self.action_request_close()

    # ── actions ───────────────────────────────────────────────────────────

    def action_cursor_up(self) -> None:
        self.query_one("#dl-list", ListView).action_cursor_up()

    def action_cursor_down(self) -> None:
        self.query_one("#dl-list", ListView).action_cursor_down()

    def action_request_close(self) -> None:
        self._on_close(None)