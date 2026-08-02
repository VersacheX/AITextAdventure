"""
Event handlers for tab activation, input changes, tree/list highlighting, and buttons.
Each tree category has its own dedicated handler in treehandlers.
"""
from __future__ import annotations

from collections import defaultdict

from rich.style import Style
from rich.text import Text

from typing import TYPE_CHECKING

from textual.containers import Vertical
from textual.widgets import Button, DataTable, Input, ListView, RadioSet, Static, Tabs, Tree

from tui.screens.dev.data_mgmt.components import _RecordRow
from tui.screens.dev.data_mgmt.detail_panel import (
    update_detail_for_ability,
    update_detail_for_ability_group,
    update_detail_for_dungeon,
    update_detail_for_dungeon_group,
    update_detail_for_hostile,
    update_detail_for_hostile_group,
    update_detail_for_multiple_dialogue,
    update_detail_for_npc_group,
    update_detail_for_record,
    update_detail_for_single_dialogue,
    update_detail_for_timeline_subtree,
    update_detail_for_timeline_task,
)
from tui.screens.dev.data_mgmt.npc_music_player import NpcMusicPlayerWidget
from tui.screens.dev.data_mgmt.treehandlers.dialog_handler import (
    collect_dialogue_lines_from_node,
    rebuild_dialog_tree,
)
from tui.screens.dev.data_mgmt.treehandlers.npc_handler import (
    collect_npc_records_from_node,
    rebuild_npc_tree,
)
from tui.screens.dev.data_mgmt.treehandlers.timeline_handler import (
    collect_timeline_tasks_from_node,
    rebuild_timeline_tree,
)
from tui.screens.dev.data_mgmt.utils import (
    collapse_all_nodes,
    copy_to_clipboard,
    expand_all_nodes,
    get_node_children,
    serialize_dialog_tree_visible,
    serialize_filtered_tree,
    serialize_node_visible,
    serialize_timeline_tree,
    serialize_timeline_task_detail,
    serialize_npc_tree,
)
from tui.services.dev.dataservices import (
    CATEGORIES,
    AbilityNode,
    DialogueLine,
    DungeonNode,
    HostileNode,
    NpcRecordNode,
    TimelineTaskNode,
    filter_equipment_records,
    get_dialogue_tree,
    get_dungeon_tree,
    get_npc_tree,
    get_timeline_tree,
    search_records,
)
from tui.services.dev.dataservices.timeline_validator import validate_timeline_integrity

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen

_DIALOG_CATEGORY      = "character_dialog"
_EQUIPMENT_CATEGORY   = "equipment"
_TIMELINE_CATEGORY    = "timeline"
_NPC_CATEGORY         = "npc"
_ABILITY_CATEGORY     = "ability"
_HOSTILE_CATEGORY     = "hostile"
_DUNGEON_CATEGORY     = "dungeon"
_CITY_CATEGORY        = "city"
_SIMULATION_CATEGORY  = "simulation"


def _active_tree_id(screen: "DataMgmtScreen") -> str:
    if screen._category == _DIALOG_CATEGORY:
        return "#dm-dialog-tree"
    if screen._category == _TIMELINE_CATEGORY:
        return "#dm-timeline-tree"
    if screen._category == _NPC_CATEGORY:
        return "#dm-npc-tree"
    if screen._category == _ABILITY_CATEGORY:
        return "#dm-ability-tree"
    if screen._category == _HOSTILE_CATEGORY:
        return "#dm-hostile-tree"
    if screen._category == _DUNGEON_CATEGORY:
        return "#dm-dungeon-tree"
    return "#dm-dialog-tree"  # fallback


def set_filter_mode(screen: "DataMgmtScreen", category: str) -> None:
    from tui.screens.dev.data_mgmt.simulation_panel import SimulationPanel  # noqa: PLC0415

    is_dialog     = category == _DIALOG_CATEGORY
    is_equipment  = category == _EQUIPMENT_CATEGORY
    is_timeline   = category == _TIMELINE_CATEGORY
    is_npc        = category == _NPC_CATEGORY
    is_ability    = category == _ABILITY_CATEGORY
    is_hostile    = category == _HOSTILE_CATEGORY
    is_dungeon    = category == _DUNGEON_CATEGORY
    is_city       = category == _CITY_CATEGORY
    is_simulation = category == _SIMULATION_CATEGORY
    is_tree       = is_dialog or is_timeline or is_npc or is_dungeon

    screen.query_one("#dm-filter", Input).display                  = not (is_dialog or is_equipment or is_ability or is_hostile or is_simulation)
    screen.query_one("#dm-dialog-filter-row").display              = is_dialog
    screen.query_one("#dm-equipment-filter-row", Vertical).display = is_equipment
    screen.query_one("#dm-hostile-filter-row",   Vertical).display = is_hostile
    screen.query_one("#dm-ability-filter-row",   Vertical).display = is_ability
    screen.query_one("#dm-list", ListView).display                 = not is_tree and not is_equipment and not is_hostile and not is_ability and not is_simulation
    screen.query_one("#dm-equipment-table", DataTable).display     = is_equipment
    screen.query_one("#dm-hostile-table",   DataTable).display     = is_hostile
    screen.query_one("#dm-ability-table",   DataTable).display     = is_ability
    screen.query_one("#dm-dialog-tree",  Tree).display             = is_dialog
    screen.query_one("#dm-timeline-tree", Tree).display            = is_timeline
    screen.query_one("#dm-npc-tree",     Tree).display             = is_npc
    screen.query_one("#dm-ability-tree", Tree).display             = False
    screen.query_one("#dm-hostile-tree", Tree).display             = False
    screen.query_one("#dm-dungeon-tree", Tree).display             = is_dungeon
    screen.query_one("#dm-expand",   Button).display               = is_tree
    screen.query_one("#dm-collapse", Button).display               = is_tree
    screen.query_one("#dm-copy",     Button).display               = is_tree or is_equipment or is_hostile or is_ability
    screen.query_one("#dm-validate-timeline",     Button).display = is_timeline
    screen.query_one("#dm-validate-abilities",    Button).display = is_ability
    screen.query_one("#dm-validate-hostiles",     Button).display = is_hostile
    screen.query_one("#dm-validate-dungeons",     Button).display = is_dungeon
    screen.query_one("#dm-validate-city-region",  Button).display = is_city
    screen.query_one("#dm-equip-sort-dir",    Button).display      = is_equipment
    screen.query_one("#dm-hostile-sort-dir",  Button).display      = is_hostile
    screen.query_one("#dm-ability-sort-dir",  Button).display      = is_ability
    screen.query_one(NpcMusicPlayerWidget).display                 = is_npc

    # Simulation panel: mount on demand, remove when leaving
    detail_panel = screen.query_one("#dm-detail-panel")
    existing_sim = list(detail_panel.query(SimulationPanel))
    if is_simulation:
        if not existing_sim:
            detail_panel.remove_children()
            detail_panel.mount(SimulationPanel())
    else:
        for w in existing_sim:
            w.remove()


