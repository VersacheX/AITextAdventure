import random
from typing import Optional, Dict, Any, List

from game import constants
from game.objects.item import Item, Rarity, RarityDefaultWeights
from game.objects.weapon import Weapon
from game.objects.armor import Armor, ArmorType
from game.objects.utility_item import UtilityItem
from game.objects.special_item import SpecialItem

from game.objects.armor import _instantiate_armor
from game.objects.weapon import _instantiate_weapon
from game.objects.utility_item import _instantiate_utility
from game.objects.special_item import _instantiate_special


def _armor_slot_from_string(slot: str) -> ArmorType:
	key = slot.strip().lower()
	if key == 'head':
		return ArmorType.HEAD
	if key == 'body':
		return ArmorType.BODY
	if key == 'arms':
		return ArmorType.ARMS
	if key == 'legs':
		return ArmorType.LEGS
	# default
	return ArmorType.BODY


def _seed_weight(seed: Dict[str, Any]) -> float:
	"""Return spawn weight for a seed dict. Uses explicit spawn_weight if present,
	otherwise uses rarity default mapping. Seeds store rarity as a string."""
	r = seed.get('rarity')
	if r is None:
		return 0.0
	rarity = Rarity(r)
	
	# allow seeds to override weight explicitly
	if 'spawn_weight' in seed and seed['spawn_weight'] is not None:
		return float(seed['spawn_weight'])
	return float(RarityDefaultWeights.get(rarity,0.0))


def _flatten_all_seeds(player_level: int) -> List[Dict[str, Any]]:
	"""Return a flat list of seed dicts applicable for the given player level.
	Adds a '_seed_type' field: 'weapon','armor','utility','special' and for armor sets 'slot'."""
	out: List[Dict[str, Any]] = []

	def get_min_max_lvl(player_level: int, item_type_max_lvl):
		loot_range = 4
		min_lvl = max(1, player_level - loot_range)
		max_lvl = player_level + loot_range
		total_level_range = max_lvl - min_lvl
		# if level range exceeds item type max level set max to item type max level and min to keep range
		if max_lvl > item_type_max_lvl:
			max_lvl = item_type_max_lvl
			min_lvl = max(1, max_lvl - total_level_range)

		return min_lvl, max_lvl

	# get max 'min_spawn_level' from WEAPON_SEEDS
	weap_min,weap_max	 = get_min_max_lvl(player_level, max(w.get('min_spawn_level',1) for w in constants.WEAPON_SEEDS))
	for w in constants.WEAPON_SEEDS:
		if weap_min <= w.get('min_spawn_level', 1) <= weap_max:
			item = dict(w)
			item['_seed_type'] = 'weapon'
			out.append(item)

	# armor grouped by slot
	arm_min, arm_max = get_min_max_lvl(player_level, max(a.get('min_spawn_level',1) for group in constants.ARMOR_SEEDS.values() for a in group))
	for slot, group in constants.ARMOR_SEEDS.items():
		for a in group:
			if arm_max >= a.get('min_spawn_level',1) >= arm_min:
				item = dict(a)
				item['_seed_type'] = 'armor'
				item['_slot'] = slot
				out.append(item)

	# utility
	util_min, util_max = get_min_max_lvl(player_level, max(u.get('min_spawn_level',1) for u in constants.UTILITY_ITEM_SEEDS))
	for u in constants.UTILITY_ITEM_SEEDS:
		if util_min <= u.get('min_spawn_level',1) <= util_max:
			item = dict(u)
			item['_seed_type'] = 'utility'
			out.append(item)

	# special
	special_min, special_max = get_min_max_lvl(player_level, max(s.get('min_spawn_level', 1) for s in constants.SPECIAL_ITEM_SEEDS))
	for s in constants.SPECIAL_ITEM_SEEDS:
		if special_min <= s.get('min_spawn_level',1) <= special_max:
			item = dict(s)
			item['_seed_type'] = 'special'
			out.append(item)
	return out


def _choose_seed_by_weight(candidates: List[Dict[str, Any]], rng: Optional[random.Random] = None) -> Optional[Dict[str, Any]]:
	if not candidates:
		return None
	weights = [_seed_weight(s) for s in candidates]
	total = sum(weights)
	if total <=0:
		return None
	# normalize
	p = [w / total for w in weights]
	if rng is None:
		choice = random.choices(candidates, weights=p, k=1)[0]
	else:
		choice = rng.choices(candidates, weights=p, k=1)[0]
	return choice


def _create_item_from_seed(seed: Dict[str, Any]) -> Item:
	stype = seed.get('_seed_type')
	if stype == 'weapon':
		return _instantiate_weapon(seed)   
	if stype == 'armor':
		slot = seed.get('_slot', 'body')
		return _instantiate_armor(seed, slot)
	if stype == 'utility':
		return _instantiate_utility(seed)
	if stype == 'special':
		return _instantiate_special(seed)

	# fallback generic item
	print(f'Unknown seed type "{stype}" encountered in _create_item_from_seed: {seed}')
	return None

def generate_loot_for_sublocation(subloc: Dict[str, Any], player_level: int =1, rng: Optional[random.Random] = None) -> Optional[Item]:
	"""Generate a single loot item for the given sublocation and player level.

	This function expects to be called only when a pre-check has already
	determined that the sublocation yields something (i.e., a loot chance
	has passed). It uses seed data and rarity weights to pick an appropriate
	item and returns an Item-derived object or None if none selected.
	"""
	candidates = _flatten_all_seeds(player_level)
	# choose seed by rarity weights
	seed = _choose_seed_by_weight(candidates, rng=rng)
	if seed is None:
		return None
	item = _create_item_from_seed(seed)
	# set spawn metadata if present
	if 'min_spawn_level' in seed:
		item.min_spawn_level = int(seed.get('min_spawn_level',1))
		
	if 'rarity' in seed:		
		item.rarity = Rarity(seed.get('rarity'))
		
	return item
