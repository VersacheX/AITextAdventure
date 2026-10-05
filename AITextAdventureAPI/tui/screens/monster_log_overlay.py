"""
MonsterLogOverlay: floating monster-log widget for InventoryScreen.

Mirrors `old/game_screens/monster_log_screen.py`, following the same
docked-list-with-detail-panel pattern already proven in `equip_overlay.py`:
  - Lists every hostile the player has slain at least once, built from
    `player_game.enemies_slain` via `tui.services.monster_log_service`.
  - Up / Down navigate the list; the detail panel always shows the
    highlighted hostile's full stat block (stats, attributes, abilities,
    drops) reusing the legacy `format_hostile_summary_full` formatter.
  - Escape closes the overlay.

This overlay is read-only — there is no equip/discard/use action, matching
the legacy screen's behavior (up/down/esc only).

The CSS class "inv-overlay" is added in on_mount so InventoryScreen can
query and remove any open overlay generically.
"""
from __future__ import annotations

from typing import Any, Callable

from rich.markup import escape as rich_escape
from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widget import Widget
from textual.widgets import Label, ListItem, ListView, Static

from tui.services.monster_log_service import build_slain_hostiles


def _hostile_row_label(hostile: Any, count: int) -> str:
    name = rich_escape(str(getattr(hostile, "name", "?")))
    lvl  = getattr(hostile, "level", "?")
    return f"{name}  [dim](lvl {lvl})[/dim]  [yellow]x{count}[/yellow]"


def _safe(value: Any, default: str = "—") -> str:
    if value is None:
        return default
    text = str(value)
    return text if text.strip() else default


def _drop_name(drop: Any) -> str:
    if drop is None:
        return "None"
    return _safe(getattr(drop, "name", drop), "None")


def _build_hostile_detail(hostile: Any | None) -> str:
    if hostile is None:
        return "[dim]No hostiles slain yet.[/dim]"

    from game.constants import fmt_element_glyphs, fmt_status_glyphs

    def esc(value: Any, default: str = "—") -> str:
        return rich_escape(_safe(value, default))

    name = esc(getattr(hostile, "name", "?"), "?")
    level = esc(getattr(hostile, "level", "?"), "?")

    # ── abilities: resolve PlayerAbility display names ──────────────────────
    ability_names: list[str] = []
    for ab in getattr(hostile, "abilities", []) or []:
        ab_name = getattr(ab, "name", None) or getattr(ab, "id", None)
        ab_lvl = getattr(ab, "level", None)
        if ab_name:
            label = str(ab_name)
            if ab_lvl:
                label += f" (lvl {ab_lvl})"
            ability_names.append(rich_escape(label))

    # ── affinities rendered with shared compact glyphs ──────────────────────
    weaknesses  = fmt_element_glyphs(getattr(hostile, "weaknesses", []) or [])
    resistances = fmt_element_glyphs(getattr(hostile, "resistances", []) or [])
    immunities  = fmt_status_glyphs(getattr(hostile, "immunities", []) or [])

    money_range = getattr(hostile, "money_range", None)

    lines: list[str] = []
    lines.append(f"[b]{name}[/b]  [dim]lvl {level}[/dim]")
    lines.append(f"[dim]{esc(getattr(hostile, 'hostile_type', None))}[/dim]")
    lines.append("")

    # Core
    lines.append("[u]Core[/u]")
    lines.append(f"Rarity:  {esc(getattr(hostile, 'rarity', None))}")
    lines.append(
        f"HP:  {esc(getattr(hostile, 'current_hp', None))}/{esc(getattr(hostile, 'max_hp', None))}"
    )
    lines.append(
        f"AP:  {esc(getattr(hostile, 'current_ap', None))}/{esc(getattr(hostile, 'max_ap', None))}"
    )
    lines.append(f"Defense:  {esc(getattr(hostile, 'defense', None))}")
    lines.append(f"Base XP:  {esc(getattr(hostile, 'base_xp', None))}")
    lines.append("")

    # Stats
    lines.append("[u]Stats[/u]")
    lines.append(
        f"STR {esc(getattr(hostile, 'strength', None))}   "
        f"DEX {esc(getattr(hostile, 'dexterity', None))}"
    )
    lines.append(
        f"INT {esc(getattr(hostile, 'intelligence', None))}   "
        f"CON {esc(getattr(hostile, 'constitution', None))}"
    )
    lines.append("")

    # Attacks
    lines.append("[u]Attacks[/u]")
    lines.append(f"Basic:   {esc(getattr(hostile, 'basic_attack', None))}")
    lines.append(f"Strong:  {esc(getattr(hostile, 'strong_attack', None))}")
    lines.append("")

    # Abilities
    lines.append("[u]Abilities[/u]")
    if ability_names:
        lines.extend(f"- {a}" for a in ability_names)
    else:
        lines.append("[dim]None[/dim]")
    lines.append("")

    # Affinities (compact glyphs matching the ability-handler status column)
    lines.append("[u]Affinities[/u]")
    lines.append(f"Weakness:    {rich_escape(weaknesses)}")
    lines.append(f"Resistance:  {rich_escape(resistances)}")
    lines.append(f"Immunity:    {rich_escape(immunities)}")
    lines.append("")

    # Loot — each drop on its own line
    lines.append("[u]Loot[/u]")
    lines.append(f"Common Drop:  {rich_escape(_drop_name(getattr(hostile, 'common_drop', None)))}")
    lines.append(f"Rare Drop:    {rich_escape(_drop_name(getattr(hostile, 'rare_drop', None)))}")
    money_txt = f"{money_range[0]} - {money_range[1]}" if money_range else "—"
    lines.append(f"Money:        {rich_escape(money_txt)}")

    return "\n".join(lines)


