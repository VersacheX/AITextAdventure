"""
Detail panel rendering logic for displaying DevRecord and DialogueLine data.

NPC records with an ``image`` field get a composite layout:
  - Braille + truecolor portrait rendered via Rich's Text.from_ansi() so
    the ANSI colour sequences are interpreted correctly by Textual.
  - Name / id header below the portrait.
  - Full detail text (description, psychology, enneagram…) below that.
  - The outer ScrollableContainer #dm-detail-panel scrolls everything.

  ┌──────────────────────┬──────────────────────┐
  │  Portrait (50%)      │  Name / id           │
  │  2:1 aspect ratio    │  MBTI: …             │
  │  max 20 rows         │  Enneagram: …        │
  ├──────────────────────┴──────────────────────┤
  │  Full detail text (scrollable)              │
  └─────────────────────────────────────────────┘

Clicking the portrait opens PortraitFullscreen — a full-screen modal.
Image rendering requires Pillow only.  Falls back gracefully on any error.
"""
from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, List, Optional

from rich.markup import escape as rich_escape
from rich.text import Text
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Static

from tui.services.dev.dev_data_service import DevRecord, DialogueLine
from tui.services.dev.npc_image_renderer import image_to_braille_ansi

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen

# tui/assets/ resolved once relative to this file — correct from any cwd.
_ASSETS_DIR = Path(__file__).parent.parent.parent.parent / "assets"

# Portrait fits 50% of the 80-char detail panel, capped at 20 rows.
# Braille: 1 cell = 2px wide × 4px tall.
_IMG_MAX_COLS = 38
_IMG_MAX_ROWS = 20


def _resolve_asset(filename: str) -> Path | None:
    """Return the resolved Path for an asset filename, or None if not found.

    Supports colon-separated convention: ``folder:stem``
    e.g. ``voidwalkers:stigma1``  →  ``tui/assets/voidwalkers/stigma1.{ext}``

    A plain filename with no colon is resolved directly under _ASSETS_DIR.
    """
    if not filename:
        return None

    _EXTS = (".jpeg", ".jpg", ".png", ".gif")

    if ":" in filename:
        folder, stem = filename.split(":", 1)
        base = _ASSETS_DIR / folder.strip() / stem.strip()
    else:
        base = _ASSETS_DIR / filename

    if base.exists():
        return base
    for ext in _EXTS:
        alt = base.with_suffix(ext)
        if alt.exists():
            return alt

    return None


def _extract_quick_stats(detail: str) -> tuple[str, str]:
    """Parse the pre-formatted detail string and return (mbti_line, enneagram_line).

    Looks for the first lines starting with 'MBTI:' and 'Enneagram:'.
    Returns empty strings if not found.
    """
    mbti = ""
    enneagram = ""
    for line in detail.splitlines():
        stripped = line.strip()
        if not mbti and stripped.startswith("MBTI:"):
            mbti = stripped
        elif not enneagram and stripped.startswith("Enneagram:"):
            enneagram = stripped
        if mbti and enneagram:
            break
    return mbti, enneagram


class _ClickablePortrait(Static):
    """A braille portrait Static that opens PortraitFullscreen on click."""

    DEFAULT_CSS = """
    _ClickablePortrait {
        width: 100%;
        height: auto;
        padding: 0;
    }

    _ClickablePortrait:hover {
        opacity: 0.85;
    }
    """

    def __init__(self, ansi_text: Text, image_path: Path) -> None:
        super().__init__(ansi_text, id="npc-portrait")
        self._image_path = image_path

    def on_click(self) -> None:
        from tui.screens.dev.data_mgmt.portrait_fullscreen import PortraitFullscreen  # noqa: PLC0415
        self.app.push_screen(PortraitFullscreen(self._image_path))


