"""
Screen implementations for the Fracture TUI.

Every screen inherits from `BaseScreen` (see `base_screen.py`) and is
registered by name in `FractureApp.SCREENS` (see `tui/app.py`) so it can be
navigated to via `self.app.goto_screen("<name>")`.

Implemented so far:
    - TitleScreen ("title")
    - ServerSelectScreen ("server_select")
    - AuthScreen ("auth")
    - LoginScreen / RegisterScreen ("login" / "register")
    - MainMenuScreen ("main_menu")
    - LoadGameScreen ("load_game")
    - OverworldScreen ("overworld")
    - InventoryScreen ("inventory")

Planned next (in this order):
    - New Game / Character Creation ("new_game")
"""