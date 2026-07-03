"""
Screen manager handles transitions between screens and maintains the screen stack.
"""
from typing import Optional, Dict, Any, List
from enum import Enum


class ScreenType(Enum):
    """Available screen types in the application."""
    SERVER_SELECT = "server_select"
    AUTH = "auth"
    MAIN_MENU = "main_menu"
    NEW_GAME = "new_game"
    LOAD_GAME = "load_game"
    OVERWORLD = "overworld"
    COMBAT = "combat"
    INVENTORY = "inventory"
    DUNGEON = "dungeon"


class Screen:
    """Base screen interface that all screens must implement."""

    def __init__(self, manager: 'ScreenManager'):
        self.manager = manager
        self.is_active = False

    def on_enter(self, context: Optional[Dict[str, Any]] = None) -> None:
        """Called when screen becomes active."""
        self.is_active = True

    def on_exit(self) -> None:
        """Called when screen becomes inactive."""
        self.is_active = False

    def render(self) -> None:
        """Render the screen content."""
        raise NotImplementedError("Screen must implement render()")

    def handle_input(self, key: str) -> Optional[str]:
        """
        Handle user input.

        Returns:
            - None: input handled internally
            - "pop": pop this screen from stack
            - "push:<screen_type>": push new screen
            - "replace:<screen_type>": replace current screen
        """
        raise NotImplementedError("Screen must implement handle_input()")


class ScreenManager:
    """
    Manages screen stack and transitions.

    Screens are organized in a stack where the top screen is active.
    Common patterns:
    - push: Add new screen on top (e.g., open inventory)
    - pop: Remove top screen (e.g., close dialog)
    - replace: Replace current screen (e.g., login -> main menu)
    """

    def __init__(self):
        self._stack: List[Screen] = []
        self._screen_classes: Dict[ScreenType, type] = {}
        self._running = False

    def register_screen(self, screen_type: ScreenType, screen_class: type) -> None:
        """Register a screen class for a given type."""
        self._screen_classes[screen_type] = screen_class

    def push(self, screen_type: ScreenType, context: Optional[Dict[str, Any]] = None) -> None:
        """Push a new screen onto the stack."""
        if self._stack:
            self._stack[-1].on_exit()

        screen_class = self._screen_classes.get(screen_type)
        if not screen_class:
            raise ValueError(f"Screen type {screen_type} not registered")

        screen = screen_class(self)
        screen.on_enter(context)
        self._stack.append(screen)

    def pop(self) -> None:
        """Pop the current screen from the stack."""
        if not self._stack:
            return

        screen = self._stack.pop()
        screen.on_exit()

        if self._stack:
            self._stack[-1].on_enter()

    def replace(self, screen_type: ScreenType, context: Optional[Dict[str, Any]] = None) -> None:
        """Replace the current screen."""
        if self._stack:
            self.pop()
        self.push(screen_type, context)

    def current_screen(self) -> Optional[Screen]:
        """Get the current active screen."""
        return self._stack[-1] if self._stack else None

    def run(self, initial_screen: ScreenType) -> None:
        """Start the screen manager loop."""
        self._running = True
        self.push(initial_screen)

        while self._running and self._stack:
            screen = self.current_screen()
            if screen:
                screen.render()
                # Input handling is delegated to individual screens

    def quit(self) -> None:
        """Stop the screen manager loop."""
        self._running = False
        while self._stack:
            self.pop()