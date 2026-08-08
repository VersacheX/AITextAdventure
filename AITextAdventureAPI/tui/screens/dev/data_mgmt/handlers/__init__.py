"""
Public re-export shim so existing call-sites require no changes.

All behaviour lives in the sub-modules; this file only re-exports the
symbols that data_mgmt_screen.py (and any other caller) imports directly
from `handlers`.
"""
from __future__ import annotations

from tui.screens.dev.data_mgmt.handlers.core import (
    handle_button_pressed,
    handle_input_changed,
    handle_list_view_highlighted,
    handle_radio_set_changed,
    handle_tab_activated,
    handle_tree_node_highlighted,
    rebuild_list_for_screen,
    set_filter_mode,
)
from tui.screens.dev.data_mgmt.handlers.dialog_handler import (
    rebuild_dialog_tree_for_screen,
)
from tui.screens.dev.data_mgmt.handlers.timeline_handler import (
    rebuild_timeline_tree_for_screen,
    validate_timeline_for_screen,
)
from tui.screens.dev.data_mgmt.handlers.npc_handler import (
    rebuild_npc_tree_for_screen,
    validate_npc_for_screen,
)
from tui.screens.dev.data_mgmt.handlers.ability_handler import (
    rebuild_ability_tree_for_screen,
    validate_abilities_for_screen,
)
from tui.screens.dev.data_mgmt.handlers.hostile_handler import (
    rebuild_hostile_tree_for_screen,
    validate_hostiles_for_screen,
)
from tui.screens.dev.data_mgmt.handlers.dungeon_handler import (
    rebuild_dungeon_tree_for_screen,
    validate_dungeons_for_screen,
)
from tui.screens.dev.data_mgmt.handlers.city_region_handler import (
    validate_city_region_for_screen,
)
from tui.screens.dev.data_mgmt.handlers.equipment_handler import (
    get_equipment_slot_filter,
    get_equipment_sort_col,
    get_equipment_type_filter,
    rebuild_list_for_screen as _rebuild_equip,   # internal alias — not exported
    validate_equipment_for_screen,
)
from tui.screens.dev.data_mgmt.handlers.character_handler import (
    validate_characters_for_screen,
)

__all__ = [
    # core
    "handle_button_pressed",
    "handle_input_changed",
    "handle_list_view_highlighted",
    "handle_radio_set_changed",
    "handle_tab_activated",
    "handle_tree_node_highlighted",
    "rebuild_list_for_screen",
    "set_filter_mode",
    # per-category
    "rebuild_dialog_tree_for_screen",
    "rebuild_timeline_tree_for_screen",
    "rebuild_npc_tree_for_screen",
    "rebuild_ability_tree_for_screen",
    "rebuild_hostile_tree_for_screen",
    "rebuild_dungeon_tree_for_screen",
    # validators
    "validate_timeline_for_screen",
    "validate_abilities_for_screen",
    "validate_hostiles_for_screen",
    "validate_dungeons_for_screen",
    "validate_city_region_for_screen",
    "validate_equipment_for_screen",
    "validate_characters_for_screen",
    "validate_npc_for_screen",
    # equipment helpers
    "get_equipment_type_filter",
    "get_equipment_slot_filter",
    "get_equipment_sort_col",
]