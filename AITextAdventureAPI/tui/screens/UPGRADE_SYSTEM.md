# Upgrade Stats System

## Overview
The upgrade stats overlay allows players to allocate unused stat points and power points to improve their characters. This mirrors the console game's `select_upgrade_screen.py` functionality.

## Point Types

### Stat Points (`unused_stat_points`)
- Used to increase base stats: STR, DEX, INT, CON
- Gained on level-up (default: 6 points per level)
- Each point spent increases the stat by 1

#### Stat Effects
- **STR (Strength)**: Increases melee damage and weapon damage
- **DEX (Dexterity)**: Increases accuracy and evasion
- **INT (Intelligence)**: Increases magic effectiveness and max AP gain per level
- **CON (Constitution)**: Increases max HP (2 HP per point) and max HP gain per level

### Power Points (`unused_power_points`)
- Used to increase max HP or max AP
- Gained on level-up (default: 15 points per level)
- Each point spent increases max HP or max AP by 1

## Console vs TUI Differences

### Console Implementation
•	Navigate: Arrow keys
•	Change quantity: +/- keys
•	Apply: Enter
•	Cancel: Escape


### TUI Implementation
•	Navigate: +/- buttons per stat
•	Apply: Apply button
•	Reset: Reset button (clears pending changes)
•	Cancel: Close button or Escape key


## Upgrade Flow

### 1. Opening the Overlay
Inventory Screen → (U) or click "Upgrade" button ↓ Check if selected character has points available ↓ Mount UpgradeOverlay centered on screen

### 2. Allocating Points
Click + button next to stat ↓ Pending allocation increases (if points available) ↓ Display shows: Current value + "+X" pending ↓ Available points counter updates

### 3. Applying Changes
Click Apply button ↓ Player.allocate_stats(str, dex, int, con) called Player.apply_power_point_allocation(hp, ap) called ↓ Pending allocations reset to zero ↓ If no points remaining: auto-close overlay Else: refresh display and keep open

## Code Integration

### Player Methods Used

#### `Player.allocate_stats(str_inc, dex_inc, con_inc, int_inc, use_stat_points=True)`
Increases base stats and consumes unused_stat_points
CON increases also add 2 HP per point immediately
player.allocate_stats(str_inc=2, dex_inc=1, con_inc=0, int_inc=0)

#### `Player.apply_power_point_allocation(hp_points, ap_points)`
Increases max_hp and max_ap, consumes unused_power_points
Also increases current_hp and current_ap by the same amount
player.apply_power_point_allocation(hp_points=10, ap_points=5)

### Stat Calculation
Base stat from player
base_str = player.strength
Modified stat (includes equipment bonuses and status effects)
modified_str = player.get_modified_strength()
Equipment bonus = modified - base
str_bonus = modified_str - base_str

## Display Format

### Points Info Bar
Stat Points: 4/10  Power Points: 12/15 ^remaining  ^total

### Stat Rows
STR    12    +2    [-] [+] ^label ^cur  ^pend

## Validation

### Increment Checks
- **Power stats (HP/AP)**: Sum of pending HP+AP allocations must not exceed `unused_power_points`
- **Base stats (STR/DEX/INT/CON)**: Sum of pending stat allocations must not exceed `unused_stat_points`

### Apply Checks
- At least one pending allocation must be > 0
- Consumes points from respective pools
- Auto-closes overlay when both pools are exhausted

## Testing Checklist

- [ ] Overlay opens when character has points available
- [ ] Overlay shows error when character has no points
- [ ] + button increments pending allocation
- [ ] - button decrements pending allocation
- [ ] Cannot increment beyond available points
- [ ] Reset button clears all pending allocations
- [ ] Apply button correctly updates player stats
- [ ] HP allocation increases both max_hp and current_hp
- [ ] AP allocation increases both max_ap and current_ap
- [ ] CON allocation increases max_hp by 2 per point
- [ ] Overlay auto-closes when all points exhausted
- [ ] Overlay updates when switching characters (← →)
- [ ] Escape key closes overlay

## Future Enhancements

- [ ] Keyboard shortcuts for +/- per stat (e.g., H/Shift+H for HP)
- [ ] Visual preview of stat effects (damage, defense, etc.)
- [ ] Undo last application (before closing overlay)
- [ ] Preset allocation profiles (balanced, offensive, defensive)
- [ ] Confirmation dialog before applying large changes