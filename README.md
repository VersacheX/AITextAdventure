# Fracture

**Fracture** is a text-based adventure RPG rendered in a flicker-free terminal UI.
Explore an overworld of cities and regions, fight hostiles, delve procedurally
generated dungeons, level a party of up to five characters across 32 attainables, and progress through
a branching, event-driven story that spans continents and reality itself.

### The Story

You and your friends were knocking back a few drinks when blinding light tore
through the bar and reality shifted around you. When it settled you were
*here* — a looted, chaotic city in a world that isn't yours, with three of your
companions missing. This is the **Fracture**: a wound in reality.

From a single ruined city the journey widens outward — bounty hunts and black
market deals give way to a resistance, an airship,
and a continent-spanning search for the scattered halves of... Along
the way you gather dozens of party members, battling through seven regions with parties of up to five at a time from — desert,
forest, grassland, mountains, shallows, snow, and swamp — each with their own
grief, purpose, and reason to fight. Standing against you are the **Voidwalkers**:
manifestations of attention, sensation, grief, self-loathing, order, prophecy,
and inevitability — Glamour, Scalpel, Rapture, Lament, Garbage, Stigma, Edict,
Crux, Oracle, Cataclysm, and finally Dominion and the Void itself. Fracture is a
story about identity, memory, and meaning — and whether a world can be held
together by choice when the systems that once sustained it have decided it
should end.

### Under the Hood

The interface is built on [Textual](https://textual.textualize.io), a modern
compositor that repaints only the terminal cells that change between frames —
there is no full-screen clear/reprint loop, so the display never flickers and
never tears. On top of that sits a fully data-driven engine: the entire
narrative is expressed as an **event-driven timeline** of tasks, dialogs, NPC
placements, dungeon spawns, and item awards, validated by an integrity checker
so 21 chapters, regional arcs, and dozens of city stories stay consistent.
Dungeons are procedurally generated, the party and combat systems are built
around five archetypes (technique, tech, faith, magic, skill), and the game
supports both local and online play with named save slots — plus a developer
data browser for inspecting saves and seed data.

---

## Features

### World & exploration

- Overworld exploration across multiple regions and cities, each with shops, inns, and townsfolk to talk to
- Fast travel between discovered locations via the hyperway network
- Procedurally generated dungeons with lootable treasure, hidden rooms, and interactive NPCs
- Region-specific side quests and optional companions to recruit as you explore

### Party & progression

- Party system (1–5 characters) with five archetypes: technique, tech, faith, magic, skill
- Stat and ability leveling with archetype-specific requirements
- Spend earned points to raise stats and unlock new abilities as your party grows
- Equipment and inventory management with weapons, armor, and accessories across multiple rarity tiers

### Encounters & activities

- Turn-based party combat against standard, elite, and boss-tier enemies
- Optional puzzle, riddle, and games-of-chance encounters tucked away in the world
- An in-game contact log that keeps track of the NPCs you meet

### Story & structure

- Event-driven story timeline (tasks, dialogs, NPC placement, dungeons)
- Local and online play modes with save/load to named slots (*note* online requires setting up the data FastAPI server)
- A developer data-management browser for inspecting seed data (*note* may be worth investing in having it be able to look at saves)

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
[`game_instructions.txt`](game_instructions.txt). 

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
