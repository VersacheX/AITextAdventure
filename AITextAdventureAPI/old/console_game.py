# -*- coding: utf-8 -*-
import os
import logging
import json
import base64
import pickle
import re

from readchar import readkey

from console_game_gameloop import new_game, run_game_loop
# Use HTTP client for auth so console acts like a front-end and doesn't init DB directly
from client_api_requests.client_api_requests import ClientAPI
# new: use load_game_service helpers
from client_api_requests.load_game_service import load_player_games, load_player_game

# save adapter wiring
from client_api_requests.save_service_adapter import set_adapter, get_adapter
from client_api_requests.save_services.api_save_service import APISaveService
from client_api_requests.save_services.local_save_service import LocalSaveService
from client_api_requests.local_storage_service import LocalStorageAdapter

# Do NOT import or use the DB layer directly from the console application.
# The console must interact with the backend API only.


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# configure logging for debug runs
# --logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


def auth_menu():
    """Authentication menu: choose mode, then login/register/guest.

    This configures the global save adapter via `set_adapter(...)`. It uses
    the adapter's auth methods (register/login) so both Local and API modes
    behave the same from the UI perspective.

    Returns:
      - dict with keys: username, access_token, client  (client is underlying ClientAPI or LocalStorageAdapter)
      - None for guest
    """
    # create a default HTTP client for the online flow only
    default_http_client = None
    try:
        default_http_client = ClientAPI()
    except Exception:
        default_http_client = None

    user = None
    while not user:
        clear_screen()
        print("\n=== Authentication ===")
        # Ask mode selection first (local vs online)
        print("1) Play Local")
        print("2) Play Online")
        mode = input("Select an option (1-2): ").strip().lower()
        if mode in ("1", "local", "l"):
            # configure local adapter + service
            local_adapter = LocalStorageAdapter()
            local_service = LocalSaveService(local_adapter)
            set_adapter(local_service)
            # underlying auth client for later calls / token storage
            auth_client = local_adapter
            print("Play Local selected. Local save adapter configured.")
        elif mode in ("2", "online", "o"):
            # configure API-backed service
            api_client = ClientAPI()
            api_service = APISaveService(api_client)
            set_adapter(api_service)
            auth_client = api_client
            print("Play Online selected. API adapter configured.")
        else:
            print("Invalid selection. Choose 1 or 2.")
            readkey()
            continue

        # Normal auth flow (use adapter's auth methods)
        clear_screen()
        print("1) Login")
        print("2) Register")
        print("3) Continue as guest")
        print("4) Exit")
        choice = input("Select an option (1-4): ").strip().lower()

        if choice in ("1", "login", "l"):
            uname = input("Username: ").strip()
            pwd = input("Password: ").strip()

            # delegate to configured adapter for login (APISaveService or LocalSaveService)
            try:
                adapter = get_adapter()
                res = adapter.login(uname, pwd)
                # attempt to expose access_token if underlying client has it
                token = getattr(auth_client, "access_token", None)
                user = {"username": uname, "access_token": token, "client": auth_client}
                print(f"Logged in as {uname}")
                return user
            except Exception as ex:
                print("Login failed:", ex)
                readkey()
                continue

        elif choice in ("2", "register", "r"):
            uname = input("Choose a username: ").strip()
            pwd = input("Choose a password: ").strip()

            try:
                adapter = get_adapter()
                adapter.register(uname, pwd)
                # perform login after register
                adapter.login(uname, pwd)
                token = getattr(auth_client, "access_token", None)
                user = {"username": uname, "access_token": token, "client": auth_client}
                print(f"Registered and logged in as {uname}")
                return user
            except Exception as ex:
                print("Register failed:", ex)
                readkey()
                continue

        elif choice in ("3", "guest", "g"):
            print("Continuing as guest.")
            # keep adapter configured (allows local anonymous saves if desired)
            return None

        elif choice in ("4", "exit", "e"):
            print("Exiting.")
            raise SystemExit(0)

        else:
            print("Invalid selection. Choose 1-4.")


def load_game_menu(api):
    """List saves using the lightweight summaries and load a save using the central loader.

    Prefer the configured adapter (if any) so the selected backend is used.
    """
    if load_player_games is None or load_player_game is None:
        print("Save listing/loader service not available. Login and server support required.")
        return None

    # prefer configured adapter when available
    try:
        adapter = get_adapter()
    except Exception:
        adapter = None

    try:
        summaries = load_player_games(save_adapter=adapter)
    except Exception as e:
        print("Failed to fetch saves:", e)    
        readkey()
        return None

    if not summaries:
        print("No saves")
        readkey()
        return None

    print("Saves:")
    for idx, s in enumerate(summaries, start=1):
        print(
            f" {idx}) id={s.get('id')}: {s.get('name')} - {s.get('main_character')} Level:{s.get('level')} Money:{s.get('money')} Modified:{s.get('updated_at')}"

        )

    pick = input("Enter save index to load (or press Enter to cancel): ")
    if not pick:
        return None

    sel = None
    num = int(pick)
    if 1 <= num <= len(summaries):
        sel = summaries[num - 1]

    if not sel:
        print("No matching save found")
        return None

    sid = sel.get("id")
    try:
        pg = load_player_game(sid, save_adapter=adapter)
    except Exception as e:
        print("Failed to load save:", e)
        return None

    if pg is None:
        print("Save blob format not recognized or missing")
        return None

    print(f"Loaded save id={sid}, starting game...")
    return pg


def main_menu():
    # Run auth menu first
    current_user = auth_menu()

    while True:
        clear_screen()
        print("\n=== Fracture (Console Prototype) ===")
        print("1) New Game")
        print("2) Load Game")
        print("3) Logout")
        print("4) Exit")
        choice = input("Select an option (1-4): ").strip().lower()

        if choice in ("1", "new", "new game", "n"):
            api = current_user["client"]
            new_game(api)

        elif choice in ("2", "load", "l"):
            if current_user and isinstance(current_user, dict) and current_user.get("client"):
                api = current_user["client"]
                pg = load_game_menu(api)
                if pg is not None:
                    # run_game_loop expects a PlayerGame and a viewport tuple (width, height, radius)
                    viewport = (75, 25, 4)
                    run_game_loop(pg, viewport, api)
                # otherwise return to main menu
            else:
                print("Load game requires login. Please login via the Authentication menu.")

        elif choice in ("3", "logout", "o"):
            print("Logging out...")
            current_user = auth_menu()

        elif choice in ("4", "exit", "e"):
            print("Exiting. Goodbye.")
            break

        else:
            print("Invalid selection. Please choose 1-4.")


if __name__ == "__main__":
    """
    Entry point for the console game.
    run pyinstaller fracture.spec to build executable.
    """
    main_menu()
