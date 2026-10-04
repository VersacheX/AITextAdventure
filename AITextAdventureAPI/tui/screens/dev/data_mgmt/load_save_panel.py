"""
Load Save panel for the dev data-management screen.

Mirrors `SimulationPanel`: it is a full-replacement widget mounted into
`#dm-detail-panel` when the "Load Save" tab is active. It has two modes:

  * Browse: surfaces every saved game across all accounts (account-agnostic,
    no login required). Selecting one loads it into memory.
  * Inspect: once a save is loaded, browse the live game state (Tasks, Items,
    Characters, NPCs) and *attempt to complete tasks* by fulfilling their
    conditions (meet / defeat / fetch / goto), then run the game's own
    completion flow so real completion events fire. "Play" jumps to the
    overworld with the (possibly mutated) game active.

All save I/O runs on background workers via `tui.services.dev
.dev_save_browser`; game inspection/mutation is pure in-memory logic via
`tui.services.dev.dev_game_inspector`. Nothing here imports
`ClientAPI`/`requests` or blocks the UI.
"""
from __future__ import annotations

import queue
from typing import Any, Dict, List, Optional

from rich.markup import escape as rich_escape
from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label, ListItem, ListView, Static


def _format_save_row(save: Dict[str, Any]) -> str:
    name = save.get("name") or "Unnamed Save"
    character = save.get("main_character") or "Unknown"
    level = save.get("level")
    money = save.get("money")
    user_id = save.get("user_id")
    updated = save.get("updated_at") or "unknown"
    level_part = f"Level {level}" if level is not None else "Level ?"
    money_part = f"${money}" if money is not None else "$?"
    owner_part = f"user {user_id}" if user_id is not None else "user ?"
    return (
        f"{rich_escape(str(name))} \u2014 {rich_escape(str(character))}\n"
        f"{level_part}   {money_part}   {owner_part}   Updated {updated}"
    )


class SaveListItem(ListItem):
    """A single save entry carrying its save id."""

    def __init__(self, save: Dict[str, Any]) -> None:
        super().__init__(Label(_format_save_row(save)))
        self.save_id = save.get("id")
        self.save_name = str(save.get("name") or "Unnamed Save")


class EntityItem(ListItem):
    """An entry in the inspect list, carrying the live game object + index."""

    def __init__(self, label_text: str, obj: Any, index: int) -> None:
        super().__init__(Label(label_text))
        self.obj = obj
        self.index = index


_CATEGORIES = ("tasks", "items", "characters", "npcs")


