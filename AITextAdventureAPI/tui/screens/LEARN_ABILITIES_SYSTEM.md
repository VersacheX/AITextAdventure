# Learn Abilities System

## Overview
The learn abilities overlay allows players to browse and learn new abilities for their characters. Abilities are filtered by stat requirements and ability type, matching the console game's `select_ability_screen.py` functionality.

## Ability Learning Flow

### 1. Ability Slots
- Gained every N levels (default: every 4 levels via `ability_acquirement_level_amount`)
- Stored in `Player.unused_ability_slots`
- Each learned ability consumes one slot
- Overlay auto-closes when slots reach zero

### 2. Stat Requirements
Abilities have type-specific stat requirements defined in:
`game/region_seeds/player_abilities/ability_requirements.py`

#### Requirement Formula
required_stat = base_requirement + (base_requirement * (level - 1) * 1.5) ** 1.25

#### Requirement Types
- **Magic**: Intelligence (18+ per level)
- **Tech**: Intelligence (13+) + Dexterity (9+)
- **Skill**: Dexterity (18+ per level)
- **Spirit**: Intelligence (13+) + Constitution (9+)
- **Technique**: Strength (13+) + Constitution (9+)

### 3. Ability Types

#### Magic
- High intelligence requirement
- Elemental damage/status effects
- High AP cost

#### Tech
- Intelligence + dexterity
- Gadgets, devices, technical effects
- Moderate AP cost

#### Skill
- High dexterity requirement
- Physical techniques, precision strikes
- Low AP cost

#### Spirit
- Intelligence + constitution
- Healing, buffs, holy damage
- Moderate AP cost

#### Technique
- Strength + constitution
- Martial arts, weapon techniques
- Low-moderate AP cost

## Console vs TUI Differences

### Console Implementation
•	Navigate: Arrow keys
•	Filter: +/- keys (cycles through types)
•	Learn: Enter
•	Cancel: Escape

### TUI Implementation
•	Navigate: Click or arrow keys in list
•	Filter: Click filter buttons (All/Magic/Tech/Skill/Spirit/Technique)
•	Learn: Click Learn button or press Enter
•	Cancel: Click Close button or press Escape

## Ability Display Format

### List Item
Fireball (Lv.3)  Damage 50p 10ap F (AOE) ^name    ^level  ^effect ^power ^ap ^elem ^aoe

### Detail Panel
Fireball (Lv.3 magic) Launches a ball of fire at enemies. Effect: Damage Power: 85 (base 50) AP Cost: 10 Elements: Fire Targets all enemies

## Code Integration

### Key Methods

#### `get_potential_player_abilities_as_player_ability_list(player)`
Returns list of PlayerAbility objects the player can learn
Filters by:
- Stat requirements
- Abilities not already known
- Non-player-only abilities
abilities = get_potential_player_abilities_as_player_ability_list(player)

#### `Player.learn_ability(ability)`
Adds ability to player.abilities list
Consumes one unused_ability_slot
Returns True if successful
player.learn_ability(ability)

### Ability Properties

#### Core Attributes
- `id`: Unique identifier
- `name`: Display name
- `description`: Flavor text
- `ability_type`: Magic/Tech/Skill/Spirit/Technique (enum)
- `level`: Ability level (affects requirements and power)

#### Combat Attributes
- `base_power`: Base damage/healing value
- `ap_cost`: Action points required to use
- `effect`: Damage/Heal/Status/Revive/Cure (enum)
- `elements`: List of Element enums (Fire/Ice/Lightning/etc.)
- `status_keys`: List of status effect IDs to apply
- `can_aoe`: Whether ability targets all enemies

#### Power Calculation
Base formula
power = base_power * (1 + 0.2 * (level - 1)) * (1 + 0.35 * element_count)
With owner stats
stat_modifier = sum(primary_stats) * level final_power = power + stat_modifier

## Filter Behavior

### "All" Filter
Shows every ability the player qualifies for (all types combined).

### Type Filters
Each filter button shows only abilities of that type:
- **Magic**: Only magic abilities
- **Tech**: Only tech abilities
- **Skill**: Only skill abilities
- **Spirit**: Only spirit abilities
- **Technique**: Only technique abilities

### Dynamic Filtering
When filter changes:
1. Re-filter ability list
2. Update button styles (primary = active)
3. Select first ability in filtered list
4. Update detail panel

## Stat Requirement Display

### Meeting Requirements
Abilities appear in the list only if ALL stat requirements are met.

### Example: Tech Ability Level 2
Required: INT 26, DEX 18 Player:   INT 30, DEX 15 Result:   NOT SHOWN (dexterity too low)

### Example: Spirit Ability Level 1
Required: INT 13, CON 9 Player:   INT 15, CON 10 Result:   SHOWN (all requirements met)

## Loading Performance

### Background Thread
Ability loading runs in a worker thread because:
- `get_potential_player_abilities_as_player_ability_list()` checks hundreds of abilities
- Stat calculations for each ability can be slow
- Prevents UI freezing during initial load

### Worker Pattern
@work(thread=True) def _load_abilities_worker(self): abilities = get_potential_player_abilities_as_player_ability_list(self._player) self.app.call_from_thread(self._on_abilities_loaded, abilities)

## Testing Checklist

- [ ] Overlay opens when character has ability slots
- [ ] Overlay shows error when character has no slots
- [ ] All filter buttons work correctly
- [ ] Ability list shows only qualified abilities
- [ ] Stat requirements properly enforced
- [ ] Detail panel shows correct ability info
- [ ] Power calculation includes player stats
- [ ] Learn button adds ability to player
- [ ] unused_ability_slots decrements on learn
- [ ] Overlay auto-closes when slots exhausted
- [ ] Overlay refreshes when switching characters (← →)
- [ ] Learned abilities no longer appear in list
- [ ] Escape key closes overlay

## Future Enhancements

- [ ] Show requirement breakdown in detail panel
- [ ] Visual indicator for "almost qualified" abilities
- [ ] Preview of ability in combat (damage estimate)
- [ ] Ability comparison (vs currently known abilities)
- [ ] Search/filter by name or element
- [ ] Ability unlock notifications on level-up
- [ ] Recommend abilities based on character build