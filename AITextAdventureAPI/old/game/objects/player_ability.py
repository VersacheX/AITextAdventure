from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Dict, Any
import game.constants as const
import random
import fnmatch
import game.status_utils as status_utils
from game.region_seeds.player_abilities.ability_requirements import ABILITY_TYPE_REQUIREMENTS
# ABILITY_TYPE_REQUIREMENTS = [
#     {"ability_type": "technique", "required_stats_per_ability_level": [{"strength": 13, "constitution": 9}]},
#     {"ability_type": "spirit", "required_stats_per_ability_level": [{"intelligence": 13}, {"constitution": 9}]},
#     {"ability_type": "magic", "required_stats_per_ability_level": [{"intelligence": 18}]},
#     {"ability_type": "tech", "required_stats_per_ability_level": [{"intelligence": 13}, {"dexterity": 9}]},
#     {"ability_type": "skill", "required_stats_per_ability_level": [{"dexterity": 18}]},
# ]

class AbilityType(Enum):
	MAGIC = "magic"
	TECH = "tech"
	SKILL = "skill"
	SPIRIT = "spirit"
	TECHNIQUE = "technique"

class AbilityStatType:
	#MAGIC = ("magic", [{"intelligence": 18}])
	# TECH = ("tech", [{"intelligence": 13}, {"dexterity": 9}])
	# Mapping from ability_type to required_stats_per_ability_level using ABILITY_TYPE_REQUIREMENTS
	MAGIC = ("magic", [req for req in ABILITY_TYPE_REQUIREMENTS if req.get('ability_type') == 'magic'])
	TECH = ("tech", [req for req in ABILITY_TYPE_REQUIREMENTS if req.get('ability_type') == 'tech'])
	SKILL = ("skill", [req for req in ABILITY_TYPE_REQUIREMENTS if req.get('ability_type') == 'skill'])
	SPIRIT = ("spirit", [req for req in ABILITY_TYPE_REQUIREMENTS if req.get('ability_type') == 'spirit'])
	TECHNIQUE = ("technique", [req for req in ABILITY_TYPE_REQUIREMENTS if req.get('ability_type') == 'technique'])


class Element(Enum):
	LIGHT = "light"
	DARK = "dark"
	EARTH = "earth"
	AIR = "air"
	FIRE = "fire"
	WATER = "water"
	ELECTRIC = "electric"
	ICE = "ice"


class EffectType(Enum):
	DAMAGE = "damage"
	HEAL = "heal"
	STATUS = "status"
	REVIVE = "revive"
	CURE = "cure"


