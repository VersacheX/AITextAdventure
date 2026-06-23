from typing import Optional, Tuple, List, Callable, Dict, Any

from ai_services.ai_pathing_logic import find_nearest_target_by_predicate, direction_from_path, find_path_to
from ai_services.ai_ui_helper import type_victory_message
from game.objects.armor import Armor
from game.objects.weapon import Weapon
from game.objects.utility_item import UtilityItem
from ai_services.ai_city_and_region_helper import find_nearest_shop


def _is_high_value_loot(tup) -> bool:
	# tup = (x,y,z, s)
	x, y, z, s = tup
	try:
		if not isinstance(s, dict):
			return False
		loot = s.get('loot')
		money = s.get('money', 0)
		# prioritize healing/utility, then armor, then money
		if loot:
			# simple heuristics: dict/object with category_name or name containing 'heal' or 'utility'
			name = getattr(loot, 'name', None) if hasattr(loot, 'name') else (loot.get('name') if isinstance(loot, dict) else None)
			cat = getattr(loot, 'category_name', None) if hasattr(loot, 'category_name') else (loot.get('category_name') if isinstance(loot, dict) else None)
			if isinstance(cat, str) and 'utility' in cat.lower():
				return True
			if isinstance(name, str) and 'heal' in name.lower():
				return True
			# armor like items often have 'defense'
			if (hasattr(loot, 'defense') and getattr(loot, 'defense') is not None) or (isinstance(loot, dict) and loot.get('defense') is not None):
				return True
	except Exception:
		return False
	return False


def find_nearest_loot_path(player, player_game, predicate: Optional[Callable] = None) -> Optional[Tuple[Tuple[int,int], List[str]]]:  # should be Optional[Tuple[Tuple[int,int, int], List[str]]]
	"""Return nearest loot target coordinate and path (list of direction keys) or None.

	If `predicate` is None the function uses the internal `_is_high_value_loot` predicate.
	If `predicate` is provided it should accept a single loot item and return truthy
	for desired loot (this keeps callers simple: e.g. `lambda it: it in healing_items`).
	"""
	if predicate is None:
		# use existing high-value heuristic which expects the full (x,y,z,s) tuple
		return find_nearest_target_by_predicate(player, player_game, lambda t: _is_high_value_loot(t))

	# wrap the provided predicate (which expects a loot object) into the full-tuple predicate
	def _wrapped_full_tuple_pred(tup):
		try:
			if not isinstance(tup, tuple):
				return False
			x, y, z, s = tup
			if not isinstance(s, dict):
				return False
			loot = s.get('loot')
			if loot is None:
				return False
			return bool(predicate(loot))
		except Exception:
			return False

	return find_nearest_target_by_predicate(player, player_game, _wrapped_full_tuple_pred)


def next_direction_to_loot(player, player_game, predicate: Optional[Callable] = None, max_distance: int = None) -> Optional[str]:
	"""Return first direction step towards nearest loot that matches `predicate`.

	`predicate` may be None (use high-value heuristic) or a callable accepting a
	single loot item and returning truthy when the loot is desired.
	"""
	p = find_nearest_loot_path(player, player_game, predicate)
	if max_distance is not None and p:
		coord, path = p

		if distance_from_player(player, coord) > max_distance:
			return None
	if not p:
		return None
	coord, path = p
	result = direction_from_path(path)
	# if the player is at the same x,y coord as the loot result, we need to decide if it is on a different z-level then the player then set result to u for up and j for down
	
	return result

def distance_from_player(player, coord: Tuple[int,int]) -> int:
	"""Return manhattan distance from player to coord (x,y)."""
	return abs(player.x - coord[0]) + abs(player.y - coord[1])


# --- Shop-finding helpers (search tiles for building shops) ---

def _collect_shop_tiles(active_area, predicate) -> List[Tuple[int,int,dict]]:
	"""Return list of (x,y,building_dict) for tiles in active_area where predicate(building) is True."""
	results = []
	try:
		tiles = getattr(active_area, 'tiles', {}) or {}
		for (x,y), t in tiles.items():
			try:
				b = getattr(t, 'building', None)
				if not b:
					continue
				if predicate(b):
					results.append((x,y,b))
			except Exception:
				continue
	except Exception:
		pass
	return results


def find_nearest_shop_path(player, player_game, shop_type) -> Optional[Tuple[Tuple[int,int], List[str]]]:
	"""Find nearest tile whose building satisfies predicate. Returns (coord, path) or None."""
	shop_pos, shop_region = find_nearest_shop(player.x, player.y, player_game, shop_type)

	if not shop_pos:
		return (None, None)
	path = find_path_to(player, shop_pos, player_game)
	if path is not None:
		return (shop_pos, path)

	return None


def next_direction_to_nearest_shop(player, player_game, shop_type) -> Optional[str]:
	res = find_nearest_shop_path(player, player_game, shop_type)
	if not res:
		return None
	coord, path = res
	return direction_from_path(path)


def shop_is_armor(building) -> bool:
	# building may be dict with 'name' or flags
	try:
		if isinstance(building, dict):
			name = building.get('name') or building.get('id') or ''
			if isinstance(name, str) and 'armor' in name.lower():
				return True
			# some shops use can_buy + category
			if building.get('can_buy') and building.get('type') == 'shoparmor':
				return True
			# generic can_buy + tags
			if building.get('can_buy') and 'armor' in (building.get('tags') or []):
				return True
		# object-like
		if hasattr(building, 'name') and isinstance(getattr(building, 'name'), str) and 'armor' in getattr(building, 'name').lower():
			return True
	except Exception:
		pass
	return False


