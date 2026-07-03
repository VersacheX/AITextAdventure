"""
Authentication screen: login, register, or guest access.
"""
from typing import Optional, Dict, Any
from tui.core.screen_manager import Screen, ScreenType
from tui.core.renderer import clear_screen, make_box, center_box_in_terminal
from tui.core.input_handler import InputHandler


class AuthScreen(Screen):
    """
    Authentication screen for login/register/guest access.

    Uses the configured save adapter for authentication.
    """

    def __init__(self, manager):
        super().__init__(manager)
        self.user_context: Optional[Dict[str, Any]] = None
        self.options = [
            ("1", "Login", "login"),
            ("2", "Register", "register"),
            ("3", "Continue as Guest", "guest"),
            ("4", "Back", "back"),
            ("Q", "Exit", "exit")
        ]

    def render(self) -> None:
        """Render the authentication screen."""
        clear_screen()

        # Title
        title = ["=== Authentication ===", ""]
        title_box = make_box(title, 60, center_content=True)

        # Options
        options_content = [""]
        for key, label, _ in self.options:
            options_content.append(f"{key}) {label}")
        options_content.append("")

        options_box = make_box(options_content, 60)

        # Combine and center
        all_lines = title_box + [""] + options_box
        centered = center_box_in_terminal(all_lines)

        for line in centered:
            print(line)

    def handle_input(self, key: Optional[str] = None) -> Optional[str]:
        """Handle authentication input."""
        if key is None:
            key = InputHandler.get_key()

        for opt_key, label, action in self.options:
            if key == opt_key.lower():
                if action == "exit":
                    self.manager.quit()
                    return None

                elif action == "back":
                    return "replace:server_select"

                elif action == "login":
                    return self._handle_login()

                elif action == "register":
                    return self._handle_register()

                elif action == "guest":
                    print("\nContinuing as guest...")
                    input("Press Enter to continue...")
                    return "replace:main_menu"

        return None

    def _handle_login(self) -> Optional[str]:
        """Handle login flow."""
        print("\n=== Login ===")
        username = InputHandler.get_text("Username: ")
        password = InputHandler.get_text("Password: ")

        try:
            from client_api_requests.save_service_adapter import get_adapter
            adapter = get_adapter()
            adapter.login(username, password)

            # Store user context
            self.user_context = {
                "username": username,
                "authenticated": True
            }

            print(f"\nLogged in as {username}")
            input("Press Enter to continue...")
            return "replace:main_menu"

        except Exception as e:
            print(f"\nLogin failed: {e}")
            input("Press Enter to continue...")
            return None

    def _handle_register(self) -> Optional[str]:
        """Handle registration flow."""
        print("\n=== Register ===")
        username = InputHandler.get_text("Choose a username: ")
        password = InputHandler.get_text("Choose a password: ")

        try:
            from client_api_requests.save_service_adapter import get_adapter
            adapter = get_adapter()
            adapter.register(username, password)

            # Auto-login after registration
            adapter.login(username, password)

            self.user_context = {
                "username": username,
                "authenticated": True
            }

            print(f"\nRegistered and logged in as {username}")
            input("Press Enter to continue...")
            return "replace:main_menu"

        except Exception as e:
            print(f"\nRegistration failed: {e}")
            input("Press Enter to continue...")
            return None