def set_dialog_mode(screen: "DataMgmtScreen", is_dialog: bool) -> None:
    """Kept for call-site compatibility — delegates to set_filter_mode."""
    set_filter_mode(screen, _DIALOG_CATEGORY if is_dialog else screen._category)


def handle_tab_activated(screen: "DataMgmtScreen", event: Tabs.TabActivated) -> None:
    tab_id = event.tab.id or ""
    if tab_id.startswith("tab-"):
        category = tab_id.removeprefix("tab-")
        if category in CATEGORIES:
            screen._category = category
            set_filter_mode(screen, category)
            if category == _DIALOG_CATEGORY:
                rebuild_dialog_tree_for_screen(screen)
            elif category == _TIMELINE_CATEGORY:
                rebuild_timeline_tree_for_screen(screen)
            elif category == _NPC_CATEGORY:
                rebuild_npc_tree_for_screen(screen)
            elif category == _ABILITY_CATEGORY:
                rebuild_ability_tree_for_screen(screen)
            elif category == _HOSTILE_CATEGORY:
                rebuild_hostile_tree_for_screen(screen)
            elif category == _DUNGEON_CATEGORY:
                rebuild_dungeon_tree_for_screen(screen)
            elif category == _SIMULATION_CATEGORY:
                pass  # SimulationPanel is self-contained
            else:
                rebuild_list_for_screen(screen)


def handle_input_changed(screen: "DataMgmtScreen", event: Input.Changed) -> None:
    input_id = event.input.id
    if input_id == "dm-filter":
        if screen._category == _TIMELINE_CATEGORY:
            rebuild_timeline_tree_for_screen(screen)
        elif screen._category == _NPC_CATEGORY:
            rebuild_npc_tree_for_screen(screen)
        elif screen._category == _HOSTILE_CATEGORY:
            rebuild_hostile_tree_for_screen(screen)
        elif screen._category == _DUNGEON_CATEGORY:
            rebuild_dungeon_tree_for_screen(screen)
        else:
            rebuild_list_for_screen(screen)
    elif input_id == "dm-ability-filter":
        rebuild_ability_tree_for_screen(screen)
    elif input_id in ("dm-filter-act", "dm-filter-chapter", "dm-filter-task", "dm-filter-character"):
        rebuild_dialog_tree_for_screen(screen)


def handle_radio_set_changed(screen: "DataMgmtScreen", event: RadioSet.Changed) -> None:
    if event.radio_set.id in (
        "dm-equipment-type-radio",
        "dm-equipment-slot-radio",
        "dm-equipment-sort-radio",
    ):
        if event.radio_set.id == "dm-equipment-type-radio":
            type_filter = get_equipment_type_filter(screen)
            slot_radio  = screen.query_one("#dm-equipment-slot-radio", RadioSet)
            slot_radio.disabled = type_filter in ("weapon", "accessory")
        rebuild_list_for_screen(screen)

    elif event.radio_set.id == "dm-hostile-sort-radio":
        rebuild_hostile_tree_for_screen(screen)

    elif event.radio_set.id == "dm-ability-sort-radio":
        rebuild_ability_tree_for_screen(screen)


_SORT_COL_MAP: dict[str, str] = {
    "equip-sort-lv":     "level",
    "equip-sort-rarity": "rarity_rank",
    "equip-sort-dmg":    "damage",
    "equip-sort-def":    "defense",
    "equip-sort-crit":   "crit",
    "equip-sort-tsp":    "tsp",
    "equip-sort-tep":    "tep",
    "equip-sort-tap":    "tap",
    "equip-sort-tp":     "tp",
}


def get_equipment_sort_col(screen: "DataMgmtScreen") -> str:
    try:
        sort_radio = screen.query_one("#dm-equipment-sort-radio", RadioSet)
        pressed_id = sort_radio.pressed_button.id if sort_radio.pressed_button else "equip-sort-none"
        return _SORT_COL_MAP.get(pressed_id, "")
    except Exception:
        return ""


def get_equipment_type_filter(screen: "DataMgmtScreen") -> str:
    try:
        type_radio = screen.query_one("#dm-equipment-type-radio", RadioSet)
        pressed_id = type_radio.pressed_button.id if type_radio.pressed_button else "equip-type-all"
        if pressed_id == "equip-type-weapon":
            return "weapon"
        elif pressed_id == "equip-type-armor":
            return "armor"
        elif pressed_id == "equip-type-accessory":
            return "accessory"
        return ""
    except Exception:
        return ""


def get_equipment_slot_filter(screen: "DataMgmtScreen") -> str:
    try:
        slot_radio = screen.query_one("#dm-equipment-slot-radio", RadioSet)
        pressed_id = slot_radio.pressed_button.id if slot_radio.pressed_button else "equip-slot-all"
        if pressed_id == "equip-slot-head":
            return "head"
        elif pressed_id == "equip-slot-body":
            return "body"
        elif pressed_id == "equip-slot-arms":
            return "arms"
        elif pressed_id == "equip-slot-legs":
            return "legs"
        return ""
    except Exception:
        return ""


def handle_list_view_highlighted(screen: "DataMgmtScreen", event: ListView.Highlighted) -> None:
    record = event.item.record if isinstance(event.item, _RecordRow) else None
    update_detail_for_record(screen, record)


def handle_tree_node_highlighted(screen: "DataMgmtScreen", event: Tree.NodeHighlighted) -> None:
    from tui.screens.dev.data_mgmt.treehandlers.ability_handler import (  # noqa: PLC0415
        collect_ability_nodes_from_node,
    )
    from tui.screens.dev.data_mgmt.treehandlers.hostile_handler import (  # noqa: PLC0415
        collect_hostile_nodes_from_node,
    )
    from tui.screens.dev.data_mgmt.treehandlers.dungeon_handler import (  # noqa: PLC0415
        collect_dungeon_nodes_from_node,
    )

    category = screen._category
    node     = event.node
    data     = node.data

    if category == _DIALOG_CATEGORY:
        if isinstance(data, DialogueLine):
            update_detail_for_single_dialogue(screen, data)
        else:
            lines = collect_dialogue_lines_from_node(node)
            update_detail_for_multiple_dialogue(screen, lines)

    elif category == _TIMELINE_CATEGORY:
        if isinstance(data, TimelineTaskNode):
            screen._last_selected_timeline_node = data
            update_detail_for_timeline_task(screen, data)
        else:
            screen._last_selected_timeline_node = None
            tasks = collect_timeline_tasks_from_node(node)
            update_detail_for_timeline_subtree(screen, tasks)

    elif category == _NPC_CATEGORY:
        if isinstance(data, NpcRecordNode):
            screen.select_npc_record(data.record, start_music=True)
        else:
            npc_nodes = collect_npc_records_from_node(node)
            update_detail_for_npc_group(screen, npc_nodes)

    elif category == _ABILITY_CATEGORY:
        if isinstance(data, AbilityNode):
            update_detail_for_ability(screen, data)
        else:
            ability_nodes = collect_ability_nodes_from_node(node)
            update_detail_for_ability_group(screen, ability_nodes)

    elif category == _HOSTILE_CATEGORY:
        if isinstance(data, HostileNode):
            update_detail_for_hostile(screen, data)
        else:
            hostile_nodes = collect_hostile_nodes_from_node(node)
            update_detail_for_hostile_group(screen, hostile_nodes)

    elif category == _DUNGEON_CATEGORY:
        if isinstance(data, DungeonNode):
            update_detail_for_dungeon(screen, data)
        else:
            dungeon_nodes = collect_dungeon_nodes_from_node(node)
            update_detail_for_dungeon_group(screen, dungeon_nodes)


