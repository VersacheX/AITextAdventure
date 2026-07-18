"""
accessory.py — Accessory dataclass and instantiation helper.

Accessories are equipped in the Player.accessories array (up to
Player.max_accessory_slots, default 3).  Each accessory can provide:
  - immunities   : list[str]  — status ids that are blocked entirely
  - resistances  : list[str]  — element names that reduce incoming elemental damage
  - weaknesses   : list[str]  — element names that increase incoming elemental damage
  - stat buffs   : strength / dexterity / intelligence / constitution
  - crit_bonus   : float      — added to weapon critical_chance (percentage points)
  - damage_bonus : int        — flat bonus to every outgoing attack
  - special_effect: str       — reserved key for future runtime systems
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Accessory:
    """Runtime accessory object instantiated from a seed dict."""

    id: str = ""
    name: str = "Unnamed Accessory"
    description: str = ""
    min_level: int = 1
    rarity: str = "common"
    value: int = 0
    # Required by PlayerGame.pick_up_item / remove_single_item_unit
    quantity: int = 1

    # Status immunity / elemental interaction
    immunities:  List[str] = field(default_factory=list)
    resistances: List[str] = field(default_factory=list)
    weaknesses:  List[str] = field(default_factory=list)

    # Stat bonuses applied via Player.get_modified_*
    strength:     int = 0
    dexterity:    int = 0
    intelligence: int = 0
    constitution: int = 0

    # Combat bonuses
    crit_bonus:   float = 0.0
    damage_bonus: int   = 0

    # Reserved for future systems (e.g. 'amplify_ability', 'lifesteal')
    special_effect: str = ""


def instantiate_accessory(seed: Dict[str, Any]) -> Accessory:
    """Create an Accessory instance from a constants seed dict."""
    return Accessory(
        id=seed.get('id', ''),
        name=seed.get('name', 'Unknown'),
        description=seed.get('description', ''),
        min_level=int(seed.get('min_level', 1)),
        rarity=seed.get('rarity', 'common'),
        value=int(seed.get('value', 0)),
        quantity=1,
        immunities=list(seed.get('immunities') or []),
        resistances=list(seed.get('resistances') or []),
        weaknesses=list(seed.get('weaknesses') or []),
        strength=int(seed.get('strength', 0)),
        dexterity=int(seed.get('dexterity', 0)),
        intelligence=int(seed.get('intelligence', 0)),
        constitution=int(seed.get('constitution', 0)),
        crit_bonus=float(seed.get('crit_bonus', 0.0)),
        damage_bonus=int(seed.get('damage_bonus', 0)),
        special_effect=str(seed.get('special_effect', '') or ''),
    )