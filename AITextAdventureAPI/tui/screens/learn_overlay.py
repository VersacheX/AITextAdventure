"""
LearnOverlay: ability learning interface for the selected character.

Mirrors `old/game_screens/select_ability_screen.py`: the player browses
abilities they can learn (filtered by their current stats and ability type),
then selects one to add to their known abilities. Each learned ability
consumes one unused_ability_slot.

The console version uses arrow keys for navigation, +/- for ability type
filtering (all/magic/tech/skill/faith/technique), and Enter to learn. The
TUI mirrors this with a scrollable list, filter buttons, and a Learn button.

Stat requirements are enforced via `get_potential_player_abilities()` from
`old/game/objects/player_ability.py`, which checks
`ABILITY_TYPE_REQUIREMENTS` and filters abilities by the player's current
base stats (strength, dexterity, intelligence, constitution).

The overlay remains open even when the player has no remaining ability slots,
showing a message instead of auto-closing. This allows the player to review
available abilities and switch characters while the overlay is open.
"""
from __future__ import annotations

from typing import Any, Callable, List, Optional

from rich.markup import escape as rich_escape
from textual import on, work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label, ListItem, ListView, Static

from tui.screens.base_screen import BaseScreen


class LearnOverlay(Static):
    """Floating ability learning panel - positioned at bottom of screen."""

    BINDINGS = [
        Binding("enter", "learn_selected", "Learn", show=False),
        Binding("escape", "close_overlay", "Cancel", show=False),
    ]

    DEFAULT_CSS = """
    LearnOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 22;
        background: $surface;
        border-top: thick $accent;
    }

    #learn-title {
        width: 100%;
        text-align: center;
        text-style: bold;
        background: $boost;
        color: $text;
        padding: 0 1;
        height: 1;
    }

    #learn-content {
        width: 100%;
        height: 1fr;
        layout: horizontal;
        padding: 1 2;
    }

    #left-panel {
        width: 2fr;
        height: 100%;
    }

    #right-panel {
        width: 1fr;
        height: 100%;
        margin-left: 2;
    }

    .learn-info {
        width: 100%;
        text-align: left;
        color: $text 80%;
        margin-bottom: 1;
    }

    #filter-bar {
        width: 100%;
        height: auto;
        layout: horizontal;
        margin-bottom: 1;
    }

    #filter-bar Button {
        min-width: 12;
        height: 3;
        margin-right: 1;
    }

    #ability-list {
        width: 100%;
        height: 1fr;
        border: solid $primary;
    }

    #ability-list > ListItem {
        height: auto;
        padding: 0 1;
    }

    #ability-list > ListItem.--highlight {
        background: $accent 30%;
    }

    #ability-detail {
        width: 100%;
        height: 1fr;
        border: solid $primary;
        padding: 1;
        margin-bottom: 1;
        overflow-y: auto;
    }

    #learn-actions {
        width: 100%;
        layout: horizontal;
        height: auto;
    }

    #learn-actions Button {
        width: 1fr;
        margin-right: 1;
    }

    #learn-actions Button:last-child {
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

        # Ability type filters
        self._filters = ["all", "magic", "tech", "skill", "spirit", "technique"]
        self._current_filter = "all"

        # Cached ability list
        self._abilities: List[Any] = []
        self._selected_ability: Optional[Any] = None

    def compose(self) -> ComposeResult:
        """Build the learn abilities panel UI."""
        with Vertical():
            yield Static("=== Learn Abilities ===", id="learn-title")

            with Horizontal(id="learn-content"):
                # Left panel: filters and list
                with Vertical(id="left-panel"):
                    yield Static("", classes="learn-info", id="slots-info")

                    # Filter buttons
                    with Horizontal(id="filter-bar"):
                        yield Button("All", id="filter-all", variant="primary")
                        yield Button("Magic", id="filter-magic", variant="default")
                        yield Button("Tech", id="filter-tech", variant="default")
                        yield Button("Skill", id="filter-skill", variant="default")
                        yield Button("Faith", id="filter-faith", variant="default")
                        yield Button("Technique", id="filter-technique", variant="default")

                    # Ability list
                    yield ListView(id="ability-list")

                # Right panel: detail and actions
                with Vertical(id="right-panel"):
                    # Detail panel
                    yield Static("", id="ability-detail")

                    # Action buttons
                    with Horizontal(id="learn-actions"):
                        yield Button("Learn", id="btn-learn", variant="primary", disabled=True)
                        yield Button("Cancel", id="btn-cancel", variant="default")

    def on_mount(self) -> None:
        """Initialize display with available abilities."""
        self.add_class("inv-overlay")
        self._load_abilities_worker()
        # Focus the list view for keyboard navigation
        try:
            self.query_one("#ability-list", ListView).focus()
        except Exception:
            pass

    def on_player_changed(self, new_player: Any) -> None:
        """Called by InventoryScreen when the active character changes.
        
        Updates the internal player reference and reloads abilities.
        """
        self._player = new_player
        self._selected_ability = None
        self._load_abilities_worker()

    @work(thread=True)
    def _load_abilities_worker(self) -> None:
        """Load available abilities in a background thread (can be slow)."""
        from game.objects.player_ability import get_potential_player_abilities_as_player_ability_list

        try:
            abilities = get_potential_player_abilities_as_player_ability_list(self._player)
            self.app.call_from_thread(self._on_abilities_loaded, abilities)
        except Exception as e:
            self.app.call_from_thread(
                self._on_abilities_loaded, [], error=str(e)
            )

    def _on_abilities_loaded(
        self, abilities: List[Any], *, error: str | None = None
    ) -> None:
        """Called on the main thread after abilities are loaded."""
        if error:
            self.notify(f"Could not load abilities: {error}", severity="error")
            self._abilities = []
        else:
            self._abilities = abilities

        self._refresh_display()

    def _refresh_display(self) -> None:
        """Update all UI elements with current filter and selection."""
        # Get player name for display
        player_name = rich_escape(str(getattr(self._player, "name", "Character")))
        
        # Update slots info
        slots = int(getattr(self._player, "unused_ability_slots", 0) or 0)
        try:
            if slots > 0:
                self.query_one("#slots-info", Static).update(
                    f"[bold]{player_name}[/bold]  |  Available Ability Slots: [yellow]{slots}[/yellow]  |  [dim]Click to select, press Enter or click Learn button[/dim]"
                )
            else:
                self.query_one("#slots-info", Static).update(
                    f"[bold]{player_name}[/bold]  |  [dim]No ability slots available[/dim]"
                )
        except Exception:
            pass

        # Filter abilities by current type
        filtered = self._filter_abilities(self._abilities, self._current_filter)

        # Update list
        try:
            list_view = self.query_one("#ability-list", ListView)
            list_view.clear()
            for ability in filtered:
                list_view.append(self._build_ability_list_item(ability))
        except Exception:
            pass

        # Update filter button styles
        for filter_name in self._filters:
            try:
                btn = self.query_one(f"#filter-{filter_name}", Button)
                if filter_name == self._current_filter:
                    btn.variant = "primary"
                else:
                    btn.variant = "default"
            except Exception:
                pass

        # Update learn button and detail based on slots and available abilities
        has_slots = slots > 0
        has_abilities = len(filtered) > 0

        try:
            learn_btn = self.query_one("#btn-learn", Button)
            learn_btn.disabled = not (has_slots and has_abilities)
        except Exception:
            pass

        if not has_abilities:
            try:
                if not has_slots:
                    self.query_one("#ability-detail", Static).update(
                        "[dim]No ability slots available.\n\nLevel up to gain more ability slots![/dim]"
                    )
                else:
                    self.query_one("#ability-detail", Static).update(
                        "[dim]No abilities available with current filter.\n\nTry a different filter or increase your stats to unlock more abilities.[/dim]"
                    )
            except Exception:
                pass
            self._selected_ability = None
        else:
            # Select first ability by default if none selected or current selection not in filtered list
            if self._selected_ability not in filtered:
                self._selected_ability = filtered[0] if filtered else None
            self._update_detail()

    def _filter_abilities(
        self, abilities: List[Any], filter_type: str
    ) -> List[Any]:
        """Filter abilities by type."""
        if filter_type == "all":
            return abilities

        filtered: List[Any] = []
        for ability in abilities:
            ability_type = getattr(ability, "ability_type", None)
            if ability_type is not None:
                type_value = (
                    getattr(ability_type, "value", None)
                    if hasattr(ability_type, "value")
                    else str(ability_type)
                )
                if str(type_value).lower() == filter_type.lower():
                    filtered.append(ability)
        return filtered

    def _build_ability_list_item(self, ability: Any) -> ListItem:
        """Build a ListItem for one ability."""
        name = rich_escape(str(getattr(ability, "name", "Ability")))
        level = getattr(ability, "level", 1)
        ap_cost = getattr(ability, "ap_cost", 0)

        # Build suffix with effect, power, elements, etc.
        parts: List[str] = []

        # Effect
        effect = getattr(ability, "effect", None)
        if effect:
            effect_val = (
                getattr(effect, "value", None) if hasattr(effect, "value") else str(effect)
            )
            parts.append(str(effect_val).capitalize() if effect_val else "")

        # Base power
        base_power = getattr(ability, "base_power", None)
        if base_power is not None and base_power > 0:
            parts.append(f"{int(base_power)}p")

        # AP cost
        if ap_cost:
            parts.append(f"{int(ap_cost)}ap")

        # Elements (show as symbols)
        elements = getattr(ability, "elements", []) or []
        if elements:
            elem_chars = []
            for elem in elements:
                elem_val = (
                    getattr(elem, "value", None) if hasattr(elem, "value") else str(elem)
                )
                elem_chars.append(str(elem_val)[:1].upper())  # First char
            if elem_chars:
                parts.append("".join(elem_chars))

        # AOE
        if getattr(ability, "can_aoe", False):
            parts.append("(AOE)")

        suffix = " ".join(parts)
        label_text = f"[bold]{name}[/bold] (Lv.{level})  {suffix}"

        item = ListItem(Label(label_text))
        item.ability = ability  # Store reference
        return item

    def _update_detail(self) -> None:
        """Update the detail panel with selected ability info."""
        if self._selected_ability is None:
            try:
                self.query_one("#ability-detail", Static).update(
                    "[dim]No ability selected.[/dim]"
                )
            except Exception:
                pass
            return

        ability = self._selected_ability
        lines: List[str] = []

        # Name and basic info
        name = rich_escape(str(getattr(ability, "name", "Ability")))
        level = getattr(ability, "level", 1)
        ability_type = getattr(ability, "ability_type", None)
        type_str = (
            getattr(ability_type, "value", "?")
            if ability_type
            else "?"
        )
        lines.append(f"[bold]{name}[/bold] (Lv.{level} {type_str})")

        # Description
        desc = rich_escape(str(getattr(ability, "description", "")))
        if desc:
            lines.append(desc)
            lines.append("")

        # Effect details
        effect = getattr(ability, "effect", None)
        base_power = getattr(ability, "base_power", 0)
        ap_cost = getattr(ability, "ap_cost", 0)

        if effect:
            effect_val = (
                getattr(effect, "value", None) if hasattr(effect, "value") else str(effect)
            )
            lines.append(f"Effect: [yellow]{str(effect_val).capitalize()}[/yellow]")

        if base_power:
            # Show computed power with player's stats
            try:
                computed = ability.compute_power_with_owner(self._player)
                lines.append(f"Power: [green]{computed}[/green] (base {base_power})")
            except Exception:
                lines.append(f"Power: {base_power}")

        lines.append(f"AP Cost: [cyan]{ap_cost}[/cyan]")

        # Elements
        elements = getattr(ability, "elements", []) or []
        if elements:
            elem_names = []
            for elem in elements:
                elem_val = (
                    getattr(elem, "value", None) if hasattr(elem, "value") else str(elem)
                )
                elem_names.append(str(elem_val).capitalize())
            lines.append(f"Elements: {', '.join(elem_names)}")

        # Status effects
        status_keys = getattr(ability, "status_keys", None)
        if status_keys:
            lines.append(f"Status: {', '.join(str(k) for k in status_keys)}")

        # AOE
        if getattr(ability, "can_aoe", False):
            lines.append("[yellow]Targets all enemies[/yellow]")

        try:
            self.query_one("#ability-detail", Static).update("\n".join(lines))
        except Exception:
            pass

    @on(ListView.Highlighted)
    def _on_list_highlighted(self, event: ListView.Highlighted) -> None:
        """Update detail when a different ability is highlighted (single click)."""
        if event.item and hasattr(event.item, "ability"):
            self._selected_ability = event.item.ability
            self._update_detail()

    @on(Button.Pressed)
    def _on_button(self, event: Button.Pressed) -> None:
        """Handle all button presses."""
        button_id = event.button.id or ""

        if button_id.startswith("filter-"):
            filter_type = button_id.replace("filter-", "")
            self._current_filter = filter_type
            self._refresh_display()
            # Refocus list after filter change
            try:
                self.query_one("#ability-list", ListView).focus()
            except Exception:
                pass
        elif button_id == "btn-learn":
            self._learn_selected()
        elif button_id == "btn-cancel":
            self.action_close_overlay()

    def action_learn_selected(self) -> None:
        """Learn the currently selected ability (Enter key binding)."""
        self._learn_selected()

    def action_close_overlay(self) -> None:
        """Close the overlay (Escape key binding)."""
        self._on_close(None)
        self.remove()

    def _learn_selected(self) -> None:
        """Learn the currently selected ability."""
        if self._selected_ability is None:
            self.notify("No ability selected.", severity="warning")
            return

        # Check if player has slots
        slots = int(getattr(self._player, "unused_ability_slots", 0) or 0)
        if slots <= 0:
            self.notify("No ability slots available. Level up to gain more!", severity="warning")
            return

        # Learn the ability
        try:
            self._player.learn_ability(self._selected_ability)
            ability_name = str(getattr(self._selected_ability, "name", "Ability"))

            # Check remaining slots
            remaining = int(getattr(self._player, "unused_ability_slots", 0) or 0)

            # Show notification
            if remaining > 0:
                self.notify(f"Learned {ability_name}! ({remaining} slots left)", title="Success")
            else:
                self.notify(f"Learned {ability_name}! (No slots remaining)", title="Success")

            # Signal the inventory screen to refresh character cards
            self._on_close(f"learned_{ability_name}")

            # Refresh display (don't close even if no slots remaining)
            self._load_abilities_worker()

        except Exception as e:
            self.notify(f"Failed to learn ability: {e}", severity="error")