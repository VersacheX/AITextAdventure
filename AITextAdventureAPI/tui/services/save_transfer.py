"""
save_transfer: adapter-only save deserialization for the TUI.

Replaces `tui/` screens' use of `client_api_requests.load_game_service
.load_player_game()`. That `old/` module imports
`client_api_requests.client_api_requests.ClientAPI` at module scope, which
eagerly `import requests` at module scope too -- so merely importing it
(even to call a function that never touches the network) requires
`requests` to be installed. Under Local mode, that has no reason to be a
hard dependency, but it crashed exactly this way when
`LoadGameScreen` loaded a save:

    ModuleNotFoundError: No module named 'requests'

This module reimplements only the piece `LoadGameScreen` actually needs,
using nothing but the already-configured `SaveService` adapter
(`client_api_requests.save_service_adapter.get_adapter()`) and the standard
library (`base64`, `pickle`) -- no `ClientAPI`/`requests` import anywhere
in this file or its call chain.
"""
from __future__ import annotations

import base64
import json
import pickle
from typing import Any

from client_api_requests.save_service_interface import SaveService


def load_player_game(save_id: Any, adapter: SaveService) -> Any:
    """Load a specific save by id and return an unpickled PlayerGame.

    Raises RuntimeError with an explicit reason on any failure so callers
    (UI/background worker) can show a useful message to the user.
    """
    # 1) fetch the save record from the configured adapter
    try:
        save = adapter.get_save(save_id)
    except Exception as exc:
        raise RuntimeError(f"adapter.get_save failed: {exc}") from exc

    if not isinstance(save, dict):
        raise RuntimeError("adapter.get_save returned unexpected shape (not a dict)")

    # 2) normalize blob to a dict (server clients may return a JSON string)
    blob = save.get("blob")
    if blob is None:
        raise RuntimeError("save record missing 'blob' field")

    if isinstance(blob, str):
        try:
            blob = json.loads(blob)
        except Exception as exc:
            # surface a short excerpt to help identify corruption/format mismatch
            excerpt = (blob[:200] + "...") if len(blob) > 200 else blob
            raise RuntimeError(f"'blob' is a JSON string but json.loads() failed: {exc}. blob excerpt: {excerpt}") from exc

    if not isinstance(blob, dict):
        raise RuntimeError(f"'blob' field is not an object after normalization (type={type(blob).__name__})")

    # 3) locate the base64-encoded pickle inside blob
    pickle_b64 = blob.get("pickle")
    if not isinstance(pickle_b64, str):
        raise RuntimeError("'blob' does not contain a 'pickle' string")

    # 4) decode base64
    try:
        raw = base64.b64decode(pickle_b64)
    except Exception as exc:
        excerpt = (pickle_b64[:200] + "...") if len(pickle_b64) > 200 else pickle_b64
        raise RuntimeError(f"base64 decode failed: {exc}. pickle excerpt: {excerpt}") from exc

    # 5) unpickle safely (may raise)
    try:
        player_game = pickle.loads(raw)
    except Exception as exc:
        raise RuntimeError(f"pickle.loads failed: {exc}") from exc

    # attach save_id for downstream consumers (same behavior as old loader)
    try:
        setattr(player_game, "save_id", save_id)
    except Exception:
        # non-critical: ignore if attribute cannot be set
        pass

    return player_game