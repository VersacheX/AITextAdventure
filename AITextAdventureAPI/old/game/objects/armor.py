from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, Any
from .item import Item


class ArmorType(Enum):
	HEAD = "head"
	BODY = "body"
	ARMS = "arms"
	LEGS = "legs"


@dataclass
class Armor(Item):
	"""Armor item that can be equipped to a specific slot.

	Fields:
	- slot: ArmorType where this armor can be equipped
	- defense: flat damage reduction provided by the armor
	- durability: current durability
	- max_durability: maximum durability
	"""
	slot: ArmorType = ArmorType.BODY
	defense: int =0
	durability: int =100
	max_durability: int =100
	strength: Optional[int] = 0  # optional strength buff
	dexterity: Optional[int] = 0  # optional dexterity buff
	intelligence: Optional[int] = 0  # optional intelligence buff
	constitution: Optional[int] = 0  # optional constitution buff
	elements: Optional[list[str]] = None  # optional list of elemental attributes, e.g. ["fire", "ice"]

	def is_broken(self) -> bool:
		return self.durability <=0

	def take_damage(self, amount: int) -> None:
		"""Reduce durability by amount (non-negative)."""
		if amount <=0:
			return
		#self.durability = max(0, self.durability - amount)

	def repair(self, amount: int) -> None:
		if amount <=0:
			return
		self.durability = min(self.max_durability, self.durability + amount)

def _instantiate_armor(seed: Dict[str, Any], slot_name: str) -> Armor:
    a = Armor(
        id=seed.get('id'),
        name=seed.get('name'),
        description=seed.get('description', ''),
        slot=ArmorType[slot_name.upper()] if slot_name.upper() in ArmorType.__members__ else ArmorType.BODY,
        defense=seed.get('defense',1),
        durability=seed.get('durability',50),
        max_durability=seed.get('max_durability',50),
        value=seed.get('value',0),
        min_spawn_level=seed.get('min_spawn_level',1),
		strength=seed.get('strength'),
		dexterity=seed.get('dexterity'),
		intelligence=seed.get('intelligence'),
		constitution=seed.get('constitution'),
		elements=seed.get('elements')
    )
    return a