# New Game Flow Documentation

## Overview
The TUI new game flow mirrors `old/console_game_gameloop.py`'s `new_game()` function, providing a flicker-free, async implementation using Textual's compositor and worker threads.

## Flow Steps

### 1. User Input (NewGameScreen)
- User enters character name
- Input validation (name cannot be empty)
- "Begin" button triggers world generation

### 2. World Generation (Background Thread)
The `_build_world()` method runs off the UI thread to prevent blocking:
Create player at origin
player = Player(name, 0, 0, 0, False)
Create world container
pg = PlayerGame()
Equip starting gear (hardcoded 'technique' focus)
equip_player_character(player, pg, focus="technique")
Add character to game & active party
pg.add_character(player)
Generate first region at origin
pg.create_region_at((0, 0))

This matches the console game's sequence exactly:
- `old/console_game_gameloop.py:389-398`

### 3. Transition to Overworld
On success:
- `set_active_game(pg)` - stores game in global state
- `goto_screen("overworld")` - pushes OverworldScreen
- Notification: "World created. Welcome to Fracture."

This matches the console flow where `new_game()` calls `run_game_loop()`.

### 4. Error Handling
If world generation fails:
- Error notification shown
- Input re-enabled
- User can try again

## Key Implementation Details

### Why Background Thread?
`PlayerGame.create_region_at()` performs procedural generation which can take several seconds:
- Imports region seed modules dynamically
- Calls `build_region_map()` to generate tiles
- Creates tasks for stories
- Potentially generates thousands of tiles

Running on a background thread (via `@work(thread=True)`) prevents UI blocking.

### State Management
- `tui/services/game_state.py` holds the singleton `_active_game`
- OverworldScreen reads from `get_active_game()` on mount
- No threading of PlayerGame through screen stack needed

### Default Focus
The console game hardcodes `focus='technique'` in the call to `equip_player_character()`. The TUI matches this for now. Full character creation (class/focus selection) is a later roadmap item.

## Console Game Equivalents

| Console Code | TUI Implementation |
|--------------|-------------------|
| `console_game.py:main_menu()` choice 1 | MainMenuScreen "New Game" button |
| `console_game_gameloop.py:new_game()` | `NewGameScreen._build_world()` |
| `run_game_loop(pg, viewport, api)` | `goto_screen("overworld")` |

## Testing the Flow

1. Start TUI: `python -m tui.main`
2. Navigate: Title → Auth → Main Menu → New Game
3. Enter character name
4. Wait for "Please wait - building initial region..."
5. Should transition to OverworldScreen automatically

## Future Enhancements

- [ ] Class/focus selection UI before world generation
- [ ] Progress indicator for region generation
- [ ] Preview of starting location description
- [ ] Difficulty selection