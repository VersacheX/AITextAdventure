import random
from typing import List, Optional, Union, Tuple, Dict, Any
from dataclasses import dataclass, field
import uuid

from .item import Item
from .armor import Armor
from .weapon import Weapon
from .utility_item import UtilityItem
from .special_item import SpecialItem

import game.status_utils as status_utils
import game.constants as const
from game.region_seeds.player_abilities.ability_requirements import (
	CLASS_STAT_SPLIT,
	CLASS_LEVEL1_STATS,
	CLASS_HP_RATIO,
)

ItemType = Union[Item, Armor, Weapon, UtilityItem, SpecialItem]

# IMPLEMENTATION_SPEC_leveling.md Part 1: flat HP per level, and HP per CON
# depending on whether the CON was gained at creation (level 1) or by leveling.
HP_PER_LEVEL = 35             # flat max HP per level (was 20)
HP_PER_CON_AT_CREATION = 2    # level-1 / starting CON
HP_PER_CON_ON_LEVEL = 8       # CON gained after level 1
HP_FORMULA_VERSION = 2

_DEFAULT_MAX_ACCESSORY_SLOTS = 3


@dataclass
class Player:
	from .player_ability import PlayerAbility
	"""Simple player representation used by the console demo and movement service.

	Constructor matches usage in `console_game_gameloop.py`: `Player(name,0,0,0, False)`.
	Fields:
	- name: player display name
	- x, y, z: integer world coordinates (z is the vertical index; z==0 -> floor1 for display)
	- inside: bool whether the player is inside a building
	"""
	# seed id on object instantiation so it is unique (not part of dataclass __init__)
	_uuid: str = field(default_factory=lambda: uuid.uuid4().hex, init=False)

	name: str
	x: int = 0
	y: int = 0
	z: int = 0
	inside: bool = False

	arm_armor: Optional[Armor] = None
	head_armor: Optional[Armor] = None
	body_armor: Optional[Armor] = None
	leg_armor: Optional[Armor] = None
	equipped_weapon: Optional[Weapon] = None

	# Accessory slot: array of equipped accessories, capped by max_accessory_slots.
	# Each entry is an Accessory instance from constants_accessories.
	accessories: List[Any] = field(default_factory=list)
	max_accessory_slots: int = _DEFAULT_MAX_ACCESSORY_SLOTS

	power_points_per_level: int = 15
	max_hp_per_lvl: int = HP_PER_LEVEL
	max_ap_per_lvl: int = 5
	max_hp: int = 20
	current_hp: int = 20
	max_ap: int = 5
	current_ap: int = 5
	hp_formula_version: int = HP_FORMULA_VERSION

	unused_ability_slots: int = 1
	unused_stat_points: int = 10
	unused_power_points: int = 15
	initial_stat_distribution_amount: int = 10
	per_level_stat_distribution_amount: int = 6
	strength: int = 8
	dexterity: int = 8
	constitution: int = 8
	intelligence: int = 8

	level: int = 1
	experience: int = 0
	xp_needed_to_level: int = 100

	abilities: List[PlayerAbility] = field(default_factory=list)
	ability_acquirement_level_amount: int = 4

	id: Optional[str] = None
	npc_id: Optional[str] = None
	character_class: Optional[str] = None
	elements_base: List[str] = field(default_factory=list)
	last_broken_armor: List[str] = field(default_factory=list)
	last_broken_weapon_dropped: Optional[str] = None
	statuses: List[dict] = field(default_factory=list)

	# ── Pickle / save-file compatibility ──────────────────────────────────

	def __setstate__(self, state: dict) -> None:
		"""Restore a Player from a pickled state dict.

		Guarantees forward-compatibility: any field introduced after an older
		save was made will be set to its default so the game never crashes on
		load when new fields are added.
		"""
		# Provide defaults for every field that may be missing from old saves.
		defaults = {
			'_uuid':                            uuid.uuid4().hex,
			'name':                             'Unknown',
			'x': 0, 'y': 0, 'z': 0,
			'inside':                           False,
			'arm_armor':                        None,
			'head_armor':                       None,
			'body_armor':                       None,
			'leg_armor':                        None,
			'equipped_weapon':                  None,
			'accessories':                      [],
			'max_accessory_slots':              _DEFAULT_MAX_ACCESSORY_SLOTS,
			'power_points_per_level':           15,
			'max_hp_per_lvl':                   20,  # old saves: pre-migration value; migrated below
			'max_ap_per_lvl':                   5,
			'max_hp':                           20,
			'current_hp':                       20,
			'max_ap':                           5,
			'current_ap':                       5,
			'hp_formula_version':               1,  # old saves predate the HP formula version flag
			'unused_ability_slots':             1,
			'unused_stat_points':               10,
			'unused_power_points':              15,
			'initial_stat_distribution_amount': 10,
			'per_level_stat_distribution_amount': 6,
			'strength':                         8,
			'dexterity':                        8,
			'constitution':                     8,
			'intelligence':                     8,
			'level':                            1,
			'experience':                       0,
			'xp_needed_to_level':              100,
			'abilities':                        [],
			'ability_acquirement_level_amount': 4,
			'id':                               None,
			'npc_id':                           None,
			'character_class':                  None,
			'elements_base':                    [],
			'last_broken_armor':                [],
			'last_broken_weapon_dropped':       None,
			'statuses':                         [],
		}
		for key, default in defaults.items():
			self.__dict__[key] = state.get(key, default)

		# IMPLEMENTATION_SPEC_leveling.md 1.4: migrate HP for saves made before
		# the flat-35/CON*8 formula. Runs once per character (version flag).
		if int(getattr(self, 'hp_formula_version', 1) or 1) < HP_FORMULA_VERSION:
			lv = max(1, int(getattr(self, 'level', 1) or 1))
			cls = getattr(self, 'character_class', None)
			if not cls:
				cid = getattr(self, 'npc_id', None) or getattr(self, 'id', None)
				cls = (getattr(const, 'CHARACTER_NPC_CLASS_MAP', {}) or {}).get(cid)
			con_per_level = 3 if cls in ('technique', 'spirit') else 1
			con_gained = (lv - 1) * con_per_level
			delta = (lv - 1) * (HP_PER_LEVEL - 20) + con_gained * (HP_PER_CON_ON_LEVEL - 2)
			self.max_hp = int(getattr(self, 'max_hp', 20) or 20) + delta
			if int(getattr(self, 'current_hp', 0) or 0) > 0:
				self.current_hp = min(self.max_hp, int(self.current_hp) + delta)
			self.max_hp_per_lvl = HP_PER_LEVEL
			self.hp_formula_version = HP_FORMULA_VERSION

	# ── Accessory management ───────────────────────────────────────────────

	def equip_accessory(self, player_game, accessory: Any) -> bool:
		"""Equip an accessory into the accessory array if a slot is free.

		Creates an independent copy of the accessory for the equipped slot so
		the inventory instance and the equipped instance never alias each other.
		Returns True on success, False if no slots are available.
		"""
		if accessory is None:
			return False
		if len(self.accessories) >= self.max_accessory_slots:
			return False
		# Use an independent copy so stacked inventory objects and equipped
		# slots never share the same reference.
		from dataclasses import replace as _dc_replace  # noqa: PLC0415
		equipped_copy = _dc_replace(accessory, quantity=1)
		self.accessories.append(equipped_copy)
		if player_game is not None:
			player_game.remove_single_item_unit(accessory)
		return True

	def unequip_accessory(self, player_game, accessory: Any) -> bool:
		"""Remove an equipped accessory and return it to inventory.

		Returns True on success, False if not equipped.
		"""
		if accessory not in self.accessories:
			return False
		self.accessories.remove(accessory)
		if player_game is not None:
			player_game.pick_up_item(accessory)
		return True

	def unequip_weapon(self, player_game) -> bool:
		"""Unequip the current weapon back to inventory.

		Returns True on success, False if no weapon is equipped.
		"""
		if self.equipped_weapon is None:
			return False
		if player_game is not None:
			player_game.pick_up_item(self.equipped_weapon)
		self.equipped_weapon = None
		return True

	def unequip_armor(self, player_game, slot_attr: str) -> bool:
		"""Unequip the armor in `slot_attr` (e.g. 'head_armor') back to inventory.

		Returns True on success, False if that slot is empty.
		"""
		current = getattr(self, slot_attr, None)
		if current is None:
			return False
		if player_game is not None:
			player_game.pick_up_item(current)
		setattr(self, slot_attr, None)
		return True

	def get_accessory_immunities(self) -> set:
		"""Return the union of all status immunities granted by equipped accessories."""
		immunities: set = set()
		for acc in self.accessories:
			for sid in (getattr(acc, 'immunities', None) or []):
				immunities.add(sid)
		return immunities

	def has_accessory_immunity(self, status_id: str) -> bool:
		"""Return True if any equipped accessory grants immunity to status_id."""
		return status_id in self.get_accessory_immunities()

	def get_accessory_resistances(self) -> set:
		"""Return the union of all elemental resistances granted by equipped accessories."""
		resistances: set = set()
		for acc in self.accessories:
			for elem in (getattr(acc, 'resistances', None) or []):
				resistances.add(elem)
		return resistances

	def get_accessory_weaknesses(self) -> set:
		"""Return the union of all elemental weaknesses from equipped accessories."""
		weaknesses: set = set()
		for acc in self.accessories:
			for elem in (getattr(acc, 'weaknesses', None) or []):
				weaknesses.add(elem)
		return weaknesses

	# ── Status methods ─────────────────────────────────────────────────────

	def get_modified_strength(self) -> int:
		modified = self.strength
		modified = status_utils.compute_modified_stat(self, 'strength', modified)
		pieces = [self.head_armor, self.body_armor, self.arm_armor, self.leg_armor, self.equipped_weapon]
		for p in pieces:
			if p is not None:
				modified += p.strength
		for acc in self.accessories:
			modified += getattr(acc, 'strength', 0) or 0
		return max(1, modified)

	def get_modified_dexterity(self) -> int:
		modified = self.dexterity
		modified = status_utils.compute_modified_stat(self, 'dexterity', modified)
		pieces = [self.head_armor, self.body_armor, self.arm_armor, self.leg_armor, self.equipped_weapon]
		for p in pieces:
			if p is not None:
				modified += p.dexterity
		for acc in self.accessories:
			modified += getattr(acc, 'dexterity', 0) or 0
		return max(1, modified)

	def get_modified_intelligence(self) -> int:
		modified = self.intelligence
		modified = status_utils.compute_modified_stat(self, 'intelligence', modified)
		pieces = [self.head_armor, self.body_armor, self.arm_armor, self.leg_armor, self.equipped_weapon]
		for p in pieces:
			if p is not None:
				modified += p.intelligence
		for acc in self.accessories:
			modified += getattr(acc, 'intelligence', 0) or 0
		return max(1, modified)

	def get_modified_constitution(self) -> int:
		modified = self.constitution
		modified = status_utils.compute_modified_stat(self, 'constitution', modified)
		pieces = [self.head_armor, self.body_armor, self.arm_armor, self.leg_armor, self.equipped_weapon]
		for p in pieces:
			if p is not None:
				modified += p.constitution
		for acc in self.accessories:
			modified += getattr(acc, 'constitution', 0) or 0
		return max(1, modified)

	def add_status(self, descriptor: dict, source: Optional[object] = None) -> None:
		"""Apply a status descriptor.

		Accessory immunities block the status entirely.
		Accessory resistances halve the duration (min 1).
		Accessory weaknesses extend the duration by 50%.
		Mirrors the logic in RandomHostile.add_status.
		"""
		if not descriptor or not isinstance(descriptor, dict):
			return
		sid = descriptor.get('id', '')
		if not sid:
			return

		# 1. Immunity — accessory blocks the status entirely
		if self.has_accessory_immunity(sid):
			return

		s = dict(descriptor)
		duration = int(s.get('duration', 1))

		# 2. Resistance — halve duration (min 1)
		if sid in self.get_accessory_resistances():
			if duration > 1:
				duration = max(1, duration // 2)

		# 3. Weakness — extend duration by 50% (permanent statuses are never extended)
		if sid in self.get_accessory_weaknesses():
			if duration != -1:
				duration = int(duration * 1.5)

		s['turns_remaining'] = duration
		if source is not None:
			s['source'] = getattr(source, 'id', None) or getattr(source, 'name', None)
		self.statuses.append(s)

	def remove_status_by_id(self, status_id: str) -> int:
		"""Remove statuses matching id. Returns number removed."""
		if not status_id:
			return 0
		before = len(self.statuses)
		self.statuses = [st for st in self.statuses if st.get('id') != status_id]
		return before - len(self.statuses)

	def cure_all_debuffs(self) -> int:
		"""Remove common debuff ids and return count removed."""
		debuff_ids = const.HARMFUL_STATUS_EFFECTS
		#debuff_ids = {"elemental_debuff", "attack_debuff", "defense_debuff", "intelligence_debuff", "continuous_damage"}
		before = len(self.statuses)
		self.statuses = [st for st in self.statuses if st.get('id') not in debuff_ids]
		return before - len(self.statuses)
	
	def cure_elemental_and_stat_debuffs(self) -> int:
		"""removes all debuffs with status key containing 'debuff'
		"""
		before = len(self.statuses)
		self.statuses = [st for st in self.statuses if 'debuff' not in st.get('id')]
		return before - len(self.statuses)

	def clear_statuses_end_of_combat(self) -> int:
		"""Remove all statuses at the end of combat except petrify and
		continuous_damage. Petrify must be cured explicitly, and
		continuous_damage retains its remaining duration/stacks across
		combats rather than being wiped.
		"""
		before = len(self.statuses)
		self.statuses = [
			st for st in self.statuses
			if st.get('id') in ('petrify', 'continuous_damage')
		]
		return before - len(self.statuses)

	def tick_statuses(self) -> None:
		"""Decrement turns_remaining and drop expired statuses.
		Permanent statuses have turns_remaining == -1 and are preserved until explicitly removed.
		"""
		new = []
		for st in self.statuses:
			# treat explicit -1 as permanent: keep without decrementing
			tr_raw = st.get('turns_remaining', st.get('duration',1))
			
			tr = int(tr_raw)
			
			if tr == -1:
				# permanent status: retain as-is
				new.append(st)
			else:
				tr -=1
				if tr >0:
					st['turns_remaining'] = tr
					new.append(st)
		# replace statuses with surviving list
		self.statuses = new

	##### COMBAT METHODS #######

	def is_alive(self) -> bool:
		return self.current_hp >0

	def is_incapacitated(self) -> bool:
		"""Return True if the player is dead or petrified.

		Used to exclude a party member from combat reward distribution: an
		incapacitated player neither counts toward the XP split nor receives a
		share of it. Mirrors the petrify check used by the combat simulator's
     annihilation logic.
		"""
		if not self.is_alive():
			return True
		return any(
			(s.get('id') == 'petrify')
			for s in (self.statuses or [])
			if isinstance(s, dict)
		)

	def take_damage(self, amount: int, attacker: Optional[object] = None, elements: Optional[List[str]] = None, physical: bool = False) -> int:
		"""Reduce HP by amount and return actual damage taken.

		Elemental interactions (immunity, weakness, resistance) from equipped
		accessories are applied before status-based modifiers, mirroring
		RandomHostile.take_damage.
		"""
		last_broken_weapon_dropped: Optional[str] = None
		self.last_damage_immune = False
		if amount <= 0:
			return 0

		elements = status_utils.with_physical_stack(elements, physical)

		armor_block = 0
		if physical:
			pieces = [self.head_armor, self.body_armor, self.arm_armor, self.leg_armor]
			for a in pieces:
				if a is not None and not a.is_broken():
					armor_block += a.defense
		net = max(0, amount - armor_block)

		if elements:
			mult = status_utils.elemental_multiplier(
				elements,
				self.get_accessory_immunities(),
				self.get_accessory_weaknesses(),
				self.get_accessory_resistances(),
			)
			if mult == 0.0:
				self.last_damage_immune = True
			net = int(net * mult)

		net = status_utils.compute_incoming_damage(self, net, elements, is_physical=physical)
		if physical and 'sleep' in [s.get('id') for s in self.statuses]:
			self.remove_status_by_id('sleep')
		self.current_hp = max(0, self.current_hp - net)
		return net

	def attack(self, target: Optional[object] = None) -> dict:
		if not self.equipped_weapon:
			base_damage = max(1, int(self.get_modified_strength())) + self.level
			weapon_name = 'Unarmed'
			crit_chance = 0.0
		else:
			weapon_name = self.equipped_weapon.name
			base_damage = int(self.equipped_weapon.expected_damage()) + self.get_modified_strength()
			crit_chance = self.equipped_weapon.critical_chance

		# Accessories may add flat damage and crit bonuses
		for acc in self.accessories:
			base_damage += getattr(acc, 'damage_bonus', 0) or 0
			crit_chance += getattr(acc, 'crit_bonus', 0) or 0

		hit_chance = status_utils.physical_hit_chance(self, target)
		hit_roll = random.random() * 100

		result = {
			'attacker_id': self.id,
			'attacker_name': self.name,
			'weapon': weapon_name,
			'damage': 0,
			'hit': False,
		}

		if hit_roll > hit_chance:
			return result

		damage = max(0, int(random.normalvariate(base_damage, max(1, base_damage * 0.2))))
		elems = status_utils.collect_attack_elements(self)
		damage = status_utils.compute_outgoing_damage(self, damage, elems, is_physical=True)

		if crit_chance and (random.random() * 100) < crit_chance:
			damage *= 2
			result['crit'] = True
		else:
			result['crit'] = False

		result['damage'] = damage
		result['hit'] = True

		if target is not None:
			applied = target.take_damage(damage, attacker=self, elements=elems if elems else None, physical=True)
			result['applied'] = applied
			if target.last_broken_armor:
				result['armor_broken'] = list(target.last_broken_armor)

		return result

	# ── Ability / item use ─────────────────────────────────────────────────

	def heal(self, amount: int) -> int:
		if amount <= 0:
			return 0
		old = self.current_hp
		self.current_hp = min(self.max_hp, self.current_hp + amount)
		return self.current_hp - old

	def use_ability(self, ability: PlayerAbility, target: Optional[object] = None, targets: List[Optional[object]] = None) -> Dict[str, Any]:
		from .player_ability import PlayerAbility
		if not ability:
			return {'used': False, 'error': 'no_ability'}
		if not isinstance(ability, PlayerAbility):
			return {'used': False, 'error': 'invalid_ability_type'}
		cost = ability.ap_cost
		if cost and not self.spend_ap(cost):
			return {'used': False, 'error': 'insufficient_ap'}
		results: List[Dict[str, Any]] = []
		for t in (targets or []):
			pr = ((len(targets) - 1) * 0.1) if targets else 0.0
			r = ability.apply(target=t, owner=self, percent_reduction=pr)
			if isinstance(r, dict):
				r['ability_id'] = ability.id
				r['ability_name'] = ability.name
			results.append(r)
		return {'used': True, 'ability_id': ability.id, 'results': results}

	def use_item(self, inv_idx: int, player_game, target=None) -> dict:
		if inv_idx < 0 or inv_idx >= len(player_game.inventory):
			return {'used': False, 'note': f'{inv_idx} of {len(player_game.inventory)}', 'error': 'invalid_index'}
		item = player_game.inventory[inv_idx]
		if not isinstance(item, UtilityItem):
			return {'used': False, 'note': f'item type: {item.__class__.__name__}', 'error': 'not_utility'}
		target = self if target is None else target
		res = item.apply(target)
		player_game.remove_single_item_unit(item)
		return res

	# ── AP management ──────────────────────────────────────────────────────

	def restore_ap(self, amount: int) -> int:
		if amount <= 0:
			return 0
		old = self.current_ap
		self.current_ap = min(self.max_ap, self.current_ap + amount)
		return self.current_ap - old

	def spend_ap(self, amount: int) -> bool:
		amt = int(amount)
		if amt <= 0:
			return True
		if self.current_ap < amt:
			return False
		self.current_ap = max(0, self.current_ap - amt)
		return True

	# ── Equipment management ───────────────────────────────────────────────

	def equip_weapon(self, player_game, weapon: Optional[Weapon]) -> bool:
		if not isinstance(weapon, Weapon):
			return False
		if self.equipped_weapon is not None:
			player_game.pick_up_item(self.equipped_weapon)
		self.equipped_weapon = weapon
		if weapon in player_game.inventory:
			player_game.remove_single_item_unit(weapon)
		return True

	def equip_armor(self, player_game, armor: Optional[Armor]) -> bool:
		if armor is None or not isinstance(armor, Armor):
			return False
		raw_slot = armor.slot
		slot_key = None
		from enum import Enum
		if raw_slot.name:
			slot_name = raw_slot.value
			slot_key = const.ARMOR_TYPES[slot_name]
		if slot_key is None:
			return False
		attr_name = f"{slot_key}_armor"
		current_armor = getattr(self, attr_name, None)
		if current_armor is not None:
			player_game.pick_up_item(current_armor)
		setattr(self, attr_name, armor)
		if armor in player_game.inventory:
			player_game.remove_single_item_unit(armor)
		return True

	# ── Level up / stat management ─────────────────────────────────────────

	def get_required_experience_to_level(self) -> int:
		max_experience_required_to_level = 20000
		scaling_factor = min(self.level / 60, 1.0)
		required_xp = int(self.xp_needed_to_level + (max_experience_required_to_level - self.xp_needed_to_level) * scaling_factor)
		return required_xp

	def gain_experience(self, amount: int) -> int:
		if amount is None or amount <= 0:
			return 0
		self.experience += int(amount)
		levels_gained = 0
		while self.experience >= self.get_required_experience_to_level():
			self.experience -= self.get_required_experience_to_level()
			self.level += 1
			levels_gained += 1
		return levels_gained

	def check_level_up_awards(self) -> Tuple[bool, int, int]:
		has_new_ability = False
		stat_points = 0
		if self.level % self.ability_acquirement_level_amount == 0:
			self.unused_ability_slots += 1
			has_new_ability = True
		elif self.unused_ability_slots > 0:
			has_new_ability = True
		self.unused_stat_points += 4
		self.allocate_stats(1, 1, 1, 1)
		self.max_ap += self.max_ap_per_lvl
		self.max_hp += self.max_hp_per_lvl
		# Level-up now restores only what the level added (tally), not a full
		# heal/restore. A fallen character (current_hp <= 0) stays down.
		self.current_ap += self.max_ap_per_lvl
		if self.current_hp > 0:
			self.current_hp += self.max_hp_per_lvl
		self.unused_stat_points += self.per_level_stat_distribution_amount
		self.unused_power_points += self.power_points_per_level
		# Class-assigned characters auto-distribute all gained points so they
		# follow their predefined growth profile without manual upgrades.
		if getattr(self, 'character_class', None):
			self.auto_allocate_level_points()
		self.current_hp = min(self.current_hp, self.max_hp)
		self.current_ap = min(self.current_ap, self.max_ap)
		return has_new_ability, self.per_level_stat_distribution_amount, self.power_points_per_level

	def auto_allocate_level_points(self) -> None:
		"""Spend all unused stat/power points using the class curve
		(IMPLEMENTATION_SPEC_class_growth_elements.md Part 1): the per-level
		stat points go entirely to the class's primary/secondary stats in a
		fixed ratio (4:2, or 6:0 for magic), not round-robin across all four.
		"""
		char_class = str(getattr(self, 'character_class', '') or '').lower()
		split = CLASS_STAT_SPLIT.get(char_class)
		if not split:
			return  # classless (custom character) keeps manual allocation

		pts = int(getattr(self, 'unused_stat_points', 0) or 0)
		if pts > 0:
			total = sum(split.values())
			inc = {k: pts * v // total for k, v in split.items()}
			# remainder goes to the primary stat (highest split value)
			primary = max(split, key=split.get)
			inc[primary] = inc.get(primary, 0) + (pts - sum(inc.values()))
			self.allocate_stats(
				inc.get('strength', 0),
				inc.get('dexterity', 0),
				inc.get('constitution', 0),
				inc.get('intelligence', 0),
				use_stat_points=True,
			)

		ppts = int(getattr(self, 'unused_power_points', 0) or 0)
		if ppts > 0:
			ratio = CLASS_HP_RATIO.get(char_class, 0.50)
			hp_pts = max(0, min(ppts, int(round(ppts * ratio))))
			ap_pts = max(0, ppts - hp_pts)
			self.apply_power_point_allocation(hp_pts, ap_pts)

	def upgrade_stats(self, str_inc: int = 0, dex_inc: int = 0, con_inc: int = 0, int_inc: int = 0, hp_points: int = 0, ap_points: int = 0) -> None:
		self.allocate_stats(str_inc, dex_inc, con_inc, int_inc)
		self.apply_power_point_allocation(hp_points, ap_points)

	def allocate_stats(self, str_inc: int = 0, dex_inc: int = 0, con_inc: int = 0, int_inc: int = 0, use_stat_points: bool = True, hp_per_con: int = HP_PER_CON_ON_LEVEL) -> None:
		if str_inc:
			self.strength += int(str_inc)
		if dex_inc:
			self.dexterity += int(dex_inc)
		if con_inc:
			self.constitution += int(con_inc)
			hp_inc = int(con_inc) * int(hp_per_con)
			self.max_hp += hp_inc
			if self.current_hp > 0:  # a level-up/stat gain is not a revive
				self.current_hp += hp_inc
		if int_inc:
			self.intelligence += int(int_inc)
		if use_stat_points:
			self.unused_stat_points -= max(0, (str_inc + dex_inc + con_inc + int_inc))

	def apply_power_point_allocation(self, hp_points: int = 0, ap_points: int = 0) -> None:
		if hp_points:
			self.max_hp += int(hp_points)
		if ap_points:
			self.max_ap += int(ap_points)
		if self.current_hp > 0:  # a level-up/stat gain is not a revive
			self.current_hp += int(hp_points)
		self.current_ap += int(ap_points)
		self.unused_power_points -= max(0, (hp_points + ap_points))

	def learn_ability(self, ability: PlayerAbility) -> bool:
		if not ability:
			return False
		if ability in self.abilities:
			return False

		# Enforce class + element learn gate when a class assignment exists.
		from game.objects.player_ability import can_learn
		if not can_learn(self, ability, check_stats=False):
			return False

		self.unused_ability_slots = max(0, self.unused_ability_slots - 1)
		self.abilities.append(ability)
		return True

	def populate_from_json(self, data: dict) -> None:
		if not data or not isinstance(data, dict):
			return
		ignored_fields = ['arm_armor', 'head_armor', 'body_armor', 'leg_armor', 'equipped_weapon', 'abilities', 'accessories']
		for key, value in data.items():
			if key not in ignored_fields:
				if hasattr(self, key):
					setattr(self, key, value)

	# ── Deprecated ────────────────────────────────────────────────────────


def apply_class_curve(p, cls: str, target_level: int) -> None:
	"""Reset p's stats/HP/AP to the class curve at target_level.

	IMPLEMENTATION_SPEC_class_growth_elements.md Part 1c. Equipment and
	abilities are untouched. Used by both generation and recruits so every
	class-assigned character follows the same growth rule.
	"""
	cls = str(cls or '').lower()
	if cls not in CLASS_LEVEL1_STATS:
		return
	p.character_class = cls
	p.level = 1
	p.strength, p.dexterity, p.constitution, p.intelligence = CLASS_LEVEL1_STATS[cls]
	# Level-1 HP/AP: base 20 + creation-rate CON bonus, then the level-1
	# power points split by the class's hp_ratio.
	p.max_hp = 20 + (p.constitution - 8) * HP_PER_CON_AT_CREATION
	p.max_ap = 5
	pp = int(p.power_points_per_level)
	hp = int(round(pp * CLASS_HP_RATIO[cls]))
	p.max_hp += hp
	p.max_ap += pp - hp
	p.unused_stat_points = 0
	p.unused_power_points = 0
	p.unused_ability_slots = 0
	p.current_hp, p.current_ap = p.max_hp, p.max_ap
	for lvl in range(2, int(target_level) + 1):
		p.level = lvl
		p.check_level_up_awards()   # +1 all, +6 by class split, +15 power points by hp_ratio
	p.current_hp, p.current_ap = p.max_hp, p.max_ap  # creation/recruitment joins at full, not a level-up


def assign_character_elements(p, char_id=None, overwrite=False) -> None:
	"""Set p.elements_base from CHARACTER_NPC_ELEMENT_MAP. Never guesses from class."""
	if getattr(p, 'elements_base', None) and not overwrite:
		return
	emap = getattr(const, 'CHARACTER_NPC_ELEMENT_MAP', {}) or {}
	for key in (char_id, getattr(p, 'npc_id', None), getattr(p, 'id', None)):
		if key and key in emap:
			p.elements_base = list(emap[key])
			return
	p.elements_base = list(getattr(p, 'elements_base', None) or [])


def generate_player_from_attainable_character_seed(seed) -> Player:
	if not isinstance(seed, dict):
		return None
	name = seed.get('name') or seed.get('id') or 'Unnamed'
	p = Player(name)
	p.populate_from_json(seed)
	char_id = seed.get('npc_id') or seed.get('id')
	if not getattr(p, 'character_class', None):
		p.character_class = (getattr(const, 'CHARACTER_NPC_CLASS_MAP', {}) or {}).get(char_id)
	if not getattr(p, 'npc_id', None) and seed.get('npc_id'):
		p.npc_id = seed.get('npc_id')
	assign_character_elements(p, char_id=char_id)
	# IMPLEMENTATION_SPEC_class_growth_elements.md 1.3e: recruits follow the
	# class curve rather than their hand-written seed stats. This overrides
	# strength/dexterity/constitution/intelligence/max_hp/max_ap/current_*.
	cls = getattr(p, 'character_class', None)
	if cls and cls in CLASS_LEVEL1_STATS:
		seed_level = int(seed.get('level') or p.level or 1)
		apply_class_curve(p, cls, seed_level)
		p.unused_ability_slots = int(seed.get('unused_ability_slots') or 0)
	from game.objects.item import instantiate_item_from_id
	armor_keys = ['arm_armor', 'head_armor', 'body_armor', 'leg_armor']
	for key in armor_keys:
		val = seed.get(key)
		if val:
			itm = instantiate_item_from_id(val)
			if itm is not None:
				setattr(p, key, itm)
	weap_ref = seed.get('equipped_weapon') or seed.get('weapon')
	if weap_ref:
		w = instantiate_item_from_id(weap_ref)
		if w is not None:
			p.equipped_weapon = w
	abilities = seed.get('abilities') or []
	if abilities and isinstance(abilities, (list, str)):
		from game.objects.player_ability import _instantiate_from_seed
		ability_seeds = const.PLAYER_ABILITY_SEEDS
		seed_map = {s.get('id'): s for s in ability_seeds}
		for aid in abilities:
			if not aid:
				continue
			aseed = seed_map.get(aid)
			if aseed:
				ability_obj = _instantiate_from_seed(aseed)
				p.abilities.append(ability_obj)
	return p


