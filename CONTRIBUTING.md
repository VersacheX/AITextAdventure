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
- **Blocking I/O**: Any screen action that performs blocking I/O (HTTP requests via `ClientAPI`/`APISaveService`, or local SQLite access via `LocalStorageAdapter`/`LocalSaveService`) must run that call inside a Textual background worker using `@work(thread=True)`, and marshal any resulting UI updates back onto the main thread via `self.app.call_from_thread(...)`. Never call these adapter methods directly from a widget/screen event handler on the UI thread — a slow or unreachable server would otherwise freeze the whole compositor. See `tui/screens/login_screen.py` (`LoginScreen._do_submit`) for the reference pattern.
- **Incremental delivery**: Build and verify one screen (or one cohesive slice) at a time. Each increment should be runnable on its own and checked for flicker/visual issues before moving on to the next screen.