@dataclass
class PlayerAbility:
	"""Represents a player ability composed of elemental units.

	Rules implemented:
	- Ability has a type (magic/tech/skill/spirit) and a level.
	- The number of element "units" the ability can contain grows with level
	 (by default: max elements == level).
	- Elements are chosen from the canonical list and may repeat; repeats
	 increase potency.
	- Abilities have a base power and an effect type (damage/heal/status).
	- `compute_power` provides a deterministic power value based on base
	 power, level and number of element units.
	
	This class intentionally does not depend on a particular combat or
	entity model; `apply` returns a descriptive dict that a caller/game
	system can translate into concrete effects on targets.
	"""
	id: Optional[str] = None
	name: str = "Unnamed Ability"
	description: str = ""
	ability_type: AbilityType = AbilityType.MAGIC
	level: int =1
	elements: List[Element] = field(default_factory=list)
	base_power: int =10
	ap_cost: int =1
	effect: EffectType = EffectType.DAMAGE
	# when effect is a status subtype, `status_key` holds the specific status id
	status_keys: List[Optional[str]] = None
	can_aoe: bool = False
	non_player_ability: bool = False

	def max_elements(self) -> int:
		"""Return how many elemental units this ability can contain.
		Default policy: max elements == ability level (minimum1).
		"""
		return max(1, int(self.level))

	def can_add_element(self) -> bool:
		return len(self.elements) < self.max_elements()

	def add_element(self, element: Element) -> bool:
		"""Add an element unit if there's room. Returns True on success."""
		if not self.can_add_element():
			return False
		self.elements.append(element)
		return True

	def remove_element(self, index: int) -> Optional[Element]:
		"""Remove element at index and return it, or None if out of range."""
		if index <0 or index >= len(self.elements):
			return None
		return self.elements.pop(index)

	def compute_power(self) -> int:
		"""Compute the ability's effective power.

		This version accepts optional owner stat scaling by reading the
		primary stat for the ability type from `AbilityStatType` mapping.
		If the caller wishes to include the owner's stat in the calculation
		they should call `compute_power_with_owner(owner)` or pass the owner's
		stat through `compute_power_with_owner` helper.
		"""
		level_multiplier =1.0 +0.20 * max(0, self.level -1)
		element_multiplier =1.0 +0.35 * len(self.elements)
		power = int(self.base_power * level_multiplier * element_multiplier)
		return max(0, power)

	def compute_power_with_owner(self, owner: Optional[object] = None, percent_reduction: float = 0.0) -> int:
		"""Compute power including owner's primary-stat scaling.
		Owner is expected to have attributes: strength, dexterity, constitution, intelligence.
		Scaling: every point above baseline (3) increases power by5% (0.05), points below
		baseline reduce power accordingly. The stat baseline of3 matches player defaults.
		"""
		base_power = self.compute_power()
		if owner is None:
			return base_power

		# determine which stats to consider based on ability type requirements
		stat_names = []
		atype_val = self.ability_type.value if isinstance(self.ability_type, AbilityType) else str(self.ability_type)
		for entry in ABILITY_TYPE_REQUIREMENTS:
			if entry.get('ability_type') == atype_val:
				reqs = entry.get('required_stats_per_ability_level') or []
				for req in reqs:
					for k in req.keys():
						if k not in stat_names:
							stat_names.append(k)

		# stat_val should be calculated using owner.get_modified_{stat_name}() which guaranteed exists on player and hostile
		stat_vals = []
		for stat_name in stat_names:
			get_modified = getattr(owner, f"get_modified_{stat_name}", None)
			stat_val = get_modified()
			if stat_val is not None:
				stat_vals.append(stat_val)
		stat_val = sum(stat_vals) / len(stat_vals) if stat_vals else None

		if stat_val is None:
			return base_power
		modifier = (float(stat_val)) * float(self.level)
		# clamp modifier to reasonable bounds
		result = max(0, int(base_power + modifier))
		result -= int(result * percent_reduction)
		return result

	def effect_summary(self, owner: Optional[object] = None) -> Dict[str, Any]:
		"""Return a serializable summary describing the ability's effect."""
		value = {
			"id": self.id,
			"name": self.name,
			"description": self.description,
			"type": self.ability_type.value,
			"level": self.level,
			"elements": [e.value for e in self.elements],
			"effect": self.effect.value,
			"status_keys": self.status_keys,
			"ap_cost": self.ap_cost,
			"power": (self.compute_power_with_owner(owner) if owner is not None else self.compute_power()),
		} 

		return value

	def is_elemental(self, element: Element) -> bool:
		"""Return True if the given element is present among the units."""
		return element in self.elements

	def _derive_status_effects(self, owner: Optional[object], target: Optional[object], percent_reduction: float = 0.0) -> List[Dict[str, Any]]:
		"""Derive status descriptors from a status template (effect-based) and elements.

		Templates live in `const.STATUS_EFFECTS`. Each effect previously produced one descriptor
		per element unit; updated behaviour: a status ability produces a single status descriptor
		that contains all associated elements. The single descriptor will be applied at most once.
		"""
		effects: List[Dict[str, Any]] = []
		templates = getattr(const, 'STATUS_EFFECTS', {}) or {}

		for key in (self.status_keys or []):
			# if no key, try to use element-agnostic default
			template = templates.get(key)
			if template is None:
				input(f"no template found for status key {key}")
			# compute ability-scaled power to use for damage-per-turn calculations
			ability_power = self.compute_power_with_owner(owner)
			# determine target constitution for resistance/hit calculations (if provided)
			target_const = target.get_modified_constitution()
			if not target_const:
				input (f"why does target not have const ? {target}")

			# Build a single descriptor that aggregates all elements
			element_values = [e.value for e in self.elements]
			tpl = template
			# Determine duration: respect explicit 'duration' or handle duration_per_level == -1 as permanent
			if tpl.get('duration') is not None:
				duration = tpl.get('duration')
			else:
				dpl = tpl.get('duration_per_level',0.5)
					# duration_per_level == -1 indicates a permanent status until removed
				if dpl == -1:
					duration = -1
				else:
					duration = max(1, int(self.level + float(dpl)))

			# build descriptor
			desc: Dict[str, Any] = {
				"id": tpl.get('id', key),
				"name": f"{tpl.get('display','').strip() or tpl.get('name','')}",
				"type": tpl.get('id', tpl.get('type', 'status')).replace('_',' '),
			}
			if duration == -1:
				desc['duration'] = -1
			else:
					# apply percent reduction to non-permanent durations
				raw = int(max(1, int(duration)))
				desc['duration'] = max(1, raw - int(raw * percent_reduction))

			# attach elements as a list (all elements mapped to this single debuff)
			desc['elements'] = element_values

			# magnitude: scale by number of element units so multi-element abilities are stronger
			if tpl.get('magnitude_per_level') is not None:
				base_mag = max(tpl.get('min_magnitude',0), int(self.level * tpl.get('magnitude_per_level')))
				mag = int(base_mag * (1.0 - percent_reduction) * max(1, len(element_values)))
				desc['magnitude'] = mag

			# heal per turn: beneficial mirror of continuous damage (e.g. 'regen').
			# Derived from ability power the same way damage_per_turn is, but applied
			# as healing each turn instead of damage.
			if tpl.get('heal_per_turn') is not None:
				hpt = int(tpl.get('heal_per_turn') * (1.0 - percent_reduction) * max(1, len(element_values)))
				desc['heal_per_turn'] = hpt
			elif tpl.get('min_heal_per_turn') is not None:
				hmt = max(tpl.get('min_heal_per_turn',1), int(self.level * ability_power * float(tpl.get('magnitude_per_level',0))))
				hmt = int(hmt * (1.0 - percent_reduction) * max(1, len(element_values)))
				desc['heal_per_turn'] = hmt
			# damage per turn: prefer explicit template value otherwise derive from magnitude/ability_power
			elif tpl.get('damage_per_turn') is not None:
				dpt = int(tpl.get('damage_per_turn') * (1.0 - percent_reduction) * max(1, len(element_values)))
				desc['damage_per_turn'] = dpt
			elif tpl.get('magnitude_per_level') is not None:
				# use owner-scaled ability power when available
				dmt = max(tpl.get('min_damage_per_turn',1), int(self.level * ability_power * float(tpl.get('magnitude_per_level'))))
				dmt = int(dmt * (1.0 - percent_reduction) * max(1, len(element_values)))
				desc['damage_per_turn'] = dmt

			# include reference to originating ability
			desc['ability_id'] = self.id
			desc['ability_name'] = self.name

			# apply constitution-based hit check once for the aggregated debuff
			if ability_power <=0:
				hit_chance =0.05
			else:
				hit_chance = float(ability_power) / (float(ability_power) + float(max(1, target_const)) *3.0)
			# clamp
			hit_chance = max(0.05, min(0.95, hit_chance))

			# Check for status immunities, resistances, and weaknesses on the target
			status_id = desc.get('id')
			if status_id and hasattr(target, 'immunities') and status_id in target.immunities:
				hit_chance = 0.0  # Immune
			elif status_id and hasattr(target, 'resistances') and status_id in target.resistances:
				hit_chance *= 0.5  # 50% chance to resist
			elif status_id and hasattr(target, 'weaknesses') and status_id in target.weaknesses:
				hit_chance = min(1.0, hit_chance * 1.5)  # 50% higher chance to land

			# set hit chance to 100% if is beneficial or above 1
			if self._is_beneficial_ability() or hit_chance > 1.0:
				hit_chance = 1.0
			r = random.random()
			if r <= hit_chance:
				effects.append(desc)

		return effects

	def apply(self, target: Optional[object] = None, owner: Optional[object] = None, percent_reduction: float = 0.0) -> Dict[str, Any]:
		"""Return a description of what applying this ability would do.

			This method is intentionally abstract about `target` type: it returns
		
			a dictionary the caller can consume to actually modify a target entity.
		"""
		from game.objects.random_hostile import RandomHostile
		summary = self.effect_summary(owner)
		# include a textual hint for consumers about the action
		if self.effect == EffectType.DAMAGE:
			power = self.compute_power_with_owner(owner, percent_reduction= percent_reduction)

			target_name = target.name
			# apply immediately if a target is provided
			# Build element list from ability elements + attacker statuses
			elems = status_utils.collect_attack_elements(owner, [e.value if e.value else str(e) for e in self.elements] if self.elements else None)
			# Apply outgoing modifiers from attacker statuses (elemental_attack_buff, attack_buff, etc.)
			power = status_utils.compute_outgoing_damage(owner, power, elems)
			# If target is a RandomHostile it supports the extended signature

			applied = target.take_damage(power, attacker=owner, elements=elems if elems else None, physical=False)
			if applied is not None:
				summary['dealt'] = applied

			summary["action"] = f"{self.name} deals {applied} damage to {target_name}"
		elif self.effect == EffectType.HEAL:
			power = self.compute_power_with_owner(owner, percent_reduction= percent_reduction)
			summary["action"] = f"{self.name} restores {power} HP to {target.name}"

			restored = target.heal(power)
			summary['restored'] = restored
		elif self.effect == EffectType.STATUS:
			# build structured status effect info so game systems can apply them
			status_effects = self._derive_status_effects(owner, target, percent_reduction= percent_reduction)
			if len(status_effects) ==0:
				summary["action"] = f"{self.name} failed to apply any status effects to {target.name}"
				return summary

			#status effects
			#[{'id': 'elemental_debuff', 'name': 'E Debuff - Air', 'type': 'elemental debuff', 'duration': 1, 'element': 'air', 'magnitude': 4, 'damage_per_turn': 0, 'ability_id': 'air_skill_lv1_smoke_bomb', 'ability_name': 'Smoke Bomb'}]
			summary["status_effects"] = status_effects
			# readable hint: prefer human-friendly display names when available in constants
			key_map = const.ABILITY_STATUS_KEY_DISPLAY_NAMES
			
			display_names = [key_map.get((s.get('id') if isinstance(s, dict) else None) or s, (s.get('id') if isinstance(s, dict) else str(s))) for s in status_effects]

			# let's make it readable friendly and display without the json brackets
			display_names_display = ", ".join(display_names)

			summary["action"] = f"{self.name} applied status effect(s) {display_names_display} to {target.name}"
			# if target provided, attach statuses to it
			if target is not None:
				added =0
				for desc in status_effects:
					target.add_status(desc, source=owner)
					added +=1
				summary['status_applied'] = added

			# If this status ability also has a non-zero base_power, apply an immediate
			# secondary effect. Beneficial (buff) status abilities heal the target;
			# harmful (debuff) status abilities deal damage to the target.
			if self.base_power != 0:
				power = self.compute_power_with_owner(owner, percent_reduction= percent_reduction)
				if power and power >0 and target is not None:

					power = int(power * status_utils.LOW_DMG_STATUS_MOD)

					if self._is_beneficial_ability():
						# beneficial status: convert power into healing for the target
						restored = target.heal(power)
						if restored is not None:
							summary['status_heal'] = restored
					else:
						# Build element list and apply outgoing modifiers
						elems = status_utils.collect_attack_elements(owner, [e.value if hasattr(e, 'value') else str(e) for e in self.elements] if self.elements else None)
						power = status_utils.compute_outgoing_damage(owner, power, elems)

						applied = target.take_damage(power, attacker=owner, elements=elems if elems else None, physical=False)

						if applied is not None:
							summary['status_damage'] = applied
		# Revive effect: computed power is interpreted as a percentage of target.max_hp; clears statuses on revive
		elif self.effect == EffectType.REVIVE:
			pct = self.compute_power_with_owner(owner, percent_reduction= percent_reduction)
			summary["action"] = f"{self.name} revives {target.name} to {pct}% of max HP"
			if target is not None and hasattr(target, 'is_alive'):
				if not target.is_alive():
					# compute revive HP as percentage of max_hp when available

					revive_hp = int(max(1, int(round(float(target.max_hp) * (float(pct) /100.0)))))
					# set current_hp but do not exceed max_hp
					target.current_hp = min(target.max_hp, revive_hp)

					target.statuses = []
					
					summary['revived'] = True
				else:
					summary['revived'] = False
		elif self.effect == EffectType.CURE:
			# CURE uses status_key to remove statuses from the target.
			# If status_key == 'all' then use cure_all_debuffs() to remove common debuffs;
			# if status_key == 'debuff' then use cure_elemental_and_stat_debuffs();
			# otherwise status_key is a concrete status id (single or list) to remove.
			# CURE also carries a base_power that heals the target on application,
			# mirroring the beneficial secondary hit of a buff STATUS ability
			# (flat, halved by status_utils.LOW_DMG_STATUS_MOD, no level multiplier).

			if not target:
				summary['action'] = f"{self.name} would cure statuses but no target provided"
				return summary

			def _apply_cure_heal():
				"""Apply the cure's base_power as healing, halved like a status hit."""
				if self.base_power == 0 or target is None:
					return
				power = self.compute_power_with_owner(owner, percent_reduction=percent_reduction)
				if power and power > 0:
					power = int(power * status_utils.LOW_DMG_STATUS_MOD)
					restored = target.heal(power)
					if restored is not None:
						summary['status_heal'] = restored

			removed = 0
			cured_all = False
			# support 'all' keyword
			for key in (self.status_keys or []):
				if isinstance(key, str) and key.lower() == 'all':
					removed = target.cure_all_debuffs()
					cured_all = True
					break
				elif isinstance(key, str) and key.lower() == 'debuff':
					removed += target.cure_elemental_and_stat_debuffs()
				# support single id or list of ids
				else:
					removed += target.remove_status_by_id(key)

			_apply_cure_heal()

			if cured_all:
				summary['action'] = f"{self.name} removed {removed} debuff(s) from {target.name}"
			else:
				summary['action'] = f"{self.name} removed {removed} status(es) from {target.name}"
			summary['removed'] = removed
			return summary

		#input (f"summary: {summary}")
		# callers can also inspect 'power' and 'elements' to enact effects
		return summary
	
	def _is_beneficial_ability(self) -> bool:
		"""Return True if ability.effect matches BENEFICIAL_PLAYER_ABILITY_EFFECTS."""
		# Normalize effect value
		#effect: EffectType = EffectType.DAMAGE
		eff = self.effect
		#eff_val = self.effect.value
        
		patterns = const.BENEFICIAL_PLAYER_ABILITY_EFFECTS

		# Special-case: 'status' effects are ambiguous only consider them
		# beneficial when the specific status key matches a buff pattern (e.g. '*_buff').
		if eff == EffectType.STATUS:
			for status_key in (self.status_keys or []):
				# collect patterns that indicate buffs
				buff_patterns = [p for p in patterns if '_buff' in str(p)]
				if bool(buff_patterns) and self._matches_patterns(status_key, buff_patterns):
					return True
			return False

		# Otherwise, match the effect string against the configured patterns
		# excluding the generic 'status' marker.
		non_status_patterns = [p for p in patterns if str(p).lower() != 'status']
		return self._matches_patterns(str(eff.value), non_status_patterns)

	def _matches_patterns(self, value: Optional[str], patterns: List[str]) -> bool:
		"""Case-insensitive wildcard match against a list of patterns."""
		if not value:
			return False
		val = str(value).lower()
		for p in (patterns or []):
			if fnmatch.fnmatch(val, str(p).lower()):
				return True
		return False

