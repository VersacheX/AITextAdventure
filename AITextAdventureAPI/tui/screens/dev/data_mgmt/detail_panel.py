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

        # ── Integrity section ─────────────────────────────────────────
        errors = (r.extras or {}).get("_errors") if r.extras else None
        if errors is not None:
            hard_errors = [e for e in errors if e.severity == "error"]
            info_items  = [e for e in errors if e.severity == "info"]
            if not hard_errors and not info_items:
                yield Static("Integrity: [green]OK[/green]", classes="tl-section-header")
            else:
                if hard_errors:
                    parts = [f"[red]{len(hard_errors)} error(s)[/red]"]
                    if info_items:
                        parts.append(f"[cyan]{len(info_items)} info[/cyan]")
                    yield Static(
                        f"Integrity: [red]FAIL[/red]  ({', '.join(parts)})",
                        classes="tl-section-header",
                    )
                else:
                    yield Static(
                        f"Integrity: [cyan]INFO  ({len(info_items)} note(s))[/cyan]",
                        classes="tl-section-header",
                    )
                for err in errors:
                    colour = "cyan" if err.severity == "info" else "red"
                    yield Static(
                        f"  [{colour}]{rich_escape(err.code)}[/{colour}]"
                        f"  [dim]{rich_escape(err.message)}[/dim]",
                        classes="tl-section-header",
                    )

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
    info_item_ids: set | None = None,
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
        if item_id in info_item_ids:
            return [f"  [cyan]{label}  {rich_escape(item_id)}[/cyan]"]
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
        info_item_ids: set = set()

        with Vertical(classes="tl-section"):
            if not node.errors:
                yield Static("Integrity: [green]OK[/green]", classes="tl-section-header")
            else:
                has_error     = any(e.severity == "error"     for e in node.errors)
                has_warning   = any(e.severity == "warning"   for e in node.errors)
                has_info      = any(e.severity == "info"      for e in node.errors)
                has_notice    = any(e.severity == "notice"    for e in node.errors)
                has_duplicate = any(e.severity == "duplicate" for e in node.errors)

                error_count     = sum(1 for e in node.errors if e.severity == "error")
                warning_count   = sum(1 for e in node.errors if e.severity == "warning")
                info_count      = sum(1 for e in node.errors if e.severity == "info")
                notice_count    = sum(1 for e in node.errors if e.severity == "notice")
                duplicate_count = sum(1 for e in node.errors if e.severity == "duplicate")

                if has_error or has_warning:
                    parts = []
                    if error_count:
                        parts.append(f"[red]{error_count} error(s)[/red]")
                    if warning_count:
                        parts.append(f"[yellow]{warning_count} warning(s)[/yellow]")
                    if info_count:
                        parts.append(f"[cyan]{info_count} info[/cyan]")
                    if notice_count:
                        parts.append(f"[magenta]{notice_count} notice(s)[/magenta]")
                    if duplicate_count:
                        parts.append(f"[bright_magenta]{duplicate_count} duplicate(s)[/bright_magenta]")
                    yield Static(
                        f"Integrity: [red]FAIL[/red]  ({', '.join(parts)})",
                        classes="tl-section-header",
                    )
                elif has_notice or has_duplicate:
                    parts = []
                    if notice_count:
                        parts.append(f"[magenta]{notice_count} notice(s)[/magenta]")
                    if duplicate_count:
                        parts.append(f"[bright_magenta]{duplicate_count} duplicate(s)[/bright_magenta]")
                    if info_count:
                        parts.append(f"[cyan]{info_count} info[/cyan]")
                    yield Static(
                        f"Integrity: [#e040fb]NOTICE[/#e040fb]  ({', '.join(parts)})",
                        classes="tl-section-header",
                    )
                else:
                    yield Static(
                        f"Integrity: [cyan]INFO  ({info_count} note(s))[/cyan]",
                        classes="tl-section-header",
                    )

                # Collect item_ids flagged at info level for cyan event highlighting
                info_item_ids = {
                    e.related_entity_id
                    for e in node.errors
                    if e.severity == "info" and e.related_entity_id
                }

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
                    if err.severity == "info":
                        colour = "cyan"
                    elif err.severity == "warning":
                        colour = "yellow"
                    elif err.severity == "notice" and err.code in ("MEET_DELIVER_NO_CHARACTER_DIALOG", "HOSTILE_ABILITY_MISMATCH"):
                        colour = "blue"
                    elif err.severity == "notice":
                        colour = "#e040fb"
                    elif err.severity == "duplicate":
                        colour = "bright_magenta"
                    else:
                        colour = "red"
                    yield Static(
                        f"  [{colour}]{code_str}[/{colour}]  {msg_str}[dim]{extra}[/dim]",
                        classes="tl-event-row",
                    )

        # ── Acquired events ───────────────────────────────────────────
        with Vertical(classes="tl-section"):
            yield Static(f"Acquired  ({len(acquire)})", classes="tl-section-header")
            if acquire:
                for ev in acquire:
                    if isinstance(ev, dict):
                        for line in _format_event_lines(ev, dialog_index, name_map, info_item_ids):
                            yield Static(line, classes="tl-event-row")
            else:
                yield Static("  (none)", classes="tl-empty")

        # ── Completed events ──────────────────────────────────────────
        with Vertical(classes="tl-section"):
            yield Static(f"Completed  ({len(complete)})", classes="tl-section-header")
            if complete:
                for ev in complete:
                    if isinstance(ev, dict):
                        for line in _format_event_lines(ev, dialog_index, name_map, info_item_ids):
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
    """Return the first Static child of *container*, creating one if needed.

    If any composite children (NpcDetailPanel, DungeonDetailPanel, etc.) are
    still mounted from a previous selection, remove them first so they don't
    leak into non-NPC detail renders.
    """
    from textual.widgets import Static as _Static  # noqa: PLC0415

    # Remove any composite widget children — keep plain Statics intact so
    # _ensure_static can reuse them without a remove/remount race.
    for child in list(container.children):
        if not isinstance(child, _Static):
            child.remove()

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

    if record.category == "city":
        _render_city_detail(detail_panel, record)
        return

    if record.category == "character":
        _render_character_detail(detail_panel, record)
        return

    if record.category == "equipment":
        _render_equipment_detail(detail_panel, record)
        return

    static = _ensure_static(detail_panel)
    header = f"[bold]{rich_escape(record.name)}[/bold]"
    if record.subtitle:
        header += f"\n[dim]{rich_escape(record.subtitle)}[/dim]"
    static.update(f"{header}\n\n{rich_escape(record.detail)}")

