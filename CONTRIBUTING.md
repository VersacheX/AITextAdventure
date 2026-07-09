# Contributing to AITextAdventure

## General Guidelines

- Keep changes scoped and incremental. Prefer several small, verifiable steps over one large change, especially for UI work where visual/runtime behavior needs to be checked between steps.
- Match the style and structure of surrounding code in the file/module you're editing.

## TUI Development Standards (`AITextAdventureAPI/tui`)

The `tui` package is the actively developed, professional replacement for the older console prototype in `AITextAdventureAPI/old`. The following rules are mandatory for all work in `tui`:

- **Framework**: [Textual](https://textual.textualize.io) is the required framework for all new TUI screens. Do not build new terminal UI using raw `print()` + `readchar` input loops (that pattern is legacy, confined to `AITextAdventureAPI/old`, and must not be extended).
- **No manual screen clearing**: Never call `os.system('cls')`, `os.system('clear')`, or otherwise manually clear and reprint the entire terminal in a loop. Textual's compositor performs diffed rendering (only changed cells repaint) — screens must rely on that instead of any home-grown clear/redraw cycle. This is the primary mechanism for eliminating flicker.
- **Screen management**: All navigation goes through the stack-based screen manager (`FractureApp` in `tui/app.py`), using the inherited `push_screen` / `pop_screen` / `switch_screen` methods and the named `SCREENS` registry. Do not implement ad-hoc, per-screen navigation loops.
- **Base class**: Every screen must inherit from `BaseScreen` (`tui/screens/base_screen.py`) rather than subclassing Textual's `Screen` directly, so shared chrome (header/footer) and the back-navigation binding stay consistent across the app.
- **Input**: Support both keyboard navigation and mouse interaction where appropriate. Textual widgets provide mouse support by default — custom key handling must not block or bypass it.
- **Blocking I/O**: Any screen action that performs blocking I/O must be offloaded with `@work(thread=True)` and results posted back to the UI thread via `app.call_from_thread(...)`.

## Dev Data Management Screen (`tui/screens/dev/data_mgmt`)

- **NPC theme music — tab switching**: NPC theme music intentionally continues playing when the user switches away from the NPC tab to any other tab. Music only changes or stops when a new NPC leaf node is selected, or when `DataMgmtScreen` is unmounted. **Do not add any `music.stop()` or `music.shutdown()` call inside `handle_tab_activated` in `handlers.py`.**The `old/` directory contains a legacy console prototype (`old/console_game.py`, `old/game_screens/*.py`) and remains the source of truth for game logic (`old/game/objects/*.py`, `old/combat_balancing_simulation/*.py`, `old/services/*.py`). It should not be extended with new UI, and should not be modified when porting its logic to `tui/` — only adapted via `tui/services/` wrappers.