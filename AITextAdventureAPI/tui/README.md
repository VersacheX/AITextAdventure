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

## Running
# Normal game entry point
python AITextAdventureAPI/run_tui.py

# Developer data browser (boots directly into DataMgmtScreen — no login required)
python AITextAdventureAPI/run_dev_tui.py


### Debugging

Because Textual owns the whole terminal, **do not use `print()` or `input()`
for debugging inside a running screen** — it will corrupt the display.
# Terminal 1 — Textual log console
textual console

# Terminal 2 — run with dev mode so logs route to the console above
textual run --dev AITextAdventureAPI/run_tui.py


Or use `self.log(...)` from within any widget/screen.

---

## Architecture

### `FractureApp` (`tui/app.py`) — the screen manager

`FractureApp` subclasses Textual's `App`, which already implements a
stack-based screen manager (`push_screen` / `pop_screen` / `switch_screen`).
`FractureApp` wraps that stack with two explicit methods so screens have one
obvious navigation API:

- `self.app.goto_screen("name")` — push a registered screen by name. If the
  name is not registered, shows a "coming soon" toast instead of crashing.
- `self.app.go_back()` — pop the current screen.

Screens are registered in `FractureApp.SCREENS`:

| Key | Screen |
|---|---|
| `title` | `TitleScreen` |
| `server_select` | `ServerSelectScreen` |
| `auth` | `AuthScreen` |
| `login` | `LoginScreen` |
| `register` | `RegisterScreen` |
| `main_menu` | `MainMenuScreen` |
| `load_game` | `LoadGameScreen` |
| `new_game` | `NewGameScreen` |
| `overworld` | `OverworldScreen` |
| `inventory` | `InventoryScreen` |
| `tasks` | `TasksScreen` |
| `dungeon` | `DungeonScreen` |
| `dev_data_mgmt` | `DataMgmtScreen` |

### `BaseScreen` (`tui/screens/base_screen.py`)

Every screen must inherit from `BaseScreen`, not Textual's `Screen` directly.
It provides shared `Header`/`Footer` chrome via `compose_content()` (override
this instead of `compose()`), and a shared `Escape → go_back` binding.

### Blocking I/O runs in workers

Any screen that calls into `client_api_requests`, save adapters, or the legacy
`old/` game engine in ways that can block must do so inside a
`@work(thread=True)` method and marshal results back with
`self.app.call_from_thread(...)`. Never call blocking operations directly from
a button handler — a slow or unreachable server, or a slow seed-data load,
would freeze the compositor.

### `GameState` (`tui/services/game_state.py`)

A process-wide singleton (`get_active_game()` / `set_active_game()`) that
holds the currently active `PlayerGame` after a save is loaded or a new game
is started. All downstream screens read it from here rather than having a
`PlayerGame` threaded through every `push_screen()` call.

### `Session` (`tui/services/session.py`)

Holds the current username and play mode (local/online) after authentication,
so later screens can display it without re-deriving it from the adapter.

### Import path note

Everything under `old/` uses bare imports and expects `old/` to be a
`sys.path` root. Both `run_tui.py` and `run_dev_tui.py` add
`AITextAdventureAPI/` (for the `tui` package) and `AITextAdventureAPI/old/`
(for `game.objects.*`, `services.*`, etc.) to `sys.path` before importing
`tui.app`.

---

## Screen inventory

### Full screens

| Screen | File | Status | Notes |
|---|---|---|---|
| Title | `tui/screens/title_screen.py` | ✅ Implemented | Opening screen |
| Server Select | `tui/screens/server_select_screen.py` | ✅ Implemented | Local vs. online adapter selection |
| Auth | `tui/screens/auth_screen.py` | ✅ Implemented | Login / Register / Guest |
| Login | `tui/screens/login_screen.py` | ✅ Implemented | |
| Register | `tui/screens/register_screen.py` | ✅ Implemented | |
| Main Menu | `tui/screens/main_menu_screen.py` | ✅ Implemented | New Game / Load Game / Logout / Quit |
| New Game | `tui/screens/new_game_screen.py` | ✅ Implemented | Party/character setup; full character creation later |
| Load Game | `tui/screens/load_game_screen.py` | ✅ Implemented | Scrollable save list |
| Overworld | `tui/screens/overworld_screen.py` | ✅ Implemented | WASD movement, tile renderer, region generation |
| Dungeon | `tui/screens/dungeon_screen.py` | ✅ Implemented | Floor navigation, NPC meet, item pickup |
| Inventory | `tui/screens/inventory_screen.py` | ✅ Implemented | Hub for all inventory overlays |
| Tasks | `tui/screens/tasks_screen.py` | ✅ Implemented | Active + completed task tree |
| Combat | `tui/screens/combat_screen.py` | ✅ Implemented | Turn-based; driven by `tui/services/combat_service.py` |
| Dev Data Browser | `tui/screens/dev/data_mgmt/data_mgmt_screen.py` | ✅ Implemented | Seed data browser with NPC music player |

### Modals and overlay widgets (mounted on `InventoryScreen`)