def handle_button_pressed(screen: "DataMgmtScreen", event: Button.Pressed) -> None:
    bid = event.button.id or ""
    if bid == "dm-expand":
        tree_id = _active_tree_id(screen)
        expand_all_nodes(screen.query_one(tree_id, Tree))
    elif bid == "dm-collapse":
        tree_id = _active_tree_id(screen)
        collapse_all_nodes(screen.query_one(tree_id, Tree))
    elif bid == "dm-copy":
        _handle_copy(screen)
    elif bid == "dm-validate-timeline":
        validate_timeline_for_screen(screen)
    elif bid == "dm-validate-abilities":
        validate_abilities_for_screen(screen)
    elif bid == "dm-validate-hostiles":
        validate_hostiles_for_screen(screen)
    elif bid == "dm-validate-dungeons":
        validate_dungeons_for_screen(screen)
    elif bid == "dm-validate-city-region":
        validate_city_region_for_screen(screen)
    elif bid == "dm-equip-sort-dir":
        screen._equipment_sort_asc = not screen._equipment_sort_asc
        event.button.label = "↑" if screen._equipment_sort_asc else "↓"
        rebuild_list_for_screen(screen)
    elif bid == "dm-hostile-sort-dir":
        screen._hostile_sort_asc = not screen._hostile_sort_asc
        event.button.label = "↑" if screen._hostile_sort_asc else "↓"
        rebuild_hostile_tree_for_screen(screen)
    elif bid == "dm-ability-sort-dir":
        screen._ability_sort_asc = not screen._ability_sort_asc
        event.button.label = "↑" if screen._ability_sort_asc else "↓"
        rebuild_ability_tree_for_screen(screen)


def _handle_copy(screen: "DataMgmtScreen") -> None:
    category = screen._category

    if category == _DIALOG_CATEGORY:
        from tui.screens.dev.data_mgmt.utils import serialize_dialog_tree_from_widget  # noqa: PLC0415
        tree_widget = screen.query_one("#dm-dialog-tree", Tree)
        text = serialize_dialog_tree_from_widget(tree_widget)

    elif category == _TIMELINE_CATEGORY:
        from tui.services.dev.dataservices import get_timeline_tree  # noqa: PLC0415
        from tui.screens.dev.data_mgmt.utils import serialize_timeline_tree_visible  # noqa: PLC0415
        tree_widget = screen.query_one("#dm-timeline-tree", Tree)
        text = serialize_timeline_tree_visible(tree_widget, get_timeline_tree(), screen)

    elif category == _NPC_CATEGORY:
        if screen._last_npc_filtered is not None:
            text = serialize_npc_tree(screen._last_npc_filtered)
        else:
            tree = screen.query_one("#dm-npc-tree", Tree)
            text = "\n".join(serialize_node_visible(tree.root, depth=0))

    elif category == _ABILITY_CATEGORY:
        nodes = getattr(screen, "_ability_flat_nodes", [])
        header = "\t".join(_ABILITY_COLUMNS + ["Messages"])
        rows = [header]
        for node in nodes:
            if not isinstance(node, AbilityNode):
                continue
            seed        = node.record.extras.get("_seed") or {}
            elements    = seed.get("elements") or []
            status_keys = seed.get("status_keys") or []
            effect      = str(seed.get("effect", "") or "")
            error_count = len(node.errors)
            has_error   = any(e.severity == "error"   for e in node.errors)
            has_warning = any(e.severity == "warning" for e in node.errors)
            if error_count == 0:
                err_cell = "✓"
            elif has_error:
                err_cell = f"✗ {error_count}"
            elif has_warning:
                err_cell = f"⚠ {error_count}"
            else:
                err_cell = f"• {error_count}"
            messages = " | ".join(
                f"[{e.severity.upper()}] {e.code}: {e.message}"
                for e in node.errors
            ) if node.errors else ""
            rows.append("\t".join([
                node.label,
                node.ability_id,
                str(node.level),
                node.ability_type,
                _fmt_elem_list(elements),
                effect,
                _fmt_status_list(status_keys),
                err_cell,
                messages,
            ]))
        text = "\n".join(rows)

    elif category == _HOSTILE_CATEGORY:
        nodes = getattr(screen, "_hostile_flat_nodes", [])
        header = "\t".join(_HOSTILE_COLUMNS + ["Messages"])
        rows = [header]
        for node in nodes:
            if not isinstance(node, HostileNode):
                continue
            rar_abbr    = _HOSTILE_RARITY_ABBR.get(node.rarity, node.rarity[:3].title())
            error_count = len(node.errors)
            has_error   = any(e.severity == "error"   for e in node.errors)
            has_warning = any(e.severity == "warning" for e in node.errors)
            if error_count == 0:
                err_cell = "✓"
            elif has_error:
                err_cell = f"✗ {error_count}"
            elif has_warning:
                err_cell = f"⚠ {error_count}"
            else:
                err_cell = f"• {error_count}"
            messages = " | ".join(
                f"[{e.severity.upper()}] {e.code}: {e.message}"
                for e in node.errors
            ) if node.errors else ""
            rows.append("\t".join([
                node.label,
                node.hostile_id,
                node.location_dungeon or "Overworld",
                node.location_region  or "—",
                str(node.level),
                rar_abbr,
                err_cell,
                messages,
            ]))
        text = "\n".join(rows)

    elif category == _EQUIPMENT_CATEGORY:
        records = screen._last_filtered or []
        text = "\n".join(f"{r.name}  {r.subtitle}" for r in records)

    else:
        if screen._last_filtered is not None:
            text = serialize_filtered_tree(screen._last_filtered)
        else:
            text = ""

    if text:
        copy_to_clipboard(text)
        screen.notify("Copied to clipboard", timeout=2.0)


