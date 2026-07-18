"""
AccessorySlotScreen: modal for choosing which accessory slot to equip into.

Flow
----
1. Shows all slots (0 … max_accessory_slots-1).
   - Empty slots:    "[Empty]"  → equip immediately on confirm.
   - Occupied slots: accessory name + key stats → asks "Replace?" inline.
2. Escape / Cancel dismisses with None (no action taken).
3. On confirmation the screen dismisses with the chosen slot index (int)
   and, if replacing, the outgoing accessory is returned to inventory
   before the caller equips the new one.

The caller (equip_overlay._do_equip) receives the slot index and handles
the actual equip call so all inventory bookkeeping stays in one place.
"""
from __future__ import annotations

from typing import Any

from rich.markup import escape as rich_escape
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label, ListItem, ListView, Static

from tui.screens.base_screen import BaseScreen


def _acc_summary(acc: Any) -> str:
    """One-line summary of an equipped accessory for the slot list."""
    name  = rich_escape(str(getattr(acc, "name", "?")))
    parts: list[str] = []
    for attr, label in (("strength","STR"), ("dexterity","DEX"),
                         ("intelligence","INT"), ("constitution","CON")):
        v = int(getattr(acc, attr, 0) or 0)
        if v:
            parts.append(f"+{v}{label}")
    dmg_b  = int(getattr(acc, "damage_bonus", 0) or 0)
    crit_b = float(getattr(acc, "crit_bonus", 0.0) or 0)
    if dmg_b:
        parts.append(f"+{dmg_b}DMG")
    if crit_b:
        parts.append(f"+{crit_b:.0f}%Crit")
    imm = list(getattr(acc, "immunities", []) or [])
    if imm:
        parts.append(f"Imm:{len(imm)}")
    stat_s = f"  [dim]{', '.join(parts)}[/dim]" if parts else ""
    return f"{name}{stat_s}"


class _SlotRow(ListItem):
    def __init__(self, slot_index: int, current_acc: Any | None) -> None:
        self.slot_index   = slot_index
        self.current_acc  = current_acc
        if current_acc is None:
            label_text = f"[dim]Slot {slot_index + 1}  —  [Empty][/dim]"
        else:
            label_text = f"Slot {slot_index + 1}  —  {_acc_summary(current_acc)}"
        super().__init__(Label(label_text))


class AccessorySlotScreen(BaseScreen):
    """Choose which slot to equip an accessory into.

    Dismissed with the chosen slot index (int) or None if cancelled.
    When the chosen slot is occupied the outgoing accessory is unequipped
    back to inventory before dismissal so the caller can equip the new one.
    """

    show_header = False
    show_footer = False

    BINDINGS = [
        Binding("escape", "cancel", "Cancel", show=True),
        Binding("enter",  "confirm_slot", "Confirm", show=True),
    ]

    DEFAULT_CSS = """
    AccessorySlotScreen {
        align: center middle;
        background: $background 60%;
    }

    #slot-panel {
        width: 62;
        height: auto;
        max-height: 28;
        border: round $accent;
        padding: 1 2;
        background: $surface;
    }

    #slot-title {
        text-style: bold;
        text-align: center;
        margin-bottom: 1;
    }

    #slot-subtitle {
        color: $text 55%;
        text-align: center;
        margin-bottom: 1;
    }

    #slot-list {
        height: auto;
        max-height: 10;
        margin-bottom: 1;
    }

    #confirm-row {
        height: auto;
        display: none;
        margin-bottom: 1;
        padding: 0 1;
        background: $boost;
    }

    #confirm-text {
        width: 1fr;
        color: $warning;
    }

    #slot-btn-row {
        align: center middle;
        height: auto;
        margin-top: 1;
    }

    #slot-btn-row Button {
        margin: 0 1;
        min-width: 14;
    }
    """

    def __init__(self, item: Any, player: Any, player_game: Any) -> None:
        super().__init__()
        self._item        = item
        self._player      = player
        self._player_game = player_game
        self._pending_replace: bool = False

    # ── compose ───────────────────────────────────────────────────────────

    def compose_content(self) -> ComposeResult:
        accessories = list(getattr(self._player, "accessories",        []) or [])
        max_slots   = int(getattr(self._player, "max_accessory_slots", 3) or 3)
        iname       = rich_escape(str(getattr(self._item, "name", "?")))

        with Vertical(id="slot-panel"):
            yield Static(f"Equip  {iname}", id="slot-title")
            yield Static("Choose a slot — occupied slots will be replaced.", id="slot-subtitle")
            yield ListView(id="slot-list")
            with Horizontal(id="confirm-row"):
                yield Static("", id="confirm-text")
            with Horizontal(id="slot-btn-row"):
                yield Button("Equip",  id="btn-slot-equip",  variant="primary", disabled=True)
                yield Button("Cancel", id="btn-slot-cancel")

    def on_mount(self) -> None:
        self._rebuild_list()
        self.query_one("#slot-list", ListView).focus()

    # ── list population ───────────────────────────────────────────────────

    def _rebuild_list(self) -> None:
        accessories = list(getattr(self._player, "accessories",        []) or [])
        max_slots   = int(getattr(self._player, "max_accessory_slots", 3) or 3)
        lv = self.query_one("#slot-list", ListView)
        lv.clear()
        for i in range(max_slots):
            current = accessories[i] if i < len(accessories) else None
            lv.append(_SlotRow(i, current))

    # ── events ────────────────────────────────────────────────────────────

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        row = event.item
        if not isinstance(row, _SlotRow):
            self._set_confirm(None)
            return
        self.query_one("#btn-slot-equip", Button).disabled = False
        if row.current_acc is not None:
            acc_name = rich_escape(str(getattr(row.current_acc, "name", "?")))
            self._set_confirm(f"Replace  {acc_name}?  It will return to your inventory.")
        else:
            self._set_confirm(None)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Double-click / Enter on list row acts as confirm."""
        self._confirm_highlighted()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-slot-equip":
            self._confirm_highlighted()
        elif event.button.id == "btn-slot-cancel":
            self.dismiss(None)

    # ── actions ───────────────────────────────────────────────────────────

    def action_confirm_slot(self) -> None:
        self._confirm_highlighted()

    def action_cancel(self) -> None:
        self.dismiss(None)

    # ── internal ─────────────────────────────────────────────────────────

    def _set_confirm(self, message: str | None) -> None:
        row = self.query_one("#confirm-row")
        txt = self.query_one("#confirm-text", Static)
        if message:
            txt.update(f"[yellow]{message}[/yellow]")
            row.display = True
        else:
            row.display = False

    def _confirm_highlighted(self) -> None:
        lv  = self.query_one("#slot-list", ListView)
        row = lv.highlighted_child
        if not isinstance(row, _SlotRow):
            return
        slot_index  = row.slot_index
        current_acc = row.current_acc

        # If slot is occupied, unequip current accessory back to inventory first
        if current_acc is not None:
            try:
                self._player.unequip_accessory(self._player_game, current_acc)
            except Exception:
                pass

        self.dismiss(slot_index)