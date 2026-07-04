Here's the improved `README.md` file, incorporating the new content while maintaining the existing structure and information:

# Fracture TUI (Text User Interface)

A flicker-free, Textual-based interface for the Fracture game, replacing the
`old/console_game.py` + `old/game_screens/*.py` prototype (raw `print()` /
`readchar` loops with `os.system('cls')` full-screen clears).

## Why Textual

Textual renders through a compositor that diffs frames and only repaints the
terminal cells that actually changed. There is **no manual screen-clearing
loop anywhere in this package** — that is the mechanism that eliminates
flicker, and it must stay that way. Never add `os.system('cls')` or an
equivalent full-screen clear/reprint cycle to this package.

## Scope of Work

All new development happens inside `AITextAdventureAPI/tui` and its subfolders — do not modify files under `AITextAdventureAPI/old` directly. If a screen needs a service to integrate with the legacy `old/` game engine (save adapters, player/game objects, combat, etc.), build a thin wrapper under `AITextAdventureAPI/tui/services/` that imports from `old/` rather than changing `old/` itself.

## Architecture

### `FractureApp` (`tui/app.py`) — the screen manager

`FractureApp` subclasses Textual's `App`, which already implements a
stack-based screen manager (`push_screen` / `pop_screen` / `switch_screen`).
`FractureApp` wraps that stack with two small, explicit methods so screens
have one obvious navigation API:

- `self.app.goto_screen("name")` — push a registered screen by name. If the
  screen isn't registered yet, shows a "coming soon" toast instead of
  crashing (useful while building screens incrementally).
- `self.app.go_back()` — pop the current screen, if there's somewhere to go
  back to.

Screens are registered in `FractureApp.SCREENS`, a `dict[str, type[Screen]]`.

### `BaseScreen` (`tui/screens/base_screen.py`)

Every screen must inherit from `BaseScreen`, not Textual's `Screen`
directly. It provides:

- Shared `Header`/`Footer` chrome via `compose_content()` (override this
  instead of `compose()`).
- A shared `escape` ? `go_back` binding.

### Blocking I/O runs in workers

`LoginScreen` (`tui/screens/login_screen.py`) establishes the pattern for
any screen that needs to call into `client_api_requests` (HTTP via
`APISaveService`, or local SQLite via `LocalSaveService`): the adapter call
runs inside a `@work(thread=True)` method, and the result is marshaled back
to the UI thread with `self.app.call_from_thread(...)`. Never call
`adapter.login()` / `adapter.register()` / etc. directly from a button
handler on the UI thread — a slow or unreachable server would freeze the
whole compositor.

### Session (`tui/services/session.py`)

A small process-wide singleton (`get_session()` / `set_session()`, same
pattern as `client_api_requests.save_service_adapter`) that remembers the
current username and play mode (local/online) after login, register, or
guest access, so later screens (Main Menu, etc.) can display it without
re-deriving it from the adapter.

### Temporary shim: `tui/services/adapter_bootstrap.py`

Server Selection (local vs. online) is not implemented yet. Until it is,
`AuthScreen` and `LoginScreen` call `ensure_default_local_adapter()` on
mount, which configures a local SQLite-backed adapter if none has been set.
This mirrors what `old/console_game.py`'s `auth_menu()` did for its "Play
Local" option. **Delete this shim and its call sites once Server Selection
is built and always configures the adapter first.**

### Import path note

Everything under `old/` (e.g. `client_api_requests.*`, `game.objects.*`)
uses bare imports and expects `old/` itself to be a `sys.path` root (the
same way `old/console_game.py` and `old/run_equipment_screen_test.py` run).
`run_tui.py` adds both `AITextAdventureAPI/` (for the `tui` package) and
`AITextAdventureAPI/old/` (for everything `tui` screens import from `old`)
to `sys.path` before importing `tui.app`.

### Screen status

| Screen                                 | Status       | Key          |
|----------------------------------------|--------------|--------------|
| Title / opening                        | ? Implemented | `title`      |
| Login / Register / Guest menu          | ? Implemented | `auth`       |
| Login form                             | ? Implemented | `login`      |
| Register form                          | ? Implemented | `register`   |
| Server Selection                       | ? Next       | `server_select` |
| Main Menu                             | ? Planned     | `main_menu`  |
| Character Creation / Selection         | ? Planned (later) | —            |

## Running

To get started with the Fracture TUI, follow these steps:

1. Install the required dependencies:
   pip install -r tui/requirements.txt

2. Run the application:
   python run_tui.py

### Debugging

Because Textual owns the whole terminal, **do not use `print()` or
`input()` for debugging inside a running screen** — it will corrupt the
display. Instead, run the app in dev mode with a separate log console:

# terminal 1
textual console

# terminal 2
textual run --dev tui/app.py

Or use `self.log(...)` from within a widget/screen, which is routed to the
`textual console` window instead of stdout.

## Cleanup: files to delete

The following files were part of the original non-Textual prototype
(`os.system('cls')` + blocking `readchar` loops) and have been reduced to
short deprecation stubs. They are no longer used by anything and should be
deleted from disk (this tooling can create/overwrite files but cannot
delete them):

- `tui/main.py`
- `tui/core/__init__.py`
- `tui/core/screen_manager.py`
- `tui/core/renderer.py`
- `tui/core/input_handler.py`
- `tui/screens/server_select_screen.py`
- `tui/screens/main_menu_screen.py`
- `tui/screens/new_game_screen.py`
- `tui/screens/load_game_screen.py`

## Next steps

1. Verify `AuthScreen` / `LoginScreen` / `RegisterScreen` for flicker/visual
   correctness, including the local-adapter register ? login round trip.
2. Build **Server Selection** (`server_select`) — local vs. online, wiring
   `LocalSaveService` / `APISaveService` the same way `old/console_game.py`'s
   `auth_menu()` did — and insert it between Title and Auth. Remove the
   temporary `adapter_bootstrap` shim once this is done.
3. Build **Main Menu** (`main_menu`).
4. Character Creation / Selection (later).

Each screen will be built and checked individually before moving to the
next, per project convention.

This revised README maintains the original structure while integrating the new content seamlessly, ensuring clarity and coherence throughout the document.