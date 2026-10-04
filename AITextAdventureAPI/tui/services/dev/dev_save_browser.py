"""
dev_save_browser: account-agnostic save listing/loading for the dev TUI.

The dev TUI (`run_dev_tui.py`) boots straight into the data-management
screen, skipping the normal title -> server-select -> auth flow. That means
no `SaveService` adapter is configured and nobody is "logged in", so the
production, user-scoped `SaveService.list_saves()` would return an empty
list. Developers don't care which account owns a save -- they just want to
surface every saved game and load one into memory as a test fixture (so a
world-reshaping test can start from a real late-game state instead of
replaying hours of content).

This module therefore:

  * Lazily configures a Local SQLite adapter if none is set yet, so the dev
    TUI works without going through Server Selection.
  * Lists *all* saves regardless of owner via
    `LocalStorageAdapter.list_all_saves()`.
  * Reuses the adapter-only `tui.services.save_transfer.load_player_game()`
    for the actual blob -> PlayerGame deserialization, so there is no
    `ClientAPI`/`requests` import and no blocking `input()` anywhere on this
    path (both unsafe under a Textual background worker).

All functions here are safe to call from a `@work(thread=True)` worker.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


def _get_local_adapter():
    """Return a configured Local adapter, configuring one if needed.

    Dev tooling is local-only: if the global adapter hasn't been set (because
    Server Selection was skipped), configure a local SQLite adapter on the
    fly. If an Online adapter happens to be configured, fall back to a fresh
    local adapter instead, since account-agnostic listing is a local concept.
    """
    from client_api_requests.save_service_adapter import get_adapter
    from client_api_requests.save_services.local_save_service import LocalSaveService
    from client_api_requests.local_storage_service import LocalStorageAdapter

    try:
        adapter = get_adapter()
    except Exception:
        adapter = None

    if isinstance(adapter, LocalSaveService):
        return adapter.local_adapter

    # No adapter yet, or a non-local one -> configure a local adapter so dev
    # listing works without login/server selection.
    from tui.services.server_config import configure_local

    configure_local()
    return get_adapter().local_adapter


def list_all_saves() -> List[Dict[str, Any]]:
    """Return every saved game across all accounts, newest first.

    Each entry is a lightweight metadata dict (id, user_id, name,
    main_character, level, money, updated_at) -- never the full blob.
    """
    local = _get_local_adapter()
    raw = local.list_all_saves()
    return raw if isinstance(raw, list) else []


def load_save_into_memory(save_id: Any) -> Optional[Any]:
    """Load a save by id and return the deserialized PlayerGame.

    Account-agnostic: `get_save()` fetches by primary key regardless of
    owner. Raises RuntimeError (from `save_transfer`) with an explicit reason
    on failure so the caller can surface it.
    """
    from client_api_requests.save_service_adapter import get_adapter
    from tui.services.save_transfer import load_player_game

    # Ensure an adapter is configured before load_player_game() asks for one.
    _get_local_adapter()
    adapter = get_adapter()
    return load_player_game(save_id, adapter)