def _render_character_detail(detail_panel: Any, record: "DevRecord") -> None:
    """Render a character DevRecord, highlighting any invalid equipment or
    ability ids inline in red within the detail text."""
    static = _ensure_static(detail_panel)

    invalid_equip    = (record.extras or {}).get("_invalid_equip")    or set()
    invalid_abilities = (record.extras or {}).get("_invalid_abilities") or set()
    errors            = (record.extras or {}).get("_errors")           or []
    validated         = (record.extras or {}).get("_validated", False)

    lines: list[str] = []

    # Header
    lines.append(f"[bold]{rich_escape(record.name)}[/bold]")
    if record.subtitle:
        lines.append(f"[dim]{rich_escape(record.subtitle)}[/dim]")
    lines.append("")

    # Integrity summary banner
    if validated and errors:
        lines.append(f"[red]Integrity: FAIL  ({len(errors)} issue(s))[/red]")
        for e in errors:
            lines.append(f"  [red]{rich_escape(e.code)}[/red]  [dim]{rich_escape(e.message)}[/dim]")
        lines.append("")
    elif validated:
        lines.append("[green]Integrity: OK[/green]")
        lines.append("")

    # Detail body — walk line-by-line, highlight invalid ids inline
    for raw_line in record.detail.splitlines():
        if not (invalid_equip or invalid_abilities):
            # Nothing to highlight — fast path
            lines.append(rich_escape(raw_line))
            continue

        # Equipment lines: "Weapon : some_id"  /  "Head   : some_id"  etc.
        # The id is the token after the last colon, stripped.
        stripped = raw_line.strip()
        if ":" in stripped and any(
            stripped.startswith(prefix)
            for prefix in ("Weapon", "Head", "Body", "Arms", "Legs", "Accessory")
        ):
            label, _, value = raw_line.partition(":")
            item_id = value.strip()
            if item_id in invalid_equip:
                lines.append(
                    f"{rich_escape(label)}: [red]{rich_escape(item_id)}[/red]"
                )
                continue

        # Ability lines: the line is indented and contains only the ability id
        if stripped and stripped in invalid_abilities:
            indent = raw_line[: len(raw_line) - len(raw_line.lstrip())]
            lines.append(f"{indent}[red]{rich_escape(stripped)}[/red]")
            continue

        lines.append(rich_escape(raw_line))

    static.update("\n".join(lines))


