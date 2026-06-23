from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import random
import uuid


from .item import Item
from .weapon import Weapon
from .armor import Armor, ArmorType
from .utility_item import UtilityItem
from .special_item import SpecialItem
import game.constants as const
import game.status_utils as status_utils

#from game.objects.item import instantiate_item_from_id
# AI decision engine for hostiles
from combat_balancing_simulation.hostile_ai_service import decide_action

@dataclass
class RandomHostile:
	"""Simple hostile NPC used for random encounters.

	This class is intentionally lightweight — it provides basic stats,
	a weapon and optional armor, and simple methods for attacking and
	taking damage. The generator function below creates instances with
	randomized equipment and loot based on level.
	"""
	from .player_ability import PlayerAbility
	_uuid: str = field(default_factory=lambda: uuid.uuid4().hex)
	id: Optional[str] = None
	name: str = "- Missing Hostile -"
	level: int =1
	max_hp: int =10
	current_hp: int =10
	max_ap: int =5
	current_ap: int =5
	x: int =0
	y: int =0
	z: int =0
	equipped_weapon: Optional[Weapon] = None
	armor: List[Armor] = field(default_factory=list)
	inventory: List[Item] = field(default_factory=list)
	common_drop: Item = None
	rare_drop: Item = None
	money_range: Optional[tuple[int,int]] = None
	hostile_type: str = "creature"
	# transient tracking for broken armor pieces in combat
	last_broken_armor: List[str] = field(default_factory=list)
	# core RPG-style stats for personality and scaling
	strength: int =1
	dexterity: int =1
	constitution: int =1
	intelligence: int =1
	# base pools that are augmented by stats/level
	base_hp: int =5
	base_ap: int =3
	base_xp: int =0
	min_spawn_level: int =1
	rarity: str = "common"
	base_str: int = 1
	base_con: int =1
	base_int: int = 1
	base_dex: int = 1
	str_per_level: int = 1
	dex_per_level: int = 1
	con_per_level: int = 1
	int_per_level: int = 1
	defense: int = 0
	
	# Status effects currently applied to this hostile. Each is a dict similar to
	# those produced by PlayerAbility._derive_status_effects().
	# Each status is a dict: {id, name, type, duration, magnitude, elements, turns_remaining, source}
	statuses: List[dict] = field(default_factory=list)
	# Abilities the hostile can use (PlayerAbility instances)
	abilities: List[PlayerAbility] = field(default_factory=list)
	basic_attack: str = ""
	strong_attack: str = ""

	# Elemental affinities
	weaknesses: List[str] = field(default_factory=list)
	resistances: List[str] = field(default_factory=list)
	immunities: List[str] = field(default_factory=list)

	def get_modified_strength (self) -> int:
		"""compute effective strength using status modifiers, armor and weapon"""
		modified = self.strength
		
		modified = status_utils.compute_modified_stat(self, 'strength', modified)

		return max(1, modified)

	def get_modified_dexterity (self) -> int:
		"""compute effective dexterity using status modifiers, armor and weapon"""
		modified = self.dexterity
		modified = status_utils.compute_modified_stat(self, 'dexterity', modified)

		return max(1, modified)

	def get_modified_intelligence (self) -> int:
		"""compute effective intelligence using status modifiers, armor and weapon"""
		modified = self.intelligence
		modified = status_utils.compute_modified_stat(self, 'intelligence', modified)
		return max(1, modified)

	def get_modified_constitution(self) -> int:
		"""compute effective constitution using status modifiers, armor and weapon"""
		modified = self.constitution
		modified = status_utils.compute_modified_stat(self, 'constitution', modified)
		return max(1, modified)

	def is_alive(self) -> bool:
		return self.current_hp >0

	def take_damage(self, amount: int, attacker: Optional[object] = None, elements: Optional[List[str]] = None, physical: bool = False) -> int:
		"""Reduce HP and return actual damage taken (after armor absorption).

		Armor absorption is simplified: sum of armor.defense across equipped armor
		is subtracted from incoming damage (but not below 0).
		"""
		if amount <=0:
			return 0
		# incorporate inherent defense into absorption (hostile-specific)
		inherent_def = self.defense

		# compute armor absorption and reduce durability proportionally
		# reset transient
		self.last_broken_armor = []
		armor_block = 0
		# add inherent defense into block
		armor_block += inherent_def
		for a in self.armor:
			if a and not a.is_broken():
				armor_block += a.defense
		net = max(0, amount - armor_block)
		# apply incoming status modifiers (defense buffs/debuffs, elemental debuffs)
		if elements:
			# immunities: if any element matches an immunity, damage is nullified
			imms = self.immunities or []
			if any(e in imms for e in elements):
				net =0
			else:
				# weaknesses: amplify damage per matching element (e.g. +25% per match, capped)
				weaks = self.weaknesses or []
				weak_matches = sum(1 for e in elements if e in weaks)
				if weak_matches >0:
					amp = min(2.0,1.0 +0.25 * weak_matches)
					net = int(net * amp)
				# resistances: reduce damage per matching element (each -20% up to -60%)
				res = self.resistances or []
				matches = sum(1 for e in elements if e in res)
				if matches >0:
					reduction = min(0.6,0.2 * matches)
					net = int(net * (1.0 - reduction))
			# allow status_utils to further modify net
			net = status_utils.compute_incoming_damage(self, net, elements, is_physical = physical)

		# apply durability loss to pieces that contributed
		if armor_block >0:
			dmg_share = max(1, net //2)
			for a in self.armor:
				if a and not a.is_broken() and not getattr(a, 'unbreakable', False):
					before = a.durability
					a.take_damage(dmg_share)
					if before >0 and a.is_broken():
						# record broken piece name for UI
						self.last_broken_armor.append(a.name)

		if physical == True and 'sleep' in [s.get('id') for s in self.statuses]:
			# waking up on damage
			self.remove_status_by_id('sleep')

		self.current_hp = max(0, self.current_hp - net)
		return net

	def heal(self, amount: int) -> int:
		if amount <=0:
			return 0
		old = self.current_hp
		self.current_hp = min(self.max_hp, self.current_hp + amount)
		return self.current_hp - old

	def attack(self, enemies: List[Optional[object]] = None, allies: List[Optional[object]] = None) -> Dict[str, Any]:
		"""Perform an attack. Returns a dict describing the attack outcome.

		If `target` has a `take_damage` method it will be called with the
		calculated damage. Otherwise the attack is only described.
		"""
		# temp assignment until intelligence is built out
		# ``enemies`` expected to be a list of Player objects
		enemies_list = [e for e in (enemies or []) if e]
		allies_list = [a for a in (allies or []) if a]

		# Use AI decision engine to pick action
		action = decide_action(self, enemies=enemies_list, allies=allies_list)

		if action and action.get('type') == 'ability' and action.get('ability'):
			ability = action.get('ability')
			tgts = action.get('targets', [])
			# attempt to use ability via use_ability (supports multi-target list)
			res = self.use_ability(ability, targets=tgts)
			if res:
				return {
					"attacker_id": self.id,
					"attacker_name": self.name,
					"used_ability": True,
					"ability_result": res,
					"targets": tgts,
				}
			# if ability failed fall through to basic attack

		# basic attack: delegate to perform_basic_attack to avoid duplicate logic
		# pick a sensible target for basic attack
		target = None
		if enemies_list:
			# prefer the chosen target from AI if present
			if action and action.get('targets'):
				cand = action.get('targets')[0]
				if cand and getattr(cand, 'is_alive', lambda: True)():
					target = cand
			# fallback to first alive enemy
			if target is None:
				input ("fallback first target")
				alive_enemies = [e for e in enemies_list if getattr(e, 'is_alive', lambda: True)()]
				if alive_enemies:
					target = alive_enemies[0]

		if target is None:
			input("no target found for basic attack")
		return self.perform_basic_attack(target)

	def perform_basic_attack(self, target: Optional[object] = None) -> Dict[str, Any]:
		"""Perform a simplified single-target basic attack against `target`.
		Returns a dict describing the outcome (same shape as in `attack`).
		This mirrors the basic-attack branch used by the AI decision flow.
		"""
		import random
		result: Dict[str, Any] = {
			"attacker_id": self.id,
			"attacker_name": self.name,
			"weapon": None,
			"damage":0,
			"hit": False,
		}

		# determine damage and weapon info
		if not getattr(self, 'equipped_weapon', None):
			weapon_name = self.basic_attack if getattr(self, 'basic_attack', None) else 'Unarmed'
			base_damage = max(1, int(self.get_modified_strength() + (self.level //1)))
			crit_chance =0.0
		else:
			weapon_name = self.basic_attack if getattr(self, 'basic_attack', None) else 'Unarmed'
			base_damage = int(self.equipped_weapon.expected_damage())
			base_damage += max(1, int(self.get_modified_strength() + (self.level //1)))
			crit_chance = getattr(self.equipped_weapon, 'critical_chance',0)

		result['weapon'] = weapon_name

		# compute accuracy / evasion
		attacker_acc =50 + (self.level *2) + (self.get_modified_dexterity() *2)
		target_evasion =10
		if target is not None:
			target_evasion =10 + target.get_modified_dexterity() *2
		hit_chance = max(5, min(95,50 + (attacker_acc - target_evasion)))
		hit_roll = random.random() *100

		if hit_roll > hit_chance:
			result['hit'] = False
			result['target_id'] = getattr(target, '_uuid', None) or getattr(target, 'id', None) or getattr(target, 'name', None)
			result['target_name'] = getattr(target, 'name', None)
			return result

		# hit: compute damage with variance
		damage = max(0, int(random.normalvariate(base_damage, max(1, base_damage *0.2))))
		# collect elements and apply outgoing modifiers
		base_elements = None
		elems = status_utils.collect_attack_elements(self, base_elements)
		damage = status_utils.compute_outgoing_damage(self, damage, elems if elems else None)

		# crit
		if crit_chance and (random.random() *100) < crit_chance:
			damage *=2
			result['crit'] = True
		else:
			result['crit'] = False

		result['damage'] = damage
		result['hit'] = True

		# apply to target if possible
		if target is not None:
			applied = target.take_damage(damage, attacker=self, elements=elems if elems else None, physical=True)
			result['applied'] = applied
			result['target_id'] = getattr(target, '_uuid', None) or getattr(target, 'id', None) or getattr(target, 'name', None)
			result['target_name'] = getattr(target, 'name', None)

		if target is None:
			input("no target wtf")
		return result

	#note to later add mutitarget/aoe support
	def use_ability(self, ability: Optional[object], target: Optional[object] = None, targets: Optional[List[object]] = None) -> Dict[str, Any]:
		"""Use a PlayerAbility (or ability id) against a target. Returns result dict."""
		from .player_ability import PlayerAbility

		if not ability:
			return {'used': False, 'error': 'no_ability'}
		# resolve ability instance
		if ability is None:
			return {'used': False, 'error': 'ability_not_known'}

		cost = ability.ap_cost
		if cost > self.current_ap:
			return {'used': False, 'error': 'insufficient_ap'}

		# spend AP
		self.current_ap = max(0, self.current_ap - cost)
		# apply ability
		results: List[Dict[str, Any]] = []
		# if explicit targets list provided, apply to each target
		for t in (targets or []): # explicit target is Player or RandomHostile
			# simple percent reduction scaling when hitting multiple targets
			pr = ((len(targets) - 1) *0.1) if targets else 0.0
			r = ability.apply(target=t, owner=self, percent_reduction=pr)
			if isinstance(r, dict):
				r['ability_id'] = ability.id
				r['ability_name'] = ability.name
			results.append(r)

		# summary
		return {'used': True, 'ability_id': ability.id, 'ability_name': ability.name, 'results': results}

	def choose_and_use_ability(self, target: Optional[object] = None) -> Optional[Dict[str, Any]]:
		"""Simple AI to pick a usable ability and apply it to `target`.
	
		Returns the result dict from `use_ability` or None if none usable.
		"""
		# be defensive: self.abilities may be None or contain falsy entries
		pa_list = self.abilities or []
		candidates = [a for a in pa_list if a and a.ap_cost <= self.current_ap]
		if not candidates:
			return None
		# prefer higher-level abilities some of the time
		if random.random() <0.2:
			choice = max(candidates, key=lambda x: x.level)
		else:
			choice = random.choice(candidates)
		return self.use_ability(choice, target)

	def equip_weapon(self, weapon: Weapon) -> None:
		self.equipped_weapon = weapon

	def equip_armor(self, armor_piece: Armor) -> None:
		# replace armor of the same slot if present
		for i, a in enumerate(self.armor):
			if a.slot == armor_piece.slot:
				self.armor[i] = armor_piece
				return
		self.armor.append(armor_piece)

	def add_loot(self, item: Item) -> None:
		self.inventory.append(item)

	def drop_loot(self) -> List[Item]:
		"""Return and clear inventory; called when hostile is defeated."""
		#do an rng roll to determine if common_drop
		# also do seperate rng check for rare drop
		loot = list()
		rng_common = random.random()
		if self.common_drop and rng_common < 0.2:
			# item = instantiate_item_from_id(self.common_drop)
			# if item:
			loot.append(self.common_drop)
		rng_rare = random.random()
		if self.rare_drop and rng_rare < 0.05:
			# item = instantiate_item_from_id(self.rare_drop)
			# if item:
			loot.append(self.rare_drop)

		self.inventory.clear()
		return loot

	# players is from game.objects.player import Player
	def award_players(self, player_game, players: List[object]) -> Dict[str, Any]:
		"""Distribute loot and XP to a list of `players`.
		each player receives a the total amount of xp divided by the number of players. and then modified based on level difference
		loot is distributed to the PlayerGame's shared inventory and money pool. obeying player_game.max_inventory_count
		"""
		# Collect loot and distribute to shared inventory / money. Also track awarded items and money for return.
		loot = self.drop_loot()

		awarded_items: List[Item] = []
		money_awarded =0
		if loot:
			for it in loot:
				# add to shared inventory if space
				if player_game.pick_up_item(it):
					awarded_items.append(it)

		# add money if applicable
		if self.money_range:
			lo, hi = self.money_range
			qty = random.randint(max(0, lo), max(lo, hi))
			if qty > 0:
				player_game.add_money(qty)
				money_awarded += qty

		
		# determine xp to award (per-hostile)
		xp = getattr(self, 'base_xp', None)
		if not xp:
			xp = max(1, self.level *10)
		else:
			xp = int(xp *10)

		# distribute xp among players, modified by level difference
		xp_per_player = xp // max(1, len(players)) if players else 0
		xp_awarded_map: Dict[str, int] = {}
		level_gains: List[Dict[str, int]] = []
		for p in players:
			# identify player id for reporting
			pid = getattr(p, '_uuid', None) or getattr(p, 'id', None) or getattr(p, 'name', None)
			modifier = float(self.level) / max(1, int(getattr(p, 'level',1)))
			final_xp = int(xp_per_player * modifier)
			# award xp and record levels gained
			levels_gained = p.gain_experience(final_xp)
			# record
			xp_awarded_map[pid] = xp_awarded_map.get(pid,0) + final_xp
			if levels_gained:
				if levels_gained > 0:
					for (lg) in range(levels_gained):
						p.check_level_up_awards()
				level_gains.append({'player_id': pid, 'levels_gained': levels_gained})

		# Return detailed award info so callers can queue and aggregate across multiple hostiles.
		return {
			'loot': loot or [],
			'awarded_items': awarded_items,
			'money_awarded': money_awarded,
			'xp_awarded': xp,
			'levels_gained': level_gains,
		}

	def add_status(self, descriptor: dict, source: Optional[object] = None) -> None:
		"""Apply a status descriptor to the entity, checking for immunities,
		resistances, and weaknesses.
		"""
		if not descriptor or not isinstance(descriptor, dict):
			return

		status_id = descriptor.get('id')
		if not status_id:
			return

		# 1. Check for Immunity
		if status_id in self.immunities:
			return  # Do not apply the status

		s = dict(descriptor)
		duration = int(s.get('duration', 1))

		# 2. Check for Resistance
		if status_id in self.resistances:
			if duration > 1:
				# Reduce duration by half, ensuring it's at least 1 turn
				duration = max(1, duration // 2)
			# Optional: Could also reduce magnitude here

		# 3. Check for Weakness
		if status_id in self.weaknesses:
			if duration != -1: # Don't extend permanent statuses
				# Increase duration by 50%
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

	def tick_statuses(self) -> None:
		"""Advance time for statuses, decrementing turns and removing expired ones.
		Permanent statuses (turns_remaining == -1) are preserved until explicitly removed.
		"""
		new = []
		for st in self.statuses:
			tr_raw = st.get('turns_remaining', st.get('duration',1))
			
			tr = int(tr_raw)
			
			if tr == -1:
				new.append(st)
			else:
				tr -=1
				if tr >0:
					st['turns_remaining'] = tr
					new.append(st)
		self.statuses = new

	def populate_from_json(self, data: dict) -> None:
		"""Populate attributes from a JSON-like dict."""
		for k, v in data.items():
			if hasattr(self, k):
				# if attribute is min_spawn_level 
				if k == 'min_spawn_level':
					input("Debug: min_spawn_level encountered")
				setattr(self, k, v)

	def level_to(self, target_level: int) -> int:
		"""Advance (or set) this hostile to `target_level` and recompute derived stats.

		This increments core stats deterministically using the instance's
		base_* and *_per_level fields, then recomputes HP/AP/evasion and base_xp.
		Returns the number of levels gained (0 if target_level <= current level).
		"""
		if not isinstance(target_level, int) or target_level <1:
			raise ValueError('target_level must be an integer >=1')

		# no-op if already at or above target
		if target_level <= self.level:
			return 0

		old_level = self.level
		# perform incremental increases per level using this instance's per-level fields
		for _level in range(self.level +1, int(target_level) +1):
			# increase core stats by per-level amounts (deterministic)
			self.strength = max(1, int(self.strength + (self.str_per_level or 0))) + 1
			self.dexterity = max(1, int(self.dexterity + (self.dex_per_level or 0))) + 1
			self.constitution = max(1, int(self.constitution + (self.con_per_level or 0))) + 1
			self.intelligence = max(1, int(self.intelligence + (self.int_per_level or 0))) + 1

		# update level to target
		self.level = int(target_level)

		# Recompute pools using same formulas as generator for the final level
		lvl = self.level

		self.max_hp = max(3, int(self.base_hp + self.constitution *2 + lvl *5))
		self.current_hp = int(self.max_hp)

		self.max_ap = max(1, int(self.base_ap + self.intelligence + (lvl //2)))
		self.current_ap = int(self.max_ap)

		# base xp: prefer explicit base_xp if set, else derive from simple formula
		if self.base_xp:
			self.base_xp = int(self.base_xp)
		else:
			self.base_xp = max(1, lvl *10 + (self.strength + self.constitution + self.dexterity + self.intelligence) //4)

		if self.equipped_weapon is not None:
			self.equipped_weapon.damage = max(1,1 + lvl *2)

		return self.level - old_level


# def generate_random_hostile(region, player, player_game, choice, level: int =1) -> RandomHostile:
# 	from .player_ability import _instantiate_from_seed as instantiatePlayerAbility
# 	"""Factory to create a RandomHostile with randomized stats and gear.

# 	The generator uses simple scaling rules: HP and AP scale with level,
# 	weapons and armor get damage/defense scaled by level. A few random
# 	items may be added to inventory as loot.
# 	"""

# 	# create hostile with placeholder stats; values will be adjusted below
# 	hostile = RandomHostile(
# 		id=None,
# 		name='uknow',
# 		level=level,
# 		# temporary HP/AP; will be recomputed after assigning stats
# 		max_hp=0,
# 		current_hp=0,
# 		max_ap=0,
# 		current_ap=0,
# 		hostile_type="humanoid" if 'uknow' in ("Rogue", "Bandit", "Raider") else "beast",
# 		# keep dex as a base stat; others will be filled in
# 		dexterity=1,
# 		strength=1,
# 		constitution=1,
# 		intelligence=1,
# 	)
# 	# set hostile stats from seed, all fields match json names
# 	hostile.min_spawn_level = choice.get('min_spawn_level',1) if choice is not None else 1
# 	hostile.rarity = choice.get('rarity', 'common') if choice is not None else 'common'
# 	hostile.weaknesses = choice.get('weaknesses', []) if choice is not None else []
# 	hostile.resistances = choice.get('resistances', []) if choice is not None else []
# 	hostile.immunities = choice.get('immunities', []) if choice is not None else []
# 	hostile.base_str = choice.get('base_str',1) if choice is not None else 1
# 	hostile.base_dex = choice.get('base_dex',1) if choice is not None else 1
# 	hostile.base_con = choice.get('base_con',1) if choice is not None else 1
# 	hostile.base_int = choice.get('base_int',1) if choice is not None else 1
# 	hostile.str_per_level = choice.get('str_per_level',1) if choice is not None else 1
# 	hostile.dex_per_level = choice.get('dex_per_level',1) if choice is not None else 1
# 	hostile.con_per_level = choice.get('con_per_level',1) if choice is not None else 1
# 	hostile.int_per_level = choice.get('int_per_level',1) if choice is not None else 1


# 	# attach seed id and drop metadata if available
# 	if choice is not None:
# 		hostile.id = choice.get('id')
# 		hostile.name = choice.get('name', hostile.name)
		
# 		hostile.common_drop = instantiate_item_from_id(choice.get('common_drop', None))
# 		hostile.rare_drop = instantiate_item_from_id(choice.get('rare_drop', None))
# 		hostile.money_range = choice.get('money_range')
# 		# optional stat seeds: allow per-seed base and per-level growth
# 		seed_str = choice.get('base_str', None)
# 		seed_dex = choice.get('base_dex', None)
# 		seed_con = choice.get('base_con', None)
# 		seed_int = choice.get('base_int', None)
# 		seed_base_hp = choice.get('base_hp', None)
# 		seed_base_ap = choice.get('base_ap', None)
# 		seed_base_xp = choice.get('base_xp', None)
# 		hostile.basic_attack = choice.get('basic_attack', "")
# 		hostile.strong_attack = choice.get('strong_attack', "")
# 		# optional abilities attached to the seed
# 		seed_abilities = choice.get('player_abilities')
# 		if seed_abilities:
# 			for aid in seed_abilities:
# 				# find ability seed
# 				aseed = next((s for s in getattr(const, 'PLAYER_ABILITY_SEEDS', []) if s.get('id') == aid), None)
# 				if aseed:
# 					hostile.abilities.append(instantiatePlayerAbility(aseed))

# 	# Basic weapon
# 	wep = Weapon(
# 		name=f"Teeth L{level}" if hostile.hostile_type == "beast" else f"Fist L{level}",
# 		damage=1 + level *2,
# 		ap_cost=1,
# 		range=1,
# 		critical_chance=min(25.0,5.0 + level *2.0),
# 	)
# 	# give basic weapon some durability
# 	wep.durability =10 + level *5
# 	wep.max_durability = wep.durability
# 	hostile.equip_weapon(wep)

# 	# Random armor pieces (small chance)
# 	if random.random() <0.5:
# 		armor_piece = Armor(name=f"Hide Armor L{level}", slot=ArmorType.BODY, defense=level *1 +1, durability=20 + level *10, max_durability=20 + level *10)
# 		hostile.equip_armor(armor_piece)

# 	# Assign base stats with simple growth rules.
# 	hostile.strength = max(1, int(seed_str + level * choice.get('str_per_level',0) + random.randint(-1,1))) if choice is not None and seed_str is not None else max(1,1 + level //3 + random.randint(0,2))
# 	hostile.dexterity = max(1, int(seed_dex + level * choice.get('dex_per_level',0) + random.randint(-1,1))) if choice is not None and seed_dex is not None else max(1,1 + level //3 + random.randint(0,2))
# 	hostile.constitution = max(1, int(seed_con + level * choice.get('con_per_level',0) + random.randint(-1,1))) if choice is not None and seed_con is not None else max(1,1 + level //2 + random.randint(0,2))
# 	hostile.intelligence = max(1, int(seed_int + level * choice.get('int_per_level',0) + random.randint(-1,1))) if choice is not None and seed_int is not None else max(1,1 + level //4 + random.randint(0,2))

# 	# base HP/AP defaults or seed overrides
# 	hostile.base_hp = seed_base_hp if seed_base_hp is not None else 5
# 	hostile.base_ap = seed_base_ap if seed_base_ap is not None else 3
# 	# compute final pools
# 	hostile.max_hp = max(3, hostile.base_hp + hostile.constitution *2 + level *2)
# 	hostile.current_hp = hostile.max_hp
# 	hostile.max_ap = max(1, hostile.base_ap + hostile.intelligence *1 + (level //2))
# 	hostile.current_ap = hostile.max_ap

# 	# derive evasion from dexterity
# 	hostile.evasion =10 + hostile.dexterity *2

# 	# base XP
# 	if choice is not None and seed_base_xp is not None:
# 		hostile.base_xp = int(seed_base_xp)
# 	else:
# 		hostile.base_xp = max(1, level *10 + (hostile.strength + hostile.constitution + hostile.dexterity + hostile.intelligence) //4)

# 	return hostile
