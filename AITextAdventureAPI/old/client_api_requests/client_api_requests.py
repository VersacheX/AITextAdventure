import os
import json
from typing import Any, Dict, Optional

import requests

# load local .env if available
try:
    from dotenv import load_dotenv
    base = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(os.path.normpath(base))
except Exception:
    pass

DEFAULT_BASE = os.environ.get('API_SERVER_URL', 'http://127.0.0.1:2222')


class ClientAPI:
    def __init__(self, base_url: Optional[str] = None) -> None:
        self.base_url = (base_url or DEFAULT_BASE).rstrip('/')
        # try to pick up persisted tokens from environment
        self.access_token: Optional[str] = os.environ.get('API_ACCESS_TOKEN')
        self.refresh_token: Optional[str] = os.environ.get('API_REFRESH_TOKEN')

    def _auth_headers(self) -> Dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"
        return headers

    def register(self, username: str, password: str) -> Dict[str, Any]:
        url = f"{self.base_url}/api/auth/register"
        payload = {"username": username, "password": password}
        r = requests.post(url, json=payload)
        r.raise_for_status()
        return r.json()

    def login(self, username: str, password: str) -> Dict[str, Any]:
        # OAuth2 password form
        url = f"{self.base_url}/api/auth/token"
        payload = {"username": username, "password": password}
        r = requests.post(url, data=payload)
        r.raise_for_status()
        data = r.json()
        # token response may include refresh_token
        self.access_token = data.get('access_token')
        self.refresh_token = data.get('refresh_token')
        # persist tokens to environment for other ClientAPI instances
        if self.access_token:
            os.environ['API_ACCESS_TOKEN'] = self.access_token
        if self.refresh_token:
            os.environ['API_REFRESH_TOKEN'] = self.refresh_token
        return data

    def refresh(self) -> Dict[str, Any]:
        if not self.refresh_token:
            raise RuntimeError('no refresh token available')
        url = f"{self.base_url}/api/auth/token/refresh"
        r = requests.post(url, json={"refresh_token": self.refresh_token})
        r.raise_for_status()
        data = r.json()
        self.access_token = data.get('access_token')
        if self.access_token:
            os.environ['API_ACCESS_TOKEN'] = self.access_token
        return data




    #########################    # Save game methods
    def list_saves(self) -> Dict[str, Any]:
        url = f"{self.base_url}/api/auth/saves"
        r = requests.get(url, headers=self._auth_headers())
        r.raise_for_status()
        data = r.json()

        return data

    def create_save(self, 
                    name: str, 
                    main_character: str, 
                    level: int, 
                    money: int, 
                    blob: str, 
                    schema_version: int = 1, 
                    metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/api/auth/saves"
        payload = {"name": name, 
                   "main_character": main_character, 
                   "level": level, 
                   "money": money, 
                   "blob": blob, 
                   "schema_version": schema_version, 
                   "metadata": metadata}
        r = requests.post(url, headers=self._auth_headers(), json=payload)
        r.raise_for_status()
        return r.json()

    def update_save(self, 
                    save_id: int, 
                    name: str, 
                    main_character: str, 
                    level: int, 
                    money: int, 
                    blob: str, 
                    schema_version: int = 1, 
                    metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/api/auth/saves/{save_id}"
        payload = {"name": name, 
                   "main_character": main_character, 
                   "level": level, 
                   "money": money, 
                   "blob": blob, 
                   "schema_version": schema_version, 
                   "metadata": metadata}
        r = requests.put(url, headers=self._auth_headers(), json=payload)
        r.raise_for_status()
        return r.json()

    def get_save(self, save_id: int) -> Dict[str, Any]:
        url = f"{self.base_url}/api/auth/saves/{save_id}"
        r = requests.get(url, headers=self._auth_headers())
        r.raise_for_status()
        return r.json()

    def delete_save(self, save_id: int) -> Dict[str, Any]:
        url = f"{self.base_url}/api/auth/saves/{save_id}"
        r = requests.delete(url, headers=self._auth_headers())
        r.raise_for_status()
        return r.json()


# # Small script usage when executed directly
# if __name__ == '__main__':
#     cli = ClientAPI()
#     print('Base URL:', cli.base_url)
#     # Quick interactive demo
#     import getpass
#     print('1) register\n2) login')
#     choose = input('choice: ').strip()
#     if choose == '1':
#         u = input('username: ')
#         p = getpass.getpass('password: ')
#         print(cli.register(u, p))
#     elif choose == '2':
#         u = input('username: ')
#         p = getpass.getpass('password: ')
#         print(cli.login(u, p))
#     else:
#         print('no-op')
