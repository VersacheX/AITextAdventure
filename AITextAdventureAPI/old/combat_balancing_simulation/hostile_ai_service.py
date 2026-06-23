import stat
from typing import List, Optional, Dict, Any
import random

from game.objects.player_ability import EffectType


def has_any_status(ent: object, keys: List[str]) -> bool:
	for key in keys:
		if has_status(ent, key):
			return True
	return False

def has_status(entity: Optional[object], status_id: str) -> bool:
	if entity is None or status_id is None:
		return False

	statuses = getattr(entity, 'statuses', []) or []
	
	for s in statuses:
		if s.get('id') == status_id:
			return True
	return False


def choose_enemy_target(enemies: List[object]) -> Optional[object]:
	if not enemies:
		return None
	# prefer alive enemy with highest current_hp
	alive = [e for e in enemies if e is not None and e.is_alive()]
	if not alive:
		if not enemies:
			input(f"NO ENEMIES FOR SOME REASON")
		return enemies[0] if enemies else None
	return max(alive, key=lambda e: e.current_hp)


def choose_ally_target_for_heal(allies: List[object]) -> Optional[object]:
	if not allies:
		return None
	alive = [a for a in allies if a is not None and getattr(a, 'is_alive', lambda: True)()]
	if not alive:
		return None
	# choose lowest hp percentage
	def hp_pct(a):
		max_hp = getattr(a, 'max_hp', 1) or 1
		return getattr(a, 'current_hp', 0) / float(max_hp)
	return min(alive, key=hp_pct)


def threat_score(entity: Optional[object]) -> float:
	"""Estimate an ally's threat/power for buff targeting.

	Simple heuristic: sum of modified offensive stats and weapon damage.
	"""
	if entity is None:
		return 0.0
	score = 0.0
	ms = getattr(entity, 'get_modified_strength', lambda: getattr(entity, 'strength', 0))()
	mi = getattr(entity, 'get_modified_intelligence', lambda: getattr(entity, 'intelligence', 0))()

	weapon = entity.equipped_weapon
	wep_dmg = 0
	if weapon is not None:
		wep_dmg = weapon.damage
	score = float(ms) * 1.2 + float(mi) * 0.8 + float(wep_dmg)
	return score


def choose_targets_for_ability(ability: object, enemies: List[object], allies: List[object]) -> List[object]:
	# return list of targets appropriate for ability.effect
	if ability is None:
		return []
	eff = getattr(ability, 'effect', None)
	# STATUS abilities: choose allies for buff, enemies for debuff
	if eff == EffectType.STATUS:
		# STATUS_KEY_UPDATE: change to a for loop to handle status_keys instead
		for key in getattr(ability, 'status_keys', []) or []:
			if key.endswith('_buff'):
				# buff allies needing it
				candidates = [a for a in (allies or []) if a and not has_status(a, key) and a.is_alive()]
				if not candidates:
					# fallback to any alive ally
					candidates = [a for a in (allies or []) if a and a.is_alive()]
				# if AOEs choose all candidates, else pick highest-threat ally to buff
				if getattr(ability, 'can_aoe', False):
					return candidates
				# prefer buffing the ally with highest threat score
				best = max(candidates, key=lambda a: threat_score(a)) if candidates else None
				return [best] if best else []
			elif key.endswith('_debuff'):
				candidates = [e for e in (enemies or []) if e and not has_status(e, key) and e.is_alive()]
				if getattr(ability, 'can_aoe', False):
					return candidates
				target = choose_enemy_target(candidates)
				if not target:
					input(f"NO ENEMY CANDIDATES 1")
				return [target] if target else []
			else:
				# other status types (continuous_damage etc.) target enemies
				candidates = [e for e in (enemies or []) if e and e.is_alive()]
				if getattr(ability, 'can_aoe', False):
					return candidates
				target = choose_enemy_target(candidates)
				if not target:
					input(f"NO ENEMY CANDIDATES 7")
				return [target] if target else []
	# HEAL
	if eff == EffectType.HEAL:
		# pick lowest HP ally or all if AOE
		if getattr(ability, 'can_aoe', False):
			return [a for a in (allies or []) if a and a.is_alive()]
		ally = choose_ally_target_for_heal(allies or [])
		return [ally] if ally else []
	# REVIVE
	if eff == EffectType.REVIVE:
		# pick a dead ally
		dead = [a for a in (allies or []) if a and not a.is_alive()]
		if not dead:
			return []
		if getattr(ability, 'can_aoe', False):
			return dead
		return [dead[0]]
	# DAMAGE
	if eff == EffectType.DAMAGE:
		# pick enemy target(s). Prefer AOEs when multiple enemies alive
		alive_enemies = [e for e in (enemies or []) if e and e.is_alive()]
		if not alive_enemies:
			return []
		if getattr(ability, 'can_aoe', False) and len(alive_enemies) > 1:
			return alive_enemies
		target = choose_enemy_target(alive_enemies)
		if not target:
			input(f"NO ENEMY CANDIDATES 5")
		return [target]

	# fallback to single primary enemy
	target = choose_enemy_target(enemies)
	if not target:
		input(f"NO ENEMY CANDIDATES 4")
	return [target] if target else []