def _render_city_detail(detail_panel: Any, record: "DevRecord") -> None:
    """Render a city or region DevRecord, including validation errors if present."""
    #detail_panel.remove_children()
    static = _ensure_static(detail_panel)
    lines: list[str] = []
    lines.append(f"[bold]{rich_escape(record.name)}[/bold]")
    if record.subtitle:
        lines.append(f"[dim]{rich_escape(record.subtitle)}[/dim]")
    lines.append("")

    errors = (record.extras or {}).get("_errors") or []
    if errors:
        has_error   = any(getattr(e, "severity", "") == "error"   for e in errors)
        has_warning = any(getattr(e, "severity", "") == "warning" for e in errors)
        if has_error:
            hc, kind = "red",    "FAIL"
        elif has_warning:
            hc, kind = "yellow", "WARN"
        else:
            hc, kind = "cyan",   "INFO"
        lines.append(f"[{hc}]Integrity: {kind}  ({len(errors)} issue(s))[/{hc}]")
        for e in errors:
            sev = getattr(e, "severity", "error")
            c   = "red" if sev == "error" else "yellow" if sev == "warning" else "cyan"
            zone_tag = f" [{rich_escape(getattr(e, 'zone', ''))}]" if getattr(e, "zone", "") else ""
            lines.append(f"  [{c}]{rich_escape(e.code)}[/{c}]{zone_tag}  [dim]{rich_escape(e.message)}[/dim]")
    elif (record.extras or {}).get("_validated"):
        lines.append("[green]Integrity: OK — full Lv 1–100 coverage[/green]")

    lines.append("")
    if record.detail:
        lines.append(rich_escape(record.detail))

    static.update("\n".join(lines))


def _render_equipment_detail(detail_panel: Any, record: "DevRecord") -> None:
    """Render an equipment DevRecord, showing validation errors in the header
    when the equipment validator has run."""
    #detail_panel.remove_children()
    static = _ensure_static(detail_panel)
    lines: list[str] = []

    lines.append(f"[bold]{rich_escape(record.name)}[/bold]")
    if record.subtitle:
        lines.append(f"[dim]{rich_escape(record.subtitle)}[/dim]")
    lines.append("")

    errors    = (record.extras or {}).get("_errors")    or []
    validated = (record.extras or {}).get("_validated", False)

    if validated and errors:
        has_error   = any(getattr(e, "severity", "") == "error"   for e in errors)
        has_warning = any(getattr(e, "severity", "") == "warning" for e in errors)
        if has_error:
            hc, kind = "red",    "FAIL"
        elif has_warning:
            hc, kind = "yellow", "WARN"
        else:
            hc, kind = "cyan",   "INFO"
        lines.append(f"[{hc}]Integrity: {kind}  ({len(errors)} issue(s))[/{hc}]")
        for e in errors:
            sev = getattr(e, "severity", "error")
            c   = "red" if sev == "error" else "yellow" if sev == "warning" else "cyan"
            lines.append(f"  [{c}]{rich_escape(e.code)}[/{c}]  [dim]{rich_escape(e.message)}[/dim]")
        lines.append("")
    elif validated:
        lines.append("[green]Integrity: OK — item has a valid award source[/green]")
        lines.append("")

    if record.detail:
        lines.append(rich_escape(record.detail))

    static.update("\n".join(lines))

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