def get_potential_player_abilities(player: Optional[object] = None) -> List[Dict[str, Any]]:
	"""Return list of ability dicts from constants that the player does not already have.

	This converts the seed dicts in `PLAYER_ABILITY_SEEDS` into serializable dicts
	that callers can present in the UI. If `player` is provided and has an `abilities`
	list, abilities already known will be filtered out.

	Selection rules (updated):
	- Abilities are filtered by stat requirements defined in
	 `game.region_seeds.player_abilities.ability_requirements.ABILITY_TYPE_REQUIREMENTS`.
	 Each requirement specifies per-ability-level stat minima; the effective
	 required stat is (per_level_value * ability_level). For example a spirit
	 ability with level2 requires int13*2 and con9*2.@@-< Not the actual formula but yeh.
	 -actual formula currently --- required = int(per_level_val) + int((int(per_level_val) * ((level - 1)* 1.5)) **1.25)
	- Only abilities for which the player meets all required stats are returned.
	- We return all abilities the player is capable of using ignoring existing abilities and non-player abilities.
	- player.abilities are PlayerAbility objects strongly typed; we check .id against seed ids.
	"""
	res: List[Dict[str, Any]] = []
	owned = set()
	owned = player.abilities

	abilities = getattr(const, 'PLAYER_ABILITY_SEEDS', []) or []
	# prefer lower-level (entry-level) abilities first so players see level-1 abilities
	abilities = sorted(abilities, key=lambda x: int(x.get('level',1)))

	# build quick lookup from ability_type -> list of per-level requirement dicts
	req_lookup = {}
	for entry in ABILITY_TYPE_REQUIREMENTS:
		type_name = entry.get('ability_type')
		reqs = entry.get('required_stats_per_ability_level') or []
		req_lookup[type_name] = reqs

	for a in abilities:
		# skip seeds explicitly marked as non-player abilities (support both key names)
		if a.get('non_player_ability'):
			continue

		# skip abilities already owned
		if any(owned_ability.id == a.get('id') for owned_ability in owned):
			continue

		# If player provided, filter by stat-based requirements
		if player is not None:
			atype = a.get('ability_type')
			level = int(a.get('level',1))
			# find requirements for this ability type
			reqs = req_lookup.get(atype) if atype is not None else None
			meets = True
			if reqs:
				# each dict in reqs represents a stat requirement; multiply by ability level
				for req in reqs:
					for stat_name, per_level_val in req.items():
						required = int(per_level_val) + int((int(per_level_val) * ((level - 1)* 1.5)) **1.25)
						player_val = int(getattr(player, stat_name,0) or 0)
						if player_val < required:
							meets = False
							break
					if not meets:
						break
			if not meets:
				continue

		entry = {
			'id': a.get('id'),
			'name': a.get('name'),
			'description': a.get('description', ''),
			'ability_type': a.get('ability_type'),
			'level': a.get('level'),
			'elements': list(a.get('elements', [])),
			'base_power': a.get('base_power'),
			'ap_cost': a.get('ap_cost'),
			'effect': a.get('effect'),
			'status_keys': a.get('status_keys'),
			'can_aoe': a.get('can_aoe', False),
			'non_player_ability': a.get('non_player_ability', False)
		}
		res.append(entry)

	return res