| Widget | File | Purpose |
|---|---|---|
| `ItemsOverlay` | `tui/screens/items_overlay.py` | Browse/use/discard inventory items; filter by type |
| `EquipOverlay` | `tui/screens/equip_overlay.py` | Browse/equip/discard equipment; sorted by level → TSP → primary stat → crit; full item card with elements and stat diff vs currently equipped |
| `PartyOverlay` | `tui/screens/party_overlay.py` | Party member management |
| `AbilitiesOverlay` | `tui/screens/abilities_overlay.py` | All known abilities; beneficial ones usable; pushes `AbilityTargetScreen` |
| `AbilityTargetScreen` | `tui/screens/ability_target_screen.py` | Target picker for beneficial abilities; AOE "Use on All" when `can_aoe=True` |
| `LearnOverlay` | `tui/screens/learn_overlay.py` | Learn new abilities using `unused_ability_slots` |
| `UpgradeOverlay` | `tui/screens/upgrade_overlay.py` | Distribute stat points and power points |
| `MonsterLogOverlay` | `tui/screens/monster_log_overlay.py` | Enemies encountered log |
| `NPCLogOverlay` | `tui/screens/npc_log_overlay.py` | Met NPCs log; unlocks after story trigger |
| `CityLogOverlay` | `tui/screens/city_log_overlay.py` | Visited cities with descriptions; resolved via `CITY_DATA` registry |
| `DungeonLogOverlay` | `tui/screens/dungeon_log_overlay.py` | All known dungeons; locked ones shown dim with lock text; coordinates and floor count |
| `SaveOverlay` | `tui/screens/save_overlay.py` | In-game save |
| `LoadOverlay` | `tui/screens/load_overlay.py` | In-game load |
| `ShopOverlay` | `tui/screens/shop_overlay.py` | Buy/sell; quantity selector before purchase |
| `ItemActionScreen` | `tui/screens/item_action_screen.py` | Equip / Use / Discard modal with stat diff |
| `ConfirmScreen` | `tui/screens/confirm_screen.py` | Reusable Yes/No modal |

### Overlay interaction conventions

All overlays on `InventoryScreen` follow these rules:

- Add `"inv-overlay"` CSS class in `on_mount` so `InventoryScreen._close_overlay()` can remove any open overlay generically.
- **Click = highlight/select only.** Never execute an action on click.
- **Enter / explicit button = action.** Equip, Use, Discard, etc. require a deliberate key press or button click.
- Expose `on_player_changed(player)` if they need to react to `InventoryScreen`'s `◄/►` character navigation.

---

## Services (`tui/services/`)

| Service | File | Purpose |
|---|---|---|
| `GameState` | `game_state.py` | Active `PlayerGame` singleton |
| `Session` | `session.py` | Logged-in user and play mode |
| `MovementService` | `movement_service.py` | Wraps `old/services/player_movement_service`; resolves active area, validates moves |
| `DungeonRenderer` | `dungeon_renderer.py` | Renders dungeon tile grids for `DungeonScreen` |
| `CombatService` | `combat_service.py` | Turn resolution wrapping legacy combat engine |
| `AdapterBootstrap` | `adapter_bootstrap.py` | **Temporary shim** — configures local SQLite adapter when server select hasn't run yet. Delete once ServerSelectScreen always runs first. |

### Dev data services (`tui/services/dev/dataservices/`)

Seed-data cache and tree builders for `DataMgmtScreen`.

| Module | Purpose |
|---|---|
| `catalog.py` | `preload()`, `get_records()`, `filter_equipment_records()` — central cache |
| `record_builders.py` | Builds `DevRecord` objects from constants; equipment detail includes rarity, level, damage/defense, elements, stat bonuses, TSP (total stat power), durability, value |
| `dialogue_service.py` | Dialogue tree builder and filter |
| `timeline_service.py` | Timeline/task tree builder and filter |
| `npc_service.py` | NPC tree builder; resolves portrait and `song_id` |

---

## Audio (`tui/audio/`)

| Module | Purpose |
|---|---|
| `music_controller.py` | `NPCMusicController` — pygame-backed theme music for NPC selection in `DataMgmtScreen`. Resolves `<song_id>.*` from `tui/assets/music/`. Handles play/pause/skip/autoplay/loop. Music continues across tab switches within `DataMgmtScreen` and resumes after sub-screens (e.g. portrait fullscreen) are dismissed. |

---

## Legacy `old/` integration

All integration with `old/` goes through thin wrappers in `tui/services/`.
**Do not modify files under `old/` directly** unless the change is a pure
backend fix (e.g. a data-shape bug). If a screen needs a new capability from
the legacy engine, build a service wrapper under `tui/services/` that imports
from `old/`.

Key `old/` modules consumed by TUI services:

| `old/` module | Consumed by |
|---|---|
| `game.objects.player_game.PlayerGame` | `GameState`, all screens via `get_active_game()` |
| `game.objects.player.Player` | `InventoryScreen`, overlays, `CombatService` |
| `game.objects.player_ability.PlayerAbility` | `AbilitiesOverlay`, `LearnOverlay` |
| `game.objects.weapon.Weapon` / `armor.Armor` | `EquipOverlay`, `record_builders` |
| `game.constants` / `game.constants_other` | Seed data; `CITY_DATA`, `PLAYER_ABILITY_SEEDS`, `WEAPON_SEEDS`, `ARMOR_SEEDS`, `DUNGEON_SETTINGS`, `BENEFICIAL_PLAYER_ABILITY_EFFECTS` |
| `services.player_movement_service` | `MovementService` |

---

## Files to delete

These files are deprecated stubs no longer used by anything:

- `AITextAdventureAPI/tui/main.py`
- `AITextAdventureAPI/tui/core/__init__.py`
- `AITextAdventureAPI/tui/core/screen_manager.py`
- `AITextAdventureAPI/tui/core/renderer.py`
- `AITextAdventureAPI/tui/core/input_handler.py`