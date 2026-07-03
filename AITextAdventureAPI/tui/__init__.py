"""
TUI (Text User Interface) package for the Fracture game.

Built on Textual (https://textual.textualize.io), which renders through a
compositor that only repaints the terminal cells that actually changed
between frames. That is what eliminates flicker here — there is no manual
`os.system('cls')` / full-screen-clear-and-reprint loop anywhere in this
package, by design.

Entry point: `tui.app.run()` (see `run_tui.py` at the project root).
"""

__version__ = "0.2.0"