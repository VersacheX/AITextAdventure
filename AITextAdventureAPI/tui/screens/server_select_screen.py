"""
Server selection screen: choose between local and online modes.
"""
from typing import Optional, Dict, Any
from tui.core.screen_manager import Screen, ScreenType
from tui.core.renderer import clear_screen, make_box, center_box_in_terminal
from tui.core.input_handler import InputHandler


class ServerSelectScreen(Screen):
    """
    Initial screen for selecting play mode (local vs online).

    This screen configures the save adapter that will be used throughout
    the session.
    """

    def __init__(self, manager):
        super().__init__(manager)
        self.options = [
            ("1", "Play Local", "local"),
            ("2", "Play Online", "online"),
            ("Q", "Exit", "exit")
        ]

    def render(self) -> None:
        """Render the server selection screen."""
        clear_screen()

        # Title
        title = ["=== Fracture ===", "", "Select Play Mode:"]
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
        """Handle server selection input."""
        if key is None:
            key = InputHandler.get_key()

        # Find matching option
        for opt_key, label, mode in self.options:
            if key == opt_key.lower():
                if mode == "exit":
                    self.manager.quit()
                    return None

                # Configure adapter based on selection
                if mode == "local":
                    from client_api_requests.save_service_adapter import set_adapter
                    from client_api_requests.save_services.local_save_service import LocalSaveService
                    from client_api_requests.local_storage_service import LocalStorageAdapter

                    adapter = LocalStorageAdapter()
                    service = LocalSaveService(adapter)
                    set_adapter(service)
                    print(f"\n{label} mode configured.")

                elif mode == "online":
                    from client_api_requests.save_service_adapter import set_adapter
                    from client_api_requests.save_services.api_save_service import APISaveService
                    from client_api_requests.client_api_requests import ClientAPI

                    api = ClientAPI()
                    service = APISaveService(api)
                    set_adapter(service)
                    print(f"\n{label} mode configured.")

                input("Press Enter to continue...")
                return "replace:auth"

        # Invalid input - re-render
        return None