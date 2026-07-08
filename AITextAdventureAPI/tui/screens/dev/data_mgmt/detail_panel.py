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
from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Static

from tui.services.dev.dataservices import DevRecord, DialogueLine, NpcRecordNode, TimelineTaskNode

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen

_ASSETS_DIR  = Path(__file__).parent.parent.parent.parent / "assets"
_IMG_MAX_COLS = 38
_IMG_MAX_ROWS = 20


def _resolve_asset(filename: str) -> Path | None:
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

        # Resolve asset path (pure path logic — no I/O)
        self._resolved: Optional[Path] = (
            _resolve_asset(record.image) if record.image else None
        )
        self._cols: int = 0
        self._rows: int = 0

        # Read image dimensions only (PIL lazy header read, ~1ms, no pixel decode)
        if self._resolved is not None:
            try:
                from PIL import Image as PilImage  # noqa: PLC0415
                img_w, img_h = PilImage.open(self._resolved).size
                cols = _IMG_MAX_COLS
                rows = max(1, round(cols * img_h / (img_w * 2)))
                if rows > _IMG_MAX_ROWS:
                    rows = _IMG_MAX_ROWS
                    cols = max(1, round(rows * img_w * 2 / img_h))
                    cols = min(cols, _IMG_MAX_COLS)
                self._cols = cols
                self._rows = rows
            except Exception:
                self._resolved = None

    def compose(self) -> ComposeResult:
        r = self._record
        mbti_line, enneagram_line = _extract_quick_stats(r.detail)
        info_parts = [
            f"[bold]{rich_escape(r.name)}[/bold]",
            f"[dim]{rich_escape(r.id)}[/dim]",
        ]
        if r.subtitle:
            info_parts.append(f"[dim]{rich_escape(r.subtitle)}[/dim]")
        if mbti_line:
            info_parts.append("")
            info_parts.append(rich_escape(mbti_line))
        if enneagram_line:
            info_parts.append(rich_escape(enneagram_line))

        with Horizontal(id="npc-header-row"):
            with Vertical(id="npc-portrait-col"):
                if self._resolved is not None:
                    yield _ClickablePortrait(Text("[dim]  Loading…[/dim]"), self._resolved)
                else:
                    yield Static("[dim]  (no image)[/dim]", id="npc-portrait")
            with Vertical(id="npc-info-col"):
                yield Static("\n".join(info_parts), id="npc-name-bar")
        yield Static(rich_escape(r.detail), id="npc-detail-body")

    def on_mount(self) -> None:
        if self._resolved is not None and self._cols > 0:
            self._render_portrait()

    @work(thread=True, exclusive=True)
    def _render_portrait(self) -> None:
        from tui.services.dev.npc_image_cache import get_cached  # noqa: PLC0415
        from tui.services.dev.npc_image_renderer import chafa_available, get_portrait_ansi  # noqa: PLC0415

        # Check cache BEFORE rendering so we can show an accurate notification.
        renderer_key = "chafa" if chafa_available() else "braille"
        was_cached = get_cached(self._resolved, self._cols, self._rows, renderer_key) is not None

        ansi = get_portrait_ansi(self._resolved, self._cols, self._rows)
        if ansi is not None:
            if was_cached:
                self.app.call_from_thread(
                    self.app.notify, "⚡ Portrait loaded from cache", timeout=2.0
                )
            else:
                self.app.call_from_thread(
                    self.app.notify, "💾 Portrait rendered and saved to .ansi", timeout=3.0
                )
            self.app.call_from_thread(self._apply_portrait, ansi)

    def _apply_portrait(self, ansi: str) -> None:
        # Update the pre-mounted _ClickablePortrait in-place.
        # Static.update() is synchronous — safe to call via call_from_thread.
        try:
            portrait = self.query_one("#npc-portrait", _ClickablePortrait)
            portrait.update(Text.from_ansi(ansi))
        except Exception:
            pass


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


def _format_timeline_task_detail(task_node: TimelineTaskNode) -> str:
    """Format the raw task dict into a human-readable detail string."""
    task     = task_node.task
    ttype    = str(task.get("type", "?"))
    to_type  = task.get("to_type")
    to_id    = task.get("to_id")
    acquire  = task.get("task_acquire_events", []) or []
    complete = task.get("task_complete_events", []) or []

    lines = [
        f"Source: {task_node.source_path}",
        f"Type: {ttype}",
    ]
    if to_type or to_id:
        lines.append(f"Target: {to_type or '?'} → {to_id or '?'}")
    if task.get("item_id"):
        lines.append(f"Item: {task['item_id']}")
    if task.get("coordinates"):
        lines.append(f"Coordinates: {task['coordinates']}")

    lines.append("")
    lines.append(f"Acquire events ({len(acquire)}):")
    for ev in acquire:
        if isinstance(ev, dict):
            lines.append(f"  - {ev.get('event_type', '?')}  {ev.get('params', {})}")

    lines.append("")
    lines.append(f"Complete events ({len(complete)}):")
    for ev in complete:
        if isinstance(ev, dict):
            lines.append(f"  - {ev.get('event_type', '?')}  {ev.get('params', {})}")

    return "\n".join(lines)


def update_detail_for_timeline_task(screen: "DataMgmtScreen", task_node: TimelineTaskNode) -> None:
    """Update the detail panel with a single TimelineTaskNode."""
    detail_panel = screen.query_one("#dm-detail-panel")
    static = _ensure_static(detail_panel)
    header = (
        f"[bold]{rich_escape(task_node.label)}[/bold]"
        f"\n[dim]{rich_escape(task_node.task_id)}[/dim]"
    )
    detail = _format_timeline_task_detail(task_node)
    static.update(f"{header}\n\n{rich_escape(detail)}")


def update_detail_for_timeline_subtree(
    screen: "DataMgmtScreen",
    task_nodes: List[TimelineTaskNode],
) -> None:
    """Update the detail panel with an aggregate view of task nodes from a subtree."""
    detail_panel = screen.query_one("#dm-detail-panel")
    static = _ensure_static(detail_panel)
    if not task_nodes:
        static.update("[dim]← select a task from the tree[/dim]")
        return
    parts = [
        f"[bold]{rich_escape(t.label)}[/bold]  "
        f"[dim]{rich_escape(t.task_id)}[/dim]  "
        f"[dim]({rich_escape(t.source_path)})[/dim]"
        for t in task_nodes
    ]
    static.update("\n".join(parts))


def update_detail_for_npc_group(
    screen: "DataMgmtScreen",
    npc_nodes: List[NpcRecordNode],
) -> None:
    """Update the detail panel with an aggregate view of NPCs from a group selection."""
    detail_panel = screen.query_one("#dm-detail-panel")
    static = _ensure_static(detail_panel)
    if not npc_nodes:
        static.update("[dim]← select an NPC from the tree[/dim]")
        return
    parts = [
        f"[bold]{rich_escape(n.label)}[/bold]  "
        f"[dim]{rich_escape(n.npc_id)}[/dim]  "
        f"[dim]({rich_escape(n.source_group)})[/dim]"
        for n in npc_nodes
    ]
    static.update("\n".join(parts))


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