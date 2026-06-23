"""SaveService interface used by console UI to interact with saves.

Define an abstract interface that both the online API-backed implementation
and the local sqlite-backed implementation will implement.

This interface mirrors the ClientAPI surface and adds simple auth methods so
adapters can be used interchangeably where code expects register/login/logout.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class SaveService(ABC):
    """Abstract save service that mirrors the HTTP ClientAPI surface."""

    @abstractmethod
    def list_saves(self) -> List[Dict[str, Any]]:
        """Return a list of save summary dicts as the API returns them."""
        raise NotImplementedError()

    @abstractmethod
    def get_save(self, save_id: Any) -> Dict[str, Any]:
        """Return the raw save object/dict for the given save id (same shape as ClientAPI.get_save)."""
        raise NotImplementedError()

    @abstractmethod
    def create_save(
        self,
        name: str,
        main_character: str,
        level: int,
        money: int,
        blob: str,
        schema_version: int = 1,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Create a save. Signature matches ClientAPI.create_save."""
        raise NotImplementedError()

    @abstractmethod
    def update_save(
        self,
        save_id: Any,
        name: str,
        main_character: str,
        level: int,
        money: int,
        blob: str,
        schema_version: int = 1,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Update a save. Signature matches ClientAPI.update_save."""
        raise NotImplementedError()

    @abstractmethod
    def delete_save(self, save_id: Any) -> Dict[str, Any]:
        """Delete a save. Signature matches ClientAPI.delete_save."""
        raise NotImplementedError()

    # Authentication helpers so adapter can be used directly for auth flows
    @abstractmethod
    def register(self, username: str, password: str) -> Any:
        """Register a user. Return provider-specific result (dict/int)."""
        raise NotImplementedError()

    @abstractmethod
    def login(self, username: str, password: str) -> Any:
        """Login a user. Return provider-specific result (dict/int)."""
        raise NotImplementedError()

    @abstractmethod
    def logout(self, user_id: Any = None) -> bool:
        """Logout user / clear session tokens. Return True on success."""
        raise NotImplementedError()
