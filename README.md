Here's the improved `README.md` file incorporating the new content while maintaining the existing structure and coherence:

# Project Title

## Overview

This project is designed to create and manage dynamic dungeons for a game environment. It allows for the addition of non-player characters (NPCs) and treasures within specified locations of the dungeon.

## Features

- Dynamic dungeon generation
- Placement of NPCs and treasures
- Customizable dungeon parameters

## Events

### `dungeon_add_npc`

This event allows you to add an NPC to a specified location within the dungeon.

#### Parameters

- `dungeon_id` (string): The identifier for the dungeon.
- `npc_id` (string): The identifier for the NPC to be added.
- `location` (string): The type of tile where the NPC will be placed (e.g., corridor, treasure room).
- `depth` (integer, optional): Determines how deep into the dungeon the NPC is placed. See the `depth` parameter section for more details.

### `dungeon_add_treasure`

This event allows you to add a treasure item to a specified location within the dungeon.

#### Parameters

- `dungeon_id` (string): The identifier for the dungeon.
- `item_id` (string): The identifier for the treasure item to be added.
- `location` (string): The type of tile where the treasure will be placed (e.g., corridor, treasure room).
- `depth` (integer, optional): Determines how deep into the dungeon the treasure is placed. See the `depth` parameter section for more details.

### `dungeon_add_npc` and `dungeon_add_treasure` — `depth` Parameter

Both events accept an optional `depth` parameter (integer, 0–100).

- **Omitted / `None`** — entity is placed anywhere in the specified `location` tile type (original behaviour).
- **`0`** — places the entity as close to the dungeon entrance as possible.
- **`100`** — places the entity as deep as possible (near the `final_chamber` end).
- **Any value in between** — the placement is normalized to the closest matching tile at that percentile of Manhattan distance from the entrance centroid. A ±10% tolerance band is used; if no tiles fall within the band, the single nearest candidate is used so placement never hard-fails.

#### Examples

# NPC placed ~80% deep into the dungeon
{ 'event_type': 'dungeon_add_npc', 'params': { 'dungeon_id': 'seth_hideout', 'npc_id': 'seth', 'location': 'corridor', 'depth': 80 }}

# Treasure placed near the entrance (~10% depth)
{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'seth_hideout', 'item_id': 'silver_key', 'location': 'corridor', 'depth': 10 }}

# No depth = full scope (original behaviour)
{ 'event_type': 'dungeon_add_treasure', 'params': { 'dungeon_id': 'seth_hideout', 'item_id': 'ornate_bracers', 'location': 'treasure_room' }}

## Installation

Instructions on how to install and set up the project.

## Usage

Instructions on how to use the project, including examples and best practices.

## Contributing

Guidelines for contributing to the project.

## License

Information about the project's license.

This revised README.md maintains the original structure while seamlessly integrating the new content about the `depth` parameter for the `dungeon_add_npc` and `dungeon_add_treasure` events.