def validate_timeline_for_screen(screen: "DataMgmtScreen") -> None:
    """Run the timeline integrity validator and repaint the tree.

    Errors are annotated in-place on each ``TimelineTaskNode.errors`` list.
    The tree is then rebuilt so labels for invalid tasks render in red/yellow/cyan.
    A status notification reports error, warning, and total affected task counts.
    Info-severity annotations are excluded from the toast counts.
    """
    import game.constants as const

    groups = get_timeline_tree()
    validate_timeline_integrity(groups, const)

    # Repaint — rebuild uses the now-annotated nodes from the same cache
    rebuild_timeline_tree_for_screen(screen)

    # Tally by severity across all annotated nodes — info excluded from counts
    error_tasks     = 0
    warning_tasks   = 0
    duplicate_tasks = 0
    notice_tasks    = 0
    for group in groups:
        for bucket in group.buckets:
            for tn in bucket.tasks:
                has_error     = any(e.severity == "error"     for e in tn.errors)
                has_warning   = any(e.severity == "warning"   for e in tn.errors)
                has_duplicate = any(e.severity == "duplicate" for e in tn.errors)
                has_notice    = any(e.severity == "notice"    for e in tn.errors)
                if has_error:
                    error_tasks += 1
                if has_warning:
                    warning_tasks += 1
                if has_duplicate:
                    duplicate_tasks += 1
                if has_notice:
                    notice_tasks += 1

    total_tasks = error_tasks + warning_tasks + duplicate_tasks + notice_tasks

    if total_tasks == 0:
        screen.notify("✓ Timeline integrity OK — no errors found.", timeout=3.0)
    else:
        parts = []
        if error_tasks:
            parts.append(f"{error_tasks} error task(s)")
        if warning_tasks:
            parts.append(f"{warning_tasks} warning task(s)")
        if duplicate_tasks:
            parts.append(f"{duplicate_tasks} duplicate task(s)")
        if notice_tasks:
            parts.append(f"{notice_tasks} notice task(s)")
        screen.notify(
            f"✗ {total_tasks} total affected task(s): {', '.join(parts)}.",
            severity="warning",
            timeout=5.0,
        )


def rebuild_dialog_tree_for_screen(screen: "DataMgmtScreen") -> None:
    if not screen._loaded:
        return
    tree = screen.query_one("#dm-dialog-tree", Tree)
    total_lines, filtered = rebuild_dialog_tree(
        tree,
        act_query=screen.query_one("#dm-filter-act", Input).value.strip(),
        chapter_query=screen.query_one("#dm-filter-chapter", Input).value.strip(),
        task_query=screen.query_one("#dm-filter-task", Input).value.strip(),
        character_query=screen.query_one("#dm-filter-character", Input).value.strip(),
        user_expanded=screen._user_expanded,
        user_collapsed=screen._user_collapsed,
    )
    screen._last_filtered = filtered
    screen.query_one("#dm-status", Static).update(f"{total_lines} line(s)")
    update_detail_for_single_dialogue(screen, None)


def rebuild_timeline_tree_for_screen(screen: "DataMgmtScreen") -> None:
    if not screen._loaded:
        return
    query = screen.query_one("#dm-filter", Input).value.strip()
    tree  = screen.query_one("#dm-timeline-tree", Tree)
    total_tasks, filtered = rebuild_timeline_tree(
        tree,
        query=query,
        user_expanded=screen._timeline_user_expanded,
        user_collapsed=screen._timeline_user_collapsed,
    )
    screen._last_timeline_filtered = filtered
    screen.query_one("#dm-status", Static).update(f"{total_tasks} task(s)")
    update_detail_for_timeline_subtree(screen, [])


def rebuild_npc_tree_for_screen(screen: "DataMgmtScreen") -> None:
    if not screen._loaded:
        return
    query = screen.query_one("#dm-filter", Input).value.strip()
    tree  = screen.query_one("#dm-npc-tree", Tree)
    total_npcs, filtered = rebuild_npc_tree(
        tree,
        query=query,
        user_expanded=screen._npc_user_expanded,
        user_collapsed=screen._npc_user_collapsed,
    )
    screen._last_npc_filtered = filtered
    screen.query_one("#dm-status", Static).update(f"{total_npcs} NPC(s)")
    screen.restore_npc_selection()


def rebuild_ability_tree_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.screens.dev.data_mgmt.treehandlers.ability_handler import rebuild_ability_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.ability_service import _flat_ability_nodes             # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_ability_tree                        # noqa: PLC0415

    if not screen._loaded:
        return
    query = ""
    try:
        query = screen.query_one("#dm-ability-filter", Input).value.strip()
    except Exception:
        pass

    # Keep hidden tree in sync (backing store for validator)
    tree = screen.query_one("#dm-ability-tree", Tree)
    total, filtered = rebuild_ability_tree(
        tree,
        query=query,
        user_expanded=screen._ability_user_expanded,
        user_collapsed=screen._ability_user_collapsed,
    )
    screen._last_ability_filtered = filtered

    # Repopulate the visible DataTable
    nodes = _flat_ability_nodes(filtered if filtered is not None else get_ability_tree())
    _populate_ability_table(screen, nodes)

    screen.query_one("#dm-status", Static).update(f"{total} ability(s)")
    update_detail_for_ability_group(screen, [])


def rebuild_hostile_tree_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.screens.dev.data_mgmt.treehandlers.hostile_handler import rebuild_hostile_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.hostile_service import flat_hostile_nodes             # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_hostile_tree                       # noqa: PLC0415

    if not screen._loaded:
        return
    query = ""
    try:
        query = screen.query_one("#dm-filter", Input).value.strip()
    except Exception:
        pass

    # Keep hidden tree in sync (used by validator to iterate HostileNode.errors)
    tree = screen.query_one("#dm-hostile-tree", Tree)
    total, filtered = rebuild_hostile_tree(
        tree,
        query=query,
        user_expanded=screen._hostile_user_expanded,
        user_collapsed=screen._hostile_user_collapsed,
    )
    screen._last_hostile_filtered = filtered

    # Repopulate the visible DataTable
    nodes = flat_hostile_nodes(filtered if filtered is not None else get_hostile_tree())
    _populate_hostile_table(screen, nodes)

    screen.query_one("#dm-status", Static).update(f"{total} hostile(s)")


def rebuild_dungeon_tree_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.screens.dev.data_mgmt.treehandlers.dungeon_handler import rebuild_dungeon_tree  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.detail_panel import update_detail_for_dungeon_group       # noqa: PLC0415

    if not screen._loaded:
        return
    query = ""
    try:
        query = screen.query_one("#dm-filter", Input).value.strip()
    except Exception:
        pass
    tree = screen.query_one("#dm-dungeon-tree", Tree)
    total, filtered = rebuild_dungeon_tree(
        tree,
        query=query,
        user_expanded=screen._dungeon_user_expanded,
        user_collapsed=screen._dungeon_user_collapsed,
    )
    screen._last_dungeon_filtered = filtered
    screen.query_one("#dm-status", Static).update(f"{total} dungeon(s)")
    update_detail_for_dungeon_group(screen, [])


