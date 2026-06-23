from typing import Optional, List, Dict, Any

# Utility helpers to compute damage modifiers from statuses.
# These are intentionally simple and can be adjusted later.

BLOCKING_STATUS_IDS = {"petrify", "stun", "sleep", "paralyze"}


def get_blocking_status(entity: Optional[object]) -> Optional[Dict[str, Any]]:
	"""Return the first blocking status dict applied to `entity`, or None.

	Blocking statuses are those that prevent the entity from taking actions during
	their turn (e.g. petrify, stun, sleep, paralyze).
	"""
	if entity is None:
		return None

	statuses = entity.statuses or []
	
	for s in statuses:
		if not isinstance(s, dict):			
			continue
		if s.get('id') in BLOCKING_STATUS_IDS:			
			return s
	return None


def can_take_actions(entity: Optional[object]) -> bool:
	"""Return True if entity may take actions this turn (no blocking statuses present)."""
	return get_blocking_status(entity) is None


def _status_elements(s: Dict[str, Any]) -> List[str]:
	"""Helper: return status elements as a list (preserve duplicates).
	Supports legacy single-key 'element' and newer 'elements' list.
	"""
	if not s:
		return []
	if isinstance(s.get('elements'), list):
		return [str(e) for e in s.get('elements') if e is not None]
	elif s.get('element') is not None:
		return [str(s.get('element'))]
	return []


def compute_outgoing_damage(attacker: Optional[object], base_damage: int, elements: Optional[List[str]] = None) -> int:
	"""Apply attack-side modifiers (attack_buff/attack_debuff/elemental_attack_buff) to base_damage.
	Returns adjusted damage as int.
	
	This function now considers multiplicity: both attack elements and status elements may
	contain duplicates. The elemental attack buff scales with (attack_element_count * status_element_count).
	"""
	if attacker is None or base_damage <=0:
		return base_damage
	dmg = int(base_damage)
	statuses = attacker.statuses or []
	# percentage modifier accumulator (positive increases damage, negative decreases)
	percent =1.0
	for s in statuses:
		sid = s.get('id')
		mag = float(s.get('magnitude',0) or 0.0)
		# attack buff increases outgoing damage
		if sid == 'attack_buff':
			percent += mag *0.25
		elif sid == 'attack_debuff':
			percent -= mag *0.25
		elif sid == 'elemental_attack_buff' and elements:
			# support both legacy single-element and new 'elements' list on statuses
			status_elems = _status_elements(s)
			if not status_elems:
				continue
			# for each unique element in the status, scale by counts from attack and status
			for se in set(status_elems):
				attack_count = elements.count(se)
				status_count = status_elems.count(se)
				if attack_count >0:
					# small base factor retained (0.01) but multiplied by the product of counts
					percent += mag *0.01 * (attack_count * status_count)
	# apply percent
	if percent !=0.0:
		adj = int(dmg * percent)
		return max(0, adj)
	return dmg


def compute_incoming_damage(target: Optional[object], incoming_damage: int, elements: Optional[List[str]] = None, is_physical: bool = False) -> int:
	"""Apply target-side defense modifiers (defense_buff/defense_debuff/elemental_defense_buff/elemental_debuff).
	Returns adjusted damage.

	Elemental modifiers now consider multiplicity: an attack with N matching elements and a status
	with M of those elements scales the modifier by N * M.
	"""
	if target is None or incoming_damage <=0:
		return incoming_damage
	dmg = int(incoming_damage)
	statuses = getattr(target, 'statuses', []) or []
	
	percent =1.0
	for s in statuses:
		sid = s.get('id')
		mag = float(s.get('magnitude',0) or 0.0)
		if sid == 'defense_buff' and is_physical:
			percent -= mag *0.25
		elif sid == 'defense_debuff' and is_physical: # target takes increased damage (this is supposed to be physical damage)
			percent += mag *1.50
		elif sid == 'elemental_defense_buff' and elements:
			status_elems = _status_elements(s)
			if status_elems:
				# for each element type in the status, reduce damage proportional to attack_count * status_count
				for se in set(status_elems):
					attack_count = elements.count(se)
					status_count = status_elems.count(se)
					if attack_count >0:
						percent -= mag *0.10 * (attack_count * status_count)
		elif sid == 'elemental_debuff' and elements: # when hit by matching element, take increased damage
			status_elems = _status_elements(s)
			if status_elems:
				for se in set(status_elems):
					attack_count = elements.count(se)
					status_count = status_elems.count(se)
					if attack_count >0:
						percent += mag *0.10 * (attack_count * status_count)

	# apply percent to damage
	if percent !=0.0:
		adj = int(dmg * percent)
		return max(0, adj)
	return dmg