def decide_action(hostile: object, enemies: List[Optional[object]] = None, allies: List[Optional[object]] = None) -> Dict[str, Any]:
	"""Decide whether the hostile should use an ability (and which) or perform a basic attack.

	Returns a dict: {'type': 'ability'|'attack', 'ability': PlayerAbility or None, 'targets': List[objects], 'reason': str}
	"""
	enemies = [e for e in (enemies or []) if e]
	allies = [a for a in (allies or []) if a]

	# Confused behavior: pick random action/targeting. This can target allies or enemies
	# and may use abilities or basic attacks. Works for both hostiles and players
	# when called from their respective attack/use logic.
	if has_status(hostile, 'confuse'):
		# collect alive units excluding self
		alive_enemies = [e for e in enemies if e and getattr(e, 'is_alive', lambda: True)()]
		alive_allies = [a for a in allies if a and getattr(a, 'is_alive', lambda: True)()]
		alive_others = [u for u in (alive_enemies + alive_allies) if u is not None and getattr(u, 'is_alive', lambda: True)() and u is not hostile]
		if not alive_others:
			return {'type': 'attack', 'ability': None, 'targets': [], 'reason': 'confused_no_targets'}

		# decide whether to attempt an ability (if any usable) or basic attack
		usable = [a for a in getattr(hostile, 'abilities', []) or [] if a and getattr(a, 'ap_cost',0) <= getattr(hostile, 'current_ap',0)]
		#50% chance to try ability when usable exist
		if usable and random.random() <0.5:
			choice = random.choice(usable)
			# decide side for targeting: status buffs -> allies, debuffs -> enemies, damage -> enemies
			eff = getattr(choice, 'effect', None)
			# STATUS_KEY_UPDATE: change to a for loop to handle status_keys instead
			for key in getattr(choice, 'status_keys', []) or []:
				#status_key = getattr(choice, 'status_key', '') or ''
				status_key  = key
				# default to targeting enemies for damage/others
				if str(eff).lower() == 'status' and status_key.endswith('_buff'):
					target_side = 'allies'
				elif str(eff).lower() == 'status' and status_key.endswith('_debuff'):
					target_side = 'enemies'
				else:
					# randomize target side for chaotic behavior
					target_side = 'enemies' if random.random() <0.7 else 'allies'

				if getattr(choice, 'can_aoe', False):
					if target_side == 'enemies':
						tgts = alive_enemies
					else:
						tgts = alive_allies
					# filter out None and dead
					tgts = [t for t in (tgts or []) if t and getattr(t, 'is_alive', lambda: True)()]
					return {'type': 'ability', 'ability': choice, 'targets': tgts, 'reason': 'confused_ability_aoe'}
				else:
					# single random target from chosen side
					pool = alive_enemies if target_side == 'enemies' else alive_allies
					if not pool:
						# fallback to any other
						pool = alive_others
					tgt = random.choice(pool)
					return {'type': 'ability', 'ability': choice, 'targets': [tgt], 'reason': 'confused_ability_single'}

		# fallback to random basic attack: may hit ally or enemy
		# pick a random living unit (excluding self)
		tgt = random.choice(alive_others)
		return {'type': 'attack', 'ability': None, 'targets': [tgt], 'reason': 'confused_attack'}

	enemies = [e for e in (enemies or []) if e]
	allies = [a for a in (allies or []) if a]
	usable = [a for a in getattr(hostile, 'abilities', []) or [] if a and getattr(a, 'ap_cost', 0) <= getattr(hostile, 'current_ap', 0)]

	# small helper to compute hp ratio safely
	def hp_ratio(ent: object) -> float:
		max_hp = getattr(ent, 'max_hp', 1) or 1
		return float(getattr(ent, 'current_hp', 0)) / float(max_hp)

	# Evaluate need: allies low HP or dead
	low_allies = [a for a in allies if getattr(a, 'is_alive', lambda: True)() and hp_ratio(a) < 0.5]
	dead_allies = [a for a in allies if not getattr(a, 'is_alive', lambda: True)]

	# quick list of low-HP enemies for nuke decisions
	low_hp_enemies = [e for e in enemies if getattr(e, 'is_alive', lambda: True)() and hp_ratio(e) < 0.35]

	# Priority: Revive (careful) > Heal > Buff high-threat allies > Debuff enemies > Damage (nuke low-HP) > Attack

	#1) Revive - avoid wasting weak revives: require revive to restore at least10% or be AOE
	revives = [a for a in usable if a.effect == EffectType.REVIVE]
	if revives and dead_allies:
		# pick revive that can target single dead or aoe
		# prefer revives that restore a meaningful percentage
		viable_revives = []
		for r in revives:
			
			pct = r.compute_power_with_owner(hostile)
			
			if getattr(r, 'can_aoe', False) or (pct and pct >= 10):
				viable_revives.append(r)
		if viable_revives:
			choice = random.choice(viable_revives)
			tgts = choose_targets_for_ability(choice, enemies, allies)
			if tgts:
				return {'type': 'ability', 'ability': choice, 'targets': tgts, 'reason': 'revive_needed'}

	#2) Heal
	heals = [a for a in usable if a.effect == EffectType.HEAL]
	if heals and low_allies:
		# prefer AOE heal if more than one ally low
		aoe_heals = [h for h in heals if getattr(h, 'can_aoe', False)]
		if aoe_heals and len(low_allies) > 1 and random.random() < 0.9:
			choice = random.choice(aoe_heals)
			return {'type': 'ability', 'ability': choice, 'targets': choose_targets_for_ability(choice, enemies, allies), 'reason': 'aoe_heal'}
		# single-target heal
		single_heals = [h for h in heals if not getattr(h, 'can_aoe', False)] or heals
		choice = random.choice(single_heals)
		return {'type': 'ability', 'ability': choice, 'targets': choose_targets_for_ability(choice, enemies, allies), 'reason': 'single_heal'}

	#3) Buff allies - prefer high-threat allies
	# fix to use status_keys instead of status_key and find if any status_keys is _buff
	status_buffs = [a for a in usable if a.effect == EffectType.STATUS and any((getattr(a, 'status_keys', []) or [])[i].endswith('_buff') for i in range(len(getattr(a, 'status_keys', []) or [])))]
	#status_buffs = [a for a in usable if a.effect == EffectType.STATUS and (getattr(a, 'status_key', '') or '').endswith('_buff')]
	for sb in status_buffs:
		# if any ally lacks this buff, consider using it
		cands = [al for al in allies if not has_any_status(al, [sb]) and getattr(al, 'is_alive', lambda: True)()]
		if cands:
			# if aoe prefer it for many targets
			if getattr(sb, 'can_aoe', False) and len(cands) > 1 and random.random() < 0.9:
				return {'type': 'ability', 'ability': sb, 'targets': choose_targets_for_ability(sb, enemies, allies), 'reason': 'aoe_buff'}
			# otherwise buff highest-threat ally
			return {'type': 'ability', 'ability': sb, 'targets': choose_targets_for_ability(sb, enemies, allies), 'reason': 'buff_high_threat'}

	#4) Debuff enemies
	status_debuffs = [a for a in usable if a.effect == EffectType.STATUS and any((getattr(a, 'status_keys', []) or [])[i].endswith('_debuff') for i in range(len(getattr(a, 'status_keys', []) or [])))]
	#status_debuffs = [a for a in usable if a.effect == EffectType.STATUS and (getattr(a, 'status_key', '') or '').endswith('_debuff')]
	#input (f"STATUS DEBUFFS: {status_debuffs}")
	for sd in status_debuffs:
		#input (f"CHECKING DEBUFF: {sd}")

		cands = [en for en in enemies if not has_any_status(en, sd.status_keys) and getattr(en, 'is_alive', lambda: True)()]
		if cands:
			if getattr(sd, 'can_aoe', False) and len(cands) > 1 and random.random() < 0.8:
				return {'type': 'ability', 'ability': sd, 'targets': choose_targets_for_ability(sd, enemies, allies), 'reason': 'aoe_debuff'}
			return {'type': 'ability', 'ability': sd, 'targets': choose_targets_for_ability(sd, enemies, allies), 'reason': 'debuff_enemy'}

	#5) Damage abilities - prefer nuking low-HP enemies when available
	damage_abilities = [a for a in usable if a.effect == EffectType.DAMAGE]
	if damage_abilities:
		# if there are low-HP enemies, try to pick a single-target ability that can finish one
		if low_hp_enemies:
			# evaluate which ability would most likely kill (compute power with owner)
			best_choice = None
			best_target = None
			best_score = -1
			for d in damage_abilities:
				for tgt in low_hp_enemies:
					power = d.compute_power_with_owner(hostile)
					# use target current_hp as kill threshold
					if power >= getattr(tgt, 'current_hp', 0):
						# prioritize non-AOE single-target nukes to conserve AP
						score = float(power) - float(getattr(tgt, 'current_hp', 0))
						if score > best_score:
							best_score = score
							best_choice = d
							best_target = tgt
			if best_choice and best_target:
				return {'type': 'ability', 'ability': best_choice, 'targets': [best_target], 'reason': 'nuke_finish'}
		# otherwise prefer aoe damage if multiple enemies alive
		aoe_candidates = [d for d in damage_abilities if getattr(d, 'can_aoe', False)]
		alive_count = len([e for e in enemies if getattr(e, 'is_alive', lambda: True)()])
		if aoe_candidates and alive_count > 1 and random.random() < 0.85:
			choice = random.choice(aoe_candidates)
			return {'type': 'ability', 'ability': choice, 'targets': choose_targets_for_ability(choice, enemies, allies), 'reason': 'aoe_damage'}
		# else pick single-target damage
		choice = random.choice(damage_abilities)
		return {'type': 'ability', 'ability': choice, 'targets': choose_targets_for_ability(choice, enemies, allies), 'reason': 'single_damage'}

	#6) Fall back to basic attack
	# Determine sensible attack target
	attack_target = choose_enemy_target(enemies)
	if not attack_target:
		input(f"NO ENEMY CANDIDATES 22")
	return {'type': 'attack', 'ability': None, 'targets': [attack_target] if attack_target else [], 'reason': 'basic_attack'}
