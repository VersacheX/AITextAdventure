"""
DEPRECATED: replaced by `tui.services.server_config`.

`ServerSelectScreen` (`tui/screens/server_select_screen.py`) now always
configures the save adapter via `server_config.configure_local()` /
`configure_online()` before `auth` is ever reached, so the "configure a
default local adapter on first auth-screen mount" shim this module
provided is no longer needed. Nothing in `tui/` imports this module
anymore; it is kept only as a pointer for anything external that might
still reference it, and can be deleted outright.
"""
from __future__ import annotations

from tui.services.server_config import configure_local, current_mode  # noqa: F401


def ensure_default_local_adapter() -> None:
    """Deprecated — use `tui.services.server_config.configure_local()`
    from `ServerSelectScreen` instead."""
    configure_local()


def current_adapter_mode() -> str:
    """Deprecated — use `tui.services.server_config.current_mode()` instead."""
    return current_mode()