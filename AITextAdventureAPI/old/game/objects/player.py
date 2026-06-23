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

ItemType = Union[Item, Armor, Weapon, UtilityItem, SpecialItem]

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
	x: int =0
	y: int =0
	z: int =0
	inside: bool = False

	arm_armor: Optional[Armor] = None
	head_armor: Optional[Armor] = None
	body_armor: Optional[Armor] = None
	leg_armor: Optional[Armor] = None
	equipped_weapon: Optional[Weapon] = None

	power_points_per_level: int =15 # these are distributed between max_hp and max_ap on level up and at start
	max_hp_per_lvl: int =20
	max_ap_per_lvl: int =5
	max_hp: int =20
	current_hp: int =20
	max_ap: int =5
	current_ap: int =5
	
	unused_ability_slots: int =1
	unused_stat_points: int =10 
	unused_power_points: int =15
	initial_stat_distribution_amount: int =10 # points to distribute at level1
	per_level_stat_distribution_amount: int =6 # points to distribute at each level up
	strength: int =8 # strength affects melee damage and melee weapon/unarmed damage
	dexterity: int =8 # dexterity affects ranged weapon accuracy and evasion
	constitution: int =8 # constitution buffs automatic max_hp gain per level before power point distribution
	intelligence: int =8 # intelligence buffs automatic max_ap gain per level before power point distribution

	level: int =1
	experience: int =0 # current player experience - resets to 0 + remainder on level up - player level to enemy level controls xp earned ratio
	xp_needed_to_level: int =100 # experience needed to reach next level - scales with level

	abilities: List[PlayerAbility] = field(default_factory=list)
	ability_acquirement_level_amount: int =4 # every N levels, player gets a new ability

	id: Optional[str] = None
	npc_id: Optional[str] = None  # link to NPC definition if applicable
	# transient tracking for combat messages
	last_broken_armor: List[str] = field(default_factory=list)

	last_broken_weapon_dropped: Optional[str] = None

	# Status effects currently applied to this entity.
	# Each status is a dict: {id, name, type, duration, magnitude, elements, turns_remaining, source}
	statuses: List[dict] = field(default_factory=list)


	##### POSITION METHODS #######

	# def move(self, dx: int, dy: int, dz: int =0) -> None:
	# 	self.x += dx
	# 	self.y += dy
	# 	self.z += dz
	
	##### STATUS METHODS #######

	def get_modified_strength (self) -> int:
		"""compute effective strength using status modifiers, armor and weapon"""
		modified = self.strength
		modified = status_utils.compute_modified_stat(self, 'strength', modified)

		# add strength buff from all armor annd weapon pieces
		pieces = [self.head_armor, self.body_armor, self.arm_armor, self.leg_armor, self.equipped_weapon]
		for p in pieces:
			if p is not None:
				modified += p.strength

		return max(1, modified)

	def get_modified_dexterity (self) -> int:
		"""compute effective dexterity using status modifiers, armor and weapon"""
		modified = self.dexterity
		modified = status_utils.compute_modified_stat(self, 'dexterity', modified)

		# add dexterity buff from all armor annd weapon pieces
		pieces = [self.head_armor, self.body_armor, self.arm_armor, self.leg_armor, self.equipped_weapon]
		for p in pieces:
			if p is not None:
				modified += p.dexterity

		return max(1, modified)

	def get_modified_intelligence (self) -> int:
		"""compute effective intelligence using status modifiers, armor and weapon"""
		modified = self.intelligence
		modified = status_utils.compute_modified_stat(self, 'intelligence', modified)

		# add intelligence buff from all armor annd weapon pieces
		pieces = [self.head_armor, self.body_armor, self.arm_armor, self.leg_armor, self.equipped_weapon]
		for p in pieces:
			if p is not None:
				modified += p.intelligence
		return max(1, modified)

	def get_modified_constitution(self) -> int:
		"""compute effective constitution using status modifiers, armor and weapon"""
		modified = self.constitution
		modified = status_utils.compute_modified_stat(self, 'constitution', modified)

		# add consitution buff from all armor annd weapon pieces
		pieces = [self.head_armor, self.body_armor, self.arm_armor, self.leg_armor, self.equipped_weapon]
		for p in pieces:
			if p is not None:
				modified += p.constitution

		return max(1, modified)

	def add_status(self, descriptor: dict, source: Optional[object] = None) -> None:
		"""Apply a status descriptor to the player. Descriptor is copied and
		initialised with `turns_remaining` from `duration`.
		"""
		if not descriptor or not isinstance(descriptor, dict):
			return
		s = dict(descriptor)
		s['turns_remaining'] = int(s.get('duration',1))
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

	def take_damage(self, amount: int, attacker: Optional[object] = None, elements: Optional[List[str]] = None, physical: bool =False) -> int:
		"""Reduce HP by amount and return actual damage taken."""
		# reset transient
		#self.last_broken_armor = []
		# self.last_broken_armor_stored = []
		# self.last_broken_armor_dropped = []
		#self.last_broken_weapon_stored = None
		last_broken_weapon_dropped: Optional[str] = None
		if amount <=0:
			return 0
		# simple armor reduction: sum defense of worn armor
		armor_block =0
		pieces = [self.head_armor, self.body_armor, self.arm_armor, self.leg_armor]
		for a in pieces:
			if a is not None and not a.is_broken:
				armor_block += a.defense
		net = max(0, amount - armor_block)
		# apply incoming status modifiers (defense buffs/debuffs)
		net = status_utils.compute_incoming_damage(self, net, elements, is_physical = physical)
		
		if physical == True and 'sleep' in [s.get('id') for s in self.statuses]:
			# waking up on damage
			self.remove_status_by_id('sleep')
		# apply damage to HP (no durability changes for player-worn gear)
		self.current_hp = max(0, self.current_hp - net)
		return net

	def attack(self, target: Optional[object] = None) -> dict:
		"""Perform a player attack against a target. Uses weapon/strength for damage
		and dexterity for accuracy. Returns result dict similar to RandomHostile.attack.
		"""
		if not self.equipped_weapon:
			base_damage = max(1, int(self.get_modified_strength()))  + self.level
			weapon_name = 'Unarmed'
			crit_chance =0.0
		else:
			weapon_name = self.equipped_weapon.name
			# include player's strength as a flat bonus to weapon damage
			base_damage = int(self.equipped_weapon.expected_damage()) + (self.get_modified_strength())
			crit_chance = self.equipped_weapon.critical_chance

		attacker_acc =50 + (self.level *2) + (self.get_modified_dexterity() *2)
		target_evasion =10
		if target is not None:
			target_evasion =10 + (target.get_modified_dexterity() *2)
		hit_chance = max(5, min(95,50 + (attacker_acc - target_evasion)))
		hit_roll = random.random() *100

		result = {
			'attacker_id': self.id,
			'attacker_name': self.name,
			'weapon': weapon_name,
			'damage':0,
			'hit': False,
		}

		if hit_roll > hit_chance:
			# miss
			return result

		# hit -> compute damage with variance
		damage = max(0, int(random.normalvariate(base_damage, max(1, base_damage *0.2))))
		
		# apply attacker-side status modifiers		
		# collect elements from weapon/ability and attacker statuses
		elems = status_utils.collect_attack_elements(self)
		damage = status_utils.compute_outgoing_damage(self, damage, elems)

		# crit
		if crit_chance and (random.random() *100) < crit_chance:
			damage *=2
			result['crit'] = True
		else:
			result['crit'] = False

		result['damage'] = damage
		result['hit'] = True

		if target is not None:
			# pass elemental list to target so incoming-side modifiers (resistances/debuffs) apply

			applied = target.take_damage(damage, attacker=self, elements=elems if elems else None, physical=True)
			result['applied'] = applied

			# if target reported broken armor (transient), include in result
			if target.last_broken_armor:
				result['armor_broken'] = list(target.last_broken_armor)

		return result	

	##### ABILITY AND ITEM USE MANAGEMENT / combat and noncombat #######

	def heal(self, amount: int) -> int:
		if amount <=0:
			return 0
		old = self.current_hp
		self.current_hp = min(self.max_hp, self.current_hp + amount)
		return self.current_hp - old

	#note to later add mutitarget/aoe support
	def use_ability(self, ability: PlayerAbility, target: Optional[object] = None, targets: List[Optional[object]] = None) -> Dict[str, Any]:
		from .player_ability import PlayerAbility
		#target can be RandomHostile or Player
		#targets can be a list of RandomHostile or Player
		"""Use a PlayerAbility (or ability id) against a target. Returns the ability's apply() result or an error dict."""
		if not ability:
			return {'used': False, 'error': 'no_ability'}
		# resolve ability instance

		if not isinstance(ability, PlayerAbility):
			return {'used': False, 'error': 'invalid_ability_type'}

		cost = ability.ap_cost

		if cost and not self.spend_ap(cost):
			return {'used': False, 'error': 'insufficient_ap'}
		# apply ability to single target or multiple targets
		results: List[Dict[str, Any]] = []
		# support multi-target list
		for t in (targets or []):
			# percent_reduction scales with number of targets (simple balancing)
			pr = ((len(targets) - 1) *0.1) if targets else 0.0
			r = ability.apply(target=t, owner=self, percent_reduction=pr)
			if isinstance(r, dict):
				r['ability_id'] = ability.id
				r['ability_name'] = ability.name
			results.append(r)

		return {'used': True, 'ability_id': ability.id, 'results': results}

	def use_item(self, inv_idx: int, player_game, target = None) -> dict:
		"""Use a utility item from inventory at index `inv_idx`.

		Removes item if uses are depleted. Returns result dict from the item's `apply` method.
		If index invalid or item not usable, returns {'used': False, 'error': '...'}.
		"""
		if inv_idx <0 or inv_idx >= len(player_game.inventory):
			return {'used': False, 'note': f'{inv_idx} of {len(player_game.inventory)}', 'error': 'invalid_index'}
		item = player_game.inventory[inv_idx]
		if not isinstance(item, UtilityItem):
			return {'used': False, 'note': f'item type: {item.__class__.__name__}', 'error': 'not_utility'}
		target = self if target is None else target

		res = item.apply(target)
		player_game.remove_single_item_unit(item)

		return res

	######## ACTION POINT MANAGEMENT #######

	def restore_ap(self, amount: int) -> int:
		if amount <=0:
			return 0
		old = self.current_ap
		self.current_ap = min(self.max_ap, self.current_ap + amount)
		return self.current_ap - old

	def spend_ap(self, amount: int) -> bool:
		"""Attempt to spend `amount` AP. Returns True if spent, False if insufficient AP.

		This is the safe API callers (UI/game systems) should use instead of
		directly manipulating `current_ap`.
		"""
		amt = int(amount)
		if amt <=0:
			return True
		if self.current_ap < amt:
			return False
		self.current_ap = max(0, self.current_ap - amt)
		return True

	####### EQUIPMENT MANAGEMENT ####

	def equip_weapon(self, player_game, weapon: Optional[Weapon]) -> bool:
		"""Equip the given weapon. Returns True if successful, False otherwise.

		This implementation requires the caller to pass a proper `Weapon` instance.
		If another type is passed, the call fails fast.
		"""
		# require a Weapon instance
		if not isinstance(weapon, Weapon):
			return False

		# if currently equipped, move it to inventory (allow +1 slot to unequip)
		if self.equipped_weapon is not None:
			player_game.pick_up_item(self.equipped_weapon)

		# equip new weapon and remove from inventory if present
		self.equipped_weapon = weapon
		if weapon in player_game.inventory:
			player_game.remove_single_item_unit(weapon)
		return True

	def equip_armor(self, player_game, armor: Optional[Armor]) -> bool:
		"""Equip the given armor piece. Returns True if successful, False otherwise."""
		if armor is None or not isinstance(armor, Armor):
			return False
		# normalize slot: accept ArmorType enum or string-like values
		raw_slot = armor.slot
		slot_key = None

		from enum import Enum
		# if it's an enum (ArmorType), map to name
		if raw_slot.name:
			slot_name = raw_slot.value
			slot_key = const.ARMOR_TYPES[slot_name]

		if slot_key is None:
			return False

		attr_name = f"{slot_key}_armor"
		#input (f"Equipping {armor.name} to slot {slot_key} (attribute: {attr_name})")
		# if currently equipped move equipped item to inventory (respect capacity)
		current_armor = getattr(self, attr_name, None)
		if current_armor is not None:
			player_game.pick_up_item(current_armor)
			
		# equip
		setattr(self, attr_name, armor)
		# after equipping, remove from inventory if present
		if armor in player_game.inventory:
			player_game.remove_single_item_unit(armor)
		return True

	#### LEVEL UP AND STAT MANAGEMENT ####

	def get_required_experience_to_level(self) -> int:
		"""
			NEED TO HAVE REQUIRED EXPERIENCE SCALE BASED ON LEVEL
			SCALING SHOULD BE PROGRESSIVE UNTIL LEVEL 60 WHERE IT FLATTENS OUT
			USE self.xp_needed_to_level AS BASELINE
		"""
		max_experience_reqquired_to_level = 20000
		scaling_factor = min(self.level / 60, 1.0)
		required_xp = int(self.xp_needed_to_level + (max_experience_reqquired_to_level - self.xp_needed_to_level) * scaling_factor)
		# exmple result for level 15  = 3333 
		# example result for level 55  = 18333
		return required_xp


	def gain_experience(self, amount: int) -> int:
		"""Add experience to the player and handle level up increments.

		Returns the number of levels gained (0 if none).
		"""
		if amount is None:
			return 0
		if amount <=0:
			return 0
		self.experience += int(amount)
		levels_gained =0
		# simple fixed threshold leveling; unspent experience carries over
		while self.experience >= self.get_required_experience_to_level():
			self.experience -= self.get_required_experience_to_level()
			self.level +=1
			levels_gained +=1

		return levels_gained

	def check_level_up_awards(self) -> Tuple[bool, int, int]:
		"""Check if the player has new abilities to learn and how many stat points they can distribute.

		Returns a tuple (has_new_ability: bool, stat_points: int).
		"""
		has_new_ability = False
		stat_points = 0
		if self.level % self.ability_acquirement_level_amount == 0:
			self.unused_ability_slots += 1
			has_new_ability = True
		elif self.unused_ability_slots >0:
			has_new_ability = True

		self.unused_stat_points += 4
		self.allocate_stats(1, 1, 1, 1)
		self.max_ap += self.max_ap_per_lvl
		self.max_hp += self.max_hp_per_lvl
		self.unused_stat_points += self.per_level_stat_distribution_amount

		self.unused_power_points += self.power_points_per_level
		self.heal(self.max_hp)
		self.restore_ap(self.max_ap)

		return has_new_ability, self.per_level_stat_distribution_amount, self.power_points_per_level



	def upgrade_stats(self, str_inc: int =0, dex_inc: int =0, con_inc: int =0, int_inc: int =0, hp_points: int = 0, ap_points: int = 0) -> None:
		"""Apply stat and power point increases outside of level up context."""
		self.allocate_stats(str_inc, dex_inc, con_inc, int_inc)
		self.apply_power_point_allocation(hp_points, ap_points)

	def allocate_stats(self, str_inc: int =0, dex_inc: int =0, con_inc: int =0, int_inc: int =0, use_stat_points: bool = True) -> None:
		"""Apply stat increases to the player."""
		if str_inc:
			self.strength += int(str_inc)
		if dex_inc:
			self.dexterity += int(dex_inc)
		if con_inc:
			self.constitution += int(con_inc)
			hp_inc =  int(con_inc) * 2
			self.max_hp += hp_inc  # each constitution point adds 2 max HP
			self.current_hp  += hp_inc
		if int_inc:
			self.intelligence += int(int_inc)

		if use_stat_points:
			self.unused_stat_points -= max(0, (str_inc + dex_inc + con_inc + int_inc))

	def apply_power_point_allocation(self, hp_points: int =0, ap_points: int =0) -> None:
		"""Apply allocated power points to max HP and AP and set current to max."""
		if hp_points:
			self.max_hp += int(hp_points)
		if ap_points:
			self.max_ap += int(ap_points)
		# set current to new maxima
		self.current_hp += int(hp_points)
		self.current_ap += int(ap_points)
		self.unused_power_points -= max(0, (hp_points + ap_points))

	def learn_ability(self, ability: PlayerAbility) -> bool:
		"""Add a new ability to the player's known abilities by id. Returns True if learned, False if already known."""
		if not ability:
			return False

		if ability in self.abilities:
			return False
		self.unused_ability_slots = max(0, self.unused_ability_slots -1)
		self.abilities.append(ability)
		return

	def populate_from_json(self, data: dict) -> None:
		"""Populate player fields from a JSON-like dict."""
		if not data or not isinstance(data, dict):
			return
		ignored_fields = ['arm_armor', 'head_armor', 'body_armor', 'leg_armor', 'equipped_weapon', 'abilities']
		for key, value in data.items():
			if key not in ignored_fields:
				if hasattr(self, key):
					setattr(self, key, value)



	######## TO BE DEPRECATED
	def level_up(self, str_inc: int =0, dex_inc: int =0, con_inc: int =0, int_inc: int =0, hp_points: int =0, ap_points: int =0, selected_ability: Optional[str] = None) -> None:
		"""Apply level up increases to stats and power points.
		Parameters correspond to increases to apply.
		"""
		self.max_ap += int_inc * 2
		self.max_hp += con_inc * 2
		self.allocate_stats(str_inc, dex_inc, con_inc, int_inc)
		self.apply_power_point_allocation(hp_points, ap_points)
		self.heal(self.max_hp)
		self.restore_ap(self.max_ap)
		
		# add selected ability if provided and not already known
		if selected_ability:
			if selected_ability not in self.abilities:
				self.abilities.append(selected_ability)

