"""
ServerConfig: configures which SaveService backend (Local SQLite vs. Online
API) is active, and centralizes the connectivity check for Online mode.

This is the "better service" Server Selection needs to accommodate both
backends, replacing the temporary `adapter_bootstrap` shim. It mirrors what
`old/console_game.py`'s `auth_menu()` did inline, but returns actionable
results instead of printing to stdout, since it's called from a Textual
background worker (see `tui/screens/server_select_screen.py`).

Both `configure_local()` and `configure_online()` only import their backing
adapter (`LocalStorageAdapter` / `ClientAPI`) *inside* the function body,
not at module import time. `client_api_requests.client_api_requests
.ClientAPI` imports the `requests` package eagerly at module scope --
deferring the import here means choosing Local never touches `requests` at
all, so it isn't a hard dependency for players who never select Online.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional, Tuple

from client_api_requests.save_service_adapter import set_adapter

DEFAULT_ONLINE_BASE_URL = os.environ.get("API_SERVER_URL", "http://127.0.0.1:2222")


@dataclass
class ServerConfig:
    """Describes which backend is configured and how to reach it."""

    mode: str  # "local" or "online"
    base_url: Optional[str] = None  # only meaningful when mode == "online"


_config: Optional[ServerConfig] = None


def get_server_config() -> Optional[ServerConfig]:
    """Return the last-applied server configuration, or None if Server
    Selection hasn't run yet this session."""
    return _config


def current_mode() -> str:
    """Best-effort mode label for `Session.mode`. Defaults to "local" if
    Server Selection hasn't configured anything yet (shouldn't happen in
    normal flow, since `title` always routes there before `auth`)."""
    return _config.mode if _config else "local"


def configure_local(db_path: Optional[str] = None) -> ServerConfig:
    """Configure and activate the local SQLite-backed save adapter."""
    from client_api_requests.save_services.local_save_service import LocalSaveService
    from client_api_requests.local_storage_service import LocalStorageAdapter

    set_adapter(LocalSaveService(LocalStorageAdapter(db_path)))
    global _config
    _config = ServerConfig(mode="local")
    return _config


def test_online_connection(base_url: str, timeout: float = 4.0) -> Tuple[bool, str]:
    """Best-effort reachability check for an Online server's `/health`
    endpoint. Safe to call from a background worker; performs a real
    blocking HTTP request with a short timeout so a dead/unreachable server
    fails fast instead of hanging.

    Returns (True, "ok") on success, or (False, <reason>) otherwise.
    """
    try:
        import requests
    except ImportError:
        return False, "The 'requests' package is required for Online mode (pip install requests)."

    url = base_url.rstrip("/") + "/health"
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except Exception as exc:  # noqa: BLE001 - reason is surfaced to the user
        return False, str(exc)
    return True, "ok"


def configure_online(base_url: Optional[str] = None) -> ServerConfig:
    """Configure and activate the API-backed save adapter for `base_url`
    (or `ClientAPI`'s own default if omitted). Does not itself verify
    reachability -- call `test_online_connection()` first if you want to
    fail fast with a friendly message."""
    from client_api_requests.client_api_requests import ClientAPI
    from client_api_requests.save_services.api_save_service import APISaveService

    client = ClientAPI(base_url) if base_url else ClientAPI()
    set_adapter(APISaveService(client))
    global _config
    _config = ServerConfig(mode="online", base_url=client.base_url)
    return _config