def _build_chapter_header(task_nodes: "List[TimelineTaskNode]") -> str:
    """Return a Rich-markup header block for a chapter-level subtree selection.

    Returns an empty string if the task_nodes are not all from the same
    ``main:chN`` source path (i.e. not a chapter-level selection).
    """
    import re

    if not task_nodes:
        return ""

    # All tasks must share the same "main:chN" source path
    paths = {t.source_path for t in task_nodes}
    if len(paths) != 1:
        return ""
    source_path = next(iter(paths))
    m = re.fullmatch(r"main:ch(\d+)", source_path)
    if not m:
        return ""
    chapter_num = int(m.group(1))

    # ── City / region / size lookup ───────────────────────────────────────
    city_key    = ""
    city_name   = ""
    region      = ""
    size_label  = ""
    try:
        from game.region_seeds.world_constants import CHAPTER_CITY_ORDER  # noqa: PLC0415
        if 1 <= chapter_num <= len(CHAPTER_CITY_ORDER):
            city_key = CHAPTER_CITY_ORDER[chapter_num - 1]   # e.g. "forest_mid_city"
            # city_key → region + size  ("forest_mid_city" → "forest", "mid city")
            _SIZE_LABELS = {
                "large_city": "Large City",
                "mid_city":   "Mid City",
                "small_city": "Small City",
            }
            for suffix, label in _SIZE_LABELS.items():
                if city_key.endswith("_" + suffix):
                    region     = city_key[: -(len(suffix) + 1)].replace("_", " ").title()
                    size_label = label
                    break
    except Exception:
        pass

    # Try to resolve the city display name from the constants module
    if city_key:
        try:
            import importlib  # noqa: PLC0415
            bucket = city_key[:-5] if city_key.endswith("_city") else city_key   # strip trailing "_city"
            mod_path = (
                f"game.region_seeds.regions.cities"
                f".{bucket.split('_')[0]}"
                f".constants_buildings_{bucket.split('_', 1)[1]}_city"
            )
            mod = importlib.import_module(mod_path)
            city_name = getattr(mod, "CITY_NAME", "")
        except Exception:
            pass

    # ── Scan events for created NPCs, dungeons, attainable characters ─────
    created_npcs:   list[str] = []
    joined_chars:   list[str] = []
    created_dung:   list[str] = []

    for task_node in task_nodes:
        task = task_node.task
        for bucket in ("task_acquire_events", "task_complete_events"):
            for evt in task.get(bucket) or []:
                etype  = evt.get("event_type", "")
                params = evt.get("params") or {}
                if etype == "create_npc":
                    npc_id = params.get("npc_id") or params.get("id") or ""
                    if npc_id and npc_id not in created_npcs:
                        created_npcs.append(npc_id)
                elif etype == "character_join":
                    char_id = params.get("character_id") or params.get("npc_id") or ""
                    if char_id and char_id not in joined_chars:
                        joined_chars.append(char_id)
                elif etype == "create_dungeon":
                    dung_id = params.get("dungeon_id") or params.get("id") or ""
                    if dung_id and dung_id not in created_dung:
                        created_dung.append(dung_id)

    # ── Assemble header markup ────────────────────────────────────────────
    lines: list[str] = []
    lines.append(f"[bold cyan]Chapter {chapter_num}[/bold cyan]")

    if city_name:
        city_display = f"[bold]{rich_escape(city_name)}[/bold]"
    elif city_key:
        city_display = f"[bold]{rich_escape(city_key)}[/bold]"
    else:
        city_display = "[dim]unknown[/dim]"

    region_part = (
        f"  [dim]{rich_escape(region)} · {rich_escape(size_label)}[/dim]"
        if region and size_label
        else ""
    )
    lines.append(f"City:      {city_display}{region_part}")

    def _fmt_list(items: list[str]) -> str:
        return "  " + ",  ".join(rich_escape(i) for i in items) if items else "  [dim]none[/dim]"

    lines.append(f"New NPCs:  {_fmt_list(created_npcs)}")
    lines.append(f"Dungeons:  {_fmt_list(created_dung)}")
    lines.append(f"Joins:     {_fmt_list(joined_chars)}")
    lines.append(f"[dim]{'─' * 48}[/dim]")   # horizontal rule before task breakdown

    return "\n".join(lines)


# ── Chapter subtree detail widget ─────────────────────────────────────────

def _parse_chapter_data(task_nodes: "List[TimelineTaskNode]") -> "dict | None":
    """Extract chapter metadata from a uniform ``main:chN`` task list.

    Returns a dict with keys:
        chapter_num, city_key, city_name, region, size_label,
        created_npcs, joined_chars, created_dung
    or ``None`` if *task_nodes* are not all from the same ``main:chN`` path.
    """
    import re  # noqa: PLC0415

    if not task_nodes:
        return None
    paths = {t.source_path for t in task_nodes}
    if len(paths) != 1:
        return None
    m = re.fullmatch(r"main:ch(\d+)", next(iter(paths)))
    if not m:
        return None
    chapter_num = int(m.group(1))

    city_key   = ""
    city_name  = ""
    region     = ""
    size_label = ""
    try:
        from game.region_seeds.world_constants import CHAPTER_CITY_ORDER  # noqa: PLC0415
        if 1 <= chapter_num <= len(CHAPTER_CITY_ORDER):
            city_key = CHAPTER_CITY_ORDER[chapter_num - 1]
            _SIZE_LABELS = {
                "large_city": "Large City",
                "mid_city":   "Mid City",
                "small_city": "Small City",
            }
            for suffix, lbl in _SIZE_LABELS.items():
                if city_key.endswith("_" + suffix):
                    region     = city_key[: -(len(suffix) + 1)].replace("_", " ").title()
                    size_label = lbl
                    break
    except Exception:
        pass

    if city_key:
        try:
            import importlib  # noqa: PLC0415
            bucket   = city_key[:-5] if city_key.endswith("_city") else city_key
            mod_path = (
                f"game.region_seeds.regions.cities"
                f".{bucket.split('_')[0]}"
                f".constants_buildings_{bucket.split('_', 1)[1]}_city"
            )
            city_name = getattr(importlib.import_module(mod_path), "CITY_NAME", "")
        except Exception:
            pass

    created_npcs: list[str] = []
    joined_chars: list[str] = []
    created_dung: list[str] = []

    for task_node in task_nodes:
        task = task_node.task
        for bucket in ("task_acquire_events", "task_complete_events"):
            for evt in task.get(bucket) or []:
                etype  = evt.get("event_type", "")
                params = evt.get("params") or {}
                if etype == "create_npc":
                    npc_id = params.get("npc_id") or params.get("id") or ""
                    if npc_id and npc_id not in created_npcs:
                        created_npcs.append(npc_id)
                elif etype == "character_join":
                    char_id = params.get("character_id") or params.get("npc_id") or ""
                    if char_id and char_id not in joined_chars:
                        joined_chars.append(char_id)
                elif etype == "create_dungeon":
                    dung_id = params.get("dungeon_id") or params.get("id") or ""
                    if dung_id and dung_id not in created_dung:
                        created_dung.append(dung_id)

    return dict(
        chapter_num  = chapter_num,
        city_key     = city_key,
        city_name    = city_name,
        region        = region,
        size_label   = size_label,
        created_npcs  = created_npcs,
        joined_chars  = joined_chars,
        created_dung  = created_dung,
    )


