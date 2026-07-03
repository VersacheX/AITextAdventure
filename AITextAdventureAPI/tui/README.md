# Fracture TUI (Text User Interface)

Modern text-based interface for the Fracture game, built on clean screen management principles.

## Architecture

### Core Components

- **ScreenManager**: Manages screen stack and transitions
- **Screen**: Base class for all screens
- **Renderer**: Rendering utilities (boxes, borders, text formatting)
- **InputHandler**: Consistent keyboard input handling

### Screen Flow
ServerSelect → Auth → MainMenu → NewGame/LoadGame → Overworld ↓                      ↓ Guest                  Combat/Dungeon

### Screens Implemented

1. **ServerSelectScreen**: Choose local or online play mode
2. **AuthScreen**: Login, register, or guest access
3. **MainMenuScreen**: New game, load game, logout
4. **NewGameScreen**: Character creation
5. **LoadGameScreen**: Save selection and loading

### Screens Planned

- **OverworldScreen**: Main game exploration
- **CombatScreen**: Turn-based combat
- **InventoryScreen**: Item management
- **DungeonScreen**: Dungeon exploration

## Usage

### Running the TUI
python -m tui.main


### Project Structure
tui/├── init.py 
	# EntryPoint
	├── main.py                 
	├── README.md 
	├── core/ │   
		├── screen_manager.py   
	  	├── renderer.py         
		└── input_handler.py    
	└── screens/ 
		├── init.py 
		├── server_select_screen.py 
		├── auth_screen.py 
		├── main_menu_screen.py 
		├── new_game_screen.py 
		└── load_game_screen.py


## Design Principles

### Screen Management

Screens use a stack-based approach:
- **Push**: Add screen on top (overlays)
- **Pop**: Remove current screen (close dialog/menu)
- **Replace**: Swap current screen (state transitions)

### Input Handling

Screens return action strings from `handle_input()`:
- `None`: Input handled, stay on screen
- `"pop"`: Close current screen
- `"push:<type>"`: Open new screen
- `"replace:<type>"`: Replace current screen

### Rendering

All rendering uses consistent utilities:
- Box drawing with `make_box()`
- Text wrapping with `wrap_text()`
- Dialog boxes with `make_dialog_box()`
- Centering with `center_box_in_terminal()`

## Integration Points

### Save Adapters

The TUI integrates with the existing save system:
- `LocalSaveService` for offline play
- `APISaveService` for online play
- Configured at server selection

### Game Objects

Uses existing game logic:
- `Player`, `PlayerGame` for state
- `Combat`, `Dungeon` systems
- Item, ability, and equipment management

## Next Steps

1. Implement `OverworldScreen` (viewport rendering, movement)
2. Integrate `CombatScreen` (adapt existing combat simulator)
3. Add `InventoryScreen` (item management UI)
4. Implement `DungeonScreen` (minimap, exploration)
5. Add save/autosave functionality
6. Implement settings/options screen