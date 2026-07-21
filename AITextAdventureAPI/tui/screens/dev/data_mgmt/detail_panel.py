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
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple

from rich.markup import escape as rich_escape
from rich.text import Text
from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Static

from tui.services.dev.dataservices import (
    DevRecord,
    DialogueLine,
    NpcRecordNode,
    TimelineTaskNode,
    get_dialog_index,
    get_npc_names,
)

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen

_ASSETS_DIR   = Path(__file__).parent.parent.parent.parent / "assets"
_IMG_MAX_COLS = 38
_IMG_MAX_ROWS = 20

# The five player-character npc_ids that pending_character resolves to at runtime
_PENDING_CHARACTER_IDS: Tuple[str, ...] = (
    "technique", "magic", "tech", "skill", "faith",
)


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
    """Parse the pre-formatted detail string and return (mbti_line, enneagram_line)."""
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

        self._resolved: Optional[Path] = (
            _resolve_asset(record.image) if record.image else None
        )
        self._cols: int = 0
        self._rows: int = 0

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
        try:
            portrait = self.query_one("#npc-portrait", _ClickablePortrait)
            portrait.update(Text.from_ansi(ansi))
        except Exception:
            pass


# ── Timeline event formatting ─────────────────────────────────────────────

def _speaker_label(npc_id: Optional[str], name_map: Dict[str, str]) -> str:
    """Resolve an npc_id to a display name, handling special placeholders."""
    if not npc_id:
        return "Narrator"
    if npc_id in name_map:
        return name_map[npc_id]
    return npc_id.replace("_", " ").title()


def _format_dialog_event(
    ev: Dict[str, Any],
    is_character_dialog: bool,
    dialog_index: Dict[Tuple[Any, Any], List[str]],
    name_map: Dict[str, str],
) -> List[str]:
    """
    Format an initiate_dialog or initiate_character_dialog event into readable lines.

    Rules:
    - npc_id=None or missing → "Narrator"
    - npc_id="pending_character" (dialog only) → expand to all 5 player-character
      possibilities, each with their own lines if found in the index.
    - Otherwise look up (npc_id, dialog_id) in the dialog index and emit lines.
    - Returns a list of strings; each will become one Static row.
    """
    params    = ev.get("params") or {}
    npc_id    = params.get("npc_id") or None
    dialog_id = params.get("dialog_id") or ""
    prefix    = "Character Dialog" if is_character_dialog else "Dialog"

    # pending_character expands to all 5 player-character possibilities
    if npc_id == "pending_character":
        out: List[str] = []
        for cid in _PENDING_CHARACTER_IDS:
            lines = dialog_index.get((cid, dialog_id), [])
            cname = name_map.get(cid, cid.title())
            if lines:
                out.append(f"  {prefix}  {cname}  (pending)")
                for ln in lines:
                    out.append(f"    \"{rich_escape(str(ln))}\"")
            else:
                out.append(f"  {prefix}  {cname}  (pending)  [{rich_escape(dialog_id)}]")
        return out

    speaker  = _speaker_label(npc_id, name_map)
    dlg_lines = dialog_index.get((npc_id, dialog_id), [])

    if dlg_lines:
        out = [f"  {prefix}  {rich_escape(speaker)}"]
        for ln in dlg_lines:
            out.append(f"    \"{rich_escape(str(ln))}\"")
        return out

    # No lines found — show the reference so it's still informative
    return [f"  {prefix}  {rich_escape(speaker)}  [{rich_escape(dialog_id)}]"]