def validate_timeline_for_screen(screen: "DataMgmtScreen") -> None:
    """Run the timeline integrity validator and repaint the tree."""
    import game.constants as const

    groups = get_timeline_tree()
    validate_timeline_integrity(groups, const)

    rebuild_timeline_tree_for_screen(screen)

    error_tasks = warning_tasks = duplicate_tasks = notice_tasks = 0
    for group in groups:
        for bucket in group.buckets:
            for tn in bucket.tasks:
                has_error     = any(e.severity == "error"     for e in tn.errors)
                has_warning   = any(e.severity == "warning"   for e in tn.errors)
                has_duplicate = any(e.severity == "duplicate" for e in tn.errors)
                has_notice    = any(e.severity == "notice"    for e in tn.errors)
                if has_error:
                    error_tasks += 1
                if has_warning:
                    warning_tasks += 1
                if has_duplicate:
                    duplicate_tasks += 1
                if has_notice:
                    notice_tasks += 1

    total_tasks = error_tasks + warning_tasks + duplicate_tasks + notice_tasks

    if total_tasks == 0:
        screen.notify("✓ Timeline integrity OK — no errors found.", timeout=3.0)
    else:
        screen.notify(
            f"✗ {total_tasks} issue(s) found in timeline — flagged in tree.",
            severity="warning",
            timeout=5.0,
        )


def validate_abilities_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.ability_validator import validate_ability_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_ability_tree               # noqa: PLC0415

    tree    = get_ability_tree()
    summary = validate_ability_tree(tree)

    rebuild_ability_tree_for_screen(screen)

    invalid      = summary.get("invalid", 0)
    total_errors = summary.get("total_errors", 0)

    if total_errors == 0:
        screen.notify("✓ Ability integrity OK — no issues found.", timeout=3.0)
    else:
        screen.notify(
            f"✗ {total_errors} issue(s) across {invalid} ability(s) — flagged in table.",
            severity="warning",
            timeout=5.0,
        )


def validate_hostiles_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.hostile_validator import validate_hostile_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_hostile_tree               # noqa: PLC0415
    import game.constants as const                                                    # noqa: PLC0415

    tree    = get_hostile_tree()
    summary = validate_hostile_tree(tree, const)

    rebuild_hostile_tree_for_screen(screen)

    invalid      = summary.get("invalid", 0)
    total_errors = summary.get("total_errors", 0)

    if total_errors == 0:
        screen.notify("✓ Hostile integrity OK — no issues found.", timeout=3.0)
    else:
        screen.notify(
            f"✗ {total_errors} issue(s) across {invalid} hostile(s) — flagged in tree.",
            severity="warning",
            timeout=5.0,
        )


def validate_dungeons_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.dungeon_validator import validate_dungeon_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_dungeon_tree                # noqa: PLC0415
    import game.constants as const                                                     # noqa: PLC0415

    tree    = get_dungeon_tree()
    summary = validate_dungeon_tree(tree, const)

    rebuild_dungeon_tree_for_screen(screen)

    invalid      = summary.get("invalid", 0)
    total_errors = summary.get("total_errors", 0)

    if total_errors == 0:
        screen.notify("✓ Dungeon integrity OK — no issues found.", timeout=3.0)
    else:
        screen.notify(
            f"✗ {total_errors} issue(s) across {invalid} dungeon(s) — flagged in tree.",
            severity="warning",
            timeout=5.0,
        )


def validate_city_region_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.city_region_validator import validate_region_for_screen  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_records                              # noqa: PLC0415
    import game.constants as const  # noqa: PLC0415

    summary = validate_region_for_screen(const)

    total_errors = summary.get("total_errors", 0)
    invalid      = summary.get("invalid", 0)
    scanned      = summary.get("regions_scanned", 0)
    by_code      = summary.get("by_code", {})
    nodes        = summary.get("nodes", [])

    if scanned == 0:
        screen.notify("⚠ No REGION_DATA found in constants — nothing to validate.", severity="warning", timeout=4.0)
        return

    # Store validation errors back onto the matching DevRecords so the list
    # and detail panel can render them with color.
    city_records = {r.id: r for r in get_records(_CITY_CATEGORY)}
    for node in nodes:
        record_id = f"region_{node.region_id}"
        rec = city_records.get(record_id)
        if rec is not None:
            if rec.extras is None:
                rec.extras = {}
            rec.extras["_errors"]    = node.errors
            rec.extras["_validated"] = True

    rebuild_list_for_screen(screen)

    gaps     = by_code.get("REGION_HOSTILE_COVERAGE_GAP", 0)
    sparse   = by_code.get("REGION_HOSTILE_COVERAGE_SPARSE", 0)
    no_seeds = by_code.get("REGION_HOSTILE_NO_SEEDS", 0)

    if total_errors == 0:
        screen.notify(f"✓ All {scanned} regions have full Lv 1–100 hostile coverage.", timeout=3.0)
    else:
        parts = []
        if no_seeds:
            parts.append(f"{no_seeds} zone(s) empty")
        if gaps:
            parts.append(f"{gaps} coverage gap(s)")
        if sparse:
            parts.append(f"{sparse} sparse band(s)")
        screen.notify(
            f"✗ {invalid}/{scanned} region(s) have issues — {', '.join(parts)}.",
            severity="warning",
            timeout=6.0,
        )


# ── Symbol maps ───────────────────────────────────────────────────────────────

_ELEMENT_SYMBOLS: dict[str, str] = {
    "dark":     "(D)",
    "light":    "(L)",
    "earth":    "(Ë)",
    "fire":     "(F)",
    "water":    "(W)",
    "air":      "(A)",
    "ice":      "(I)",
    "electric": "(É)",
}

# Unicode single-char glyphs for status effects — chosen for terminal readability
_STATUS_SYMBOLS: dict[str, str] = {
    "petrify":               "⬡",   # hollow hexagon → frozen/stone
    "stun":                  "✦",   # burst star → shocked/dazed
    "sleep":                 "☽",   # crescent → unconscious
    "confuse":               "⁈",   # interrobang → disoriented
    "silence":               "⊘",   # slashed circle → no voice
    "continuous_damage":     "♾",   # infinity → ongoing tick
    "elemental_debuff":      "◆",   # filled diamond → elemental weakness
    "attack_debuff":         "↓A",
    "defense_debuff":        "↓D",
    "strength_debuff":       "↓S",
    "dexterity_debuff":      "↓X",
    "intelligence_debuff":   "↓I",
    "constitution_debuff":   "↓C",
    "attack_buff":           "↑A",  # arrow + letter → attack raised
    "defense_buff":          "↑D",
    "strength_buff":         "↑S",
    "dexterity_buff":        "↑X",
    "intelligence_buff":     "↑I",
    "constitution_buff":     "↑C",
    "elemental_attack_buff": "↑EA", # elemental attack raised
    "elemental_defense_buff":"↑ED", # elemental defense raised
    "scanned":               "👁"   # eye → analysed/revealed
}


