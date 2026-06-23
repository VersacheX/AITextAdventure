from typing import List, Dict, Any, Optional
import json
import base64
import pickle

from client_api_requests.client_api_requests import ClientAPI

try:
	from game.objects.player_game import PlayerGame
except Exception:
	PlayerGame = None


def _try_unpickle_b64(b64: str) -> Optional[Any]:
	raw = base64.b64decode(b64)
	return pickle.loads(raw)


def load_player_games(save_adapter: Any = None) -> List[Dict[str, Any]]:
	"""Return lightweight list of saves with only the fields required by the UI:
	[{id, main_character, level, money, updated_at}, ...]
	"""
	api = save_adapter or ClientAPI()
	try:
		saves = api.list_saves()
	except Exception as e:
		input(e)
		return []

	out: List[Dict[str, Any]] = []
	if not isinstance(saves, list):
		return out

	for s in saves:
		sid = s.get('id')
		# Prefer explicit top-level fields
		main_character = s.get('main_character')
		name = s.get('name')
		level = s.get('level')
		money = s.get('money')
		last_mod = s.get('updated_at')

		out.append({'id': sid, 'name': name, 'main_character': main_character, 'level': level, 'money': money, 'updated_at': last_mod})

	return out


def load_player_game(save_id: int, save_adapter: Any = None) -> Optional[Any]:
	"""Load a specific save by id and return an unpickled PlayerGame, or None on failure.
	Attempts common blob locations and falls back to metadata['pickle_b64'].
	"""
	api = save_adapter or ClientAPI()
	try:
		sv = api.get_save(save_id)
	except Exception:
		return None

	if not isinstance(sv, dict):
		return None

	#1) check top-level 'blob' / 'payload' / 'data'
	blob = sv.get('blob')

	# If blob is a dict containing 'pickle' key
	if isinstance(blob, dict):
		p = blob.get('pickle')
		if isinstance(p, str):
			pg = _try_unpickle_b64(p)
			if pg is not None:
				pg.save_id = save_id
				return pg

	return None