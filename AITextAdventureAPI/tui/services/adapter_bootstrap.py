"""
TEMPORARY adapter bootstrap shim.

Server Selection (not yet implemented — see `tui/README.md` roadmap) will
be responsible for explicitly configuring the save adapter (local vs.
online) via `client_api_requests.save_service_adapter.set_adapter(...)`
before ever pushing the "auth" screen, exactly like `old/console_game.py`'s
`auth_menu()` did.

Until that screen exists, `ensure_default_local_adapter()` configures a
local (SQLite-backed) adapter automatically the first time an auth-related
screen mounts, so Auth/Login/Register are usable standalone right now.

Delete this module (and its call sites in `auth_screen.py` /
`login_screen.py`) once Server Selection always configures the adapter
first.
"""
from __future__ import annotations

from client_api_requests.save_service_adapter import get_adapter, set_adapter
from client_api_requests.save_services.local_save_service import LocalSaveService
from client_api_requests.local_storage_service import LocalStorageAdapter


def ensure_default_local_adapter() -> None:
    """Configure a local save adapter if none has been set yet (no-op otherwise)."""
    try:
        get_adapter()
    except RuntimeError:
        set_adapter(LocalSaveService(LocalStorageAdapter()))


def current_adapter_mode() -> str:
    """Best-effort guess at whether the configured adapter is local or online.

    Used to populate `Session.mode` without Server Selection needing to pass
    explicit constructor arguments through screen navigation.
    """
    try:
        adapter = get_adapter()
    except RuntimeError:
        return "local"
    return "local" if isinstance(adapter, LocalSaveService) else "online"