def _fmt_elem_list(elems: list[str]) -> str:
    """Format a list of element names as compact symbols."""
    if not elems:
        return "—"
    return "".join(_ELEMENT_SYMBOLS.get(e, f"({e[:1].upper()})") for e in elems)


def _fmt_status_list(statuses: list[str]) -> str:
    """Format a list of status ids as compact unicode glyphs."""
    if not statuses:
        return "—"
    return " ".join(_STATUS_SYMBOLS.get(s, f"[{s[:2]}]") for s in statuses)


_RARITY_ABBR_MAP = {
    "common": "Com", "uncommon": "Unc", "rare": "Rar", "superrare": "SR", "notfound": "Not",
}

_TYPE_ABBR_MAP = {
    "weapon":       "WPN",
    "armor · head": "A-HD",
    "armor · body": "A-BD",
    "armor · arms": "A-AR",
    "armor · legs": "A-LG",
    "accessory":    "ACC",
}

_EQUIP_COLUMNS = (
    "Name", "Type", "Lv", "Rarity", "Elem",
    "DMG", "DEF", "CRIT", "TSP", "TEP", "TAP", "TP",
    "Imm", "Res", "Wk",
)


def _balance_ratings(records: list) -> list[str]:
    """Return a 'weak' / 'strong' / '' rating for each record."""
    tp_by_group: dict = defaultdict(list)
    for r in records:
        x = r.extras
        broad = "weapon" if x.get("damage") else "armor"
        key   = (broad, x.get("level", 0))
        tp_by_group[key].append(x.get("tp", 0))

    tp_avg: dict = {
        k: sum(v) / len(v) for k, v in tp_by_group.items() if len(v) > 1
    }

    ratings: list[str] = []
    for r in records:
        x     = r.extras
        broad = "weapon" if x.get("damage") else "armor"
        key   = (broad, x.get("level", 0))
        avg   = tp_avg.get(key, 0)
        tp    = x.get("tp", 0)
        if avg and tp / avg < 0.65:
            ratings.append("weak")
        elif avg and tp / avg > 1.45:
            ratings.append("strong")
        else:
            ratings.append("")
    return ratings


def _cell(value: str, rating: str) -> Text:
    """Wrap a cell value in a Rich Text with the appropriate balance colour."""
    if rating == "weak":
        return Text(value, style=Style(color="red", dim=True))
    if rating == "strong":
        return Text(value, style=Style(color="yellow"))
    return Text(value)


def _populate_equipment_table(screen: "DataMgmtScreen", records: list) -> None:
    table = screen.query_one("#dm-equipment-table", DataTable)
    table.clear(columns=True)
    for col in _EQUIP_COLUMNS:
        table.add_column(col, key=col)

    ratings = _balance_ratings(records)

    for idx, (r, rating) in enumerate(zip(records, ratings)):
        x         = r.extras
        rarity    = x.get("rarity", "")
        rar_disp  = _RARITY_ABBR_MAP.get(rarity, rarity[:3].title() if rarity else "—")
        type_abbr = _TYPE_ABBR_MAP.get(x.get("type_label", ""), x.get("type_label", "")[:4].upper() or "—")
        dmg  = str(x["damage"])     if x.get("damage")  else "—"
        defn = str(x["defense"])    if x.get("defense") else "—"
        crit = f"{x['crit']:.1f}"  if x.get("crit")    else "—"
        tsp  = str(x.get("tsp, 0"))
        tep  = str(x.get("tep, 0"))
        tap_val = x.get("tap", 0)
        tap  = str(tap_val) if tap_val != 0 else "—"
        tp   = str(x.get("tp",  0))
        elem = x.get("elements", "") or "—"

        imm_raw = x.get("immunities") or []
        res_raw = x.get("resistances") or []
        wk_raw  = x.get("weaknesses") or []

        def _fmt_mixed(items: list[str]) -> str:
            if not items:
                return "—"
            parts = []
            for item in items:
                if item in _STATUS_SYMBOLS:
                    parts.append(_STATUS_SYMBOLS[item])
                elif item in _ELEMENT_SYMBOLS:
                    parts.append(_ELEMENT_SYMBOLS[item])
                else:
                    parts.append(f"[{item[:3]}]")
            return " ".join(parts)

        imm_disp = _fmt_mixed(imm_raw)
        res_disp = _fmt_mixed(res_raw)
        wk_disp  = _fmt_mixed(wk_raw)

        table.add_row(
            _cell(r.name,                   rating),
            _cell(type_abbr,                rating),
            _cell(str(x.get("level", 0)),   rating),
            _cell(rar_disp,                 rating),
            _cell(elem,                     rating),
            _cell(dmg,                      rating),
            _cell(defn,                     rating),
            _cell(crit,                     rating),
            _cell(tsp,                      rating),
            _cell(tep,                      rating),
            _cell(tap,                      rating),
            _cell(tp,                       rating),
            _cell(imm_disp,                 rating),
            _cell(res_disp,                 rating),
            _cell(wk_disp,                  rating),
            key=str(idx),
        )


# ── Ability table ─────────────────────────────────────────────────────────────

_ABILITY_COLUMNS = [
    "Name", "ID", "Level", "Type", "Elements", "Effect", "Statuses", "Errors",
]

_ABILITY_SORT_KEYS: dict[str, str] = {
    "ability-sort-type":     "ability_type",
    "ability-sort-lv":       "level",
    "ability-sort-effect":   "effect",
    "ability-sort-name":     "name",
    "ability-sort-severity": "severity_rank",
}

_ROW_ERROR_STYLE   = Style(color="red")
_ROW_WARN_STYLE    = Style(color="yellow")
_ROW_NOTICE_STYLE  = Style(color="#e040fb")   # magenta — matches timeline notice
_ROW_BLUE_STYLE    = Style(color="#2323ff")   # blue — matches timeline blue-notice
_ROW_INFO_STYLE    = Style(color="cyan")
_ROW_OK_STYLE      = Style(color="green", dim=True)
_ROW_DEFAULT_STYLE = Style()


_ABILITY_BLUE_NOTICE_CODES  = frozenset({"ABILITY_BALANCE_STRONG"})
_ABILITY_MGNTA_NOTICE_CODES = frozenset({"ABILITY_BALANCE_WEAK"})  # unused — info only


def _ability_row_style(errors: list) -> Style:
    """Row tint for ability grid: error=red, warning=yellow, notice=blue, info=cyan."""
    if not errors:
        return _ROW_DEFAULT_STYLE
    if any(e.severity == "error"   for e in errors):
        return _ROW_ERROR_STYLE
    if any(e.severity == "warning" for e in errors):
        return _ROW_WARN_STYLE
    if any(e.severity == "notice" and e.code in _ABILITY_BLUE_NOTICE_CODES for e in errors):
        return _ROW_BLUE_STYLE
    if any(e.severity == "notice" for e in errors):
        return _ROW_NOTICE_STYLE
    if any(e.severity == "info"   for e in errors):
        return _ROW_INFO_STYLE
    return _ROW_DEFAULT_STYLE


