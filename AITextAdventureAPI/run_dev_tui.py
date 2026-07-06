"""
run_dev_tui.py — Development runner that boots directly into the data
management screen instead of the normal title → auth → main menu flow.

This launcher is used by developers to quickly access save-file browsing,
save inspection, deletion, and load-game testing without needing to log in
every time.

To use:
    python run_dev_tui.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# Locate the AITextAdventureAPI folder relative to this script, so imports
# like `tui.app`, `tui.screens`, `game.objects`, etc. can resolve.
api_root = Path(__file__).parent
old_root = api_root / "old"

# Both old/ and the repo root need to be on sys.path so bare imports like
# `game.objects.player` find the right modules.
if str(api_root) not in sys.path:
    sys.path.insert(0, str(api_root))
if str(old_root) not in sys.path:
    sys.path.insert(0, str(old_root))

from tui.app import FractureApp

if __name__ == "__main__":
    app = FractureApp()
    app.start_screen = "dev_data_mgmt"
    app.run()