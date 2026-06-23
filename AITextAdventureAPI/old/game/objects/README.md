# Game Objects Reference

## Overview
Core game object definitions used throughout AI Text Adventure.

## Object Types

### Task System (`task.py`)
- Task Types (meet, deliver, fetch, defeat, goto)
- TaskEventType enum
- Task lifecycle and completion checking

### Player Game (`player_game.py`)
- Player state management
- Inventory system
- Quest tracking
- Regional progress

### NPCs (`npc.py`)
- NPC creation and behavior
- Dialog system integration
- Standing text mechanics
- Met/unmet state tracking

### Items (`item.py`)
- Item types and categories
- Equipment system
- Consumables
- Quest items

### Dungeons (`dungeon.py`)
- Dungeon structure
- Tile types
- Entity placement
- Treasure/NPC spawning

### Combat (`combat.py`)
- Combat mechanics
- Boss battles
- Mob definitions

## Usage Patterns

### Creating a New Task Type
[Example code]

### Instantiating an NPC
[Example code]

### Adding Items to Inventory
[Example code]

## Event System Integration
How objects interact with `task_completion_service.py`

## Common Pitfalls
- Task ID mismatches
- NPC location references
- Item quantity handling