def _format_event_lines(
    ev: Dict[str, Any],
    dialog_index: Dict[Tuple[Any, Any], List[str]],
    name_map: Dict[str, str],
) -> List[str]:
    """
    Format a single task event dict into one or more readable display lines.

    Output format by event type:
    - initiate_dialog / initiate_character_dialog:
        Dialog  Speaker
          "line one"
          "line two"
    - set_npc_standing_text:
        NPC Standing Text  velka  "text"
    - award_task / remove_task / cancel_task:
        Award Task  task_id
    - award_item / remove_item:
        Award Item  item_id
    - award_money:
        Award Money  amount
    - Everything else:
        Event Label  key=value  key=value  ...
    """
    raw_type = str(ev.get("event_type", "?"))
    params   = ev.get("params") or {}

    if raw_type == "initiate_dialog":
        return _format_dialog_event(ev, False, dialog_index, name_map)

    if raw_type == "initiate_character_dialog":
        return _format_dialog_event(ev, True, dialog_index, name_map)

    if raw_type == "set_npc_standing_text":
        npc_id  = params.get("npc_id") or ""
        speaker = _speaker_label(npc_id, name_map) if npc_id else "?"
        texts   = params.get("standing_text") or []
        if isinstance(texts, list):
            joined = "  ".join(str(t) for t in texts)
        else:
            joined = str(texts)
        return [f"  NPC Standing Text  {rich_escape(speaker)}  \"{rich_escape(joined)}\""]

    if raw_type in ("award_task", "remove_task", "cancel_task"):
        label   = raw_type.replace("_", " ").title()
        task_id = str(params.get("task_id", "?"))
        return [f"  {label}  {rich_escape(task_id)}"]

    if raw_type in ("award_item", "remove_item"):
        label   = raw_type.replace("_", " ").title()
        item_id = str(params.get("item_id", "?"))
        return [f"  {label}  {rich_escape(item_id)}"]

    if raw_type == "award_money":
        return [f"  Award Money  {params.get('amount', '?')}"]

    # Generic fallback: Event Label  key=value  key=value
    label     = raw_type.replace("_", " ").title()
    param_str = "  ".join(
        f"{k}={rich_escape(str(v))}" for k, v in params.items()
    )
    return [f"  {label}" + (f"  {param_str}" if param_str else "")]


# ── Timeline detail widget ────────────────────────────────────────────────

class TimelineDetailPanel(Widget):
    """Sectioned detail panel for a single timeline task.

    Layout:
      ┌─ Task header (id, source, type, target) ─┐
      ├─ Acquired events ─────────────────────────┤
      └─ Completed events ────────────────────────┘

    ``height: auto`` lets content overflow the outer ScrollableContainer.
    """

    DEFAULT_CSS = """
    TimelineDetailPanel {
        width: 100%;
        height: auto;
        layout: vertical;
    }
    .tl-section {
        width: 100%;
        height: auto;
        padding: 0 2 1 2;
        border-bottom: solid $accent 20%;
    }
    .tl-section-header {
        width: 100%;
        height: auto;
        padding: 0 0 0 0;
        color: $accent;
        text-style: bold;
    }
    .tl-event-row {
        width: 100%;
        height: auto;
        color: $text 85%;
    }
    .tl-empty {
        width: 100%;
        height: auto;
        padding: 0 0 0 2;
        color: $text 40%;
    }
    """

    def __init__(self, task_node: TimelineTaskNode | None, summary_text: str = "") -> None:
        super().__init__()
        self._task_node    = task_node
        self._summary_text = summary_text

    def compose(self) -> ComposeResult:
        if self._task_node is None:
            yield Static(
                self._summary_text or "[dim]← select a task from the tree[/dim]",
                classes="tl-section",
            )
            return

        node     = self._task_node
        task     = node.task
        ttype    = str(task.get("type", "?"))
        to_type  = task.get("to_type")
        to_id    = task.get("to_id")
        acquire  = task.get("task_acquire_events") or []
        complete = task.get("task_complete_events") or []

        dialog_index = get_dialog_index()
        name_map     = get_npc_names()

        # ── Header section ────────────────────────────────────────────
        header_lines = [
            f"[bold]{rich_escape(node.label)}[/bold]",
            f"[dim]{rich_escape(node.task_id)}[/dim]",
            "",
            f"Source:  [dim]{rich_escape(node.source_path)}[/dim]",
            f"Type:    [dim]{rich_escape(ttype)}[/dim]",
        ]
        if to_type or to_id:
            header_lines.append(
                f"Target:  [dim]{rich_escape(str(to_type or '?'))} → "
                f"{rich_escape(str(to_id or '?'))}[/dim]"
            )
        if task.get("item_id"):
            header_lines.append(f"Item:    [dim]{rich_escape(str(task['item_id']))}[/dim]")
        if task.get("coordinates"):
            header_lines.append(f"Coords:  [dim]{rich_escape(str(task['coordinates']))}[/dim]")

        with Vertical(classes="tl-section"):
            yield Static("\n".join(header_lines))

        # ── Integrity section ─────────────────────────────────────────
        with Vertical(classes="tl-section"):
            if not node.errors:
                yield Static("Integrity: [green]OK[/green]", classes="tl-section-header")
            else:
                yield Static(
                    f"Integrity: [red]FAIL  ({len(node.errors)} error(s))[/red]",
                    classes="tl-section-header",
                )
                for err in node.errors:
                    code_str = rich_escape(err.code)
                    msg_str  = rich_escape(err.message)
                    extra    = ""
                    if err.event_type:
                        extra += f"  event={rich_escape(err.event_type)}"
                    if err.related_task_id:
                        extra += f"  task={rich_escape(err.related_task_id)}"
                    if err.related_entity_id:
                        extra += f"  entity={rich_escape(err.related_entity_id)}"
                    yield Static(
                        f"  [red]{code_str}[/red]  {msg_str}[dim]{extra}[/dim]",
                        classes="tl-event-row",
                    )

        # ── Acquired events ───────────────────────────────────────────
        with Vertical(classes="tl-section"):
            yield Static(f"Acquired  ({len(acquire)})", classes="tl-section-header")
            if acquire:
                for ev in acquire:
                    if isinstance(ev, dict):
                        for line in _format_event_lines(ev, dialog_index, name_map):
                            yield Static(line, classes="tl-event-row")
            else:
                yield Static("  (none)", classes="tl-empty")

        # ── Completed events ──────────────────────────────────────────
        with Vertical(classes="tl-section"):
            yield Static(f"Completed  ({len(complete)})", classes="tl-section-header")
            if complete:
                for ev in complete:
                    if isinstance(ev, dict):
                        for line in _format_event_lines(ev, dialog_index, name_map):
                            yield Static(line, classes="tl-event-row")
            else:
                yield Static("  (none)", classes="tl-empty")


