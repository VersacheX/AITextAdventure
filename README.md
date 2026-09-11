# Fracture

**Fracture** is a text-based adventure RPG rendered in a flicker-free terminal UI.
Explore an overworld of cities and regions, fight hostiles, delve procedurally
generated dungeons, level a party of up to five characters, and progress through
a branching, event-driven story.

The interface is built on [Textual](https://textual.textualize.io), which
repaints only the terminal cells that change between frames — there is no
full-screen clear/reprint loop, so the display never flickers.

---

## Features

- Overworld exploration with cities, regions, shops, inns, and hyperway fast-travel
- Party system (1–5 characters) with five archetypes: technique, tech, faith, magic, skill
- Stat/ability leveling with archetype-specific requirements
- Procedurally generated dungeons with lootable treasure and interactive NPCs
- Event-driven story timeline (tasks, dialogs, NPC placement, dungeons)
- Local and online play modes with save/load to named slots
- A developer data-management browser for inspecting saves and seed data

---

## Installation

### Prerequisites

- **Python 3.10+**
- A terminal that supports Textual (Windows Terminal, most modern terminals).
  On Windows, avoid the legacy console host where possible.

### Set up

```bash
# 1. Clone the repository
git clone https://github.com/VersacheX/AITextAdventure.git
cd AITextAdventure

# 2. (Recommended) create and activate a virtual environment
python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r AITextAdventureAPI/tui/requirements.txt
```

---

## Usage

The application has two entry points, both under `AITextAdventureAPI/`.

### Play the game

```bash
python AITextAdventureAPI/run_tui.py
```

This boots the normal flow: title ? server select ? auth ? main menu, from
which you can start a new game or load a save.

### Developer data browser

```bash
python AITextAdventureAPI/run_dev_tui.py
```

This boots directly into the data-management screen (save browsing,
inspection, deletion, seed-data validation, and load-game testing) without
requiring a login.

> Both launchers add `AITextAdventureAPI/` and `AITextAdventureAPI/old/` to
> `sys.path` before importing `tui.app`, so the `tui` package and the legacy
> bare-import modules under `old/` (e.g. `game.objects.*`) both resolve.

### How to play

Full in-game controls and mechanics are documented in
[`game_instructions.txt`](game_instructions.txt). Quick reference:

| Context | Keys |
|---|---|
| Overworld | Arrow keys to move · `i` inventory · `n` NPC log · `m` hostiles · `q` quit |
| Inventory | `?/?` select character · `e` equip · `u` upgrade stats · `l` learn abilities · `p` party |
| Dungeon | Arrow keys to move · `u`/`d` change floor on arrows · `space` loot/interact |

Map symbols (overworld): `µ` bar · `@` inn · `Æ` weapons · `?` items · `¥` armor
· `?` hyperway · `Ð` dungeon entrance. See `game_instructions.txt` for the full legend.

> **Do not right-click inside the game window**, and never use `print()` /
> `input()` for debugging inside a running screen — either will corrupt the
> Textual display. Use `self.log(...)` or the Textual console instead:
>
> ```bash
> # Terminal 1 — Textual log console
> textual console
>
> # Terminal 2 — run in dev mode so logs route to the console above
> textual run --dev AITextAdventureAPI/run_tui.py
> ```

---

## Building a standalone executable

Both entry points are frozen with [PyInstaller](https://pyinstaller.org) using
committed `.spec` files in `AITextAdventureAPI/`. Build with the spec (not the
raw script) so the required assets and package metadata come along — the specs
bundle the `tui/styles` and `tui/assets` folders, `readchar`/`tzdata` metadata,
set `pathex=['.', 'old']`, and load the custom Textual hook from `hooks/`.

The custom hook (`AITextAdventureAPI/hooks/hook-textual.py`) is required because
Textual lazy-imports its widgets via `__getattr__`, which PyInstaller's static
analyzer cannot follow; the hook force-collects every `textual` and `rich`
submodule plus Textual's CSS/TCSS data files.

> Note: `*.spec`, `build/`, and `dist/` are gitignored, so the spec files live
> in your working tree but are not tracked in git.

```bash
# Install the build tool
pip install pyinstaller

# From the AITextAdventureAPI/ directory:
cd AITextAdventureAPI

# Build the game
pyinstaller fracture_tui.spec

# Build the developer data browser
pyinstaller fracture_dev_tui.spec

# (Legacy) build the old console prototype
pyinstaller fracture.spec
```

| Spec file | Entry point | Output name |
|---|---|---|
| `fracture_tui.spec` | `run_tui.py` | `fracture_tui` |
| `fracture_dev_tui.spec` | `run_dev_tui.py` | `fracture_dev_tui` |
| `fracture.spec` | `old/console_game.py` | `fracture` (legacy console prototype) |

The resulting executables are written to `AITextAdventureAPI/dist/`.

> If a run of the frozen build reports a missing module, add it to the hook's
> `hiddenimports` (or the spec's `hiddenimports` list) and rebuild.

---

## Contributing

Contributions are welcome. Please keep the following conventions in mind:

- **Never break the no-flicker rule.** Do not add `os.system('cls')` or any
  full-screen clear/reprint cycle to the `tui` package.
- **New screens** must inherit from `BaseScreen` (`tui/screens/base_screen.py`)
  and override `compose_content()` rather than `compose()`.
- **Blocking I/O** (server calls, save adapters, seed-data loads, the legacy
  `old/` engine) must run inside a `@work(thread=True)` worker and marshal
  results back with `self.app.call_from_thread(...)`, never directly from a
  button handler.
- **Follow the existing style** of the surrounding code and match the seed-data
  formatting conventions when editing story/region files.
- Run and verify the app with `python AITextAdventureAPI/run_tui.py` before
  opening a pull request.

The `AITextAdventureAPI/tui/README.md` documents the screen architecture and
navigation API in detail.

### Workflow

1. Fork the repository and create a feature branch.
2. Make your changes with clear, focused commits.
3. Verify the app launches and your change behaves as expected.
4. Open a pull request describing the change and its motivation.

---

## License

No license has been specified for this project yet. Until a license is added,
all rights are reserved by the repository owner. If you intend to use or
distribute this code, please contact the maintainer via the
[project repository](https://github.com/VersacheX/AITextAdventure).