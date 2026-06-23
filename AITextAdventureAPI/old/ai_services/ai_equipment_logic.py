from typing import List, Any, Dict, Optional

from AITextAdventureAPI.old.game.objects.weapon import Weapon
from game.objects.armor import Armor, ArmorType


def _normalize_slot_name(slot: Any) -> Optional[str]:
	"""Return a normalized uppercase slot name (e.g. 'HEAD','BODY') or None."""
	if slot is None:
		return None
	# ArmorType enum
	if isinstance(slot, ArmorType):
		return slot.name.upper()
	# # object with name attribute
	# name = getattr(slot, "name", None)
	# if isinstance(name, str):
	# 	return name.upper()
	# # string or dict
	# if isinstance(slot, str):
	# 	return slot.upper()
	# if isinstance(slot, dict):
	# 	s = slot.get("slot") or slot.get("slot_name")
	# 	if isinstance(s, str):
	# 		return s.upper()
		
	return None


def get_current_armor_defense(player: Any, slot_name: str) -> int:
	"""Return the defense value of the player's currently equipped armor in the given slot.

	slot_name: one of 'HEAD','BODY','ARMS','LEGS' (case-insensitive)
	"""
	if not slot_name:
		return 0
	sn = slot_name.upper()
	if sn == "HEAD":
		a = player.head_armor
	elif sn == "BODY":
		a = player.body_armor
	elif sn == "ARMS":
		a = player.arm_armor
	elif sn == "LEGS":
		a = player.leg_armor
	else:
		# unknown slot
		return 0
	if a is None:
		return 0
	return int(a.defense) or 0


def equip_item_if_better(player: Any, item: Any) -> bool:
	"""Equip `item` onto the player if it is an upgrade for its armor slot.

	If equipping, the previous item (if any) will be placed into the player's inventory
	when possible. Returns True if the item was equipped, False otherwise.

	This function will also handle weapons (items with a `damage` attribute) by
	delegating to `equip_weapon_if_better` when the item has no armor slot.
	"""
	if item is None:
		return False
	# determine slot name
	slot = item.slot
	slot_name = _normalize_slot_name(slot)
	# if no armor slot, treat as potential weapon
	if slot_name is None:
		# detect weapon by presence of damage attribute or dict key
		dmg = getattr(item, "damage", None)
		if dmg is not None:
			# delegate to weapon equip logic
			return equip_weapon_if_better(player, item)
		# not a weapon and no slot
		return False

	cur_def = get_current_armor_defense(player, slot_name)
	new_def = item.defense

	if new_def <= cur_def:
		return False

	# equip via Player API which handles stashing/un-stashing
	# player.equip_armor accepts Armor instances or dict-like seeds
	return bool(getattr(player, 'equip_armor', lambda x: False)(item))

def select_purchases_for_armor(player: Any, stock: List[Any], budget: int = 0, include_weapons: bool = False) -> List[Any]:
	"""Select a list of armor items from `stock` to purchase given `budget`.

	Strategy:
	- For each slot, prefer the highest-defense affordable item that improves current defense.
	- Do not exceed budget. Return list of items to buy (may be empty).

	If `include_weapons` is True then the function will also consider weapons from the
	stock and may include a weapon purchase using remaining budget.
	"""
	if not stock:
		return []
	# normalize stock by slot
	by_slot: Dict[str, List[Any]] = {}
	for it in stock:
		slot = it.slot
		sn = _normalize_slot_name(slot)
		if sn is None:
			continue
		by_slot.setdefault(sn, []).append(it)

	picks: List[Any] = []
	remaining = int(budget or 0)

	# iterate slots and pick best upgrade available within budget
	for slot_name, items in by_slot.items():
		# current defense
		cur = get_current_armor_defense(player, slot_name)

		# sort candidate items by defense desc, then by value asc
		def _val(itm: Any) -> int:
			return itm.value

		def _def(itm: Any) -> int:
			return itm.defense

		candidates = sorted(items, key=lambda x: (_def(x) * -1, _val(x)))
		for cand in candidates:
			cand_def = _def(cand)
			cand_price = _val(cand)
			if cand_def <= cur:
				# not an upgrade
				continue
			if cand_price > remaining:
				# cannot afford this candidate, continue to next (cheaper) candidate
				continue
			picks.append(cand)
			remaining -= cand_price
			# only one purchase per slot for now
			break

	# optionally consider weapons using remaining budget
	if include_weapons and remaining > 0:
		# helper to detect weapon-like items
		def _is_weapon(it: Any) -> bool:
			if isinstance(it, dict):
				return it.damage
			return it.damage

		weapon_stock = [it for it in stock if _is_weapon(it)]
		if weapon_stock:
			wpicks = select_purchases_for_weapons(player, weapon_stock, remaining)
			# subtract cost of chosen weapons from remaining and extend picks
			for w in wpicks:
				price = w.value
				
				if price <= remaining:
					picks.append(w)
					remaining -= price

	return picks


# detect item needs (simple heuristic: low count of healing/utility items)
def _is_healing_item(it: Any) -> bool:
	name = getattr(it, "name", "") or (it.get("name") if isinstance(it, dict) else "")
	cat = getattr(it, "category_name", "") or (it.get("category_name") if isinstance(it, dict) else "")
	# utility category or heal in name
	if isinstance(cat, str) and "utility" in cat.lower():
		return True
	if isinstance(name, str) and "heal" in name.lower():
		return True
	# explicit healing flags
	if getattr(it, "healing", None) or getattr(it, "hp_restore", None):
		return True
	# items that restore AP or have heal_fraction/ap_fraction
	if isinstance(it, dict):
		if it.get("heal_fraction") or it.get("ap_fraction"):
			return True
		if it.get("effect") and str(it.get("effect")).startswith("heal"):
			return True
	else:
		if getattr(it, "heal_fraction", None) or getattr(it, "ap_fraction", None):
			return True
		if getattr(it, "effect", None) and str(getattr(it, "effect")).startswith("heal"):
			return True
	return False


