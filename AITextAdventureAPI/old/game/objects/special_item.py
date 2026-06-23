from dataclasses import dataclass
from typing import Optional, Dict, Any
from .item import Item


@dataclass
class SpecialItem(Item):
	"""Special/non-consumable unique items with story or quest value."""
	effect_description: Optional[str] = None
	recipes: Optional[list] = None

	related_task_id: int = -1 # ID of related quest/task, if any


def _instantiate_special(seed: Dict[str, Any]) -> SpecialItem:
	"""Create a SpecialItem from a seed dict.

	This mirrors other _instantiate_* helpers used across the codebase and
	is intentionally simple: it maps common fields and attaches optional
	metadata when present.
	"""
	si = SpecialItem(
		id=seed.get('id'),
		name=seed.get('name'),
		description=seed.get('description', ''),
		value=seed.get('value',0),
		min_spawn_level=seed.get('min_spawn_level',1),
	)
	# optional metadata
	if 'effect_description' in seed:
		si.effect_description = seed.get('effect_description')
	if 'recipes' in seed:
		si.recipes = seed.get('recipes')
	if 'related_task_id' in seed:
		
		si.related_task_id = int(seed.get('related_task_id', -1))
		
	# propagate rarity string if provided (Item.populate_from_json can normalize later)
	if 'rarity' in seed:
		
		# store raw string on spawn-level field for later conversion if needed
		si.rarity = seed.get('rarity')
		
	return si