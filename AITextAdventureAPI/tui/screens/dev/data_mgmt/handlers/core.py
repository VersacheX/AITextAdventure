"""
Core event dispatch: tab activation, input changes, button presses, tree/list
highlights, toolbar visibility, list rebuild, and copy routing.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

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
from tui.screens.dev.data_mgmt.treehandlers.dialog_handler import collect_dialogue_lines_from_node
from tui.screens.dev.data_mgmt.treehandlers.npc_handler import collect_npc_records_from_node
from tui.screens.dev.data_mgmt.treehandlers.timeline_handler import collect_timeline_tasks_from_node
from tui.screens.dev.data_mgmt.utils import (
    collapse_all_nodes,
    copy_to_clipboard,
    expand_all_nodes,
    get_node_children,
    serialize_dialog_tree_visible,
    serialize_filtered_tree,
    serialize_node_visible,
    serialize_npc_tree,
    serialize_timeline_tree_visible,
)
from tui.services.dev.dataservices import (
    CATEGORIES,
    AbilityNode,
    DialogueLine,
    DungeonNode,
    HostileNode,
    NpcRecordNode,
    TimelineTaskNode,
    get_timeline_tree,
    search_records,
)

from tui.screens.dev.data_mgmt.handlers._constants import (
    DIALOG_CATEGORY,
    EQUIPMENT_CATEGORY,
    TIMELINE_CATEGORY,
    NPC_CATEGORY,
    ABILITY_CATEGORY,
    HOSTILE_CATEGORY,
    DUNGEON_CATEGORY,
    CITY_CATEGORY,
    CHARACTER_CATEGORY,
    SIMULATION_CATEGORY,
)

# Lazy imports of per-category handlers (avoids circular imports at module level)

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen

# Keep old private aliases so any internal call in this file resolves cleanly
_DIALOG_CATEGORY     = DIALOG_CATEGORY
_EQUIPMENT_CATEGORY  = EQUIPMENT_CATEGORY
_TIMELINE_CATEGORY   = TIMELINE_CATEGORY
_NPC_CATEGORY        = NPC_CATEGORY
_ABILITY_CATEGORY    = ABILITY_CATEGORY
_HOSTILE_CATEGORY    = HOSTILE_CATEGORY
_DUNGEON_CATEGORY    = DUNGEON_CATEGORY
_CITY_CATEGORY       = CITY_CATEGORY
_CHARACTER_CATEGORY  = CHARACTER_CATEGORY
_SIMULATION_CATEGORY = SIMULATION_CATEGORY


# ── Toolbar active-tree helper ────────────────────────────────────────────────

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
    return "#dm-dialog-tree"


# ── Toolbar visibility ────────────────────────────────────────────────────────

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
    is_character  = category == _CHARACTER_CATEGORY
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
    screen.query_one("#dm-copy",     Button).display               = is_tree or is_equipment or is_hostile or is_ability or is_character or is_city
    screen.query_one("#dm-validate-timeline",     Button).display  = is_timeline
    screen.query_one("#dm-validate-abilities",    Button).display  = is_ability
    screen.query_one("#dm-validate-hostiles",     Button).display  = is_hostile
    screen.query_one("#dm-validate-dungeons",     Button).display  = is_dungeon
    screen.query_one("#dm-validate-city-region",  Button).display  = is_city
    screen.query_one("#dm-validate-equipment",    Button).display  = is_equipment
    screen.query_one("#dm-validate-characters",   Button).display  = is_character
    screen.query_one("#dm-validate-npc",          Button).display  = is_npc
    screen.query_one("#dm-equip-sort-dir",   Button).display       = is_equipment
    screen.query_one("#dm-hostile-sort-dir", Button).display       = is_hostile
    screen.query_one("#dm-ability-sort-dir", Button).display       = is_ability
    screen.query_one(NpcMusicPlayerWidget).display                 = is_npc

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
    set_filter_mode(screen, _DIALOG_CATEGORY if is_dialog else screen._category)


# ── Tab activation ────────────────────────────────────────────────────────────

def handle_tab_activated(screen: "DataMgmtScreen", event: Tabs.TabActivated) -> None:
    from tui.screens.dev.data_mgmt.handlers.dialog_handler   import rebuild_dialog_tree_for_screen    # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.timeline_handler import rebuild_timeline_tree_for_screen  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.npc_handler      import rebuild_npc_tree_for_screen       # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.ability_handler  import rebuild_ability_tree_for_screen   # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.hostile_handler  import rebuild_hostile_tree_for_screen   # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.dungeon_handler  import rebuild_dungeon_tree_for_screen   # noqa: PLC0415

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
                pass
            else:
                rebuild_list_for_screen(screen)


# ── Input / radio changes ────────────────────────────────────────────────────

def handle_input_changed(screen: "DataMgmtScreen", event: Input.Changed) -> None:
    from tui.screens.dev.data_mgmt.handlers.dialog_handler   import rebuild_dialog_tree_for_screen    # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.timeline_handler import rebuild_timeline_tree_for_screen  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.npc_handler      import rebuild_npc_tree_for_screen       # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.hostile_handler  import rebuild_hostile_tree_for_screen   # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.dungeon_handler  import rebuild_dungeon_tree_for_screen   # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.ability_handler  import rebuild_ability_tree_for_screen   # noqa: PLC0415

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
    from tui.screens.dev.data_mgmt.handlers.equipment_handler import get_equipment_type_filter  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.hostile_handler   import rebuild_hostile_tree_for_screen  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.ability_handler   import rebuild_ability_tree_for_screen  # noqa: PLC0415

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


# ── List/tree highlight ───────────────────────────────────────────────────────

def handle_list_view_highlighted(screen: "DataMgmtScreen", event: ListView.Highlighted) -> None:
    record = event.item.record if isinstance(event.item, _RecordRow) else None
    update_detail_for_record(screen, record)


def handle_tree_node_highlighted(screen: "DataMgmtScreen", event: Tree.NodeHighlighted) -> None:
    from tui.screens.dev.data_mgmt.treehandlers.ability_handler import collect_ability_nodes_from_node  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.treehandlers.hostile_handler import collect_hostile_nodes_from_node  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.treehandlers.dungeon_handler import collect_dungeon_nodes_from_node  # noqa: PLC0415

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


# ── Button press dispatcher ───────────────────────────────────────────────────

def handle_button_pressed(screen: "DataMgmtScreen", event: Button.Pressed) -> None:
    from tui.screens.dev.data_mgmt.handlers.timeline_handler    import validate_timeline_for_screen    # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.ability_handler     import validate_abilities_for_screen, rebuild_ability_tree_for_screen   # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.hostile_handler     import validate_hostiles_for_screen, rebuild_hostile_tree_for_screen    # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.dungeon_handler     import validate_dungeons_for_screen    # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.city_region_handler import validate_city_region_for_screen # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.equipment_handler   import validate_equipment_for_screen   # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.character_handler   import validate_characters_for_screen  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.npc_handler         import validate_npc_for_screen         # noqa: PLC0415

    bid = event.button.id or ""
    if bid == "dm-expand":
        expand_all_nodes(screen.query_one(_active_tree_id(screen), Tree))
    elif bid == "dm-collapse":
        collapse_all_nodes(screen.query_one(_active_tree_id(screen), Tree))
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
    elif bid == "dm-validate-equipment":
        validate_equipment_for_screen(screen)
    elif bid == "dm-validate-characters":
        validate_characters_for_screen(screen)
    elif bid == "dm-validate-npc":
        validate_npc_for_screen(screen)
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


# ── Copy router ───────────────────────────────────────────────────────────────

def _handle_copy(screen: "DataMgmtScreen") -> None:
    from tui.screens.dev.data_mgmt.utils import serialize_dialog_tree_from_widget  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.equipment_handler  import copy_equipment   # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.hostile_handler    import copy_hostiles    # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.ability_handler    import copy_abilities   # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.character_handler  import copy_characters  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.city_region_handler import copy_city       # noqa: PLC0415

    category = screen._category

    if category == _DIALOG_CATEGORY:
        text = serialize_dialog_tree_from_widget(screen.query_one("#dm-dialog-tree", Tree))

    elif category == _TIMELINE_CATEGORY:
        text = serialize_timeline_tree_visible(
            screen.query_one("#dm-timeline-tree", Tree),
            get_timeline_tree(),
            screen,
        )

    elif category == _NPC_CATEGORY:
        if screen._last_npc_filtered is not None:
            text = serialize_npc_tree(screen._last_npc_filtered)
        else:
            tree = screen.query_one("#dm-npc-tree", Tree)
            text = "\n".join(serialize_node_visible(tree.root, depth=0))

    elif category == _ABILITY_CATEGORY:
        text = copy_abilities(screen)

    elif category == _HOSTILE_CATEGORY:
        text = copy_hostiles(screen)

    elif category == _EQUIPMENT_CATEGORY:
        text = copy_equipment(screen)

    elif category == _CHARACTER_CATEGORY:
        text = copy_characters(screen)

    elif category == _CITY_CATEGORY:
        text = copy_city(screen)

    else:
        text = serialize_filtered_tree(screen._last_filtered) if screen._last_filtered is not None else ""

    if text:
        copy_to_clipboard(text)
        screen.notify("Copied to clipboard", timeout=2.0)


# ── Generic list rebuild (non-equipment categories) ──────────────────────────

def rebuild_list_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.screens.dev.data_mgmt.handlers.equipment_handler import rebuild_list_for_screen as _equip_rebuild  # noqa: PLC0415

    if not screen._loaded:
        return
    if screen._category == EQUIPMENT_CATEGORY:
        _equip_rebuild(screen)
        return

    query = ""
    try:
        query = screen.query_one("#dm-filter", Input).value.strip()
    except Exception:
        pass

    list_view = screen.query_one("#dm-list", ListView)
    list_view.clear()
    records = search_records(screen._category, query)
    screen._last_filtered = records
    for record in records:
        list_view.append(_RecordRow(record))
    screen.query_one("#dm-status", Static).update(f"{len(records)} record(s)")