"""API-backed SaveService implementation.

Thin wrapper that mirrors ClientAPI method signatures so existing helpers
(`save_game_service.py` and `load_game_service.py`) can use an adapter
interchangeably with ClientAPI. Also exposes register/login/logout.
"""
from typing import Any, Dict, Optional, List

from ..save_service_interface import SaveService
from ..client_api_requests import ClientAPI  # type: ignore


class APISaveService(SaveService):
    def __init__(self, client: ClientAPI):
        """Wrap a ClientAPI instance (should be authenticated by caller)."""
        self.client = client

    def list_saves(self) -> List[Dict[str, Any]]:
        return self.client.list_saves()

    def get_save(self, save_id: Any) -> Dict[str, Any]:
        return self.client.get_save(save_id)

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
        return self.client.create_save(
            name=name,
            main_character=main_character,
            level=level,
            money=money,
            blob=blob,
            schema_version=schema_version,
            metadata=metadata,
        )

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
        return self.client.update_save(
            save_id=save_id,
            name=name,
            main_character=main_character,
            level=level,
            money=money,
            blob=blob,
            schema_version=schema_version,
            metadata=metadata,
        )

    def delete_save(self, save_id: Any) -> Dict[str, Any]:
        return self.client.delete_save(save_id)

    # Auth methods
    def register(self, username: str, password: str) -> Any:
        return self.client.register(username, password)

    def login(self, username: str, password: str) -> Any:
        return self.client.login(username, password)

    def logout(self, user_id: Any = None) -> bool:
        # ClientAPI has no logout endpoint; clear tokens client-side
        try:
            self.client.access_token = None
            self.client.refresh_token = None
            # also clear environment keys if present
            import os

            os.environ.pop("API_ACCESS_TOKEN", None)
            os.environ.pop("API_REFRESH_TOKEN", None)
        except Exception:
            pass
        return True
