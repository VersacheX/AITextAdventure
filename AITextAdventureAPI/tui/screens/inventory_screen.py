"""
InventoryScreen: character management screen.

Layout:
  ┌── info bar (chapter / money) ──────────────────────────────────┐
  │ [Items (i)] [Equip (e)] [Party (p)] [Learn (l)] [Upgrade (u)]  │  action bar
  │ [Monster Log (m)] [NPC Log (n)*] [Save (s)]                   │  *unlocked only
  ├────────────────────────────────────────────────────────────────┤
  │  Card 0  │  Card 1  │ ► Card 2 ◄ │  Card 3  │  Card 4         │  character row
  │  ...                                                           │
  ├────────────────────────────────────────────────────────────────┤
  │ pager / status bar                                             │
  └────────────────────────────────────────────────────────────────┘

← / → (or A / D) navigate between characters, also while an overlay is open.
B toggles the abilities list for the selected character (only when no overlay).
Escape closes any open overlay first, then returns to the previous screen.

Overlay widgets (Items, Equip, Party, Learn, Upgrade, Monster Log, NPC Log)
float above the character cards on the "overlay" CSS layer.  Each overlay
adds the CSS class "inv-overlay" in its on_mount so this screen can close
them generically.

The NPC Log button/binding is only shown when the active game's
`npc_log_locked` is False, mirroring `old/game_screens/inventory_screen.py`
(`(n)pc's` only appears once unlocked through story progression).
"""
from __future__ import annotations

from typing import Any

from rich.markup import escape as rich_escape
from textual import events, on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal
from textual.widgets import Button, Static

from tui.screens.base_screen import BaseScreen
from tui.services.game_state import get_active_game

_MAX_DISPLAY: int = 5


def _build_card_text(
    player: Any, player_game: Any, *, show_abilities: bool = False
) -> str:
    """Return Rich-markup text content for one character card."""
    lines: list[str] = []

    name  = rich_escape(str(getattr(player, "name", "?")))
    level = getattr(player, "level", 0)
    lines.append(f"[bold]{name}[/bold]  Lv.{level}")
    lines.append("")

    cur_hp = getattr(player, "current_hp", 0)
    max_hp = getattr(player, "max_hp",     0)
    cur_ap = getattr(player, "current_ap", 0)
    max_ap = getattr(player, "max_ap",     0)
    lines.append(f"HP  {cur_hp}/{max_hp}")
    lines.append(f"AP  {cur_ap}/{max_ap}")

    cur_xp = getattr(player, "experience", 0)
    try:
        next_xp = player.get_required_experience_to_level()
    except Exception:
        next_xp = "?"
    lines.append(f"XP  {cur_xp}/{next_xp}")
    lines.append("")

    str_b = getattr(player, "strength",     0)
    dex_b = getattr(player, "dexterity",    0)
    int_b = getattr(player, "intelligence", 0)
    con_b = getattr(player, "constitution", 0)
    try:
        str_bonus = player.get_modified_strength()     - str_b
        dex_bonus = player.get_modified_dexterity()    - dex_b
        int_bonus = player.get_modified_intelligence() - int_b
        con_bonus = player.get_modified_constitution() - con_b
        lines.append(f"STR {str_b}+{str_bonus}")
        lines.append(f"DEX {dex_b}+{dex_bonus}")
        lines.append(f"INT {int_b}+{int_bonus}")
        lines.append(f"CON {con_b}+{con_bonus}")
    except Exception:
        lines.append(f"STR {str_b}")
        lines.append(f"DEX {dex_b}")
        lines.append(f"INT {int_b}")
        lines.append(f"CON {con_b}")
    lines.append("")

    weapon = getattr(player, "equipped_weapon", None)
    head   = getattr(player, "head_armor",      None)
    body   = getattr(player, "body_armor",      None)
    arms   = getattr(player, "arm_armor",       None)
    legs   = getattr(player, "leg_armor",       None)
    lines.append(f"WPN   {rich_escape(weapon.name if weapon else 'None')}")
    lines.append(f"HEAD  {rich_escape(head.name   if head   else 'None')}")
    lines.append(f"BODY  {rich_escape(body.name   if body   else 'None')}")
    lines.append(f"ARMS  {rich_escape(arms.name   if arms   else 'None')}")
    lines.append(f"LEGS  {rich_escape(legs.name   if legs   else 'None')}")
    lines.append("")

    up_abil = int(getattr(player, "unused_ability_slots", 0) or 0)
    up_stat = int(getattr(player, "unused_stat_points",   0) or 0)
    up_pow  = int(getattr(player, "unused_power_points",  0) or 0)
    s_str  = f"S:{up_abil}"  if up_abil else "[dim]S:0[/dim]"
    sp_str = f"SP:{up_stat}" if up_stat else "[dim]SP:0[/dim]"
    pp_str = f"PP:{up_pow}"  if up_pow  else "[dim]PP:0[/dim]"
    lines.append(f"[yellow]{s_str}  {sp_str}  {pp_str}[/yellow]")

    if show_abilities:
        abilities = getattr(player, "abilities", []) or []
        lines.append("")
        lines.append("[dim]── Abilities ──[/dim]")
        if abilities:
            for a in abilities[:10]:
                lines.append(f"  {rich_escape(str(getattr(a, 'name', a)))}")
        else:
            lines.append("  [dim]None[/dim]")

    return "\n".join(lines)


