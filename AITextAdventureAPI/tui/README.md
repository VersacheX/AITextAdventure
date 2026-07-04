# Fracture TUI (Text User Interface)

A flicker-free, Textual-based interface for the Fracture game, replacing the
`old/console_game.py` + `old/game_screens/*.py` prototype (raw `print()` /
`readchar` loops with `os.system('cls')` full-screen clears).

## Scope of work

All new development happens inside `AITextAdventureAPI/tui` and its
subfolders — do not modify files under `AITextAdventureAPI/old` directly.
If a screen needs a service to integrate with the legacy `old/` game engine
(save adapters, player/game objects, combat, etc.), build a thin wrapper
under `tui/services/` that imports from `old/` rather than changing `old/`
itself. See `tui/services/server_config.py` for an example of this pattern.

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

### `tui/services/` — integration with the `old/` game engine

Small, process-wide singletons that screens share state through, following
the same pattern as `old/client_api_requests/save_service_adapter.py`
(module-level instance + get/set functions):

- `server_config.py` — configures which `SaveService` backend (Local
  SQLite vs. Online API) is active; owned by `ServerSelectScreen`.
- `session.py` — tracks the current username / play mode / guest state.
- `game_state.py` — holds the active `PlayerGame` for downstream screens
  (Overworld, Combat, Inventory) once New Game / Load Game populates it.

### `tui/screens/inventory_screen.py` — inventory + party management

`InventoryScreen` is the first screen to use the legacy-style character row
plus docked overlays, but rebuilt as Textual widgets instead of a blocking
`readchar` loop. It keeps the selected party member in the main character row
and mounts overlay widgets on the bottom of the screen for tasks like items
and equipment.

Current overlay behavior:

- `ItemsOverlay` filters inventory by item type (`all`, `utility`, `weapon`,
  `armor`, `special`) and docks to the bottom of the screen.
- `EquipOverlay` filters equipment by slot (`all`, `weapon`, `head`, `body`,
  `arms`, `legs`) and shows stat comparisons against the currently equipped
  item.
- In both overlays, `Tab` / `Shift-Tab` change the filter, `←` / `→` change
  the selected party member, and `Enter` or clicking an item opens a modal
  action popup.
- The action popup is used to confirm equip/use/discard choices without
  leaving the inventory screen.

The overlays are intentionally docked to the bottom and sized to preserve the
character row above them. They do not use full-screen clears.

### Screen status

| Screen                                 | Status         | Key             |
|-----------------------------------------|----------------|-----------------|
| Title / opening                        | ✅ Implemented | `title`         |
| Server Selection (Local / Online)      | ✅ Implemented | `server_select` |
| Login / Register / Guest               | ✅ Implemented | `auth`, `login`, `register` |
| Main Menu                              | ✅ Implemented | `main_menu`     |
| Load Game                              | ✅ Implemented | `load_game`     |
| Inventory / Party Management           | ✅ Implemented | `inventory`     |
| Overworld                               | ⏳ Next         | `overworld`     |
| New Game / Character Creation          | ⏳ Planned (later) | `new_game`   |

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

## Cleanup: legacy files to delete

The following files were part of the original non-Textual prototype
(`os.system('cls')` + blocking `readchar` loops) and have been reduced to
short deprecation stubs. They are no longer used by anything and should be
deleted from disk (this tooling can create/overwrite files but cannot
delete them):

- `tui/services/adapter_bootstrap.py` (replaced by `tui/services/server_config.py`)

## Next steps

1. Continue expanding the remaining inventory overlays and polish their
   interactions with the character row.
2. Build **Overworld** (`overworld`) — map/legend/stats/menu, using
   `old/game_screens/overworld_screen.py`'s `display_viewport()` as the
   layout reference.
3. New Game / Character Creation (later).

Each screen will be built and checked individually before moving to the
next, per project convention.