def shop_is_items(building) -> bool:
	try:
		if isinstance(building, dict):
			name = building.get('name') or building.get('id') or ''
			if isinstance(name, str) and ('item' in name.lower() or 'shop' in name.lower()):
				return True
			if building.get('can_buy') and building.get('type') == 'shopitems':
				return True
			if building.get('can_buy') and 'utility' in (building.get('tags') or []):
				return True
		if hasattr(building, 'name') and isinstance(getattr(building, 'name'), str) and ('item' in getattr(building, 'name').lower() or 'shop' in getattr(building, 'name').lower()):
			return True
	except Exception:
		pass
	return False


# Helpers and pickup logic moved from demo so other modules can reuse

def _is_healing_item(it: Any) -> bool:
	try:
		name = getattr(it, 'name', '') or (it.get('name') if isinstance(it, dict) else '')
		cat = getattr(it, 'category_name', '') or (it.get('category_name') if isinstance(it, dict) else '')
		if isinstance(cat, str) and 'utility' in cat.lower():
			return True
		if isinstance(name, str) and 'heal' in name.lower():
			return True
		if getattr(it, 'healing', None) or getattr(it, 'healed', None) or getattr(it, 'hp_restore', None):
			return True
	except Exception:
		pass
	return False


def _is_armor_item(it: Any) -> bool:
	try:
		# armor items will usually have a 'defense' attribute
		if getattr(it, 'defense', None) is not None:
			return True
		if isinstance(it, dict) and 'defense' in it:
			return True
	except Exception:
		pass
	return False


def _get_armor_slot_name(it: Any):
	try:
		slot = getattr(it, 'slot', None)
		if slot:
			return getattr(slot, 'name', None) or (slot.get('name') if isinstance(slot, dict) else None)
		# fallback check on dict
		if isinstance(it, dict):
			s = it.get('slot') or it.get('slot_name')
			return s
	except Exception:
		pass
	return None


def _armor_defense_value(it: Any) -> Optional[int]:
	try:
		return int(getattr(it, 'defense', it.get('defense') if isinstance(it, dict) else 0) or 0)
	except Exception:
		return None


def pick_up_sublocations_at_player(active_area, player) -> List[str]:
	"""AI inspects sublocations at current pos and picks up prioritized loot.
	Priorities: healing items, armor that is better than equipped, then others.
	Returns list of picked item descriptions (strings). Empty list if nothing picked.
	"""
	key = (player.x, player.y, player.z)
	sl = active_area.subloc_map.get(key, []) if getattr(active_area, 'subloc_map', None) else []
	if not sl:
		return []

	# score sublocations by priority
	scored: List[Tuple[int, Dict[str, Any]]] = []
	for s in sl:
		score =0
		if not isinstance(s, dict):
			continue
		loot = s.get('loot')
		money = s.get('money',0)
		if loot:
			if _is_healing_item(loot):
				score +=100
			if _is_armor_item(loot):
				# if better than equipped, increase score
				slot = loot.slot.name.upper()
				def_val = loot.defense
				cur_def = 0
				try:
					if slot == 'HEAD' and player.head_armor:
						cur_def = player.head_armor.defense
					elif slot == 'BODY' and player.body_armor:
						cur_def = player.body_armor.defense
					elif slot == 'ARMS' and player.arm_armor:
						cur_def = player.arm_armor.defense
					elif slot == 'LEGS' and player.leg_armor:
						cur_def = player.leg_armor.defense
				except Exception:
					cur_def =0
				if def_val > cur_def:
					score +=80 + (def_val - cur_def)
				else:
					score +=10
			if money and money >0:
				score +=5
			scored.append((score, s))

	scored.sort(key=lambda x: x[0], reverse=True)

	picked_items: List[str] = []
	for score, s in scored:
		loot = s.get('loot')
		money = s.get('money',0)
		if loot:
			active_area.loot_sublocation(player, s)

			name = loot.name
			type_victory_message(f"AI picks up {name}.", delay=0.02)
			picked_items.append(f"picked {name}")
			
			if money and money >0:
				type_victory_message(f"AI picks up {money} money.", delay=0.02)
				picked_items.append(f"picked {money} money")

			# healing or utility -> pick up into inventory via area API
			if _is_healing_item(loot):
				name = loot.name
				type_victory_message(f"AI picks up healing item: {name}", delay=0.02)
				picked_items.append(f"picked {name}")
				continue

			# Try to equip via Player API for armor/weapons when possible
			try:
				# find the looted item instance in the player's inventory by matching id
				player_item = next((it for it in player.inventory if it.id == loot.id), None)
				if player_item is None:
					# nothing to equip
					continue
				if isinstance(player_item, Armor):
					# attempt to equip; equip_armor will handle inventory for old piece
					if player.equip_armor(player_item):
						type_victory_message(f"AI equips {player_item.name} as upgrade!", delay=0.02)						
						picked_items.append(f"equipped {player_item.name}")
						continue
					else:
						type_victory_message(f"AI could not equip {player_item.name}.", delay=0.02)
				elif isinstance(player_item, Weapon):
					if player.equip_weapon(player_item):
						type_victory_message(f"AI equips {player_item.name} as weapon!", delay=0.02)
						picked_items.append(f"equipped {player_item.name}")
						continue
					else:
						type_victory_message(f"AI could not equip {player_item.name}.", delay=0.02)
				elif isinstance(player_item, UtilityItem):
					type_victory_message(f"AI found utility item: {player_item.name}.", delay=0.02)
				else:
					type_victory_message(f"AI found unrecognizable item: {player_item.name}.", delay=0.02)
					type_victory_message(f"Item type: {type(player_item).__name__}", delay=0.02)
					type_victory_message("AI will not be equipping this item.", delay=0.02)
			except Exception as e:
				print(f"Error equipping looted item. {e}")
				input("Press Enter to continue...")
				pass
	return picked_items