class CharacterCard(Static):
    """Single character info panel.  The CSS class 'selected' highlights it."""

    DEFAULT_CSS = """
    CharacterCard {
        width: 1fr;
        height: 100%;
        border: solid $primary;
        padding: 1 2;
        overflow-y: auto;
    }

    CharacterCard.selected {
        border: double $accent;
        background: $surface-lighten-1;
    }
    """


class InventoryScreen(BaseScreen):
    """
    Character management screen.

    ← / → change the selected character whether or not an overlay is open.
    B toggles the abilities panel (only when no overlay is open).
    Overlay widgets add the CSS class "inv-overlay" so _close_overlay() can
    remove any of them without a type import.
    """

    LAYERS = ("default", "overlay")
    show_header = False

    BINDINGS = [
        Binding("left",  "move_left",        "Prev",      show=True),
        Binding("a",     "move_left",         "Prev",      show=False),
        Binding("right", "move_right",        "Next",      show=True),
        Binding("d",     "move_right",        "Next",      show=False),
        Binding("b",     "toggle_abilities",  "Abilities", show=True),
        Binding("m",     "open_monster_log",  "Monster Log", show=True),
        Binding("n",     "open_npc_log",      "NPC Log",   show=True),
    ]

    _selected: int
    _offset: int
    _abilities_on: frozenset

    DEFAULT_CSS = """
    InventoryScreen { layout: vertical; }

    #info-bar {
        height: 1;
        background: $boost;
        color: $text;
        padding: 0 1;
        text-style: bold;
    }

    #action-bar {
        height: 3;
        background: $panel;
        border-bottom: solid $accent;
        padding: 0 1;
        layout: horizontal;
    }

    #action-bar Button {
        height: 1;
        min-width: 12;
        margin-right: 1;
        border: none;
    }

    #characters-row {
        height: 1fr;
        padding: 1;
    }

    #pager-bar {
        height: 1;
        background: $surface-darken-1;
        color: $text 60%;
        padding: 0 1;
        text-align: center;
    }

    Footer { height: 1; }
    """

    # ── compose ──────────────────────────────────────────────────────────────

    def compose_content(self) -> ComposeResult:
        pg      = get_active_game()
        chapter = getattr(pg, "current_chapter", "?") if pg else "?"
        money   = getattr(pg, "money", 0)             if pg else 0

        yield Static(f"Chapter: {chapter}  |  Money: {money}", id="info-bar")

        with Horizontal(id="action-bar"):
            yield Button("Items (i)",       id="btn-items",       variant="default")
            yield Button("Equip (e)",       id="btn-equip",       variant="default")
            yield Button("Party (p)",       id="btn-party",       variant="default")
            yield Button("Learn (l)",       id="btn-learn",       variant="default")
            yield Button("Upgrade (u)",     id="btn-upgrade",     variant="default")
            yield Button("Monster Log (m)", id="btn-monster-log", variant="default")
            yield Button(
                "NPC Log (n)", id="btn-npc-log", variant="default", disabled=True
            )
            yield Button("Save (s)",        id="btn-save",        variant="default")

        with Horizontal(id="characters-row"):
            for slot in range(_MAX_DISPLAY):
                yield CharacterCard("", id=f"char-card-{slot}")

        yield Static("", id="pager-bar")

    # ── lifecycle ─────────────────────────────────────────────────────────────

    def on_mount(self) -> None:
        self._selected     = 0
        self._offset       = 0
        self._abilities_on = frozenset()
        self.call_after_refresh(self._refresh_cards)
        self.call_after_refresh(self._refresh_npc_log_button)

    def on_resize(self, event: events.Resize) -> None:
        self._refresh_cards()

    def on_screen_resume(self) -> None:
        self._refresh_cards()
        self._refresh_npc_log_button()

    # ── overlay management ────────────────────────────────────────────────────

    def _overlay_active(self) -> bool:
        return bool(self.query(".inv-overlay"))

    def _close_overlay(self, _message: str | None = None) -> None:
        for w in self.query(".inv-overlay"):
            w.remove()
        self._refresh_cards()

    def _open_items_overlay(self) -> None:
        pg = get_active_game()
        if pg is None:
            self.notify("No active game.", title="Items")
            return
        from tui.screens.items_overlay import ItemsOverlay
        self.mount(ItemsOverlay(pg, self._close_overlay))

    def _open_equip_overlay(self) -> None:
        pg = get_active_game()
        if pg is None:
            self.notify("No active game.", title="Equip")
            return
        from tui.screens.equip_overlay import EquipOverlay
        self.mount(EquipOverlay(pg, self._close_overlay))

    def _open_monster_log_overlay(self) -> None:
        pg = get_active_game()
        if pg is None:
            self.notify("No active game.", title="Monster Log")
            return
        if self._overlay_active():
            self._close_overlay()
            return
        from tui.screens.monster_log_overlay import MonsterLogOverlay
        self.mount(MonsterLogOverlay(pg, self._close_overlay))

    def _open_npc_log_overlay(self) -> None:
        pg = get_active_game()
        if pg is None:
            self.notify("No active game.", title="NPC Log")
            return
        if getattr(pg, "npc_log_locked", True):
            self.notify("The NPC log has not been unlocked yet.", title="NPC Log")
            return
        if self._overlay_active():
            self._close_overlay()
            return
        from tui.screens.npc_log_overlay import NPCLogOverlay
        self.mount(NPCLogOverlay(pg, self._close_overlay))

    # ── escape: close overlay first, then go back ─────────────────────────────

    def action_go_back(self) -> None:
        if self._overlay_active():
            self._close_overlay()
        else:
            self.app.go_back()

    # ── navigation (works with overlays open) ─────────────────────────────────

    def action_move_left(self) -> None:
        pg = get_active_game()
        if pg is None:
            return
        total = len(list(getattr(pg, "characters", [])))
        if total == 0 or self._selected <= 0:
            return
        self._selected -= 1
        if self._selected < self._offset:
            self._offset = self._selected
        self._refresh_cards()
        self._notify_overlays_player_changed()

    def action_move_right(self) -> None:
        pg = get_active_game()
        if pg is None:
            return
        total = len(list(getattr(pg, "characters", [])))
        if total == 0 or self._selected >= total - 1:
            return
        self._selected += 1
        if self._selected >= self._offset + _MAX_DISPLAY:
            self._offset = self._selected - _MAX_DISPLAY + 1
        self._refresh_cards()
        self._notify_overlays_player_changed()

    def action_toggle_abilities(self) -> None:
        if self._overlay_active():
            return
        shown = set(self._abilities_on)
        if self._selected in shown:
            shown.discard(self._selected)
        else:
            shown.add(self._selected)
        self._abilities_on = frozenset(shown)
        self._refresh_cards()

    def action_open_monster_log(self) -> None:
        self._open_monster_log_overlay()

    def action_open_npc_log(self) -> None:
        self._open_npc_log_overlay()

    def _notify_overlays_player_changed(self) -> None:
        """Tell any open overlay that the active character has changed."""
        for w in self.query(".inv-overlay"):
            if hasattr(w, "on_player_changed"):
                w.on_player_changed()

    # ── button handlers ───────────────────────────────────────────────────────

    @on(Button.Pressed, "#btn-items")
    def _on_items(self) -> None:
        if self._overlay_active():
            self._close_overlay()
        else:
            self._open_items_overlay()

    @on(Button.Pressed, "#btn-equip")
    def _on_equip(self) -> None:
        if self._overlay_active():
            self._close_overlay()
        else:
            self._open_equip_overlay()

    @on(Button.Pressed, "#btn-party")
    def _on_party(self) -> None:
        self.notify("Party overlay — coming soon.", title="Party")

    @on(Button.Pressed, "#btn-learn")
    def _on_learn(self) -> None:
        pg = get_active_game()
        if pg is not None:
            players = list(getattr(pg, "characters", []))
            if 0 <= self._selected < len(players):
                slots = int(
                    getattr(players[self._selected], "unused_ability_slots", 0) or 0
                )
                if slots <= 0:
                    self.notify(
                        "No ability slots available for the selected character.",
                        title="Learn",
                    )
                    return
        self.notify("Learn abilities overlay — coming soon.", title="Learn")

    @on(Button.Pressed, "#btn-upgrade")
    def _on_upgrade(self) -> None:
        self.notify("Upgrade stats overlay — coming soon.", title="Upgrade")

    @on(Button.Pressed, "#btn-monster-log")
    def _on_monster_log(self) -> None:
        self._open_monster_log_overlay()

    @on(Button.Pressed, "#btn-npc-log")
    def _on_npc_log(self) -> None:
        self._open_npc_log_overlay()

    @on(Button.Pressed, "#btn-save")
    def _on_save(self) -> None:
        self.notify("Save — coming soon.", title="Save")

    # ── rendering ─────────────────────────────────────────────────────────────

    def _refresh_npc_log_button(self) -> None:
        """Enable the NPC Log button only once `player_game.npc_log_locked`
        is False, mirroring the legacy `(n)pc's` action-bar gating."""
        pg     = get_active_game()
        locked = getattr(pg, "npc_log_locked", True) if pg is not None else True
        try:
            self.query_one("#btn-npc-log", Button).disabled = bool(locked)
        except Exception:
            pass

    def _refresh_cards(self) -> None:
        pg      = get_active_game()
        players: list = list(getattr(pg, "characters", [])) if pg is not None else []
        total   = len(players)

        sel = max(0, min(self._selected, total - 1)) if total else 0
        off = max(0, min(self._offset,   total - 1)) if total else 0
        if sel < off:
            off = sel
        if total > 0 and sel >= off + _MAX_DISPLAY:
            off = max(0, sel - _MAX_DISPLAY + 1)
        self._selected = sel
        self._offset   = off

        if pg is not None:
            try:
                chapter = getattr(pg, "current_chapter", "?")
                money   = getattr(pg, "money", 0)
                self.query_one("#info-bar", Static).update(
                    f"Chapter: {chapter}  |  Money: {money}"
                )
            except Exception:
                pass

        self._refresh_npc_log_button()

        try:
            if total:
                shown_end = min(off + _MAX_DISPLAY, total)
                pager = (
                    f"Showing {off + 1}–{shown_end} of {total} characters"
                    f"  |  Selected: {sel + 1}"
                )
            else:
                pager = "No characters loaded"
            self.query_one("#pager-bar", Static).update(pager)
        except Exception:
            pass

        for slot in range(_MAX_DISPLAY):
            player_idx = off + slot
            try:
                card = self.query_one(f"#char-card-{slot}", CharacterCard)
            except Exception:
                continue
            if player_idx < total:
                player    = players[player_idx]
                show_abil = player_idx in self._abilities_on
                card.update(_build_card_text(player, pg, show_abilities=show_abil))
                card.set_class(player_idx == sel, "selected")
            else:
                card.update("[dim]—[/dim]")
                card.remove_class("selected")