def generate_player_from_attainable_character_seed(seed) -> Player:
	"""
	Create a Player instance from an attainable-character seed dict.

	This will populate simple attributes from the seed and instantiate
	armor/weapon/abilities using existing factory helpers.
	"""
	if not isinstance(seed, dict):
		return None

	# create player with provided name (Player requires a name)
	name = seed.get('name') or seed.get('id') or 'Unnamed'
	p = Player(name)

	# populate simple fields that match Player attributes
	# use populate_from_json to apply numeric and string fields where possible	
	p.populate_from_json(seed)
	
	# instantiate equipment items (armor/weapon) from ids in seed
	from game.objects.item import instantiate_item_from_id
	# armor slots expected keys in seed
	armor_keys = ['arm_armor', 'head_armor', 'body_armor', 'leg_armor']
	for key in armor_keys:
		val = seed.get(key)
		if val:
			itm = instantiate_item_from_id(val)
			if itm is not None:
				setattr(p, key, itm)

	# equipped weapon
	weap_ref = seed.get('equipped_weapon') or seed.get('weapon')
	if weap_ref:
		w = instantiate_item_from_id(weap_ref)
		if w is not None:
			p.equipped_weapon = w

	# instantiate abilities from ids
	abilities = seed.get('abilities') or []

	if abilities and isinstance(abilities, (list, str)):
		from game.objects.player_ability import _instantiate_from_seed
		# build a lookup of ability seeds by id from constants
		ability_seeds = const.PLAYER_ABILITY_SEEDS
		seed_map = {s.get('id'): s for s in ability_seeds}
		for aid in abilities:
			if not aid:
				continue
			aseed = seed_map.get(aid)
			if aseed:
				ability_obj = _instantiate_from_seed(aseed)
				p.abilities.append(ability_obj)

	# return instantiated player
	return p


