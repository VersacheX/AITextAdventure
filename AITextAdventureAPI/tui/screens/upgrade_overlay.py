"""
UpgradeOverlay: stat and power point allocation for the selected character.

Mirrors `old/game_screens/select_upgrade_screen.py`: the player distributes
unused stat points (STR/DEX/INT/CON) and unused power points (HP/AP) to
improve the selected character. The overlay shows current values, available
points, and a simple +/- interface for each stat.

The console version uses +/- keys to increment a quantity counter for the
selected stat, then Enter to apply. The TUI mirrors that with buttons for
each stat showing current value + pending allocation, and Apply/Reset buttons.

Stats consume stat points (1 point = 1 stat point).
Power (HP/AP) consumes power points (1 point = 1 HP or 1 AP).

The overlay auto-closes when both pools (unused_stat_points and
unused_power_points) are exhausted after applying changes.
"""
from __future__ import annotations

from typing import Any, Callable, Optional

from textual import on
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label, Static

from tui.screens.base_screen import BaseScreen


class UpgradeOverlay(Static):
    """Floating upgrade panel for stat/power allocation - positioned at bottom."""

    DEFAULT_CSS = """
    UpgradeOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 16;
        background: $surface;
        border-top: thick $accent;
    }

    #upgrade-title {
        width: 100%;
        text-align: center;
        text-style: bold;
        background: $boost;
        color: $text;
        padding: 0 1;
        height: 1;
    }

    #upgrade-content {
        width: 100%;
        height: 1fr;
        padding: 1 2;
        layout: horizontal;
    }

    #upgrade-left {
        width: 1fr;
        height: 100%;
        padding-right: 2;
        border-right: solid $accent;
    }

    #upgrade-right {
        width: 1fr;
        height: 100%;
        padding-left: 2;
    }

    .section-header {
        width: 100%;
        text-align: center;
        color: $text;
        text-style: bold;
        height: 1;
        margin-bottom: 1;
    }

    .stat-row {
        width: 100%;
        height: 3;
        layout: horizontal;
        align: left middle;
        margin-bottom: 1;
    }

    .stat-label {
        width: 8;
        height: 3;
        content-align: left middle;
        color: $text;
        text-style: bold;
    }

    .stat-value {
        width: 8;
        height: 3;
        content-align: center middle;
        color: $accent;
    }

    .stat-pending {
        width: 8;
        height: 3;
        content-align: center middle;
        color: $warning;
    }

    .stat-row Button {
        height: 3;
        width: 5;
        min-width: 5;
        margin-left: 1;
    }

    .stat-grid-row {
        width: 100%;
        height: auto;
        layout: horizontal;
    }

    .stat-grid-row .stat-row {
        width: 1fr;
    }

    #upgrade-actions {
        width: 100%;
        layout: horizontal;
        height: 3;
        align: center middle;
    }

    #upgrade-actions Button {
        min-width: 12;
        height: 3;
        margin-right: 1;
    }

    #upgrade-actions Button:last-child {
        margin-right: 0;
    }
    """

    def __init__(
        self,
        player: Any,
        player_game: Any,
        on_close: Callable[[str | None], None],
    ) -> None:
        super().__init__()
        self._player = player
        self._player_game = player_game
        self._on_close = on_close

        # Pending allocations (not yet applied to player)
        self._pending: dict[str, int] = {
            "hp": 0,
            "ap": 0,
            "str": 0,
            "dex": 0,
            "int": 0,
            "con": 0,
        }

    def compose(self) -> ComposeResult:
        """Build the upgrade panel UI."""
        with Vertical():
            yield Static("=== Upgrade Stats ===", id="upgrade-title")

            with Horizontal(id="upgrade-content"):
                # Left column: Power Points
                with Vertical(id="upgrade-left"):
                    yield Static("", classes="section-header", id="pp-header")
                    yield self._build_stat_row("hp", "HP")
                    yield self._build_stat_row("ap", "AP")

                # Right column: Stat Points (2x2 grid)
                with Vertical(id="upgrade-right"):
                    yield Static("", classes="section-header", id="sp-header")
                    with Horizontal(classes="stat-grid-row"):
                        yield self._build_stat_row("str", "STR")
                        yield self._build_stat_row("dex", "DEX")
                    with Horizontal(classes="stat-grid-row"):
                        yield self._build_stat_row("int", "INT")
                        yield self._build_stat_row("con", "CON")

            # Action buttons
            with Horizontal(id="upgrade-actions"):
                yield Button("Apply", id="btn-apply", variant="primary")
                yield Button("Reset", id="btn-reset", variant="default")
                yield Button("Cancel", id="btn-cancel", variant="default")

    def _build_stat_row(self, key: str, label: str) -> Horizontal:
        """Build a single stat row with label, current value, pending, and +/- buttons."""
        row = Horizontal(classes="stat-row")
        row.compose_add_child(Static(label, classes="stat-label"))
        row.compose_add_child(Static("", classes="stat-value", id=f"val-{key}"))
        row.compose_add_child(Static("", classes="stat-pending", id=f"pend-{key}"))
        row.compose_add_child(Button("−", id=f"btn-dec-{key}", variant="default"))
        row.compose_add_child(Button("+", id=f"btn-inc-{key}", variant="primary"))
        return row

    def on_mount(self) -> None:
        """Initialize display with current player stats and available points."""
        self.add_class("inv-overlay")
        self._refresh_display()
        self.focus()

    def on_player_changed(self, new_player: Any) -> None:
        """Called by InventoryScreen when the active character changes."""
        self._player = new_player
        # Reset pending allocations
        for key in self._pending:
            self._pending[key] = 0
        self._refresh_display()

    def _refresh_display(self) -> None:
        """Update all stat displays and available points."""
        # Update available points display
        stat_points = int(getattr(self._player, "unused_stat_points", 0) or 0)
        power_points = int(getattr(self._player, "unused_power_points", 0) or 0)

        # Calculate remaining after pending allocations
        pending_stat = sum(self._pending[k] for k in ("str", "dex", "int", "con"))
        pending_power = sum(self._pending[k] for k in ("hp", "ap"))
        remaining_stat = max(0, stat_points - pending_stat)
        remaining_power = max(0, power_points - pending_power)

        try:
            self.query_one("#pp-header", Static).update(
                f"[bold]Power Points:[/bold] [yellow]{remaining_power}[/yellow]"
            )
        except Exception:
            pass

        try:
            self.query_one("#sp-header", Static).update(
                f"[bold]Stat Points:[/bold] [yellow]{remaining_stat}[/yellow]"
            )
        except Exception:
            pass

        # Update each stat row
        self._update_stat_display("hp", "max_hp", is_power=True)
        self._update_stat_display("ap", "max_ap", is_power=True)
        self._update_stat_display("str", "strength")
        self._update_stat_display("dex", "dexterity")
        self._update_stat_display("int", "intelligence")
        self._update_stat_display("con", "constitution")

    def _update_stat_display(
        self, key: str, attr: str, *, is_power: bool = False
    ) -> None:
        """Update the current value and pending display for one stat."""
        current = int(getattr(self._player, attr, 0) or 0)
        pending = self._pending.get(key, 0)

        try:
            self.query_one(f"#val-{key}", Static).update(str(current))
        except Exception:
            pass

        try:
            pend_widget = self.query_one(f"#pend-{key}", Static)
            if pending > 0:
                pend_widget.update(f"+{pending}")
            else:
                pend_widget.update("")
        except Exception:
            pass

    @on(Button.Pressed)
    def _on_button(self, event: Button.Pressed) -> None:
        """Handle all button presses."""
        button_id = event.button.id or ""

        if button_id == "btn-apply":
            self._apply_changes()
        elif button_id == "btn-reset":
            self._reset_pending()
        elif button_id == "btn-cancel":
            self._on_close(None)
            self.remove()
        elif button_id.startswith("btn-inc-"):
            key = button_id.replace("btn-inc-", "")
            self._increment(key)
        elif button_id.startswith("btn-dec-"):
            key = button_id.replace("btn-dec-", "")
            self._decrement(key)

    def _increment(self, key: str) -> None:
        """Increment pending allocation for the given stat."""
        is_power = key in ("hp", "ap")
        stat_points = int(getattr(self._player, "unused_stat_points", 0) or 0)
        power_points = int(getattr(self._player, "unused_power_points", 0) or 0)

        if is_power:
            # Check if we have power points available
            pending_power = sum(self._pending[k] for k in ("hp", "ap"))
            if pending_power >= power_points:
                return  # Can't allocate more than available
        else:
            # Check if we have stat points available
            pending_stat = sum(self._pending[k] for k in ("str", "dex", "int", "con"))
            if pending_stat >= stat_points:
                return  # Can't allocate more than available

        self._pending[key] += 1
        self._refresh_display()

    def _decrement(self, key: str) -> None:
        """Decrement pending allocation for the given stat."""
        if self._pending[key] > 0:
            self._pending[key] -= 1
            self._refresh_display()

    def _reset_pending(self) -> None:
        """Reset all pending allocations to zero."""
        for key in self._pending:
            self._pending[key] = 0
        self._refresh_display()

    def _apply_changes(self) -> None:
        """Apply pending allocations to the player character."""
        # Check if there are any pending changes
        total_pending = sum(self._pending.values())
        if total_pending == 0:
            self.notify("No changes to apply.", severity="warning")
            return

        # Apply stat allocations
        str_inc = self._pending.get("str", 0)
        dex_inc = self._pending.get("dex", 0)
        int_inc = self._pending.get("int", 0)
        con_inc = self._pending.get("con", 0)

        if str_inc or dex_inc or int_inc or con_inc:
            self._player.allocate_stats(
                str_inc=str_inc,
                dex_inc=dex_inc,
                con_inc=con_inc,
                int_inc=int_inc,
                use_stat_points=True,
            )

        # Apply power point allocations
        hp_add = self._pending.get("hp", 0)
        ap_add = self._pending.get("ap", 0)

        if hp_add or ap_add:
            self._player.apply_power_point_allocation(hp_points=hp_add, ap_points=ap_add)

        # Reset pending
        for key in self._pending:
            self._pending[key] = 0

        # Check if both pools are exhausted
        remaining_stat = int(getattr(self._player, "unused_stat_points", 0) or 0)
        remaining_power = int(getattr(self._player, "unused_power_points", 0) or 0)

        # Signal inventory screen to refresh
        self._on_close("stats_upgraded")

        if remaining_stat <= 0 and remaining_power <= 0:
            self.notify("All points allocated!", title="Success")
            self.remove()
        else:
            # Refresh display and keep overlay open
            self.notify("Changes applied.", title="Success")
            self._refresh_display()