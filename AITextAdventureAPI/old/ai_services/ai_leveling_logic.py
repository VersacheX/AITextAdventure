from typing import Optional, Tuple, Dict, Any

from game.objects.player import Player
from game import constants as const
from ai_services.ai_ui_helper import type_victory_message


def _choose_ability_for_player(p: Player) -> Optional[str]:
	"""Pick a sensible ability id for a player when one is available.

	Strategy:
	- Look up ability seeds from const.PLAYER_ABILITY_SEEDS (if present).
	- Prefer abilities the player does not already know and whose level <= player.level.
	- For a simple heuristic pick the highest-level new ability available.
	"""
	seeds = getattr(const, 'PLAYER_ABILITY_SEEDS', []) or []
	candidates = [s for s in seeds if int(s.get('level',1)) <= int(getattr(p, 'level',1))]
	# filter out known ids
	known = set()
	for a in getattr(p, 'abilities', []) or []:
		known.add(getattr(a, 'id', a) if a is not None else a)
	candidates = [s for s in candidates if s.get('id') not in known]
	if not candidates:
		return None
	# prefer higher-level abilities (more interesting)
	candidates.sort(key=lambda x: int(x.get('level',1)), reverse=True)
	return candidates[0].get('id')


def _distribute_stat_points(p: Player, pts: int, build: str = 'brawler') -> Tuple[int, int, int, int]:
	"""Return (str_inc, dex_inc, con_inc, int_inc) for `pts` points for given build.

	Current supported builds:
	- 'brawler': prioritize Strength, then Constitution, then Dexterity, then Intelligence.
	- 'balanced': spread evenly.
	- 'glass': prioritize Strength and Dexterity, minimal Con/Int.
	
	Defaults to brawler if unknown.
	"""
	str_inc = dex_inc = con_inc = int_inc =0
	if pts <=0:
		return 0,0,0,0
	if build == 'balanced':
		# distribute round-robin
		order = ['str', 'dex', 'con', 'int']
		idx =0
		while pts >0:
			which = order[idx %4]
			if which == 'str':
				str_inc +=1
			elif which == 'dex':
				dex_inc +=1
			elif which == 'con':
				con_inc +=1
			else:
				int_inc +=1
			idx +=1
			pts -=1
		return str_inc, dex_inc, con_inc, int_inc

	# brawler and others default
	if build == 'glass':
		# favor STR and DEX
		while pts >0:
			if pts >1:
				str_inc +=1
				pts -=1
			if pts >0:
				dex_inc +=1
				pts -=1
		return str_inc, dex_inc, con_inc, int_inc

	# brawler: put as many as possible into STR, then CON, then DEX
	while pts >0:
		if pts >0:
			str_inc +=1
			pts -=1
		if pts >0:
			con_inc +=1
			pts -=1
		if pts >0:
			dex_inc +=1
			pts -=1
	# remaining (if any) to int
	if pts >0:
		int_inc += pts
		pts =0
	return str_inc, dex_inc, con_inc, int_inc


def _distribute_power_points(p: Player, pts: int, build: str = 'brawler') -> Tuple[int, int]:
	"""Return (hp_points, ap_points) allocation. Brawlers favor HP entirely."""
	if pts <=0:
		return 0,0
	if build == 'balanced':
		hp = pts //2
		ap = pts - hp
		return hp, ap
	# brawler
	return pts,0


def ai_level_up_player(p: Player, build: str = 'brawler') -> Dict[str, Any]:
	"""Automatically perform a level-up for an AI player according to `build`.

	Returns a dict with details of the change: increments, selected ability id (if any).
	"""
	result: Dict[str, Any] = {'levels_gained':0, 'stat_alloc': (0,0,0,0), 'power_alloc': (0,0), 'selected_ability': None}
	# determine how many levels to apply (Player.gain_experience already updated level in demo, but this helper should just apply awards for newly gained levels)
	# We assume caller increments p.level already; here we just allocate the per-level awards once per call.
	select_new_ability, stat_points, power_points = p.check_level_up_awards()
	
	# allocate stat points
	str_inc, dex_inc, con_inc, int_inc = _distribute_stat_points(p, int(stat_points or 0), build)

	# allocate power points
	hp_pts, ap_pts = _distribute_power_points(p, int(power_points or 0), build)

	p.upgrade_stats(str_inc, dex_inc, con_inc, int_inc, hp_pts, ap_pts)

	# choose ability if available <- choose ability last
	selected = None
	if select_new_ability:
		selected = _choose_ability_for_player(p)

	# inform via typewriter
	if selected:
		type_victory_message(f"AI learned new ability: {selected}", delay=0.1)
	type_victory_message(f"AI leveled up: +STR {str_inc} +DEX {dex_inc} +CON {con_inc} +INT {int_inc} | +HP {hp_pts} +AP {ap_pts}", delay=0.1)

	result['stat_alloc'] = (str_inc, dex_inc, con_inc, int_inc)
	result['power_alloc'] = (hp_pts, ap_pts)
	result['selected_ability'] = selected
	# report one level processed (caller increments level elsewhere)
	result['levels_gained'] =1
	return result