LOW_DMG_STATUS_MOD = 0.5
def apply_continuous_damage(entity: Optional[object]) -> Dict[str, Any]:
	"""Apply damage-per-turn from continuous statuses on the entity.
	Returns a dict summary: {'total_damage': int, 'applied': int}
	"""
	res = {'total_damage':0, 'applied':0}
	if entity is None:
		return res
	statuses = entity.statuses or []
	
	total =0
	for s in statuses:
		if s.get('id') == 'continuous_damage':
			dpt = s.get('damage_per_turn')
			if dpt is not None:
				amt = int(dpt * LOW_DMG_STATUS_MOD * 0.10)
				if amt >0:
					# element for the tick: support list or single
					se = _status_elements(s)
					# use take_damage if available (pass None as attacker)
					applied = entity.take_damage(amt, attacker=None, elements=se if se else None, physical=False)
					res['applied'] += applied
					total += amt
	res['total_damage'] = total
	return res


def collect_attack_elements(attacker: Optional[object], base_elements: Optional[List[str]] = None) -> List[str]:
	"""Return a normalized list of element strings to consider for an outgoing attack.

	This aggregates any explicit elements provided (e.g. from an ability or weapon)
	and any elemental-attack statuses present on the attacker (e.g. 'elemental_attack_buff').
	The result now preserves multiplicity (duplicates) so callers can rely on counts.
	"""
	out: List[str] = []
	# add base elements preserving duplicates
	if base_elements:
		for e in base_elements:
			if e is None:
				continue
			ev = e.value if hasattr(e, 'value') else str(e)
			if ev:
				out.append(ev)

	# include elements from elemental_attack_buff statuses (preserve duplicates from status.elements)
	statuses = []
	if attacker is not None:
		statuses = attacker.statuses or []

	for s in statuses:
		
		if s.get('id') == 'elemental_attack_buff':
			status_elems = _status_elements(s)
			for se in status_elems:
				if se:
					out.append(se)
		
	return out


def compute_modified_stat(entity: Optional[object], stat_name: str, base_value: int) -> int:
	"""Compute a stat value modified by any applicable status effects on `entity`.

	Supported stat_name values: 'strength', 'dexterity', 'intelligence', 'constitution'.
	This function looks for statuses with ids like '<stat>_buff' and '<stat>_debuff'
	and adds/subtracts their 'magnitude' (interpreted as an integer) from the base value.
	strength and intelligence are damage stats... intelligence also affect healing power
	dexterity affects accuracy, evasion, and combat speed
	constitution affects HP and status resistance.

	Returns the adjusted stat as an int. If no applicable statuses are present, returns base_value.
	"""
	# Safely obtain statuses; allow entity to be None or missing attribute
	statuses = entity.statuses or []
	
	modified = int(base_value)
	for s in statuses:
		sid = s.get('id')

		# read magnitude as float to support fractional scaling
		mag = float(s.get('magnitude',0) or 0.0)

		# apply buffs/debuffs matching the requested stat
		if sid == f'{stat_name}_buff':
			# use exponentiation instead of bitwise XOR; keep integer result
			modified += int(mag **1.2)
		elif sid == f'{stat_name}_debuff':
			modified -= int(mag **1.2)

	return int(modified)
