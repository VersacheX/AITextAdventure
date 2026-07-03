"""
Screen implementations for the Fracture TUI.

Every screen inherits from `BaseScreen` (see `base_screen.py`) and is
registered by name in `FractureApp.SCREENS` (see `tui/app.py`) so it can be
navigated to via `self.app.goto_screen("<name>")`.

Implemented so far:
    - TitleScreen ("title")

Planned next (in this order):
    - Server Selection
    - Login / Register
    - Main Menu
    - Character Creation / Selection
"""