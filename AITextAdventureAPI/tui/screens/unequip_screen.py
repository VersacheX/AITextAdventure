"""
UnequipScreen: modal for removing equipped gear back to inventory.

Flow
----
1. Lists every occupied equipment slot for the selected character:
   weapon, head/body/arms/legs armor, and each equipped accessory.
2. Click (or arrow-key + Enter) a slot to select it — a Yes/No confirm
   dialog appears. Confirming returns the item to the shared inventory and
   the list refreshes in place so several pieces can be removed in one visit.
3. Escape / Close dismisses. The screen dismisses with True if anything was
   unequipped (so the caller can refresh its list) or None if nothing changed.

Only equipped slots are shown — empty slots are omitted so the list is a
direct "what can I take off" view.
"""
from __future__ import annotations

from typing import Any

from rich.markup import escape as rich_escape
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label, ListItem, ListView, Static

from tui.screens.base_screen import BaseScreen
from tui.screens.confirm_screen import ConfirmScreen

# (label, slot-attr) for the fixed armor/weapon slots, in display order.
_ARMOR_SLOTS: tuple[tuple[str, str], ...] = (
    ("HEAD", "head_armor"),
    ("BODY", "body_armor"),
    ("ARMS", "arm_armor"),
    ("LEGS", "leg_armor"),
)


def _gear_summary(item: Any) -> str:
    """One-line stat summary for an equipped item."""
    parts: list[str] = []
    dmg = int(getattr(item, "damage", 0) or 0)
    dfn = int(getattr(item, "defense", 0) or 0)
    if dmg:
        parts.append(f"DMG:{dmg}")
    if dfn:
        parts.append(f"DEF:{dfn}")
    for attr, label in (("strength", "STR"), ("dexterity", "DEX"),
                        ("intelligence", "INT"), ("constitution", "CON")):
        v = int(getattr(item, attr, 0) or 0)
        if v:
            parts.append(f"+{v}{label}")
    return f"  [dim]{', '.join(parts)}[/dim]" if parts else ""


class _EquippedRow(ListItem):
    """A single equipped slot. `kind` is 'weapon' | 'armor' | 'accessory'."""

    def __init__(self, kind: str, label: str, item: Any, slot_attr: str | None = None) -> None:
        self.kind      = kind
        self.item      = item
        self.slot_attr = slot_attr
        iname = rich_escape(str(getattr(item, "name", "?")))
        super().__init__(Label(f"{label:<5} {iname}{_gear_summary(item)}"))


class UnequipScreen(BaseScreen):
    """Choose an equipped slot to remove. Dismissed with True if changed, else None."""

    show_header = False
    show_footer = False

    BINDINGS = [
        Binding("escape", "cancel",  "Cancel",   show=True),
        Binding("enter",  "confirm", "Unequip",  show=True),
    ]

    DEFAULT_CSS = """
    UnequipScreen {
        align: center middle;
        background: $background 60%;
    }

    #uneq-panel {
        width: 62;
        height: auto;
        max-height: 28;
        border: round $accent;
        padding: 1 2;
        background: $surface;
    }

    #uneq-title {
        text-style: bold;
        text-align: center;
        margin-bottom: 1;
    }

    #uneq-subtitle {
        color: $text 55%;
        text-align: center;
        margin-bottom: 1;
    }

    #uneq-list {
        height: auto;
        max-height: 12;
        margin-bottom: 1;
    }

    #uneq-btn-row {
        align: center middle;
        height: auto;
        margin-top: 1;
    }

    #uneq-btn-row Button {
        margin: 0 1;
        min-width: 14;
    }
    """

    def __init__(self, player: Any, player_game: Any) -> None:
        super().__init__()
        self._player      = player
        self._player_game = player_game
        self._changed     = False

    # ── compose ───────────────────────────────────────────────────────────

    def compose_content(self) -> ComposeResult:
        pname = rich_escape(str(getattr(self._player, "name", "?")))
        with Vertical(id="uneq-panel"):
            yield Static(f"Unequip — {pname}", id="uneq-title")
            yield Static("Select a slot to return its item to inventory.", id="uneq-subtitle")
            yield ListView(id="uneq-list")
            with Horizontal(id="uneq-btn-row"):
                yield Button("Close", id="btn-uneq-cancel")

    def on_mount(self) -> None:
        self._rebuild_list()
        self.query_one("#uneq-list", ListView).focus()

    # ── list population ───────────────────────────────────────────────────

    def _rebuild_list(self) -> None:
        lv = self.query_one("#uneq-list", ListView)
        lv.clear()

        weapon = getattr(self._player, "equipped_weapon", None)
        if weapon is not None:
            lv.append(_EquippedRow("weapon", "WPN", weapon))

        for label, attr in _ARMOR_SLOTS:
            piece = getattr(self._player, attr, None)
            if piece is not None:
                lv.append(_EquippedRow("armor", label, piece, slot_attr=attr))

        for acc in list(getattr(self._player, "accessories", []) or []):
            lv.append(_EquippedRow("accessory", "ACC", acc))

        # Nothing left to remove — close out (report whether anything changed).
        if len(lv.children) == 0:
            self.dismiss(True if self._changed else None)
            return

    # ── events ────────────────────────────────────────────────────────────

    # def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
    #     row = event.item
    #     if not isinstance(row, _EquippedRow):
    #         self._set_confirm(None)
    #         self.query_one("#btn-uneq-do", Button).disabled = True
    #         return
    #     self.query_one("#btn-uneq-do", Button).disabled = False
    #     iname = rich_escape(str(getattr(row.item, "name", "?")))
    #     self._set_confirm(f"Unequip {iname}?  It will return to your inventory.")

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Click / Enter on a row asks to confirm the unequip."""
        self._confirm_highlighted()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-uneq-cancel":
            self.dismiss(True if self._changed else None)

    # ── actions ───────────────────────────────────────────────────────────

    def action_confirm(self) -> None:
        self._confirm_highlighted()

    def action_cancel(self) -> None:
        self.dismiss(True if self._changed else None)

    # ── internal ─────────────────────────────────────────────────────────

    # def _set_confirm(self, message: str | None) -> None:
    #     row = self.query_one("#uneq-confirm-row")
    #     txt = self.query_one("#uneq-confirm-text", Static)
    #     if message:
    #         txt.update(f"[yellow]{message}[/yellow]")
    #         row.display = True
    #     else:
    #         row.display = False

    def _confirm_highlighted(self) -> None:
        lv  = self.query_one("#uneq-list", ListView)
        row = lv.highlighted_child
        if not isinstance(row, _EquippedRow):
            return

        iname = rich_escape(str(getattr(row.item, "name", "item")))

        def _on_confirm(confirmed: bool | None) -> None:
            if confirmed:
                self._do_unequip(row)

        self.app.push_screen(
            ConfirmScreen(f"Unequip {iname}? It will return to your inventory."),
            _on_confirm,
        )

    def _do_unequip(self, row: "_EquippedRow") -> None:
        try:
            if row.kind == "weapon":
                ok = self._player.unequip_weapon(self._player_game)
            elif row.kind == "armor":
                ok = self._player.unequip_armor(self._player_game, row.slot_attr)
            else:  # accessory
                ok = self._player.unequip_accessory(self._player_game, row.item)
        except Exception as exc:
            self.app.notify(f"Error unequipping: {rich_escape(str(exc))}", title="Unequip")
            return

        if ok:
            self._changed = True
            iname = rich_escape(str(getattr(row.item, "name", "item")))
            self.app.notify(f"Unequipped {iname}.", title="Unequip")

        # Refresh in place so more pieces can be removed in the same visit.
        self._rebuild_list()