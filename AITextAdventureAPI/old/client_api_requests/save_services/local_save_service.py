"""Local SaveService implementation (delegates to LocalStorageAdapter)."""

from typing import Any, Dict, Optional, List

from ..save_service_interface import SaveService
from ..local_storage_service import LocalStorageAdapter  # type: ignore


class LocalSaveService(SaveService):
    def __init__(self, local_adapter: LocalStorageAdapter):
        self.local_adapter = local_adapter

    def list_saves(self) -> List[Dict[str, Any]]:
        return self.local_adapter.list_saves()

    def get_save(self, save_id: Any) -> Dict[str, Any]:
        return self.local_adapter.get_save(int(save_id))

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
        return self.local_adapter.create_save(name, main_character, level, money, blob, schema_version, metadata)

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
        return self.local_adapter.update_save(int(save_id), name, main_character, level, money, blob, schema_version, metadata)

    def delete_save(self, save_id: Any) -> Dict[str, Any]:
        return self.local_adapter.delete_save(int(save_id))

    def register(self, username: str, password: str) -> Any:
        return self.local_adapter.register(username, password)

    def login(self, username: str, password: str) -> Any:
        return self.local_adapter.login(username, password)

    def logout(self, user_id: Any = None) -> bool:
        return self.local_adapter.logout(user_id)
