"""
Convenience runner for the TUI application.

Usage:
    python run_tui.py
"""
import sys
import os

# Add parent directory to path so tui module can be imported
sys.path.insert(0, os.path.dirname(__file__))

from tui.main import main

if __name__ == "__main__":
    main()