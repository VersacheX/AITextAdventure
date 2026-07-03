"""
Convenience runner for the Fracture TUI application.

Usage:
    python run_tui.py
"""
import sys
import os

_THIS_DIR = os.path.dirname(__file__)

# Add this directory so the `tui` package can be imported.
sys.path.insert(0, _THIS_DIR)

# Add `old/` so its bare-import modules (e.g. `client_api_requests.*`,
# `game.objects.*`) resolve. Everything under `old/` imports as if `old/`
# itself were a sys.path root (see e.g. `old/console_game.py`,
# `old/run_equipment_screen_test.py`), not as `old.client_api_requests...`.
sys.path.insert(0, os.path.join(_THIS_DIR, "old"))

from tui.app import run

if __name__ == "__main__":
    run()