class ChapterDetailPanel(Widget):
    """Two-section detail panel for any single-bucket timeline selection.

    Covers main (chapter), extended (city story), and regional story buckets.

    Layout mirrors NpcDetailPanel:
      ┌─ Header (title, subtitle, region/size, counts) ───┐  border-bottom
      └─ Task breakdown (scrollable body)  ───────────────┘
    """

    DEFAULT_CSS = """
    ChapterDetailPanel {
        width: 100%;
        height: auto;
        layout: vertical;
    }
    #ch-header {
        width: 100%;
        height: auto;
        padding: 1 2;
        border-bottom: solid $accent 30%;
    }
    #ch-header-title {
        width: 100%;
        height: auto;
    }
    #ch-meta-col {
        width: 100%;
        height: auto;
        padding: 1 0 0 0;
    }
    #ch-body {
        width: 100%;
        height: auto;
        padding: 1 2;
    }
    .ch-meta-label {
        width: 100%;
        height: auto;
        color: $accent;
        text-style: bold;
    }
    .ch-meta-value {
        width: 100%;
        height: auto;
        padding: 0 0 0 2;
        color: $text 85%;
    }
    .ch-task-row {
        width: 100%;
        height: auto;
        color: $text 85%;
    }
    .ch-integrity {
        width: 100%;
        height: auto;
        padding: 1 0 0 0;
    }
    """

    def __init__(
        self,
        data: dict,
        task_nodes: "List[TimelineTaskNode]",
    ) -> None:
        super().__init__()
        self._data       = data
        self._task_nodes = task_nodes

    def compose(self) -> ComposeResult:
        d = self._data

        def _list_markup(items: list[str]) -> str:
            return "  ".join(rich_escape(i) for i in items) if items else "[dim]none[/dim]"

        # ── Header block ──────────────────────────────────────────────
        with Vertical(id="ch-header"):
            title_markup = f"[bold cyan]{rich_escape(d['title'])}[/bold cyan]"
            if d["subtitle"]:
                title_markup += f"\n[dim]{rich_escape(d['subtitle'])}[/dim]"
            yield Static(title_markup, id="ch-header-title")

            with Vertical(id="ch-meta-col"):
                if d["region"] and d["size_label"]:
                    yield Static("Region / Size", classes="ch-meta-label")
                    yield Static(
                        f"{rich_escape(d['region'])}  ·  {rich_escape(d['size_label'])}",
                        classes="ch-meta-value",
                    )
                elif d["region"]:
                    yield Static("Region", classes="ch-meta-label")
                    yield Static(rich_escape(d["region"]), classes="ch-meta-value")

                yield Static("New NPCs", classes="ch-meta-label")
                yield Static(_list_markup(d["created_npcs"]), classes="ch-meta-value")
                yield Static("Dungeons", classes="ch-meta-label")
                yield Static(_list_markup(d["created_dung"]), classes="ch-meta-value")
                yield Static("Character Joins", classes="ch-meta-label")
                yield Static(_list_markup(d["joined_chars"]), classes="ch-meta-value")

        # ── Task breakdown body ───────────────────────────────────────
        with Vertical(id="ch-body"):
            invalid       = sum(1 for t in self._task_nodes if t.errors)
            total_errors  = sum(len(t.errors) for t in self._task_nodes)
            any_validated = any(t.errors is not None for t in self._task_nodes)

            if invalid:
                yield Static(
                    f"[red]Integrity: {invalid} invalid task(s), "
                    f"{total_errors} error(s)[/red]",
                    classes="ch-integrity",
                )
            elif any_validated:
                yield Static("[green]Integrity: OK[/green]", classes="ch-integrity")

            for t in self._task_nodes:
                error_suffix = (
                    f"  [red](errors: {len(t.errors)})[/red]" if t.errors else ""
                )
                yield Static(
                    f"[bold]{rich_escape(t.label)}[/bold]  "
                    f"[dim]{rich_escape(t.task_id)}[/dim]"
                    + error_suffix,
                    classes="ch-task-row",
                )

