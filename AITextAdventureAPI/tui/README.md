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
- A shared `escape` → `go_back` binding.

### Screen status

| Screen                                 | Status       | Key          |
|----------------------------------------|--------------|--------------|
| Title / opening                        | ✅ Implemented | `title`      |
| Server Selection                       | ⏳ Next       | `server_select` |
| Login / Register                       | ⏳ Planned     | `auth`       |
| Main Menu                             | ⏳ Planned     | `main_menu`  |
| Character Creation / Selection         | ⏳ Planned (later) | —            |

## Running
pip install -r tui/requirements.txt python run_tui.py


### Debugging

Because Textual owns the whole terminal, **do not use `print()` or
`input()` for debugging inside a running screen** — it will corrupt the
display. Instead, run the app in dev mode with a separate log console:

terminal 1
textual console
terminal 2
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
- `tui/screens/auth_screen.py`
- `tui/screens/main_menu_screen.py`
- `tui/screens/new_game_screen.py`
- `tui/screens/load_game_screen.py`

## Next steps

1. Verify `TitleScreen` for flicker/visual correctness.
2. Build **Server Selection** (`server_select`) — local vs. online, wiring
   `LocalSaveService` / `APISaveService` the same way `old/console_game.py`'s
   `auth_menu()` did.
3. Build **Login / Register** (`auth`).
4. Build **Main Menu** (`main_menu`).
5. Character Creation / Selection (later).

Each screen will be built and checked individually before moving to the
next, per project convention.
