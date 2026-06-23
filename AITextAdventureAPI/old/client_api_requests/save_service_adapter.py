"""Runtime adapter selector for save services.

Exposes a global adapter and top-level functions that mirror the ClientAPI
methods plus auth helpers (register/login/logout). This allows existing
helpers and the console to use the configured adapter interchangeably.
"""
from typing import Optional, Any, Dict, List

from .save_service_interface import SaveService

_adapter: Optional[SaveService] = None


def set_adapter(adapter: SaveService) -> None:
    """Set the global save service adapter to use at runtime."""
    global _adapter
    _adapter = adapter


def get_adapter() -> SaveService:
    """Return the configured save adapter or raise if none set."""
    if _adapter is None:
        raise RuntimeError("SaveService adapter not configured. Call set_adapter() at startup.")
    return _adapter


# Delegating functions that mirror ClientAPI signatures so existing helpers can use them
def list_saves() -> List[Dict[str, Any]]:
    return get_adapter().list_saves()


def get_save(save_id: Any) -> Dict[str, Any]:
    return get_adapter().get_save(save_id)


def create_save(
    name: str,
    main_character: str,
    level: int,
    money: int,
    blob: str,
    schema_version: int = 1,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    return get_adapter().create_save(name, main_character, level, money, blob, schema_version, metadata)


def update_save(
    save_id: Any,
    name: str,
    main_character: str,
    level: int,
    money: int,
    blob: str,
    schema_version: int = 1,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    return get_adapter().update_save(save_id, name, main_character, level, money, blob, schema_version, metadata)


def delete_save(save_id: Any) -> Dict[str, Any]:
    return get_adapter().delete_save(save_id)


# Auth delegations
def register(username: str, password: str) -> Any:
    return get_adapter().register(username, password)


def login(username: str, password: str) -> Any:
    return get_adapter().login(username, password)


def logout(user_id: Any = None) -> bool:
    return get_adapter().logout(user_id)