def get_potential_player_abilities_as_player_ability_list(player: Optional[object] = None) -> List[PlayerAbility]:
	"""Return potential player abilities as instantiated PlayerAbility objects."""
	dicts = get_potential_player_abilities(player)
	res: List[PlayerAbility] = []
	for d in dicts:
		ability = _instantiate_from_seed(d)
		res.append(ability)
	return res

def _instantiate_from_seed(seed: Dict[str, Any]) -> PlayerAbility:
	"""Create a PlayerAbility instance from a seed dict in constants."""
	if not seed:
		return PlayerAbility()
	# map strings to enums; be permissive
	atype = AbilityType(seed.get('ability_type'))
	elements = []
	for e in seed.get('elements', []):
		elem = Element(e)
		if elem is not None:
			elements.append(elem)
	
	effect = EffectType(seed.get('effect'))
	
	return PlayerAbility(
		id=seed.get('id'),
		name=seed.get('name') or 'Ability',
		description=seed.get('description',''),
		ability_type=atype,
		level=seed.get('level',1),
		elements=elements,
		base_power=seed.get('base_power',10),
		ap_cost=seed.get('ap_cost',1),
		effect=effect,
		status_keys=seed.get('status_keys'),
		can_aoe=seed.get('can_aoe', False),
		non_player_ability=seed.get('non_player_ability', False),
	)


def get_player_ability_instances(player: Optional[object]) -> List[PlayerAbility]:
	"""Return instantiated PlayerAbility objects for abilities the player knows."""
	res: List[PlayerAbility] = []
	if player is None:
		return res
	owned = getattr(player, 'abilities', []) or []
	for aid in owned:
		seed = next((s for s in getattr(const, 'PLAYER_ABILITY_SEEDS', []) if s.get('id') == aid), None)
		if seed is not None:
			res.append(_instantiate_from_seed(seed))
	return res

