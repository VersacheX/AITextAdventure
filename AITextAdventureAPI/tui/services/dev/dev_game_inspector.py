"""
dev_game_inspector: read/manipulate helpers for a loaded PlayerGame in the
dev TUI's "Load Save" inspector.

The Load Save tab loads a save into memory (see `dev_save_browser`) and then
lets a developer browse the live game state (tasks, items, characters, NPCs)
and *attempt to complete tasks* by fulfilling their conditions -- e.g. mark a
Meet target's NPC as met, register a Defeat target as slain, grant a Fetch
item, or teleport to a Goto coordinate -- then run the game's own
`check_completion_terms()` / `complete_task()` so the real task-completion
events fire exactly as they would in normal play.

Everything here is pure, synchronous logic operating on an in-memory
PlayerGame; there is no I/O, so it is safe to call directly from UI handlers.
"""
from __future__ import annotations

import contextlib
import io
from typing import Any, Dict, List, Optional, Tuple


# ?? Action report capture ??????????????????????????????????????????????????????

class ActionReport:
    """Collects human-readable output produced while a game action runs.

    Task/world mutations in this codebase surface progress two ways: plain
    ``print()`` calls and ``PlayerGame.add_info_dialog_line()`` entries. Both
    are invisible in the dev TUI unless captured. ``run_with_report`` wraps a
    callable so everything it prints *and* every info-dialog line it appends is
    gathered into one report the panel can render.
    """

    def __init__(self) -> None:
        self.lines: List[str] = []

    def add(self, line: str) -> None:
        if line is None:
            return
        for part in str(line).splitlines() or [""]:
            self.lines.append(part)

    def extend(self, lines: List[str]) -> None:
        for ln in lines:
            self.add(ln)

    def text(self) -> str:
        return "\n".join(self.lines)

    def is_empty(self) -> bool:
        return not self.lines


class _StreamingWriter(io.TextIOBase):
    """A stdout replacement that forwards each completed line to a callback.

    Long-running world generation ``print()``s progress line-by-line. Buffering
    everything until the action finishes (as ``io.StringIO`` does) makes the dev
    panel look frozen. This writer flushes on every newline so the UI can stream
    progress as it happens while still collecting the full text.
    """

    def __init__(self, on_line, sink: ActionReport) -> None:
        super().__init__()
        self._on_line = on_line
        self._sink = sink
        self._partial = ""

    def write(self, s: str) -> int:
        if not s:
            return 0
        self._partial += s
        while "\n" in self._partial:
            line, self._partial = self._partial.split("\n", 1)
            self._emit(line)
        return len(s)

    def flush(self) -> None:  # noqa: D401 - stdlib signature
        if self._partial:
            self._emit(self._partial)
            self._partial = ""

    def _emit(self, line: str) -> None:
        self._sink.add(line)
        if self._on_line is not None:
            try:
                self._on_line(line)
            except Exception:  # noqa: BLE001 - never let UI callback break capture
                pass


def run_with_report(pg: Any, fn, on_line=None) -> Tuple[Any, "ActionReport"]:
    """Run ``fn()`` capturing stdout and any new ``pg.info_dialogs`` lines.

    Returns ``(result, report)``. Newly appended info-dialog lines are drained
    from ``pg.info_dialogs`` so they don't re-show later in normal play.

    If ``on_line`` is provided it is invoked with each completed stdout line as
    it is produced, enabling live streaming of long-running actions (e.g. world
    generation) into the UI instead of only reporting once the action finishes.
    """
    report = ActionReport()

    info_dialogs = getattr(pg, "info_dialogs", None)
    start_len = len(info_dialogs) if isinstance(info_dialogs, list) else 0

    # NOTE: world generation routes progress through both stdout *and* the
    # world_gen_progress broadcaster. The stdout redirect below already captures
    # those lines, so we deliberately do NOT also subscribe to the broadcaster
    # here (that would double every line in the report).
    writer = _StreamingWriter(on_line, report)
    result = None
    try:
        with contextlib.redirect_stdout(writer):
            result = fn()
    finally:
        writer.flush()

        # Drain and record any info-dialog lines the action produced.
        if isinstance(info_dialogs, list) and len(info_dialogs) > start_len:
            new_lines = info_dialogs[start_len:]
            for ln in new_lines:
                report.add(str(ln))
                if on_line is not None:
                    try:
                        on_line(str(ln))
                    except Exception:  # noqa: BLE001
                        pass
            del info_dialogs[start_len:]

    return result, report