class LoadSavePanel(Vertical):
    """Full-replacement widget for #dm-detail-panel when the Load Save tab is active."""

    DEFAULT_CSS = """
    LoadSavePanel {
        width: 100%;
        height: 100%;
        padding: 1 2;
        overflow-y: auto;
    }

    #ls-header {
        width: 100%;
        height: 1;
        text-style: bold;
        color: $accent;
        margin-bottom: 1;
    }

    #ls-status {
        height: auto;
        color: $text 60%;
        margin-bottom: 1;
    }

    #ls-browse-buttons, #ls-cat-row, #ls-world-row, #ls-action-row {
        height: auto;
        margin-bottom: 1;
    }

    #ls-browse-buttons Button,
    #ls-cat-row Button,
    #ls-world-row Button,
    #ls-action-row Button {
        margin-right: 1;
    }

    #ls-list {
        height: 1fr;
        min-height: 8;
        border: solid $accent 20%;
    }

    SaveListItem Label, EntityItem Label {
        padding: 0 1;
    }

    #ls-detail {
        height: auto;
        min-height: 6;
        border: solid $accent 20%;
        padding: 0 1;
        margin-top: 1;
    }

    #ls-report-header {
        height: 1;
        text-style: bold;
        color: $accent;
        margin-top: 1;
    }

    #ls-report {
        height: auto;
        min-height: 4;
        max-height: 14;
        border: solid $accent 20%;
        padding: 0 1;
        overflow-y: auto;
    }

    #ls-report-row {
        height: auto;
        margin-top: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("\u2500\u2500 Load Save \u2500\u2500", id="ls-header")
        yield Static("Loading saves...", id="ls-status")
        with Horizontal(id="ls-browse-buttons"):
            yield Button("Refresh", id="ls-refresh", variant="default")
        with Horizontal(id="ls-cat-row"):
            yield Button("Tasks", id="ls-cat-tasks", variant="primary")
            yield Button("Items", id="ls-cat-items", variant="default")
            yield Button("Characters", id="ls-cat-characters", variant="default")
            yield Button("NPCs", id="ls-cat-npcs", variant="default")
            yield Button("Back to Saves", id="ls-back", variant="default")
            yield Button("Play \u25b6", id="ls-play", variant="success")
        with Horizontal(id="ls-world-row"):
            yield Button("Collect All Treasure", id="ls-collect-treasure", variant="warning")
        with Horizontal(id="ls-action-row"):
            yield Button("Fulfill", id="ls-fulfill", variant="warning")
            yield Button("Attempt Complete", id="ls-attempt", variant="success")
            yield Button("Force Complete", id="ls-force", variant="error")
        yield ListView(id="ls-list")
        yield Static("", id="ls-detail")
        yield Static("\u2500\u2500 Report \u2500\u2500", id="ls-report-header")
        yield Static("", id="ls-report")
        with Horizontal(id="ls-report-row"):
            yield Button("Clear Report", id="ls-clear-report", variant="default")

    def on_mount(self) -> None:
        self._busy = False
        self._mode = "browse"            # "browse" | "inspect"
        self._category = "tasks"
        self._selected_obj: Any = None
        self._report_lines: List[str] = []
        # Live report streaming: the worker pushes lines into this queue without
        # blocking; a UI-thread interval timer drains + renders in batches so a
        # fast emitter (world generation prints thousands of lines) can't flood
        # call_from_thread and stall the compositor. The report then updates in
        # real time instead of only after the action finishes.
        self._report_queue: "queue.Queue[str]" = queue.Queue()
        self._drain_timer = self.set_interval(0.1, self._drain_report_queue, pause=True)
        self._apply_mode()
        self._refresh_saves()

    # ?? events ????????????????????????????????????????????????????????????

    def on_button_pressed(self, event: Button.Pressed) -> None:
        event.stop()
        bid = event.button.id
        if bid == "ls-refresh":
            self._refresh_saves()
        elif bid == "ls-back":
            self._mode = "browse"
            self._selected_obj = None
            self._apply_mode()
            self._refresh_saves()
        elif bid == "ls-play":
            self._play()
        elif bid == "ls-collect-treasure":
            self._do_collect_treasure()
        elif bid and bid.startswith("ls-cat-"):
            self._category = bid.removeprefix("ls-cat-")
            self._refresh_category_buttons()
            self._populate_inspect_list()
        elif bid == "ls-fulfill":
            self._do_fulfill()
        elif bid == "ls-attempt":
            self._do_attempt_complete()
        elif bid == "ls-force":
            self._do_force_complete()
        elif bid == "ls-clear-report":
            self._clear_report()

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        event.stop()
        item = event.item
        if isinstance(item, SaveListItem) and item.save_id is not None:
            self._load_save(item.save_id)
        elif isinstance(item, EntityItem):
            self._selected_obj = item.obj
            self._update_detail()

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        # Stop our list's highlight events from bubbling up to the parent
        # DataMgmtScreen, whose handler treats non-record rows as "no match"
        # and would reset (destroy) this panel in the detail area.
        event.stop()
        item = event.item
        if isinstance(item, EntityItem):
            self._selected_obj = item.obj
            self._update_detail()

    # ?? mode / visibility ?????????????????????????????????????????????????

    def _apply_mode(self) -> None:
        inspect = self._mode == "inspect"
        self.query_one("#ls-browse-buttons").display = not inspect
        self.query_one("#ls-cat-row").display = inspect
        self.query_one("#ls-world-row").display = inspect
        self.query_one("#ls-action-row").display = inspect and self._category == "tasks"
        self.query_one("#ls-detail", Static).display = inspect
        self.query_one("#ls-report-header", Static).display = inspect
        self.query_one("#ls-report", Static).display = inspect
        self.query_one("#ls-report-row").display = inspect

    def _refresh_category_buttons(self) -> None:
        for cat in _CATEGORIES:
            try:
                btn = self.query_one(f"#ls-cat-{cat}", Button)
                btn.variant = "primary" if cat == self._category else "default"
            except Exception:
                pass
        self.query_one("#ls-action-row").display = self._category == "tasks"

    # ?? browse: listing saves ?????????????????????????????????????????????

    def _refresh_saves(self) -> None:
        if self._mode != "browse":
            return
        self._busy = True
        self._set_status("Loading saves...")
        list_view = self.query_one("#ls-list", ListView)
        list_view.clear()
        list_view.disabled = True
        self.query_one("#ls-refresh", Button).disabled = True
        self._fetch_saves()

    @work(thread=True, exclusive=True)
    def _fetch_saves(self) -> None:
        from tui.services.dev.dev_save_browser import list_all_saves  # noqa: PLC0415

        try:
            saves = list_all_saves()
        except Exception as exc:  # noqa: BLE001
            self.app.call_from_thread(self._on_fetch_error, str(exc))
            return
        self.app.call_from_thread(self._on_fetch_success, saves)

    def _on_fetch_success(self, saves: List[Dict[str, Any]]) -> None:
        self._busy = False
        list_view = self.query_one("#ls-list", ListView)
        list_view.clear()
        if not saves:
            self._set_status("No saved games found.")
        else:
            for save in saves:
                list_view.append(SaveListItem(save))
            self._set_status(f"{len(saves)} save(s). Enter to load into memory.")
            list_view.focus()
        list_view.disabled = False
        self.query_one("#ls-refresh", Button).disabled = False

    def _on_fetch_error(self, message: str) -> None:
        self._busy = False
        self._set_status(f"Failed to load saves: {rich_escape(message)}")
        self.query_one("#ls-list", ListView).disabled = False
        self.query_one("#ls-refresh", Button).disabled = False

    # ?? loading a save into memory ?????????????????????????????????????????

    def _load_save(self, save_id: Any) -> None:
        self._busy = True
        self._set_status("Loading save...")
        self.query_one("#ls-list", ListView).disabled = True
        self.query_one("#ls-refresh", Button).disabled = True
        self._fetch_and_apply_save(save_id)

    @work(thread=True, exclusive=True)
    def _fetch_and_apply_save(self, save_id: Any) -> None:
        from tui.services.dev.dev_save_browser import load_save_into_memory  # noqa: PLC0415

        try:
            player_game = load_save_into_memory(save_id)
        except Exception as exc:  # noqa: BLE001
            self.app.call_from_thread(self._on_load_error, str(exc))
            return
        if player_game is None:
            self.app.call_from_thread(self._on_load_error, "save data could not be read")
            return
        self.app.call_from_thread(self._on_load_success, player_game)

    def _on_load_success(self, player_game: Any) -> None:
        from tui.services.game_state import set_active_game  # noqa: PLC0415

        set_active_game(player_game)
        self._busy = False
        self._mode = "inspect"
        self._category = "tasks"
        self._selected_obj = None
        self.query_one("#ls-list", ListView).disabled = False
        self.query_one("#ls-refresh", Button).disabled = False
        self._apply_mode()
        self._refresh_category_buttons()
        self._populate_inspect_list()
        self.app.notify("Save loaded into memory.", title="Load Save")

    def _on_load_error(self, message: str) -> None:
        self._busy = False
        self.app.notify(
            f"Could not load save: {rich_escape(message)}",
            title="Load Save",
            severity="error",
        )
        self._set_status("Select a save to load.")
        self.query_one("#ls-list", ListView).disabled = False
        self.query_one("#ls-refresh", Button).disabled = False

    # ?? inspect: list game entities ????????????????????????????????????????

    def _active_pg(self) -> Optional[Any]:
        from tui.services.game_state import get_active_game  # noqa: PLC0415

        return get_active_game()

    def _populate_inspect_list(self) -> None:
        from tui.services.dev import dev_game_inspector as insp  # noqa: PLC0415

        pg = self._active_pg()
        list_view = self.query_one("#ls-list", ListView)
        list_view.clear()
        self._selected_obj = None
        self.query_one("#ls-detail", Static).update("")

        if pg is None:
            self._set_status("No game in memory.")
            return

        if self._category == "tasks":
            objs = insp.list_tasks(pg)
            labeler = insp.task_label
        elif self._category == "items":
            objs = insp.list_items(pg)
            labeler = insp.item_label
        elif self._category == "characters":
            objs = insp.list_characters(pg)
            labeler = insp.character_label
        else:
            objs = insp.list_npcs(pg)
            labeler = insp.npc_label

        for i, obj in enumerate(objs):
            try:
                text = rich_escape(labeler(obj))
            except Exception:
                text = f"<unlabelable #{i}>"
            list_view.append(EntityItem(text, obj, i))

        name = getattr(pg, "name", "loaded game")
        self._set_status(
            f"[b]{rich_escape(str(name))}[/b] - {len(objs)} {self._category}."
        )
        if objs:
            list_view.focus()

    def _update_detail(self) -> None:
        from tui.services.dev import dev_game_inspector as insp  # noqa: PLC0415

        detail = self.query_one("#ls-detail", Static)
        pg = self._active_pg()
        obj = self._selected_obj
        if pg is None or obj is None:
            detail.update("")
            return

        if self._category == "tasks":
            detail.update("\n".join(insp.describe_task(pg, obj)))
        elif self._category == "items":
            detail.update(self._describe_item(obj))
        elif self._category == "characters":
            detail.update(self._describe_character(obj))
        else:
            detail.update(self._describe_npc(obj))

    def _describe_item(self, item: Any) -> str:
        parts = [f"[bold]{rich_escape(str(getattr(item, 'name', '?')))}[/bold]"]
        for attr in ("id", "quantity", "value", "weight", "rarity", "description"):
            if hasattr(item, attr):
                parts.append(f"{attr}: {rich_escape(str(getattr(item, attr)))}")
        return "\n".join(parts)

    def _describe_character(self, char: Any) -> str:
        parts = [f"[bold]{rich_escape(str(getattr(char, 'name', '?')))}[/bold]"]
        for attr in ("level", "experience", "max_hp", "current_hp", "max_ap", "current_ap",
                     "strength", "dexterity", "constitution", "intelligence", "id"):
            if hasattr(char, attr):
                parts.append(f"{attr}: {rich_escape(str(getattr(char, attr)))}")
        return "\n".join(parts)

    def _describe_npc(self, npc: Any) -> str:
        parts = [f"[bold]{rich_escape(str(getattr(npc, 'name', '?')))}[/bold]"]
        for attr in ("id", "met", "description", "position", "location_reference_id"):
            if hasattr(npc, attr):
                parts.append(f"{attr}: {rich_escape(str(getattr(npc, attr)))}")
        return "\n".join(parts)

    # ?? inspect: task actions ??????????????????????????????????????????????

    def _require_task(self) -> Optional[Any]:
        if self._category != "tasks":
            self.app.notify("Select the Tasks category first.", title="Load Save")
            return None
        if self._selected_obj is None:
            self.app.notify("Select a task first.", title="Load Save")
            return None
        return self._selected_obj

    def _do_fulfill(self) -> None:
        from tui.services.dev import dev_game_inspector as insp  # noqa: PLC0415

        task = self._require_task()
        if task is None:
            return
        pg = self._active_pg()
        (changed, msg), report = insp.run_with_report(
            pg, lambda: insp.fulfill_conditions(pg, task)
        )
        self._log_action("Fulfill", msg, report)
        self.app.notify(rich_escape(msg), title="Fulfill",
                        severity="information" if changed else "warning")
        self._update_detail()

    def _do_attempt_complete(self) -> None:
        task = self._require_task()
        if task is None:
            return
        pg = self._active_pg()
        if pg is None:
            self.app.notify("No game loaded.", title="Attempt Complete", severity="warning")
            return
        # attempt_complete() runs the game's real completion flow, whose events
        # execute synchronously and may generate a world/dungeon. Route it
        # through the same guarded background worker as Force Complete so a long
        # chain can't freeze the UI and no second action can race it.
        self._begin_worker_action("Attempt Complete")
        self._run_task_worker(task, "Attempt Complete", force=False)

    def _do_force_complete(self) -> None:
        task = self._require_task()
        if task is None:
            return
        pg = self._active_pg()
        if pg is None:
            self.app.notify("No game loaded.", title="Force Complete", severity="warning")
            return
        # Force completion can trigger intro-story world generation, which is a
        # long-running loop. Run it on a background worker and stream its output
        # into the report panel so the UI stays responsive instead of freezing.
        self._begin_worker_action("Force Complete")
        self._run_task_worker(task, "Force Complete", force=True)

    # ?? guarded task worker ????????????????????????????????????????????????

    def _begin_worker_action(self, action: str) -> None:
        """Lock every panel control for a worker's lifetime and start streaming.

        Disabling only one button would leave Back, Play, Fulfill, the other
        complete actions and category controls live while the worker mutates the
        shared PlayerGame -- a user could enter the overworld or start another
        exclusive worker mid-generation. Lock them all; they are restored in the
        done callback (both success and failure).
        """
        self._set_actions_disabled(True)
        self._report_lines.append(f"[b]\u2023 {rich_escape(action)}[/b]: running...")
        self._render_report()
        self._drain_timer.resume()

    @work(thread=True, exclusive=True)
    def _run_task_worker(self, task: Any, action: str, force: bool) -> None:
        from tui.services.dev import dev_game_inspector as insp  # noqa: PLC0415

        pg = self._active_pg()

        def stream_line(line: str) -> None:
            # Non-blocking hand-off: never block the generation loop on the UI.
            self._report_queue.put(str(line))

        if force:
            op = lambda: insp.force_complete(pg, task)  # noqa: E731
        else:
            op = lambda: insp.attempt_complete(pg, task)  # noqa: E731

        (result, _report) = insp.run_with_report(pg, op, on_line=stream_line)
        done, msg = result
        self.app.call_from_thread(self._on_task_worker_done, action, done, msg)

    def _drain_report_queue(self) -> None:
        """Pull any queued streamed lines and render them in one batch."""
        drained: List[str] = []
        try:
            while True:
                drained.append(self._report_queue.get_nowait())
        except queue.Empty:
            pass
        if not drained:
            return
        for line in drained:
            self._report_lines.append(f"    {rich_escape(str(line))}")
        if len(self._report_lines) > 2000:
            self._report_lines = self._report_lines[-2000:]
        self._render_report()

    def _on_task_worker_done(self, action: str, done: bool, msg: str) -> None:
        # Flush any lines still queued, then stop the drain timer.
        self._drain_report_queue()
        try:
            self._drain_timer.pause()
        except Exception:
            pass
        self._report_lines.append(f"[b]\u2023 {rich_escape(action)} done[/b]: {rich_escape(msg)}")
        self._render_report()
        self._set_actions_disabled(False)
        self.app.notify(rich_escape(msg), title=action,
                        severity="information" if done else "warning")
        self._refresh_selected_task_row()

    def _set_actions_disabled(self, disabled: bool) -> None:
        """Enable/disable every interactive control in the inspect panel."""
        for bid in (
            "ls-refresh", "ls-back", "ls-play", "ls-collect-treasure",
            "ls-fulfill", "ls-attempt", "ls-force",
            "ls-cat-tasks", "ls-cat-items", "ls-cat-characters", "ls-cat-npcs",
        ):
            try:
                self.query_one(f"#{bid}", Button).disabled = disabled
            except Exception:
                pass
        try:
            self.query_one("#ls-list", ListView).disabled = disabled
        except Exception:
            pass

    def _refresh_selected_task_row(self) -> None:
        # Rebuild the list so completion state / new tasks are reflected, then
        # keep the detail panel in sync.
        self._populate_inspect_list()
        self._update_detail()

    # ?? play ???????????????????????????????????????????????????????????????

    def _play(self) -> None:
        pg = self._active_pg()
        if pg is None:
            self.app.notify("No game loaded.", title="Load Save", severity="warning")
            return
        self.app.goto_screen("overworld")

    # ?? world actions ??????????????????????????????????????????????????????

    def _do_collect_treasure(self) -> None:
        from tui.services.dev import dev_game_inspector as insp  # noqa: PLC0415

        pg = self._active_pg()
        if pg is None:
            self.app.notify("No game loaded.", title="Load Save", severity="warning")
            return
        (result, report) = insp.run_with_report(
            pg, lambda: insp.collect_all_dungeon_treasure(pg)
        )
        collected, _skipped, msg = result
        self._log_action("Collect Treasure", msg, report)
        self.app.notify(rich_escape(msg), title="Collect Treasure",
                        severity="information" if collected else "warning")
        # Items category may now show the new loot.
        if self._category == "items":
            self._populate_inspect_list()

    # ?? helpers ???????????????????????????????????????????????????????????

    def _set_status(self, text: str) -> None:
        try:
            self.query_one("#ls-status", Static).update(text)
        except Exception:
            pass

    def _log_action(self, action: str, summary: str, report: Any) -> None:
        """Append an action's result + captured output to the report log."""
        self._report_lines.append(f"[b]\u2023 {rich_escape(action)}[/b]: {rich_escape(summary)}")
        try:
            detail_lines = report.lines if report is not None else []
        except Exception:
            detail_lines = []
        for ln in detail_lines:
            self._report_lines.append(f"    {rich_escape(str(ln))}")
        # Keep the log bounded so it never grows without limit.
        if len(self._report_lines) > 500:
            self._report_lines = self._report_lines[-500:]
        self._render_report()

    def _clear_report(self) -> None:
        self._report_lines = []
        self._render_report()

    def _render_report(self) -> None:
        try:
            widget = self.query_one("#ls-report", Static)
        except Exception:
            return
        if not self._report_lines:
            widget.update("[dim]No actions yet.[/dim]")
        else:
            widget.update("\n".join(self._report_lines))
        # Keep the newest streamed lines in view as the log grows.
        try:
            widget.scroll_end(animate=False)
        except Exception:
            pass