# ── Subtree header data extraction ───────────────────────────────────────

def _parse_subtree_header_data(task_nodes: "List[TimelineTaskNode]") -> "dict | None":
    """Extract display metadata from a uniform single-bucket task list.

    Handles all three group types:
      • ``main:chN``           → chapter header
      • ``extended:<bucket>``  → city-story header
      • ``regional:<region>``  → regional-story header

    Returns a dict with keys:
        kind            "chapter" | "extended" | "regional"
        title           primary bold title string
        subtitle        secondary dim string (may be empty)
        region          humanized region name (may be empty)
        size_label      "Large City" / "Mid City" / "Small City" (may be empty)
        chapter_num     int or None
        continent_num   int or None
        created_npcs    list[str]
        joined_chars    list[str]
        created_dung    list[str]

    Returns ``None`` if tasks span multiple buckets/groups.
    """
    import re  # noqa: PLC0415

    if not task_nodes:
        return None
    paths = {t.source_path for t in task_nodes}
    if len(paths) != 1:
        return None
    source_path = next(iter(paths))
    if ":" not in source_path:
        return None

    group_key, bucket_key = source_path.split(":", 1)

    kind         = ""
    title        = ""
    subtitle     = ""
    region       = ""
    size_label   = ""
    chapter_num  = None
    continent_num = None

    if group_key == "main":
        m = re.fullmatch(r"ch(\d+)", bucket_key)
        if not m:
            return None
        kind        = "chapter"
        chapter_num = int(m.group(1))

        # city for this chapter
        city_key  = ""
        city_name = ""
        try:
            from game.region_seeds.world_constants import CHAPTER_CITY_ORDER  # noqa: PLC0415
            if 1 <= chapter_num <= len(CHAPTER_CITY_ORDER):
                city_key = CHAPTER_CITY_ORDER[chapter_num - 1]
        except Exception:
            pass

        if city_key:
            _SIZE_MAP = {
                "large_city": "Large City",
                "mid_city":   "Mid City",
                "small_city": "Small City",
            }
            for suffix, lbl in _SIZE_MAP.items():
                if city_key.endswith("_" + suffix):
                    region     = city_key[: -(len(suffix) + 1)].replace("_", " ").title()
                    size_label = lbl
                    break
            try:
                import importlib  # noqa: PLC0415
                bkt      = city_key[:-5] if city_key.endswith("_city") else city_key
                mod_path = (
                    f"game.region_seeds.regions.cities"
                    f".{bkt.split('_')[0]}"
                    f".constants_buildings_{bkt.split('_', 1)[1]}_city"
                )
                city_name = getattr(importlib.import_module(mod_path), "CITY_NAME", "")
            except Exception:
                pass

        from tui.services.dev.dataservices.timeline_service import _CHAPTER_TITLES  # noqa: PLC0415
        ch_title = _CHAPTER_TITLES.get(chapter_num, "")
        title    = f"Chapter {chapter_num}" + (f" — {ch_title}" if ch_title else "")
        subtitle = (city_name or city_key or "").strip()

    elif group_key == "extended":
        # bucket_key is e.g. "desert_large" (no trailing _city)
        kind = "extended"
        _SIZE_MAP = {
            "large": "Large City",
            "mid":   "Mid City",
            "small": "Small City",
        }
        parts = bucket_key.rsplit("_", 1)
        if len(parts) == 2 and parts[1] in _SIZE_MAP:
            region     = parts[0].replace("_", " ").title()
            size_label = _SIZE_MAP[parts[1]]
        else:
            region = bucket_key.replace("_", " ").title()

        # look up city name and chapter/continent from timeline service metadata
        city_name = ""
        try:
            import importlib  # noqa: PLC0415
            mod_path  = (
                f"game.region_seeds.regions.cities"
                f".{parts[0]}"
                f".constants_buildings_{bucket_key}_city"
            )
            city_name = getattr(importlib.import_module(mod_path), "CITY_NAME", "")
        except Exception:
            pass

        try:
            from tui.services.dev.dataservices.timeline_service import _CITY_METADATA  # noqa: PLC0415
            meta = _CITY_METADATA.get(bucket_key)
            if meta:
                chapter_num, continent_num = meta
        except Exception:
            pass

        title    = city_name or (region + (" " + size_label if size_label else ""))
        subtitle = (
            "  ·  ".join(
                s for s in [
                    f"Ch.{chapter_num}"   if chapter_num   else "",
                    f"Cont.{continent_num}" if continent_num else "",
                ]
                if s
            )
        )

    elif group_key == "regional":
        kind   = "regional"
        region = bucket_key.replace("_", " ").title()
        title  = f"{region} Region"
        subtitle = "Regional Story"

    else:
        return None

    # ── Scan events ───────────────────────────────────────────────────
    created_npcs: list[str] = []
    joined_chars: list[str] = []
    created_dung: list[str] = []

    for task_node in task_nodes:
        task = task_node.task
        for bucket in ("task_acquire_events", "task_complete_events"):
            for evt in task.get(bucket) or []:
                etype  = evt.get("event_type", "")
                params = evt.get("params") or {}
                if etype == "create_npc":
                    npc_id = params.get("npc_id") or params.get("id") or ""
                    if npc_id and npc_id not in created_npcs:
                        created_npcs.append(npc_id)
                elif etype == "character_join":
                    char_id = params.get("character_id") or params.get("npc_id") or ""
                    if char_id and char_id not in joined_chars:
                        joined_chars.append(char_id)
                elif etype == "create_dungeon":
                    dung_id = params.get("dungeon_id") or params.get("id") or ""
                    if dung_id and dung_id not in created_dung:
                        created_dung.append(dung_id)

    return dict(
        kind          = kind,
        title         = title,
        subtitle      = subtitle,
        region        = region,
        size_label    = size_label,
        chapter_num   = chapter_num,
        continent_num = continent_num,
        created_npcs  = created_npcs,
        joined_chars  = joined_chars,
        created_dung  = created_dung,
    )