# ?? Listing ????????????????????????????????????????????????????????????????????

def list_tasks(pg: Any) -> List[Any]:
    return list(getattr(pg, "tasks", []) or [])


def list_items(pg: Any) -> List[Any]:
    return list(getattr(pg, "inventory", []) or [])


def list_characters(pg: Any) -> List[Any]:
    return list(getattr(pg, "characters", []) or [])


def list_npcs(pg: Any) -> List[Any]:
    return list(getattr(pg, "npcs", []) or [])


# ?? Formatting ?????????????????????????????????????????????????????????????????

def task_label(task: Any) -> str:
    tid = str(getattr(task, "task_id", "?"))
    ttype = str(getattr(task, "type", "?")).replace("TaskType.", "")
    done = getattr(task, "completed", False)
    mark = "[x]" if done else "[ ]"
    return f"{mark} {tid}  ({ttype})"


def item_label(item: Any) -> str:
    name = str(getattr(item, "name", getattr(item, "id", "?")))
    qty = getattr(item, "quantity", None)
    qty_part = f" x{qty}" if qty is not None else ""
    return f"{name}{qty_part}"


def character_label(char: Any) -> str:
    name = str(getattr(char, "name", "?"))
    lvl = getattr(char, "level", None)
    lvl_part = f"  Lv {lvl}" if lvl is not None else ""
    return f"{name}{lvl_part}"


def npc_label(npc: Any) -> str:
    name = str(getattr(npc, "name", getattr(npc, "id", "?")))
    met = getattr(npc, "met", False)
    met_part = "  (met)" if met else "  (unmet)"
    return f"{name}{met_part}"


def describe_task(pg: Any, task: Any) -> List[str]:
    """Return a list of detail lines describing a task and its completion state."""
    tid = str(getattr(task, "task_id", "?"))
    ttype = str(getattr(task, "type", "?")).replace("TaskType.", "")
    lines: List[str] = [f"[bold]{tid}[/bold]", "", f"Type: [cyan]{ttype}[/cyan]"]

    to_type = getattr(task, "to_type", None)
    if to_type is not None:
        tt = str(to_type).replace("SpecialTaskToType.", "")
        to_id = getattr(task, "to_id", "?")
        lines.append(f"Target: {tt} ({to_id})")
    if hasattr(task, "item_id"):
        lines.append(f"Item: {getattr(task, 'item_id')}")
    if hasattr(task, "special_item_id"):
        lines.append(f"Special Item: {getattr(task, 'special_item_id')}")
    if hasattr(task, "coordinates"):
        lines.append(f"Coordinates: {tuple(getattr(task, 'coordinates'))}")

    completed = getattr(task, "completed", False)
    status = "[green]completed[/green]" if completed else "[yellow]active[/yellow]"
    lines += ["", f"Status: {status}"]

    if not completed:
        ready = False
        if _type_value(task) == "deliver":
            item_id = getattr(task, "special_item_id", None)
            ready = any(
                getattr(i, "id", None) == item_id and getattr(i, "quantity", 0) > 0
                for i in getattr(pg, "inventory", [])
            )
        else:
            try:
                ready = bool(task.check_completion_terms(pg))
            except Exception as exc:  # noqa: BLE001
                lines.append(f"[red]check error: {exc}[/red]")
        lines.append(
            "[green]Conditions met - ready to complete.[/green]"
            if ready
            else "[dim]Conditions not yet met.[/dim]"
        )

    return lines


# ?? Condition fulfillment ??????????????????????????????????????????????????????

def can_fulfill(task: Any) -> bool:
    """True if this task has a dev-fulfillable target condition."""
    ttype = _type_value(task)
    return ttype in ("meet", "defeat", "fetch", "goto", "deliver")


