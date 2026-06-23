from typing import Any, List, Dict, Optional


def is_healing_item(it: Any) -> bool:
	"""Return True if `it` appears to be a healing/utility item.

	Accepts either object instances or dict-like seeds.
	"""
	if it is None:
		return False

	# dict-like
	if isinstance(it, dict):
		name = str(it.get("name", "")).lower()
		cat = str(it.get("category_name", "")).lower()
		if "utility" in cat:
			return True
		if any(k in name for k in ("heal", "herb", "stimpak", "elixir")):
			return True
		if any(k in it for k in ("effect", "heal_fraction", "ap_fraction")):
			return True
		return False

	# object-like
	name = str(getattr(it, "name", "")).lower()
	cat = str(getattr(it, "category_name", "")).lower()

	if "utility" in cat:
		return True
	if any(k in name for k in ("heal", "herb", "stimpak", "elixir")):
		return True
	if getattr(it, "effect", None) is not None:
		return True
	if getattr(it, "heal_fraction", None) is not None:
		return True
	if getattr(it, "ap_fraction", None) is not None:
		return True

	return False


def find_healing_item_index(player_game: Any) -> Optional[int]:
	"""Return inventory index of a healing item or None if none available."""
	inv = player_game.inventory
	for i, it in enumerate(inv):
		if is_healing_item(it):
			return i
	return None


def player_ai_take_turn(player: Any, hostile: Any, player_game) -> List[str]:
	"""Perform a single AI-controlled player turn against `hostile`.

	Strategy:
	- If player HP is low (<=1/3 of max) attempt to use a healing item.
	- Otherwise perform `player.attack(hostile)`.

	Returns list of log lines describing actions/outcomes.
	"""
	logs: List[str] = []

	max_hp = player.max_hp
	current_hp = player.current_hp

	# heal threshold:1/3 of max_hp (at least1)
	heal_threshold = max(1, max_hp //3) if max_hp >0 else 1

	# Attempt to heal if at or below threshold
	if current_hp <= heal_threshold:
		idx = find_healing_item_index(player_game)
		if idx is not None:
			inv = player_game.inventory

			item = inv[idx]
			item_name = item.name

			res = player.use_item(idx, player_game)
			if isinstance(res, dict) and res.get("used"):
				logs.append(f"AI used {item_name} to recover.")
				return logs

	# Perform attack
	res = player.attack(hostile)

	if isinstance(res, dict):
		hit = bool(res.get("hit"))
		dmg = int(res.get("applied", res.get("damage",0)) or 0)
		if not hit:
			logs.append("AI attacks but misses.")
		else:
			logs.append(f"AI attacks and deals {dmg} damage to {hostile.name}.")
	else:
		logs.append("AI attacks but no result was produced.")

	return logs


def hostile_take_turn(hostile: Any, player: Any) -> List[str]:
	"""Hostile performs its turn against `player`. Returns logs."""
	logs: List[str] = []
	
	res = hostile.attack(player)

	if isinstance(res, dict):
		hit = bool(res.get("hit"))
		dmg = int(res.get("applied", res.get("damage",0)) or 0)
		if not hit:
			logs.append(f"{getattr(hostile, 'name', 'Hostile')} attacks but misses.")
		else:
			logs.append(f"{getattr(hostile, 'name', 'Hostile')} hits for {dmg} damage.")

	return logs


def run_combat(player: Any, hostile: Any, max_rounds: int =200) -> Dict[str, Any]:
	"""Simulate a combat until one side dies or max_rounds reached.

	Returns a dict: { 'winner': 'player'|'hostile'|'draw', 'rounds': int, 'log': [str,...] }
	"""
	logs: List[str] = []
	rounds =0

	while (
		rounds < max_rounds
		and player.is_alive()
		and hostile.is_alive()
		):
		rounds +=1
		logs.append(f"-- Round {rounds} --")

		# player's turn
		logs.extend(player_ai_take_turn(player, hostile))
		if not hostile.is_alive():
			logs.append(f"{player.name} defeated {hostile.name}.")
			return {"winner": "player", "rounds": rounds, "log": logs}

		# hostile's turn
		logs.extend(hostile_take_turn(hostile, player))
		if not player.is_alive():
			logs.append(f"{hostile.name} defeated {player.name}.")
			return {"winner": "hostile", "rounds": rounds, "log": logs}

	# no winner within max rounds -> draw
	logs.append("Combat ended in a draw.")
	return {"winner": "draw", "rounds": rounds, "log": logs}
