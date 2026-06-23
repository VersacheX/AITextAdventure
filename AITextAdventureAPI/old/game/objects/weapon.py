from dataclasses import dataclass
from typing import Optional, Dict, Any
from .item import Item


@dataclass
class Weapon(Item):
	"""Weapon item used for combat.

	Fields:
	- damage: base damage dealt by the weapon
	- damage_type: textual damage type (e.g., "slashing", "piercing")
	- ap_cost: action points cost to use
	- range: effective range in tiles
	- critical_chance: percent (0-100)
	"""
	damage: int =1
	damage_type: str = "physical"
	ap_cost: int =0
	range: int =1
	critical_chance: float =0.0
	strength: Optional[int] = 0  # optional strength buff
	dexterity: Optional[int] = 0  # optional dexterity buff
	intelligence: Optional[int] = 0  # optional intelligence buff
	constitution: Optional[int] = 0  # optional constitution buff
	elements: Optional[list[str]] = None  # optional list of elemental attributes, e.g. ["fire", "ice"]

	# optional durability for weapons
	durability: int =1
	max_durability: int =1

	def expected_damage(self) -> float:
		"""Return expected damage considering critical chance (simple model)."""
		return self.damage * (1 + (self.critical_chance /100.0))

def _instantiate_weapon(seed: Dict[str, Any]) -> Weapon:
    w = Weapon(
        id=seed.get('id'),
        name=seed.get('name'),
        description=seed.get('description', ''),
        damage=seed.get('damage',1),
        damage_type=seed.get('damage_type', 'physical'),
        ap_cost=seed.get('ap_cost',1),
        range=seed.get('range',1),
        critical_chance=seed.get('critical_chance',0.0),
        value=seed.get('value',0),
        min_spawn_level=seed.get('min_spawn_level',1),
		strength=seed.get('strength'),
		dexterity=seed.get('dexterity'),
		intelligence=seed.get('intelligence'),
		elements=seed.get('elements')
    )

    # assign basic durability if provided or derived from value
    max_dur = seed.get('max_durability') or seed.get('durability') or max(10, int(w.value //2))
    w.max_durability = max_dur
    w.durability = seed.get('durability', w.max_durability)
    return w