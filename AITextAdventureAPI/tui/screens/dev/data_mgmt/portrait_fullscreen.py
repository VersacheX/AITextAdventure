"""portrait_fullscreen: full-screen braille portrait modal.

Opened when the user clicks the NPC portrait in the detail panel.
The image is re-rendered to fill as much of the terminal as possible
while preserving the source image's aspect ratio.  Click anywhere or
press Escape to close.

Performance notes
─────────────────
- Portrait rendering uses get_portrait_ansi(), which checks the two-level
  cache (memory + disk sidecar) before spawning any subprocess or pixel decode.
- The render runs inside a @work(thread=True, exclusive=True) worker
  so the compositor is never blocked.  exclusive=True means any in-progress
  render is cancelled before a new one starts (handles rapid resize events).
- The worker result is applied back on the main thread via call_from_thread.
"""
from __future__ import annotations

from pathlib import Path

from rich.text import Text
from textual import work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.screen import Screen
from textual.widgets import Static
from textual.worker import get_current_worker


class PortraitFullscreen(Screen):
    """Full-screen modal that renders a portrait at aspect-correct size.

    Does not inherit BaseScreen — no header/footer chrome so the image fills
    as much of the terminal as possible.  Escape or a mouse click anywhere
    dismisses it.
    """

    BINDINGS = [
        Binding("escape", "dismiss", "Close", show=True),
    ]

    DEFAULT_CSS = """
    PortraitFullscreen {
        align: center middle;
        background: $background;
    }

    #fs-portrait {
        width: 100%;
        height: 100%;
        content-align: center middle;
    }
    """

    def __init__(self, image_path: Path) -> None:
        super().__init__()
        self._image_path = image_path

    def compose(self) -> ComposeResult:
        yield Static("[dim]Loading…[/dim]", id="fs-portrait")

    def on_mount(self) -> None:
        self._render_worker()

    def on_resize(self) -> None:
        """Re-render on resize; exclusive=True cancels any in-progress job."""
        self._render_worker()

    @work(thread=True, exclusive=True)
    def _render_worker(self) -> None:
        """Background thread: compute portrait ANSI and push result to compositor."""
        worker = get_current_worker()

        t_cols = self.app.size.width
        t_rows = self.app.size.height

        # Read dimensions for aspect-ratio calculation (header-only, fast)
        try:
            from PIL import Image as PilImage  # noqa: PLC0415
            img_w, img_h = PilImage.open(self._image_path).size
        except Exception:
            if not worker.is_cancelled:
                self.app.call_from_thread(
                    self.query_one("#fs-portrait", Static).update,
                    "[dim](could not open image)[/dim]",
                )
            return

        if worker.is_cancelled:
            return

        # Aspect-ratio constrained sizing (same logic as before)
        cols = t_cols
        rows = max(1, round(cols * img_h / (img_w * 2)))
        if rows > t_rows:
            rows = t_rows
            cols = max(1, round(rows * img_w * 2 / img_h))
            cols = min(cols, t_cols)

        if worker.is_cancelled:
            return

        from tui.services.dev.npc_image_renderer import get_portrait_ansi  # noqa: PLC0415
        ansi = get_portrait_ansi(self._image_path, cols, rows)

        if ansi is None:
            if not worker.is_cancelled:
                self.app.call_from_thread(
                    self.query_one("#fs-portrait", Static).update,
                    "[dim](render failed)[/dim]",
                )
            return

        if worker.is_cancelled:
            return

        v_pad = max(0, (t_rows - rows) // 2)
        rich_text = Text.from_ansi("\n" * v_pad + ansi)

        self.app.call_from_thread(
            self.query_one("#fs-portrait", Static).update, rich_text
        )

    def on_click(self) -> None:
        """Click anywhere to dismiss."""
        self.dismiss()