def fulfill_conditions(pg: Any, task: Any) -> Tuple[bool, str]:
    """Best-effort: force the world state so the task's conditions are met.

    Returns (changed, message). Does NOT complete the task -- call
    `attempt_complete()` afterwards to run the real completion flow.
    """
    ttype = _type_value(task)

    if ttype == "meet":
        return _fulfill_meet(pg, task)
    if ttype == "defeat":
        return _fulfill_defeat(pg, task)
    if ttype == "fetch":
        return _fulfill_fetch(pg, task)
    if ttype == "goto":
        return _fulfill_goto(pg, task)
    if ttype == "deliver":
        return _fulfill_deliver(pg, task)

    return False, f"No automatic fulfillment for task type '{ttype}'."


def _fulfill_meet(pg: Any, task: Any) -> Tuple[bool, str]:
    to_id = getattr(task, "to_id", None)
    try:
        npc_id = pg.translate_npc_ref_to_id(to_id)
    except Exception:
        npc_id = to_id
    npc = next((n for n in getattr(pg, "npcs", []) if getattr(n, "id", None) == npc_id), None)
    if npc is None:
        return False, f"NPC '{npc_id}' not present in this game; cannot mark met."
    setattr(npc, "met", True)
    return True, f"Marked NPC '{npc_id}' as met."


def _fulfill_defeat(pg: Any, task: Any) -> Tuple[bool, str]:
    to_id = getattr(task, "to_id", None)
    if to_id is None:
        return False, "Task has no defeat target id."
    slain = getattr(pg, "enemies_slain", None)
    if slain is None:
        slain = {}
        pg.enemies_slain = slain
    slain[to_id] = slain.get(to_id, 0) + 1
    return True, f"Registered a slain '{to_id}'."


def _fulfill_fetch(pg: Any, task: Any) -> Tuple[bool, str]:
    item_id = getattr(task, "item_id", None)
    if item_id is None:
        return False, "Task has no fetch item_id."
    # Already have it?
    for item in getattr(pg, "inventory", []):
        if getattr(item, "id", None) == item_id and getattr(item, "quantity", 0) > 0:
            return False, f"Already hold item '{item_id}'."
    try:
        from game.objects.item import Item  # noqa: PLC0415

        granted = Item(id=item_id, name=item_id, quantity=1, stackable=False)
        pg.inventory.append(granted)
        return True, f"Granted item '{item_id}' to inventory."
    except Exception as exc:  # noqa: BLE001
        return False, f"Could not grant item '{item_id}': {exc}"


def _fulfill_goto(pg: Any, task: Any) -> Tuple[bool, str]:
    coords = getattr(task, "coordinates", None)
    if not coords:
        return False, "Task has no coordinates."
    try:
        pg.x, pg.y, pg.z = int(coords[0]), int(coords[1]), int(coords[2])
        return True, f"Teleported player to {tuple(coords)}."
    except Exception as exc:  # noqa: BLE001
        return False, f"Could not set coordinates: {exc}"


def _fulfill_deliver(pg: Any, task: Any) -> Tuple[bool, str]:
    """Grant the deliver task's required special item to inventory.

    Deliver completion (`_check_deliver`) is gated on the player actually
    carrying `special_item_id` (see PlayerGame._player_has_deliver_item), so
    fulfilling means granting that item. The delivery itself still completes
    through the real NPC-interaction / completion flow.
    """
    item_id = getattr(task, "special_item_id", None)
    if item_id is None:
        return False, "Task has no deliver special_item_id."
    for item in getattr(pg, "inventory", []):
        if getattr(item, "id", None) == item_id and getattr(item, "quantity", 0) > 0:
            return False, f"Already hold deliver item '{item_id}'."
    try:
        from game.objects.special_item import SpecialItem  # noqa: PLC0415

        granted = SpecialItem(id=item_id, name=item_id, quantity=1)
        pg.inventory.append(granted)
        return True, f"Granted deliver item '{item_id}' to inventory."
    except Exception as exc:  # noqa: BLE001
        return False, f"Could not grant deliver item '{item_id}': {exc}"


# ?? Completion ?????????????????????????????????????????????????????????????????

