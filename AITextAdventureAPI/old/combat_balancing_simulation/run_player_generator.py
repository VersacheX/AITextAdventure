#!/usr/bin/env python3
"""Run the combat_balancing_simulation.player_generator to create test players.
Usage: python -m old.run_player_generator or run this file directly.
"""
import argparse
import sys
from typing import Optional, List, Dict, Any
import random

from ai_controlled_demo import PlayerGame
from game.objects.player import Player
from game.objects.player_game import PlayerGame
import game.constants_other as const_other

from combat_balancing_simulation.player_details_screen import format_player_summary
from combat_balancing_simulation.player_generator import generate_player
from game.constants import CHARACTER_CLASS_MAP

PLAYER_GAME = PlayerGame()


# def _derive_stat_focus_from_ability_type(ability_type: str) -> str:
# 	"""Given an ability_type id (e.g. 'technique'), pick the stat focus by
# 	reversing PREFERRED_ABILITY_TYPES. If multiple stats match, return the first.
# 	Defaults to 'strength' if nothing matches.
# 	"""
# 	atype = (ability_type or '').lower()
# 	for stat, types in (PREFERRED_ABILITY_TYPES or {}).items():
# 		if atype in [t.lower() for t in (types or [])]:
# 			return stat
# 	return 'strength'


def add_player(count: int =4, level: int =15, ability_type_focus: Optional[str] = None, seed: Optional[int] = None, base_name: str = 'NPC', player_game: PlayerGame) -> List[Player]:
	"""Create `count` players. If `ability_type_focus` is provided, use it for
	all players; otherwise pick a random ability type per character from
	`CHARACTER_CLASS_MAP` keys. The display name is taken from the map value and
	stat focus is derived from PREFERRED_ABILITY_TYPES.
	"""

	rng = random.Random(seed)
	created: List[Player] = []
	atypes = list(const.CHARACTER_CLASS_MAP.keys())

	# If caller didn't request a specific ability type and there are enough
	# distinct types, pick unique types for the party to increase variety.
	unique_types = None
	if ability_type_focus is None and count <= len(atypes):
		
		unique_types = rng.sample(atypes, count)
		

	for i in range(count):
		# choose ability type per character (or use provided)
		if ability_type_focus:
			atype = ability_type_focus
		elif unique_types is not None:
			atype = unique_types[i]
		else:
			atype = rng.choice(atypes)
		# display name is the mapping value; append index to avoid duplicate names
		display_name = f"{CHARACTER_CLASS_MAP.get(atype, atype).strip()}"
		# derive stat focus from ability type
		stat_focus = atype# _derive_stat_focus_from_ability_type(atype)
		# pick a per-player seed so each generated character differs when a base seed is provided
		if isinstance(seed, int):
			pseed = int(seed) + i
		else:
			pseed = rng.randint(0,2**31 -1)
		# call generator once with per-player seed and derived stat focus
		res = generate_player(name=display_name, focus=stat_focus, target_level=level, seed=pseed, player_game= player_game)
		if isinstance(res, tuple) and len(res) ==2:
			p = res[0]
		else:
			p = res
		PLAYER_GAME.add_character(p)
		created.append(p)

	return created


def summarize_player(players: List[Player]) -> List[Dict[str, Any]]:
	"""Build summary dicts for a list of Player objects compatible with
	`format_player_summary` in the combat_balancing_simulation module.
	Returns a list of summary dicts in the same order as `players`.
	"""
	summaries: List[Dict[str, Any]] = []
	lookup = {a.get('id'): a for a in const_other.PLAYER_ABILITY_SEEDS }
	for p in players:
		abilities_info = []
		for aid in p.abilities:
			seed = lookup[aid]
			abilities_info.append({'id': aid, 'name': seed['name'], 'level': seed['level']})

		# inventory_info = []
		# for it in p.inventory:
		# 	# assume inventory items are proper item objects
		# 	inventory_info.append({'id': it.id, 'name': it.name, 'effect': it.effect})

		summary = {
			'name': p.name,
			'level': p.level,
			'max_hp': p.max_hp,
			'max_ap': p.max_ap,
			'strength': p.strength + ' + ' + (p.get_modified_strength() - p.strength),
			'dexterity': p.dexterity + ' + ' + (p.get_modified_dexterity() - p.dexterity),
			'constitution': p.constitution + ' + ' + (p.get_modified_constitution() - p.constitution),
			'intelligence': p.intelligence + ' + ' + (p.get_modified_intelligence() - p.intelligence),
			'equipped': {
				'weapon': p.equipped_weapon.name if p.equipped_weapon else None,
				'head': p.head_armor.name if p.head_armor else None,
				'body': p.body_armor.name if p.body_armor else None,
				'arms': p.arm_armor.name if p.arm_armor else None,
				'legs': p.leg_armor.name if p.leg_armor else None,
			},
			'abilities': abilities_info,
			#'inventory': inventory_info,
		}
		summaries.append(summary)
	return summaries


def main() -> None:
	parser = argparse.ArgumentParser(description="Run player generator for combat balancing tests")
	parser.add_argument("--name", default="Test", help="Player name")
	# make focus optional: if not provided, add_player will randomize per-character
	parser.add_argument("--focus", choices=list(CHARACTER_CLASS_MAP.keys()), default=None, help="Ability-type focus (use id from CHARACTER_CLASS_MAP). Omit to randomize per character")
	parser.add_argument("--level", type=int, default=10, help="Target player level")
	parser.add_argument("--seed", type=int, default=None, help="Random seed (int)")
	parser.add_argument("--count", type=int, default=1, help="Number of players to generate")

	args = parser.parse_args()

	player_game = PlayerGame()  # Instantiate PlayerGame
	# For this task: create 4 characters at level 15 and display them side-by-side
	players = add_player(count=4, level=15, ability_type_focus=args.focus, seed=args.seed, base_name=args.name, player_game=player_game)
	# build summaries
	summaries = summarize_player(players)


	# format boxes for each summary with consistent width
	box_width = 60
	all_boxes = [format_player_summary(s, player_game, box_width) for s in summaries]
	# compute max number of lines across boxes
	max_lines = max(len(b) for b in all_boxes) if all_boxes else 0

	# pad boxes to have equal number of lines
	for b in all_boxes:
		while len(b) < max_lines:
			b.append(' ' * box_width)

	# print lines side-by-side with two spaces between boxes
	for i in range(max_lines):
		row = ' '.join(b[i] for b in all_boxes)
		print(row)


if __name__ == "__main__":
	main()