def _ability_error_cell(errors: list) -> Text:
    """Cell indicator for ability grid matching hostile severity colors."""
    if not errors:
        return Text("✓", style=_ROW_OK_STYLE)
    has_error      = any(e.severity == "error"   for e in errors)
    has_warning    = any(e.severity == "warning" for e in errors)
    has_blue_notice = any(e.severity == "notice" and e.code in _ABILITY_BLUE_NOTICE_CODES for e in errors)
    has_notice     = any(e.severity == "notice"  for e in errors)
    has_info       = any(e.severity == "info"    for e in errors)
    count = len(errors)
    if has_error:
        return Text(f"✗ {count}", style=_ROW_ERROR_STYLE)
    if has_warning:
        return Text(f"⚠ {count}", style=_ROW_WARN_STYLE)
    if has_blue_notice:
        return Text(f"● {count}", style=_ROW_BLUE_STYLE)
    if has_notice:
        return Text(f"● {count}", style=_ROW_NOTICE_STYLE)
    if has_info:
        return Text(f"• {count}", style=_ROW_INFO_STYLE)
    return Text(f"• {count}")


def _ability_severity_rank(node: "AbilityNode") -> int:
    if any(e.severity == "error"   for e in node.errors):
        return 0
    if any(e.severity == "warning" for e in node.errors):
        return 1
    if any(e.severity == "notice" and e.code not in _ABILITY_BLUE_NOTICE_CODES for e in node.errors):
        return 2
    if any(e.severity == "notice" and e.code in _ABILITY_BLUE_NOTICE_CODES for e in node.errors):
        return 3
    if any(e.severity == "info"   for e in node.errors):
        return 4
    if node.errors:
        return 5
    return 6


def get_ability_sort_col(screen: "DataMgmtScreen") -> str:
    try:
        sort_radio = screen.query_one("#dm-ability-sort-radio", RadioSet)
        pressed_id = sort_radio.pressed_button.id if sort_radio.pressed_button else "ability-sort-type"
        return _ABILITY_SORT_KEYS.get(pressed_id, "ability_type")
    except Exception:
        return "ability_type"


def _populate_ability_table(screen: "DataMgmtScreen", nodes: list) -> None:
    """Populate #dm-ability-table from a flat list of AbilityNode, with sort and colour."""
    sort_col = get_ability_sort_col(screen)
    sort_asc = getattr(screen, "_ability_sort_asc", True)

    def _sort_key(n: "AbilityNode"):
        sev  = _ability_severity_rank(n)
        seed = n.record.extras.get("_seed") or {}
        if sort_col == "ability_type":
            primary = n.ability_type.lower()
        elif sort_col == "level":
            primary = n.level
        elif sort_col == "effect":
            primary = str(seed.get("effect", "") or "").lower()
        elif sort_col == "name":
            primary = n.label.lower()
        elif sort_col == "severity_rank":
            primary = sev
        else:
            primary = n.ability_type.lower()
        return (primary, sev, n.level)

    valid_nodes  = [n for n in nodes if isinstance(n, AbilityNode)]
    sorted_nodes = sorted(valid_nodes, key=_sort_key, reverse=not sort_asc)

    table: DataTable = screen.query_one("#dm-ability-table", DataTable)
    table.clear(columns=True)
    for col in _ABILITY_COLUMNS:
        table.add_column(col, key=col)

    screen._ability_flat_nodes = sorted_nodes

    for idx, node in enumerate(sorted_nodes):
        row_style   = _ability_row_style(node.errors)
        seed        = node.record.extras.get("_seed") or {}
        elements    = seed.get("elements") or []
        status_keys = seed.get("status_keys") or []
        effect      = str(seed.get("effect", "") or "")
        table.add_row(
            Text(node.label,                    style=row_style),
            Text(node.ability_id,               style=row_style),
            Text(str(node.level),               style=row_style),
            Text(node.ability_type,             style=row_style),
            Text(_fmt_elem_list(elements),      style=row_style),
            Text(effect,                        style=row_style),
            Text(_fmt_status_list(status_keys), style=row_style),
            _ability_error_cell(node.errors),
            key=str(idx),
        )


# ── Hostile table ─────────────────────────────────────────────────────────────

_HOSTILE_COLUMNS = [
    "Name", "ID", "Dungeon", "Region", "Level", "Rarity", "Errors",
]

_HOSTILE_RARITY_ABBR: dict[str, str] = {
    "common":    "Com",
    "uncommon":  "Unc",
    "rare":      "Rar",
    "superrare": "SR",
    "notfound":  "?",
}

_HOSTILE_RARITY_RANK: dict[str, int] = {
    "common": 0, "uncommon": 1, "rare": 2, "superrare": 3, "notfound": 99,
}

_HOSTILE_SORT_KEYS = {
    "hostile-sort-lv":       "level",
    "hostile-sort-rarity":   "rarity_rank",
    "hostile-sort-dungeon":  "location_dungeon",
    "hostile-sort-region":   "location_region",
    "hostile-sort-name":     "name",
    "hostile-sort-severity": "severity_rank",
}


_BLUE_NOTICE_CODES  = frozenset({"HOSTILE_BALANCE_STRONG"})
_MGNTA_NOTICE_CODES = frozenset({"HOSTILE_ABILITY_MISMATCH"})


def _hostile_row_style(errors: list) -> Style:
    """Row tint: error=red, warning=yellow, notice-magenta, notice-blue, info=cyan."""
    if not errors:
        return _ROW_DEFAULT_STYLE
    if any(e.severity == "error" for e in errors):
        return _ROW_ERROR_STYLE
    if any(e.severity == "warning" for e in errors):
        return _ROW_WARN_STYLE
    if any(e.severity == "notice" and e.code in _MGNTA_NOTICE_CODES for e in errors):
        return _ROW_NOTICE_STYLE
    if any(e.severity == "notice" and e.code in _BLUE_NOTICE_CODES for e in errors):
        return _ROW_BLUE_STYLE
    if any(e.severity == "info" for e in errors):
        return _ROW_INFO_STYLE
    return _ROW_DEFAULT_STYLE