# ── Dungeon detail widget ─────────────────────────────────────────────────

def _dungeon_tile_markup(ch: str, color: Optional[str]) -> str:
    """Return a single tile character wrapped in Rich color markup if a
    color is provided, escaped so square brackets in the glyph are safe."""
    if not ch:
        ch = "?"
    safe = ch.replace("[", "\\[")
    if color:
        return f"[{color}]{safe}[/]"
    return safe


class DungeonDetailPanel(Widget):
    """Detail panel for a dungeon DevRecord.

    Displays:
      • Name / id header
      • Tile legend: each of the three tile types shown in its assigned color
      • Layout stats (floors, rooms/floor, visible distance)
      • Hostile list, boss list, NPCs, items  (same content as the old plain-text detail)
    """

    DEFAULT_CSS = """
    DungeonDetailPanel {
        width: 100%;
        height: auto;
        layout: vertical;
    }
    .dg-section {
        width: 100%;
        height: auto;
        padding: 0 2 1 2;
        border-bottom: solid $accent 20%;
    }
    .dg-section-header {
        width: 100%;
        height: auto;
        color: $accent;
        text-style: bold;
    }
    .dg-row {
        width: 100%;
        height: auto;
        color: $text 85%;
    }
    """

    def __init__(self, record: "DevRecord") -> None:
        super().__init__()
        self._record = record

    def compose(self) -> ComposeResult:
        r  = self._record
        ex = r.extras or {}

        open_tile   = str(ex.get("open_area_tile",  ".") or ".")
        imp_tile    = str(ex.get("impassable_tile",  "#") or "#")
        border_tile = str(ex.get("border_tile",      "*") or "*")
        open_color  = ex.get("open_area_color")  or None
        imp_color   = ex.get("impassable_color") or None
        border_color= ex.get("border_color")     or None

        open_mu   = _dungeon_tile_markup(open_tile,   open_color)
        imp_mu    = _dungeon_tile_markup(imp_tile,    imp_color)
        border_mu = _dungeon_tile_markup(border_tile, border_color)

        # ── header ────────────────────────────────────────────────────
        with Vertical(classes="dg-section"):
            yield Static(
                f"[bold]{rich_escape(r.name)}[/bold]\n"
                f"[dim]{rich_escape(r.id)}[/dim]",
            )

        # ── tile legend ───────────────────────────────────────────────
        with Vertical(classes="dg-section"):
            yield Static("Tiles", classes="dg-section-header")
            yield Static(
                f" {open_mu}  Floor (open area)\n"
                f" {imp_mu}  Wall  (impassable)\n"
                f" {border_mu}  Perimeter (border)",
                classes="dg-row",
            )

        # ── layout stats ──────────────────────────────────────────────
        with Vertical(classes="dg-section"):
            yield Static("Layout", classes="dg-section-header")
            yield Static(
                f" Floors:            {ex.get('floors', '?')}\n"
                f" Rooms / floor:     {ex.get('rooms', '?')}\n"
                f" Visible distance:  {ex.get('visible_distance', '?')}",
                classes="dg-row",
            )

        # ── hostile / boss / npc / item lists ─────────────────────────
        with Vertical(classes="dg-section"):
            yield Static(rich_escape(r.detail), classes="dg-row")


