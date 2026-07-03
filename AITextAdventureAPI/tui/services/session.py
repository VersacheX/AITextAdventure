"""
Session: tiny process-wide singleton tracking the current user/save-mode.

This does not replace `client_api_requests.save_service_adapter` (which
still owns the actual `SaveService` instance) — it just remembers who is
logged in and how, so screens like the future Main Menu can display
"Logged in as <username>" / offer "Logout" without re-deriving that from
the adapter each time.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Session:
    """Describes the current play mode and (optionally) logged-in user."""

    mode: str  # "local" or "online"
    username: Optional[str] = None
    is_guest: bool = False

    @property
    def is_authenticated(self) -> bool:
        return bool(self.username) and not self.is_guest


_session: Optional[Session] = None


def set_session(session: Optional[Session]) -> None:
    """Set (or clear, with None) the current session."""
    global _session
    _session = session


def get_session() -> Optional[Session]:
    """Return the current session, or None if nobody has signed in yet."""
    return _session