def _hostile_error_cell(errors: list) -> Text:
    """Cell indicator: ✗ red, ⚠ yellow, ● magenta, ● blue (notice), • cyan (info)."""
    if not errors:
        return Text("✓", style=_ROW_OK_STYLE)
    has_error         = any(e.severity == "error"   for e in errors)
    has_warning       = any(e.severity == "warning" for e in errors)
    has_magenta_notice = any(e.severity == "notice" and e.code in _MGNTA_NOTICE_CODES for e in errors)
    has_blue_notice   = any(e.severity == "notice" and e.code in _BLUE_NOTICE_CODES   for e in errors)
    has_info          = any(e.severity == "info"    for e in errors)
    count = len(errors)
    if has_error:
        return Text(f"✗ {count}", style=_ROW_ERROR_STYLE)
    if has_warning:
        return Text(f"⚠ {count}", style=_ROW_WARN_STYLE)
    if has_magenta_notice:
        return Text(f"● {count}", style=_ROW_NOTICE_STYLE)
    if has_blue_notice:
        return Text(f"● {count}", style=_ROW_BLUE_STYLE)
    if has_info:
        return Text(f"• {count}", style=_ROW_INFO_STYLE)
    return Text(f"• {count}")


def _hostile_severity_rank(node: "HostileNode") -> int:
    if any(e.severity == "error"   for e in node.errors):
        return 0
    if any(e.severity == "warning" for e in node.errors):
        return 1
    if any(e.severity == "notice" and e.code in _MGNTA_NOTICE_CODES for e in node.errors):
        return 2
    if any(e.severity == "notice" and e.code in _BLUE_NOTICE_CODES  for e in node.errors):
        return 3
    if any(e.severity == "info"    for e in node.errors):
        return 4
    if node.errors:
        return 5
    return 6


def get_hostile_sort_col(screen: "DataMgmtScreen") -> str:
    try:
        sort_radio = screen.query_one("#dm-hostile-sort-radio", RadioSet)
        pressed_id = sort_radio.pressed_button.id if sort_radio.pressed_button else "hostile-sort-lv"
        return _HOSTILE_SORT_KEYS.get(pressed_id, "level")
    except Exception:
        return "level"


def _populate_hostile_table(screen: "DataMgmtScreen", nodes: list) -> None:
    """Populate #dm-hostile-table from a flat list of HostileNode, with sort and colour."""
    sort_col = get_hostile_sort_col(screen)
    sort_asc = getattr(screen, "_hostile_sort_asc", True)

    def _sort_key(n: "HostileNode"):
        sev = _hostile_severity_rank(n)
        if sort_col == "level":
            primary = n.level
        elif sort_col == "rarity_rank":
            primary = _HOSTILE_RARITY_RANK.get(n.rarity, 99)
        elif sort_col == "location_dungeon":
            primary = (n.location_dungeon or "").lower()
        elif sort_col == "location_region":
            primary = (n.location_region or "").lower()
        elif sort_col == "name":
            primary = n.label.lower()
        elif sort_col == "severity_rank":
            primary = sev
        else:
            primary = n.level
        return (primary, sev, n.label.lower())

    valid_nodes = [n for n in nodes if isinstance(n, HostileNode)]
    sorted_nodes = sorted(valid_nodes, key=_sort_key, reverse=not sort_asc)

    table: DataTable = screen.query_one("#dm-hostile-table", DataTable)
    table.clear(columns=True)
    for col in _HOSTILE_COLUMNS:
        table.add_column(col, key=col)

    screen._hostile_flat_nodes = sorted_nodes

    for idx, node in enumerate(sorted_nodes):
        row_style = _hostile_row_style(node.errors)
        rar_abbr  = _HOSTILE_RARITY_ABBR.get(node.rarity, node.rarity[:3].title())
        table.add_row(
            Text(node.label,                           style=row_style),
            Text(node.hostile_id,                      style=row_style),
            Text(node.location_dungeon or "Overworld", style=row_style),
            Text(node.location_region  or "—",         style=row_style),
            Text(str(node.level),                      style=row_style),
            Text(rar_abbr,                             style=row_style),
            _hostile_error_cell(node.errors),
            key=str(idx),
        )


def rebuild_list_for_screen(screen: "DataMgmtScreen") -> None:
    """Rebuild the flat ListView (or equipment DataTable) for the active non-tree category."""
    if not screen._loaded:
        return
    category = screen._category
    query    = ""
    try:
        query = screen.query_one("#dm-filter", Input).value.strip()
    except Exception:
        pass

    if category == _EQUIPMENT_CATEGORY:
        records = filter_equipment_records(
            get_equipment_type_filter(screen),
            get_equipment_slot_filter(screen),
        )
        sort_col = get_equipment_sort_col(screen)
        if sort_col:
            sort_asc = getattr(screen, "_equipment_sort_asc", True)
            records = sorted(
                records,
                key=lambda r: r.extras.get(sort_col, 0),
                reverse=not sort_asc,
            )
        screen._last_filtered = records
        _populate_equipment_table(screen, records)
        screen.query_one("#dm-status", Static).update(f"{len(records)} record(s)")
        return

    list_view = screen.query_one("#dm-list", ListView)
    list_view.clear()
    records = search_records(category, query)
    screen._last_filtered = records
    for record in records:
        list_view.append(_RecordRow(record))
    screen.query_one("#dm-status", Static).update(f"{len(records)} record(s)")


def handle_copy_action(screen: "DataMgmtScreen") -> None:
    """Copy visible tree content to clipboard for whichever tree is active."""
    category = screen._category
    tree_id  = _active_tree_id(screen)

    try:
        tree = screen.query_one(tree_id, Tree)
    except Exception:
        tree = None

    text        = ""
    highlighted = None
    if tree is not None:
        highlighted = getattr(tree, "highlighted_node", None) or getattr(tree, "focused_node", None)

    if highlighted and highlighted is not getattr(tree, "root", None):
        text = "\n".join(serialize_node_visible(highlighted, depth=0))
    elif tree is not None:
        lines = []
        for child in get_node_children(tree.root):
            lines.extend(serialize_node_visible(child, depth=0))
        text = "\n".join(lines)
    else:
        if category == _TIMELINE_CATEGORY:
            from tui.services.dev.dataservices import get_timeline_tree  # noqa: PLC0415
            from tui.screens.dev.data_mgmt.utils import serialize_timeline_tree_visible  # noqa: PLC0415
            tree_widget = screen.query_one("#dm-timeline-tree", Tree)
            text = serialize_timeline_tree_visible(tree_widget, get_timeline_tree(), screen)
        elif category == _NPC_CATEGORY:
            text = serialize_npc_tree(screen._last_npc_filtered or get_npc_tree())
        else:
            filtered = screen._last_filtered or get_dialogue_tree()
            text = serialize_filtered_tree(filtered)

    copied = copy_to_clipboard(text)
    status = "Copied to clipboard" if copied else "Saved to temp file (fallback)"
    def handle_radio_set_changed(screen: "DataMgmtScreen", event: RadioSet.Changed) -> None:
        if event.radio_set.id in (
            "dm-equipment-type-radio",
            "dm-equipment-slot-radio",
            "dm-equipment-sort-radio",
        ):
            rebuild_list_for_screen(screen)
    screen.query_one("#dm-status", Static).update(status)
