# Dialog and Encounter System

## Overview
The TUI dialog system mirrors the console game's message flow where `pg.info_dialogs` queues story messages, NPC interactions, and encounter notifications that must be displayed sequentially in the center of the screen.

## Components

### 1. MessageDialog Widget (`tui/screens/message_dialog.py`)
- Centered popup mounted on the "overlay" layer
- Blocks input (steals focus) until dismissed
- Cycles through message queue automatically
- Any key press advances to next message
- Auto-removes when queue is exhausted

**Usage:**
messages = ["Line 1", "Line 2: Speaker Name", "..."] self._show_dialog(messages, title="Story")

### 2. Encounter Service (`tui/services/encounter_service.py`)
Handles three types of encounters:

#### A. Pending Boss Fights
if pg.pending_fight_mob_id: messages.append("A powerful foe blocks your path!") messages.append("Prepare for battle!")

#### B. Random Encounters
is_encounter = pg.countdown_random_encounter_timer() if is_encounter: messages.append("You sense danger approaching...") messages.append("An enemy appears!")

#### C. Dungeon Encounters
Dungeons handle their own encounters internally (not checked by overworld).

### 3. OverworldScreen Integration

#### Dialog Check Flow
Movement/Action → _check_dialogs_and_refresh() ↓ Check pg.info_dialogs queue ↓ Pop all messages → _show_dialog() ↓ Display MessageDialog (blocks input) ↓ Player advances through messages ↓ Dialog auto-removes → _refresh_all()

#### Encounter Check Flow
Movement → try_move() succeeds ↓ _refresh_all() (immediate visual feedback) ↓ check_and_handle_encounters() ↓ If encounter → _show_dialog(encounter_messages) ↓ After dialog → _trigger_combat() ↓ Combat result → refresh or game over

## Console Game Equivalents

| Console Code | TUI Implementation |
|--------------|-------------------|
| `pg.info_dialogs` queue | Same queue, checked in `_check_dialogs_and_refresh()` |
| `while pg.info_dialogs: display_viewport()` loop | `MessageDialog` with message queue |
| `readkey()` to advance | Any key binding + `action_advance()` |
| `if pg.pending_fight_mob_id:` | `check_and_handle_encounters()` |
| `pg.countdown_random_encounter_timer()` | Called in `encounter_service.py` |
| `simulate_check_random_encounter()` | `trigger_random_encounter()` wrapper |

## Key Differences from Console

### Console
- Blocks entire loop with `while info_dialogs`
- Manual `clear_screen()` + `display_viewport()` for each message
- Explicit `readkey()` call

### TUI
- Non-blocking: dialog is a mounted Widget
- Compositor handles rendering (no flicker)
- Any key handled by Textual bindings
- Auto-refresh after dialog removal

## Message Sources

### Story Events
- Task completion (`task.task_complete_events`)
- Task acquisition (`task.task_acquire_events`)
- Dialog events (`initiate_dialog`, `initiate_character_dialog`)

### NPC Interactions
- `pg.handle_npc_interaction_at_player_location(npc_id)`
- NPC standing text

### System Events
- Dungeon locked messages (`pg.add_dungeon_standing_text()`)
- Aircraft enter/land messages
- Item pickup notifications

### Encounters
- Boss fight warnings
- Random encounter alerts
- Combat results

## Testing the Flow

1. **Story Messages:**
   - Complete a task that has dialog events
   - Messages should appear centered
   - Any key advances to next message

2. **Random Encounters:**
   - Move around unsafe areas
   - Encounter timer should count down
   - When zero: "You sense danger approaching..." → combat

3. **Boss Fights:**
   - Trigger task that sets `pg.pending_fight_mob_id`
   - Move to trigger encounter check
   - "A powerful foe blocks your path!" → combat

4. **Queue Handling:**
   - Multiple messages should display sequentially
   - Footer shows progress: `[2/5] Press any key...`
   - Last message advances + auto-removes dialog

## Future Enhancements

- [ ] Character portraits in dialog
- [ ] Sound effects for encounters
- [ ] Animated dialog entry/exit
- [ ] Combat preview before engaging
- [ ] Encounter avoidance mechanic