# ── public API ──────────────────────────────────────────────────────────────

def _reset_to_static(container: Any, markup: str) -> None:
    """Replace all children of *container* with a single Static showing *markup*."""
    container.remove_children()
    container.mount(Static(markup))


def _ensure_static(container: Any) -> "Static":
    """Return the first Static child of *container*, creating one if needed."""
    from textual.widgets import Static as _Static  # noqa: PLC0415
    try:
        return container.query_one(_Static)
    except Exception:
        s = _Static("")
        container.mount(s)
        return s


def update_detail_for_record(screen: "DataMgmtScreen", record: "DevRecord | None") -> None:
    """Update the detail panel for a DevRecord."""
    detail_panel = screen.query_one("#dm-detail-panel")

    if record is None:
        _reset_to_static(detail_panel, "[dim]No matching records.[/dim]")
        return

    if record.category == "npc":
        detail_panel.remove_children()
        detail_panel.mount(NpcDetailPanel(record))
        return

    if record.category == "dungeon":
        detail_panel.remove_children()
        detail_panel.mount(DungeonDetailPanel(record))
        return

    static = _ensure_static(detail_panel)
    header = f"[bold]{rich_escape(record.name)}[/bold]"
    if record.subtitle:
        header += f"\n[dim]{rich_escape(record.subtitle)}[/dim]"
    static.update(f"{header}\n\n{rich_escape(record.detail)}")


def update_detail_for_single_dialogue(screen: "DataMgmtScreen", line: "DialogueLine | None") -> None:
    """Update detail panel with a single DialogueLine."""
    detail_panel = screen.query_one("#dm-detail-panel")
    static = _ensure_static(detail_panel)
    if line is None:
        static.update("[dim]← select a dialogue line from the tree[/dim]")
        return
    static.update(f"[bold]{rich_escape(line.speaker)}[/bold]\n\n{rich_escape(line.text)}")


def update_detail_for_multiple_dialogue(screen: "DataMgmtScreen", lines: "List[DialogueLine]") -> None:
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


def update_detail_for_timeline_task(screen: "DataMgmtScreen", task_node: "TimelineTaskNode") -> None:
    """Update the detail panel with a single TimelineTaskNode (sectioned)."""
    detail_panel = screen.query_one("#dm-detail-panel")
    detail_panel.remove_children()
    detail_panel.mount(TimelineDetailPanel(task_node))


def update_detail_for_timeline_subtree(
    screen: "DataMgmtScreen",
    task_nodes: "List[TimelineTaskNode]",
) -> None:
    """Update the detail panel with an aggregate summary of task nodes from a subtree."""
    detail_panel = screen.query_one("#dm-detail-panel")
    detail_panel.remove_children()
    if not task_nodes:
        detail_panel.mount(TimelineDetailPanel(None))
        return

    invalid      = sum(1 for t in task_nodes if t.errors)
    total_errors = sum(len(t.errors) for t in task_nodes)

    if invalid:
        integrity_line = (
            f"\n[red]Integrity: {invalid} invalid task(s), "
            f"{total_errors} error(s) in subtree[/red]"
        )
    else:
        any_validated = any(t.errors is not None for t in task_nodes)
        integrity_line = "\n[green]Integrity: OK[/green]" if any_validated else ""

    summary = "\n".join(
        f"[bold]{rich_escape(t.label)}[/bold]  "
        f"[dim]{rich_escape(t.task_id)}[/dim]  "
        f"[dim]({rich_escape(t.source_path)})[/dim]"
        + (f"  [red](errors: {len(t.errors)})[/red]" if t.errors else "")
        for t in task_nodes
    ) + integrity_line

    detail_panel.mount(TimelineDetailPanel(None, summary_text=summary))


