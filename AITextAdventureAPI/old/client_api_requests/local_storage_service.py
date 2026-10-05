import os
import sqlite3
import json
import base64
import hashlib
import binascii
import datetime
from typing import Optional, Any, Dict, List

# Lightweight local adapter that mirrors the server Save model (no slot column).
class LocalStorageError(Exception):
    pass


class LocalStorageAdapter:
    """Local storage adapter that mirrors server Save model and ClientAPI surface.

    - No 'slot' column: saves are full records (name, blob, main_character, level, money, metadata).
    - Methods implemented: register, login, logout, list_saves, get_save, create_save, update_save, delete_save.
    - `blob` is stored as TEXT (JSON string or other); get_save returns parsed blob when possible.
    """

    def __init__(self, db_path: Optional[str] = None):
        if db_path:
            self.db_path = os.path.abspath(db_path)
        else:
            self.db_path = os.path.join(os.getcwd(), "ai_local_db.sqlite3")
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.access_token: Optional[str] = None
        self.refresh_token: Optional[str] = None
        self.current_user_id: Optional[int] = None
        self._ensure_db()

    def _connect(self):
        conn = sqlite3.connect(self.db_path, timeout=30, check_same_thread=False)
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.row_factory = sqlite3.Row
        return conn

    def _ensure_db(self):
        conn = self._connect()
        try:
            cur = conn.cursor()
            # users table
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            # saves table aligned with user_api.models.Save
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS saves (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    blob TEXT NOT NULL,
                    schema_version INTEGER NOT NULL DEFAULT 1,
                    metadata TEXT NULL,
                    main_character TEXT NULL,
                    level INTEGER NULL,
                    money INTEGER DEFAULT 0,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )
            conn.commit()
        finally:
            conn.close()

    # password helpers
    def _hash_password(self, password: str, salt: Optional[bytes] = None) -> str:
        if salt is None:
            salt = os.urandom(16)
        dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
        return binascii.hexlify(salt).decode() + "$" + binascii.hexlify(dk).decode()

    def _verify_password(self, password: str, stored: str) -> bool:
        try:
            salt_hex, dk_hex = stored.split("$")
            salt = binascii.unhexlify(salt_hex)
            expected = binascii.unhexlify(dk_hex)
            test = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100_000)
            return binascii.hexlify(test) == binascii.hexlify(expected)
        except Exception:
            return False

    # Auth
    def register(self, username: str, password: str) -> Dict[str, Any]:
        if not username or not password:
            raise LocalStorageError("username and password required")
        conn = self._connect()
        try:
            cur = conn.cursor()
            now = datetime.datetime.utcnow().isoformat()
            pw = self._hash_password(password)
            try:
                cur.execute(
                    "INSERT INTO users (username, password_hash, created_at) VALUES (?, ?, ?)",
                    (username, pw, now),
                )
                conn.commit()
                return {"id": cur.lastrowid}
            except sqlite3.IntegrityError:
                raise LocalStorageError("username already exists")
        finally:
            conn.close()

    def login(self, username: str, password: str) -> Dict[str, Any]:
        if not username or not password:
            raise LocalStorageError("username and password required")
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute("SELECT id, password_hash FROM users WHERE username = ?", (username,))
            row = cur.fetchone()
            if not row or not self._verify_password(password, row["password_hash"]):
                raise LocalStorageError("invalid username or password")
            uid = int(row["id"])
            self.current_user_id = uid
            token = base64.b64encode(os.urandom(18)).decode("utf-8")
            self.access_token = f"local-{uid}-{token}"
            self.refresh_token = None
            return {"id": uid, "access_token": self.access_token, "refresh_token": None}
        finally:
            conn.close()

    def logout(self, user_id: Optional[int] = None) -> bool:
        self.access_token = None
        self.refresh_token = None
        self.current_user_id = None
        return True

    # Save CRUD (ClientAPI-like)
    def list_saves(self) -> List[Dict[str, Any]]:
        if self.current_user_id is None:
            return []
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT id, name, main_character, level, money, updated_at FROM saves WHERE user_id = ? ORDER BY updated_at DESC",
                (self.current_user_id,),
            )
            rows = cur.fetchall()
            out: List[Dict[str, Any]] = []
            for r in rows:
                out.append(
                    {
                        "id": r["id"],
                        "name": r["name"],
                        "main_character": r["main_character"],
                        "level": r["level"],
                        "money": r["money"],
                        "updated_at": r["updated_at"],
                    }
                )
            return out
        finally:
            conn.close()

    def list_all_saves(self) -> List[Dict[str, Any]]:
        """Account-agnostic listing of every save in the DB.

        Unlike `list_saves()`, this ignores `current_user_id` so developer
        tooling can surface all saved games for loading as test fixtures
        without needing to know (or be logged in as) the owning account.
        """
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT id, user_id, name, main_character, level, money, updated_at FROM saves ORDER BY updated_at DESC",
            )
            rows = cur.fetchall()
            out: List[Dict[str, Any]] = []
            for r in rows:
                out.append(
                    {
                        "id": r["id"],
                        "user_id": r["user_id"],
                        "name": r["name"],
                        "main_character": r["main_character"],
                        "level": r["level"],
                        "money": r["money"],
                        "updated_at": r["updated_at"],
                    }
                )
            return out
        finally:
            conn.close()

    def get_save(self, save_id: int) -> Dict[str, Any]:
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(
                "SELECT id, user_id, name, blob, schema_version, metadata, main_character, level, money, created_at, updated_at FROM saves WHERE id = ?",
                (save_id,),
            )
            row = cur.fetchone()
            if not row:
                raise RuntimeError("save not found")
            blob_val = row["blob"]
            try:
                parsed = json.loads(blob_val) if isinstance(blob_val, str) else blob_val
            except Exception:
                parsed = blob_val
            return {
                "id": row["id"],
                "user_id": row["user_id"],
                "name": row["name"],
                "schema_version": row["schema_version"],
                "metadata": json.loads(row["metadata"]) if row["metadata"] else None,
                "blob": parsed,
                "main_character": row["main_character"],
                "level": row["level"],
                "money": row["money"],
                "updated_at": row["updated_at"],
                "created_at": row["created_at"],
            }
        finally:
            conn.close()

    def create_save(
        self, name: str, main_character: str, level: int, money: int, blob: str, schema_version: int = 1, metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        user_id = self.current_user_id or 0
        now = datetime.datetime.utcnow().isoformat()
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(
                """
                INSERT INTO saves (user_id, name, blob, schema_version, metadata, main_character, level, money, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    name or "autosave",
                    blob,
                    schema_version,
                    json.dumps(metadata) if metadata is not None else None,
                    main_character,
                    level,
                    money,
                    now,
                    now,
                ),
            )
            conn.commit()
            return {"id": cur.lastrowid}
        finally:
            conn.close()

    def update_save(
        self, save_id: int, name: str, main_character: str, level: int, money: int, blob: str, schema_version: int = 1, metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        now = datetime.datetime.utcnow().isoformat()
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute(
                """
                UPDATE saves
                SET name = ?, blob = ?, schema_version = ?, metadata = ?, main_character = ?, level = ?, money = ?, updated_at = ?
                WHERE id = ?
                """,
                (name, blob, schema_version, json.dumps(metadata) if metadata is not None else None, main_character, level, money, now, save_id),
            )
            conn.commit()
            return {"id": save_id}
        finally:
            conn.close()

    def delete_save(self, save_id: int) -> Dict[str, Any]:
        conn = self._connect()
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM saves WHERE id = ?", (save_id,))
            conn.commit()
            return {"id": save_id}
        finally:
            conn.close()
