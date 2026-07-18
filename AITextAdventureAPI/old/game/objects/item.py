from dataclasses import dataclass
import game.constants  as const
from typing import Optional, Any, List
from enum import Enum
import fnmatch

class Rarity(Enum):
	COMMON = "common"
	UNCOMMON = "uncommon"
	RARE = "rare"
	SUPERRARE = "superrare"
	NOTFOUND = "notfound"


# Default spawn weights (percent) per rarity used by generators when an explicit
# spawn_weight is not provided on an item instance.
RarityDefaultWeights = {
	Rarity.COMMON:58.0,
	Rarity.UNCOMMON:28.0,
	Rarity.RARE:12.0,
	Rarity.SUPERRARE:2.0,
	Rarity.NOTFOUND:0.0,
}

@dataclass
class Item:
	"""Base class for all items.

	Fields:
	- id: optional unique identifier
	- name: display name
	- description: short description
	- weight: item weight (arbitrary units)
	- value: monetary value
	- stackable: whether item stacks in inventory
	- max_stack: maximum items per stack
	- quantity: current quantity (for stackable items)
	- min_spawn_level: minimum player/area level required for this item to spawn
	- rarity: rarity category used to weight spawn tables
	- spawn_weight: optional explicit spawn weight (percent). When None the
	 generator should use the RarityDefaultWeights mapping for the item's rarity.
	"""
	id: Optional[str] = None
	name: str = "Unnamed Item"
	description: str = ""
	weight: float =0.0
	value: int =0
	stackable: bool = False
	max_stack: int =1
	quantity: int =1

	# Spawn/generation properties
	min_spawn_level: int =1
	rarity: Rarity = Rarity.COMMON
	spawn_weight: Optional[float] = None
	# If True, item does not lose durability or break
	unbreakable: bool = False

	def is_stack_full(self) -> bool:
		return self.stackable and self.quantity >= self.max_stack

	def can_stack_with(self, other: "Item") -> bool:
		return (
			other is not None
			and type(self) is type(other)
			and self.stackable
			and other.stackable
			and self.id == other.id
		)

	def add_quantity(self, amount: int) -> int:
		"""Try to add quantity to this stack. Returns leftover amount that couldn't be added."""
		if not self.stackable:
			return amount
		space = max(0, self.max_stack - self.quantity)
		to_add = min(space, amount)
		self.quantity += to_add
		return amount - to_add

	def remove_quantity(self, amount: int) -> int:
		"""Remove quantity and return actual removed amount."""
		removed = min(self.quantity, amount)
		self.quantity -= removed
		return removed

	def get_spawn_weight(self) -> float:
		"""Return the spawn weight (percent) for this item.

		If `spawn_weight` is explicitly set on the instance that value is
		returned. Otherwise the default weight for the item's rarity is used.
		"""
		if self.spawn_weight is not None:
			return float(self.spawn_weight)
		return float(RarityDefaultWeights.get(self.rarity,0.0))

	def can_spawn_for_level(self, level: int) -> bool:
		"""Return True if the given level meets the item's minimum spawn requirement."""
		return level >= max(1, int(self.min_spawn_level))

	def populate_from_json(self, data: dict) -> None:
		"""Populate item fields from JSON data."""
		self.id = data.get("id", self.id)
		self.name = data.get("name", self.name)
		self.description = data.get("description", self.description)
		self.weight = data.get("weight", self.weight)
		self.value = data.get("value", self.value)
		self.stackable = data.get("stackable", self.stackable)
		self.max_stack = data.get("max_stack", self.max_stack)
		self.quantity = data.get("quantity", self.quantity)
		self.min_spawn_level = data.get("min_spawn_level", self.min_spawn_level)
		rarity_str = data.get("rarity", self.rarity.value)
		
		self.rarity = Rarity(rarity_str)
		
		self.spawn_weight = data.get("spawn_weight", self.spawn_weight)
		self.unbreakable = data.get("unbreakable", self.unbreakable)
	
	def _is_beneficial_item(self) -> bool:
		"""Return True if item.effect matches BENEFICIAL_ITEM_EFFECTS."""		

		return self._matches_patterns(self.effect, const.BENEFICIAL_ITEM_EFFECTS)

	def _matches_patterns(self, value: Optional[str], patterns: List[str]) -> bool:
		"""Case-insensitive wildcard match against a list of patterns."""
		if not value:
			return False
		val = str(value).lower()
		for p in (patterns or []):
			if fnmatch.fnmatch(val, str(p).lower()):
				return True
		return False


# Helper to instantiate an Item (Weapon/Armor/Utility/Special) from a seed id or seed dict.
# This centralizes logic so other modules can call it instead of duplicating
# instantiation code and risking import cycles.
def instantiate_item_from_id(drop_ref):
    """Given a drop reference which may be:
    - None -> returns None
    - a string id referencing a seed in game.constants (WEAPON_SEEDS, ARMOR_SEEDS,
      UTILITY_ITEM_SEEDS, SPECIAL_ITEM_SEEDS) or ACCESSORY_SEEDS
    - a seed dict (mapping)

    Attempts to create and return a concrete Item (Weapon/Armor/UtilityItem/SpecialItem/Accessory)
    using the object's module-level _instantiate_* helpers. Exceptions from imports
    or instantiation will propagate to the caller (no try/except here by request).
    """
    if not drop_ref:
        return None

    import game.constants as const

    from game.objects.weapon import _instantiate_weapon
    from game.objects.armor import _instantiate_armor
    from game.objects.utility_item import _instantiate_utility
    from game.objects.special_item import _instantiate_special

    def _find_in_const(list_or_map, ident):
        if not list_or_map:
            return None, None
        is_map = isinstance(list_or_map, dict)
        for entry in (list_or_map.items() if is_map else list_or_map):
            if is_map:
                slot, group = entry
                for s in group or []:
                    if isinstance(s, dict) and s.get('id') == ident:
                        return s, slot
            else:
                s = entry
                if isinstance(s, dict) and s.get('id') == ident:
                    return s, None
        return None, None

    if isinstance(drop_ref, str):
        ident = drop_ref

        # try weapon
        s, _ = _find_in_const(const.WEAPON_SEEDS, ident)
        if s:
            return _instantiate_weapon(s)
        # try armor
        s, slot = _find_in_const(const.ARMOR_SEEDS, ident)
        if s:
            return _instantiate_armor(s, slot)
        # try utility
        s, _ = _find_in_const(const.UTILITY_ITEM_SEEDS, ident)
        if s:
            return _instantiate_utility(s)
        # try special
        s, _ = _find_in_const(const.SPECIAL_ITEM_SEEDS, ident)
        if s:
            return _instantiate_special(s)
        # try accessory
        try:
            from game.constants_accesories import ACCESSORY_SEEDS
            from game.objects.accessory import instantiate_accessory
            acc_seed = next((a for a in ACCESSORY_SEEDS if a.get('id') == ident), None)
            if acc_seed:
                return instantiate_accessory(acc_seed)
        except ImportError:
            pass

        return None

    return None