def update_detail_for_npc_group(
    screen: "DataMgmtScreen",
    npc_nodes: "List[NpcRecordNode]",
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


def update_detail_for_ability(
    screen: "DataMgmtScreen",
    ability_node: "AbilityNode",
) -> None:
    """Update the detail panel for a single AbilityNode."""
    from tui.services.dev.dataservices.models import AbilityNode as _AbilityNode  # noqa: PLC0415

    detail_panel = screen.query_one("#dm-detail-panel")
    detail_panel.remove_children()

    record  = ability_node.record
    errors  = ability_node.errors
    lines: list[str] = []

    # Header
    lines.append(f"[bold]{rich_escape(record.name)}[/bold]")
    lines.append(f"[dim]{rich_escape(record.id)}[/dim]")
    lines.append("")

    # Validation block
    if errors:
        has_error = any(e.severity == "error"   for e in errors)
        colour    = "red" if has_error else "yellow"
        kind      = "FAIL" if has_error else "WARN"
        lines.append(f"[{colour}]Integrity: {kind}  ({len(errors)} issue(s))[/{colour}]")
        for e in errors:
            c = "red" if e.severity == "error" else "yellow"
            lines.append(f"  [{c}]{rich_escape(e.code)}[/{c}]  [dim]{rich_escape(e.message)}[/dim]")
    else:
        lines.append("[green]Integrity: OK[/green]")

    lines.append("")
    lines.append(rich_escape(record.detail))

    detail_panel.mount(Static("\n".join(lines)))


def update_detail_for_ability_group(
    screen: "DataMgmtScreen",
    ability_nodes: "List[AbilityNode]",
) -> None:
    """Update the detail panel with an aggregate view of a selected ability subtree."""
    detail_panel = screen.query_one("#dm-detail-panel")
    detail_panel.remove_children()

    if not ability_nodes:
        detail_panel.mount(Static("[dim]← select an ability from the tree[/dim]"))
        return

    invalid      = sum(1 for n in ability_nodes if n.errors)
    total_errors = sum(len(n.errors) for n in ability_nodes)

    if invalid:
        integrity_line = (
            f"\n[red]Integrity: {invalid} invalid, "
            f"{total_errors} issue(s) in subtree[/red]"
        )
    else:
        any_validated = any(n.errors is not None for n in ability_nodes)
        integrity_line = "\n[green]Integrity: OK[/green]" if any_validated else ""

    parts = [
        f"[bold]{rich_escape(n.label)}[/bold]  "
        f"[dim]{rich_escape(n.ability_id)}[/dim]"
        + (f"  [red](issues: {len(n.errors)})[/red]" if n.errors else "")
        for n in ability_nodes
    ]
    detail_panel.mount(Static("\n".join(parts) + integrity_line))


def update_detail_for_hostile(
    screen: "DataMgmtScreen",
    hostile_node: "HostileNode",
) -> None:
    """Update the detail panel for a single HostileNode."""
    detail_panel = screen.query_one("#dm-detail-panel")
    detail_panel.remove_children()

    record = hostile_node.record
    errors = hostile_node.errors
    lines: list[str] = []

    lines.append(f"[bold]{rich_escape(record.name)}[/bold]")
    lines.append(f"[dim]{rich_escape(record.id)}[/dim]")
    lines.append("")

    if errors:
        has_error = any(e.severity == "error" for e in errors)
        colour    = "red" if has_error else "yellow"
        kind      = "FAIL" if has_error else "WARN"
        lines.append(f"[{colour}]Integrity: {kind}  ({len(errors)} issue(s))[/{colour}]")
        for e in errors:
            c = "red" if e.severity == "error" else "yellow"
            lines.append(f"  [{c}]{rich_escape(e.code)}[/{c}]  [dim]{rich_escape(e.message)}[/dim]")
    else:
        lines.append("[green]Integrity: OK[/green]")

    lines.append("")
    lines.append(rich_escape(record.detail))

    detail_panel.mount(Static("\n".join(lines)))


def update_detail_for_hostile_group(
    screen: "DataMgmtScreen",
    hostile_nodes: "List[HostileNode]",
) -> None:
    """Update the detail panel with an aggregate view of a hostile subtree."""
    detail_panel = screen.query_one("#dm-detail-panel")
    detail_panel.remove_children()

    if not hostile_nodes:
        detail_panel.mount(Static("[dim]← select a hostile from the tree[/dim]"))
        return

    invalid      = sum(1 for n in hostile_nodes if n.errors)
    total_errors = sum(len(n.errors) for n in hostile_nodes)

    if invalid:
        integrity_line = (
            f"\n[red]Integrity: {invalid} invalid, "
            f"{total_errors} issue(s) in subtree[/red]"
        )
    else:
        any_validated = any(n.errors is not None for n in hostile_nodes)
        integrity_line = "\n[green]Integrity: OK[/green]" if any_validated else ""

    parts = [
        f"[bold]{rich_escape(n.label)}[/bold]  "
        f"[dim]{rich_escape(n.hostile_id)}[/dim]"
        + (f"  [red](issues: {len(n.errors)})[/red]" if n.errors else "")
        for n in hostile_nodes
    ]
    detail_panel.mount(Static("\n".join(parts) + integrity_line))