def attempt_complete(pg: Any, task: Any) -> Tuple[bool, str]:
    """Run the game's real completion check; complete the task if met.

    Returns (completed, message).
    """
    if getattr(task, "completed", False):
        return False, "Task already completed."

    # Deliver tasks never satisfy check_completion_terms() (it returns False
    # by design because delivery is normally driven by NPC interaction). Mirror
    # that real gate here: complete only if the player carries the item.
    if _type_value(task) == "deliver":
        return _attempt_complete_deliver(pg, task)

    try:
        ready = bool(task.check_completion_terms(pg))
    except Exception as exc:  # noqa: BLE001
        return False, f"Completion check failed: {exc}"
    if not ready:
        return False, "Conditions not met - cannot complete yet."
    try:
        pg.complete_task(task)
    except Exception as exc:  # noqa: BLE001
        return False, f"complete_task raised: {exc}"
    return True, f"Completed task '{getattr(task, 'task_id', '?')}'."


def _attempt_complete_deliver(pg: Any, task: Any) -> Tuple[bool, str]:
    """Complete a deliver task if the player carries its special item.

    Matches the gate used by PlayerGame's NPC-interaction paths
    (`_player_has_deliver_item`): the delivery can only complete when the
    required item is in inventory.
    """
    item_id = getattr(task, "special_item_id", None)
    has_item = False
    try:
        checker = getattr(pg, "_player_has_deliver_item", None)
        if callable(checker):
            has_item = bool(checker(task))
        else:
            has_item = any(
                getattr(i, "id", None) == item_id and getattr(i, "quantity", 0) > 0
                for i in getattr(pg, "inventory", [])
            )
    except Exception as exc:  # noqa: BLE001
        return False, f"Deliver check failed: {exc}"

    if not has_item:
        return False, (
            f"Missing deliver item '{item_id}'. Use Fulfill to grant it first."
        )
    try:
        pg.complete_task(task)
    except Exception as exc:  # noqa: BLE001
        return False, f"complete_task raised: {exc}"
    return True, f"Delivered - completed task '{getattr(task, 'task_id', '?')}'."


def force_complete(pg: Any, task: Any) -> Tuple[bool, str]:
    """Complete the task's events regardless of conditions (dev override)."""
    if getattr(task, "completed", False):
        return False, "Task already completed."
    try:
        pg.complete_task(task)
    except Exception as exc:  # noqa: BLE001
        return False, f"complete_task raised: {exc}"
    return True, f"Force-completed task '{getattr(task, 'task_id', '?')}'."


# ?? Dungeon treasure ???????????????????????????????????????????????????????????

def collect_all_dungeon_treasure(pg: Any) -> Tuple[int, int, str]:
    """Pick up every item entity sitting in every dungeon in the game.

    Walks each dungeon's tiles, and for each item entity (anything that isn't
    an NPC marker dict) tries `pg.pick_up_item()`. Successfully collected items
    are removed from their tile. Returns (collected, skipped, message) where
    `skipped` counts items that couldn't be collected (e.g. inventory full).
    """
    from game.objects.player import ItemType  # noqa: PLC0415

    dungeons = getattr(pg, "dungeons", None) or []
    if not dungeons:
        return 0, 0, "No dungeons in this game."

    collected = 0
    skipped = 0
    for dungeon in dungeons:
        tiles = getattr(dungeon, "tiles", None) or {}
        for tile in tiles.values():
            entities = getattr(tile, "entities", None)
            if not entities:
                continue
            for ent in list(entities):
                # Skip NPC markers (stored as dicts); only collect item objects.
                if isinstance(ent, dict):
                    continue
                if not isinstance(ent, ItemType):
                    continue
                try:
                    picked = pg.pick_up_item(ent)
                except Exception:
                    picked = False
                if picked:
                    try:
                        entities.remove(ent)
                    except ValueError:
                        pass
                    collected += 1
                else:
                    skipped += 1

    if collected == 0 and skipped == 0:
        return 0, 0, "No treasure found in any dungeon."
    msg = f"Collected {collected} item(s) from {len(dungeons)} dungeon(s)."
    if skipped:
        msg += f" {skipped} could not be picked up (inventory full?)."
    return collected, skipped, msg


# ?? internals ??????????????????????????????????????????????????????????????????

def _type_value(task: Any) -> str:
    t = getattr(task, "type", None)
    val = getattr(t, "value", None)
    if isinstance(val, str):
        return val
    return str(t).replace("TaskType.", "").lower()