class NpcDetailPanel(Widget):
    """Composite NPC detail widget.

    Top row: portrait (left 50%, max 20 rows) | name + quick stats (right 50%)
    Below:   full detail text (scrollable via outer ScrollableContainer)

    ``height: auto`` is required so the panel grows past the height of the
    outer ``ScrollableContainer``, giving it real overflow to scroll.
    """

    DEFAULT_CSS = """
    NpcDetailPanel {
        width: 100%;
        height: auto;
        layout: vertical;
    }

    #npc-header-row {
        width: 100%;
        height: auto;
        layout: horizontal;
        border-bottom: solid $accent 30%;
    }

    #npc-portrait-col {
        width: 1fr;
        height: auto;
    }

    #npc-info-col {
        width: 1fr;
        height: auto;
        padding: 1 2;
        border-left: solid $accent 20%;
    }

    #npc-detail-body {
        width: 100%;
        height: auto;
        padding: 1 2;
    }
    """

    def __init__(self, record: DevRecord) -> None:
        super().__init__()
        self._record = record

    def compose(self) -> ComposeResult:
        r = self._record

        # ── portrait: aspect-constrained, max 20 rows, 50% panel width ───
        resolved: Optional[Path] = _resolve_asset(r.image) if r.image else None
        portrait_ansi: Optional[str] = None

        if resolved is not None:
            try:
                from PIL import Image as PilImage  # noqa: PLC0415
                img = PilImage.open(resolved)
                img_w, img_h = img.size

                # Fit to max cols first, then cap rows
                cols = _IMG_MAX_COLS
                rows = max(1, round(cols * img_h / (img_w * 2)))
                if rows > _IMG_MAX_ROWS:
                    rows = _IMG_MAX_ROWS
                    cols = max(1, round(rows * img_w * 2 / img_h))
                    cols = min(cols, _IMG_MAX_COLS)

                portrait_ansi = image_to_braille_ansi(img, cols=cols, rows=rows)
            except Exception:
                portrait_ansi = None

        # ── quick stats from detail string ────────────────────────────────
        mbti_line, enneagram_line = _extract_quick_stats(r.detail)

        info_parts = [
            f"[bold]{rich_escape(r.name)}[/bold]",
            f"[dim]{rich_escape(r.id)}[/dim]",
        ]
        if mbti_line:
            info_parts.append("")
            info_parts.append(rich_escape(mbti_line))
        if enneagram_line:
            info_parts.append(rich_escape(enneagram_line))

        # ── header row: portrait | info ───────────────────────────────────
        with Horizontal(id="npc-header-row"):
            with Vertical(id="npc-portrait-col"):
                if portrait_ansi and resolved is not None:
                    yield _ClickablePortrait(Text.from_ansi(portrait_ansi), resolved)
                else:
                    yield Static("[dim]  (no image)[/dim]", id="npc-portrait")
            with Vertical(id="npc-info-col"):
                yield Static("\n".join(info_parts), id="npc-name-bar")

        # ── full detail below ─────────────────────────────────────────────
        yield Static(rich_escape(r.detail), id="npc-detail-body")


# ── public API ──────────────────────────────────────────────────────────────

def update_detail_for_record(screen: "DataMgmtScreen", record: DevRecord | None) -> None:
    """Update the detail panel for a DevRecord."""
    detail_panel = screen.query_one("#dm-detail-panel")

    if record is None:
        _reset_to_static(detail_panel, "[dim]No matching records.[/dim]")
        return

    if record.category == "npc":
        detail_panel.remove_children()
        detail_panel.mount(NpcDetailPanel(record))
        return

    static = _ensure_static(detail_panel)
    header = f"[bold]{rich_escape(record.name)}[/bold]"
    if record.subtitle:
        header += f"\n[dim]{rich_escape(record.subtitle)}[/dim]"
    static.update(f"{header}\n\n{rich_escape(record.detail)}")


def update_detail_for_single_dialogue(screen: "DataMgmtScreen", line: DialogueLine | None) -> None:
    """Update detail panel with a single DialogueLine."""
    detail_panel = screen.query_one("#dm-detail-panel")
    static = _ensure_static(detail_panel)
    if line is None:
        static.update("[dim]← select a dialogue line from the tree[/dim]")
        return
    static.update(f"[bold]{rich_escape(line.speaker)}[/bold]\n\n{rich_escape(line.text)}")


def update_detail_for_multiple_dialogue(screen: "DataMgmtScreen", lines: List[DialogueLine]) -> None:
    """Update detail panel with multiple DialogueLines (subtree selection)."""
    detail_panel = screen.query_one("#dm-detail-panel")
    static = _ensure_static(detail_panel)
    if not lines:
        static.update("[dim]No dialogue lines under this node.[/dim]")
        return
    parts: List[str] = []
    for ln in lines:
        parts.append(f"[bold]{rich_escape(ln.speaker)}[/bold]\n{rich_escape(ln.text)}")
    static.update("\n\n".join(parts))


# ── helpers ──────────────────────────────────────────────────────────────────

def _reset_to_static(detail_panel: Widget, text: str) -> None:
    _ensure_static(detail_panel).update(text)


def _ensure_static(detail_panel: Widget) -> Static:
    """Return ``#dm-detail-text``, rebuilding it if ``NpcDetailPanel`` is mounted."""
    try:
        return detail_panel.query_one("#dm-detail-text", Static)
    except Exception:
        detail_panel.remove_children()
        s = Static("", id="dm-detail-text")
        detail_panel.mount(s)
        return s