class ChapterDetailPanel(Widget):
    """Two-section detail panel for any single-bucket timeline selection.

    Covers main (chapter), extended (city story), and regional story buckets.

    Layout mirrors NpcDetailPanel:
      ┌─ Header (title, subtitle, region/size, counts) ───┐  border-bottom
      └─ Task breakdown (scrollable body)  ───────────────┘
    """

    DEFAULT_CSS = """
    ChapterDetailPanel {
        width: 100%;
        height: auto;
        layout: vertical;
    }
    #ch-header {
        width: 100%;
        height: auto;
        padding: 1 2;
        border-bottom: solid $accent 30%;
    }
    #ch-header-title {
        width: 100%;
        height: auto;
    }
    #ch-meta-col {
        width: 100%;
        height: auto;
        padding: 1 0 0 0;
    }
    #ch-body {
        width: 100%;
        height: auto;
        padding: 1 2;
    }
    .ch-meta-label {
        width: 100%;
        height: auto;
        color: $accent;
        text-style: bold;
    }
    .ch-meta-value {
        width: 100%;
        height: auto;
        padding: 0 0 0 2;
        color: $text 85%;
    }
    .ch-task-row {
        width: 100%;
        height: auto;
        color: $text 85%;
    }
    .ch-integrity {
        width: 100%;
        height: auto;
        padding: 1 0 0 0;
    }
    """

    def __init__(
        self,
        data: dict,
        task_nodes: "List[TimelineTaskNode]",
    ) -> None:
        super().__init__()
        self._data       = data
        self._task_nodes = task_nodes

    def compose(self) -> ComposeResult:
        d = self._data

        def _list_markup(items: list[str]) -> str:
            return "  ".join(rich_escape(i) for i in items) if items else "[dim]none[/dim]"

        # ── Header block ──────────────────────────────────────────────
        with Vertical(id="ch-header"):
            title_markup = f"[bold cyan]{rich_escape(d['title'])}[/bold cyan]"
            if d["subtitle"]:
                title_markup += f"\n[dim]{rich_escape(d['subtitle'])}[/dim]"
            yield Static(title_markup, id="ch-header-title")

            with Vertical(id="ch-meta-col"):
                if d["region"] and d["size_label"]:
                    yield Static("Region / Size", classes="ch-meta-label")
                    yield Static(
                        f"{rich_escape(d['region'])}  ·  {rich_escape(d['size_label'])}",
                        classes="ch-meta-value",
                    )
                elif d["region"]:
                    yield Static("Region", classes="ch-meta-label")
                    yield Static(rich_escape(d["region"]), classes="ch-meta-value")

                yield Static("New NPCs", classes="ch-meta-label")
                yield Static(_list_markup(d["created_npcs"]), classes="ch-meta-value")
                yield Static("Dungeons", classes="ch-meta-label")
                yield Static(_list_markup(d["created_dung"]), classes="ch-meta-value")
                yield Static("Character Joins", classes="ch-meta-label")
                yield Static(_list_markup(d["joined_chars"]), classes="ch-meta-value")

        # ── Task breakdown body ───────────────────────────────────────
        with Vertical(id="ch-body"):
            invalid       = sum(1 for t in self._task_nodes if t.errors)
            total_errors  = sum(len(t.errors) for t in self._task_nodes)
            any_validated = any(t.errors is not None for t in self._task_nodes)

            if invalid:
                yield Static(
                    f"[red]Integrity: {invalid} invalid task(s), "
                    f"{total_errors} error(s)[/red]",
                    classes="ch-integrity",
                )
            elif any_validated:
                yield Static("[green]Integrity: OK[/green]", classes="ch-integrity")

            for t in self._task_nodes:
                error_suffix = (
                    f"  [red](errors: {len(t.errors)})[/red]" if t.errors else ""
                )
                yield Static(
                    f"[bold]{rich_escape(t.label)}[/bold]  "
                    f"[dim]{rich_escape(t.task_id)}[/dim]"
                    + error_suffix,
                    classes="ch-task-row",
                )

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

    header_data = _parse_subtree_header_data(task_nodes)
    if header_data is not None:
        detail_panel.mount(ChapterDetailPanel(header_data, task_nodes))
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
            c = "red" if e.severity == "error" else "yellow" if e.severity == "warning" else "cyan"
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
        has_error   = any(e.severity == "error"   for e in errors)
        has_warning = any(e.severity == "warning" for e in errors)
        colour = "red" if has_error else ("yellow" if has_warning else "cyan")
        kind   = "FAIL" if has_error else ("WARN" if has_warning else "INFO")
        lines.append(f"[{colour}]Integrity: {kind}  ({len(errors)} issue(s))[/{colour}]")
        for e in errors:
            c = "red" if e.severity == "error" else "yellow" if e.severity == "warning" else "cyan"
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


