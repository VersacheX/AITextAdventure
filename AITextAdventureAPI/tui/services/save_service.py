"""
save_service: TUI adapter for serialising and persisting a PlayerGame.

Mirrors `old/client_api_requests/save_game_service.save_player_game()` but
uses the already-configured SaveService adapter
(`client_api_requests.save_service_adapter`) directly — no `ClientAPI` or
`requests` import anywhere in this call chain, matching the pattern
established by `tui/services/save_transfer.py` for loading.

Logic (mirrors legacy `save_game_service.py`):
  - `name` provided AND differs from current slot → create a new save slot,
    update ``pg.name`` and ``pg.save_id``.
  - `name` absent/empty → overwrite the existing slot via ``pg.save_id``
    if one exists, otherwise fall back to creating a new slot.
"""
from __future__ import annotations

import base64
import json
import pickle
from datetime import datetime
from typing import Any, Optional, Tuple


def save_player_game(
    pg: Any,
    name: Optional[str] = None,
) -> Tuple[bool, str]:
    """Serialise ``pg`` and persist it via the configured SaveService adapter.

    Args:
        pg:   the active PlayerGame instance.
        name: if provided (non-empty), creates a new save slot with this name
              and updates ``pg.name`` / ``pg.save_id`` to point at it.
              If None or empty, overwrites the existing slot identified by
              ``pg.save_id`` (if present) or creates a new slot otherwise.

    Returns:
        ``(success: bool, message: str)`` — message is user-readable.
    """
    from client_api_requests.save_service_adapter import get_adapter  # noqa: PLC0415

    try:
        adapter = get_adapter()
    except RuntimeError as exc:
        return False, f"Save unavailable: {exc}"

    try:
        # resolve final name
        stripped = name.strip() if name and name.strip() else None
        final_name = stripped or getattr(pg, "name", None) or (
            "autosave - " + datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        )
        pg.name = final_name

        # serialise to base64-encoded pickle (same format as load path)
        blob_bytes = pickle.dumps(pg)
        blob_b64 = base64.b64encode(blob_bytes).decode("utf-8")
        payload = json.dumps({"pickle": blob_b64})

        main_char = pg.characters[0].name if getattr(pg, "characters", None) else "Unknown"
        level = pg.get_max_character_level()
        money = int(getattr(pg, "money", 0))

        sid = getattr(pg, "save_id", None)

        if sid is not None and not stripped:
            # overwrite existing slot — name unchanged
            res = adapter.update_save(
                sid, final_name, main_char, level, money, payload, schema_version=1
            )
            result_id = res.get("id")
        else:
            # new slot (explicit name given, or no save_id exists yet)
            res = adapter.create_save(
                final_name, main_char, level, money, payload, schema_version=1
            )
            new_id = res.get("id")
            pg.save_id = new_id
            result_id = new_id

        msg = f"Saved: {final_name}"
        if result_id is not None:
            msg += f"  (slot {result_id})"
        return True, msg

    except Exception as exc:  # noqa: BLE001 — surfaced as user-readable text
        return False, f"Save failed: {exc}"