class _HostileRow(ListItem):
    def __init__(self, hostile: Any, count: int) -> None:
        super().__init__(Label(_hostile_row_label(hostile, count)))
        self.hostile = hostile


class MonsterLogOverlay(Widget):
    """
    Floating monster-log viewer docked to the bottom of InventoryScreen.

    Up / Down navigate the list of slain hostiles.  The right-hand panel
    always shows the full stat/ability/drop summary for the highlighted
    entry.  Escape closes the overlay.  There is no edit/action flow — this
    overlay is purely informational, matching `old/game_screens/monster_log_screen.py`.
    """

    can_focus = True

    BINDINGS = [
        Binding("up",     "cursor_up",     "Up",    show=False),
        Binding("down",   "cursor_down",   "Down",  show=False),
        Binding("escape", "request_close", "Close", show=True),
    ]

    DEFAULT_CSS = """
    MonsterLogOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 20;
        background: $surface;
        border-top: solid $accent;
        layout: vertical;
    }

    #ml-header {
        height: 1;
        text-align: center;
        text-style: bold;
        background: $boost;
        padding: 0 1;
    }

    #ml-main-row {
        height: 1fr;
    }

    #ml-list-panel {
        width: 1fr;
        height: 100%;
    }

    #ml-list {
        height: 100%;
    }

    #ml-detail-panel {
        width: 46;
        height: 100%;
        padding: 0 1;
        overflow-y: auto;
        scrollbar-size-vertical: 1;
        border-left: solid $accent 30%;
    }

    #ml-detail-text {
        width: 100%;
        height: auto;
    }

    #ml-hint {
        height: 1;
        padding: 0 1;
        color: $text 50%;
        text-align: center;
        border-top: solid $accent 30%;
    }
    """

    def __init__(self, player_game: Any, on_close: Callable[[str | None], None]) -> None:
        super().__init__()
        self._pg       = player_game
        self._on_close = on_close
        self._hostiles: list[Any] = []
        self._counts: dict[str, int] = {}

    # ── compose ───────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        yield Static("── Monster Log ──", id="ml-header")
        with Horizontal(id="ml-main-row"):
            with Vertical(id="ml-list-panel"):
                yield ListView(id="ml-list")
            with VerticalScroll(id="ml-detail-panel"):
                yield Static("", id="ml-detail-text")
        yield Static(
            "[dim]▲▼:navigate  Esc:close[/dim]",
            id="ml-hint",
        )

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self._hostiles, self._counts = build_slain_hostiles(self._pg)
        self._rebuild_list()
        self.query_one("#ml-list", ListView).focus()

    # ── internal ──────────────────────────────────────────────────────────

    def _rebuild_list(self) -> None:
        lv = self.query_one("#ml-list", ListView)
        lv.clear()
        for hostile in self._hostiles:
            count = self._counts.get(getattr(hostile, "id", None), 0)
            lv.append(_HostileRow(hostile, count))
        self.query_one("#ml-header", Static).update(
            f"── Monster Log ({len(self._hostiles)} entries) ──"
        )
        self._update_detail(self._highlighted_hostile())

    def _highlighted_hostile(self) -> Any | None:
        lv    = self.query_one("#ml-list", ListView)
        child = lv.highlighted_child
        return child.hostile if isinstance(child, _HostileRow) else None

    def _update_detail(self, hostile: Any | None) -> None:
        self.query_one("#ml-detail-text", Static).update(_build_hostile_detail(hostile))

    # ── events ────────────────────────────────────────────────────────────

    @on(ListView.Highlighted, "#ml-list")
    def _on_highlighted(self, event: ListView.Highlighted) -> None:
        hostile = event.item.hostile if isinstance(event.item, _HostileRow) else None
        self._update_detail(hostile)

    # ── actions ───────────────────────────────────────────────────────────

    def action_cursor_up(self) -> None:
        self.query_one("#ml-list", ListView).action_cursor_up()

    def action_cursor_down(self) -> None:
        self.query_one("#ml-list", ListView).action_cursor_down()

    def action_request_close(self) -> None:
        self._on_close(None)