def update_detail_for_dungeon(
    screen: "DataMgmtScreen",
    dungeon_node: "DungeonNode",
) -> None:
    """Update the detail panel for a single DungeonNode."""
    detail_panel = screen.query_one("#dm-detail-panel")
    detail_panel.remove_children()

    record   = dungeon_node.record
    errors   = dungeon_node.errors
    settings = dungeon_node.settings
    lines: list[str] = []

    lines.append(f"[bold]{rich_escape(record.name)}[/bold]")
    lines.append(f"[dim]{rich_escape(dungeon_node.dungeon_id)}[/dim]")
    lines.append(f"[dim]Group: {rich_escape(dungeon_node.group_id)}[/dim]")
    lines.append("")

    if errors:
        has_error  = any(e.severity == "error"   for e in errors)
        has_warn   = any(e.severity == "warning" for e in errors)
        has_notice = any(e.severity == "notice"  for e in errors)
        if has_error:
            header_colour, kind = "red",    "FAIL"
        elif has_warn:
            header_colour, kind = "yellow", "WARN"
        elif has_notice:
            header_colour, kind = "cyan",   "INFO"
        else:
            header_colour, kind = "cyan",   "INFO"
        lines.append(f"[{header_colour}]Integrity: {kind}  ({len(errors)} issue(s))[/{header_colour}]")
        for e in errors:
            if e.severity == "error":
                c = "red"
            elif e.severity == "warning":
                c = "yellow"
            else:
                c = "cyan"
            lines.append(f"  [{c}]{rich_escape(e.code)}[/{c}]  [dim]{rich_escape(e.message)}[/dim]")
    else:
        lines.append("[green]Integrity: OK[/green]")

    lines.append("")

    if settings:
        for key, val in settings.items():
            lines.append(f"[dim]{rich_escape(str(key))}:[/dim] {rich_escape(str(val))}")
        lines.append("")

    if record.detail:
        lines.append(rich_escape(record.detail))

    detail_panel.mount(Static("\n".join(lines)))


def update_detail_for_dungeon_group(
    screen: "DataMgmtScreen",
    dungeon_nodes: "List[DungeonNode]",
) -> None:
    """Update the detail panel with an aggregate view of a dungeon subtree."""
    detail_panel = screen.query_one("#dm-detail-panel")
    detail_panel.remove_children()

    if not dungeon_nodes:
        detail_panel.mount(Static("[dim]← select a dungeon from the tree[/dim]"))
        return

    invalid      = sum(1 for n in dungeon_nodes if n.errors)
    total_errors = sum(len(n.errors) for n in dungeon_nodes)

    if invalid:
        integrity_line = (
            f"\n[red]Integrity: {invalid} invalid, "
            f"{total_errors} issue(s) in subtree[/red]"
        )
    else:
        any_validated = any(n.errors is not None for n in dungeon_nodes)
        integrity_line = "\n[green]Integrity: OK[/green]" if any_validated else ""

    parts = [
        f"[bold]{rich_escape(n.label)}[/bold]  "
        f"[dim]{rich_escape(n.dungeon_id)}[/dim]"
        + (f"  [red](issues: {len(n.errors)})[/red]" if n.errors else "")
        for n in dungeon_nodes
    ]
    detail_panel.mount(Static("\n".join(parts) + integrity_line))