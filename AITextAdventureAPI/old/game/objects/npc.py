from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from .item import Item
from .special_item import SpecialItem


@dataclass
class NPC:
	"""Non-player character representation.

	NPCs may be located inside buildings (with a building id and floor index)
	and can provide dialogue, trade, or give a special item. This class is
	kept intentionally simple; game systems can extend it or wrap it with
	behavioral/AI components later.
	"""
	id: Optional[str] = None
	name: str = "NPC"
	description: str = ""
	# Optional position in the world (x, y, z)
	position: Optional[Tuple[int, int, int]] = None
	# Optional reference to a location id (e.g., building or region reference)
	location_reference_id: Optional[str] = None
	standing_text = [
		"Yo, I'm standing here!",
		'You do what I asked?'
	]
	met: bool = False

	def from_dict(d: dict) -> "NPC":
		return NPC(
			id=d.get("id"),
			name=d.get("name", "NPC"),
			description=d.get("description", ""),
			position=tuple(d["position"]) if "position" in d else None,
			location_reference_id=d.get("location_reference_id"),
			met= d.get("met", False)
		)