# ------------------ Weapon helpers ------------------

def get_current_weapon_damage(player: Any) -> int:
	"""Return damage value of currently equipped weapon (or0)."""
	w = player.equipped_weapon
	if w is not None:
		return w.damage
	return 0


def equip_weapon_if_better(player: Any, item: Weapon) -> bool:
	"""Equip weapon if it has higher damage than currently equipped.

	If equipping, the old weapon is placed into inventory when possible.
	Returns True if equipped.
	"""
	if item is None:
		return False

	new_dmg = item.damage

	cur = get_current_weapon_damage(player)
	if new_dmg <= cur:
		return False

	# delegate to player's equip_weapon which handles inventory moves and dict seeds
	return player.equip_weapon(item)


def select_purchases_for_weapons(player: Any, stock: List[Weapon], budget: int = 0) -> List[Any]:
	"""Select weapon purchases from stock given budget.

	Strategy: prefer weapons that increase damage and provide best (damage delta / price).
	"""
	if not stock:
		return []
	cur = get_current_weapon_damage(player)
	picks: List[Weapon] = []
	remaining = int(budget or 0)

	candidates = []
	for it in stock:
		dmg = it.damage
		price = it.value
		delta = dmg - cur
		if delta <= 0:
			continue
		score = float(delta) / (price if price > 0 else 1.0)
		candidates.append((score, delta, price, it))

	candidates.sort(key=lambda x: (x[0], x[1]), reverse=True)
	for score, delta, price, it in candidates:
		if price > remaining:
			continue
		picks.append(it)
		remaining -= price
		# for now pick only one weapon
		break
	return picks


# ------------------ Item / Utility purchase helpers ------------------

def _get_item_id(it: Item) -> Optional[str]:
	return it.id

def _get_item_value(it: Item) -> int:
	return it.value


def _get_item_effect(it: UtilityItem) -> Optional[str]:
	return it.effect


def select_purchases_for_items(player: Any, stock: List[UtilityItem], budget: int = 0, required_inventory: Optional[Dict[str, int]] = None) -> List[Any]:
	"""Select utility/item purchases given budget.

	Rules:
	- Healing items and AP restoratives prioritized when low on those items.
	- Items that remove or cure specific status effects (have `effect`) are low priority
	 unless the player currently has that status (or effect == 'cure_all_debuffs').
	- If `required_inventory` (mapping item id -> desired count) is provided, try to
	 satisfy it first within budget.
	"""
	if not stock:
		return []
	remaining = int(budget or 0)
	picks: List[UtilityItem] = []

	# inventory counts by id/name
	inv = getattr(player, "inventory", []) or []
	have_counts: Dict[str, int] = {}
	for it in inv:
		iid = _get_item_id(it)
		if not iid:
			continue
		have_counts[iid] = have_counts.get(iid, 0) + 1

	# helper: check player's active status ids
	player_status_ids = set()
	for st in getattr(player, "statuses", []) or []:
		if isinstance(st, dict):
			player_status_ids.add(st.get("id"))

	# satisfy required inventory first
	if required_inventory:
		for want_id, want_count in (required_inventory.items()):
			have = have_counts.get(want_id, 0)
			need = max(0, int(want_count) - have)
			if need <= 0:
				continue
			# find matching stock entries by id or name
			candidates = [s for s in stock if (_get_item_id(s) == want_id)]
			# sort by price asc
			candidates.sort(key=lambda x: _get_item_value(x))
			for c in candidates:
				price = _get_item_value(c)
				if price > remaining:
					continue
				picks.append(c)
				remaining -= price
				need -= 1
				if need <= 0:
					break

	# candidate pools
	healing_candidates: List[Any] = []
	status_cures: List[Any] = []
	cure_all_candidates: List[Any] = []

	for it in stock:
		# skip if already picked
		if it in picks:
			continue
		# determine categories
		effect = _get_item_effect(it)
		if _is_healing_item(it):
			healing_candidates.append(it)
			continue
		if effect:
			# consider specific status cures if player has the exact status id
			if isinstance(effect, str) and effect == 'cure_all_debuffs':
				cure_all_candidates.append(it)
			elif isinstance(effect, str) and effect in player_status_ids:
				status_cures.append(it)
			# otherwise low priority (skip for now)

	# sort healing items by value asc (cheaper first) and prefer those that heal more if available
	healing_candidates.sort(key=lambda x: (_get_item_value(x), 0))
	for h in healing_candidates:
		price = _get_item_value(h)
		if price > remaining:
			continue
		# prefer to have at least 2 healing items
		count_have = have_counts.get(_get_item_id(h) or '', 0) + sum(1 for p in picks if _get_item_id(p) == _get_item_id(h))
		if count_have >= 2:
			continue
		picks.append(h)
		remaining -= price

	# consider status-specific cures (only if player has that status)
	for s in status_cures:
		price = _get_item_value(s)
		if price > remaining:
			continue
		picks.append(s)
		remaining -= price

	# consider cure_all_debuffs items only if affordable and we have remaining budget
	for c in cure_all_candidates:
		price = _get_item_value(c)
		if price > remaining:
			continue
		picks.append(c)
		remaining -= price

	return picks